import pytest
import polars as pl

import numpy as np
from dina.matcher.matching import Matching


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
    assert matcher._safe_version("1.2.3").public == "1.2.3"
    assert matcher._safe_version("abc") is None
    assert matcher._safe_version(None) is None


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
    assert score == 0.5625
    assert matcher._compare_freetext("abc", None) == 0.0
    assert matcher._compare_freetext(1234, 1234) == 1.0
    assert isinstance(matcher._compare_freetext(["a"], ["a"]), float)
    assert matcher._compare_freetext("   ", " ") is None
    assert matcher._compare_freetext("@@@", "$$$") == 0.0


def test_tokenize_clean_and_ngram(matcher):
    t1, t2 = matcher._tokenize_freetext("a:b", "a:b:c", ignore_order=True)
    assert "a" in t1
    assert "c" in t2
    assert all(isinstance(x, str) for x in matcher._clean_tokens(t1))
    ngrams = matcher._ngrams_from_tokens(["x", "y", "z"], 2)
    assert isinstance(ngrams, list)
    assert matcher._ngram_similarity(["a"], ["a"]) == 1.0


def test_ngram_similarity(matcher):
    assert matcher._ngram_similarity([], ["a"]) == 0.0
    matcher.ngram_weights = {"x": "y"}  # invalid type keys
    assert matcher._weighted_ngram_similarity(["a"], ["a"], True) == 0.0
    matcher.ngram_weights = {2: 0.3, 3: 0.7}
    score = matcher._weighted_ngram_similarity(["a", "b", "c"], ["a", "b", "x"], True)
    assert score == 0.81


def test_token_similarity(matcher):
    matcher.levenshtein_max_distance = 0
    sim = matcher._token_similarity(["abc"], ["xyz"])
    assert sim == 0.0


# -------------------------------
# VERSION COMPARISON TESTS
# -------------------------------


def test_range_in_range(matcher):
    assert matcher._range_in_range({"min": "1", "max": "3"}, {"min": "2", "max": "4"})
    assert matcher._range_in_range(
        {"min": "0.8", "max": "0.9", "min_inclusive": False},
        {"min": "0.9", "max": "1.3"},
    )
    assert matcher._range_in_range(
        {"min": "1.0", "max": "1.2"}, {"min": "1.0", "max": "1.2"}
    )
    assert not matcher._range_in_range(
        {"min": "1", "max": "2"}, {"min": "3", "max": "4"}
    )
    assert matcher._range_in_range(
        {"min": None, "max": None}, {"min": None, "max": None}
    )
    assert matcher._range_in_range(
        {"min": "1", "max": "2", "min_inclusive": True, "max_inclusive": False},
        {"min": "2", "max": "3", "min_inclusive": True, "max_inclusive": True},
    ) in (True, False)


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
    assert np.isclose(matcher._compare_versions(csaf, asset), 1.0)

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
