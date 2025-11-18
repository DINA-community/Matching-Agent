import pytest
import datetime
import asyncio
from contextlib import suppress

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import ForeignKey, String, JSON, DateTime, text
from sqlalchemy.exc import IntegrityError

from unittest.mock import Mock, patch, AsyncMock

from dina.cachedb.fetcher_view import FetcherView
from dina.cachedb.model import relationship


# Ensure Windows event loop compatibility
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Postgres test container (optional)
with suppress(ImportError):
    from testcontainers.postgres import PostgresContainer


Base = declarative_base()


# ====================================================================================================
# MODELS
# ====================================================================================================


class SynchronizerMetadata(Base):
    """Minimal metadata table for testing FetcherView behavior."""

    __tablename__ = "synchronizer_metadata"
    __table_args__ = {"schema": "cacheDB"}

    origin_uri: Mapped[str] = mapped_column(String, primary_key=True)
    plugin_metadata: Mapped[dict] = mapped_column(JSON, default={})
    last_run: Mapped[datetime.datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )


class DummyAsset(Base):
    """Simple asset model used for get_existing() tests."""

    __tablename__ = "asset"

    id: Mapped[int] = mapped_column(primary_key=True)
    origin_uri: Mapped[str] = mapped_column(String)
    name: Mapped[str] = mapped_column(String)

    # Dummy relationships to satisfy FetcherView joinedload/noload logic
    product = relationship("DummyAsset", uselist=False, viewonly=True)
    matches = relationship("DummyAsset", uselist=True, viewonly=True)
    children = relationship("DummyAsset", uselist=True, viewonly=True)
    parents = relationship("DummyAsset", uselist=True, viewonly=True)

    parent_id: Mapped[int | None] = mapped_column(ForeignKey("asset.id"))


# ====================================================================================================
# FIXTURES
# ====================================================================================================


@pytest.fixture(scope="session")
def pg_url():
    """
    Start PostgreSQL using testcontainers if available.
    Falls back to SQLite if Docker or Postgres is unavailable.
    """
    try:
        with PostgresContainer("postgres:15") as pg:
            sync_url = pg.get_connection_url()

            # Convert sync URL to async psycopg URL
            async_url = sync_url.replace(
                "postgresql+psycopg2://", "postgresql+psycopg_async://"
            ).replace("postgresql://", "postgresql+psycopg_async://")
            yield async_url
            return

    except Exception as e:
        print(f"[INFO] Falling back to SQLite: {e}")
        yield "sqlite+aiosqlite:///:memory:"


@pytest.fixture(scope="function")
async def async_engine(pg_url):
    """
    Create a fresh async engine for each test.
    Ensures the cacheDB schema and tables exist.
    """
    engine = create_async_engine(pg_url, echo=False, future=True)

    async with engine.begin() as conn:
        await conn.execute(text('CREATE SCHEMA IF NOT EXISTS "cacheDB"'))
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    yield engine
    await engine.dispose()


# ====================================================================================================
# TESTS
# ====================================================================================================


@pytest.mark.asyncio
async def test_get_existing_returns_correct_records(async_engine):
    """Ensure get_existing() returns only matching origin_uri records."""

    async with AsyncSession(async_engine) as session:
        session.add_all(
            [
                DummyAsset(id=1, origin_uri="https://fake.netbox", name="DeviceA"),
                DummyAsset(id=2, origin_uri="https://other.origin", name="DeviceB"),
            ]
        )
        await session.commit()

    fetcher = FetcherView("https://fake.netbox", async_engine)
    result = await fetcher.get_existing(DummyAsset, DummyAsset.id == 1)

    assert len(result) == 1
    assert result[0].name == "DeviceA"


@pytest.mark.asyncio
async def test_metadata_roundtrip(async_engine):
    """Ensure plugin metadata is persisted and retrieved correctly."""
    fetcher = FetcherView("https://fake.netbox", async_engine)

    data = {"version": 1, "status": "ok"}
    await fetcher.set_plugin_metadata(data)

    assert await fetcher.plugin_metadata() == data


@pytest.mark.asyncio
async def test_last_run_roundtrip(async_engine):
    """Ensure last_run is stored and returned with correct timestamp."""
    fetcher = FetcherView("https://fake.netbox", async_engine)

    now = datetime.datetime.now(datetime.timezone.utc)
    await fetcher.set_last_run(now)

    last_run = await fetcher.last_run()
    assert isinstance(last_run, datetime.datetime)
    assert abs((last_run - now).total_seconds()) < 1


@pytest.mark.asyncio
async def test_get_meta_creates_new_record(async_engine):
    """Ensure __get_meta() creates a metadata record when none exists."""
    fetcher = FetcherView("https://fake.netbox", async_engine)
    await fetcher.set_plugin_metadata({"test": True})

    async with AsyncSession(async_engine) as session:
        count = (
            await session.execute(
                text('SELECT COUNT(*) FROM "cacheDB".synchronizer_metadata')
            )
        ).scalar_one()

        assert count == 1


@pytest.mark.asyncio
async def test_get_meta_integrityerror_branch(async_engine):
    """
    Ensure __get_meta() correctly handles IntegrityError during commit()
    and retries loading the metadata entry.
    """

    fetcher = FetcherView("https://fake.origin", async_engine)

    fake_error = IntegrityError(
        statement="INSERT ...",
        params={},
        orig=Exception("duplicate key violates constraint"),
    )

    async with AsyncSession(async_engine) as session:
        first_exec = Mock()
        first_exec.scalar_one_or_none = Mock(return_value=None)

        second_exec = Mock()
        second_exec.scalar_one = Mock(return_value="fake_meta")

        async def fake_execute(*args, **kwargs):
            if not hasattr(fake_execute, "called"):
                fake_execute.called = True
                return first_exec
            return second_exec

        with (
            patch.object(
                session, "execute", AsyncMock(side_effect=fake_execute)
            ) as mock_execute,
            patch.object(
                session, "commit", AsyncMock(side_effect=fake_error)
            ) as mock_commit,
            patch.object(session, "rollback", AsyncMock()) as mock_rollback,
        ):
            result = await fetcher._FetcherView__get_meta(session)

        assert result == "fake_meta"
        assert mock_execute.await_count == 2
        mock_commit.assert_awaited_once()
        mock_rollback.assert_awaited_once()
