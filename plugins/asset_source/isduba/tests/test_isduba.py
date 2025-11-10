import pytest
from datetime import datetime, timezone
from unittest.mock import AsyncMock, MagicMock
from types import SimpleNamespace
from pydantic import HttpUrl

from dina.cachedb.database import CsafProduct, MappedRelationship
from dina.plugins.datasource.isduba.isduba import IsdubaDataSource, process_document
from dina.plugins.datasource.isduba.generated import isduba_api_client
from dina.synchronizer.plugin_base.data_source import (
    CleanUpDecision,
    FetchRelationshipsResult,
    Relationship,
)
from examples import DOCS_META, DOCUMENTS_FULL


# -----------------------------------------------------------
# Fixtures & Hilfsfunktionen
# -----------------------------------------------------------


@pytest.fixture
def mock_config():
    """Erstellt eine Fake-Plugin-Konfiguration für Tests."""
    plugin_data = dict(
        url="https://fake.url",
        keycloak_url="https://fake.keycloak",
        username="srcm",
        password="srcm",
        verify_ssl=False,
        connection_pool_maxsize=10,
    )
    datasource = SimpleNamespace(Plugin=plugin_data)
    return SimpleNamespace(DataSource=datasource)


def _make_dummy_api(monkeypatch, docs_meta, docs_full):
    """Mockt den isduba_api_client, sodass er Fake-Dokumente zurückgibt."""
    fake_api = MagicMock()
    fake_api.documents_get = AsyncMock(
        return_value=SimpleNamespace(documents=docs_meta)
    )
    lookup = {m["id"]: f for m, f in zip(docs_meta, docs_full)}
    fake_api.documents_id_get = AsyncMock(side_effect=lambda doc_id: lookup.get(doc_id))

    monkeypatch.setattr(
        "dina.plugins.datasource.isduba.isduba.isduba_api_client.DefaultApi",
        lambda _: fake_api,
    )

    class DummyCtx:
        async def __aenter__(self):
            return MagicMock()

        async def __aexit__(self, *_):
            pass

    monkeypatch.setattr(
        "dina.plugins.datasource.isduba.isduba.isduba_api_client.ApiClient",
        lambda _: DummyCtx(),
    )
    return fake_api


def _dummy_fetcher_view():
    """Erstellt ein einfaches Mock-FetcherView-Objekt."""
    view = MagicMock()
    view.last_run = AsyncMock(return_value=datetime.now(timezone.utc))
    view.get_existing = AsyncMock(return_value=[])
    return view


# -----------------------------------------------------------
# Tests: fetch_products
# -----------------------------------------------------------


@pytest.mark.asyncio
async def test_fetch_products_with_docs(monkeypatch, mock_config):
    plugin = IsdubaDataSource(mock_config)
    plugin._get_token = AsyncMock(return_value="fake-token")
    _make_dummy_api(monkeypatch, DOCS_META, DOCUMENTS_FULL)
    plugin._create_api_config = MagicMock(return_value=MagicMock())

    result = await plugin.fetch_products(_dummy_fetcher_view())

    assert result.again is True
    assert isinstance(result.data, list)
    assert len(result.data) == 4
    assert result.data[0].uri.endswith(str(DOCS_META[0]["id"]))


@pytest.mark.asyncio
async def test_fetch_products_empty_response(monkeypatch, mock_config):
    plugin = IsdubaDataSource(mock_config)
    plugin._get_token = AsyncMock(return_value="fake-token")
    _make_dummy_api(monkeypatch, [], [])
    plugin._create_api_config = MagicMock(return_value=MagicMock())

    result = await plugin.fetch_products(_dummy_fetcher_view())
    assert not result.again
    assert not result.data


