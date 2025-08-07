# ISDuBA API

The installation script of the ISDuBA fetcher plugin in the root directory of this project includes the following steps among others:

- Download the swagger file of the ISDuBA API and store it as isduba-api.json:
  ```
  curl -o isduba-api.json --insecure https://<host:port>/swagger/doc.json
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
  uv run openapi-generator-cli generate -i isduba-api.json -g python -o src/dina/plugins/datasource/isduba/api_client --package-name isduba_api_client
  ```
  
- Install the client:
  ```
  uv add src/dina/plugins/datasource/isduba/api_client
  ```
