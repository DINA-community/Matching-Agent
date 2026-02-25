from __future__ import annotations
import tomllib
from pathlib import Path
from typing import Self, get_args, get_origin

from pydantic import BaseModel, Field, model_validator

from dina.cachedb.database import CacheDB
from dina.common.log import LoggingConfig


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


def apply_updates(target: dict, updates: dict[str, object]) -> dict:
    for key, value in updates.items():
        if not isinstance(key, str):
            raise ValueError("All update keys must be strings")
        parts = key.split(".")
        cursor = target
        for part in parts[:-1]:
            next_val = cursor.get(part)
            if not isinstance(next_val, dict):
                cursor[part] = {}
            cursor = cursor[part]
        if value is None:
            cursor.pop(parts[-1], None)
        else:
            cursor[parts[-1]] = value
    return target


def _model_for_annotation(annotation: object) -> type[BaseModel] | None:
    origin = get_origin(annotation)
    if origin is None:
        if isinstance(annotation, type) and issubclass(annotation, BaseModel):
            return annotation
        return None
    if origin is list or origin is dict or origin is set:
        return None
    for arg in get_args(annotation):
        if isinstance(arg, type) and issubclass(arg, BaseModel):
            return arg
    return None


def validate_update_keys(model: type[BaseModel], updates: dict[str, object]) -> None:
    invalid: list[str] = []
    for key in updates.keys():
        parts = key.split(".")
        current_model: type[BaseModel] | None = model
        for idx, part in enumerate(parts):
            if current_model is None:
                invalid.append(key)
                break
            fields = current_model.model_fields
            if part not in fields:
                invalid.append(key)
                break
            if idx == len(parts) - 1:
                break
            field = fields[part]
            current_model = _model_for_annotation(field.annotation)
    if invalid:
        invalid_list = ", ".join(sorted(set(invalid)))
        raise ValueError(f"Unsupported configuration key(s): {invalid_list}")


def validate_update_prefixes(
    updates: dict[str, object], allowed_prefixes: set[str]
) -> None:
    invalid: list[str] = []
    for key in updates.keys():
        prefix = key.split(".", 1)[0]
        if prefix not in allowed_prefixes:
            invalid.append(key)
    if invalid:
        invalid_list = ", ".join(sorted(set(invalid)))
        allowed = ", ".join(sorted(allowed_prefixes))
        raise ValueError(
            f"Unsupported configuration key(s): {invalid_list}. "
            f"Allowed prefixes: {allowed}"
        )


def _toml_format_value(value: object) -> str:
    if isinstance(value, Path):
        value = str(value)
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    if isinstance(value, list):
        return "[" + ", ".join(_toml_format_value(v) for v in value) + "]"
    raise ValueError(f"Unsupported TOML value type: {type(value)}")


def dump_toml(data: dict) -> str:
    lines: list[str] = []

    def write_table(prefix: str, table: dict) -> None:
        scalars: list[tuple[str, object]] = []
        nested: list[tuple[str, dict]] = []
        for key, val in table.items():
            if isinstance(val, dict):
                nested.append((key, val))
            elif val is None:
                continue
            else:
                scalars.append((key, val))
        for key, val in scalars:
            lines.append(f"{key} = {_toml_format_value(val)}")
        for key, val in nested:
            section = f"{prefix}.{key}" if prefix else key
            if lines and lines[-1] != "":
                lines.append("")
            lines.append(f"[{section}]")
            write_table(section, val)

    for key, val in data.items():
        if isinstance(val, dict):
            if lines and lines[-1] != "":
                lines.append("")
            lines.append(f"[{key}]")
            write_table(str(key), val)
        elif val is None:
            continue
        else:
            lines.append(f"{key} = {_toml_format_value(val)}")
    return "\n".join(lines) + "\n"


def write_toml_file(path: Path, data: dict) -> None:
    path.write_text(dump_toml(data), encoding="utf-8")


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


class ApiConfig(BaseModel):
    host: str
    port: int
    access_token_expire_minutes: int


class SynchronizerSectionConfig(BaseModel):
    sync_interval: int | None = None
    fixed_time_of_day: str | None = None  # Format: "HH:MM" in 24-hour format
    preprocessor_plugins: list[str]
    plugin_configs_path: Path
    trigger_matcher_on_sync: bool = True
    # Number of seconds before last_run to consider records stale for cleanup
    cleanup_grace_period: int
    # The cleanup procedure is executed every cleanup_interval seconds
    cleanup_interval: int

    @model_validator(mode="after")
    def validate_scheduling_config(self):
        """Ensure sync_interval and fixed_time_of_day are mutually exclusive."""
        if self.sync_interval is None and self.fixed_time_of_day is None:
            raise ValueError(
                "Either sync_interval or fixed_time_of_day must be specified"
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


class SynchronizerConfig(BaseModel):
    Synchronizer: SynchronizerSectionConfig
    Api: ApiConfig
    Logging: LoggingConfig | None = None
