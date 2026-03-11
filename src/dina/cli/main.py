import argparse
import asyncio
import tomllib
from pathlib import Path
from typing import Any, cast

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
            prog="csaf_matcher_cli",
            description="DINA command-line utilities",
        )
        parser.add_argument(
            "--json",
            action="store_true",
            help="Output machine-readable JSON",
        )
        # Allow passing common API args at the root level (before selecting a group)
        # These are optional here; we'll validate when dispatching a specific group.
        self._add_common_api_args(parser)
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
            default=Path("./assets/config.toml"),
            help="Path to TOML config containing a [Cachedb] section",
        )

        # matcher subcommands
        matcher = subparsers.add_parser("matcher", help="Interact with Matcher API")
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
        matches_list.add_argument(
            "--after-id",
            type=int,
            default=0,
            help="Return matches with an id greater than this value",
        )
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
            nargs="*",
            help="Asset URLs to match",
        )
        task_start.add_argument(
            "--csaf-documents",
            nargs="*",
            help="CSAF document URLs to match",
        )
        task_start.set_defaults(action="matcher_task_start")

        task_status = task_sub.add_parser("status", help="Get matcher status")
        task_status.set_defaults(action="matcher_task_status")

        task_running = task_sub.add_parser(
            "running", help="List running matching tasks"
        )
        task_running.add_argument("--limit", type=int, default=100)
        task_running.add_argument("--after-id", type=int, default=0)
        task_running.set_defaults(action="matcher_task_running")

        task_running_get = task_sub.add_parser(
            "running-get", help="Get a single running matching task"
        )
        task_running_get.add_argument("id", type=int, help="Task ID")
        task_running_get.set_defaults(action="matcher_task_running_get")

        task_history = task_sub.add_parser("history", help="List past matching runs")
        task_history.add_argument("--limit", type=int, default=100)
        task_history.add_argument("--after-id", type=int, default=0)
        task_history.add_argument(
            "--state",
            type=str,
            help="Optional run state filter (e.g. running, completed, cancelled)",
        )
        task_history.set_defaults(action="matcher_task_history")

        task_history_get = task_sub.add_parser(
            "history-get", help="Get a single historical matching run"
        )
        task_history_get.add_argument("id", type=int, help="Run ID")
        task_history_get.set_defaults(action="matcher_task_history_get")

        task_stop = task_sub.add_parser("stop", help="Stop the matcher")
        task_stop.add_argument("--task-id", type=int, help="Stop a specific task")
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

        clear_runs = clear_sub.add_parser("runs", help="Clear matcher run history")
        clear_runs.set_defaults(action="matcher_clear_runs")

        clear_assets = clear_sub.add_parser("assets", help="Clear assets cache")
        clear_assets.add_argument("--origin-uri", required=True)
        clear_assets.set_defaults(action="matcher_clear_assets")

        clear_csaf = clear_sub.add_parser("csaf", help="Clear CSAF cache")
        clear_csaf.add_argument("--origin-uri", required=True)
        clear_csaf.set_defaults(action="matcher_clear_csaf")

        # matcher config group
        matcher_config = matcher_sub.add_parser("config", help="View or update config")
        matcher_config.add_argument(
            "--get",
            action="store_true",
            help="Get matcher configuration",
        )
        matcher_config.add_argument(
            "--set",
            dest="updates",
            action="append",
            default=[],
            help="Update value (key=value). Use dotted keys for nested fields.",
        )
        matcher_config.set_defaults(action="matcher_config")

        # synchronizer subcommands (generic for any sync service base URL)
        sync = subparsers.add_parser(
            "sync", help="Interact with a Synchronizer API (asset or CSAF)"
        )
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

        sync_config = sync_sub.add_parser("config", help="View or update config")
        sync_config.add_argument(
            "--get",
            action="store_true",
            help="Get synchronizer configuration",
        )
        sync_config.add_argument(
            "--set",
            dest="updates",
            action="append",
            default=[],
            help="Update value (key=value). Use dotted keys for nested fields.",
        )
        sync_config.set_defaults(action="sync_config")

        return parser

    async def run(self):
        """Run the CLI."""
        args = self.parser.parse_args()
        self._output_json = bool(getattr(args, "json", False))
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
        """Add common API arguments without making them parser-required.

        We validate their presence in the dispatch functions so callers can supply
        them at the root level (before command/group).
        """
        p.add_argument(
            "--base-url",
            required=False,
            help="Base URL of the API, e.g., http://localhost:8000",
        )
        p.add_argument("--username", "-u", required=False)
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
        async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
            resp = await client.post(
                f"{base_url.rstrip('/')}/token",
                data={"username": username, "password": password},
                headers={"Content-Type": "application/x-www-form-urlencoded"},
            )
            self._raise_for_status(resp, "auth")
            data = resp.json()
            if not isinstance(data, dict) or "access_token" not in data:
                raise RuntimeError("Unexpected token response")
            return str(data["access_token"])

    def _raise_for_status(self, resp: httpx.Response, context: str) -> None:
        if resp.status_code < 400:
            return
        detail = ""
        try:
            payload = resp.json()
            if isinstance(payload, dict) and "detail" in payload:
                detail = str(payload["detail"])
        except Exception:
            detail = resp.text.strip()
        if resp.status_code == 401:
            msg = "Unauthorized. Check username/password."
        elif resp.status_code == 403:
            msg = "Forbidden. The account lacks permission."
        elif resp.status_code == 404:
            msg = "Not found. Check the ID or endpoint."
        elif resp.status_code == 409:
            msg = "Conflict. The request could not be completed."
        elif resp.status_code == 422:
            msg = "Unprocessable entity. Check parameter types."
        elif resp.status_code >= 500:
            msg = "Server error. Try again or check server logs."
        else:
            msg = f"HTTP {resp.status_code}"
        if detail:
            msg = f"{msg} ({detail})"
        raise RuntimeError(f"{context} failed: {msg}")

    def _auth_headers(self, token: str) -> dict[str, str]:
        return {"Authorization": f"Bearer {token}"}

    @staticmethod
    def _parse_update_value(raw: str) -> Any:
        lowered = raw.lower()
        if lowered in ("true", "false"):
            return lowered == "true"
        if lowered in ("null", "none"):
            return None
        if raw.startswith(("{", "[", '"')):
            import json

            try:
                return json.loads(raw)
            except json.JSONDecodeError:
                pass
        try:
            return int(raw)
        except ValueError:
            pass
        try:
            return float(raw)
        except ValueError:
            pass
        return raw

    def _parse_updates(self, updates: list[str]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for item in updates:
            if "=" not in item:
                raise RuntimeError(f"Invalid update '{item}'. Use key=value.")
            key, raw = item.split("=", 1)
            key = key.strip()
            if not key:
                raise RuntimeError(f"Invalid update '{item}'. Use key=value.")
            result[key] = self._parse_update_value(raw.strip())
        return result

    @staticmethod
    def _print_json(data: Any) -> None:
        # Avoid additional dependency; use built-in print of dict/list
        import json

        print(json.dumps(data, indent=2, ensure_ascii=False))

    def _format_value(self, value: Any, indent: int = 0) -> str:
        pad = "  " * indent
        if isinstance(value, dict):
            if not value:
                return "{}"
            lines = []
            for key, val in value.items():
                formatted = self._format_value(val, indent + 1)
                if "\n" in formatted:
                    lines.append(f"{pad}{key}:\n{formatted}")
                else:
                    lines.append(f"{pad}{key}: {formatted}")
            return "\n".join(lines)
        if isinstance(value, list):
            if not value:
                return "[]"
            # If list of dicts, show each item as a block
            if all(isinstance(item, dict) for item in value):
                blocks = []
                for idx, item in enumerate(value, start=1):
                    blocks.append(f"{pad}- [{idx}]")
                    blocks.append(self._format_value(item, indent + 1))
                return "\n".join(blocks)
            # Simple list
            items = ", ".join(self._format_value(item, 0) for item in value)
            return f"[{items}]"
        if isinstance(value, str):
            return value
        if value is None:
            return "null"
        return str(value)

    def _print_output(self, data: Any, *, force_json: bool = False) -> None:
        if force_json or self._output_json:
            self._print_json(data)
            return
        print(self._format_value(data))

    # ------------- matcher commands -------------
    async def _dispatch_matcher(self, args: argparse.Namespace) -> None:
        # Validate required auth/base options (can be provided at root or group level)
        missing: list[str] = []
        base = getattr(args, "base_url", None)
        if not base:
            missing.append("--base-url")
        username = getattr(args, "username", None)
        if not username:
            missing.append("-u/--username")
        if missing:
            self.parser.error(
                "Missing required options for matcher: "
                + ", ".join(missing)
                + ". Pass them before 'matcher'."
            )
        # mypy: after validation, treat as str
        base = cast(str, base)
        username = cast(str, username)
        resolved_pwd = self._resolve_password(getattr(args, "password", None))
        if getattr(args, "action", None) == "matcher_token":
            token = await self._get_token(base, username, resolved_pwd)
            print(token)
            return

        token = await self._get_token(base, username, resolved_pwd)
        headers = self._auth_headers(token)

        async with httpx.AsyncClient(
            timeout=60.0, headers=headers, follow_redirects=True
        ) as client:
            action = getattr(args, "action", None)
            if action == "matcher_matches_list":
                params: dict[str, Any] = {
                    "limit": args.limit,
                    "after_id": args.after_id,
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
                self._raise_for_status(resp, "matches list")
                self._print_output(resp.json())

            elif action == "matcher_matches_get":
                resp = await client.get(
                    f"{base.rstrip('/')}/matches/{args.id}",
                )
                self._raise_for_status(resp, "match get")
                self._print_output(resp.json())

            elif action == "matcher_task_start":
                qparams: dict[str, Any] = {}
                if args.assets:
                    qparams["assets"] = args.assets
                if args.csaf_documents:
                    qparams["csaf_documents"] = args.csaf_documents
                resp = await client.post(
                    f"{base.rstrip('/')}/task/start", params=qparams
                )
                self._raise_for_status(resp, "task start")
                print("Started.")

            elif action == "matcher_task_status":
                resp = await client.get(f"{base.rstrip('/')}/task/status")
                self._raise_for_status(resp, "task status")
                self._print_output(resp.json())

            elif action == "matcher_task_running":
                params = {"limit": args.limit, "after_id": args.after_id}
                resp = await client.get(
                    f"{base.rstrip('/')}/task/running", params=params
                )
                self._raise_for_status(resp, "task running")
                self._print_output(resp.json())

            elif action == "matcher_task_running_get":
                resp = await client.get(f"{base.rstrip('/')}/task/running/{args.id}")
                self._raise_for_status(resp, "task running get")
                self._print_output(resp.json())

            elif action == "matcher_task_history":
                params: dict[str, Any] = {
                    "limit": args.limit,
                    "after_id": args.after_id,
                }
                if args.state:
                    params["state"] = args.state
                resp = await client.get(
                    f"{base.rstrip('/')}/task/history", params=params
                )
                self._raise_for_status(resp, "task history")
                self._print_output(resp.json())

            elif action == "matcher_task_history_get":
                resp = await client.get(f"{base.rstrip('/')}/task/history/{args.id}")
                self._raise_for_status(resp, "task history get")
                self._print_output(resp.json())

            elif action == "matcher_task_stop":
                params = {}
                if args.task_id is not None:
                    params["task_id"] = args.task_id
                resp = await client.post(f"{base.rstrip('/')}/task/stop", params=params)
                self._raise_for_status(resp, "task stop")
                print("Stop requested.")

            elif action == "matcher_clear_all":
                resp = await client.post(f"{base.rstrip('/')}/clear/all")
                self._raise_for_status(resp, "clear all")
                print("Cleared all caches.")

            elif action == "matcher_clear_matches":
                resp = await client.post(f"{base.rstrip('/')}/clear/matches")
                self._raise_for_status(resp, "clear matches")
                print("Cleared matches cache.")

            elif action == "matcher_clear_runs":
                resp = await client.post(f"{base.rstrip('/')}/clear/runs")
                self._raise_for_status(resp, "clear runs")
                print("Cleared matcher run history.")

            elif action == "matcher_clear_assets":
                resp = await client.post(
                    f"{base.rstrip('/')}/clear/assets",
                    params={"origin_uri": args.origin_uri},
                )
                self._raise_for_status(resp, "clear assets")
                print("Cleared assets cache.")

            elif action == "matcher_clear_csaf":
                resp = await client.post(
                    f"{base.rstrip('/')}/clear/csaf",
                    params={"origin_uri": args.origin_uri},
                )
                self._raise_for_status(resp, "clear csaf")
                print("Cleared CSAF cache.")

            elif action == "matcher_config":
                if not args.get and not args.updates:
                    raise RuntimeError("config requires --get or --set")
                if args.get:
                    resp = await client.get(f"{base.rstrip('/')}/config")
                    self._raise_for_status(resp, "config get")
                    self._print_output(resp.json())
                if args.updates:
                    updates = self._parse_updates(args.updates)
                    resp = await client.post(
                        f"{base.rstrip('/')}/config",
                        json=updates,
                    )
                    self._raise_for_status(resp, "config set")
                    self._print_output(resp.json())

            else:
                self.parser.error("Unknown matcher command")

    # ------------- synchronizer commands -------------
    async def _dispatch_sync(self, args: argparse.Namespace) -> None:
        # Validate required auth/base options (can be provided at root or group level)
        missing: list[str] = []
        base = getattr(args, "base_url", None)
        if not base:
            missing.append("--base-url")
        username = getattr(args, "username", None)
        if not username:
            missing.append("-u/--username")
        if missing:
            self.parser.error(
                "Missing required options for sync: "
                + ", ".join(missing)
                + ". Pass them before 'sync'."
            )
        base = cast(str, base)
        username = cast(str, username)
        resolved_pwd = self._resolve_password(getattr(args, "password", None))
        if getattr(args, "action", None) == "sync_token":
            token = await self._get_token(base, username, resolved_pwd)
            print(token)
            return

        token = await self._get_token(base, username, resolved_pwd)
        headers = self._auth_headers(token)

        async with httpx.AsyncClient(
            timeout=60.0, headers=headers, follow_redirects=True
        ) as client:
            action = getattr(args, "action", None)
            if action == "sync_task_start":
                resp = await client.post(f"{base.rstrip('/')}/task/start")
                self._raise_for_status(resp, "sync start")
                print("Synchronization start requested.")

            elif action == "sync_task_status":
                resp = await client.get(f"{base.rstrip('/')}/task/status")
                self._raise_for_status(resp, "sync status")
                self._print_output(resp.json())

            elif action == "sync_config":
                if not args.get and not args.updates:
                    raise RuntimeError("config requires --get or --set")
                if args.get:
                    resp = await client.get(f"{base.rstrip('/')}/config")
                    self._raise_for_status(resp, "config get")
                    self._print_output(resp.json())
                if args.updates:
                    updates = self._parse_updates(args.updates)
                    resp = await client.post(
                        f"{base.rstrip('/')}/config",
                        json=updates,
                    )
                    self._raise_for_status(resp, "config set")
                    self._print_output(resp.json())

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

        cache_db = CacheDB(config)
        try:
            await cache_db.connect()
            await cache_db.create_user(username, password)
        finally:
            await cache_db.disconnect()


async def run_cli():
    """Run the CLI."""
    cli = CLI()

    try:
        await cli.run()

    except RuntimeError as e:
        logger.error(str(e))
        raise SystemExit(1)

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
