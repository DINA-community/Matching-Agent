"""Exercise PIH conversion and matching without external services."""

import math

import queue
from typing import Any

import pytest
from dina.plugins.datasource.isduba.isduba import process_document

from dina.cachedb.model import Asset, CsafProduct, Match, Product, ProductType
from dina.matcher.main import match_pairs


def run_pairs(
    csaf: CsafProduct,
    assets: list[Asset],
    weights: dict[str, float],
    threshold: float = 0.0,
) -> list[Match]:
    config = {"database": {"other_fields": weights}}
    pairs = []
    for asset in assets:
        pairs.append((csaf, asset))

    output = queue.Queue()
    match_pairs(
        task_id=1,
        matches=output,
        log_queue=None,
        logging_config=None,
        pairs=pairs,
        threshold=threshold,
        matching_config=config,
        matching_config_hash="pih-test",
    )
    _task_id, _processed_pairs, matches = output.get_nowait()
    return matches


def csaf_product(helper: dict[str, Any]) -> CsafProduct:
    document = {
        "document": {"title": "PIH regression", "csaf_version": "2.0"},
        "product_tree": {
            "branches": [
                {
                    "category": "product_name",
                    "name": "Example product",
                    "product": {
                        "name": "Example product",
                        "product_id": "affected-product",
                        "product_identification_helper": helper,
                    },
                }
            ]
        },
    }
    products = process_document({"id": 55}, document, "https://advisories.example.org")
    assert len(products) == 1
    products[0].id = 11
    return products[0]


@pytest.mark.parametrize(
    "helper_field,asset_field,csaf_value,asset_value",
    [
        ("serial_numbers", "serial_numbers", ["SN-1"], ["other", " sn-1 "]),
        ("model_numbers", "model_numbers", ["MODEL-1"], ["model-1"]),
        ("skus", "part_numbers", ["PART-1"], ["part-1"]),
        (
            "sbom_urls",
            "sbom_urls",
            ["https://example.org/SBOM.json"],
            ["https://example.org/SBOM.json"],
        ),
    ],
    ids=["serial-number", "model-number", "sku-to-part-number", "sbom-url"],
)
def test_csaf_identifiers_reach_worker_scores(
    helper_field: str,
    asset_field: str,
    csaf_value: list[str],
    asset_value: list[str],
) -> None:
    csaf = csaf_product({helper_field: csaf_value})
    assets = []
    test_values = [(22, asset_value), (23, ["different"]), (24, [])]
    for asset_id, values in test_values:
        product = Product(product_type=ProductType.Device)
        setattr(product, asset_field, values)
        assets.append(Asset(id=asset_id, product=product))

    matches = run_pairs(csaf, assets, {asset_field: 1.0})

    assert len(matches) == 3
    assert matches[0].asset_id == 22
    assert math.isclose(matches[0].score, 100.0)
    assert matches[1].asset_id == 23
    assert math.isclose(matches[1].score, 0.0)
    assert matches[2].asset_id == 24
    assert math.isclose(matches[2].score, 0.0)

    accepted = run_pairs(csaf, assets, {asset_field: 1.0}, 50.0)

    assert len(accepted) == 1
    assert accepted[0].asset_id == 22
    assert math.isclose(accepted[0].score, 100.0)


def test_missing_pih_fields_do_not_dilute_available_evidence() -> None:
    csaf = csaf_product({
        "serial_numbers": ["SN-1"],
        "sbom_urls": ["https://example.org/SBOM.json"],
    })
    assets = [
        Asset(
            id=22,
            product=Product(
                product_type=ProductType.Device,
                serial_numbers=["SN-1"],
                sbom_urls=["https://example.org/sbom.json"],
            ),
        )
    ]
    weights = {"serial_numbers": 1.0, "sbom_urls": 1.0, "model_numbers": 1.0}

    matches = run_pairs(csaf, assets, weights, 50.0)

    assert len(matches) == 1
    assert matches[0].asset_id == 22
    assert math.isclose(matches[0].score, 50.0)
    assert run_pairs(csaf, assets, weights, 51.0) == []
