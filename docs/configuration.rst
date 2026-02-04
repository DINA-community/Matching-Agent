.. _configuration:

Configuration
=============

.. include:: _includes/section-toc.rstinc

This section describes all configuration files used by the Matching Agent components and their plugins.
All components (Asset Synchronizer, CSAF Synchronizer, and Matcher) share the main service configuration file
``assets/config.toml`` (or ``docker/assets/config.toml`` in container images), but additional files and
environment variables are also used.

.. _config-assetsync:

Asset Synchronizer Configuration (assets/config.toml)
--------------------------------
The Asset Synchronizer (assetsync) fetches asset/product data from configured data sources and stores
them in the cache database. It uses the ``[Assetsync]`` section in ``assets/config.toml``.

.. code-block:: toml

   [Cachedb]
   host = "localhost"
   port = 2345
   database = "cachedb"
   username = "admin"
   password = "secret"

   [Assetsync.Synchronizer]
   sync_interval = 3600
   plugin_configs_path = "./assets/plugin_configs/data_source/asset"
   preprocessor_plugins = ["identity"]
   cleanup_interval = 86400
   cleanup_grace_period = 604800

   [Assetsync.Api]
   host = "0.0.0.0"
   port = 8992
   access_token_expire_minutes = 10

Parameters
~~~~~~~~~~

- ``[Assetsync.Synchronizer]`` section:

  - ``sync_interval`` (int, required): Interval in seconds between synchronization runs. Assets are fetched
    from all configured data sources at this frequency.
  - ``plugin_configs_path`` (str path, required): Directory containing asset data source plugin
    configuration files (e.g., ``netbox.toml``).
  - ``preprocessor_plugins`` (list[str], required): List of preprocessor plugin names to apply transformations
    to fetched data before storage. Use ``["identity"]`` if no transformations are needed.
  - ``cleanup_interval`` (int, required): Interval in seconds between cleanup runs that remove stale data.
  - ``cleanup_grace_period`` (int, required): Grace period in seconds before deleting assets that are no longer
    present in the source.

- ``[Assetsync.Api]`` section:

  - ``host`` (str, required): Hostname/IP address the HTTP API server binds to. Use "0.0.0.0" to listen on all interfaces.
  - ``port`` (int, required): TCP port for the HTTP API server.
  - ``access_token_expire_minutes`` (int, required): Access token lifetime for the API (minutes).

- ``[Cachedb]`` section:

  - ``host`` (str, required): PostgreSQL database hostname.
  - ``port`` (int, required): PostgreSQL database port.
  - ``database`` (str, required): Name of the database to use.
  - ``username`` (str, required): Database user for authentication.
  - ``password`` (str, required): Database password for authentication.

- ``[Assetsync.Logging]`` section (optional):

  - ``level`` (str, optional): File log level. Accepted: "TRACE", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL".
  - ``file`` (str path, required if section present): Log file path. If omitted, file logging is disabled.
  - ``max_bytes`` (int, optional): Rotate when the file exceeds this many bytes. Default 10,000,000.
  - ``backup_count`` (int, optional): How many rotated files to keep. Default 5.


.. _config-csafsync:

CSAF Synchronizer Configuration (assets/config.toml)
--------------------------------
The CSAF Synchronizer (csafsync) fetches CSAF security advisories from configured data sources and
stores them in the cache database. It uses the ``[Csafsync]`` section in ``assets/config.toml``.

.. code-block:: toml

   [Csafsync.Synchronizer]
   sync_interval = 3600
   plugin_configs_path = "./assets/plugin_configs/data_source/csaf"
   preprocessor_plugins = []
   cleanup_interval = 86400
   cleanup_grace_period = 604800

   [Csafsync.Api]
   host = "0.0.0.0"
   port = 8991
   access_token_expire_minutes = 10

Parameters
~~~~~~~~~~

The parameters are identical to the Asset Synchronizer configuration (see above), except they are located under the ``[Csafsync]`` prefix:

- ``plugin_configs_path`` points to CSAF data source configurations instead of asset sources.
- ``port`` defaults to 8991 for the CSAF sync API.

``[Csafsync.Logging]`` is optional and uses the same fields as ``[Assetsync.Logging]``.


.. _config-matcher:

Matcher Configuration (assets/config.toml)
---------------------
The Matcher service periodically matches assets against CSAF advisories to identify vulnerabilities.
It uses the ``[Matcher]`` section in ``assets/config.toml``.

.. code-block:: toml

   [Matcher]
   sync_interval = 60
   match_threshold = 0
   asset_plugins_path = "./assets/plugin_configs/data_source/asset"
   csaf_plugins_path = "./assets/plugin_configs/data_source/csaf"

   [Matcher.Api]
   host = "0.0.0.0"
   port = 8998
   access_token_expire_minutes = 10

Parameters
~~~~~~~~~~

- ``[Matcher]`` section:

  - ``sync_interval`` (int, required): Interval in seconds between matching runs. The matcher queries the
    cache database for assets and CSAF documents and performs matching at this frequency.
  - ``match_threshold`` (float, required): Minimum score to keep a match (0 keeps all matches).
  - ``asset_plugins_path`` (str path, required): Directory containing asset data source plugin
    configurations. Used to determine which asset sources are active.
  - ``csaf_plugins_path`` (str path, required): Directory containing CSAF data source plugin
    configurations. Used to determine which CSAF sources are active.

