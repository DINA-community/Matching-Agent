# ISDuBA Data Source Plugin

This plugin integrates the Matching-Agent with an ISDuBA instance to fetch vulnerability advisory/product-tree information via the ISDuBA REST API.


## Prerequisites

- Python version compatible with the Matching-Agent (see project root README / pyproject.toml)
- A reachable ISDuBA deployment
- Credentials for ISDuBA (username/password)
- Matching-Agent core application installed and runnable

## Installation
For development environments, follow the procedure for the main project README.
If installing from pypi, simply provide the `extra` name `datasource-isduba` associated with this plugin.

## Configuration

Add a DataSource section for ISDuBA to your plugin configuration TOML.
An example is provided at assets/plugin_configs/asset_source/isduba/active/isduba.toml.

Example:

```toml
[DataSource]
plugin_name = "isduba_fetcher"

[DataSource.ISDuBA]
url = "https://your-isduba-host"
username = "your-username"
password = "your-password"
verify_ssl = false
```

Configuration keys:
- DataSource.plugin_name: Must be set to "isduba_fetcher" to load this plugin.
- DataSource.ISDuBA.url: Base URL of your ISDuBA instance (scheme + host). The plugin will call both <url>:8081 for token and <url>/api for API.
- DataSource.ISDuBA.username: Username for password grant.
- DataSource.ISDuBA.password: Password for password grant.
- DataSource.ISDuBA.verify_ssl: Boolean. If false, SSL certificate verification is disabled for outbound requests (useful for lab/testing with self-signed certs). Prefer true in production.

