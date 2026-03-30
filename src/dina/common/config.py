from __future__ import annotations
import tomllib
from types import UnionType
from pathlib import Path
from typing import Any, Self, Union, get_args, get_origin

from pydantic import BaseModel, Field, model_validator
from pydantic_core import PydanticUndefined

from dina.cachedb.database import CacheDB
from dina.common.log import LoggingConfig


class Config(BaseModel):
    Cachedb: CacheDB.Config = Field(
        ..., description="Database connection settings for the cache database."
    )
    Assetsync: SynchronizerConfig = Field(
        ..., description="Configuration for the asset synchronizer service."
    )
    Csafsync: SynchronizerConfig = Field(
        ..., description="Configuration for the CSAF synchronizer service."
    )
    Matcher: MatcherConfig = Field(
        ..., description="Configuration for the matcher service."
    )

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


def _annotation_to_string(annotation: object) -> str:
    origin = get_origin(annotation)
    if origin is None:
        if annotation is Any:
            return "any"
        if annotation is Path:
            return "path"
        if isinstance(annotation, type):
            return annotation.__name__
        return str(annotation)

    args = get_args(annotation)
    if origin in (Union, UnionType):
        rendered = [_annotation_to_string(arg) for arg in args if arg is not type(None)]
        if len(rendered) != len(args):
            rendered.append("null")
        return " | ".join(rendered)
    if origin is list:
        inner = _annotation_to_string(args[0]) if args else "any"
        return f"list[{inner}]"
    if origin is dict:
        key_t = _annotation_to_string(args[0]) if args else "any"
        val_t = _annotation_to_string(args[1]) if len(args) > 1 else "any"
        return f"dict[{key_t}, {val_t}]"
    if origin is set:
        inner = _annotation_to_string(args[0]) if args else "any"
        return f"set[{inner}]"
    return str(annotation)


def build_config_parameter_info(
    model: type[BaseModel], prefix: str = ""
) -> dict[str, dict[str, object]]:
    """Build flattened metadata for all leaf configuration parameters."""
    model.model_rebuild(force=True)
    metadata: dict[str, dict[str, object]] = {}
    for name, field in model.model_fields.items():
        key = f"{prefix}.{name}" if prefix else name
        nested_model = _model_for_annotation(field.annotation)
        if nested_model is not None:
            metadata.update(build_config_parameter_info(nested_model, key))
            continue

        required = field.is_required()
        default: object | None
        if required:
            default = None
        elif field.default is not PydanticUndefined:
            default = field.default
        elif field.default_factory is not None:
            default = "<factory>"
        else:
            default = None

        metadata[key] = {
            "type": _annotation_to_string(field.annotation),
            "required": required,
            "default": default,
            "description": field.description,
        }
    return metadata


class MatcherConfig(BaseModel):
    sync_interval: int | None = Field(
        None,
        description="Run matching every N seconds; mutually exclusive with fixed_time_of_day.",
    )
    fixed_time_of_day: str | None = Field(
        None,
        description='Run matching once per day at "HH:MM" (24-hour format); mutually exclusive with sync_interval.',
    )
    max_duration: int | None = Field(
        None, description="Maximum allowed runtime (seconds) for one matching run."
    )
    match_threshold: float = Field(
        ..., description="Minimum score required for a match to be accepted."
    )
    Api: ApiConfig = Field(..., description="Matcher API server configuration.")
    asset_plugins_path: Path = Field(
        ..., description="Path to asset data source plugin configuration files."
    )
    csaf_plugins_path: Path = Field(
        ..., description="Path to CSAF data source plugin configuration files."
    )
    Logging: LoggingConfig | None = Field(
        None, description="Optional matcher-specific logging configuration."
    )

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
    freetext_fields_separator: str = Field(
        ...,
        description="Separator used to split free-text fields before tokenization.",
    )
    freetext_fields: dict[str, float] = Field(
        default_factory=dict,
        description="Mapping of free-text field names to field weights.",
    )
    ordered_fields: dict[str, float] = Field(
        default_factory=dict,
        description="Mapping of ordered-comparison field names to field weights.",
    )
    other_fields: dict[str, float] = Field(
        default_factory=dict,
        description="Mapping of exact/other field names to field weights.",
    )
    freetext_fields_weights: dict[str, float] = Field(
        default_factory=dict,
        description="Additional weighting rules for free-text scoring components.",
    )


