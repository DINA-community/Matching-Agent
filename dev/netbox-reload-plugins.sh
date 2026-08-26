#!/usr/bin/bash
# Reloads the NetBox application, so a full container restart is not needed.
# Edits under dev/plugins/csaf or dev/plugins/d3c directly effective.
#
# Services `netbox-worker` and `netbox-housekeeping` are unaffected.
set -euo pipefail

cd "$(dirname -- "${BASH_SOURCE[0]}")"

docker compose -f docker-compose.yml exec netbox \
  curl -fs --unix-socket /opt/unit/unit.sock \
  http://localhost/control/applications/netbox/restart
echo
