#!/usr/bin/env bash

# Starts the local development environment defined in dev/docker-compose.yml
#
# Usage:
#   ./dev/start-local-env.sh                         # start services in background
#   ./dev/start-local-env.sh --recreate              # recreate containers
#   ./dev/start-local-env.sh --stop                  # stop
#   ./dev/start-local-env.sh --down                  # stop and remove services
#   ./dev/start-local-env.sh --down --volumes        # stop, remove services AND named volumes
#   ./dev/start-local-env.sh --recreate --volumes    # full reset: down -v, then up (fresh volumes)
#
# Notes:
# - Requires Docker and Docker Compose (v2: `docker compose`).
# - After startup, retrieve the NetBox API token with:
#     docker compose -f dev/docker-compose.yml logs netbox-setup

set -euo pipefail

COMPOSE_FILE="dev/docker-compose.yml"
ENV_FILE="dev/.env"
ENV_SAMPLE="dev/configuration/.env.example" 
NETBOX_URL="NETBOX_CLIENT_HOSTNAME_URL"
ISDUBA_SAMPLE="assets/plugin_configs/data_source/csaf/sample/isduba.toml"
NETBOX_SAMPLE="assets/plugin_configs/data_source/asset/sample/netbox.toml"
NETBOX_FILE="assets/plugin_configs/data_source/asset/netbox-local.toml"
ISDUBA_FILE="assets/plugin_configs/data_source/csaf/isduba-local.toml"
LOCAL_SETTING="FULLY_LOCAL"

error() { echo "[ERROR] $*" >&2; }
info()  { echo "[INFO]  $*"; }

need_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    error "Required command '$1' not found in PATH"; exit 127
  fi
}

need_env() {
  # Checks if .env exists and use example instead if user approves
  ENV_FILE="dev/.env"
  ENV_SAMPLE="dev/configuration/.env.example"   
  if [ ! -f "$ENV_FILE" ]; then
    read -rp "$ENV_FILE does not exist. Create from $ENV_SAMPLE? This will create a fully local setup [y/N] " answer
    if [[ "$answer" =~ ^[Yy] ]]; then

      cp "$ENV_SAMPLE" "$ENV_FILE" || { echo "Failed to copy $ENV_SAMPLE to $ENV_FILE"; exit 127; }
      sed -i "s|^\($LOCAL_SETTING=\).*|\1true|" "$ENV_FILE"
      echo "$ENV_FILE created from $ENV_SAMPLE"
      cp /dev/configuration/plugins-local.py /dev/configuration/plugins.py  ## fix me before pull request
      set_local_toml
    else
      echo "Please provide $ENV_FILE. Otherwise the installation can not be continued."
      exit 1
    fi
  fi
}

set_local_toml() {
  declare -A REPLACEMENTS=(
    ["url = "]="ISDUBA_CLIENT_HOSTNAME_URL"
    ["keycloak_url = "]="ISDUBA_CLIENT_KEYCLOAK_URL"
    ["keycloak_realm = "]="ISDUBA_CLIENT_KEYCLOAK_REALM"
    ["username = "]="ISDUBA_CLIENT_USER"
    ["password = "]="ISDUBA_CLIENT_PASSWORD"
    )
    ## Set local tomls files
    cp "$NETBOX_SAMPLE" "$NETBOX_FILE" 
    cp "$ISDUBA_SAMPLE" "$ISDUBA_FILE" 
    value=$(grep -E "^${NETBOX_URL}=" "$ENV_FILE" | tail -n 1 | cut -d '=' -f 2-)
    sed -i "s|^\(api_url = \).*|\1\"$value\"|" "$NETBOX_FILE"

    ## Adjust the isduba setting with environment file
    for pattern in "${!REPLACEMENTS[@]}"; do
      value=$(grep -E "^${REPLACEMENTS[$pattern]}=" "$ENV_FILE" | tail -n 1 | cut -d '=' -f 2-)
      sed -i "s|^\($pattern\).*|\1\"$value\"|" "$ISDUBA_FILE"
    done
    
}

ensure_compose() {
  # Prefer `docker compose` (v2). Fall back to `docker-compose` (v1) if available.
  if command -v docker >/dev/null 2>&1 && docker compose version >/dev/null 2>&1; then
    echo "docker compose"
  elif command -v docker-compose >/dev/null 2>&1; then
    echo "docker-compose"
  else
    error "Neither 'docker compose' nor 'docker-compose' is available."; exit 127
  fi
}

print_post_instructions() {
  cat <<EOF

Services are starting. Useful info:
- NetBox UI:     http://netbox.localhost/  (admin / admin)
- ISDuBA UI:     http://isduba.localhost/  (user / user)

To get the NetBox API token printed by the setup container:
  $COMPOSE_CMD -f $COMPOSE_FILE logs netbox-setup

./dev/start-local-env.sh                       # start services in background
./dev/start-local-env.sh --recreate            # recreate containers
./dev/start-local-env.sh --stop                # stop 
./dev/start-local-env.sh --down                # stop and remove services
./dev/start-local-env.sh --down --volumes      # stop and remove services AND named volumes
./dev/start-local-env.sh --recreate --volumes  # full reset: down -v, then up (fresh volumes)
EOF
}

