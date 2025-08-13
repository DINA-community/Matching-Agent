from typing import List
from dina.common import logging
from dina.synchronizer.base import DataSourcePlugin
import httpx

import dina.plugins.datasource.isduba.generated.isduba_api_client as isduba_api_client

# from .connector import get_csaf_product_tree
# from .converter import convert_into_database_format
from .datamodels import CsafProductTree

# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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

    async def fetch_data(self) -> List[CsafProductTree]:
        """Fetch data from the data source and return it as a list of Assets or CsafDocuments."""
        # Implement your data fetching logic here
        # This is where you would connect to your data source and retrieve data

        # Fetch data from ISDuBA
        logger.trace("IsdubaDataSource: Fetching data from ISDuBA")

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
        ret = []

        # Enter a context with an instance of the API client
        # with isduba_api_client.ApiClient(configuration) as api_client:
        #     # Create an instance of the API class
        #     api_instance = isduba_api_client.DefaultApi(api_client)

        #     limit = 2
        #     offset = 0

        #     while True:
        #         logger.trace("offset: {}".format(offset))

        #         # Return documents.
        #         try:
        #             # Return a list of documents
        #             logger.trace("Requesting list of documents...")
        #             advisories = None  # bool | Return advisories (optional)
        #             query = None  # str | Document query (optional)
        #             columns = None  # str | Columns (optional)
        #             orders = None  # str | Ordering (optional)
        #             count = None  # bool | Enable counting (optional)
        #             # limit = 10  # int | Maximum documents (optional)
        #             # offset = None  # int | Offset (optional)
        #             api_response = api_instance.documents_get(
        #                 advisories=advisories,
        #                 query=query,
        #                 columns=columns,
        #                 orders=orders,
        #                 count=count,
        #                 limit=limit,
        #                 offset=offset,
        #             )

        #             if not api_response.documents:
        #                 break

        #             for doc in api_response.documents:
        #                 id = doc["id"]
        #                 api_response = api_instance.documents_id_get(id)
        #                 csaf_product_tree = await get_csaf_product_tree(api_response["document"], api_response["product_tree"]["branches"])

        #                 if csaf_product_tree != None:
        #                     tree = await convert_into_database_format(csaf_product_tree)

        #                     for t in tree:
        #                         ret.append(t)

        #             offset += limit

        #             break # TODO: stop the process for csafsync

        #         except Exception as e:
        #             raise Exception(
        #                 "Exception when calling DefaultApi->documents_get:\n\n%s" % e
        #             )

        # Return a list of Asset or CsafDocument objects
        return ret
