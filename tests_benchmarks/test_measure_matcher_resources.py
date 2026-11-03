import argparse
import asyncio
import itertools
import multiprocessing
import threading
import time
import tomllib
from pathlib import Path

import matplotlib.pyplot as plt
import psutil
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import selectinload

from dina.cachedb.database import CacheDB
from dina.cachedb.model import Asset, CsafProduct
from dina.common.config import Config
from dina.matcher.main import match_pairs


def parse_asset_csaf_pair(value: str) -> tuple[int, int]:
    try:
        asset_count_str, csaf_count_str = value.split(":")
        asset_count = int(asset_count_str)
        csaf_count = int(csaf_count_str)
        if asset_count <= 0 or csaf_count <= 0:
            raise ValueError
        return asset_count, csaf_count
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"Invalid format '{value}'. Expected e.g. 10:20 or 5:40"
        )


async def load_assets_and_csafs(
    asset_limit: int,
    csaf_limit: int,
    config: Config,
):
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
                .limit(asset_limit)
            )
            assets = list(assets_result.scalars().all())

            csaf_result = await session.execute(
                select(CsafProduct)
                .options(selectinload(CsafProduct.product))
                .where(CsafProduct.product.has())
                .order_by(CsafProduct.id)
                .limit(csaf_limit)
            )
            csafs = list(csaf_result.scalars().all())

        return assets, csafs
    finally:
        await cache_db.disconnect()


def build_pairs(assets, csafs):
    return list(itertools.product(csafs, assets))


def bytes_to_mb(value: int) -> float:
    return value / (1024 * 1024)


def measure_match_pairs(
    pairs,
    matching_config: dict,
    logging_config,
    threshold: float = 50.0,
    sample_interval: float = 0.2,
):
    process = psutil.Process()
    samples: list[dict] = []
    running = True

    process.cpu_percent(interval=None)

    def monitor():
        nonlocal running
        while running:
            try:
                samples.append(
                    {
                        "ts": time.perf_counter(),
                        "cpu_percent": process.cpu_percent(interval=None),
                        "rss": process.memory_info().rss,
                    }
                )
            except psutil.Error:
                pass
            time.sleep(sample_interval)

    monitor_thread = threading.Thread(target=monitor, daemon=True)
    monitor_thread.start()

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
        matching_config_hash="resource-measurement",
    )

    duration = time.perf_counter() - start

    running = False
    monitor_thread.join(timeout=1)

    try:
        task_id, processed_pairs, matches = matches_queue.get(timeout=5)
    except Exception:
        task_id, processed_pairs, matches = 1, [], []

    max_cpu = max((sample["cpu_percent"] for sample in samples), default=0.0)
    avg_cpu = (
        sum(sample["cpu_percent"] for sample in samples) / len(samples)
        if samples
        else 0.0
    )
    max_rss = max((sample["rss"] for sample in samples), default=0)
    avg_rss = sum(sample["rss"] for sample in samples) / len(samples) if samples else 0

    return {
        "task_id": task_id,
        "duration_s": duration,
        "input_pairs": len(pairs),
        "processed_pairs": len(processed_pairs),
        "matches_found": len(matches),
        "max_cpu_percent": max_cpu,
        "avg_cpu_percent": avg_cpu,
        "max_rss_mb": bytes_to_mb(max_rss),
        "avg_rss_mb": bytes_to_mb(avg_rss),
        "samples": samples,
    }


