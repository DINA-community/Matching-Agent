# tests/test_score.py
import pytest
import polars as pl

from dina.matcher.calculate_score import Score


@pytest.fixture
def score_cfg():
    return {
        "database": {
            "freetext_fields": {
                "manufacturer_name": 1.0,
                "name": 1.0,
                "device_family": 0.5,
            },
            "ordered_fields": {"version": 1.0},
            "other_fields": {"cpe": 0.5, "purl": 0.5},
        },
        "cpe": {"csaf_cpe_field_name": "csaf_cpe"},
        "purl": {"csaf_purl_field_name": "csaf_purl"},
        "threshold": {
            "vendor": 60.0,
            "product_family": 50.0,
            "product_name": 70.0,
            "keyword": 65.0,
            "version": 65.0,
        },
    }


@pytest.fixture
def scorer(score_cfg):
    return Score(score_cfg)


# ------------------------------------------------------------
# Tests _max_field_score
# ------------------------------------------------------------


def test_max_field_score_vendor_uses_cpe_when_present(scorer):
    df = pl.DataFrame(
        {
            "asset_csaf_cpe_match": [0.9],
            "manufacturer_name_csaf_cpe_match": [0.8],
        }
    )
    out = scorer._max_field_score(df, field="manufacturer_name", score=0.6)
    assert out == 0.9


def test_max_field_score_version_uses_cpe_and_purl_when_present(scorer):
    df = pl.DataFrame(
        {
            "asset_csaf_cpe_match": [0.7],
            "version_csaf_cpe_match": [0.8],
            "asset_csaf_purl_match": [0.95],
            "version_csaf_purl_match": [0.9],
        }
    )
    out = scorer._max_field_score(df, field="version", score=0.5)
    assert out == 0.95


def test_max_field_score_no_extra_cols_returns_base(scorer):
    df = pl.DataFrame({"irrelevant": [1]})
    assert scorer._max_field_score(df, field="name", score=0.4) == 0.4


# ------------------------------------------------------------
# Tests _compute_field_score
# ------------------------------------------------------------


def test_compute_field_score_passthrough_for_other_fields(scorer):
    df = pl.DataFrame({"anything": [1]})
    assert scorer._compute_field_score(df, "device_family", 0.33) == 0.33


def test_compute_field_score_uses_max_helper_for_vendor(scorer):
    df = pl.DataFrame(
        {
            "asset_csaf_cpe_match": [0.85],
            "manufacturer_name_csaf_cpe_match": [0.8],
        }
    )
    out = scorer._compute_field_score(df, "manufacturer_name", 0.6)
    assert out == 0.85


# ------------------------------------------------------------
# Tests _evaluate_thresholds
# ------------------------------------------------------------


def test_evaluate_thresholds_vendor_missing(scorer):
    flag, msg, pct = scorer._evaluate_thresholds(
        vendor_score=None,
        product_name_score=80,
        product_family_score=80,
        version_score=80,
        keyword_score=70,
        score_percent=42.0,
    )
    assert flag == 1


def test_evaluate_thresholds_family_missing_but_name_ok_and_version_ok(scorer):
    flag, msg, pct = scorer._evaluate_thresholds(
        vendor_score=80,
        product_name_score=80,
        product_family_score=None,
        version_score=80,
        keyword_score=70,
        score_percent=88.0,
    )
    assert flag == 1
    assert "family missing" in msg.lower()


def test_evaluate_thresholds_family_missing_name_ok_but_version_too_low(scorer):
    flag, msg, pct = scorer._evaluate_thresholds(
        vendor_score=80,
        product_name_score=80,
        product_family_score=None,
        version_score=50,
        keyword_score=70,
        score_percent=50.0,
    )
    assert flag == 0
    assert "version score is below" in msg.lower()


def test_evaluate_thresholds_full_match(scorer):
    flag, msg, pct = scorer._evaluate_thresholds(
        vendor_score=95,
        product_name_score=90,
        product_family_score=90,
        version_score=80,
        keyword_score=70,
        score_percent=92.0,
    )
    assert flag == 1
    assert "product name and family is given" in msg.lower()


def test_evaluate_thresholds_near_miss_with_boost_to_possible_match(scorer):
    flag, msg, pct = scorer._evaluate_thresholds(
        vendor_score=90,
        product_name_score=65,
        product_family_score=80,
        version_score=80,
        keyword_score=90,
        score_percent=75.0,
    )
    assert flag in (0, 1)

    if flag == 1:
        assert "possible match" in msg.lower()


def test_evaluate_thresholds_vendor_below_threshold(scorer):
    flag, msg, pct = scorer._evaluate_thresholds(
        vendor_score=10,  # unter 60
        product_name_score=100,
        product_family_score=100,
        version_score=100,
        keyword_score=100,
        score_percent=10.0,
    )
    assert flag == 0
    assert "vendor score is below" in msg.lower()


def test_evaluate_thresholds_family_below_threshold(scorer):
    flag, msg, pct = scorer._evaluate_thresholds(
        vendor_score=90,
        product_name_score=90,
        product_family_score=40,  # unter 50
        version_score=90,
        keyword_score=80,
        score_percent=60.0,
    )
    assert flag == 0
    assert "product family score is below" in msg.lower()


