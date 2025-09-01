import asyncio
import time
from datetime import timezone
from typing import List

from pydantic import BaseModel
from sqlalchemy import Integer

from dina.cachedb.fetcher_view import FetcherView
from dina.cachedb.model import (
    Asset,
    CsafProduct,
    Product,
    ProductType,
)
from dina.common import logging
from dina.plugins.datasource.netbox.generated.api_client import AuthenticatedClient
from dina.plugins.datasource.netbox.generated.api_client.api.dcim import (
    dcim_device_types_list,
    dcim_devices_list,
    dcim_manufacturers_list,
)
from dina.plugins.datasource.netbox.generated.api_client.api.plugins import (
    plugins_d3c_software_list_list,
)
from dina.plugins.datasource.netbox.generated.api_client.models import (
    DeviceTypeCustomFields,
)
from dina.synchronizer.plugin_base.data_source import (
    CleanUpDecision,
    DataSourcePlugin,
    FetchDataResult,
)

logger = logging.get_logger(__name__)


class NetboxDataSource(DataSourcePlugin):
    class Config(BaseModel):
        api_url: str
        api_token: str

    def __init__(self, config: DataSourcePlugin.Config):
        if config.DataSource.Plugin is not None:
            config.DataSource.Plugin = NetboxDataSource.Config.model_validate(
                config.DataSource.Plugin
            )
        super().__init__(config)
        # Extract configuration values
        try:
            netbox = self.config.DataSource.Plugin
            self.client = AuthenticatedClient(
                base_url=netbox.api_url, prefix="Token", token=netbox.api_token
            )
        except KeyError:
            raise KeyError("Missing Netbox configuration parameter")
        logger.debug(
            f"Initialized NetboxDataSource with API URL: {self.config.DataSource.Plugin.api_url}"
        )

    async def fetch_data(
        self,
        fetcher_view: FetcherView,
    ) -> FetchDataResult:
        last_run = (await fetcher_view.last_run()).astimezone(tz=timezone.utc)
        current_time = time.time()

        # We want to fetch all devices and device_types and manufacturers.
        # We then need to check if there were updates to only parts of an asset.
        (
            devices_result,
            software_results,
            device_types_result,
            manufacturers_result,
        ) = await asyncio.gather(
            dcim_devices_list.asyncio(client=self.client, last_updated_gt=[last_run]),
            plugins_d3c_software_list_list.asyncio(
                client=self.client, last_updated_gt=[last_run]
            ),
            dcim_device_types_list.asyncio(
                client=self.client, last_updated_gt=[last_run]
            ),
            dcim_manufacturers_list.asyncio(
                client=self.client, last_updated_gt=[last_run]
            ),
        )

        if devices_result:
            devices = {device.id: device for device in devices_result.results}
        else:
            raise Exception("what dis")

        if software_results:
            software = {sw.id: sw for sw in software_results.results}
        else:
            raise Exception("what dis")

        if device_types_result:
            device_types = {
                device_type.id: device_type
                for device_type in device_types_result.results
            }
        else:
            raise Exception("what dis")

        if manufacturers_result:
            manufacturers = {
                manufacturer.id: manufacturer
                for manufacturer in manufacturers_result.results
            }
        else:
            raise Exception("what dis")

        # TODO: Maybe we can use graphql instead to reduce the amount of communication needed?
        if manufacturers:
            # Extend the devices we need to update with devices that received an update to the manufacturer only.
            if devices_result := await dcim_devices_list.asyncio(
                client=self.client,
                manufacturer_id=list(manufacturers.keys()),
                id_n=list(devices.keys()),
            ):
                for device in devices_result.results:
                    if device.id not in devices:
                        devices[device.id] = device

            if software_results := await plugins_d3c_software_list_list.asyncio(
                client=self.client, id_n=list(software.keys())
            ):
                for sw in software_results.results:
                    # TODO: The netbox api needs to support filtering on manufacturer_id
                    if sw.id not in software and sw.manufacturer.id in manufacturers:
                        software[sw.id] = sw

        # Extend the devices we need to update with devices that received an update to the device_type only.
        if device_types:
            if devices_result := await dcim_devices_list.asyncio(
                client=self.client,
                device_type_id=list(device_types.keys()),
                id_n=list(devices.keys()),
            ):
                for device in devices_result.results:
                    if device.id not in devices:
                        devices[device.id] = device

        # Fetch the missing device types and manufacturers.
        if devices:
            missing_device_type_ids = {
                device.device_type.id
                for device in devices.values()
                if device.device_type.id not in device_types
            }
            if missing_device_type_ids:
                if device_types_result := await dcim_device_types_list.asyncio(
                    client=self.client,
                    id=list(missing_device_type_ids),
                ):
                    device_types.update(
                        {
                            device_type.id: device_type
                            for device_type in device_types_result.results
                        }
                    )

            missing_manufacturer_ids = {
                device.device_type.manufacturer.id
                for device in devices.values()
                if device.device_type.manufacturer.id not in manufacturers
            }
            if missing_manufacturer_ids:
                if manufacturers_result := await dcim_manufacturers_list.asyncio(
                    client=self.client,
                    id=list(missing_manufacturer_ids),
                ):
                    manufacturers.update(
                        {
                            manufacturer.id: manufacturer
                            for manufacturer in manufacturers_result.results
                        }
                    )

        existing_device_assets = {
            asset.origin_info["device_id"]: asset
            for asset in await fetcher_view.get_existing(
                Asset,
                Asset.origin_info["device_id"]
                .astext.cast(Integer)
                .in_(list(devices.keys())),
            )
        }

        existing_software_assets = {
            sw.origin_info["software_id"]: sw
            for sw in await fetcher_view.get_existing(
                Asset,
                Asset.origin_info["software_id"]
                .astext.cast(Integer)
                .in_(list(software.keys())),
            )
        }

        assets: List[Asset | CsafProduct] = []
        for device in devices.values():
            logger.debug(f"Adding asset for device: {device.name}")
            device_type = device_types[device.device_type.id]
            manufacturer = manufacturers[device_type.manufacturer.id]
            origin_info = {
                "device_id": device.id,
                "device_type_id": device_type.id,
                "manufacturer_id": manufacturer.id,
            }

            if asset := existing_device_assets.get(device.id, None):
                asset.last_update = current_time
                asset.origin_info = origin_info
            else:
                asset = Asset(
                    product=Product(),
                    last_update=current_time,
                    origin_uri=self.origin_uri,
                    origin_info=origin_info,
                )

            asset.product.product_type = ProductType.Device
            if isinstance(device.name, str):
                asset.product.name = device.name
            if isinstance(device.serial, str):
                asset.product.serial_numbers = [device.serial]

            asset.product.model = device_type.model
            if isinstance(device_type.part_number, str):
                asset.product.part_numbers = [device_type.part_number]
            if isinstance(device_type.custom_fields, DeviceTypeCustomFields):
                asset.product.model_numbers = [
                    device_type.custom_fields.additional_properties["model_number"]
                ]
                asset.product.hardware_name = (
                    device_type.custom_fields.additional_properties["hardware_name"]
                )
                asset.product.version = [
                    device_type.custom_fields.additional_properties["hardware_version"]
                ]
                asset.product.device_family = (
                    device_type.custom_fields.additional_properties["device_family"]
                )
                asset.product.cpe = device_type.custom_fields.additional_properties[
                    "cpe"
                ]

            asset.product.manufacturer_name = manufacturer.name
            asset.children.append(asset)
            assets.append(asset)

        for sw in software.values():
            logger.debug(f"Adding asset for device: {sw.name}")
            manufacturer = manufacturers[sw.manufacturer.id]
            origin_info = {
                "software_id": sw.id,
                "manufacturer_id": manufacturer.id,
            }

            if asset := existing_software_assets.get(sw.id, None):
                asset.last_update = current_time
                asset.origin_info = origin_info
            else:
                asset = Asset(
                    product=Product(),
                    last_update=current_time,
                    origin_uri=self.origin_uri,
                    origin_info=origin_info,
                )

            asset.product.product_type = ProductType.Software
            if isinstance(sw.name, str):
                asset.product.name = sw.name
            if isinstance(sw.version, str):
                asset.product.version = [sw.version]
            if isinstance(sw.cpe, str):
                asset.product.cpe = sw.cpe
            if isinstance(sw.purl, str):
                asset.product.purl = sw.purl
            if isinstance(sw.sbom_urls, list):
                asset.product.sbom_urls = sw.sbom_urls  # type: ignore

            asset.product.manufacturer_name = manufacturer.name
            asset.children.append(asset)
            assets.append(asset)

        return FetchDataResult(again=False, data=assets)
        # # In a real implementation, this would use the API URL and token to fetch data
        #
        # def find_cachedb_type(nb_type):
        #     if nb_type == "dcim.device":
        #         return "Device"
        #     elif nb_type == "d3c.software":
        #         return "Software"
        #     else:
        #         return None
        #
        # response = await plugins_d3c_software_list_list.asyncio(client=self.client)
        # for x in response.results:
        #     results.append(
        #         Software(
        #             nb_id=x.id,
        #             name=x.name,
        #             nb_manu_id=x.manufacturer.id,
        #             version=[x.version],
        #             cpe=x.cpe,
        #             purl=x.purl,
        #             sbom_urls=x.sbom_urls,
        #             last_seen=starttime,
        #         )
        #     )
        #
        # response = await plugins_d3c_hash_list_list.asyncio(client=self.client)
        # for x in response.results:
        #     results.append(
        #         File(
        #             nb_id=x.id,
        #             filename=x.filename,
        #             nb_software_id=x.software.id,
        #             last_seen=starttime,
        #         )
        #     )
        #
        # response = await plugins_d3c_filehash_list_list.asyncio(client=self.client)
        # for x in response.results:
        #     results.append(
        #         Hash(
        #             nb_id=x.id,
        #             nb_file_id=x.hash_.id,
        #             algorithm=x.algorithm,
        #             value=x.value,
        #             last_seen=starttime,
        #         )
        #     )
        #
        # response = await plugins_d3c_productrelationship_list_list.asyncio(
        #     client=self.client
        # )
        # for x in response.results:
        #     source_type = find_cachedb_type(x.source_type)
        #     target_type = find_cachedb_type(x.destination_type)
        #     if source_type and target_type:
        #         results.append(
        #             ProductRelationship(
        #                 nb_id=x.id,
        #                 nb_source_id=x.source_id,
        #                 source_type=source_type,
        #                 nb_target_id=x.destination_id,
        #                 target_type=target_type,
        #                 category=int(x.category),
        #                 last_seen=starttime,
        #             )
        #         )
        #
        # # logger.info(f"DATA: {results}")
        # await asyncio.sleep(10)
        # return results

    async def cleanup_data(
        self, data_to_check: List[Asset | CsafProduct]
    ) -> List[CleanUpDecision]:
        logger.debug(f"Cleanup data: {data_to_check}")
        # TODO: Perform the proper cleanup actions.
        # We need to query the netbox api for the provided assets and check if they still exist.
        return [
            CleanUpDecision(can_delete=False, id=d.id, ty=Asset) for d in data_to_check
        ]

    @property
    def origin_uri(self):
        return self.config.DataSource.Plugin.api_url

    def endpoint_info(self) -> str:
        return f"{self.config.DataSource.Plugin.api_url}"
