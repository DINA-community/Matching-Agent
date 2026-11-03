from dina.common.config import Config, build_config_parameter_info


def test_build_config_parameter_info_contains_known_keys():
    info = build_config_parameter_info(Config)

    assert "Matcher.match_threshold" in info
    assert info["Matcher.match_threshold"]["type"] == "float"
    assert info["Matcher.match_threshold"]["required"] is True
    assert info["Matcher.match_threshold"]["description"] is not None

    assert "Assetsync.Synchronizer.sync_interval" in info
    assert "Cachedb.host" in info
    assert "Matcher.Logging.file" in info
