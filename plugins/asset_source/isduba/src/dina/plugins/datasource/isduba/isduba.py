from typing import Any, List

from dina.plugins.datasource.isduba.datamodels import CsafProductTree
import httpx
from pydantic import BaseModel

from dina.cachedb.fetcher_view import FetcherView
from dina.cachedb.model import Asset, CsafProduct
from dina.common import logging

from dina.plugins.datasource.isduba.connector import get_csaf_product_tree
from dina.plugins.datasource.isduba.converter import convert_into_database_format
from dina.plugins.datasource.isduba.generated import isduba_api_client
from dina.synchronizer.base import DataSourcePlugin

logger = logging.get_logger(__name__)


class IsdubaDataSource(DataSourcePlugin):
    class Config(BaseModel):
        username: str
        password: str
        verify_ssl: bool
        url: str

    def __init__(self, config):
        config.DataSource.Plugin = IsdubaDataSource.Config.model_validate(
            config.DataSource.Plugin
        )
        super().__init__(config)

    def endpoint_info(self) -> str:
        """Return information about the data source endpoint."""
        return self.config.DataSource.Plugin.url

    async def fetch_data(self, fetcher_view: FetcherView) -> List[Asset | CsafProduct]:
        """Fetch data from the data source and return it as a list of Assets or CsafDocuments."""
        plugin = IsdubaDataSource(self.config)
       
        token_url = "{}:8081/realms/isduba/protocol/openid-connect/token".format(
             plugin.origin_uri
         )
        
        token = (
            httpx.post(
                 token_url,
                 data={
                     "grant_type": "password",
                     "client_id": "auth",
                     "username": self.config.DataSource.Plugin.username,
                     "password": self.config.DataSource.Plugin.password,
                 },
                 verify=self.config.DataSource.Plugin.verify_ssl,
             )
             .json()
             .get("access_token")
         )

        api_url = "{}/api".format(plugin.origin_uri)

        configuration = isduba_api_client.Configuration(
            host=api_url,
            api_key={"bearerAuth": token},
            api_key_prefix={"bearerAuth": "Bearer"},
        )
        configuration.verify_ssl = self.config.DataSource.Plugin.verify_ssl
        ret = []

        # Enter a context with an instance of the API client
        async with isduba_api_client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = isduba_api_client.DefaultApi(api_client)

            try:
                api_response = await api_instance.documents_get(limit=5, offset=0)

                if not api_response.documents:
                    return ret

                for document in api_response.documents:
                    id = document["id"]
                    path = f"/api/documents/{id}"
                    api_response = await api_instance.documents_id_get(id)
                    csaf_product_tree: CsafProductTree = await get_csaf_product_tree(plugin.origin_uri, path, api_response["document"], api_response["product_tree"])

                    if csaf_product_tree is not None:
                        tree = await convert_into_database_format(fetcher_view, csaf_product_tree)

                        for t in tree:
                            ret.append(t)

            except Exception as e:
                raise Exception(
                    "Exception when calling DefaultApi->documents_get:\n\n%s" % e
                )

            await api_client.close()

        # Return a list of Asset or CsafDocument objects
        return ret

    async def cleanup_data(self, data_to_check: List[Any]):
        return []

    @property
    def origin_uri(self):
        return self.config.DataSource.Plugin.url
