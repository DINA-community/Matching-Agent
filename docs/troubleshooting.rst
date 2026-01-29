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

