import multiprocessing
import queue
from pathlib import Path
from types import SimpleNamespace

from dina.common.log import LoggingConfig
from dina.matcher.config_hash import hash_matching_config
from dina.matcher.main import match_pairs


def test_hash_matching_config_is_order_independent():
    a = {"database": {"freetext_fields": {"name": 1.0, "manufacturer_name": 0.5}}}
    b = {"database": {"freetext_fields": {"manufacturer_name": 0.5, "name": 1.0}}}
    assert hash_matching_config(a) == hash_matching_config(b)


def test_match_pairs_sets_run_and_config_hash():
    cfg = {
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
        "threshold": {
            "vendor": 60,
            "product_family": 50,
            "product_name": 70,
            "keyword": 65,
            "version": 65,
        },
    }
    product_dict = {
        "name": "demo",
        "manufacturer_name": "vendor",
        "version": {"min_max_version": [{"min": "1.0", "max": "1.0"}]},
        "cpe": None,
        "purl": None,
    }
    csaf = SimpleNamespace(
        id=11, product=SimpleNamespace(to_dict=lambda: dict(product_dict))
    )
    asset = SimpleNamespace(
        id=22, product=SimpleNamespace(to_dict=lambda: dict(product_dict))
    )
    out_q: queue.Queue = queue.Queue()
    log_q = multiprocessing.Queue()
    cfg_hash = hash_matching_config(cfg)

    match_pairs(
        task_id=99,
        matches=out_q,
        log_queue=log_q,
        logging_config=LoggingConfig(file=Path("/tmp/matcher-test.log")),
        pairs=[(csaf, asset)],
        threshold=-1.0,
        matching_config=cfg,
        matching_config_hash=cfg_hash,
    )

    task_id, processed_pairs, matches = out_q.get()
    assert task_id == 99
    assert processed_pairs == [(11, 22)]
    assert all(m.matcher_run_id == 99 for m in matches)
    assert all(m.matching_config_hash == cfg_hash for m in matches)
