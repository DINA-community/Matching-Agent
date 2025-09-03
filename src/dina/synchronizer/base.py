"""
Base classes for manager daemons.

This module provides the base infrastructure for manager daemons
that fetch data, transform it, and preprocess it using plugins.
"""

from __future__ import annotations

import asyncio
import datetime
import logging
import time
import tomllib
import traceback
from abc import ABC
from collections import defaultdict
from importlib.metadata import EntryPoints, entry_points
from pathlib import Path
from typing import Dict, List, Optional, Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from dina.cachedb.database import CacheDB
from dina.cachedb.fetcher_view import FetcherView
from dina.cachedb.model import Asset, CsafProduct
from dina.synchronizer.plugin_base.data_source import DataSourcePlugin, Relationship
from dina.synchronizer.plugin_base.preprocessor import PreprocessorPlugin

# Set up logging
logger = logging.getLogger(__name__)

type TomlEntry = (
    dict[str, TomlEntry] | list[TomlEntry] | str | int | float | bool | None
)


class ApiConfig(BaseModel):
    host: str
    port: int


class SynchronizerSectionConfig(BaseModel):
    sync_interval: int
    preprocessor_plugins: List[str]
    Api: ApiConfig


class SynchronizerConfig(BaseModel):
    Assetsync: Optional[dict] = None
    Synchronizer: SynchronizerSectionConfig
    Cachedb: CacheDB.Config


class PluginLoadError(Exception):
    pass


