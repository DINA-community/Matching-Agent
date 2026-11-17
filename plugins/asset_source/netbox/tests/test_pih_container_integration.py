"""Read real D3C identifiers and use them to match a CSAF document."""

import queue
from datetime import UTC, datetime
from unittest.mock import AsyncMock

import httpx
import pytest
from dina.plugins.datasource.isduba.isduba import process_document
from dina.plugins.datasource.netbox.netbox import NetboxDataSource
from netbox_integration import MANAGE, execute
from pydantic import HttpUrl

from dina.cachedb.fetcher_view import FetcherView
from dina.matcher.main import match_pairs
from dina.synchronizer.plugin_base.data_source import DataSourceConfig, DataSourcePlugin


@pytest.mark.integration
async def test_d3c_identifiers_reach_matcher(netbox: str, netbox_client: httpx.Client, monkeypatch: pytest.MonkeyPatch) -> None:
    execute(
        netbox,
        "netbox",
        MANAGE
        + [
            "shell",
            "-c",
            """
from dcim.models import DeviceType, Manufacturer
from d3c.models import FileHash, Hash, Software, XGenericUri

manufacturer = Manufacturer.objects.create(name="PIH vendor", slug="pih-vendor")
cases = [
    ("matching", "sha256", "abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789", "urn:vendor", "https://example.org/A"),
    ("hash-only", "sha256", "abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789", "urn:vendor", "https://example.org/a"),
    ("uri-only", "sha512", "abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0123456789", "urn:vendor", "https://example.org/A"),
    ("different", "sha256", "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef", "urn:other", "https://example.org/A"),
]
for name, algorithm, value, namespace, uri in cases:
    software = Software.objects.create(name=name, manufacturer=manufacturer)
    file = Hash.objects.create(software=software, filename="installed.bin")
    FileHash.objects.create(hash=file, algorithm=algorithm, value=value)
    XGenericUri.objects.create(content_object=software, namespace=namespace, uri=uri)

missing = Software.objects.create(name="missing", manufacturer=manufacturer)
device_type = DeviceType.objects.create(
    id=missing.id, manufacturer=manufacturer, model="PIH device", slug="pih-device"
)

XGenericUri.objects.create(
    content_object=device_type, namespace="urn:vendor", uri="https://example.org/A"
)
""",
        ],
    )

    plugin_config = NetboxDataSource.Config(
        api_url=HttpUrl(str(netbox_client.base_url)),
        api_token=netbox_client.headers["Authorization"].removeprefix("Bearer "),
    )
    data_source_config = DataSourceConfig(plugin_name="netbox", publish_matches=False, Plugin=plugin_config)
    datasource = NetboxDataSource(DataSourcePlugin.Config(DataSource=data_source_config))
    # Create mock cache db
    view = AsyncMock(spec=FetcherView)
    view.last_run.return_value = datetime(2000, 1, 1, tzinfo=UTC)
    view.get_existing.return_value = []

    async with datasource.client:
        fetched = await datasource.fetch_products(view)
    assert len(fetched.data) == 5  # the 5 software records created above, including the "missing" one

    document = {
        "document": {"title": "PIH regression", "csaf_version": "2.0"},
        "product_tree": {
            "branches": [
                {
                    "category": "product_name",
                    "name": "Example product",
                    "product": {
                        "name": "Example product",
                        "product_id": "affected-product",
                        "product_identification_helper": {
                            "hashes": [
                                {
                                    "filename": "advisory.bin",
                                    "file_hashes": [
                                        {
                                            "algorithm": "SHA256",
                                            "value": "ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789",
                                        }
                                    ],
                                }
                            ],
                            "x_generic_uris": [
                                {
                                    "namespace": "urn:vendor",
                                    "uri": "https://example.org/A",
                                }
                            ],
                        },
                    },
                }
            ],
        },
    }
    csaf = process_document({"id": 55}, document, "https://fake.origin")[0]
    csaf.id = 11
    pairs = []
    names = {}
    for asset in fetched.data:
        asset.id = asset.origin_info["software_id"]
        names[asset.id] = asset.product.name
        pairs.append((csaf, asset))

    for threshold in [0.0, 75.0]:
        output = queue.Queue()
        match_pairs(
            task_id=1,
            matches=output,
            log_queue=None,
            logging_config=None,
            pairs=pairs,
            threshold=threshold,
            # Only use our hashes and URIs for matching
            matching_config={"database": {"other_fields": {"hashes": 1.0, "x_generic_uris": 1.0}}},
            matching_config_hash="pih-test",
        )
        _task_id, _processed_pairs, matches = output.get_nowait()
        scores = {}
        for match in matches:
            scores[names[match.asset_id]] = match.score
        if threshold == 0.0:
            assert scores == pytest.approx({
                "matching": 100.0,
                "hash-only": 50.0,
                "uri-only": 50.0,
                "different": 0.0,
                "missing": 0.0,
            })
        else:
            assert scores == pytest.approx({"matching": 100.0})
