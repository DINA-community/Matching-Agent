import asyncio

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
