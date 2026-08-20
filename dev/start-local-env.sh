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
PLUGINS_SAMPLE="dev/configuration/plugins.py.example"
API_START=dev/scripts-install/script_api.sh
LOCAL_SETTING="FULLY_LOCAL"
JWT="JWT_KEY"

ENV_FILES=(
	".env"
	"dev/.env"
	"docker/.env"
	"dev/isduba/docker/.env"
)

FILE_PAIRS=(
	"dev/configuration/.env.example .env"
	"dev/configuration/.env.example dev/.env"
	"docker/.env.example docker/.env"
	"dev/configuration/.env.isduba.example dev/isduba/docker/.env"
	"$PLUGINS_SAMPLE $PLUGINS_FILE"
)

API_PID=(
	"assetsync.pid"
	"csafsync.pid"
	"matcher.pid"
)

error() { echo "[ERROR] $*" >&2; }
warning() { echo "[WARNING] $*" >&2; }
info() { echo "[INFO]  $*" >&2; }

need_cmd() {
	if ! command -v "$1" >/dev/null 2>&1; then
		error "Required command '$1' not found in PATH"
		exit 127
	fi
}

need_dep() {
	## INSTALL DEPENDENCIES
	KEY=$(grep -E '^DEP=' "$ENV_FILE" | tail -n 1 | cut -d '=' -f 2- || true)
	if [ -z "$KEY" ]; then
		warning "Your $ENV_FILE is missing the DEP entry. Compare $ENV_SAMPLE."
		exit 1
	fi
	if [ "$KEY" == "false" ]; then
		if check_response "Do you want to check for missing dependencies and install them? [Y/n] " Y; then
			wdir=$(pwd)
			idir="$wdir/dev/scripts-install/"
			cd "$idir" || {
				warning "$idir missing?! You just executed me there!"
				exit 1
			}
			#bash ./install_depsetup.sh
			cd ../../
			sed -i "s|^\(DEP=\).*|\1true|" "$ENV_FILE"
			info "--DEP set true in $ENV_FILE"
		fi
	else
		info "--[DEP] DEP is set as executed in $ENV_FILE. Skip check."
	fi
}

need_env() {
	# Checks if .env exists and setup a default installation if user approves
	info "--[ENV] Check for $ENV_FILE"
	if [ ! -f "$ENV_FILE" ]; then
		if check_response "$ENV_FILE does not exist. Create from $ENV_SAMPLE? This will create a fully local setup [Y/n]" "Y"; then
			if ! check_response "Did you execute the following command? uv sync --all-extras? Otherwise it will be executed now. [y/N]" "N"; then
				info "--[ENV] sync wird ausgeführt"
				uv sync --all-extras
			fi
			cp -p "$ENV_SAMPLE" "$ENV_FILE" || {
				error "Failed to copy $ENV_SAMPLE to $ENV_FILE"
				exit 127
			}
			sed -i "s|^\($LOCAL_SETTING=\).*|\1true|" "$ENV_FILE"
			info "--[ENV] $ENV_FILE created from $ENV_SAMPLE"
			# Remove # for plugin_settings in plugins.py
			set_plugin_config
			set_local_toml
		else
			if check_response "Please provide $ENV_FILE. Otherwise the installation will probably not work if the README was not used accordingly. Proceed? [y/N]" "N"; then
				info "Installation initiating..."
				sleep 2
			else
				info "Installation stopped by user."
				exit 1
			fi
		fi
	fi
}

set_local_toml() {
	info "--[ENV] Set local toml files"
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
	info "--[ENV] Set local toml files done"
}

