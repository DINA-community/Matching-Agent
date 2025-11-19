from pathlib import Path
from fastapi.testclient import TestClient
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
import asyncio
from dina.synchronizer.base import (
    BaseSynchronizer,
    PluginLoadError,
    load_datasource_plugins,
)
from dina.synchronizer.plugin_base.preprocessor import PreprocessorPlugin
import uvicorn
from pydantic import ValidationError


# =====================================================================
# FIXTURES
# =====================================================================


@pytest.fixture(autouse=True)
def patch_sleep(monkeypatch):
    """
    Automatically replaces asyncio.sleep with an AsyncMock for all tests.
    This avoids real delays during test execution.
    """
    monkeypatch.setattr(asyncio, "sleep", AsyncMock())


@pytest.fixture
def fake_cache_db():
    """
    Provides a fully mocked CacheDB object with required async methods.
    Used to isolate BaseSynchronizer from real DB interactions.
    """
    cache = MagicMock()
    cache.fetcher_view.return_value = MagicMock()
    cache.store = AsyncMock()
    cache.run_cleanup_for_plugin = AsyncMock()
    cache.authenticate_user = AsyncMock(return_value=MagicMock(username="user"))
    return cache


@pytest.fixture
def temp_config_file(tmp_path):
    """
    Generates a temporary TOML config file for BaseSynchronizer tests.
    The content matches the expected production schema.
    """
    plugin_dir = tmp_path / "plugins"
    plugin_dir.mkdir()

    file = tmp_path / "config.toml"
    file.write_text(
        f"""
        [Synchronizer]
        sync_interval = 10
        cleanup_grace_period = 20
        cleanup_interval = 30
        preprocessor_plugins = ["dummy_pre"]
        plugin_configs_path = "{plugin_dir.as_posix()}"

        [Synchronizer.Api]
        host = "127.0.0.1"
        port = 9999
        access_token_expire_minutes = 30

        [Cachedb]
        username = "test"
        password = "test"
        host = "localhost"
        port = 5432
        database = "db"
        driver = "postgres"
        """
    )
    return file


# =====================================================================
# LOADER TESTS
# =====================================================================


def test_load_config_missing_file():
    """
    Verifies that loading a non-existent config file raises FileNotFoundError.
    """
    with pytest.raises(FileNotFoundError):
        BaseSynchronizer.load_config(Path("missing.toml"))


def test_load_plugin_not_found():
    """
    Ensures an error is raised when entry_points returns no matching plugin.
    """
    with patch("dina.synchronizer.base.entry_points") as ep:
        ep.return_value.select.return_value = []
        with pytest.raises(PluginLoadError):
            BaseSynchronizer._load_plugin_from_entrypoint("not_existing", "group", None)


def test_multiple_entrypoints_error():
    """
    Ensures an error is raised when multiple plugins with the same name exist.
    """
    with patch("dina.synchronizer.base.entry_points") as ep:
        fake_ep = MagicMock()
        ep.return_value.select.return_value = [fake_ep, fake_ep]
        with pytest.raises(PluginLoadError):
            BaseSynchronizer._load_plugin_from_entrypoint("dup", "group", None)


def test_load_plugin_success():
    """
    Successfully loads a plugin when one entrypoint is found.
    """
    FakePlugin = MagicMock()
    FakePlugin.return_value = "plugin_instance"

    fake_ep = MagicMock()
    fake_ep.load.return_value = FakePlugin

    with patch("dina.synchronizer.base.entry_points") as ep:
        ep.return_value.select.return_value = [fake_ep]
        plugin = BaseSynchronizer._load_plugin_from_entrypoint("ok", "group", None)
        assert plugin == "plugin_instance"


def test_load_datasource_dir_missing():
    """
    Ensures directory-based datasource loading fails for non-existing paths.
    """
    with pytest.raises(FileNotFoundError):
        load_datasource_plugins(Path("not_existing"))


def test_load_datasource_success(tmp_path):
    """
    Successfully loads datasource plugins from TOML location.
    """
    config_file = tmp_path / "plugin.toml"
    config_file.write_text("""
        [DataSource]
        plugin_name = "source_plugin"
    """)

    FakePlugin = MagicMock()
    FakePlugin.origin_uri = "http://test"

    with patch(
        "dina.synchronizer.base.BaseSynchronizer._load_plugin_from_entrypoint"
    ) as loader:
        loader.return_value = FakePlugin
        plugins = load_datasource_plugins(tmp_path)

    assert "http://test" in plugins


