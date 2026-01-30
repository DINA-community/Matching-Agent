import json
from pathlib import Path
import tomllib
import pytest

from dina.plugins.preprocessing.default.default import DefaultPreprocessor
from examples_preprocessing import CSAF_PRODUCT

# ------------------------------------------------------------
# Tests for DefaultPreprocessor
# ------------------------------------------------------------


@pytest.fixture(scope="session")
def matching_config():
    config_path = Path("./assets/plugin_configs/default/matching_config.toml")

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, "rb") as f:
        return tomllib.load(f)


@pytest.fixture
def plugin(matching_config):
    p = DefaultPreprocessor(config=matching_config)
    return p


@pytest.mark.asyncio
async def test_preprocess_freetext_fields(plugin):
    """Ensure freetext fields are normalized using Normalizer.parse_freetext."""
    plugin.freetext_fields = {"name": 1.0}
    plugin.ordered_fields = {}
    plugin.other_fields = {}

    result = await plugin.preprocess([CSAF_PRODUCT])

    assert result[0].product.name == "example:software"


@pytest.mark.asyncio
async def test_preprocess_ordered_fields(plugin):
    """Ensure ordered fields (e.g. version) are parsed correctly."""
    plugin.freetext_fields = {}
    plugin.ordered_fields = {"version": 1.0}
    plugin.other_fields = {}

    result = await plugin.preprocess([CSAF_PRODUCT])

    assert result[0].product.version == [
        {
            "schema": "semantic-versioning",
            "raw": "1.0.0",
            "package": None,
            "release_prefix": None,
            "release_number": "1.0.0",
            "release_branch": None,
            "build_number": None,
            "qualifier": None,
            "architecture": None,
            "date": None,
            "epoch": None,
            "min_max_version": [{"min": "1.0.0", "max": "1.0.0"}],
        }
    ]


@pytest.mark.asyncio
async def test_preprocess_ordered_field_model_json_dump(plugin):
    """Ensure model field is converted to JSON when parser returns dict/list."""
    plugin.freetext_fields = {}
    plugin.ordered_fields = {"model": 1.0}
    plugin.other_fields = {}

    result = await plugin.preprocess([CSAF_PRODUCT])

    val = result[0].product.model
    assert isinstance(val, str)
    assert json.loads(val) == {
        "schema": "freetext",
        "raw": "x200",
        "package": None,
        "release_prefix": None,
        "release_number": None,
        "release_branch": None,
        "build_number": None,
        "qualifier": None,
        "architecture": None,
        "date": None,
        "epoch": None,
        "min_max_version": None,
    }


@pytest.mark.asyncio
async def test_preprocess_other_fields(plugin):
    """Ensure other_fields cpe, purl, and files are handled correctly."""
    plugin.freetext_fields = {}
    plugin.ordered_fields = {}
    plugin.other_fields = {"cpe": 0.35, "purl": 0.35, "files": 0.3}
    expected_cpe = {
        "raw": "cpe:2.3:a:example:software:1.0.0:*:*:*:*:*:*:*",
        "part": "a",
        "vendor": "example",
        "product": "software",
        "version": {
            "schema": "semantic-versioning",
            "raw": "1.0.0",
            "package": None,
            "release_prefix": None,
            "release_number": "1.0.0",
            "release_branch": None,
            "build_number": None,
            "qualifier": None,
            "architecture": None,
            "date": None,
            "epoch": None,
            "min_max_version": [{"min": "1.0.0", "max": "1.0.0"}],
        },
        "update": None,
        "edition": None,
        "language": None,
        "sw_edition": None,
        "target_sw": None,
        "target_hw": None,
        "other": None,
    }

    expected_purl = {
        "raw": "pkg:generic/example@1.0.0",
        "version": {
            "schema": "semantic-versioning",
            "raw": "1.0.0",
            "package": None,
            "release_number": "1.0.0",
            "release_prefix": None,
            "release_branch": None,
            "qualifier": None,
            "build_number": None,
            "architecture": None,
            "date": None,
            "epoch": None,
            "min_max_version": [{"min": "1.0.0", "max": "1.0.0"}],
        },
        "type": "generic",
        "name": "example",
        "namespace": None,
        "subpath": None,
        "qualifiers": None,
    }

    expected_files = {
        "name": "firmware:bin",
        "hash_algorithm": "sha256",
        "file_hash": "abc123",
    }

    result = await plugin.preprocess([CSAF_PRODUCT])
    assert json.loads(result[0].product.cpe) == expected_cpe
    assert json.loads(result[0].product.purl) == expected_purl
    assert json.loads(result[0].product.files) == [expected_files]


@pytest.mark.asyncio
async def test_preprocess_skips_empty_values(plugin):
    """Ensure fields with None or empty values are skipped safely."""
    plugin.freetext_fields = {"name": 0.4}
    plugin.ordered_fields = {"version": 0.3}
    plugin.other_fields = {"cpe": 0.3}

    result = await plugin.preprocess([CSAF_PRODUCT])

    assert result[0].product.name == "example:software"
    assert result[0].product.version == [
        {
            "schema": "semantic-versioning",
            "raw": "1.0.0",
            "package": None,
            "release_prefix": None,
            "release_number": "1.0.0",
            "release_branch": None,
            "build_number": None,
            "qualifier": None,
            "architecture": None,
            "date": None,
            "epoch": None,
            "min_max_version": [{"min": "1.0.0", "max": "1.0.0"}],
        }
    ]
