import logging
from typing import List, Optional, Type, Union

from pydantic import BaseModel
from sqlalchemy import delete, select, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.sql.ddl import CreateSchema

from dina.cachedb.fetcher_view import FetcherView
from dina.cachedb.model import (
    Asset,
    Base,
    CsafProduct,
    Product,
)
from dina.synchronizer.plugin_base.data_source import DataSourcePlugin

logger = logging.getLogger(__name__)


class CacheDB:
    class Config(BaseModel):
        host: str
        port: int
        database: str
        username: str
        password: str

    def __init__(self) -> None:
        super().__init__()
        self.engine: Optional[AsyncEngine] = None

    async def connect(self, config: Config) -> None:
        self.engine = create_async_engine(
            f"postgresql+asyncpg://{config.username}:{config.password}@{config.host}:{config.port}/{config.database}",
        )
        async with self.engine.begin() as conn:
            await conn.execute(CreateSchema("cacheDB", if_not_exists=True))
            await conn.run_sync(Base.metadata.create_all)

    def fetcher_view(self, origin: str) -> FetcherView:
        if self.engine is not None:
            return FetcherView(origin, self.engine)
        else:
            raise Exception("Database not connected")

    async def store(self, data: List[Union[Asset, CsafProduct]]) -> None:
        """
        Stores a list of assets or CSAF documents into the database. This function ensures
        the provided data is added to the database in a single transaction using the
        Session context management.

        :param data: A list containing either Asset or CsafDocument objects to be stored
            in the database.
        :type data: List[Union[Asset, CsafDocument]]

        :return: None
        """
        if not data:
            return

        # Split data into assets and csaf_docs
        new_data = [o for o in data if o.id is None]
        assets_to_update = [
            o for o in data if isinstance(o, Asset) and o.id is not None
        ]
        csaf_products_to_update = [
            o for o in data if isinstance(o, CsafProduct) and o.id is not None
        ]

        async with AsyncSession(self.engine) as session:
            async with session.begin():
                if new_data:
                    session.add_all(new_data)
                if assets_to_update:
                    await self.__update(session, Asset, assets_to_update)

                if csaf_products_to_update:
                    await self.__update(session, CsafProduct, csaf_products_to_update)

    async def __update(
        self,
        session: AsyncSession,
        ty: Type[Asset | CsafProduct],
        data: List[Asset] | List[CsafProduct],
    ):
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

    async def run_cleanup_for_plugin(self, source: DataSourcePlugin):
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                fetcher_view = self.fetcher_view(source.origin_uri)
                last_run = await fetcher_view.last_run()
                # TODO: Make the time configurable
                stale_timestamp = last_run.timestamp() - 60
                # We want to check if anything that was fetched X seconds before the last run is still valid
                stmt = select(Asset).where(Asset.last_update < stale_timestamp)
                asset_results = await session.execute(stmt)
                data: List[Asset | CsafProduct] = list(asset_results.scalars().all())

                csaf_stmt = select(CsafProduct).where(
                    CsafProduct.last_update < stale_timestamp
                )
                csaf_results = await session.execute(csaf_stmt)
                data.extend(list(csaf_results.scalars().all()))

                cleanup_results = await source.cleanup_data(data)
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

    async def disconnect(self) -> None:
        if self.engine is not None:
            await self.engine.dispose()
