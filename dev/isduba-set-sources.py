#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["httpx", "python-dotenv"]
# ///
"""
Adds sources to the ISDuBA instances via its REST API.

CSAF documents in `documents_dir` uploaded as single documents.

Optionally also configures default CSAF providers in ISDuBA.
Sources and the document age are read from dev/configuration/isduba-sources.json
Existing sources with the same name are skipped, so the script is safe to re-run at any time.
"""

import json
import sys
import time
from argparse import ArgumentParser
from functools import cache
from pathlib import Path
from typing import Any

import httpx
from dotenv import dotenv_values

REPO_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = REPO_ROOT / "dev/.env"
CONFIG_FILE = REPO_ROOT / "dev/configuration/isduba-sources.json"

# Keycloak needs to be up and the realm created by the keycloak-setup container
# this can take some time on a fresh start
KEYCLOAK_TIMEOUT = 120
# Similar for ISDuBA
ISDUBA_TIMEOUT = 120
TIMEOUT = httpx.Timeout(30.0)


def error(*args):
    print("[ERROR]", *args, file=sys.stderr)


def warning(*args):
    print("[WARNING]", *args, file=sys.stderr)


def info(*args):
    print("[INFO] ", *args, file=sys.stderr)


@cache
def _env() -> dict[str, str | None]:
    """Parse the env file once (cached)"""
    return dotenv_values(ENV_FILE)


def get_env(key: str, default: str = "") -> str:
    """Read a key from the env file"""
    value = _env().get(key)
    return default if value is None else value


def get_token(client: httpx.Client) -> str:
    """Wait for Keycloak and get a token"""
    keycloak_url = get_env("ISDUBA_CLIENT_KEYCLOAK_URL", "http://keycloak.localhost")
    realm = get_env("ISDUBA_CLIENT_KEYCLOAK_REALM", "isduba")
    url = f"{keycloak_url.rstrip('/')}/realms/{realm}/protocol/openid-connect/token"
    login_data = {
        "grant_type": "password",
        "client_id": get_env("ISDUBA_CLIENT_KEYCLOAK_CLIENT_ID", "auth"),
        "username": get_env("ISDUBA_CLIENT_USER", "user"),
        "password": get_env("ISDUBA_CLIENT_PASSWORD", "user"),
    }

    deadline = time.monotonic() + KEYCLOAK_TIMEOUT
    while True:
        try:
            response = client.post(url, data=login_data)
            if response.is_success and (token := response.json().get("access_token")):
                return token
        except httpx.HTTPError:
            pass  # not up yet
        if time.monotonic() >= deadline:
            error("Could not obtain an access token from Keycloak within the timeout")
            sys.exit(1)
        time.sleep(2)


def wait_for_isduba(client: httpx.Client, api: str):
    """Wait until the ISDuBA API answers"""
    deadline = time.monotonic() + ISDUBA_TIMEOUT
    while True:
        try:
            if client.get(f"{api}/sources").is_success:
                return
        except httpx.HTTPError:
            pass
        if time.monotonic() >= deadline:
            error("ISDuBA did not become ready within the timeout")
            sys.exit(1)
        time.sleep(2)


def feeds_from_pmd(pmd: dict[str, Any]) -> list[tuple[str, str]]:
    """Return label and URL of the feeds advertised in the PMD. Mirrors what the ISDuBA UI does
    https://github.com/ISDuBA/ISDuBA/blob/e5f0c58648ffaf74e83b3d5326943543e269e399/client/src/lib/Sources/source.ts#L256"""
    feeds = []
    for entry in pmd.get("distributions", []):
        for feed in (entry.get("rolie") or {}).get("feeds", []):
            url = feed.get("url", "")
            label = feed.get("summary") or " ".join(
                part for part in (feed.get("tlp_label", ""), url.rsplit("/", 1)[-1]) if part
            )
            feeds.append((label, url))
        if directory_url := entry.get("directory_url"):
            parts = [p for p in directory_url.split("/") if p]
            label = (parts[-1] if parts else "directory")
            # If a feed label (last part of the URI) is not unique, append `#` until the label is unique
            while label in {existing_label for existing_label, _ in feeds}:
                label += '#'
            feeds.append((label, directory_url))
    return feeds


