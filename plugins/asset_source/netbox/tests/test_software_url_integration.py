"""Follow connector-generated software URLs against a real NetBox/D3C server."""

from uuid import uuid4

import httpx
import pytest
from dina.plugins.datasource.netbox.netbox import NetboxDataSource
from pydantic import HttpUrl

from dina.synchronizer.plugin_base.data_source import DataSourceConfig, DataSourcePlugin


@pytest.mark.integration
@pytest.mark.parametrize("string_id", [False, True], ids=["integer-id", "string-id"])
def test_software_resource_url_retrieves_real_record(netbox_client: httpx.Client, string_id: bool) -> None:
    """Create software through D3C and retrieve it using the connector's URL."""
    client = netbox_client
    base_url = str(client.base_url)
    token = client.headers["Authorization"].removeprefix("Bearer ")

    datasource = NetboxDataSource(
        DataSourcePlugin.Config(
            DataSource=DataSourceConfig(
                plugin_name="netbox",
                publish_matches=False,
                Plugin=NetboxDataSource.Config(api_url=HttpUrl(base_url), api_token=token),
            )
        )
    )
    name = f"url-test-{uuid4().hex}"
    manufacturer_response = client.post("/api/dcim/manufacturers/", json={"name": name, "slug": name})
    print(manufacturer_response.status_code, manufacturer_response.text)
    assert manufacturer_response.status_code == 201, manufacturer_response.text
    manufacturer = manufacturer_response.json()
    try:
        created = client.post(
            "/api/plugins/d3c/software-list/",
            json={"name": name, "version": "1.0", "manufacturer": manufacturer["id"]},
        )
        assert created.status_code == 201, created.text
        software = created.json()
        try:
            software_id = str(software["id"]) if string_id else software["id"]
            path = datasource.build_resource_path({"software_id": software_id})
            response = client.get(f"{str(datasource.origin_uri).rstrip('/')}{path}")
            assert response.status_code == 200, response.text
            assert response.json()["id"] == software["id"]
            assert response.json()["name"] == name
            assert response.json()["version"] == "1.0"
        finally:
            deleted = client.delete(software["url"])
            assert deleted.status_code == 204, deleted.text
    finally:
        deleted = client.delete(manufacturer["url"])
        assert deleted.status_code == 204, deleted.text
