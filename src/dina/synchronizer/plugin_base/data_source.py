from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, List, Type, Union

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


class DataSourcePlugin(ABC):
    class Config(BaseModel):
        DataSource: DataSourceConfig

    def __init__(self, config: Config):
        self.config = config

    @abstractmethod
    async def fetch_data(
        self, fetcher_view: FetcherView
    ) -> List[Union[Asset, CsafProduct]]: ...

    @abstractmethod
    async def cleanup_data(
        self, data_to_check: List[Asset | CsafProduct]
    ) -> List[CleanUpDecision]:
        """
        This function is called for data marked as stale.
        The plugin needs to decide if the data needs to be cleaned up
        or if its timestamp needs to be refreshed.

        The function returns a list of CleanUpDecision objects.
        The decision must contain the id of the data item and the type
        of the item and a flag whether the item can be deleted.

        Each plugin only receives data for which it is the originator.
        :param data_to_check:
        """
        ...

    def debug_info(self) -> str:
        """Return debug information about the plugin."""
        return f"plugin {self.config.DataSource.plugin_name} for endpoint {self.endpoint_info()}"

    @property
    @abstractmethod
    def origin_uri(self): ...

    @abstractmethod
    def endpoint_info(self) -> str:
        """Return endpoint information about the plugin."""
        ...
