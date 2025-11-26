import asyncio
from pathlib import Path
import argparse

from dina.cachedb.database import CacheDB
from dina.common.log import configure_logging, get_logger
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

    def __init__(self, config_path: Path = Path("./assets/csafsync.toml")):
        """
        Initialize the CSAF Manager.
        """
        cache_db = CacheDB()
        super().__init__(
            cache_db,
            config_path,
        )
        # Configure logging
        configure_logging(self.config.Logging)


async def run_csaf_manager(config_path: Path = Path("./assets/csafsync.toml")):
    """Run the CSAF Manager."""
    # Create and initialize the CSAF Manager
    csaf_manager = CSAFSynchronizer(config_path=config_path)

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
        parser = argparse.ArgumentParser(description="Run the CSAF Synchronizer")
        parser.add_argument(
            "--config",
            type=Path,
            default=Path("./assets/csafsync.toml"),
            help="Path to CSAF synchronizer configuration TOML file",
        )
        args = parser.parse_args()

        # Run the CSAF Manager
        asyncio.run(run_csaf_manager(config_path=args.config))
    except KeyboardInterrupt:
        logger.info("CSAF Manager stopped by user")
    except Exception as e:
        logger.error(f"CSAF Manager failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()
