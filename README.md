# Matching-Agent

This repository contains a shared infrastructure for manager daemons that fetch, transform, and store data in a
PostgreSQL database. It includes two concrete implementations:

1. **Asset Manager (`assetman`)**: Fetches and processes asset data.
2. **CSAF Manager (`csafman`)**: Fetches and processes CSAF (Common Security Advisory Framework) data.

## Project Structure

- `src/manager/`: Shared infrastructure for manager daemons.
- `src/assetman/`: Asset Manager implementation.
- `src/csafman/`: CSAF Manager implementation.
- `src/matcher/`: Main package.
- `plugins/`: Plugin implementations for extending functionality.

For more details about the manager infrastructure, see
the [Manager Infrastructure README](src/csaf_matcher/manager/README.md).

## Getting Started

Install [uv](https://docs.astral.sh/uv/) in any way that suits you.

Run in your terminal or inside pycharm (double tap `<Ctrl>` and enter the command)

```shell
uv sync --all-extras
```

to set up the local dev environment.

Afterwards any target can be run by typing `uv run <TARGET_NAME>` or by selecting it in the run configurations menu
in Pycharm.
For example, try running the following to start the matching agent.

```shell
uv run matcher
```

To run the Asset Manager:

```shell
uv run assetman
```

To run the CSAF Manager:

```shell
uv run csafman
```

### Setting up git pre-commit hooks

Before commiting anything, make sure you have set up your git pre-commit hooks correctly.
To do so, simply run the following:

```shell
uv run pre-commit install
```
