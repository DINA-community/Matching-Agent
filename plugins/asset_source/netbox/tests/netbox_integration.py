"""Docker helpers shared by the NetBox integration tests."""

import subprocess
from pathlib import Path

import pytest

COMPOSE_FILE = Path(__file__).with_name("docker-compose.yml")
MANAGE = ["/opt/netbox/venv/bin/python", "/opt/netbox/netbox/manage.py"]


def docker(command: list[str], *, check: bool = True, timeout: int = 600) -> subprocess.CompletedProcess[str]:
    """Run a Docker CLI command."""
    try:
        result = subprocess.run(
            ["docker", *command],
            capture_output=True,
            check=False,
            text=True,
            timeout=timeout,
        )
    except FileNotFoundError:
        msg = "Docker CLI is unavailable"
        pytest.fail(msg, pytrace=False)
    except subprocess.TimeoutExpired:
        msg = f"Docker command timed out: docker {' '.join(command)}"
        pytest.fail(msg, pytrace=False)
    if check and result.returncode:
        msg = f"Docker command failed: docker {' '.join(command)}\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        pytest.fail(msg, pytrace=False)
    return result


def compose(
    project: str,
    command: list[str],
    *,
    check: bool = True,
    timeout: int = 600,
) -> subprocess.CompletedProcess[str]:
    """Run Docker Compose."""
    return docker(
        [
            "compose",
            "--project-name",
            project,
            "--file",
            str(COMPOSE_FILE),
            *command,
        ],
        check=check,
        timeout=timeout,
    )


def execute(project: str, service: str, command: list[str]) -> str:
    """Run a command in a Compose service and return its output."""
    return compose(project, ["exec", "-T", service, *command]).stdout


def setup_token(project: str) -> str:
    """Run the production token setup script and return its output."""
    return execute(project, "netbox", ["bash", "/opt/netbox/init-scripts/netbox-token.sh"])
