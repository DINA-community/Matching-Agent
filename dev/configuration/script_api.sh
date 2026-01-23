#!/usr/bin/env bash
set -e

# Detect OS / Desktop Environment
OS="$(uname -s)"
TERM_CMD=""

if [[ "$OS" == "Linux" ]]; then
  if command -v konsole >/dev/null 2>&1; then
    TERM_CMD="konsole"
  elif command -v gnome-terminal >/dev/null 2>&1; then
    TERM_CMD="gnome-terminal"
  else
    echo "No supported terminal found (konsole or gnome-terminal)."
    exit 1
  fi
else
  echo "Unsupported OS: $OS"
  exit 1
fi

# Functions to open terminals
open_konsole() {
  local title="$1"
  local cmd="$2"
  konsole -p tabtitle="$title" -e bash -c "$cmd; exec bash" &
}

open_gnome_terminal() {
  local title="$1"
  local cmd="$2"
  gnome-terminal --title="$title" -- bash -c "$cmd; exec bash" &
}

# Run the commands based on terminal
if [[ "$TERM_CMD" == "konsole" ]]; then
  open_konsole "csafsync" "uv run csafsync"
  open_konsole "assetsync" "uv run assetsync"
  open_konsole "matcher" "uv run csaf_matcher"
else
  open_gnome_terminal "csafsync" "uv run csafsync"
  open_gnome_terminal "assetsync" "uv run assetsync"
  open_gnome_terminal "matcher" "uv run csaf_matcher"
fi
