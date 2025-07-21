import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dcim_devices_list_airflow import DcimDevicesListAirflow
from ...models.paginated_device_with_config_context_list import (
    PaginatedDeviceWithConfigContextList,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    airflow: Union[Unset, DcimDevicesListAirflow] = UNSET,
    asset_tag: Union[Unset, list[str]] = UNSET,
    asset_tag_empty: Union[Unset, bool] = UNSET,
    asset_tag_ic: Union[Unset, list[str]] = UNSET,
    asset_tag_ie: Union[Unset, list[str]] = UNSET,
    asset_tag_iew: Union[Unset, list[str]] = UNSET,
    asset_tag_isw: Union[Unset, list[str]] = UNSET,
    asset_tag_n: Union[Unset, list[str]] = UNSET,
    asset_tag_nic: Union[Unset, list[str]] = UNSET,
    asset_tag_nie: Union[Unset, list[str]] = UNSET,
    asset_tag_niew: Union[Unset, list[str]] = UNSET,
    asset_tag_nisw: Union[Unset, list[str]] = UNSET,
    cluster_group: Union[Unset, list[str]] = UNSET,
    cluster_group_n: Union[Unset, list[str]] = UNSET,
    cluster_group_id: Union[Unset, list[int]] = UNSET,
    cluster_group_id_n: Union[Unset, list[int]] = UNSET,
    cluster_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cluster_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    config_template_id: Union[Unset, list[Union[None, int]]] = UNSET,
    config_template_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    console_port_count: Union[Unset, list[int]] = UNSET,
    console_port_count_empty: Union[Unset, bool] = UNSET,
    console_port_count_gt: Union[Unset, list[int]] = UNSET,
    console_port_count_gte: Union[Unset, list[int]] = UNSET,
    console_port_count_lt: Union[Unset, list[int]] = UNSET,
    console_port_count_lte: Union[Unset, list[int]] = UNSET,
    console_port_count_n: Union[Unset, list[int]] = UNSET,
    console_ports: Union[Unset, bool] = UNSET,
    console_server_port_count: Union[Unset, list[int]] = UNSET,
    console_server_port_count_empty: Union[Unset, bool] = UNSET,
    console_server_port_count_gt: Union[Unset, list[int]] = UNSET,
    console_server_port_count_gte: Union[Unset, list[int]] = UNSET,
    console_server_port_count_lt: Union[Unset, list[int]] = UNSET,
    console_server_port_count_lte: Union[Unset, list[int]] = UNSET,
    console_server_port_count_n: Union[Unset, list[int]] = UNSET,
    console_server_ports: Union[Unset, bool] = UNSET,
    contact: Union[Unset, list[int]] = UNSET,
    contact_n: Union[Unset, list[int]] = UNSET,
    contact_group: Union[Unset, list[str]] = UNSET,
    contact_group_n: Union[Unset, list[str]] = UNSET,
    contact_role: Union[Unset, list[int]] = UNSET,
    contact_role_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    description: Union[Unset, list[str]] = UNSET,
    description_empty: Union[Unset, bool] = UNSET,
    description_ic: Union[Unset, list[str]] = UNSET,
    description_ie: Union[Unset, list[str]] = UNSET,
    description_iew: Union[Unset, list[str]] = UNSET,
    description_isw: Union[Unset, list[str]] = UNSET,
    description_n: Union[Unset, list[str]] = UNSET,
    description_nic: Union[Unset, list[str]] = UNSET,
    description_nie: Union[Unset, list[str]] = UNSET,
    description_niew: Union[Unset, list[str]] = UNSET,
    description_nisw: Union[Unset, list[str]] = UNSET,
    device_bay_count: Union[Unset, list[int]] = UNSET,
    device_bay_count_empty: Union[Unset, bool] = UNSET,
    device_bay_count_gt: Union[Unset, list[int]] = UNSET,
    device_bay_count_gte: Union[Unset, list[int]] = UNSET,
    device_bay_count_lt: Union[Unset, list[int]] = UNSET,
    device_bay_count_lte: Union[Unset, list[int]] = UNSET,
    device_bay_count_n: Union[Unset, list[int]] = UNSET,
    device_bays: Union[Unset, bool] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    front_port_count: Union[Unset, list[int]] = UNSET,
    front_port_count_empty: Union[Unset, bool] = UNSET,
    front_port_count_gt: Union[Unset, list[int]] = UNSET,
    front_port_count_gte: Union[Unset, list[int]] = UNSET,
    front_port_count_lt: Union[Unset, list[int]] = UNSET,
    front_port_count_lte: Union[Unset, list[int]] = UNSET,
    front_port_count_n: Union[Unset, list[int]] = UNSET,
    has_oob_ip: Union[Unset, bool] = UNSET,
    has_primary_ip: Union[Unset, bool] = UNSET,
    has_virtual_device_context: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_count: Union[Unset, list[int]] = UNSET,
    interface_count_empty: Union[Unset, bool] = UNSET,
    interface_count_gt: Union[Unset, list[int]] = UNSET,
    interface_count_gte: Union[Unset, list[int]] = UNSET,
    interface_count_lt: Union[Unset, list[int]] = UNSET,
    interface_count_lte: Union[Unset, list[int]] = UNSET,
    interface_count_n: Union[Unset, list[int]] = UNSET,
    interfaces: Union[Unset, bool] = UNSET,
    inventory_item_count: Union[Unset, list[int]] = UNSET,
    inventory_item_count_empty: Union[Unset, bool] = UNSET,
    inventory_item_count_gt: Union[Unset, list[int]] = UNSET,
    inventory_item_count_gte: Union[Unset, list[int]] = UNSET,
    inventory_item_count_lt: Union[Unset, list[int]] = UNSET,
    inventory_item_count_lte: Union[Unset, list[int]] = UNSET,
    inventory_item_count_n: Union[Unset, list[int]] = UNSET,
    is_full_depth: Union[Unset, bool] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    latitude: Union[Unset, list[float]] = UNSET,
    latitude_empty: Union[Unset, bool] = UNSET,
    latitude_gt: Union[Unset, list[float]] = UNSET,
    latitude_gte: Union[Unset, list[float]] = UNSET,
    latitude_lt: Union[Unset, list[float]] = UNSET,
    latitude_lte: Union[Unset, list[float]] = UNSET,
    latitude_n: Union[Unset, list[float]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    local_context_data: Union[Unset, bool] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[str]] = UNSET,
    location_id_n: Union[Unset, list[str]] = UNSET,
    longitude: Union[Unset, list[float]] = UNSET,
    longitude_empty: Union[Unset, bool] = UNSET,
    longitude_gt: Union[Unset, list[float]] = UNSET,
    longitude_gte: Union[Unset, list[float]] = UNSET,
    longitude_lt: Union[Unset, list[float]] = UNSET,
    longitude_lte: Union[Unset, list[float]] = UNSET,
    longitude_n: Union[Unset, list[float]] = UNSET,
    mac_address: Union[Unset, list[str]] = UNSET,
    mac_address_ic: Union[Unset, list[str]] = UNSET,
    mac_address_ie: Union[Unset, list[str]] = UNSET,
    mac_address_iew: Union[Unset, list[str]] = UNSET,
    mac_address_isw: Union[Unset, list[str]] = UNSET,
    mac_address_n: Union[Unset, list[str]] = UNSET,
    mac_address_nic: Union[Unset, list[str]] = UNSET,
    mac_address_nie: Union[Unset, list[str]] = UNSET,
    mac_address_niew: Union[Unset, list[str]] = UNSET,
    mac_address_nisw: Union[Unset, list[str]] = UNSET,
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    model: Union[Unset, list[str]] = UNSET,
    model_n: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_bay_count: Union[Unset, list[int]] = UNSET,
    module_bay_count_empty: Union[Unset, bool] = UNSET,
    module_bay_count_gt: Union[Unset, list[int]] = UNSET,
    module_bay_count_gte: Union[Unset, list[int]] = UNSET,
    module_bay_count_lt: Union[Unset, list[int]] = UNSET,
    module_bay_count_lte: Union[Unset, list[int]] = UNSET,
    module_bay_count_n: Union[Unset, list[int]] = UNSET,
    module_bays: Union[Unset, bool] = UNSET,
    name: Union[Unset, list[str]] = UNSET,
    name_empty: Union[Unset, bool] = UNSET,
    name_ic: Union[Unset, list[str]] = UNSET,
    name_ie: Union[Unset, list[str]] = UNSET,
    name_iew: Union[Unset, list[str]] = UNSET,
    name_isw: Union[Unset, list[str]] = UNSET,
    name_n: Union[Unset, list[str]] = UNSET,
    name_nic: Union[Unset, list[str]] = UNSET,
    name_nie: Union[Unset, list[str]] = UNSET,
    name_niew: Union[Unset, list[str]] = UNSET,
    name_nisw: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    oob_ip_id: Union[Unset, list[int]] = UNSET,
    oob_ip_id_n: Union[Unset, list[int]] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_bay_id: Union[Unset, list[int]] = UNSET,
    parent_bay_id_n: Union[Unset, list[int]] = UNSET,
    parent_device_id: Union[Unset, list[int]] = UNSET,
    parent_device_id_n: Union[Unset, list[int]] = UNSET,
    pass_through_ports: Union[Unset, bool] = UNSET,
    platform: Union[Unset, list[str]] = UNSET,
    platform_n: Union[Unset, list[str]] = UNSET,
    platform_id: Union[Unset, list[Union[None, int]]] = UNSET,
    platform_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    position: Union[Unset, list[float]] = UNSET,
    position_empty: Union[Unset, bool] = UNSET,
    position_gt: Union[Unset, list[float]] = UNSET,
    position_gte: Union[Unset, list[float]] = UNSET,
    position_lt: Union[Unset, list[float]] = UNSET,
    position_lte: Union[Unset, list[float]] = UNSET,
    position_n: Union[Unset, list[float]] = UNSET,
    power_outlet_count: Union[Unset, list[int]] = UNSET,
    power_outlet_count_empty: Union[Unset, bool] = UNSET,
    power_outlet_count_gt: Union[Unset, list[int]] = UNSET,
    power_outlet_count_gte: Union[Unset, list[int]] = UNSET,
    power_outlet_count_lt: Union[Unset, list[int]] = UNSET,
    power_outlet_count_lte: Union[Unset, list[int]] = UNSET,
    power_outlet_count_n: Union[Unset, list[int]] = UNSET,
    power_outlets: Union[Unset, bool] = UNSET,
    power_port_count: Union[Unset, list[int]] = UNSET,
    power_port_count_empty: Union[Unset, bool] = UNSET,
    power_port_count_gt: Union[Unset, list[int]] = UNSET,
    power_port_count_gte: Union[Unset, list[int]] = UNSET,
    power_port_count_lt: Union[Unset, list[int]] = UNSET,
    power_port_count_lte: Union[Unset, list[int]] = UNSET,
    power_port_count_n: Union[Unset, list[int]] = UNSET,
    power_ports: Union[Unset, bool] = UNSET,
    primary_ip4: Union[Unset, list[str]] = UNSET,
    primary_ip4_n: Union[Unset, list[str]] = UNSET,
    primary_ip4_id: Union[Unset, list[int]] = UNSET,
    primary_ip4_id_n: Union[Unset, list[int]] = UNSET,
    primary_ip6: Union[Unset, list[str]] = UNSET,
    primary_ip6_n: Union[Unset, list[str]] = UNSET,
    primary_ip6_id: Union[Unset, list[int]] = UNSET,
    primary_ip6_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    rear_port_count: Union[Unset, list[int]] = UNSET,
    rear_port_count_empty: Union[Unset, bool] = UNSET,
    rear_port_count_gt: Union[Unset, list[int]] = UNSET,
    rear_port_count_gte: Union[Unset, list[int]] = UNSET,
    rear_port_count_lt: Union[Unset, list[int]] = UNSET,
    rear_port_count_lte: Union[Unset, list[int]] = UNSET,
    rear_port_count_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[str]] = UNSET,
    role_id_n: Union[Unset, list[str]] = UNSET,
    serial: Union[Unset, list[str]] = UNSET,
    serial_empty: Union[Unset, bool] = UNSET,
    serial_ic: Union[Unset, list[str]] = UNSET,
    serial_ie: Union[Unset, list[str]] = UNSET,
    serial_iew: Union[Unset, list[str]] = UNSET,
    serial_isw: Union[Unset, list[str]] = UNSET,
    serial_n: Union[Unset, list[str]] = UNSET,
    serial_nic: Union[Unset, list[str]] = UNSET,
    serial_nie: Union[Unset, list[str]] = UNSET,
    serial_niew: Union[Unset, list[str]] = UNSET,
    serial_nisw: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    status: Union[Unset, list[str]] = UNSET,
    status_empty: Union[Unset, bool] = UNSET,
    status_ic: Union[Unset, list[str]] = UNSET,
    status_ie: Union[Unset, list[str]] = UNSET,
    status_iew: Union[Unset, list[str]] = UNSET,
    status_isw: Union[Unset, list[str]] = UNSET,
    status_n: Union[Unset, list[str]] = UNSET,
    status_nic: Union[Unset, list[str]] = UNSET,
    status_nie: Union[Unset, list[str]] = UNSET,
    status_niew: Union[Unset, list[str]] = UNSET,
    status_nisw: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tenant: Union[Unset, list[str]] = UNSET,
    tenant_n: Union[Unset, list[str]] = UNSET,
    tenant_group: Union[Unset, list[str]] = UNSET,
    tenant_group_n: Union[Unset, list[str]] = UNSET,
    tenant_group_id: Union[Unset, list[str]] = UNSET,
    tenant_group_id_n: Union[Unset, list[str]] = UNSET,
    tenant_id: Union[Unset, list[Union[None, int]]] = UNSET,
    tenant_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    vc_position: Union[Unset, list[int]] = UNSET,
    vc_position_empty: Union[Unset, bool] = UNSET,
    vc_position_gt: Union[Unset, list[int]] = UNSET,
    vc_position_gte: Union[Unset, list[int]] = UNSET,
    vc_position_lt: Union[Unset, list[int]] = UNSET,
    vc_position_lte: Union[Unset, list[int]] = UNSET,
    vc_position_n: Union[Unset, list[int]] = UNSET,
    vc_priority: Union[Unset, list[int]] = UNSET,
    vc_priority_empty: Union[Unset, bool] = UNSET,
    vc_priority_gt: Union[Unset, list[int]] = UNSET,
    vc_priority_gte: Union[Unset, list[int]] = UNSET,
    vc_priority_lt: Union[Unset, list[int]] = UNSET,
    vc_priority_lte: Union[Unset, list[int]] = UNSET,
    vc_priority_n: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id_n: Union[Unset, list[int]] = UNSET,
    virtual_chassis_member: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_airflow: Union[Unset, str] = UNSET
    if not isinstance(airflow, Unset):
        json_airflow = airflow.value

    params["airflow"] = json_airflow

    json_asset_tag: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag, Unset):
        json_asset_tag = asset_tag

    params["asset_tag"] = json_asset_tag

    params["asset_tag__empty"] = asset_tag_empty

    json_asset_tag_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag_ic, Unset):
        json_asset_tag_ic = asset_tag_ic

    params["asset_tag__ic"] = json_asset_tag_ic

    json_asset_tag_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag_ie, Unset):
        json_asset_tag_ie = asset_tag_ie

    params["asset_tag__ie"] = json_asset_tag_ie

    json_asset_tag_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag_iew, Unset):
        json_asset_tag_iew = asset_tag_iew

    params["asset_tag__iew"] = json_asset_tag_iew

    json_asset_tag_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag_isw, Unset):
        json_asset_tag_isw = asset_tag_isw

    params["asset_tag__isw"] = json_asset_tag_isw

    json_asset_tag_n: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag_n, Unset):
        json_asset_tag_n = asset_tag_n

    params["asset_tag__n"] = json_asset_tag_n

    json_asset_tag_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag_nic, Unset):
        json_asset_tag_nic = asset_tag_nic

    params["asset_tag__nic"] = json_asset_tag_nic

    json_asset_tag_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag_nie, Unset):
        json_asset_tag_nie = asset_tag_nie

    params["asset_tag__nie"] = json_asset_tag_nie

    json_asset_tag_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag_niew, Unset):
        json_asset_tag_niew = asset_tag_niew

    params["asset_tag__niew"] = json_asset_tag_niew

    json_asset_tag_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag_nisw, Unset):
        json_asset_tag_nisw = asset_tag_nisw

    params["asset_tag__nisw"] = json_asset_tag_nisw

    json_cluster_group: Union[Unset, list[str]] = UNSET
    if not isinstance(cluster_group, Unset):
        json_cluster_group = cluster_group

    params["cluster_group"] = json_cluster_group

    json_cluster_group_n: Union[Unset, list[str]] = UNSET
    if not isinstance(cluster_group_n, Unset):
        json_cluster_group_n = cluster_group_n

    params["cluster_group__n"] = json_cluster_group_n

    json_cluster_group_id: Union[Unset, list[int]] = UNSET
    if not isinstance(cluster_group_id, Unset):
        json_cluster_group_id = cluster_group_id

    params["cluster_group_id"] = json_cluster_group_id

    json_cluster_group_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(cluster_group_id_n, Unset):
        json_cluster_group_id_n = cluster_group_id_n

    params["cluster_group_id__n"] = json_cluster_group_id_n

    json_cluster_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(cluster_id, Unset):
        json_cluster_id = []
        for cluster_id_item_data in cluster_id:
            cluster_id_item: Union[None, int]
            cluster_id_item = cluster_id_item_data
            json_cluster_id.append(cluster_id_item)

    params["cluster_id"] = json_cluster_id

    json_cluster_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(cluster_id_n, Unset):
        json_cluster_id_n = []
        for cluster_id_n_item_data in cluster_id_n:
            cluster_id_n_item: Union[None, int]
            cluster_id_n_item = cluster_id_n_item_data
            json_cluster_id_n.append(cluster_id_n_item)

    params["cluster_id__n"] = json_cluster_id_n

    json_config_template_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(config_template_id, Unset):
        json_config_template_id = []
        for config_template_id_item_data in config_template_id:
            config_template_id_item: Union[None, int]
            config_template_id_item = config_template_id_item_data
            json_config_template_id.append(config_template_id_item)

    params["config_template_id"] = json_config_template_id

    json_config_template_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(config_template_id_n, Unset):
        json_config_template_id_n = []
        for config_template_id_n_item_data in config_template_id_n:
            config_template_id_n_item: Union[None, int]
            config_template_id_n_item = config_template_id_n_item_data
            json_config_template_id_n.append(config_template_id_n_item)

    params["config_template_id__n"] = json_config_template_id_n

    json_console_port_count: Union[Unset, list[int]] = UNSET
    if not isinstance(console_port_count, Unset):
        json_console_port_count = console_port_count

    params["console_port_count"] = json_console_port_count

    params["console_port_count__empty"] = console_port_count_empty

    json_console_port_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(console_port_count_gt, Unset):
        json_console_port_count_gt = console_port_count_gt

    params["console_port_count__gt"] = json_console_port_count_gt

    json_console_port_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(console_port_count_gte, Unset):
        json_console_port_count_gte = console_port_count_gte

    params["console_port_count__gte"] = json_console_port_count_gte

    json_console_port_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(console_port_count_lt, Unset):
        json_console_port_count_lt = console_port_count_lt

    params["console_port_count__lt"] = json_console_port_count_lt

    json_console_port_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(console_port_count_lte, Unset):
        json_console_port_count_lte = console_port_count_lte

    params["console_port_count__lte"] = json_console_port_count_lte

    json_console_port_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(console_port_count_n, Unset):
        json_console_port_count_n = console_port_count_n

    params["console_port_count__n"] = json_console_port_count_n

    params["console_ports"] = console_ports

    json_console_server_port_count: Union[Unset, list[int]] = UNSET
    if not isinstance(console_server_port_count, Unset):
        json_console_server_port_count = console_server_port_count

    params["console_server_port_count"] = json_console_server_port_count

    params["console_server_port_count__empty"] = console_server_port_count_empty

    json_console_server_port_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(console_server_port_count_gt, Unset):
        json_console_server_port_count_gt = console_server_port_count_gt

    params["console_server_port_count__gt"] = json_console_server_port_count_gt

    json_console_server_port_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(console_server_port_count_gte, Unset):
        json_console_server_port_count_gte = console_server_port_count_gte

    params["console_server_port_count__gte"] = json_console_server_port_count_gte

    json_console_server_port_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(console_server_port_count_lt, Unset):
        json_console_server_port_count_lt = console_server_port_count_lt

    params["console_server_port_count__lt"] = json_console_server_port_count_lt

    json_console_server_port_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(console_server_port_count_lte, Unset):
        json_console_server_port_count_lte = console_server_port_count_lte

    params["console_server_port_count__lte"] = json_console_server_port_count_lte

    json_console_server_port_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(console_server_port_count_n, Unset):
        json_console_server_port_count_n = console_server_port_count_n

    params["console_server_port_count__n"] = json_console_server_port_count_n

    params["console_server_ports"] = console_server_ports

    json_contact: Union[Unset, list[int]] = UNSET
    if not isinstance(contact, Unset):
        json_contact = contact

    params["contact"] = json_contact

    json_contact_n: Union[Unset, list[int]] = UNSET
    if not isinstance(contact_n, Unset):
        json_contact_n = contact_n

    params["contact__n"] = json_contact_n

    json_contact_group: Union[Unset, list[str]] = UNSET
    if not isinstance(contact_group, Unset):
        json_contact_group = contact_group

    params["contact_group"] = json_contact_group

    json_contact_group_n: Union[Unset, list[str]] = UNSET
    if not isinstance(contact_group_n, Unset):
        json_contact_group_n = contact_group_n

    params["contact_group__n"] = json_contact_group_n

    json_contact_role: Union[Unset, list[int]] = UNSET
    if not isinstance(contact_role, Unset):
        json_contact_role = contact_role

    params["contact_role"] = json_contact_role

    json_contact_role_n: Union[Unset, list[int]] = UNSET
    if not isinstance(contact_role_n, Unset):
        json_contact_role_n = contact_role_n

    params["contact_role__n"] = json_contact_role_n

    json_created: Union[Unset, list[str]] = UNSET
    if not isinstance(created, Unset):
        json_created = []
        for created_item_data in created:
            created_item = created_item_data.isoformat()
            json_created.append(created_item)

    params["created"] = json_created

    json_created_empty: Union[Unset, list[str]] = UNSET
    if not isinstance(created_empty, Unset):
        json_created_empty = []
        for created_empty_item_data in created_empty:
            created_empty_item = created_empty_item_data.isoformat()
            json_created_empty.append(created_empty_item)

    params["created__empty"] = json_created_empty

    json_created_gt: Union[Unset, list[str]] = UNSET
    if not isinstance(created_gt, Unset):
        json_created_gt = []
        for created_gt_item_data in created_gt:
            created_gt_item = created_gt_item_data.isoformat()
            json_created_gt.append(created_gt_item)

    params["created__gt"] = json_created_gt

    json_created_gte: Union[Unset, list[str]] = UNSET
    if not isinstance(created_gte, Unset):
        json_created_gte = []
        for created_gte_item_data in created_gte:
            created_gte_item = created_gte_item_data.isoformat()
            json_created_gte.append(created_gte_item)

    params["created__gte"] = json_created_gte

    json_created_lt: Union[Unset, list[str]] = UNSET
    if not isinstance(created_lt, Unset):
        json_created_lt = []
        for created_lt_item_data in created_lt:
            created_lt_item = created_lt_item_data.isoformat()
            json_created_lt.append(created_lt_item)

    params["created__lt"] = json_created_lt

    json_created_lte: Union[Unset, list[str]] = UNSET
    if not isinstance(created_lte, Unset):
        json_created_lte = []
        for created_lte_item_data in created_lte:
            created_lte_item = created_lte_item_data.isoformat()
            json_created_lte.append(created_lte_item)

    params["created__lte"] = json_created_lte

    json_created_n: Union[Unset, list[str]] = UNSET
    if not isinstance(created_n, Unset):
        json_created_n = []
        for created_n_item_data in created_n:
            created_n_item = created_n_item_data.isoformat()
            json_created_n.append(created_n_item)

    params["created__n"] = json_created_n

    json_created_by_request: Union[Unset, str] = UNSET
    if not isinstance(created_by_request, Unset):
        json_created_by_request = str(created_by_request)
    params["created_by_request"] = json_created_by_request

    json_description: Union[Unset, list[str]] = UNSET
    if not isinstance(description, Unset):
        json_description = description

    params["description"] = json_description

    params["description__empty"] = description_empty

    json_description_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(description_ic, Unset):
        json_description_ic = description_ic

    params["description__ic"] = json_description_ic

    json_description_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(description_ie, Unset):
        json_description_ie = description_ie

    params["description__ie"] = json_description_ie

    json_description_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(description_iew, Unset):
        json_description_iew = description_iew

    params["description__iew"] = json_description_iew

    json_description_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(description_isw, Unset):
        json_description_isw = description_isw

    params["description__isw"] = json_description_isw

    json_description_n: Union[Unset, list[str]] = UNSET
    if not isinstance(description_n, Unset):
        json_description_n = description_n

    params["description__n"] = json_description_n

    json_description_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(description_nic, Unset):
        json_description_nic = description_nic

    params["description__nic"] = json_description_nic

    json_description_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(description_nie, Unset):
        json_description_nie = description_nie

    params["description__nie"] = json_description_nie

    json_description_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(description_niew, Unset):
        json_description_niew = description_niew

    params["description__niew"] = json_description_niew

    json_description_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(description_nisw, Unset):
        json_description_nisw = description_nisw

    params["description__nisw"] = json_description_nisw

    json_device_bay_count: Union[Unset, list[int]] = UNSET
    if not isinstance(device_bay_count, Unset):
        json_device_bay_count = device_bay_count

    params["device_bay_count"] = json_device_bay_count

    params["device_bay_count__empty"] = device_bay_count_empty

    json_device_bay_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(device_bay_count_gt, Unset):
        json_device_bay_count_gt = device_bay_count_gt

    params["device_bay_count__gt"] = json_device_bay_count_gt

    json_device_bay_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(device_bay_count_gte, Unset):
        json_device_bay_count_gte = device_bay_count_gte

    params["device_bay_count__gte"] = json_device_bay_count_gte

    json_device_bay_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(device_bay_count_lt, Unset):
        json_device_bay_count_lt = device_bay_count_lt

    params["device_bay_count__lt"] = json_device_bay_count_lt

    json_device_bay_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(device_bay_count_lte, Unset):
        json_device_bay_count_lte = device_bay_count_lte

    params["device_bay_count__lte"] = json_device_bay_count_lte

    json_device_bay_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(device_bay_count_n, Unset):
        json_device_bay_count_n = device_bay_count_n

    params["device_bay_count__n"] = json_device_bay_count_n

    params["device_bays"] = device_bays

    json_device_type: Union[Unset, list[str]] = UNSET
    if not isinstance(device_type, Unset):
        json_device_type = device_type

    params["device_type"] = json_device_type

    json_device_type_n: Union[Unset, list[str]] = UNSET
    if not isinstance(device_type_n, Unset):
        json_device_type_n = device_type_n

    params["device_type__n"] = json_device_type_n

    json_device_type_id: Union[Unset, list[int]] = UNSET
    if not isinstance(device_type_id, Unset):
        json_device_type_id = device_type_id

    params["device_type_id"] = json_device_type_id

    json_device_type_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(device_type_id_n, Unset):
        json_device_type_id_n = device_type_id_n

    params["device_type_id__n"] = json_device_type_id_n

    json_front_port_count: Union[Unset, list[int]] = UNSET
    if not isinstance(front_port_count, Unset):
        json_front_port_count = front_port_count

    params["front_port_count"] = json_front_port_count

    params["front_port_count__empty"] = front_port_count_empty

    json_front_port_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(front_port_count_gt, Unset):
        json_front_port_count_gt = front_port_count_gt

    params["front_port_count__gt"] = json_front_port_count_gt

    json_front_port_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(front_port_count_gte, Unset):
        json_front_port_count_gte = front_port_count_gte

    params["front_port_count__gte"] = json_front_port_count_gte

    json_front_port_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(front_port_count_lt, Unset):
        json_front_port_count_lt = front_port_count_lt

    params["front_port_count__lt"] = json_front_port_count_lt

    json_front_port_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(front_port_count_lte, Unset):
        json_front_port_count_lte = front_port_count_lte

    params["front_port_count__lte"] = json_front_port_count_lte

    json_front_port_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(front_port_count_n, Unset):
        json_front_port_count_n = front_port_count_n

    params["front_port_count__n"] = json_front_port_count_n

    params["has_oob_ip"] = has_oob_ip

    params["has_primary_ip"] = has_primary_ip

    params["has_virtual_device_context"] = has_virtual_device_context

    json_id: Union[Unset, list[int]] = UNSET
    if not isinstance(id, Unset):
        json_id = id

    params["id"] = json_id

    params["id__empty"] = id_empty

    json_id_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(id_gt, Unset):
        json_id_gt = id_gt

    params["id__gt"] = json_id_gt

    json_id_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(id_gte, Unset):
        json_id_gte = id_gte

    params["id__gte"] = json_id_gte

    json_id_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(id_lt, Unset):
        json_id_lt = id_lt

    params["id__lt"] = json_id_lt

    json_id_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(id_lte, Unset):
        json_id_lte = id_lte

    params["id__lte"] = json_id_lte

    json_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(id_n, Unset):
        json_id_n = id_n

    params["id__n"] = json_id_n

    json_interface_count: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_count, Unset):
        json_interface_count = interface_count

    params["interface_count"] = json_interface_count

    params["interface_count__empty"] = interface_count_empty

    json_interface_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_count_gt, Unset):
        json_interface_count_gt = interface_count_gt

    params["interface_count__gt"] = json_interface_count_gt

    json_interface_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_count_gte, Unset):
        json_interface_count_gte = interface_count_gte

    params["interface_count__gte"] = json_interface_count_gte

    json_interface_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_count_lt, Unset):
        json_interface_count_lt = interface_count_lt

    params["interface_count__lt"] = json_interface_count_lt

    json_interface_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_count_lte, Unset):
        json_interface_count_lte = interface_count_lte

    params["interface_count__lte"] = json_interface_count_lte

    json_interface_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_count_n, Unset):
        json_interface_count_n = interface_count_n

    params["interface_count__n"] = json_interface_count_n

    params["interfaces"] = interfaces

    json_inventory_item_count: Union[Unset, list[int]] = UNSET
    if not isinstance(inventory_item_count, Unset):
        json_inventory_item_count = inventory_item_count

    params["inventory_item_count"] = json_inventory_item_count

    params["inventory_item_count__empty"] = inventory_item_count_empty

    json_inventory_item_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(inventory_item_count_gt, Unset):
        json_inventory_item_count_gt = inventory_item_count_gt

    params["inventory_item_count__gt"] = json_inventory_item_count_gt

    json_inventory_item_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(inventory_item_count_gte, Unset):
        json_inventory_item_count_gte = inventory_item_count_gte

    params["inventory_item_count__gte"] = json_inventory_item_count_gte

    json_inventory_item_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(inventory_item_count_lt, Unset):
        json_inventory_item_count_lt = inventory_item_count_lt

    params["inventory_item_count__lt"] = json_inventory_item_count_lt

    json_inventory_item_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(inventory_item_count_lte, Unset):
        json_inventory_item_count_lte = inventory_item_count_lte

    params["inventory_item_count__lte"] = json_inventory_item_count_lte

    json_inventory_item_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(inventory_item_count_n, Unset):
        json_inventory_item_count_n = inventory_item_count_n

    params["inventory_item_count__n"] = json_inventory_item_count_n

    params["is_full_depth"] = is_full_depth

    json_last_updated: Union[Unset, list[str]] = UNSET
    if not isinstance(last_updated, Unset):
        json_last_updated = []
        for last_updated_item_data in last_updated:
            last_updated_item = last_updated_item_data.isoformat()
            json_last_updated.append(last_updated_item)

    params["last_updated"] = json_last_updated

    json_last_updated_empty: Union[Unset, list[str]] = UNSET
    if not isinstance(last_updated_empty, Unset):
        json_last_updated_empty = []
        for last_updated_empty_item_data in last_updated_empty:
            last_updated_empty_item = last_updated_empty_item_data.isoformat()
            json_last_updated_empty.append(last_updated_empty_item)

    params["last_updated__empty"] = json_last_updated_empty

    json_last_updated_gt: Union[Unset, list[str]] = UNSET
    if not isinstance(last_updated_gt, Unset):
        json_last_updated_gt = []
        for last_updated_gt_item_data in last_updated_gt:
            last_updated_gt_item = last_updated_gt_item_data.isoformat()
            json_last_updated_gt.append(last_updated_gt_item)

    params["last_updated__gt"] = json_last_updated_gt

    json_last_updated_gte: Union[Unset, list[str]] = UNSET
    if not isinstance(last_updated_gte, Unset):
        json_last_updated_gte = []
        for last_updated_gte_item_data in last_updated_gte:
            last_updated_gte_item = last_updated_gte_item_data.isoformat()
            json_last_updated_gte.append(last_updated_gte_item)

    params["last_updated__gte"] = json_last_updated_gte

    json_last_updated_lt: Union[Unset, list[str]] = UNSET
    if not isinstance(last_updated_lt, Unset):
        json_last_updated_lt = []
        for last_updated_lt_item_data in last_updated_lt:
            last_updated_lt_item = last_updated_lt_item_data.isoformat()
            json_last_updated_lt.append(last_updated_lt_item)

    params["last_updated__lt"] = json_last_updated_lt

    json_last_updated_lte: Union[Unset, list[str]] = UNSET
    if not isinstance(last_updated_lte, Unset):
        json_last_updated_lte = []
        for last_updated_lte_item_data in last_updated_lte:
            last_updated_lte_item = last_updated_lte_item_data.isoformat()
            json_last_updated_lte.append(last_updated_lte_item)

    params["last_updated__lte"] = json_last_updated_lte

    json_last_updated_n: Union[Unset, list[str]] = UNSET
    if not isinstance(last_updated_n, Unset):
        json_last_updated_n = []
        for last_updated_n_item_data in last_updated_n:
            last_updated_n_item = last_updated_n_item_data.isoformat()
            json_last_updated_n.append(last_updated_n_item)

    params["last_updated__n"] = json_last_updated_n

    json_latitude: Union[Unset, list[float]] = UNSET
    if not isinstance(latitude, Unset):
        json_latitude = latitude

    params["latitude"] = json_latitude

    params["latitude__empty"] = latitude_empty

    json_latitude_gt: Union[Unset, list[float]] = UNSET
    if not isinstance(latitude_gt, Unset):
        json_latitude_gt = latitude_gt

    params["latitude__gt"] = json_latitude_gt

    json_latitude_gte: Union[Unset, list[float]] = UNSET
    if not isinstance(latitude_gte, Unset):
        json_latitude_gte = latitude_gte

    params["latitude__gte"] = json_latitude_gte

    json_latitude_lt: Union[Unset, list[float]] = UNSET
    if not isinstance(latitude_lt, Unset):
        json_latitude_lt = latitude_lt

    params["latitude__lt"] = json_latitude_lt

    json_latitude_lte: Union[Unset, list[float]] = UNSET
    if not isinstance(latitude_lte, Unset):
        json_latitude_lte = latitude_lte

    params["latitude__lte"] = json_latitude_lte

    json_latitude_n: Union[Unset, list[float]] = UNSET
    if not isinstance(latitude_n, Unset):
        json_latitude_n = latitude_n

    params["latitude__n"] = json_latitude_n

    params["limit"] = limit

    params["local_context_data"] = local_context_data

    json_location: Union[Unset, list[str]] = UNSET
    if not isinstance(location, Unset):
        json_location = location

    params["location"] = json_location

    json_location_n: Union[Unset, list[str]] = UNSET
    if not isinstance(location_n, Unset):
        json_location_n = location_n

    params["location__n"] = json_location_n

    json_location_id: Union[Unset, list[str]] = UNSET
    if not isinstance(location_id, Unset):
        json_location_id = location_id

    params["location_id"] = json_location_id

    json_location_id_n: Union[Unset, list[str]] = UNSET
    if not isinstance(location_id_n, Unset):
        json_location_id_n = location_id_n

    params["location_id__n"] = json_location_id_n

    json_longitude: Union[Unset, list[float]] = UNSET
    if not isinstance(longitude, Unset):
        json_longitude = longitude

    params["longitude"] = json_longitude

    params["longitude__empty"] = longitude_empty

    json_longitude_gt: Union[Unset, list[float]] = UNSET
    if not isinstance(longitude_gt, Unset):
        json_longitude_gt = longitude_gt

    params["longitude__gt"] = json_longitude_gt

    json_longitude_gte: Union[Unset, list[float]] = UNSET
    if not isinstance(longitude_gte, Unset):
        json_longitude_gte = longitude_gte

    params["longitude__gte"] = json_longitude_gte

    json_longitude_lt: Union[Unset, list[float]] = UNSET
    if not isinstance(longitude_lt, Unset):
        json_longitude_lt = longitude_lt

    params["longitude__lt"] = json_longitude_lt

    json_longitude_lte: Union[Unset, list[float]] = UNSET
    if not isinstance(longitude_lte, Unset):
        json_longitude_lte = longitude_lte

    params["longitude__lte"] = json_longitude_lte

    json_longitude_n: Union[Unset, list[float]] = UNSET
    if not isinstance(longitude_n, Unset):
        json_longitude_n = longitude_n

    params["longitude__n"] = json_longitude_n

    json_mac_address: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address, Unset):
        json_mac_address = mac_address

    params["mac_address"] = json_mac_address

    json_mac_address_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address_ic, Unset):
        json_mac_address_ic = mac_address_ic

    params["mac_address__ic"] = json_mac_address_ic

    json_mac_address_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address_ie, Unset):
        json_mac_address_ie = mac_address_ie

    params["mac_address__ie"] = json_mac_address_ie

    json_mac_address_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address_iew, Unset):
        json_mac_address_iew = mac_address_iew

    params["mac_address__iew"] = json_mac_address_iew

    json_mac_address_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address_isw, Unset):
        json_mac_address_isw = mac_address_isw

    params["mac_address__isw"] = json_mac_address_isw

    json_mac_address_n: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address_n, Unset):
        json_mac_address_n = mac_address_n

    params["mac_address__n"] = json_mac_address_n

    json_mac_address_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address_nic, Unset):
        json_mac_address_nic = mac_address_nic

    params["mac_address__nic"] = json_mac_address_nic

    json_mac_address_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address_nie, Unset):
        json_mac_address_nie = mac_address_nie

    params["mac_address__nie"] = json_mac_address_nie

    json_mac_address_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address_niew, Unset):
        json_mac_address_niew = mac_address_niew

    params["mac_address__niew"] = json_mac_address_niew

    json_mac_address_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address_nisw, Unset):
        json_mac_address_nisw = mac_address_nisw

    params["mac_address__nisw"] = json_mac_address_nisw

    json_manufacturer: Union[Unset, list[str]] = UNSET
    if not isinstance(manufacturer, Unset):
        json_manufacturer = manufacturer

    params["manufacturer"] = json_manufacturer

    json_manufacturer_n: Union[Unset, list[str]] = UNSET
    if not isinstance(manufacturer_n, Unset):
        json_manufacturer_n = manufacturer_n

    params["manufacturer__n"] = json_manufacturer_n

    json_manufacturer_id: Union[Unset, list[int]] = UNSET
    if not isinstance(manufacturer_id, Unset):
        json_manufacturer_id = manufacturer_id

    params["manufacturer_id"] = json_manufacturer_id

    json_manufacturer_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(manufacturer_id_n, Unset):
        json_manufacturer_id_n = manufacturer_id_n

    params["manufacturer_id__n"] = json_manufacturer_id_n

    json_model: Union[Unset, list[str]] = UNSET
    if not isinstance(model, Unset):
        json_model = model

    params["model"] = json_model

    json_model_n: Union[Unset, list[str]] = UNSET
    if not isinstance(model_n, Unset):
        json_model_n = model_n

    params["model__n"] = json_model_n

    json_modified_by_request: Union[Unset, str] = UNSET
    if not isinstance(modified_by_request, Unset):
        json_modified_by_request = str(modified_by_request)
    params["modified_by_request"] = json_modified_by_request

    json_module_bay_count: Union[Unset, list[int]] = UNSET
    if not isinstance(module_bay_count, Unset):
        json_module_bay_count = module_bay_count

    params["module_bay_count"] = json_module_bay_count

    params["module_bay_count__empty"] = module_bay_count_empty

    json_module_bay_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(module_bay_count_gt, Unset):
        json_module_bay_count_gt = module_bay_count_gt

    params["module_bay_count__gt"] = json_module_bay_count_gt

    json_module_bay_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(module_bay_count_gte, Unset):
        json_module_bay_count_gte = module_bay_count_gte

    params["module_bay_count__gte"] = json_module_bay_count_gte

    json_module_bay_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(module_bay_count_lt, Unset):
        json_module_bay_count_lt = module_bay_count_lt

    params["module_bay_count__lt"] = json_module_bay_count_lt

    json_module_bay_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(module_bay_count_lte, Unset):
        json_module_bay_count_lte = module_bay_count_lte

    params["module_bay_count__lte"] = json_module_bay_count_lte

    json_module_bay_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(module_bay_count_n, Unset):
        json_module_bay_count_n = module_bay_count_n

    params["module_bay_count__n"] = json_module_bay_count_n

    params["module_bays"] = module_bays

    json_name: Union[Unset, list[str]] = UNSET
    if not isinstance(name, Unset):
        json_name = name

    params["name"] = json_name

    params["name__empty"] = name_empty

    json_name_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(name_ic, Unset):
        json_name_ic = name_ic

    params["name__ic"] = json_name_ic

    json_name_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(name_ie, Unset):
        json_name_ie = name_ie

    params["name__ie"] = json_name_ie

    json_name_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(name_iew, Unset):
        json_name_iew = name_iew

    params["name__iew"] = json_name_iew

    json_name_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(name_isw, Unset):
        json_name_isw = name_isw

    params["name__isw"] = json_name_isw

    json_name_n: Union[Unset, list[str]] = UNSET
    if not isinstance(name_n, Unset):
        json_name_n = name_n

    params["name__n"] = json_name_n

    json_name_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(name_nic, Unset):
        json_name_nic = name_nic

    params["name__nic"] = json_name_nic

    json_name_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(name_nie, Unset):
        json_name_nie = name_nie

    params["name__nie"] = json_name_nie

    json_name_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(name_niew, Unset):
        json_name_niew = name_niew

    params["name__niew"] = json_name_niew

    json_name_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(name_nisw, Unset):
        json_name_nisw = name_nisw

    params["name__nisw"] = json_name_nisw

    params["offset"] = offset

    json_oob_ip_id: Union[Unset, list[int]] = UNSET
    if not isinstance(oob_ip_id, Unset):
        json_oob_ip_id = oob_ip_id

    params["oob_ip_id"] = json_oob_ip_id

    json_oob_ip_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(oob_ip_id_n, Unset):
        json_oob_ip_id_n = oob_ip_id_n

    params["oob_ip_id__n"] = json_oob_ip_id_n

    params["ordering"] = ordering

    json_parent_bay_id: Union[Unset, list[int]] = UNSET
    if not isinstance(parent_bay_id, Unset):
        json_parent_bay_id = parent_bay_id

    params["parent_bay_id"] = json_parent_bay_id

    json_parent_bay_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(parent_bay_id_n, Unset):
        json_parent_bay_id_n = parent_bay_id_n

    params["parent_bay_id__n"] = json_parent_bay_id_n

    json_parent_device_id: Union[Unset, list[int]] = UNSET
    if not isinstance(parent_device_id, Unset):
        json_parent_device_id = parent_device_id

    params["parent_device_id"] = json_parent_device_id

    json_parent_device_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(parent_device_id_n, Unset):
        json_parent_device_id_n = parent_device_id_n

    params["parent_device_id__n"] = json_parent_device_id_n

    params["pass_through_ports"] = pass_through_ports

    json_platform: Union[Unset, list[str]] = UNSET
    if not isinstance(platform, Unset):
        json_platform = platform

    params["platform"] = json_platform

    json_platform_n: Union[Unset, list[str]] = UNSET
    if not isinstance(platform_n, Unset):
        json_platform_n = platform_n

    params["platform__n"] = json_platform_n

    json_platform_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(platform_id, Unset):
        json_platform_id = []
        for platform_id_item_data in platform_id:
            platform_id_item: Union[None, int]
            platform_id_item = platform_id_item_data
            json_platform_id.append(platform_id_item)

    params["platform_id"] = json_platform_id

    json_platform_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(platform_id_n, Unset):
        json_platform_id_n = []
        for platform_id_n_item_data in platform_id_n:
            platform_id_n_item: Union[None, int]
            platform_id_n_item = platform_id_n_item_data
            json_platform_id_n.append(platform_id_n_item)

    params["platform_id__n"] = json_platform_id_n

    json_position: Union[Unset, list[float]] = UNSET
    if not isinstance(position, Unset):
        json_position = position

    params["position"] = json_position

    params["position__empty"] = position_empty

    json_position_gt: Union[Unset, list[float]] = UNSET
    if not isinstance(position_gt, Unset):
        json_position_gt = position_gt

    params["position__gt"] = json_position_gt

    json_position_gte: Union[Unset, list[float]] = UNSET
    if not isinstance(position_gte, Unset):
        json_position_gte = position_gte

    params["position__gte"] = json_position_gte

    json_position_lt: Union[Unset, list[float]] = UNSET
    if not isinstance(position_lt, Unset):
        json_position_lt = position_lt

    params["position__lt"] = json_position_lt

    json_position_lte: Union[Unset, list[float]] = UNSET
    if not isinstance(position_lte, Unset):
        json_position_lte = position_lte

    params["position__lte"] = json_position_lte

    json_position_n: Union[Unset, list[float]] = UNSET
    if not isinstance(position_n, Unset):
        json_position_n = position_n

    params["position__n"] = json_position_n

    json_power_outlet_count: Union[Unset, list[int]] = UNSET
    if not isinstance(power_outlet_count, Unset):
        json_power_outlet_count = power_outlet_count

    params["power_outlet_count"] = json_power_outlet_count

    params["power_outlet_count__empty"] = power_outlet_count_empty

    json_power_outlet_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(power_outlet_count_gt, Unset):
        json_power_outlet_count_gt = power_outlet_count_gt

    params["power_outlet_count__gt"] = json_power_outlet_count_gt

    json_power_outlet_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(power_outlet_count_gte, Unset):
        json_power_outlet_count_gte = power_outlet_count_gte

    params["power_outlet_count__gte"] = json_power_outlet_count_gte

    json_power_outlet_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(power_outlet_count_lt, Unset):
        json_power_outlet_count_lt = power_outlet_count_lt

    params["power_outlet_count__lt"] = json_power_outlet_count_lt

    json_power_outlet_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(power_outlet_count_lte, Unset):
        json_power_outlet_count_lte = power_outlet_count_lte

    params["power_outlet_count__lte"] = json_power_outlet_count_lte

    json_power_outlet_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(power_outlet_count_n, Unset):
        json_power_outlet_count_n = power_outlet_count_n

    params["power_outlet_count__n"] = json_power_outlet_count_n

    params["power_outlets"] = power_outlets

    json_power_port_count: Union[Unset, list[int]] = UNSET
    if not isinstance(power_port_count, Unset):
        json_power_port_count = power_port_count

    params["power_port_count"] = json_power_port_count

    params["power_port_count__empty"] = power_port_count_empty

    json_power_port_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(power_port_count_gt, Unset):
        json_power_port_count_gt = power_port_count_gt

    params["power_port_count__gt"] = json_power_port_count_gt

    json_power_port_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(power_port_count_gte, Unset):
        json_power_port_count_gte = power_port_count_gte

    params["power_port_count__gte"] = json_power_port_count_gte

    json_power_port_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(power_port_count_lt, Unset):
        json_power_port_count_lt = power_port_count_lt

    params["power_port_count__lt"] = json_power_port_count_lt

    json_power_port_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(power_port_count_lte, Unset):
        json_power_port_count_lte = power_port_count_lte

    params["power_port_count__lte"] = json_power_port_count_lte

    json_power_port_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(power_port_count_n, Unset):
        json_power_port_count_n = power_port_count_n

    params["power_port_count__n"] = json_power_port_count_n

    params["power_ports"] = power_ports

    json_primary_ip4: Union[Unset, list[str]] = UNSET
    if not isinstance(primary_ip4, Unset):
        json_primary_ip4 = primary_ip4

    params["primary_ip4"] = json_primary_ip4

    json_primary_ip4_n: Union[Unset, list[str]] = UNSET
    if not isinstance(primary_ip4_n, Unset):
        json_primary_ip4_n = primary_ip4_n

    params["primary_ip4__n"] = json_primary_ip4_n

    json_primary_ip4_id: Union[Unset, list[int]] = UNSET
    if not isinstance(primary_ip4_id, Unset):
        json_primary_ip4_id = primary_ip4_id

    params["primary_ip4_id"] = json_primary_ip4_id

    json_primary_ip4_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(primary_ip4_id_n, Unset):
        json_primary_ip4_id_n = primary_ip4_id_n

    params["primary_ip4_id__n"] = json_primary_ip4_id_n

    json_primary_ip6: Union[Unset, list[str]] = UNSET
    if not isinstance(primary_ip6, Unset):
        json_primary_ip6 = primary_ip6

    params["primary_ip6"] = json_primary_ip6

    json_primary_ip6_n: Union[Unset, list[str]] = UNSET
    if not isinstance(primary_ip6_n, Unset):
        json_primary_ip6_n = primary_ip6_n

    params["primary_ip6__n"] = json_primary_ip6_n

    json_primary_ip6_id: Union[Unset, list[int]] = UNSET
    if not isinstance(primary_ip6_id, Unset):
        json_primary_ip6_id = primary_ip6_id

    params["primary_ip6_id"] = json_primary_ip6_id

    json_primary_ip6_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(primary_ip6_id_n, Unset):
        json_primary_ip6_id_n = primary_ip6_id_n

    params["primary_ip6_id__n"] = json_primary_ip6_id_n

    params["q"] = q

    json_rack_id: Union[Unset, list[int]] = UNSET
    if not isinstance(rack_id, Unset):
        json_rack_id = rack_id

    params["rack_id"] = json_rack_id

    json_rack_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(rack_id_n, Unset):
        json_rack_id_n = rack_id_n

    params["rack_id__n"] = json_rack_id_n

    json_rear_port_count: Union[Unset, list[int]] = UNSET
    if not isinstance(rear_port_count, Unset):
        json_rear_port_count = rear_port_count

    params["rear_port_count"] = json_rear_port_count

    params["rear_port_count__empty"] = rear_port_count_empty

    json_rear_port_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(rear_port_count_gt, Unset):
        json_rear_port_count_gt = rear_port_count_gt

    params["rear_port_count__gt"] = json_rear_port_count_gt

    json_rear_port_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(rear_port_count_gte, Unset):
        json_rear_port_count_gte = rear_port_count_gte

    params["rear_port_count__gte"] = json_rear_port_count_gte

    json_rear_port_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(rear_port_count_lt, Unset):
        json_rear_port_count_lt = rear_port_count_lt

    params["rear_port_count__lt"] = json_rear_port_count_lt

    json_rear_port_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(rear_port_count_lte, Unset):
        json_rear_port_count_lte = rear_port_count_lte

    params["rear_port_count__lte"] = json_rear_port_count_lte

    json_rear_port_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(rear_port_count_n, Unset):
        json_rear_port_count_n = rear_port_count_n

    params["rear_port_count__n"] = json_rear_port_count_n

    json_region: Union[Unset, list[str]] = UNSET
    if not isinstance(region, Unset):
        json_region = region

    params["region"] = json_region

    json_region_n: Union[Unset, list[str]] = UNSET
    if not isinstance(region_n, Unset):
        json_region_n = region_n

    params["region__n"] = json_region_n

    json_region_id: Union[Unset, list[str]] = UNSET
    if not isinstance(region_id, Unset):
        json_region_id = region_id

    params["region_id"] = json_region_id

    json_region_id_n: Union[Unset, list[str]] = UNSET
    if not isinstance(region_id_n, Unset):
        json_region_id_n = region_id_n

    params["region_id__n"] = json_region_id_n

    json_role: Union[Unset, list[str]] = UNSET
    if not isinstance(role, Unset):
        json_role = role

    params["role"] = json_role

    json_role_n: Union[Unset, list[str]] = UNSET
    if not isinstance(role_n, Unset):
        json_role_n = role_n

    params["role__n"] = json_role_n

    json_role_id: Union[Unset, list[str]] = UNSET
    if not isinstance(role_id, Unset):
        json_role_id = role_id

    params["role_id"] = json_role_id

    json_role_id_n: Union[Unset, list[str]] = UNSET
    if not isinstance(role_id_n, Unset):
        json_role_id_n = role_id_n

    params["role_id__n"] = json_role_id_n

    json_serial: Union[Unset, list[str]] = UNSET
    if not isinstance(serial, Unset):
        json_serial = serial

    params["serial"] = json_serial

    params["serial__empty"] = serial_empty

    json_serial_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_ic, Unset):
        json_serial_ic = serial_ic

    params["serial__ic"] = json_serial_ic

    json_serial_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_ie, Unset):
        json_serial_ie = serial_ie

    params["serial__ie"] = json_serial_ie

    json_serial_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_iew, Unset):
        json_serial_iew = serial_iew

    params["serial__iew"] = json_serial_iew

    json_serial_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_isw, Unset):
        json_serial_isw = serial_isw

    params["serial__isw"] = json_serial_isw

    json_serial_n: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_n, Unset):
        json_serial_n = serial_n

    params["serial__n"] = json_serial_n

    json_serial_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_nic, Unset):
        json_serial_nic = serial_nic

    params["serial__nic"] = json_serial_nic

    json_serial_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_nie, Unset):
        json_serial_nie = serial_nie

    params["serial__nie"] = json_serial_nie

    json_serial_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_niew, Unset):
        json_serial_niew = serial_niew

    params["serial__niew"] = json_serial_niew

    json_serial_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_nisw, Unset):
        json_serial_nisw = serial_nisw

    params["serial__nisw"] = json_serial_nisw

    json_site: Union[Unset, list[str]] = UNSET
    if not isinstance(site, Unset):
        json_site = site

    params["site"] = json_site

    json_site_n: Union[Unset, list[str]] = UNSET
    if not isinstance(site_n, Unset):
        json_site_n = site_n

    params["site__n"] = json_site_n

    json_site_group: Union[Unset, list[str]] = UNSET
    if not isinstance(site_group, Unset):
        json_site_group = site_group

    params["site_group"] = json_site_group

    json_site_group_n: Union[Unset, list[str]] = UNSET
    if not isinstance(site_group_n, Unset):
        json_site_group_n = site_group_n

    params["site_group__n"] = json_site_group_n

    json_site_group_id: Union[Unset, list[str]] = UNSET
    if not isinstance(site_group_id, Unset):
        json_site_group_id = site_group_id

    params["site_group_id"] = json_site_group_id

    json_site_group_id_n: Union[Unset, list[str]] = UNSET
    if not isinstance(site_group_id_n, Unset):
        json_site_group_id_n = site_group_id_n

    params["site_group_id__n"] = json_site_group_id_n

    json_site_id: Union[Unset, list[int]] = UNSET
    if not isinstance(site_id, Unset):
        json_site_id = site_id

    params["site_id"] = json_site_id

    json_site_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(site_id_n, Unset):
        json_site_id_n = site_id_n

    params["site_id__n"] = json_site_id_n

    json_status: Union[Unset, list[str]] = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    params["status__empty"] = status_empty

    json_status_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(status_ic, Unset):
        json_status_ic = status_ic

    params["status__ic"] = json_status_ic

    json_status_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(status_ie, Unset):
        json_status_ie = status_ie

    params["status__ie"] = json_status_ie

    json_status_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(status_iew, Unset):
        json_status_iew = status_iew

    params["status__iew"] = json_status_iew

    json_status_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(status_isw, Unset):
        json_status_isw = status_isw

    params["status__isw"] = json_status_isw

    json_status_n: Union[Unset, list[str]] = UNSET
    if not isinstance(status_n, Unset):
        json_status_n = status_n

    params["status__n"] = json_status_n

    json_status_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(status_nic, Unset):
        json_status_nic = status_nic

    params["status__nic"] = json_status_nic

    json_status_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(status_nie, Unset):
        json_status_nie = status_nie

    params["status__nie"] = json_status_nie

    json_status_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(status_niew, Unset):
        json_status_niew = status_niew

    params["status__niew"] = json_status_niew

    json_status_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(status_nisw, Unset):
        json_status_nisw = status_nisw

    params["status__nisw"] = json_status_nisw

    json_tag: Union[Unset, list[str]] = UNSET
    if not isinstance(tag, Unset):
        json_tag = tag

    params["tag"] = json_tag

    json_tag_n: Union[Unset, list[str]] = UNSET
    if not isinstance(tag_n, Unset):
        json_tag_n = tag_n

    params["tag__n"] = json_tag_n

    json_tag_id: Union[Unset, list[int]] = UNSET
    if not isinstance(tag_id, Unset):
        json_tag_id = tag_id

    params["tag_id"] = json_tag_id

    json_tag_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(tag_id_n, Unset):
        json_tag_id_n = tag_id_n

    params["tag_id__n"] = json_tag_id_n

    json_tenant: Union[Unset, list[str]] = UNSET
    if not isinstance(tenant, Unset):
        json_tenant = tenant

    params["tenant"] = json_tenant

    json_tenant_n: Union[Unset, list[str]] = UNSET
    if not isinstance(tenant_n, Unset):
        json_tenant_n = tenant_n

    params["tenant__n"] = json_tenant_n

    json_tenant_group: Union[Unset, list[str]] = UNSET
    if not isinstance(tenant_group, Unset):
        json_tenant_group = tenant_group

    params["tenant_group"] = json_tenant_group

    json_tenant_group_n: Union[Unset, list[str]] = UNSET
    if not isinstance(tenant_group_n, Unset):
        json_tenant_group_n = tenant_group_n

    params["tenant_group__n"] = json_tenant_group_n

    json_tenant_group_id: Union[Unset, list[str]] = UNSET
    if not isinstance(tenant_group_id, Unset):
        json_tenant_group_id = tenant_group_id

    params["tenant_group_id"] = json_tenant_group_id

    json_tenant_group_id_n: Union[Unset, list[str]] = UNSET
    if not isinstance(tenant_group_id_n, Unset):
        json_tenant_group_id_n = tenant_group_id_n

    params["tenant_group_id__n"] = json_tenant_group_id_n

    json_tenant_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(tenant_id, Unset):
        json_tenant_id = []
        for tenant_id_item_data in tenant_id:
            tenant_id_item: Union[None, int]
            tenant_id_item = tenant_id_item_data
            json_tenant_id.append(tenant_id_item)

    params["tenant_id"] = json_tenant_id

    json_tenant_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(tenant_id_n, Unset):
        json_tenant_id_n = []
        for tenant_id_n_item_data in tenant_id_n:
            tenant_id_n_item: Union[None, int]
            tenant_id_n_item = tenant_id_n_item_data
            json_tenant_id_n.append(tenant_id_n_item)

    params["tenant_id__n"] = json_tenant_id_n

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    json_vc_position: Union[Unset, list[int]] = UNSET
    if not isinstance(vc_position, Unset):
        json_vc_position = vc_position

    params["vc_position"] = json_vc_position

    params["vc_position__empty"] = vc_position_empty

    json_vc_position_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(vc_position_gt, Unset):
        json_vc_position_gt = vc_position_gt

    params["vc_position__gt"] = json_vc_position_gt

    json_vc_position_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(vc_position_gte, Unset):
        json_vc_position_gte = vc_position_gte

    params["vc_position__gte"] = json_vc_position_gte

    json_vc_position_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(vc_position_lt, Unset):
        json_vc_position_lt = vc_position_lt

    params["vc_position__lt"] = json_vc_position_lt

    json_vc_position_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(vc_position_lte, Unset):
        json_vc_position_lte = vc_position_lte

    params["vc_position__lte"] = json_vc_position_lte

    json_vc_position_n: Union[Unset, list[int]] = UNSET
    if not isinstance(vc_position_n, Unset):
        json_vc_position_n = vc_position_n

    params["vc_position__n"] = json_vc_position_n

    json_vc_priority: Union[Unset, list[int]] = UNSET
    if not isinstance(vc_priority, Unset):
        json_vc_priority = vc_priority

    params["vc_priority"] = json_vc_priority

    params["vc_priority__empty"] = vc_priority_empty

    json_vc_priority_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(vc_priority_gt, Unset):
        json_vc_priority_gt = vc_priority_gt

    params["vc_priority__gt"] = json_vc_priority_gt

    json_vc_priority_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(vc_priority_gte, Unset):
        json_vc_priority_gte = vc_priority_gte

    params["vc_priority__gte"] = json_vc_priority_gte

    json_vc_priority_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(vc_priority_lt, Unset):
        json_vc_priority_lt = vc_priority_lt

    params["vc_priority__lt"] = json_vc_priority_lt

    json_vc_priority_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(vc_priority_lte, Unset):
        json_vc_priority_lte = vc_priority_lte

    params["vc_priority__lte"] = json_vc_priority_lte

    json_vc_priority_n: Union[Unset, list[int]] = UNSET
    if not isinstance(vc_priority_n, Unset):
        json_vc_priority_n = vc_priority_n

    params["vc_priority__n"] = json_vc_priority_n

    json_virtual_chassis_id: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_chassis_id, Unset):
        json_virtual_chassis_id = virtual_chassis_id

    params["virtual_chassis_id"] = json_virtual_chassis_id

    json_virtual_chassis_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_chassis_id_n, Unset):
        json_virtual_chassis_id_n = virtual_chassis_id_n

    params["virtual_chassis_id__n"] = json_virtual_chassis_id_n

    params["virtual_chassis_member"] = virtual_chassis_member

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/dcim/devices/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedDeviceWithConfigContextList]:
    if response.status_code == 200:
        response_200 = PaginatedDeviceWithConfigContextList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedDeviceWithConfigContextList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    airflow: Union[Unset, DcimDevicesListAirflow] = UNSET,
    asset_tag: Union[Unset, list[str]] = UNSET,
    asset_tag_empty: Union[Unset, bool] = UNSET,
    asset_tag_ic: Union[Unset, list[str]] = UNSET,
    asset_tag_ie: Union[Unset, list[str]] = UNSET,
    asset_tag_iew: Union[Unset, list[str]] = UNSET,
    asset_tag_isw: Union[Unset, list[str]] = UNSET,
    asset_tag_n: Union[Unset, list[str]] = UNSET,
    asset_tag_nic: Union[Unset, list[str]] = UNSET,
    asset_tag_nie: Union[Unset, list[str]] = UNSET,
    asset_tag_niew: Union[Unset, list[str]] = UNSET,
    asset_tag_nisw: Union[Unset, list[str]] = UNSET,
    cluster_group: Union[Unset, list[str]] = UNSET,
    cluster_group_n: Union[Unset, list[str]] = UNSET,
    cluster_group_id: Union[Unset, list[int]] = UNSET,
    cluster_group_id_n: Union[Unset, list[int]] = UNSET,
    cluster_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cluster_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    config_template_id: Union[Unset, list[Union[None, int]]] = UNSET,
    config_template_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    console_port_count: Union[Unset, list[int]] = UNSET,
    console_port_count_empty: Union[Unset, bool] = UNSET,
    console_port_count_gt: Union[Unset, list[int]] = UNSET,
    console_port_count_gte: Union[Unset, list[int]] = UNSET,
    console_port_count_lt: Union[Unset, list[int]] = UNSET,
    console_port_count_lte: Union[Unset, list[int]] = UNSET,
    console_port_count_n: Union[Unset, list[int]] = UNSET,
    console_ports: Union[Unset, bool] = UNSET,
    console_server_port_count: Union[Unset, list[int]] = UNSET,
    console_server_port_count_empty: Union[Unset, bool] = UNSET,
    console_server_port_count_gt: Union[Unset, list[int]] = UNSET,
    console_server_port_count_gte: Union[Unset, list[int]] = UNSET,
    console_server_port_count_lt: Union[Unset, list[int]] = UNSET,
    console_server_port_count_lte: Union[Unset, list[int]] = UNSET,
    console_server_port_count_n: Union[Unset, list[int]] = UNSET,
    console_server_ports: Union[Unset, bool] = UNSET,
    contact: Union[Unset, list[int]] = UNSET,
    contact_n: Union[Unset, list[int]] = UNSET,
    contact_group: Union[Unset, list[str]] = UNSET,
    contact_group_n: Union[Unset, list[str]] = UNSET,
    contact_role: Union[Unset, list[int]] = UNSET,
    contact_role_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    description: Union[Unset, list[str]] = UNSET,
    description_empty: Union[Unset, bool] = UNSET,
    description_ic: Union[Unset, list[str]] = UNSET,
    description_ie: Union[Unset, list[str]] = UNSET,
    description_iew: Union[Unset, list[str]] = UNSET,
    description_isw: Union[Unset, list[str]] = UNSET,
    description_n: Union[Unset, list[str]] = UNSET,
    description_nic: Union[Unset, list[str]] = UNSET,
    description_nie: Union[Unset, list[str]] = UNSET,
    description_niew: Union[Unset, list[str]] = UNSET,
    description_nisw: Union[Unset, list[str]] = UNSET,
    device_bay_count: Union[Unset, list[int]] = UNSET,
    device_bay_count_empty: Union[Unset, bool] = UNSET,
    device_bay_count_gt: Union[Unset, list[int]] = UNSET,
    device_bay_count_gte: Union[Unset, list[int]] = UNSET,
    device_bay_count_lt: Union[Unset, list[int]] = UNSET,
    device_bay_count_lte: Union[Unset, list[int]] = UNSET,
    device_bay_count_n: Union[Unset, list[int]] = UNSET,
    device_bays: Union[Unset, bool] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    front_port_count: Union[Unset, list[int]] = UNSET,
    front_port_count_empty: Union[Unset, bool] = UNSET,
    front_port_count_gt: Union[Unset, list[int]] = UNSET,
    front_port_count_gte: Union[Unset, list[int]] = UNSET,
    front_port_count_lt: Union[Unset, list[int]] = UNSET,
    front_port_count_lte: Union[Unset, list[int]] = UNSET,
    front_port_count_n: Union[Unset, list[int]] = UNSET,
    has_oob_ip: Union[Unset, bool] = UNSET,
    has_primary_ip: Union[Unset, bool] = UNSET,
    has_virtual_device_context: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_count: Union[Unset, list[int]] = UNSET,
    interface_count_empty: Union[Unset, bool] = UNSET,
    interface_count_gt: Union[Unset, list[int]] = UNSET,
    interface_count_gte: Union[Unset, list[int]] = UNSET,
    interface_count_lt: Union[Unset, list[int]] = UNSET,
    interface_count_lte: Union[Unset, list[int]] = UNSET,
    interface_count_n: Union[Unset, list[int]] = UNSET,
    interfaces: Union[Unset, bool] = UNSET,
    inventory_item_count: Union[Unset, list[int]] = UNSET,
    inventory_item_count_empty: Union[Unset, bool] = UNSET,
    inventory_item_count_gt: Union[Unset, list[int]] = UNSET,
    inventory_item_count_gte: Union[Unset, list[int]] = UNSET,
    inventory_item_count_lt: Union[Unset, list[int]] = UNSET,
    inventory_item_count_lte: Union[Unset, list[int]] = UNSET,
    inventory_item_count_n: Union[Unset, list[int]] = UNSET,
    is_full_depth: Union[Unset, bool] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    latitude: Union[Unset, list[float]] = UNSET,
    latitude_empty: Union[Unset, bool] = UNSET,
    latitude_gt: Union[Unset, list[float]] = UNSET,
    latitude_gte: Union[Unset, list[float]] = UNSET,
    latitude_lt: Union[Unset, list[float]] = UNSET,
    latitude_lte: Union[Unset, list[float]] = UNSET,
    latitude_n: Union[Unset, list[float]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    local_context_data: Union[Unset, bool] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[str]] = UNSET,
    location_id_n: Union[Unset, list[str]] = UNSET,
    longitude: Union[Unset, list[float]] = UNSET,
    longitude_empty: Union[Unset, bool] = UNSET,
    longitude_gt: Union[Unset, list[float]] = UNSET,
    longitude_gte: Union[Unset, list[float]] = UNSET,
    longitude_lt: Union[Unset, list[float]] = UNSET,
    longitude_lte: Union[Unset, list[float]] = UNSET,
    longitude_n: Union[Unset, list[float]] = UNSET,
    mac_address: Union[Unset, list[str]] = UNSET,
    mac_address_ic: Union[Unset, list[str]] = UNSET,
    mac_address_ie: Union[Unset, list[str]] = UNSET,
    mac_address_iew: Union[Unset, list[str]] = UNSET,
    mac_address_isw: Union[Unset, list[str]] = UNSET,
    mac_address_n: Union[Unset, list[str]] = UNSET,
    mac_address_nic: Union[Unset, list[str]] = UNSET,
    mac_address_nie: Union[Unset, list[str]] = UNSET,
    mac_address_niew: Union[Unset, list[str]] = UNSET,
    mac_address_nisw: Union[Unset, list[str]] = UNSET,
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    model: Union[Unset, list[str]] = UNSET,
    model_n: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_bay_count: Union[Unset, list[int]] = UNSET,
    module_bay_count_empty: Union[Unset, bool] = UNSET,
    module_bay_count_gt: Union[Unset, list[int]] = UNSET,
    module_bay_count_gte: Union[Unset, list[int]] = UNSET,
    module_bay_count_lt: Union[Unset, list[int]] = UNSET,
    module_bay_count_lte: Union[Unset, list[int]] = UNSET,
    module_bay_count_n: Union[Unset, list[int]] = UNSET,
    module_bays: Union[Unset, bool] = UNSET,
    name: Union[Unset, list[str]] = UNSET,
    name_empty: Union[Unset, bool] = UNSET,
    name_ic: Union[Unset, list[str]] = UNSET,
    name_ie: Union[Unset, list[str]] = UNSET,
    name_iew: Union[Unset, list[str]] = UNSET,
    name_isw: Union[Unset, list[str]] = UNSET,
    name_n: Union[Unset, list[str]] = UNSET,
    name_nic: Union[Unset, list[str]] = UNSET,
    name_nie: Union[Unset, list[str]] = UNSET,
    name_niew: Union[Unset, list[str]] = UNSET,
    name_nisw: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    oob_ip_id: Union[Unset, list[int]] = UNSET,
    oob_ip_id_n: Union[Unset, list[int]] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_bay_id: Union[Unset, list[int]] = UNSET,
    parent_bay_id_n: Union[Unset, list[int]] = UNSET,
    parent_device_id: Union[Unset, list[int]] = UNSET,
    parent_device_id_n: Union[Unset, list[int]] = UNSET,
    pass_through_ports: Union[Unset, bool] = UNSET,
    platform: Union[Unset, list[str]] = UNSET,
    platform_n: Union[Unset, list[str]] = UNSET,
    platform_id: Union[Unset, list[Union[None, int]]] = UNSET,
    platform_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    position: Union[Unset, list[float]] = UNSET,
    position_empty: Union[Unset, bool] = UNSET,
    position_gt: Union[Unset, list[float]] = UNSET,
    position_gte: Union[Unset, list[float]] = UNSET,
    position_lt: Union[Unset, list[float]] = UNSET,
    position_lte: Union[Unset, list[float]] = UNSET,
    position_n: Union[Unset, list[float]] = UNSET,
    power_outlet_count: Union[Unset, list[int]] = UNSET,
    power_outlet_count_empty: Union[Unset, bool] = UNSET,
    power_outlet_count_gt: Union[Unset, list[int]] = UNSET,
    power_outlet_count_gte: Union[Unset, list[int]] = UNSET,
    power_outlet_count_lt: Union[Unset, list[int]] = UNSET,
    power_outlet_count_lte: Union[Unset, list[int]] = UNSET,
    power_outlet_count_n: Union[Unset, list[int]] = UNSET,
    power_outlets: Union[Unset, bool] = UNSET,
    power_port_count: Union[Unset, list[int]] = UNSET,
    power_port_count_empty: Union[Unset, bool] = UNSET,
    power_port_count_gt: Union[Unset, list[int]] = UNSET,
    power_port_count_gte: Union[Unset, list[int]] = UNSET,
    power_port_count_lt: Union[Unset, list[int]] = UNSET,
    power_port_count_lte: Union[Unset, list[int]] = UNSET,
    power_port_count_n: Union[Unset, list[int]] = UNSET,
    power_ports: Union[Unset, bool] = UNSET,
    primary_ip4: Union[Unset, list[str]] = UNSET,
    primary_ip4_n: Union[Unset, list[str]] = UNSET,
    primary_ip4_id: Union[Unset, list[int]] = UNSET,
    primary_ip4_id_n: Union[Unset, list[int]] = UNSET,
    primary_ip6: Union[Unset, list[str]] = UNSET,
    primary_ip6_n: Union[Unset, list[str]] = UNSET,
    primary_ip6_id: Union[Unset, list[int]] = UNSET,
    primary_ip6_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    rear_port_count: Union[Unset, list[int]] = UNSET,
    rear_port_count_empty: Union[Unset, bool] = UNSET,
    rear_port_count_gt: Union[Unset, list[int]] = UNSET,
    rear_port_count_gte: Union[Unset, list[int]] = UNSET,
    rear_port_count_lt: Union[Unset, list[int]] = UNSET,
    rear_port_count_lte: Union[Unset, list[int]] = UNSET,
    rear_port_count_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[str]] = UNSET,
    role_id_n: Union[Unset, list[str]] = UNSET,
    serial: Union[Unset, list[str]] = UNSET,
    serial_empty: Union[Unset, bool] = UNSET,
    serial_ic: Union[Unset, list[str]] = UNSET,
    serial_ie: Union[Unset, list[str]] = UNSET,
    serial_iew: Union[Unset, list[str]] = UNSET,
    serial_isw: Union[Unset, list[str]] = UNSET,
    serial_n: Union[Unset, list[str]] = UNSET,
    serial_nic: Union[Unset, list[str]] = UNSET,
    serial_nie: Union[Unset, list[str]] = UNSET,
    serial_niew: Union[Unset, list[str]] = UNSET,
    serial_nisw: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    status: Union[Unset, list[str]] = UNSET,
    status_empty: Union[Unset, bool] = UNSET,
    status_ic: Union[Unset, list[str]] = UNSET,
    status_ie: Union[Unset, list[str]] = UNSET,
    status_iew: Union[Unset, list[str]] = UNSET,
    status_isw: Union[Unset, list[str]] = UNSET,
    status_n: Union[Unset, list[str]] = UNSET,
    status_nic: Union[Unset, list[str]] = UNSET,
    status_nie: Union[Unset, list[str]] = UNSET,
    status_niew: Union[Unset, list[str]] = UNSET,
    status_nisw: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tenant: Union[Unset, list[str]] = UNSET,
    tenant_n: Union[Unset, list[str]] = UNSET,
    tenant_group: Union[Unset, list[str]] = UNSET,
    tenant_group_n: Union[Unset, list[str]] = UNSET,
    tenant_group_id: Union[Unset, list[str]] = UNSET,
    tenant_group_id_n: Union[Unset, list[str]] = UNSET,
    tenant_id: Union[Unset, list[Union[None, int]]] = UNSET,
    tenant_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    vc_position: Union[Unset, list[int]] = UNSET,
    vc_position_empty: Union[Unset, bool] = UNSET,
    vc_position_gt: Union[Unset, list[int]] = UNSET,
    vc_position_gte: Union[Unset, list[int]] = UNSET,
    vc_position_lt: Union[Unset, list[int]] = UNSET,
    vc_position_lte: Union[Unset, list[int]] = UNSET,
    vc_position_n: Union[Unset, list[int]] = UNSET,
    vc_priority: Union[Unset, list[int]] = UNSET,
    vc_priority_empty: Union[Unset, bool] = UNSET,
    vc_priority_gt: Union[Unset, list[int]] = UNSET,
    vc_priority_gte: Union[Unset, list[int]] = UNSET,
    vc_priority_lt: Union[Unset, list[int]] = UNSET,
    vc_priority_lte: Union[Unset, list[int]] = UNSET,
    vc_priority_n: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id_n: Union[Unset, list[int]] = UNSET,
    virtual_chassis_member: Union[Unset, bool] = UNSET,
) -> Response[PaginatedDeviceWithConfigContextList]:
    """Get a list of device objects.

    Args:
        airflow (Union[Unset, DcimDevicesListAirflow]):
        asset_tag (Union[Unset, list[str]]):
        asset_tag_empty (Union[Unset, bool]):
        asset_tag_ic (Union[Unset, list[str]]):
        asset_tag_ie (Union[Unset, list[str]]):
        asset_tag_iew (Union[Unset, list[str]]):
        asset_tag_isw (Union[Unset, list[str]]):
        asset_tag_n (Union[Unset, list[str]]):
        asset_tag_nic (Union[Unset, list[str]]):
        asset_tag_nie (Union[Unset, list[str]]):
        asset_tag_niew (Union[Unset, list[str]]):
        asset_tag_nisw (Union[Unset, list[str]]):
        cluster_group (Union[Unset, list[str]]):
        cluster_group_n (Union[Unset, list[str]]):
        cluster_group_id (Union[Unset, list[int]]):
        cluster_group_id_n (Union[Unset, list[int]]):
        cluster_id (Union[Unset, list[Union[None, int]]]):
        cluster_id_n (Union[Unset, list[Union[None, int]]]):
        config_template_id (Union[Unset, list[Union[None, int]]]):
        config_template_id_n (Union[Unset, list[Union[None, int]]]):
        console_port_count (Union[Unset, list[int]]):
        console_port_count_empty (Union[Unset, bool]):
        console_port_count_gt (Union[Unset, list[int]]):
        console_port_count_gte (Union[Unset, list[int]]):
        console_port_count_lt (Union[Unset, list[int]]):
        console_port_count_lte (Union[Unset, list[int]]):
        console_port_count_n (Union[Unset, list[int]]):
        console_ports (Union[Unset, bool]):
        console_server_port_count (Union[Unset, list[int]]):
        console_server_port_count_empty (Union[Unset, bool]):
        console_server_port_count_gt (Union[Unset, list[int]]):
        console_server_port_count_gte (Union[Unset, list[int]]):
        console_server_port_count_lt (Union[Unset, list[int]]):
        console_server_port_count_lte (Union[Unset, list[int]]):
        console_server_port_count_n (Union[Unset, list[int]]):
        console_server_ports (Union[Unset, bool]):
        contact (Union[Unset, list[int]]):
        contact_n (Union[Unset, list[int]]):
        contact_group (Union[Unset, list[str]]):
        contact_group_n (Union[Unset, list[str]]):
        contact_role (Union[Unset, list[int]]):
        contact_role_n (Union[Unset, list[int]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        description (Union[Unset, list[str]]):
        description_empty (Union[Unset, bool]):
        description_ic (Union[Unset, list[str]]):
        description_ie (Union[Unset, list[str]]):
        description_iew (Union[Unset, list[str]]):
        description_isw (Union[Unset, list[str]]):
        description_n (Union[Unset, list[str]]):
        description_nic (Union[Unset, list[str]]):
        description_nie (Union[Unset, list[str]]):
        description_niew (Union[Unset, list[str]]):
        description_nisw (Union[Unset, list[str]]):
        device_bay_count (Union[Unset, list[int]]):
        device_bay_count_empty (Union[Unset, bool]):
        device_bay_count_gt (Union[Unset, list[int]]):
        device_bay_count_gte (Union[Unset, list[int]]):
        device_bay_count_lt (Union[Unset, list[int]]):
        device_bay_count_lte (Union[Unset, list[int]]):
        device_bay_count_n (Union[Unset, list[int]]):
        device_bays (Union[Unset, bool]):
        device_type (Union[Unset, list[str]]):
        device_type_n (Union[Unset, list[str]]):
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
        front_port_count (Union[Unset, list[int]]):
        front_port_count_empty (Union[Unset, bool]):
        front_port_count_gt (Union[Unset, list[int]]):
        front_port_count_gte (Union[Unset, list[int]]):
        front_port_count_lt (Union[Unset, list[int]]):
        front_port_count_lte (Union[Unset, list[int]]):
        front_port_count_n (Union[Unset, list[int]]):
        has_oob_ip (Union[Unset, bool]):
        has_primary_ip (Union[Unset, bool]):
        has_virtual_device_context (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_count (Union[Unset, list[int]]):
        interface_count_empty (Union[Unset, bool]):
        interface_count_gt (Union[Unset, list[int]]):
        interface_count_gte (Union[Unset, list[int]]):
        interface_count_lt (Union[Unset, list[int]]):
        interface_count_lte (Union[Unset, list[int]]):
        interface_count_n (Union[Unset, list[int]]):
        interfaces (Union[Unset, bool]):
        inventory_item_count (Union[Unset, list[int]]):
        inventory_item_count_empty (Union[Unset, bool]):
        inventory_item_count_gt (Union[Unset, list[int]]):
        inventory_item_count_gte (Union[Unset, list[int]]):
        inventory_item_count_lt (Union[Unset, list[int]]):
        inventory_item_count_lte (Union[Unset, list[int]]):
        inventory_item_count_n (Union[Unset, list[int]]):
        is_full_depth (Union[Unset, bool]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        latitude (Union[Unset, list[float]]):
        latitude_empty (Union[Unset, bool]):
        latitude_gt (Union[Unset, list[float]]):
        latitude_gte (Union[Unset, list[float]]):
        latitude_lt (Union[Unset, list[float]]):
        latitude_lte (Union[Unset, list[float]]):
        latitude_n (Union[Unset, list[float]]):
        limit (Union[Unset, int]):
        local_context_data (Union[Unset, bool]):
        location (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_id (Union[Unset, list[str]]):
        location_id_n (Union[Unset, list[str]]):
        longitude (Union[Unset, list[float]]):
        longitude_empty (Union[Unset, bool]):
        longitude_gt (Union[Unset, list[float]]):
        longitude_gte (Union[Unset, list[float]]):
        longitude_lt (Union[Unset, list[float]]):
        longitude_lte (Union[Unset, list[float]]):
        longitude_n (Union[Unset, list[float]]):
        mac_address (Union[Unset, list[str]]):
        mac_address_ic (Union[Unset, list[str]]):
        mac_address_ie (Union[Unset, list[str]]):
        mac_address_iew (Union[Unset, list[str]]):
        mac_address_isw (Union[Unset, list[str]]):
        mac_address_n (Union[Unset, list[str]]):
        mac_address_nic (Union[Unset, list[str]]):
        mac_address_nie (Union[Unset, list[str]]):
        mac_address_niew (Union[Unset, list[str]]):
        mac_address_nisw (Union[Unset, list[str]]):
        manufacturer (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_id (Union[Unset, list[int]]):
        manufacturer_id_n (Union[Unset, list[int]]):
        model (Union[Unset, list[str]]):
        model_n (Union[Unset, list[str]]):
        modified_by_request (Union[Unset, UUID]):
        module_bay_count (Union[Unset, list[int]]):
        module_bay_count_empty (Union[Unset, bool]):
        module_bay_count_gt (Union[Unset, list[int]]):
        module_bay_count_gte (Union[Unset, list[int]]):
        module_bay_count_lt (Union[Unset, list[int]]):
        module_bay_count_lte (Union[Unset, list[int]]):
        module_bay_count_n (Union[Unset, list[int]]):
        module_bays (Union[Unset, bool]):
        name (Union[Unset, list[str]]):
        name_empty (Union[Unset, bool]):
        name_ic (Union[Unset, list[str]]):
        name_ie (Union[Unset, list[str]]):
        name_iew (Union[Unset, list[str]]):
        name_isw (Union[Unset, list[str]]):
        name_n (Union[Unset, list[str]]):
        name_nic (Union[Unset, list[str]]):
        name_nie (Union[Unset, list[str]]):
        name_niew (Union[Unset, list[str]]):
        name_nisw (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        oob_ip_id (Union[Unset, list[int]]):
        oob_ip_id_n (Union[Unset, list[int]]):
        ordering (Union[Unset, str]):
        parent_bay_id (Union[Unset, list[int]]):
        parent_bay_id_n (Union[Unset, list[int]]):
        parent_device_id (Union[Unset, list[int]]):
        parent_device_id_n (Union[Unset, list[int]]):
        pass_through_ports (Union[Unset, bool]):
        platform (Union[Unset, list[str]]):
        platform_n (Union[Unset, list[str]]):
        platform_id (Union[Unset, list[Union[None, int]]]):
        platform_id_n (Union[Unset, list[Union[None, int]]]):
        position (Union[Unset, list[float]]):
        position_empty (Union[Unset, bool]):
        position_gt (Union[Unset, list[float]]):
        position_gte (Union[Unset, list[float]]):
        position_lt (Union[Unset, list[float]]):
        position_lte (Union[Unset, list[float]]):
        position_n (Union[Unset, list[float]]):
        power_outlet_count (Union[Unset, list[int]]):
        power_outlet_count_empty (Union[Unset, bool]):
        power_outlet_count_gt (Union[Unset, list[int]]):
        power_outlet_count_gte (Union[Unset, list[int]]):
        power_outlet_count_lt (Union[Unset, list[int]]):
        power_outlet_count_lte (Union[Unset, list[int]]):
        power_outlet_count_n (Union[Unset, list[int]]):
        power_outlets (Union[Unset, bool]):
        power_port_count (Union[Unset, list[int]]):
        power_port_count_empty (Union[Unset, bool]):
        power_port_count_gt (Union[Unset, list[int]]):
        power_port_count_gte (Union[Unset, list[int]]):
        power_port_count_lt (Union[Unset, list[int]]):
        power_port_count_lte (Union[Unset, list[int]]):
        power_port_count_n (Union[Unset, list[int]]):
        power_ports (Union[Unset, bool]):
        primary_ip4 (Union[Unset, list[str]]):
        primary_ip4_n (Union[Unset, list[str]]):
        primary_ip4_id (Union[Unset, list[int]]):
        primary_ip4_id_n (Union[Unset, list[int]]):
        primary_ip6 (Union[Unset, list[str]]):
        primary_ip6_n (Union[Unset, list[str]]):
        primary_ip6_id (Union[Unset, list[int]]):
        primary_ip6_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        rack_id (Union[Unset, list[int]]):
        rack_id_n (Union[Unset, list[int]]):
        rear_port_count (Union[Unset, list[int]]):
        rear_port_count_empty (Union[Unset, bool]):
        rear_port_count_gt (Union[Unset, list[int]]):
        rear_port_count_gte (Union[Unset, list[int]]):
        rear_port_count_lt (Union[Unset, list[int]]):
        rear_port_count_lte (Union[Unset, list[int]]):
        rear_port_count_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[str]]):
        role_id_n (Union[Unset, list[str]]):
        serial (Union[Unset, list[str]]):
        serial_empty (Union[Unset, bool]):
        serial_ic (Union[Unset, list[str]]):
        serial_ie (Union[Unset, list[str]]):
        serial_iew (Union[Unset, list[str]]):
        serial_isw (Union[Unset, list[str]]):
        serial_n (Union[Unset, list[str]]):
        serial_nic (Union[Unset, list[str]]):
        serial_nie (Union[Unset, list[str]]):
        serial_niew (Union[Unset, list[str]]):
        serial_nisw (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
        status (Union[Unset, list[str]]):
        status_empty (Union[Unset, bool]):
        status_ic (Union[Unset, list[str]]):
        status_ie (Union[Unset, list[str]]):
        status_iew (Union[Unset, list[str]]):
        status_isw (Union[Unset, list[str]]):
        status_n (Union[Unset, list[str]]):
        status_nic (Union[Unset, list[str]]):
        status_nie (Union[Unset, list[str]]):
        status_niew (Union[Unset, list[str]]):
        status_nisw (Union[Unset, list[str]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        tenant (Union[Unset, list[str]]):
        tenant_n (Union[Unset, list[str]]):
        tenant_group (Union[Unset, list[str]]):
        tenant_group_n (Union[Unset, list[str]]):
        tenant_group_id (Union[Unset, list[str]]):
        tenant_group_id_n (Union[Unset, list[str]]):
        tenant_id (Union[Unset, list[Union[None, int]]]):
        tenant_id_n (Union[Unset, list[Union[None, int]]]):
        updated_by_request (Union[Unset, UUID]):
        vc_position (Union[Unset, list[int]]):
        vc_position_empty (Union[Unset, bool]):
        vc_position_gt (Union[Unset, list[int]]):
        vc_position_gte (Union[Unset, list[int]]):
        vc_position_lt (Union[Unset, list[int]]):
        vc_position_lte (Union[Unset, list[int]]):
        vc_position_n (Union[Unset, list[int]]):
        vc_priority (Union[Unset, list[int]]):
        vc_priority_empty (Union[Unset, bool]):
        vc_priority_gt (Union[Unset, list[int]]):
        vc_priority_gte (Union[Unset, list[int]]):
        vc_priority_lt (Union[Unset, list[int]]):
        vc_priority_lte (Union[Unset, list[int]]):
        vc_priority_n (Union[Unset, list[int]]):
        virtual_chassis_id (Union[Unset, list[int]]):
        virtual_chassis_id_n (Union[Unset, list[int]]):
        virtual_chassis_member (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDeviceWithConfigContextList]
    """

    kwargs = _get_kwargs(
        airflow=airflow,
        asset_tag=asset_tag,
        asset_tag_empty=asset_tag_empty,
        asset_tag_ic=asset_tag_ic,
        asset_tag_ie=asset_tag_ie,
        asset_tag_iew=asset_tag_iew,
        asset_tag_isw=asset_tag_isw,
        asset_tag_n=asset_tag_n,
        asset_tag_nic=asset_tag_nic,
        asset_tag_nie=asset_tag_nie,
        asset_tag_niew=asset_tag_niew,
        asset_tag_nisw=asset_tag_nisw,
        cluster_group=cluster_group,
        cluster_group_n=cluster_group_n,
        cluster_group_id=cluster_group_id,
        cluster_group_id_n=cluster_group_id_n,
        cluster_id=cluster_id,
        cluster_id_n=cluster_id_n,
        config_template_id=config_template_id,
        config_template_id_n=config_template_id_n,
        console_port_count=console_port_count,
        console_port_count_empty=console_port_count_empty,
        console_port_count_gt=console_port_count_gt,
        console_port_count_gte=console_port_count_gte,
        console_port_count_lt=console_port_count_lt,
        console_port_count_lte=console_port_count_lte,
        console_port_count_n=console_port_count_n,
        console_ports=console_ports,
        console_server_port_count=console_server_port_count,
        console_server_port_count_empty=console_server_port_count_empty,
        console_server_port_count_gt=console_server_port_count_gt,
        console_server_port_count_gte=console_server_port_count_gte,
        console_server_port_count_lt=console_server_port_count_lt,
        console_server_port_count_lte=console_server_port_count_lte,
        console_server_port_count_n=console_server_port_count_n,
        console_server_ports=console_server_ports,
        contact=contact,
        contact_n=contact_n,
        contact_group=contact_group,
        contact_group_n=contact_group_n,
        contact_role=contact_role,
        contact_role_n=contact_role_n,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        description=description,
        description_empty=description_empty,
        description_ic=description_ic,
        description_ie=description_ie,
        description_iew=description_iew,
        description_isw=description_isw,
        description_n=description_n,
        description_nic=description_nic,
        description_nie=description_nie,
        description_niew=description_niew,
        description_nisw=description_nisw,
        device_bay_count=device_bay_count,
        device_bay_count_empty=device_bay_count_empty,
        device_bay_count_gt=device_bay_count_gt,
        device_bay_count_gte=device_bay_count_gte,
        device_bay_count_lt=device_bay_count_lt,
        device_bay_count_lte=device_bay_count_lte,
        device_bay_count_n=device_bay_count_n,
        device_bays=device_bays,
        device_type=device_type,
        device_type_n=device_type_n,
        device_type_id=device_type_id,
        device_type_id_n=device_type_id_n,
        front_port_count=front_port_count,
        front_port_count_empty=front_port_count_empty,
        front_port_count_gt=front_port_count_gt,
        front_port_count_gte=front_port_count_gte,
        front_port_count_lt=front_port_count_lt,
        front_port_count_lte=front_port_count_lte,
        front_port_count_n=front_port_count_n,
        has_oob_ip=has_oob_ip,
        has_primary_ip=has_primary_ip,
        has_virtual_device_context=has_virtual_device_context,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface_count=interface_count,
        interface_count_empty=interface_count_empty,
        interface_count_gt=interface_count_gt,
        interface_count_gte=interface_count_gte,
        interface_count_lt=interface_count_lt,
        interface_count_lte=interface_count_lte,
        interface_count_n=interface_count_n,
        interfaces=interfaces,
        inventory_item_count=inventory_item_count,
        inventory_item_count_empty=inventory_item_count_empty,
        inventory_item_count_gt=inventory_item_count_gt,
        inventory_item_count_gte=inventory_item_count_gte,
        inventory_item_count_lt=inventory_item_count_lt,
        inventory_item_count_lte=inventory_item_count_lte,
        inventory_item_count_n=inventory_item_count_n,
        is_full_depth=is_full_depth,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        latitude=latitude,
        latitude_empty=latitude_empty,
        latitude_gt=latitude_gt,
        latitude_gte=latitude_gte,
        latitude_lt=latitude_lt,
        latitude_lte=latitude_lte,
        latitude_n=latitude_n,
        limit=limit,
        local_context_data=local_context_data,
        location=location,
        location_n=location_n,
        location_id=location_id,
        location_id_n=location_id_n,
        longitude=longitude,
        longitude_empty=longitude_empty,
        longitude_gt=longitude_gt,
        longitude_gte=longitude_gte,
        longitude_lt=longitude_lt,
        longitude_lte=longitude_lte,
        longitude_n=longitude_n,
        mac_address=mac_address,
        mac_address_ic=mac_address_ic,
        mac_address_ie=mac_address_ie,
        mac_address_iew=mac_address_iew,
        mac_address_isw=mac_address_isw,
        mac_address_n=mac_address_n,
        mac_address_nic=mac_address_nic,
        mac_address_nie=mac_address_nie,
        mac_address_niew=mac_address_niew,
        mac_address_nisw=mac_address_nisw,
        manufacturer=manufacturer,
        manufacturer_n=manufacturer_n,
        manufacturer_id=manufacturer_id,
        manufacturer_id_n=manufacturer_id_n,
        model=model,
        model_n=model_n,
        modified_by_request=modified_by_request,
        module_bay_count=module_bay_count,
        module_bay_count_empty=module_bay_count_empty,
        module_bay_count_gt=module_bay_count_gt,
        module_bay_count_gte=module_bay_count_gte,
        module_bay_count_lt=module_bay_count_lt,
        module_bay_count_lte=module_bay_count_lte,
        module_bay_count_n=module_bay_count_n,
        module_bays=module_bays,
        name=name,
        name_empty=name_empty,
        name_ic=name_ic,
        name_ie=name_ie,
        name_iew=name_iew,
        name_isw=name_isw,
        name_n=name_n,
        name_nic=name_nic,
        name_nie=name_nie,
        name_niew=name_niew,
        name_nisw=name_nisw,
        offset=offset,
        oob_ip_id=oob_ip_id,
        oob_ip_id_n=oob_ip_id_n,
        ordering=ordering,
        parent_bay_id=parent_bay_id,
        parent_bay_id_n=parent_bay_id_n,
        parent_device_id=parent_device_id,
        parent_device_id_n=parent_device_id_n,
        pass_through_ports=pass_through_ports,
        platform=platform,
        platform_n=platform_n,
        platform_id=platform_id,
        platform_id_n=platform_id_n,
        position=position,
        position_empty=position_empty,
        position_gt=position_gt,
        position_gte=position_gte,
        position_lt=position_lt,
        position_lte=position_lte,
        position_n=position_n,
        power_outlet_count=power_outlet_count,
        power_outlet_count_empty=power_outlet_count_empty,
        power_outlet_count_gt=power_outlet_count_gt,
        power_outlet_count_gte=power_outlet_count_gte,
        power_outlet_count_lt=power_outlet_count_lt,
        power_outlet_count_lte=power_outlet_count_lte,
        power_outlet_count_n=power_outlet_count_n,
        power_outlets=power_outlets,
        power_port_count=power_port_count,
        power_port_count_empty=power_port_count_empty,
        power_port_count_gt=power_port_count_gt,
        power_port_count_gte=power_port_count_gte,
        power_port_count_lt=power_port_count_lt,
        power_port_count_lte=power_port_count_lte,
        power_port_count_n=power_port_count_n,
        power_ports=power_ports,
        primary_ip4=primary_ip4,
        primary_ip4_n=primary_ip4_n,
        primary_ip4_id=primary_ip4_id,
        primary_ip4_id_n=primary_ip4_id_n,
        primary_ip6=primary_ip6,
        primary_ip6_n=primary_ip6_n,
        primary_ip6_id=primary_ip6_id,
        primary_ip6_id_n=primary_ip6_id_n,
        q=q,
        rack_id=rack_id,
        rack_id_n=rack_id_n,
        rear_port_count=rear_port_count,
        rear_port_count_empty=rear_port_count_empty,
        rear_port_count_gt=rear_port_count_gt,
        rear_port_count_gte=rear_port_count_gte,
        rear_port_count_lt=rear_port_count_lt,
        rear_port_count_lte=rear_port_count_lte,
        rear_port_count_n=rear_port_count_n,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
        serial=serial,
        serial_empty=serial_empty,
        serial_ic=serial_ic,
        serial_ie=serial_ie,
        serial_iew=serial_iew,
        serial_isw=serial_isw,
        serial_n=serial_n,
        serial_nic=serial_nic,
        serial_nie=serial_nie,
        serial_niew=serial_niew,
        serial_nisw=serial_nisw,
        site=site,
        site_n=site_n,
        site_group=site_group,
        site_group_n=site_group_n,
        site_group_id=site_group_id,
        site_group_id_n=site_group_id_n,
        site_id=site_id,
        site_id_n=site_id_n,
        status=status,
        status_empty=status_empty,
        status_ic=status_ic,
        status_ie=status_ie,
        status_iew=status_iew,
        status_isw=status_isw,
        status_n=status_n,
        status_nic=status_nic,
        status_nie=status_nie,
        status_niew=status_niew,
        status_nisw=status_nisw,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        tenant=tenant,
        tenant_n=tenant_n,
        tenant_group=tenant_group,
        tenant_group_n=tenant_group_n,
        tenant_group_id=tenant_group_id,
        tenant_group_id_n=tenant_group_id_n,
        tenant_id=tenant_id,
        tenant_id_n=tenant_id_n,
        updated_by_request=updated_by_request,
        vc_position=vc_position,
        vc_position_empty=vc_position_empty,
        vc_position_gt=vc_position_gt,
        vc_position_gte=vc_position_gte,
        vc_position_lt=vc_position_lt,
        vc_position_lte=vc_position_lte,
        vc_position_n=vc_position_n,
        vc_priority=vc_priority,
        vc_priority_empty=vc_priority_empty,
        vc_priority_gt=vc_priority_gt,
        vc_priority_gte=vc_priority_gte,
        vc_priority_lt=vc_priority_lt,
        vc_priority_lte=vc_priority_lte,
        vc_priority_n=vc_priority_n,
        virtual_chassis_id=virtual_chassis_id,
        virtual_chassis_id_n=virtual_chassis_id_n,
        virtual_chassis_member=virtual_chassis_member,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    airflow: Union[Unset, DcimDevicesListAirflow] = UNSET,
    asset_tag: Union[Unset, list[str]] = UNSET,
    asset_tag_empty: Union[Unset, bool] = UNSET,
    asset_tag_ic: Union[Unset, list[str]] = UNSET,
    asset_tag_ie: Union[Unset, list[str]] = UNSET,
    asset_tag_iew: Union[Unset, list[str]] = UNSET,
    asset_tag_isw: Union[Unset, list[str]] = UNSET,
    asset_tag_n: Union[Unset, list[str]] = UNSET,
    asset_tag_nic: Union[Unset, list[str]] = UNSET,
    asset_tag_nie: Union[Unset, list[str]] = UNSET,
    asset_tag_niew: Union[Unset, list[str]] = UNSET,
    asset_tag_nisw: Union[Unset, list[str]] = UNSET,
    cluster_group: Union[Unset, list[str]] = UNSET,
    cluster_group_n: Union[Unset, list[str]] = UNSET,
    cluster_group_id: Union[Unset, list[int]] = UNSET,
    cluster_group_id_n: Union[Unset, list[int]] = UNSET,
    cluster_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cluster_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    config_template_id: Union[Unset, list[Union[None, int]]] = UNSET,
    config_template_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    console_port_count: Union[Unset, list[int]] = UNSET,
    console_port_count_empty: Union[Unset, bool] = UNSET,
    console_port_count_gt: Union[Unset, list[int]] = UNSET,
    console_port_count_gte: Union[Unset, list[int]] = UNSET,
    console_port_count_lt: Union[Unset, list[int]] = UNSET,
    console_port_count_lte: Union[Unset, list[int]] = UNSET,
    console_port_count_n: Union[Unset, list[int]] = UNSET,
    console_ports: Union[Unset, bool] = UNSET,
    console_server_port_count: Union[Unset, list[int]] = UNSET,
    console_server_port_count_empty: Union[Unset, bool] = UNSET,
    console_server_port_count_gt: Union[Unset, list[int]] = UNSET,
    console_server_port_count_gte: Union[Unset, list[int]] = UNSET,
    console_server_port_count_lt: Union[Unset, list[int]] = UNSET,
    console_server_port_count_lte: Union[Unset, list[int]] = UNSET,
    console_server_port_count_n: Union[Unset, list[int]] = UNSET,
    console_server_ports: Union[Unset, bool] = UNSET,
    contact: Union[Unset, list[int]] = UNSET,
    contact_n: Union[Unset, list[int]] = UNSET,
    contact_group: Union[Unset, list[str]] = UNSET,
    contact_group_n: Union[Unset, list[str]] = UNSET,
    contact_role: Union[Unset, list[int]] = UNSET,
    contact_role_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    description: Union[Unset, list[str]] = UNSET,
    description_empty: Union[Unset, bool] = UNSET,
    description_ic: Union[Unset, list[str]] = UNSET,
    description_ie: Union[Unset, list[str]] = UNSET,
    description_iew: Union[Unset, list[str]] = UNSET,
    description_isw: Union[Unset, list[str]] = UNSET,
    description_n: Union[Unset, list[str]] = UNSET,
    description_nic: Union[Unset, list[str]] = UNSET,
    description_nie: Union[Unset, list[str]] = UNSET,
    description_niew: Union[Unset, list[str]] = UNSET,
    description_nisw: Union[Unset, list[str]] = UNSET,
    device_bay_count: Union[Unset, list[int]] = UNSET,
    device_bay_count_empty: Union[Unset, bool] = UNSET,
    device_bay_count_gt: Union[Unset, list[int]] = UNSET,
    device_bay_count_gte: Union[Unset, list[int]] = UNSET,
    device_bay_count_lt: Union[Unset, list[int]] = UNSET,
    device_bay_count_lte: Union[Unset, list[int]] = UNSET,
    device_bay_count_n: Union[Unset, list[int]] = UNSET,
    device_bays: Union[Unset, bool] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    front_port_count: Union[Unset, list[int]] = UNSET,
    front_port_count_empty: Union[Unset, bool] = UNSET,
    front_port_count_gt: Union[Unset, list[int]] = UNSET,
    front_port_count_gte: Union[Unset, list[int]] = UNSET,
    front_port_count_lt: Union[Unset, list[int]] = UNSET,
    front_port_count_lte: Union[Unset, list[int]] = UNSET,
    front_port_count_n: Union[Unset, list[int]] = UNSET,
    has_oob_ip: Union[Unset, bool] = UNSET,
    has_primary_ip: Union[Unset, bool] = UNSET,
    has_virtual_device_context: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_count: Union[Unset, list[int]] = UNSET,
    interface_count_empty: Union[Unset, bool] = UNSET,
    interface_count_gt: Union[Unset, list[int]] = UNSET,
    interface_count_gte: Union[Unset, list[int]] = UNSET,
    interface_count_lt: Union[Unset, list[int]] = UNSET,
    interface_count_lte: Union[Unset, list[int]] = UNSET,
    interface_count_n: Union[Unset, list[int]] = UNSET,
    interfaces: Union[Unset, bool] = UNSET,
    inventory_item_count: Union[Unset, list[int]] = UNSET,
    inventory_item_count_empty: Union[Unset, bool] = UNSET,
    inventory_item_count_gt: Union[Unset, list[int]] = UNSET,
    inventory_item_count_gte: Union[Unset, list[int]] = UNSET,
    inventory_item_count_lt: Union[Unset, list[int]] = UNSET,
    inventory_item_count_lte: Union[Unset, list[int]] = UNSET,
    inventory_item_count_n: Union[Unset, list[int]] = UNSET,
    is_full_depth: Union[Unset, bool] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    latitude: Union[Unset, list[float]] = UNSET,
    latitude_empty: Union[Unset, bool] = UNSET,
    latitude_gt: Union[Unset, list[float]] = UNSET,
    latitude_gte: Union[Unset, list[float]] = UNSET,
    latitude_lt: Union[Unset, list[float]] = UNSET,
    latitude_lte: Union[Unset, list[float]] = UNSET,
    latitude_n: Union[Unset, list[float]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    local_context_data: Union[Unset, bool] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[str]] = UNSET,
    location_id_n: Union[Unset, list[str]] = UNSET,
    longitude: Union[Unset, list[float]] = UNSET,
    longitude_empty: Union[Unset, bool] = UNSET,
    longitude_gt: Union[Unset, list[float]] = UNSET,
    longitude_gte: Union[Unset, list[float]] = UNSET,
    longitude_lt: Union[Unset, list[float]] = UNSET,
    longitude_lte: Union[Unset, list[float]] = UNSET,
    longitude_n: Union[Unset, list[float]] = UNSET,
    mac_address: Union[Unset, list[str]] = UNSET,
    mac_address_ic: Union[Unset, list[str]] = UNSET,
    mac_address_ie: Union[Unset, list[str]] = UNSET,
    mac_address_iew: Union[Unset, list[str]] = UNSET,
    mac_address_isw: Union[Unset, list[str]] = UNSET,
    mac_address_n: Union[Unset, list[str]] = UNSET,
    mac_address_nic: Union[Unset, list[str]] = UNSET,
    mac_address_nie: Union[Unset, list[str]] = UNSET,
    mac_address_niew: Union[Unset, list[str]] = UNSET,
    mac_address_nisw: Union[Unset, list[str]] = UNSET,
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    model: Union[Unset, list[str]] = UNSET,
    model_n: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_bay_count: Union[Unset, list[int]] = UNSET,
    module_bay_count_empty: Union[Unset, bool] = UNSET,
    module_bay_count_gt: Union[Unset, list[int]] = UNSET,
    module_bay_count_gte: Union[Unset, list[int]] = UNSET,
    module_bay_count_lt: Union[Unset, list[int]] = UNSET,
    module_bay_count_lte: Union[Unset, list[int]] = UNSET,
    module_bay_count_n: Union[Unset, list[int]] = UNSET,
    module_bays: Union[Unset, bool] = UNSET,
    name: Union[Unset, list[str]] = UNSET,
    name_empty: Union[Unset, bool] = UNSET,
    name_ic: Union[Unset, list[str]] = UNSET,
    name_ie: Union[Unset, list[str]] = UNSET,
    name_iew: Union[Unset, list[str]] = UNSET,
    name_isw: Union[Unset, list[str]] = UNSET,
    name_n: Union[Unset, list[str]] = UNSET,
    name_nic: Union[Unset, list[str]] = UNSET,
    name_nie: Union[Unset, list[str]] = UNSET,
    name_niew: Union[Unset, list[str]] = UNSET,
    name_nisw: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    oob_ip_id: Union[Unset, list[int]] = UNSET,
    oob_ip_id_n: Union[Unset, list[int]] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_bay_id: Union[Unset, list[int]] = UNSET,
    parent_bay_id_n: Union[Unset, list[int]] = UNSET,
    parent_device_id: Union[Unset, list[int]] = UNSET,
    parent_device_id_n: Union[Unset, list[int]] = UNSET,
    pass_through_ports: Union[Unset, bool] = UNSET,
    platform: Union[Unset, list[str]] = UNSET,
    platform_n: Union[Unset, list[str]] = UNSET,
    platform_id: Union[Unset, list[Union[None, int]]] = UNSET,
    platform_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    position: Union[Unset, list[float]] = UNSET,
    position_empty: Union[Unset, bool] = UNSET,
    position_gt: Union[Unset, list[float]] = UNSET,
    position_gte: Union[Unset, list[float]] = UNSET,
    position_lt: Union[Unset, list[float]] = UNSET,
    position_lte: Union[Unset, list[float]] = UNSET,
    position_n: Union[Unset, list[float]] = UNSET,
    power_outlet_count: Union[Unset, list[int]] = UNSET,
    power_outlet_count_empty: Union[Unset, bool] = UNSET,
    power_outlet_count_gt: Union[Unset, list[int]] = UNSET,
    power_outlet_count_gte: Union[Unset, list[int]] = UNSET,
    power_outlet_count_lt: Union[Unset, list[int]] = UNSET,
    power_outlet_count_lte: Union[Unset, list[int]] = UNSET,
    power_outlet_count_n: Union[Unset, list[int]] = UNSET,
    power_outlets: Union[Unset, bool] = UNSET,
    power_port_count: Union[Unset, list[int]] = UNSET,
    power_port_count_empty: Union[Unset, bool] = UNSET,
    power_port_count_gt: Union[Unset, list[int]] = UNSET,
    power_port_count_gte: Union[Unset, list[int]] = UNSET,
    power_port_count_lt: Union[Unset, list[int]] = UNSET,
    power_port_count_lte: Union[Unset, list[int]] = UNSET,
    power_port_count_n: Union[Unset, list[int]] = UNSET,
    power_ports: Union[Unset, bool] = UNSET,
    primary_ip4: Union[Unset, list[str]] = UNSET,
    primary_ip4_n: Union[Unset, list[str]] = UNSET,
    primary_ip4_id: Union[Unset, list[int]] = UNSET,
    primary_ip4_id_n: Union[Unset, list[int]] = UNSET,
    primary_ip6: Union[Unset, list[str]] = UNSET,
    primary_ip6_n: Union[Unset, list[str]] = UNSET,
    primary_ip6_id: Union[Unset, list[int]] = UNSET,
    primary_ip6_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    rear_port_count: Union[Unset, list[int]] = UNSET,
    rear_port_count_empty: Union[Unset, bool] = UNSET,
    rear_port_count_gt: Union[Unset, list[int]] = UNSET,
    rear_port_count_gte: Union[Unset, list[int]] = UNSET,
    rear_port_count_lt: Union[Unset, list[int]] = UNSET,
    rear_port_count_lte: Union[Unset, list[int]] = UNSET,
    rear_port_count_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[str]] = UNSET,
    role_id_n: Union[Unset, list[str]] = UNSET,
    serial: Union[Unset, list[str]] = UNSET,
    serial_empty: Union[Unset, bool] = UNSET,
    serial_ic: Union[Unset, list[str]] = UNSET,
    serial_ie: Union[Unset, list[str]] = UNSET,
    serial_iew: Union[Unset, list[str]] = UNSET,
    serial_isw: Union[Unset, list[str]] = UNSET,
    serial_n: Union[Unset, list[str]] = UNSET,
    serial_nic: Union[Unset, list[str]] = UNSET,
    serial_nie: Union[Unset, list[str]] = UNSET,
    serial_niew: Union[Unset, list[str]] = UNSET,
    serial_nisw: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    status: Union[Unset, list[str]] = UNSET,
    status_empty: Union[Unset, bool] = UNSET,
    status_ic: Union[Unset, list[str]] = UNSET,
    status_ie: Union[Unset, list[str]] = UNSET,
    status_iew: Union[Unset, list[str]] = UNSET,
    status_isw: Union[Unset, list[str]] = UNSET,
    status_n: Union[Unset, list[str]] = UNSET,
    status_nic: Union[Unset, list[str]] = UNSET,
    status_nie: Union[Unset, list[str]] = UNSET,
    status_niew: Union[Unset, list[str]] = UNSET,
    status_nisw: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tenant: Union[Unset, list[str]] = UNSET,
    tenant_n: Union[Unset, list[str]] = UNSET,
    tenant_group: Union[Unset, list[str]] = UNSET,
    tenant_group_n: Union[Unset, list[str]] = UNSET,
    tenant_group_id: Union[Unset, list[str]] = UNSET,
    tenant_group_id_n: Union[Unset, list[str]] = UNSET,
    tenant_id: Union[Unset, list[Union[None, int]]] = UNSET,
    tenant_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    vc_position: Union[Unset, list[int]] = UNSET,
    vc_position_empty: Union[Unset, bool] = UNSET,
    vc_position_gt: Union[Unset, list[int]] = UNSET,
    vc_position_gte: Union[Unset, list[int]] = UNSET,
    vc_position_lt: Union[Unset, list[int]] = UNSET,
    vc_position_lte: Union[Unset, list[int]] = UNSET,
    vc_position_n: Union[Unset, list[int]] = UNSET,
    vc_priority: Union[Unset, list[int]] = UNSET,
    vc_priority_empty: Union[Unset, bool] = UNSET,
    vc_priority_gt: Union[Unset, list[int]] = UNSET,
    vc_priority_gte: Union[Unset, list[int]] = UNSET,
    vc_priority_lt: Union[Unset, list[int]] = UNSET,
    vc_priority_lte: Union[Unset, list[int]] = UNSET,
    vc_priority_n: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id_n: Union[Unset, list[int]] = UNSET,
    virtual_chassis_member: Union[Unset, bool] = UNSET,
) -> Optional[PaginatedDeviceWithConfigContextList]:
    """Get a list of device objects.

    Args:
        airflow (Union[Unset, DcimDevicesListAirflow]):
        asset_tag (Union[Unset, list[str]]):
        asset_tag_empty (Union[Unset, bool]):
        asset_tag_ic (Union[Unset, list[str]]):
        asset_tag_ie (Union[Unset, list[str]]):
        asset_tag_iew (Union[Unset, list[str]]):
        asset_tag_isw (Union[Unset, list[str]]):
        asset_tag_n (Union[Unset, list[str]]):
        asset_tag_nic (Union[Unset, list[str]]):
        asset_tag_nie (Union[Unset, list[str]]):
        asset_tag_niew (Union[Unset, list[str]]):
        asset_tag_nisw (Union[Unset, list[str]]):
        cluster_group (Union[Unset, list[str]]):
        cluster_group_n (Union[Unset, list[str]]):
        cluster_group_id (Union[Unset, list[int]]):
        cluster_group_id_n (Union[Unset, list[int]]):
        cluster_id (Union[Unset, list[Union[None, int]]]):
        cluster_id_n (Union[Unset, list[Union[None, int]]]):
        config_template_id (Union[Unset, list[Union[None, int]]]):
        config_template_id_n (Union[Unset, list[Union[None, int]]]):
        console_port_count (Union[Unset, list[int]]):
        console_port_count_empty (Union[Unset, bool]):
        console_port_count_gt (Union[Unset, list[int]]):
        console_port_count_gte (Union[Unset, list[int]]):
        console_port_count_lt (Union[Unset, list[int]]):
        console_port_count_lte (Union[Unset, list[int]]):
        console_port_count_n (Union[Unset, list[int]]):
        console_ports (Union[Unset, bool]):
        console_server_port_count (Union[Unset, list[int]]):
        console_server_port_count_empty (Union[Unset, bool]):
        console_server_port_count_gt (Union[Unset, list[int]]):
        console_server_port_count_gte (Union[Unset, list[int]]):
        console_server_port_count_lt (Union[Unset, list[int]]):
        console_server_port_count_lte (Union[Unset, list[int]]):
        console_server_port_count_n (Union[Unset, list[int]]):
        console_server_ports (Union[Unset, bool]):
        contact (Union[Unset, list[int]]):
        contact_n (Union[Unset, list[int]]):
        contact_group (Union[Unset, list[str]]):
        contact_group_n (Union[Unset, list[str]]):
        contact_role (Union[Unset, list[int]]):
        contact_role_n (Union[Unset, list[int]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        description (Union[Unset, list[str]]):
        description_empty (Union[Unset, bool]):
        description_ic (Union[Unset, list[str]]):
        description_ie (Union[Unset, list[str]]):
        description_iew (Union[Unset, list[str]]):
        description_isw (Union[Unset, list[str]]):
        description_n (Union[Unset, list[str]]):
        description_nic (Union[Unset, list[str]]):
        description_nie (Union[Unset, list[str]]):
        description_niew (Union[Unset, list[str]]):
        description_nisw (Union[Unset, list[str]]):
        device_bay_count (Union[Unset, list[int]]):
        device_bay_count_empty (Union[Unset, bool]):
        device_bay_count_gt (Union[Unset, list[int]]):
        device_bay_count_gte (Union[Unset, list[int]]):
        device_bay_count_lt (Union[Unset, list[int]]):
        device_bay_count_lte (Union[Unset, list[int]]):
        device_bay_count_n (Union[Unset, list[int]]):
        device_bays (Union[Unset, bool]):
        device_type (Union[Unset, list[str]]):
        device_type_n (Union[Unset, list[str]]):
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
        front_port_count (Union[Unset, list[int]]):
        front_port_count_empty (Union[Unset, bool]):
        front_port_count_gt (Union[Unset, list[int]]):
        front_port_count_gte (Union[Unset, list[int]]):
        front_port_count_lt (Union[Unset, list[int]]):
        front_port_count_lte (Union[Unset, list[int]]):
        front_port_count_n (Union[Unset, list[int]]):
        has_oob_ip (Union[Unset, bool]):
        has_primary_ip (Union[Unset, bool]):
        has_virtual_device_context (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_count (Union[Unset, list[int]]):
        interface_count_empty (Union[Unset, bool]):
        interface_count_gt (Union[Unset, list[int]]):
        interface_count_gte (Union[Unset, list[int]]):
        interface_count_lt (Union[Unset, list[int]]):
        interface_count_lte (Union[Unset, list[int]]):
        interface_count_n (Union[Unset, list[int]]):
        interfaces (Union[Unset, bool]):
        inventory_item_count (Union[Unset, list[int]]):
        inventory_item_count_empty (Union[Unset, bool]):
        inventory_item_count_gt (Union[Unset, list[int]]):
        inventory_item_count_gte (Union[Unset, list[int]]):
        inventory_item_count_lt (Union[Unset, list[int]]):
        inventory_item_count_lte (Union[Unset, list[int]]):
        inventory_item_count_n (Union[Unset, list[int]]):
        is_full_depth (Union[Unset, bool]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        latitude (Union[Unset, list[float]]):
        latitude_empty (Union[Unset, bool]):
        latitude_gt (Union[Unset, list[float]]):
        latitude_gte (Union[Unset, list[float]]):
        latitude_lt (Union[Unset, list[float]]):
        latitude_lte (Union[Unset, list[float]]):
        latitude_n (Union[Unset, list[float]]):
        limit (Union[Unset, int]):
        local_context_data (Union[Unset, bool]):
        location (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_id (Union[Unset, list[str]]):
        location_id_n (Union[Unset, list[str]]):
        longitude (Union[Unset, list[float]]):
        longitude_empty (Union[Unset, bool]):
        longitude_gt (Union[Unset, list[float]]):
        longitude_gte (Union[Unset, list[float]]):
        longitude_lt (Union[Unset, list[float]]):
        longitude_lte (Union[Unset, list[float]]):
        longitude_n (Union[Unset, list[float]]):
        mac_address (Union[Unset, list[str]]):
        mac_address_ic (Union[Unset, list[str]]):
        mac_address_ie (Union[Unset, list[str]]):
        mac_address_iew (Union[Unset, list[str]]):
        mac_address_isw (Union[Unset, list[str]]):
        mac_address_n (Union[Unset, list[str]]):
        mac_address_nic (Union[Unset, list[str]]):
        mac_address_nie (Union[Unset, list[str]]):
        mac_address_niew (Union[Unset, list[str]]):
        mac_address_nisw (Union[Unset, list[str]]):
        manufacturer (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_id (Union[Unset, list[int]]):
        manufacturer_id_n (Union[Unset, list[int]]):
        model (Union[Unset, list[str]]):
        model_n (Union[Unset, list[str]]):
        modified_by_request (Union[Unset, UUID]):
        module_bay_count (Union[Unset, list[int]]):
        module_bay_count_empty (Union[Unset, bool]):
        module_bay_count_gt (Union[Unset, list[int]]):
        module_bay_count_gte (Union[Unset, list[int]]):
        module_bay_count_lt (Union[Unset, list[int]]):
        module_bay_count_lte (Union[Unset, list[int]]):
        module_bay_count_n (Union[Unset, list[int]]):
        module_bays (Union[Unset, bool]):
        name (Union[Unset, list[str]]):
        name_empty (Union[Unset, bool]):
        name_ic (Union[Unset, list[str]]):
        name_ie (Union[Unset, list[str]]):
        name_iew (Union[Unset, list[str]]):
        name_isw (Union[Unset, list[str]]):
        name_n (Union[Unset, list[str]]):
        name_nic (Union[Unset, list[str]]):
        name_nie (Union[Unset, list[str]]):
        name_niew (Union[Unset, list[str]]):
        name_nisw (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        oob_ip_id (Union[Unset, list[int]]):
        oob_ip_id_n (Union[Unset, list[int]]):
        ordering (Union[Unset, str]):
        parent_bay_id (Union[Unset, list[int]]):
        parent_bay_id_n (Union[Unset, list[int]]):
        parent_device_id (Union[Unset, list[int]]):
        parent_device_id_n (Union[Unset, list[int]]):
        pass_through_ports (Union[Unset, bool]):
        platform (Union[Unset, list[str]]):
        platform_n (Union[Unset, list[str]]):
        platform_id (Union[Unset, list[Union[None, int]]]):
        platform_id_n (Union[Unset, list[Union[None, int]]]):
        position (Union[Unset, list[float]]):
        position_empty (Union[Unset, bool]):
        position_gt (Union[Unset, list[float]]):
        position_gte (Union[Unset, list[float]]):
        position_lt (Union[Unset, list[float]]):
        position_lte (Union[Unset, list[float]]):
        position_n (Union[Unset, list[float]]):
        power_outlet_count (Union[Unset, list[int]]):
        power_outlet_count_empty (Union[Unset, bool]):
        power_outlet_count_gt (Union[Unset, list[int]]):
        power_outlet_count_gte (Union[Unset, list[int]]):
        power_outlet_count_lt (Union[Unset, list[int]]):
        power_outlet_count_lte (Union[Unset, list[int]]):
        power_outlet_count_n (Union[Unset, list[int]]):
        power_outlets (Union[Unset, bool]):
        power_port_count (Union[Unset, list[int]]):
        power_port_count_empty (Union[Unset, bool]):
        power_port_count_gt (Union[Unset, list[int]]):
        power_port_count_gte (Union[Unset, list[int]]):
        power_port_count_lt (Union[Unset, list[int]]):
        power_port_count_lte (Union[Unset, list[int]]):
        power_port_count_n (Union[Unset, list[int]]):
        power_ports (Union[Unset, bool]):
        primary_ip4 (Union[Unset, list[str]]):
        primary_ip4_n (Union[Unset, list[str]]):
        primary_ip4_id (Union[Unset, list[int]]):
        primary_ip4_id_n (Union[Unset, list[int]]):
        primary_ip6 (Union[Unset, list[str]]):
        primary_ip6_n (Union[Unset, list[str]]):
        primary_ip6_id (Union[Unset, list[int]]):
        primary_ip6_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        rack_id (Union[Unset, list[int]]):
        rack_id_n (Union[Unset, list[int]]):
        rear_port_count (Union[Unset, list[int]]):
        rear_port_count_empty (Union[Unset, bool]):
        rear_port_count_gt (Union[Unset, list[int]]):
        rear_port_count_gte (Union[Unset, list[int]]):
        rear_port_count_lt (Union[Unset, list[int]]):
        rear_port_count_lte (Union[Unset, list[int]]):
        rear_port_count_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[str]]):
        role_id_n (Union[Unset, list[str]]):
        serial (Union[Unset, list[str]]):
        serial_empty (Union[Unset, bool]):
        serial_ic (Union[Unset, list[str]]):
        serial_ie (Union[Unset, list[str]]):
        serial_iew (Union[Unset, list[str]]):
        serial_isw (Union[Unset, list[str]]):
        serial_n (Union[Unset, list[str]]):
        serial_nic (Union[Unset, list[str]]):
        serial_nie (Union[Unset, list[str]]):
        serial_niew (Union[Unset, list[str]]):
        serial_nisw (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
        status (Union[Unset, list[str]]):
        status_empty (Union[Unset, bool]):
        status_ic (Union[Unset, list[str]]):
        status_ie (Union[Unset, list[str]]):
        status_iew (Union[Unset, list[str]]):
        status_isw (Union[Unset, list[str]]):
        status_n (Union[Unset, list[str]]):
        status_nic (Union[Unset, list[str]]):
        status_nie (Union[Unset, list[str]]):
        status_niew (Union[Unset, list[str]]):
        status_nisw (Union[Unset, list[str]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        tenant (Union[Unset, list[str]]):
        tenant_n (Union[Unset, list[str]]):
        tenant_group (Union[Unset, list[str]]):
        tenant_group_n (Union[Unset, list[str]]):
        tenant_group_id (Union[Unset, list[str]]):
        tenant_group_id_n (Union[Unset, list[str]]):
        tenant_id (Union[Unset, list[Union[None, int]]]):
        tenant_id_n (Union[Unset, list[Union[None, int]]]):
        updated_by_request (Union[Unset, UUID]):
        vc_position (Union[Unset, list[int]]):
        vc_position_empty (Union[Unset, bool]):
        vc_position_gt (Union[Unset, list[int]]):
        vc_position_gte (Union[Unset, list[int]]):
        vc_position_lt (Union[Unset, list[int]]):
        vc_position_lte (Union[Unset, list[int]]):
        vc_position_n (Union[Unset, list[int]]):
        vc_priority (Union[Unset, list[int]]):
        vc_priority_empty (Union[Unset, bool]):
        vc_priority_gt (Union[Unset, list[int]]):
        vc_priority_gte (Union[Unset, list[int]]):
        vc_priority_lt (Union[Unset, list[int]]):
        vc_priority_lte (Union[Unset, list[int]]):
        vc_priority_n (Union[Unset, list[int]]):
        virtual_chassis_id (Union[Unset, list[int]]):
        virtual_chassis_id_n (Union[Unset, list[int]]):
        virtual_chassis_member (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDeviceWithConfigContextList
    """

    return sync_detailed(
        client=client,
        airflow=airflow,
        asset_tag=asset_tag,
        asset_tag_empty=asset_tag_empty,
        asset_tag_ic=asset_tag_ic,
        asset_tag_ie=asset_tag_ie,
        asset_tag_iew=asset_tag_iew,
        asset_tag_isw=asset_tag_isw,
        asset_tag_n=asset_tag_n,
        asset_tag_nic=asset_tag_nic,
        asset_tag_nie=asset_tag_nie,
        asset_tag_niew=asset_tag_niew,
        asset_tag_nisw=asset_tag_nisw,
        cluster_group=cluster_group,
        cluster_group_n=cluster_group_n,
        cluster_group_id=cluster_group_id,
        cluster_group_id_n=cluster_group_id_n,
        cluster_id=cluster_id,
        cluster_id_n=cluster_id_n,
        config_template_id=config_template_id,
        config_template_id_n=config_template_id_n,
        console_port_count=console_port_count,
        console_port_count_empty=console_port_count_empty,
        console_port_count_gt=console_port_count_gt,
        console_port_count_gte=console_port_count_gte,
        console_port_count_lt=console_port_count_lt,
        console_port_count_lte=console_port_count_lte,
        console_port_count_n=console_port_count_n,
        console_ports=console_ports,
        console_server_port_count=console_server_port_count,
        console_server_port_count_empty=console_server_port_count_empty,
        console_server_port_count_gt=console_server_port_count_gt,
        console_server_port_count_gte=console_server_port_count_gte,
        console_server_port_count_lt=console_server_port_count_lt,
        console_server_port_count_lte=console_server_port_count_lte,
        console_server_port_count_n=console_server_port_count_n,
        console_server_ports=console_server_ports,
        contact=contact,
        contact_n=contact_n,
        contact_group=contact_group,
        contact_group_n=contact_group_n,
        contact_role=contact_role,
        contact_role_n=contact_role_n,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        description=description,
        description_empty=description_empty,
        description_ic=description_ic,
        description_ie=description_ie,
        description_iew=description_iew,
        description_isw=description_isw,
        description_n=description_n,
        description_nic=description_nic,
        description_nie=description_nie,
        description_niew=description_niew,
        description_nisw=description_nisw,
        device_bay_count=device_bay_count,
        device_bay_count_empty=device_bay_count_empty,
        device_bay_count_gt=device_bay_count_gt,
        device_bay_count_gte=device_bay_count_gte,
        device_bay_count_lt=device_bay_count_lt,
        device_bay_count_lte=device_bay_count_lte,
        device_bay_count_n=device_bay_count_n,
        device_bays=device_bays,
        device_type=device_type,
        device_type_n=device_type_n,
        device_type_id=device_type_id,
        device_type_id_n=device_type_id_n,
        front_port_count=front_port_count,
        front_port_count_empty=front_port_count_empty,
        front_port_count_gt=front_port_count_gt,
        front_port_count_gte=front_port_count_gte,
        front_port_count_lt=front_port_count_lt,
        front_port_count_lte=front_port_count_lte,
        front_port_count_n=front_port_count_n,
        has_oob_ip=has_oob_ip,
        has_primary_ip=has_primary_ip,
        has_virtual_device_context=has_virtual_device_context,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface_count=interface_count,
        interface_count_empty=interface_count_empty,
        interface_count_gt=interface_count_gt,
        interface_count_gte=interface_count_gte,
        interface_count_lt=interface_count_lt,
        interface_count_lte=interface_count_lte,
        interface_count_n=interface_count_n,
        interfaces=interfaces,
        inventory_item_count=inventory_item_count,
        inventory_item_count_empty=inventory_item_count_empty,
        inventory_item_count_gt=inventory_item_count_gt,
        inventory_item_count_gte=inventory_item_count_gte,
        inventory_item_count_lt=inventory_item_count_lt,
        inventory_item_count_lte=inventory_item_count_lte,
        inventory_item_count_n=inventory_item_count_n,
        is_full_depth=is_full_depth,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        latitude=latitude,
        latitude_empty=latitude_empty,
        latitude_gt=latitude_gt,
        latitude_gte=latitude_gte,
        latitude_lt=latitude_lt,
        latitude_lte=latitude_lte,
        latitude_n=latitude_n,
        limit=limit,
        local_context_data=local_context_data,
        location=location,
        location_n=location_n,
        location_id=location_id,
        location_id_n=location_id_n,
        longitude=longitude,
        longitude_empty=longitude_empty,
        longitude_gt=longitude_gt,
        longitude_gte=longitude_gte,
        longitude_lt=longitude_lt,
        longitude_lte=longitude_lte,
        longitude_n=longitude_n,
        mac_address=mac_address,
        mac_address_ic=mac_address_ic,
        mac_address_ie=mac_address_ie,
        mac_address_iew=mac_address_iew,
        mac_address_isw=mac_address_isw,
        mac_address_n=mac_address_n,
        mac_address_nic=mac_address_nic,
        mac_address_nie=mac_address_nie,
        mac_address_niew=mac_address_niew,
        mac_address_nisw=mac_address_nisw,
        manufacturer=manufacturer,
        manufacturer_n=manufacturer_n,
        manufacturer_id=manufacturer_id,
        manufacturer_id_n=manufacturer_id_n,
        model=model,
        model_n=model_n,
        modified_by_request=modified_by_request,
        module_bay_count=module_bay_count,
        module_bay_count_empty=module_bay_count_empty,
        module_bay_count_gt=module_bay_count_gt,
        module_bay_count_gte=module_bay_count_gte,
        module_bay_count_lt=module_bay_count_lt,
        module_bay_count_lte=module_bay_count_lte,
        module_bay_count_n=module_bay_count_n,
        module_bays=module_bays,
        name=name,
        name_empty=name_empty,
        name_ic=name_ic,
        name_ie=name_ie,
        name_iew=name_iew,
        name_isw=name_isw,
        name_n=name_n,
        name_nic=name_nic,
        name_nie=name_nie,
        name_niew=name_niew,
        name_nisw=name_nisw,
        offset=offset,
        oob_ip_id=oob_ip_id,
        oob_ip_id_n=oob_ip_id_n,
        ordering=ordering,
        parent_bay_id=parent_bay_id,
        parent_bay_id_n=parent_bay_id_n,
        parent_device_id=parent_device_id,
        parent_device_id_n=parent_device_id_n,
        pass_through_ports=pass_through_ports,
        platform=platform,
        platform_n=platform_n,
        platform_id=platform_id,
        platform_id_n=platform_id_n,
        position=position,
        position_empty=position_empty,
        position_gt=position_gt,
        position_gte=position_gte,
        position_lt=position_lt,
        position_lte=position_lte,
        position_n=position_n,
        power_outlet_count=power_outlet_count,
        power_outlet_count_empty=power_outlet_count_empty,
        power_outlet_count_gt=power_outlet_count_gt,
        power_outlet_count_gte=power_outlet_count_gte,
        power_outlet_count_lt=power_outlet_count_lt,
        power_outlet_count_lte=power_outlet_count_lte,
        power_outlet_count_n=power_outlet_count_n,
        power_outlets=power_outlets,
        power_port_count=power_port_count,
        power_port_count_empty=power_port_count_empty,
        power_port_count_gt=power_port_count_gt,
        power_port_count_gte=power_port_count_gte,
        power_port_count_lt=power_port_count_lt,
        power_port_count_lte=power_port_count_lte,
        power_port_count_n=power_port_count_n,
        power_ports=power_ports,
        primary_ip4=primary_ip4,
        primary_ip4_n=primary_ip4_n,
        primary_ip4_id=primary_ip4_id,
        primary_ip4_id_n=primary_ip4_id_n,
        primary_ip6=primary_ip6,
        primary_ip6_n=primary_ip6_n,
        primary_ip6_id=primary_ip6_id,
        primary_ip6_id_n=primary_ip6_id_n,
        q=q,
        rack_id=rack_id,
        rack_id_n=rack_id_n,
        rear_port_count=rear_port_count,
        rear_port_count_empty=rear_port_count_empty,
        rear_port_count_gt=rear_port_count_gt,
        rear_port_count_gte=rear_port_count_gte,
        rear_port_count_lt=rear_port_count_lt,
        rear_port_count_lte=rear_port_count_lte,
        rear_port_count_n=rear_port_count_n,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
        serial=serial,
        serial_empty=serial_empty,
        serial_ic=serial_ic,
        serial_ie=serial_ie,
        serial_iew=serial_iew,
        serial_isw=serial_isw,
        serial_n=serial_n,
        serial_nic=serial_nic,
        serial_nie=serial_nie,
        serial_niew=serial_niew,
        serial_nisw=serial_nisw,
        site=site,
        site_n=site_n,
        site_group=site_group,
        site_group_n=site_group_n,
        site_group_id=site_group_id,
        site_group_id_n=site_group_id_n,
        site_id=site_id,
        site_id_n=site_id_n,
        status=status,
        status_empty=status_empty,
        status_ic=status_ic,
        status_ie=status_ie,
        status_iew=status_iew,
        status_isw=status_isw,
        status_n=status_n,
        status_nic=status_nic,
        status_nie=status_nie,
        status_niew=status_niew,
        status_nisw=status_nisw,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        tenant=tenant,
        tenant_n=tenant_n,
        tenant_group=tenant_group,
        tenant_group_n=tenant_group_n,
        tenant_group_id=tenant_group_id,
        tenant_group_id_n=tenant_group_id_n,
        tenant_id=tenant_id,
        tenant_id_n=tenant_id_n,
        updated_by_request=updated_by_request,
        vc_position=vc_position,
        vc_position_empty=vc_position_empty,
        vc_position_gt=vc_position_gt,
        vc_position_gte=vc_position_gte,
        vc_position_lt=vc_position_lt,
        vc_position_lte=vc_position_lte,
        vc_position_n=vc_position_n,
        vc_priority=vc_priority,
        vc_priority_empty=vc_priority_empty,
        vc_priority_gt=vc_priority_gt,
        vc_priority_gte=vc_priority_gte,
        vc_priority_lt=vc_priority_lt,
        vc_priority_lte=vc_priority_lte,
        vc_priority_n=vc_priority_n,
        virtual_chassis_id=virtual_chassis_id,
        virtual_chassis_id_n=virtual_chassis_id_n,
        virtual_chassis_member=virtual_chassis_member,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    airflow: Union[Unset, DcimDevicesListAirflow] = UNSET,
    asset_tag: Union[Unset, list[str]] = UNSET,
    asset_tag_empty: Union[Unset, bool] = UNSET,
    asset_tag_ic: Union[Unset, list[str]] = UNSET,
    asset_tag_ie: Union[Unset, list[str]] = UNSET,
    asset_tag_iew: Union[Unset, list[str]] = UNSET,
    asset_tag_isw: Union[Unset, list[str]] = UNSET,
    asset_tag_n: Union[Unset, list[str]] = UNSET,
    asset_tag_nic: Union[Unset, list[str]] = UNSET,
    asset_tag_nie: Union[Unset, list[str]] = UNSET,
    asset_tag_niew: Union[Unset, list[str]] = UNSET,
    asset_tag_nisw: Union[Unset, list[str]] = UNSET,
    cluster_group: Union[Unset, list[str]] = UNSET,
    cluster_group_n: Union[Unset, list[str]] = UNSET,
    cluster_group_id: Union[Unset, list[int]] = UNSET,
    cluster_group_id_n: Union[Unset, list[int]] = UNSET,
    cluster_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cluster_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    config_template_id: Union[Unset, list[Union[None, int]]] = UNSET,
    config_template_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    console_port_count: Union[Unset, list[int]] = UNSET,
    console_port_count_empty: Union[Unset, bool] = UNSET,
    console_port_count_gt: Union[Unset, list[int]] = UNSET,
    console_port_count_gte: Union[Unset, list[int]] = UNSET,
    console_port_count_lt: Union[Unset, list[int]] = UNSET,
    console_port_count_lte: Union[Unset, list[int]] = UNSET,
    console_port_count_n: Union[Unset, list[int]] = UNSET,
    console_ports: Union[Unset, bool] = UNSET,
    console_server_port_count: Union[Unset, list[int]] = UNSET,
    console_server_port_count_empty: Union[Unset, bool] = UNSET,
    console_server_port_count_gt: Union[Unset, list[int]] = UNSET,
    console_server_port_count_gte: Union[Unset, list[int]] = UNSET,
    console_server_port_count_lt: Union[Unset, list[int]] = UNSET,
    console_server_port_count_lte: Union[Unset, list[int]] = UNSET,
    console_server_port_count_n: Union[Unset, list[int]] = UNSET,
    console_server_ports: Union[Unset, bool] = UNSET,
    contact: Union[Unset, list[int]] = UNSET,
    contact_n: Union[Unset, list[int]] = UNSET,
    contact_group: Union[Unset, list[str]] = UNSET,
    contact_group_n: Union[Unset, list[str]] = UNSET,
    contact_role: Union[Unset, list[int]] = UNSET,
    contact_role_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    description: Union[Unset, list[str]] = UNSET,
    description_empty: Union[Unset, bool] = UNSET,
    description_ic: Union[Unset, list[str]] = UNSET,
    description_ie: Union[Unset, list[str]] = UNSET,
    description_iew: Union[Unset, list[str]] = UNSET,
    description_isw: Union[Unset, list[str]] = UNSET,
    description_n: Union[Unset, list[str]] = UNSET,
    description_nic: Union[Unset, list[str]] = UNSET,
    description_nie: Union[Unset, list[str]] = UNSET,
    description_niew: Union[Unset, list[str]] = UNSET,
    description_nisw: Union[Unset, list[str]] = UNSET,
    device_bay_count: Union[Unset, list[int]] = UNSET,
    device_bay_count_empty: Union[Unset, bool] = UNSET,
    device_bay_count_gt: Union[Unset, list[int]] = UNSET,
    device_bay_count_gte: Union[Unset, list[int]] = UNSET,
    device_bay_count_lt: Union[Unset, list[int]] = UNSET,
    device_bay_count_lte: Union[Unset, list[int]] = UNSET,
    device_bay_count_n: Union[Unset, list[int]] = UNSET,
    device_bays: Union[Unset, bool] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    front_port_count: Union[Unset, list[int]] = UNSET,
    front_port_count_empty: Union[Unset, bool] = UNSET,
    front_port_count_gt: Union[Unset, list[int]] = UNSET,
    front_port_count_gte: Union[Unset, list[int]] = UNSET,
    front_port_count_lt: Union[Unset, list[int]] = UNSET,
    front_port_count_lte: Union[Unset, list[int]] = UNSET,
    front_port_count_n: Union[Unset, list[int]] = UNSET,
    has_oob_ip: Union[Unset, bool] = UNSET,
    has_primary_ip: Union[Unset, bool] = UNSET,
    has_virtual_device_context: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_count: Union[Unset, list[int]] = UNSET,
    interface_count_empty: Union[Unset, bool] = UNSET,
    interface_count_gt: Union[Unset, list[int]] = UNSET,
    interface_count_gte: Union[Unset, list[int]] = UNSET,
    interface_count_lt: Union[Unset, list[int]] = UNSET,
    interface_count_lte: Union[Unset, list[int]] = UNSET,
    interface_count_n: Union[Unset, list[int]] = UNSET,
    interfaces: Union[Unset, bool] = UNSET,
    inventory_item_count: Union[Unset, list[int]] = UNSET,
    inventory_item_count_empty: Union[Unset, bool] = UNSET,
    inventory_item_count_gt: Union[Unset, list[int]] = UNSET,
    inventory_item_count_gte: Union[Unset, list[int]] = UNSET,
    inventory_item_count_lt: Union[Unset, list[int]] = UNSET,
    inventory_item_count_lte: Union[Unset, list[int]] = UNSET,
    inventory_item_count_n: Union[Unset, list[int]] = UNSET,
    is_full_depth: Union[Unset, bool] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    latitude: Union[Unset, list[float]] = UNSET,
    latitude_empty: Union[Unset, bool] = UNSET,
    latitude_gt: Union[Unset, list[float]] = UNSET,
    latitude_gte: Union[Unset, list[float]] = UNSET,
    latitude_lt: Union[Unset, list[float]] = UNSET,
    latitude_lte: Union[Unset, list[float]] = UNSET,
    latitude_n: Union[Unset, list[float]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    local_context_data: Union[Unset, bool] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[str]] = UNSET,
    location_id_n: Union[Unset, list[str]] = UNSET,
    longitude: Union[Unset, list[float]] = UNSET,
    longitude_empty: Union[Unset, bool] = UNSET,
    longitude_gt: Union[Unset, list[float]] = UNSET,
    longitude_gte: Union[Unset, list[float]] = UNSET,
    longitude_lt: Union[Unset, list[float]] = UNSET,
    longitude_lte: Union[Unset, list[float]] = UNSET,
    longitude_n: Union[Unset, list[float]] = UNSET,
    mac_address: Union[Unset, list[str]] = UNSET,
    mac_address_ic: Union[Unset, list[str]] = UNSET,
    mac_address_ie: Union[Unset, list[str]] = UNSET,
    mac_address_iew: Union[Unset, list[str]] = UNSET,
    mac_address_isw: Union[Unset, list[str]] = UNSET,
    mac_address_n: Union[Unset, list[str]] = UNSET,
    mac_address_nic: Union[Unset, list[str]] = UNSET,
    mac_address_nie: Union[Unset, list[str]] = UNSET,
    mac_address_niew: Union[Unset, list[str]] = UNSET,
    mac_address_nisw: Union[Unset, list[str]] = UNSET,
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    model: Union[Unset, list[str]] = UNSET,
    model_n: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_bay_count: Union[Unset, list[int]] = UNSET,
    module_bay_count_empty: Union[Unset, bool] = UNSET,
    module_bay_count_gt: Union[Unset, list[int]] = UNSET,
    module_bay_count_gte: Union[Unset, list[int]] = UNSET,
    module_bay_count_lt: Union[Unset, list[int]] = UNSET,
    module_bay_count_lte: Union[Unset, list[int]] = UNSET,
    module_bay_count_n: Union[Unset, list[int]] = UNSET,
    module_bays: Union[Unset, bool] = UNSET,
    name: Union[Unset, list[str]] = UNSET,
    name_empty: Union[Unset, bool] = UNSET,
    name_ic: Union[Unset, list[str]] = UNSET,
    name_ie: Union[Unset, list[str]] = UNSET,
    name_iew: Union[Unset, list[str]] = UNSET,
    name_isw: Union[Unset, list[str]] = UNSET,
    name_n: Union[Unset, list[str]] = UNSET,
    name_nic: Union[Unset, list[str]] = UNSET,
    name_nie: Union[Unset, list[str]] = UNSET,
    name_niew: Union[Unset, list[str]] = UNSET,
    name_nisw: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    oob_ip_id: Union[Unset, list[int]] = UNSET,
    oob_ip_id_n: Union[Unset, list[int]] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_bay_id: Union[Unset, list[int]] = UNSET,
    parent_bay_id_n: Union[Unset, list[int]] = UNSET,
    parent_device_id: Union[Unset, list[int]] = UNSET,
    parent_device_id_n: Union[Unset, list[int]] = UNSET,
    pass_through_ports: Union[Unset, bool] = UNSET,
    platform: Union[Unset, list[str]] = UNSET,
    platform_n: Union[Unset, list[str]] = UNSET,
    platform_id: Union[Unset, list[Union[None, int]]] = UNSET,
    platform_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    position: Union[Unset, list[float]] = UNSET,
    position_empty: Union[Unset, bool] = UNSET,
    position_gt: Union[Unset, list[float]] = UNSET,
    position_gte: Union[Unset, list[float]] = UNSET,
    position_lt: Union[Unset, list[float]] = UNSET,
    position_lte: Union[Unset, list[float]] = UNSET,
    position_n: Union[Unset, list[float]] = UNSET,
    power_outlet_count: Union[Unset, list[int]] = UNSET,
    power_outlet_count_empty: Union[Unset, bool] = UNSET,
    power_outlet_count_gt: Union[Unset, list[int]] = UNSET,
    power_outlet_count_gte: Union[Unset, list[int]] = UNSET,
    power_outlet_count_lt: Union[Unset, list[int]] = UNSET,
    power_outlet_count_lte: Union[Unset, list[int]] = UNSET,
    power_outlet_count_n: Union[Unset, list[int]] = UNSET,
    power_outlets: Union[Unset, bool] = UNSET,
    power_port_count: Union[Unset, list[int]] = UNSET,
    power_port_count_empty: Union[Unset, bool] = UNSET,
    power_port_count_gt: Union[Unset, list[int]] = UNSET,
    power_port_count_gte: Union[Unset, list[int]] = UNSET,
    power_port_count_lt: Union[Unset, list[int]] = UNSET,
    power_port_count_lte: Union[Unset, list[int]] = UNSET,
    power_port_count_n: Union[Unset, list[int]] = UNSET,
    power_ports: Union[Unset, bool] = UNSET,
    primary_ip4: Union[Unset, list[str]] = UNSET,
    primary_ip4_n: Union[Unset, list[str]] = UNSET,
    primary_ip4_id: Union[Unset, list[int]] = UNSET,
    primary_ip4_id_n: Union[Unset, list[int]] = UNSET,
    primary_ip6: Union[Unset, list[str]] = UNSET,
    primary_ip6_n: Union[Unset, list[str]] = UNSET,
    primary_ip6_id: Union[Unset, list[int]] = UNSET,
    primary_ip6_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    rear_port_count: Union[Unset, list[int]] = UNSET,
    rear_port_count_empty: Union[Unset, bool] = UNSET,
    rear_port_count_gt: Union[Unset, list[int]] = UNSET,
    rear_port_count_gte: Union[Unset, list[int]] = UNSET,
    rear_port_count_lt: Union[Unset, list[int]] = UNSET,
    rear_port_count_lte: Union[Unset, list[int]] = UNSET,
    rear_port_count_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[str]] = UNSET,
    role_id_n: Union[Unset, list[str]] = UNSET,
    serial: Union[Unset, list[str]] = UNSET,
    serial_empty: Union[Unset, bool] = UNSET,
    serial_ic: Union[Unset, list[str]] = UNSET,
    serial_ie: Union[Unset, list[str]] = UNSET,
    serial_iew: Union[Unset, list[str]] = UNSET,
    serial_isw: Union[Unset, list[str]] = UNSET,
    serial_n: Union[Unset, list[str]] = UNSET,
    serial_nic: Union[Unset, list[str]] = UNSET,
    serial_nie: Union[Unset, list[str]] = UNSET,
    serial_niew: Union[Unset, list[str]] = UNSET,
    serial_nisw: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    status: Union[Unset, list[str]] = UNSET,
    status_empty: Union[Unset, bool] = UNSET,
    status_ic: Union[Unset, list[str]] = UNSET,
    status_ie: Union[Unset, list[str]] = UNSET,
    status_iew: Union[Unset, list[str]] = UNSET,
    status_isw: Union[Unset, list[str]] = UNSET,
    status_n: Union[Unset, list[str]] = UNSET,
    status_nic: Union[Unset, list[str]] = UNSET,
    status_nie: Union[Unset, list[str]] = UNSET,
    status_niew: Union[Unset, list[str]] = UNSET,
    status_nisw: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tenant: Union[Unset, list[str]] = UNSET,
    tenant_n: Union[Unset, list[str]] = UNSET,
    tenant_group: Union[Unset, list[str]] = UNSET,
    tenant_group_n: Union[Unset, list[str]] = UNSET,
    tenant_group_id: Union[Unset, list[str]] = UNSET,
    tenant_group_id_n: Union[Unset, list[str]] = UNSET,
    tenant_id: Union[Unset, list[Union[None, int]]] = UNSET,
    tenant_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    vc_position: Union[Unset, list[int]] = UNSET,
    vc_position_empty: Union[Unset, bool] = UNSET,
    vc_position_gt: Union[Unset, list[int]] = UNSET,
    vc_position_gte: Union[Unset, list[int]] = UNSET,
    vc_position_lt: Union[Unset, list[int]] = UNSET,
    vc_position_lte: Union[Unset, list[int]] = UNSET,
    vc_position_n: Union[Unset, list[int]] = UNSET,
    vc_priority: Union[Unset, list[int]] = UNSET,
    vc_priority_empty: Union[Unset, bool] = UNSET,
    vc_priority_gt: Union[Unset, list[int]] = UNSET,
    vc_priority_gte: Union[Unset, list[int]] = UNSET,
    vc_priority_lt: Union[Unset, list[int]] = UNSET,
    vc_priority_lte: Union[Unset, list[int]] = UNSET,
    vc_priority_n: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id_n: Union[Unset, list[int]] = UNSET,
    virtual_chassis_member: Union[Unset, bool] = UNSET,
) -> Response[PaginatedDeviceWithConfigContextList]:
    """Get a list of device objects.

    Args:
        airflow (Union[Unset, DcimDevicesListAirflow]):
        asset_tag (Union[Unset, list[str]]):
        asset_tag_empty (Union[Unset, bool]):
        asset_tag_ic (Union[Unset, list[str]]):
        asset_tag_ie (Union[Unset, list[str]]):
        asset_tag_iew (Union[Unset, list[str]]):
        asset_tag_isw (Union[Unset, list[str]]):
        asset_tag_n (Union[Unset, list[str]]):
        asset_tag_nic (Union[Unset, list[str]]):
        asset_tag_nie (Union[Unset, list[str]]):
        asset_tag_niew (Union[Unset, list[str]]):
        asset_tag_nisw (Union[Unset, list[str]]):
        cluster_group (Union[Unset, list[str]]):
        cluster_group_n (Union[Unset, list[str]]):
        cluster_group_id (Union[Unset, list[int]]):
        cluster_group_id_n (Union[Unset, list[int]]):
        cluster_id (Union[Unset, list[Union[None, int]]]):
        cluster_id_n (Union[Unset, list[Union[None, int]]]):
        config_template_id (Union[Unset, list[Union[None, int]]]):
        config_template_id_n (Union[Unset, list[Union[None, int]]]):
        console_port_count (Union[Unset, list[int]]):
        console_port_count_empty (Union[Unset, bool]):
        console_port_count_gt (Union[Unset, list[int]]):
        console_port_count_gte (Union[Unset, list[int]]):
        console_port_count_lt (Union[Unset, list[int]]):
        console_port_count_lte (Union[Unset, list[int]]):
        console_port_count_n (Union[Unset, list[int]]):
        console_ports (Union[Unset, bool]):
        console_server_port_count (Union[Unset, list[int]]):
        console_server_port_count_empty (Union[Unset, bool]):
        console_server_port_count_gt (Union[Unset, list[int]]):
        console_server_port_count_gte (Union[Unset, list[int]]):
        console_server_port_count_lt (Union[Unset, list[int]]):
        console_server_port_count_lte (Union[Unset, list[int]]):
        console_server_port_count_n (Union[Unset, list[int]]):
        console_server_ports (Union[Unset, bool]):
        contact (Union[Unset, list[int]]):
        contact_n (Union[Unset, list[int]]):
        contact_group (Union[Unset, list[str]]):
        contact_group_n (Union[Unset, list[str]]):
        contact_role (Union[Unset, list[int]]):
        contact_role_n (Union[Unset, list[int]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        description (Union[Unset, list[str]]):
        description_empty (Union[Unset, bool]):
        description_ic (Union[Unset, list[str]]):
        description_ie (Union[Unset, list[str]]):
        description_iew (Union[Unset, list[str]]):
        description_isw (Union[Unset, list[str]]):
        description_n (Union[Unset, list[str]]):
        description_nic (Union[Unset, list[str]]):
        description_nie (Union[Unset, list[str]]):
        description_niew (Union[Unset, list[str]]):
        description_nisw (Union[Unset, list[str]]):
        device_bay_count (Union[Unset, list[int]]):
        device_bay_count_empty (Union[Unset, bool]):
        device_bay_count_gt (Union[Unset, list[int]]):
        device_bay_count_gte (Union[Unset, list[int]]):
        device_bay_count_lt (Union[Unset, list[int]]):
        device_bay_count_lte (Union[Unset, list[int]]):
        device_bay_count_n (Union[Unset, list[int]]):
        device_bays (Union[Unset, bool]):
        device_type (Union[Unset, list[str]]):
        device_type_n (Union[Unset, list[str]]):
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
        front_port_count (Union[Unset, list[int]]):
        front_port_count_empty (Union[Unset, bool]):
        front_port_count_gt (Union[Unset, list[int]]):
        front_port_count_gte (Union[Unset, list[int]]):
        front_port_count_lt (Union[Unset, list[int]]):
        front_port_count_lte (Union[Unset, list[int]]):
        front_port_count_n (Union[Unset, list[int]]):
        has_oob_ip (Union[Unset, bool]):
        has_primary_ip (Union[Unset, bool]):
        has_virtual_device_context (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_count (Union[Unset, list[int]]):
        interface_count_empty (Union[Unset, bool]):
        interface_count_gt (Union[Unset, list[int]]):
        interface_count_gte (Union[Unset, list[int]]):
        interface_count_lt (Union[Unset, list[int]]):
        interface_count_lte (Union[Unset, list[int]]):
        interface_count_n (Union[Unset, list[int]]):
        interfaces (Union[Unset, bool]):
        inventory_item_count (Union[Unset, list[int]]):
        inventory_item_count_empty (Union[Unset, bool]):
        inventory_item_count_gt (Union[Unset, list[int]]):
        inventory_item_count_gte (Union[Unset, list[int]]):
        inventory_item_count_lt (Union[Unset, list[int]]):
        inventory_item_count_lte (Union[Unset, list[int]]):
        inventory_item_count_n (Union[Unset, list[int]]):
        is_full_depth (Union[Unset, bool]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        latitude (Union[Unset, list[float]]):
        latitude_empty (Union[Unset, bool]):
        latitude_gt (Union[Unset, list[float]]):
        latitude_gte (Union[Unset, list[float]]):
        latitude_lt (Union[Unset, list[float]]):
        latitude_lte (Union[Unset, list[float]]):
        latitude_n (Union[Unset, list[float]]):
        limit (Union[Unset, int]):
        local_context_data (Union[Unset, bool]):
        location (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_id (Union[Unset, list[str]]):
        location_id_n (Union[Unset, list[str]]):
        longitude (Union[Unset, list[float]]):
        longitude_empty (Union[Unset, bool]):
        longitude_gt (Union[Unset, list[float]]):
        longitude_gte (Union[Unset, list[float]]):
        longitude_lt (Union[Unset, list[float]]):
        longitude_lte (Union[Unset, list[float]]):
        longitude_n (Union[Unset, list[float]]):
        mac_address (Union[Unset, list[str]]):
        mac_address_ic (Union[Unset, list[str]]):
        mac_address_ie (Union[Unset, list[str]]):
        mac_address_iew (Union[Unset, list[str]]):
        mac_address_isw (Union[Unset, list[str]]):
        mac_address_n (Union[Unset, list[str]]):
        mac_address_nic (Union[Unset, list[str]]):
        mac_address_nie (Union[Unset, list[str]]):
        mac_address_niew (Union[Unset, list[str]]):
        mac_address_nisw (Union[Unset, list[str]]):
        manufacturer (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_id (Union[Unset, list[int]]):
        manufacturer_id_n (Union[Unset, list[int]]):
        model (Union[Unset, list[str]]):
        model_n (Union[Unset, list[str]]):
        modified_by_request (Union[Unset, UUID]):
        module_bay_count (Union[Unset, list[int]]):
        module_bay_count_empty (Union[Unset, bool]):
        module_bay_count_gt (Union[Unset, list[int]]):
        module_bay_count_gte (Union[Unset, list[int]]):
        module_bay_count_lt (Union[Unset, list[int]]):
        module_bay_count_lte (Union[Unset, list[int]]):
        module_bay_count_n (Union[Unset, list[int]]):
        module_bays (Union[Unset, bool]):
        name (Union[Unset, list[str]]):
        name_empty (Union[Unset, bool]):
        name_ic (Union[Unset, list[str]]):
        name_ie (Union[Unset, list[str]]):
        name_iew (Union[Unset, list[str]]):
        name_isw (Union[Unset, list[str]]):
        name_n (Union[Unset, list[str]]):
        name_nic (Union[Unset, list[str]]):
        name_nie (Union[Unset, list[str]]):
        name_niew (Union[Unset, list[str]]):
        name_nisw (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        oob_ip_id (Union[Unset, list[int]]):
        oob_ip_id_n (Union[Unset, list[int]]):
        ordering (Union[Unset, str]):
        parent_bay_id (Union[Unset, list[int]]):
        parent_bay_id_n (Union[Unset, list[int]]):
        parent_device_id (Union[Unset, list[int]]):
        parent_device_id_n (Union[Unset, list[int]]):
        pass_through_ports (Union[Unset, bool]):
        platform (Union[Unset, list[str]]):
        platform_n (Union[Unset, list[str]]):
        platform_id (Union[Unset, list[Union[None, int]]]):
        platform_id_n (Union[Unset, list[Union[None, int]]]):
        position (Union[Unset, list[float]]):
        position_empty (Union[Unset, bool]):
        position_gt (Union[Unset, list[float]]):
        position_gte (Union[Unset, list[float]]):
        position_lt (Union[Unset, list[float]]):
        position_lte (Union[Unset, list[float]]):
        position_n (Union[Unset, list[float]]):
        power_outlet_count (Union[Unset, list[int]]):
        power_outlet_count_empty (Union[Unset, bool]):
        power_outlet_count_gt (Union[Unset, list[int]]):
        power_outlet_count_gte (Union[Unset, list[int]]):
        power_outlet_count_lt (Union[Unset, list[int]]):
        power_outlet_count_lte (Union[Unset, list[int]]):
        power_outlet_count_n (Union[Unset, list[int]]):
        power_outlets (Union[Unset, bool]):
        power_port_count (Union[Unset, list[int]]):
        power_port_count_empty (Union[Unset, bool]):
        power_port_count_gt (Union[Unset, list[int]]):
        power_port_count_gte (Union[Unset, list[int]]):
        power_port_count_lt (Union[Unset, list[int]]):
        power_port_count_lte (Union[Unset, list[int]]):
        power_port_count_n (Union[Unset, list[int]]):
        power_ports (Union[Unset, bool]):
        primary_ip4 (Union[Unset, list[str]]):
        primary_ip4_n (Union[Unset, list[str]]):
        primary_ip4_id (Union[Unset, list[int]]):
        primary_ip4_id_n (Union[Unset, list[int]]):
        primary_ip6 (Union[Unset, list[str]]):
        primary_ip6_n (Union[Unset, list[str]]):
        primary_ip6_id (Union[Unset, list[int]]):
        primary_ip6_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        rack_id (Union[Unset, list[int]]):
        rack_id_n (Union[Unset, list[int]]):
        rear_port_count (Union[Unset, list[int]]):
        rear_port_count_empty (Union[Unset, bool]):
        rear_port_count_gt (Union[Unset, list[int]]):
        rear_port_count_gte (Union[Unset, list[int]]):
        rear_port_count_lt (Union[Unset, list[int]]):
        rear_port_count_lte (Union[Unset, list[int]]):
        rear_port_count_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[str]]):
        role_id_n (Union[Unset, list[str]]):
        serial (Union[Unset, list[str]]):
        serial_empty (Union[Unset, bool]):
        serial_ic (Union[Unset, list[str]]):
        serial_ie (Union[Unset, list[str]]):
        serial_iew (Union[Unset, list[str]]):
        serial_isw (Union[Unset, list[str]]):
        serial_n (Union[Unset, list[str]]):
        serial_nic (Union[Unset, list[str]]):
        serial_nie (Union[Unset, list[str]]):
        serial_niew (Union[Unset, list[str]]):
        serial_nisw (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
        status (Union[Unset, list[str]]):
        status_empty (Union[Unset, bool]):
        status_ic (Union[Unset, list[str]]):
        status_ie (Union[Unset, list[str]]):
        status_iew (Union[Unset, list[str]]):
        status_isw (Union[Unset, list[str]]):
        status_n (Union[Unset, list[str]]):
        status_nic (Union[Unset, list[str]]):
        status_nie (Union[Unset, list[str]]):
        status_niew (Union[Unset, list[str]]):
        status_nisw (Union[Unset, list[str]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        tenant (Union[Unset, list[str]]):
        tenant_n (Union[Unset, list[str]]):
        tenant_group (Union[Unset, list[str]]):
        tenant_group_n (Union[Unset, list[str]]):
        tenant_group_id (Union[Unset, list[str]]):
        tenant_group_id_n (Union[Unset, list[str]]):
        tenant_id (Union[Unset, list[Union[None, int]]]):
        tenant_id_n (Union[Unset, list[Union[None, int]]]):
        updated_by_request (Union[Unset, UUID]):
        vc_position (Union[Unset, list[int]]):
        vc_position_empty (Union[Unset, bool]):
        vc_position_gt (Union[Unset, list[int]]):
        vc_position_gte (Union[Unset, list[int]]):
        vc_position_lt (Union[Unset, list[int]]):
        vc_position_lte (Union[Unset, list[int]]):
        vc_position_n (Union[Unset, list[int]]):
        vc_priority (Union[Unset, list[int]]):
        vc_priority_empty (Union[Unset, bool]):
        vc_priority_gt (Union[Unset, list[int]]):
        vc_priority_gte (Union[Unset, list[int]]):
        vc_priority_lt (Union[Unset, list[int]]):
        vc_priority_lte (Union[Unset, list[int]]):
        vc_priority_n (Union[Unset, list[int]]):
        virtual_chassis_id (Union[Unset, list[int]]):
        virtual_chassis_id_n (Union[Unset, list[int]]):
        virtual_chassis_member (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDeviceWithConfigContextList]
    """

    kwargs = _get_kwargs(
        airflow=airflow,
        asset_tag=asset_tag,
        asset_tag_empty=asset_tag_empty,
        asset_tag_ic=asset_tag_ic,
        asset_tag_ie=asset_tag_ie,
        asset_tag_iew=asset_tag_iew,
        asset_tag_isw=asset_tag_isw,
        asset_tag_n=asset_tag_n,
        asset_tag_nic=asset_tag_nic,
        asset_tag_nie=asset_tag_nie,
        asset_tag_niew=asset_tag_niew,
        asset_tag_nisw=asset_tag_nisw,
        cluster_group=cluster_group,
        cluster_group_n=cluster_group_n,
        cluster_group_id=cluster_group_id,
        cluster_group_id_n=cluster_group_id_n,
        cluster_id=cluster_id,
        cluster_id_n=cluster_id_n,
        config_template_id=config_template_id,
        config_template_id_n=config_template_id_n,
        console_port_count=console_port_count,
        console_port_count_empty=console_port_count_empty,
        console_port_count_gt=console_port_count_gt,
        console_port_count_gte=console_port_count_gte,
        console_port_count_lt=console_port_count_lt,
        console_port_count_lte=console_port_count_lte,
        console_port_count_n=console_port_count_n,
        console_ports=console_ports,
        console_server_port_count=console_server_port_count,
        console_server_port_count_empty=console_server_port_count_empty,
        console_server_port_count_gt=console_server_port_count_gt,
        console_server_port_count_gte=console_server_port_count_gte,
        console_server_port_count_lt=console_server_port_count_lt,
        console_server_port_count_lte=console_server_port_count_lte,
        console_server_port_count_n=console_server_port_count_n,
        console_server_ports=console_server_ports,
        contact=contact,
        contact_n=contact_n,
        contact_group=contact_group,
        contact_group_n=contact_group_n,
        contact_role=contact_role,
        contact_role_n=contact_role_n,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        description=description,
        description_empty=description_empty,
        description_ic=description_ic,
        description_ie=description_ie,
        description_iew=description_iew,
        description_isw=description_isw,
        description_n=description_n,
        description_nic=description_nic,
        description_nie=description_nie,
        description_niew=description_niew,
        description_nisw=description_nisw,
        device_bay_count=device_bay_count,
        device_bay_count_empty=device_bay_count_empty,
        device_bay_count_gt=device_bay_count_gt,
        device_bay_count_gte=device_bay_count_gte,
        device_bay_count_lt=device_bay_count_lt,
        device_bay_count_lte=device_bay_count_lte,
        device_bay_count_n=device_bay_count_n,
        device_bays=device_bays,
        device_type=device_type,
        device_type_n=device_type_n,
        device_type_id=device_type_id,
        device_type_id_n=device_type_id_n,
        front_port_count=front_port_count,
        front_port_count_empty=front_port_count_empty,
        front_port_count_gt=front_port_count_gt,
        front_port_count_gte=front_port_count_gte,
        front_port_count_lt=front_port_count_lt,
        front_port_count_lte=front_port_count_lte,
        front_port_count_n=front_port_count_n,
        has_oob_ip=has_oob_ip,
        has_primary_ip=has_primary_ip,
        has_virtual_device_context=has_virtual_device_context,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface_count=interface_count,
        interface_count_empty=interface_count_empty,
        interface_count_gt=interface_count_gt,
        interface_count_gte=interface_count_gte,
        interface_count_lt=interface_count_lt,
        interface_count_lte=interface_count_lte,
        interface_count_n=interface_count_n,
        interfaces=interfaces,
        inventory_item_count=inventory_item_count,
        inventory_item_count_empty=inventory_item_count_empty,
        inventory_item_count_gt=inventory_item_count_gt,
        inventory_item_count_gte=inventory_item_count_gte,
        inventory_item_count_lt=inventory_item_count_lt,
        inventory_item_count_lte=inventory_item_count_lte,
        inventory_item_count_n=inventory_item_count_n,
        is_full_depth=is_full_depth,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        latitude=latitude,
        latitude_empty=latitude_empty,
        latitude_gt=latitude_gt,
        latitude_gte=latitude_gte,
        latitude_lt=latitude_lt,
        latitude_lte=latitude_lte,
        latitude_n=latitude_n,
        limit=limit,
        local_context_data=local_context_data,
        location=location,
        location_n=location_n,
        location_id=location_id,
        location_id_n=location_id_n,
        longitude=longitude,
        longitude_empty=longitude_empty,
        longitude_gt=longitude_gt,
        longitude_gte=longitude_gte,
        longitude_lt=longitude_lt,
        longitude_lte=longitude_lte,
        longitude_n=longitude_n,
        mac_address=mac_address,
        mac_address_ic=mac_address_ic,
        mac_address_ie=mac_address_ie,
        mac_address_iew=mac_address_iew,
        mac_address_isw=mac_address_isw,
        mac_address_n=mac_address_n,
        mac_address_nic=mac_address_nic,
        mac_address_nie=mac_address_nie,
        mac_address_niew=mac_address_niew,
        mac_address_nisw=mac_address_nisw,
        manufacturer=manufacturer,
        manufacturer_n=manufacturer_n,
        manufacturer_id=manufacturer_id,
        manufacturer_id_n=manufacturer_id_n,
        model=model,
        model_n=model_n,
        modified_by_request=modified_by_request,
        module_bay_count=module_bay_count,
        module_bay_count_empty=module_bay_count_empty,
        module_bay_count_gt=module_bay_count_gt,
        module_bay_count_gte=module_bay_count_gte,
        module_bay_count_lt=module_bay_count_lt,
        module_bay_count_lte=module_bay_count_lte,
        module_bay_count_n=module_bay_count_n,
        module_bays=module_bays,
        name=name,
        name_empty=name_empty,
        name_ic=name_ic,
        name_ie=name_ie,
        name_iew=name_iew,
        name_isw=name_isw,
        name_n=name_n,
        name_nic=name_nic,
        name_nie=name_nie,
        name_niew=name_niew,
        name_nisw=name_nisw,
        offset=offset,
        oob_ip_id=oob_ip_id,
        oob_ip_id_n=oob_ip_id_n,
        ordering=ordering,
        parent_bay_id=parent_bay_id,
        parent_bay_id_n=parent_bay_id_n,
        parent_device_id=parent_device_id,
        parent_device_id_n=parent_device_id_n,
        pass_through_ports=pass_through_ports,
        platform=platform,
        platform_n=platform_n,
        platform_id=platform_id,
        platform_id_n=platform_id_n,
        position=position,
        position_empty=position_empty,
        position_gt=position_gt,
        position_gte=position_gte,
        position_lt=position_lt,
        position_lte=position_lte,
        position_n=position_n,
        power_outlet_count=power_outlet_count,
        power_outlet_count_empty=power_outlet_count_empty,
        power_outlet_count_gt=power_outlet_count_gt,
        power_outlet_count_gte=power_outlet_count_gte,
        power_outlet_count_lt=power_outlet_count_lt,
        power_outlet_count_lte=power_outlet_count_lte,
        power_outlet_count_n=power_outlet_count_n,
        power_outlets=power_outlets,
        power_port_count=power_port_count,
        power_port_count_empty=power_port_count_empty,
        power_port_count_gt=power_port_count_gt,
        power_port_count_gte=power_port_count_gte,
        power_port_count_lt=power_port_count_lt,
        power_port_count_lte=power_port_count_lte,
        power_port_count_n=power_port_count_n,
        power_ports=power_ports,
        primary_ip4=primary_ip4,
        primary_ip4_n=primary_ip4_n,
        primary_ip4_id=primary_ip4_id,
        primary_ip4_id_n=primary_ip4_id_n,
        primary_ip6=primary_ip6,
        primary_ip6_n=primary_ip6_n,
        primary_ip6_id=primary_ip6_id,
        primary_ip6_id_n=primary_ip6_id_n,
        q=q,
        rack_id=rack_id,
        rack_id_n=rack_id_n,
        rear_port_count=rear_port_count,
        rear_port_count_empty=rear_port_count_empty,
        rear_port_count_gt=rear_port_count_gt,
        rear_port_count_gte=rear_port_count_gte,
        rear_port_count_lt=rear_port_count_lt,
        rear_port_count_lte=rear_port_count_lte,
        rear_port_count_n=rear_port_count_n,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
        serial=serial,
        serial_empty=serial_empty,
        serial_ic=serial_ic,
        serial_ie=serial_ie,
        serial_iew=serial_iew,
        serial_isw=serial_isw,
        serial_n=serial_n,
        serial_nic=serial_nic,
        serial_nie=serial_nie,
        serial_niew=serial_niew,
        serial_nisw=serial_nisw,
        site=site,
        site_n=site_n,
        site_group=site_group,
        site_group_n=site_group_n,
        site_group_id=site_group_id,
        site_group_id_n=site_group_id_n,
        site_id=site_id,
        site_id_n=site_id_n,
        status=status,
        status_empty=status_empty,
        status_ic=status_ic,
        status_ie=status_ie,
        status_iew=status_iew,
        status_isw=status_isw,
        status_n=status_n,
        status_nic=status_nic,
        status_nie=status_nie,
        status_niew=status_niew,
        status_nisw=status_nisw,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        tenant=tenant,
        tenant_n=tenant_n,
        tenant_group=tenant_group,
        tenant_group_n=tenant_group_n,
        tenant_group_id=tenant_group_id,
        tenant_group_id_n=tenant_group_id_n,
        tenant_id=tenant_id,
        tenant_id_n=tenant_id_n,
        updated_by_request=updated_by_request,
        vc_position=vc_position,
        vc_position_empty=vc_position_empty,
        vc_position_gt=vc_position_gt,
        vc_position_gte=vc_position_gte,
        vc_position_lt=vc_position_lt,
        vc_position_lte=vc_position_lte,
        vc_position_n=vc_position_n,
        vc_priority=vc_priority,
        vc_priority_empty=vc_priority_empty,
        vc_priority_gt=vc_priority_gt,
        vc_priority_gte=vc_priority_gte,
        vc_priority_lt=vc_priority_lt,
        vc_priority_lte=vc_priority_lte,
        vc_priority_n=vc_priority_n,
        virtual_chassis_id=virtual_chassis_id,
        virtual_chassis_id_n=virtual_chassis_id_n,
        virtual_chassis_member=virtual_chassis_member,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    airflow: Union[Unset, DcimDevicesListAirflow] = UNSET,
    asset_tag: Union[Unset, list[str]] = UNSET,
    asset_tag_empty: Union[Unset, bool] = UNSET,
    asset_tag_ic: Union[Unset, list[str]] = UNSET,
    asset_tag_ie: Union[Unset, list[str]] = UNSET,
    asset_tag_iew: Union[Unset, list[str]] = UNSET,
    asset_tag_isw: Union[Unset, list[str]] = UNSET,
    asset_tag_n: Union[Unset, list[str]] = UNSET,
    asset_tag_nic: Union[Unset, list[str]] = UNSET,
    asset_tag_nie: Union[Unset, list[str]] = UNSET,
    asset_tag_niew: Union[Unset, list[str]] = UNSET,
    asset_tag_nisw: Union[Unset, list[str]] = UNSET,
    cluster_group: Union[Unset, list[str]] = UNSET,
    cluster_group_n: Union[Unset, list[str]] = UNSET,
    cluster_group_id: Union[Unset, list[int]] = UNSET,
    cluster_group_id_n: Union[Unset, list[int]] = UNSET,
    cluster_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cluster_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    config_template_id: Union[Unset, list[Union[None, int]]] = UNSET,
    config_template_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    console_port_count: Union[Unset, list[int]] = UNSET,
    console_port_count_empty: Union[Unset, bool] = UNSET,
    console_port_count_gt: Union[Unset, list[int]] = UNSET,
    console_port_count_gte: Union[Unset, list[int]] = UNSET,
    console_port_count_lt: Union[Unset, list[int]] = UNSET,
    console_port_count_lte: Union[Unset, list[int]] = UNSET,
    console_port_count_n: Union[Unset, list[int]] = UNSET,
    console_ports: Union[Unset, bool] = UNSET,
    console_server_port_count: Union[Unset, list[int]] = UNSET,
    console_server_port_count_empty: Union[Unset, bool] = UNSET,
    console_server_port_count_gt: Union[Unset, list[int]] = UNSET,
    console_server_port_count_gte: Union[Unset, list[int]] = UNSET,
    console_server_port_count_lt: Union[Unset, list[int]] = UNSET,
    console_server_port_count_lte: Union[Unset, list[int]] = UNSET,
    console_server_port_count_n: Union[Unset, list[int]] = UNSET,
    console_server_ports: Union[Unset, bool] = UNSET,
    contact: Union[Unset, list[int]] = UNSET,
    contact_n: Union[Unset, list[int]] = UNSET,
    contact_group: Union[Unset, list[str]] = UNSET,
    contact_group_n: Union[Unset, list[str]] = UNSET,
    contact_role: Union[Unset, list[int]] = UNSET,
    contact_role_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    description: Union[Unset, list[str]] = UNSET,
    description_empty: Union[Unset, bool] = UNSET,
    description_ic: Union[Unset, list[str]] = UNSET,
    description_ie: Union[Unset, list[str]] = UNSET,
    description_iew: Union[Unset, list[str]] = UNSET,
    description_isw: Union[Unset, list[str]] = UNSET,
    description_n: Union[Unset, list[str]] = UNSET,
    description_nic: Union[Unset, list[str]] = UNSET,
    description_nie: Union[Unset, list[str]] = UNSET,
    description_niew: Union[Unset, list[str]] = UNSET,
    description_nisw: Union[Unset, list[str]] = UNSET,
    device_bay_count: Union[Unset, list[int]] = UNSET,
    device_bay_count_empty: Union[Unset, bool] = UNSET,
    device_bay_count_gt: Union[Unset, list[int]] = UNSET,
    device_bay_count_gte: Union[Unset, list[int]] = UNSET,
    device_bay_count_lt: Union[Unset, list[int]] = UNSET,
    device_bay_count_lte: Union[Unset, list[int]] = UNSET,
    device_bay_count_n: Union[Unset, list[int]] = UNSET,
    device_bays: Union[Unset, bool] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    front_port_count: Union[Unset, list[int]] = UNSET,
    front_port_count_empty: Union[Unset, bool] = UNSET,
    front_port_count_gt: Union[Unset, list[int]] = UNSET,
    front_port_count_gte: Union[Unset, list[int]] = UNSET,
    front_port_count_lt: Union[Unset, list[int]] = UNSET,
    front_port_count_lte: Union[Unset, list[int]] = UNSET,
    front_port_count_n: Union[Unset, list[int]] = UNSET,
    has_oob_ip: Union[Unset, bool] = UNSET,
    has_primary_ip: Union[Unset, bool] = UNSET,
    has_virtual_device_context: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_count: Union[Unset, list[int]] = UNSET,
    interface_count_empty: Union[Unset, bool] = UNSET,
    interface_count_gt: Union[Unset, list[int]] = UNSET,
    interface_count_gte: Union[Unset, list[int]] = UNSET,
    interface_count_lt: Union[Unset, list[int]] = UNSET,
    interface_count_lte: Union[Unset, list[int]] = UNSET,
    interface_count_n: Union[Unset, list[int]] = UNSET,
    interfaces: Union[Unset, bool] = UNSET,
    inventory_item_count: Union[Unset, list[int]] = UNSET,
    inventory_item_count_empty: Union[Unset, bool] = UNSET,
    inventory_item_count_gt: Union[Unset, list[int]] = UNSET,
    inventory_item_count_gte: Union[Unset, list[int]] = UNSET,
    inventory_item_count_lt: Union[Unset, list[int]] = UNSET,
    inventory_item_count_lte: Union[Unset, list[int]] = UNSET,
    inventory_item_count_n: Union[Unset, list[int]] = UNSET,
    is_full_depth: Union[Unset, bool] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    latitude: Union[Unset, list[float]] = UNSET,
    latitude_empty: Union[Unset, bool] = UNSET,
    latitude_gt: Union[Unset, list[float]] = UNSET,
    latitude_gte: Union[Unset, list[float]] = UNSET,
    latitude_lt: Union[Unset, list[float]] = UNSET,
    latitude_lte: Union[Unset, list[float]] = UNSET,
    latitude_n: Union[Unset, list[float]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    local_context_data: Union[Unset, bool] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[str]] = UNSET,
    location_id_n: Union[Unset, list[str]] = UNSET,
    longitude: Union[Unset, list[float]] = UNSET,
    longitude_empty: Union[Unset, bool] = UNSET,
    longitude_gt: Union[Unset, list[float]] = UNSET,
    longitude_gte: Union[Unset, list[float]] = UNSET,
    longitude_lt: Union[Unset, list[float]] = UNSET,
    longitude_lte: Union[Unset, list[float]] = UNSET,
    longitude_n: Union[Unset, list[float]] = UNSET,
    mac_address: Union[Unset, list[str]] = UNSET,
    mac_address_ic: Union[Unset, list[str]] = UNSET,
    mac_address_ie: Union[Unset, list[str]] = UNSET,
    mac_address_iew: Union[Unset, list[str]] = UNSET,
    mac_address_isw: Union[Unset, list[str]] = UNSET,
    mac_address_n: Union[Unset, list[str]] = UNSET,
    mac_address_nic: Union[Unset, list[str]] = UNSET,
    mac_address_nie: Union[Unset, list[str]] = UNSET,
    mac_address_niew: Union[Unset, list[str]] = UNSET,
    mac_address_nisw: Union[Unset, list[str]] = UNSET,
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    model: Union[Unset, list[str]] = UNSET,
    model_n: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_bay_count: Union[Unset, list[int]] = UNSET,
    module_bay_count_empty: Union[Unset, bool] = UNSET,
    module_bay_count_gt: Union[Unset, list[int]] = UNSET,
    module_bay_count_gte: Union[Unset, list[int]] = UNSET,
    module_bay_count_lt: Union[Unset, list[int]] = UNSET,
    module_bay_count_lte: Union[Unset, list[int]] = UNSET,
    module_bay_count_n: Union[Unset, list[int]] = UNSET,
    module_bays: Union[Unset, bool] = UNSET,
    name: Union[Unset, list[str]] = UNSET,
    name_empty: Union[Unset, bool] = UNSET,
    name_ic: Union[Unset, list[str]] = UNSET,
    name_ie: Union[Unset, list[str]] = UNSET,
    name_iew: Union[Unset, list[str]] = UNSET,
    name_isw: Union[Unset, list[str]] = UNSET,
    name_n: Union[Unset, list[str]] = UNSET,
    name_nic: Union[Unset, list[str]] = UNSET,
    name_nie: Union[Unset, list[str]] = UNSET,
    name_niew: Union[Unset, list[str]] = UNSET,
    name_nisw: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    oob_ip_id: Union[Unset, list[int]] = UNSET,
    oob_ip_id_n: Union[Unset, list[int]] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_bay_id: Union[Unset, list[int]] = UNSET,
    parent_bay_id_n: Union[Unset, list[int]] = UNSET,
    parent_device_id: Union[Unset, list[int]] = UNSET,
    parent_device_id_n: Union[Unset, list[int]] = UNSET,
    pass_through_ports: Union[Unset, bool] = UNSET,
    platform: Union[Unset, list[str]] = UNSET,
    platform_n: Union[Unset, list[str]] = UNSET,
    platform_id: Union[Unset, list[Union[None, int]]] = UNSET,
    platform_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    position: Union[Unset, list[float]] = UNSET,
    position_empty: Union[Unset, bool] = UNSET,
    position_gt: Union[Unset, list[float]] = UNSET,
    position_gte: Union[Unset, list[float]] = UNSET,
    position_lt: Union[Unset, list[float]] = UNSET,
    position_lte: Union[Unset, list[float]] = UNSET,
    position_n: Union[Unset, list[float]] = UNSET,
    power_outlet_count: Union[Unset, list[int]] = UNSET,
    power_outlet_count_empty: Union[Unset, bool] = UNSET,
    power_outlet_count_gt: Union[Unset, list[int]] = UNSET,
    power_outlet_count_gte: Union[Unset, list[int]] = UNSET,
    power_outlet_count_lt: Union[Unset, list[int]] = UNSET,
    power_outlet_count_lte: Union[Unset, list[int]] = UNSET,
    power_outlet_count_n: Union[Unset, list[int]] = UNSET,
    power_outlets: Union[Unset, bool] = UNSET,
    power_port_count: Union[Unset, list[int]] = UNSET,
    power_port_count_empty: Union[Unset, bool] = UNSET,
    power_port_count_gt: Union[Unset, list[int]] = UNSET,
    power_port_count_gte: Union[Unset, list[int]] = UNSET,
    power_port_count_lt: Union[Unset, list[int]] = UNSET,
    power_port_count_lte: Union[Unset, list[int]] = UNSET,
    power_port_count_n: Union[Unset, list[int]] = UNSET,
    power_ports: Union[Unset, bool] = UNSET,
    primary_ip4: Union[Unset, list[str]] = UNSET,
    primary_ip4_n: Union[Unset, list[str]] = UNSET,
    primary_ip4_id: Union[Unset, list[int]] = UNSET,
    primary_ip4_id_n: Union[Unset, list[int]] = UNSET,
    primary_ip6: Union[Unset, list[str]] = UNSET,
    primary_ip6_n: Union[Unset, list[str]] = UNSET,
    primary_ip6_id: Union[Unset, list[int]] = UNSET,
    primary_ip6_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    rear_port_count: Union[Unset, list[int]] = UNSET,
    rear_port_count_empty: Union[Unset, bool] = UNSET,
    rear_port_count_gt: Union[Unset, list[int]] = UNSET,
    rear_port_count_gte: Union[Unset, list[int]] = UNSET,
    rear_port_count_lt: Union[Unset, list[int]] = UNSET,
    rear_port_count_lte: Union[Unset, list[int]] = UNSET,
    rear_port_count_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[str]] = UNSET,
    role_id_n: Union[Unset, list[str]] = UNSET,
    serial: Union[Unset, list[str]] = UNSET,
    serial_empty: Union[Unset, bool] = UNSET,
    serial_ic: Union[Unset, list[str]] = UNSET,
    serial_ie: Union[Unset, list[str]] = UNSET,
    serial_iew: Union[Unset, list[str]] = UNSET,
    serial_isw: Union[Unset, list[str]] = UNSET,
    serial_n: Union[Unset, list[str]] = UNSET,
    serial_nic: Union[Unset, list[str]] = UNSET,
    serial_nie: Union[Unset, list[str]] = UNSET,
    serial_niew: Union[Unset, list[str]] = UNSET,
    serial_nisw: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    status: Union[Unset, list[str]] = UNSET,
    status_empty: Union[Unset, bool] = UNSET,
    status_ic: Union[Unset, list[str]] = UNSET,
    status_ie: Union[Unset, list[str]] = UNSET,
    status_iew: Union[Unset, list[str]] = UNSET,
    status_isw: Union[Unset, list[str]] = UNSET,
    status_n: Union[Unset, list[str]] = UNSET,
    status_nic: Union[Unset, list[str]] = UNSET,
    status_nie: Union[Unset, list[str]] = UNSET,
    status_niew: Union[Unset, list[str]] = UNSET,
    status_nisw: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tenant: Union[Unset, list[str]] = UNSET,
    tenant_n: Union[Unset, list[str]] = UNSET,
    tenant_group: Union[Unset, list[str]] = UNSET,
    tenant_group_n: Union[Unset, list[str]] = UNSET,
    tenant_group_id: Union[Unset, list[str]] = UNSET,
    tenant_group_id_n: Union[Unset, list[str]] = UNSET,
    tenant_id: Union[Unset, list[Union[None, int]]] = UNSET,
    tenant_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    vc_position: Union[Unset, list[int]] = UNSET,
    vc_position_empty: Union[Unset, bool] = UNSET,
    vc_position_gt: Union[Unset, list[int]] = UNSET,
    vc_position_gte: Union[Unset, list[int]] = UNSET,
    vc_position_lt: Union[Unset, list[int]] = UNSET,
    vc_position_lte: Union[Unset, list[int]] = UNSET,
    vc_position_n: Union[Unset, list[int]] = UNSET,
    vc_priority: Union[Unset, list[int]] = UNSET,
    vc_priority_empty: Union[Unset, bool] = UNSET,
    vc_priority_gt: Union[Unset, list[int]] = UNSET,
    vc_priority_gte: Union[Unset, list[int]] = UNSET,
    vc_priority_lt: Union[Unset, list[int]] = UNSET,
    vc_priority_lte: Union[Unset, list[int]] = UNSET,
    vc_priority_n: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id_n: Union[Unset, list[int]] = UNSET,
    virtual_chassis_member: Union[Unset, bool] = UNSET,
) -> Optional[PaginatedDeviceWithConfigContextList]:
    """Get a list of device objects.

    Args:
        airflow (Union[Unset, DcimDevicesListAirflow]):
        asset_tag (Union[Unset, list[str]]):
        asset_tag_empty (Union[Unset, bool]):
        asset_tag_ic (Union[Unset, list[str]]):
        asset_tag_ie (Union[Unset, list[str]]):
        asset_tag_iew (Union[Unset, list[str]]):
        asset_tag_isw (Union[Unset, list[str]]):
        asset_tag_n (Union[Unset, list[str]]):
        asset_tag_nic (Union[Unset, list[str]]):
        asset_tag_nie (Union[Unset, list[str]]):
        asset_tag_niew (Union[Unset, list[str]]):
        asset_tag_nisw (Union[Unset, list[str]]):
        cluster_group (Union[Unset, list[str]]):
        cluster_group_n (Union[Unset, list[str]]):
        cluster_group_id (Union[Unset, list[int]]):
        cluster_group_id_n (Union[Unset, list[int]]):
        cluster_id (Union[Unset, list[Union[None, int]]]):
        cluster_id_n (Union[Unset, list[Union[None, int]]]):
        config_template_id (Union[Unset, list[Union[None, int]]]):
        config_template_id_n (Union[Unset, list[Union[None, int]]]):
        console_port_count (Union[Unset, list[int]]):
        console_port_count_empty (Union[Unset, bool]):
        console_port_count_gt (Union[Unset, list[int]]):
        console_port_count_gte (Union[Unset, list[int]]):
        console_port_count_lt (Union[Unset, list[int]]):
        console_port_count_lte (Union[Unset, list[int]]):
        console_port_count_n (Union[Unset, list[int]]):
        console_ports (Union[Unset, bool]):
        console_server_port_count (Union[Unset, list[int]]):
        console_server_port_count_empty (Union[Unset, bool]):
        console_server_port_count_gt (Union[Unset, list[int]]):
        console_server_port_count_gte (Union[Unset, list[int]]):
        console_server_port_count_lt (Union[Unset, list[int]]):
        console_server_port_count_lte (Union[Unset, list[int]]):
        console_server_port_count_n (Union[Unset, list[int]]):
        console_server_ports (Union[Unset, bool]):
        contact (Union[Unset, list[int]]):
        contact_n (Union[Unset, list[int]]):
        contact_group (Union[Unset, list[str]]):
        contact_group_n (Union[Unset, list[str]]):
        contact_role (Union[Unset, list[int]]):
        contact_role_n (Union[Unset, list[int]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        description (Union[Unset, list[str]]):
        description_empty (Union[Unset, bool]):
        description_ic (Union[Unset, list[str]]):
        description_ie (Union[Unset, list[str]]):
        description_iew (Union[Unset, list[str]]):
        description_isw (Union[Unset, list[str]]):
        description_n (Union[Unset, list[str]]):
        description_nic (Union[Unset, list[str]]):
        description_nie (Union[Unset, list[str]]):
        description_niew (Union[Unset, list[str]]):
        description_nisw (Union[Unset, list[str]]):
        device_bay_count (Union[Unset, list[int]]):
        device_bay_count_empty (Union[Unset, bool]):
        device_bay_count_gt (Union[Unset, list[int]]):
        device_bay_count_gte (Union[Unset, list[int]]):
        device_bay_count_lt (Union[Unset, list[int]]):
        device_bay_count_lte (Union[Unset, list[int]]):
        device_bay_count_n (Union[Unset, list[int]]):
        device_bays (Union[Unset, bool]):
        device_type (Union[Unset, list[str]]):
        device_type_n (Union[Unset, list[str]]):
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
        front_port_count (Union[Unset, list[int]]):
        front_port_count_empty (Union[Unset, bool]):
        front_port_count_gt (Union[Unset, list[int]]):
        front_port_count_gte (Union[Unset, list[int]]):
        front_port_count_lt (Union[Unset, list[int]]):
        front_port_count_lte (Union[Unset, list[int]]):
        front_port_count_n (Union[Unset, list[int]]):
        has_oob_ip (Union[Unset, bool]):
        has_primary_ip (Union[Unset, bool]):
        has_virtual_device_context (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_count (Union[Unset, list[int]]):
        interface_count_empty (Union[Unset, bool]):
        interface_count_gt (Union[Unset, list[int]]):
        interface_count_gte (Union[Unset, list[int]]):
        interface_count_lt (Union[Unset, list[int]]):
        interface_count_lte (Union[Unset, list[int]]):
        interface_count_n (Union[Unset, list[int]]):
        interfaces (Union[Unset, bool]):
        inventory_item_count (Union[Unset, list[int]]):
        inventory_item_count_empty (Union[Unset, bool]):
        inventory_item_count_gt (Union[Unset, list[int]]):
        inventory_item_count_gte (Union[Unset, list[int]]):
        inventory_item_count_lt (Union[Unset, list[int]]):
        inventory_item_count_lte (Union[Unset, list[int]]):
        inventory_item_count_n (Union[Unset, list[int]]):
        is_full_depth (Union[Unset, bool]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        latitude (Union[Unset, list[float]]):
        latitude_empty (Union[Unset, bool]):
        latitude_gt (Union[Unset, list[float]]):
        latitude_gte (Union[Unset, list[float]]):
        latitude_lt (Union[Unset, list[float]]):
        latitude_lte (Union[Unset, list[float]]):
        latitude_n (Union[Unset, list[float]]):
        limit (Union[Unset, int]):
        local_context_data (Union[Unset, bool]):
        location (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_id (Union[Unset, list[str]]):
        location_id_n (Union[Unset, list[str]]):
        longitude (Union[Unset, list[float]]):
        longitude_empty (Union[Unset, bool]):
        longitude_gt (Union[Unset, list[float]]):
        longitude_gte (Union[Unset, list[float]]):
        longitude_lt (Union[Unset, list[float]]):
        longitude_lte (Union[Unset, list[float]]):
        longitude_n (Union[Unset, list[float]]):
        mac_address (Union[Unset, list[str]]):
        mac_address_ic (Union[Unset, list[str]]):
        mac_address_ie (Union[Unset, list[str]]):
        mac_address_iew (Union[Unset, list[str]]):
        mac_address_isw (Union[Unset, list[str]]):
        mac_address_n (Union[Unset, list[str]]):
        mac_address_nic (Union[Unset, list[str]]):
        mac_address_nie (Union[Unset, list[str]]):
        mac_address_niew (Union[Unset, list[str]]):
        mac_address_nisw (Union[Unset, list[str]]):
        manufacturer (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_id (Union[Unset, list[int]]):
        manufacturer_id_n (Union[Unset, list[int]]):
        model (Union[Unset, list[str]]):
        model_n (Union[Unset, list[str]]):
        modified_by_request (Union[Unset, UUID]):
        module_bay_count (Union[Unset, list[int]]):
        module_bay_count_empty (Union[Unset, bool]):
        module_bay_count_gt (Union[Unset, list[int]]):
        module_bay_count_gte (Union[Unset, list[int]]):
        module_bay_count_lt (Union[Unset, list[int]]):
        module_bay_count_lte (Union[Unset, list[int]]):
        module_bay_count_n (Union[Unset, list[int]]):
        module_bays (Union[Unset, bool]):
        name (Union[Unset, list[str]]):
        name_empty (Union[Unset, bool]):
        name_ic (Union[Unset, list[str]]):
        name_ie (Union[Unset, list[str]]):
        name_iew (Union[Unset, list[str]]):
        name_isw (Union[Unset, list[str]]):
        name_n (Union[Unset, list[str]]):
        name_nic (Union[Unset, list[str]]):
        name_nie (Union[Unset, list[str]]):
        name_niew (Union[Unset, list[str]]):
        name_nisw (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        oob_ip_id (Union[Unset, list[int]]):
        oob_ip_id_n (Union[Unset, list[int]]):
        ordering (Union[Unset, str]):
        parent_bay_id (Union[Unset, list[int]]):
        parent_bay_id_n (Union[Unset, list[int]]):
        parent_device_id (Union[Unset, list[int]]):
        parent_device_id_n (Union[Unset, list[int]]):
        pass_through_ports (Union[Unset, bool]):
        platform (Union[Unset, list[str]]):
        platform_n (Union[Unset, list[str]]):
        platform_id (Union[Unset, list[Union[None, int]]]):
        platform_id_n (Union[Unset, list[Union[None, int]]]):
        position (Union[Unset, list[float]]):
        position_empty (Union[Unset, bool]):
        position_gt (Union[Unset, list[float]]):
        position_gte (Union[Unset, list[float]]):
        position_lt (Union[Unset, list[float]]):
        position_lte (Union[Unset, list[float]]):
        position_n (Union[Unset, list[float]]):
        power_outlet_count (Union[Unset, list[int]]):
        power_outlet_count_empty (Union[Unset, bool]):
        power_outlet_count_gt (Union[Unset, list[int]]):
        power_outlet_count_gte (Union[Unset, list[int]]):
        power_outlet_count_lt (Union[Unset, list[int]]):
        power_outlet_count_lte (Union[Unset, list[int]]):
        power_outlet_count_n (Union[Unset, list[int]]):
        power_outlets (Union[Unset, bool]):
        power_port_count (Union[Unset, list[int]]):
        power_port_count_empty (Union[Unset, bool]):
        power_port_count_gt (Union[Unset, list[int]]):
        power_port_count_gte (Union[Unset, list[int]]):
        power_port_count_lt (Union[Unset, list[int]]):
        power_port_count_lte (Union[Unset, list[int]]):
        power_port_count_n (Union[Unset, list[int]]):
        power_ports (Union[Unset, bool]):
        primary_ip4 (Union[Unset, list[str]]):
        primary_ip4_n (Union[Unset, list[str]]):
        primary_ip4_id (Union[Unset, list[int]]):
        primary_ip4_id_n (Union[Unset, list[int]]):
        primary_ip6 (Union[Unset, list[str]]):
        primary_ip6_n (Union[Unset, list[str]]):
        primary_ip6_id (Union[Unset, list[int]]):
        primary_ip6_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        rack_id (Union[Unset, list[int]]):
        rack_id_n (Union[Unset, list[int]]):
        rear_port_count (Union[Unset, list[int]]):
        rear_port_count_empty (Union[Unset, bool]):
        rear_port_count_gt (Union[Unset, list[int]]):
        rear_port_count_gte (Union[Unset, list[int]]):
        rear_port_count_lt (Union[Unset, list[int]]):
        rear_port_count_lte (Union[Unset, list[int]]):
        rear_port_count_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[str]]):
        role_id_n (Union[Unset, list[str]]):
        serial (Union[Unset, list[str]]):
        serial_empty (Union[Unset, bool]):
        serial_ic (Union[Unset, list[str]]):
        serial_ie (Union[Unset, list[str]]):
        serial_iew (Union[Unset, list[str]]):
        serial_isw (Union[Unset, list[str]]):
        serial_n (Union[Unset, list[str]]):
        serial_nic (Union[Unset, list[str]]):
        serial_nie (Union[Unset, list[str]]):
        serial_niew (Union[Unset, list[str]]):
        serial_nisw (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
        status (Union[Unset, list[str]]):
        status_empty (Union[Unset, bool]):
        status_ic (Union[Unset, list[str]]):
        status_ie (Union[Unset, list[str]]):
        status_iew (Union[Unset, list[str]]):
        status_isw (Union[Unset, list[str]]):
        status_n (Union[Unset, list[str]]):
        status_nic (Union[Unset, list[str]]):
        status_nie (Union[Unset, list[str]]):
        status_niew (Union[Unset, list[str]]):
        status_nisw (Union[Unset, list[str]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        tenant (Union[Unset, list[str]]):
        tenant_n (Union[Unset, list[str]]):
        tenant_group (Union[Unset, list[str]]):
        tenant_group_n (Union[Unset, list[str]]):
        tenant_group_id (Union[Unset, list[str]]):
        tenant_group_id_n (Union[Unset, list[str]]):
        tenant_id (Union[Unset, list[Union[None, int]]]):
        tenant_id_n (Union[Unset, list[Union[None, int]]]):
        updated_by_request (Union[Unset, UUID]):
        vc_position (Union[Unset, list[int]]):
        vc_position_empty (Union[Unset, bool]):
        vc_position_gt (Union[Unset, list[int]]):
        vc_position_gte (Union[Unset, list[int]]):
        vc_position_lt (Union[Unset, list[int]]):
        vc_position_lte (Union[Unset, list[int]]):
        vc_position_n (Union[Unset, list[int]]):
        vc_priority (Union[Unset, list[int]]):
        vc_priority_empty (Union[Unset, bool]):
        vc_priority_gt (Union[Unset, list[int]]):
        vc_priority_gte (Union[Unset, list[int]]):
        vc_priority_lt (Union[Unset, list[int]]):
        vc_priority_lte (Union[Unset, list[int]]):
        vc_priority_n (Union[Unset, list[int]]):
        virtual_chassis_id (Union[Unset, list[int]]):
        virtual_chassis_id_n (Union[Unset, list[int]]):
        virtual_chassis_member (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDeviceWithConfigContextList
    """

    return (
        await asyncio_detailed(
            client=client,
            airflow=airflow,
            asset_tag=asset_tag,
            asset_tag_empty=asset_tag_empty,
            asset_tag_ic=asset_tag_ic,
            asset_tag_ie=asset_tag_ie,
            asset_tag_iew=asset_tag_iew,
            asset_tag_isw=asset_tag_isw,
            asset_tag_n=asset_tag_n,
            asset_tag_nic=asset_tag_nic,
            asset_tag_nie=asset_tag_nie,
            asset_tag_niew=asset_tag_niew,
            asset_tag_nisw=asset_tag_nisw,
            cluster_group=cluster_group,
            cluster_group_n=cluster_group_n,
            cluster_group_id=cluster_group_id,
            cluster_group_id_n=cluster_group_id_n,
            cluster_id=cluster_id,
            cluster_id_n=cluster_id_n,
            config_template_id=config_template_id,
            config_template_id_n=config_template_id_n,
            console_port_count=console_port_count,
            console_port_count_empty=console_port_count_empty,
            console_port_count_gt=console_port_count_gt,
            console_port_count_gte=console_port_count_gte,
            console_port_count_lt=console_port_count_lt,
            console_port_count_lte=console_port_count_lte,
            console_port_count_n=console_port_count_n,
            console_ports=console_ports,
            console_server_port_count=console_server_port_count,
            console_server_port_count_empty=console_server_port_count_empty,
            console_server_port_count_gt=console_server_port_count_gt,
            console_server_port_count_gte=console_server_port_count_gte,
            console_server_port_count_lt=console_server_port_count_lt,
            console_server_port_count_lte=console_server_port_count_lte,
            console_server_port_count_n=console_server_port_count_n,
            console_server_ports=console_server_ports,
            contact=contact,
            contact_n=contact_n,
            contact_group=contact_group,
            contact_group_n=contact_group_n,
            contact_role=contact_role,
            contact_role_n=contact_role_n,
            created=created,
            created_empty=created_empty,
            created_gt=created_gt,
            created_gte=created_gte,
            created_lt=created_lt,
            created_lte=created_lte,
            created_n=created_n,
            created_by_request=created_by_request,
            description=description,
            description_empty=description_empty,
            description_ic=description_ic,
            description_ie=description_ie,
            description_iew=description_iew,
            description_isw=description_isw,
            description_n=description_n,
            description_nic=description_nic,
            description_nie=description_nie,
            description_niew=description_niew,
            description_nisw=description_nisw,
            device_bay_count=device_bay_count,
            device_bay_count_empty=device_bay_count_empty,
            device_bay_count_gt=device_bay_count_gt,
            device_bay_count_gte=device_bay_count_gte,
            device_bay_count_lt=device_bay_count_lt,
            device_bay_count_lte=device_bay_count_lte,
            device_bay_count_n=device_bay_count_n,
            device_bays=device_bays,
            device_type=device_type,
            device_type_n=device_type_n,
            device_type_id=device_type_id,
            device_type_id_n=device_type_id_n,
            front_port_count=front_port_count,
            front_port_count_empty=front_port_count_empty,
            front_port_count_gt=front_port_count_gt,
            front_port_count_gte=front_port_count_gte,
            front_port_count_lt=front_port_count_lt,
            front_port_count_lte=front_port_count_lte,
            front_port_count_n=front_port_count_n,
            has_oob_ip=has_oob_ip,
            has_primary_ip=has_primary_ip,
            has_virtual_device_context=has_virtual_device_context,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            interface_count=interface_count,
            interface_count_empty=interface_count_empty,
            interface_count_gt=interface_count_gt,
            interface_count_gte=interface_count_gte,
            interface_count_lt=interface_count_lt,
            interface_count_lte=interface_count_lte,
            interface_count_n=interface_count_n,
            interfaces=interfaces,
            inventory_item_count=inventory_item_count,
            inventory_item_count_empty=inventory_item_count_empty,
            inventory_item_count_gt=inventory_item_count_gt,
            inventory_item_count_gte=inventory_item_count_gte,
            inventory_item_count_lt=inventory_item_count_lt,
            inventory_item_count_lte=inventory_item_count_lte,
            inventory_item_count_n=inventory_item_count_n,
            is_full_depth=is_full_depth,
            last_updated=last_updated,
            last_updated_empty=last_updated_empty,
            last_updated_gt=last_updated_gt,
            last_updated_gte=last_updated_gte,
            last_updated_lt=last_updated_lt,
            last_updated_lte=last_updated_lte,
            last_updated_n=last_updated_n,
            latitude=latitude,
            latitude_empty=latitude_empty,
            latitude_gt=latitude_gt,
            latitude_gte=latitude_gte,
            latitude_lt=latitude_lt,
            latitude_lte=latitude_lte,
            latitude_n=latitude_n,
            limit=limit,
            local_context_data=local_context_data,
            location=location,
            location_n=location_n,
            location_id=location_id,
            location_id_n=location_id_n,
            longitude=longitude,
            longitude_empty=longitude_empty,
            longitude_gt=longitude_gt,
            longitude_gte=longitude_gte,
            longitude_lt=longitude_lt,
            longitude_lte=longitude_lte,
            longitude_n=longitude_n,
            mac_address=mac_address,
            mac_address_ic=mac_address_ic,
            mac_address_ie=mac_address_ie,
            mac_address_iew=mac_address_iew,
            mac_address_isw=mac_address_isw,
            mac_address_n=mac_address_n,
            mac_address_nic=mac_address_nic,
            mac_address_nie=mac_address_nie,
            mac_address_niew=mac_address_niew,
            mac_address_nisw=mac_address_nisw,
            manufacturer=manufacturer,
            manufacturer_n=manufacturer_n,
            manufacturer_id=manufacturer_id,
            manufacturer_id_n=manufacturer_id_n,
            model=model,
            model_n=model_n,
            modified_by_request=modified_by_request,
            module_bay_count=module_bay_count,
            module_bay_count_empty=module_bay_count_empty,
            module_bay_count_gt=module_bay_count_gt,
            module_bay_count_gte=module_bay_count_gte,
            module_bay_count_lt=module_bay_count_lt,
            module_bay_count_lte=module_bay_count_lte,
            module_bay_count_n=module_bay_count_n,
            module_bays=module_bays,
            name=name,
            name_empty=name_empty,
            name_ic=name_ic,
            name_ie=name_ie,
            name_iew=name_iew,
            name_isw=name_isw,
            name_n=name_n,
            name_nic=name_nic,
            name_nie=name_nie,
            name_niew=name_niew,
            name_nisw=name_nisw,
            offset=offset,
            oob_ip_id=oob_ip_id,
            oob_ip_id_n=oob_ip_id_n,
            ordering=ordering,
            parent_bay_id=parent_bay_id,
            parent_bay_id_n=parent_bay_id_n,
            parent_device_id=parent_device_id,
            parent_device_id_n=parent_device_id_n,
            pass_through_ports=pass_through_ports,
            platform=platform,
            platform_n=platform_n,
            platform_id=platform_id,
            platform_id_n=platform_id_n,
            position=position,
            position_empty=position_empty,
            position_gt=position_gt,
            position_gte=position_gte,
            position_lt=position_lt,
            position_lte=position_lte,
            position_n=position_n,
            power_outlet_count=power_outlet_count,
            power_outlet_count_empty=power_outlet_count_empty,
            power_outlet_count_gt=power_outlet_count_gt,
            power_outlet_count_gte=power_outlet_count_gte,
            power_outlet_count_lt=power_outlet_count_lt,
            power_outlet_count_lte=power_outlet_count_lte,
            power_outlet_count_n=power_outlet_count_n,
            power_outlets=power_outlets,
            power_port_count=power_port_count,
            power_port_count_empty=power_port_count_empty,
            power_port_count_gt=power_port_count_gt,
            power_port_count_gte=power_port_count_gte,
            power_port_count_lt=power_port_count_lt,
            power_port_count_lte=power_port_count_lte,
            power_port_count_n=power_port_count_n,
            power_ports=power_ports,
            primary_ip4=primary_ip4,
            primary_ip4_n=primary_ip4_n,
            primary_ip4_id=primary_ip4_id,
            primary_ip4_id_n=primary_ip4_id_n,
            primary_ip6=primary_ip6,
            primary_ip6_n=primary_ip6_n,
            primary_ip6_id=primary_ip6_id,
            primary_ip6_id_n=primary_ip6_id_n,
            q=q,
            rack_id=rack_id,
            rack_id_n=rack_id_n,
            rear_port_count=rear_port_count,
            rear_port_count_empty=rear_port_count_empty,
            rear_port_count_gt=rear_port_count_gt,
            rear_port_count_gte=rear_port_count_gte,
            rear_port_count_lt=rear_port_count_lt,
            rear_port_count_lte=rear_port_count_lte,
            rear_port_count_n=rear_port_count_n,
            region=region,
            region_n=region_n,
            region_id=region_id,
            region_id_n=region_id_n,
            role=role,
            role_n=role_n,
            role_id=role_id,
            role_id_n=role_id_n,
            serial=serial,
            serial_empty=serial_empty,
            serial_ic=serial_ic,
            serial_ie=serial_ie,
            serial_iew=serial_iew,
            serial_isw=serial_isw,
            serial_n=serial_n,
            serial_nic=serial_nic,
            serial_nie=serial_nie,
            serial_niew=serial_niew,
            serial_nisw=serial_nisw,
            site=site,
            site_n=site_n,
            site_group=site_group,
            site_group_n=site_group_n,
            site_group_id=site_group_id,
            site_group_id_n=site_group_id_n,
            site_id=site_id,
            site_id_n=site_id_n,
            status=status,
            status_empty=status_empty,
            status_ic=status_ic,
            status_ie=status_ie,
            status_iew=status_iew,
            status_isw=status_isw,
            status_n=status_n,
            status_nic=status_nic,
            status_nie=status_nie,
            status_niew=status_niew,
            status_nisw=status_nisw,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
            tenant=tenant,
            tenant_n=tenant_n,
            tenant_group=tenant_group,
            tenant_group_n=tenant_group_n,
            tenant_group_id=tenant_group_id,
            tenant_group_id_n=tenant_group_id_n,
            tenant_id=tenant_id,
            tenant_id_n=tenant_id_n,
            updated_by_request=updated_by_request,
            vc_position=vc_position,
            vc_position_empty=vc_position_empty,
            vc_position_gt=vc_position_gt,
            vc_position_gte=vc_position_gte,
            vc_position_lt=vc_position_lt,
            vc_position_lte=vc_position_lte,
            vc_position_n=vc_position_n,
            vc_priority=vc_priority,
            vc_priority_empty=vc_priority_empty,
            vc_priority_gt=vc_priority_gt,
            vc_priority_gte=vc_priority_gte,
            vc_priority_lt=vc_priority_lt,
            vc_priority_lte=vc_priority_lte,
            vc_priority_n=vc_priority_n,
            virtual_chassis_id=virtual_chassis_id,
            virtual_chassis_id_n=virtual_chassis_id_n,
            virtual_chassis_member=virtual_chassis_member,
        )
    ).parsed
