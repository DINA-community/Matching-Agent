Production Deployment with Docker
=================================

This guide describes how to run the Matching Agent in a production‑like setup
using the Docker assets located in the repository's ``docker/`` directory.

Overview
--------

The compose stack runs the following services:

- PostgreSQL 16 (``postgres``) — shared cache DB used by all components
- Asset Synchronizer (``assetsync``)
- CSAF Synchronizer (``csafsync``)
- Matcher (``matcher``)
- TLS reverse proxy (``gateway``) — NGINX that exposes the three APIs over HTTPS

APIs are published via the gateway on a single HTTPS port (default ``443``) with
paths:

- ``/matcher`` (e.g. ``https://localhost:443/matcher/``)
- ``/assetsync`` (e.g. ``https://localhost:443/assetsync/``)
- ``/csafsync`` (e.g. ``https://localhost:443/csafsync/``)

OpenAPI docs are typically available at ``/docs`` under each prefix, for example
``https://localhost:443/matcher/docs``.


Repository layout
-----------------

The Docker setup consists of:

- ``docker/docker-compose.yml`` — compose file for production‑style deployment
- ``docker/.env.example`` — example environment configuration (copy to ``.env``)
- ``docker/assetsync.Dockerfile`` — assetsync image
- ``docker/csafsync.Dockerfile`` — csafsync image
- ``docker/matcher.Dockerfile`` — matcher image
- ``docker/nginx/`` — gateway image build context (self‑signed TLS generation and routing config)

Service configuration TOML files for containers are expected under ``docker/assets/``.
Adjust them for your environment (data sources, credentials, hostnames).


Prerequisites
-------------

- Docker Engine and Docker Compose plugin
- CPU/Memory sized appropriately for your data volumes
- Optional: a proper DNS name you will assign to the gateway certificate


Quick start
-----------

1) Copy and adjust environment

.. code-block:: bash

   cd docker
   cp .env.example .env
   # IMPORTANT: change passwords, ports, and set TLS_CN to the hostname you'll use

Key variables in ``docker/.env``:

- ``POSTGRES_DB``, ``POSTGRES_USER``, ``POSTGRES_PASSWORD`` — database settings
- ``HTTPS_PORT`` — external port of the HTTPS gateway (defaults to 443)
- ``TLS_CN`` — Common Name for the self‑signed certificate (defaults to ``localhost``)
- ``*_LOG_LEVEL`` — log levels per service (INFO by default)

2) Build and start

.. code-block:: bash

   docker compose up -d --build

The first run will also create named volumes ``postgres-data`` and ``gateway-certs``.
The gateway will generate a self‑signed certificate using ``TLS_CN`` and store it in
the ``gateway-certs`` volume.

3) Access the APIs

- Matcher: ``https://<host>:<HTTPS_PORT>/matcher/``
- Assetsync: ``https://<host>:<HTTPS_PORT>/assetsync/``
- CSAFsync: ``https://<host>:<HTTPS_PORT>/csafsync/``

If using a self‑signed cert, your browser/HTTP client will warn about trust; accept
it locally or configure proper TLS as described below.


Production notes
----------------

Persistence
^^^^^^^^^^^

- PostgreSQL data is stored in the named volume ``postgres-data``.
- TLS materials are stored in ``gateway-certs``.

Backups
^^^^^^^

Use ``pg_dump`` against the running ``postgres`` service or mount the volume and
perform filesystem‑level backups according to your policies.

Upgrades
^^^^^^^^

To upgrade to a new application version:

1. Pull or check out the desired git revision.
2. Rebuild images and recreate containers:

   .. code-block:: bash

      docker compose pull   # if images are published, otherwise skip
      docker compose up -d --build

Changing TLS certificate
^^^^^^^^^^^^^^^^^^^^^^^^

To regenerate a new self‑signed certificate (e.g., after changing ``TLS_CN``):

.. code-block:: bash

   docker compose down
   docker volume rm matching-agent_gateway-certs || true
   docker compose up -d

Alternatively, customize the NGINX image to use your organization's TLS cert/key
by extending ``docker/nginx``.

Health checks and logs
^^^^^^^^^^^^^^^^^^^^^^

Each service is configured with a simple HTTP health check. You can inspect status
and logs via:

.. code-block:: bash

   docker compose ps
   docker compose logs -f gateway matcher assetsync csafsync postgres

Stopping and removal
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   docker compose down           # stop and remove containers
   docker compose down -v        # also remove named volumes (data loss)


Troubleshooting
---------------

- Gateway shows 502/504: ensure backend services are healthy (``docker compose ps``)
- Certificate warnings: expected with self‑signed certs; use a trusted cert for production
- Database connection errors: verify ``POSTGRES_*`` vars and TOML DB settings
- API reachable on HTTP but not HTTPS: verify ``HTTPS_PORT`` exposure and local firewall


Reference: environment variables
--------------------------------

The compose file accepts these variables (see ``docker/.env.example`` for defaults):

- ``POSTGRES_DB`` — Database name (default: ``cachedb``)
- ``POSTGRES_USER`` — Database user (default: ``admin``)
- ``POSTGRES_PASSWORD`` — Database password (default: ``secret``)
- ``MATCHER_LOG_LEVEL`` — Matcher service log level (default: ``INFO``)
- ``ASSETSYNC_LOG_LEVEL`` — Asset Synchronizer log level (default: ``INFO``)
- ``CSAFSYNC_LOG_LEVEL`` — CSAF Synchronizer log level (default: ``INFO``)
- ``HTTPS_PORT`` — Public HTTPS port for the gateway (default: ``443``)
- ``TLS_CN`` — Certificate Common Name used for self‑signed TLS (default: ``localhost``)


See also
--------

- ``docker/docker-compose.yml`` for the full stack definition
- ``docker/.env.example`` for configurable defaults
- ``docker/nginx/nginx.conf`` for gateway routing
- The service configuration files under ``assets/``
