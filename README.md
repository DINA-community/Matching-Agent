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

| Feature               | Status | Notes                                           |
|-----------------------|--------|:------------------------------------------------|
| Asset Synchronization | ✅ Done | Basic asset data syncing implemented            |
| CSAF Synchronization  | ✅ Done | CSAF advisory data syncing implemented          |
| Asset-CSAF Matching   | ✅ Done | A simple Matcher that matches everything is WIP |
| REST API              | 🚧 WIP | Groundwork has been done. Need to specify API   |
| Webhook Notifications | 🚧 WIP | Notification system being developed             |
| Plugin System         | ✅ Done | Extensible plugin architecture ready            |

## Project Structure

- `src/dina/synchronizer/`: Shared infrastructure for synchronizer daemons.
- `src/dina/assetsync/`: Asset Synchronizer implementation.
- `src/dina/csafsync/`: CSAF Synchronizer implementation.
- `src/dina/matcher/`: Main package.
- `plugins/`: Plugin implementations for extending functionality.

For more details about the synchronizer infrastructure, see the Synchronizer Infrastructure README. (TODO)

## Getting Started

### Installation on Ubuntu

Clone the repository.

```cd /home
git clone -b feat/initial_structure https://github.com/DINA-community/Matching-Agent.git
cd Matching-Agent
```

Install [uv](https://docs.astral.sh/uv/), docker and docker compose in any way that suits you.

### after installation

Create the development database:

```shell
docker compose -f dev/docker-compose.yml up -d
```

Install the dependencies with uv by running in your terminal or inside pycharm (double tap `<Ctrl>` and enter the
command)

```shell
uv sync --all-extras
```

to set up the local dev environment.

### Setting up git pre-commit hooks

Before commiting anything, make sure you have set up your git pre-commit hooks correctly.
To do so, simply run the following:

```shell
uv run pre-commit install
```

To manually run the pre-commit hooks (in case you want to check without commiting), run the following:

```shell
uv run pre-commit run --all-files
```

If you want to run the linter manually, run the following:

```shell
uv run ruff check
```

## Configuration and APIs

This project provides three long-running components: two synchronizers and the matcher. Each reads a TOML
configuration file from the assets/ directory and exposes a small HTTP API.

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
csaf_plugins_path = "./assets/plugin_configs/data_source/csaf/active"

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

### Asset Synchronizer configuration (assets/assetsync.toml)

Example (defaults in repo):

```
[Assetsync]
# Asset-specific options go here (plugin-specific)

[Synchronizer]
sync_interval = 60
preprocessor_plugins = ["identity"]
plugin_configs_path = "./assets/plugin_configs/data_source/asset/"

[Synchronizer.Api]
host = "0.0.0.0"
port = 8000

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
plugin_configs_path = "./assets/plugin_configs/data_source/csaf/active/"

[Synchronizer.Api]
host = "0.0.0.0"
port = 8001

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
