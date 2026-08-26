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

Project Structure
--------------------
This section provides an overview of the project’s directory and package structure to help new users quickly find the right entry points.


- ``assets/``: Configuration files for plugins and the matching logic
- ``dev/``: Docker Compose setup for development purposes comprising a Postgres, ISDUBA, and NetBox instance
- ``docker/``: Docker files to build and run the project in containers for production
- ``docs/``: Project documentation (Sphinx sources)

- ``plugins/``: Extensions implemented as plugins

  - ``asset_source/``: Data source plugins (read external data and map it to the internal data model)

    - ``isduba/``: Import from ISDUBA
    - ``netbox/``: Import from NetBox
    - ``sample/``: Example/demo plugin used as a template

  - ``preprocessing/``: Preprocessing (normalization, text cleanup)

    - ``default/``: Default preprocessing implementation
    - ``identity/``: A preprocessing plugin that does nothing to the data. Used as an example.

- ``src/dina/``: Main package (production code)

  - ``assetsync/``: Entry point and logic for the asset synchronizer
  - ``cachedb/``: Database access and data model (schema, repositories/queries)
  - ``cli/``: CLI for user management (Cache DB) and for controlling the matcher/synchronizer APIs
  - ``common/``: Shared utilities (e.g., logging, configuration, auth helpers)
  - ``csafsync/``: Entry point and logic for the CSAF synchronizer
  - ``matcher/``: Matching run and matching logic

    - ``main.py``: The core components of the matcher
    - ``matching.py``: Implements the matching logic
    - ``calculate_score.py``: Calculates scores and evaluates results

  - ``synchronizer/``: Plugin interfaces for fetching, preprocessing, relationship mapping, and cleanup, as well as reporting newly found matches back to the data source

- ``tests/``: Tests (pytest), fixtures, and test data

Git Branches
------------

- ``main`` contains the latest stable release.
- ``chore/pre-release`` is the active development branch: branch from it for new work and target it with pull requests, unless told otherwise.

Quick start
-----------
1) Clone the repository and switch to the development branch:

   .. code-block:: bash

      git clone --recurse-submodules https://github.com/DINA-community/Matching-Agent.git

      cd Matching-Agent

      git checkout chore/pre-release

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
        ./dev/start-local-env.sh --stop                # stop
        ./dev/start-local-env.sh --down                # stop and remove services
        ./dev/start-local-env.sh --down --volumes      # stop and remove services AND named volumes
        ./dev/start-local-env.sh --recreate --volumes  # full reset: down -v, then up
        ./dev/start-local-env.sh --clean               # remove local images + local env/toml/plugins.py

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

   .. note::
      Datasource plugins are expected to fetch valid source data. For CSAF sources, this means the
      fetched CSAF documents must already be valid at the upstream source system.

   - NetBox fetcher (asset source):

     - Copy: ``assets/plugin_configs/data_source/asset/sample/netbox.toml``
       to a new file in ``assets/plugin_configs/data_source/asset/`` (e.g. ``netbox-local.toml``)
     - Set ``url`` (e.g. http://netbox.localhost/) and ``api_token`` (see token from setup logs)

   - ISDuBA fetcher (CSAF source):

     - Copy: ``assets/plugin_configs/data_source/csaf/sample/isduba.toml``
       to a new file in ``assets/plugin_configs/data_source/csaf/`` (e.g. ``isduba-local.toml``)
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

Running Tests
-------------

The Matching Agent project contains tests in several locations:

- ``tests/`` — core unit and integration tests
- ``plugins/asset_source/<plugin>/tests/`` — tests for asset-source plugins
- ``plugins/preprocessing/<plugin>/tests/`` — tests for preprocessing plugins


Running all tests
^^^^^^^^^^^^^^^^^

To run the full test suite:

.. code-block:: bash

    uv run pytest -v -s


Running a single test or file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can execute an individual test file by passing its path:

.. code-block:: bash

    uv run pytest -v -s <path-to-test>

Example:

.. code-block:: bash

    uv run pytest -v -s tests/matcher/test_matching.py


Plugin-specific tests
^^^^^^^^^^^^^^^^^^^^^

Plugin tests are included automatically when the corresponding plugin is installed
(e.g. via ``uv sync --extra <plugin>``).
If a plugin is not installed, its tests will be skipped.


Testing with Coverage
^^^^^^^^^^^^^^^^^^^^^

To run tests with coverage reporting using ``pytest-cov``:

.. code-block:: bash

    uv run pytest --cov=dina --cov-report=html --cov-report=term

This generates an HTML coverage report in ``htmlcov/`` and prints a summary to the terminal.

**TL;DR**: Use ``--cov=<package>`` to measure coverage, and ``--cov-report=html`` or ``--cov-report=term`` to generate reports.

For more information:

- pytest documentation: https://docs.pytest.org/
- pytest-cov documentation: https://pytest-cov.readthedocs.io/