set_plugin_config() {
	## setup assumes a comment out plugin_config
	if [[ ! -f "$PLUGINS_FILE" ]]; then
		info "--[ENV] $PLUGINS_FILE is missing. $PLUGINS_SAMPLE will be modified and used."
		cp -p "$PLUGINS_SAMPLE" "$PLUGINS_FILE"
	fi
	## checks before action
	LINE_START=$(awk '/^# PLUGINS_CONFIG/ { print NR }' $PLUGINS_FILE)
	LINE_STOP=$(awk -v start="$LINE_START" 'NR > start && /^# }/ { print NR }' $PLUGINS_FILE)
	[[ -n $LINE_START && -n $LINE_STOP ]] || {
		echo "ERROR: Line boundaries for commenting in plugin settings not found"
		exit 1
	}
	if (( LINE_STOP - LINE_START == 31 )); then
		sed -i "${LINE_START},${LINE_STOP}s/^#\s//" $PLUGINS_FILE
	else
		warning "--[ENV] Schema of PLUGIN_CONFIG seems to have changed. Installation stopped."
		exit 1
	fi
}

check_response() {
	local text="$1"
	local default_reply="${2:-None}" # Assign default reply if provided
	local reply
	while true; do
		read -rp "[INPUT] $text" reply </dev/tty
		if [ -z "$reply" ]; then
			reply="$default_reply"
		fi
		case "$reply" in
		[yY] | [yY][eE][sS]) return 0 ;;
		"" | [nN] | [nN][oO]) return 1 ;;
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
		error "Neither 'docker compose' nor 'docker-compose' is available."
		exit 127
	fi
}

remove_files() {
	local file_list=("$@")
	for file in "${file_list[@]}"; do
		if $confirm_all || check_response "Remove $file? [Y/n]" "Y"; then
			info "--[EXE] Removing: $file"
			rm -f "$file"
			removed=true
		else
			info "--[EXE] Keeping: $file"
		fi
	done
}

