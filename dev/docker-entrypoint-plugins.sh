#!/bin/bash
# Installs the NetBox plugins (CSAF and D3C) editable from the bind-mounts.

set -euo pipefail
source /opt/netbox/venv/bin/activate

echo "Installing NetBox plugins (editable) from mounted submodules..."
uv pip install -e /opt/netbox-plugins/d3c
# csaf must be installed with --no-deps so uv doesn't try to re-resolve d3c from PyPI
uv pip install -e /opt/netbox-plugins/csaf --no-deps

exec "$@"
