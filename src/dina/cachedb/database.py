from typing import List, Union, Optional

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from sqlalchemy.sql.ddl import CreateSchema

from dina.cachedb.model import Base, Asset, CsafDocument


class CacheDB:
    def __init__(self) -> None:
        super().__init__()
        self.engine: Optional[AsyncEngine] = None

    async def connect(self) -> None:
        self.engine = create_async_engine(
            "postgresql+asyncpg://postgres:postgres@localhost:5432/cachedb"
        )
        async with self.engine.begin() as conn:
            await conn.execute(CreateSchema("cacheDB", if_not_exists=True))
            await conn.run_sync(Base.metadata.create_all)

    async def store(self, data: List[Union[Asset, CsafDocument]]) -> None:
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
                session.add_all(data)

    async def disconnect(self) -> None:
        if self.engine is not None:
            await self.engine.dispose()