remove_local_configs() {
	# Ask for confirmation at the beginning for a full cleanup
	local confirm_all=true
	local removed=false
	if check_response "--[EXE] Remove all local files directly? [Y/n]" "Y"; then
		confirm_all=true
	else
		confirm_all=false
	fi

	# remove .env files
	for env_file in "${ENV_FILES[@]}"; do
		if [[ -f "$env_file" ]]; then
			remove_files "$env_file"
			removed=true
		fi
	done
	if [[ "$removed" == false ]]; then
		info "--[EXE] No local env files found to remove."
	fi

	# Remove toml files in asset
	if [[ -d "assets/plugin_configs/data_source/asset" ]]; then
		mapfile -t asset_files < <(find assets/plugin_configs/data_source/asset -maxdepth 1 -type f -name "*.toml" -print0)
		if [[ ${#asset_files[@]} -gt 0 ]]; then
			remove_files "${asset_files[@]}"
		else
			info "--[EXE] No plugin TOML file in asset found."
		fi

	fi

	# Remove toml files in csaf
	if [[ -d "assets/plugin_configs/data_source/csaf" ]]; then
		mapfile -t csaf_files < <(find assets/plugin_configs/data_source/csaf -maxdepth 1 -type f -name "*.toml" -print0)
		if [[ ${#csaf_files[@]} -gt 0 ]]; then
			remove_files "${csaf_files[@]}"
		else
			info "--[EXE] No plugin TOML files in csaf found."
		fi
	fi

}

remove_plugins_config() {
	local plugins_file=$PLUGINS_FILE
	if [[ -f "$plugins_file" ]]; then
		if check_response "Remove $plugins_file? [Y/n]" "Y"; then
			info "--[EXE] Removing local plugins configuration: $plugins_file"
			rm -f "$plugins_file"
		else
			info "--[EXE] Keeping: $plugins_file"
		fi
	else
		info "--[EXE] Plugins configuration file not found at $plugins_file"
	fi
}

ensure_local_configs() {
	# Set sample files in case file is missing
	# Note that the dev/.env is already set by fkt need_env
	for pair in "${FILE_PAIRS[@]}"; do
		set -- $pair
		local target_file="$2"
		local example_file="$1"
		if [[ -f "$example_file" && ! -f "$target_file" ]]; then
			info "--[EXE] Copying $example_file to $target_file"
			cp -fp "$example_file" "$target_file"
		fi
	done
}

prune_project_images() {
	local compose_file="$1"
	if [[ -f "$compose_file" ]]; then
		info "--[EXE] Removing local images for $compose_file..."
		command_output=$($COMPOSE_CMD -f "$compose_file" down --rmi local --remove-orphans 2>&1)
		if echo "$command_output" | grep -iq "variable is not set"; then
			info "--[EXE] There is no project image"
		else

			$COMPOSE_CMD -f "$compose_file" down --rmi local --remove-orphans #|| true
		fi
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
./dev/start-local-env.sh -c, --clean               # remove local images + local env/toml/plugins.py
./dev/start-local-env.sh -d, --down                # stop and remove services
./dev/start-local-env.sh -d -r, --down --volumes      # stop and remove services AND named volumes
./dev/start-local-env.sh -r -v, --recreate --volumes  # full reset: down -v, then up (fresh volumes)
./dev/start-local-env.sh -r, --recreate            # recreate containers
./dev/start-local-env.sh -s, --stop                # stop 

If you want to use a test database for netbox look at
  dev/test-cases

If not done yet, please set account for API access:
  uv run csaf_matcher_cli user create -u admin
EOF
}

parse_arguments() {
	local ACTION="up"        # Default action
	local WITH_VOLUMES=false # Default value for volumes flag
	local valid_actions=("up" "down" "recreate" "stop" "clean")
	local valid_flags=("u" "d" "r" "s" "c" "v")

	while [[ $# -gt 0 ]]; do
		case "$1" in
		-h | --help)
			cat >&2 <<USAGE
Usage: $0 [Options]
    Options:
    -c, --clean      Remove local images and configs.
    -d, --down       Stop and remove services.
    -r, --recreate   Recreate containers. (up -d --force-recreate --remove-orphans))
    -s, --stop       Stop services.
    -u, --up         Start services. (default)
    -v, --volumes    Remove named volumes (with --down or --recreate).

    Combination:
    --recreate --volumes   Full reset (down -v && up)
    
    Requirements:
    Docker and Docker Compose (v2) required.

    Receiving NetBox API token:
    docker compose -f dev/docker-compose.yml logs netbox-setup
USAGE
			exit 1
			;;
		--*)
			if [[ "${1:0:3}" == "---" ]]; then
				print_help "$1"
			else
				case "$1" in
				--up) ACTION="up" ;;
				--volumes) WITH_VOLUMES=true ;;
				--down) ACTION="down" ;;
				--stop) ACTION="stop" ;;
				--recreate) ACTION="recreate" ;;
				--clean) ACTION="clean" ;;
				*)
					print_help "$1"
					;;
				esac
			fi
			shift
			;;
		-*)
			flags="${1:1}" # Remove leading '-'
			if ((${#flags} > 2)); then
				error "Too many options"
				print_help "$flags"
			else
				for ((i = 0; i < ${#flags}; i++)); do
					arg="${flags:i:1}"
					if [[ ! " ${valid_flags[*]} " =~ " ${arg} " ]]; then
						error "Invalid flag '$arg'"
						print_help "$arg"
					fi
					case "$arg" in
					u) ACTION="up" ;;
					v) WITH_VOLUMES=true ;;
					d) ACTION="down" ;;
					s) ACTION="stop" ;;
					r) ACTION="recreate" ;;
					c) ACTION="clean" ;;
					esac
				done
			fi
			shift
			;;
		*)
			print_help "$1"

			;;
		esac
	done

	# Validate action
	if [[ ! " ${valid_actions[*]} " =~ " ${ACTION} " ]]; then
		print_help "$ACTION"
	fi

	echo "$ACTION|$WITH_VOLUMES"
}

print_help() {
	echo "Invalid option: $1" >&2
	echo "Use -h or --help for help" >&2
	exit 1
}

main() {
	local parameter
	parameter=$(parse_arguments "$@")
	IFS='|' read -r ACTION WITH_VOLUMES <<<"$parameter"
	checks
	execute
	post_processing
	cleanup
}

