from abc import abstractmethod, ABC
from typing import Any, List, Union

from pydantic import BaseModel

from dina.cachedb.model import Asset, CsafDocument


class DataSourceConfig(BaseModel):
    plugin_name: str
    timeout_seconds: int
    update_interval: int
    Plugin: Any


class DataSourcePlugin(ABC):
    class Config(BaseModel):
        DataSource: DataSourceConfig

    def __init__(self, config: Config):
        self.config = config
        self.origin_module = self.__module__

    @abstractmethod
    async def fetch_data(self) -> List[Union[Asset, CsafDocument]]: ...

    @abstractmethod
    async def cleanup_data(self, data_to_check: List[Any]): ...

    def debug_info(self) -> str:
        """Return debug information about the plugin."""
        return f"plugin {self.config.DataSource.plugin_name} for endpoint {self.endpoint_info()}"

    @abstractmethod
    def endpoint_info(self) -> str:
        """Return endpoint information about the plugin."""
        ...
