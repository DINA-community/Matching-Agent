# Matching-Agent

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

### Setting up git pre-commit hooks
Before commiting anything, make sure you have set up your git pre-commit hooks correctly.
To do so, simply run the following:
```shell
uv run pre-commit install
```