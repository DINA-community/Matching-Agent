import asyncio
import itertools
import tomllib
from pathlib import Path

import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import selectinload

from dina.cachedb.database import CacheDB
from dina.cachedb.model import Asset, CsafProduct
from dina.common.config import Config


@pytest.fixture(scope="session")
def config():
    return Config.load(Path("./assets/config.toml"))


@pytest.fixture(scope="session")
def matching_config():
    with open(Path("./assets/plugin_configs/default/matching_config.toml"), "rb") as f:
        return tomllib.load(f)


@pytest.fixture(scope="session")
def logging_config(config):
    return config.Matcher.Logging


async def _load_assets_and_csafs(limit: int, config: Config):
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

        print(
            f"Geladen für Limit {limit}: "
            f"{len(assets)} Assets, {len(csafs)} CSAFs, {len(assets) * len(csafs)} Paare"
        )

        return assets, csafs
    finally:
        await cache_db.disconnect()


def _build_pairs(assets, csafs):
    return list(itertools.product(csafs, assets))


@pytest.fixture(scope="session")
def pairs_10(config):
    assets, csafs = asyncio.run(_load_assets_and_csafs(10, config))
    return _build_pairs(assets, csafs)


@pytest.fixture(scope="session")
def pairs_20(config):
    assets, csafs = asyncio.run(_load_assets_and_csafs(20, config))
    return _build_pairs(assets, csafs)


@pytest.fixture(scope="session")
def pairs_30(config):
    assets, csafs = asyncio.run(_load_assets_and_csafs(30, config))
    return _build_pairs(assets, csafs)
