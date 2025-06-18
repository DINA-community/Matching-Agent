import asyncio
import sys

from csaf_matcher.common.logging import configure_logging, get_logger
from csaf_matcher.manager.base import BaseManager

# Configure logging
configure_logging()

logger = get_logger(__name__)


class CSAFManager(BaseManager):
    """
    Asset Manager implementation.

    This class extends the BaseManager to provide functionality specific to asset management.
    """

    def __init__(self):
        """
        Initialize the Asset Manager.
        """
        super().__init__()
        # TODO: Initialize connections to asset databases and the cache database.
        # TODO: Find the appropriate transformer plugins.


async def run_csaf_manager():
    """Run the Asset Manager."""
    # Create and initialize the Asset Manager
    asset_manager = CSAFManager()

    try:
        # Run the Asset Manager pipeline
        await asset_manager.run()

        logger.info("Asset Manager completed successfully")
    except Exception as e:
        logger.error(f"Asset Manager failed: {str(e)}")
        raise
    finally:
        # TODO: Do cleanup
        pass


def main():
    """Entry point for the Asset Manager."""
    try:
        # Run the Asset Manager
        asyncio.run(run_csaf_manager())
    except KeyboardInterrupt:
        logger.info("Asset Manager stopped by user")
    except Exception as e:
        logger.error(f"Asset Manager failed: {str(e)}")
        sys.exit(1)
