# Netbox Data Fetcher Plugin

A plugin for the matcher that fetches asset data from Netbox instances.
This plugin allows integration with Netbox to retrieve device and infrastructure information.

## Prerequisites

- Python 3.13 or higher
- Running Netbox instance
- Asset-CSAF matcher core application

## Updating `assets/netbox-api.yaml`

`assets/netbox-api.yaml` is the OpenAPI/Swagger specification of NetBox itself.
The file is used by `build_hook.py`.

Steps for updating the file:

1. Fetch the schema from a running NetBox instance:

   ```bash
   curl -o netbox-api.yaml http://<netbox-host>:8000/api/schema/ -H "Authorization: Bearer nbt_<key>.<secret>"
   ```

   Or use your browser and fetch the URL.

   Save the file at `assets/netbox-api.yaml`.

2. Patch some known incompatibilities with `openapi-python-client` (see also [#133](https://github.com/DINA-community/Matching-Agent/issues/133)):

   ```bash
   sed -i 's/m³/m^3/g' assets/netbox-api.yaml
   ```

3. Remove redundant `multipart/form-data` request bodies that would trigger [a bug](https://github.com/openapi-generators/openapi-python-client/issues/1451) in `openapi-python-client`:

   ```bash
   ./assets/dedupe_multipart_bodies.py assets/netbox-api.yaml
   ```

   See the application help page / file docstring for more technical details.

4. Verify the result builds fine by running:

   ```bash
   uv build
   ```

   and that the generated client actually imports and works:

   ```bash
   uv run pytest plugins/asset_source/netbox/tests/
   ```
