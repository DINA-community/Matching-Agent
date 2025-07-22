import asyncio
from typing import List

from dina.cachedb.model import Asset
from dina.common import logging
from dina.synchronizer.plugin_base.data_source import DataSourcePlugin
from .api_client import Client  # type: ignore
from .api_client.api.dcim import dcim_manufacturers_list  # type: ignore
from .api_client.api.dcim import dcim_device_types_list
from .api_client.api.dcim import dcim_devices_list

logger = logging.get_logger(__name__)


class NetboxDataSource(DataSourcePlugin):
    def __init__(self, config=None):
        super().__init__(config)
        # Extract configuration values
        try:
            netbox = self.config["DataSource"]["Netbox"]
            self.api_url = netbox["api_url"]
            self.api_token = netbox["api_token"]
            self.client = Client(
                base_url=self.api_url,
                headers={"Authorization": f"Token {self.api_token}"},
            )
        except KeyError:
            raise KeyError("Missing Netbox configuration parameter")
        logger.debug(f"Initialized NetboxDataSource with API URL: {self.api_url}")

    async def fetch_data(self) -> List[Asset]:
        # In a real implementation, this would use the API URL and token to fetch data
        results = []
        response = await dcim_manufacturers_list.asyncio(client=self.client)
        results = response.results
        response = await dcim_device_types_list.asyncio(client=self.client)
        results = results + response.results
        response = await dcim_devices_list.asyncio(client=self.client)
        results = results + response.results
        logger.info(f"DATA: {results}")
        await asyncio.sleep(1)
        return [results]

    def endpoint_info(self) -> str:
        return f"{self.api_url}"