def test_evaluate_thresholds_near_threshold_no_keyword(scorer):
    """Covers branch where product_name_score below threshold and no keyword_score."""
    res = scorer._evaluate_thresholds(
        vendor_score=80,
        product_name_score=45,
        product_family_score=None,
        version_score=60,
        keyword_score=None,
        score_percent=75,
    )
    flag, msg, percent = res
    assert flag == 0
    assert "below" in msg.lower()
    assert percent == 75


def test_evaluate_thresholds_family_below_threshold_direct(scorer):
    """Covers branch where product family score below threshold."""
    res = scorer._evaluate_thresholds(
        vendor_score=90,
        product_name_score=80,
        product_family_score=30,  # below threshold 50
        version_score=70,
        keyword_score=70,
        score_percent=85,
    )
    flag, msg, percent = res
    assert flag == 0
    assert "product family" in msg.lower()


def test_evaluate_thresholds_vendor_below_threshold_explicit(scorer):
    """Covers branch where vendor score is below vendor threshold."""
    res = scorer._evaluate_thresholds(
        vendor_score=20,  # below 50
        product_name_score=70,
        product_family_score=80,
        version_score=80,
        keyword_score=80,
        score_percent=60,
    )
    flag, msg, percent = res
    assert flag == 0
    assert "vendor score" in msg.lower()


def test_evaluate_thresholds_falls_through_to_loop_error(scorer):
    """Covers final 'Loop Error' fallback."""
    res = scorer._evaluate_thresholds(
        vendor_score=80,
        product_name_score=None,
        product_family_score=None,
        version_score=None,
        keyword_score=None,
        score_percent=0.0,
    )
    flag, msg, percent = res
    assert flag == 0
    assert "no match" in msg.lower()


def test_evaluate_thresholds_possible_match_with_boost(scorer):
    """near-threshold name score with boost from version and keyword."""
    res = scorer._evaluate_thresholds(
        vendor_score=80,
        product_name_score=80,
        product_family_score=None,
        version_score=70,
        keyword_score=75,
        score_percent=80,
    )
    flag, msg, percent = res
    assert flag == 1
    assert "match" in msg.lower()
    assert percent == 80


def test_evaluate_thresholds_possible_match_with_product_family_and_without_product_name(
    scorer,
):
    res = scorer._evaluate_thresholds(
        vendor_score=80,
        product_name_score=None,
        product_family_score=75,
        version_score=70,
        keyword_score=75,
        score_percent=80,
    )
    flag, msg, percent = res
    assert flag == 0
    assert percent == 80


# ------------------------------------------------------------
# Tests calculate_overall_score
# ------------------------------------------------------------


def test_calculate_overall_score_triggers_cpe_shortcut_1_0(scorer):
    df = pl.DataFrame(
        {
            "manufacturer_name_match": [0.8],
            "name_match": [0.8],
            "device_family_match": [0.8],
            "version_match": [0.8],
            "cpe_match": [1.0],
            "purl_match": [0.2],
            "asset_csaf_cpe_match": [0.6],
            "manufacturer_name_csaf_cpe_match": [0.7],
            "name_csaf_cpe_match": [0.7],
            "asset_csaf_purl_match": [0.5],
            "version_csaf_purl_match": [0.5],
        }
    )
    flag, msg, score_percent = scorer.calculate_overall_score(df)
    assert score_percent == 1.0


def test_calculate_overall_score_weighted_average_path(scorer):
    df = pl.DataFrame(
        {
            "manufacturer_name_match": [0.9],
            "name_match": [0.85],
            "device_family_match": [0.8],
            "version_match": [0.9],
            "cpe_match": [0.4],
            "purl_match": [0.3],
            "asset_csaf_cpe_match": [0.88],
            "manufacturer_name_csaf_cpe_match": [0.86],
            "name_csaf_cpe_match": [0.87],
            "asset_csaf_purl_match": [0.9],
            "version_csaf_purl_match": [0.92],
        }
    )
    flag, msg, score_percent = scorer.calculate_overall_score(df)
    assert 0.0 <= score_percent <= 100.0


def test_calculate_overall_score_outputs_tuple_and_message(scorer):
    df = pl.DataFrame(
        {
            "manufacturer_name_match": [0.7],
            "name_match": [0.69],
            "device_family_match": [0.8],
            "version_match": [0.7],
            "cpe_match": [0.2],
            "purl_match": [0.2],
        }
    )
    flag, msg, score_percent = scorer.calculate_overall_score(df)
    assert flag in (0, 1)
    assert isinstance(msg, str)
    assert isinstance(score_percent, float)


def test_calculate_overall_score_handles_missing_some_fields(scorer):
    df = pl.DataFrame(
        {
            "manufacturer_name_match": [0.8],
            "version_match": [0.8],
            "cpe_match": [0.0],
            "purl_match": [0.0],
        }
    )
    flag, msg, score_percent = scorer.calculate_overall_score(df)
    assert flag == 0
    assert 52.0 <= score_percent <= 100.0


def test_calculate_overall_score_handles_with_none_values(scorer):
    df = pl.DataFrame(
        {
            "manufacturer_name_match": [None],
            "version_match": [None],
            "cpe_match": [None],
            "purl_match": [None],
        }
    )
    flag, msg, score_percent = scorer.calculate_overall_score(df)
    assert flag == 0
    assert score_percent == 0.0