class VersionConfig(BaseModel):
    weights: dict[str, float] = Field(
        default_factory=dict,
        description="Weights for version-comparison features used in matching.",
    )


class CpeConfig(BaseModel):
    csaf_cpe_field_name: str = Field(
        ..., description="Name of the CSAF field containing CPE data."
    )
    weights: dict[str, float] = Field(
        default_factory=dict,
        description="Weights for CPE-comparison features used in matching.",
    )


class PurlConfig(BaseModel):
    csaf_purl_field_name: str = Field(
        ..., description="Name of the CSAF field containing PURL data."
    )
    weights: dict[str, float] = Field(
        default_factory=dict,
        description="Weights for PURL-comparison features used in matching.",
    )


class NgramConfig(BaseModel):
    weights: dict[int, float] = Field(
        default_factory=dict, description="Per-ngram-size weights (e.g., 2, 3)."
    )


class LevenshteinConfig(BaseModel):
    max_distance: int = Field(
        ..., description="Maximum Levenshtein edit distance considered similar."
    )


class ThresholdConfig(BaseModel):
    vendor: int = Field(..., description="Threshold for vendor token matching.")
    product_family: int = Field(
        ..., description="Threshold for product family token matching."
    )
    product_name: int = Field(..., description="Threshold for product name matching.")
    keyword: int = Field(..., description="Threshold for keyword matching.")
    version: int = Field(..., description="Threshold for version matching.")


class MatchingConfig(BaseModel):
    database: DatabaseConfig = Field(
        ..., description="Settings for DB-backed field extraction and weighting."
    )
    version: VersionConfig = Field(
        ..., description="Version-comparison scoring configuration."
    )
    cpe: CpeConfig = Field(..., description="CPE-comparison configuration.")
    purl: PurlConfig = Field(..., description="PURL-comparison configuration.")
    ngram: NgramConfig = Field(..., description="N-gram similarity configuration.")
    levenshtein: LevenshteinConfig = Field(
        ..., description="Levenshtein similarity configuration."
    )
    threshold: ThresholdConfig = Field(
        ..., description="Thresholds used by the matching decision logic."
    )


class ApiConfig(BaseModel):
    host: str = Field(..., description="Host/interface the API server binds to.")
    port: int = Field(..., description="Port the API server listens on.")
    access_token_expire_minutes: int = Field(
        ..., description="JWT access token lifetime in minutes."
    )


class SynchronizerSectionConfig(BaseModel):
    sync_interval: int | None = Field(
        None,
        description="Run synchronization every N seconds; mutually exclusive with fixed_time_of_day.",
    )
    fixed_time_of_day: str | None = Field(
        None,
        description='Run synchronization once per day at "HH:MM" (24-hour format); mutually exclusive with sync_interval.',
    )
    preprocessor_plugins: list[str] = Field(
        ..., description="Ordered list of preprocessor plugin names to apply."
    )
    plugin_configs_path: Path = Field(
        ..., description="Path to datasource plugin TOML configuration files."
    )
    trigger_matcher_on_sync: bool = Field(
        True, description="Trigger matcher automatically after successful sync."
    )
    # Number of seconds before last_run to consider records stale for cleanup
    cleanup_grace_period: int = Field(
        ...,
        description="Grace period in seconds before stale records are eligible for cleanup.",
    )
    # The cleanup procedure is executed every cleanup_interval seconds
    cleanup_interval: int = Field(
        ..., description="Interval in seconds between cleanup runs."
    )

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
    Synchronizer: SynchronizerSectionConfig = Field(
        ..., description="Core synchronization behavior and scheduling settings."
    )
    Api: ApiConfig = Field(..., description="Synchronizer API server configuration.")
    Logging: LoggingConfig | None = Field(
        None, description="Optional synchronizer-specific logging configuration."
    )
