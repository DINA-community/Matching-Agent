#!/bin/bash

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
# shellcheck source=dev/scripts-install/utils.sh
source "${SCRIPT_DIR}/utils.sh"

main() {
	syt="$1"
	log="$2"
	info() { echo "[INFO] $*" >&2; }
	info "# Starting APIs"
	if [[ "$syt" == "remote" ]]; then
		exe_remote
	else
		exe_local
	fi
	info "--[API] finished."
}

exe_remote() {
	# Start the APIs. Stdout in one window
	info "The APIs will be called in this interface"
	uv run assetsync &
	echo "$!" >assetsync.pid
	sleep 2
	uv run csafsync &
	echo "$!" >csafsync.pid
	sleep 5
	uv run csaf_matcher &
	echo "$!" >matcher.pid
	sleep 5
}

exe_local() {

	OS="$(uname -s)"
	if [[ "$OS" != "Linux" ]]; then
		info "--[API] Unsupported OS: $OS"
		exit 1
	fi
	# Select terminal if not set
	if ! command -v "$TERMINAL" >/dev/null 2>&1; then
		set_terminal
	fi
	open_terminal "csafsync" "uv run csafsync"
	open_terminal "assetsync" "uv run assetsync"
	open_terminal "matcher" "uv run csaf_matcher"

}

main "$@"
