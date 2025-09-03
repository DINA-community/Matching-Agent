import datetime
from typing import Any, Dict, List, Type

from sqlalchemy import ColumnExpressionArgument, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.orm import joinedload, noload

from dina.cachedb.model import Asset, CsafProduct, SynchronizerMetadata


class FetcherView:
    def __init__(self, origin: str, engine: AsyncEngine) -> None:
        self.__engine = engine
        self.__origin = origin

    async def get_existing[T: Asset | CsafProduct](
        self,
        cls: Type[T],
        where_clause: ColumnExpressionArgument,
    ) -> List[T]:
        async with AsyncSession(self.__engine) as session:
            result: List[T] = list(
                (
                    await session.execute(
                        select(cls)
                        .where(where_clause)
                        .options(joinedload(cls.product))
                        .options(noload(cls.matches))
                        .options(noload(cls.children))
                        .options(noload(cls.parents))
                        .filter(cls.origin_uri == self.__origin)
                    )
                )
                .unique()
                .scalars()
                .all()
            )
            # We want to remove all instances from the session so that any changes
            # are not directly synced.
            # The synchronization will occur later after preprocessing during store_data.
            session.expunge_all()
            return result

    async def set_plugin_metadata(self, plugin_metadata: Dict[str, Any]):
        async with AsyncSession(self.__engine) as session:
            metadata = await self.__get_meta(session)
            metadata.plugin_metadata = plugin_metadata
            await session.merge(metadata)
            await session.commit()

    async def plugin_metadata(self) -> Dict[str, Any]:
        async with AsyncSession(self.__engine) as session:
            return await (
                await self.__get_meta(session)
            ).awaitable_attrs.plugin_metadata

    async def last_run(self) -> datetime.datetime:
        async with AsyncSession(self.__engine) as session:
            return await (await self.__get_meta(session)).awaitable_attrs.last_run

    async def set_last_run(self, last_run: datetime.datetime):
        async with AsyncSession(self.__engine) as session:
            metadata = await self.__get_meta(session)
            metadata.last_run = last_run
            await session.merge(metadata)
            await session.commit()

    async def __get_meta(self, session: AsyncSession) -> SynchronizerMetadata:
        stmt = select(SynchronizerMetadata).where(
            SynchronizerMetadata.origin_uri == self.__origin
        )
        db_metadata = (await session.execute(stmt)).scalar_one_or_none()
        if db_metadata is None:
            db_metadata = SynchronizerMetadata(
                origin_uri=self.__origin, plugin_metadata={}
            )
            session.add(db_metadata)
            try:
                await session.commit()
                await session.flush()
            except IntegrityError:
                # Another process/thread created the record between our query and insert
                # Roll back and query again
                await session.rollback()
                stmt = select(SynchronizerMetadata).where(
                    SynchronizerMetadata.origin_uri == self.__origin
                )
                db_metadata = (await session.execute(stmt)).scalar_one()
        return db_metadata
