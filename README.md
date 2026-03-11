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
| Asset Synchronization  | ✅ Done | Basic asset data syncing implemented                                         |
| CSAF Synchronization   | ✅ Done | CSAF advisory data syncing implemented                                       |
| Asset-CSAF Matching    | ✅ Done | A simple Matcher that matches everything with maximum score.                 |
| Sophisticated Matching | 🚧 WIP | A sophisticated matching algorithm that properly assigns match probabilities. |
| REST API               | 🚧 WIP | Groundwork has been done. Need to specify API                                 |
| Webhook Notifications  | 🚧 WIP | Notification system being developed                                           |
| Plugin System          | ✅ Done | Extensible plugin architecture ready                                         |

## Project Structure

- `src/dina/synchronizer/`: Shared infrastructure for synchronizer daemons.
- `src/dina/assetsync/`: Asset Synchronizer implementation.
- `src/dina/csafsync/`: CSAF Synchronizer implementation.
- `src/dina/matcher/`: Main package.
- `plugins/`: Plugin implementations for extending functionality.

For more details about the synchronizer infrastructure, see the Synchronizer Infrastructure README. (TODO)

## Getting Started

### Requirements

Make sure you have the following requirements installed:

- [uv](https://docs.astral.sh/uv/) (0.9 or newer)
- git
- docker (28.5 or newer)
- docker compose (2.40 or newer)
- OpenJDK 17 (or newer) (optional, required for ISDuBA CSAF source). Ensure `java` is on your `PATH` (or set `JAVA_HOME` accordingly).

The following steps are intended for setting up a development environment on Ubuntu.
For other distributions or operating systems, you may need to adjust the instructions accordingly.

First, clone the repository:

```shell
git clone --recurse-submodules https://github.com/DINA-community/Matching-Agent.git
cd Matching-Agent
uv sync --extra isduba_fetcher # If you plan to use the ISDuBA CSAF source (default plugin name `isduba_fetcher`)
```

You can either build the docs with `make docs` and follow the instructions there or proceed with the instructions below.

## Installation

To set up a development environment, follow the steps below.

- Use either of the following methods to set up the runtime environment:
  - [Fully local setup](#fully-local-setup)
  - [Setup with external asset sources](#setup-with-external-asset-sources)
- And then configure according to the [Configuration](#configuration) documentation
  - [Plugins](#configure-plugins)
  - [API](#configure-apis)
- For production use refer to the [Production Docker setup](#production-docker-setup)

### Fully Local Setup

You can start, stop, and recreate the full local development stack (PostgreSQL, NetBox, ISDuBA, etc.) using the helper script in the `dev/` directory.
In order for the script to work, you need to set the correct environment variables in the `.env` file.
To configure the environment variables, copy the `.env.example` file to `.env` and modify the values as needed.
If `dev/configuration/plugins.py` is missing, copy it from `dev/configuration/plugins.py.example`.
The dev script will also copy available `*.env.example` and `plugins.py.example` files automatically on first run.

```bash
./dev/start-local-env.sh                       # start services in background
./dev/start-local-env.sh --recreate            # recreate containers
./dev/start-local-env.sh --stop                # stop 
./dev/start-local-env.sh --down                # stop and remove services
./dev/start-local-env.sh --down --volumes      # stop and remove services AND named volumes
./dev/start-local-env.sh --recreate --volumes  # full reset: down -v, then up (fresh volumes)
./dev/start-local-env.sh --clean               # remove local images + local env/toml/plugins.py
```

After startup, the API token is printed. This information is needed for the [configuration of the NetBox plugin](#configure-plugins). You can retrieve the NetBox API token any time from the setup container logs:

```bash
docker compose -f dev/docker-compose.yml logs netbox-setup
```

### Setup with External Asset Sources

In case you would like to use your own installations of NetBox and ISDuBA or other sources, you can use the following docker-compose files to setup the dependencies for the synchronizers and the matcher:

```shell
docker compose -f dev/docker-compose-silab.yml up -d
```

You will need to obtain the necessary credentials and configuration parameters from the services you have installed and configure them according to the [Configure Plugins](#configure-plugins) section.

## Configuration

Before starting the services, make sure to configure the plugins and the APIs according to the instructions below.

### Configure Plugins

To configure the Netbox fetcher plugin, copy the file [`assets/plugin_configs/data_source/asset/sample/netbox.toml`](assets/plugin_configs/data_source/asset/sample/netbox.toml) to `assets/plugin_configs/data_source/asset/netbox_local.toml` and adjust the values to your environment.
The file can be named any way you like, but it must be a toml file.

```shell
cp assets/plugin_configs/data_source/asset/sample/netbox.toml assets/plugin_configs/data_source/asset/netbox_local.toml
```

To configure the ISDuBA fetcher plugin, copy the file [`assets/plugin_configs/data_source/csaf/sample/isduba.toml`](assets/plugin_configs/data_source/csaf/sample/isduba.toml) to `assets/plugin_configs/data_source/csaf/isduba_local.toml` and adjust the values to your environment.
The file can be named any way you like, but it must be a toml file.

```shell
cp assets/plugin_configs/data_source/csaf/sample/isduba.toml assets/plugin_configs/data_source/csaf/isduba_local.toml
```

Before starting the synchronizers, make sure to create some assets and CSAF documents in the NetBox and ISDuBA instances.
Follow the corresponding instructions in the [NetBox](https://netboxlabs.com/docs/netbox/) and [ISDuBA documentation](https://github.com/ISDuBA/ISDuBA/blob/main/docs/README.md).

Next, install the python dependencies with uv by running in your terminal or inside pycharm (double tap `<Ctrl>` and enter the command) to set up the local python environment:

```shell
uv sync --all-extras
```

This will install all the available plugins in the `plugins/` directory in addition to the base package.
If you want to install only the base package, just run `uv sync`.
The plugins can be installed with `uv sync --extra <PLUGIN_NAME>` later on.
To install multiple extras, provide multiple `--extra` arguments.

### Configure APIs

This project provides three long-running components: two synchronizers and the matcher. All components read a shared TOML
configuration file from `assets/config.toml` and expose their respective HTTP APIs.

- Asset Synchronizer (assetsync)
  - Default API: <http://0.0.0.0:8992>
- CSAF Synchronizer (csafsync)
  - Default API: <http://0.0.0.0:8991>
- Matcher
  - Default API: <http://0.0.0.0:8998>

You can change host and port for each service in the `assets/config.toml` config under the respective `[..Api]` section.
The API documentation can be found at `http://<host:port>/docs`.

#### Configuration (assets/config.toml)

The `assets/config.toml` file contains configuration for all three components:

```toml
[Cachedb]
host = "localhost"
port = 2345
database = "cachedb"
username = "admin"
password = "secret"

[Matcher]
# Seconds between matching runs (mutually exclusive with fixed_time_of_day)
sync_interval = 86400
# OR: Run at a fixed time of day (mutually exclusive with sync_interval)
# fixed_time_of_day = "02:30"  # Format: "HH:MM" in 24-hour format
# Maximum duration in seconds for a matching run (optional)
# max_duration = 3600  # Stop matching after 1 hour
# Threshold for showing matches
match_threshold = 0
# Path to asset data source plugin configs used for the assetsync
asset_plugins_path = "./assets/plugin_configs/data_source/asset"
# Path to CSAF data source plugin configs used for the csafsync
csaf_plugins_path = "./assets/plugin_configs/data_source/csaf"

[Matcher.Api]
host = "0.0.0.0"
port = 8998

[Assetsync]
# Assetsync specific configuration

[Assetsync.Synchronizer]
# Seconds between sync runs (mutually exclusive with fixed_time_of_day)
sync_interval = 86400
# OR: Run at a fixed time of day (mutually exclusive with sync_interval)
# fixed_time_of_day = "03:00"  # Format: "HH:MM" in 24-hour format
plugin_configs_path = "./assets/plugin_configs/data_source/asset/"
# When false, do not trigger the matcher after a successful sync batch is stored
# This is true by default.
# trigger_matcher_on_sync = false
cleanup_grace_period = 86400
cleanup_interval = 60
preprocessor_plugins = ["identity", "default"]

[Assetsync.Api]
host = "0.0.0.0"
port = 8992

[Csafsync]
# Csaf specific configuration

[Csafsync.Synchronizer]
# Seconds between sync runs (mutually exclusive with fixed_time_of_day)
sync_interval = 86400
# OR: Run at a fixed time of day (mutually exclusive with sync_interval)
# fixed_time_of_day = "03:00"  # Format: "HH:MM" in 24-hour format
plugin_configs_path = "./assets/plugin_configs/data_source/csaf"
# When false, do not trigger the matcher after a successful sync batch is stored
# This is true by default.
# trigger_matcher_on_sync = false
cleanup_grace_period = 86400
cleanup_interval = 60
preprocessor_plugins = ["identity", "default"]

[Csafsync.Api]
host = "0.0.0.0"
port = 8991
```

#### Scheduling Configuration

Both the Matcher and Synchronizers support two mutually exclusive scheduling modes:

**Interval-based scheduling** (default):
- `sync_interval`: Time in seconds between runs. For example, `86400` runs every 24 hours after the previous run completes.

**Fixed time of day scheduling**:
- `fixed_time_of_day`: Run once per day at a specific time in 24-hour format (e.g., `"02:30"` for 2:30 AM).

**Important**: For the Matcher, you must specify at most one of these options. If you omit both,
matching only runs when triggered manually. Synchronizers still require exactly one scheduling option.

#### Configuration Options

- `Matcher.sync_interval` or `Matcher.fixed_time_of_day`: When to run matching cycles (omit both for manual-only).
- `Matcher.max_duration`: (Optional) Maximum duration in seconds for a matching run. If set, the matching process will gracefully stop after this duration, preserving all matches found up to that point. Useful for preventing excessively long matching runs.
- `Matcher.match_threshold`: Value for showing possible matches
- `Matcher.asset_plugins_path`: Path to the directory containing asset-specific plugin configuration files.
- `Matcher.csaf_plugins_path`: Path to the directory containing CSAF-specific plugin configuration files.
- `Matcher.Api.host/port`: Address where the Matcher FastAPI server listens.
- `Assetsync.Synchronizer.Api.host/port`: Address where the Asset Synchronizer FastAPI server listens.
- `Csafsync.Synchronizer.Api.host/port`: Address where the CSAF Synchronizer FastAPI server listens.
- `Cachedb`: Connection to the shared cache DB used by all components.

Both synchronizers share the following configuration (Assetsync.Synchronizer and Csafsync.Synchronizer):

- `.Synchronizer.sync_interval` or `.Synchronizer.fixed_time_of_day`: When to run fetch cycles.
- `.Synchronizer.trigger_matcher_on_sync`: When false, do not trigger a matcher run after synchronization.
- `.Synchronizer.preprocessor_plugins`: List and order of preprocessing plugins.
- `.Synchronizer.plugin_configs_path`: Path to the directory containing plugin configuration files.
- `.Synchronizer.cleanup_grace_period`: Time in seconds from the last synchronization after which assets are considered stale and will be deleted.
- `.Api.host/port`: Address for the synchronizer API.

The configuration for the plugins is located in the `assets/plugin_configs` directory.

#### Netbox CSAF Plugin configuration

The Netbox CSAF plugin needs to authenticate with the Matcher API.
Follow the instructions in the [Netbox CSAF Plugin README](https://github.com/DINA-community/CSAF-Netbox-Plugin).

When using the local setup, the plugin config is located at `\dev\configuration\plugins.py`.

## Authenticate with the API

The synchronizer components (Asset/CSAF) and the Matcher expose a small FastAPI HTTP API that uses OAuth2 Password flow to issue short‑lived JWT bearer tokens.

Quick start:

1) Make sure the component is running (e.g., Matcher default at <http://localhost:8998/>; configurable in `assets/matcher.toml`) after executing the setup and configuration.
2) Create or update a user in the CacheDB using the CLI:

```bash
uv run csaf_matcher_cli user create -u admin
```

**Note**: For interactive use, do not pass passwords via `-p/--password`. The CLI will securely prompt
for the password. Reserve `-p` only for non-interactive environments (e.g., CI) and source secrets
from a secure provider.

For a detailed guide (including HTTP and Python examples, troubleshooting, and security notes), see:

- docs/authentication.rst
- docs/matcher-cli.rst

### Running Applications

Your development environment is now ready to use. If using the fully local environment, the NetBox and ISDuBA services will be available at:

- NetBox UI: <http://netbox.localhost/> (default: admin / admin)
- ISDuBA UI: <http://isduba.localhost/> (default: user / user)

Targets can be run by typing `uv run <TARGET_NAME>` or by selecting it in the run configurations menu in Pycharm.

To run the Matching Agent:

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

### Running Tests

Tests can be executed using uv as well. All test targets are defined in the pyproject.toml, so you can run them with:

```shell
uv run pytest -v -s
```

To run a single test file:

```shell
uv run pytest -v  -s tests/matcher/test_matching.py
```

## Production Docker Setup

This repository ships a simple production‑ready Docker setup that runs the three services (assetsync, csafsync, matcher) with a shared PostgreSQL database and exposes all three APIs over HTTPS via an NGINX reverse proxy.

The core services themselves do not implement native TLS listeners. Without a reverse proxy, there is no TLS support for external traffic. This separation is intentional and follows common industry practice (TLS termination at the edge proxy, application services kept lean).

For instructions on how to set up the environment, see the corresponding section in the docs.
For professional deployments, use the SSL/TLS guidance in the production docs (trusted certificates, reverse proxy hardening, and NGINX example configuration).
The docs are built with `make docs` and can be found in the `docs/_build/html/production-setup.html` directory.

> Note Under development see [Issue #9](https://github.com/DINA-community/Matching-Agent/issues/9)

## Contributing

If you want to contribute to the project, please read the [Contributing Guide](CONTRIBUTING.md).
