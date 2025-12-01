#!/usr/bin/env bash
set -euo pipefail

CERT_DIR=${CERT_DIR:-/etc/nginx/certs}
CN=${TLS_CN:-localhost}

mkdir -p "$CERT_DIR"

if [[ ! -f "$CERT_DIR/server.key" || ! -f "$CERT_DIR/server.crt" ]]; then
  echo "[nginx] Generating self-signed certificate for CN=$CN ..."
  openssl req -x509 -nodes -newkey rsa:4096 \
    -keyout "$CERT_DIR/server.key" \
    -out "$CERT_DIR/server.crt" \
    -subj "/CN=$CN" \
    -days 3650
  chmod 600 "$CERT_DIR/server.key"
fi

echo "[nginx] Starting nginx with TLS on :8443"
exec nginx -g 'daemon off;'
