import asyncio
from typing import List

from dina.cachedb.model import Asset, Manufacturer, DeviceType, Device, Software, File, Hash
from dina.common import logging
from dina.synchronizer.plugin_base.data_source import DataSourcePlugin
from .api_client import Client  # type: ignore
from .api_client.api.dcim import dcim_manufacturers_list,dcim_device_types_list,dcim_devices_list
from .api_client.api.plugins import plugins_d3c_software_list_list, plugins_d3c_filehash_list_list, plugins_d3c_hash_list_list

logger = logging.get_logger(__name__)


class NetboxDataSource(DataSourcePlugin):
    def __init__(self, config=None):
        super().__init__(config)
        # Extract configuration values
        try:
            netbox = self.config["DataSource"]["Netbox"]
            self.api_url = netbox["api_url"]
            self.api_token = netbox["api_token"]
            self.client = Client(
                base_url=self.api_url,
                headers={"Authorization": f"Token {self.api_token}"},
            )
        except KeyError:
            raise KeyError("Missing Netbox configuration parameter")
        logger.debug(f"Initialized NetboxDataSource with API URL: {self.api_url}")

    async def fetch_data(self) -> List[Asset]:
        # In a real implementation, this would use the API URL and token to fetch data
        results = []

        response = await dcim_manufacturers_list.asyncio(client=self.client)
        for x in response.results:
            results.append(Manufacturer(nb_id=x.id, name=x.name))

        response = await dcim_device_types_list.asyncio(client=self.client)
        for x in response.results:
            if x.custom_fields.additional_properties['model_number'] == None:
                model_number = ""
            else:
                model_number=x.custom_fields.additional_properties['model_number']
            results.append(DeviceType(nb_id=x.id,model=x.model,model_number=model_number,part_number=x.part_number, hardware_name=x.custom_fields.additional_properties['hardware_name'],hardware_version=x.custom_fields.additional_properties['hardware_version'],device_family=x.custom_fields.additional_properties['device_family'],cpe=x.custom_fields.additional_properties['cpe'],nb_manu_id=x.manufacturer.id))

        response = await dcim_devices_list.asyncio(client=self.client)
        for x in response.results:
            results.append(Device(nb_id=x.id, name=x.name, serial=x.serial, nb_devicetype_id=x.device_type.id))

        response = await plugins_d3c_software_list_list.asyncio(client=self.client)
        for x in response.results:
            results.append(Software(nb_id=x.id,name=x.name,nb_manu_id=x.manufacturer.id,version=x.version,cpe=x.cpe,purl=x.purl,sbom_urls=x.sbom_urls))

        response = await plugins_d3c_filehash_list_list.asyncio(client=self.client)
        for x in response.results:
            logger.info(f"DATA: {x}")
            #results.append(File(nb_id=x.id, nb_software_id=x.hash_.software.id, filename=x.hash_.filename))

        response = await plugins_d3c_hash_list_list.asyncio(client=self.client)
        for x in response.results:
            logger.info(f"DATA: {x}")
            #results.append(Hash(nb_id=x.id, filename=x.name, nb_file_id=x.filename.id, algorithm=x.algorithm, value=x.value))

        logger.info(f"DATA: {results}")
        await asyncio.sleep(1)
        return results

    def endpoint_info(self) -> str:
        return f"{self.api_url}"
