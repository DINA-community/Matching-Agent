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
    plugins_d3c_productrelationship_list_list,
    plugins_d3c_software_list_list,
)
from dina.plugins.datasource.netbox.generated.api_client.models import (
    DeviceTypeCustomFields,
)
from dina.synchronizer.plugin_base.data_source import (
    CleanUpDecision,
    DataSourcePlugin,
    FetchProductsResult,
    FetchRelationshipsResult,
    MappedRelationship,
    ProductId,
    Relationship,
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

    async def fetch_products(
        self,
        fetcher_view: FetcherView,
    ) -> FetchProductsResult:
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
            assets.append(asset)

        return FetchProductsResult(again=False, data=assets)

    async def fetch_relationships(
        self, fetcher_view: FetcherView
    ) -> FetchRelationshipsResult:
        last_run = (await fetcher_view.last_run()).astimezone(tz=timezone.utc)

        if response := await plugins_d3c_productrelationship_list_list.asyncio(
            client=self.client,
            last_updated_gt=[last_run],
        ):
            return FetchRelationshipsResult(
                again=False,
                data=[
                    Relationship(
                        parent=ProductId(
                            relation.source_id, find_cachedb_type(relation.source_type)
                        ),
                        child=ProductId(
                            relation.destination_id,
                            find_cachedb_type(relation.destination_type),
                        ),
                        ty=Asset,
                        origin_info={"relation_id": relation.id},
                    )
                    for relation in response.results
                ],
            )

        return FetchRelationshipsResult(again=False)

    async def map_relationships(
        self, fetcher_view: FetcherView, relations: List[Relationship]
    ) -> List[MappedRelationship]:
        device_ids = set()
        software_ids = set()
        for relation in relations:
            match relation.parent.product_type:
                case ProductType.Device:
                    device_ids.add(relation.parent.id)
                case ProductType.Software:
                    software_ids.add(relation.parent.id)
                case _:
                    raise RuntimeError("Invalid device type")
            match relation.child.product_type:
                case ProductType.Device:
                    device_ids.add(relation.child.id)
                case ProductType.Software:
                    software_ids.add(relation.child.id)
                case _:
                    raise RuntimeError("Invalid device type")

        devices = {
            device.origin_info["device_id"]: device.id
            for device in await fetcher_view.get_existing(
                Asset,
                Asset.origin_info["device_id"]
                .astext.cast(Integer)
                .in_(list(device_ids)),
            )
        }
        software = {
            software.origin_info["software_id"]: software.id
            for software in await fetcher_view.get_existing(
                Asset,
                Asset.origin_info["software_id"]
                .astext.cast(Integer)
                .in_(list(software_ids)),
            )
        }

        mapped = []

        for relation in relations:
            match relation.parent.product_type:
                case ProductType.Device:
                    parent_id = devices[relation.parent.id]
                case ProductType.Software:
                    parent_id = software[relation.parent.id]
                case _:
                    raise RuntimeError(
                        f"Relation parent {relation.parent.id} has unknown type"
                    )
            match relation.child.product_type:
                case ProductType.Device:
                    child_id = devices[relation.child.id]
                case ProductType.Software:
                    child_id = software[relation.child.id]
                case _:
                    raise RuntimeError(
                        f"Relation child {relation.child.id} has unknown type"
                    )

            mapped.append(
                MappedRelationship(
                    parent=parent_id,
                    child=child_id,
                    ty=Asset,
                    origin_info=relation.origin_info,
                )
            )

        unique_mapped = {(m.parent, m.child): m for m in mapped}
        return list(unique_mapped.values())

    async def cleanup_products(
        self, data_to_check: List[Asset | CsafProduct]
    ) -> List[CleanUpDecision]:
        logger.debug(f"Cleanup data: {data_to_check}")
        if not data_to_check:
            return []
        devices = {
            int(d.origin_info["device_id"]): d
            for d in data_to_check
            if d.product.product_type == ProductType.Device
        }
        software_set = {
            int(d.origin_info["software_id"]): d
            for d in data_to_check
            if d.product.product_type == ProductType.Software
        }

        devices_result, software_result = await asyncio.gather(
            dcim_devices_list.asyncio(client=self.client, id=list(devices.keys())),
            plugins_d3c_software_list_list.asyncio(
                client=self.client, id=list(software_set.keys())
            ),
        )

        decisions: List[CleanUpDecision] = []

        if devices_result:
            for device in devices_result.results:
                # The device still exists. Remove it from the set and mark it as kept
                kept_device = devices.pop(device.id)
                decisions.append(
                    CleanUpDecision(can_delete=False, id=kept_device.id, ty=Asset)
                )

        if software_result:
            for software in software_result.results:
                kept_software = software_set.pop(software.id)
                decisions.append(
                    CleanUpDecision(can_delete=False, id=kept_software.id, ty=Asset)
                )

        # Add the remaining devices and software to the decisions as to be deleted.
        decisions.extend(
            map(
                lambda x: CleanUpDecision(can_delete=True, id=x.id, ty=Asset),
                devices.values(),
            )
        )
        decisions.extend(
            map(
                lambda x: CleanUpDecision(can_delete=True, id=x.id, ty=Asset),
                software_set.values(),
            )
        )

        return decisions

    async def cleanup_relationships(
        self, relationships_to_check: List[MappedRelationship]
    ) -> List[MappedRelationship]:
        if not relationships_to_check:
            return []

        existing_relations = {
            r.origin_info["relation_id"]: r for r in relationships_to_check
        }
        result = []
        if response := await plugins_d3c_productrelationship_list_list.asyncio(
            client=self.client,
            id=list(existing_relations.keys()),
        ):
            for relation in response.results:
                kept_relation = existing_relations.pop(relation.id)
                kept_relation.can_delete = False
                result.append(kept_relation)

        for existing_relation in existing_relations.values():
            existing_relation.can_delete = True
            result.append(existing_relation)

        return result

    @property
    def origin_uri(self):
        return self.config.DataSource.Plugin.api_url

    def endpoint_info(self) -> str:
        return f"{self.config.DataSource.Plugin.api_url}"

    def build_resource_path(self, origin_info: dict[str, object]) -> str:
        try:
            if "device_id" in origin_info:
                return f"/api/dcim/devices/{int(origin_info['device_id'])}/"
            if "software_id" in origin_info:
                return f"/api/plugins/d3c/software/{int(origin_info['software_id'])}/"
            if "relation_id" in origin_info:
                # List endpoint in generated client is productrelationship-list
                return f"/api/plugins/d3c/productrelationship-list/{int(origin_info['relation_id'])}/"
        except Exception:
            return ""
        return ""


def find_cachedb_type(netbox_type) -> ProductType:
    """
    Determines the ProductType corresponding to the given NetBox type.
    """
    if netbox_type == "dcim.device":
        return ProductType.Device
    elif netbox_type == "d3c.software":
        return ProductType.Software
    else:
        return ProductType.Undefined
