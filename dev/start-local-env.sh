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
#   ./dev/start-local-env.sh --clean                 # remove local images + local env/toml/plugins.py
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
PLUGINS_FILE="dev/configuration/plugins.py"
API_START=dev/configuration/script_api.sh
LOCAL_SETTING="FULLY_LOCAL"
JWT="JWT_KEY"

error() { echo "[ERROR] $*" >&2; }
info()  { echo "[INFO]  $*"; }

need_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    error "Required command '$1' not found in PATH"; exit 127
  fi
}

need_env() {
  # Checks if .env exists and use example instead if user approves
  if [ ! -f "$ENV_FILE" ]; then
    read -rp "$ENV_FILE does not exist. Create from $ENV_SAMPLE? This will create a fully local setup [y/N] " answer

    if [[ "$answer" =~ ^[Yy] ]]; then
      read -rp "Did you execute the following command: uv sync --all-extras ?" check    
      if [[ "$check" =~ ^[Yy] ]]; then
        cp -p "$ENV_SAMPLE" "$ENV_FILE" || { echo "Failed to copy $ENV_SAMPLE to $ENV_FILE"; exit 127; }
        sed -i "s|^\($LOCAL_SETTING=\).*|\1true|" "$ENV_FILE"
        echo "$ENV_FILE created from $ENV_SAMPLE"
        # Remove # for plugin_settings in  plugins.py
        set_plugin_config
        set_local_toml
      else
        echo "Please do so. Exit"
        exit 1
      fi
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
    cp -p "$NETBOX_SAMPLE" "$NETBOX_FILE"
    cp -p "$ISDUBA_SAMPLE" "$ISDUBA_FILE" 
    value=$(grep -E "^${NETBOX_URL}=" "$ENV_FILE" | tail -n 1 | cut -d '=' -f 2-)
    sed -i "s|^\(api_url = \).*|\1\"$value\"|" "$NETBOX_FILE"

    ## Adjust the isduba setting with environment file
    for pattern in "${!REPLACEMENTS[@]}"; do
      value=$(grep -E "^${REPLACEMENTS[$pattern]}=" "$ENV_FILE" | tail -n 1 | cut -d '=' -f 2-)
      sed -i "s|^\($pattern\).*|\1\"$value\"|" "$ISDUBA_FILE"
    done   
}

set_plugin_config(){
  ## setup assumes a comment out plugin_config
  LINE_START=$(awk '/^# PLUGINS_CONFIG/ { print NR }' $PLUGINS_FILE)
  LINE_STOP=$(awk -v start="$LINE_START" 'NR > start && /^# }/ { print NR }' $PLUGINS_FILE)

  ## checks before action
  [[ -n $LINE_START && -n $LINE_STOP ]] || { echo "ERROR: Line boundaries for commenting in plugin settings not found"; exit 1; }
  if (( $LINE_STOP - $LINE_START == 31 )); then
      sed -i "${LINE_START},${LINE_STOP}s/^#\s//" $PLUGINS_FILE
      else
      echo "Schema of PLUGIN_CONFIG seems to have changed. Installation stopped."
      exit 1
  fi
}

confirm_remove() {
  local target="$1"
  local reply
  while true; do
    if ! read -r -p "Remove $target? [y/N] " reply </dev/tty; then
      reply=""
    fi
    case "$reply" in
      [yY]|[yY][eE][sS]) return 0 ;;
      ""|[nN]|[nN][oO]) return 1 ;;
      *) echo "Please answer y or n." ;;
    esac
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

remove_local_configs() {
  local removed=false

  for env_file in ".env" "dev/.env" "docker/.env" "dev/isduba/docker/.env"; do
    if [[ -f "$env_file" ]]; then
      if confirm_remove "$env_file"; then
        info "Removing local env file: $env_file"
        rm -f "$env_file"
        removed=true
      else
        info "Keeping: $env_file"
      fi
    fi
  done

  if [[ -d "assets/plugin_configs/data_source/asset" ]]; then
    while IFS= read -r -d '' file; do
      if confirm_remove "$file"; then
        info "Removing local plugin config: $file"
        rm -f "$file"
        removed=true
      else
        info "Keeping: $file"
      fi
    done < <(find assets/plugin_configs/data_source/asset -maxdepth 1 -type f -name "*.toml" -print0)
  fi

  if [[ -d "assets/plugin_configs/data_source/csaf" ]]; then
    while IFS= read -r -d '' file; do
      if confirm_remove "$file"; then
        info "Removing local plugin config: $file"
        rm -f "$file"
        removed=true
      else
        info "Keeping: $file"
      fi
    done < <(find assets/plugin_configs/data_source/csaf -maxdepth 1 -type f -name "*.toml" -print0)
  fi

  if [[ "$removed" == false ]]; then
    info "No local env or plugin TOML files found to remove."
  fi
}

