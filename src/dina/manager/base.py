"""
Base classes for manager daemons.

This module provides the base infrastructure for manager daemons
that fetch data, transform it, and preprocess it using plugins.
"""

from __future__ import annotations

import asyncio
import logging
import tomllib
from abc import ABC
from importlib.metadata import entry_points
from pathlib import Path
from typing import List, Union

from dina.cachedb.database import CacheDB
from dina.cachedb.model import Asset, CsafDocument
from dina.manager.plugin_base.data_source import DataSourcePlugin

# Set up logging
logger = logging.getLogger(__name__)


class BaseManager(ABC):
    def __init__(self, cache_db: CacheDB, data_source_plugin_configs: Path):
        """Initialize the BaseManager."""
        self.cache_db: CacheDB = cache_db
        self.pending_data: List[Union[Asset, CsafDocument]] = []
        self.preprocessed_data: List[Union[Asset, CsafDocument]] = []

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
        plugin_configs = plugin_configs.resolve()
        if not plugin_configs.exists() or not plugin_configs.is_dir():
            raise FileNotFoundError(
                f"Plugin configuration directory not found: {plugin_configs}"
            )

        plugins: List[DataSourcePlugin] = []

        installed_plugins = entry_points(group="dina.plugins.datasource")
        logger.info(f"Found {len(installed_plugins)} installed plugins:")
        for installed_plugin in installed_plugins:
            logger.info(f" - {installed_plugin.group}.{installed_plugin.name}")

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
                    epoints = installed_plugins.select(name=plugin_name)
                    if not epoints:
                        raise ModuleNotFoundError(
                            f"No module called {plugin_name} found"
                        )
                    if len(epoints) > 1:
                        raise ValueError(
                            f"Too many entrypoints for plugin {plugin_name} found: {epoints}"
                        )
                    loaded_plugin = [plugin.load() for plugin in epoints][0]
                except KeyError as e:
                    logger.error(f"Failed to import plugin module '{plugin_name}': {e}")
                    continue

                # Initialize the plugin with the configuration
                plugin_instance = loaded_plugin(config=config_data)
                plugins.append(plugin_instance)

                logger.info(
                    f"Successfully loaded plugin: {plugin_name} with config: {config_file}"
                )

            except Exception as e:
                logger.error(f"Error loading plugin from {config_file}: {e}")

        return plugins

    async def setup(self):
        await self.cache_db.connect()

    async def run(self):
        """Run the manager."""
        async with asyncio.TaskGroup() as tg:
            logger.info(f"Starting {len(self.data_sources)} data fetching tasks:")
            for source in self.data_sources:
                logger.info(f"Creating task for {source.debug_info()}")
                tg.create_task(self.fetch_data_task(source))
            logger.info("Starting preprocessing task")
            tg.create_task(self.preprocess_data_task())
            logger.info("Starting storing task")
            tg.create_task(self.store_data_task())

    async def fetch_data_task(self, source: DataSourcePlugin):
        """Perform a collection of data from a single data source."""
        while True:
            self.pending_data.extend(await source.fetch_data())

    async def preprocess_data_task(self):
        while True:
            if self.pending_data:
                logger.info(f"Preprocessing {len(self.pending_data)} items")
                # TODO: Pass data to preprocessing plugin instead of doing no-op
                self.preprocessed_data.extend(self.pending_data)
                self.pending_data.clear()
            else:
                await asyncio.sleep(0.1)

    async def store_data_task(self):
        """Store the preprocessed data."""
        while True:
            if self.preprocessed_data:
                logger.info(f"Storing {len(self.preprocessed_data)} items in cacheDB")
                self.preprocessed_data.clear()
                # TODO: Re-enable once the rest is stable enough
                # await self.cache_db.store(data)
            else:
                await asyncio.sleep(0.1)

    async def cleanup(self):
        await self.cache_db.disconnect()
