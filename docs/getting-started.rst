Developer Installation and Getting Started
==========================================

This guide helps you set up a local development environment for the Matching Agent project and run
its components. It assumes you will use uv for Python dependency management, as used in this repo.

Prerequisites
-------------
- uv (https://docs.astral.sh/uv/)
- Docker and Docker Compose (optional, for local services like NetBox/ISDuBA and PostgreSQL)
- Java Runtime Environment (JRE/JDK) required only when building/using the ISDuBA plugin (recommended: OpenJDK 17+)

Quick start
-----------
1) Clone the repository

   .. code-block:: bash

      git clone https://github.com/DINA-community/Matching-Agent.git
      cd Matching-Agent

2) Create the Python environment and install dependencies
    - Base package only:

    .. code-block:: bash

        uv sync

    - With all plugin extras in ``plugins/``:

    .. code-block:: bash

        uv sync --all-extras

    - With selected extras (repeat --extra for multiple):

    .. code-block:: bash

        uv sync --extra netbox_fetcher --extra isduba_fetcher --extra preprocessor-identity

    .. note::
       The ISDuBA CSAF source (``isduba_fetcher``) requires a Java runtime at build time. Ensure ``java`` is available on
       your system ``PATH`` (or set ``JAVA_HOME``) before running the above command. Without Java, installation of the
       ISDuBA plugin will fail.

3) Start local supporting services
    You can use the helper script (recommended) or run Docker Compose directly.

    - Recommended: use the dev helper script to start/stop/recreate the local stack

    .. code-block:: bash

        ./dev/start-local-env.sh                       # start services in background
        ./dev/start-local-env.sh --recreate            # recreate containers
        ./dev/start-local-env.sh --down                # stop and remove services
        ./dev/start-local-env.sh --down --volumes      # stop and remove services AND named volumes
        ./dev/start-local-env.sh --recreate --volumes  # full reset: down -v, then up

    - Alternative: run Docker Compose directly

    .. code-block:: bash

        # Use externally installed NetBox/ISDuBA and only start a local database
        docker compose -f dev/docker-compose-silab.yml up -d

        # Or run a fully local stack (NetBox, ISDuBA, DB)
        docker compose -f dev/docker-compose.yml up -d

    When using the fully local development environment, the URLs and default credentials are as follows:

    - NetBox UI: http://netbox.localhost/ (default: admin/admin)
    - NetBox Keycloak instance: http://keycloak.localhost/
    - ISDuBA UI: http://isduba.localhost/ (default: user/user)
    - The NetBox API token is printed by the ``netbox-setup`` container logs. The script will attempt to
      print it automatically; if needed, you can retrieve it manually:
        .. code-block:: bash

            docker compose -f dev/docker-compose.yml logs netbox-setup

4) Configure plugins

   Copy and adapt sample configuration files from ``assets/plugin_configs`` to enable data sources:

   - NetBox fetcher (asset source):

     - Copy: ``assets/plugin_configs/data_source/asset/sample/netbox.toml``
       to a new file in ``assets/plugin_configs/data_source/asset/`` (e.g. ``netbox_local.toml``)
     - Set ``url`` (e.g. http://netbox.localhost/) and ``api_token`` (see token from setup logs)

   - ISDuBA fetcher (CSAF source):

     - Copy: ``assets/plugin_configs/data_source/csaf/sample/isduba.toml``
       to a new file in ``assets/plugin_configs/data_source/csaf/`` (e.g. ``isduba_local.toml``)
     - Set ``url`` (e.g. http://isduba.localhost/), ``username``/``password`` (default user/user), and
       ``keycloak_url`` (e.g. http://keycloak.localhost/)

Running the services
--------------------
This project provides three long-running components. Each reads its TOML config from ``assets/`` and
serves a small HTTP API for status and interaction.

- Asset Synchronizer (assetsync)
  - Config: ``assets/assetsync.toml``
  - Default API: http://localhost:8992

- CSAF Synchronizer (csafsync)
  - Config: ``assets/csafsync.toml``
  - Default API: http://localhost:8991

- Matcher
  - Config: ``assets/matcher.toml``
  - Default API: http://localhost:8998

Run them with uv (using console scripts defined in pyproject):

.. code-block:: bash

   # Asset sync
   uv run assetsync

   # CSAF sync
   uv run csafsync

   # Matcher
   uv run csaf_matcher

Visit the OpenAPI docs at ``http://<host>:<port>/docs`` for each service.

Developer workflow
------------------
- Linting

  .. code-block:: bash

     uv run ruff check

- Static type checks

  .. code-block:: bash

     uv run mypy src

- Pre-commit hooks

  .. code-block:: bash

     uv run pre-commit install
     uv run pre-commit run --all-files

Configuration references
------------------------
Asset Synchronizer Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

**Parameters:**

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
  - ``port`` (int): PostgreSQL database port.
  - ``database`` (str): Name of the database to use.
  - ``username`` (str): Database user for authentication.
  - ``password`` (str): Database password for authentication.

CSAF Synchronizer Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

**Parameters:**

The parameters are identical to the Asset Synchronizer configuration (see above), except:

- ``plugin_configs_path`` points to CSAF data source configurations instead of asset sources.
- ``port`` defaults to 8991 for the CSAF sync API.

Matcher Configuration
~~~~~~~~~~~~~~~~~~~~~
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

**Parameters:**

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
