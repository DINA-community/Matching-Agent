#!/bin/bash

# Ensure script is run with appropriate permissions
if [[ $(id -u) -ne 0 ]]; then
    echo "This script must be run as root or with sudo." >&2
    exit 1
fi

# Verify OS compatibility
if [[ ! -f /etc/os-release ]]; then
    echo "Error: /etc/os-release not found. This script is designed for Debian/Ubuntu-based systems." >&2
    exit 1
fi

KEYRING="/etc/apt/keyrings/docker.asc"
SOURCES="/etc/apt/sources.list.d/docker.sources"
GPG_URL="https://download.docker.com/linux/ubuntu/gpg"

echo "[DOCKER] Installing Docker repository..."

# Download GPG key with proper permissions
curl -fsSL "$GPG_URL" -o "$KEYRING" || {
    echo "Error: Failed to download Docker GPG key" >&2
    exit 1
}

chmod a+r "$KEYRING" || {
    echo "Error: Failed to set keyring permissions" >&2
    exit 1
}

# Add the repository to Apt sources
cat > "$SOURCES" <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: $KEYRING
EOF

echo "[DOCKER] Docker repository added successfully."
echo "[DOCKER] Run 'apt-get update' to use the new repository."