#!/bin/bash
set -euo pipefail

cp -R /test-plugins/d3c /test-plugins/csaf /opt/netbox-plugins/
exec /opt/netbox/docker-entrypoint-plugins.sh /opt/netbox/docker-entrypoint.sh "$@"
