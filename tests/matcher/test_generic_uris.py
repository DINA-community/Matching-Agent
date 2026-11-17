"""Generic URI matching preserves the namespace and the complete URI."""

import polars as pl
import pytest

from dina.cachedb.model import Product, ProductType
from dina.matcher.main import _product_columns
from dina.matcher.matching import Matching


@pytest.mark.parametrize(
    "asset,expected",
    [
        ([{"namespace": "urn:vendor", "uri": "https://example.org/A"}], 1.0),
        ([{"namespace": "urn:other", "uri": "https://example.org/A"}], 0.0),
        ([{"namespace": "urn:vendor", "uri": "https://example.org/a"}], 0.0),
        (
            [
                {"namespace": "urn:vendor", "uri": "https://example.org/other"},
                {"namespace": "urn:other", "uri": "https://example.org/A"},
            ],
            0.0,
        ),
        (
            [
                {"namespace": "urn:other", "uri": "https://example.org/other"},
                {"namespace": "urn:vendor", "uri": "https://example.org/A"},
            ],
            1.0,
        ),
        ([{"uri": "https://example.org/A"}], 0.0),
        ([], None),
        (None, None),
    ],
)
def test_generic_uri_matching(
    asset: list[dict[str, str]] | None, expected: float | None
) -> None:
    csaf = Product(
        product_type=ProductType.Software,
        x_generic_uris=[{"namespace": "urn:vendor", "uri": "https://example.org/A"}],
    )
    product = Product(product_type=ProductType.Software, x_generic_uris=asset)
    df = pl.DataFrame(
        [
            {
                "csaf_x_generic_uris": _product_columns(csaf)["x_generic_uris"],
                "asset_x_generic_uris": _product_columns(product)["x_generic_uris"],
            }
        ]
    )
    matcher = Matching({"database": {"other_fields": {"x_generic_uris": 1.0}}})
    result = matcher._match_other_fields(df, "csaf_cpe", "csaf_purl")
    assert result["x_generic_uris_match"].item() == expected
