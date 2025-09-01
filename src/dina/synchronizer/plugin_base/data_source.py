from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, List, Type

from pydantic import BaseModel

from dina.cachedb.fetcher_view import FetcherView
from dina.cachedb.model import Asset, CsafProduct


class DataSourceConfig(BaseModel):
    plugin_name: str
    timeout_seconds: int
    update_interval: int
    Plugin: Any = object()


@dataclass
class CleanUpDecision:
    can_delete: bool
    id: int
    ty: Type[Asset | CsafProduct]


@dataclass
class FetchDataResult:
    """Result object containing fetched data and fetch continuation flag.

    Attributes:
        data: List of fetched Asset or CsafProduct objects from the data source
        again: Boolean flag indicating if another fetch should be performed immediately
            (True) or wait for the next scheduled interval (False)
    """

    again: bool
    data: List[Asset | CsafProduct] = field(default_factory=list)


class DataSourcePlugin(ABC):
    """Base class for data source plugins that fetch and manage data from external sources.

    This abstract class defines the interface that all data source plugins must implement
    to interact with the synchronization system. It provides methods for fetching data,
    cleaning up stale data, and providing debug information about the plugin.
    """

    class Config(BaseModel):
        DataSource: DataSourceConfig

    def __init__(self, config: Config):
        self.config = config

    @abstractmethod
    async def fetch_data(self, fetcher_view: FetcherView) -> FetchDataResult:
        """Fetch data from the external data source.

        This method is responsible for retrieving data from the external source
        and converting it into the internal data model format.

        Args:
            fetcher_view: View object providing access to the current state of cached data.

        Returns:
            List of Asset or CsafProduct objects containing the fetched and converted data.
        """
        ...

    @abstractmethod
    async def cleanup_data(
        self, data_to_check: List[Asset | CsafProduct]
    ) -> List[CleanUpDecision]:
        """Determine which stale data items should be deleted.

        Args:
            data_to_check: List of stale data items to evaluate for cleanup.
                Only includes data items originating from this plugin.

        Returns:
            List of CleanUpDecision objects containing:
                - can_delete: Whether the item should be deleted
                - id: The ID of the data item
                - ty: The type of the data item (Asset or CsafProduct)
        """
        ...

    def debug_info(self) -> str:
        """Return debug information about the plugin."""
        return f"plugin {self.config.DataSource.plugin_name} for endpoint {self.endpoint_info()}"

    @property
    @abstractmethod
    def origin_uri(self):
        """The URI of the data source.

        Returns:
            str: The base URI of the external data source this plugin connects to.
        """
        ...

    @abstractmethod
    def endpoint_info(self) -> str:
        """Return endpoint information about the plugin."""
        ...
