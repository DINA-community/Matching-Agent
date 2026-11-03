import pytest
import polars as pl

import numpy as np
from dina.matcher.matching import Matching
from packaging.version import Version


@pytest.fixture
def matcher():
    """Create a reusable Matching instance with all config sections."""
    config = {
        "database": {
            "freetext_fields_separator": ":",
            "freetext_fields_weights": {"token": 0.5, "ngram": 0.25, "overlap": 0.25},
            "freetext_fields": {"name": 1.0, "manufacturer_name": 1.0},
            "ordered_fields": {"version": 1.0},
            "other_fields": {"cpe": 0.5, "purl": 0.5},
        },
        "ngram": {"weights": {2: 0.5, 3: 0.5}},
        "levenshtein": {"max_distance": 1},
        "version": {
            "weights": {"min_max_version": 0.5, "qualifier": 0.5, "release_number": 0.5}
        },
        "cpe": {"csaf_cpe_field_name": "csaf_cpe", "weights": {"version": 0.3}},
        "purl": {"csaf_purl_field_name": "csaf_purl", "weights": {"version": 0.3}},
    }
    return Matching(config)


# -------------------------------
# BASIC HELPER TESTS
# -------------------------------


def test_safe_version(matcher):
    assert matcher._safe_version("1.2.3") == Version("1.2.3")
    assert matcher._safe_version("abc") is None
    assert matcher._safe_version(None) is None
    assert matcher._safe_version("not_a_version") is None


def test_weighted_mean(matcher):
    assert matcher._weighted_mean([], []) == 0.0
    assert matcher._weighted_mean([1], []) == 0.0
    assert matcher._weighted_mean([1, np.nan, 0.5], [1, 1, 1]) == 0.75


def test_safe_load(matcher):
    assert matcher._safe_load(None) is None
    assert matcher._safe_load("{}") == {}
    assert matcher._safe_load("{not-json}") is None
    assert matcher._safe_load('{"key": "value"}') == {"key": "value"}
    assert matcher._safe_load({"a": 1}) == {"a": 1}
    assert matcher._safe_load("") is None
    assert matcher._safe_load('{"a": 1}') == {"a": 1}


def test_extract_field(matcher):
    d = {"name": "nginx", "version": {"raw": "1.0"}}
    assert matcher._extract_field(d, "name") == "nginx"
    assert matcher._extract_field(d, "version") == {"raw": "1.0"}
    assert matcher._extract_field("{}", "version") is None
    assert matcher._extract_field({"version": "1.0.0"}, "version") == {"raw": "1.0.0"}
    result = matcher._extract_field('{"version": "{\\"raw\\": \\"2.0\\"}"}', "version")
    assert isinstance(result, dict) and "raw" in result
    assert result == {"raw": "2.0"}
    assert matcher._extract_field({"version": 123}, "version") == {"raw": "123"}
    assert matcher._extract_field('{"something": 1}', "version") is None
    assert matcher._extract_field("", "version") is None
    assert matcher._extract_field(123, None) is None


def test_has_valid_json(matcher):
    df = pl.DataFrame({"col": ['{"a": 1}', "null", None]})
    assert matcher._has_valid_json(df, "col")
    df_invalid = pl.DataFrame({"col": ["x", None]})
    assert not matcher._has_valid_json(df_invalid, "col")


# -------------------------------
# FREETEXT TESTS
# -------------------------------


def test_compare_freetext(matcher):
    assert matcher._compare_freetext("nginx", "nginx") == 1.0
    assert matcher._compare_freetext("nginx:web", "nginx:server") == 0.375
    assert matcher._compare_freetext("", "") is None
    assert matcher._compare_freetext(None, "") is None
    assert matcher._compare_freetext("foo", "bar") == 0.0
    score = matcher._compare_freetext(123, "123!")
    assert isinstance(score, float)
    assert score >= 0.375
    assert matcher._compare_freetext("abc", None) is None
    assert matcher._compare_freetext(1234, 1234) == 1.0
    assert isinstance(matcher._compare_freetext(["a"], ["a"]), float)
    assert matcher._compare_freetext("   ", " ") is None
    assert matcher._compare_freetext("@@@", "$$$") == 0.0
    assert matcher._compare_freetext("foo", "") is None


