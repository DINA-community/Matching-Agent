import asyncio
from pathlib import Path

from dina.cachedb.database import CacheDB
from dina.common.logging import configure_logging, get_logger
from dina.synchronizer.base import BaseSynchronizer
import sys

logger = get_logger(__name__)

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class CSAFSynchronizer(BaseSynchronizer):
    """
    CSAF Manager implementation.

    This class extends the BaseManager to provide functionality specific to CSAF management.
    """

    def __init__(self):
        """
        Initialize the CSAF Manager.
        """
        cache_db = CacheDB()
        super().__init__(
            cache_db,
            Path("./assets/csafsync.toml"),
        )
        # Configure logging
        configure_logging(self.config.Logging)


async def run_csaf_manager():
    """Run the CSAF Manager."""
    # Create and initialize the CSAF Manager
    csaf_manager = CSAFSynchronizer()

    try:
        await csaf_manager.setup()
        # Run the CSAF Manager pipeline
        await csaf_manager.run()

        logger.info("CSAF Manager completed successfully")
    except Exception as e:
        logger.error(f"CSAF Manager failed: {str(e)}")
        raise
    finally:
        await csaf_manager.cleanup()


def main():
    """Entry point for the CSAF Manager."""
    try:
        # Run the CSAF Manager
        asyncio.run(run_csaf_manager())
    except KeyboardInterrupt:
        logger.info("CSAF Manager stopped by user")
    except Exception as e:
        logger.error(f"CSAF Manager failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()
