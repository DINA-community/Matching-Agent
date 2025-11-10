from dina.cachedb.model import File, FileList
from examples import DOCUMENTS_FULL
from dina.plugins.datasource.isduba.connector import (
    get_csaf_product_tree,
    get_relationships,
    get_product_identification_helper,
    get_product_version,
    get_product,
    get_product_info,
)
from dina.plugins.datasource.isduba.datamodels import (
    CsafDocument,
    CsafProductTree,
    ProductIdentificationHelper,
    ProductInfo,
    ProductVersion,
    ProductVersionRange,
    Product,
    Relationship,
)

# ============================================================
# Tests for get_csaf_product_tree
# ============================================================


def test_get_csaf_product_tree_valid_input():
    """Should build a CsafProductTree from valid document and product_tree."""
    tree = get_csaf_product_tree(
        "https://host",
        "/api/documents/1",
        DOCUMENTS_FULL[0]["document"],
        DOCUMENTS_FULL[0]["product_tree"],
    )
    assert isinstance(tree, CsafProductTree)
    assert isinstance(tree.csaf_document, CsafDocument)
    assert (
        tree.csaf_document.title
        == "Multiple Vulnerabilities in SENTRON 7KT PAC1260 Data Manager"
    )
    assert tree.product_list and isinstance(tree.product_list[0][0], ProductInfo)


def test_get_csaf_product_tree_handles_missing_branches():
    """Should return None if branches missing or empty."""
    assert get_csaf_product_tree("https://host", "/api/documents/1", {}, {}) is None
    assert (
        get_csaf_product_tree(
            "https://host", "/api/documents/1", {"title": "x"}, {"branches": []}
        )
        is None
    )


# ============================================================
# Tests for get_relationships
# ============================================================


def test_get_relationships_returns_list():
    """Should convert relationships dicts into Relationship objects."""
    rels = get_relationships(DOCUMENTS_FULL[0]["product_tree"])
    assert len(rels) == 1
    rel = rels[0]
    assert isinstance(rel, Relationship)
    assert rel.category == "fake-category"
    assert rel.product_reference == "fake-product-id-1"
    assert rel.relates_to_product_reference == "fake-product-id-11"


def test_get_relationships_empty_tree_returns_empty_list():
    assert get_relationships(None) == []
    assert get_relationships({}) == []


# ============================================================
# Tests for get_product_identification_helper
# ============================================================


def test_get_product_identification_helper_basic_fields():
    """Should correctly populate ProductIdentificationHelper from dict."""
    data = {"cpe": "cpe:/a:x:y", "purl": "pkg:generic/foo@1.0", "skus": ["SKU1"]}
    helper = get_product_identification_helper(data)
    assert isinstance(helper, ProductIdentificationHelper)
    assert helper.cpe == "cpe:/a:x:y"
    assert helper.purl == "pkg:generic/foo@1.0"
    assert helper.skus == ["SKU1"]


def test_get_product_identification_helper_with_hashes():
    """Should create FileList with File entries when hashes are present."""
    data = {
        "hashes": [
            {
                "filename": "a.bin",
                "file_hashes": [{"algorithm": "sha256", "value": "abc"}],
            },
            {
                "filename": "b.bin",
                "file_hashes": [{"algorithm": "md5", "value": "def"}],
            },
        ]
    }

    helper = get_product_identification_helper(data)
    assert isinstance(helper.files, FileList)
    assert len(helper.files.files) == 2
    f = helper.files.files[0]
    assert isinstance(f, File)
    assert f.name == "a.bin"
    assert f.hash_algorithm == "sha256"
    assert f.file_hash == "abc"


def test_get_product_identification_helper_none_input():
    """Should return None for empty or None input."""
    assert get_product_identification_helper(None) is None
    assert get_product_identification_helper({}) is None


# ============================================================
# Tests for get_product_version
# ============================================================


def test_get_product_version_creates_version_object():
    """Should create ProductVersion with attached Product."""
    branch = {"product": {"name": "DeviceX", "product_id": "PID1"}}

    result = get_product_version("1.0", branch)
    assert isinstance(result, ProductVersion)
    assert result.name == "1.0"
    assert isinstance(result.product, Product)
    assert result.product.name == "DeviceX"


def test_get_product_version_range_creates_range_object():
    """Should create ProductVersionRange when as_range=True."""
    branch = {"product": {"name": "DeviceX", "product_id": "PID1"}}

    result = get_product_version("2.x", branch, as_range=True)
    assert isinstance(result, ProductVersionRange)
    assert result.name == "2.x"
    assert result.product.product_id == "PID1"


# # ============================================================
# # Tests for get_product
# # ============================================================


def test_get_product_creates_product_with_helper():
    """Should create Product including nested identification helper."""
    data = {
        "name": "RouterX",
        "product_id": "RID1",
        "product_identification_helper": {
            "cpe": "cpe:/h:x:y",
            "purl": "pkg:device/routerx@2",
        },
    }

    p = get_product(data)
    assert isinstance(p, Product)
    assert p.name == "RouterX"
    assert p.product_id == "RID1"
    assert isinstance(p.product_identification_helper, ProductIdentificationHelper)
    assert p.product_identification_helper.purl.startswith("pkg:")


# ============================================================
# Tests for get_product_info
# ============================================================


def test_get_product_info_builds_nested_info_structure():
    """Should build nested ProductInfo objects from branches."""
    branch = {
        "category": "vendor",
        "name": "VendorX",
        "branches": [
            {
                "category": "product_name",
                "name": "DeviceY",
                "branches": [
                    {
                        "category": "product_version",
                        "name": "1.2",
                        "product": {"name": "DeviceY", "product_id": "PID2"},
                    }
                ],
            }
        ],
    }

    infos = get_product_info(branch)

    # expect one leaf node result
    assert isinstance(infos, list)
    assert len(infos) == 1

    info = infos[0]
    assert isinstance(info, ProductInfo)
    assert info.manufacturer == "VendorX"
    assert info.product_name == "DeviceY"
    assert isinstance(info.product_version, ProductVersion)
    assert info.product_version.name == "1.2"
    assert info.product.product_id == "PID2"


def test_get_product_info_handles_empty_branch():
    """Should return a single ProductInfo if no sub-branches exist."""
    branch = {"category": "vendor", "name": "SoloVendor"}
    result = get_product_info(branch)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0].manufacturer == "SoloVendor"
