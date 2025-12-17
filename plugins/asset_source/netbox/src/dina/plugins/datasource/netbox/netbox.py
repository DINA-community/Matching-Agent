import asyncio
import time
from datetime import timezone, datetime
from typing import List, Any

import httpx
from pydantic import BaseModel, HttpUrl
from sqlalchemy import Integer

from dina.cachedb.fetcher_view import FetcherView
from dina.cachedb.model import (
    Asset,
    CsafProduct,
    Product,
    ProductType,
    Match,
)
from dina.common import log
from dina.plugins.datasource.netbox.generated.api_client import AuthenticatedClient
from dina.plugins.datasource.netbox.generated.api_client.api.dcim import (
    dcim_device_types_list,
    dcim_devices_list,
    dcim_manufacturers_list,
)
from dina.plugins.datasource.netbox.generated.api_client.api.plugins import (
    plugins_d3c_productrelationship_list_list,
    plugins_d3c_software_list_list,
    plugins_csaf_csafmatch_list_create,
)
from dina.plugins.datasource.netbox.generated.api_client.errors import UnexpectedStatus
from dina.plugins.datasource.netbox.generated.api_client.models import (
    DeviceTypeCustomFields,
    CsafMatchRequest,
)
from dina.plugins.datasource.netbox.generated.api_client.types import UNSET
from dina.synchronizer.plugin_base.data_source import (
    CleanUpDecision,
    DataSourcePlugin,
    FetchProductsResult,
    FetchRelationshipsResult,
    MappedRelationship,
    ProductId,
    Relationship,
)

logger = log.get_logger(__name__)


