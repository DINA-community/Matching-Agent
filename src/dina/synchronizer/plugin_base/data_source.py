"""
Data source plugin base module.

This module defines the abstract base class and supporting data structures for data source
plugins that fetch and synchronize external asset or CSAF product data. Data source plugins
are responsible for retrieving data from external systems, managing relationships between
entities, cleaning up stale data, and optionally receiving notifications about new matches.

The module provides a plugin interface that allows the synchronization system to interact
with various external data sources in a uniform way, regardless of the underlying API or
data format.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, List, Type

from pydantic import BaseModel, HttpUrl

from dina.cachedb.fetcher_view import FetcherView
from dina.cachedb.model import Asset, CsafProduct, ProductType, Match


class DataSourceConfig(BaseModel):
    """Configuration for a data source plugin.

    Args:
        plugin_name: Unique identifier for the plugin instance.
        publish_matches: Whether to send match notifications back to the data source.
        Plugin: Plugin class reference (for dynamic loading).
    """

    plugin_name: str
    publish_matches: bool = False
    Plugin: Any = object()


@dataclass
class CleanUpDecision:
    """Decision about whether a product can be deleted during cleanup.

    Args:
        can_delete: Whether the product should be removed from the cache.
        id: Database ID of the product to potentially delete.
        ty: Type of the product (Asset or CsafProduct class).
    """

    can_delete: bool
    id: int
    ty: Type[Asset | CsafProduct]


@dataclass
class ProductId:
    """Identifier for a product in the plugin's native format.

    This represents a product ID as known to the external data source, before
    mapping to the internal database ID.

    Args:
        id: Plugin-specific identifier (can be string, int, or other type).
        product_type: Category of the product (Software, Device, etc.).
    """

    id: Any
    product_type: ProductType


@dataclass
class Relationship:
    """
    Represents a relationship between a parent and a child entity along with metadata.

    This class is used for managing relationships between entities such as assets or
    csaf products. It encapsulates the IDs of the parent and child entities, the type of
    the relationship, and metadata for tracking the relationship's origin.

    Args:
        parent: The ProductId of the parent entity in plugin-native format.
        child: The ProductId of the child entity in plugin-native format.
        ty: The type of relationship (Asset or CsafProduct class).
        origin_info: Plugin-specific metadata about the relationship source.
    """

    parent: ProductId
    child: ProductId
    ty: Type[Asset | CsafProduct]
    origin_info: dict[str, Any] = field(default_factory=dict)


@dataclass
class MappedRelationship:
    """Relationship between entities using internal database IDs.

    This represents a relationship after the plugin-native IDs have been mapped
    to the internal cache database IDs.

    Args:
        parent: Database ID of the parent entity.
        child: Database ID of the child entity.
        ty: Type of relationship (Asset or CsafProduct class).
        origin_uri: URI identifying the data source of this relationship.
        origin_info: Plugin-specific metadata about the relationship.
        can_delete: Whether this relationship can be removed during cleanup.
    """

    parent: int
    child: int
    ty: Type[Asset | CsafProduct]
    origin_uri: str = ""
    origin_info: dict[str, Any] = field(default_factory=dict)
    can_delete: bool = False


@dataclass
class FetchRelationshipsResult:
    """Result from fetching relationships from the data source.

    Args:
        again: Whether the plugin has more relationships to fetch (pagination).
        data: List of relationships retrieved in this batch.
    """

    again: bool
    data: List[Relationship] = field(default_factory=list)


@dataclass
class FetchProductsResult:
    """Result from fetching products from the data source.

    Args:
        again: Whether the plugin has more products to fetch (pagination).
        data: List of Asset or CsafProduct objects retrieved in this batch.
    """

    again: bool
    data: List[Asset | CsafProduct] = field(default_factory=list)


class DataSourcePlugin(ABC):
    """Base class for data source plugins that fetch and manage data from external sources.

    This abstract class defines the interface that all data source plugins must implement
    to integrate with the synchronization system. Plugins are responsible for:

    - Fetching products and relationships from external data sources
    - Mapping plugin-native identifiers to internal database IDs
    - Determining which stale data should be cleaned up
    - Optionally receiving notifications about new matches
    - Providing URIs and debug information about the data source

    Subclasses should implement all abstract methods to provide the specific logic for
    interacting with their particular external data source.

    Usage:
        Plugins are typically loaded dynamically by the synchronization system based on
        configuration files. The synchronization system will call the plugin methods in
        a specific order during the sync cycle.
    """

    class Config(BaseModel):
        """Configuration model for the plugin.

        Args:
            DataSource: Data source specific configuration.
        """

        DataSource: DataSourceConfig

    def __init__(self, config: Config):
        """Initialize the plugin with configuration.

        Args:
            config: Plugin configuration containing data source settings.
        """
        self.config = config

    @abstractmethod
    def build_resource_path(self, origin_info: dict[str, Any]) -> str:
        """Construct a URL path component for a resource based on its origin metadata.

        The returned path should start with '/' and be suitable for appending to the
        origin_uri to form a complete resource URI. If a stable path cannot be determined
        from the origin_info, return an empty string.

        Args:
            origin_info: Plugin-specific metadata about the resource's origin.

        Returns:
            Path component starting with '/', or empty string if path cannot be determined.
        """

    def build_resource_uri(self, origin_info: dict[str, Any]) -> str:
        """Construct a complete URI for a resource based on its origin metadata.

        Args:
            origin_info: Plugin-specific metadata about the resource's origin.

        Returns:
            Complete URI identifying the resource in the external system.
        """
        path = self.build_resource_path(origin_info).lstrip("/")
        return str(self.origin_uri) + path

    @abstractmethod
    async def fetch_products(self, fetcher_view: FetcherView) -> FetchProductsResult:
        """Fetch a batch of products from the external data source.

        This method retrieves products and converts them to the internal data model.
        For large data sources, fetching can be paginated by returning `again=True`
        to indicate more data is available.

        Args:
            fetcher_view: Provides access to the current cached data for incremental sync.

        Returns:
            FetchProductsResult with fetched products and pagination flag.
        """
        ...

    @abstractmethod
    async def fetch_relationships(
        self, fetcher_view: FetcherView
    ) -> FetchRelationshipsResult:
        """Fetch a batch of relationships from the external data source.

        Relationships define parent-child hierarchies between products. The returned
        relationships use plugin-native IDs which will later be mapped to database IDs.

        Args:
            fetcher_view: Provides access to the current cached data for incremental sync.

        Returns:
            FetchRelationshipsResult with fetched relationships and pagination flag.
        """
        ...

    @abstractmethod
    async def map_relationships(
        self, fetcher_view: FetcherView, relations: List[Relationship]
    ) -> List[MappedRelationship]:
        """Convert plugin-native relationship IDs to internal database IDs.

        This method translates the plugin's native product identifiers to the
        corresponding database IDs used in the cache. Relationships that cannot
        be mapped (e.g., references to non-existent products) should be omitted.

        Args:
            fetcher_view: Provides access to cached data for ID lookup.
            relations: Relationships with plugin-native IDs to map.

        Returns:
            List of relationships with mapped database IDs.
        """
        ...

    @abstractmethod
    async def cleanup_products(
        self, data_to_check: List[Asset | CsafProduct]
    ) -> List[CleanUpDecision]:
        """Determine which stale products should be deleted during cleanup.

        The synchronizer identifies products that haven't been seen in recent sync runs
        as potentially stale. This method allows the plugin to decide whether each
        product should actually be deleted, based on plugin-specific logic.

        Args:
            data_to_check: Stale products from this plugin to evaluate.

        Returns:
            List of cleanup decisions indicating which products can be deleted.
        """
        ...

    @abstractmethod
    async def cleanup_relationships(
        self, relationships_to_check: List[MappedRelationship]
    ) -> List[MappedRelationship]:
        """Determine which stale relationships should be deleted during cleanup.

        Returns the subset of provided relationships that should be removed from the
        cache database.

        Args:
            relationships_to_check: Stale relationships from this plugin to evaluate.

        Returns:
            List of relationships that should be deleted.
        """
        ...

    @abstractmethod
    async def notify_new_matches(self, new_matches: List[Match]):
        """Receive notification of new matches found by the matcher.

        If the plugin's configuration has `publish_matches=True`, this method is called
        when the matcher finds new relationships between assets and CSAF products.
        Plugins can use this to update the external data source or trigger workflows.

        Args:
            new_matches: Newly discovered matches involving this plugin's products.
        """
        ...

    def debug_info(self) -> str:
        """Provide a human-readable description of the plugin for debugging.

        Returns:
            String describing the plugin name and endpoint.
        """
        return f"plugin {self.config.DataSource.plugin_name} for endpoint {self.endpoint_info()}"

    @property
    @abstractmethod
    def origin_uri(self) -> HttpUrl:
        """The base URI of the external data source.

        Returns:
            Base URI used for constructing resource URIs.
        """
        ...

    @abstractmethod
    def endpoint_info(self) -> str:
        """Provide endpoint information about the data source.

        Returns:
            Human-readable description of the data source endpoint.
        """
        ...
