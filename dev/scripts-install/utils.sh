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

  # 1) Use user-set TERMINAL.
  # Parameters for window title and command vary a lot between emulators,
  # so a few well-known ones get their native title flag; anything else
  # falls back to a best-effort guess.
  if has_terminal; then
    call_terminal
    return

  elif has_xdg_terminal; then
    # 2) generic way to launch the standard terminal
    info_api "xdg will be used. Starting API $title..."
    if command -v xdg-terminal-exec >/dev/null 2>&1; then
      xdg-terminal-exec bash -c '
          printf "\033]0;%s\007" "$1"
          eval "$2"
          exec bash
      ' bash "$title" "$cmd" &

      echo "$!" >"$title.pid"
      return
    fi
    # 3) the slightly older variant to launch the standard terminal, only
    #    accepts a single command string (run via the shell), not argv.
    if command -v xdg-terminal >/dev/null 2>&1; then
      xdg-terminal "$full_cmd" &
      echo "$!" >"$title.pid"
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
  case "$(basename -- "$TERMINAL")" in
    konsole)
      "$TERMINAL" -p tabtitle="$title" -e bash -c "$full_cmd" &
      ;;
    gnome-terminal)
      "$TERMINAL" --title="$title" -- bash -c "$full_cmd" &
      ;;
    xfce4-terminal)
      "$TERMINAL" --title="$title" -x bash -c "$full_cmd" &
      ;;
    *)
      # Guess the parameters in any other case
      "$TERMINAL" -e bash -c "$full_cmd" &
      ;;
  esac
  echo "$!" >"$title.pid"
}
