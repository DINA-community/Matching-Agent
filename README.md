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
- Sphinx (for docs)

You can either build the docs with `uv run make docs` and follow the instructions there or proceed with the instructions below.

The following steps are intended for setting up a development environment on Ubuntu.
For other distributions or operating systems, you may need to adjust the instructions accordingly.

First, clone the repository:

```shell
git clone -b feat/initial_structure --recurse-submodules https://github.com/DINA-community/Matching-Agent.git
cd Matching-Agent
uv sync --extra isduba_fetcher # If you plan to use the ISDuBA CSAF source (default plugin name `isduba_fetcher`)
```

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

You can start, stop, and recreate the full local development stack (PostgreSQL, NetBox, ISDuBA, etc.) using the helper script in the `dev/` directory:

```bash
./dev/start-local-env.sh                       # start services in background
./dev/start-local-env.sh --recreate            # recreate containers
./dev/start-local-env.sh --down                # stop and remove services
./dev/start-local-env.sh --down --volumes      # stop and remove services AND named volumes
./dev/start-local-env.sh --recreate --volumes  # full reset: down -v, then up (fresh volumes)
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
vim assets/plugin_configs/data_source/asset/netbox_local.toml
```

To configure the ISDuBA fetcher plugin, copy the file [`assets/plugin_configs/data_source/csaf/sample/isduba.toml`](assets/plugin_configs/data_source/csaf/sample/isduba.toml) to `assets/plugin_configs/data_source/csaf/isduba_local.toml` and adjust the values to your environment.
The file can be named any way you like, but it must be a toml file.

Before starting the synchronizers, make sure to create some assets and CSAF documents in the NetBox and ISDuBA instances.
Follow the corresponding instructions in the [NetBox](https://netboxlabs.com/docs/netbox/) and [ISDuBA documentation](https://github.com/ISDuBA/ISDuBA/blob/main/docs/README.md).

```shell
cp assets/plugin_configs/data_source/csaf/sample/isduba.toml assets/plugin_configs/data_source/csaf/isduba_local.toml
vim assets/plugin_configs/data_source/csaf/isduba_local.toml
```

Next, install the python dependencies with uv by running in your terminal or inside pycharm (double tap `<Ctrl>` and enter the command) to set up the local python environment:

```shell
uv sync --all-extras
```

This will install all the available plugins in the `plugins/` directory in addition to the base package.
If you want to install only the base package, just run `uv sync`.
The plugins can be installed with `uv sync --extra <PLUGIN_NAME>` later on.
To install multiple extras, provide multiple `--extra` arguments.

### Configure APIs

This project provides three long-running components: two synchronizers and the matcher. Each reads a TOML
configuration file from the `assets/` directory and exposes a small HTTP API.

- Asset Synchronizer (assetsync)
  - Config file: assets/assetsync.toml
  - Default API: <http://0.0.0.0:8992>
- CSAF Synchronizer (csafsync)
  - Config file: assets/csafsync.toml
  - Default API: <http://0.0.0.0:8991>
- Matcher
  - Config file: assets/matcher.toml
  - Default API: <http://0.0.0.0:8998>

You can change host and port for each service in the respective config under the [..Api] section.
The API documentation can be found at `http://<host:port>/docs`.

#### Matcher configuration (assets/matcher.toml)

Minimal example (defaults in repo):

```toml
[Matcher]
sync_interval = 60  # seconds between matching runs
match_threshold = 0
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

- `Matcher.sync_interval`: Minimal delay between matching cycles.
- `Matcher.match_threshold`: Value for showing possible matches
- `Matcher.asset_plugins_path`: Path to the directory containing asset-specific plugin configuration files.
- `Matcher.csaf_plugins_path`: Path to the directory containing CSAF-specific plugin configuration files.
- `Matcher.Api.host/port`: Address where the FastAPI server listens.
- `Matcher.Cachedb`: Connection to the shared cache DB used by all components.

#### Asset Synchronizer configuration (assets/assetsync.toml)

Example (defaults in repo):

```toml
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

- `Synchronizer.sync_interval`: Minimal delay between fetch cycles.
- `Synchronizer.preprocessor_plugins`: List and order of preprocessing plugins.
- `Synchronizer.plugin_configs_path`: Path to the directory containing plugin configuration files.
- `Synchronizer.cleanup_grace_period`: Time in seconds from the last synchronization after which assets are considered stale and will be deleted.
- `Synchronizer.Api.host/port`: Address for the synchronizer API.
- `Cachedb`: Connection to the shared cache DB.
- `Data source plugins`: Configuration TOML files are loaded from assets/plugin_configs/asset_source/…

#### CSAF Synchronizer configuration (assets/csafsync.toml)

Example (defaults in repo):

```toml
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

This repository ships a simple production‑ready Docker setup that runs the three services (assetsync, csafsync, matcher) with a shared PostgreSQL database and exposes all three APIs over HTTPS using a self‑signed certificate.

For instructions on how to set up the environment, see the corresponding section in the docs.
The docs are built with `make docs` and can be found in the `docs/_build/html/production-setup.html` directory.

> Note Under development see [Issue #9](https://github.com/DINA-community/Matching-Agent/issues/9)

## Contributing

If you want to contribute to the project, please read the [Contributing Guide](CONTRIBUTING.md).