def test_tokenize_clean_and_ngram(matcher):
    t1, t2 = matcher._tokenize_freetext("a:b", "a:b:c", ignore_order=True)
    assert "a" in t1
    assert "c" in t2
    assert all(isinstance(x, str) for x in matcher._clean_tokens(t1))
    ngrams = matcher._ngrams_from_tokens(["x", "y", "z"], 2)
    assert isinstance(ngrams, list)
    assert matcher._ngram_similarity(["a"], ["a"]) == 1.0
    assert matcher._ngrams_from_tokens([], n=2) == []


def test_ngram_similarity(matcher):
    matcher.ngram_weights = {"x": "y"}  # invalid type keys
    assert matcher._weighted_ngram_similarity(["a"], ["a"], True) == 0.0
    matcher.ngram_weights = {2: 0.3, 3: 0.7}
    score = matcher._weighted_ngram_similarity(["a", "b", "c"], ["a", "b", "x"], True)
    assert score == 0.81
    matcher.ngram_weights = {}
    score = matcher._weighted_ngram_similarity([], [], True)
    assert score == 0.0

    matcher.ngram_weights = {1: 0.2, 2: 0.3, 3: 0.5}

    test_cases = [
        {
            "name": "Test empty value",
            "asset_tokens": [],
            "csaf_tokens": ["a"],
            "min_score": 0.0,
            "max_score": 0.0,
        },
        {
            "name": "Partial overlap - nginx server vs proxy",
            "asset_tokens": ["nginx", "server"],
            "csaf_tokens": ["nginx", "proxy"],
            "min_score": 0.0,
            "max_score": 0.5,
        },
        {
            "name": "Typo tolerance test",
            "asset_tokens": ["a", "servder"],
            "csaf_tokens": ["ngianx", "proxdy"],
            "min_score": 0.0,
            "max_score": 0.1,
        },
        {
            "name": "Industrial product naming variation",
            "asset_tokens": ["et200sp", "im155-6", "profinet"],
            "csaf_tokens": ["et200sp", "155-6", "pn", "interface", "module"],
            "min_score": 0.0,
            "max_score": 0.5,
        },
        {
            "name": "Different product series",
            "asset_tokens": ["S7-600", "at"],
            "csaf_tokens": ["S7-400", "at"],
            "min_score": 0.5,
            "max_score": 1.0,
        },
        {
            "name": "Additional CSAF context tokens",
            "asset_tokens": ["nginx", "proxy"],
            "csaf_tokens": ["manager", "nginx", "proxy"],
            "min_score": 0.6,
            "max_score": 1.0,
        },
    ]

    for case in test_cases:
        score = matcher._weighted_ngram_similarity(
            case["asset_tokens"], case["csaf_tokens"], ignore_order=True
        )
        assert case["min_score"] <= score <= case["max_score"]


def test_token_similarity(matcher):
    matcher.levenshtein_max_distance = 0
    sim = matcher._token_similarity(["abc"], ["xyz"])
    assert sim == 0.0


# -------------------------------
# VERSION COMPARISON TESTS
# -------------------------------


