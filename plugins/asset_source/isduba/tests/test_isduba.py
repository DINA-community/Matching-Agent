from datetime import datetime, timezone
from pydantic import HttpUrl
import pytest
from unittest.mock import AsyncMock, MagicMock

from types import SimpleNamespace

from dina.plugins.datasource.isduba.isduba import IsdubaDataSource
from dina.plugins.datasource.isduba.generated import isduba_api_client
from plugins.asset_source.isduba.tests.examples import DOCS_META, DOCUMENTS_FULL
# from pprint import pprint


# TODO: create more tests
@pytest.fixture
def mock_config():
    plugin_data = {
        "url": "https://fake.url",
        "keycloak_url": "https://fake.keycloak",
        "username": "srcm",
        "password": "srcm",
        "verify_ssl": False,
        "connection_pool_maxsize": 10,
    }

    datasource = SimpleNamespace(Plugin=plugin_data)
    config = SimpleNamespace(DataSource=datasource)

    return config


@pytest.mark.asyncio
async def test_fetch_products_with_docs(monkeypatch, mock_config):
    plugin = IsdubaDataSource(mock_config)

    plugin._get_token = AsyncMock(return_value="fake-token")

    fake_api = MagicMock()
    fake_api.documents_get = AsyncMock(
        return_value=SimpleNamespace(documents=DOCS_META)
    )
    doc_lookup = {meta["id"]: full for meta, full in zip(DOCS_META, DOCUMENTS_FULL)}

    fake_api.documents_id_get = AsyncMock(
        side_effect=lambda doc_id: doc_lookup.get(doc_id)
    )

    monkeypatch.setattr(
        "dina.plugins.datasource.isduba.isduba.isduba_api_client.DefaultApi",
        lambda api_client: fake_api,
    )

    class DummyApiClientCtx:
        async def __aenter__(self):
            return MagicMock()

        async def __aexit__(self, exc_type, exc, tb):
            pass

    monkeypatch.setattr(
        "dina.plugins.datasource.isduba.isduba.isduba_api_client.ApiClient",
        lambda conf: DummyApiClientCtx(),
    )

    plugin._create_api_config = MagicMock(
        return_value=isduba_api_client.Configuration(
            host="https://fake.api",
            api_key={"bearerAuth": "fake-token"},
            api_key_prefix={"bearerAuth": "Bearer"},
            debug=False,
        )
    )

    fetcher_view = MagicMock()
    fetcher_view.last_run = AsyncMock(return_value=datetime.now(timezone.utc))
    fetcher_view.get_existing = AsyncMock(return_value=[])

    result = await plugin.fetch_products(fetcher_view)
    assert result.again is True
    assert isinstance(result.data, list)
    assert len(result.data) == 3
    assert (
        result.data[0]
        and hasattr(result.data[0], "uri")
        and result.data[0].uri.endswith(str(DOCS_META[0]["id"]))
    )
    # pprint(vars(result.data[0]))


# @pytest.mark.asyncio
# async def test_build_resource_path_returns_path(mock_config):
#     plugin = IsdubaDataSource(mock_config)
#     path = plugin.build_resource_path({"path": "/api/documents/123"})
#     assert path == "/api/documents/123"
#     assert plugin.build_resource_path({}) == ""


def test_endpoint_info(mock_config):
    plugin = IsdubaDataSource(mock_config)
    assert plugin.endpoint_info() == HttpUrl("https://fake.url/")
