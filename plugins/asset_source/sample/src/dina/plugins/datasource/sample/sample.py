import asyncio
from typing import Any, List

from pydantic import HttpUrl

from dina.cachedb.fetcher_view import FetcherView
from dina.common import log
from dina.synchronizer.base import DataSourcePlugin
from dina.synchronizer.plugin_base.data_source import (
    MappedRelationship,
    Relationship,
    FetchRelationshipsResult,
    FetchProductsResult,
)

logger = log.get_logger(__name__)


class SampleDataSource(DataSourcePlugin):
    async def fetch_relationships(
        self, fetcher_view: FetcherView
    ) -> FetchRelationshipsResult:
        return FetchRelationshipsResult(again=False)

    async def map_relationships(
        self, fetcher_view: FetcherView, relations: List[Relationship]
    ) -> List[MappedRelationship]:
        return []

    async def cleanup_relationships(
        self, relationships_to_check: List[MappedRelationship]
    ) -> List[MappedRelationship]:
        return relationships_to_check

    def __init__(self, config):
        super().__init__(config)
        # Extract configuration values
        try:
            pass
            # plugin_config = self.config["DataSource"]["YourPluginSection"]
            # self.some_param = plugin_config["some_param"]
            # Add other configuration parameters as needed
        except KeyError:
            raise KeyError("Missing required configuration parameter")

    def endpoint_info(self) -> str:
        """Return information about the data source endpoint."""
        return "http://endpoint.sample.com/"

    async def fetch_products(self, fetcher_view: FetcherView) -> FetchProductsResult:
        """Fetch data from the data source and return it as a list of Assets or CsafProducts."""
        # Implement your data fetching logic here
        # This is where you would connect to your data source and retrieve data

        # Example: Simulate fetching data with a delay
        logger.trace("SampleDataSource: Fetching data from data source")
        await asyncio.sleep(1)

        # Return a list of Asset or CsafDocument objects
        return FetchProductsResult(again=False)

    @property
    def origin_uri(self) -> HttpUrl:
        return HttpUrl("http://endpoint.sample.com/")

    async def cleanup_products(self, data_to_check: List[Any]):
        pass