class NetboxDataSource(DataSourcePlugin):
    class Config(BaseModel):
        api_url: HttpUrl
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
                base_url=str(netbox.api_url),
                prefix="Token",
                token=netbox.api_token,
                raise_on_unexpected_status=True,
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
            dcim_devices_list.asyncio(
                client=self.client, last_updated_gt=[last_run], ordering="-id"
            ),
            plugins_d3c_software_list_list.asyncio(
                client=self.client, last_updated_gt=[last_run], ordering="-id"
            ),
            dcim_device_types_list.asyncio(
                client=self.client, last_updated_gt=[last_run], ordering="-id"
            ),
            dcim_manufacturers_list.asyncio(
                client=self.client, last_updated_gt=[last_run], ordering="-id"
            ),
            return_exceptions=True,
        )

        try:
            devices_result = validate_response(devices_result)
            devices = {device.id: device for device in devices_result.results}
        except UnexpectedStatus as e:
            logger.error(f"Failed to fetch devices: {e.status_code}")
            devices = {}

        try:
            software_results = validate_response(software_results)
            software = {sw.id: sw for sw in software_results.results}
        except UnexpectedStatus as e:
            logger.error(f"Failed to fetch software: {e.status_code} {e.content}")
            if e.status_code == 404:
                logger.warning(
                    "Received 404 when fetching software. This might be because the D3C plugin is not installed on the provided netbox instance."
                )
            software = {}

        try:
            device_types_result = validate_response(device_types_result)
            device_types = {
                device_type.id: device_type
                for device_type in device_types_result.results
            }
        except UnexpectedStatus as e:
            logger.error(f"Failed to fetch device_types: {e.status_code}")
            device_types = {}

        try:
            manufacturers_result = validate_response(manufacturers_result)
            manufacturers = {
                manufacturer.id: manufacturer
                for manufacturer in manufacturers_result.results
            }
        except UnexpectedStatus as e:
            logger.error(f"Failed to fetch manufacturers: {e.status_code}")
            manufacturers = {}

        # TODO: Maybe we can use graphql instead to reduce the amount of communication needed?
        if manufacturers:
            # Extend the devices we need to update with devices that received an update to the manufacturer only.
            if devices_result := await dcim_devices_list.asyncio(
                client=self.client,
                manufacturer_id=list(manufacturers.keys()),
                id_n=list(devices.keys()),
                ordering="-id",
            ):
                for device in devices_result.results:
                    if device.id not in devices:
                        devices[device.id] = device

            try:
                software_results = await plugins_d3c_software_list_list.asyncio(
                    client=self.client, id_n=list(software.keys()), ordering="-id"
                )
                software_results = validate_response(software_results)
                for sw in software_results.results:
                    # TODO: The netbox api needs to support filtering on manufacturer_id
                    if sw.id not in software and sw.manufacturer.id in manufacturers:
                        software[sw.id] = sw
            except UnexpectedStatus as e:
                logger.error(f"Failed to fetch software: {e.status_code}")
                if e.status_code == 404:
                    logger.warning(
                        "Received 404 when fetching software. This might be because the D3C plugin is not installed on the provided netbox instance."
                    )
                software = {}

        # Extend the devices we need to update with devices that received an update to the device_type only.
        if device_types:
            if devices_result := await dcim_devices_list.asyncio(
                client=self.client,
                device_type_id=list(device_types.keys()),
                id_n=list(devices.keys()),
                ordering="-id",
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
                    client=self.client, id=list(missing_device_type_ids), ordering="-id"
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
                    ordering="-id",
                ):
                    manufacturers.update(
                        {
                            manufacturer.id: manufacturer
                            for manufacturer in manufacturers_result.results
                        }
                    )

        if software:
            missing_manufacturer_ids = {
                sw.manufacturer.id
                for sw in software.values()
                if sw.manufacturer.id not in manufacturers
            }
            if missing_manufacturer_ids:
                if manufacturers_result := await dcim_manufacturers_list.asyncio(
                    client=self.client,
                    id=list(missing_manufacturer_ids),
                    ordering="-id",
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
                asset.uri = self.build_resource_uri(origin_info)
            else:
                asset = Asset(
                    product=Product(),
                    last_update=current_time,
                    origin_uri=str(self.origin_uri),
                    origin_info=origin_info,
                    uri=self.build_resource_uri(origin_info),
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
                asset.uri = self.build_resource_uri(origin_info)
            else:
                asset = Asset(
                    product=Product(),
                    last_update=current_time,
                    origin_uri=str(self.origin_uri),
                    origin_info=origin_info,
                    uri=self.build_resource_uri(origin_info),
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

        try:
            response = await plugins_d3c_productrelationship_list_list.asyncio(
                client=self.client, last_updated_gt=[last_run], ordering="-id"
            )
            response = validate_response(response)
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
        except UnexpectedStatus as e:
            logger.error(f"Failed to fetch relationships: {e.status_code}")
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
            dcim_devices_list.asyncio(
                client=self.client, id=list(devices.keys()), ordering="-id"
            ),
            plugins_d3c_software_list_list.asyncio(
                client=self.client, id=list(software_set.keys()), ordering="-id"
            ),
            return_exceptions=True,
        )

        decisions: List[CleanUpDecision] = []

        try:
            devices_result = validate_response(devices_result)
            for device in devices_result.results:
                # The device still exists. Remove it from the set and mark it as kept
                kept_device = devices.pop(device.id)
                decisions.append(
                    CleanUpDecision(can_delete=False, id=kept_device.id, ty=Asset)
                )
        except UnexpectedStatus as e:
            logger.error(f"Failed to fetch devices: {e.status_code}")

        try:
            software_result = validate_response(software_result)
            for software in software_result.results:
                kept_software = software_set.pop(software.id)
                decisions.append(
                    CleanUpDecision(can_delete=False, id=kept_software.id, ty=Asset)
                )
        except UnexpectedStatus as e:
            logger.error(f"Failed to fetch software: {e.status_code}")

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
        try:
            response = await plugins_d3c_productrelationship_list_list.asyncio(
                client=self.client, id=list(existing_relations.keys()), ordering="-id"
            )
            response = validate_response(response)
            for relation in response.results:
                kept_relation = existing_relations.pop(relation.id)
                kept_relation.can_delete = False
                result.append(kept_relation)

            for existing_relation in existing_relations.values():
                existing_relation.can_delete = True
                result.append(existing_relation)
        except UnexpectedStatus as e:
            logger.error(f"Failed to fetch relationships: {e.status_code}")

        return result

    async def notify_new_matches(self, new_matches: List[Match]):
        class BulkBody:
            def __init__(self, items: List[Any]):
                self.items = items

            def to_dict(self):
                return [item.to_dict() for item in self.items]

        # Monkey patch the response parser to always return None.
        from dina.plugins.datasource.netbox.generated.api_client.models import CsafMatch

        def parse_response_monkey(
            *, client, response: httpx.Response
        ) -> CsafMatch | None:
            if response.status_code == 201:
                return None

            if client.raise_on_unexpected_status:
                from dina.plugins.datasource.netbox.generated.api_client import errors

                raise errors.UnexpectedStatus(response.status_code, response.content)
            else:
                return None

        plugins_csaf_csafmatch_list_create._parse_response = parse_response_monkey

        batch_size = 100
        for i in range(0, len(new_matches), batch_size):
            batch = new_matches[i : i + batch_size]
            try:
                await plugins_csaf_csafmatch_list_create.asyncio(
                    client=self.client,
                    body=BulkBody(
                        [
                            CsafMatchRequest(
                                csaf_document=match.csaf_product.uri,
                                device=(match.asset.origin_info or {}).get(
                                    "device_id", UNSET
                                ),
                                software=(match.asset.origin_info or {}).get(
                                    "software_id", UNSET
                                ),
                                product_name_id=(
                                    match.csaf_product.origin_info or {}
                                ).get("product_name_id", UNSET),
                                score=match.score,
                                time=datetime.fromtimestamp(
                                    match.timestamp or time.time()
                                ),
                            )
                            for match in batch
                        ]
                    ),  # type: ignore
                )
            except (httpx.HTTPError, UnexpectedStatus) as e:
                logger.error(f"Failed to notify new matches: {e}")

    @property
    def origin_uri(self):
        return self.config.DataSource.Plugin.api_url

    def endpoint_info(self) -> str:
        return f"{self.config.DataSource.Plugin.api_url}"

    def build_resource_path(self, origin_info: dict[str, Any]) -> str:
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


def validate_response[T](response: T | BaseException | None) -> T:
    if response is None:
        raise RuntimeError("No response")
    if isinstance(response, BaseException):
        raise response
    return response
