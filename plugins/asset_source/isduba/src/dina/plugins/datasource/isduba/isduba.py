# import asyncio
from typing import List, Union

from dina.cachedb.model import CsafDocument, Asset
from dina.common import logging
from dina.synchronizer.base import DataSourcePlugin

import httpx
import isduba_api_client


logger = logging.get_logger(__name__)


class IsdubaDataSource(DataSourcePlugin):
    def __init__(self, config):
        super().__init__(config)
        # Extract configuration values
        try:
            plugin_config = self.config["DataSource"]["ISDuBA"]
            self.username = plugin_config["username"]
            self.password = plugin_config["password"]
            self.verify_ssl = plugin_config["verify_ssl"]
            self.url = plugin_config["url"]
            # Add other configuration parameters as needed
        except KeyError:
            raise KeyError("Missing required configuration parameter")

    def endpoint_info(self) -> str:
        """Return information about the data source endpoint."""
        return self.url

    async def fetch_data(self) -> List[Union[Asset, CsafDocument]]:
        """Fetch data from the data source and return it as a list of Assets or CsafDocuments."""
        # Implement your data fetching logic here
        # This is where you would connect to your data source and retrieve data

        # Fetch data from ISDuBA
        logger.trace("IsdubaDataSource: Fetching data from ISDuBA")
        # await asyncio.sleep(1)

        token_url = "{}:8081/realms/isduba/protocol/openid-connect/token".format(
            self.url
        )
        logger.trace("Fetching bearer token from {}".format(token_url))
        token = (
            httpx.post(
                token_url,
                data={
                    "grant_type": "password",
                    "client_id": "auth",
                    "username": self.username,
                    "password": self.password,
                },
                verify=self.verify_ssl,
            )
            .json()
            .get("access_token")
        )

        api_url = "{}/api".format(self.url)
        logger.trace("Creating client for API at {}".format(api_url))
        # Defining the host is optional and defaults to /api
        # See configuration.py for a list of all supported configuration parameters.
        configuration = isduba_api_client.Configuration(
            host=api_url,
            api_key={"bearerAuth": token},
            api_key_prefix={"bearerAuth": "Bearer"},
        )
        configuration.verify_ssl = self.verify_ssl

        # Enter a context with an instance of the API client
        with isduba_api_client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = isduba_api_client.DefaultApi(api_client)

            logger.trace("Requesting application information...")
            # Returns application information.
            try:
                api_response = api_instance.about_get()
                logger.trace("The response of DefaultApi->about_get:")
                logger.trace(api_response)
            except Exception as e:
                raise Exception(
                    "Exception when calling DefaultApi->about_get:\n\n%s" % e
                )

            # Return documents.
            try:
                # Return a list of documents
                logger.trace("Requesting list of documents...")
                advisories = None  # bool | Return advisories (optional)
                query = None  # str | Document query (optional)
                columns = None  # str | Columns (optional)
                orders = None  # str | Ordering (optional)
                count = None  # bool | Enable counting (optional)
                limit = 1  # int | Maximum documents (optional)
                offset = None  # int | Offset (optional)
                api_response = api_instance.documents_get(
                    advisories=advisories,
                    query=query,
                    columns=columns,
                    orders=orders,
                    count=count,
                    limit=limit,
                    offset=offset,
                )
                logger.trace("The response of DefaultApi->documents_get:")
                logger.trace(api_response)

                # Returns the document with given id.
                logger.trace("Requesting document with first ID...")
                id = api_response.documents[0]["id"]
                api_response = api_instance.documents_id_get(id)
                logger.trace("The response of DefaultApi->documents_id_get:")
                logger.trace(api_response)

            except Exception as e:
                raise Exception(
                    "Exception when calling DefaultApi->documents_get:\n\n%s" % e
                )

        # Return a list of Asset or CsafDocument objects
        return []
