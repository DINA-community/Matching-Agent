"""
Database module for DINA cache operations.

This module provides the CacheDB class, which serves as the primary interface
for interacting with the PostgreSQL database. It handles storage and retrieval
of assets, CSAF products, matches, and their relationships, as well as managing
matcher runs, triggers, and user authentication.

The database uses SQLAlchemy for async PostgreSQL operations and stores data
in a 'cacheDB' schema.
"""

import datetime
from typing import Any, AsyncGenerator, List, Optional, Type, Union

import sqlalchemy.exc
from pydantic import BaseModel, Field, HttpUrl
from sqlalchemy import (
    and_,
    delete,
    func,
    literal,
    or_,
    select,
    tuple_,
    update,
)
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import contains_eager, joinedload
from sqlalchemy.sql.ddl import CreateSchema

from dina.cachedb.fetcher_view import FetcherView
from dina.cachedb.model import (
    Asset,
    Base,
    CsafProduct,
    Match,
    MatcherRun,
    MatcherTrigger,
    Product,
    SynchronizerMetadata,
    User,
    csaf_product_relationship,
    product_relationship,
)
from dina.common.log import get_logger
from dina.synchronizer.plugin_base.data_source import (
    DataSourcePlugin,
    MappedRelationship,
)

logger = get_logger(__name__)


