.. _configuration:

Configuration
=============

.. include:: _includes/section-toc.rstinc

This section describes the service configuration files used by the Matching Agent components.
You can reference these details from both the getting started guide and the production setup guide.


.. _config-assetsync:

Asset Synchronizer Configuration
--------------------------------
The Asset Synchronizer (assetsync) fetches asset/product data from configured data sources and stores
them in the cache database. Configuration file: ``assets/assetsync.toml``

.. code-block:: toml

   [Synchronizer]
   sync_interval = 3600
   plugin_configs_path = "./assets/plugin_configs/data_source/asset"
   preprocessor_plugins = ["identity"]
   cleanup_interval = 86400
   cleanup_grace_period = 604800

   [Synchronizer.Api]
   host = "0.0.0.0"
   port = 8992

   [Cachedb]
   host = "localhost"
   port = 2345
   database = "cachedb"
   username = "admin"
   password = "secret"

Parameters
~~~~~~~~~~

- ``[Synchronizer]`` section:

  - ``sync_interval`` (int): Interval in seconds between synchronization runs. Assets are fetched
    from all configured data sources at this frequency.
  - ``plugin_configs_path`` (str): Path to the directory containing asset data source plugin
    configuration files (e.g., ``netbox.toml``).
  - ``preprocessor_plugins`` (list): List of preprocessor plugin names to apply transformations
    to fetched data before storage. At least one plugin is required. If no transformations are
    needed, use the "identity" plugin.
  - ``cleanup_interval`` (int): Interval in seconds between cleanup runs that remove stale data.
    Default: 86400 (24 hours).
  - ``cleanup_grace_period`` (int): Grace period in seconds before deleting assets that are no longer
    present in the source. Default: 604800 (7 days).

- ``[Synchronizer.Api]`` section:

  - ``host`` (str): Hostname/IP address the HTTP API server binds to. Use "0.0.0.0" to listen on all interfaces.
  - ``port`` (int): TCP port for the HTTP API server.

- ``[Cachedb]`` section:

  - ``host`` (str): PostgreSQL database hostname.
  - ``port`` (str|int): PostgreSQL database port.
  - ``database`` (str): Name of the database to use.
  - ``username`` (str): Database user for authentication.
  - ``password`` (str): Database password for authentication.


.. _config-csafsync:

CSAF Synchronizer Configuration
--------------------------------
The CSAF Synchronizer (csafsync) fetches CSAF security advisories from configured data sources and
stores them in the cache database. Configuration file: ``assets/csafsync.toml``

.. code-block:: toml

   [Synchronizer]
   sync_interval = 3600
   plugin_configs_path = "./assets/plugin_configs/data_source/csaf"
   preprocessor_plugins = []
   cleanup_interval = 86400
   cleanup_grace_period = 604800

   [Synchronizer.Api]
   host = "0.0.0.0"
   port = 8991

   [Cachedb]
   host = "localhost"
   port = 2345
   database = "cachedb"
   username = "admin"
   password = "secret"

Parameters
~~~~~~~~~~

The parameters are identical to the Asset Synchronizer configuration (see above), except:

- ``plugin_configs_path`` points to CSAF data source configurations instead of asset sources.
- ``port`` defaults to 8991 for the CSAF sync API.


.. _config-matcher:

Matcher Configuration
---------------------
The Matcher service periodically matches assets against CSAF advisories to identify vulnerabilities.
Configuration file: ``assets/matcher.toml``

.. code-block:: toml

   [Matcher]
   sync_interval = 60
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

Parameters
~~~~~~~~~~

- ``[Matcher]`` section:

  - ``sync_interval`` (int): Interval in seconds between matching runs. The matcher queries the
    cache database for assets and CSAF documents and performs matching at this frequency.
  - ``asset_plugins_path`` (str): Path to the directory containing asset data source plugin
    configurations. Used to determine which asset sources are active.
  - ``csaf_plugins_path`` (str): Path to the directory containing CSAF data source plugin
    configurations. Used to determine which CSAF sources are active.

- ``[Matcher.Api]`` section:

  - ``host`` (str): Hostname/IP address the HTTP API server binds to. Use "0.0.0.0" to listen on all interfaces.
  - ``port`` (int): TCP port for the HTTP API server.

- ``[Matcher.Cachedb]`` section:

  - ``host`` (str): PostgreSQL database hostname.
  - ``port`` (int): PostgreSQL database port.
  - ``database`` (str): Name of the database to use.
  - ``username`` (str): Database user for authentication.
  - ``password`` (str): Database password for authentication.