checks() {
	info "#Checks started"
	info "## Check Argument"
	info "--Action: $ACTION and Volume: $WITH_VOLUMES"
	if [[ "$ACTION" == "up" && "$WITH_VOLUMES" == true ]]; then
		error "--[CHK] --volumes is only supported with --down or --recreate"
		exit 2
	fi
	if [[ "$ACTION" == "clean" && "$WITH_VOLUMES" == true ]]; then
		error "--[CHK] --volumes is not supported with --clean"
		exit 2
	fi
	info "## Check Setting"
	if [[ "$ACTION" == "clean" || "$ACTION" == "down" || "$ACTION" == "stop" ]]; then
		need_cmd docker
		COMPOSE_CMD=$(ensure_compose)
	else # Skipping unnecessary checks for cleaning
		## INSTALL DEPENDENCIES
		need_env
		need_dep
		need_cmd docker
		COMPOSE_CMD=$(ensure_compose)
		need_cmd git

		# Checking for Compose file, ensures the root folder.
		if [[ ! -f "$COMPOSE_FILE" ]]; then
			error "-[CHK]Compose file '$COMPOSE_FILE' not found. Run from the repository root."
			exit 1
		fi

		# Best-effort hint if submodules (for dev services) are missing
		if [[ ! -d "dev/netbox" || ! -d "dev/isduba" || ! "$(ls -A dev/netbox)" || ! "$(ls -A dev/isduba)" ]]; then
			info "Some dev service directories seem missing. Installing"
			git submodule update --init --recursive
		fi
	fi
	info "-[CHK] completed"
}

execute() {
	info "# Execute action $ACTION"
	case "$ACTION" in
	stop)
		info "--[EXE] Stopping dev environment..."
		stop_apis
		$COMPOSE_CMD -f "$COMPOSE_FILE" stop
		exit 0
		;;
	clean)
		info "--[EXE] Cleaning local development environment..."
		prune_project_images "$COMPOSE_FILE"
		remove_local_configs
		remove_plugins_config
		info "--[EXE] Clean complete."
		exit 0
		;;
	down)
		stop_apis
		if [[ "$WITH_VOLUMES" == true ]]; then
			info "--[EXE] Stopping and removing dev environment and named volumes..."
			$COMPOSE_CMD -f "$COMPOSE_FILE" down -v
		else
			info "--[EXE] Stopping and removing dev environment..."
			$COMPOSE_CMD -f "$COMPOSE_FILE" down
		fi
		exit 0
		;;
	recreate)
		ensure_local_configs
		stop_apis
		sleep 2
		if [[ "$WITH_VOLUMES" == true ]]; then
			info "-- [EXE] Recreating dev environment with volume reset (down -v; up)..."
			$COMPOSE_CMD -f "$COMPOSE_FILE" down -v || true
			$COMPOSE_CMD -f "$COMPOSE_FILE" up -d --force-recreate --remove-orphans
		else
			info "-- [EXE] Starting dev environment (recreate containers)..."
			$COMPOSE_CMD -f "$COMPOSE_FILE" up -d --force-recreate --remove-orphans
		fi
		;;
	up)
		info "-- [EXE] Starting dev environment..."
		ensure_local_configs
		sleep 2
		$COMPOSE_CMD -f "$COMPOSE_FILE" up -d
		;;
	*)
		warning "Action undefined and checks skip this."
		exit 127
	esac

}


stop_process() {
	# Helper function of stop_apis
    local pid="$1"
    local label="$2"
    
    # Don't kill invalid or PID 1
    if [[ -z "$pid" ]] || [[ "$pid" == "1" ]]; then
        info "Skipping PID $pid (invalid or PID 1)"
        return
    fi
    
    # Check if process exists
    if ! kill -0 "$pid" 2>/dev/null; then
        info "Process $pid is not running"
        # Try to find child processes by name
        local name="${label%%.*}"
        if pgrep -f "$name" > /dev/null 2>&1; then
            local child_pids
            child_pids=$(pgrep -f "$name")
            if [[ -n "$child_pids" ]]; then
                echo "$child_pids" | xargs kill -SIGTERM 2>/dev/null
                info "Killed $name with SIGTERM (by name)"
            fi
        fi
        return
    fi
    
    # Graceful shutdown with timeout
    kill -SIGTERM "$pid"
    info "Killed $label with SIGTERM ($pid)"
    
    local timeout=5
    while kill -0 "$pid" 2>/dev/null && [[ $timeout -gt 0 ]]; do
        sleep 1
        ((timeout--))
    done
    
    # Force kill if still running
    if kill -0 "$pid" 2>/dev/null; then
        kill -SIGKILL "$pid" 2>/dev/null
        info "Force killed $label with SIGKILL ($pid)"
    fi
}

