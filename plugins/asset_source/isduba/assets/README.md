# This directory contains the assets for the isduba plugin.

## isduba API
The api file is downloaded from the isduba API.
When updating the api file, please make sure to:

Correct
- version tag
- host
- document return values
- security definitions

in the swagger file.
Currently, this can be done with the following command:
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