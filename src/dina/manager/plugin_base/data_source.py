from abc import abstractmethod, ABC
from typing import Any, Dict, List, Union

from dina.cachedb.model import Asset, CsafDocument


class DataSourcePlugin(ABC):
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    @abstractmethod
    async def fetch_data(self) -> List[Union[Asset, CsafDocument]]: ...

    def debug_info(self) -> str:
        """Return debug information about the plugin."""
        return f"{self.config.get('plugin_type')} plugin {self.config.get('plugin_name')} for endpoint {self.endpoint_info()}"

    @abstractmethod
    def endpoint_info(self) -> str:
        """Return endpoint information about the plugin."""
        ...
