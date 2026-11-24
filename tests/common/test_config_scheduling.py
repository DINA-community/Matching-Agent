import pytest
from pydantic import ValidationError

from dina.common.config import MatcherConfig, SynchronizerSectionConfig


@pytest.fixture(params=[MatcherConfig, SynchronizerSectionConfig])
def scheduling_config(
    request: pytest.FixtureRequest,
):
    if request.param is MatcherConfig:
        return MatcherConfig, {
            "match_threshold": 0,
            "Api": {
                "host": "127.0.0.1",
                "port": 8998,
                "access_token_expire_minutes": 30,
            },
            "asset_plugins_path": "assets",
            "csaf_plugins_path": "csaf",
        }
    return SynchronizerSectionConfig, {
        "preprocessor_plugins": ["identity"],
        "plugin_configs_path": "plugins",
        "cleanup_grace_period": 60,
        "cleanup_interval": 30,
    }


def test_scheduling_accepts_interval(scheduling_config) -> None:
    model, data = scheduling_config

    config = model.model_validate({**data, "sync_interval": 60})

    assert config.model_dump()["sync_interval"] == 60
    assert config.model_dump()["fixed_time_of_day"] is None


@pytest.mark.parametrize("time_of_day", ["00:00", "03:00", "23:59"])
def test_scheduling_accepts_fixed_time(scheduling_config, time_of_day: str) -> None:
    model, data = scheduling_config

    config = model.model_validate({**data, "fixed_time_of_day": time_of_day})

    assert config.model_dump()["fixed_time_of_day"] == time_of_day
    assert config.model_dump()["sync_interval"] is None


def test_scheduling_rejects_interval_and_fixed_time_together(scheduling_config) -> None:
    model, data = scheduling_config

    with pytest.raises(ValidationError) as exc_info:
        model.model_validate({
            **data,
            "sync_interval": 60,
            "fixed_time_of_day": "03:00",
        })

    assert "mutually exclusive" in str(exc_info.value)


@pytest.mark.parametrize(
    "time_of_day",
    ["24:00", "12:60", "-1:00", "12:-1", "abc", "12", "12:00:00", ""],
)
def test_scheduling_rejects_invalid_fixed_time(scheduling_config, time_of_day: str) -> None:
    model, data = scheduling_config

    with pytest.raises(ValidationError) as exc_info:
        model.model_validate({**data, "fixed_time_of_day": time_of_day})

    assert "fixed_time_of_day must be in HH:MM format" in str(exc_info.value)


def test_scheduling_requirement_depends_on_service(scheduling_config) -> None:
    model, data = scheduling_config

    if model is MatcherConfig:
        config = model.model_validate(data)
        assert config.sync_interval is None
        assert config.fixed_time_of_day is None
    else:
        with pytest.raises(ValidationError) as exc_info:
            model.model_validate(data)
        assert "Either sync_interval or fixed_time_of_day must be specified" in str(exc_info.value)