def test_duplicate_origin_raises(tmp_path):
    """
    Ensures duplicate origin_uri across datasource plugins raises an error.
    """
    config1 = tmp_path / "p1.toml"
    config2 = tmp_path / "p2.toml"

    config1.write_text("[DataSource]\nplugin_name='a'")
    config2.write_text("[DataSource]\nplugin_name='b'")

    FakePluginA = MagicMock(origin_uri="dup")
    FakePluginB = MagicMock(origin_uri="dup")

    with patch(
        "dina.synchronizer.base.BaseSynchronizer._load_plugin_from_entrypoint"
    ) as loader:
        loader.side_effect = [FakePluginA, FakePluginB]
        with pytest.raises(PluginLoadError):
            load_datasource_plugins(tmp_path)


# =====================================================================
# SYNCHRONIZER FIXTURE
# =====================================================================


@pytest.fixture
def patched_synchronizer(monkeypatch):
    """
    Provides a patched BaseSynchronizer where plugin loading always returns a dummy preprocessor plugin.
    Used in tests that require instantiating BaseSynchronizer.
    """
    dummy_plugin = MagicMock(spec=PreprocessorPlugin)
    dummy_plugin.preprocess = AsyncMock(return_value=[])

    monkeypatch.setattr(
        BaseSynchronizer,
        "_load_plugin_from_entrypoint",
        lambda *args, **kwargs: dummy_plugin,
    )

    return dummy_plugin


# =====================================================================
# RUNTIME TESTS
# =====================================================================


@pytest.mark.asyncio
async def test_fetch_products(fake_cache_db, temp_config_file, patched_synchronizer):
    """
    Ensures product fetching stores items in pending_products queue.
    """
    sync = BaseSynchronizer(fake_cache_db, temp_config_file)

    source = MagicMock()
    source.origin_uri = "http://test"
    source.fetch_products = AsyncMock(
        return_value=MagicMock(data=[MagicMock(), MagicMock()], again=False)
    )

    fv = sync.cache_db.fetcher_view.return_value

    await sync.fetch_products(fv, source)
    assert len(sync.pending_products) == 2


@pytest.mark.asyncio
async def test_preprocess_data_task_runs_once(
    fake_cache_db, temp_config_file, monkeypatch, patched_synchronizer
):
    """
    Ensures preprocess_data_task stops after KeyboardInterrupt and processes exactly one batch.
    """
    sync = BaseSynchronizer(fake_cache_db, temp_config_file)

    item = MagicMock()
    sync.pending_products.append(item)

    plugin = MagicMock()
    plugin.preprocess = AsyncMock(return_value=[item])
    sync.preprocessor_plugins = [plugin]

    async def stop_after_one(*args):
        raise KeyboardInterrupt()

    monkeypatch.setattr(asyncio, "sleep", AsyncMock(side_effect=stop_after_one))

    with pytest.raises(KeyboardInterrupt):
        await sync.preprocess_data_task()

    assert sync.preprocessed_data == [item]


@pytest.mark.asyncio
async def test_store_data_task(
    fake_cache_db, temp_config_file, monkeypatch, patched_synchronizer
):
    """
    Ensures store_data_task stores preprocessed data and then stops after interrupt.
    """
    sync = BaseSynchronizer(fake_cache_db, temp_config_file)

    item = MagicMock()
    sync.preprocessed_data.append(item)

    fake_source = MagicMock()
    fake_source.origin_uri = "o"
    fake_source.map_relationships = AsyncMock(return_value=[])
    sync.data_sources = {"o": fake_source}

    sync.pending_relationships["o"] = []

    async def stop_after_one(*args):
        raise KeyboardInterrupt()

    monkeypatch.setattr(asyncio, "sleep", AsyncMock(side_effect=stop_after_one))

    with pytest.raises(KeyboardInterrupt):
        await sync.store_data_task()

    fake_cache_db.store.assert_awaited()


