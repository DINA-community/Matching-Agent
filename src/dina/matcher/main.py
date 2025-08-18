import asyncio

import uvicorn
from fastapi import FastAPI, APIRouter

from dina.common.logging import configure_logging, get_logger

# Configure logging
configure_logging()

logger = get_logger(__name__)


class Matcher:
    def __init__(self):
        """
        Initialize the Matcher.
        """

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

        config = uvicorn.Config(app=api, host="0.0.0.0", port=8998)
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
