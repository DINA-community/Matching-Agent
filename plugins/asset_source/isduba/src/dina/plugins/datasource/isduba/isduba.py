import asyncio
import concurrent.futures
from datetime import datetime, timezone
from typing import Any, List

import httpx
from pydantic import BaseModel, HttpUrl
from sqlalchemy import String, and_, cast

from dina.cachedb.database import MappedRelationship
from dina.cachedb.fetcher_view import FetcherView
from dina.cachedb.model import Asset, CsafProduct, Match
from dina.common import log
from dina.plugins.datasource.isduba.connector import (
    get_csaf_product_tree,
    get_relationships,
)
from dina.plugins.datasource.isduba.converter import (
    _update_product_fields,
    convert_into_database_format,
)
from dina.plugins.datasource.isduba.generated import isduba_api_client
from dina.synchronizer.base import DataSourcePlugin
from dina.synchronizer.plugin_base.data_source import (
    CleanUpDecision,
    FetchProductsResult,
    FetchRelationshipsResult,
    Relationship,
)

logger = log.get_logger(__name__)


class IsdubaDataSource(DataSourcePlugin):
    class Config(BaseModel):
        username: str
        password: str
        verify_ssl: bool
        url: HttpUrl
        keycloak_url: HttpUrl
        keycloak_realm: str

    def __init__(self, config):
        config.DataSource.Plugin = IsdubaDataSource.Config.model_validate(
            config.DataSource.Plugin
        )
        self.__limit = 500
        self.__offset = 0
        super().__init__(config)
        log.get_logger("httpx").setLevel(log.WARNING)
        log.get_logger("httpcore").setLevel(log.WARNING)

    def endpoint_info(self) -> str:
        """Return information about the data source endpoint."""
        return self.config.DataSource.Plugin.url

    async def fetch_products(self, fetcher_view: FetcherView) -> FetchProductsResult:
        """Fetch data from the data source and return it as a list of Assets or CsafDocuments."""
        token = await self._get_token(self.config.DataSource.Plugin.keycloak_url)
        configuration = self._create_api_config(self.origin_uri, token)
        async with isduba_api_client.ApiClient(configuration) as api_client:
            api_instance = isduba_api_client.DefaultApi(api_client)
            try:
                last_run = (await fetcher_view.last_run()).astimezone(tz=timezone.utc)

                query = f"$current_release_date {last_run.isoformat()} timestamp >= $current_release_date {datetime.now(timezone.utc).isoformat()} timestamp <="

                api_response = await api_instance.documents_get(
                    limit=self.__limit,
                    offset=self.__offset,
                    query=query,
                    orders="-critical",
                )

                if not api_response.documents:
                    # If there are no more results, we reset the offset to zero and return an empty list
                    # The fetcher will be called for the next syncing interval and can start from offset 0
                    self.__offset = 0
                    return FetchProductsResult(again=False)

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
                # Get all product name IDs from the new products
                product_name_ids = [p.origin_info["product_name_id"] for p in products]
                paths = [p.origin_info["path"] for p in products]

                # Initialize dictionary to store existing products
                existing_products = {}

                # Process in batches
                batch_size = 1000
                batches = []
                for i in range(0, len(product_name_ids), batch_size):
                    logger.debug(
                        f"Searching duplicates for batch {i} to {i + batch_size}"
                    )
                    product_id_batch = product_name_ids[i : i + batch_size]
                    path_batch = paths[i : i + batch_size]
                    batches.append(
                        await fetcher_view.get_existing(
                            CsafProduct,
                            and_(
                                CsafProduct.origin_info["product_name_id"].astext.in_(
                                    product_id_batch
                                ),
                                CsafProduct.origin_info["path"].astext.in_(path_batch),
                            ),
                        )
                    )

                for batch in batches:
                    # Add batch results to the existing_products dictionary
                    existing_products.update(
                        {
                            (
                                prod.origin_info.get("product_name_id"),
                                prod.origin_info.get("path"),
                            ): prod
                            for prod in batch
                        }
                    )

                logger.info(f"Found {len(existing_products)} duplicates")

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
                    products[i].uri = self.build_resource_uri(products[i].origin_info)

                self.__offset += self.__limit
                if products:
                    logger.info(f"Fetched {len(products)} products")
                    return FetchProductsResult(again=True, data=products)

            except Exception as e:
                raise Exception(
                    f"Exception when calling DefaultApi->documents_get:\n\n{e}"
                )

        return FetchProductsResult(again=False)

    async def _get_token(self, keycloak_uri: HttpUrl) -> str:
        """Retrieve an access token via Keycloak."""
        token_url = f"{keycloak_uri.unicode_string()}/realms/{self.config.DataSource.Plugin.keycloak_realm}/protocol/openid-connect/token"
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
        api_url = f"{origin_uri}api"
        configuration = isduba_api_client.Configuration(
            host=api_url,
            api_key={"bearerAuth": token},
            api_key_prefix={"bearerAuth": "Bearer"},
            debug=True,
        )
        configuration.verify_ssl = self.config.DataSource.Plugin.verify_ssl

        return configuration

    async def fetch_relationships(
        self, fetcher_view: FetcherView
    ) -> FetchRelationshipsResult:
        last_run = (await fetcher_view.last_run()).astimezone(tz=timezone.utc)

        existing_products = await fetcher_view.get_existing(
            CsafProduct, CsafProduct.last_update > last_run.timestamp()
        )

        if not existing_products:
            return FetchRelationshipsResult(again=False)

        token = await self._get_token(self.config.DataSource.Plugin.keycloak_url)
        config = self._create_api_config(self.origin_uri, token)

        async with isduba_api_client.ApiClient(config) as api_client:
            api = isduba_api_client.DefaultApi(api_client)

            for prod in existing_products:
                try:
                    doc_id_str = prod.origin_info["path"]
                    doc_id = int(doc_id_str.removeprefix("/api/documents/"))

                    response = await api.documents_id_get(doc_id)

                    product_tree = response.get("product_tree")

                    if not product_tree:
                        continue

                    relationships: list[Relationship] = []

                    existing_relationships: List[Relationship] = get_relationships(
                        product_tree
                    )

                    for rel in existing_relationships:
                        product_ref = await fetcher_view.get_existing(
                            CsafProduct,
                            and_(
                                cast(
                                    CsafProduct.origin_info["product_name_id"].astext,
                                    String,
                                )
                                == str(rel.product_reference),
                                cast(CsafProduct.origin_info["path"].astext, String)
                                == doc_id_str,
                            ),
                        )
                        relates_to_ref = await fetcher_view.get_existing(
                            CsafProduct,
                            and_(
                                cast(
                                    CsafProduct.origin_info["product_name_id"].astext,
                                    String,
                                )
                                == str(rel.relates_to_product_reference),
                                cast(CsafProduct.origin_info["path"].astext, String)
                                == doc_id_str,
                            ),
                        )

                        if product_ref and relates_to_ref:
                            relationships.append(
                                Relationship(
                                    parent=product_ref[0],
                                    child=relates_to_ref[0],
                                    ty=CsafProduct,
                                )
                            )

                    return FetchRelationshipsResult(again=False, data=relationships)

                except Exception as e:
                    logger.error(f"Error fetching relationships for {prod.id}: {e}")

        return FetchRelationshipsResult(again=False)

    async def map_relationships(
        self, fetcher_view: FetcherView, relations: List[Relationship]
    ) -> List[MappedRelationship]:
        logger.info(f"Storing {len(relations)} relationships between CSAF products")
        return [
            MappedRelationship(parent=rel.parent.id, child=rel.child.id, ty=CsafProduct)
            for rel in relations
        ]

    async def notify_new_matches(self, new_matches: List[Match]):
        # There is no notification mechanism for isduba.
        pass

    async def cleanup_products(
        self, data_to_check: List[Asset | CsafProduct]
    ) -> List[CleanUpDecision]:
        logger.debug(f"Cleanup data: {data_to_check}")

        if not data_to_check:
            return []

        token = await self._get_token(self.config.DataSource.Plugin.keycloak_url)
        configuration = self._create_api_config(self.origin_uri, token)

        async with isduba_api_client.ApiClient(configuration) as api_client:
            api_instance = isduba_api_client.DefaultApi(api_client)

            results = []

            for d in data_to_check:
                try:
                    doc_id = int(d.origin_info["path"].removeprefix("/api/documents/"))
                    document_result = await self._safe_documents_id_get(
                        api_instance, doc_id
                    )

                    results.append(
                        CleanUpDecision(
                            can_delete=document_result is None,
                            id=d.id,
                            ty=CsafProduct,
                        )
                    )
                except Exception as e:
                    logger.error(f"Error checking CSAF product {d.id}: {e}")
                    raise

        return results

    async def _safe_documents_id_get(self, api_instance, doc_id: int):
        try:
            return await api_instance.documents_id_get(doc_id)
        except isduba_api_client.exceptions.UnauthorizedException:
            token = await self._get_token(self.config.DataSource.Plugin.keycloak_url)
            configuration = self._create_api_config(self.origin_uri, token)
            async with isduba_api_client.ApiClient(configuration) as new_client:
                new_instance = isduba_api_client.DefaultApi(new_client)
                return await new_instance.documents_id_get(doc_id)

    async def cleanup_relationships(
        self, relationships_to_check: List[MappedRelationship]
    ) -> List[MappedRelationship]:
        return relationships_to_check

    @property
    def origin_uri(self) -> HttpUrl:
        return self.config.DataSource.Plugin.url

    def build_resource_path(self, origin_info: dict[str, Any]) -> str:
        path = origin_info.get("path")
        return str(path) if path else ""


def process_document(
    document: dict, response: Any, origin_uri: str
) -> List[CsafProduct]:
    doc_id = document["id"]
    path = f"/api/documents/{doc_id}"

    assert isinstance(response, dict)
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
