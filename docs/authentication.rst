API Authentication Guide
========================

This guide explains how to authenticate with the synchronizer APIs provided by the Matching Agent
(e.g., Asset Synchronizer and CSAF Synchronizer). The APIs are implemented with FastAPI and
use OAuth2 Password flow to issue short‑lived JWT bearer tokens.

Overview
--------
- Token endpoint: ``POST /token`` (unauthenticated)
- Protected endpoints: e.g., ``GET /status`` and ``POST /start``
- Authorization: ``Authorization: Bearer <access_token>``
- Token expiry: configurable via ``[Synchronizer.Api].access_token_expire_minutes`` in the component TOML config
- Swagger UI: ``/docs`` (interactive)

Prerequisites
-------------
1) Ensure the synchronizer is running.
   - Asset Synchronizer default: ``http://localhost:8992`` (configurable in ``assets/assetsync.toml``)
   - CSAF Synchronizer default: ``http://localhost:8991`` (configurable in ``assets/csafsync.toml``)

2) Create a user account in the CacheDB to authenticate against. Use the CLI:

   .. code-block:: bash

      # Uses [Cachedb] from assets/assetsync.toml by default (override with --config)
      uv run csaf_matcher_cli user create -u admin

   Notes:
   - If the user already exists, this will be logged.
   - Passwords are hashed server‑side using the project’s configured algorithm.
   - For interactive use, do not pass passwords via ``-p/--password``. The CLI will securely prompt.
     Reserve ``-p`` for non‑interactive environments (e.g., CI) and source secrets securely.

Obtain an access token
----------------------
The token endpoint expects form‑encoded fields ``username`` and ``password`` (OAuth2 password flow).

- With curl:

  .. code-block:: bash

     BASE_URL="http://localhost:8992"  # adjust for the component you are calling
     curl -sS -X POST "$BASE_URL/token" \
       -H "Content-Type: application/x-www-form-urlencoded" \
       -d "username=alice&password=S3cur3!" | jq

  Example response:

  .. code-block:: json

     {
       "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
       "token_type": "bearer"
     }

Call protected endpoints
------------------------
Use the token in the ``Authorization`` header with the ``Bearer`` scheme.

- curl example:

  .. code-block:: bash

     TOKEN="<paste access_token>"
     curl -sS "$BASE_URL/status" -H "Authorization: Bearer $TOKEN" | jq

Token lifetime and configuration
--------------------------------
- Expiration is defined by ``[Synchronizer.Api].access_token_expire_minutes`` in the component config TOML.
- When a token expires, request a new one via ``POST /token``.
- The token payload currently contains the session username and an expiry timestamp.

Interactive docs
----------------
Each synchronizer exposes OpenAPI documentation:

- Swagger UI: ``/docs`` (lets you acquire a token and try requests)

Troubleshooting
---------------
- 401 Unauthorized when calling protected endpoints:
  - Ensure you included ``Authorization: Bearer <access_token>``.
  - Verify the user exists and is ``active`` in the CacheDB.
  - Ensure you are calling the correct base URL and port for the running component.
  - If the token may be expired, obtain a fresh token from ``/token``.

- 401 from ``/token`` with "Incorrect username or password":
  - Verify credentials and that the user exists (use the CLI to create/update).

Security notes
--------------
- The default development configuration is not intended for production. Review and harden settings, including
  secrets management and network exposure, before deploying in a production environment.