- ``[Matcher.Api]`` section:

  - ``host`` (str, required): Hostname/IP address the HTTP API server binds to. Use "0.0.0.0" to listen on all interfaces.
  - ``port`` (int, required): TCP port for the HTTP API server.
  - ``access_token_expire_minutes`` (int, required): Access token lifetime for the API (minutes).

- ``[Matcher.Logging]`` section (optional):

  - ``level`` (str, optional): File log level. Accepted: "TRACE", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL".
  - ``file`` (str path, required if section present): Log file path. If omitted, file logging is disabled.
  - ``max_bytes`` (int, optional): Rotate when the file exceeds this many bytes. Default 10,000,000.
  - ``backup_count`` (int, optional): How many rotated files to keep. Default 5.


Plugin Configuration Files (assets/plugin_configs/**)
-----------------------------------------------------
Data source and preprocessor plugins have their own configuration files. Each data source config file
is a TOML document with a top-level ``[DataSource]`` section and a ``[DataSource.Plugin]`` section.
Container images include a copy under ``docker/assets/plugin_configs`` with the same structure.

Common data source flags (required unless noted):

- ``DataSource.plugin_name`` (str, required): Plugin entry point name. Must match the installed plugin.
- ``DataSource.publish_matches`` (bool, optional): Whether to send match results back to the source.
  Default is ``false``.
- ``DataSource.Plugin`` (table, required): Plugin-specific settings.

Netbox data source (``assets/plugin_configs/data_source/asset/*.toml``):

- ``DataSource.Plugin.api_url`` (str URL, required): Base URL of the Netbox API.
- ``DataSource.Plugin.api_token`` (str, required): API token for Netbox.

ISDuBA data source (``assets/plugin_configs/data_source/csaf/*.toml``):

- ``DataSource.Plugin.url`` (str URL, required): Base URL of the ISDuBA API.
- ``DataSource.Plugin.keycloak_url`` (str URL, required): Keycloak base URL.
- ``DataSource.Plugin.keycloak_realm`` (str, required): Keycloak realm.
- ``DataSource.Plugin.username`` (str, required): Keycloak username.
- ``DataSource.Plugin.password`` (str, required): Keycloak password.
- ``DataSource.Plugin.verify_ssl`` (bool, required): Whether to verify TLS certificates.


Container Environment Configuration (docker/.env.example)
---------------------------------------------------------
These environment variables are consumed by ``docker/docker-compose.yml`` and the service containers.

- ``POSTGRES_DB`` (str, required): Database name.
- ``POSTGRES_USER`` (str, required): Database user.
- ``POSTGRES_PASSWORD`` (str, required): Database password.
- ``POSTGRES_PORT`` (int, required): Database port on the host.
- ``HTTPS_PORT`` (int, required): Public TLS port for the gateway.
- ``TLS_CN`` (str, required): Common Name for the self-signed certificate.
- ``MATCHER_LOG_LEVEL`` (str, optional): Console log level for matcher (overrides default).
- ``ASSETSYNC_LOG_LEVEL`` (str, optional): Console log level for assetsync (overrides default).
- ``CSAFSYNC_LOG_LEVEL`` (str, optional): Console log level for csafsync (overrides default).


Local Environment Configuration (.env)
--------------------------------------
The services load environment variables from a local ``.env`` if present.

- ``JWT_SECRET_KEY`` (str, required): Secret key for signing access tokens.
- ``LOG_LEVEL`` (str, optional): Console log level for all services (default "INFO").


Development Environment Configuration (dev/.env.example)
--------------------------------------------------------
These variables are used by the development stack under ``dev/``. All are required.

- ``CACHEDB_POSTGRES_DB`` (str, required): CacheDB database name.
- ``CACHEDB_POSTGRES_USER`` (str, required): CacheDB database user.
- ``CACHEDB_POSTGRES_PASSWORD`` (str, required): CacheDB database password.
- ``KC_DB_USERNAME`` (str, required): Keycloak database user.
- ``KC_DB_PASSWORD`` (str, required): Keycloak database password.
- ``KC_BOOTSTRAP_ADMIN_USERNAME`` (str, required): Keycloak admin username.
- ``KC_BOOTSTRAP_ADMIN_PASSWORD`` (str, required): Keycloak admin password.
- ``KC_HOSTNAME`` (str, required): Keycloak base URL.
- ``ISDUBA_POSTGRES_PASSWORD`` (str, required): ISDuBA database password.
- ``ISDUBA_CLIENT_KEYCLOAK_URL`` (str, required): ISDuBA client Keycloak URL.
- ``ISDUBA_CLIENT_KEYCLOAK_REALM`` (str, required): ISDuBA client Keycloak realm.
- ``ISDUBA_CLIENT_KEYCLOAK_CLIENT_ID`` (str, required): ISDuBA client Keycloak client id.
- ``ISDUBA_CLIENT_IDLE_TIMEOUT`` (str, required): ISDuBA client idle timeout (e.g., ``"30m"``).
- ``ISDUBA_CLIENT_HOSTNAME_URL`` (str, required): ISDuBA client hostname URL.
- ``NETBOX_SUPERUSER_PASSWORD`` (str, required): Netbox superuser password.
- ``NETBOX_SUPERUSER_NAME`` (str, required): Netbox superuser username.
- ``NETBOX_SUPERUSER_EMAIL`` (str, required): Netbox superuser email.
- ``BUILD_VERSION`` (str, required): Build/version tag for dev images.

