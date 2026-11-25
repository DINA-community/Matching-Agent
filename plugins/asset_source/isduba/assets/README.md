# This directory contains the assets for the ISDuBA plugin.

## isduba API
The api file is downloaded from the [ISDuBA API](http://isduba.localhost/swagger/doc.json).

```bash
curl http://isduba.localhost/swagger/doc.json -o plugins/asset_source/isduba/assets/isduba-api.json
```

When updating the API file, please make sure to:

Correct
- version tag
- host
- document return values
- security definitions

in the swagger file.

This can be done with the following command:

```bash
sed -i \
  -e 's/Apache 2.0/Apache-2.0/g' \
  -e 's/"additionalProperties": {}/"additionalProperties": true/g' \
  -e "$(wc -l < plugins/asset_source/isduba/assets/isduba-api.json)s/$/,/" \
  -e '$i\
"securityDefinitions": {\
    "bearerAuth": {\
        "name": "Authorization",\
        "in": "header",\
        "type": "apiKey",\
        "description": "JWT Authorization header"\
    }\
},\
"security": [ { "bearerAuth": [] } ]' \
  plugins/asset_source/isduba/assets/isduba-api.json
```

For the endpoint `/documents/{id}/cve_related` the `id` parameter is missing ([ISDuBA #1679](https://github.com/ISDuBA/ISDuBA/issues/1679)).
It needs to be added manually.

Make a test run:
```bash
uv sync --all-extras
uv run pytest plugins/asset_source/isduba/tests
# requires a running dev stack
uv run pytest -m integration plugins/asset_source/isduba/tests
```
