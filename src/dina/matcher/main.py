import asyncio
import datetime
import time
import tomllib
import traceback

import uvicorn
from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl

from dina.cachedb.database import CacheDB
from dina.cachedb.model import Match
from dina.common.logging import configure_logging, get_logger
import sys

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
    csaf_origin: str
    asset_origin: str
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


class Matcher:
    class Config(BaseModel):
        Matcher: MatcherConfig

    def __init__(self):
        """
        Initialize the Matcher.
        """
        with open("./assets/matcher.toml", "rb") as f:
            self.__config = Matcher.Config.model_validate(tomllib.load(f))
        self.__cache_db = CacheDB()
        self.__last_synchronization: float | None = None

    async def run(self):
        """Run the matcher."""
        await self.__cache_db.connect(self.__config.Matcher.Cachedb)
        async with asyncio.TaskGroup() as tg:
            tg.create_task(self.__serve_api())
            tg.create_task(self.__matching_task())

    async def __matching_task(self):
        while True:
            if (
                self.__last_synchronization is None
                or self.__last_synchronization + self.__config.Matcher.sync_interval
                < time.time()
            ):
                try:
                    async for csaf, asset in self.__cache_db.fetch_pairs():
                        matches = []
                        match = Match()
                        match.asset_id = asset.id
                        match.csaf_product_id = csaf.id
                        match.score = 100
                        match.timestamp = datetime.datetime.now().timestamp()
                        match.status = ""
                        matches.append(match)
                        await self.__cache_db.store_matches(matches)
                except Exception as e:
                    logger.error(f"Error fetching matches: {e}")
                    print(traceback.format_exc())

                self.__last_synchronization = time.time()
            else:
                await asyncio.sleep(1)

    async def __serve_api(self):
        api = FastAPI()

        sub_route = APIRouter(prefix="/subscribe")
        task_route = APIRouter(prefix="/task")
        matches_route = APIRouter(prefix="/matches")

        @matches_route.get("/")
        async def get_matches() -> list[APIMatch]:
            logger.info("Getting matches")
            return [
                APIMatch(
                    id=match.id,
                    csaf_origin=match.csaf_product.origin_uri,
                    asset_origin=match.asset.origin_uri,
                    timestamp=match.timestamp,
                    score=match.score,
                    status=match.status,
                )
                for match in await self.__cache_db.get_matches()
            ]

        @matches_route.get("/{match_id}")
        async def get_match(match_id: int) -> APIMatch:
            logger.info(f"Getting match {match_id}")
            match = await self.__cache_db.get_match(match_id)
            if match is None:
                raise HTTPException(status_code=404, detail="Match not found")
            return APIMatch(
                id=match.id,
                csaf_origin=match.csaf_product.origin_uri,
                asset_origin=match.asset.origin_uri,
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
