"""
Base classes for manager daemons.

This module provides the base infrastructure for manager daemons
that fetch data, transform it, and preprocess it using plugins.
"""

from __future__ import annotations

import asyncio
import datetime
import enum
import time
import tomllib
from abc import ABC
from collections import defaultdict
from importlib.metadata import EntryPoints, entry_points
from pathlib import Path
from typing import Annotated

import fastapi
import uvicorn
from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, HttpUrl, model_validator

from dina.cachedb.database import CacheDB
from dina.cachedb.fetcher_view import FetcherView
from dina.cachedb.model import Asset, CsafProduct
from dina.common.log import LoggingConfig, get_logger

from dina.common.auth import AccessChecker, create_access_token, SessionData, Token
from dina.synchronizer.plugin_base.data_source import DataSourcePlugin, Relationship
from dina.synchronizer.plugin_base.preprocessor import PreprocessorPlugin

# Set up logging
logger = get_logger(__name__)

type TomlEntry = (
    dict[str, TomlEntry] | list[TomlEntry] | str | int | float | bool | None
)


class ApiConfig(BaseModel):
    host: str
    port: int
    access_token_expire_minutes: int


class SynchronizerSectionConfig(BaseModel):
    sync_interval: int | None = None
    fixed_time_of_day: str | None = None  # Format: "HH:MM" in 24-hour format
    preprocessor_plugins: list[str]
    plugin_configs_path: Path
    trigger_matcher_on_sync: bool = True
    # Number of seconds before last_run to consider records stale for cleanup
    cleanup_grace_period: int
    # The cleanup procedure is executed every cleanup_interval seconds
    cleanup_interval: int

    @model_validator(mode="after")
    def validate_scheduling_config(self):
        """Ensure sync_interval and fixed_time_of_day are mutually exclusive."""
        if self.sync_interval is None and self.fixed_time_of_day is None:
            raise ValueError(
                "Either sync_interval or fixed_time_of_day must be specified"
            )
        if self.sync_interval is not None and self.fixed_time_of_day is not None:
            raise ValueError(
                "sync_interval and fixed_time_of_day are mutually exclusive"
            )

        # Validate time format if fixed_time_of_day is provided
        if self.fixed_time_of_day is not None:
            try:
                hours, minutes = self.fixed_time_of_day.split(":")
                h, m = int(hours), int(minutes)
                if not (0 <= h <= 23 and 0 <= m <= 59):
                    raise ValueError
            except (ValueError, AttributeError):
                raise ValueError(
                    f"fixed_time_of_day must be in HH:MM format (24-hour), got: {self.fixed_time_of_day}"
                )
        return self


class SynchronizerConfig(BaseModel):
    Synchronizer: SynchronizerSectionConfig
    Api: ApiConfig
    Logging: LoggingConfig | None = None


class PluginLoadError(Exception):
    pass


