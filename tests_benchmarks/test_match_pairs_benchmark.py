import argparse
import asyncio
import itertools
import math
import multiprocessing
import statistics
import time
import tomllib
from pathlib import Path

import matplotlib.pyplot as plt
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import selectinload

from dina.cachedb.database import CacheDB
from dina.cachedb.model import Asset, CsafProduct
from dina.common.config import Config
from dina.matcher.main import match_pairs


def percentile(values: list[float], p: float) -> float:
    if not values:
        return 0.0
    if len(values) == 1:
        return values[0]
    values = sorted(values)
    k = (len(values) - 1) * p
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return values[int(k)]
    d0 = values[f] * (c - k)
    d1 = values[c] * (k - f)
    return d0 + d1


def iqr(values: list[float]) -> float:
    if not values:
        return 0.0
    q1 = percentile(values, 0.25)
    q3 = percentile(values, 0.75)
    return q3 - q1


async def load_assets_and_csafs(limit: int, config: Config):
    cache_db = CacheDB(config.Cachedb)
    await cache_db.connect()
    try:
        session_factory = async_sessionmaker(
            cache_db.engine,
            expire_on_commit=False,
        )

        async with session_factory() as session:
            assets_result = await session.execute(
                select(Asset)
                .options(selectinload(Asset.product))
                .where(Asset.product.has())
                .order_by(Asset.id)
                .limit(limit)
            )
            assets = list(assets_result.scalars().all())

            csaf_result = await session.execute(
                select(CsafProduct)
                .options(selectinload(CsafProduct.product))
                .where(CsafProduct.product.has())
                .order_by(CsafProduct.id)
                .limit(limit)
            )
            csafs = list(csaf_result.scalars().all())

        return assets, csafs
    finally:
        await cache_db.disconnect()


def build_pairs(assets, csafs):
    return list(itertools.product(csafs, assets))


def run_match_pairs_once(
    pairs,
    matching_config: dict,
    logging_config,
    threshold: float,
):
    manager = multiprocessing.Manager()
    matches_queue = manager.Queue()
    log_queue = manager.Queue()

    start = time.perf_counter()

    match_pairs(
        task_id=1,
        matches=matches_queue,
        log_queue=log_queue,
        logging_config=logging_config,
        pairs=pairs,
        threshold=threshold,
        matching_config=matching_config,
        matching_config_hash="benchhash",
    )

    duration = time.perf_counter() - start

    try:
        _, processed_pairs, matches = matches_queue.get(timeout=5)
    except Exception:
        processed_pairs, matches = [], []

    return {
        "duration_s": duration,
        "processed_pairs": len(processed_pairs),
        "matches_found": len(matches),
    }


def benchmark_match_pairs(
    pairs,
    matching_config: dict,
    logging_config,
    threshold: float,
    rounds: int,
):
    durations = []
    processed_pairs = 0
    matches_found = 0

    for _ in range(rounds):
        result = run_match_pairs_once(
            pairs=pairs,
            matching_config=matching_config,
            logging_config=logging_config,
            threshold=threshold,
        )
        durations.append(result["duration_s"])
        processed_pairs = result["processed_pairs"]
        matches_found = result["matches_found"]

    mean = statistics.mean(durations)
    median = statistics.median(durations)
    stddev = statistics.stdev(durations) if len(durations) > 1 else 0.0
    ops = 1.0 / mean if mean > 0 else 0.0

    return {
        "input_pairs": len(pairs),
        "processed_pairs": processed_pairs,
        "matches_found": matches_found,
        "min_s": min(durations),
        "max_s": max(durations),
        "mean_s": mean,
        "stddev_s": stddev,
        "median_s": median,
        "iqr_s": iqr(durations),
        "ops": ops,
        "rounds": rounds,
        "iterations": 1,
        "raw_durations": durations,
    }


def print_results_table(results: list[dict]):
    headers = [
        "Name",
        "Pairs",
        "Processed",
        "Matches",
        "Min (s)",
        "Max (s)",
        "Mean (s)",
        "StdDev (s)",
        "Median (s)",
        "IQR (s)",
        "OPS",
        "Rounds",
        "Iterations",
    ]

    rows = []
    for result in results:
        rows.append(
            [
                result["name"],
                str(result["input_pairs"]),
                str(result["processed_pairs"]),
                str(result["matches_found"]),
                f"{result['min_s']:.4f}",
                f"{result['max_s']:.4f}",
                f"{result['mean_s']:.4f}",
                f"{result['stddev_s']:.4f}",
                f"{result['median_s']:.4f}",
                f"{result['iqr_s']:.4f}",
                f"{result['ops']:.4f}",
                str(result["rounds"]),
                str(result["iterations"]),
            ]
        )

    widths = [len(h) for h in headers]
    for row in rows:
        for i, value in enumerate(row):
            widths[i] = max(widths[i], len(value))

    def fmt_row(values):
        return " | ".join(v.ljust(widths[i]) for i, v in enumerate(values))

    separator = "-+-".join("-" * w for w in widths)

    print()
    print(fmt_row(headers))
    print(separator)
    for row in rows:
        print(fmt_row(row))
    print()


