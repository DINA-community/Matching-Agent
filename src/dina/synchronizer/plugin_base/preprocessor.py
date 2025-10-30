from abc import ABC, abstractmethod
from pathlib import Path
import tomllib
from typing import List, Union

from dina.cachedb.model import Asset, CsafProduct


class PreprocessorPlugin(ABC):
    def __init__(self, config=None, **kwargs):
        super().__init__(**kwargs)

        if isinstance(config, Path):
            self.config_file = config
            self.config = self.load_config(config)
        elif isinstance(config, dict):
            self.config_file = None
            self.config = config
        else:
            self.config_file = None
            self.config = {}

        db = self.config.get("database", self.config)
        self.freetext_fields = db.get("freetext_fields", {})
        self.ordered_fields = db.get("ordered_fields", {})
        self.other_fields = db.get("other_fields", {})

    @abstractmethod
    async def preprocess(
        self, data: List[Union[Asset, CsafProduct]]
    ) -> List[Union[Asset, CsafProduct]]:
        """
        Asynchronously preprocess a given list of `data` items. This function takes each element
        in the provided list, processes it, and then returns a new list of processed items.

        :param data: A list of either `Asset` or `CsafDocument` objects that need to be preprocessed.
                      Each object in the list will go through preprocessing based on its type.
        :return: A list of preprocessed items of the same types (`Asset` or `CsafDocument`).
        """
        ...

    def load_config(self, path: Path):
        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {path}")
        try:
            with path.open("rb") as f:
                return tomllib.load(f)
        except tomllib.TOMLDecodeError as e:
            raise ValueError(f"Invalid TOML file: {path}\n{e}")
