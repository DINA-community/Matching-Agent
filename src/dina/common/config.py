from __future__ import annotations
import tomllib
from pathlib import Path
from typing import Self

from pydantic import BaseModel, Field, model_validator

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
    sync_interval: int | None = None
    fixed_time_of_day: str | None = None  # Format: "HH:MM" in 24-hour format
    max_duration: int | None = None  # Maximum duration in seconds for a matching run
    match_threshold: float
    Api: ApiConfig
    asset_plugins_path: Path
    csaf_plugins_path: Path
    Logging: LoggingConfig | None = None

    @model_validator(mode="after")
    def validate_scheduling_config(self):
        """Ensure sync_interval and fixed_time_of_day are mutually exclusive."""
        if self.sync_interval is not None and self.fixed_time_of_day is not None:
            raise ValueError(
                "sync_interval and fixed_time_of_day are mutually exclusive"
            )
        if self.sync_interval is not None and self.fixed_time_of_day is not None:
            raise ValueError(
                "sync_interval and fixed_time_of_day are mutually exclusive"
            )

        # Validate time format if fixed_time_of_day is provided
        if self.fixed_time_of_day is not None:
            try:
                hours, minutes = self.fixed_time_of_day.split(":")
                h, m = int(hours), int(minutes)
                if not (0 <= h <= 23 and 0 <= m <= 59):
                    raise ValueError
            except (ValueError, AttributeError):
                raise ValueError(
                    f"fixed_time_of_day must be in HH:MM format (24-hour), got: {self.fixed_time_of_day}"
                )
        return self


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
