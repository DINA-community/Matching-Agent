import httpx
import pytest
import re
import tomllib
from datetime import datetime, timezone
from unittest.mock import AsyncMock, MagicMock
from pathlib import Path
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
from examples import DOCS_META, ISDUBA_DOCUMENTS


# -----------------------------------------------------------
# Fixtures & Helper Functions
# -----------------------------------------------------------


@pytest.fixture
def mock_config():
    """Fake plugin configuration"""
    plugin_data = dict(
        url="https://fake.url",
        keycloak_url="https://fake.keycloak",
        keycloak_realm="isduba",
        username="srcm",
        password="srcm",
        verify_ssl=False,
        connection_pool_maxsize=10,
    )
    datasource = SimpleNamespace(Plugin=plugin_data)
    return SimpleNamespace(DataSource=datasource)


# Assumes it was written by dev/start-local-env.sh, CI, or some other automation
LIVE_CONFIG = Path(__file__).parents[4] / "assets/plugin_configs/data_source/csaf/isduba-local.toml"


@pytest.fixture(params=["mock", pytest.param("live", marks=pytest.mark.integration)])
def backend(request):
    """Mocked ISDuBA API"""
    return request.param


@pytest.fixture
def plugin_config(backend, mock_config):
    """
    Plugin configuration for the backend
    live: requires running dev stack with ISDuBA
    mock: just unit-tests with mocked APIs
    """
    if backend == "mock":
        return mock_config
    try:
        with LIVE_CONFIG.open("rb") as file:
            plugin_data = tomllib.load(file)["DataSource"]["Plugin"]
    except (OSError, KeyError, tomllib.TOMLDecodeError) as e:
        pytest.fail(f"Integation tests: cannot load {LIVE_CONFIG}: {e!s}", pytrace=False)
    try:
        httpx.get(plugin_data["url"], verify=plugin_data["verify_ssl"]).raise_for_status()
    except httpx.HTTPError as e:
        pytest.fail(f"Integration tests: ISDuBA at {plugin_data['url']} is unreachable: {e!s}",
                    pytrace=False)
    return SimpleNamespace(DataSource=SimpleNamespace(Plugin=plugin_data))


# The query fetch_products sends, ISDuBA filters the documents by it
QUERY = re.compile(r"\$current_release_date (\S+) timestamp >= \$current_release_date (\S+) timestamp <=")
EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)


class FakeIsdubaApi:
    """Mock the python client generated based on the OpenAPI spec"""

    def __init__(self, api_client):
        self.api_client = api_client

    def _authorize(self):
        if self.api_client.configuration.api_key["bearerAuth"] != "fake-token":
            raise isduba_api_client.exceptions.UnauthorizedException(status=401, reason="Unauthorized")

    async def documents_get(self, limit=None, offset=0, query=None, orders=None):
        self._authorize()
        # parse the isduba query syntax, used by test_fetch_products_empty_response
        since, until = map(datetime.fromisoformat, QUERY.fullmatch(query).groups())
        documents = [
            meta
            for meta in DOCS_META  # already ordered by descending `critical` value
            if since <= datetime.fromisoformat(ISDUBA_DOCUMENTS[meta["id"]]["document"]["tracking"]["current_release_date"]) <= until
        ][offset : offset + limit]
        # ISDuBA returns no list instead of an empty one
        return SimpleNamespace(documents=documents or None)

    async def documents_id_get(self, doc_id):
        self._authorize()
        if doc_id not in ISDUBA_DOCUMENTS:
            raise isduba_api_client.exceptions.NotFoundException(status=404, reason="Not Found")
        return ISDUBA_DOCUMENTS[doc_id]


def _mock_isduba(monkeypatch, plugin):
    """Mock token, API client and configuration"""
    plugin._get_token = AsyncMock(return_value="fake-token")
    monkeypatch.setattr(
        "dina.plugins.datasource.isduba.isduba.isduba_api_client.DefaultApi",
        FakeIsdubaApi,
    )


def _dummy_fetcher_view(last_run=None):
    view = MagicMock()
    view.last_run = AsyncMock(return_value=last_run or datetime.now(timezone.utc))
    view.get_existing = AsyncMock(return_value=[])
    return view


# -----------------------------------------------------------
# Tests: fetch_products
# -----------------------------------------------------------


@pytest.mark.asyncio
async def test_fetch_products_with_docs(monkeypatch, backend, plugin_config):
    """Tests that fetch_products correctly returns a list of documents when API data is available."""
    plugin = IsdubaDataSource(plugin_config)
    if backend == "mock":
        _mock_isduba(monkeypatch, plugin)

    result = await plugin.fetch_products(_dummy_fetcher_view(last_run=EPOCH))

    assert result.again is True
    assert isinstance(result.data, list)
    assert {p.origin_info["path"] for p in result.data} == {f"/api/documents/{doc_id}" for doc_id in ISDUBA_DOCUMENTS}
    # The products of the most critical document come first
    assert result.data[0].uri.startswith(f"{plugin.origin_uri}api/documents/{DOCS_META[0]['id']}#")


