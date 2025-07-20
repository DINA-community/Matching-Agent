#!/usr/bin/env bash
echo "Setting up Matching-Agent development tools"

docker compose -f dev/docker-compose.yml up -d
curl -LsSf https://astral.sh/uv/install.sh | sh

