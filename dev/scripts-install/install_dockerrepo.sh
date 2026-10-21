#!/bin/bash

KEYRING="/etc/apt/keyrings/docker.asc"
SOURCES="/etc/apt/sources.list.d/docker.sources"
GPG_URL="https://download.docker.com/linux/ubuntu/gpg"

# Verify OS compatibility
if [[ ! -f /etc/os-release ]]; then
    echo "Error: /etc/os-release not found. This script is designed for Debian/Ubuntu-based systems." >&2
    exit 1
fi


echo "[DOCKER] Installing Docker repository..."

DISTRO="$(. /etc/os-release && echo "${ID:-}")"
CODENAME=$(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")

case "$DISTRO" in
  ubuntu) REPO="ubuntu" ;;
  debian) REPO="debian" ;;
  *)      REPO="ubuntu"                           # Linux Mint, Pop!_OS, ... fall back to Ubuntu
            [[ -n "$CODENAME" ]] || { echo "Error: cannot detect codename; set it manually." >&2; exit 1; } ;;
esac

BASE_URL="https://download.docker.com/linux/${REPO}"
echo "[DOCKER] distro=$DISTRO codename=${CODENAME:-?} repo=$REPO"
echo "$BASE_URL"



# Download GPG key with proper permissions
sudo curl -fsSL "$BASE_URL/gpg" -o "$KEYRING" || {
    echo "Error: Failed to download Docker GPG key" >&2
    exit 1
}

sudo chmod a+r "$KEYRING" || {
    echo "Error: Failed to set keyring permissions" >&2
    exit 1
}

# Add the repository to Apt sources

TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT

cat > "$TMP" <<EOF
Types: deb
URIs: $BASE_URL
Suites: $CODENAME
Components: stable
Signed-By: $KEYRING
EOF

sudo install -m 0644 -o root -g root "$TMP" "$SOURCES"

echo "[DOCKER] Docker repository added successfully."
echo "[DOCKER] Run 'apt-get update' to use the new repository."