def print_results_table(results: list[dict]):
    headers = [
        "Assets",
        "CSAFs",
        "Pairs",
        "Processed",
        "Matches",
        "Duration (s)",
        "CPU max (%)",
        "CPU avg (%)",
        "RAM max (MB)",
        "RAM avg (MB)",
    ]

    rows = []
    for result in results:
        rows.append(
            [
                str(result["assets_count"]),
                str(result["csafs_count"]),
                str(result["input_pairs"]),
                str(result["processed_pairs"]),
                str(result["matches_found"]),
                f"{result['duration_s']:.4f}",
                f"{result['max_cpu_percent']:.2f}",
                f"{result['avg_cpu_percent']:.2f}",
                f"{result['max_rss_mb']:.2f}",
                f"{result['avg_rss_mb']:.2f}",
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


def generate_plots(results: list[dict], output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)

    labels = [f"{r['assets_count']}:{r['csafs_count']}" for r in results]
    pair_counts = [result["input_pairs"] for result in results]
    durations = [result["duration_s"] for result in results]
    cpu_avg = [result["avg_cpu_percent"] for result in results]
    cpu_max = [result["max_cpu_percent"] for result in results]
    ram_avg = [result["avg_rss_mb"] for result in results]
    ram_max = [result["max_rss_mb"] for result in results]
    matches = [result["matches_found"] for result in results]

    # Runtime
    plt.figure(figsize=(8, 5))
    plt.plot(pair_counts, durations, marker="o")
    for x, y, label in zip(pair_counts, durations, labels):
        plt.annotate(
            label, (x, y), textcoords="offset points", xytext=(0, 8), ha="center"
        )
    plt.xlabel("Number of pairs")
    plt.ylabel("Duration (seconds)")
    plt.title("Matcher runtime")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_dir / "matcher_duration.png", dpi=150)
    plt.close()

    # CPU
    plt.figure(figsize=(8, 5))
    plt.plot(pair_counts, cpu_avg, marker="o", label="CPU avg (%)")
    plt.plot(pair_counts, cpu_max, marker="o", label="CPU max (%)")
    for x, y, label in zip(pair_counts, cpu_avg, labels):
        plt.annotate(
            label, (x, y), textcoords="offset points", xytext=(0, 8), ha="center"
        )
    plt.xlabel("Number of pairs")
    plt.ylabel("CPU (%)")
    plt.title("Matcher CPU usage")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_dir / "matcher_cpu.png", dpi=150)
    plt.close()

    # RAM
    plt.figure(figsize=(8, 5))
    plt.plot(pair_counts, ram_avg, marker="o", label="RAM avg (MB)")
    plt.plot(pair_counts, ram_max, marker="o", label="RAM max (MB)")
    for x, y, label in zip(pair_counts, ram_avg, labels):
        plt.annotate(
            label, (x, y), textcoords="offset points", xytext=(0, 8), ha="center"
        )
    plt.xlabel("Number of pairs")
    plt.ylabel("RAM (MB)")
    plt.title("Matcher RAM usage")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_dir / "matcher_ram.png", dpi=150)
    plt.close()

    # Matches
    plt.figure(figsize=(8, 5))
    plt.plot(pair_counts, matches, marker="o")
    for x, y, label in zip(pair_counts, matches, labels):
        plt.annotate(
            label, (x, y), textcoords="offset points", xytext=(0, 8), ha="center"
        )
    plt.xlabel("Number of pairs")
    plt.ylabel("Matches found")
    plt.title("Matches found")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_dir / "matcher_matches.png", dpi=150)
    plt.close()


def main():
    parser = argparse.ArgumentParser(
        description="Resource measurement for match_pairs()"
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("./assets/config.toml"),
        help="Path to config.toml",
    )
    parser.add_argument(
        "--pairs",
        type=parse_asset_csaf_pair,
        nargs="+",
        default=[(10, 10), (20, 20), (30, 30)],
        help="Pairs in the format assets:csafs, e.g. 10:20 5:40 30:30",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=50.0,
        help="Match threshold",
    )
    parser.add_argument(
        "--sample-interval",
        type=float,
        default=0.2,
        help="Sampling interval for CPU/RAM in seconds",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("./tests_benchmarks/benchmark_plots"),
        help="Directory for generated plots",
    )
    args = parser.parse_args()

    config = Config.load(args.config)

    with open(Path("./assets/plugin_configs/default/matching_config.toml"), "rb") as f:
        matching_config = tomllib.load(f)

    logging_config = config.Matcher.Logging

    all_results = []

    for asset_limit, csaf_limit in args.pairs:
        assets, csafs = asyncio.run(
            load_assets_and_csafs(asset_limit, csaf_limit, config)
        )
        pairs = build_pairs(assets, csafs)

        print(
            f"Starting measurement for Assets={asset_limit}, CSAFs={csaf_limit}: "
            f"{len(assets)} assets, {len(csafs)} CSAFs, {len(pairs)} pairs"
        )

        result = measure_match_pairs(
            pairs=pairs,
            matching_config=matching_config,
            logging_config=logging_config,
            threshold=args.threshold,
            sample_interval=args.sample_interval,
        )

        result["assets_count"] = len(assets)
        result["csafs_count"] = len(csafs)

        all_results.append(result)

        print(
            f"Finished: duration={result['duration_s']:.4f}s, "
            f"matches={result['matches_found']}, "
            f"CPU max={result['max_cpu_percent']:.2f}%, "
            f"RAM max={result['max_rss_mb']:.2f} MB"
        )

    print_results_table(all_results)
    generate_plots(all_results, args.output_dir)

    print(f"Plots were saved to: {args.output_dir.resolve()}")


if __name__ == "__main__":
    main()
