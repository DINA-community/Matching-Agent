import argparse
import asyncio
import tomllib
from pathlib import Path
from typing import Any

import httpx

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
            "--password",
            "-p",
            required=False,
            help="Password (omit to be prompted securely)",
        )
        create.set_defaults(active=True)
        create.add_argument(
            "--config",
            "-c",
            type=Path,
            default=Path("./assets/assetsync.toml"),
            help="Path to TOML config containing a [Cachedb] section",
        )

        # matcher subcommands
        matcher = subparsers.add_parser("matcher", help="Interact with Matcher API")
        self._add_common_api_args(matcher)
        matcher_sub = matcher.add_subparsers(dest="matcher_command", required=True)

        # matcher token
        matcher_token = matcher_sub.add_parser("token", help="Obtain access token")
        matcher_token.set_defaults(action="matcher_token")

        # matcher matches group
        matcher_matches = matcher_sub.add_parser("matches", help="Query matches")
        matches_sub = matcher_matches.add_subparsers(
            dest="matcher_matches_command", required=True
        )

        matches_list = matches_sub.add_parser("list", help="List matches")
        matches_list.add_argument("--limit", type=int, default=100)
        matches_list.add_argument("--offset", type=int, default=0)
        matches_list.add_argument("--origin-uri", type=str)
        matches_list.add_argument("--time-lte", type=float)
        matches_list.add_argument("--time-gte", type=float)
        matches_list.add_argument(
            "--assets",
            nargs="*",
            help="List of asset URLs to filter by",
        )
        matches_list.add_argument(
            "--csaf-documents",
            nargs="*",
            help="List of CSAF document URLs to filter by",
        )
        matches_list.add_argument("--threshold", type=float)
        matches_list.set_defaults(action="matcher_matches_list")

        matches_get = matches_sub.add_parser("get", help="Get a single match")
        matches_get.add_argument("id", type=int, help="Match ID")
        matches_get.set_defaults(action="matcher_matches_get")

        # matcher task group
        matcher_task = matcher_sub.add_parser("task", help="Control matching task")
        task_sub = matcher_task.add_subparsers(
            dest="matcher_task_command", required=True
        )

        task_start = task_sub.add_parser("start", help="Start a matching task")
        task_start.add_argument(
            "--assets",
            type=int,
            nargs="*",
            help="Asset IDs to match",
        )
        task_start.add_argument(
            "--csaf-products",
            type=int,
            nargs="*",
            help="CSAF product IDs to match",
        )
        task_start.set_defaults(action="matcher_task_start")

        task_status = task_sub.add_parser("status", help="Get matcher status")
        task_status.set_defaults(action="matcher_task_status")

        task_stop = task_sub.add_parser("stop", help="Stop the matcher")
        task_stop.set_defaults(action="matcher_task_stop")

        # matcher clear group
        matcher_clear = matcher_sub.add_parser("clear", help="Clear caches")
        clear_sub = matcher_clear.add_subparsers(
            dest="matcher_clear_command", required=True
        )

        clear_all = clear_sub.add_parser("all", help="Clear all caches")
        clear_all.set_defaults(action="matcher_clear_all")

        clear_matches = clear_sub.add_parser("matches", help="Clear matches cache")
        clear_matches.set_defaults(action="matcher_clear_matches")

        clear_assets = clear_sub.add_parser("assets", help="Clear assets cache")
        clear_assets.add_argument("--origin-uri", required=True)
        clear_assets.set_defaults(action="matcher_clear_assets")

        clear_csaf = clear_sub.add_parser("csaf", help="Clear CSAF cache")
        clear_csaf.add_argument("--origin-uri", required=True)
        clear_csaf.set_defaults(action="matcher_clear_csaf")

        # synchronizer subcommands (generic for any sync service base URL)
        sync = subparsers.add_parser(
            "sync", help="Interact with a Synchronizer API (asset or CSAF)"
        )
        self._add_common_api_args(sync)
        sync_sub = sync.add_subparsers(dest="sync_command", required=True)

        sync_token = sync_sub.add_parser("token", help="Obtain access token")
        sync_token.set_defaults(action="sync_token")

        sync_task = sync_sub.add_parser("task", help="Control synchronization task")
        sync_task_sub = sync_task.add_subparsers(
            dest="sync_task_command", required=True
        )
        sync_start = sync_task_sub.add_parser("start", help="Start sync run")
        sync_start.set_defaults(action="sync_task_start")
        sync_status = sync_task_sub.add_parser("status", help="Sync status")
        sync_status.set_defaults(action="sync_task_status")

        return parser

    async def run(self):
        """Run the CLI."""
        args = self.parser.parse_args()
        if args.command == "user" and args.user_command == "create":
            # Prompt for password if not provided
            resolved_pwd = self._resolve_password(getattr(args, "password", None))
            await self._cmd_user_create(
                config_path=args.config,
                username=args.username,
                password=resolved_pwd,
            )
        elif args.command == "matcher":
            await self._dispatch_matcher(args)
        elif args.command == "sync":
            await self._dispatch_sync(args)
        else:
            self.parser.error("Unknown command")

    # ------------- helpers -------------
    def _add_common_api_args(self, p: argparse.ArgumentParser) -> None:
        p.add_argument(
            "--base-url",
            required=True,
            help="Base URL of the API, e.g., http://localhost:8000",
        )
        p.add_argument("--username", "-u", required=True)
        p.add_argument(
            "--password",
            "-p",
            required=False,
            help="Password (omit to be prompted securely)",
        )

    @staticmethod
    def _resolve_password(pwd: str | None) -> str:
        """Return provided password or interactively prompt for one.

        Uses getpass to avoid echoing the password on the terminal.
        """
        if pwd is not None and pwd != "":
            return pwd
        import getpass

        return getpass.getpass("Password: ")

    async def _get_token(self, base_url: str, username: str, password: str) -> str:
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(
                f"{base_url.rstrip('/')}/token",
                data={"username": username, "password": password},
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            resp.raise_for_status()
            data = resp.json()
            if not isinstance(data, dict) or "access_token" not in data:
                raise RuntimeError("Unexpected token response")
            return str(data["access_token"])

    def _auth_headers(self, token: str) -> dict[str, str]:
        return {"Authorization": f"Bearer {token}"}

    @staticmethod
    def _print_json(data: Any) -> None:
        # Avoid additional dependency; use built-in print of dict/list
        import json

        print(json.dumps(data, indent=2, ensure_ascii=False))

    # ------------- matcher commands -------------
    async def _dispatch_matcher(self, args: argparse.Namespace) -> None:
        base = args.base_url
        resolved_pwd = self._resolve_password(getattr(args, "password", None))
        if getattr(args, "action", None) == "matcher_token":
            token = await self._get_token(base, args.username, resolved_pwd)
            print(token)
            return

        token = await self._get_token(base, args.username, resolved_pwd)
        headers = self._auth_headers(token)

        async with httpx.AsyncClient(timeout=60.0, headers=headers) as client:
            action = getattr(args, "action", None)
            if action == "matcher_matches_list":
                params: dict[str, Any] = {
                    "limit": args.limit,
                    "offset": args.offset,
                }
                if args.origin_uri:
                    params["origin_uri"] = args.origin_uri
                if args.time_lte is not None:
                    params["time_lte"] = args.time_lte
                if args.time_gte is not None:
                    params["time_gte"] = args.time_gte
                if args.assets:
                    params["assets"] = args.assets
                if args.csaf_documents:
                    params["csaf_documents"] = args.csaf_documents
                if args.threshold is not None:
                    params["threshold"] = args.threshold

                resp = await client.get(f"{base.rstrip('/')}/matches/", params=params)
                resp.raise_for_status()
                self._print_json(resp.json())

            elif action == "matcher_matches_get":
                resp = await client.get(
                    f"{base.rstrip('/')}/matches/{args.id}",
                )
                resp.raise_for_status()
                self._print_json(resp.json())

            elif action == "matcher_task_start":
                qparams: dict[str, Any] = {}
                if args.assets:
                    qparams["assets"] = args.assets
                if args.csaf_products:
                    qparams["csaf_products"] = args.csaf_products
                resp = await client.post(
                    f"{base.rstrip('/')}/task/start", params=qparams
                )
                resp.raise_for_status()
                print("Started.")

            elif action == "matcher_task_status":
                resp = await client.get(f"{base.rstrip('/')}/task/status")
                resp.raise_for_status()
                self._print_json(resp.json())

            elif action == "matcher_task_stop":
                resp = await client.post(f"{base.rstrip('/')}/task/stop")
                resp.raise_for_status()
                print("Stop requested.")

            elif action == "matcher_clear_all":
                resp = await client.post(f"{base.rstrip('/')}/clear/all")
                resp.raise_for_status()
                print("Cleared all caches.")

            elif action == "matcher_clear_matches":
                resp = await client.post(f"{base.rstrip('/')}/clear/matches")
                resp.raise_for_status()
                print("Cleared matches cache.")

            elif action == "matcher_clear_assets":
                resp = await client.post(
                    f"{base.rstrip('/')}/clear/assets",
                    params={"origin_uri": args.origin_uri},
                )
                resp.raise_for_status()
                print("Cleared assets cache.")

            elif action == "matcher_clear_csaf":
                resp = await client.post(
                    f"{base.rstrip('/')}/clear/csaf",
                    params={"origin_uri": args.origin_uri},
                )
                resp.raise_for_status()
                print("Cleared CSAF cache.")

            else:
                self.parser.error("Unknown matcher command")

    # ------------- synchronizer commands -------------
    async def _dispatch_sync(self, args: argparse.Namespace) -> None:
        base = args.base_url
        resolved_pwd = self._resolve_password(getattr(args, "password", None))
        if getattr(args, "action", None) == "sync_token":
            token = await self._get_token(base, args.username, resolved_pwd)
            print(token)
            return

        token = await self._get_token(base, args.username, resolved_pwd)
        headers = self._auth_headers(token)

        async with httpx.AsyncClient(timeout=60.0, headers=headers) as client:
            action = getattr(args, "action", None)
            if action == "sync_task_start":
                resp = await client.post(f"{base.rstrip('/')}/task/start")
                resp.raise_for_status()
                print("Synchronization start requested.")

            elif action == "sync_task_status":
                resp = await client.get(f"{base.rstrip('/')}/task/status")
                resp.raise_for_status()
                self._print_json(resp.json())

            else:
                self.parser.error("Unknown sync command")

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
