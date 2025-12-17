import pytest
from dina.cachedb.model import Product
from dina.plugins.datasource.isduba.converter import (
    convert_into_database_format,
    _update_product_fields,
    _determine_product_type,
    _get_product_values,
    _extract_from_version,
    _extract_product_info,
    _extract_cpe_part,
    _list_to_str,
)
from dina.plugins.datasource.isduba.datamodels import ProductIdentificationHelper
from examples import CSAF_PRODUCT_TREE, PRODUCT_HELPER, PRODUCT_INFO, PRODUCT_VERSION


# ============================================================
# Tests for main conversion logic
# ============================================================


@pytest.mark.asyncio
async def test_convert_into_database_format():
    """Test that convert_into_database_format correctly builds CsafProduct objects."""
    result = convert_into_database_format(CSAF_PRODUCT_TREE)

    assert len(result) == 1
    csaf = result[0]
    assert csaf.origin_info["product_name_id"] == "P-001"
    assert csaf.product.cpe == "cpe:/a:vendor:product:1.2.3"


# ============================================================
# Tests for helper: _update_product_fields
# ============================================================


def test_update_product_fields_copies_all_fields():
    """Test that all relevant Product fields are copied correctly."""
    source = Product(name="Source", version=["1.0"], cpe="a", manufacturer_name="XCorp")
    target = Product(name="Target", version=["0.9"])

    _update_product_fields(target, source)

    assert target.name == "Source"
    assert target.cpe == "a"
    assert target.manufacturer_name == "XCorp"


# ============================================================
# Tests for helper: _determine_product_type
# ============================================================


def test_determine_product_type_various_cases():
    """Test product type detection for software, device, and undefined."""
    assert _determine_product_type("a", None).name == "Software"

    helper = ProductIdentificationHelper(serial_numbers=["123"])
    assert _determine_product_type(None, helper).name == "Device"

    assert _determine_product_type(None, None).name == "Undefined"


# ============================================================
# Tests for helper: _get_product_values
# ============================================================


def test_get_product_values_extracts_correct_data():
    """Test that product values are extracted correctly from ProductInfo."""
    pid, cpe, helper_out, version, names = _get_product_values(PRODUCT_INFO)

    assert pid == "P-001"
    assert cpe == "a"
    assert "Example Product" in names
    assert helper_out.purl == "pkg:generic/vendor@1.2.3"
    assert "1.2.3" in version


# ============================================================
# Tests for helper: _extract_from_version
# ============================================================


def test_extract_from_version_adds_name_and_product():
    """Test that _extract_from_version adds version and product names."""
    versions, products = [], []

    _extract_from_version(PRODUCT_VERSION, versions, products)

    assert versions == ["1.2.3"]
    assert products == ["Example Product"]

    # Running again should not duplicate entries
    _extract_from_version(PRODUCT_VERSION, versions, products)

    assert versions == ["1.2.3"]
    assert products == ["Example Product"]


# ============================================================
# Tests for helper: _extract_product_info
# ============================================================


def test_extract_product_info_with_helper_and_cpe():
    """Test that helper and cpe are correctly extracted."""
    pid, helper_out, cpe = _extract_product_info(PRODUCT_VERSION, PRODUCT_HELPER, None)

    assert pid == "P-001"
    assert helper_out is PRODUCT_HELPER
    assert cpe == "a"


# ============================================================
# Tests for helper: _extract_cpe_part
# ============================================================


@pytest.mark.parametrize(
    "cpe,expected",
    [
        ("cpe:/a:vendor:product", "a"),
        ("cpe:2.3:a:vendor:product", "a"),
        ("invalid", None),
        ("", None),
    ],
)
def test_extract_cpe_part(cpe, expected):
    """Test various CPE string extraction cases."""
    assert _extract_cpe_part(cpe) == expected


# ============================================================
# Tests for helper: _list_to_str
# ============================================================


def test_list_to_str_works_as_expected():
    """Test that lists are joined correctly into strings."""
    assert _list_to_str(["a", "b"]) == "a, b"
    assert _list_to_str([]) is None
