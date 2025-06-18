import asyncio
import logging
from typing import List

from cachedb.model import Asset
from manager.base import DataSourcePlugin

logger = logging.getLogger(__name__)


class NetboxDataSource(DataSourcePlugin):
    def __init__(self, config=None):
        super().__init__(config)
        # Extract configuration values
        self.api_url = self.config.get("api_url", "")
        self.api_token = self.config.get("api_token", "")
        logger.debug(f"Initialized NetboxDataSource with API URL: {self.api_url}")

    async def fetch_data(self) -> List[Asset]:
        logger.debug(f"Fetching data from Netbox at {self.api_url}")
        # In a real implementation, this would use the API URL and token to fetch data
        await asyncio.sleep(1)
        return [Asset()]

    def endpoint_info(self) -> str:
        return f"{self.api_url}"
