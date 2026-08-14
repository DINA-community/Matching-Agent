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
#
# This only works with commands that do not use double quotes
#
#   open_terminal "<title>" "<command>"
open_terminal() {
  local title="$1"
  local cmd="$2"
  local full_cmd="$cmd; exec bash"

  # 1) Use user-set TERMINAL.
  # Parameters for window title and command vary a lot between emulators,
  # so a few well-known ones get their native title flag; anything else
  # falls back to a best-effort guess.
  if [[ -n "${TERMINAL:-}" ]] && command -v "$TERMINAL" >/dev/null 2>&1; then
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
    return
  fi

  # 2) generic way to launch the standard terminal
  if command -v xdg-terminal-exec >/dev/null 2>&1; then
    xdg-terminal-exec --title="$title" bash -c "$full_cmd" &
    echo "$!" >"$title.pid"
    return
  fi

  # 3) the slighly older variant to launch the standard terminal, only
  #    accepts a single command string (run via the shell), not argv.
  if command -v xdg-terminal >/dev/null 2>&1; then
    xdg-terminal "$full_cmd" &
    echo "$!" >"$title.pid"
    return
  fi

  echo "No terminal found (set \$TERMINAL, or install xdg-terminal-exec/xdg-terminal and configure a default terminal)." >&2
  exit 1
}

set_terminal() {
  # Choose from x-terminal-emulator list. Otherwise xdg-terminal-exec will be used (if installed)
  mapfile -t terminals < <(update-alternatives --list x-terminal-emulator)

  if ((${#terminals[@]} == 0)); then
      echo "No terminal emulators found." >&2
      exit 1
  fi

  terminals+=("None / Cancel")

  echo "Choose the default terminal emulator:"
  select terminal in "${terminals[@]}"; do
      if [[ "$terminal" == "None / Cancel" ]]; then
          echo "No terminal emulator selected."
          exit 0
      elif [[ -n "$terminal" ]]; then
          echo "Default terminal set to: $terminal" >&2         
          export TERMINAL="$terminal"
          break
      else
          echo "Invalid selection. Please try again."
      fi
  done
}
