from unittest.mock import patch
import pytest

from dina.synchronizer.plugin_base.preprocessor import PreprocessorPlugin


class DummyPreprocessor(PreprocessorPlugin):
    def preprocess(self, *args, **kwargs):
        return {}


@pytest.fixture
def tmp_config_file(tmp_path):
    """Create a temporary configuration file."""
    cfg_path = tmp_path / "config.yaml"
    cfg_path.write_text("dummy_config: true")
    return cfg_path


# -------------------------------
# INIT TESTS
# -------------------------------


def test_preprocessor_init_with_path(tmp_config_file):
    """When config is a Path, load_config() should be called."""
    with patch.object(
        DummyPreprocessor, "load_config", return_value={"ok": True}
    ) as mock_load:
        plugin = DummyPreprocessor(config=tmp_config_file)

    mock_load.assert_called_once_with(tmp_config_file)
    assert plugin.config == {"ok": True}
    assert plugin.config_file == tmp_config_file


def test_preprocessor_init_with_dict():
    """When config is a dict, load_config() should not be called."""
    cfg = {"param": "value"}
    with patch.object(DummyPreprocessor, "load_config", return_value={}) as mock_load:
        plugin = DummyPreprocessor(config=cfg)

    mock_load.assert_not_called()
    assert plugin.config == cfg
    assert plugin.config_file is None


def test_preprocessor_init_with_none():
    """When config is None, config should be empty and config_file should be None."""
    plugin = DummyPreprocessor(config=None)
    assert plugin.config == {}
    assert plugin.config_file is None


def test_preprocessor_init_with_invalid_type():
    """When config is neither a dict nor a Path, config should remain empty."""
    plugin = DummyPreprocessor(config=1234)
    assert plugin.config == {}
    assert plugin.config_file is None


# -------------------------------
# TESTS FOR load_config()
# -------------------------------


def test_load_config_valid_toml(tmp_path):
    """Should successfully load a valid TOML config file."""
    config_file = tmp_path / "config.toml"
    config_file.write_text('name = "Matching-Agent"\nversion = "1.0"\n')

    plugin = DummyPreprocessor()
    result = plugin.load_config(config_file)

    assert isinstance(result, dict)
    assert "name" in result
    assert result["name"] == "Matching-Agent"


def test_load_config_file_not_found(tmp_path):
    """Should raise FileNotFoundError if the file does not exist."""
    missing_file = tmp_path / "does_not_exist.toml"
    assert not missing_file.exists()

    plugin = DummyPreprocessor()

    with pytest.raises(FileNotFoundError):
        plugin.load_config(missing_file)


def test_load_config_invalid_toml(tmp_path):
    """Should raise ValueError when TOML file is invalid."""
    invalid_file = tmp_path / "broken.toml"
    invalid_file.write_text('foo = "bar"\n[unclosed')

    plugin = DummyPreprocessor()

    with pytest.raises(ValueError) as excinfo:
        plugin.load_config(invalid_file)

    assert "Invalid TOML file" in str(excinfo.value)