@pytest.mark.asyncio
async def test_fetch_products_error_in_document(monkeypatch, mock_config):
    plugin = IsdubaDataSource(mock_config)
    plugin._get_token = AsyncMock(return_value="fake-token")

    fake_api = MagicMock()
    fake_api.documents_get = AsyncMock(
        return_value=SimpleNamespace(documents=DOCS_META[:1])
    )
    fake_api.documents_id_get = AsyncMock(side_effect=Exception("Error"))

    class DummyApiClientCtx:
        async def __aenter__(self):
            return MagicMock()

        async def __aexit__(self, exc_type, exc, tb):
            pass

    monkeypatch.setattr(
        "dina.plugins.datasource.isduba.isduba.isduba_api_client.ApiClient",
        lambda conf: DummyApiClientCtx(),
    )
    plugin._create_api_config = MagicMock(return_value=MagicMock())

    fetcher_view = _dummy_fetcher_view()

    with pytest.raises(Exception, match="Exception when calling DefaultApi"):
        await plugin.fetch_products(fetcher_view)


@pytest.mark.asyncio
async def test_cleanup_products_returns_expected_decisions(monkeypatch, mock_config):
    """Tests that cleanup_products correctly returns CleanUpDecision objects."""

    plugin = IsdubaDataSource(mock_config)

    plugin._get_token = AsyncMock(return_value="fake-token")

    plugin._create_api_config = MagicMock(
        return_value=isduba_api_client.Configuration(
            host="https://fake.api",
            api_key={"bearerAuth": "fake-token"},
            api_key_prefix={"bearerAuth": "Bearer"},
            debug=False,
        )
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

    plugin._safe_documents_id_get = AsyncMock(return_value=None)

    product1 = MagicMock(spec=CsafProduct)
    product1.id = 101
    product1.origin_info = {"path": "/api/documents/101"}

    product2 = MagicMock(spec=CsafProduct)
    product2.id = 202
    product2.origin_info = {"path": "/api/documents/202"}

    data_to_check = [product1, product2]

    result = await plugin.cleanup_products(data_to_check)

    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(r, CleanUpDecision) for r in result)

    assert all(r.can_delete for r in result)
    assert {r.id for r in result} == {101, 202}
    assert all(r.ty is CsafProduct for r in result)


@pytest.mark.asyncio
async def test_safe_documents_id_get_success(mock_config):
    """Tests that _safe_documents_id_get returns result when no exception occurs."""
    plugin = IsdubaDataSource(mock_config)

    fake_api = MagicMock()
    fake_api.documents_id_get = AsyncMock(return_value={"result": "ok"})

    result = await plugin._safe_documents_id_get(fake_api, 123)

    assert result == {"result": "ok"}
    fake_api.documents_id_get.assert_awaited_once_with(123)


@pytest.mark.asyncio
async def test_safe_documents_id_get_unauthorized(monkeypatch, mock_config):
    """Tests that _safe_documents_id_get refreshes token on UnauthorizedException."""

    plugin = IsdubaDataSource(mock_config)

    fake_api = MagicMock()
    fake_api.documents_id_get = AsyncMock(
        side_effect=isduba_api_client.exceptions.UnauthorizedException(
            "401 Unauthorized"
        )
    )

    plugin._get_token = AsyncMock(return_value="new-fake-token")

    fake_new_api = MagicMock()
    fake_new_api.documents_id_get = AsyncMock(return_value={"result": "new-client-ok"})

    monkeypatch.setattr(
        "dina.plugins.datasource.isduba.isduba.isduba_api_client.DefaultApi",
        lambda client: fake_new_api,
    )

    class DummyClientCtx:
        async def __aenter__(self):
            return MagicMock()

        async def __aexit__(self, exc_type, exc, tb):
            pass

    monkeypatch.setattr(
        "dina.plugins.datasource.isduba.isduba.isduba_api_client.ApiClient",
        lambda conf: DummyClientCtx(),
    )

    plugin._create_api_config = MagicMock(return_value=MagicMock())

    result = await plugin._safe_documents_id_get(fake_api, 999)

    assert result == {"result": "new-client-ok"}
    plugin._get_token.assert_awaited_once()
    fake_new_api.documents_id_get.assert_awaited_once_with(999)


