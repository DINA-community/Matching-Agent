import asyncio
from typing import Any, List, Union

from dina.cachedb.fetcher_view import FetcherView
from dina.cachedb.model import Asset, CsafProduct
from dina.common import logging
from dina.synchronizer.base import DataSourcePlugin

logger = logging.get_logger(__name__)


class SampleDataSource(DataSourcePlugin):
    def __init__(self, config):
        super().__init__(config)
        # Extract configuration values
        try:
            plugin_config = self.config["DataSource"]["YourPluginSection"]
            self.some_param = plugin_config["some_param"]
            # Add other configuration parameters as needed
        except KeyError:
            raise KeyError("Missing required configuration parameter")

    def endpoint_info(self) -> str:
        """Return information about the data source endpoint."""
        return "http://endpoint.sample.com/"

    async def fetch_data(
        self, fetcher_view: FetcherView
    ) -> List[Union[Asset, CsafProduct]]:
        """Fetch data from the data source and return it as a list of Assets or CsafProducts."""
        # Implement your data fetching logic here
        # This is where you would connect to your data source and retrieve data

        # Example: Simulate fetching data with a delay
        logger.trace("SampleDataSource: Fetching data from data source")
        await asyncio.sleep(1)

        # Return a list of Asset or CsafDocument objects
        return []

    @property
    def origin_uri(self) -> str:
        return "http://endpoint.sample.com/"

    async def cleanup_data(self, data_to_check: List[Any]):
        pass
