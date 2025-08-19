import asyncio
import time
from typing import List, Union, Any

from dina.cachedb.model import (
    Manufacturer,
    DeviceType,
    Device,
    Software,
    File,
    Hash,
    ProductRelationship,
    AssetSynchronizer,
)
from dina.common import logging
from dina.plugins.datasource.netbox.generated.api_client import AuthenticatedClient
from dina.plugins.datasource.netbox.generated.api_client.api.dcim import (
    dcim_manufacturers_list,
    dcim_device_types_list,
    dcim_devices_list,
)
from dina.plugins.datasource.netbox.generated.api_client.api.plugins import (
    plugins_d3c_software_list_list,
    plugins_d3c_hash_list_list,
    plugins_d3c_filehash_list_list,
    plugins_d3c_productrelationship_list_list,
)
from dina.synchronizer.plugin_base.data_source import DataSourcePlugin

logger = logging.get_logger(__name__)


class NetboxDataSource(DataSourcePlugin):
    def __init__(self, config=None):
        super().__init__(config)
        # Extract configuration values
        try:
            netbox = self.config["DataSource"]["Netbox"]
            self.api_url = netbox["api_url"]
            self.api_token = netbox["api_token"]
            self.client = AuthenticatedClient(
                base_url=self.api_url, prefix="Token", token=self.api_token
            )
        except KeyError:
            raise KeyError("Missing Netbox configuration parameter")
        logger.debug(f"Initialized NetboxDataSource with API URL: {self.api_url}")

    async def fetch_data(
        self,
    ) -> List[
        Union[
            Manufacturer, DeviceType, Device, Software, File, Hash, ProductRelationship
        ]
    ]:
        # In a real implementation, this would use the API URL and token to fetch data

        def find_cachedb_type(nb_type):
            if nb_type == "dcim.device":
                return "Device"
            elif nb_type == "d3c.software":
                return "Software"
            else:
                return None

        results = []

        starttime = time.time()
        logger.info(f"START: {starttime}")
        results.append(AssetSynchronizer(last_run=starttime))

        response = await dcim_manufacturers_list.asyncio(client=self.client)
        for x in response.results:
            results.append(Manufacturer(nb_id=x.id, name=x.name, last_seen=starttime))

        response = await dcim_device_types_list.asyncio(client=self.client)
        for x in response.results:
            results.append(
                DeviceType(
                    nb_id=x.id,
                    model=x.model,
                    model_number=[
                        x.custom_fields.additional_properties["model_number"]
                    ],
                    part_number=[x.part_number],
                    hardware_name=x.custom_fields.additional_properties[
                        "hardware_name"
                    ],
                    hardware_version=[
                        x.custom_fields.additional_properties["hardware_version"]
                    ],
                    device_family=x.custom_fields.additional_properties[
                        "device_family"
                    ],
                    cpe=x.custom_fields.additional_properties["cpe"],
                    nb_manu_id=x.manufacturer.id,
                    last_seen=starttime,
                )
            )

        response = await dcim_devices_list.asyncio(client=self.client)
        for x in response.results:
            results.append(
                Device(
                    nb_id=x.id,
                    name=x.name,
                    serial=[x.serial],
                    nb_devicetype_id=x.device_type.id,
                    last_seen=starttime,
                )
            )

        response = await plugins_d3c_software_list_list.asyncio(client=self.client)
        for x in response.results:
            results.append(
                Software(
                    nb_id=x.id,
                    name=x.name,
                    nb_manu_id=x.manufacturer.id,
                    version=[x.version],
                    cpe=x.cpe,
                    purl=x.purl,
                    sbom_urls=x.sbom_urls,
                    last_seen=starttime,
                )
            )

        response = await plugins_d3c_hash_list_list.asyncio(client=self.client)
        for x in response.results:
            results.append(
                File(
                    nb_id=x.id,
                    filename=x.filename,
                    nb_software_id=x.software.id,
                    last_seen=starttime,
                )
            )

        response = await plugins_d3c_filehash_list_list.asyncio(client=self.client)
        for x in response.results:
            results.append(
                Hash(
                    nb_id=x.id,
                    nb_file_id=x.hash_.id,
                    algorithm=x.algorithm,
                    value=x.value,
                    last_seen=starttime,
                )
            )

        response = await plugins_d3c_productrelationship_list_list.asyncio(
            client=self.client
        )
        for x in response.results:
            source_type = find_cachedb_type(x.source_type)
            target_type = find_cachedb_type(x.destination_type)
            if source_type and target_type:
                results.append(
                    ProductRelationship(
                        nb_id=x.id,
                        nb_source_id=x.source_id,
                        source_type=source_type,
                        nb_target_id=x.destination_id,
                        target_type=target_type,
                        category=int(x.category),
                        last_seen=starttime,
                    )
                )

        # logger.info(f"DATA: {results}")
        await asyncio.sleep(10)
        return results

    async def cleanup_data(self, data_to_check: List[Any]):
        pass

    def endpoint_info(self) -> str:
        return f"{self.api_url}"
