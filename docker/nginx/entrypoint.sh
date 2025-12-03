#!/usr/bin/env bash
set -euo pipefail

CERT_DIR=${CERT_DIR:-/etc/nginx/certs}
CN=${TLS_CN:-localhost}
NGINX_CONF=${NGINX_CONF:-/etc/nginx/nginx.conf}
NGINX_CONF_RENDERED=${NGINX_CONF_RENDERED:-/etc/nginx/nginx.conf.rendered}
HTTPS_PORT=${HTTPS_PORT:-443}

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

# Render nginx configuration from template with environment variables
echo "[nginx] Rendering nginx config (HTTPS_PORT=${HTTPS_PORT})"
envsubst '${HTTPS_PORT}' < "$NGINX_CONF" > "$NGINX_CONF_RENDERED"

# Test configuration before starting
nginx -t -c "$NGINX_CONF_RENDERED"

echo "[nginx] Starting nginx with TLS on :${HTTPS_PORT}"
exec nginx -g 'daemon off;' -c "$NGINX_CONF_RENDERED"
