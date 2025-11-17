import httpx
from datetime import datetime, timezone
from unittest.mock import AsyncMock, MagicMock
from pydantic import HttpUrl
import pytest

from dina.cachedb.database import Asset, Match, Product, CsafProduct
from dina.cachedb.fetcher_view import FetcherView
from dina.cachedb.model import ProductType
from dina.synchronizer.plugin_base.data_source import (
    DataSourceConfig,
    DataSourcePlugin,
    FetchProductsResult,
    FetchRelationshipsResult,
    Relationship,
    MappedRelationship,
    ProductId,
)
from dina.plugins.datasource.netbox.netbox import NetboxDataSource
from dina.plugins.datasource.netbox.generated.api_client.models.device_type_custom_fields import (
    DeviceTypeCustomFields,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def mock_config():
    """Creates a fake plugin configuration for tests."""
    plugin_data = NetboxDataSource.Config(
        api_url=HttpUrl("https://fake.netbox"),
        api_token="fake-token",
    )
    ds_cfg = DataSourceConfig(
        plugin_name="netbox",
        publish_matches=False,
        Plugin=plugin_data,
    )
    datasource = DataSourcePlugin.Config(DataSource=ds_cfg)
    return NetboxDataSource(datasource)


# ---------------------------------------------------------------------------
# Basic config and helper tests
# ---------------------------------------------------------------------------


def test_endpoint_info(mock_config):
    """Checks that endpoint_info returns the expected API URL."""
    assert mock_config.endpoint_info() == "https://fake.netbox/"


def test_validate_response_raises():
    """Ensures validate_response raises a RuntimeError on None input."""
    from dina.plugins.datasource.netbox.netbox import validate_response

    with pytest.raises(RuntimeError):
        validate_response(None)


def test_find_cachedb_type():
    """Tests type mapping from NetBox to cachedb types."""
    from dina.plugins.datasource.netbox.netbox import find_cachedb_type, ProductType

    assert find_cachedb_type("dcim.device") == ProductType.Device
    assert find_cachedb_type("d3c.software") == ProductType.Software
    assert find_cachedb_type("unknown") == ProductType.Undefined


@pytest.mark.parametrize(
    "origin_info,expected",
    [
        ({"device_id": 42}, "/api/dcim/devices/42/"),
        ({"software_id": 99}, "/api/plugins/d3c/software/99/"),
        ({"relation_id": 123}, "/api/plugins/d3c/productrelationship-list/123/"),
        ({}, ""),
        ({"device_id": "not_a_number"}, ""),
    ],
)
def test_build_resource_path(mock_config, origin_info, expected):
    """Verifies resource path generation for different origin_info inputs."""
    result = mock_config.build_resource_path(origin_info)
    assert result == expected


# ---------------------------------------------------------------------------
# fetch_products
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_fetch_products(monkeypatch, mock_config):
    """Ensures fetch_products creates correct Asset objects from fake data."""
    fetcher_view = MagicMock(spec=FetcherView)
    fetcher_view.last_run = AsyncMock(return_value=datetime.now(timezone.utc))
    fetcher_view.get_existing = AsyncMock(return_value=[])

    class DummyListResult:
        def __init__(self, results):
            self.results = results

    DummyDevice = MagicMock()
    DummyDevice.id = 1
    DummyDevice.name = "Device A"
    DummyDevice.serial = "123"
    DummyDevice.device_type = MagicMock(id=10)
    DummyDevice.device_type.manufacturer = MagicMock(id=100)

    DummyDeviceType = MagicMock(id=10)
    DummyDeviceType.model = "Type X"
    DummyDeviceType.manufacturer = MagicMock(id=100)
    DummyDeviceType.custom_fields = DeviceTypeCustomFields()
    DummyDeviceType.custom_fields.additional_properties = {
        "model_number": "MN-1",
        "hardware_name": "HW-X",
        "hardware_version": "v1.0",
        "device_family": "Family-A",
        "cpe": "cpe:/a:vendor:product:1.0",
    }

    DummyManufacturer = MagicMock(id=100)
    DummyManufacturer.name = "FakeVendor"

    # Mock NetBox API calls
    monkeypatch.setattr(
        "dina.plugins.datasource.netbox.netbox.dcim_devices_list.asyncio",
        AsyncMock(return_value=DummyListResult([DummyDevice])),
    )
    monkeypatch.setattr(
        "dina.plugins.datasource.netbox.netbox.dcim_device_types_list.asyncio",
        AsyncMock(return_value=DummyListResult([DummyDeviceType])),
    )
    monkeypatch.setattr(
        "dina.plugins.datasource.netbox.netbox.dcim_manufacturers_list.asyncio",
        AsyncMock(return_value=DummyListResult([DummyManufacturer])),
    )
    monkeypatch.setattr(
        "dina.plugins.datasource.netbox.netbox.plugins_d3c_software_list_list.asyncio",
        AsyncMock(return_value=DummyListResult([])),
    )

    result: FetchProductsResult = await mock_config.fetch_products(fetcher_view)

    assert isinstance(result, FetchProductsResult)
    assert len(result.data) == 1
    asset = result.data[0]
    assert asset.product.name == "Device A"
    assert asset.product.manufacturer_name == "FakeVendor"
    assert asset.product.model == "Type X"
    assert asset.product.device_family == "Family-A"
    assert asset.product.cpe.startswith("cpe:/a:")


# ---------------------------------------------------------------------------
# cleanup_products
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_cleanup_products_returns_delete(monkeypatch, mock_config):
    """Ensures cleanup_products marks assets for deletion when none exist remotely."""

    class DummyListResult:
        def __init__(self, results):
            self.results = results

    monkeypatch.setattr(
        "dina.plugins.datasource.netbox.netbox.dcim_devices_list.asyncio",
        AsyncMock(return_value=DummyListResult([])),
    )
    monkeypatch.setattr(
        "dina.plugins.datasource.netbox.netbox.plugins_d3c_software_list_list.asyncio",
        AsyncMock(return_value=DummyListResult([])),
    )

    dummy_asset = MagicMock()
    dummy_asset.id = 1
    dummy_asset.product.product_type = "Device"
    dummy_asset.origin_info = {"device_id": 123}

    result = await mock_config.cleanup_products([dummy_asset])

    assert isinstance(result, list)
    assert all(r.can_delete for r in result)


# ---------------------------------------------------------------------------
# notify_new_matches
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_notify_new_matches_success(monkeypatch, mock_config):
    """Verifies that notify_new_matches triggers the async API call once."""
    fake_async_create = AsyncMock()
    monkeypatch.setattr(
        "dina.plugins.datasource.netbox.netbox.plugins_csaf_csafmatch_list_create.asyncio",
        fake_async_create,
    )

    fake_asset = Asset(product=Product(), origin_info={"device_id": 42})
    fake_csaf = CsafProduct(uri="https://example.com/csaf.json")

    match = Match(asset=fake_asset, csaf_product=fake_csaf)
    await mock_config.notify_new_matches([match])

    fake_async_create.assert_awaited_once()


@pytest.mark.asyncio
async def test_notify_new_matches_http_error(monkeypatch, mock_config, caplog):
    """Ensures notify_new_matches logs an error if an HTTPError occurs."""
    fake_async_create = AsyncMock(side_effect=httpx.HTTPError("network fail"))
    monkeypatch.setattr(
        "dina.plugins.datasource.netbox.netbox.plugins_csaf_csafmatch_list_create.asyncio",
        fake_async_create,
    )

    fake_asset = Asset(product=Product(), origin_info={"device_id": 123})
    fake_csaf = CsafProduct(uri="https://fake.doc/csaf.json")

    match = Match(asset=fake_asset, csaf_product=fake_csaf)
    await mock_config.notify_new_matches([match])

    assert "Failed to notify new matches" in caplog.text


# ---------------------------------------------------------------------------
# fetch_relationships
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_fetch_relationships(monkeypatch, mock_config):
    """Ensures fetch_relationships correctly returns Relationship objects."""

    class DummyRelation:
        def __init__(self, id, source_id, destination_id):
            self.id = id
            self.source_id = source_id
            self.destination_id = destination_id
            self.source_type = "dcim.device"
            self.destination_type = "d3c.software"

    class DummyListResult:
        def __init__(self, results):
            self.results = results

    dummy_relations = DummyListResult([DummyRelation(1, 1, 2)])

    monkeypatch.setattr(
        "dina.plugins.datasource.netbox.netbox.plugins_d3c_productrelationship_list_list.asyncio",
        AsyncMock(return_value=dummy_relations),
    )
    monkeypatch.setattr(
        "dina.plugins.datasource.netbox.netbox.validate_response",
        lambda x: x,
    )

    fetcher_view = MagicMock()
    fetcher_view.last_run = AsyncMock(return_value=datetime.now(timezone.utc))

    result = await mock_config.fetch_relationships(fetcher_view)

    assert isinstance(result, FetchRelationshipsResult)
    assert not result.again
    assert all(isinstance(r, Relationship) for r in result.data)
    assert result.data[0].parent.id == 1
    assert result.data[0].child.id == 2


# ---------------------------------------------------------------------------
# map_relationships
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_map_relationships_basic(monkeypatch, mock_config):
    """Ensures map_relationships maps relationships to existing Assets correctly."""
    fetcher_view = MagicMock()
    fake_devices = [
        MagicMock(id=100, origin_info={"device_id": 1}),
        MagicMock(id=200, origin_info={"device_id": 2}),
    ]
    fake_software = [
        MagicMock(id=300, origin_info={"software_id": 10}),
        MagicMock(id=400, origin_info={"software_id": 20}),
    ]
    fetcher_view.get_existing = AsyncMock(side_effect=[fake_devices, fake_software])

    relations = [
        Relationship(
            parent=ProductId(1, ProductType.Device),
            child=ProductId(10, ProductType.Software),
            ty=Asset,
            origin_info={"relation_id": 111},
        ),
        Relationship(
            parent=ProductId(2, ProductType.Device),
            child=ProductId(20, ProductType.Software),
            ty=Asset,
            origin_info={"relation_id": 222},
        ),
    ]

    result = await mock_config.map_relationships(fetcher_view, relations)

    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(r, MappedRelationship) for r in result)
    assert {r.parent for r in result} == {100, 200}
    assert {r.child for r in result} == {300, 400}


# ---------------------------------------------------------------------------
# cleanup_relationships
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_cleanup_relationships_keeps_and_deletes(monkeypatch, mock_config):
    """Tests that cleanup_relationships sets can_delete correctly."""
    rel1 = MappedRelationship(
        parent=1, child=2, ty=Asset, origin_info={"relation_id": 10}
    )
    rel2 = MappedRelationship(
        parent=3, child=4, ty=Asset, origin_info={"relation_id": 20}
    )

    class DummyResponse:
        def __init__(self):
            self.results = [type("Rel", (), {"id": 10})()]

    fake_api_call = AsyncMock(return_value=DummyResponse())
    monkeypatch.setattr(
        "dina.plugins.datasource.netbox.netbox.plugins_d3c_productrelationship_list_list.asyncio",
        fake_api_call,
    )
    monkeypatch.setattr(
        "dina.plugins.datasource.netbox.netbox.validate_response",
        lambda x: x,
    )

    result = await mock_config.cleanup_relationships([rel1, rel2])

    kept = next(r for r in result if r.origin_info["relation_id"] == 10)
    assert kept.can_delete is False

    deleted = next(r for r in result if r.origin_info["relation_id"] == 20)
    assert deleted.can_delete is True
