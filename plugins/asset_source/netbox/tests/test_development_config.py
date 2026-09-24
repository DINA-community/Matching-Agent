import runpy
from pathlib import Path
from unittest.mock import patch

import pytest

ROOT = Path(__file__).resolve().parents[4]


@pytest.mark.parametrize(
    "path",
    [
        "dev/configuration/configuration.py",
        "dev/plugins/d3c/docker-ci/configuration/configuration.py",
    ],
)
def test_pepper_configuration(monkeypatch: pytest.MonkeyPatch, path: str) -> None:
    config = ROOT / path
    if not config.is_file():
        pytest.skip()

    monkeypatch.setenv("API_TOKEN_PEPPER_1", "environment-pepper")
    with patch("builtins.open", side_effect=FileNotFoundError):  # force return of default/env value
        settings = runpy.run_path(str(config))

    assert settings["API_TOKEN_PEPPERS"] == {1: "environment-pepper"}


@pytest.mark.parametrize(
    "path",
    [
        "dev/configuration/.env.example",
        "dev/plugins/d3c/docker-ci/env/netbox.env",
    ],
)
def test_checked_in_development_peppers_are_valid(path: str) -> None:
    """Checks the development defaults."""
    config = ROOT / path
    if not config.is_file():
        pytest.skip()

    pepper = next(line.split("=", 1)[1] for line in config.read_text().splitlines() if line.startswith("API_TOKEN_PEPPER_1="))

    assert len(pepper) >= 50
