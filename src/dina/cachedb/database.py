import datetime
import logging
from typing import List, Optional, Type, Union, AsyncGenerator

from pydantic import BaseModel
from sqlalchemy import (
    and_,
    delete,
    or_,
    select,
    update,
    literal,
    func,
)
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import joinedload
from sqlalchemy.sql.ddl import CreateSchema

from dina.cachedb.fetcher_view import FetcherView
from dina.cachedb.model import (
    Asset,
    Base,
    CsafProduct,
    Product,
    csaf_product_relationship,
    product_relationship,
    Match,
)
from dina.synchronizer.plugin_base.data_source import (
    DataSourcePlugin,
    MappedRelationship,
)

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
            f"postgresql+psycopg://{config.username}:{config.password}@{config.host}:{config.port}/{config.database}",
        )
        async with self.engine.begin() as conn:
            await conn.execute(CreateSchema("cacheDB", if_not_exists=True))
            await conn.run_sync(Base.metadata.create_all)

    def fetcher_view(self, origin: str) -> FetcherView:
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
        Stores a list of assets or CSAF documents into the database. This function ensures
        the provided data is added to the database in a single transaction using the
        Session context management.

        :param data: A list containing either Asset or CsafDocument objects to be stored
            in the database.
        :type data: List[Union[Asset, CsafDocument]]

        :return: None
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
                    "origin_uri": d.origin_uri,
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
                    .where(Asset.last_update < stale_timestamp)
                    .options(joinedload(Asset.product))
                    .filter(Asset.origin_uri == source.origin_uri)
                )
                data.extend((await session.execute(stmt)).scalars().all())

                csaf_stmt = (
                    select(CsafProduct)
                    .where(CsafProduct.last_update < stale_timestamp)
                    .options(joinedload(CsafProduct.product))
                    .filter(CsafProduct.origin_uri == source.origin_uri)
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
            .filter(product_relationship.c.origin_uri == source.origin_uri)
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
            .filter(csaf_product_relationship.c.origin_uri == source.origin_uri)
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

    async def fetch_pairs_batches(
        self,
    ) -> AsyncGenerator[list[tuple[CsafProduct, Asset]]]:
        async with AsyncSession(self.engine) as session:
            csaf_offset = 0
            csaf_limit = 500

            csaf_count = int(
                (await session.execute(func.count(CsafProduct.id))).scalar()
            )  # type: ignore
            asset_count = int((await session.execute(func.count(Asset.id))).scalar())  # type: ignore

            while True:
                logger.trace(f"Fetching csaf product offset: {csaf_offset}")
                csaf_subquery = (
                    select(CsafProduct).limit(csaf_limit).offset(csaf_offset)
                ).subquery("csaf")
                asset_offset = 0
                asset_limit = 500
                while True:
                    logger.trace(f"Fetching asset offset: {asset_offset}")
                    asset_subquery = (
                        select(Asset)
                        .limit(asset_limit)
                        .offset(asset_offset)
                        .subquery("assets")
                    )
                    pairs = (
                        select(
                            Match.id.label("match_id"),
                            Match.timestamp.label("match_timestamp"),
                            asset_subquery.c.id.label("asset_id"),
                            asset_subquery.c.last_update.label("asset_timestamp"),
                            csaf_subquery.c.id.label("csaf_id"),
                            csaf_subquery.c.last_update.label("csaf_timestamp"),
                        )
                        .select_from(asset_subquery)
                        .join(csaf_subquery, literal(value=True))
                        .join(
                            Match,
                            and_(
                                Match.asset_id == asset_subquery.c.id,
                                Match.csaf_product_id == csaf_subquery.c.id,
                            ),
                            full=True,
                        )
                        .distinct(asset_subquery.c.id, csaf_subquery.c.id)
                        .order_by(
                            asset_subquery.c.id,
                            csaf_subquery.c.id,
                            Match.timestamp.desc(),
                        )
                    ).subquery("pairs")

                    query = (
                        select(CsafProduct, Asset)
                        .select_from(pairs)
                        .where(
                            or_(
                                pairs.c.match_id.is_(None),
                                pairs.c.match_timestamp < pairs.c.asset_timestamp,
                                pairs.c.match_timestamp < pairs.c.csaf_timestamp,
                            )
                        )
                        .join(CsafProduct, CsafProduct.id == pairs.c.csaf_id)
                        .join(Asset, Asset.id == pairs.c.asset_id)
                        .options(
                            joinedload(CsafProduct.product), joinedload(Asset.product)
                        )
                    )

                    result = (await session.execute(query)).tuples().all()
                    yield result  # type: ignore

                    asset_offset += asset_limit
                    if asset_offset >= asset_count:
                        break

                csaf_offset += csaf_limit
                if csaf_offset >= csaf_count:
                    break

            return

    async def store_matches(self, matches: list[Match]):
        if not matches:
            return
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                session.add_all(matches)

    async def get_matches(self, limit: int = 100, offset: int = 0) -> list[Match]:
        async with AsyncSession(self.engine) as session:
            stmt = (
                select(Match)
                .options(joinedload(Match.asset), joinedload(Match.csaf_product))
                .order_by(Match.timestamp.desc(), Match.id.desc())
                .limit(limit)
                .offset(offset)
            )
            if result := (await session.execute(stmt)).scalars().all():
                return list(result)
        return []

    async def get_match(self, match_id: int) -> Match | None:
        async with AsyncSession(self.engine) as session:
            stmt = (
                select(Match)
                .options(joinedload(Match.asset), joinedload(Match.csaf_product))
                .where(Match.id == match_id)
            )
            if result := (await session.execute(stmt)).scalars().first():
                return result
        return None

    async def disconnect(self) -> None:
        if self.engine is not None:
            await self.engine.dispose()
