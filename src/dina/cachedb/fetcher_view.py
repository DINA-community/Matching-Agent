"""
Provides a database view interface for fetcher plugins to interact with synchronization metadata.

This module contains the FetcherView class, which serves as an abstraction layer
for fetcher plugins to query existing records and manage synchronization metadata
associated with a specific data origin.
"""

import datetime
from typing import Any, Dict, List, Type

from pydantic import HttpUrl
from sqlalchemy import ColumnExpressionArgument, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.orm import joinedload, noload

from dina.cachedb.model import Asset, CsafProduct, SynchronizerMetadata


class FetcherView:
    """
    Database view interface for fetcher plugins to access and manage synchronization data.

    Provides methods to query existing assets or CSAF products, and to read/write
    synchronization metadata (plugin state, last run time) for a specific origin URI.
    """

    def __init__(self, origin: HttpUrl, engine: AsyncEngine) -> None:
        """
        Initialize a FetcherView for a specific data origin.

        Args:
            origin: The URI identifying the data source origin.
            engine: SQLAlchemy async engine for database operations.
        """
        self.__engine = engine
        self.__origin = str(origin)

    async def get_existing[T: Asset | CsafProduct](
        self,
        cls: Type[T],
        where_clause: ColumnExpressionArgument,
    ) -> List[T]:
        """
        Query existing Asset or CsafProduct records from the database.

        Retrieves records matching the given criteria that belong to this origin.
        Returns detached instances that are not automatically synchronized to the database.

        Args:
            cls: The model class (Asset or CsafProduct) to query.
            where_clause: SQLAlchemy where clause to filter results.

        Returns:
            List of matching records detached from the session.
        """
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
        """
        Store plugin-specific metadata for this origin.

        Allows fetcher plugins to persist arbitrary state or configuration data
        associated with their synchronization runs.

        Args:
            plugin_metadata: Dictionary of plugin-specific metadata to store.
        """
        async with AsyncSession(self.__engine) as session:
            metadata = await self.__get_meta(session)
            metadata.plugin_metadata = plugin_metadata
            await session.merge(metadata)
            await session.commit()

    async def plugin_metadata(self) -> Dict[str, Any]:
        """
        Retrieve plugin-specific metadata for this origin.

        Returns:
            Dictionary of plugin-specific metadata, or empty dict if none exists.
        """
        async with AsyncSession(self.__engine) as session:
            return await (
                await self.__get_meta(session)
            ).awaitable_attrs.plugin_metadata

    async def last_run(self) -> datetime.datetime:
        """
        Get the timestamp of the last successful synchronization run for this origin.

        Returns:
            Datetime of last run in UTC timezone.
        """
        async with AsyncSession(self.__engine) as session:
            return (
                await (await self.__get_meta(session)).awaitable_attrs.last_run
            ).replace(tzinfo=datetime.timezone.utc)

    async def set_last_run(self, last_run: datetime.datetime):
        """
        Update the timestamp of the last successful synchronization run.

        Args:
            last_run: Datetime to record as the last successful run. Will be converted to UTC.
        """
        async with AsyncSession(self.__engine) as session:
            metadata = await self.__get_meta(session)
            metadata.last_run = last_run.astimezone(tz=datetime.timezone.utc)
            await session.merge(metadata)
            await session.commit()

    async def __get_meta(self, session: AsyncSession) -> SynchronizerMetadata:
        """
        Retrieve or create synchronizer metadata record for this origin.

        Handles race conditions when multiple processes attempt to create the initial record.

        Args:
            session: Active database session.

        Returns:
            SynchronizerMetadata record for this origin.
        """
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
