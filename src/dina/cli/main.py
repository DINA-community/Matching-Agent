import asyncio

from dina.common.logging import configure_logging, get_logger

configure_logging()

logger = get_logger(__name__)


class CLI:
    def __init__(self):
        super().__init__()

    async def run(self):
        """Run the CLI."""
        pass


async def run_cli():
    """Run the CLI."""
    cli = CLI()

    try:
        await cli.run()

    except Exception as e:
        logger.error(f"CLI failed: {str(e)}")
        raise


def main():
    """Entry point for the Matcher."""
    try:
        # Run the Matcher
        asyncio.run(run_cli())
    except KeyboardInterrupt:
        logger.info("Matcher stopped by user")
    except Exception as e:
        logger.error(f"Matcher failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()
