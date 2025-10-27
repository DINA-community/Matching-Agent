from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, List, Type

from pydantic import BaseModel

from dina.cachedb.fetcher_view import FetcherView
from dina.cachedb.model import Asset, CsafProduct, ProductType, Match


class DataSourceConfig(BaseModel):
    plugin_name: str
    publish_matches: bool = False
    Plugin: Any = object()


@dataclass
class CleanUpDecision:
    can_delete: bool
    id: int
    ty: Type[Asset | CsafProduct]


@dataclass
class ProductId:
    id: Any
    product_type: ProductType


@dataclass
class Relationship:
    """
    Represents a relationship between a parent and a child entity along with metadata.

    This class is used for managing relationships between entities such as assets or
    csaf products. It encapsulates the IDs of the parent and child entities, the type of
    the relationship, and whether the relationship can be deleted.

    :ivar parent: The ID of the parent entity.
    :ivar child: The ID of the child entity.
    :ivar ty: The type of relationship, which may involve an Asset or CsafProduct.
    """

    parent: ProductId
    child: ProductId
    ty: Type[Asset | CsafProduct]
    origin_info: dict[str, Any] = field(default_factory=dict)


@dataclass
class MappedRelationship:
    parent: int
    child: int
    ty: Type[Asset | CsafProduct]
    origin_uri: str = ""
    origin_info: dict[str, Any] = field(default_factory=dict)
    can_delete: bool = False


@dataclass
class FetchRelationshipsResult:
    again: bool
    data: List[Relationship] = field(default_factory=list)


@dataclass
class FetchProductsResult:
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
    In addition, the plugin also provides a channel to notify the data source of any new matches
    the matcher found during the matching phase.

    This abstract class defines the interface that all data source plugins must implement
    to interact with the synchronization system. It provides methods for fetching data,
    cleaning up stale data, and providing debug information about the plugin.
    """

    class Config(BaseModel):
        DataSource: DataSourceConfig

    def __init__(self, config: Config):
        self.config = config

    @abstractmethod
    def build_resource_path(self, origin_info: dict[str, Any]) -> str:
        """Return a plugin-specific path component for a given origin_info.

        The returned value should be a path starting with '/', suitable to be
        concatenated to the plugin's origin_uri. If the plugin cannot determine
        a stable path from the provided origin_info, it should return an empty string.
        """

    def build_resource_uri(self, origin_info: dict[str, Any]) -> str:
        """Return a plugin-specific URI for a given origin_info."""
        path = self.build_resource_path(origin_info)
        if self.origin_uri.endswith("/") and path.startswith("/"):
            return self.origin_uri[:-1] + path
        return self.origin_uri + path

    @abstractmethod
    async def fetch_products(self, fetcher_view: FetcherView) -> FetchProductsResult:
        """Fetch products associated with assets or csaf documents from the external data source.

        This method is responsible for retrieving data from the external source
        and converting it into the internal data model format.

        Args:
            fetcher_view: View object providing access to the current state of cached data.

        Returns:
            List of Asset or CsafProduct objects containing the fetched and converted data.
        """
        ...

    @abstractmethod
    async def fetch_relationships(
        self, fetcher_view: FetcherView
    ) -> FetchRelationshipsResult:
        """
        Fetch relationships associated with assets or csaf documents from the external data source.
        """
        ...

    @abstractmethod
    async def map_relationships(
        self, fetcher_view: FetcherView, relations: List[Relationship]
    ) -> List[MappedRelationship]:
        """Maps the plugin-internal ids of the relationships to the core asset or csaf-product ids."""
        ...

    @abstractmethod
    async def cleanup_products(
        self, data_to_check: List[Asset | CsafProduct]
    ) -> List[CleanUpDecision]:
        """Determine which stale products should be deleted.

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

    @abstractmethod
    async def cleanup_relationships(
        self, relationships_to_check: List[MappedRelationship]
    ) -> List[MappedRelationship]:
        """Determine which stale relationships should be deleted."""
        ...

    @abstractmethod
    async def notify_new_matches(self, new_matches: List[Match]):
        """Notify the data source that new matches were found during the matching phase."""
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
