# Netbox Data Fetcher Plugin

A plugin for the matcher that fetches asset data from Netbox instances.
This plugin allows integration with Netbox to retrieve device and infrastructure information.

## Prerequisites

- Python 3.13 or higher
- Running Netbox instance
- Asset-CSAF matcher core application

## Installation Netbox API

TODO

curl -o netbox-api-swagger.yaml http://<netbox-host>:8000/api/schema/ -H "api_token = <netbox-api-token>


in netbox-api-swagger.yaml delete the following:
devicetype_count: L132178, L147825

device_count: L131369 L131425 L132365 L132757 L135291 L139171 L139442 L147593
L162416 L166567 L169155 L169891

virtualmachine_count: L130937 L131373 L132368 L135296 L139174 L162418 L169158 L169895


python3 -m venv venv
source /home/assetmgr/venv/bin/activate
python3 -m openapi_python_client generate --path /home/netbox-api/netbox-api-swagger.yaml

in models/device_with_config_context.py comment 
face, position, airflow: L663 L871 L663 ‚L875

