from typing import List, Union

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.sql.ddl import CreateSchema

from cachedb.model import Base, Asset, CsafDocument


class CacheDB:
    def __init__(self):
        super().__init__()
        self.engine = None

    async def connect(self):
        self.engine = create_async_engine(
            "postgresql+asyncpg://postgres:postgres@localhost:5432/cachedb", echo=True
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
