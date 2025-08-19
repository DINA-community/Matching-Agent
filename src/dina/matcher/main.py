import asyncio
import tomllib

import uvicorn
from fastapi import FastAPI, APIRouter

from dina.common.logging import configure_logging, get_logger

# Configure logging
configure_logging()

logger = get_logger(__name__)


class MatcherConfig:
    def __init__(self, config):
        self.__config = config
        try:
            self.__config["Matcher"]["Api"]["host"]
        except KeyError:
            raise KeyError("Missing required configuration parameter Matcher.Api.host")
        try:
            self.__config["Matcher"]["Api"]["port"]
        except KeyError:
            raise KeyError("Missing required configuration parameter Matcher.Api.port")

    @property
    def api_host(self):
        return self.__config["Matcher"]["Api"]["host"]

    @property
    def api_port(self):
        return self.__config["Matcher"]["Api"]["port"]


class Matcher:
    def __init__(self):
        """
        Initialize the Matcher.
        """
        with open("./assets/matcher.toml", "rb") as f:
            self.__config = MatcherConfig(tomllib.load(f))

    async def run(self):
        """Run the matcher."""
        async with asyncio.TaskGroup() as tg:
            tg.create_task(self.__serve_api())

    async def __serve_api(self):
        api = FastAPI()

        task_route = APIRouter(prefix="/task")

        @task_route.put("/start")
        async def start():
            logger.info("Starting matching task")

        @task_route.get("/status")
        async def status():
            return {"status": "running"}

        @task_route.put("/stop")
        async def stop():
            logger.info("Stopping matching task")

        api.include_router(task_route)

        config = uvicorn.Config(
            app=api, host=self.__config.api_host, port=self.__config.api_port
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