main() {
  need_cmd git
  need_cmd docker

  if [[ ! -f "$COMPOSE_FILE" ]]; then
    error "Compose file '$COMPOSE_FILE' not found. Run from the repository root."
    exit 1
  fi

  # Checking for Compose file first, ensures the root folder.
  need_env

  # Best-effort hint if submodules (for dev services) are missing
  if [[ ! -d "dev/netbox" || ! -d "dev/isduba" ]]; then
    info "Some dev service directories seem missing. If this fails, run:"
    info "  git submodule update --init --recursive"
  fi

  COMPOSE_CMD=$(ensure_compose)

  # Parse arguments
  ACTION="up"           # up | down | recreate
  WITH_VOLUMES=false    # whether to remove volumes (only valid for down/recreate)
  while [[ ${1-} ]]; do
    case "$1" in
      --down)
        ACTION="down"
        ;;
      --stop)
        ACTION="stop"
        ;;
      --recreate)
        ACTION="recreate"
        ;;
      --volumes|-v)
        WITH_VOLUMES=true
        ;;
      --help|-h)
        cat >&2 <<USAGE
Usage: $0 [--recreate|--down|--stop] [--volumes]

  --stop                 Stop services
  --down                 Stop and remove services
  --recreate             Recreate containers (like: up -d --force-recreate --remove-orphans)
  --volumes, -v          When used with --down or --recreate: also delete named volumes

Notes:
  --recreate --volumes will perform a full reset: 'down -v' followed by a fresh 'up'.
USAGE
        exit 0
        ;;
      *)
        echo "Unknown option: $1" >&2
        echo "Usage: $0 [--recreate|--down|--stop] [--volumes]" >&2
        exit 2
        ;;
    esac
    shift || true
  done

  # Guard: --volumes only meaningful with --down or --recreate
  if [[ "$ACTION" == "up" && "$WITH_VOLUMES" == true ]]; then
    error "--volumes is only supported with --down or --recreate"
    exit 2
  fi

  # Execute action
  case "$ACTION" in
    stop)
      info "Stopping dev environment..."
      $COMPOSE_CMD -f "$COMPOSE_FILE" stop
      exit 0
      ;;
    down)
      if [[ "$WITH_VOLUMES" == true ]]; then
        info "Stopping and removing dev environment and named volumes..."
        $COMPOSE_CMD -f "$COMPOSE_FILE" down -v
      else
        info "Stopping and removing dev environment..."
        $COMPOSE_CMD -f "$COMPOSE_FILE" down
      fi
      exit 0
      ;;
    recreate)
      if [[ "$WITH_VOLUMES" == true ]]; then
        info "Recreating dev environment with volume reset (down -v; up)..."
        $COMPOSE_CMD -f "$COMPOSE_FILE" down -v || true
        $COMPOSE_CMD -f "$COMPOSE_FILE" up -d --force-recreate --remove-orphans
      else
        info "Starting dev environment (recreate containers)..."
        $COMPOSE_CMD -f "$COMPOSE_FILE" up -d --force-recreate --remove-orphans
      fi
      ;;
    up)
      info "Starting dev environment..."
      $COMPOSE_CMD -f "$COMPOSE_FILE" up -d
      ;;
  esac

  # After startup, try to automatically print the NetBox API token from the setup container logs.
  # The setup container prints lines like:
  #   "API Token created: <TOKEN>" or "API Token already exists: <TOKEN>"
  # We'll wait up to 120 seconds for this to appear.
  SERVICE="netbox-setup"
  TIMEOUT=${TOKEN_TIMEOUT:-120}
  info "Waiting up to ${TIMEOUT}s for NetBox API token from '$SERVICE'..."

  end_time=$(( $(date +%s) + TIMEOUT ))
  token=""
  while [ $(date +%s) -lt $end_time ]; do
    # Fetch logs; ignore errors if service not ready yet
    LOGS=$($COMPOSE_CMD -f "$COMPOSE_FILE" logs "$SERVICE" 2>/dev/null || true)
    if echo "$LOGS" | grep -Eq "API Token (created|already exists):"; then
      # Extract the last occurrence to be safe
      token=$(echo "$LOGS" | grep -E "API Token (created|already exists):" | tail -n 1 | sed -E 's/.*API Token (created|already exists):\s*//')
      break
    fi
    sleep 2
  done

  if [ -n "$token" ]; then
    echo
    info "NetBox API token detected:"
    echo "$token"
    ## set it in env 
    LOCAL_SETTING=$(grep -E "^$LOCAL_SETTING=" "$ENV_FILE" | tail -n 1 | cut -d '=' -f 2-)
    if  [ "$LOCAL_SETTING" == "true" ]; then
        sed -i "s|^\(api_token = \).*|\1\"$token\"|" "$NETBOX_FILE"
    fi

    echo
  else
    info "Could not detect NetBox API token automatically within ${TIMEOUT}s. You can retrieve it manually with:"
    echo "  $COMPOSE_CMD -f $COMPOSE_FILE logs $SERVICE"
  fi

  print_post_instructions
}

main "$@"