class BaseSynchronizer(ABC):
    starttime = 0

    def __init__(
        self,
        cache_db: CacheDB,
        config: SynchronizerConfig,
        root_path: str = "",
    ):
        """Initialize the BaseManager.

        Args:
            cache_db: The cache database to use.
            data_source_plugin_configs: Path to a directory containing data source plugin configuration files.
            root_path: The root path for the API when behind a reverse proxy (e.g., "/assetsync").
            config_class: The Pydantic model class to use for configuration.
        """
        self.__last_synchronization: float | None = None
        self.__sync_start_time: float | None = None
        self.__sync_state: SynchronizerState = SynchronizerState.STOPPED
        self.__last_cleanup: float | None = None
        self.__total_sync_runs: int = 0
        self.__total_relationship_fetch_calls: int = 0
        self.__total_products_fetched: int = 0
        self.__total_relationships_fetched: int = 0
        self.__root_path: str = root_path
        self.__store_idle_event = asyncio.Event()
        self.__store_idle_event.set()
        self.cache_db: CacheDB = cache_db
        self.pending_products: list[Asset | CsafProduct] = []
        self.pending_relationships: dict[HttpUrl, list[Relationship]] = defaultdict(
            list
        )
        self.preprocessed_data: list[Asset | CsafProduct] = []

        self.config = config

        self.data_sources: dict[HttpUrl, DataSourcePlugin] = load_datasource_plugins(
            self.config.Synchronizer.plugin_configs_path
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
    ) -> DataSourcePlugin | PreprocessorPlugin:
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
    def __load_preprocessor_plugins(
        preprocessor_plugin_names: list[str],
    ) -> list[PreprocessorPlugin]:
        """
        Load preprocessor plugins specified in the configuration file.
        Raises:
            KeyError: If the configuration file is missing required fields.
        """
        preprocessor_plugins: list[PreprocessorPlugin] = []
        try:
            if not preprocessor_plugin_names:
                logger.warning("No preprocessor plugins specified in configuration")
                raise KeyError("Missing preprocessor_plugins in configuration")

            matching_config = Path(
                "./assets/plugin_configs/default/matching_config.toml"
            )

            for plugin_name in preprocessor_plugin_names:
                plugin_instance = BaseSynchronizer._load_plugin_from_entrypoint(
                    plugin_name, "dina.plugins.preprocessing", matching_config
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
        await self.cache_db.connect()

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

    def __should_run_sync(self) -> bool:
        """Determine if synchronization should run based on configured schedule."""
        if self.__last_synchronization is None:
            return True

        if self.config.Synchronizer.sync_interval is not None:
            # Interval-based scheduling
            return (
                self.__last_synchronization + self.config.Synchronizer.sync_interval
                < time.time()
            )
        else:
            # Fixed time of day scheduling
            now = datetime.datetime.now()
            hours, minutes = map(
                int, self.config.Synchronizer.fixed_time_of_day.split(":")
            )
            target_time = now.replace(
                hour=hours, minute=minutes, second=0, microsecond=0
            )

            # If target time has passed today, set for tomorrow
            if now > target_time:
                target_time += datetime.timedelta(days=1)

            # Check if last sync was before today's target time and we've passed it
            last_sync_dt = datetime.datetime.fromtimestamp(self.__last_synchronization)
            return last_sync_dt < target_time <= now

    async def fetch_data_task(self, source: DataSourcePlugin):
        while True:
            if self.__should_run_sync():
                try:
                    self.__sync_start_time = datetime.datetime.now().timestamp()
                    fetcher_view = self.cache_db.fetcher_view(source.origin_uri)
                    self.__sync_state = SynchronizerState.RUNNING
                    self.__total_sync_runs += 1

                    again = True

                    while again:
                        if self.__sync_state == SynchronizerState.STOP_REQUESTED:
                            break
                        again = await self.fetch_products(fetcher_view, source)
                        if self.__sync_state == SynchronizerState.STOP_REQUESTED:
                            break
                        await self.fetch_relationships(fetcher_view, source)

                    if self.__sync_state != SynchronizerState.STOP_REQUESTED:
                        # Only update last run time if the run completed.
                        await fetcher_view.set_last_run(
                            datetime.datetime.fromtimestamp(self.__sync_start_time)
                        )
                        await self.__wait_for_pipeline_drain()
                        if self.config.Synchronizer.trigger_matcher_on_sync:
                            await self.cache_db.add_matcher_trigger()

                except Exception as e:
                    logger.error(
                        f"Error fetching data from {source.debug_info()}: {e}",
                        exc_info=True,
                    )
                finally:
                    self.__sync_state = SynchronizerState.STOPPED
                    self.__sync_start_time = None
                    self.__last_synchronization = time.time()

            else:
                await asyncio.sleep(1)

    async def fetch_products(self, fetcher_view: FetcherView, source: DataSourcePlugin):
        logger.debug(f"Fetching data from {source.debug_info()}")
        result = await source.fetch_products(fetcher_view)
        self.__total_products_fetched += len(result.data)
        for datapoint in result.data:
            datapoint.origin_uri = str(source.origin_uri)
            self.pending_products.append(datapoint)

        return result.again

    async def fetch_relationships(
        self, fetcher_view: FetcherView, source: DataSourcePlugin
    ):
        again = True
        while again:
            logger.debug(f"Fetching relationships from {source.debug_info()}")
            result = await source.fetch_relationships(fetcher_view)
            self.__total_relationship_fetch_calls += 1
            self.__total_relationships_fetched += len(result.data)
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
            if self.preprocessed_data:
                logger.info(f"Storing {len(self.preprocessed_data)} items in cacheDB")
                self.__store_idle_event.clear()
                data = self.preprocessed_data
                self.preprocessed_data = []
                await self.cache_db.store(data, [])
                self.__store_idle_event.set()
            elif any(self.pending_relationships.values()):
                self.__store_idle_event.clear()
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
                await self.cache_db.store([], mapped_relations)
                self.__store_idle_event.set()
            else:
                self.__store_idle_event.set()
                await asyncio.sleep(0.1)

    async def __wait_for_pipeline_drain(self) -> None:
        """Wait until pending data/relations are fully stored."""
        while (
            self.pending_products
            or self.preprocessed_data
            or any(self.pending_relationships.values())
            or not self.__store_idle_event.is_set()
        ):
            await asyncio.sleep(0.1)

    async def cleanup_task(self, source: DataSourcePlugin):
        while True:
            if (
                self.__last_cleanup is None
                or self.__last_cleanup + self.config.Synchronizer.sync_interval
                < time.time()
            ):
                logger.info(f"Running cleanup for {source.debug_info()}")
                await self.cache_db.run_cleanup_for_plugin(
                    source,
                    self.config.Synchronizer.cleanup_grace_period,
                )
                self.__last_cleanup = time.time()
            else:
                await asyncio.sleep(1)

    async def cleanup(self):
        await self.cache_db.disconnect()

    async def __api_client(self):
        api = FastAPI(root_path=self.__root_path)
        task_route = APIRouter(
            prefix="/task", dependencies=[Depends(AccessChecker(self.cache_db))]
        )

        @api.post("/token")
        async def login_for_access_token(
            form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        ) -> Token:
            user = await self.cache_db.authenticate_user(
                form_data.username, form_data.password
            )
            if not user:
                raise HTTPException(
                    status_code=fastapi.status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect username or password",
                )
            access_token_expires = datetime.timedelta(
                minutes=self.config.Api.access_token_expire_minutes
            )
            token = create_access_token(
                SessionData(username=user.username), access_token_expires
            )
            return Token(access_token=token, token_type="bearer")

        @task_route.post("/start")
        async def sync():
            self.__last_synchronization = None
            return {}

        @task_route.post("/stop")
        async def stop():
            logger.info("Stopping synchronization task")
            self.__sync_state = SynchronizerState.STOP_REQUESTED

        @task_route.get("/status")
        async def status() -> SynchronizerStatus:
            pending_relationships = sum(
                len(relations) for relations in self.pending_relationships.values()
            )
            return SynchronizerStatus(
                last_synchronization=self.__last_synchronization,
                state=self.__sync_state,
                start=self.__sync_start_time,
                last_cleanup=self.__last_cleanup,
                total_relationship_fetch_calls=self.__total_relationship_fetch_calls,
                total_products_fetched=self.__total_products_fetched,
                total_relationships_fetched=self.__total_relationships_fetched,
                pending_products=len(self.pending_products),
                pending_relationships=pending_relationships,
                preprocessed_products=len(self.preprocessed_data),
                data_sources=len(self.data_sources),
            )

        api.include_router(task_route)

        # TODO: Add security options
        config = uvicorn.Config(
            app=api,
            host=self.config.Api.host,
            port=self.config.Api.port,
        )
        server = uvicorn.Server(config)
        await server.serve()


def load_datasource_plugins(plugin_configs: Path) -> dict[HttpUrl, DataSourcePlugin]:
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

    plugins: dict[HttpUrl, DataSourcePlugin] = {}

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


class SynchronizerState(enum.Enum):
    STOPPED = "stopped"
    STOP_REQUESTED = "stop_requested"
    RUNNING = "running"


class SynchronizerStatus(BaseModel):
    state: SynchronizerState
    start: float | None = None
    last_synchronization: float | None
    last_cleanup: float | None = None
    total_relationship_fetch_calls: int = 0
    total_products_fetched: int = 0
    total_relationships_fetched: int = 0
    pending_products: int = 0
    pending_relationships: int = 0
    preprocessed_products: int = 0
    data_sources: int = 0
