import pytest

from dina.plugins.preprocessing.default.normalizer import Normalizer, Standards


@pytest.fixture
def normalizer():
    """Create a Normalizer with minimal config."""
    config = {
        "database": {"freetext_fields_separator": ":"},
        "version": {"weights": {"schema": 1, "raw": 1}},
        "cpe": {
            "weights": {
                "part": 1,
                "vendor": 1,
                "product": 1,
                "version": 1,
                "update": 1,
                "edition": 1,
                "raw": 1,
            }
        },
        "purl": {
            "weights": {
                "type": 1,
                "namespace": 1,
                "name": 1,
                "version": 1,
                "qualifiers": 1,
                "subpath": 1,
            }
        },
    }
    return Normalizer(config)


# ==========================================================
# parse_freetext
# ==========================================================


def test_parse_freetext_basic(normalizer):
    assert normalizer.parse_freetext("Hello World 2024") == "hello:world:2024"


def test_parse_freetext_none_returns_none(normalizer):
    assert normalizer.parse_freetext(None) is None


# ==========================================================
# _detect_schema
# ==========================================================


@pytest.mark.parametrize(
    "expr,expected",
    [
        ("vers:pypi/1.2.3", Standards.VERS),
        (">=1.0.0", Standards.VLS),
        ("22.04", Standards.CALVER),
        ("1.2.3", Standards.SEMVER),
        ("grafana-0:5.2.4-6.el7.src", Standards.RPM),
        ("r15b_sp3", Standards.ERICSSON_RELEASE_SCHEMA),
        ("1.0a1", Standards.PEP440),
        ("6.+.9", Standards.WILDCARD),
        ("1:2.31.1-0ubuntu9.9", Standards.DEB),
        ("random-text", Standards.FREETEXT),
        ("v4.2sp3", Standards.SAP),
    ],
)
def test_detect_schema(normalizer, expr, expected):
    assert normalizer._detect_schema(expr) == expected


# ==========================================================
# parse_version
# ==========================================================


def test_parse_version_semver(normalizer):
    result = normalizer.parse_version("1.2.3-alpha+build5")
    assert result["schema"] == Standards.SEMVER.value
    assert result["release_number"] == "1.2.3"
    assert result["qualifier"] == "alpha"
    assert result["build_number"] == "build5"
    assert result["min_max_version"][0]["min"] == "1.2.3"


def test_parse_version_calver(normalizer):
    result = normalizer.parse_version("2024.11.10")
    assert result["schema"] == Standards.CALVER.value
    assert result["date"]["year"] == 2024
    assert result["date"]["month"] == 11


def test_parse_version_freetext(normalizer):
    result = normalizer.parse_version("customVersionXYZ")
    assert result["schema"] == Standards.FREETEXT.value
    assert "customversionxyz" in result["raw"]


def test_parse_version_list_input(normalizer):
    lst = ["1.0.0", "2.0.0"]
    results = normalizer.parse_version(lst)
    assert isinstance(results, list)
    assert all(r["schema"] == Standards.SEMVER.value for r in results)


def test_parse_version_dict_passthrough(normalizer):
    data = {"schema": "semantic-versioning", "raw": "1.0.0"}
    assert normalizer.parse_version(data) == data


# ==========================================================
# parse_cpe
# ==========================================================


def test_parse_cpe_2_3(normalizer):
    cpe = "cpe:2.3:a:redhat:rhel_eus:8.1:*:*:*:*:*:*:*"
    result = normalizer.parse_cpe(cpe)
    assert result["vendor"] == "redhat"
    assert result["product"] == "rhel_eus"
    assert result["raw"].startswith("cpe:2.3:")


def test_parse_cpe_legacy(normalizer):
    cpe = "cpe:/a:redhat:jboss_fuse:6.3"
    result = normalizer.parse_cpe(cpe)
    assert result["vendor"] == "redhat"
    assert result["product"] == "jboss_fuse"
    assert isinstance(result["version"], dict)
    assert result["raw"].startswith("cpe:2.3:")


def test_parse_cpe_invalid(normalizer):
    assert normalizer.parse_cpe("notacpe") is None


# ==========================================================
# parse_purl
# ==========================================================


def test_parse_purl_basic(normalizer):
    purl = "pkg:pypi/example@1.0.0"
    result = normalizer.parse_purl(purl)
    assert result["type"] == "pypi"
    assert result["name"] == "example"
    assert result["version"]["schema"] == Standards.SEMVER.value


def test_parse_purl_with_qualifiers(normalizer):
    purl = "pkg:deb/debian/curl@7.50.3-1?arch=i386&distro=jessie"
    result = normalizer.parse_purl(purl)
    assert "arch" in result["qualifiers"]
    assert result["qualifiers"]["distro"] == "jessie"


def test_parse_purl_invalid(normalizer):
    assert normalizer.parse_purl("invalid:purl") is None


# ==========================================================
# parse_files
# ==========================================================


class DummyFile:
    def __init__(self, name, hash_algorithm, file_hash):
        self.name = name
        self.hash_algorithm = hash_algorithm
        self.file_hash = file_hash


class DummyFileList:
    def __init__(self, files):
        self.files = files


def test_parse_files_basic(normalizer):
    files = DummyFileList([DummyFile("mybinary-1.0.0.tar.gz", "sha256", "abc123")])
    result = normalizer.parse_files(files)
    assert len(result) == 1
    assert result[0]["name"] == "mybinary:1:0:0:tar:gz"
    assert result[0]["hash_algorithm"] == "sha256"


def test_parse_files_empty(normalizer):
    assert normalizer.parse_files(None) == []
    assert normalizer.parse_files(DummyFileList([])) == []


# ==========================================================
# _parse_sap
# ==========================================================


def test_parse_sap(normalizer):
    result = normalizer._parse_sap("v7 sp2 upd1")
    assert result["schema"] == Standards.SAP.value
    assert result["qualifier"] == ["sp", 2]
    assert result["build_number"] == "upd1"
    assert result["min_max_version"][0]["min"].startswith("7.")


# ==========================================================
# _parse_csaf
# ==========================================================


def test_parse_csaf_vls(normalizer):
    result = normalizer._parse_csaf(Standards.VLS, ">=1.0.0|<2.0.0")
    assert result["schema"] == Standards.VLS.value
    assert len(result["min_max_version"]) == 2


# ==========================================================
# _parse_ericsson
# ==========================================================


def test_parse_ericsson(normalizer):
    result = normalizer._parse_ericsson("r18c_mr2")
    assert result["schema"] == Standards.ERICSSON_RELEASE_SCHEMA.value
    assert result["release_number"] == 18
    assert result["qualifier"] == ["MR", 2]
