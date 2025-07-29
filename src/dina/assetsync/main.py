import asyncio
from pathlib import Path

from dina.cachedb.database import CacheDB
from dina.common.logging import configure_logging, get_logger
from dina.synchronizer.base import BaseSynchronizer

# Configure logging
configure_logging()

logger = get_logger(__name__)


class AssetSynchronizer(BaseSynchronizer):
    """
    Asset Manager implementation.

    This class extends the BaseManager to provide functionality specific to asset management.
    """

    def __init__(self):
        """
        Initialize the Asset Manager.
        """
        cache_db = CacheDB()
        super().__init__(
            cache_db, Path("./assets/plugin_configs/"), Path("./assets/assetsync.toml")
        )
        # TODO: Initialize connections to asset databases and the cache database.
        # TODO: Find the appropriate transformer plugins.



async def run_asset_manager():
    """Run the Asset Manager."""
    # Create and initialize the Asset Manager
    asset_manager = AssetSynchronizer()

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
        # Run the Asset Manager
        asyncio.run(run_asset_manager())
    except KeyboardInterrupt:
        logger.info("Asset Manager stopped by user")
    except Exception as e:
        logger.error(f"Asset Manager failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()