remove_plugins_config() {
  local plugins_file="dev/configuration/plugins.py"
  if [[ -f "$plugins_file" ]]; then
    if confirm_remove "$plugins_file"; then
      info "Removing local plugins configuration: $plugins_file"
      rm -f "$plugins_file"
    else
      info "Keeping: $plugins_file"
    fi
  else
    info "Plugins configuration file not found at $plugins_file"
  fi
}

copy_example_if_missing() {
  local example_file="$1"
  local target_file="$2"
  if [[ -f "$example_file" && ! -f "$target_file" ]]; then
    info "Copying $example_file to $target_file"
    cp -f "$example_file" "$target_file"
  fi
}

ensure_local_configs() {
  copy_example_if_missing ".env.example" ".env"
  copy_example_if_missing "dev/.env.example" "dev/.env"
  copy_example_if_missing "docker/.env.example" "docker/.env"
  copy_example_if_missing "dev/isduba/docker/.env.example" "dev/isduba/docker/.env"
  copy_example_if_missing "dev/configuration/plugins.py.example" "dev/configuration/plugins.py"
}

prune_project_images() {
  local compose_file="$1"
  if [[ -f "$compose_file" ]]; then
    info "Removing local images for $compose_file..."
    $COMPOSE_CMD -f "$compose_file" down --rmi local --remove-orphans || true
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

If not done yet, please set account for API access:
  uv run csaf_matcher_cli user create -u admin
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
      --clean)
        ACTION="clean"
        ;;
      --volumes|-v)
        WITH_VOLUMES=true
        ;;
      --help|-h)
        cat >&2 <<USAGE
Usage: $0 [--recreate|--down|--stop|--clean] [--volumes]

  --stop                 Stop services
  --down                 Stop and remove services
  --recreate             Recreate containers (like: up -d --force-recreate --remove-orphans)
  --clean                Remove local images and delete local env/plugin configs
  --volumes, -v          When used with --down or --recreate: also delete named volumes

Notes:
  --recreate --volumes will perform a full reset: 'down -v' followed by a fresh 'up'.
USAGE
        exit 0
        ;;
      *)
        echo "Unknown option: $1" >&2
        echo "Usage: $0 [--recreate|--down|--stop|--clean] [--volumes]" >&2
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
  if [[ "$ACTION" == "clean" && "$WITH_VOLUMES" == true ]]; then
    error "--volumes is not supported with --clean"
    exit 2
  fi

  if [[ "$ACTION" == "up" || "$ACTION" == "recreate" ]]; then
    ensure_local_configs
  fi

  # Execute action
  case "$ACTION" in
    stop)
      info "Stopping dev environment..."
      $COMPOSE_CMD -f "$COMPOSE_FILE" stop
      exit 0
      ;;
    clean)
      info "Cleaning local development environment..."
      prune_project_images "$COMPOSE_FILE"
      remove_local_configs
      remove_plugins_config
      info "Clean complete."
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
      # Sets token always new in case it changes.
      sed -i "s|^\(api_token = \).*|\1\"$token\"|" "$NETBOX_FILE"
    fi
    # set JWT secret key
    KEY=$(grep -E "^$JWT=" "$ENV_FILE" | tail -n 1 | cut -d '=' -f 2-)
    if  [ "$KEY" == "false" ]; then
      openssl rand -hex 32 | xargs -I{} printf "export JWT_SECRET_KEY={}\n" | tee -a .env dev/.env > /dev/null
      sed -i "s|^\($JWT=\).*|\1true|" "$ENV_FILE"
      info "JWT was created successfully"
    fi
    # start API
    read -rp "Do you want to start the apis right away [y/N] " answer
    if [[ "$answer" =~ ^[Yy] ]]; then
      bash $API_START
    fi

  else
    info "Could not detect NetBox API token automatically within ${TIMEOUT}s. You can retrieve it manually with:"
    echo "  $COMPOSE_CMD -f $COMPOSE_FILE logs $SERVICE"
  fi
  print_post_instructions
}

main "$@"
