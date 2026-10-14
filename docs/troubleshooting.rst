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


Netbox Plugin: Document Titles Not Loading in Local Development
----------------------------------------------------------------

New CSAF documents are created in NetBox with only their ISDuBA URL and the title ``Loading...``.
The CSAF plugin contains a background job *CSAF Document Sync* that runs in the docker container ``netbox-worker`` and is responsible to fetch the document details from ISDuBA.
It runs every hour and after new matches are added.

If you see CSAF documents with title ``Loading...``, the background job cannot reach ISDuBA or retrieve the information.

The job uses the URL from setting ``keycloak_url`` (in ``isduba-local.toml``) to connect to Keycloak/ISDuBA.
If these are not reachable from inside the NetBox containers, the documents cannot be fetched.

In the local development environment, the docker compose setup add internal aliases for ``*.localhost``, so the URLs work internally as they do in the browser.
In other setups make sure the ISDuBA document URLs and ``keycloak_url`` are reachable from within the NetBox worker container.

All errors of the backgroun job are printed to the ``netbox-worker`` docker container log.
