import asyncio
import concurrent.futures
from typing import Any, List

import httpx
from pydantic import BaseModel

from dina.cachedb.fetcher_view import FetcherView
from dina.cachedb.model import Asset, CsafProduct
from dina.common import logging
from dina.plugins.datasource.isduba.connector import get_csaf_product_tree
from dina.plugins.datasource.isduba.converter import (
    _update_product_fields,
    convert_into_database_format,
)
from dina.plugins.datasource.isduba.generated import isduba_api_client
from dina.synchronizer.base import DataSourcePlugin
from dina.synchronizer.plugin_base.data_source import CleanUpDecision, FetchDataResult

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
        self.__limit = 1000
        self.__offset = 0
        super().__init__(config)
        logging.get_logger("httpx").setLevel(logging.WARNING)
        logging.get_logger("httpcore").setLevel(logging.WARNING)

    def endpoint_info(self) -> str:
        """Return information about the data source endpoint."""
        return self.config.DataSource.Plugin.url

    async def fetch_data(self, fetcher_view: FetcherView) -> FetchDataResult:
        """Fetch data from the data source and return it as a list of Assets or CsafDocuments."""
        token = await self._get_token(self.origin_uri)
        configuration = self._create_api_config(self.origin_uri, token)
        async with isduba_api_client.ApiClient(configuration) as api_client:
            api_instance = isduba_api_client.DefaultApi(api_client)
            try:
                api_response = await api_instance.documents_get(
                    limit=self.__limit, offset=self.__offset
                )

                if not api_response.documents:
                    # If there are no more results, we reset the offset to zero and return an empty list
                    # The fetcher will be called for the next syncing interval and can start from offset 0
                    self.__offset = 0
                    return FetchDataResult(again=False)

                products: list[Asset | CsafProduct] = []

                document_results = await asyncio.gather(
                    *[
                        api_instance.documents_id_get(document["id"])
                        for document in api_response.documents
                    ]
                )
                logger.info(f"Fetched {len(document_results)} documents")

                with concurrent.futures.ProcessPoolExecutor() as pool:
                    loop = asyncio.get_event_loop()
                    product_lists = await asyncio.gather(
                        *[
                            loop.run_in_executor(
                                pool,
                                process_document,
                                document,
                                response,
                                self.origin_uri,
                            )
                            for document, response in zip(
                                api_response.documents, document_results
                            )
                        ]
                    )
                    for product_list in product_lists:
                        products.extend(product_list)

                logger.info("Searching for duplicates")
                existing_products = {
                    (
                        prod.origin_info.get("product_name_id"),
                        prod.origin_info.get("path"),
                    ): prod
                    # Todo: Make this faster and use chunking for large amounts of products
                    for prod in await fetcher_view.get_existing(
                        CsafProduct,
                        CsafProduct.origin_info["product_name_id"].astext.in_(
                            [p.origin_info["product_name_id"] for p in products]
                        ),
                    )
                }
                logger.debug(f"Found {len(existing_products)} duplicates")

                for i, prod in enumerate(products):
                    if existing := existing_products.get(
                        (prod.origin_info["product_name_id"], prod.origin_info["path"]),
                        None,
                    ):
                        existing.origin_info.update(prod.origin_info)
                        if existing.product:
                            _update_product_fields(existing.product, prod.product)
                        else:
                            existing.product = prod.product
                        products[i] = existing

                self.__offset += self.__limit
                if products:
                    logger.info(f"Fetched {len(products)} products")
                    return FetchDataResult(again=True, data=products)

            except Exception as e:
                raise Exception(
                    f"Exception when calling DefaultApi->documents_get:\n\n{e}"
                )

        return FetchDataResult(again=False)

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

    def _create_api_config(
        self, origin_uri: str, token: str
    ) -> isduba_api_client.Configuration:
        """Build API configuration for the isduba API client."""
        api_url = f"{origin_uri}/api"
        configuration = isduba_api_client.Configuration(
            host=api_url,
            api_key={"bearerAuth": token},
            api_key_prefix={"bearerAuth": "Bearer"},
            debug=True,
        )
        configuration.verify_ssl = self.config.DataSource.Plugin.verify_ssl

        return configuration

    async def cleanup_data(
        self, data_to_check: List[Asset | CsafProduct]
    ) -> List[CleanUpDecision]:
        return []

    @property
    def origin_uri(self):
        return self.config.DataSource.Plugin.url


def process_document(
    document: dict, response: Any, origin_uri: str
) -> List[CsafProduct]:
    doc_id = document["id"]
    path = f"/api/documents/{doc_id}"

    assert isinstance(response, dict)
    logger.debug(f"Processing document: {path}")
    product_tree = get_csaf_product_tree(
        origin_uri,
        path,
        response["document"],
        response["product_tree"],
    )

    if product_tree:
        return convert_into_database_format(product_tree)
    else:
        return []
