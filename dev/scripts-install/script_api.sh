#!/bin/bash

SCRIPT_DIR="${BASH_SOURCE[0]}"
echo $SCRIPT_DIR
SCRIPT_DIR="$(dirname -- "${BASH_SOURCE[0]}")"
echo $SCRIPT_DIR
[[ -f $SCRIPT_DIR/"utils.sh" ]] || { echo "[ERROR] utils.sh not found (looked in $SCRIPT_DIR)" >&2; exit 127; }
# shellcheck source=dev/scripts-install/utils.sh
source "${SCRIPT_DIR}/utils.sh"


main() {
	local syt="${1:-terminal}"
	# close windows after command exits
	API_KEEP_OPEN=${API_KEEP_OPEN:-0} 
	info() { echo "[INFO] $*" >&2; }
	info "# Starting APIs"
	if [[ "$syt" == "terminal" ]]; then
		exe_single
	else
		exe_separate
	fi
	info "--[API] finished."
}

exe_single() {
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

exe_separate() {
	# Start the APIs in separate windows
	OS="$(uname -s)"
	if [[ "$OS" != "Linux" ]]; then
		info "--[API] Unsupported OS: $OS"
		exit 1
	fi
	open_terminal "csafsync" "uv run csafsync"
	open_terminal "assetsync" "uv run assetsync"
	open_terminal "matcher" "uv run csaf_matcher"

}

main "$@"
