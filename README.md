# Matching-Agent

This repository contains a shared infrastructure for synchronizer daemons that fetch, transform, and store data in a
PostgreSQL database as well as a csaf-asset matching daemon.
It includes two concrete implementations:

1. **Asset Synchronizer (`assetsync`)**: Fetches and processes asset data.
2. **CSAF Synchronizer (`csafsync`)**: Fetches and processes CSAF (Common Security Advisory Framework) data.

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

Install the dependencies with uv by running in your terminal or inside pycharm (double tap `<Ctrl>` and enter the command)

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


### Running the application
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