def save_table_as_png(results: list[dict], output_path: Path):
    headers = [
        "Name",
        "Pairs",
        "Processed",
        "Matches",
        "Min (s)",
        "Max (s)",
        "Mean (s)",
        "StdDev (s)",
        "Median (s)",
        "IQR (s)",
        "OPS",
        "Rounds",
        "Iterations",
    ]

    rows = []
    for result in results:
        rows.append(
            [
                result["name"],
                str(result["input_pairs"]),
                str(result["processed_pairs"]),
                str(result["matches_found"]),
                f"{result['min_s']:.4f}",
                f"{result['max_s']:.4f}",
                f"{result['mean_s']:.4f}",
                f"{result['stddev_s']:.4f}",
                f"{result['median_s']:.4f}",
                f"{result['iqr_s']:.4f}",
                f"{result['ops']:.4f}",
                str(result["rounds"]),
                str(result["iterations"]),
            ]
        )

    fig_height = max(2.5, 0.7 * len(rows) + 1.5)
    fig, ax = plt.subplots(figsize=(18, fig_height))
    ax.axis("off")

    table = ax.table(
        cellText=rows,
        colLabels=headers,
        loc="center",
        cellLoc="center",
    )

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.6)

    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_text_props(weight="bold")

    plt.title("Matcher benchmark results", fontsize=14, pad=20)
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close()


def save_mean_plot_as_png(results: list[dict], output_path: Path):
    names = [result["name"] for result in results]
    means = [result["mean_s"] for result in results]

    plt.figure(figsize=(10, 6))
    plt.plot(names, means, marker="o")
    plt.xlabel("Benchmark case")
    plt.ylabel("Mean runtime (seconds)")
    plt.title("Matcher benchmark mean runtime")
    plt.grid(True)
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=200)
    plt.close()


def main():
    parser = argparse.ArgumentParser(
        description="Run match_pairs benchmarks and export table/plot as PNG."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("./assets/config.toml"),
        help="Path to config.toml",
    )
    parser.add_argument(
        "--limits",
        type=int,
        nargs="+",
        default=[10, 20, 30],
        help="Limits for assets and CSAFs, e.g. 10 20 30",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=50.0,
        help="Match threshold",
    )
    parser.add_argument(
        "--rounds",
        type=int,
        default=5,
        help="How many benchmark rounds to execute per case",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("./tests_benchmarks/reports_match_pairs_benchmark"),
        help="Directory for generated PNG files",
    )
    args = parser.parse_args()

    config = Config.load(args.config)

    with open(Path("./assets/plugin_configs/default/matching_config.toml"), "rb") as f:
        matching_config = tomllib.load(f)

    logging_config = config.Matcher.Logging

    all_results = []

    for limit in args.limits:
        assets, csafs = asyncio.run(load_assets_and_csafs(limit, config))
        pairs = build_pairs(assets, csafs)

        print(
            f"Starting benchmark for limit={limit}: "
            f"{len(assets)} assets, {len(csafs)} CSAFs, {len(pairs)} pairs"
        )

        result = benchmark_match_pairs(
            pairs=pairs,
            matching_config=matching_config,
            logging_config=logging_config,
            threshold=args.threshold,
            rounds=args.rounds,
        )

        result["name"] = f"pairs_{limit}"
        all_results.append(result)

        print(
            f"Finished {result['name']}: "
            f"mean={result['mean_s']:.4f}s, "
            f"min={result['min_s']:.4f}s, "
            f"max={result['max_s']:.4f}s"
        )

    print_results_table(all_results)

    table_png = args.output_dir / "benchmark_table.png"
    plot_png = args.output_dir / "benchmark_mean_runtime.png"

    save_table_as_png(all_results, table_png)
    save_mean_plot_as_png(all_results, plot_png)

    print(f"Benchmark table saved to: {table_png.resolve()}")
    print(f"Benchmark plot saved to: {plot_png.resolve()}")


if __name__ == "__main__":
    main()