def add_feeds(client: httpx.Client, api: str, source_id: int, url: str):
    """Discover feeds of a provider and register them"""
    response = client.get(f"{api}/pmd", params={"url": url})
    if not response.is_success:
        warning(
            f"--[SRC] Could not fetch PMD for '{url}' "
            f"(HTTP {response.status_code}): {response.text.strip()}. No feeds added."
        )
        return

    feeds = feeds_from_pmd(response.json())
    if not feeds:
        warning(f"--[SRC] No feeds found in PMD '{url}'.")
        return

    for label, feed_url in feeds:
        create_response = client.post(
            f"{api}/sources/{source_id}/feeds",
            data={"label": label, "url": feed_url, "log_level": ""},
        )
        if create_response.is_success:
            info(f"--[SRC]   Added feed '{label}'")
        else:
            warning(
                f"--[SRC]   Could not add feed '{label}' ({feed_url}) "
                f"(HTTP {create_response.status_code}): {create_response.text.strip()}"
            )


def create_sources(client: httpx.Client, api: str, config: dict[str, Any]):
    """Create the configured sources that do not exist yet"""
    default_age = config.get("default_age", "")

    sources_response = client.get(f"{api}/sources")
    existing = set()
    if sources_response.is_success:
        existing = {src.get("name") for src in sources_response.json().get("sources", [])}

    for source in config.get("sources", []):
        name, url = source.get("name"), source.get("url")
        if not name or not url:
            continue
        if name in existing:
            info(f"--[SRC] Source '{name}' already exists, skipping.")
            continue

        info(f"--[SRC] Creating source '{name}' ({url})")
        source_data = {"name": name, "url": url}
        if default_age:
            source_data["age"] = default_age

        created = client.post(f"{api}/sources", data=source_data)
        if not created.is_success:
            warning(f"--[SRC] Could not create source '{name}' (HTTP {created.status_code}): {created.text.strip()}")
            continue

        source_id = created.json().get("id")
        if source_id is None:
            warning(f"--[SRC] Unexpected response while creating source '{name}': {created.text.strip()}")
            continue

        add_feeds(client, api, source_id, url)

        # Activate the source
        updated_response = client.put(
            f"{api}/sources/{source_id}", data={"active": "true", "attention": "false"}
        )
        if updated_response.is_success:
            info(f"--[SRC] Source '{name}' activated.")
        else:
            warning(f"--[SRC] Could not activate source '{name}'.")


def import_documents(client: httpx.Client, api: str, config: dict[str, Any]):
    """Import local CSAF in ISDuBA"""
    documents_dir = config.get("documents_dir", "")
    if not documents_dir:
        return

    directory = Path(documents_dir)
    if not directory.is_absolute():
        directory = REPO_ROOT / directory
    if not directory.is_dir():
        warning(f"--[DOC] documents_dir '{documents_dir}' does not exist, skipping document import.")
        return

    info(f"--[DOC] Importing CSAF documents from '{documents_dir}'...")
    for path in sorted(directory.rglob("*.json")):
        with path.open("rb") as handle:
            response = client.post(f"{api}/documents", files={"file": (path.name, handle)})
        if response.status_code not in (httpx.codes.CREATED, httpx.codes.CONFLICT):
            warning(f"--[DOC] Could not import {path.name} (HTTP {response.status_code}): {response.text.strip()}")
    info("--[DOC] Document import done.")


def main() -> int:
    parser = ArgumentParser('isduba-set-sources',
                            description=__doc__)
    parser.add_argument('--configure-sources', action='store_true',
                        help='Also configure and activate CSAF providers as sources in ISDuBA')
    args = parser.parse_args()

    if not ENV_FILE.is_file():
        error(f"{ENV_FILE.relative_to(REPO_ROOT)} not found. Run ./dev/start-local-env.sh first.")
        return 1
    if not CONFIG_FILE.is_file():
        error(f"{CONFIG_FILE.relative_to(REPO_ROOT)} not found. Run ./dev/start-local-env.sh first.")
        return 1

    info("--Configuring ISDuBA providers.")
    config = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))

    isduba_url = get_env("ISDUBA_CLIENT_HOSTNAME_URL", "http://isduba.localhost")
    isduba_api = f"{isduba_url.rstrip('/')}/api"

    with httpx.Client(timeout=TIMEOUT) as client:
        token = get_token(client)
        client.headers["Authorization"] = f"Bearer {token}"
        wait_for_isduba(client, isduba_api)

        if args.configure_sources:
            create_sources(client, isduba_api, config)
        import_documents(client, isduba_api, config)

    info("--ISDuBA provider setup finished")
    return 0


if __name__ == "__main__":
    sys.exit(main())
