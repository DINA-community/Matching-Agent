import asyncio
from typing import List, Union

from dina.cachedb.model import CsafDocument, Asset
from dina.synchronizer.base import DataSourcePlugin


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

    async def fetch_data(self) -> List[Union[Asset, CsafDocument]]:
        """Fetch data from the data source and return it as a list of Assets or CsafDocuments."""
        # Implement your data fetching logic here
        # This is where you would connect to your data source and retrieve data

        # Example: Simulate fetching data with a delay
        await asyncio.sleep(1)

        # Return a list of Asset or CsafDocument objects
        return []
