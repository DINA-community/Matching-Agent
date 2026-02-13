from __future__ import annotations
import asyncio
import concurrent.futures
import datetime
import enum
import itertools
import multiprocessing
import queue
import time
import tomllib
import traceback
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from queue import Empty, Queue
from typing import Any, Annotated, AsyncGenerator, Literal

import fastapi
import uvicorn
from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.params import Query, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, HttpUrl
import polars as pl

from dina.cachedb.database import CacheDB
from dina.cachedb.model import Match, CsafProduct, Asset
from dina.common.auth import AccessChecker, Token, SessionData, create_access_token
from dina.common.config import Config, MatchingConfig
from dina.common.log import configure_logging, get_logger, LoggingConfig
import sys
import argparse

from dina.matcher.calculate_score import Score
from dina.matcher.matching import Matching

from dina.synchronizer.base import load_datasource_plugins

# Logger (handlers configured after config is loaded)
logger = get_logger(__name__)

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class MatchingState(enum.Enum):
    STOPPED = "stopped"
    STOP_REQUESTED = "stop_requested"
    RUNNING = "running"


class MatcherStatus(BaseModel):
    state: MatchingState
    start: float | None = None
    last_matching: float | None = None
    total_match_runs: int = 0
    total_pairs_processed: int = 0
    total_matches_found: int = 0
    pending_tasks: int = 0
    pending_match_batches: int = 0


class MatchingTask(BaseModel):
    id: int
    assets: list[HttpUrl]
    csaf_documents: list[HttpUrl]


class MatchingTaskInfo(BaseModel):
    id: int
    assets: list[HttpUrl]
    csaf_documents: list[HttpUrl]
    state: Literal["pending", "running"]
    start_time: float | None = None


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


@dataclass
class _ActiveMatchingTask:
    task: MatchingTask
    batch_iter: AsyncGenerator[list[tuple[CsafProduct, Asset]]]
    start_time: float