def test_range_in_range(matcher):
    test_cases = [
        {
            "name": "Partial overlap",
            "asset_range": {"min": "16.9", "max": "17.5"},
            "csaf_range": {"min": "17.0", "max": "18.0"},
            "expected": True,
        },
        {
            "name": "Asset completely before CSAF",
            "asset_range": {"min": "15.0", "max": "16.5"},
            "csaf_range": {"min": "17.0", "max": "18.0"},
            "expected": False,
        },
        {
            "name": "Asset fully inside CSAF",
            "asset_range": {"min": "17.2", "max": "17.8"},
            "csaf_range": {"min": "17.0", "max": "18.0"},
            "expected": True,
        },
        {
            "name": "Asset starts after CSAF upper bound",
            "asset_range": {"min": "18.0", "max": "19.0", "min_inclusive": False},
            "csaf_range": {"min": "17.0", "max": "18.0", "max_inclusive": True},
            "expected": False,
        },
        {
            "name": "Overlap at inclusive boundary",
            "asset_range": {"min": "18.0", "max": "19.0", "min_inclusive": True},
            "csaf_range": {"min": "17.0", "max": "18.0", "max_inclusive": True},
            "expected": True,
        },
        {
            "name": "No overlap at exclusive boundary",
            "asset_range": {"min": "18.0", "max": "19.0", "min_inclusive": True},
            "csaf_range": {"min": "17.0", "max": "18.0", "max_inclusive": False},
            "expected": False,
        },
        {
            "name": "Asset open on lower side, still overlaps",
            "asset_range": {"min": None, "max": "17.5"},
            "csaf_range": {"min": "17.0", "max": "18.0"},
            "expected": True,
        },
        {
            "name": "Asset open on upper side, completely after CSAF",
            "asset_range": {"min": "19.0", "max": None},
            "csaf_range": {"min": "17.0", "max": "18.0"},
            "expected": False,
        },
        {
            "name": "Both ranges open",
            "asset_range": {"min": None, "max": None},
            "csaf_range": {"min": None, "max": None},
            "expected": True,
        },
        {
            "name": "Same single version inclusive",
            "asset_range": {
                "min": "17.0",
                "max": "17.0",
                "min_inclusive": True,
                "max_inclusive": True,
            },
            "csaf_range": {
                "min": "17.0",
                "max": "17.0",
                "min_inclusive": True,
                "max_inclusive": True,
            },
            "expected": True,
        },
        {
            "name": "Same single version exclusive",
            "asset_range": {
                "min": "17.0",
                "max": "17.0",
                "min_inclusive": True,
                "max_inclusive": True,
            },
            "csaf_range": {
                "min": "17.0",
                "max": "17.0",
                "min_inclusive": False,
                "max_inclusive": False,
            },
            "expected": False,
        },
    ]

    for case in test_cases:
        result = matcher._range_in_range(case["asset_range"], case["csaf_range"])
        assert result is case["expected"], (
            f"{case['name']}: expected {case['expected']}, got {result} "
            f"for asset_range={case['asset_range']} and csaf_range={case['csaf_range']}"
        )


def test_compare_release_numbers(matcher):
    assert matcher._compare_release_numbers("1.2.3", "1.2.3") == 1.0
    assert matcher._compare_release_numbers("1.2.3", "1.5.0") == 0.5
    assert matcher._compare_release_numbers("1.2.3", "2.0.0") == 0.0
    assert np.isnan(matcher._compare_release_numbers(None, None))
    assert matcher._compare_release_numbers("x.y.z", "1.2.3") == 0.0


def test_compare_version_ranges(matcher):
    csaf = {"min_max_version": [{"min": "1"}]}
    asset = {"min_max_version": [{"max": "2"}]}
    val = matcher._compare_version_ranges(csaf, asset)
    assert val == 1.0
    csaf = {"min_max_version": []}
    asset = {"min_max_version": []}
    assert np.isnan(matcher._compare_version_ranges(csaf, asset))
    assert np.isnan(matcher._compare_version_ranges(None, None))
    csaf = {"min_max_version": [{"min": "1"}]}
    asset = [{"min": "1"}]
    val = matcher._compare_version_ranges(csaf, asset)
    assert val in (0.0, 1.0, np.nan)