@pytest.mark.asyncio
async def test_fetch_products_empty_response(monkeypatch, backend, plugin_config):
    """Ensures fetch_products handles an empty API response gracefully."""
    plugin = IsdubaDataSource(plugin_config)
    if backend == "mock":
        _mock_isduba(monkeypatch, plugin)

    # No documents were released since now
    result = await plugin.fetch_products(_dummy_fetcher_view())
    assert not result.again
    assert not result.data


@pytest.mark.asyncio
async def test_fetch_products_invalid_token(monkeypatch, backend, plugin_config):
    """Verifies that fetch_products raises an exception when ISDuBA rejects the token."""
    plugin = IsdubaDataSource(plugin_config)
    if backend == "mock":
        _mock_isduba(monkeypatch, plugin)
    plugin._get_token = AsyncMock(return_value="invalid-token")

    fetcher_view = _dummy_fetcher_view(last_run=EPOCH)

    with pytest.raises(Exception, match="Exception when calling DefaultApi"):
        await plugin.fetch_products(fetcher_view)


@pytest.mark.asyncio
async def test_cleanup_products_returns_expected_decisions(monkeypatch, backend, plugin_config):
    """Tests that cleanup_products correctly returns CleanUpDecision objects."""

    plugin = IsdubaDataSource(plugin_config)

    if backend == "mock":
        _mock_isduba(monkeypatch, plugin)

    # Documents that exist in ISDuBA
    doc_id1, doc_id2 = list(ISDUBA_DOCUMENTS)[:2]

    product1 = MagicMock(spec=CsafProduct)
    product1.id = 101
    product1.origin_info = {"path": f"/api/documents/{doc_id1}"}

    product2 = MagicMock(spec=CsafProduct)
    product2.id = 202
    product2.origin_info = {"path": f"/api/documents/{doc_id2}"}

    data_to_check = [product1, product2]

    result = await plugin.cleanup_products(data_to_check)

    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(r, CleanUpDecision) for r in result)
    assert {r.id for r in result} == {101, 202}
    assert all(r.ty is CsafProduct for r in result)


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
    """Checks that endpoint_info returns the expected API URL."""
    assert IsdubaDataSource(mock_config).endpoint_info() == HttpUrl("https://fake.url/")


def test_build_resource_path_returns_path(mock_config):
    """Tests that build_resource_path correctly returns the document path or an empty string."""
    plugin = IsdubaDataSource(mock_config)
    assert (
        plugin.build_resource_path(
            {"path": "/api/documents/123", "product_name_id": "42"}
        )
        == "/api/documents/123#product_id=42"
    )
    assert plugin.build_resource_path({}) == ""


def test_create_api_config(mock_config):
    """Verifies that _create_api_config builds a valid API client configuration."""
    plugin = IsdubaDataSource(mock_config)
    config = plugin._create_api_config("https://fake.url/", "token123")
    assert isinstance(config, isduba_api_client.Configuration)
    assert config.host.endswith("/api")
    assert config.api_key_prefix["bearerAuth"] == "Bearer"


# -----------------------------------------------------------
# Tests: fetch_relationships
# -----------------------------------------------------------


@pytest.mark.asyncio
async def test_fetch_relationships(monkeypatch, backend, plugin_config):
    """Ensures fetch_relationships correctly returns Relationship objects."""
    plugin = IsdubaDataSource(plugin_config)

    # A document in ISDuBA with relationships in its product tree
    doc_id, relationships = next(
        (doc_id, document["product_tree"]["relationships"])
        for doc_id, document in ISDUBA_DOCUMENTS.items()
        if document["product_tree"].get("relationships")
    )

    csaf1, csaf2 = MagicMock(spec=CsafProduct), MagicMock(spec=CsafProduct)
    csaf1.id, csaf2.id = 1, 2
    csaf1.origin_info = {"product_name_id": "p1", "path": f"/api/documents/{doc_id}"}
    csaf2.origin_info = {"product_name_id": "p2", "path": f"/api/documents/{doc_id}"}

    fetcher_view = MagicMock()
    fetcher_view.last_run = AsyncMock(return_value=datetime.now(timezone.utc))
    # The existing products, then both related products for each relationship
    fetcher_view.get_existing = AsyncMock(
        side_effect=[[csaf1, csaf2]] + [[csaf1], [csaf2]] * len(relationships)
    )

    if backend == "mock":
        _mock_isduba(monkeypatch, plugin)

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
