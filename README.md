# Matching-Agent

This repository contains a shared infrastructure for manager daemons that fetch, transform, and store data in a PostgreSQL database. It includes two concrete implementations:

1. **Asset Manager (`assetman`)**: Fetches and processes asset data.
2. **CSAF Manager (`csafman`)**: Fetches and processes CSAF (Common Security Advisory Framework) data.

## Project Structure

- `src/manager/`: Shared infrastructure for manager daemons.
- `src/assetman/`: Asset Manager implementation.
- `src/csafman/`: CSAF Manager implementation.
- `src/matcher/`: Main package.

For more details about the manager infrastructure, see the [Manager Infrastructure README](src/manager/README.md).

## Getting Started
Install [uv](https://docs.astral.sh/uv/) in any way that suits you.
If you are using PyCharm, then you should not need to do anything further.

If you are not using PyCharm, run 
```shell
uv sync
```
to set up the local dev environment.

Afterwards any target can be run by typing `uv run <TARGET_NAME>`.
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
