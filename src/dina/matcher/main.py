from __future__ import annotations
import asyncio
import concurrent.futures
import copy
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
from pydantic import BaseModel, HttpUrl, ValidationError
import polars as pl

from dina.cachedb.database import CacheDB
from dina.cachedb.model import Match, CsafProduct, Asset
from dina.common.auth import AccessChecker, Token, SessionData, create_access_token
from dina.common.config import (
    Config,
    MatchingConfig,
    apply_updates,
    validate_update_keys,
    validate_update_prefixes,
    write_toml_file,
)
from dina.common.log import configure_logging, get_logger, LoggingConfig
import sys
import argparse

from dina.matcher.calculate_score import Score
from dina.matcher.config_hash import hash_matching_config
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
    trigger: Literal["manual", "automated"]
    state: Literal[
        "pending", "running", "completed", "cancelled", "timed_out", "failed"
    ] = "pending"
    created_at: float
    start_time: float | None = None
    finished_at: float | None = None
    duration_seconds: float | None = None
    total_pairs: int = 0
    processed_pairs: int = 0
    matches_found: int = 0
    progress: float | None = None
    matching_config_hash: str | None = None
    force_recompute: bool = False
    error: str | None = None


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
    matcher_run_id: int | None = None
    matching_config_hash: str | None = None


class StartMatchingTaskRequest(BaseModel):
    assets: list[HttpUrl] = []
    csaf_documents: list[HttpUrl] = []
    matching_config: dict[str, Any] | None = None
    force_recompute: bool | None = None


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
    matching_config: dict[str, Any]
    batch_iter: AsyncGenerator[list[tuple[CsafProduct, Asset]]]
    start_time: float
    total_pairs: int
    processed_pairs: int = 0


@dataclass
class _QueuedMatchingTask:
    task: MatchingTask
    matching_config: dict[str, Any]
    force_recompute: bool = False