class BaseSynchronizer(ABC):
    starttime = 0

    def __init__(
        self, cache_db: CacheDB, data_source_plugin_configs: Path, config_file: Path
    ):
        """Initialize the BaseManager.

        Args:
            cache_db: The cache database to use.
            data_source_plugin_configs: Path to a directory containing data source plugin configuration files.
            config_file: Path to the manager configuration file (e.g., assetman.toml).
        """
        self.__last_synchronization: Optional[float] = None
        self.cache_db: CacheDB = cache_db
        self.pending_products: List[Asset | CsafProduct] = []
        self.pending_relationships: Dict[str, List[Relationship]] = defaultdict(list)
        self.preprocessed_data: List[Asset | CsafProduct] = []
        self.config_file: Path = config_file
        self.config: SynchronizerConfig = self.load_config(config_file)

        self.data_sources: Dict[str, DataSourcePlugin] = self.__load_datasource_plugins(
            data_source_plugin_configs
        )
        self.preprocessor_plugins = self.__load_preprocessor_plugins(
            self.config.Synchronizer.preprocessor_plugins
        )

    @staticmethod
    def get_installed_plugins(group: str) -> EntryPoints:
        installed_plugins = entry_points(group=group)
        logger.debug(f"Found {len(installed_plugins)} installed plugins:")
        for installed_plugin in installed_plugins:
            logger.debug(f" - {installed_plugin.group}.{installed_plugin.name}")
        return installed_plugins

    @staticmethod
    def _load_plugin_from_entrypoint(
        plugin_name: str,
        entry_points_group: str,
        config_data: DataSourcePlugin.Config | None,
    ) -> Union[DataSourcePlugin, PreprocessorPlugin]:
        """
        Load a single plugin from entry points.

        Args:
            plugin_name: Name of the plugin to load
            entry_points_group: Entry points group to search in
            config_data: Configuration data for the plugin

        Returns:
            Loaded plugin instance or None if loading failed
        """
        installed_plugins = BaseSynchronizer.get_installed_plugins(entry_points_group)

        try:
            epoints = installed_plugins.select(name=plugin_name)
            if not epoints:
                raise PluginLoadError(f"No module called {plugin_name} found")

            if len(epoints) > 1:
                raise PluginLoadError(
                    f"Too many entrypoints for plugin {plugin_name} found: {epoints}"
                )

            loaded_plugin = [plugin.load() for plugin in epoints][0]

            # Initialize plugin with or without config
            if config_data:
                plugin_instance = loaded_plugin(config=config_data)
            else:
                plugin_instance = loaded_plugin()

            logger.info(f"Successfully loaded plugin: {plugin_name}")
            return plugin_instance

        except Exception as e:
            raise PluginLoadError(f"Error loading plugin {plugin_name}: {e}")

    @staticmethod
    def load_config(config_file: Path) -> SynchronizerConfig:
        if not config_file.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_file}")

        with open(config_file, "rb") as f:
            return SynchronizerConfig.model_validate(tomllib.load(f))

    @staticmethod
    def __load_datasource_plugins(plugin_configs: Path) -> Dict[str, DataSourcePlugin]:
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

        plugins: Dict[str, DataSourcePlugin] = {}

        # Scan the directory for TOML files
        for config_file in plugin_configs.glob("*.toml"):
            try:
                # Parse the TOML file
                with open(config_file, "rb") as f:
                    config = DataSourcePlugin.Config.model_validate(tomllib.load(f))
                # Extract plugin information
                plugin_name = config.DataSource.plugin_name
                if not plugin_name:
                    logger.error(
                        f"Missing required fields in plugin configuration: {config_file}"
                    )
                    continue

                plugin_instance = BaseSynchronizer._load_plugin_from_entrypoint(
                    plugin_name, "dina.plugins.datasource", config
                )
                if isinstance(plugin_instance, PreprocessorPlugin):
                    raise ValueError(
                        f"Plugin {plugin_name} is a preprocessor plugin, not a data source plugin"
                    )
                else:
                    if plugin_instance.origin_uri in plugins:
                        raise PluginLoadError(
                            "Found duplicate origins for plugins. It is not allowed to synchronize with the same api endpoint twice"
                        )
                    plugins[plugin_instance.origin_uri] = plugin_instance

                logger.info(
                    f"Successfully loaded plugin: {plugin_name} with config: {config_file}"
                )

            except Exception as e:
                logger.error(f"Error loading plugin from {config_file}: {e}")
                raise e

        return plugins

    @staticmethod
    def __load_preprocessor_plugins(
        preprocessor_plugin_names: List[str],
    ) -> List[PreprocessorPlugin]:
        """
        Load preprocessor plugins specified in the configuration file.
        Raises:
            KeyError: If the configuration file is missing required fields.
        """
        preprocessor_plugins: List[PreprocessorPlugin] = []
        try:
            if not preprocessor_plugin_names:
                logger.warning("No preprocessor plugins specified in configuration")
                raise KeyError("Missing preprocessor_plugins in configuration")

            for plugin_name in preprocessor_plugin_names:
                plugin_instance = BaseSynchronizer._load_plugin_from_entrypoint(
                    plugin_name, "dina.plugins.preprocessing", None
                )

                if plugin_instance and isinstance(plugin_instance, PreprocessorPlugin):
                    preprocessor_plugins.append(plugin_instance)
                else:
                    raise ValueError(
                        f"Plugin {plugin_name} is not a preprocessor plugin"
                    )

        except Exception as e:
            logger.error(f"Error loading preprocessor plugins: {e}")
            raise
        return preprocessor_plugins

    async def setup(self):
        await self.cache_db.connect(self.config.Cachedb)

    async def run(self):
        """Run the manager."""
        try:
            async with asyncio.TaskGroup() as tg:
                tg.create_task(self.__api_client())
                logger.info(f"Starting {len(self.data_sources)} data fetching tasks:")
                for source in self.data_sources.values():
                    logger.info(f"Creating task for {source.debug_info()}")
                    tg.create_task(self.fetch_data_task(source))
                    tg.create_task(self.cleanup_task(source))
                logger.info("Starting preprocessing task")
                tg.create_task(self.preprocess_data_task())
                logger.info("Starting storing task")
                tg.create_task(self.store_data_task())
        except* Exception as eg:
            for e in eg.exceptions:
                logger.error("TaskGroup exception:", exc_info=e)

    async def fetch_data_task(self, source: DataSourcePlugin):
        while True:
            if (
                self.__last_synchronization is None
                or self.__last_synchronization + self.config.Synchronizer.sync_interval
                < time.time()
            ):
                try:
                    fetcher_view = self.cache_db.fetcher_view(source.origin_uri)
                    await self.fetch_products(fetcher_view, source)
                    await self.fetch_relationships(fetcher_view, source)
                    await fetcher_view.set_last_run(datetime.datetime.now())
                except Exception as e:
                    logger.error(f"Error fetching data from {source.debug_info()}: {e}")
                    print(traceback.format_exc())

                self.__last_synchronization = time.time()
            else:
                await asyncio.sleep(1)

    async def fetch_products(self, fetcher_view: FetcherView, source: DataSourcePlugin):
        again = True
        while again:
            logger.debug(f"Fetching data from {source.debug_info()}")
            result = await source.fetch_products(fetcher_view)
            for datapoint in result.data:
                datapoint.origin_uri = source.origin_uri
                self.pending_products.append(datapoint)
            again = result.again

    async def fetch_relationships(
        self, fetcher_view: FetcherView, source: DataSourcePlugin
    ):
        again = True
        while again:
            logger.debug(f"Fetching relationships from {source.debug_info()}")
            result = await source.fetch_relationships(fetcher_view)
            self.pending_relationships[source.origin_uri].extend(result.data)
            again = result.again

    async def preprocess_data_task(self):
        """Process data using the loaded preprocessor plugins."""
        assert self.preprocessor_plugins, "No preprocessor plugins loaded"
        while True:
            if self.pending_products:
                logger.info(f"Preprocessing {len(self.pending_products)} items")

                # Process data through each preprocessor plugin in sequence
                processed_data = self.pending_products
                for plugin in self.preprocessor_plugins:
                    logger.info(
                        f"Applying preprocessor plugin: {plugin.__class__.__name__}"
                    )
                    processed_data = await plugin.preprocess(processed_data)

                self.preprocessed_data.extend(processed_data)

                self.pending_products.clear()
            else:
                await asyncio.sleep(0.1)

    async def store_data_task(self):
        """Store the preprocessed data."""
        while True:
            if self.preprocessed_data or any(self.pending_relationships.values()):
                logger.info(f"Storing {len(self.preprocessed_data)} items in cacheDB")
                data = self.preprocessed_data
                self.preprocessed_data = []
                mapped_relations = []
                for origin_uri in self.pending_relationships.keys():
                    fetcher_view = self.cache_db.fetcher_view(origin_uri)
                    relations = self.pending_relationships[origin_uri]
                    self.pending_relationships[origin_uri] = []

                    def extend_origin(relation):
                        relation.origin_uri = origin_uri
                        return relation

                    mapped_relations.extend(
                        map(
                            extend_origin,
                            await self.data_sources[origin_uri].map_relationships(
                                fetcher_view, relations
                            ),
                        )
                    )
                await self.cache_db.store(data, mapped_relations)
            else:
                await asyncio.sleep(0.1)

    async def cleanup_task(self, source: DataSourcePlugin):
        while True:
            await self.cache_db.run_cleanup_for_plugin(source)
            # TODO: Refactor to only sleep a second and instead check the cleanup interval
            await asyncio.sleep(10)

    async def cleanup(self):
        await self.cache_db.disconnect()

    async def __api_client(self):
        api = FastAPI()

        @api.get("/start")
        async def sync():
            self.__last_synchronization = None
            return {}

        @api.get("/status")
        async def status():
            return {
                "last_synchronization": self.__last_synchronization,
            }

        # TODO: Add security options
        config = uvicorn.Config(
            app=api,
            host=self.config.Synchronizer.Api.host,
            port=self.config.Synchronizer.Api.port,
        )
        server = uvicorn.Server(config)
        await server.serve()
