"""
Base classes for manager daemons.

This module provides the base infrastructure for manager daemons
that fetch data, transform it, and preprocess it using plugins.
"""

from __future__ import annotations

import asyncio
import logging
import tomllib
from abc import ABC, abstractmethod
from importlib.metadata import entry_points
from pathlib import Path
from typing import Any, Dict, List, Union

from dina.cachedb.database import CacheDB
from dina.cachedb.model import Asset, CsafDocument

# Set up logging
logger = logging.getLogger(__name__)


class BaseManager(ABC):
    def __init__(self, cache_db: CacheDB, data_source_plugin_configs: Path):
        """Initialize the BaseManager."""
        self.cache_db: CacheDB = cache_db

        self.data_sources: List[DataSourcePlugin] = self.load_plugins(
            data_source_plugin_configs
        )

    @staticmethod
    def load_plugins(plugin_configs: Path) -> List[DataSourcePlugin]:
        """
        Load plugins from configuration files in the specified directory.

        Args:
            plugin_configs: Path to a directory containing plugin configuration files in TOML format.

        Returns:
            A list of initialized DataSourcePlugin instances.

        Raises:
            FileNotFoundError: If the plugin_configs path does not exist or is not a directory.
            ImportError: If a plugin module cannot be imported.
            KeyError: If a plugin configuration is missing required fields.
        """
        if not plugin_configs.exists() or not plugin_configs.is_dir():
            raise FileNotFoundError(
                f"Plugin configuration directory not found: {plugin_configs}"
            )

        plugins: List[DataSourcePlugin] = []

        # Scan the directory for TOML files
        for config_file in plugin_configs.glob("*.toml"):
            try:
                # Parse the TOML file
                with open(config_file, "rb") as f:
                    config_data = tomllib.load(f)

                data_source = config_data["DataSource"]
                # Extract plugin information
                plugin_name = data_source.get("plugin_name")

                if not plugin_name:
                    logger.error(
                        f"Missing required fields in plugin configuration: {config_file}"
                    )
                    continue

                # Import the plugin module
                try:
                    loaded_plugins = [
                        plugin.load()
                        for plugin in entry_points(
                            group="dina.plugins", name="datasource"
                        )
                    ]
                    assert len(loaded_plugins) == 1
                    loaded_plugin = loaded_plugins[0]
                except KeyError as e:
                    logger.error(f"Failed to import plugin module '{plugin_name}': {e}")
                    continue

                # Initialize the plugin with the configuration
                plugin_instance = loaded_plugin(config=config_data)
                plugins.append(plugin_instance)

                logger.info(f"Successfully loaded plugin: {plugin_name}")

            except Exception as e:
                logger.error(f"Error loading plugin from {config_file}: {e}")

        return plugins

    async def setup(self):
        await self.cache_db.connect()

    async def run(self):
        """Run the manager."""
        async with asyncio.TaskGroup() as tg:
            logger.info(f"Starting {len(self.data_sources)} data collection tasks:")
            for source in self.data_sources:
                logger.info(f"Creating task for {source.debug_info()}")
                tg.create_task(self.collection_loop(source))

    async def collection_loop(self, source: DataSourcePlugin):
        """Perform a collection of data from a single data source."""
        while True:
            data = await source.fetch_data()
            data = await self.preprocess_data(data)
            await self.store_data(data)

    async def preprocess_data(
        self, data: List[Union[Asset, CsafDocument]]
    ) -> List[Union[Asset, CsafDocument]]:
        """Preprocess the transformed data."""
        return data

    async def store_data(self, data: List[Union[Asset, CsafDocument]]):
        """Store the preprocessed data."""
        logger.info(f"Storing {len(data)} items in cacheDB")
        # TODO: Re-enable once the rest is stable enough
        # await self.cache_db.store(data)

    async def cleanup(self):
        await self.cache_db.disconnect()


class DataSourcePlugin(ABC):
    def __init__(self, config: Dict[str, Any]):
        self.config = config

    @abstractmethod
    async def fetch_data(self): ...

    def debug_info(self) -> str:
        """Return debug information about the plugin."""
        return f"{self.config.get('plugin_type')} plugin {self.config.get('plugin_name')} for endpoint {self.endpoint_info()}"

    @abstractmethod
    def endpoint_info(self) -> str:
        """Return endpoint information about the plugin."""
        ...
