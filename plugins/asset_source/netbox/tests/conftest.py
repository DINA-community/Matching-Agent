"""Isolated Docker infrastructure for NetBox integration tests."""

import uuid

import pytest
from netbox_integration import MANAGE, compose, docker, execute


@pytest.fixture
def netbox(request: pytest.FixtureRequest) -> str:
    """Start NetBox with a fresh database."""
    docker_info = docker(["info"], check=False, timeout=30)
    if docker_info.returncode:
        msg = f"Docker is unavailable: {docker_info.stderr.strip()}"
        pytest.fail(msg, pytrace=False)

    project = f"matching-netbox-{uuid.uuid4().hex[:8]}"

    def cleanup() -> None:
        compose(project, ["down", "--volumes", "--remove-orphans", "--rmi", "local"], timeout=60)

    request.addfinalizer(cleanup)
    try:
        compose(project, ["up", "--detach", "--wait", "postgres", "redis", "netbox"])
    except pytest.fail.Exception:
        logs = compose(project, ["logs", "--no-color", "--tail", "100"], check=False)
        print(logs.stdout)
        raise

    execute(
        project,
        "netbox",
        MANAGE + ["shell", "-c", "from users.models import Token; assert not Token.objects.exists()"],
    )
    return project
