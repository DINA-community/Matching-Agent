"""
Preprocessor plugin base module.

This module defines the abstract base class for preprocessor plugins that transform
Asset and CsafProduct data before it is stored in the cache database. Preprocessors
are executed in a configurable order during the synchronization process and can
modify data items according to custom business logic.

The preprocessor plugin system allows for flexible data transformation pipelines
where multiple preprocessors can be chained together, each contributing a specific
transformation step.
"""

from abc import ABC, abstractmethod
from pathlib import Path
import tomllib
from typing import List, Union

from dina.cachedb.model import Asset, CsafProduct


class PreprocessorPlugin(ABC):
    """Abstract base class for preprocessor plugins.

    Preprocessor plugins transform Asset and CsafProduct objects during the
    synchronization process. They can modify, enrich, or filter data items
    before they are stored in the cache database.

    Plugins are initialized with configuration that can be provided either as
    a TOML file path or as a dictionary. The configuration typically includes
    database field mappings that control how the preprocessor handles different
    types of fields.

    Args:
        config: Configuration for the plugin, either as a Path to a TOML file,
                a dictionary, or None for default (empty) configuration.
        **kwargs: Additional keyword arguments passed to parent classes.

    Attributes:
        config_file: Path to the configuration file if provided, otherwise None.
        config: Loaded configuration dictionary.
        freetext_fields: Mapping of freetext fields from config.
        ordered_fields: Mapping of ordered fields from config.
        other_fields: Mapping of other fields from config.
    """

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

        db = self.config.get("database", {})
        self.freetext_fields = db.get("freetext_fields", {})
        self.ordered_fields = db.get("ordered_fields", {})
        self.other_fields = db.get("other_fields", {})

    @abstractmethod
    async def preprocess(
        self, data: List[Union[Asset, CsafProduct]]
    ) -> List[Union[Asset, CsafProduct]]:
        """Transform a list of data items.

        This method receives a list of Asset or CsafProduct objects and returns
        a transformed list. The transformation can include modifications to existing
        items, filtering, or adding new derived data.

        Implementations should preserve the overall structure and type of the input
        list. The returned list may have a different length than the input if items
        are filtered or duplicated.

        Args:
            data: List of Asset or CsafProduct objects to preprocess.

        Returns:
            List of preprocessed Asset or CsafProduct objects.
        """
        ...

    def load_config(self, path: Path):
        """Load configuration from a TOML file.

        Reads and parses a TOML configuration file from the specified path.

        Args:
            path: Path to the TOML configuration file.

        Returns:
            Dictionary containing the parsed configuration.

        Raises:
            FileNotFoundError: If the configuration file does not exist.
            ValueError: If the TOML file is malformed or cannot be parsed.
        """
        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {path}")
        try:
            with path.open("rb") as f:
                return tomllib.load(f)
        except tomllib.TOMLDecodeError as e:
            raise ValueError(f"Invalid TOML file: {path}\n{e}")