def test_compare_versions(matcher):
    csaf = {
        "schema": "semver",
        "release_number": "1.0.0",
        "qualifier": None,
        "min_max_version": [{"min": "1.0.0", "max": "1.0.0"}],
    }
    asset = {
        "schema": "semver",
        "release_number": "1.0.0",
        "qualifier": None,
        "min_max_version": [{"min": "1.0.0", "max": "1.0.0"}],
    }
    assert matcher._compare_versions(csaf, asset) > 0.8

    csaf["min_max_version"] = [{"min": "1", "max": "2"}]

    assert matcher._compare_versions(csaf, asset) == 1.0

    assert (
        matcher._compare_fields(
            csaf,
            asset,
            {
                "schema": 0.05,
                "release_number": 0.10,
                "qualifier": 0.10,
                "min_max_version": 0.75,
            },
        )
        == 1.0
    )

    csaf["min_max_version"] = [{"min": None, "max": "17.2"}]
    assert 0.9 <= matcher._compare_versions(csaf, asset) <= 1.0

    csaf["min_max_version"] = [{"min": "17.-2", "max": None}]
    assert matcher._compare_versions(csaf, asset) <= 0.1

    # invalid cases
    assert matcher._compare_versions(None, asset) == 0.0
    assert matcher._compare_versions(csaf, None) == 0.0
    assert matcher._compare_versions(None, None) is None


def test_compare_version_lists(matcher):
    c = [{"min_max_version": [{"min": "1", "max": "2"}]}]
    a = [{"min_max_version": [{"min": "1", "max": "2"}]}]
    assert matcher._compare_version_lists(c, a) in (1.0, 0.0)


def test_compare_qualifiers_and_edge(matcher):
    assert (
        matcher._compare_qualifiers({"qualifier": "alpha"}, {"qualifier": "beta"})
        == 1.0
    )
    assert np.isnan(
        matcher._compare_qualifiers({"qualifier": None}, {"qualifier": None})
    )
    assert np.isnan(matcher._compare_qualifiers(None, None))
    assert (
        matcher._compare_qualifiers({"qualifier": "alpha"}, {"qualifier": "alpha.1"})
        == 1.0
    )
    assert (
        matcher._compare_qualifiers({"qualifier": 123}, {"qualifier": [1, 2, 3]}) == 1.0
    )


# -------------------------------
# FIELD COMPARISON TESTS
# -------------------------------


def test_compare_string_fields(matcher):
    assert matcher._compare_string_fields("a", "a") == 1.0


def test_compare_list_fields(matcher):
    assert matcher._compare_list_fields(["x"], ["y"]) == 0.0


def test_compare_dict_fields(matcher):
    """Covers case where values are None in both dicts."""
    assert matcher._compare_dict_fields({"x": None}, {"x": None}, {"x": 1.0}) == 0.0
    assert matcher._compare_dict_fields({"x": "a"}, {"x": "a"}, None) == 0.0
    assert matcher._compare_dict_fields(None, None, None) == 0.0
    assert matcher._compare_dict_fields({}, {}, {"x": 0.0}) == 0.0
    assert (
        matcher._compare_dict_fields(
            {"version": {"min_max_version": [{"min": "1"}]}},
            {"version": {"min_max_version": [{"min": "1"}]}},
            {"version": 1.0},
        )
        == 1.0
    )


def test_compare_fields(matcher):
    assert matcher._compare_fields("a", ["a"]) == 0.0
    assert matcher._compare_fields(["a"], ["b"]) == 0.0
    assert matcher._compare_fields({"x": "a"}, {"x": "a"}) >= 0.0
    assert matcher._compare_fields(None, None) is None
    assert matcher._compare_fields(42, {"a": 1}) == 0.0
    assert matcher._compare_fields({"a": 1}, 42) == 0.0
    assert matcher._compare_fields({}, {}) is None
    assert matcher._compare_fields({"a": "b"}, ["c"]) == 0.0
    assert matcher._compare_fields("a", {"b": "c"}) == 0.0


# -------------------------------
# POLARS DF TESTS (INTEGRATION)
# -------------------------------

# =====================================================
# DATAFRAME-BASED MATCHING TESTS
# =====================================================


