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


class AssetSynchronizer(BaseSynchronizer):
    """
    Asset Manager implementation.

    This class extends the BaseManager to provide functionality specific to asset management.
    """

    def __init__(self, config_path: Path = Path("./assets/assetsync.toml")):
        """
        Initialize the Asset Manager.
        """
        cache_db = CacheDB()
        super().__init__(
            cache_db,
            config_path,
            root_path="/assetsync",
        )
        # Configure logging
        configure_logging(self.config.Logging)


async def run_asset_manager(config_path: Path = Path("./assets/assetsync.toml")):
    """Run the Asset Manager."""
    # Create and initialize the Asset Manager
    asset_manager = AssetSynchronizer(config_path=config_path)

    try:
        await asset_manager.setup()
        # Run the Asset Manager pipeline
        await asset_manager.run()

        logger.info("Asset Manager completed successfully")
    except Exception as e:
        logger.error(f"Asset Manager failed: {str(e)}")
        raise
    finally:
        await asset_manager.cleanup()


def main():
    """Entry point for the Asset Manager."""
    try:
        parser = argparse.ArgumentParser(description="Run the Asset Synchronizer")
        parser.add_argument(
            "--config",
            type=Path,
            default=Path("./assets/assetsync.toml"),
            help="Path to asset synchronizer configuration TOML file",
        )
        args = parser.parse_args()

        # Run the Asset Manager
        asyncio.run(run_asset_manager(config_path=args.config))
    except KeyboardInterrupt:
        logger.info("Asset Manager stopped by user")
    except Exception as e:
        logger.error(f"Asset Manager failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()
