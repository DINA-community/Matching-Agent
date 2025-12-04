Developer Installation and Getting Started
==========================================

.. include:: _includes/section-toc.rstinc

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
The detailed configuration for each component has moved to a dedicated section:

- :ref:`Asset Synchronizer configuration <config-assetsync>`
- :ref:`CSAF Synchronizer configuration <config-csafsync>`
- :ref:`Matcher configuration <config-matcher>`

See that page for example TOML files and parameter descriptions.
