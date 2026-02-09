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

When using the Netbox plugin in the local development environment, you may notice that document titles from ISDUBA are not displayed correctly in the web UI, even though links are clickable.

Root Cause
~~~~~~~~~~

This is a known limitation of the local development setup due to URL accessibility constraints:

- The ISDUBA instance in the local Docker Compose environment can be reached via two different URLs:

  - ``http://isduba.localhost`` (accessible from your browser)
  - ``http://isduba-server`` (accessible from within the Docker network)

- The Netbox plugin must use **one** URL configuration to fetch document titles and generate links
- If configured with ``localhost``: Links work in the browser, but the Netbox container cannot fetch titles (it cannot resolve ``localhost`` to the ISDUBA container)
- If configured with ``isduba``: The Netbox container can fetch titles, but links are not clickable from your browser (your browser cannot resolve the ``isduba`` hostname)

Solution
~~~~~~~~

This is **not an issue in production environments**, where a single publicly accessible URL serves both purposes (e.g., ``https://isduba.example.com``).
