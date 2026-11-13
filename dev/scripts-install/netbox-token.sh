#!/bin/bash
set -e

echo "Setting up NetBox..."

/opt/netbox/venv/bin/python /opt/netbox/netbox/manage.py shell <<'PY'
import os
from pathlib import Path

from django.conf import settings
from django.contrib.auth import get_user_model
from users.choices import TokenVersionChoices
from users.models import Token

if not settings.API_TOKEN_PEPPERS:
    raise RuntimeError("Set API_TOKEN_PEPPER_1 before creating NetBox v2 tokens.")

User = get_user_model()
username = os.environ.get("NETBOX_SUPERUSER_NAME")

if not username:
    raise RuntimeError("Set NETBOX_SUPERUSER_NAME before creating a NetBox superuser.")

if not User.objects.filter(username=username).exists():
    user = User.objects.create_superuser(
        username,
        os.environ.get("NETBOX_SUPERUSER_EMAIL"),
        os.environ.get("DJANGO_SUPERUSER_PASSWORD"),
    )
    print("Superuser created.")
else:
    user = User.objects.get(username=username)
    print("Superuser already exists.")

if not user.is_active:
    raise RuntimeError("The NetBox setup user is inactive. Enable it before creating an API token.")

# Preserve the behavior from the v1 to return already created token.
# We write it, as we cannot read it back from the database.
# Not quite sure if really needed
path = Path("/tmp/netbox_token.txt")
credential = path.read_text().strip() if path.exists() else ""
key, separator, secret = credential.removeprefix("nbt_").partition(".")
token = Token.objects.filter(user=user, version=TokenVersionChoices.V2, key=key).first()
if credential.startswith("nbt_") and separator and token and token.is_active and token.write_enabled and token.validate(secret):
    print(f"API Token already exists: {credential}")
else:
    token = Token.objects.create(
        user=user,
        version=TokenVersionChoices.V2,
        write_enabled=True,
        description="Matching Agent development setup",
    )
    credential = f"nbt_{token.key}.{token.token}"
    # Dev environment: Otherwise restrict permissions for this file
    with open(path, "w") as output:
        output.write(credential)
    print(f"API Token created: {credential}")
PY

echo "NetBox setup complete!"
