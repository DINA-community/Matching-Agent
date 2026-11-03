"""Isolated Docker infrastructure for NetBox integration tests."""

import uuid
from collections.abc import Iterator

import httpx
import pytest
from netbox_integration import MANAGE, compose, docker, execute, setup_token


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


@pytest.fixture
def netbox_client(netbox: str) -> Iterator[httpx.Client]:
    """Authenticate HTTP requests to the disposable NetBox with a real v2 token."""
    setup_token(netbox)
    token = execute(netbox, "netbox", ["cat", "/tmp/netbox_token.txt"]).strip()
    address = compose(netbox, ["port", "netbox", "8080"]).stdout.strip()
    with httpx.Client(
        base_url=f"http://{address}",
        headers={"Authorization": f"Bearer {token}"},
        timeout=30,
    ) as client:
        yield client