class Matcher:
    def __init__(self, config_path: Path = Path("./assets/config.toml")) -> None:
        """
        Initialize the Matcher.
        """
        self.__config = Config.load(config_path)

        with open("./assets/plugin_configs/default/matching_config.toml", "rb") as f:
            mc = MatchingConfig.model_validate(tomllib.load(f))

        self.__matching_cfg_dict = mc.model_dump()

        # Configure logging based on config.toml
        configure_logging(self.__config.Matcher.Logging)

        self.__manager = multiprocessing.Manager()
        self.__matches: Queue[list[Match]] = self.__manager.Queue()
        self.__cache_db = CacheDB(self.__config.Cachedb)
        self.__last_matching: float | None = None
        self.__matching_tasks: deque[MatchingTask] = deque()
        self.__active_tasks: dict[int, _ActiveMatchingTask] = {}
        self.__cancelled_task_ids: set[int] = set()
        self.__next_task_id = itertools.count(1)
        self.__matching_state: MatchingState = MatchingState.STOPPED
        self.__matching_start_time: float | None = None
        self.__last_publish: float | None = None
        self.__total_match_runs: int = 0
        self.__total_pairs_processed: int = 0
        self.__total_matches_found: int = 0
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
        await self.__cache_db.connect()
        log_queue = self.__manager.Queue()
        async with asyncio.TaskGroup() as tg:
            tg.create_task(self.__serve_api())
            tg.create_task(self.__matching_task(log_queue))
            tg.create_task(self.__log_task(log_queue))
            tg.create_task(self.__store_matches_task())
            tg.create_task(self.__trigger_task())

    def __new_matching_task(
        self, assets: list[HttpUrl], csaf_documents: list[HttpUrl]
    ) -> MatchingTask:
        return MatchingTask(
            id=next(self.__next_task_id),
            assets=assets,
            csaf_documents=csaf_documents,
        )

    async def __log_task(self, log_queue: multiprocessing.Queue) -> None:
        while True:
            records = []
            try:
                # Get up to 1000 log records
                for _ in range(1000):
                    records.append(log_queue.get(block=False))
            except Empty:
                pass
            finally:
                for record in records:
                    logger.handle(record)
                await asyncio.sleep(0.01)

    def __should_run_matching(self) -> bool:
        """Determine if matching should run based on configured schedule."""
        # Always run if there are explicit matching tasks queued
        if len(self.__matching_tasks) > 0:
            return True

        if self.__last_matching is None:
            return True

        if self.__config.Matcher.sync_interval is not None:
            # Interval-based scheduling
            return (
                self.__last_matching + self.__config.Matcher.sync_interval < time.time()
            )
        else:
            # Fixed time of day scheduling
            now = datetime.datetime.now()
            hours, minutes = map(
                int, self.__config.Matcher.fixed_time_of_day.split(":")
            )
            target_time = now.replace(
                hour=hours, minute=minutes, second=0, microsecond=0
            )

            # If target time has passed today, set for tomorrow
            if now > target_time:
                target_time += datetime.timedelta(days=1)

            # Check if last matching was before today's target time and we've passed it
            last_match_dt = datetime.datetime.fromtimestamp(self.__last_matching)
            return last_match_dt < target_time <= now

    async def __matching_task(self, log_queue: multiprocessing.Queue) -> None:
        active_tasks: deque[_ActiveMatchingTask] = deque()
        parallel_tasks: list[asyncio.Future] = []
        num_processes = multiprocessing.cpu_count()
        loop = asyncio.get_event_loop()
        pool = concurrent.futures.ProcessPoolExecutor()
        last_log_output = datetime.datetime.now()

        while True:
            if self.__matching_state == MatchingState.STOP_REQUESTED:
                logger.info("Stop requested, stopping matching tasks")
                active_tasks.clear()
                self.__active_tasks.clear()
                if parallel_tasks:
                    await asyncio.gather(*parallel_tasks)
                    parallel_tasks = []
                self.__matching_state = MatchingState.STOPPED
                self.__matching_start_time = None
                self.__last_matching = time.time()
                continue

            should_run = self.__should_run_matching()
            if active_tasks or should_run:
                try:
                    if should_run and not active_tasks and not self.__matching_tasks:
                        # If no task is queued, try to match all assets and all csaf products.
                        self.__matching_tasks.append(self.__new_matching_task([], []))

                    now = datetime.datetime.now()
                    if (now - last_log_output).total_seconds() >= 5:
                        logger.info(f"Currently processing {len(active_tasks)} tasks.")
                        last_log_output = now

                    while self.__matching_tasks:
                        task = self.__matching_tasks.popleft()
                        if task.id in self.__cancelled_task_ids:
                            logger.info(f"Skipping cancelled task {task.id}")
                            self.__cancelled_task_ids.discard(task.id)
                            continue
                        logger.info(f"Starting matching task: {task}")
                        active_task = _ActiveMatchingTask(
                            task=task,
                            batch_iter=self.__cache_db.fetch_pairs_batches(
                                task.assets, task.csaf_documents, batch_size_sqrt=20
                            ),
                            start_time=time.time(),
                        )
                        active_tasks.append(active_task)
                        self.__active_tasks[task.id] = active_task
                        self.__total_match_runs += 1
                        if self.__matching_state != MatchingState.RUNNING:
                            self.__matching_state = MatchingState.RUNNING
                            self.__matching_start_time = time.time()

                    if not active_tasks:
                        await asyncio.sleep(1)
                        continue

                    task_state = active_tasks.popleft()
                    if task_state.task.id in self.__cancelled_task_ids:
                        logger.info(f"Cancelling active task {task_state.task.id}")
                        self.__cancelled_task_ids.discard(task_state.task.id)
                        self.__active_tasks.pop(task_state.task.id, None)
                        continue

                    # Check for max duration timeout per task
                    if self.__config.Matcher.max_duration is not None:
                        elapsed = time.time() - task_state.start_time
                        if elapsed >= self.__config.Matcher.max_duration:
                            logger.warning(
                                f"Matching task exceeded max_duration of {self.__config.Matcher.max_duration}s "
                                f"(elapsed: {elapsed:.1f}s). Stopping task."
                            )
                            self.__active_tasks.pop(task_state.task.id, None)
                            continue

                    try:
                        batch = await task_state.batch_iter.__anext__()
                    except StopAsyncIteration:
                        self.__active_tasks.pop(task_state.task.id, None)
                        continue

                    if not batch:
                        active_tasks.append(task_state)
                        continue

                    self.__total_pairs_processed += len(batch)
                    while self.__matches.qsize() > num_processes * 2:
                        await asyncio.sleep(0.1)
                    parallel_tasks.append(
                        loop.run_in_executor(
                            pool,
                            match_pairs,
                            self.__matches,
                            log_queue,
                            self.__config.Matcher.Logging,
                            batch,
                            self.__config.Matcher.match_threshold,
                            self.__matching_cfg_dict,
                        )
                    )
                    if len(parallel_tasks) >= num_processes:
                        await asyncio.gather(*parallel_tasks)
                        parallel_tasks = []

                    active_tasks.append(task_state)
                except Exception as e:
                    logger.error(f"Error fetching matches: {e}")
                    print(traceback.format_exc())
                finally:
                    if not active_tasks and not self.__matching_tasks:
                        if parallel_tasks:
                            await asyncio.gather(*parallel_tasks)
                            parallel_tasks = []
                        if self.__matching_state == MatchingState.RUNNING:
                            logger.info("Matching task finished")
                        self.__matching_state = MatchingState.STOPPED
                        self.__matching_start_time = None
                        self.__last_matching = time.time()
                        self.__active_tasks.clear()

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
                    self.__total_matches_found += len(matches_batch)
                except Empty:
                    pass
            if tasks:
                match_ids = await asyncio.gather(*tasks)
                match_ids = itertools.chain.from_iterable(match_ids)
                matches = await self.__cache_db.get_matches(ids=match_ids)
                # Categorize by asset origin
                categorized_matches = defaultdict(list)
                for match in matches:
                    categorized_matches[HttpUrl(match.asset.origin_uri)].append(match)
                # Let asset plugins notify subscribers of new matches
                for origin, matches in categorized_matches.items():
                    if ds := self.__data_source_plugins.get(origin):
                        if ds.config.DataSource.publish_matches:
                            logger.debug(
                                f"Notifying subscribers of new matches from {origin}"
                            )
                            await self.__data_source_plugins[origin].notify_new_matches(
                                matches
                            )
            await asyncio.sleep(0.1)

    async def __trigger_task(self):
        last_trigger_id = 0
        while True:
            try:
                triggers = await self.__cache_db.consume_matcher_triggers(
                    last_id=last_trigger_id
                )
                if triggers:
                    last_trigger_id = triggers[-1].id
                    if not self.__matching_tasks:
                        self.__matching_tasks.append(self.__new_matching_task([], []))
            except Exception as e:
                logger.error(f"Error consuming matcher triggers: {e}", exc_info=True)
            await asyncio.sleep(0.5)

    async def __serve_api(self):
        api = FastAPI(root_path="/matcher")

        sub_route = APIRouter(
            prefix="/subscribe", dependencies=[Depends(AccessChecker(self.__cache_db))]
        )
        task_route = APIRouter(
            prefix="/task", dependencies=[Depends(AccessChecker(self.__cache_db))]
        )
        matches_route = APIRouter(
            prefix="/matches", dependencies=[Depends(AccessChecker(self.__cache_db))]
        )
        clear_route = APIRouter(
            prefix="/clear", dependencies=[Depends(AccessChecker(self.__cache_db))]
        )

        @api.post("/token")
        async def login_for_access_token(
            form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        ) -> Token:
            user = await self.__cache_db.authenticate_user(
                form_data.username, form_data.password
            )
            if not user:
                raise HTTPException(
                    status_code=fastapi.status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect username or password",
                )
            access_token_expires = datetime.timedelta(
                minutes=self.__config.Matcher.Api.access_token_expire_minutes
            )
            token = create_access_token(
                SessionData(username=user.username), access_token_expires
            )
            return Token(access_token=token, token_type="bearer")

        @matches_route.get("/")
        async def get_matches(
            limit: int = 100,
            offset: int = 0,
            origin_uri: HttpUrl | None = None,
            time_lte: float | None = None,
            time_gte: float | None = None,
            assets: Annotated[list[HttpUrl] | None, Query()] = None,
            csaf_documents: Annotated[list[HttpUrl] | None, Query()] = None,
            threshold: float | None = None,
        ) -> list[APIMatch]:
            """Get a list of matches between CSAF advisories and assets.

            Parameters:
                limit (int): Maximum number of matches to return. Defaults to 100.
                offset (int): Number of matches to skip for pagination. Defaults to 0.
                origin_uri (HttpUrl | None): Filter matches to only include matches from a specific origin.
                time_lte (float | None): Filter matches to only include matches with a timestamp less than or equal to the specified value.
                time_gte (float | None): Filter matches to only include matches with a timestamp greater than or equal to the specified value.
                assets (list[int] | None): Filter matches to only include matches with assets from the specified list of assets.
                csaf_documents (list[int] | None): Filter matches to only include matches with csaf_products from the specified set of documents.
                threshold (float | None): Filter matches to only include matches with a score greater than or equal to the specified value.

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
                limit=limit,
                last_match_id=offset,
                origin_uri=origin_uri,
                time_lte=time_lte,
                time_gte=time_gte,
                assets=assets,
                csaf_products=csaf_documents,
                threshold=threshold,
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
        async def start(
            assets: Annotated[list[HttpUrl] | None, Query()] = None,
            csaf_documents: Annotated[list[HttpUrl] | None, Query()] = None,
        ):
            if assets is None:
                assets = []
            if csaf_documents is None:
                csaf_documents = []
            logger.info("Starting matching task")
            task = self.__new_matching_task(assets, csaf_documents)
            self.__matching_tasks.append(task)
            return {"id": task.id}

        @task_route.get("/running")
        async def running_tasks() -> list[MatchingTaskInfo]:
            return [
                MatchingTaskInfo(
                    id=task.task.id,
                    assets=task.task.assets,
                    csaf_documents=task.task.csaf_documents,
                    state="running",
                    start_time=task.start_time,
                )
                for task in self.__active_tasks.values()
            ]

        @task_route.get("/status")
        async def status() -> MatcherStatus:
            return MatcherStatus(
                state=self.__matching_state,
                start=self.__matching_start_time,
                last_matching=self.__last_matching,
                total_match_runs=self.__total_match_runs,
                total_pairs_processed=self.__total_pairs_processed,
                total_matches_found=self.__total_matches_found,
                pending_tasks=len(self.__matching_tasks),
                pending_match_batches=self.__matches.qsize(),
            )

        @task_route.post("/stop")
        async def stop(task_id: Annotated[int | None, Query()] = None):
            if task_id is None:
                logger.info("Stopping all matching tasks")
                self.__matching_tasks.clear()
                self.__cancelled_task_ids.update(self.__active_tasks.keys())
                self.__matching_state = MatchingState.STOP_REQUESTED
                return {"stopped": "all"}

            removed_pending = False
            if self.__matching_tasks:
                remaining: deque[MatchingTask] = deque()
                while self.__matching_tasks:
                    task = self.__matching_tasks.popleft()
                    if task.id == task_id:
                        removed_pending = True
                    else:
                        remaining.append(task)
                self.__matching_tasks = remaining

            if removed_pending:
                logger.info(f"Cancelled pending task {task_id}")
                return {"stopped": "pending", "id": task_id}

            if task_id in self.__active_tasks:
                logger.info(f"Cancellation requested for active task {task_id}")
                self.__cancelled_task_ids.add(task_id)
                return {"stopped": "running", "id": task_id}

            raise HTTPException(status_code=404, detail="Task not found")

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
            await self.__cache_db.clear_assets(origin_uri)

        @clear_route.post("/csaf")
        async def clean_csaf(origin_uri: HttpUrl):
            logger.info("Cleaning matcher csaf cache")
            await self.__cache_db.clear_csaf_products(origin_uri)

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
        path = self.__data_source_plugins[HttpUrl(origin_uri)].build_resource_path(
            origin_info
        )
        if path:
            # Ensure we don't duplicate slashes on join
            if origin_uri.endswith("/") and path.startswith("/"):
                return HttpUrl(origin_uri[:-1] + path)
            return HttpUrl(origin_uri + path)

        return HttpUrl(origin_uri)


def match_pairs(
    matches: queue.Queue[list[Match]],
    log_queue: multiprocessing.Queue,
    logging_config: LoggingConfig,
    pairs: list[tuple[CsafProduct, Asset]],
    threshold: float,
    matching_config: dict[str, Any],
):
    configure_logging(logging_config, log_queue)
    logger.debug(f"Matching batch with {len(pairs)} pairs")
    batch = []
    for csaf, asset in pairs:
        if not (csaf and csaf.product and asset and asset.product):
            continue

        csaf_dict = {f"csaf_{k}": v for k, v in csaf.product.to_dict().items()}
        asset_dict = {f"asset_{k}": v for k, v in asset.product.to_dict().items()}

        df = pl.DataFrame([{**csaf_dict, **asset_dict}], strict=False)

        matching = Matching(matching_config)
        df_matches = matching.df_matching(df)

        score = Score(matching_config)
        result, reason, score_percent = score.calculate_overall_score(df_matches)

        if score_percent < threshold:
            continue

        match = Match()
        match.asset_id = asset.id
        match.csaf_product_id = csaf.id
        match.score = score_percent
        match.timestamp = datetime.datetime.now().timestamp()
        match.status = f"result: {result}, reason: {reason}"

        batch.append(match)
    matches.put(batch)


async def run_matcher(config_path: Path = Path("./assets/config.toml")):
    """Run the Matcher."""
    # Create and initialize the Matcher
    matcher = Matcher(config_path=config_path)
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
        parser = argparse.ArgumentParser(description="Run the Matching service")
        parser.add_argument(
            "--config",
            type=Path,
            default=Path("./assets/config.toml"),
            help="Path to matcher configuration TOML file",
        )
        args = parser.parse_args()

        # Run the Matcher
        asyncio.run(run_matcher(config_path=args.config))
    except KeyboardInterrupt:
        logger.info("Matcher stopped by user")
    except Exception as e:
        logger.error(f"Matcher failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()
