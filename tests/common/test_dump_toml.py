import math
import tomllib
from pathlib import Path

import pytest

from dina.common.config import dump_toml


@pytest.mark.parametrize(
    "value",
    [
        "",
        'Text with "quotes"',
        r"C:\config\settings.toml",
        'A "quoted" \\ path',
        "tab\there",
        "unicode: \u00e4\u00f6\u00fc \u65e5\u672c",
        # Fails: control characters are written raw into the basic string,
        # tomllib rejects the result with "Illegal character".
        # "line1\nline2",
        # "windows\r\nline",
        # "\b\f",
        # "nul\x00byte",
        # "del\x7fchar",
    ],
)
def test_dump_toml_preserves_strings(value: str) -> None:
    data = {"message": value}

    result = tomllib.loads(dump_toml(data))

    assert result == data


@pytest.mark.parametrize("values", [[], ["third", "first", "second"], [3, 1, 2]])
def test_dump_toml_preserves_list_values_and_order(values: list[object]) -> None:
    data = {"items": values}

    result = tomllib.loads(dump_toml(data))

    assert result == data


def test_dump_toml_preserves_nested_tables() -> None:
    data = {
        "service": {
            "api": {"host": "localhost", "port": 8080},
            "enabled": True,
            "logging": {"level": "INFO"},
        },
        "database": {"host": "localhost", "port": 5432},
    }

    result = tomllib.loads(dump_toml(data))

    assert result == data


def test_dump_toml_omits_none_values() -> None:
    data = {
        "optional": None,
        "service": {"enabled": True, "optional": None},
    }

    result = tomllib.loads(dump_toml(data))

    assert result == {"service": {"enabled": True}}


@pytest.mark.parametrize("enabled", [True, False])
def test_dump_toml_preserves_boolean_type(enabled: bool) -> None:
    result = tomllib.loads(dump_toml({"enabled": enabled}))

    assert result["enabled"] is enabled


@pytest.mark.parametrize(
    "key",
    [
        "plain",
        "with-dash",
        "with_underscore",
        "123",
        # Fails: keys are never quoted.
        # Written as `my key = 1`, tomllib: "Expected '=' after a key".
        # "my key",
        # Non-ASCII is not allowed in bare keys, tomllib: "Invalid statement".
        # "\u00e4",
        # Written as ` = 1`, tomllib: "Invalid statement".
        # "",
        # Written as `a.b = 1`, read back as dotted key {"a": {"b": 1}}.
        # "a.b",
    ],
)
def test_dump_toml_preserves_keys(key: str) -> None:
    data = {key: 1}

    result = tomllib.loads(dump_toml(data))

    assert result == data


# Fails: top-level scalars are written in dict order, so `x = 2` ends up
# below the `[table]` header and is read back as {"table": {"a": 1, "x": 2}}.
# def test_dump_toml_preserves_top_level_scalar_after_table() -> None:
#     data = {"table": {"a": 1}, "x": 2}
#
#     result = tomllib.loads(dump_toml(data))
#
#     assert result == data


@pytest.mark.parametrize("value", [0, -1, 2**62, 1.5, -0.25, 1e20, float("inf"), float("-inf")])
def test_dump_toml_preserves_numbers(value: float) -> None:
    result = tomllib.loads(dump_toml({"number": value}))

    assert result["number"] == value
    assert type(result["number"]) is type(value)


def test_dump_toml_preserves_nan() -> None:
    result = tomllib.loads(dump_toml({"number": float("nan")}))

    assert math.isnan(result["number"])


def test_dump_toml_writes_path_as_string() -> None:
    result = tomllib.loads(dump_toml({"path": Path("logs/matcher.log")}))

    assert result == {"path": "logs/matcher.log"}


def test_dump_toml_writes_int_keys_as_string_keys() -> None:
    result = tomllib.loads(dump_toml({"weights": {2: 0.5, 3: 0.25}}))

    assert result == {"weights": {"2": 0.5, "3": 0.25}}


@pytest.mark.parametrize("value", [[1, None], {1, 2}])
def test_dump_toml_rejects_values_without_toml_representation(value: object) -> None:
    with pytest.raises(ValueError, match="Unsupported TOML value type"):
        dump_toml({"value": value})


# Fails: TOML supports all of these, but _toml_format_value raises
# "Unsupported TOML value type" for datetime, date, time and tuple.
# @pytest.mark.parametrize(
#     ("value", "expected"),
#     [
#         (
#             datetime.datetime(2026, 1, 2, 3, 4, 5),
#             datetime.datetime(2026, 1, 2, 3, 4, 5),
#         ),
#         (datetime.date(2026, 1, 2), datetime.date(2026, 1, 2)),
#         (datetime.time(3, 4, 5), datetime.time(3, 4, 5)),
#         ((1, 2), [1, 2]),
#         ([{"a": 1}, {"a": 2}], [{"a": 1}, {"a": 2}]),
#     ],
# )
# def test_dump_toml_supports_native_toml_types(
#     value: object, expected: object
# ) -> None:
#     result = tomllib.loads(dump_toml({"value": value}))
#
#     assert result == {"value": expected}
