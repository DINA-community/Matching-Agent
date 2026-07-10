#!/usr/bin/env bash

main() {
	syt=$1
	log=$2
	info() { echo "[INFO] $*" >&2; }

	info "# Starting APIs"
	if [[ $syt == "remote" ]]; then
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
	TERM_CMD=""

	if [[ "$OS" == "Linux" ]]; then
		if command -v konsole >/dev/null 2>&1; then
			TERM_CMD="konsole"
		elif command -v gnome-terminal >/dev/null 2>&1; then
			TERM_CMD="gnome-terminal"
		else
			info "--[API] No supported terminal found (konsole or gnome-terminal)."
			exit 1
		fi
	else
		info "--[API] Unsupported OS: $OS"
		exit 1
	fi

	# Functions to open terminals
	open_konsole() {
		local title="$1"
		local cmd="$2"
		konsole -p tabtitle="$title" -e bash -c "$cmd; exec bash" &
		echo "$!" >"$title.pid"
	}

	open_gnome_terminal() {
		local title="$1"
		local cmd="$2"
		gnome-terminal --title="$title" -- bash -c "$cmd; exec bash" &
		echo "$!" >"$title.pid"
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

}

main "$@"
