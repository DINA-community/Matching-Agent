# Contributing

Before you contribute to this project, make sure to set up the git pre-commit hooks as described below.

## Setting up git pre-commit hooks

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

## Check for warnings

In order to check for warning due to NetBox updates like in issue [#54](https://github.com/DINA-community/CSAF-Netbox-Plugin/issues/54)

```shell
docker exec -it dev-netbox-1 /opt/netbox/venv/bin/python -W default /opt/netbox/netbox/manage.py check
```