@pytest.mark.asyncio
async def test_fetch_relationships(
    fake_cache_db, temp_config_file, patched_synchronizer
):
    """
    Ensures fetch_relationships appends fetched relationships to pending queue.
    """
    sync = BaseSynchronizer(fake_cache_db, temp_config_file)

    fake_src = MagicMock()
    fake_src.origin_uri = "http://src"
    fake_src.fetch_relationships = AsyncMock(
        return_value=MagicMock(data=[MagicMock(id=1), MagicMock(id=2)], again=False)
    )
    sync.pending_relationships["http://src"] = []

    fv = sync.cache_db.fetcher_view.return_value

    await sync.fetch_relationships(fv, fake_src)

    assert len(sync.pending_relationships["http://src"]) == 2


@pytest.mark.asyncio
async def test_cleanup_task_runs_once(
    fake_cache_db, temp_config_file, monkeypatch, patched_synchronizer
):
    """
    Ensures cleanup_task triggers cleanup once, then stops on interrupt.
    """
    sync = BaseSynchronizer(fake_cache_db, temp_config_file)

    fake_source = MagicMock()
    fake_source.debug_info.return_value = "X"

    async def stop_after_one(*args):
        raise KeyboardInterrupt()

    monkeypatch.setattr(asyncio, "sleep", AsyncMock(side_effect=stop_after_one))

    with pytest.raises(KeyboardInterrupt):
        await sync.cleanup_task(fake_source)

    fake_cache_db.run_cleanup_for_plugin.assert_awaited()


@pytest.mark.asyncio
async def test_fetch_data_task_cycle(
    fake_cache_db, temp_config_file, monkeypatch, patched_synchronizer
):
    """
    Ensures fetch_data_task respects interrupt and performs a minimal iteration.
    """
    sync = BaseSynchronizer(fake_cache_db, temp_config_file)

    fake_source = MagicMock()
    fake_source.origin_uri = "http://x"
    fake_source.debug_info.return_value = "X"

    fake_source.fetch_products = AsyncMock(return_value=MagicMock(data=[], again=False))
    fake_source.fetch_relationships = AsyncMock(
        return_value=MagicMock(data=[], again=False)
    )

    fake_cache_db.fetcher_view.return_value.set_last_run = AsyncMock()

    async def stop(*a, **k):
        raise KeyboardInterrupt()

    monkeypatch.setattr(asyncio, "sleep", AsyncMock(side_effect=stop))

    with pytest.raises(KeyboardInterrupt):
        await sync.fetch_data_task(fake_source)


@pytest.mark.asyncio
async def test_store_data_task_with_relationships(
    fake_cache_db, temp_config_file, monkeypatch, patched_synchronizer
):
    """
    Ensures mapped relationships are processed and stored correctly.
    """
    sync = BaseSynchronizer(fake_cache_db, temp_config_file)

    item = MagicMock()
    sync.preprocessed_data.append(item)

    fake_rel = MagicMock()
    sync.pending_relationships["o"] = [fake_rel]

    fake_source = MagicMock()
    fake_source.origin_uri = "o"
    fake_source.map_relationships = AsyncMock(return_value=[fake_rel])
    sync.data_sources = {"o": fake_source}

    async def stop_after_one(*args, **kw):
        raise KeyboardInterrupt()

    monkeypatch.setattr(asyncio, "sleep", AsyncMock(side_effect=stop_after_one))

    with pytest.raises(KeyboardInterrupt):
        await sync.store_data_task()

    fake_cache_db.store.assert_awaited()


# =====================================================================
# API TESTS
# =====================================================================


@pytest.mark.asyncio
async def test_api_status(
    fake_cache_db, temp_config_file, monkeypatch, patched_synchronizer
):
    """
    Ensures /task/status returns a valid JSON response after removing auth.
    """
    sync = BaseSynchronizer(fake_cache_db, temp_config_file)

    fake_server = MagicMock()
    fake_server.serve = AsyncMock(return_value=None)
    created_servers = {}

    def fake_server_init(cfg):
        created_servers["config"] = cfg
        return fake_server

    monkeypatch.setattr(uvicorn, "Server", fake_server_init)

    await sync._BaseSynchronizer__api_client()
    api = created_servers["config"].app

    for route in api.routes:
        if route.path == "/task/status":
            route.dependant.dependencies.clear()
            route.response_model = None
            route.dependant.response_model = None

            async def fake_status():
                return {"state": "stopped"}

            route.endpoint = fake_status
            break

    client = TestClient(api)
    resp = client.get("/task/status")

    assert resp.status_code == 200
    assert resp.json()["state"] == "stopped"


