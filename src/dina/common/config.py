from __future__ import annotations
import tomllib
from pathlib import Path
from typing import Self

from pydantic import BaseModel, Field

from dina.cachedb.database import CacheDB
from dina.common.log import LoggingConfig
from dina.synchronizer.base import SynchronizerConfig


class Config(BaseModel):
    Cachedb: CacheDB.Config
    Assetsync: SynchronizerConfig
    Csafsync: SynchronizerConfig
    Matcher: MatcherConfig

    @classmethod
    def load(cls, config_file: Path) -> Self:
        if not config_file.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_file}")

        with open(config_file, "rb") as f:
            return cls.model_validate(tomllib.load(f))


class ApiConfig(BaseModel):
    host: str
    port: int
    access_token_expire_minutes: int


class MatcherConfig(BaseModel):
    sync_interval: int
    match_threshold: float
    Api: ApiConfig
    asset_plugins_path: Path
    csaf_plugins_path: Path
    Logging: LoggingConfig | None = None


class DatabaseConfig(BaseModel):
    freetext_fields_separator: str
    freetext_fields: dict[str, float] = Field(default_factory=dict)
    ordered_fields: dict[str, float] = Field(default_factory=dict)
    other_fields: dict[str, float] = Field(default_factory=dict)
    freetext_fields_weights: dict[str, float] = Field(default_factory=dict)


class VersionConfig(BaseModel):
    weights: dict[str, float] = Field(default_factory=dict)


class CpeConfig(BaseModel):
    csaf_cpe_field_name: str
    weights: dict[str, float] = Field(default_factory=dict)


class PurlConfig(BaseModel):
    csaf_purl_field_name: str
    weights: dict[str, float] = Field(default_factory=dict)


class NgramConfig(BaseModel):
    weights: dict[int, float] = Field(default_factory=dict)


class LevenshteinConfig(BaseModel):
    max_distance: int


class ThresholdConfig(BaseModel):
    vendor: int
    product_family: int
    product_name: int
    keyword: int
    version: int


class MatchingConfig(BaseModel):
    database: DatabaseConfig
    version: VersionConfig
    cpe: CpeConfig
    purl: PurlConfig
    ngram: NgramConfig
    levenshtein: LevenshteinConfig
    threshold: ThresholdConfig
