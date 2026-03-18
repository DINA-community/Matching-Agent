"""
NetBox Data Source Plugin Module

This module provides integration with NetBox as a data source for asset and vulnerability management.
It synchronizes devices, software, and their relationships from a NetBox instance, supporting both
the core NetBox DCIM API and the optional D3C plugin for software inventory.

The plugin handles incremental synchronization of assets and relationships, cleanup of stale data,
and optionally pushes vulnerability matches back to NetBox when the CSAF plugin is installed.

Dependencies:
    - NetBox instance with API access
    - Optional: D3C plugin for software inventory
    - Optional: CSAF plugin for vulnerability match notifications
"""

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
    dcim_module_types_list,
    dcim_modules_list,
)
from dina.plugins.datasource.netbox.generated.api_client.api.plugins import (
    plugins_d3c_productrelationship_list_list,
    plugins_d3c_software_list_list,
    plugins_csaf_csafmatch_list_create,
)
from dina.plugins.datasource.netbox.generated.api_client.errors import UnexpectedStatus
from dina.plugins.datasource.netbox.generated.api_client.models import (
    DeviceTypeCustomFields,
    ModuleTypeCustomFields,
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
    """
    NetBox data source plugin for synchronizing assets from a NetBox instance.

    Fetches devices, device types, manufacturers, and optionally software inventory
    from NetBox. Supports incremental updates and bidirectional synchronization of
    vulnerability matches.

    Caveats:
        - Requires valid API token with appropriate permissions
        - Software inventory requires D3C plugin to be installed on NetBox
        - Match notifications require CSAF plugin to be installed on NetBox
        - Authentication failures (403) will raise RuntimeError with guidance
    """

    class Config(BaseModel):
        """Configuration schema for NetBox data source."""

        api_url: HttpUrl
        api_token: str

    def __init__(self, config: DataSourcePlugin.Config):
        """
        Initialize the NetBox data source plugin.

        Args:
            config: Plugin configuration including api_url and api_token

        Raises:
            KeyError: If required configuration parameters are missing
        """
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
        """Fetch device, module, and software products updated since the last run."""
        last_run = (await fetcher_view.last_run()).astimezone(tz=timezone.utc)
        current_time = time.time()

        # We fetch products and their type/manufacturer records and then include products
        # whose related records changed (e.g., manufacturer/type updates).
        (
            devices_result,
            modules_result,
            software_results,
            device_types_result,
            module_types_result,
            manufacturers_result,
        ) = await asyncio.gather(
            dcim_devices_list.asyncio(
                client=self.client, last_updated_gt=[last_run], ordering="-id"
            ),
            dcim_modules_list.asyncio(
                client=self.client, last_updated_gt=[last_run], ordering="-id"
            ),
            plugins_d3c_software_list_list.asyncio(
                client=self.client, last_updated_gt=[last_run], ordering="-id"
            ),
            dcim_device_types_list.asyncio(
                client=self.client, last_updated_gt=[last_run], ordering="-id"
            ),
            dcim_module_types_list.asyncio(
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
            if e.status_code == 403:
                raise RuntimeError(
                    "Could not authenticate with the netbox instance. "
                    "Probably invalid access token. "
                    "Please make sure to correctly configure your access token in the plugin configuration."
                ) from e

        try:
            modules_result = validate_response(modules_result)
            modules = {module.id: module for module in modules_result.results}
        except UnexpectedStatus as e:
            logger.error(f"Failed to fetch modules: {e.status_code}")
            modules = {}

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
            module_types_result = validate_response(module_types_result)
            module_types = {
                module_type.id: module_type
                for module_type in module_types_result.results
            }
        except UnexpectedStatus as e:
            logger.error(f"Failed to fetch module_types: {e.status_code}")
            module_types = {}

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

            if modules_result := await dcim_modules_list.asyncio(
                client=self.client,
                manufacturer_id=list(manufacturers.keys()),
                id_n=list(modules.keys()),
                ordering="-id",
            ):
                for module in modules_result.results:
                    if module.id not in modules:
                        modules[module.id] = module

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

        # Extend modules with updates that only changed module_type.
        if module_types:
            if modules_result := await dcim_modules_list.asyncio(
                client=self.client,
                module_type_id=list(module_types.keys()),
                id_n=list(modules.keys()),
                ordering="-id",
            ):
                for module in modules_result.results:
                    if module.id not in modules:
                        modules[module.id] = module

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

        # Fetch missing module types and manufacturers.
        if modules:
            missing_module_type_ids = {
                module.module_type.id
                for module in modules.values()
                if module.module_type.id not in module_types
            }
            if missing_module_type_ids:
                if module_types_result := await dcim_module_types_list.asyncio(
                    client=self.client, id=list(missing_module_type_ids), ordering="-id"
                ):
                    module_types.update(
                        {
                            module_type.id: module_type
                            for module_type in module_types_result.results
                        }
                    )

            missing_manufacturer_ids = {
                module.module_type.manufacturer.id
                for module in modules.values()
                if module.module_type.manufacturer.id not in manufacturers
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

        existing_module_assets = {
            module.origin_info["module_id"]: module
            for module in await fetcher_view.get_existing(
                Asset,
                Asset.origin_info["module_id"]
                .astext.cast(Integer)
                .in_(list(modules.keys())),
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
            product = asset.product
            if isinstance(device_type.part_number, str):
                product.part_numbers = [device_type.part_number]
            if isinstance(device_type.custom_fields, DeviceTypeCustomFields):
                props = device_type.custom_fields.additional_properties

                model_num = props.get("model_number")
                product.model_numbers = [model_num] if model_num is not None else []
                product.hardware_name = props.get("hardware_name")

                versions = props.get("hardware_version")
                product.version = versions if versions is not None else []
                product.device_family = props.get("device_family")
                product.cpe = props.get("cpe")

            product.manufacturer_name = manufacturer.name
            assets.append(asset)

        for module in modules.values():
            logger.debug(f"Adding asset for module: {module.display}")
            module_type = module_types[module.module_type.id]
            manufacturer = manufacturers[module_type.manufacturer.id]
            origin_info = {
                "module_id": module.id,
                "module_type_id": module_type.id,
                "manufacturer_id": manufacturer.id,
            }

            if asset := existing_module_assets.get(module.id, None):
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

            asset.product.product_type = ProductType.Module
            if isinstance(module.display, str):
                asset.product.name = module.display
            if isinstance(module.serial, str):
                asset.product.serial_numbers = [module.serial]

            asset.product.model = module_type.model
            product = asset.product
            if isinstance(module_type.part_number, str):
                product.part_numbers = [module_type.part_number]
            if isinstance(module_type.custom_fields, ModuleTypeCustomFields):
                props = module_type.custom_fields.additional_properties

                model_num = props.get("model_number")
                product.model_numbers = [model_num] if model_num is not None else []
                product.hardware_name = props.get("hardware_name")

                versions = props.get("hardware_version")
                product.version = versions if versions is not None else []
                product.device_family = props.get("device_family")
                product.cpe = props.get("cpe")

            product.manufacturer_name = manufacturer.name
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
        """
        Fetch product relationships that have been updated since the last run.

        Retrieves parent-child relationships between devices and software from NetBox's
        D3C plugin, representing installation or dependency relationships.

        Args:
            fetcher_view: Database view for accessing last run metadata

        Returns:
            FetchRelationshipsResult containing list of Relationship objects

        Caveats:
            - Requires D3C plugin to be installed on NetBox
            - Returns empty result if plugin is not available (404 error)
        """
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
        """
        Map NetBox relationships to internal database asset IDs.

        Translates NetBox product IDs (device_id, module_id, software_id) to internal Asset table
        primary keys, filtering out relationships where either endpoint is not found.
        Deduplicates relationships by (parent, child) pair.

        Args:
            fetcher_view: Database view for querying existing assets
            relations: List of relationships with NetBox IDs

        Returns:
            List of MappedRelationship objects with internal database IDs

        Raises:
            RuntimeError: If a product type is neither Device, Module, nor Software
        """
        device_ids = set()
        module_ids = set()
        software_ids = set()
        for relation in relations:
            match relation.parent.product_type:
                case ProductType.Device:
                    device_ids.add(relation.parent.id)
                case ProductType.Module:
                    module_ids.add(relation.parent.id)
                case ProductType.Software:
                    software_ids.add(relation.parent.id)
                case _:
                    raise RuntimeError("Invalid device type")
            match relation.child.product_type:
                case ProductType.Device:
                    device_ids.add(relation.child.id)
                case ProductType.Module:
                    module_ids.add(relation.child.id)
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
        modules = {
            module.origin_info["module_id"]: module.id
            for module in await fetcher_view.get_existing(
                Asset,
                Asset.origin_info["module_id"]
                .astext.cast(Integer)
                .in_(list(module_ids)),
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
                case ProductType.Module:
                    parent_id = modules[relation.parent.id]
                case ProductType.Software:
                    parent_id = software[relation.parent.id]
                case _:
                    raise RuntimeError(
                        f"Relation parent {relation.parent.id} has unknown type"
                    )
            match relation.child.product_type:
                case ProductType.Device:
                    child_id = devices[relation.child.id]
                case ProductType.Module:
                    child_id = modules[relation.child.id]
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
        """
        Verify which assets still exist in NetBox and mark stale assets for deletion.

        Queries NetBox to check if devices, modules, and software still exist. Assets that are
        no longer present in NetBox are marked for deletion from the local database.

        Args:
            data_to_check: List of assets to verify

        Returns:
            List of CleanUpDecision objects indicating which assets can be deleted

        Caveats:
            - May return incomplete results if NetBox API calls fail
            - Failed API calls are logged but don't prevent processing other assets
        """
        logger.debug(f"Cleanup data: {data_to_check}")
        if not data_to_check:
            return []
        devices = {
            int(d.origin_info["device_id"]): d
            for d in data_to_check
            if d.product.product_type == ProductType.Device
        }
        modules = {
            int(d.origin_info["module_id"]): d
            for d in data_to_check
            if d.product.product_type == ProductType.Module
        }
        software_set = {
            int(d.origin_info["software_id"]): d
            for d in data_to_check
            if d.product.product_type == ProductType.Software
        }

        devices_result, modules_result, software_result = await asyncio.gather(
            dcim_devices_list.asyncio(
                client=self.client, id=list(devices.keys()), ordering="-id"
            ),
            dcim_modules_list.asyncio(
                client=self.client, id=list(modules.keys()), ordering="-id"
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
            modules_result = validate_response(modules_result)
            for module in modules_result.results:
                kept_module = modules.pop(module.id)
                decisions.append(
                    CleanUpDecision(can_delete=False, id=kept_module.id, ty=Asset)
                )
        except UnexpectedStatus as e:
            logger.error(f"Failed to fetch modules: {e.status_code}")

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
                modules.values(),
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
        """
        Verify which relationships still exist in NetBox and mark stale ones for deletion.

        Queries NetBox to check if product relationships still exist. Relationships that
        are no longer present are marked for deletion from the local database.

        Args:
            relationships_to_check: List of relationships to verify

        Returns:
            List of MappedRelationship objects with can_delete flag set appropriately

        Caveats:
            - Requires D3C plugin to be installed on NetBox
            - Returns incomplete results if API call fails (logged but not raised)
        """
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
        """
        Push newly discovered vulnerability matches back to NetBox.

        Sends CSAF vulnerability matches to NetBox in batches, creating records that
        associate assets with affected products from CSAF documents. This enables
        vulnerability tracking within NetBox.

        Args:
            new_matches: List of Match objects representing vulnerabilities found

        Caveats:
            - Requires CSAF plugin to be installed on NetBox
            - Failures are logged but do not raise exceptions
            - Processes in batches of 100 to avoid overwhelming the API
        """

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

        def to_csaf_match_request(match: Match) -> CsafMatchRequest:
            request = CsafMatchRequest(
                csaf_document=match.csaf_product.document_url(),
                device=(match.asset.origin_info or {}).get("device_id", UNSET),
                software=(match.asset.origin_info or {}).get("software_id", UNSET),
                module=(match.asset.origin_info or {}).get("module_id", UNSET),
                product_name_id=match.csaf_product.product_id(),
                score=match.score,
                description=match.status,
                time=datetime.fromtimestamp(match.timestamp or time.time()),
            )
            module_id = (match.asset.origin_info or {}).get("module_id", UNSET)
            if module_id is not UNSET:
                request["module"] = module_id
            return request

        batch_size = 100
        for i in range(0, len(new_matches), batch_size):
            batch = new_matches[i : i + batch_size]
            try:
                await plugins_csaf_csafmatch_list_create.asyncio(
                    client=self.client,
                    body=BulkBody([to_csaf_match_request(match) for match in batch]),  # type: ignore
                )
            except (httpx.HTTPError, UnexpectedStatus) as e:
                logger.error(f"Failed to notify new matches: {e}")

    @property
    def origin_uri(self):
        """
        Get the base URI of the NetBox instance.

        Returns:
            Base URL of the configured NetBox API
        """
        return self.config.DataSource.Plugin.api_url

    def endpoint_info(self) -> str:
        """
        Get human-readable information about the NetBox endpoint.

        Returns:
            Base URL of the NetBox instance
        """
        return f"{self.config.DataSource.Plugin.api_url}"

    def build_resource_path(self, origin_info: dict[str, Any]) -> str:
        """
        Construct the API path for a specific resource in NetBox.

        Generates the appropriate NetBox API endpoint path based on the resource type
        (device, module, software, or relationship) encoded in the origin_info dictionary.

        Args:
            origin_info: Dictionary containing resource type and ID information

        Returns:
            API path string (e.g., "/api/dcim/devices/123/") or empty string on error
        """
        try:
            if "device_id" in origin_info:
                return f"/api/dcim/devices/{int(origin_info['device_id'])}/"
            if "module_id" in origin_info:
                return f"/api/dcim/modules/{int(origin_info['module_id'])}/"
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
    Map NetBox content type strings to ProductType enumeration values.

    Args:
        netbox_type: NetBox content type string (e.g., "dcim.device", "dcim.module", "d3c.software")

    Returns:
        ProductType.Device for "dcim.device"
        ProductType.Module for "dcim.module"
        ProductType.Software for "d3c.software"
        ProductType.Undefined for unknown types
    """
    if netbox_type == "dcim.device":
        return ProductType.Device
    elif netbox_type == "dcim.module":
        return ProductType.Module
    elif netbox_type == "d3c.software":
        return ProductType.Software
    else:
        return ProductType.Undefined


def validate_response[T](response: T | BaseException | None) -> T:
    """
    Validate and unwrap API response objects.

    Helper function to handle responses from asyncio.gather with return_exceptions=True.
    Raises any exceptions that occurred during the API call, or raises RuntimeError
    if the response is None.

    Args:
        response: API response, exception, or None

    Returns:
        The unwrapped response object

    Raises:
        RuntimeError: If response is None
        BaseException: If response is an exception, re-raises it
    """
    if response is None:
        raise RuntimeError("No response")
    if isinstance(response, BaseException):
        raise response
    return response
