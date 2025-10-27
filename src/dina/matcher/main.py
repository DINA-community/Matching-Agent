import asyncio
import concurrent.futures
import datetime
import itertools
import multiprocessing
import queue
import time
import tomllib
import traceback
from collections import defaultdict
from pathlib import Path
from queue import Empty, Queue
from typing import Any

import uvicorn
from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
import polars as pl

from dina.cachedb.database import CacheDB
from dina.cachedb.model import Match, CsafProduct, Asset
from dina.common.logging import configure_logging, get_logger
import sys

from dina.matcher.calculate_score import Score
from dina.matcher.clean_text import Normalizer
from dina.matcher.matching import Matching

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
    match_threshold: float
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

        self.__manager = multiprocessing.Manager()
        self.__matches: Queue[list[Match]] = self.__manager.Queue()
        self.__cache_db = CacheDB()
        self.__last_matching: float | None = None
        self.__last_publish: float | None = None
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

    async def __matching_task(self) -> None:
        while True:
            if (
                self.__last_matching is None
                or self.__last_matching + self.__config.Matcher.sync_interval
                < time.time()
            ):
                try:
                    parallel_tasks = []
                    num_processes = multiprocessing.cpu_count()
                    with concurrent.futures.ProcessPoolExecutor() as pool:
                        loop = asyncio.get_event_loop()
                        async for batch in self.__cache_db.fetch_pairs_batches(20):
                            if not batch:
                                continue
                            while self.__matches.qsize() > num_processes * 2:
                                await asyncio.sleep(0.1)
                            parallel_tasks.append(
                                loop.run_in_executor(
                                    pool,
                                    match_pairs,
                                    self.__matches,
                                    batch,
                                    self.__config.Matcher.match_threshold,
                                )
                            )
                            if len(parallel_tasks) >= num_processes:
                                await asyncio.gather(*parallel_tasks)
                                parallel_tasks = []
                except Exception as e:
                    logger.error(f"Error fetching matches: {e}")
                    print(traceback.format_exc())

                self.__last_matching = time.time()
            else:
                await asyncio.sleep(1)

    async def __store_matches_task(self):
        while True:
            tasks = []
            while not self.__matches.empty():
                try:
                    matches_batch = self.__matches.get(block=False)
                    logger.debug(
                        f"Storing {len(matches_batch)} matches. ~{self.__matches.qsize()} batches remaining."
                    )
                    tasks.append(self.__cache_db.store_matches(matches_batch))
                except Empty:
                    pass
            if tasks:
                match_ids = await asyncio.gather(*tasks)
                match_ids = itertools.chain.from_iterable(match_ids)
                matches = await self.__cache_db.get_matches(ids=match_ids)
                # Categorize by asset origin
                categorized_matches = defaultdict(list)
                for match in matches:
                    categorized_matches[match.asset.origin_uri].append(match)
                # Let asset plugins notify subscribers of new matches
                for origin, matches in categorized_matches.items():
                    if self.__data_source_plugins[
                        origin
                    ].config.DataSource.publish_matches:
                        await self.__data_source_plugins[origin].notify_new_matches(
                            matches
                        )
            await asyncio.sleep(0.1)

    async def __serve_api(self):
        api = FastAPI()

        sub_route = APIRouter(prefix="/subscribe")
        task_route = APIRouter(prefix="/task")
        matches_route = APIRouter(prefix="/matches")
        clear_route = APIRouter(prefix="/clear")

        @matches_route.get("/")
        async def get_matches(
            limit: int = 100, offset: int = 0, origin_uri: str | None = None
        ) -> list[APIMatch]:
            """Get a list of matches between CSAF advisories and assets.

            Parameters:
                limit (int): Maximum number of matches to return. Defaults to 100.
                offset (int): Number of matches to skip for pagination. Defaults to 0.
                origin_uri (HttpUrl | None): Filter matches to only include matches from a specific origin.

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
            matches = await self.__cache_db.get_matches(
                limit=limit, offset=offset, origin_uri=origin_uri
            )
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
            self.__last_matching = None

        @task_route.get("/status")
        async def status():
            return {"status": "running"}

        # @task_route.post("/stop")
        # async def stop():
        #     logger.info("Stopping matching task")

        @clear_route.post("/all")
        async def clean_all():
            logger.info("Cleaning entire matcher cache")
            await self.__cache_db.clear()

        @clear_route.post("/matches")
        async def clean_matches():
            logger.info("Cleaning matcher matches cache")
            await self.__cache_db.clear_matches()

        @clear_route.post("/assets")
        async def clean_assets(origin_uri: HttpUrl):
            logger.info("Cleaning matcher assets cache")
            await self.__cache_db.clear_assets(str(origin_uri))

        @clear_route.post("/csaf")
        async def clean_csaf(origin_uri: HttpUrl):
            logger.info("Cleaning matcher csaf cache")
            await self.__cache_db.clear_csaf_products(str(origin_uri))

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
        api.include_router(clear_route)

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


def match_pairs(
    matches: queue.Queue, pairs: list[tuple[CsafProduct, Asset]], threshold: float
):
    logger.debug(f"Matching batch with {len(pairs)} pairs")
    batch = []
    for csaf, asset in pairs:
        # TODO: add product_type, sbom_urls and file
        csaf_dict = {f"csaf_{k}": v for k, v in csaf.product.to_dict().items()}
        asset_dict = {f"asset_{k}": v for k, v in asset.product.to_dict().items()}

        df = pl.DataFrame([{**csaf_dict, **asset_dict}])

        freetext_fields = [
            "name",
            "hardware_name",
            "manufacturer_name",
            "device_family",
        ]

        ordered_fields = ["version", "model", "model_numbers", "part_numbers"]

        other_fields = ["cpe", "purl"]

        pl.Config.set_fmt_str_lengths(2000)

        normalizer = Normalizer(freetext_fields, ordered_fields, other_fields)
        df_norm = normalizer.apply(df)

        # for field in freetext_fields:
        #     print(df_norm.select([f"csaf_{field}", f"asset_{field}"]))
        #     print(df_norm.select([f"csaf_{field}_norm", f"asset_{field}_norm"]))

        # for field in ordered_fields:
        #     print(df_norm.select([f"csaf_{field}", f"asset_{field}"]))
        #     print(df_norm.select([f"csaf_{field}_norm", f"asset_{field}_norm"]))

        matching = Matching(freetext_fields, ordered_fields)
        df_norm_matches = matching.df_matching(df_norm)

        score = Score(freetext_fields, ordered_fields)
        result, reason, score_procent = score.calculate_overall_score(df_norm_matches)

        # for field in freetext_fields:
        #     print(df_norm_matches.select([f"{field}_match"]))

        # for field in ordered_fields:
        #     print(df_norm_matches.select([f"{field}_match"]))

        if score_procent < threshold:
            continue

        match = Match()
        match.asset_id = asset.id
        match.csaf_product_id = csaf.id
        match.score = score_procent
        match.timestamp = datetime.datetime.now().timestamp()
        match.status = f"result: {result}, reason: {reason}"
        # match = Match()
        # match.asset_id = asset.id
        # match.csaf_product_id = csaf.id
        # match.score = 100
        # match.timestamp = datetime.datetime.now().timestamp()
        # match.status = ""
        batch.append(match)
    matches.put(batch)


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
