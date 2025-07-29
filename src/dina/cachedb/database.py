from dataclasses import dataclass
from typing import List, Union, Optional
import logging
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from sqlalchemy.sql.ddl import CreateSchema
from sqlalchemy import select

from dina.cachedb.model import Base,Manufacturer,DeviceType,Device,Software,File,Hash,ProductRelationship,AssetSynchronizer,CsafDocument

logger = logging.getLogger(__name__)


class CacheDB:
    @dataclass
    class Config:
        user: str
        password: str
        host: str
        port: int
        database: str

    def __init__(self) -> None:
        super().__init__()
        self.engine: Optional[AsyncEngine] = None

    async def connect(self, config: Config) -> None:
        self.engine = create_async_engine(
            f"postgresql+asyncpg://{config.user}:{config.password}@{config.host}:{config.port}/{config.database}"
        )
        async with self.engine.begin() as conn:
            await conn.execute(CreateSchema("cacheDB", if_not_exists=True))
            await conn.run_sync(Base.metadata.create_all)

    async def store(self, data: List[Union[Manufacturer, CsafDocument]]) -> None:
        """
        Stores a list of assets or CSAF documents into the database. This function ensures
        the provided data is added to the database in a single transaction using the
        Session context management.

        :param data: A list containing either Asset or CsafDocument objects to be stored
            in the database.
        :type data: List[Union[Asset, CsafDocument]]

        :return: None
        """
        async with AsyncSession(self.engine) as session:
            async with session.begin():
                for asset in data:
                    logger.info(f"DATA: {asset}")
                    await asset.create_or_update(session)
                await session.commit()
                await session.close()

    async def check_delete(self):

        async with AsyncSession(self.engine) as session:

            stmt = select(AssetSynchronizer)
            result = await session.execute(stmt)
            obj = result.scalar_one_or_none()
            if obj:
                starttime=obj.last_run
                logger.info(f"DELETE {starttime}")

            result = await session.execute(select(Manufacturer))
            all_objects = result.scalars().all()
            for x in all_objects:
                logger.info(f"DELETE Manufacturer: {x.name} {x.last_seen}")
                if x.last_seen < starttime:
                    logger.info(f"DELETE Manufacturer: {x.name} {x.last_seen}")
                    await session.delete(x)

            result = await session.execute(select(DeviceType))
            all_objects = result.scalars().all()
            for x in all_objects:
                if x.last_seen < starttime:
                    logger.info(f"DELETE DeviceType: {x.model} {x.last_seen}")
                    await session.delete(x)

            result = await session.execute(select(Device))
            all_objects = result.scalars().all()
            for x in all_objects:
                if x.last_seen < starttime:
                    logger.info(f"DELETE Device: {x.name} {x.last_seen}")
                    await session.delete(x)

            result = await session.execute(select(Software))
            all_objects = result.scalars().all()
            for x in all_objects:
                if x.last_seen < starttime:
                    logger.info(f"DELETE Software: {x.name} {x.last_seen}")
                    await session.delete(x)

            result = await session.execute(select(Hash))
            all_objects = result.scalars().all()
            for x in all_objects:
                if x.last_seen < starttime:
                    logger.info(f"DELETE Hash: {x.name} {x.last_seen}")
                    await session.delete(x)

            result = await session.execute(select(File))
            all_objects = result.scalars().all()
            for x in all_objects:
                if x.last_seen < starttime:
                    logger.info(f"DELETE File: {x.name} {x.last_seen}")
                    await session.delete(x)

            result = await session.execute(select(ProductRelationship))
            all_objects = result.scalars().all()
            for x in all_objects:
                if x.last_seen < starttime:
                    logger.info(f"DELETE ProductRelationship: {x.id} {x.last_seen}")
                    await session.delete(x)

            await session.commit()

    async def disconnect(self) -> None:
        if self.engine is not None:
            await self.engine.dispose()
