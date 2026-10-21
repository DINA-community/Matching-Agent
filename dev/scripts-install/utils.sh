#!/usr/bin/bash
# SPDX-FileCopyrightText: 2026 German Federal Office for Information Security (BSI) <https://www.bsi.bund.de>
# Software-Engineering: 2026 Intevation GmbH <https://intevation.de>
#
# SPDX-License-Identifier: Apache-2.0

# Shared shell scripting helpers

# Open a terminal window and start a command, setting the window/tab title
# where the terminal supports it, and recording the launched process's PID
# to "<title>.pid" in the current directory.
#
# Prefers the user's configured terminal ($TERMINAL), then the newer
# xdg-terminal-exec, then the older xdg-terminal.

info_api() { echo "[API]  $*" >&2; }

TERMINAL_PAYLOAD='
  printf "\033]0;%s\007" "$1"
  export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"
  if ! cd -- "$3"; then
    printf "[API] cannot change into %s\n" "$3" >&2
    exit 1
  fi
  # Run the command as its own job: sh execs a simple command, so the job PID
  # is the PID of "uv run ..." - the process stop_apis() sends SIGTERM to.
  # Job control stays off (plain bash -c), so Ctrl+C in the window reaches the
  # command and a prompt stays available afterwards.
  sh -c "$2" &
  cmd_pid=$!
  printf "%s\n" "$cmd_pid" > "$4"
  wait "$cmd_pid"; status=$?
  printf "\n[API] %s exited with status %s\n" "$1" "$status"
  case "$5" in
    0) exit "$status" ;;
    2) if (( status == 0 )); then exit 0; fi; exec bash ;;
    *) exec bash ;;
  fi
'

# argv handed to every emulator: bash -c <payload> <arg0> <title> <cmd> <dir> <pid>
build_payload() {
  local keep="${API_KEEP_OPEN:-1}}"
  payload=(bash -c "$TERMINAL_PAYLOAD" bash "$title" "$cmd" "$workdir" "$pidfile" "$keep")
}

# Report a broken launch here instead of leaving stop_apis() without a PID file.
wait_for_pidfile() {
  local tries=40
  while (( tries-- > 0 )); do
    [[ -s "$pidfile" ]] && return 0
    sleep 0.25
  done
  info_api "no PID file in $pidfile - terminal or command failed to start"
  return 1
}

has_xdg_terminal() {
    command -v xdg-terminal-exec >/dev/null 2>&1 || command -v xdg-terminal >/dev/null 2>&1
}

has_terminal() {
    [[ -n "${TERMINAL:-}" ]] && command -v "$TERMINAL" >/dev/null 2>&1
}

open_terminal() {
  title="$1"
  cmd="$2"
  full_cmd="$cmd; exec bash"
  workdir="$PWD"                          # captured NOW, in the script's cwd
  pidfile="$workdir/$title.pid"           # absolute: the window's cwd is elsewhere
  if [[ -z "${title//[[:space:]]/}" ]]; then
    info_api "open_terminal: empty title, refusing to start"
    return 1
  fi
  build_payload
  # 1) Use user-set TERMINAL.
  # Parameters for window title and command vary a lot between emulators,
  # so a few well-known ones get their native title flag; anything else
  # falls back to a best-effort guess.
  if has_terminal; then
    call_terminal
    return

  elif has_xdg_terminal; then
    # 2) generic way to launch the standard terminal
    if command -v xdg-terminal-exec >/dev/null 2>&1; then
      info_api "xdg-terminal-exec will be used. Starting API $title..."
      # GTK/libadwaita portal warnings go to the emulator's stderr
      xdg-terminal-exec -- "${payload[@]}" 2>/dev/null &
      wait $! 2>/dev/null \
        || info_api "xdg-terminal-exec failed - set \$TERMINAL to your emulator"
      wait_for_pidfile
      return
    fi
    # 3) the slightly older variant to launch the standard terminal, only
    #    accepts a single command string (run via the shell), not argv.
    if command -v xdg-terminal >/dev/null 2>&1; then
      echo "--[WARNING] deprecated" >&2;
      info_api "  xdg-terminal will be used. Starting API $title..."
      xdg-terminal "$full_cmd" &
      wait_for_pidfile
      return
    fi
  else
    if command -v update-alternatives >/dev/null 2>&1; then
      mapfile -t terminals < <(update-alternatives --list x-terminal-emulator)
      terminals+=("None")
      echo "Choose a terminal emulator:"
      select terminal in "${terminals[@]}"; do
        if [[ "$terminal" == "None" ]]; then
          break
        elif [[ -n "$terminal" ]]; then
          echo "Default terminal set to: $terminal" >&2
          terminal_name="$(basename -- "$terminal")"
          terminal_name="${terminal_name%.*}"
          export TERMINAL="$terminal_name"
          call_terminal
          return
        fi
        echo "Invalid selection. Please try again." >&2
      done
    else
      info_api "No terminal found with update-alternatives (set \$TERMINAL for manual override)." >&2
    fi
  info_api "No terminal found (set \$TERMINAL, or install xdg-terminal-exec/xdg-terminal and configure a default terminal)." >&2
  exit 1
  fi
}


call_terminal() {
  info_api "$TERMINAL will be used."
  [[ -n "${payload[*]:-}" ]] || build_payload
  case "$(basename -- "$TERMINAL")" in
    konsole)
      "$TERMINAL" -p tabtitle="$title" -e "${payload[@]}" &
      ;;
    gnome-terminal|org.gnome.Terminal|ptyxis|org.gnome.Ptyxis|app.org.Ptyxis)
      # gnome-terminal style clients reject -e: title flag, payload after "--"
      "$TERMINAL" --title="$title" -- "${payload[@]}" &
      ;;
    xfce4-terminal)
      "$TERMINAL" --title="$title" -x "${payload[@]}" &
      ;;
    xterm)
      "$TERMINAL" -T "$title" -e "${payload[@]}" &
      ;;
    *)
      # Guess the parameters in any other case
      "$TERMINAL" -e "${payload[@]}" &
      ;;
  esac
  wait_for_pidfile
}
