# Matching-Agent

This repository contains a shared infrastructure for synchronizer daemons that fetch, transform, and store data in a
PostgreSQL database as well as a csaf-asset matching daemon.
It includes two concrete implementations:

1. **Asset Synchronizer (`assetsync`)**: Fetches and processes asset data.
2. **CSAF Synchronizer (`csafsync`)**: Fetches and processes CSAF (Common Security Advisory Framework) data.

Furthermore, it includes the matcher implementation that uses the data from the synchronizers to match assets.
The matches can be retrieved via a REST API, and alternatively, a hook can be set up to be notified of new matches (
WIP).

## Feature Matrix

| Feature                | Status | Notes                                                                         |
|------------------------|--------|:------------------------------------------------------------------------------|
| Asset Synchronization  | ✅ Done | Basic asset data syncing implemented                                          |
| CSAF Synchronization   | ✅ Done | CSAF advisory data syncing implemented                                        |
| Asset-CSAF Matching    | ✅ Done | A simple Matcher that matches everything with maximum score.                  |
| Sophisticated Matching | 🚧 WIP | A sophisticated matching algorithm that properly assigns match probabilities. | 
| REST API               | 🚧 WIP | Groundwork has been done. Need to specify API                                 |
| Webhook Notifications  | 🚧 WIP | Notification system being developed                                           |
| Plugin System          | ✅ Done | Extensible plugin architecture ready                                          |

## Project Structure

- `src/dina/synchronizer/`: Shared infrastructure for synchronizer daemons.
- `src/dina/assetsync/`: Asset Synchronizer implementation.
- `src/dina/csafsync/`: CSAF Synchronizer implementation.
- `src/dina/matcher/`: Main package.
- `plugins/`: Plugin implementations for extending functionality.

For more details about the synchronizer infrastructure, see the Synchronizer Infrastructure README. (TODO)

## Getting Started

