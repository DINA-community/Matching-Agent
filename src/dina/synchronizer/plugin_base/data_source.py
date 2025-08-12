from abc import abstractmethod, ABC
from typing import Any, Dict, List, Union

from dina.cachedb.model import Asset, CsafProductRelationship, CsafProductTree


class DataSourcePlugin(ABC):
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    @abstractmethod
    async def fetch_data(self) -> List[Union[Asset, CsafProductTree, CsafProductRelationship]]: ...

    def debug_info(self) -> str:
        """Return debug information about the plugin."""
        return f"plugin {self.config['DataSource']['plugin_name']} for endpoint {self.endpoint_info()}"

    @abstractmethod
    def endpoint_info(self) -> str:
        """Return endpoint information about the plugin."""
        ...