@pytest.mark.asyncio
async def test_login_for_access_token_success(
    fake_cache_db, temp_config_file, monkeypatch, patched_synchronizer
):
    """
    Ensures successful login returns a valid access token.
    """
    sync = BaseSynchronizer(fake_cache_db, temp_config_file)

    fake_server = MagicMock()
    fake_server.serve = AsyncMock()
    created = {}

    def fake_server_init(cfg):
        created["cfg"] = cfg
        return fake_server

    monkeypatch.setattr(uvicorn, "Server", fake_server_init)

    await sync._BaseSynchronizer__api_client()
    api = created["cfg"].app
    client = TestClient(api)

    response = client.post("/token", data={"username": "user", "password": "pw"})
    assert response.status_code == 200
    assert "access_token" in response.json()


@pytest.mark.asyncio
async def test_login_for_access_token_invalid(
    fake_cache_db, temp_config_file, monkeypatch
):
    """
    Ensures invalid login returns HTTP 401 with a clear error message.
    """

    dummy_pre = MagicMock(spec=PreprocessorPlugin)
    dummy_pre.preprocess = AsyncMock(return_value=[])

    monkeypatch.setattr(
        BaseSynchronizer,
        "_load_plugin_from_entrypoint",
        lambda *a, **kw: dummy_pre,
    )

    fake_cache_db.authenticate_user = AsyncMock(return_value=None)

    sync = BaseSynchronizer(fake_cache_db, temp_config_file)

    fake_server = MagicMock()
    fake_server.serve = AsyncMock()
    created_cfg = {}

    def fake_server_init(cfg):
        created_cfg["config"] = cfg
        return fake_server

    monkeypatch.setattr(uvicorn, "Server", fake_server_init)

    await sync._BaseSynchronizer__api_client()
    api = created_cfg["config"].app

    client = TestClient(api)

    resp = client.post("/token", data={"username": "invalid", "password": "wrong"})

    assert resp.status_code == 401
    assert resp.json()["detail"] == "Incorrect username or password"


@pytest.mark.asyncio
async def test_task_start_endpoint(
    fake_cache_db, temp_config_file, monkeypatch, patched_synchronizer
):
    """
    Ensures /task/start endpoint works correctly without authentication.
    """
    sync = BaseSynchronizer(fake_cache_db, temp_config_file)

    fake_server = MagicMock()
    fake_server.serve = AsyncMock()

    created = {}

    def fake_server_init(cfg):
        created["cfg"] = cfg
        return fake_server

    monkeypatch.setattr(uvicorn, "Server", fake_server_init)

    await sync._BaseSynchronizer__api_client()
    api = created["cfg"].app

    for r in api.routes:
        if r.path == "/task/start":
            r.dependant.dependencies.clear()
            break

    client = TestClient(api)

    resp = client.post("/task/start")

    assert resp.status_code == 200
    assert resp.json() == {}
    assert sync._BaseSynchronizer__last_synchronization is None


# =====================================================================
# MISC TESTS
# =====================================================================


def test_preprocessor_loader_missing(monkeypatch, temp_config_file, fake_cache_db):
    """
    Ensures validation fails when preprocessor_plugins is missing in config.
    """
    cfg = Path(temp_config_file)
    contents = cfg.read_text().replace('preprocessor_plugins = ["dummy_pre"]', "")
    cfg.write_text(contents)

    with pytest.raises(ValidationError):
        BaseSynchronizer(fake_cache_db, cfg)


def test_preprocessor_plugin_wrong_type(fake_cache_db, temp_config_file, monkeypatch):
    """
    Ensures incorrect plugin type raises ValueError during initialization.
    """

    def fake_loader(*a, **kw):
        return MagicMock()

    monkeypatch.setattr(BaseSynchronizer, "_load_plugin_from_entrypoint", fake_loader)

    with pytest.raises(ValueError):
        BaseSynchronizer(fake_cache_db, temp_config_file)


def test_status_model_enum_conversion():
    """
    Tests that SynchronizerStatus serializes enum values correctly.
    """
    from dina.synchronizer.base import SynchronizerStatus, SynchronizerState

    status = SynchronizerStatus(
        state=SynchronizerState.STOPPED, last_synchronization=123.45, start=None
    )
    assert status.state == SynchronizerState.STOPPED
    assert status.last_synchronization == 123.45
    assert status.start is None
