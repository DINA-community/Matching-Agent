from typing import Any, List

from dina.plugins.datasource.isduba.datamodels import CsafProductTree
import httpx
from pydantic import BaseModel

from dina.cachedb.database import CacheDB
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
        database_host: str
        database_port: int
        database: str
        database_username: str
        database_password: str

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
        config = IsdubaDataSource(self.config)

        token = await self._get_token(config.origin_uri)
        configuration = self._create_api_config(config.origin_uri, token)

        offset, limit = 0, 100

        while True:
            try:
                token = await self._get_token(config.origin_uri)
                configuration = self._create_api_config(config.origin_uri, token)

                async with isduba_api_client.ApiClient(configuration) as api_client:
                    api_instance = isduba_api_client.DefaultApi(api_client)

                    api_response = await api_instance.documents_get(limit=limit, offset=offset)

                    if not api_response.documents:
                        break

                    all_new_data: list[Asset | CsafProduct] = []

                    for document in api_response.documents:
                        doc_id = document["id"]
                        path = f"/api/documents/{doc_id}"

                        detail_response = await api_instance.documents_id_get(doc_id)
                        csaf_product_tree: CsafProductTree = await get_csaf_product_tree(
                            config.origin_uri,
                            path,
                            detail_response["document"],
                            detail_response["product_tree"],
                        )

                        if csaf_product_tree:
                            converted = await convert_into_database_format(fetcher_view, csaf_product_tree)
                            all_new_data.extend(converted)

                    if all_new_data:
                        await self._add_data(all_new_data)

                    offset += limit

            except Exception as e:
                raise Exception(f"Exception when calling DefaultApi->documents_get:\n\n{e}")

        return []

    async def _get_token(self, origin_uri: str) -> str:
        """Retrieve an access token via Keycloak."""
        token_url = f"{origin_uri}:8081/realms/isduba/protocol/openid-connect/token"
        response = httpx.post(
            token_url,
            data={
                "grant_type": "password",
                "client_id": "auth",
                "username": self.config.DataSource.Plugin.username,
                "password": self.config.DataSource.Plugin.password,
            },
            verify=self.config.DataSource.Plugin.verify_ssl,
        )

        return response.json().get("access_token")

    def _create_api_config(self, origin_uri: str, token: str):
        """Build API configuration for the isduba API client."""
        api_url = f"{origin_uri}/api"
        configuration = isduba_api_client.Configuration(
            host=api_url,
            api_key={"bearerAuth": token},
            api_key_prefix={"bearerAuth": "Bearer"},
        )
        configuration.verify_ssl = self.config.DataSource.Plugin.verify_ssl

        return configuration

    async def _add_data(self, data: list[Asset | CsafProduct]):
        """Insert fetched data into the cache database."""
        config = CacheDB.Config(
            host= self.config.DataSource.Plugin.database_host,
            port=self.config.DataSource.Plugin.database_port,
            database=self.config.DataSource.Plugin.database,
            username=self.config.DataSource.Plugin.database_username,
            password=self.config.DataSource.Plugin.database_password,
        )

        cache_db = CacheDB()
        await cache_db.connect(config)
        await cache_db.store(data)
        await cache_db.disconnect()

    async def cleanup_data(self, data_to_check: List[Any]):
        return []
    
    @property
    def origin_uri(self):
        return self.config.DataSource.Plugin.url