class Matcher:
    def __init__(self, config_path: Path = Path("./assets/config.toml")) -> None:
        """
        Initialize the Matcher.
        """
        self.__config_path = config_path
        self.__config = Config.load(config_path)

        with open("./assets/plugin_configs/default/matching_config.toml", "rb") as f:
            mc = MatchingConfig.model_validate(tomllib.load(f))

        self.__matching_cfg_dict = mc.model_dump()

        # Configure logging based on config.toml
        configure_logging(self.__config.Matcher.Logging)

        self.__manager = multiprocessing.Manager()
        self.__matches: Queue[tuple[int, list[tuple[int, int]], list[Match]]] = (
            self.__manager.Queue()
        )
        self.__cache_db = CacheDB(self.__config.Cachedb)
        self.__last_matching: float | None = None
        self.__matching_tasks: deque[_QueuedMatchingTask] = deque()
        self.__active_tasks: dict[int, _ActiveMatchingTask] = {}
        self.__cancelled_task_ids: set[int] = set()
        self.__in_flight_by_task: dict[int, int] = {}
        self.__scheduled_batches_by_task: dict[int, int] = {}
        self.__store_in_progress_by_task: dict[int, int] = {}
        self.__matches_found_by_task: dict[int, int] = {}
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

    @staticmethod
    def _as_matching_task(run: Any) -> MatchingTask:
        finished_at = run.finished_at
        start_time = run.started_at if run.state != "pending" else None
        duration_seconds = None
        if start_time is not None:
            end = finished_at if finished_at is not None else time.time()
            duration_seconds = max(end - start_time, 0.0)
        progress = None
        if run.total_pairs > 0:
            progress = min(run.processed_pairs / run.total_pairs, 1.0)
        return MatchingTask(
            id=run.id,
            assets=[HttpUrl(v) for v in (run.assets or [])],
            csaf_documents=[HttpUrl(v) for v in (run.csaf_documents or [])],
            trigger=run.trigger,
            state=run.state,
            created_at=run.started_at,
            start_time=start_time,
            finished_at=finished_at,
            duration_seconds=duration_seconds,
            total_pairs=run.total_pairs,
            processed_pairs=run.processed_pairs,
            matches_found=run.matches_found,
            progress=progress,
            matching_config_hash=run.matching_config_hash,
            force_recompute=run.force_recompute,
            error=run.error,
        )

    @staticmethod
    def _merge_matching_config(
        base_config: dict[str, Any], overrides: dict[str, Any]
    ) -> dict[str, Any]:
        merged = copy.deepcopy(base_config)

        def _merge(target: dict[str, Any], source: dict[str, Any]) -> None:
            for key, value in source.items():
                if isinstance(value, dict) and isinstance(target.get(key), dict):
                    _merge(target[key], value)
                else:
                    target[key] = value

        _merge(merged, overrides)
        return merged

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

    async def __new_matching_task(
        self,
        assets: list[HttpUrl],
        csaf_documents: list[HttpUrl],
        trigger: Literal["manual", "automated"],
        matching_config: dict[str, Any] | None = None,
        force_recompute: bool = False,
    ) -> _QueuedMatchingTask:
        effective_matching_config = (
            copy.deepcopy(matching_config)
            if matching_config is not None
            else copy.deepcopy(self.__matching_cfg_dict)
        )
        config_hash = hash_matching_config(effective_matching_config)
        run = await self.__cache_db.create_matcher_run(
            trigger=trigger,
            assets=assets,
            csaf_documents=csaf_documents,
            matching_config_hash=config_hash,
            matching_config=effective_matching_config,
            force_recompute=force_recompute,
            state="pending",
            started_at=time.time(),
            total_pairs=0,
        )
        task = self._as_matching_task(run)
        task.matching_config_hash = config_hash
        task.force_recompute = force_recompute
        return _QueuedMatchingTask(
            task=task,
            matching_config=effective_matching_config,
            force_recompute=force_recompute,
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
        elif self.__config.Matcher.fixed_time_of_day is not None:
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
        else:
            # No schedule configured: manual triggers only
            return False

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
                cancelled_tasks = list(active_tasks)
                cancelled_task_ids = {task.task.id for task in cancelled_tasks}
                active_tasks.clear()
                self.__active_tasks.clear()
                if parallel_tasks:
                    await asyncio.gather(*parallel_tasks)
                    parallel_tasks = []
                if cancelled_task_ids:
                    await self.__wait_for_tasks_idle(cancelled_task_ids)
                for active_task in cancelled_tasks:
                    await self.__finalize_task(active_task, state="cancelled")
                self.__matching_state = MatchingState.STOPPED
                self.__matching_start_time = None
                self.__last_matching = time.time()
                continue

            should_run = self.__should_run_matching()
            if active_tasks or should_run:
                task_state: _ActiveMatchingTask | None = None
                try:
                    if should_run and not active_tasks and not self.__matching_tasks:
                        # If no task is queued, try to match all assets and all csaf products.
                        self.__matching_tasks.append(
                            await self.__new_matching_task([], [], trigger="automated")
                        )

                    now = datetime.datetime.now()
                    if (now - last_log_output).total_seconds() >= 5:
                        logger.info(f"Currently processing {len(active_tasks)} tasks.")
                        last_log_output = now

                    while self.__matching_tasks:
                        queued_task = self.__matching_tasks.popleft()
                        task = queued_task.task
                        if task.id in self.__cancelled_task_ids:
                            logger.info(f"Skipping cancelled task {task.id}")
                            self.__cancelled_task_ids.discard(task.id)
                            await self.__cache_db.finish_matcher_run(
                                task.id,
                                state="cancelled",
                                finished_at=time.time(),
                            )
                            continue
                        logger.info(f"Starting matching task: {task}")
                        total_pairs = await self.__cache_db.count_pairs_to_match(
                            assets=task.assets,
                            csaf_documents=task.csaf_documents,
                            matching_config_hash=task.matching_config_hash
                            or hash_matching_config(queued_task.matching_config),
                            force_recompute=task.force_recompute,
                        )
                        start_time = time.time()
                        task.state = "running"
                        task.start_time = start_time
                        task.total_pairs = total_pairs
                        active_task = _ActiveMatchingTask(
                            task=task,
                            matching_config=queued_task.matching_config,
                            batch_iter=self.__cache_db.fetch_pairs_batches(
                                task.assets,
                                task.csaf_documents,
                                matching_config_hash=task.matching_config_hash
                                or hash_matching_config(queued_task.matching_config),
                                force_recompute=task.force_recompute,
                                batch_size_sqrt=20,
                            ),
                            start_time=start_time,
                            total_pairs=total_pairs,
                        )
                        try:
                            await self.__cache_db.start_matcher_run(
                                run_id=task.id,
                                started_at=start_time,
                                total_pairs=total_pairs,
                            )
                        except Exception:
                            logger.exception(
                                "Failed to mark matcher run as running for task %s",
                                task.id,
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
                        await self.__wait_for_tasks_idle({task_state.task.id})
                        await self.__finalize_task(task_state, state="cancelled")
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
                            await self.__wait_for_tasks_idle({task_state.task.id})
                            await self.__finalize_task(task_state, state="timed_out")
                            continue

                    try:
                        batch = await task_state.batch_iter.__anext__()
                    except StopAsyncIteration:
                        self.__active_tasks.pop(task_state.task.id, None)
                        await self.__wait_for_tasks_idle({task_state.task.id})
                        await self.__finalize_task(task_state, state="completed")
                        continue

                    if not batch:
                        active_tasks.append(task_state)
                        continue

                    self.__total_pairs_processed += len(batch)
                    task_state.processed_pairs += len(batch)
                    try:
                        await self.__cache_db.update_matcher_run_progress(
                            task_state.task.id,
                            processed_pairs=task_state.processed_pairs,
                        )
                    except Exception:
                        logger.exception(
                            "Failed to persist processed_pairs for task %s",
                            task_state.task.id,
                        )
                    while self.__matches.qsize() > num_processes * 2:
                        await asyncio.sleep(0.1)
                    self.__in_flight_by_task[task_state.task.id] = (
                        self.__in_flight_by_task.get(task_state.task.id, 0) + 1
                    )
                    self.__scheduled_batches_by_task[task_state.task.id] = (
                        self.__scheduled_batches_by_task.get(task_state.task.id, 0) + 1
                    )
                    task_id = task_state.task.id
                    future = loop.run_in_executor(
                        pool,
                        match_pairs,
                        task_id,
                        self.__matches,
                        log_queue,
                        self.__config.Matcher.Logging,
                        batch,
                        self.__config.Matcher.match_threshold,
                        task_state.matching_config,
                        task_state.task.matching_config_hash
                        or hash_matching_config(task_state.matching_config),
                    )

                    def _done_callback(_fut, done_task_id: int = task_id):
                        self.__decrement_in_flight(done_task_id)

                    future.add_done_callback(_done_callback)
                    parallel_tasks.append(future)
                    if len(parallel_tasks) >= num_processes:
                        await asyncio.gather(*parallel_tasks)
                        parallel_tasks = []

                    active_tasks.append(task_state)
                except Exception as e:
                    logger.error(f"Error fetching matches: {e}")
                    print(traceback.format_exc())
                    if task_state is not None:
                        self.__active_tasks.pop(task_state.task.id, None)
                        await self.__wait_for_tasks_idle({task_state.task.id})
                        await self.__finalize_task(
                            task_state, state="failed", error=str(e)
                        )
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
            stored_task_ids: list[int] = []
            while not self.__matches.empty():
                try:
                    task_id, processed_pairs, matches_batch = self.__matches.get(
                        block=False
                    )
                    if task_id in self.__scheduled_batches_by_task:
                        self.__scheduled_batches_by_task[task_id] -= 1
                        if self.__scheduled_batches_by_task[task_id] <= 0:
                            del self.__scheduled_batches_by_task[task_id]
                    self.__store_in_progress_by_task[task_id] = (
                        self.__store_in_progress_by_task.get(task_id, 0) + 1
                    )
                    stored_task_ids.append(task_id)
                    logger.debug(
                        f"Storing {len(matches_batch)} matches. ~{self.__matches.qsize()} batches remaining."
                    )
                    tasks.append(
                        self.__cache_db.store_matches_for_run(
                            task_id,
                            processed_pairs=processed_pairs,
                            matches=matches_batch,
                        )
                    )
                    self.__total_matches_found += len(matches_batch)
                    self.__matches_found_by_task[task_id] = (
                        self.__matches_found_by_task.get(task_id, 0)
                        + len(matches_batch)
                    )
                    try:
                        await self.__cache_db.update_matcher_run_matches_found(
                            task_id,
                            matches_found=self.__matches_found_by_task[task_id],
                        )
                    except Exception:
                        logger.exception(
                            "Failed to persist matches_found for task %s", task_id
                        )
                except Empty:
                    pass
            if tasks:
                match_ids = await asyncio.gather(*tasks)
                for task_id in stored_task_ids:
                    count = self.__store_in_progress_by_task.get(task_id, 0) - 1
                    if count <= 0:
                        self.__store_in_progress_by_task.pop(task_id, None)
                    else:
                        self.__store_in_progress_by_task[task_id] = count
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
                        self.__matching_tasks.append(
                            await self.__new_matching_task([], [], trigger="automated")
                        )
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
        config_route = APIRouter(
            prefix="/config", dependencies=[Depends(AccessChecker(self.__cache_db))]
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
            after_id: int = 0,
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
                after_id (int): Return matches with an id greater than this value. Defaults to 0.
                origin_uri (HttpUrl | None): Filter matches to only include matches from a specific origin.
                time_lte (float | None): Filter matches to only include matches with a timestamp less than or equal to the specified value.
                time_gte (float | None): Filter matches to only include matches with a timestamp greater than or equal to the specified value.
                assets (list[HttpUrl] | None): Filter matches to only include matches for the specified asset URLs.
                csaf_documents (list[HttpUrl] | None): Filter matches to only include matches for the specified CSAF document URLs.
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
            logger.info(f"Getting matches limit={limit} after_id={after_id}")
            matches = await self.__cache_db.get_matches(
                limit=limit,
                last_match_id=after_id,
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
                    matcher_run_id=match.matcher_run_id,
                    matching_config_hash=match.matching_config_hash,
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
                matcher_run_id=match.matcher_run_id,
                matching_config_hash=match.matching_config_hash,
            )

        @task_route.post("/start")
        async def start(
            assets: Annotated[list[HttpUrl] | None, Query()] = None,
            csaf_documents: Annotated[list[HttpUrl] | None, Query()] = None,
            body: StartMatchingTaskRequest | None = fastapi.Body(default=None),
        ):
            request_assets = (
                body.assets
                if body is not None and body.assets
                else (assets if assets is not None else [])
            )
            request_csaf_documents = (
                body.csaf_documents
                if body is not None and body.csaf_documents
                else (csaf_documents if csaf_documents is not None else [])
            )
            matching_config = copy.deepcopy(self.__matching_cfg_dict)
            has_custom_matching_config = False
            if body is not None and body.matching_config is not None:
                matching_config = self._merge_matching_config(
                    matching_config, body.matching_config
                )
                try:
                    matching_config = MatchingConfig.model_validate(
                        matching_config
                    ).model_dump()
                except ValidationError as e:
                    raise HTTPException(status_code=422, detail=str(e))
                has_custom_matching_config = True
            force_recompute = (
                body.force_recompute
                if body is not None and body.force_recompute is not None
                else has_custom_matching_config
            )
            logger.info("Starting matching task")
            task = await self.__new_matching_task(
                request_assets,
                request_csaf_documents,
                trigger="manual",
                matching_config=matching_config,
                force_recompute=force_recompute,
            )
            self.__matching_tasks.append(task)
            return {
                "id": task.task.id,
                "matching_config_hash": task.task.matching_config_hash,
                "force_recompute": task.task.force_recompute,
            }

        @task_route.get("/running")
        async def running_tasks(
            limit: int = 100,
            after_id: int = 0,
        ) -> list[MatchingTask]:
            tasks = [
                task for task in self.__active_tasks.values() if task.task.id > after_id
            ]
            tasks.sort(key=lambda task: task.task.id)
            if limit is not None:
                tasks = tasks[:limit]
            result: list[MatchingTask] = []
            for task in tasks:
                progress = None
                duration_seconds = max(time.time() - task.start_time, 0.0)
                if task.total_pairs > 0:
                    progress = min(task.processed_pairs / task.total_pairs, 1.0)
                result.append(
                    MatchingTask(
                        id=task.task.id,
                        assets=task.task.assets,
                        csaf_documents=task.task.csaf_documents,
                        trigger=task.task.trigger,
                        state="running",
                        created_at=task.task.created_at,
                        start_time=task.start_time,
                        duration_seconds=duration_seconds,
                        total_pairs=task.total_pairs,
                        processed_pairs=task.processed_pairs,
                        matches_found=self.__matches_found_by_task.get(task.task.id, 0),
                        progress=progress,
                        matching_config_hash=task.task.matching_config_hash,
                        force_recompute=task.task.force_recompute,
                    )
                )
            return result

        @task_route.get("/running/{task_id}")
        async def running_task(task_id: int) -> MatchingTask:
            task = self.__active_tasks.get(task_id)
            if task is None:
                raise HTTPException(status_code=404, detail="Task not found")
            progress = None
            duration_seconds = max(time.time() - task.start_time, 0.0)
            if task.total_pairs > 0:
                progress = min(task.processed_pairs / task.total_pairs, 1.0)
            return MatchingTask(
                id=task.task.id,
                assets=task.task.assets,
                csaf_documents=task.task.csaf_documents,
                trigger=task.task.trigger,
                state="running",
                created_at=task.task.created_at,
                start_time=task.start_time,
                duration_seconds=duration_seconds,
                total_pairs=task.total_pairs,
                processed_pairs=task.processed_pairs,
                matches_found=self.__matches_found_by_task.get(task.task.id, 0),
                progress=progress,
                matching_config_hash=task.task.matching_config_hash,
                force_recompute=task.task.force_recompute,
            )

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

        @task_route.get("/history")
        async def task_history(
            limit: int = 100,
            after_id: int = 0,
            state: str | None = None,
        ) -> list[MatchingTask]:
            runs = await self.__cache_db.get_matcher_runs(
                limit=limit, after_id=after_id, state=state
            )
            return [self._as_matching_task(run) for run in runs]

        @task_route.get("/history/{run_id}")
        async def task_history_get(run_id: int) -> MatchingTask:
            run = await self.__cache_db.get_matcher_run(run_id)
            if run is None:
                raise HTTPException(status_code=404, detail="Run not found")
            return self._as_matching_task(run)

        @task_route.post("/stop")
        async def stop(task_id: Annotated[int | None, Query()] = None):
            if task_id is None:
                logger.info("Stopping all matching tasks")
                pending = list(self.__matching_tasks)
                self.__matching_tasks.clear()
                await self.__cancel_pending_tasks(pending)
                self.__cancelled_task_ids.update(self.__active_tasks.keys())
                self.__matching_state = MatchingState.STOP_REQUESTED
                return {"stopped": "all"}

            removed_pending = False
            if self.__matching_tasks:
                remaining: deque[_QueuedMatchingTask] = deque()
                while self.__matching_tasks:
                    queued_task = self.__matching_tasks.popleft()
                    task = queued_task.task
                    if task.id == task_id:
                        removed_pending = True
                    else:
                        remaining.append(queued_task)
                self.__matching_tasks = remaining

            if removed_pending:
                logger.info(f"Cancelled pending task {task_id}")
                await self.__cache_db.finish_matcher_run(
                    task_id, state="cancelled", finished_at=time.time()
                )
                return {"stopped": "pending", "id": task_id}

            if task_id in self.__active_tasks:
                logger.info(f"Cancellation requested for active task {task_id}")
                self.__cancelled_task_ids.add(task_id)
                return {"stopped": "running", "id": task_id}

            raise HTTPException(status_code=404, detail="Task not found")

        @clear_route.post("/all")
        async def clean_all():
            """Stop all matching tasks, wait for pending batches, then clear all matcher caches."""
            pending = list(self.__matching_tasks)
            self.__matching_tasks.clear()
            await self.__cancel_pending_tasks(pending)
            self.__cancelled_task_ids.update(self.__active_tasks.keys())
            self.__matching_state = MatchingState.STOP_REQUESTED
            await self.__wait_for_tasks_idle(None)
            logger.info("Cleaning entire matcher cache")
            await self.__cache_db.clear()

        @clear_route.post("/matches")
        async def clean_matches():
            """Stop all matching tasks, wait for pending batches, then clear the matches cache."""
            pending = list(self.__matching_tasks)
            self.__matching_tasks.clear()
            await self.__cancel_pending_tasks(pending)
            self.__cancelled_task_ids.update(self.__active_tasks.keys())
            self.__matching_state = MatchingState.STOP_REQUESTED
            await self.__wait_for_tasks_idle(None)
            logger.info("Cleaning matcher matches cache")
            await self.__cache_db.clear_matches()

        @clear_route.post("/runs")
        async def clean_runs():
            """Clear matcher run history while keeping cached products and matches."""
            logger.info("Cleaning matcher run history")
            await self.__cache_db.clear_matcher_runs()

        @clear_route.post("/assets")
        async def clean_assets(origin_uri: HttpUrl):
            """Stop matching tasks for this origin, wait for pending batches, then clear assets for a specific origin."""
            affected_task_ids: set[int] = set()
            removed_pending_tasks: list[_QueuedMatchingTask] = []
            if self.__matching_tasks:
                remaining: deque[_QueuedMatchingTask] = deque()
                while self.__matching_tasks:
                    queued_task = self.__matching_tasks.popleft()
                    task = queued_task.task
                    if self._matches_origin(task.assets, origin_uri):
                        affected_task_ids.add(task.id)
                        removed_pending_tasks.append(queued_task)
                        continue
                    remaining.append(queued_task)
                self.__matching_tasks = remaining
            await self.__cancel_pending_tasks(removed_pending_tasks)
            for task_id, task in self.__active_tasks.items():
                if self._matches_origin(task.task.assets, origin_uri):
                    self.__cancelled_task_ids.add(task_id)
                    affected_task_ids.add(task_id)
            if affected_task_ids:
                await self.__wait_for_tasks_idle(affected_task_ids)
            logger.info("Cleaning matcher assets cache")
            await self.__cache_db.clear_assets(origin_uri)

        @clear_route.post("/csaf")
        async def clean_csaf(origin_uri: HttpUrl):
            """Stop matching tasks for this origin, wait for pending batches, then clear CSAF products for a specific origin."""
            affected_task_ids: set[int] = set()
            removed_pending_tasks: list[_QueuedMatchingTask] = []
            if self.__matching_tasks:
                remaining: deque[_QueuedMatchingTask] = deque()
                while self.__matching_tasks:
                    queued_task = self.__matching_tasks.popleft()
                    task = queued_task.task
                    if self._matches_origin(task.csaf_documents, origin_uri):
                        affected_task_ids.add(task.id)
                        removed_pending_tasks.append(queued_task)
                        continue
                    remaining.append(queued_task)
                self.__matching_tasks = remaining
            await self.__cancel_pending_tasks(removed_pending_tasks)
            for task_id, task in self.__active_tasks.items():
                if self._matches_origin(task.task.csaf_documents, origin_uri):
                    self.__cancelled_task_ids.add(task_id)
                    affected_task_ids.add(task_id)
            if affected_task_ids:
                await self.__wait_for_tasks_idle(affected_task_ids)
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

        @config_route.get("/")
        async def get_config() -> dict[str, Any]:
            """Return the current matcher configuration."""
            return {
                "Matcher": self.__config.Matcher.model_dump(mode="json"),
                "Cachedb": self.__config.Cachedb.model_dump(mode="json"),
            }

        @config_route.post("/")
        async def update_config(
            updates: Annotated[dict[str, Any], fastapi.Body(...)],
        ) -> dict[str, Any]:
            """Validate and persist matcher configuration updates."""
            with open(self.__config_path, "rb") as f:
                raw = tomllib.load(f)
            try:
                validate_update_prefixes(updates, {"Matcher", "Cachedb"})
            except ValueError as e:
                raise HTTPException(status_code=422, detail=str(e))
            try:
                validate_update_keys(Config, updates)
            except ValueError as e:
                raise HTTPException(status_code=422, detail=str(e))
            try:
                updated = apply_updates(raw, updates)
            except ValueError as e:
                raise HTTPException(status_code=422, detail=str(e))
            try:
                validated = Config.model_validate(updated)
            except ValidationError as e:
                raise HTTPException(status_code=422, detail=str(e))
            write_toml_file(self.__config_path, validated.model_dump(mode="json"))
            self.__config = validated
            return {
                "Matcher": self.__config.Matcher.model_dump(mode="json"),
                "Cachedb": self.__config.Cachedb.model_dump(mode="json"),
            }

        api.include_router(task_route)
        api.include_router(matches_route)
        api.include_router(sub_route)
        api.include_router(clear_route)
        api.include_router(config_route)

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

    @staticmethod
    def _matches_origin(uris: list[HttpUrl], origin_uri: HttpUrl) -> bool:
        """Return True if any URI matches the given origin, or list is empty (all)."""
        if not uris:
            return True
        origin = str(origin_uri).rstrip("/")
        return any(str(uri).startswith(origin) for uri in uris)

    def __decrement_in_flight(self, task_id: int) -> None:
        count = self.__in_flight_by_task.get(task_id, 0) - 1
        if count <= 0:
            self.__in_flight_by_task.pop(task_id, None)
        else:
            self.__in_flight_by_task[task_id] = count

    async def __cancel_pending_tasks(self, tasks: list[_QueuedMatchingTask]) -> None:
        if not tasks:
            return
        now = time.time()
        for queued_task in tasks:
            task = queued_task.task
            try:
                await self.__cache_db.finish_matcher_run(
                    task.id, state="cancelled", finished_at=now
                )
            except Exception:
                logger.exception("Failed to mark pending task %s as cancelled", task.id)

    async def __finalize_task(
        self,
        task: _ActiveMatchingTask,
        *,
        state: str,
        error: str | None = None,
    ) -> None:
        if state == "completed":
            # total_pairs already excludes skipped rows by design.
            task.processed_pairs = task.total_pairs
        matches_found = self.__matches_found_by_task.get(task.task.id, 0)
        finished_at = time.time()
        duration = max(finished_at - task.start_time, 0.0)

        logger.info(
            "Finished matching task id=%s state=%s trigger=%s "
            "processed_pairs=%s total_pairs=%s matches_found=%s duration=%.2fs",
            task.task.id,
            state,
            task.task.trigger,
            task.processed_pairs,
            task.total_pairs,
            matches_found,
            duration,
        )
        if error:
            logger.error("Matching task %s error: %s", task.task.id, error)

        try:
            await self.__cache_db.finish_matcher_run(
                task.task.id,
                state=state,
                finished_at=finished_at,
                processed_pairs=task.processed_pairs,
                matches_found=matches_found,
                error=error,
            )
        except Exception:
            logger.exception(
                "Failed to update matcher run history for task %s", task.task.id
            )

        self.__matches_found_by_task.pop(task.task.id, None)
        self.__in_flight_by_task.pop(task.task.id, None)
        self.__scheduled_batches_by_task.pop(task.task.id, None)
        self.__store_in_progress_by_task.pop(task.task.id, None)

    async def __wait_for_tasks_idle(self, task_ids: set[int] | None) -> None:
        """Wait until specified tasks have no in-flight or queued batches."""
        while True:
            logger.debug(
                f"Waiting for {task_ids} to finish processing: {self.__in_flight_by_task}"
            )
            if task_ids is None:
                no_active = not self.__active_tasks
                no_in_flight = not self.__in_flight_by_task
                no_queued = not self.__scheduled_batches_by_task
                store_idle = not self.__store_in_progress_by_task
                if no_active and no_in_flight and no_queued and store_idle:
                    return
            else:
                if all(
                    self.__in_flight_by_task.get(task_id, 0) == 0
                    and self.__scheduled_batches_by_task.get(task_id, 0) == 0
                    and self.__store_in_progress_by_task.get(task_id, 0) == 0
                    for task_id in task_ids
                ):
                    return
            await asyncio.sleep(0.1)


def match_pairs(
    task_id: int,
    matches: queue.Queue[tuple[int, list[tuple[int, int]], list[Match]]],
    log_queue: multiprocessing.Queue,
    logging_config: LoggingConfig,
    pairs: list[tuple[CsafProduct, Asset]],
    threshold: float,
    matching_config: dict[str, Any],
    matching_config_hash: str,
):
    configure_logging(logging_config, log_queue)
    logger.debug(f"Matching batch with {len(pairs)} pairs")
    batch = []
    processed_pairs: list[tuple[int, int]] = []
    for csaf, asset in pairs:
        if not (csaf and csaf.product and asset and asset.product):
            continue
        processed_pairs.append((csaf.id, asset.id))

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
        match.matcher_run_id = task_id
        match.matching_config_hash = matching_config_hash

        batch.append(match)
    matches.put((task_id, processed_pairs, batch))


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
