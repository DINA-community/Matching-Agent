import pytest

from dina.common.config import (
    SynchronizerConfig,
    apply_updates,
    validate_update_keys,
    validate_update_prefixes,
)


def test_apply_updates_preserves_unrelated_settings() -> None:
    target = {
        "Synchronizer": {"sync_interval": 60, "cleanup_interval": 30},
        "Api": {"port": 8992},
    }

    result = apply_updates(target, {"Synchronizer.sync_interval": 120})

    assert result == {
        "Synchronizer": {"sync_interval": 120, "cleanup_interval": 30},
        "Api": {"port": 8992},
    }


def test_apply_updates_creates_missing_sections() -> None:
    target = {"Api": {"port": 8992}}

    result = apply_updates(target, {"Logging.level": "DEBUG"})

    assert result == {
        "Api": {"port": 8992},
        "Logging": {"level": "DEBUG"},
    }


def test_apply_updates_can_switch_scheduling_mode() -> None:
    target = {"Synchronizer": {"sync_interval": 60, "cleanup_interval": 30}}

    result = apply_updates(
        target,
        {
            "Synchronizer.sync_interval": None,
            "Synchronizer.fixed_time_of_day": "03:00",
        },
    )

    assert result == {"Synchronizer": {"cleanup_interval": 30, "fixed_time_of_day": "03:00"}}


def test_apply_updates_deleting_absent_key_preserves_existing_settings() -> None:
    target = {"Synchronizer": {"sync_interval": 60}}

    result = apply_updates(target, {"Synchronizer.fixed_time_of_day": None})

    assert result == {"Synchronizer": {"sync_interval": 60}}


@pytest.mark.parametrize(
    "key",
    ["Synchronizer.sync_interval", "Api.port", "Logging.file"],
)
def test_validate_update_keys_accepts_nested_settings(key: str) -> None:
    validate_update_keys(SynchronizerConfig, {key: None})


@pytest.mark.parametrize(
    "key",
    [
        "Synchronizer.sync_intervall",
        "Unknown.port",
        "Api.port.extra",
        "Synchronizer.preprocessor_plugins.name",
        "Logging.unknown",
    ],
)
def test_validate_update_keys_rejects_unknown_paths(key: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        validate_update_keys(SynchronizerConfig, {key: None})

    assert key in str(exc_info.value)


def test_validate_update_prefixes_accepts_allowed_sections() -> None:
    validate_update_prefixes(
        {"Assetsync.Synchronizer.sync_interval": 60, "Cachedb.port": 5432},
        {"Assetsync", "Cachedb"},
    )


@pytest.mark.parametrize("prefix", ["Csafsync", "AssetsyncExtra", "assetsync"])
def test_validate_update_prefixes_rejects_other_sections(prefix: str) -> None:
    key = f"{prefix}.Synchronizer.sync_interval"

    with pytest.raises(ValueError) as exc_info:
        validate_update_prefixes({"Assetsync.Synchronizer.sync_interval": 60, key: 120}, {"Assetsync"})

    assert key in str(exc_info.value)
