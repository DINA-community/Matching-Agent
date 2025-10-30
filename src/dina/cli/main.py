import argparse
import asyncio
import tomllib
from pathlib import Path

from dina.cachedb.database import CacheDB
from dina.common.log import configure_logging, get_logger

configure_logging()

logger = get_logger(__name__)


class CLI:
    def __init__(self):
        super().__init__()
        self.parser = self._build_parser()

    def _build_parser(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(
            prog="dina-cli",
            description="DINA command-line utilities",
        )
        subparsers = parser.add_subparsers(dest="command", required=True)

        # user subcommands
        user_parser = subparsers.add_parser("user", help="User management commands")
        user_sub = user_parser.add_subparsers(dest="user_command", required=True)

        create = user_sub.add_parser("create", help="Create or update a user")
        create.add_argument("--username", "-u", required=True, help="Username")
        create.add_argument(
            "--password", "-p", required=True, help="Password (plain text)"
        )
        create.set_defaults(active=True)
        create.add_argument(
            "--config",
            "-c",
            type=Path,
            default=Path("./assets/assetsync.toml"),
            help="Path to TOML config containing a [Cachedb] section",
        )

        return parser

    async def run(self):
        """Run the CLI."""
        args = self.parser.parse_args()
        if args.command == "user" and args.user_command == "create":
            await self._cmd_user_create(
                config_path=args.config,
                username=args.username,
                password=args.password,
            )
        else:
            self.parser.error("Unknown command")

    @staticmethod
    def _load_cachedb_config(config_path: Path) -> CacheDB.Config:
        try:
            with config_path.open("rb") as f:
                data = tomllib.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Config file not found: {config_path}. Use --config to specify the path."
            )
        if "Cachedb" not in data or not isinstance(data["Cachedb"], dict):
            raise ValueError(
                f"Config file '{config_path}' does not contain a [Cachedb] section"
            )
        return CacheDB.Config(**data["Cachedb"])

    async def _cmd_user_create(
        self, *, config_path: Path, username: str, password: str
    ) -> None:
        # Load DB config
        config = self._load_cachedb_config(config_path)

        cache_db = CacheDB()
        try:
            await cache_db.connect(config)
            await cache_db.create_user(username, password)
        finally:
            await cache_db.disconnect()


async def run_cli():
    """Run the CLI."""
    cli = CLI()

    try:
        await cli.run()

    except Exception as e:
        logger.error(f"CLI failed: {str(e)}")
        raise


def main():
    """Entry point for the CLI."""
    try:
        asyncio.run(run_cli())
    except KeyboardInterrupt:
        logger.info("CLI stopped by user")
    except Exception as e:
        logger.error(f"CLI failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()
