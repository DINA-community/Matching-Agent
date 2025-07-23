from dataclasses import dataclass
from typing import List, Union, Optional
import logging
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from sqlalchemy.sql.ddl import CreateSchema

from dina.cachedb.model import Base, Asset, CsafDocument, Manufacturer

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

    async def store(self, data: List[Union[Asset, CsafDocument, Manufacturer]]) -> None:
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

    async def disconnect(self) -> None:
        if self.engine is not None:
            await self.engine.dispose()
