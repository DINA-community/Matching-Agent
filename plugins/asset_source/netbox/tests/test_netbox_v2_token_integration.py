"""Integration test for NetBox v2 tokens."""

import subprocess
import uuid
from contextlib import suppress
from pathlib import Path

import pytest

COMPOSE_FILE = Path(__file__).with_name("docker-compose.yml")

pytestmark = [pytest.mark.integration]


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


@pytest.fixture
def netbox(request: pytest.FixtureRequest) -> str:
    """Start NetBox with a fresh database."""
    docker_info = docker(["info"], check=False, timeout=30)
    if docker_info.returncode:
        msg = f"Docker is unavailable: {docker_info.stderr.strip()}"
        pytest.fail(msg, pytrace=False)

    project = f"matching-v2-{uuid.uuid4().hex[:8]}"

    def cleanup() -> None:
        with suppress(FileNotFoundError, subprocess.TimeoutExpired):
            subprocess.run(
                [
                    "docker",
                    "compose",
                    "--project-name",
                    project,
                    "--file",
                    str(COMPOSE_FILE),
                    "down",
                    "--volumes",
                    "--remove-orphans",
                    "--rmi",
                    "local",
                ],
                capture_output=True,
                check=False,
                text=True,
                timeout=60,
            )

    request.addfinalizer(cleanup)
    compose(project, ["up", "--detach", "--wait", "postgres", "redis", "netbox"])

    manage = ["/opt/netbox/venv/bin/python", "/opt/netbox/netbox/manage.py"]
    execute(
        project,
        "netbox",
        manage + ["shell", "-c", "from users.models import Token; assert not Token.objects.exists()"],
    )
    return project


def test_v2_token_setup_and_authentication(netbox: str) -> None:
    """Create and reuse a v2 token, then authenticate core and D3C requests."""
    setup = "/opt/netbox/init-scripts/netbox-token.sh"
    first_setup = execute(netbox, "netbox", ["bash", setup])
    assert "API Token created: nbt_" in first_setup

    repeated_setup = execute(netbox, "netbox", ["bash", setup])
    assert "API Token already exists: nbt_" in repeated_setup

    checks = """
from http.client import HTTPConnection
from pathlib import Path
from users.models import Token

credential = Path("/tmp/netbox_token.txt").read_text().strip()
connection = HTTPConnection("127.0.0.1", 8080, timeout=10)

try:
    for path in ["/api/dcim/devices/", "/api/plugins/d3c/software-list/"]:
        connection.request("GET", path, headers={"Authorization": f"Bearer {credential}"})
        response = connection.getresponse()
        content = response.read()
        assert response.status == 200, (path, response.status, content)
finally:
    connection.close()

assert Token.objects.count() == 1
token = Token.objects.get()
assert token.version == 2
assert token.plaintext is None
assert token.hmac_digest
assert token.validate(credential.split(".", 1)[1])
"""
    manage = ["/opt/netbox/venv/bin/python", "/opt/netbox/netbox/manage.py"]
    execute(netbox, "netbox", manage + ["shell", "-c", checks])