def test_process_document_with_valid_product_tree(monkeypatch):
    """Tests that process_document calls convert_into_database_format when product_tree exists."""
    # --- Arrange ---
    document = {"id": 42}
    origin_uri = "https://fake.origin"
    fake_product_tree = {"branches": [{"category": "vendor"}]}
    fake_response = {
        "document": {"title": "Test CSAF"},
        "product_tree": fake_product_tree,
    }

    fake_products = [MagicMock(spec=CsafProduct), MagicMock(spec=CsafProduct)]

    monkeypatch.setattr(
        "dina.plugins.datasource.isduba.isduba.get_csaf_product_tree",
        lambda origin_uri, path, doc, tree: fake_product_tree,
    )
    monkeypatch.setattr(
        "dina.plugins.datasource.isduba.isduba.convert_into_database_format",
        lambda tree: fake_products,
    )

    result = process_document(document, fake_response, origin_uri)

    assert result == fake_products
    assert isinstance(result[0], CsafProduct)


# -----------------------------------------------------------
# Utility-Tests
# -----------------------------------------------------------


def test_endpoint_info(mock_config):
    assert IsdubaDataSource(mock_config).endpoint_info() == HttpUrl("https://fake.url/")


def test_build_resource_path_returns_path(mock_config):
    plugin = IsdubaDataSource(mock_config)
    assert (
        plugin.build_resource_path({"path": "/api/documents/123"})
        == "/api/documents/123"
    )
    assert plugin.build_resource_path({}) == ""


def test_create_api_config(mock_config):
    plugin = IsdubaDataSource(mock_config)
    config = plugin._create_api_config("https://fake.url/", "token123")
    assert isinstance(config, isduba_api_client.Configuration)
    assert config.host.endswith("/api")
    assert config.api_key_prefix["bearerAuth"] == "Bearer"


# -----------------------------------------------------------
# Tests: fetch_relationships
# -----------------------------------------------------------


@pytest.mark.asyncio
async def test_fetch_relationships_basic(monkeypatch, mock_config):
    plugin = IsdubaDataSource(mock_config)
    plugin._get_token = AsyncMock(return_value="fake-token")

    csaf1, csaf2 = MagicMock(spec=CsafProduct), MagicMock(spec=CsafProduct)
    csaf1.id, csaf2.id = 1, 2
    csaf1.origin_info = {"product_name_id": "p1", "path": "/api/documents/1"}
    csaf2.origin_info = {"product_name_id": "p2", "path": "/api/documents/1"}

    fetcher_view = MagicMock()
    fetcher_view.last_run = AsyncMock(return_value=datetime.now(timezone.utc))
    fetcher_view.get_existing = AsyncMock(
        side_effect=[[csaf1, csaf2], [csaf1], [csaf2]]
    )

    _make_dummy_api(monkeypatch, DOCS_META[:1], DOCUMENTS_FULL[:1])
    plugin._create_api_config = MagicMock(return_value=MagicMock())

    result = await plugin.fetch_relationships(fetcher_view)

    assert isinstance(result, FetchRelationshipsResult)
    assert result.again is False
    assert all(isinstance(r, Relationship) for r in result.data)
    assert result.data[0].parent.id == 1
    assert result.data[0].child.id == 2


@pytest.mark.asyncio
async def test_map_relationships_creates_mapped_relationships(mock_config):
    """Tests that map_relationships creates correct MappedRelationship objects."""
    plugin = IsdubaDataSource(mock_config)

    parent1 = MagicMock(spec=CsafProduct)
    child1 = MagicMock(spec=CsafProduct)
    parent1.id, child1.id = 101, 202

    parent2 = MagicMock(spec=CsafProduct)
    child2 = MagicMock(spec=CsafProduct)
    parent2.id, child2.id = 303, 404

    relations = [
        Relationship(parent=parent1, child=child1, ty=CsafProduct),
        Relationship(parent=parent2, child=child2, ty=CsafProduct),
    ]

    result = await plugin.map_relationships(MagicMock(), relations)

    assert isinstance(result, list)
    assert all(isinstance(m, MappedRelationship) for m in result)
    assert len(result) == 2

    assert result[0].parent == 101
    assert result[0].child == 202
    assert result[1].parent == 303
    assert result[1].child == 404

    assert all(m.ty is CsafProduct for m in result)
