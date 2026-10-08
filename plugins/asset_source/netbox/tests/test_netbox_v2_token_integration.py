"""Integration test for NetBox v2 tokens."""

import pytest

from netbox_integration import MANAGE, execute, setup_token

pytestmark = [pytest.mark.integration]


def test_v2_token_setup_and_authentication(netbox: str) -> None:
    """Create and reuse a v2 token, then authenticate core and D3C requests."""
    first_setup = setup_token(netbox)
    assert "API Token created: nbt_" in first_setup

    repeated_setup = setup_token(netbox)
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
    execute(netbox, "netbox", MANAGE + ["shell", "-c", checks])
