import asyncio
import datetime
import time
import tomllib
import traceback
from pathlib import Path
from typing import Any

import uvicorn
from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl

from dina.cachedb.database import CacheDB
from dina.cachedb.model import Match
from dina.common.logging import configure_logging, get_logger
import sys

from dina.synchronizer.base import load_datasource_plugins

# Configure logging
configure_logging()

logger = get_logger(__name__)

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


# TODO: Define correct fields
class MatchUpdate(BaseModel):
    asset_id: int
    csaf_id: int
    matching_reason: str
    score: float


class APIMatch(BaseModel):
    id: int
    csaf_origin: HttpUrl
    asset_origin: HttpUrl
    timestamp: float
    score: float
    status: str


class MatchSubscription(BaseModel):
    """
    :ivar origin_filter: A list of strings representing filters to match specific origins.
        Usually you will want to only subscribe to matches that match to an asset or csaf
        that comes from an origin you are interested in.
    """

    url: HttpUrl
    secret: str | None = None
    origin_filter: list[str]


class ApiConfig(BaseModel):
    host: str
    port: int


class MatcherConfig(BaseModel):
    sync_interval: int
    Api: ApiConfig
    Cachedb: CacheDB.Config
    asset_plugins_path: Path
    csaf_plugins_path: Path


class Matcher:
    class Config(BaseModel):
        Matcher: MatcherConfig

    def __init__(self) -> None:
        """
        Initialize the Matcher.
        """
        with open("./assets/matcher.toml", "rb") as f:
            self.__config = Matcher.Config.model_validate(tomllib.load(f))

        self.__matches: list[Match] = []
        self.__cache_db = CacheDB()
        self.__last_synchronization: float | None = None
        self.__data_source_plugins = load_datasource_plugins(
            Path(self.__config.Matcher.asset_plugins_path)
        )
        for k, v in load_datasource_plugins(
            Path(self.__config.Matcher.csaf_plugins_path)
        ).items():
            if k in self.__data_source_plugins:
                raise ValueError(f"Duplicate origin: {k}")
            self.__data_source_plugins[k] = v

    async def run(self):
        """Run the matcher."""
        await self.__cache_db.connect(self.__config.Matcher.Cachedb)
        async with asyncio.TaskGroup() as tg:
            tg.create_task(self.__serve_api())
            tg.create_task(self.__matching_task())
            tg.create_task(self.__store_matches_task())

    async def __matching_task(self):
        while True:
            if (
                self.__last_synchronization is None
                or self.__last_synchronization + self.__config.Matcher.sync_interval
                < time.time()
            ):
                try:
                    counter = 0
                    async for csaf, asset in self.__cache_db.fetch_pairs():
                        if counter % 10000 == 0:
                            logger.debug(f"Matching... {counter}")
                        counter += 1
                        match = Match()
                        match.asset_id = asset.id
                        match.csaf_product_id = csaf.id
                        match.score = 100
                        match.timestamp = datetime.datetime.now().timestamp()
                        match.status = ""
                        self.__matches.append(match)
                except Exception as e:
                    logger.error(f"Error fetching matches: {e}")
                    print(traceback.format_exc())

                self.__last_synchronization = time.time()
            else:
                await asyncio.sleep(1)

    async def __store_matches_task(self):
        while True:
            if self.__matches:
                matches = self.__matches
                self.__matches = []
                logger.debug(f"Storing {len(matches)} matches")
                await self.__cache_db.store_matches(matches)
            else:
                await asyncio.sleep(1)

    async def __serve_api(self):
        api = FastAPI()

        sub_route = APIRouter(prefix="/subscribe")
        task_route = APIRouter(prefix="/task")
        matches_route = APIRouter(prefix="/matches")

        @matches_route.get("/")
        async def get_matches(limit: int = 100, offset: int = 0) -> list[APIMatch]:
            """Get a list of matches between CSAF advisories and assets.

            Parameters:
                limit (int): Maximum number of matches to return. Defaults to 100.
                offset (int): Number of matches to skip for pagination. Defaults to 0.

            Returns:
                list[APIMatch]: A list of matches, each containing:
                    - id: Unique identifier of the match
                    - csaf_origin: Full URL to the CSAF advisory
                    - asset_origin: Full URL to the matched asset
                    - timestamp: Unix timestamp when the match was created
                    - score: Matching confidence score (0-100)
                    - status: Current status of the match
            """
            logger.info(f"Getting matches limit={limit} offset={offset}")
            matches = await self.__cache_db.get_matches(limit=limit, offset=offset)
            return [
                APIMatch(
                    id=match.id,
                    csaf_origin=self.build_full_origin_uri(
                        match.csaf_product.origin_uri, match.csaf_product.origin_info
                    ),
                    asset_origin=self.build_full_origin_uri(
                        match.asset.origin_uri, match.asset.origin_info
                    ),
                    timestamp=match.timestamp,
                    score=match.score,
                    status=match.status,
                )
                for match in matches
            ]

        @matches_route.get("/{match_id}")
        async def get_match(match_id: int) -> APIMatch:
            logger.info(f"Getting match {match_id}")
            match = await self.__cache_db.get_match(match_id)
            if match is None:
                raise HTTPException(status_code=404, detail="Match not found")
            return APIMatch(
                id=match.id,
                csaf_origin=self.build_full_origin_uri(
                    match.csaf_product.origin_uri, match.csaf_product.origin_info
                ),
                asset_origin=self.build_full_origin_uri(
                    match.asset.origin_uri, match.asset.origin_info
                ),
                timestamp=match.timestamp,
                score=match.score,
                status=match.status,
            )

        @task_route.post("/start")
        async def start():
            logger.info("Starting matching task")
            self.__last_synchronization = None

        @task_route.get("/status")
        async def status():
            return {"status": "running"}

        @task_route.post("/stop")
        async def stop():
            logger.info("Stopping matching task")

        @sub_route.post("/new_match")
        async def subscribe(body: MatchSubscription) -> None:
            logger.info(f"Subscribed to match updates from {body.origin_filter}")

        @api.webhooks.post("new_match")
        async def test(body: MatchUpdate):
            """
            When a new match is found, this webhook is triggered and a message containing the match is sent to the registered hook.
            Subscribing to this hook can be done via the /hooks/subscribe_match_updates endpoint.
            """

        api.include_router(task_route)
        api.include_router(matches_route)
        api.include_router(sub_route)

        config = uvicorn.Config(
            app=api,
            host=self.__config.Matcher.Api.host,
            port=self.__config.Matcher.Api.port,
        )
        server = uvicorn.Server(config)
        await server.serve()

    def build_full_origin_uri(
        self, origin_uri: str, origin_info: dict[str, Any]
    ) -> HttpUrl:
        """Return origin_uri extended with a plugin-provided path derived from origin_info.

        Strategy:
        - Iterate over installed data source plugins and ask each one to build a path
          for the given origin_info; return the first non-empty path.
        - If no path is available, just return the origin_uri as-is.
        """
        path = self.__data_source_plugins[origin_uri].build_resource_path(origin_info)
        if path:
            # Ensure we don't duplicate slashes on join
            if origin_uri.endswith("/") and path.startswith("/"):
                return HttpUrl(origin_uri[:-1] + path)
            return HttpUrl(origin_uri + path)

        return HttpUrl(origin_uri)


async def run_matcher():
    """Run the Matcher."""
    # Create and initialize the Matcher
    matcher = Matcher()
    try:
        # Find matches
        await matcher.run()

    except Exception as e:
        logger.error(f"Matcher failed: {str(e)}")
        raise
    finally:
        # TODO: Cleanup?
        pass


def main():
    """Entry point for the Matcher."""
    try:
        # Run the Matcher
        asyncio.run(run_matcher())
    except KeyboardInterrupt:
        logger.info("Matcher stopped by user")
    except Exception as e:
        logger.error(f"Matcher failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()
