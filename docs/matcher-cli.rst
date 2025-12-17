Matcher CLI
===========

.. include:: _includes/section-toc.rstinc

This page documents the command-line interface (CLI) used to interact with the Matcher and the
related services. The CLI wraps the HTTP APIs exposed by the components and helps you authenticate,
inspect matches, and control the matching task.

Names and how to run
--------------------

Depending on how you run the project you may invoke the CLI via one of the following:

- When using uv without installing the package system-wide:

  .. code-block:: bash

     uv run csaf_matcher_cli --help

- When installed as a console script, the program name is ``csaf_matcher_cli`` and the
  top-level help will look like it. Either way, the commands and flags are the same.

Prerequisites
-------------

1) Ensure the Matcher service is running. The default API base URL is ``http://localhost:8998`` and
   can be configured via ``assets/matcher.toml``.

2) Create a user in the CacheDB to authenticate against (if you don't have one yet):

   .. code-block:: bash

      # Uses [Cachedb] from assets/assetsync.toml by default (override with --config)
      uv run csaf_matcher_cli user create -u admin

Authentication helpers
----------------------

The CLI can obtain an OAuth2 access token for you via the ``token`` subcommand and then use it for
subsequent calls.

- Get a token for the Matcher API:

  .. code-block:: bash

     # You can pass common options at the ROOT level (before the group):
     uv run csaf_matcher_cli --base-url http://localhost:8998 -u admin \
       matcher token

     # Alternatively, pass them right after the group (before the subcommand):
     uv run csaf_matcher_cli matcher --base-url http://localhost:8998 -u admin \
       token

  The password can also be provided with ``-p/--password`` instead of via the prompt.

  .. important::

     For interactive use, do NOT pass the password via ``-p/--password``. Supplying passwords on the
     command line may expose them via shell history or process listings. Omit ``-p`` and enter the
     password at the secure prompt instead. Reserve ``-p`` for non‑interactive contexts (e.g., CI)
     and source the secret from a secure provider.

Matcher commands
----------------

Top-level group: ``matcher`` (interact with the Matcher API)

Common options for all matcher commands:

- ``--base-url``: Base URL of the Matcher API, e.g. ``http://localhost:8998`` (required)
- ``-u/--username``: Username for authentication (required)
- ``-p/--password``: Password for authentication (optional). For interactive use, omit this option to
  be prompted securely. Avoid passing passwords on the command line.

Subcommands:

1) Token
   - ``matcher token`` — Obtain and print a bearer token.

   Example:

   .. code-block:: bash

      # Preferred (root-level options):
      uv run csaf_matcher_cli --base-url http://localhost:8998 -u admin \
        matcher token

      # Also valid (group-level options before subcommand):
      uv run csaf_matcher_cli matcher --base-url http://localhost:8998 -u admin \
        token

2) Matches
   - ``matcher matches list`` — List matches with optional filters.
     Options:
     - ``--limit INT`` (default: 100)
     - ``--offset INT`` (default: 0)
     - ``--origin-uri STR``
     - ``--time-lte FLOAT`` and ``--time-gte FLOAT``
     - ``--assets URL [URL ...]`` — filter by asset URLs
     - ``--csaf-documents URL [URL ...]`` — filter by CSAF document URLs
     - ``--threshold FLOAT``

     Example:

     .. code-block:: bash

        # Preferred (root-level options):
        uv run csaf_matcher_cli --base-url http://localhost:8998 -u admin \
          matcher matches list --limit 50 --threshold 0.6

        # Also valid (group-level options before subcommand):
        uv run csaf_matcher_cli matcher --base-url http://localhost:8998 -u admin \
          matches list --limit 50 --threshold 0.6

   - ``matcher matches get <id>`` — Fetch a single match by ID.

     Example:

     .. code-block:: bash

        uv run csaf_matcher_cli --base-url http://localhost:8998 -u admin \
          matcher matches get 42

3) Task control
   - ``matcher task start`` — Start a matching task. Optional filters:
     - ``--assets INT [INT ...]`` — restrict to specific asset IDs
     - ``--csaf-products INT [INT ...]`` — restrict to specific CSAF product IDs

     Example (start a full run):

     .. code-block:: bash

        uv run csaf_matcher_cli --base-url http://localhost:8998 -u admin \
          matcher task start

     Example (restrict scope):

     .. code-block:: bash

        uv run csaf_matcher_cli --base-url http://localhost:8998 -u admin \
          matcher task start --assets 1001 1002 --csaf-products 2001

   - ``matcher task status`` — Show current matcher status.

     .. code-block:: bash

        uv run csaf_matcher_cli --base-url http://localhost:8998 -u admin \
          matcher task status

   - ``matcher task stop`` — Request a stop of the matcher.

     .. code-block:: bash

        uv run csaf_matcher_cli --base-url http://localhost:8998 -u admin \
          matcher task stop

4) Clear caches
   - ``matcher clear all`` — Clear all matcher-related caches
   - ``matcher clear matches`` — Clear only the matches cache
   - ``matcher clear assets --origin-uri <URI>`` — Clear cached assets for a given origin
   - ``matcher clear csaf --origin-uri <URI>`` — Clear cached CSAF data for a given origin

   Examples:

   .. code-block:: bash

      uv run csaf_matcher_cli --base-url http://localhost:8998 -u admin \
        matcher clear matches

      uv run csaf_matcher_cli --base-url http://localhost:8998 -u admin \
        matcher clear assets --origin-uri http://netbox.localhost/

Argument placement
------------------

- Common options like ``--base-url`` and ``-u/--username`` must appear at the root level
  (before ``matcher``).

Non‑interactive usage (automation/CI)
-------------------------------------

In automated environments where prompting is not possible, you may provide the password via ``-p``.
Ensure that you retrieve it from a secure secret manager and be aware that passing secrets on the
command line can be visible to local process listing tools depending on the operating system. Prefer
ephemeral, least‑privilege credentials and restrict machine access.

Additional commands
-------------------

The CLI also provides a generic ``sync`` group to interact with a Synchronizer API (asset or CSAF):

- ``sync token`` — Obtain a token for a Synchronizer API
- ``sync task start`` — Trigger a synchronizer run
- ``sync task status`` — Get the synchronizer status

All of these accept the same common options (``--base-url``, ``-u``, ``-p``) but target the synchronizer
endpoints instead. See the top-level ``--help`` for details.

Troubleshooting
---------------

- 401 Unauthorized: ensure credentials are correct and the user exists and is active. If the token may be expired,
  retrieve a new one via ``matcher token``.
- Connection errors: verify the Matcher service is running and ``--base-url`` points to it.
- Validation errors: re-check argument names and types (IDs are integers, lists are space-separated).
