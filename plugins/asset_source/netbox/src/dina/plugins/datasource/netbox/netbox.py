import asyncio
import logging
from typing import List

from dina.cachedb.model import Asset
from dina.synchronizer.plugin_base.data_source import DataSourcePlugin

from dina.netbox_api.net_box_rest_api_client.client import Client
from dina.netbox_api.net_box_rest_api_client.types import Response


from dina.netbox_api.net_box_rest_api_client.api.dcim import dcim_manufacturers_list

logger = logging.getLogger(__name__)


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
        self.response: Response = dcim_manufacturers_list.sync(client=self.client)
        self.results = self.response.results
        # logger.info(f"DATA: {self.results}")
        await asyncio.sleep(1)
        return [self.results]

    def endpoint_info(self) -> str:
        return f"{self.api_url}"
