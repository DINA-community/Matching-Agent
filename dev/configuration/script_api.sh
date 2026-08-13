#!/usr/bin/bash
set -e

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
# shellcheck source=../utils.sh
source "$SCRIPT_DIR/../utils.sh"

OS="$(uname -s)"
if [[ "$OS" != "Linux" ]]; then
  echo "Unsupported OS: $OS" >&2
  exit 1
fi

open_terminal "csafsync" "uv run csafsync"
open_terminal "assetsync" "uv run assetsync"
open_terminal "matcher" "uv run csaf_matcher"