class CacheDB:
    """
    Main database interface for DINA cache operations.

    Provides async methods for storing and querying assets, CSAF products, matches,
    and their relationships. Manages matcher runs, triggers, and user authentication.
    Must be connected via connect() before use.
    """

    class Config(BaseModel):
        """Configuration for PostgreSQL database connection."""

        host: str = Field(..., description="PostgreSQL host name or IP.")
        port: int = Field(..., description="PostgreSQL TCP port.")
        database: str = Field(..., description="PostgreSQL database name.")
        username: str = Field(..., description="PostgreSQL user name.")
        password: str = Field(..., description="PostgreSQL user password.")

    def __init__(self, config: Config) -> None:
        """
        Initialize the database interface.

        Args:
            config: Database connection configuration.
        """
        super().__init__()
        self.engine: Optional[AsyncEngine] = None
        self.config = config

    async def connect(self) -> None:
        """
        Establish database connection and initialize schema.

        Creates the database engine, cacheDB schema if needed, and all tables.
        Must be called before any other database operations.
        """
        self.engine = create_async_engine(
            f"postgresql+psycopg://{self.config.username}:{self.config.password}@{self.config.host}:{self.config.port}/{self.config.database}",
        )
        async with self.engine.begin() as conn:
            await conn.execute(CreateSchema("cacheDB", if_not_exists=True))
            await conn.run_sync(Base.metadata.create_all)

    def fetcher_view(self, origin: HttpUrl) -> FetcherView:
        """
        Create a view for querying synchronizer metadata by origin.

        Args:
            origin: The origin URI to create a view for.

        Returns:
            FetcherView instance for the specified origin.

        Raises:
            Exception: If database is not connected.
        """
        if self.engine is not None:
            return FetcherView(origin, self.engine)
        else:
            raise Exception("Database not connected")

    async def store(
        self,
        data: List[Union[Asset, CsafProduct]],
        relationships: List[MappedRelationship],
    ) -> None:
        """
        Store or update assets, CSAF products, and their relationships.

        Performs upserts for existing data (matched by ID) and inserts for new data.
        All operations occur in a single transaction.

        Args:
            data: Assets or CSAF products to store.
            relationships: Parent-child relationships between products to store.
        """
        if not data and not relationships:
            return

        # Split data into assets and csaf_docs
        logger.debug("Sorting items into new and to_update")
        new_data = [o for o in data if o.id is None]
        assets_to_update = [
            o for o in data if isinstance(o, Asset) and o.id is not None
        ]
        csaf_products_to_update = [
            o for o in data if isinstance(o, CsafProduct) and o.id is not None
        ]
        product_relations_to_update = [o for o in relationships if o.ty == Asset]
        csaf_product_relations_to_update = [
            o for o in relationships if o.ty == CsafProduct
        ]
        logger.debug("Done sorting")

        async with AsyncSession(self.engine) as session:
            async with session.begin():
                if new_data:
                    session.add_all(new_data)
                if assets_to_update:
                    await self.__update(session, Asset, assets_to_update)

                if csaf_products_to_update:
                    await self.__update(session, CsafProduct, csaf_products_to_update)

                await self.__upsert_relations(
                    session, Asset, product_relations_to_update
                )
                await self.__upsert_relations(
                    session, CsafProduct, csaf_product_relations_to_update
                )
        logger.info("Done storing")

    async def __upsert_relations(
        self,
        session: AsyncSession,
        ty: Type[Asset | CsafProduct],
        data: List[MappedRelationship],
    ):
        chunk_size = 200
        chunks = [data[i : i + chunk_size] for i in range(0, len(data), chunk_size)]

        for chunk in chunks:
            await self.__upsert_relations_chunk(session, ty, chunk)

    async def __upsert_relations_chunk(
        self,
        session: AsyncSession,
        ty: Type[Asset | CsafProduct],
        data: List[MappedRelationship],
    ):
        current_time = datetime.datetime.now().timestamp()
        relation_ty = product_relationship if ty == Asset else csaf_product_relationship

        if not data:
            return

        stmt = insert(relation_ty).values(
            [
                {
                    "parent_id": d.parent,
                    "child_id": d.child,
                    "origin_uri": str(d.origin_uri),
                    "origin_info": d.origin_info,
                    "last_update": current_time,
                }
                for d in data
            ]
        )
        stmt = stmt.on_conflict_do_update(
            index_elements=["parent_id", "child_id"], set_=dict(stmt.excluded)
        )
        await session.execute(stmt)

    async def __update(
        self,
        session: AsyncSession,
        ty: Type[Asset | CsafProduct],
        data: List[Asset] | List[CsafProduct],
    ):
        chunk_size = 200
        chunks = [data[i : i + chunk_size] for i in range(0, len(data), chunk_size)]

        for chunk in chunks:
            await self.__update_chunk(session, ty, chunk)

    async def __update_chunk(
        self,
        session: AsyncSession,
        ty: Type[Asset | CsafProduct],
        data: List[Asset] | List[CsafProduct],
    ):
        if not data:
            return

        stmt = insert(ty).values([d.to_dict() for d in data])
        stmt = stmt.on_conflict_do_update(
            index_elements=["id"], set_=dict(stmt.excluded)
        )
        await session.execute(stmt)

        stmt = insert(Product).values([d.product.to_dict() for d in data])
        stmt = stmt.on_conflict_do_update(
            index_elements=["id"], set_=dict(stmt.excluded)
        )
        await session.execute(stmt)

    async def run_cleanup_for_plugin(
        self, source: DataSourcePlugin, grace_period_seconds: int
    ) -> None:
        """
        Clean up stale data for a specific data source plugin.

        Identifies assets, CSAF products, and relationships that haven't been updated
        since before the grace period. Delegates to the plugin to determine which items
        can be deleted vs. refreshed.

        Args:
            source: The data source plugin to clean up for.
            grace_period_seconds: Time in seconds before last run to consider data stale.
        """
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                fetcher_view = self.fetcher_view(source.origin_uri)
                last_run = await fetcher_view.last_run()

                if last_run.tzinfo is None:
                    last_run = last_run.replace(tzinfo=datetime.timezone.utc)

                last_run = last_run.astimezone(tz=datetime.timezone.utc)

                data: List[Asset | CsafProduct] = []
                stale_timestamp = last_run.timestamp() - grace_period_seconds
                # We want to check if anything that was fetched X seconds before the last run is still valid
                stmt = (
                    select(Asset)
                    .where(
                        Asset.last_update < stale_timestamp,
                        Asset.origin_uri == str(source.origin_uri),
                    )
                    .options(joinedload(Asset.product))
                )
                data.extend((await session.execute(stmt)).scalars().all())

                csaf_stmt = (
                    select(CsafProduct)
                    .where(
                        CsafProduct.last_update < stale_timestamp,
                        CsafProduct.origin_uri == str(source.origin_uri),
                    )
                    .options(joinedload(CsafProduct.product))
                )
                data.extend((await session.execute(csaf_stmt)).scalars().all())

                await self.__clean_relations(session, source, stale_timestamp, last_run)

                if not data:
                    return None
                cleanup_results = await source.cleanup_products(data)
                assets_to_delete = [
                    result.id
                    for result in cleanup_results
                    if result.ty == Asset and result.can_delete
                ]
                assets_to_refresh = [
                    result.id
                    for result in cleanup_results
                    if result.ty == Asset and not result.can_delete
                ]

                csaf_to_delete = [
                    result.id
                    for result in cleanup_results
                    if result.ty == CsafProduct and result.can_delete
                ]
                csaf_to_refresh = [
                    result.id
                    for result in cleanup_results
                    if result.ty == CsafProduct and not result.can_delete
                ]

                if assets_to_delete:
                    del_stmt = delete(Asset).where(Asset.id.in_(assets_to_delete))
                    await session.execute(del_stmt)
                if csaf_to_delete:
                    del_stmt = delete(CsafProduct).where(
                        CsafProduct.id.in_(csaf_to_delete)
                    )
                    await session.execute(del_stmt)

                if assets_to_refresh:
                    update_stmt = (
                        update(Asset)
                        .where(Asset.id.in_(assets_to_refresh))
                        .values(last_update=last_run.timestamp())
                    )
                    await session.execute(update_stmt)
                if csaf_to_refresh:
                    update_stmt = (
                        update(CsafProduct)
                        .where(CsafProduct.id.in_(csaf_to_refresh))
                        .values(last_update=last_run.timestamp())
                    )
                    await session.execute(update_stmt)

    async def __clean_relations(
        self,
        session: AsyncSession,
        source: DataSourcePlugin,
        stale_timestamp: float,
        last_run: datetime.datetime,
    ):
        relations_to_clean: list[MappedRelationship] = []
        relation_stmt = (
            select(*product_relationship.c)
            .where(product_relationship.c.last_update < stale_timestamp)
            .filter(product_relationship.c.origin_uri == str(source.origin_uri))
        )
        relations_to_clean.extend(
            [
                MappedRelationship(
                    parent=r.parent_id,
                    child=r.child_id,
                    ty=Asset,
                    origin_info=r.origin_info,
                    origin_uri=r.origin_uri,
                )
                for r in (await session.execute(relation_stmt)).all()
            ]
        )

        csaf_relation_stmt = (
            select(*csaf_product_relationship.c)
            .where(csaf_product_relationship.c.last_update < stale_timestamp)
            .filter(csaf_product_relationship.c.origin_uri == str(source.origin_uri))
        )
        relations_to_clean.extend(
            [
                MappedRelationship(
                    parent=r.parent_id,
                    child=r.child_id,
                    ty=Asset,
                    origin_info=r.origin_info,
                    origin_uri=r.origin_uri,
                )
                for r in (await session.execute(csaf_relation_stmt)).all()
            ]
        )

        relation_cleanup_results = await source.cleanup_relationships(
            relations_to_clean
        )

        relations_to_delete = [
            result
            for result in relation_cleanup_results
            if result.ty == Asset and result.can_delete
        ]

        relations_to_refresh = [
            result
            for result in relation_cleanup_results
            if result.ty == Asset and not result.can_delete
        ]

        csaf_relations_to_delete = [
            result
            for result in relation_cleanup_results
            if result.ty == CsafProduct and result.can_delete
        ]

        csaf_relations_to_refresh = [
            result
            for result in relation_cleanup_results
            if result.ty == CsafProduct and not result.can_delete
        ]

        if relations_to_delete:
            del_stmt = delete(product_relationship).where(
                or_(
                    and_(
                        product_relationship.c.parent_id == relation.parent,
                        product_relationship.c.child_id == relation.child,
                    )
                    for relation in relations_to_delete
                )
            )
            await session.execute(del_stmt)

        if csaf_relations_to_delete:
            del_stmt = delete(csaf_product_relationship).where(
                or_(
                    and_(
                        csaf_product_relationship.c.parent_id == relation.parent,
                        csaf_product_relationship.c.child_id == relation.child,
                    )
                    for relation in relations_to_delete
                )
            )
            await session.execute(del_stmt)

        if relations_to_refresh:
            update_stmt = (
                update(product_relationship)
                .where(
                    or_(
                        and_(
                            product_relationship.c.parent_id == relation.parent,
                            product_relationship.c.child_id == relation.child,
                        )
                        for relation in relations_to_refresh
                    )
                )
                .values(last_update=last_run.timestamp())
            )
            await session.execute(update_stmt)

        if csaf_relations_to_refresh:
            update_stmt = (
                update(csaf_product_relationship)
                .where(
                    or_(
                        and_(
                            csaf_product_relationship.c.parent_id == relation.parent,
                            csaf_product_relationship.c.child_id == relation.child,
                        )
                        for relation in csaf_relations_to_refresh
                    )
                )
                .values(last_update=last_run.timestamp())
            )
            await session.execute(update_stmt)

    async def _fetch_batch_ids(
        self,
        session: AsyncSession,
        model: type[CsafProduct] | type[Asset],
        uris: list[HttpUrl],
        last_id: int,
        limit: int,
    ) -> list[int]:
        stmt = (
            select(model.id).where(model.id >= last_id).order_by(model.id).limit(limit)
        )
        if uris:
            stmt = stmt.where(model.uri.in_([str(u) for u in uris]))
        return (await session.execute(stmt)).scalars().all()  # type: ignore

    async def fetch_pairs_batches(
        self,
        assets: list[HttpUrl],
        csaf_documents: list[HttpUrl],
        matching_config_hash: str,
        force_recompute: bool = False,
        batch_size_sqrt: int = 50,
    ) -> AsyncGenerator[list[tuple[CsafProduct, Asset]]]:
        """
        Generate batches of (CSAF product, asset) pairs for matching.

        Yields batches of pairs that need to be matched. If force_recompute is False,
        only yields pairs that are unmatched, have stale matches, or were matched
        with a different configuration.

        Args:
            assets: Optional filter for specific asset URIs.
            csaf_documents: Optional filter for specific CSAF document URIs.
            matching_config_hash: Hash of current matching configuration.
            force_recompute: If True, yield all pairs regardless of match status.
            batch_size_sqrt: Square root of batch size (actual batch is this squared).

        Yields:
            Lists of (CsafProduct, Asset) tuples ready for matching.
        """
        async with AsyncSession(self.engine) as session:
            next_csaf_product_id = 0

            while True:
                logger.trace(f"Fetching csaf product offset: {next_csaf_product_id}")
                csaf_ids = await self._fetch_batch_ids(
                    session,
                    CsafProduct,
                    csaf_documents,
                    next_csaf_product_id,
                    batch_size_sqrt,
                )
                if not csaf_ids:
                    break
                next_csaf_product_id = csaf_ids[-1] + 1

                next_asset_id = 0
                while True:
                    logger.trace(f"Fetching asset offset: {next_asset_id}")

                    asset_ids = await self._fetch_batch_ids(
                        session, Asset, assets, next_asset_id, batch_size_sqrt
                    )
                    if not asset_ids:
                        break

                    next_asset_id = asset_ids[-1] + 1

                    query = (
                        select(CsafProduct, Asset)
                        .select_from(CsafProduct)
                        .join(Asset, literal(True))
                        .where(CsafProduct.id.in_(csaf_ids))
                        .where(Asset.id.in_(asset_ids))
                        .options(
                            joinedload(CsafProduct.product), joinedload(Asset.product)
                        )
                    )
                    if not force_recompute:
                        # Recompute when pair has no match, has stale match, or was
                        # matched with a different configuration hash.
                        query = query.outerjoin(
                            Match,
                            and_(
                                Match.asset_id == Asset.id,
                                Match.csaf_product_id == CsafProduct.id,
                            ),
                        ).where(
                            or_(
                                Match.id.is_(None),
                                Match.timestamp < Asset.last_update,
                                Match.timestamp < CsafProduct.last_update,
                                Match.matching_config_hash.is_(None),
                                Match.matching_config_hash != matching_config_hash,
                            )
                        )

                    if result := (await session.execute(query)).tuples().all():
                        yield result  # type: ignore

            return

    async def count_assets(self, assets: list[HttpUrl]) -> int:
        """
        Count total assets, optionally filtered by URIs.

        Args:
            assets: Optional list of asset URIs to count. If empty, counts all.

        Returns:
            Number of assets matching the filter.
        """
        async with AsyncSession(self.engine) as session:
            stmt = select(func.count()).select_from(Asset)
            if assets:
                stmt = stmt.where(Asset.uri.in_([str(a) for a in assets]))
            return int((await session.execute(stmt)).scalar_one())

    async def count_csaf_products(self, csaf_documents: list[HttpUrl]) -> int:
        """
        Count total CSAF products, optionally filtered by URIs.

        Args:
            csaf_documents: Optional list of CSAF document URIs to count. If empty, counts all.

        Returns:
            Number of CSAF products matching the filter.
        """
        async with AsyncSession(self.engine) as session:
            stmt = select(func.count()).select_from(CsafProduct)
            if csaf_documents:
                stmt = stmt.where(CsafProduct.uri.in_([str(p) for p in csaf_documents]))
            return int((await session.execute(stmt)).scalar_one())

    async def count_pairs_to_match(
        self,
        assets: list[HttpUrl],
        csaf_documents: list[HttpUrl],
        matching_config_hash: str,
        force_recompute: bool = False,
    ) -> int:
        """
        Count how many (CSAF product, asset) pairs need to be matched.

        Unless force_recompute is True, only counts pairs that are unmatched,
        have stale matches, or were matched with a different configuration.

        Args:
            assets: Optional filter for specific asset URIs.
            csaf_documents: Optional filter for specific CSAF document URIs.
            matching_config_hash: Hash of current matching configuration.
            force_recompute: If True, count all pairs regardless of match status.

        Returns:
            Number of pairs that need matching.
        """
        async with AsyncSession(self.engine) as session:
            stmt = (
                select(func.count()).select_from(CsafProduct).join(Asset, literal(True))
            )
            if not force_recompute:
                stmt = stmt.outerjoin(
                    Match,
                    and_(
                        Match.asset_id == Asset.id,
                        Match.csaf_product_id == CsafProduct.id,
                    ),
                ).where(
                    or_(
                        Match.id.is_(None),
                        Match.timestamp < Asset.last_update,
                        Match.timestamp < CsafProduct.last_update,
                        Match.matching_config_hash.is_(None),
                        Match.matching_config_hash != matching_config_hash,
                    )
                )
            if assets:
                stmt = stmt.where(Asset.uri.in_([str(a) for a in assets]))
            if csaf_documents:
                stmt = stmt.where(CsafProduct.uri.in_([str(p) for p in csaf_documents]))
            return int((await session.execute(stmt)).scalar_one())

    async def store_matches(self, matches: list[Match]) -> list[int]:
        """
        Store new match records.

        Args:
            matches: List of Match objects to insert.

        Returns:
            List of IDs for the newly created matches.
        """
        if not matches:
            return []
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                stmt = (
                    insert(Match)
                    .returning(Match.id)
                    .values([match.to_dict() for match in matches])
                )
                return (await session.execute(stmt)).scalars().all()

    async def store_matches_for_run(
        self,
        processed_pairs: list[tuple[int, int]],
        matches: list[Match],
    ) -> list[int]:
        """
        Store matches for a specific matcher run, replacing old matches for processed pairs.

        Deletes existing matches for the specified pairs before inserting new ones,
        ensuring each pair has only the most recent match results.

        Args:
            processed_pairs: List of (csaf_product_id, asset_id) tuples to replace matches for.
            matches: New match records to insert.

        Returns:
            List of IDs for the newly created matches.
        """
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                if processed_pairs:
                    delete_stmt = delete(Match).where(
                        tuple_(Match.csaf_product_id, Match.asset_id).in_(
                            processed_pairs
                        )
                    )
                    await session.execute(delete_stmt)

                if not matches:
                    return []

                stmt = (
                    insert(Match)
                    .returning(Match.id)
                    .values([match.to_dict() for match in matches])
                )
                return (await session.execute(stmt)).scalars().all()

    async def add_matcher_trigger(self, origin_uri: HttpUrl | None = None) -> None:
        """
        Add a trigger to signal the matcher to run.

        Used by synchronizers to notify the matcher that new data is available.

        Args:
            origin_uri: Optional specific origin to match. If None, matcher runs for all origins.

        Raises:
            Exception: If database is not connected.
        """
        if self.engine is None:
            raise Exception("Database not connected")
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                session.add(
                    MatcherTrigger(origin_uri=str(origin_uri) if origin_uri else None)
                )

    async def consume_matcher_triggers(self, last_id: int = 0) -> list[MatcherTrigger]:
        """
        Retrieve and delete all matcher triggers since the given ID.

        This is used by the matcher to check if it should run and to clear
        processed triggers.

        Args:
            last_id: Only return triggers with ID greater than this.

        Returns:
            List of triggers that were pending.

        Raises:
            Exception: If database is not connected.
        """
        if self.engine is None:
            raise Exception("Database not connected")
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                stmt = (
                    select(MatcherTrigger)
                    .where(MatcherTrigger.id > last_id)
                    .order_by(MatcherTrigger.id)
                )
                triggers = (await session.execute(stmt)).scalars().all()
                if triggers:
                    await session.execute(
                        delete(MatcherTrigger).where(
                            MatcherTrigger.id <= triggers[-1].id
                        )
                    )
                return triggers

    async def create_matcher_run(
        self,
        trigger: str,
        assets: list[HttpUrl],
        csaf_documents: list[HttpUrl],
        matching_config_hash: str,
        matching_config: dict[str, Any],
        *,
        force_recompute: bool = False,
        state: str = "pending",
        started_at: float | None = None,
        total_pairs: int = 0,
    ) -> MatcherRun:
        """
        Create a new matcher run record.

        Args:
            trigger: Description of what triggered this run (e.g., "manual", "scheduled").
            assets: Asset URIs to include in this run.
            csaf_documents: CSAF document URIs to include in this run.
            matching_config_hash: Hash of the matching configuration.
            matching_config: The matching configuration dictionary.
            force_recompute: Whether to recompute all pairs regardless of staleness.
            state: Initial state (typically "pending").
            started_at: Optional start timestamp (defaults to now).
            total_pairs: Total number of pairs to process.

        Returns:
            The created MatcherRun object.
        """
        if started_at is None:
            started_at = datetime.datetime.now().timestamp()
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                run = MatcherRun(
                    trigger=trigger,
                    state=state,
                    started_at=started_at,
                    total_pairs=total_pairs,
                    assets=[str(a) for a in assets],
                    csaf_documents=[str(c) for c in csaf_documents],
                    matching_config_hash=matching_config_hash,
                    matching_config=matching_config,
                    force_recompute=force_recompute,
                )
                session.add(run)
                await session.flush()
                session.expunge(run)
                return run

    async def start_matcher_run(
        self,
        run_id: int,
        *,
        started_at: float | None = None,
        total_pairs: int = 0,
    ) -> None:
        """
        Mark a matcher run as started.

        Updates the run state to "running" and sets the start time and total pairs.

        Args:
            run_id: ID of the run to start.
            started_at: Optional start timestamp (defaults to now).
            total_pairs: Total number of pairs to process.
        """
        if started_at is None:
            started_at = datetime.datetime.now().timestamp()
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                stmt = (
                    update(MatcherRun)
                    .where(MatcherRun.id == run_id)
                    .values(
                        state="running",
                        started_at=started_at,
                        total_pairs=total_pairs,
                    )
                )
                await session.execute(stmt)

    async def finish_matcher_run(
        self,
        run_id: int,
        *,
        state: str,
        finished_at: float | None = None,
        processed_pairs: int = 0,
        matches_found: int = 0,
        error: str | None = None,
    ) -> None:
        """
        Mark a matcher run as finished.

        Updates the run with final statistics and completion status.

        Args:
            run_id: ID of the run to finish.
            state: Final state (e.g., "completed", "failed", "stopped").
            finished_at: Optional finish timestamp (defaults to now).
            processed_pairs: Number of pairs that were processed.
            matches_found: Number of matches discovered.
            error: Optional error message if the run failed.
        """
        if finished_at is None:
            finished_at = datetime.datetime.now().timestamp()
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                stmt = (
                    update(MatcherRun)
                    .where(MatcherRun.id == run_id)
                    .values(
                        state=state,
                        finished_at=finished_at,
                        processed_pairs=processed_pairs,
                        matches_found=matches_found,
                        error=error,
                    )
                )
                await session.execute(stmt)

    async def update_matcher_run_progress(
        self,
        run_id: int,
        *,
        processed_pairs: int,
    ) -> None:
        """
        Update the progress of a running matcher run.

        Args:
            run_id: ID of the run to update.
            processed_pairs: Current number of processed pairs.
        """
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                stmt = (
                    update(MatcherRun)
                    .where(MatcherRun.id == run_id)
                    .values(processed_pairs=processed_pairs)
                )
                await session.execute(stmt)

    async def update_matcher_run_matches_found(
        self,
        run_id: int,
        *,
        matches_found: int,
    ) -> None:
        """
        Update the number of matches found in a running matcher run.

        Args:
            run_id: ID of the run to update.
            matches_found: Current number of matches found.
        """
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                stmt = (
                    update(MatcherRun)
                    .where(MatcherRun.id == run_id)
                    .values(matches_found=matches_found)
                )
                await session.execute(stmt)

    async def get_matcher_runs(
        self,
        limit: int | None = 100,
        after_id: int = 0,
        state: str | None = None,
    ) -> list[MatcherRun]:
        """
        Retrieve matcher run records.

        Args:
            limit: Maximum number of runs to return. None for no limit.
            after_id: Only return runs with ID greater than this (for pagination).
            state: Optional filter by run state.

        Returns:
            List of matching MatcherRun objects, ordered by start time descending.
        """
        async with AsyncSession(self.engine) as session:
            stmt = select(MatcherRun).where(MatcherRun.id > after_id)
            if state is not None:
                stmt = stmt.where(MatcherRun.state == state)
            stmt = stmt.order_by(MatcherRun.started_at.desc(), MatcherRun.id.desc())
            if limit is not None:
                stmt = stmt.limit(limit)
            return (await session.execute(stmt)).scalars().all()

    async def get_matcher_run(self, run_id: int) -> MatcherRun | None:
        """
        Retrieve a specific matcher run by ID.

        Args:
            run_id: ID of the run to retrieve.

        Returns:
            The MatcherRun object if found, None otherwise.
        """
        async with AsyncSession(self.engine) as session:
            stmt = select(MatcherRun).where(MatcherRun.id == run_id)
            return (await session.execute(stmt)).scalars().first()

    async def clear_matcher_runs(self) -> None:
        """Delete all matcher run records."""
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                await session.execute(delete(MatcherRun))

    async def get_matches(
        self,
        limit: int | None = 100,
        last_match_id: int = 0,
        origin_uri: HttpUrl | None = None,
        ids: list[int] | None = None,
        time_lte: float | None = None,
        time_gte: float | None = None,
        assets: list[HttpUrl] | None = None,
        csaf_products: list[HttpUrl] | None = None,
        threshold: float | None = None,
    ) -> list[Match]:
        """
        Query match records with optional filters.

        Args:
            limit: Maximum number of matches to return. None for no limit.
            last_match_id: Only return matches with ID >= this (for pagination).
            origin_uri: Filter by asset or CSAF product origin URI.
            ids: Filter by specific match IDs.
            time_lte: Filter matches with timestamp <= this value.
            time_gte: Filter matches with timestamp >= this value.
            assets: Filter by specific asset URIs.
            csaf_products: Filter by specific CSAF product URIs.
            threshold: Filter matches with score >= this value.

        Returns:
            List of Match objects with related asset and CSAF product loaded.
        """
        origin_uri = str(origin_uri) if origin_uri else None  # type: ignore
        async with AsyncSession(self.engine) as session:
            stmt = (
                select(Match)
                .join(Match.asset)
                .join(Match.csaf_product)
                .options(
                    contains_eager(Match.asset),
                    contains_eager(Match.csaf_product),
                    joinedload(Match.matcher_run),
                )
            )
            if origin_uri is not None:
                stmt = stmt.filter(
                    or_(
                        Asset.origin_uri == origin_uri,
                        CsafProduct.origin_uri == origin_uri,
                    )
                )
            if ids is not None:
                stmt = stmt.filter(Match.id.in_(ids))
            stmt = stmt.order_by(Match.timestamp.desc(), Match.id.desc()).where(
                Match.id >= last_match_id
            )
            if time_lte is not None:
                stmt = stmt.where(Match.timestamp <= time_lte)
            if time_gte is not None:
                stmt = stmt.where(Match.timestamp >= time_gte)
            if assets is not None:
                stmt = stmt.where(Asset.uri.in_([str(a) for a in assets]))
            if csaf_products is not None:
                stmt = stmt.where(CsafProduct.uri.in_([str(p) for p in csaf_products]))
            if threshold is not None:
                stmt = stmt.where(Match.score >= threshold)
            if limit is not None:
                stmt = stmt.limit(limit)
            if result := (await session.execute(stmt)).scalars().all():
                return list(result)
        return []

    async def get_match(self, match_id: int) -> Match | None:
        """
        Retrieve a specific match by ID.

        Args:
            match_id: ID of the match to retrieve.

        Returns:
            The Match object with related asset, CSAF product, and run loaded, or None.
        """
        async with AsyncSession(self.engine) as session:
            stmt = (
                select(Match)
                .options(
                    joinedload(Match.asset),
                    joinedload(Match.csaf_product),
                    joinedload(Match.matcher_run),
                )
                .where(Match.id == match_id)
            )
            if result := (await session.execute(stmt)).scalars().first():
                return result
        return None

    async def clear_matches(self) -> None:
        """Delete all match records."""
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                stmt = delete(Match)
                await session.execute(stmt)

    async def clear_assets(self, origin: HttpUrl) -> None:
        """
        Delete all assets from a specific origin and reset its sync metadata.

        Args:
            origin: The origin URI to clear assets for.
        """
        origin = str(origin)  # type: ignore
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                stmt = delete(Asset).where(Asset.origin_uri == origin)
                await session.execute(stmt)
                stmt = (
                    update(SynchronizerMetadata)
                    .where(SynchronizerMetadata.origin_uri == origin)
                    .values(last_run=datetime.datetime.fromtimestamp(0))
                )
                await session.execute(stmt)

    async def clear_csaf_products(self, origin: HttpUrl) -> None:
        """
        Delete all CSAF products from a specific origin and reset its sync metadata.

        Args:
            origin: The origin URI to clear CSAF products for.
        """
        origin = str(origin)
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                stmt = delete(CsafProduct).where(CsafProduct.origin_uri == origin)
                await session.execute(stmt)
                stmt = (
                    update(SynchronizerMetadata)
                    .where(SynchronizerMetadata.origin_uri == origin)
                    .values(last_run=datetime.datetime.fromtimestamp(0))
                )
                await session.execute(stmt)

    async def user_active(self, username: str) -> bool:
        """
        Check if a user exists and is active.

        Args:
            username: The username to check.

        Returns:
            True if the user exists and is active, False otherwise.
        """
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                stmt = select(User).where(User.username == username)
                if user := (await session.execute(stmt)).scalars().first():
                    if user.active:
                        return True
        return False

    async def authenticate_user(self, username: str, password: str) -> User | None:
        """
        Authenticate a user with username and password.

        Args:
            username: The username to authenticate.
            password: The password to verify.

        Returns:
            The User object if authentication succeeds, None otherwise.
        """
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                stmt = select(User).where(User.username == username)
                if user := (await session.execute(stmt)).scalars().first():
                    if user.check_password(password):
                        session.expunge(user)
                        return user
        return None

    async def create_user(self, username: str, password: str):
        """
        Create a new active user.

        Silently succeeds if the user already exists.

        Args:
            username: Username for the new user.
            password: Password for the new user (will be hashed).
        """
        try:
            async with AsyncSession(self.engine) as session:
                async with session.begin():
                    user = User(username=username, active=True)
                    user.set_password(password)
                    session.add(user)
                    await session.flush()
        except sqlalchemy.exc.IntegrityError:
            logger.info(f"User {username} already exists.")
            pass

    async def clear(self) -> None:
        """
        Clear all matcher runs, CSAF products, and assets from the database.

        Also resets all synchronizer metadata to epoch time.
        """
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                stmt = delete(MatcherRun)
                await session.execute(stmt)
                stmt = delete(CsafProduct)
                await session.execute(stmt)
                stmt = delete(Asset)
                await session.execute(stmt)
                await self.__set_all_epoch_last_run(session)

    async def __set_all_epoch_last_run(self, session: AsyncSession) -> None:
        """Sets the last run time to epoch for all synchronizer metadata entries."""
        stmt = update(SynchronizerMetadata).values(
            last_run=datetime.datetime.fromtimestamp(0)
        )
        await session.execute(stmt)

    async def disconnect(self) -> None:
        """
        Close the database connection and dispose of the engine.

        Should be called when shutting down the application.
        """
        if self.engine is not None:
            await self.engine.dispose()