def test_df_matching_runs(matcher):
    """Basic df_matching sanity check."""
    df = pl.DataFrame(
        {
            "csaf_cpe": [
                '{"version": {"min_max_version": [{"min": "1.0", "max": "1.0"}]}}'
            ],
            "csaf_purl": [
                '{"version": {"min_max_version": [{"min": "1.0", "max": "1.0"}]}}'
            ],
            "csaf_version": ['{"min_max_version": [{"min": "1.0", "max": "1.0"}]}'],
            "asset_version": ['{"min_max_version": [{"min": "1.0", "max": "1.0"}]}'],
        }
    )
    result = matcher.df_matching(df)
    assert isinstance(result, pl.DataFrame), "Expected Polars DataFrame output"


# =====================================================
# FREETEXT MATCHING TESTS
# =====================================================


@pytest.mark.parametrize(
    "df_data",
    [
        {
            "asset_name": ["foo"],
            "csaf_cpe": ['{"vendor": "foo"}'],
            "csaf_purl": ['{"version": {"min": "1"}}'],
            "csaf_name": ["foo"],
        },
        {
            "asset_name": ["foo"],
            "csaf_name": ["foo"],
            "csaf_cpe": ["not_json"],
            "csaf_purl": ['{"version": {"min": "1"}}'],
        },
        {},
        {"asset_name": ["abc"], "csaf_name": ["abc"]},
    ],
)
def test_match_freetext_fields_various(matcher, df_data):
    """Test _match_freetext_fields across valid, invalid, and empty cases."""
    matcher.freetext_fields = {"name": 1.0, "manufacturer_name": 1.0}
    df = pl.DataFrame(df_data) if df_data else pl.DataFrame()
    result = matcher._match_freetext_fields(df, df, "csaf_cpe")
    assert isinstance(result, pl.DataFrame)
    if len(df.columns) > 0:
        assert all(isinstance(c, str) for c in result.columns)


# =====================================================
# ORDERED FIELD MATCHING TESTS
# =====================================================


@pytest.mark.parametrize(
    "df_data",
    [
        {
            "csaf_version": ['{"min_max_version": [{"min": "1"}]}'],
            "asset_version": ['{"min_max_version": [{"min": "1"}]}'],
            "csaf_cpe": ['{"version": {"min": "1"}}'],
            "csaf_purl": ['{"version": {"min": "1"}}'],
        },
        {
            "csaf_version": ["invalid"],
            "asset_version": ['{"min_max_version": [{"min": "1"}]}'],
            "csaf_cpe": ["invalid"],
            "csaf_purl": ["invalid"],
        },
    ],
)
def test_match_ordered_fields_various(matcher, df_data):
    """Test _match_ordered_fields for valid and invalid JSON inputs."""
    df = pl.DataFrame(df_data)
    result = matcher._match_ordered_fields(df, df, "csaf_cpe", "csaf_purl")
    assert isinstance(result, pl.DataFrame)


# =====================================================
# OTHER FIELD MATCHING TESTS
# =====================================================


@pytest.mark.parametrize(
    "df_data",
    [
        {
            "csaf_cpe": ['{"version": {"min": "1"}}'],
            "asset_cpe": ['{"version": {"min": "1"}}'],
            "csaf_purl": ['{"version": {"min": "1"}}'],
            "asset_purl": ['{"version": {"min": "1"}}'],
        },
        {
            "csaf_cpe": ['{"version": {"min": "1"}}'],
            "asset_purl": ['{"version": {"min": "1"}}'],
        },
        {
            "csaf_cpe": ["invalid"],
            "asset_cpe": ["invalid"],
            "csaf_purl": ["invalid"],
            "asset_purl": ["invalid"],
        },
        {},
        {"csaf_cpe": ['{"v":1}'], "csaf_purl": ['{"v":1}']},
    ],
)
def test_match_other_fields_various(matcher, df_data):
    """Test _match_other_fields robustness across data types."""
    df = pl.DataFrame(df_data) if df_data else pl.DataFrame()
    result = matcher._match_other_fields(df, "csaf_cpe", "csaf_purl")
    assert isinstance(result, pl.DataFrame)
    assert result is not None
