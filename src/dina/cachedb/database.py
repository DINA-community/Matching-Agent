import datetime
from typing import AsyncGenerator, List, Optional, Type, Union

import sqlalchemy.exc
from pydantic import BaseModel, HttpUrl
from sqlalchemy import (
    and_,
    delete,
    literal,
    or_,
    select,
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

    def fetcher_view(self, origin: HttpUrl) -> FetcherView:
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
        batch_size_sqrt: int = 50,
    ) -> AsyncGenerator[list[tuple[CsafProduct, Asset]]]:
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

                    # Find pairs within this block that need matching
                    query = (
                        select(CsafProduct, Asset)
                        .select_from(CsafProduct)
                        .join(Asset, literal(True))
                        .where(CsafProduct.id.in_(csaf_ids))
                        .where(Asset.id.in_(asset_ids))
                        .outerjoin(
                            Match,
                            and_(
                                Match.asset_id == Asset.id,
                                Match.csaf_product_id == CsafProduct.id,
                            ),
                        )
                        .where(
                            or_(
                                Match.id.is_(None),
                                Match.timestamp < Asset.last_update,
                                Match.timestamp < CsafProduct.last_update,
                            )
                        )
                        .options(
                            joinedload(CsafProduct.product), joinedload(Asset.product)
                        )
                    )

                    if result := (await session.execute(query)).tuples().all():
                        yield result  # type: ignore

            return

    async def store_matches(self, matches: list[Match]) -> list[int]:
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
        origin_uri = str(origin_uri) if origin_uri else None  # type: ignore
        async with AsyncSession(self.engine) as session:
            stmt = (
                select(Match)
                .join(Match.asset)
                .join(Match.csaf_product)
                .options(
                    contains_eager(Match.asset), contains_eager(Match.csaf_product)
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
        async with AsyncSession(self.engine) as session:
            stmt = (
                select(Match)
                .options(joinedload(Match.asset), joinedload(Match.csaf_product))
                .where(Match.id == match_id)
            )
            if result := (await session.execute(stmt)).scalars().first():
                return result
        return None

    async def clear_matches(self) -> None:
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                stmt = delete(Match)
                await session.execute(stmt)

    async def clear_assets(self, origin: HttpUrl) -> None:
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
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                stmt = select(User).where(User.username == username)
                if user := (await session.execute(stmt)).scalars().first():
                    if user.active:
                        return True
        return False

    async def authenticate_user(self, username: str, password: str) -> User | None:
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                stmt = select(User).where(User.username == username)
                if user := (await session.execute(stmt)).scalars().first():
                    if user.check_password(password):
                        session.expunge(user)
                        return user
        return None

    async def create_user(self, username: str, password: str):
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
        async with AsyncSession(self.engine) as session:
            async with session.begin():
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
        if self.engine is not None:
            await self.engine.dispose()
