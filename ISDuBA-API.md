# Generating the ISDuBA API

- Download the swagger file of the ISDuBA API and store it as isduba-api.json:
  ```
  wget --no-check-certificate -O isduba-api.json https://<host:port>/swagger/doc.json
  ```
  
- Correct
  - version tag
  - host
  - document return values
  - security definitions
  in the swagger file:
  ```
  sed -i \
      -e 's/Apache 2.0/Apache-2.0/g' \
      -e 's/"host": ""/"host": "https:\/\/<host:port>"/g' \
      -e 's/"additionalProperties": {}/"additionalProperties": true/g' \
	  -e "$(wc -l < isduba-api.json)s/$/,/" \
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
	  isduba-api.json
  ```
  
- Generate the python client for the ISDuBA API:
  ```
  uv run openapi-generator-cli generate -i isduba-api.json -g python -o plugins/asset_source/isduba/src/dina/plugins/datasource/isduba/api_client --package-name isduba_client
  ```
  
- Install the client:
  ```
  uv add plugins/asset_source/isduba/src/dina/plugins/datasource/isduba/api_client
  ```