The following steps are intended for setting up a development environment on Ubuntu.
For production use refer to the [Production Docker setup](#production-docker-setup) section below.
For other distributions or operating systems, you may need to adjust the instructions accordingly.

1. Install [uv](https://docs.astral.sh/uv/), git, docker and docker compose in any way that suits you.
2. Clone the repository.

```shell
git clone -b feat/initial_structure https://github.com/DINA-community/Matching-Agent.git
cd Matching-Agent
```

3. (optional) If you want to use the docker-compose setup, also clone the submodules:
```shell
git submodule update --init --recursive
```

You now can either build the docs with `make docs` and follow the instructions there or proceed with the instructions below.

### Plugin build prerequisite (ISDuBA)

If you plan to use the ISDuBA CSAF source (the `isduba_fetcher` extra or the ISDuBA plugin workspace), a Java runtime is required during the build/install step. Make sure a Java Runtime Environment is available on your machine before running `uv sync` with the ISDuBA extras:

- Recommended: OpenJDK 17 (or newer)
- Ensure `java` is on your `PATH` (or set `JAVA_HOME` accordingly)

Example:

```bash
uv sync --extra isduba_fetcher
```

Without Java present, the ISDuBA plugin build will fail.

### Quick start: local dev environment script

You can start, stop, and recreate the full local development stack (PostgreSQL, NetBox, ISDuBA, etc.) using the helper script in the `dev/` directory:

```bash
./dev/start-local-env.sh                       # start services in background
./dev/start-local-env.sh --recreate            # recreate containers
./dev/start-local-env.sh --down                # stop and remove services
./dev/start-local-env.sh --down --volumes      # stop and remove services AND named volumes
./dev/start-local-env.sh --recreate --volumes  # full reset: down -v, then up (fresh volumes)
```

Notes:
- Requires Docker and Docker Compose (`docker compose`).
- If you haven't initialized submodules yet, run `git submodule update --init --recursive`.
- After startup, you can retrieve the NetBox API token from the setup container logs:
  ```bash
  docker compose -f dev/docker-compose.yml logs netbox-setup
  ```

The NetBox and ISDuBA services will be available at:
- NetBox UI: http://netbox.localhost/ (default: admin / admin)
- ISDuBA UI: http://isduba.localhost/ (default: user / user)

### Alternative: run docker compose directly

There are two possible ways to set up a development environment using Docker Compose directly.
First, you can use externally installed asset or CSAF inventories and only set up a local database:

```shell
docker compose -f dev/docker-compose-silab.yml up -d
```

Alternatively, you can set up a fully local environment with a NetBox and ISDuBA installation:

```shell
docker compose -f dev/docker-compose.yml up -d
```

If you use the fully local environment, the API token for NetBox is printed by the `netbox-setup` container. You can read it with:

```shell
docker compose -f dev/docker-compose.yml logs netbox-setup
```
The API token is printed to the console.

To configure the netbox fetcher plugin, copy the file [assets/plugin_configs/data_source/asset/sample/netbox.toml](assets/plugin_configs/data_source/asset/sample/netbox.toml) to `assets/plugin_configs/data_source/asset/netbox_local.toml`.
The file can be named any way you like, but it must be a toml file.
Replace the `api_token` with the API token printed by the netbox-setup container.
Replace the `url` with the url of the netbox instance (http://netbox.localhost/).

To configure the ISDuBA fetcher plugin, copy the file [assets/plugin_configs/data_source/csaf/sample/isduba.toml](assets/plugin_configs/data_source/csaf/sample/isduba.toml) to `assets/plugin_configs/data_source/csaf/isduba_local.toml`.
The file can be named any way you like, but it must be a toml file.
Replace the `url` with the url of the ISDuBA instance http://isduba.localhost/.
Replace the `username` and `password` with the credentials of the ISDuBA user (user/user).
Replace the `keycloak_url` with the url of the keycloak instance http://keycloak.localhost/.

The ISDuBA interface can be reached at http://isduba.localhost/ and the netbox interface at http://netbox.localhost/.
The default credentials are:
- Netbox: admin / admin
- ISDuBA: user / user

Before starting the synchronizers, make sure to create some assets and csaf advisories in the netbox and ISDuBA instances.
Follow the corresponding instructions in the netbox and ISDuBA documentation.

Next, install the python dependencies with uv by running in your terminal or inside pycharm (double tap `<Ctrl>` and enter the
command) to set up the local python environment:

```shell
uv sync --all-extras
```

This will install all the available plugins in the `plugins/` directory in addition to the base package.
If you want to install only the base package, just run `uv sync`.
The plugins can be installed with `uv sync --extra <PLUGIN_NAME>` later on.
To install multiple extras, provie multiple `--extra` arguments.

### Matcher CLI

A command-line interface is available to interact with the Matcher service (obtain tokens, list/get matches, start/stop tasks, clear caches). See the full guide:

- docs/matcher-cli.rst

Quick example (using uv):

```bash
uv run csaf_matcher_cli --base-url http://localhost:8998 -u admin \
  matcher matches list --limit 20
```

Note: For interactive use, omit `-p/--password` to be securely prompted.

## Contributing

If you want to contribute to the project, please read the [Contributing Guide](CONTRIBUTING.md).

```shell
uv run ruff check
```

## Configuration and APIs

This project provides three long-running components: two synchronizers and the matcher. Each reads a TOML
configuration file from the `assets/` directory and exposes a small HTTP API.

- Asset Synchronizer (assetsync)
  - Config file: assets/assetsync.toml
  - Default API: http://0.0.0.0:8000
- CSAF Synchronizer (csafsync)
  - Config file: assets/csafsync.toml
  - Default API: http://0.0.0.0:8001
- Matcher
  - Config file: assets/matcher.toml
  - Default API: http://0.0.0.0:8998

You can change host and port for each service in the respective config under the [..Api] section.

### Matcher configuration (assets/matcher.toml)

Minimal example (defaults in repo):

```
[Matcher]
sync_interval = 60  # seconds between matching runs
asset_plugins_path = "./assets/plugin_configs/data_source/asset"
csaf_plugins_path = "./assets/plugin_configs/data_source/csaf"

[Matcher.Api]
host = "0.0.0.0"
port = 8998

[Matcher.Cachedb]
host = "localhost"
port = 2345
database = "cachedb"
username = "admin"
password = "secret"
```

- Matcher.sync_interval: Minimal delay between matching cycles.
- Matcher.asset_plugins_path: Path to the directory containing asset-specific plugin configuration files.
- Matcher.csaf_plugins_path: Path to the directory containing CSAF-specific plugin configuration files.
- Matcher.Api.host/port: Address where the FastAPI server listens.
- Matcher.Cachedb: Connection to the shared cache DB used by all components.

The API documentation can be found at `http://host:port/docs`.

## Production Docker setup

This repository ships a simple production‑ready Docker setup that runs the three services (assetsync, csafsync, matcher) with a shared PostgreSQL database and exposes all three APIs over HTTPS using a self‑signed certificate.

Contents:
- docker/assetsync.Dockerfile, docker/csafsync.Dockerfile, docker/matcher.Dockerfile (built with uv inside the image)
- docker/assets/*.toml – service configs pre‑configured for Docker (DB points to the `postgres` service)
- docker/nginx – lightweight TLS reverse proxy that terminates HTTPS and routes to the three services
- docker/docker-compose.yml – production compose file
- docker/.env.example – environment defaults you can copy to `.env`

### Quick start

1) Create an environment file

```
cd docker
cp .env.example .env
# IMPORTANT: Adjust passwords/ports and TLS_CN (used as certificate CN)
```

2) Build and start the stack

```
docker compose up -d --build
```

This starts:
- postgres (16‑alpine)
- assetsync, csafsync, matcher (Python images built from source)
- gateway (NGINX, generates a self‑signed TLS cert on first run)

3) Access the APIs via HTTPS

- Matcher: https://localhost:8443/matcher/
- Assetsync: https://localhost:8443/assetsync/
- CSAFsync: https://localhost:8443/csafsync/

OpenAPI docs (if enabled in the service) are typically available at `/docs` under each prefix, for example:

- https://localhost:8443/matcher/docs
- https://localhost:8443/assetsync/docs
- https://localhost:8443/csafsync/docs

Note: Your browser/HTTP client will warn about the self‑signed certificate. You can trust it locally or override verification as appropriate.

### Configuration notes

- The services run with Docker‑specific TOML configs from `docker/assets/*.toml`. They point to the `postgres` service using the credentials from `docker/.env`. The toml files need to be adjusted to match your environment. I.e., the asset sources need to be configured to point to the sources of the environment where you are deploying the services.
- The services listen on the following internal ports (routed by the gateway):
  - matcher: 8998
  - assetsync: 8992
  - csafsync: 8991
- The HTTPS gateway listens on port `8443` by default and can be changed via `HTTPS_PORT` in `docker/.env`.
- To regenerate a self‑signed certificate, remove the `gateway-certs` volume and restart the `gateway` service:

```
docker compose down
docker volume rm matching-agent_gateway-certs || true
docker compose up -d
```

### Stop and remove

```
docker compose down
# Add -v to remove named volumes as well
docker compose down -v
```

### Asset Synchronizer configuration (assets/assetsync.toml)

Example (defaults in repo):

```
[Assetsync]
# Asset-specific options go here (plugin-specific)

[Synchronizer]
sync_interval = 60
preprocessor_plugins = ["identity"]
plugin_configs_path = "./assets/plugin_configs/data_source/asset"
cleanup_grace_period = 3600

[Synchronizer.Api]
host = "0.0.0.0"
port = 8992

[Cachedb]
host = "localhost"
port = 2345
database = "cachedb"
username = "admin"
password = "secret"
```

- Synchronizer.sync_interval: Minimal delay between fetch cycles.
- Synchronizer.preprocessor_plugins: List and order of preprocessing plugins.
- Synchronizer.plugin_configs_path: Path to the directory containing plugin configuration files.
- Synchronizer.cleanup_grace_period: Time in seconds from the last synchronization after which assets are considered stale and will be deleted.
- Synchronizer.Api.host/port: Address for the synchronizer API.
- Cachedb: Connection to the shared cache DB.
- Data source plugins: Configuration TOML files are loaded from assets/plugin_configs/asset_source/…

The API documentation can be found at `http://host:port/docs`.

### CSAF Synchronizer configuration (assets/csafsync.toml)

Example (defaults in repo):

```
[Csafsync]
# CSAF-specific options go here (plugin-specific)

[Synchronizer]
sync_interval = 60
preprocessor_plugins = ["identity"]
plugin_configs_path = "./assets/plugin_configs/data_source/csaf"
cleanup_grace_period = 3600

[Synchronizer.Api]
host = "0.0.0.0"
port = 8991

[Cachedb]
host = "localhost"
port = 2345
database = "cachedb"
username = "admin"
password = "secret"
```

- Same meaning as for the Asset Synchronizer

The API documentation can be found at `http://host:port/docs`.

### Running the applications

Targets can be run by typing `uv run <TARGET_NAME>` or by selecting it in the run configurations menu
in Pycharm.
For example, try running the following to start the matching agent.

```shell
uv run csaf_matcher
```

To run the Asset Synchronizer:

```shell
uv run assetsync
```

To run the CSAF Synchronizer:

```shell
uv run csafsync
```


## Authenticate with the API

The synchronizer components (Asset/CSAF) and the Matcher expose a small FastAPI HTTP API that uses OAuth2 Password flow to issue short‑lived JWT bearer tokens.

Quick start:

1) Make sure the component is running (e.g., Asset Synchronizer default at http://localhost:8992; configurable in `assets/assetsync.toml`).
2) Create or update a user in the CacheDB using the CLI:

```bash
uv run csaf_matcher_cli user create -u admin
```

Note: For interactive use, do not pass passwords via `-p/--password`. The CLI will securely prompt
for the password. Reserve `-p` only for non-interactive environments (e.g., CI) and source secrets
from a secure provider.

3) Obtain an access token (form fields `username` and `password`):

```bash
BASE_URL="http://localhost:8992"  # adjust to the component you call
curl -sS -X POST "$BASE_URL/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=admin"
# => {"access_token": "<JWT>", "token_type": "bearer"}
```

4) Call protected endpoints with the token:

```bash
TOKEN="<paste access_token>"
curl -sS "$BASE_URL/status" -H "Authorization: Bearer $TOKEN"
```

Notes:
- Token lifetime is controlled by `[Synchronizer.Api].access_token_expire_minutes` in the component’s TOML config.
- Interactive API docs are available at `$BASE_URL/docs` (Swagger UI).

For a detailed guide (including HTTPie and Python examples, troubleshooting, and security notes), see:
- docs/authentication.rst