stop_apis() {
	# Since PID of the xdg-terminal-exec process, not necessarily the PID of the terminal window or bash process it launches. 
	# So using that PID later to monitor/kill the terminal may not work reliably.
	# As a result, the stop function checks for the title name also if PID is outdated.
    info "--[EXE] Stopping APIs"
    for pidfile in "${API_PID[@]}"; do
        if [[ -f "$pidfile" ]]; then
            pid="$(<"$pidfile")"
            local name="${pidfile%%.*}"
            stop_process "$pid" "$name"
            rm -f -- "$pidfile"
        fi
    done
    info "--[EXE] Stopping APIs finished"
}

post_processing() {
	# After startup, try to automatically print the NetBox API token from the setup container logs.
	# The setup container prints lines like:
	#   "API Token created: <TOKEN>" or "API Token already exists: <TOKEN>"
	# We'll wait up to 120 seconds for this to appear.
	info "# Start post_processing"
	SERVICE="netbox-setup"
	TIMEOUT=${TOKEN_TIMEOUT:-120}
	info "--[PoP] Waiting up to ${TIMEOUT}s for NetBox API token from '$SERVICE'..."

	end_time=$(($(date +%s) + TIMEOUT))
	token=""
	while [ "$(date +%s)" -lt $end_time ]; do
		# Fetch logs; ignore errors if service not ready yet
		LOGS=$($COMPOSE_CMD -f "$COMPOSE_FILE" logs "$SERVICE" 2>/dev/null || true)
		if echo "$LOGS" | grep -Eq "API Token (created|already exists):"; then
			# Extract the last occurrence to be safe
			token=$(echo "$LOGS" | grep -E "API Token (created|already exists):" | tail -n 1 | sed -E 's/.*API Token (created|already exists):\s*//')
			break
		fi
		sleep 2
	done

}

cleanup() {
	info "#Start cleanup from script."
	if [ -n "$token" ]; then
		echo
		info "--[CLE] NetBox API token detected:"
		echo "$token"
		## set it in env
		LOCAL_SETTING=$(grep -E "^$LOCAL_SETTING=" "$ENV_FILE" | tail -n 1 | cut -d '=' -f 2-)
		if [ "$LOCAL_SETTING" == "true" ]; then
			# Sets token always new in case it changes.
			sed -i "s|^\(api_token = \).*|\1\"$token\"|" "$NETBOX_FILE"
		fi
		# set JWT secret key
		KEY=$(grep -E "^$JWT=" "$ENV_FILE" | tail -n 1 | cut -d '=' -f 2-)
		if [ "$KEY" == "false" ]; then
			openssl rand -hex 32 | xargs -I{} printf "export JWT_SECRET_KEY={}\n" | tee -a .env dev/.env >/dev/null
			sed -i "s|^\($JWT=\).*|\1true|" "$ENV_FILE"
			info "--[CLE] JWT was created successfully"
		fi
		# Start API
		local excess
		if check_response "Do you want to start the apis right away? [y/N]" "N"; then
			if check_response "Do you execute the script on a remote PC (using ssh)? [Y/n]" "Y"; then
				excess="remote"
			else
				excess="local"
			fi
			bash $API_START $excess
		fi

	else
		info "--[CLE] Could not detect NetBox API token automatically within ${TIMEOUT}s. You can retrieve it manually with:"
		echo "  $COMPOSE_CMD -f $COMPOSE_FILE logs $SERVICE"
	fi
	print_post_instructions

}

main "$@"
