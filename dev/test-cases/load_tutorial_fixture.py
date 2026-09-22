"""Create or update tutorial data through NetBox's REST API.

Run with:
    NETBOX_TOKEN='<token>' uv run dev/test-cases/load_tutorial_fixture.py
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

import httpx

Record = dict[str, Any]
FIXTURE = Path(__file__).with_name("tutorial-1.fixture.json")


class ImportFailure(RuntimeError):
    """Raised when the fixture cannot be loaded."""


class NetBoxApi:
    """Minimal client for the NetBox endpoints used below."""

    def __init__(self, url: str, token: str) -> None:
        self.client = httpx.Client(
            base_url=f"{url.rstrip('/')}/api/",
            headers={"Authorization": f"Bearer {token}"},
            timeout=30.0,
        )

    def close(self) -> None:
        self.client.close()

    def list(self, endpoint: str) -> list[Record]:
        records: list[Record] = []
        url: str | None = endpoint
        while url:
            response = self.request("GET", url, params={"limit": 1000})
            page = response.json()
            records.extend(page["results"])
            url = page["next"]
        return records

    def create(self, endpoint: str, values: Record) -> Record:
        return self.request("POST", endpoint, json=values).json()

    def update(self, endpoint: str, record_id: int, values: Record) -> Record:
        return self.request("PATCH", f"{endpoint}{record_id}/", json=values).json()

    def request(self, method: str, url: str, **kwargs: Any) -> httpx.Response:
        try:
            response = self.client.request(method, url, **kwargs)
            response.raise_for_status()
            return response
        except httpx.HTTPError as error:
            detail = ""
            if isinstance(error, httpx.HTTPStatusError):
                detail = f": {error.response.text}"
            raise ImportFailure(f"{method} {url} failed{detail}") from error


def relation_id(value: Any) -> int:
    """Return the ID from a NetBox relation."""
    if isinstance(value, dict):
        return int(value["id"])
    return int(value)


def matches(value: Any, expected: Any) -> bool:
    """Compare a NetBox response value with a value sent to the API."""
    if isinstance(expected, dict):
        return isinstance(value, dict) and all(
            key in value and matches(value[key], child)
            for key, child in expected.items()
        )
    if isinstance(value, dict):
        if "id" in value and isinstance(expected, int):
            value = value["id"]
        elif "value" in value:
            value = value["value"]
    return value == expected


def upsert(
    api: NetBoxApi,
    endpoint: str,
    current: Record | None,
    values: Record,
) -> Record:
    """Create a missing record or update an existing one."""
    if current is None:
        return api.create(endpoint, values)
    if any(not matches(current.get(key), value) for key, value in values.items()):
        return api.update(endpoint, current["id"], values)
    return current


def fields(item: Record, names: tuple[str, ...]) -> Record:
    return {name: item[name] for name in names}


def load_fixture(api: NetBoxApi, fixture: Record) -> None:
    """Load fixture sections in dependency order."""
    simple_sections = (
        ("sites", "dcim/sites/", ("name", "slug", "status", "description")),
        ("device_roles", "dcim/device-roles/", ("name", "slug", "description")),
        ("manufacturers", "dcim/manufacturers/", ("name", "slug", "description")),
    )
    simple_records: dict[str, dict[str, Record]] = {}
    for section, endpoint, names in simple_sections:
        records = {item["name"]: item for item in api.list(endpoint)}
        for item in fixture[section]:
            records[item["name"]] = upsert(
                api, endpoint, records.get(item["name"]), fields(item, names)
            )
        simple_records[section] = records

    site_ids = {name: item["id"] for name, item in simple_records["sites"].items()}
    role_ids = {
        name: item["id"] for name, item in simple_records["device_roles"].items()
    }
    manufacturer_ids = {
        name: item["id"] for name, item in simple_records["manufacturers"].items()
    }

    endpoint = "dcim/device-types/"
    device_types = {
        (relation_id(item["manufacturer"]), item["model"]): item
        for item in api.list(endpoint)
    }
    for item in fixture["device_types"]:
        key = manufacturer_ids[item["manufacturer"]], item["model"]
        values = fields(
            item,
            (
                "model",
                "slug",
                "part_number",
                "description",
                "comments",
                "custom_fields",
            ),
        )
        values["manufacturer"] = key[0]
        device_types[key] = upsert(api, endpoint, device_types.get(key), values)
    device_type_ids = {key: item["id"] for key, item in device_types.items()}

    endpoint = "dcim/devices/"
    devices = {item["name"]: item for item in api.list(endpoint)}
    for item in fixture["devices"]:
        values = fields(item, ("name", "description", "custom_fields"))
        values.update(
            role=role_ids[item["role"]],
            device_type=device_type_ids[
                manufacturer_ids[item["device_type_manufacturer"]],
                item["device_type"],
            ],
            site=site_ids[item["site"]],
        )
        devices[item["name"]] = upsert(api, endpoint, devices.get(item["name"]), values)
    device_ids = {name: item["id"] for name, item in devices.items()}

    endpoint = "dcim/module-types/"
    module_types = {
        (relation_id(item["manufacturer"]), item["model"]): item
        for item in api.list(endpoint)
    }
    for item in fixture["module_types"]:
        key = manufacturer_ids[item["manufacturer"]], item["model"]
        values = fields(item, ("model", "part_number", "description"))
        values["manufacturer"] = key[0]
        module_types[key] = upsert(api, endpoint, module_types.get(key), values)
    module_type_ids = {key: item["id"] for key, item in module_types.items()}

    endpoint = "dcim/module-bays/"
    module_bays = {
        (relation_id(item["device"]), item["name"]): item for item in api.list(endpoint)
    }
    for item in fixture["module_bays"]:
        key = device_ids[item["device"]], item["name"]
        values = fields(item, ("name", "label", "position", "description"))
        values["device"] = key[0]
        module_bays[key] = upsert(api, endpoint, module_bays.get(key), values)
    module_bay_ids = {key: item["id"] for key, item in module_bays.items()}

    endpoint = "dcim/modules/"
    modules = {relation_id(item["module_bay"]): item for item in api.list(endpoint)}
    for item in fixture["modules"]:
        module_bay_id = module_bay_ids[device_ids[item["device"]], item["module_bay"]]
        values = fields(item, ("description", "status"))
        values.update(
            device=device_ids[item["device"]],
            module_bay=module_bay_id,
            module_type=module_type_ids[
                manufacturer_ids[item["module_type_manufacturer"]],
                item["module_type"],
            ],
        )
        modules[module_bay_id] = upsert(
            api, endpoint, modules.get(module_bay_id), values
        )

    endpoint = "plugins/d3c/software-list/"
    software = {
        (relation_id(item["manufacturer"]), item["name"], item["version"]): item
        for item in api.list(endpoint)
    }
    for item in fixture["software"]:
        key = (
            manufacturer_ids[item["manufacturer"]],
            item["name"],
            item["version"],
        )
        values = fields(item, ("name", "version", "is_firmware", "cpe", "purl"))
        values["manufacturer"] = key[0]
        software[key] = upsert(api, endpoint, software.get(key), values)
    software_ids = {key: item["id"] for key, item in software.items()}

    def related_object(descriptor: Record) -> tuple[str, int]:
        if descriptor["kind"] == "device":
            return "dcim.device", device_ids[descriptor["name"]]
        if descriptor["kind"] == "software":
            key = (
                manufacturer_ids[descriptor["manufacturer"]],
                descriptor["name"],
                descriptor["version"],
            )
            return "d3c.software", software_ids[key]
        raise ImportFailure(f"Unknown relationship kind: {descriptor['kind']}")

    endpoint = "plugins/d3c/productrelationship-list/"
    relationships: dict[tuple[Any, ...], Record] = {}
    for item in api.list(endpoint):
        category = item["category"]
        if isinstance(category, dict):
            category = category.get("value", category)
        source_type = item["source_type"]
        if isinstance(source_type, dict):
            source_type = source_type.get("value", source_type)
        destination_type = item["destination_type"]
        if isinstance(destination_type, dict):
            destination_type = destination_type.get("value", destination_type)
        key = (
            source_type,
            item["source_id"],
            category,
            destination_type,
            item["destination_id"],
        )
        relationships[key] = item

    for item in fixture["product_relationships"]:
        source_type, source_id = related_object(item["source"])
        destination_type, destination_id = related_object(item["destination"])
        key = (
            source_type,
            source_id,
            item["category"],
            destination_type,
            destination_id,
        )
        values = {
            "source_type": source_type,
            "source_id": source_id,
            "category": item["category"],
            "destination_type": destination_type,
            "destination_id": destination_id,
        }
        relationships[key] = upsert(api, endpoint, relationships.get(key), values)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--url", default=os.environ.get("NETBOX_URL", "http://localhost:8800")
    )
    return parser.parse_args()


def main() -> int:
    token = os.environ.get("NETBOX_TOKEN")
    if not token:
        print("ERROR: Set NETBOX_TOKEN to a NetBox API token.", file=sys.stderr)
        return 2

    api = NetBoxApi(parse_arguments().url, token)
    try:
        fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        load_fixture(api, fixture)
    except (ImportFailure, KeyError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    finally:
        api.close()

    print("Tutorial fixture loaded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
