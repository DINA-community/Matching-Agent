Troubleshooting
===============

This section describes common issues and their solutions.

Polars: Missing required CPU features
-------------------------------------

When running the Matching Agent (or its components like `csafsync`, `assetsync`) in a virtualized environment (e.g., QEMU) or on older hardware, you might encounter a warning similar to this:

.. code-block:: text

    RuntimeWarning: Missing required CPU features.
    The following required CPU features were not detected:
        avx, avx2, fma, bmi1, bmi2, lzcnt, pclmulqdq, movbe
    Continuing to use this version of Polars on this processor will likely result in a crash.
    Install the `polars-lts-cpu` package instead of `polars` to run Polars with better compatibility.

This happens because the default `polars` package requires modern CPU instructions for optimal performance.

Solutions
~~~~~~~~~

1. **Upgrade Virtual Machine CPU Model**:
   If you are using QEMU/KVM, try using a newer CPU model like `x86-64-v3` or `x86-64-v4` or `host`.
   For example, in QEMU: `-cpu x86-64-v3`. Note that even with `x86-64-v3`, some features like `pclmulqdq` might still be reported as missing depending on the host, but basic operations might still work.

2. **Use Polars with Runtime Compatibility**:
   If you cannot change the CPU model, you can install the compatibility version of Polars:

   .. code-block:: bash

       uv pip install "polars[rtcompat]"

Daemon authentication problems
------------------------------

If the assetsync daemon ``uv run assetsync`` logs messages like these:

.. code-block::

   RuntimeError: Could not authenticate with the NetBox instance. Probably invalid access token. Please make sure to correctly configure your access token in the plugin configuration.
   dina.synchronizer.base - ERROR - Error fetching data from plugin netbox_fetcher for endpoint http://netbox.localhost/: Could not authenticate with the NetBox instance. Probably invalid access token. Please make sure to correctly configure your access token in the plugin configuration.

or the ``csaf_matcher``:

.. code-block::

   dina.plugins.datasource.netbox.netbox - ERROR - Failed to notify new matches: Unexpected status code: 403

Then the configured authentication token is not correct.
Configure the NetBox token in the assetsync configuration, see Getting started, section *Configure plugins*.
A new token is generated with every new setup of the NetBox instance and needs to be set manually.

Then start the ``csaf_matcher`` and ``assetsync`` again.

Please note, that matches that were previously found, are not automatically published to NetBox again.
To force a Re-Publish, run this command:

.. code-block:: bash

   access_token=$(curl -s -X POST http://localhost:8998/token -d "username=admin&password=admin" | jq -r .access_token)
   curl -s -X POST -H "Authorization: Bearer $access_token" -H "Content-Type: application/json" -d '{"force_recompute": true}' http://localhost:8998/task/start

Netbox Plugin: Document Titles Not Loading in Local Development
----------------------------------------------------------------

New CSAF documents are created in NetBox with only their ISDuBA URL and the title ``Loading...``.
The CSAF plugin contains a background job *CSAF Document Sync* that runs in the docker container ``netbox-worker`` and is responsible to fetch the document details from ISDuBA.
It runs every hour and after new matches are added.

If you see CSAF documents with title ``Loading...``, the background job cannot reach ISDuBA or retrieve the information.

The job uses the URL from setting ``keycloak_url`` (in ``isduba-local.toml``) to connect to Keycloak/ISDuBA.
If these are not reachable from inside the NetBox containers, the documents cannot be fetched.

In the local development environment, the docker compose setup adds internal aliases for ``*.localhost``, so the URLs work internally as they do in the browser.
In other setups make sure the ISDuBA document URLs and ``keycloak_url`` are reachable from within the NetBox worker container.

All errors of the background job are printed to the ``netbox-worker`` docker container log.

Update Submodules
------------------

git submodules --update --remote
git submodules status

.. code-block:: bash

   $git submodules --update --remote
   $git submodules status
   +e4b0c6ab7afaaf5153e4b48aab61f52c6c60d909 dev/isduba (v.0.17.0-114-ge4b0c6ab)
   7689fec7a70717f7e72feecb383e7a3f55538b5f dev/netbox (5.1.1)
   +4ebde51fdb3f839330b0b8ec1f60e3b69d05052d dev/plugins/csaf (v1.0-rc1-103-g4ebde51)
   e3c278baef2d9cd6045057f1bb8293d0e6d1970e dev/plugins/d3c (v1.0-rc1-114-ge3c278b)

The + sign indicate a update in the submodule. In order to apply on the
repository use `git add dev/isduba` for instance, since a new version is
available. 

