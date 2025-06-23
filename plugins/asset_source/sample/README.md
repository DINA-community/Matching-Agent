# Sample Plugin Documentation

This document provides a guide on how to implement and register a new plugin for the DINA Matching Agent.

## Plugin Structure

A DINA data source plugin consists of the following mandatory components:

1. **Plugin Class**: A Python class that inherits from `DataSourcePlugin` and implements the required methods.
2. **Entry Point Registration**: Configuration in `pyproject.toml` that registers the plugin with the system.
3. **Configuration File**: One or more TOML files that configure the plugin instances' behavior.

## Implementing a Plugin

### 1. Create a New Plugin Package

If developing a plugin in the main matcher repository, navigate to the `plugins/asset_source` directory.

Create a new project by typing `uv init --package your_plugin_name`.

Adjust the structure of the new package to the following if necessary:

```
your_plugin_name/
├── README.md
├── pyproject.toml
└── src/
    └── dina/
        └── plugins/
            └── datasource/
                └── your_plugin_name/
                    ├── __init__.py
                    ├── your_plugin_name.py
                    └── py.typed
```

### 2. Implement the Plugin Class

Create a class that inherits from `DataSourcePlugin` and implements the required methods:

```python
import asyncio
from typing import List, Union

from dina.cachedb.model import CsafDocument, Asset
from dina.manager.plugin_base.data_source import DataSourcePlugin


class YourPluginDataSource(DataSourcePlugin):
    def __init__(self, config):
        super().__init__(config)
        # Extract configuration values
        try:
            plugin_config = self.config["DataSource"]["YourPluginSection"]
            self.some_param = plugin_config["some_param"]
            # Add other configuration parameters as needed
        except KeyError:
            raise KeyError("Missing required configuration parameter")

    def endpoint_info(self) -> str:
        """Return information about the data source endpoint."""
        return "https://your-data-source-endpoint.com/"

    async def fetch_data(self) -> List[Union[Asset, CsafDocument]]:
        """Fetch data from the data source and return it as a list of Assets or CsafDocuments."""
        # Implement your data fetching logic here
        # This is where you would connect to your data source and retrieve data

        # Example: Simulate fetching data with a delay
        await asyncio.sleep(1)

        # Return a list of Asset or CsafDocument objects
        return [Asset()]
```

Required methods:

- `__init__(self, config)`: Initialize the plugin with the provided configuration.
- `endpoint_info(self) -> str`: Return a string with information about the data source endpoint.
- `fetch_data(self) -> List[Union[Asset, CsafDocument]]`: Asynchronously fetch data from the data source.

### 3. Configure the pyproject.toml

Create a `pyproject.toml` file with the following content:

```toml
[project]
# The name must match `dina.plugins.datasource.<plugin_name>`
name = "dina.plugins.datasource.your_plugin_name"
version = "0.1.0"
description = "Your plugin description"
readme = "README.md"
authors = [
    { name = "Your Name", email = "your.email@example.com" }
]
requires-python = ">=3.13"

# All data source plugins depend on the base matcher package
dependencies = [
    "dina.matcher",
    # Add any additional dependencies your plugin needs
]

[tool.hatch.build.targets.wheel]
packages = ["src/dina"]

# A datasource plugin must specify the correct DataSource class as an entry-point
[project.entry-points."dina.plugins.datasource"]
your_plugin_name = "dina.plugins.datasource.your_plugin_name.your_plugin_name:YourPluginDataSource"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.uv.sources]
"dina.matcher" = { workspace = true }
```

Important points:

- The package name must follow the pattern `dina.plugins.datasource.your_plugin_name`.
- The entry point name (`your_plugin_name`) must match the name used in the configuration file.
- The entry point value must point to your plugin class.

## Registering a Plugin instance

### 1. Build and Install the Plugin

When working in the main repository, add the plugin as an extra to the main package:

```shell
uv add --optional your_plugin_name --project=dina.plugins.datasource.your_plugin_name --editable plugins/asset_source/your_plugin_name
```

And then make sure all extras are installed for development purposes:

```bash
uv sync --all-extras
```

TODO: Describe process for external plugins.

### 2. Create a Configuration File

Create a TOML configuration file in the `assets/plugin_configs/` directory.
Each configuration file corresponds to one instance of a plugin.
This makes it possible to configure multiple instances of the same plugin to, for example,
connect to multiple instances of an asset or CSAF database.

```toml
[DataSource]
plugin_name = "your_plugin_name"
timeout_seconds = 30
update_interval = 60

# Add your plugin-specific configuration section
[DataSource.YourPluginSection]
some_param = "value"
# Add other parameters as needed
```

Required fields:

- `[DataSource]` section with:
    - `plugin_name`: Must match the entry point name in pyproject.toml
    - `timeout_seconds`: Timeout for data fetching operations
    - `update_interval`: How often to fetch data (in seconds)
- Plugin-specific section with any parameters your plugin needs

## Plugin Loading Process

When the DINA Matching Agent starts:

1. It scans the `assets/plugin_configs/` directory for TOML files.
2. For each file, it extracts the `plugin_name` from the `[DataSource]` section.
3. It looks for an entry point with that name in the `dina.plugins.datasource` group.
4. If found, it loads the plugin class and initializes it with the configuration.
5. The plugin's `fetch_data` method is called periodically to retrieve data.

## Example

The sample plugin in this directory provides a minimal example of a working plugin:

- `sample.py`: A simple plugin implementation
- `pyproject.toml`: Entry point registration
- Configuration file: `assets/plugin_configs/sample.toml`

You can use this as a starting point for your own plugin implementation.
