#!/usr/bin/bash
# Reloads the NetBox application, so a full container restart is not needed.
# Edits under dev/plugins/csaf or dev/plugins/d3c directly effective.
#
# Services `netbox-worker` and `netbox-housekeeping` are unaffected.
#
# Granian gracefully respawns its workers on SIGHUP
# The `tini --` entrypoint forwards all signals to Granian
set -euo pipefail

cd "$(dirname -- "${BASH_SOURCE[0]}")"

docker compose -f docker-compose.yml exec netbox kill -HUP 1
echo "Sent SIGHUP to NetBox (Granian) to reload all workers."
