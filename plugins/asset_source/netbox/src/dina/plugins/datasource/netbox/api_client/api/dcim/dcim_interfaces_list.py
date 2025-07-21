import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dcim_interfaces_list_cable_end import DcimInterfacesListCableEnd
from ...models.paginated_interface_list import PaginatedInterfaceList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    bridge_id: Union[Unset, list[int]] = UNSET,
    bridge_id_n: Union[Unset, list[int]] = UNSET,
    cable_end: Union[Unset, DcimInterfacesListCableEnd] = UNSET,
    cable_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cable_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cabled: Union[Unset, bool] = UNSET,
    connected: Union[Unset, bool] = UNSET,
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
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    device_id_n: Union[Unset, list[int]] = UNSET,
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_id: Union[Unset, list[int]] = UNSET,
    device_role_id_n: Union[Unset, list[int]] = UNSET,
    device_status: Union[Unset, list[str]] = UNSET,
    device_status_empty: Union[Unset, bool] = UNSET,
    device_status_ic: Union[Unset, list[str]] = UNSET,
    device_status_ie: Union[Unset, list[str]] = UNSET,
    device_status_iew: Union[Unset, list[str]] = UNSET,
    device_status_isw: Union[Unset, list[str]] = UNSET,
    device_status_n: Union[Unset, list[str]] = UNSET,
    device_status_nic: Union[Unset, list[str]] = UNSET,
    device_status_nie: Union[Unset, list[str]] = UNSET,
    device_status_niew: Union[Unset, list[str]] = UNSET,
    device_status_nisw: Union[Unset, list[str]] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    duplex: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_empty: Union[Unset, bool] = UNSET,
    duplex_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_n: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    kind: Union[Unset, str] = UNSET,
    l2vpn: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_n: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_id: Union[Unset, list[int]] = UNSET,
    l2vpn_id_n: Union[Unset, list[int]] = UNSET,
    label: Union[Unset, list[str]] = UNSET,
    label_empty: Union[Unset, bool] = UNSET,
    label_ic: Union[Unset, list[str]] = UNSET,
    label_ie: Union[Unset, list[str]] = UNSET,
    label_iew: Union[Unset, list[str]] = UNSET,
    label_isw: Union[Unset, list[str]] = UNSET,
    label_n: Union[Unset, list[str]] = UNSET,
    label_nic: Union[Unset, list[str]] = UNSET,
    label_nie: Union[Unset, list[str]] = UNSET,
    label_niew: Union[Unset, list[str]] = UNSET,
    label_nisw: Union[Unset, list[str]] = UNSET,
    lag_id: Union[Unset, list[int]] = UNSET,
    lag_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
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
    mark_connected: Union[Unset, bool] = UNSET,
    mgmt_only: Union[Unset, bool] = UNSET,
    mode: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_empty: Union[Unset, bool] = UNSET,
    mode_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_n: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_id: Union[Unset, list[Union[None, int]]] = UNSET,
    module_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    mtu: Union[Unset, list[int]] = UNSET,
    mtu_empty: Union[Unset, bool] = UNSET,
    mtu_gt: Union[Unset, list[int]] = UNSET,
    mtu_gte: Union[Unset, list[int]] = UNSET,
    mtu_lt: Union[Unset, list[int]] = UNSET,
    mtu_lte: Union[Unset, list[int]] = UNSET,
    mtu_n: Union[Unset, list[int]] = UNSET,
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
    occupied: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, list[int]] = UNSET,
    parent_id_n: Union[Unset, list[int]] = UNSET,
    poe_mode: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_empty: Union[Unset, bool] = UNSET,
    poe_mode_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_n: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_empty: Union[Unset, bool] = UNSET,
    poe_type_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_n: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    primary_mac_address: Union[Unset, list[str]] = UNSET,
    primary_mac_address_n: Union[Unset, list[str]] = UNSET,
    primary_mac_address_id: Union[Unset, list[int]] = UNSET,
    primary_mac_address_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    rf_channel: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_empty: Union[Unset, bool] = UNSET,
    rf_channel_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_n: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_frequency: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_empty: Union[Unset, bool] = UNSET,
    rf_channel_frequency_gt: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_gte: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_lt: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_lte: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_n: Union[Unset, list[float]] = UNSET,
    rf_channel_width: Union[Unset, list[float]] = UNSET,
    rf_channel_width_empty: Union[Unset, bool] = UNSET,
    rf_channel_width_gt: Union[Unset, list[float]] = UNSET,
    rf_channel_width_gte: Union[Unset, list[float]] = UNSET,
    rf_channel_width_lt: Union[Unset, list[float]] = UNSET,
    rf_channel_width_lte: Union[Unset, list[float]] = UNSET,
    rf_channel_width_n: Union[Unset, list[float]] = UNSET,
    rf_role: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_empty: Union[Unset, bool] = UNSET,
    rf_role_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_n: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    speed: Union[Unset, list[int]] = UNSET,
    speed_empty: Union[Unset, list[int]] = UNSET,
    speed_gt: Union[Unset, list[int]] = UNSET,
    speed_gte: Union[Unset, list[int]] = UNSET,
    speed_lt: Union[Unset, list[int]] = UNSET,
    speed_lte: Union[Unset, list[int]] = UNSET,
    speed_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tx_power: Union[Unset, list[int]] = UNSET,
    tx_power_empty: Union[Unset, bool] = UNSET,
    tx_power_gt: Union[Unset, list[int]] = UNSET,
    tx_power_gte: Union[Unset, list[int]] = UNSET,
    tx_power_lt: Union[Unset, list[int]] = UNSET,
    tx_power_lte: Union[Unset, list[int]] = UNSET,
    tx_power_n: Union[Unset, list[int]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    type_empty: Union[Unset, bool] = UNSET,
    type_ic: Union[Unset, list[str]] = UNSET,
    type_ie: Union[Unset, list[str]] = UNSET,
    type_iew: Union[Unset, list[str]] = UNSET,
    type_isw: Union[Unset, list[str]] = UNSET,
    type_n: Union[Unset, list[str]] = UNSET,
    type_nic: Union[Unset, list[str]] = UNSET,
    type_nie: Union[Unset, list[str]] = UNSET,
    type_niew: Union[Unset, list[str]] = UNSET,
    type_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    vdc: Union[Unset, list[str]] = UNSET,
    vdc_n: Union[Unset, list[str]] = UNSET,
    vdc_id: Union[Unset, list[int]] = UNSET,
    vdc_id_n: Union[Unset, list[int]] = UNSET,
    vdc_identifier: Union[Unset, list[Union[None, int]]] = UNSET,
    vdc_identifier_n: Union[Unset, list[Union[None, int]]] = UNSET,
    virtual_chassis: Union[Unset, list[str]] = UNSET,
    virtual_chassis_n: Union[Unset, list[str]] = UNSET,
    virtual_chassis_id: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id_n: Union[Unset, list[int]] = UNSET,
    virtual_chassis_member: Union[Unset, list[str]] = UNSET,
    virtual_chassis_member_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_id_n: Union[Unset, list[int]] = UNSET,
    virtual_circuit_termination_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_termination_id_n: Union[Unset, list[int]] = UNSET,
    vlan: Union[Unset, str] = UNSET,
    vlan_id: Union[Unset, str] = UNSET,
    vlan_translation_policy: Union[Unset, list[str]] = UNSET,
    vlan_translation_policy_n: Union[Unset, list[str]] = UNSET,
    vlan_translation_policy_id: Union[Unset, list[int]] = UNSET,
    vlan_translation_policy_id_n: Union[Unset, list[int]] = UNSET,
    vrf: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_n: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_id: Union[Unset, list[int]] = UNSET,
    vrf_id_n: Union[Unset, list[int]] = UNSET,
    wireless_lan_id: Union[Unset, list[int]] = UNSET,
    wireless_lan_id_n: Union[Unset, list[int]] = UNSET,
    wireless_link_id: Union[Unset, list[Union[None, int]]] = UNSET,
    wireless_link_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    wwn: Union[Unset, list[str]] = UNSET,
    wwn_ic: Union[Unset, list[str]] = UNSET,
    wwn_ie: Union[Unset, list[str]] = UNSET,
    wwn_iew: Union[Unset, list[str]] = UNSET,
    wwn_isw: Union[Unset, list[str]] = UNSET,
    wwn_n: Union[Unset, list[str]] = UNSET,
    wwn_nic: Union[Unset, list[str]] = UNSET,
    wwn_nie: Union[Unset, list[str]] = UNSET,
    wwn_niew: Union[Unset, list[str]] = UNSET,
    wwn_nisw: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_bridge_id: Union[Unset, list[int]] = UNSET
    if not isinstance(bridge_id, Unset):
        json_bridge_id = bridge_id

    params["bridge_id"] = json_bridge_id

    json_bridge_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(bridge_id_n, Unset):
        json_bridge_id_n = bridge_id_n

    params["bridge_id__n"] = json_bridge_id_n

    json_cable_end: Union[Unset, str] = UNSET
    if not isinstance(cable_end, Unset):
        json_cable_end = cable_end.value

    params["cable_end"] = json_cable_end

    json_cable_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(cable_id, Unset):
        json_cable_id = []
        for cable_id_item_data in cable_id:
            cable_id_item: Union[None, int]
            cable_id_item = cable_id_item_data
            json_cable_id.append(cable_id_item)

    params["cable_id"] = json_cable_id

    json_cable_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(cable_id_n, Unset):
        json_cable_id_n = []
        for cable_id_n_item_data in cable_id_n:
            cable_id_n_item: Union[None, int]
            cable_id_n_item = cable_id_n_item_data
            json_cable_id_n.append(cable_id_n_item)

    params["cable_id__n"] = json_cable_id_n

    params["cabled"] = cabled

    params["connected"] = connected

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

    json_device: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(device, Unset):
        json_device = []
        for device_item_data in device:
            device_item: Union[None, str]
            device_item = device_item_data
            json_device.append(device_item)

    params["device"] = json_device

    json_device_n: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(device_n, Unset):
        json_device_n = []
        for device_n_item_data in device_n:
            device_n_item: Union[None, str]
            device_n_item = device_n_item_data
            json_device_n.append(device_n_item)

    params["device__n"] = json_device_n

    json_device_id: Union[Unset, list[int]] = UNSET
    if not isinstance(device_id, Unset):
        json_device_id = device_id

    params["device_id"] = json_device_id

    json_device_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(device_id_n, Unset):
        json_device_id_n = device_id_n

    params["device_id__n"] = json_device_id_n

    json_device_role: Union[Unset, list[str]] = UNSET
    if not isinstance(device_role, Unset):
        json_device_role = device_role

    params["device_role"] = json_device_role

    json_device_role_n: Union[Unset, list[str]] = UNSET
    if not isinstance(device_role_n, Unset):
        json_device_role_n = device_role_n

    params["device_role__n"] = json_device_role_n

    json_device_role_id: Union[Unset, list[int]] = UNSET
    if not isinstance(device_role_id, Unset):
        json_device_role_id = device_role_id

    params["device_role_id"] = json_device_role_id

    json_device_role_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(device_role_id_n, Unset):
        json_device_role_id_n = device_role_id_n

    params["device_role_id__n"] = json_device_role_id_n

    json_device_status: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status, Unset):
        json_device_status = device_status

    params["device_status"] = json_device_status

    params["device_status__empty"] = device_status_empty

    json_device_status_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status_ic, Unset):
        json_device_status_ic = device_status_ic

    params["device_status__ic"] = json_device_status_ic

    json_device_status_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status_ie, Unset):
        json_device_status_ie = device_status_ie

    params["device_status__ie"] = json_device_status_ie

    json_device_status_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status_iew, Unset):
        json_device_status_iew = device_status_iew

    params["device_status__iew"] = json_device_status_iew

    json_device_status_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status_isw, Unset):
        json_device_status_isw = device_status_isw

    params["device_status__isw"] = json_device_status_isw

    json_device_status_n: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status_n, Unset):
        json_device_status_n = device_status_n

    params["device_status__n"] = json_device_status_n

    json_device_status_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status_nic, Unset):
        json_device_status_nic = device_status_nic

    params["device_status__nic"] = json_device_status_nic

    json_device_status_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status_nie, Unset):
        json_device_status_nie = device_status_nie

    params["device_status__nie"] = json_device_status_nie

    json_device_status_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status_niew, Unset):
        json_device_status_niew = device_status_niew

    params["device_status__niew"] = json_device_status_niew

    json_device_status_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status_nisw, Unset):
        json_device_status_nisw = device_status_nisw

    params["device_status__nisw"] = json_device_status_nisw

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

    json_duplex: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(duplex, Unset):
        json_duplex = []
        for duplex_item_data in duplex:
            duplex_item: Union[None, str]
            duplex_item = duplex_item_data
            json_duplex.append(duplex_item)

    params["duplex"] = json_duplex

    params["duplex__empty"] = duplex_empty

    json_duplex_ic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(duplex_ic, Unset):
        json_duplex_ic = []
        for duplex_ic_item_data in duplex_ic:
            duplex_ic_item: Union[None, str]
            duplex_ic_item = duplex_ic_item_data
            json_duplex_ic.append(duplex_ic_item)

    params["duplex__ic"] = json_duplex_ic

    json_duplex_ie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(duplex_ie, Unset):
        json_duplex_ie = []
        for duplex_ie_item_data in duplex_ie:
            duplex_ie_item: Union[None, str]
            duplex_ie_item = duplex_ie_item_data
            json_duplex_ie.append(duplex_ie_item)

    params["duplex__ie"] = json_duplex_ie

    json_duplex_iew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(duplex_iew, Unset):
        json_duplex_iew = []
        for duplex_iew_item_data in duplex_iew:
            duplex_iew_item: Union[None, str]
            duplex_iew_item = duplex_iew_item_data
            json_duplex_iew.append(duplex_iew_item)

    params["duplex__iew"] = json_duplex_iew

    json_duplex_isw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(duplex_isw, Unset):
        json_duplex_isw = []
        for duplex_isw_item_data in duplex_isw:
            duplex_isw_item: Union[None, str]
            duplex_isw_item = duplex_isw_item_data
            json_duplex_isw.append(duplex_isw_item)

    params["duplex__isw"] = json_duplex_isw

    json_duplex_n: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(duplex_n, Unset):
        json_duplex_n = []
        for duplex_n_item_data in duplex_n:
            duplex_n_item: Union[None, str]
            duplex_n_item = duplex_n_item_data
            json_duplex_n.append(duplex_n_item)

    params["duplex__n"] = json_duplex_n

    json_duplex_nic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(duplex_nic, Unset):
        json_duplex_nic = []
        for duplex_nic_item_data in duplex_nic:
            duplex_nic_item: Union[None, str]
            duplex_nic_item = duplex_nic_item_data
            json_duplex_nic.append(duplex_nic_item)

    params["duplex__nic"] = json_duplex_nic

    json_duplex_nie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(duplex_nie, Unset):
        json_duplex_nie = []
        for duplex_nie_item_data in duplex_nie:
            duplex_nie_item: Union[None, str]
            duplex_nie_item = duplex_nie_item_data
            json_duplex_nie.append(duplex_nie_item)

    params["duplex__nie"] = json_duplex_nie

    json_duplex_niew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(duplex_niew, Unset):
        json_duplex_niew = []
        for duplex_niew_item_data in duplex_niew:
            duplex_niew_item: Union[None, str]
            duplex_niew_item = duplex_niew_item_data
            json_duplex_niew.append(duplex_niew_item)

    params["duplex__niew"] = json_duplex_niew

    json_duplex_nisw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(duplex_nisw, Unset):
        json_duplex_nisw = []
        for duplex_nisw_item_data in duplex_nisw:
            duplex_nisw_item: Union[None, str]
            duplex_nisw_item = duplex_nisw_item_data
            json_duplex_nisw.append(duplex_nisw_item)

    params["duplex__nisw"] = json_duplex_nisw

    params["enabled"] = enabled

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

    params["kind"] = kind

    json_l2vpn: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(l2vpn, Unset):
        json_l2vpn = []
        for l2vpn_item_data in l2vpn:
            l2vpn_item: Union[None, int]
            l2vpn_item = l2vpn_item_data
            json_l2vpn.append(l2vpn_item)

    params["l2vpn"] = json_l2vpn

    json_l2vpn_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(l2vpn_n, Unset):
        json_l2vpn_n = []
        for l2vpn_n_item_data in l2vpn_n:
            l2vpn_n_item: Union[None, int]
            l2vpn_n_item = l2vpn_n_item_data
            json_l2vpn_n.append(l2vpn_n_item)

    params["l2vpn__n"] = json_l2vpn_n

    json_l2vpn_id: Union[Unset, list[int]] = UNSET
    if not isinstance(l2vpn_id, Unset):
        json_l2vpn_id = l2vpn_id

    params["l2vpn_id"] = json_l2vpn_id

    json_l2vpn_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(l2vpn_id_n, Unset):
        json_l2vpn_id_n = l2vpn_id_n

    params["l2vpn_id__n"] = json_l2vpn_id_n

    json_label: Union[Unset, list[str]] = UNSET
    if not isinstance(label, Unset):
        json_label = label

    params["label"] = json_label

    params["label__empty"] = label_empty

    json_label_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(label_ic, Unset):
        json_label_ic = label_ic

    params["label__ic"] = json_label_ic

    json_label_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(label_ie, Unset):
        json_label_ie = label_ie

    params["label__ie"] = json_label_ie

    json_label_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(label_iew, Unset):
        json_label_iew = label_iew

    params["label__iew"] = json_label_iew

    json_label_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(label_isw, Unset):
        json_label_isw = label_isw

    params["label__isw"] = json_label_isw

    json_label_n: Union[Unset, list[str]] = UNSET
    if not isinstance(label_n, Unset):
        json_label_n = label_n

    params["label__n"] = json_label_n

    json_label_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(label_nic, Unset):
        json_label_nic = label_nic

    params["label__nic"] = json_label_nic

    json_label_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(label_nie, Unset):
        json_label_nie = label_nie

    params["label__nie"] = json_label_nie

    json_label_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(label_niew, Unset):
        json_label_niew = label_niew

    params["label__niew"] = json_label_niew

    json_label_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(label_nisw, Unset):
        json_label_nisw = label_nisw

    params["label__nisw"] = json_label_nisw

    json_lag_id: Union[Unset, list[int]] = UNSET
    if not isinstance(lag_id, Unset):
        json_lag_id = lag_id

    params["lag_id"] = json_lag_id

    json_lag_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(lag_id_n, Unset):
        json_lag_id_n = lag_id_n

    params["lag_id__n"] = json_lag_id_n

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

    params["limit"] = limit

    json_location: Union[Unset, list[str]] = UNSET
    if not isinstance(location, Unset):
        json_location = location

    params["location"] = json_location

    json_location_n: Union[Unset, list[str]] = UNSET
    if not isinstance(location_n, Unset):
        json_location_n = location_n

    params["location__n"] = json_location_n

    json_location_id: Union[Unset, list[int]] = UNSET
    if not isinstance(location_id, Unset):
        json_location_id = location_id

    params["location_id"] = json_location_id

    json_location_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(location_id_n, Unset):
        json_location_id_n = location_id_n

    params["location_id__n"] = json_location_id_n

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

    params["mark_connected"] = mark_connected

    params["mgmt_only"] = mgmt_only

    json_mode: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode, Unset):
        json_mode = []
        for mode_item_data in mode:
            mode_item: Union[None, str]
            mode_item = mode_item_data
            json_mode.append(mode_item)

    params["mode"] = json_mode

    params["mode__empty"] = mode_empty

    json_mode_ic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode_ic, Unset):
        json_mode_ic = []
        for mode_ic_item_data in mode_ic:
            mode_ic_item: Union[None, str]
            mode_ic_item = mode_ic_item_data
            json_mode_ic.append(mode_ic_item)

    params["mode__ic"] = json_mode_ic

    json_mode_ie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode_ie, Unset):
        json_mode_ie = []
        for mode_ie_item_data in mode_ie:
            mode_ie_item: Union[None, str]
            mode_ie_item = mode_ie_item_data
            json_mode_ie.append(mode_ie_item)

    params["mode__ie"] = json_mode_ie

    json_mode_iew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode_iew, Unset):
        json_mode_iew = []
        for mode_iew_item_data in mode_iew:
            mode_iew_item: Union[None, str]
            mode_iew_item = mode_iew_item_data
            json_mode_iew.append(mode_iew_item)

    params["mode__iew"] = json_mode_iew

    json_mode_isw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode_isw, Unset):
        json_mode_isw = []
        for mode_isw_item_data in mode_isw:
            mode_isw_item: Union[None, str]
            mode_isw_item = mode_isw_item_data
            json_mode_isw.append(mode_isw_item)

    params["mode__isw"] = json_mode_isw

    json_mode_n: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode_n, Unset):
        json_mode_n = []
        for mode_n_item_data in mode_n:
            mode_n_item: Union[None, str]
            mode_n_item = mode_n_item_data
            json_mode_n.append(mode_n_item)

    params["mode__n"] = json_mode_n

    json_mode_nic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode_nic, Unset):
        json_mode_nic = []
        for mode_nic_item_data in mode_nic:
            mode_nic_item: Union[None, str]
            mode_nic_item = mode_nic_item_data
            json_mode_nic.append(mode_nic_item)

    params["mode__nic"] = json_mode_nic

    json_mode_nie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode_nie, Unset):
        json_mode_nie = []
        for mode_nie_item_data in mode_nie:
            mode_nie_item: Union[None, str]
            mode_nie_item = mode_nie_item_data
            json_mode_nie.append(mode_nie_item)

    params["mode__nie"] = json_mode_nie

    json_mode_niew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode_niew, Unset):
        json_mode_niew = []
        for mode_niew_item_data in mode_niew:
            mode_niew_item: Union[None, str]
            mode_niew_item = mode_niew_item_data
            json_mode_niew.append(mode_niew_item)

    params["mode__niew"] = json_mode_niew

    json_mode_nisw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode_nisw, Unset):
        json_mode_nisw = []
        for mode_nisw_item_data in mode_nisw:
            mode_nisw_item: Union[None, str]
            mode_nisw_item = mode_nisw_item_data
            json_mode_nisw.append(mode_nisw_item)

    params["mode__nisw"] = json_mode_nisw

    json_modified_by_request: Union[Unset, str] = UNSET
    if not isinstance(modified_by_request, Unset):
        json_modified_by_request = str(modified_by_request)
    params["modified_by_request"] = json_modified_by_request

    json_module_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(module_id, Unset):
        json_module_id = []
        for module_id_item_data in module_id:
            module_id_item: Union[None, int]
            module_id_item = module_id_item_data
            json_module_id.append(module_id_item)

    params["module_id"] = json_module_id

    json_module_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(module_id_n, Unset):
        json_module_id_n = []
        for module_id_n_item_data in module_id_n:
            module_id_n_item: Union[None, int]
            module_id_n_item = module_id_n_item_data
            json_module_id_n.append(module_id_n_item)

    params["module_id__n"] = json_module_id_n

    json_mtu: Union[Unset, list[int]] = UNSET
    if not isinstance(mtu, Unset):
        json_mtu = mtu

    params["mtu"] = json_mtu

    params["mtu__empty"] = mtu_empty

    json_mtu_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(mtu_gt, Unset):
        json_mtu_gt = mtu_gt

    params["mtu__gt"] = json_mtu_gt

    json_mtu_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(mtu_gte, Unset):
        json_mtu_gte = mtu_gte

    params["mtu__gte"] = json_mtu_gte

    json_mtu_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(mtu_lt, Unset):
        json_mtu_lt = mtu_lt

    params["mtu__lt"] = json_mtu_lt

    json_mtu_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(mtu_lte, Unset):
        json_mtu_lte = mtu_lte

    params["mtu__lte"] = json_mtu_lte

    json_mtu_n: Union[Unset, list[int]] = UNSET
    if not isinstance(mtu_n, Unset):
        json_mtu_n = mtu_n

    params["mtu__n"] = json_mtu_n

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

    params["occupied"] = occupied

    params["offset"] = offset

    params["ordering"] = ordering

    json_parent_id: Union[Unset, list[int]] = UNSET
    if not isinstance(parent_id, Unset):
        json_parent_id = parent_id

    params["parent_id"] = json_parent_id

    json_parent_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(parent_id_n, Unset):
        json_parent_id_n = parent_id_n

    params["parent_id__n"] = json_parent_id_n

    json_poe_mode: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_mode, Unset):
        json_poe_mode = []
        for poe_mode_item_data in poe_mode:
            poe_mode_item: Union[None, str]
            poe_mode_item = poe_mode_item_data
            json_poe_mode.append(poe_mode_item)

    params["poe_mode"] = json_poe_mode

    params["poe_mode__empty"] = poe_mode_empty

    json_poe_mode_ic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_mode_ic, Unset):
        json_poe_mode_ic = []
        for poe_mode_ic_item_data in poe_mode_ic:
            poe_mode_ic_item: Union[None, str]
            poe_mode_ic_item = poe_mode_ic_item_data
            json_poe_mode_ic.append(poe_mode_ic_item)

    params["poe_mode__ic"] = json_poe_mode_ic

    json_poe_mode_ie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_mode_ie, Unset):
        json_poe_mode_ie = []
        for poe_mode_ie_item_data in poe_mode_ie:
            poe_mode_ie_item: Union[None, str]
            poe_mode_ie_item = poe_mode_ie_item_data
            json_poe_mode_ie.append(poe_mode_ie_item)

    params["poe_mode__ie"] = json_poe_mode_ie

    json_poe_mode_iew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_mode_iew, Unset):
        json_poe_mode_iew = []
        for poe_mode_iew_item_data in poe_mode_iew:
            poe_mode_iew_item: Union[None, str]
            poe_mode_iew_item = poe_mode_iew_item_data
            json_poe_mode_iew.append(poe_mode_iew_item)

    params["poe_mode__iew"] = json_poe_mode_iew

    json_poe_mode_isw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_mode_isw, Unset):
        json_poe_mode_isw = []
        for poe_mode_isw_item_data in poe_mode_isw:
            poe_mode_isw_item: Union[None, str]
            poe_mode_isw_item = poe_mode_isw_item_data
            json_poe_mode_isw.append(poe_mode_isw_item)

    params["poe_mode__isw"] = json_poe_mode_isw

    json_poe_mode_n: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_mode_n, Unset):
        json_poe_mode_n = []
        for poe_mode_n_item_data in poe_mode_n:
            poe_mode_n_item: Union[None, str]
            poe_mode_n_item = poe_mode_n_item_data
            json_poe_mode_n.append(poe_mode_n_item)

    params["poe_mode__n"] = json_poe_mode_n

    json_poe_mode_nic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_mode_nic, Unset):
        json_poe_mode_nic = []
        for poe_mode_nic_item_data in poe_mode_nic:
            poe_mode_nic_item: Union[None, str]
            poe_mode_nic_item = poe_mode_nic_item_data
            json_poe_mode_nic.append(poe_mode_nic_item)

    params["poe_mode__nic"] = json_poe_mode_nic

    json_poe_mode_nie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_mode_nie, Unset):
        json_poe_mode_nie = []
        for poe_mode_nie_item_data in poe_mode_nie:
            poe_mode_nie_item: Union[None, str]
            poe_mode_nie_item = poe_mode_nie_item_data
            json_poe_mode_nie.append(poe_mode_nie_item)

    params["poe_mode__nie"] = json_poe_mode_nie

    json_poe_mode_niew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_mode_niew, Unset):
        json_poe_mode_niew = []
        for poe_mode_niew_item_data in poe_mode_niew:
            poe_mode_niew_item: Union[None, str]
            poe_mode_niew_item = poe_mode_niew_item_data
            json_poe_mode_niew.append(poe_mode_niew_item)

    params["poe_mode__niew"] = json_poe_mode_niew

    json_poe_mode_nisw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_mode_nisw, Unset):
        json_poe_mode_nisw = []
        for poe_mode_nisw_item_data in poe_mode_nisw:
            poe_mode_nisw_item: Union[None, str]
            poe_mode_nisw_item = poe_mode_nisw_item_data
            json_poe_mode_nisw.append(poe_mode_nisw_item)

    params["poe_mode__nisw"] = json_poe_mode_nisw

    json_poe_type: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_type, Unset):
        json_poe_type = []
        for poe_type_item_data in poe_type:
            poe_type_item: Union[None, str]
            poe_type_item = poe_type_item_data
            json_poe_type.append(poe_type_item)

    params["poe_type"] = json_poe_type

    params["poe_type__empty"] = poe_type_empty

    json_poe_type_ic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_type_ic, Unset):
        json_poe_type_ic = []
        for poe_type_ic_item_data in poe_type_ic:
            poe_type_ic_item: Union[None, str]
            poe_type_ic_item = poe_type_ic_item_data
            json_poe_type_ic.append(poe_type_ic_item)

    params["poe_type__ic"] = json_poe_type_ic

    json_poe_type_ie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_type_ie, Unset):
        json_poe_type_ie = []
        for poe_type_ie_item_data in poe_type_ie:
            poe_type_ie_item: Union[None, str]
            poe_type_ie_item = poe_type_ie_item_data
            json_poe_type_ie.append(poe_type_ie_item)

    params["poe_type__ie"] = json_poe_type_ie

    json_poe_type_iew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_type_iew, Unset):
        json_poe_type_iew = []
        for poe_type_iew_item_data in poe_type_iew:
            poe_type_iew_item: Union[None, str]
            poe_type_iew_item = poe_type_iew_item_data
            json_poe_type_iew.append(poe_type_iew_item)

    params["poe_type__iew"] = json_poe_type_iew

    json_poe_type_isw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_type_isw, Unset):
        json_poe_type_isw = []
        for poe_type_isw_item_data in poe_type_isw:
            poe_type_isw_item: Union[None, str]
            poe_type_isw_item = poe_type_isw_item_data
            json_poe_type_isw.append(poe_type_isw_item)

    params["poe_type__isw"] = json_poe_type_isw

    json_poe_type_n: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_type_n, Unset):
        json_poe_type_n = []
        for poe_type_n_item_data in poe_type_n:
            poe_type_n_item: Union[None, str]
            poe_type_n_item = poe_type_n_item_data
            json_poe_type_n.append(poe_type_n_item)

    params["poe_type__n"] = json_poe_type_n

    json_poe_type_nic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_type_nic, Unset):
        json_poe_type_nic = []
        for poe_type_nic_item_data in poe_type_nic:
            poe_type_nic_item: Union[None, str]
            poe_type_nic_item = poe_type_nic_item_data
            json_poe_type_nic.append(poe_type_nic_item)

    params["poe_type__nic"] = json_poe_type_nic

    json_poe_type_nie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_type_nie, Unset):
        json_poe_type_nie = []
        for poe_type_nie_item_data in poe_type_nie:
            poe_type_nie_item: Union[None, str]
            poe_type_nie_item = poe_type_nie_item_data
            json_poe_type_nie.append(poe_type_nie_item)

    params["poe_type__nie"] = json_poe_type_nie

    json_poe_type_niew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_type_niew, Unset):
        json_poe_type_niew = []
        for poe_type_niew_item_data in poe_type_niew:
            poe_type_niew_item: Union[None, str]
            poe_type_niew_item = poe_type_niew_item_data
            json_poe_type_niew.append(poe_type_niew_item)

    params["poe_type__niew"] = json_poe_type_niew

    json_poe_type_nisw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(poe_type_nisw, Unset):
        json_poe_type_nisw = []
        for poe_type_nisw_item_data in poe_type_nisw:
            poe_type_nisw_item: Union[None, str]
            poe_type_nisw_item = poe_type_nisw_item_data
            json_poe_type_nisw.append(poe_type_nisw_item)

    params["poe_type__nisw"] = json_poe_type_nisw

    json_primary_mac_address: Union[Unset, list[str]] = UNSET
    if not isinstance(primary_mac_address, Unset):
        json_primary_mac_address = primary_mac_address

    params["primary_mac_address"] = json_primary_mac_address

    json_primary_mac_address_n: Union[Unset, list[str]] = UNSET
    if not isinstance(primary_mac_address_n, Unset):
        json_primary_mac_address_n = primary_mac_address_n

    params["primary_mac_address__n"] = json_primary_mac_address_n

    json_primary_mac_address_id: Union[Unset, list[int]] = UNSET
    if not isinstance(primary_mac_address_id, Unset):
        json_primary_mac_address_id = primary_mac_address_id

    params["primary_mac_address_id"] = json_primary_mac_address_id

    json_primary_mac_address_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(primary_mac_address_id_n, Unset):
        json_primary_mac_address_id_n = primary_mac_address_id_n

    params["primary_mac_address_id__n"] = json_primary_mac_address_id_n

    params["q"] = q

    json_rack: Union[Unset, list[str]] = UNSET
    if not isinstance(rack, Unset):
        json_rack = rack

    params["rack"] = json_rack

    json_rack_n: Union[Unset, list[str]] = UNSET
    if not isinstance(rack_n, Unset):
        json_rack_n = rack_n

    params["rack__n"] = json_rack_n

    json_rack_id: Union[Unset, list[int]] = UNSET
    if not isinstance(rack_id, Unset):
        json_rack_id = rack_id

    params["rack_id"] = json_rack_id

    json_rack_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(rack_id_n, Unset):
        json_rack_id_n = rack_id_n

    params["rack_id__n"] = json_rack_id_n

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

    json_rf_channel: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_channel, Unset):
        json_rf_channel = []
        for rf_channel_item_data in rf_channel:
            rf_channel_item: Union[None, str]
            rf_channel_item = rf_channel_item_data
            json_rf_channel.append(rf_channel_item)

    params["rf_channel"] = json_rf_channel

    params["rf_channel__empty"] = rf_channel_empty

    json_rf_channel_ic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_channel_ic, Unset):
        json_rf_channel_ic = []
        for rf_channel_ic_item_data in rf_channel_ic:
            rf_channel_ic_item: Union[None, str]
            rf_channel_ic_item = rf_channel_ic_item_data
            json_rf_channel_ic.append(rf_channel_ic_item)

    params["rf_channel__ic"] = json_rf_channel_ic

    json_rf_channel_ie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_channel_ie, Unset):
        json_rf_channel_ie = []
        for rf_channel_ie_item_data in rf_channel_ie:
            rf_channel_ie_item: Union[None, str]
            rf_channel_ie_item = rf_channel_ie_item_data
            json_rf_channel_ie.append(rf_channel_ie_item)

    params["rf_channel__ie"] = json_rf_channel_ie

    json_rf_channel_iew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_channel_iew, Unset):
        json_rf_channel_iew = []
        for rf_channel_iew_item_data in rf_channel_iew:
            rf_channel_iew_item: Union[None, str]
            rf_channel_iew_item = rf_channel_iew_item_data
            json_rf_channel_iew.append(rf_channel_iew_item)

    params["rf_channel__iew"] = json_rf_channel_iew

    json_rf_channel_isw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_channel_isw, Unset):
        json_rf_channel_isw = []
        for rf_channel_isw_item_data in rf_channel_isw:
            rf_channel_isw_item: Union[None, str]
            rf_channel_isw_item = rf_channel_isw_item_data
            json_rf_channel_isw.append(rf_channel_isw_item)

    params["rf_channel__isw"] = json_rf_channel_isw

    json_rf_channel_n: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_channel_n, Unset):
        json_rf_channel_n = []
        for rf_channel_n_item_data in rf_channel_n:
            rf_channel_n_item: Union[None, str]
            rf_channel_n_item = rf_channel_n_item_data
            json_rf_channel_n.append(rf_channel_n_item)

    params["rf_channel__n"] = json_rf_channel_n

    json_rf_channel_nic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_channel_nic, Unset):
        json_rf_channel_nic = []
        for rf_channel_nic_item_data in rf_channel_nic:
            rf_channel_nic_item: Union[None, str]
            rf_channel_nic_item = rf_channel_nic_item_data
            json_rf_channel_nic.append(rf_channel_nic_item)

    params["rf_channel__nic"] = json_rf_channel_nic

    json_rf_channel_nie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_channel_nie, Unset):
        json_rf_channel_nie = []
        for rf_channel_nie_item_data in rf_channel_nie:
            rf_channel_nie_item: Union[None, str]
            rf_channel_nie_item = rf_channel_nie_item_data
            json_rf_channel_nie.append(rf_channel_nie_item)

    params["rf_channel__nie"] = json_rf_channel_nie

    json_rf_channel_niew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_channel_niew, Unset):
        json_rf_channel_niew = []
        for rf_channel_niew_item_data in rf_channel_niew:
            rf_channel_niew_item: Union[None, str]
            rf_channel_niew_item = rf_channel_niew_item_data
            json_rf_channel_niew.append(rf_channel_niew_item)

    params["rf_channel__niew"] = json_rf_channel_niew

    json_rf_channel_nisw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_channel_nisw, Unset):
        json_rf_channel_nisw = []
        for rf_channel_nisw_item_data in rf_channel_nisw:
            rf_channel_nisw_item: Union[None, str]
            rf_channel_nisw_item = rf_channel_nisw_item_data
            json_rf_channel_nisw.append(rf_channel_nisw_item)

    params["rf_channel__nisw"] = json_rf_channel_nisw

    json_rf_channel_frequency: Union[Unset, list[float]] = UNSET
    if not isinstance(rf_channel_frequency, Unset):
        json_rf_channel_frequency = rf_channel_frequency

    params["rf_channel_frequency"] = json_rf_channel_frequency

    params["rf_channel_frequency__empty"] = rf_channel_frequency_empty

    json_rf_channel_frequency_gt: Union[Unset, list[float]] = UNSET
    if not isinstance(rf_channel_frequency_gt, Unset):
        json_rf_channel_frequency_gt = rf_channel_frequency_gt

    params["rf_channel_frequency__gt"] = json_rf_channel_frequency_gt

    json_rf_channel_frequency_gte: Union[Unset, list[float]] = UNSET
    if not isinstance(rf_channel_frequency_gte, Unset):
        json_rf_channel_frequency_gte = rf_channel_frequency_gte

    params["rf_channel_frequency__gte"] = json_rf_channel_frequency_gte

    json_rf_channel_frequency_lt: Union[Unset, list[float]] = UNSET
    if not isinstance(rf_channel_frequency_lt, Unset):
        json_rf_channel_frequency_lt = rf_channel_frequency_lt

    params["rf_channel_frequency__lt"] = json_rf_channel_frequency_lt

    json_rf_channel_frequency_lte: Union[Unset, list[float]] = UNSET
    if not isinstance(rf_channel_frequency_lte, Unset):
        json_rf_channel_frequency_lte = rf_channel_frequency_lte

    params["rf_channel_frequency__lte"] = json_rf_channel_frequency_lte

    json_rf_channel_frequency_n: Union[Unset, list[float]] = UNSET
    if not isinstance(rf_channel_frequency_n, Unset):
        json_rf_channel_frequency_n = rf_channel_frequency_n

    params["rf_channel_frequency__n"] = json_rf_channel_frequency_n

    json_rf_channel_width: Union[Unset, list[float]] = UNSET
    if not isinstance(rf_channel_width, Unset):
        json_rf_channel_width = rf_channel_width

    params["rf_channel_width"] = json_rf_channel_width

    params["rf_channel_width__empty"] = rf_channel_width_empty

    json_rf_channel_width_gt: Union[Unset, list[float]] = UNSET
    if not isinstance(rf_channel_width_gt, Unset):
        json_rf_channel_width_gt = rf_channel_width_gt

    params["rf_channel_width__gt"] = json_rf_channel_width_gt

    json_rf_channel_width_gte: Union[Unset, list[float]] = UNSET
    if not isinstance(rf_channel_width_gte, Unset):
        json_rf_channel_width_gte = rf_channel_width_gte

    params["rf_channel_width__gte"] = json_rf_channel_width_gte

    json_rf_channel_width_lt: Union[Unset, list[float]] = UNSET
    if not isinstance(rf_channel_width_lt, Unset):
        json_rf_channel_width_lt = rf_channel_width_lt

    params["rf_channel_width__lt"] = json_rf_channel_width_lt

    json_rf_channel_width_lte: Union[Unset, list[float]] = UNSET
    if not isinstance(rf_channel_width_lte, Unset):
        json_rf_channel_width_lte = rf_channel_width_lte

    params["rf_channel_width__lte"] = json_rf_channel_width_lte

    json_rf_channel_width_n: Union[Unset, list[float]] = UNSET
    if not isinstance(rf_channel_width_n, Unset):
        json_rf_channel_width_n = rf_channel_width_n

    params["rf_channel_width__n"] = json_rf_channel_width_n

    json_rf_role: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_role, Unset):
        json_rf_role = []
        for rf_role_item_data in rf_role:
            rf_role_item: Union[None, str]
            rf_role_item = rf_role_item_data
            json_rf_role.append(rf_role_item)

    params["rf_role"] = json_rf_role

    params["rf_role__empty"] = rf_role_empty

    json_rf_role_ic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_role_ic, Unset):
        json_rf_role_ic = []
        for rf_role_ic_item_data in rf_role_ic:
            rf_role_ic_item: Union[None, str]
            rf_role_ic_item = rf_role_ic_item_data
            json_rf_role_ic.append(rf_role_ic_item)

    params["rf_role__ic"] = json_rf_role_ic

    json_rf_role_ie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_role_ie, Unset):
        json_rf_role_ie = []
        for rf_role_ie_item_data in rf_role_ie:
            rf_role_ie_item: Union[None, str]
            rf_role_ie_item = rf_role_ie_item_data
            json_rf_role_ie.append(rf_role_ie_item)

    params["rf_role__ie"] = json_rf_role_ie

    json_rf_role_iew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_role_iew, Unset):
        json_rf_role_iew = []
        for rf_role_iew_item_data in rf_role_iew:
            rf_role_iew_item: Union[None, str]
            rf_role_iew_item = rf_role_iew_item_data
            json_rf_role_iew.append(rf_role_iew_item)

    params["rf_role__iew"] = json_rf_role_iew

    json_rf_role_isw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_role_isw, Unset):
        json_rf_role_isw = []
        for rf_role_isw_item_data in rf_role_isw:
            rf_role_isw_item: Union[None, str]
            rf_role_isw_item = rf_role_isw_item_data
            json_rf_role_isw.append(rf_role_isw_item)

    params["rf_role__isw"] = json_rf_role_isw

    json_rf_role_n: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_role_n, Unset):
        json_rf_role_n = []
        for rf_role_n_item_data in rf_role_n:
            rf_role_n_item: Union[None, str]
            rf_role_n_item = rf_role_n_item_data
            json_rf_role_n.append(rf_role_n_item)

    params["rf_role__n"] = json_rf_role_n

    json_rf_role_nic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_role_nic, Unset):
        json_rf_role_nic = []
        for rf_role_nic_item_data in rf_role_nic:
            rf_role_nic_item: Union[None, str]
            rf_role_nic_item = rf_role_nic_item_data
            json_rf_role_nic.append(rf_role_nic_item)

    params["rf_role__nic"] = json_rf_role_nic

    json_rf_role_nie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_role_nie, Unset):
        json_rf_role_nie = []
        for rf_role_nie_item_data in rf_role_nie:
            rf_role_nie_item: Union[None, str]
            rf_role_nie_item = rf_role_nie_item_data
            json_rf_role_nie.append(rf_role_nie_item)

    params["rf_role__nie"] = json_rf_role_nie

    json_rf_role_niew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_role_niew, Unset):
        json_rf_role_niew = []
        for rf_role_niew_item_data in rf_role_niew:
            rf_role_niew_item: Union[None, str]
            rf_role_niew_item = rf_role_niew_item_data
            json_rf_role_niew.append(rf_role_niew_item)

    params["rf_role__niew"] = json_rf_role_niew

    json_rf_role_nisw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(rf_role_nisw, Unset):
        json_rf_role_nisw = []
        for rf_role_nisw_item_data in rf_role_nisw:
            rf_role_nisw_item: Union[None, str]
            rf_role_nisw_item = rf_role_nisw_item_data
            json_rf_role_nisw.append(rf_role_nisw_item)

    params["rf_role__nisw"] = json_rf_role_nisw

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

    json_speed: Union[Unset, list[int]] = UNSET
    if not isinstance(speed, Unset):
        json_speed = speed

    params["speed"] = json_speed

    json_speed_empty: Union[Unset, list[int]] = UNSET
    if not isinstance(speed_empty, Unset):
        json_speed_empty = speed_empty

    params["speed__empty"] = json_speed_empty

    json_speed_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(speed_gt, Unset):
        json_speed_gt = speed_gt

    params["speed__gt"] = json_speed_gt

    json_speed_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(speed_gte, Unset):
        json_speed_gte = speed_gte

    params["speed__gte"] = json_speed_gte

    json_speed_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(speed_lt, Unset):
        json_speed_lt = speed_lt

    params["speed__lt"] = json_speed_lt

    json_speed_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(speed_lte, Unset):
        json_speed_lte = speed_lte

    params["speed__lte"] = json_speed_lte

    json_speed_n: Union[Unset, list[int]] = UNSET
    if not isinstance(speed_n, Unset):
        json_speed_n = speed_n

    params["speed__n"] = json_speed_n

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

    json_tx_power: Union[Unset, list[int]] = UNSET
    if not isinstance(tx_power, Unset):
        json_tx_power = tx_power

    params["tx_power"] = json_tx_power

    params["tx_power__empty"] = tx_power_empty

    json_tx_power_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(tx_power_gt, Unset):
        json_tx_power_gt = tx_power_gt

    params["tx_power__gt"] = json_tx_power_gt

    json_tx_power_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(tx_power_gte, Unset):
        json_tx_power_gte = tx_power_gte

    params["tx_power__gte"] = json_tx_power_gte

    json_tx_power_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(tx_power_lt, Unset):
        json_tx_power_lt = tx_power_lt

    params["tx_power__lt"] = json_tx_power_lt

    json_tx_power_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(tx_power_lte, Unset):
        json_tx_power_lte = tx_power_lte

    params["tx_power__lte"] = json_tx_power_lte

    json_tx_power_n: Union[Unset, list[int]] = UNSET
    if not isinstance(tx_power_n, Unset):
        json_tx_power_n = tx_power_n

    params["tx_power__n"] = json_tx_power_n

    json_type_: Union[Unset, list[str]] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    params["type__empty"] = type_empty

    json_type_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(type_ic, Unset):
        json_type_ic = type_ic

    params["type__ic"] = json_type_ic

    json_type_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(type_ie, Unset):
        json_type_ie = type_ie

    params["type__ie"] = json_type_ie

    json_type_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(type_iew, Unset):
        json_type_iew = type_iew

    params["type__iew"] = json_type_iew

    json_type_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(type_isw, Unset):
        json_type_isw = type_isw

    params["type__isw"] = json_type_isw

    json_type_n: Union[Unset, list[str]] = UNSET
    if not isinstance(type_n, Unset):
        json_type_n = type_n

    params["type__n"] = json_type_n

    json_type_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(type_nic, Unset):
        json_type_nic = type_nic

    params["type__nic"] = json_type_nic

    json_type_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(type_nie, Unset):
        json_type_nie = type_nie

    params["type__nie"] = json_type_nie

    json_type_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(type_niew, Unset):
        json_type_niew = type_niew

    params["type__niew"] = json_type_niew

    json_type_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(type_nisw, Unset):
        json_type_nisw = type_nisw

    params["type__nisw"] = json_type_nisw

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    json_vdc: Union[Unset, list[str]] = UNSET
    if not isinstance(vdc, Unset):
        json_vdc = vdc

    params["vdc"] = json_vdc

    json_vdc_n: Union[Unset, list[str]] = UNSET
    if not isinstance(vdc_n, Unset):
        json_vdc_n = vdc_n

    params["vdc__n"] = json_vdc_n

    json_vdc_id: Union[Unset, list[int]] = UNSET
    if not isinstance(vdc_id, Unset):
        json_vdc_id = vdc_id

    params["vdc_id"] = json_vdc_id

    json_vdc_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(vdc_id_n, Unset):
        json_vdc_id_n = vdc_id_n

    params["vdc_id__n"] = json_vdc_id_n

    json_vdc_identifier: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(vdc_identifier, Unset):
        json_vdc_identifier = []
        for vdc_identifier_item_data in vdc_identifier:
            vdc_identifier_item: Union[None, int]
            vdc_identifier_item = vdc_identifier_item_data
            json_vdc_identifier.append(vdc_identifier_item)

    params["vdc_identifier"] = json_vdc_identifier

    json_vdc_identifier_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(vdc_identifier_n, Unset):
        json_vdc_identifier_n = []
        for vdc_identifier_n_item_data in vdc_identifier_n:
            vdc_identifier_n_item: Union[None, int]
            vdc_identifier_n_item = vdc_identifier_n_item_data
            json_vdc_identifier_n.append(vdc_identifier_n_item)

    params["vdc_identifier__n"] = json_vdc_identifier_n

    json_virtual_chassis: Union[Unset, list[str]] = UNSET
    if not isinstance(virtual_chassis, Unset):
        json_virtual_chassis = virtual_chassis

    params["virtual_chassis"] = json_virtual_chassis

    json_virtual_chassis_n: Union[Unset, list[str]] = UNSET
    if not isinstance(virtual_chassis_n, Unset):
        json_virtual_chassis_n = virtual_chassis_n

    params["virtual_chassis__n"] = json_virtual_chassis_n

    json_virtual_chassis_id: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_chassis_id, Unset):
        json_virtual_chassis_id = virtual_chassis_id

    params["virtual_chassis_id"] = json_virtual_chassis_id

    json_virtual_chassis_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_chassis_id_n, Unset):
        json_virtual_chassis_id_n = virtual_chassis_id_n

    params["virtual_chassis_id__n"] = json_virtual_chassis_id_n

    json_virtual_chassis_member: Union[Unset, list[str]] = UNSET
    if not isinstance(virtual_chassis_member, Unset):
        json_virtual_chassis_member = virtual_chassis_member

    params["virtual_chassis_member"] = json_virtual_chassis_member

    json_virtual_chassis_member_id: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_chassis_member_id, Unset):
        json_virtual_chassis_member_id = virtual_chassis_member_id

    params["virtual_chassis_member_id"] = json_virtual_chassis_member_id

    json_virtual_circuit_id: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_circuit_id, Unset):
        json_virtual_circuit_id = virtual_circuit_id

    params["virtual_circuit_id"] = json_virtual_circuit_id

    json_virtual_circuit_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_circuit_id_n, Unset):
        json_virtual_circuit_id_n = virtual_circuit_id_n

    params["virtual_circuit_id__n"] = json_virtual_circuit_id_n

    json_virtual_circuit_termination_id: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_circuit_termination_id, Unset):
        json_virtual_circuit_termination_id = virtual_circuit_termination_id

    params["virtual_circuit_termination_id"] = json_virtual_circuit_termination_id

    json_virtual_circuit_termination_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_circuit_termination_id_n, Unset):
        json_virtual_circuit_termination_id_n = virtual_circuit_termination_id_n

    params["virtual_circuit_termination_id__n"] = json_virtual_circuit_termination_id_n

    params["vlan"] = vlan

    params["vlan_id"] = vlan_id

    json_vlan_translation_policy: Union[Unset, list[str]] = UNSET
    if not isinstance(vlan_translation_policy, Unset):
        json_vlan_translation_policy = vlan_translation_policy

    params["vlan_translation_policy"] = json_vlan_translation_policy

    json_vlan_translation_policy_n: Union[Unset, list[str]] = UNSET
    if not isinstance(vlan_translation_policy_n, Unset):
        json_vlan_translation_policy_n = vlan_translation_policy_n

    params["vlan_translation_policy__n"] = json_vlan_translation_policy_n

    json_vlan_translation_policy_id: Union[Unset, list[int]] = UNSET
    if not isinstance(vlan_translation_policy_id, Unset):
        json_vlan_translation_policy_id = vlan_translation_policy_id

    params["vlan_translation_policy_id"] = json_vlan_translation_policy_id

    json_vlan_translation_policy_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(vlan_translation_policy_id_n, Unset):
        json_vlan_translation_policy_id_n = vlan_translation_policy_id_n

    params["vlan_translation_policy_id__n"] = json_vlan_translation_policy_id_n

    json_vrf: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(vrf, Unset):
        json_vrf = []
        for vrf_item_data in vrf:
            vrf_item: Union[None, str]
            vrf_item = vrf_item_data
            json_vrf.append(vrf_item)

    params["vrf"] = json_vrf

    json_vrf_n: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(vrf_n, Unset):
        json_vrf_n = []
        for vrf_n_item_data in vrf_n:
            vrf_n_item: Union[None, str]
            vrf_n_item = vrf_n_item_data
            json_vrf_n.append(vrf_n_item)

    params["vrf__n"] = json_vrf_n

    json_vrf_id: Union[Unset, list[int]] = UNSET
    if not isinstance(vrf_id, Unset):
        json_vrf_id = vrf_id

    params["vrf_id"] = json_vrf_id

    json_vrf_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(vrf_id_n, Unset):
        json_vrf_id_n = vrf_id_n

    params["vrf_id__n"] = json_vrf_id_n

    json_wireless_lan_id: Union[Unset, list[int]] = UNSET
    if not isinstance(wireless_lan_id, Unset):
        json_wireless_lan_id = wireless_lan_id

    params["wireless_lan_id"] = json_wireless_lan_id

    json_wireless_lan_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(wireless_lan_id_n, Unset):
        json_wireless_lan_id_n = wireless_lan_id_n

    params["wireless_lan_id__n"] = json_wireless_lan_id_n

    json_wireless_link_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(wireless_link_id, Unset):
        json_wireless_link_id = []
        for wireless_link_id_item_data in wireless_link_id:
            wireless_link_id_item: Union[None, int]
            wireless_link_id_item = wireless_link_id_item_data
            json_wireless_link_id.append(wireless_link_id_item)

    params["wireless_link_id"] = json_wireless_link_id

    json_wireless_link_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(wireless_link_id_n, Unset):
        json_wireless_link_id_n = []
        for wireless_link_id_n_item_data in wireless_link_id_n:
            wireless_link_id_n_item: Union[None, int]
            wireless_link_id_n_item = wireless_link_id_n_item_data
            json_wireless_link_id_n.append(wireless_link_id_n_item)

    params["wireless_link_id__n"] = json_wireless_link_id_n

    json_wwn: Union[Unset, list[str]] = UNSET
    if not isinstance(wwn, Unset):
        json_wwn = wwn

    params["wwn"] = json_wwn

    json_wwn_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(wwn_ic, Unset):
        json_wwn_ic = wwn_ic

    params["wwn__ic"] = json_wwn_ic

    json_wwn_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(wwn_ie, Unset):
        json_wwn_ie = wwn_ie

    params["wwn__ie"] = json_wwn_ie

    json_wwn_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(wwn_iew, Unset):
        json_wwn_iew = wwn_iew

    params["wwn__iew"] = json_wwn_iew

    json_wwn_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(wwn_isw, Unset):
        json_wwn_isw = wwn_isw

    params["wwn__isw"] = json_wwn_isw

    json_wwn_n: Union[Unset, list[str]] = UNSET
    if not isinstance(wwn_n, Unset):
        json_wwn_n = wwn_n

    params["wwn__n"] = json_wwn_n

    json_wwn_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(wwn_nic, Unset):
        json_wwn_nic = wwn_nic

    params["wwn__nic"] = json_wwn_nic

    json_wwn_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(wwn_nie, Unset):
        json_wwn_nie = wwn_nie

    params["wwn__nie"] = json_wwn_nie

    json_wwn_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(wwn_niew, Unset):
        json_wwn_niew = wwn_niew

    params["wwn__niew"] = json_wwn_niew

    json_wwn_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(wwn_nisw, Unset):
        json_wwn_nisw = wwn_nisw

    params["wwn__nisw"] = json_wwn_nisw

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/dcim/interfaces/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedInterfaceList]:
    if response.status_code == 200:
        response_200 = PaginatedInterfaceList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedInterfaceList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    bridge_id: Union[Unset, list[int]] = UNSET,
    bridge_id_n: Union[Unset, list[int]] = UNSET,
    cable_end: Union[Unset, DcimInterfacesListCableEnd] = UNSET,
    cable_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cable_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cabled: Union[Unset, bool] = UNSET,
    connected: Union[Unset, bool] = UNSET,
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
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    device_id_n: Union[Unset, list[int]] = UNSET,
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_id: Union[Unset, list[int]] = UNSET,
    device_role_id_n: Union[Unset, list[int]] = UNSET,
    device_status: Union[Unset, list[str]] = UNSET,
    device_status_empty: Union[Unset, bool] = UNSET,
    device_status_ic: Union[Unset, list[str]] = UNSET,
    device_status_ie: Union[Unset, list[str]] = UNSET,
    device_status_iew: Union[Unset, list[str]] = UNSET,
    device_status_isw: Union[Unset, list[str]] = UNSET,
    device_status_n: Union[Unset, list[str]] = UNSET,
    device_status_nic: Union[Unset, list[str]] = UNSET,
    device_status_nie: Union[Unset, list[str]] = UNSET,
    device_status_niew: Union[Unset, list[str]] = UNSET,
    device_status_nisw: Union[Unset, list[str]] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    duplex: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_empty: Union[Unset, bool] = UNSET,
    duplex_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_n: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    kind: Union[Unset, str] = UNSET,
    l2vpn: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_n: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_id: Union[Unset, list[int]] = UNSET,
    l2vpn_id_n: Union[Unset, list[int]] = UNSET,
    label: Union[Unset, list[str]] = UNSET,
    label_empty: Union[Unset, bool] = UNSET,
    label_ic: Union[Unset, list[str]] = UNSET,
    label_ie: Union[Unset, list[str]] = UNSET,
    label_iew: Union[Unset, list[str]] = UNSET,
    label_isw: Union[Unset, list[str]] = UNSET,
    label_n: Union[Unset, list[str]] = UNSET,
    label_nic: Union[Unset, list[str]] = UNSET,
    label_nie: Union[Unset, list[str]] = UNSET,
    label_niew: Union[Unset, list[str]] = UNSET,
    label_nisw: Union[Unset, list[str]] = UNSET,
    lag_id: Union[Unset, list[int]] = UNSET,
    lag_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
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
    mark_connected: Union[Unset, bool] = UNSET,
    mgmt_only: Union[Unset, bool] = UNSET,
    mode: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_empty: Union[Unset, bool] = UNSET,
    mode_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_n: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_id: Union[Unset, list[Union[None, int]]] = UNSET,
    module_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    mtu: Union[Unset, list[int]] = UNSET,
    mtu_empty: Union[Unset, bool] = UNSET,
    mtu_gt: Union[Unset, list[int]] = UNSET,
    mtu_gte: Union[Unset, list[int]] = UNSET,
    mtu_lt: Union[Unset, list[int]] = UNSET,
    mtu_lte: Union[Unset, list[int]] = UNSET,
    mtu_n: Union[Unset, list[int]] = UNSET,
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
    occupied: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, list[int]] = UNSET,
    parent_id_n: Union[Unset, list[int]] = UNSET,
    poe_mode: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_empty: Union[Unset, bool] = UNSET,
    poe_mode_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_n: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_empty: Union[Unset, bool] = UNSET,
    poe_type_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_n: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    primary_mac_address: Union[Unset, list[str]] = UNSET,
    primary_mac_address_n: Union[Unset, list[str]] = UNSET,
    primary_mac_address_id: Union[Unset, list[int]] = UNSET,
    primary_mac_address_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    rf_channel: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_empty: Union[Unset, bool] = UNSET,
    rf_channel_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_n: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_frequency: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_empty: Union[Unset, bool] = UNSET,
    rf_channel_frequency_gt: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_gte: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_lt: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_lte: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_n: Union[Unset, list[float]] = UNSET,
    rf_channel_width: Union[Unset, list[float]] = UNSET,
    rf_channel_width_empty: Union[Unset, bool] = UNSET,
    rf_channel_width_gt: Union[Unset, list[float]] = UNSET,
    rf_channel_width_gte: Union[Unset, list[float]] = UNSET,
    rf_channel_width_lt: Union[Unset, list[float]] = UNSET,
    rf_channel_width_lte: Union[Unset, list[float]] = UNSET,
    rf_channel_width_n: Union[Unset, list[float]] = UNSET,
    rf_role: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_empty: Union[Unset, bool] = UNSET,
    rf_role_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_n: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    speed: Union[Unset, list[int]] = UNSET,
    speed_empty: Union[Unset, list[int]] = UNSET,
    speed_gt: Union[Unset, list[int]] = UNSET,
    speed_gte: Union[Unset, list[int]] = UNSET,
    speed_lt: Union[Unset, list[int]] = UNSET,
    speed_lte: Union[Unset, list[int]] = UNSET,
    speed_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tx_power: Union[Unset, list[int]] = UNSET,
    tx_power_empty: Union[Unset, bool] = UNSET,
    tx_power_gt: Union[Unset, list[int]] = UNSET,
    tx_power_gte: Union[Unset, list[int]] = UNSET,
    tx_power_lt: Union[Unset, list[int]] = UNSET,
    tx_power_lte: Union[Unset, list[int]] = UNSET,
    tx_power_n: Union[Unset, list[int]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    type_empty: Union[Unset, bool] = UNSET,
    type_ic: Union[Unset, list[str]] = UNSET,
    type_ie: Union[Unset, list[str]] = UNSET,
    type_iew: Union[Unset, list[str]] = UNSET,
    type_isw: Union[Unset, list[str]] = UNSET,
    type_n: Union[Unset, list[str]] = UNSET,
    type_nic: Union[Unset, list[str]] = UNSET,
    type_nie: Union[Unset, list[str]] = UNSET,
    type_niew: Union[Unset, list[str]] = UNSET,
    type_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    vdc: Union[Unset, list[str]] = UNSET,
    vdc_n: Union[Unset, list[str]] = UNSET,
    vdc_id: Union[Unset, list[int]] = UNSET,
    vdc_id_n: Union[Unset, list[int]] = UNSET,
    vdc_identifier: Union[Unset, list[Union[None, int]]] = UNSET,
    vdc_identifier_n: Union[Unset, list[Union[None, int]]] = UNSET,
    virtual_chassis: Union[Unset, list[str]] = UNSET,
    virtual_chassis_n: Union[Unset, list[str]] = UNSET,
    virtual_chassis_id: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id_n: Union[Unset, list[int]] = UNSET,
    virtual_chassis_member: Union[Unset, list[str]] = UNSET,
    virtual_chassis_member_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_id_n: Union[Unset, list[int]] = UNSET,
    virtual_circuit_termination_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_termination_id_n: Union[Unset, list[int]] = UNSET,
    vlan: Union[Unset, str] = UNSET,
    vlan_id: Union[Unset, str] = UNSET,
    vlan_translation_policy: Union[Unset, list[str]] = UNSET,
    vlan_translation_policy_n: Union[Unset, list[str]] = UNSET,
    vlan_translation_policy_id: Union[Unset, list[int]] = UNSET,
    vlan_translation_policy_id_n: Union[Unset, list[int]] = UNSET,
    vrf: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_n: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_id: Union[Unset, list[int]] = UNSET,
    vrf_id_n: Union[Unset, list[int]] = UNSET,
    wireless_lan_id: Union[Unset, list[int]] = UNSET,
    wireless_lan_id_n: Union[Unset, list[int]] = UNSET,
    wireless_link_id: Union[Unset, list[Union[None, int]]] = UNSET,
    wireless_link_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    wwn: Union[Unset, list[str]] = UNSET,
    wwn_ic: Union[Unset, list[str]] = UNSET,
    wwn_ie: Union[Unset, list[str]] = UNSET,
    wwn_iew: Union[Unset, list[str]] = UNSET,
    wwn_isw: Union[Unset, list[str]] = UNSET,
    wwn_n: Union[Unset, list[str]] = UNSET,
    wwn_nic: Union[Unset, list[str]] = UNSET,
    wwn_nie: Union[Unset, list[str]] = UNSET,
    wwn_niew: Union[Unset, list[str]] = UNSET,
    wwn_nisw: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedInterfaceList]:
    """Get a list of interface objects.

    Args:
        bridge_id (Union[Unset, list[int]]):
        bridge_id_n (Union[Unset, list[int]]):
        cable_end (Union[Unset, DcimInterfacesListCableEnd]):
        cable_id (Union[Unset, list[Union[None, int]]]):
        cable_id_n (Union[Unset, list[Union[None, int]]]):
        cabled (Union[Unset, bool]):
        connected (Union[Unset, bool]):
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
        device (Union[Unset, list[Union[None, str]]]):
        device_n (Union[Unset, list[Union[None, str]]]):
        device_id (Union[Unset, list[int]]):
        device_id_n (Union[Unset, list[int]]):
        device_role (Union[Unset, list[str]]):
        device_role_n (Union[Unset, list[str]]):
        device_role_id (Union[Unset, list[int]]):
        device_role_id_n (Union[Unset, list[int]]):
        device_status (Union[Unset, list[str]]):
        device_status_empty (Union[Unset, bool]):
        device_status_ic (Union[Unset, list[str]]):
        device_status_ie (Union[Unset, list[str]]):
        device_status_iew (Union[Unset, list[str]]):
        device_status_isw (Union[Unset, list[str]]):
        device_status_n (Union[Unset, list[str]]):
        device_status_nic (Union[Unset, list[str]]):
        device_status_nie (Union[Unset, list[str]]):
        device_status_niew (Union[Unset, list[str]]):
        device_status_nisw (Union[Unset, list[str]]):
        device_type (Union[Unset, list[str]]):
        device_type_n (Union[Unset, list[str]]):
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
        duplex (Union[Unset, list[Union[None, str]]]):
        duplex_empty (Union[Unset, bool]):
        duplex_ic (Union[Unset, list[Union[None, str]]]):
        duplex_ie (Union[Unset, list[Union[None, str]]]):
        duplex_iew (Union[Unset, list[Union[None, str]]]):
        duplex_isw (Union[Unset, list[Union[None, str]]]):
        duplex_n (Union[Unset, list[Union[None, str]]]):
        duplex_nic (Union[Unset, list[Union[None, str]]]):
        duplex_nie (Union[Unset, list[Union[None, str]]]):
        duplex_niew (Union[Unset, list[Union[None, str]]]):
        duplex_nisw (Union[Unset, list[Union[None, str]]]):
        enabled (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        kind (Union[Unset, str]):
        l2vpn (Union[Unset, list[Union[None, int]]]):
        l2vpn_n (Union[Unset, list[Union[None, int]]]):
        l2vpn_id (Union[Unset, list[int]]):
        l2vpn_id_n (Union[Unset, list[int]]):
        label (Union[Unset, list[str]]):
        label_empty (Union[Unset, bool]):
        label_ic (Union[Unset, list[str]]):
        label_ie (Union[Unset, list[str]]):
        label_iew (Union[Unset, list[str]]):
        label_isw (Union[Unset, list[str]]):
        label_n (Union[Unset, list[str]]):
        label_nic (Union[Unset, list[str]]):
        label_nie (Union[Unset, list[str]]):
        label_niew (Union[Unset, list[str]]):
        label_nisw (Union[Unset, list[str]]):
        lag_id (Union[Unset, list[int]]):
        lag_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_id (Union[Unset, list[int]]):
        location_id_n (Union[Unset, list[int]]):
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
        mark_connected (Union[Unset, bool]):
        mgmt_only (Union[Unset, bool]):
        mode (Union[Unset, list[Union[None, str]]]):
        mode_empty (Union[Unset, bool]):
        mode_ic (Union[Unset, list[Union[None, str]]]):
        mode_ie (Union[Unset, list[Union[None, str]]]):
        mode_iew (Union[Unset, list[Union[None, str]]]):
        mode_isw (Union[Unset, list[Union[None, str]]]):
        mode_n (Union[Unset, list[Union[None, str]]]):
        mode_nic (Union[Unset, list[Union[None, str]]]):
        mode_nie (Union[Unset, list[Union[None, str]]]):
        mode_niew (Union[Unset, list[Union[None, str]]]):
        mode_nisw (Union[Unset, list[Union[None, str]]]):
        modified_by_request (Union[Unset, UUID]):
        module_id (Union[Unset, list[Union[None, int]]]):
        module_id_n (Union[Unset, list[Union[None, int]]]):
        mtu (Union[Unset, list[int]]):
        mtu_empty (Union[Unset, bool]):
        mtu_gt (Union[Unset, list[int]]):
        mtu_gte (Union[Unset, list[int]]):
        mtu_lt (Union[Unset, list[int]]):
        mtu_lte (Union[Unset, list[int]]):
        mtu_n (Union[Unset, list[int]]):
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
        occupied (Union[Unset, bool]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        parent_id (Union[Unset, list[int]]):
        parent_id_n (Union[Unset, list[int]]):
        poe_mode (Union[Unset, list[Union[None, str]]]):
        poe_mode_empty (Union[Unset, bool]):
        poe_mode_ic (Union[Unset, list[Union[None, str]]]):
        poe_mode_ie (Union[Unset, list[Union[None, str]]]):
        poe_mode_iew (Union[Unset, list[Union[None, str]]]):
        poe_mode_isw (Union[Unset, list[Union[None, str]]]):
        poe_mode_n (Union[Unset, list[Union[None, str]]]):
        poe_mode_nic (Union[Unset, list[Union[None, str]]]):
        poe_mode_nie (Union[Unset, list[Union[None, str]]]):
        poe_mode_niew (Union[Unset, list[Union[None, str]]]):
        poe_mode_nisw (Union[Unset, list[Union[None, str]]]):
        poe_type (Union[Unset, list[Union[None, str]]]):
        poe_type_empty (Union[Unset, bool]):
        poe_type_ic (Union[Unset, list[Union[None, str]]]):
        poe_type_ie (Union[Unset, list[Union[None, str]]]):
        poe_type_iew (Union[Unset, list[Union[None, str]]]):
        poe_type_isw (Union[Unset, list[Union[None, str]]]):
        poe_type_n (Union[Unset, list[Union[None, str]]]):
        poe_type_nic (Union[Unset, list[Union[None, str]]]):
        poe_type_nie (Union[Unset, list[Union[None, str]]]):
        poe_type_niew (Union[Unset, list[Union[None, str]]]):
        poe_type_nisw (Union[Unset, list[Union[None, str]]]):
        primary_mac_address (Union[Unset, list[str]]):
        primary_mac_address_n (Union[Unset, list[str]]):
        primary_mac_address_id (Union[Unset, list[int]]):
        primary_mac_address_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_n (Union[Unset, list[str]]):
        rack_id (Union[Unset, list[int]]):
        rack_id_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        rf_channel (Union[Unset, list[Union[None, str]]]):
        rf_channel_empty (Union[Unset, bool]):
        rf_channel_ic (Union[Unset, list[Union[None, str]]]):
        rf_channel_ie (Union[Unset, list[Union[None, str]]]):
        rf_channel_iew (Union[Unset, list[Union[None, str]]]):
        rf_channel_isw (Union[Unset, list[Union[None, str]]]):
        rf_channel_n (Union[Unset, list[Union[None, str]]]):
        rf_channel_nic (Union[Unset, list[Union[None, str]]]):
        rf_channel_nie (Union[Unset, list[Union[None, str]]]):
        rf_channel_niew (Union[Unset, list[Union[None, str]]]):
        rf_channel_nisw (Union[Unset, list[Union[None, str]]]):
        rf_channel_frequency (Union[Unset, list[float]]):
        rf_channel_frequency_empty (Union[Unset, bool]):
        rf_channel_frequency_gt (Union[Unset, list[float]]):
        rf_channel_frequency_gte (Union[Unset, list[float]]):
        rf_channel_frequency_lt (Union[Unset, list[float]]):
        rf_channel_frequency_lte (Union[Unset, list[float]]):
        rf_channel_frequency_n (Union[Unset, list[float]]):
        rf_channel_width (Union[Unset, list[float]]):
        rf_channel_width_empty (Union[Unset, bool]):
        rf_channel_width_gt (Union[Unset, list[float]]):
        rf_channel_width_gte (Union[Unset, list[float]]):
        rf_channel_width_lt (Union[Unset, list[float]]):
        rf_channel_width_lte (Union[Unset, list[float]]):
        rf_channel_width_n (Union[Unset, list[float]]):
        rf_role (Union[Unset, list[Union[None, str]]]):
        rf_role_empty (Union[Unset, bool]):
        rf_role_ic (Union[Unset, list[Union[None, str]]]):
        rf_role_ie (Union[Unset, list[Union[None, str]]]):
        rf_role_iew (Union[Unset, list[Union[None, str]]]):
        rf_role_isw (Union[Unset, list[Union[None, str]]]):
        rf_role_n (Union[Unset, list[Union[None, str]]]):
        rf_role_nic (Union[Unset, list[Union[None, str]]]):
        rf_role_nie (Union[Unset, list[Union[None, str]]]):
        rf_role_niew (Union[Unset, list[Union[None, str]]]):
        rf_role_nisw (Union[Unset, list[Union[None, str]]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
        speed (Union[Unset, list[int]]):
        speed_empty (Union[Unset, list[int]]):
        speed_gt (Union[Unset, list[int]]):
        speed_gte (Union[Unset, list[int]]):
        speed_lt (Union[Unset, list[int]]):
        speed_lte (Union[Unset, list[int]]):
        speed_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        tx_power (Union[Unset, list[int]]):
        tx_power_empty (Union[Unset, bool]):
        tx_power_gt (Union[Unset, list[int]]):
        tx_power_gte (Union[Unset, list[int]]):
        tx_power_lt (Union[Unset, list[int]]):
        tx_power_lte (Union[Unset, list[int]]):
        tx_power_n (Union[Unset, list[int]]):
        type_ (Union[Unset, list[str]]):
        type_empty (Union[Unset, bool]):
        type_ic (Union[Unset, list[str]]):
        type_ie (Union[Unset, list[str]]):
        type_iew (Union[Unset, list[str]]):
        type_isw (Union[Unset, list[str]]):
        type_n (Union[Unset, list[str]]):
        type_nic (Union[Unset, list[str]]):
        type_nie (Union[Unset, list[str]]):
        type_niew (Union[Unset, list[str]]):
        type_nisw (Union[Unset, list[str]]):
        updated_by_request (Union[Unset, UUID]):
        vdc (Union[Unset, list[str]]):
        vdc_n (Union[Unset, list[str]]):
        vdc_id (Union[Unset, list[int]]):
        vdc_id_n (Union[Unset, list[int]]):
        vdc_identifier (Union[Unset, list[Union[None, int]]]):
        vdc_identifier_n (Union[Unset, list[Union[None, int]]]):
        virtual_chassis (Union[Unset, list[str]]):
        virtual_chassis_n (Union[Unset, list[str]]):
        virtual_chassis_id (Union[Unset, list[int]]):
        virtual_chassis_id_n (Union[Unset, list[int]]):
        virtual_chassis_member (Union[Unset, list[str]]):
        virtual_chassis_member_id (Union[Unset, list[int]]):
        virtual_circuit_id (Union[Unset, list[int]]):
        virtual_circuit_id_n (Union[Unset, list[int]]):
        virtual_circuit_termination_id (Union[Unset, list[int]]):
        virtual_circuit_termination_id_n (Union[Unset, list[int]]):
        vlan (Union[Unset, str]):
        vlan_id (Union[Unset, str]):
        vlan_translation_policy (Union[Unset, list[str]]):
        vlan_translation_policy_n (Union[Unset, list[str]]):
        vlan_translation_policy_id (Union[Unset, list[int]]):
        vlan_translation_policy_id_n (Union[Unset, list[int]]):
        vrf (Union[Unset, list[Union[None, str]]]):
        vrf_n (Union[Unset, list[Union[None, str]]]):
        vrf_id (Union[Unset, list[int]]):
        vrf_id_n (Union[Unset, list[int]]):
        wireless_lan_id (Union[Unset, list[int]]):
        wireless_lan_id_n (Union[Unset, list[int]]):
        wireless_link_id (Union[Unset, list[Union[None, int]]]):
        wireless_link_id_n (Union[Unset, list[Union[None, int]]]):
        wwn (Union[Unset, list[str]]):
        wwn_ic (Union[Unset, list[str]]):
        wwn_ie (Union[Unset, list[str]]):
        wwn_iew (Union[Unset, list[str]]):
        wwn_isw (Union[Unset, list[str]]):
        wwn_n (Union[Unset, list[str]]):
        wwn_nic (Union[Unset, list[str]]):
        wwn_nie (Union[Unset, list[str]]):
        wwn_niew (Union[Unset, list[str]]):
        wwn_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedInterfaceList]
    """

    kwargs = _get_kwargs(
        bridge_id=bridge_id,
        bridge_id_n=bridge_id_n,
        cable_end=cable_end,
        cable_id=cable_id,
        cable_id_n=cable_id_n,
        cabled=cabled,
        connected=connected,
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
        device=device,
        device_n=device_n,
        device_id=device_id,
        device_id_n=device_id_n,
        device_role=device_role,
        device_role_n=device_role_n,
        device_role_id=device_role_id,
        device_role_id_n=device_role_id_n,
        device_status=device_status,
        device_status_empty=device_status_empty,
        device_status_ic=device_status_ic,
        device_status_ie=device_status_ie,
        device_status_iew=device_status_iew,
        device_status_isw=device_status_isw,
        device_status_n=device_status_n,
        device_status_nic=device_status_nic,
        device_status_nie=device_status_nie,
        device_status_niew=device_status_niew,
        device_status_nisw=device_status_nisw,
        device_type=device_type,
        device_type_n=device_type_n,
        device_type_id=device_type_id,
        device_type_id_n=device_type_id_n,
        duplex=duplex,
        duplex_empty=duplex_empty,
        duplex_ic=duplex_ic,
        duplex_ie=duplex_ie,
        duplex_iew=duplex_iew,
        duplex_isw=duplex_isw,
        duplex_n=duplex_n,
        duplex_nic=duplex_nic,
        duplex_nie=duplex_nie,
        duplex_niew=duplex_niew,
        duplex_nisw=duplex_nisw,
        enabled=enabled,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        kind=kind,
        l2vpn=l2vpn,
        l2vpn_n=l2vpn_n,
        l2vpn_id=l2vpn_id,
        l2vpn_id_n=l2vpn_id_n,
        label=label,
        label_empty=label_empty,
        label_ic=label_ic,
        label_ie=label_ie,
        label_iew=label_iew,
        label_isw=label_isw,
        label_n=label_n,
        label_nic=label_nic,
        label_nie=label_nie,
        label_niew=label_niew,
        label_nisw=label_nisw,
        lag_id=lag_id,
        lag_id_n=lag_id_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        location=location,
        location_n=location_n,
        location_id=location_id,
        location_id_n=location_id_n,
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
        mark_connected=mark_connected,
        mgmt_only=mgmt_only,
        mode=mode,
        mode_empty=mode_empty,
        mode_ic=mode_ic,
        mode_ie=mode_ie,
        mode_iew=mode_iew,
        mode_isw=mode_isw,
        mode_n=mode_n,
        mode_nic=mode_nic,
        mode_nie=mode_nie,
        mode_niew=mode_niew,
        mode_nisw=mode_nisw,
        modified_by_request=modified_by_request,
        module_id=module_id,
        module_id_n=module_id_n,
        mtu=mtu,
        mtu_empty=mtu_empty,
        mtu_gt=mtu_gt,
        mtu_gte=mtu_gte,
        mtu_lt=mtu_lt,
        mtu_lte=mtu_lte,
        mtu_n=mtu_n,
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
        occupied=occupied,
        offset=offset,
        ordering=ordering,
        parent_id=parent_id,
        parent_id_n=parent_id_n,
        poe_mode=poe_mode,
        poe_mode_empty=poe_mode_empty,
        poe_mode_ic=poe_mode_ic,
        poe_mode_ie=poe_mode_ie,
        poe_mode_iew=poe_mode_iew,
        poe_mode_isw=poe_mode_isw,
        poe_mode_n=poe_mode_n,
        poe_mode_nic=poe_mode_nic,
        poe_mode_nie=poe_mode_nie,
        poe_mode_niew=poe_mode_niew,
        poe_mode_nisw=poe_mode_nisw,
        poe_type=poe_type,
        poe_type_empty=poe_type_empty,
        poe_type_ic=poe_type_ic,
        poe_type_ie=poe_type_ie,
        poe_type_iew=poe_type_iew,
        poe_type_isw=poe_type_isw,
        poe_type_n=poe_type_n,
        poe_type_nic=poe_type_nic,
        poe_type_nie=poe_type_nie,
        poe_type_niew=poe_type_niew,
        poe_type_nisw=poe_type_nisw,
        primary_mac_address=primary_mac_address,
        primary_mac_address_n=primary_mac_address_n,
        primary_mac_address_id=primary_mac_address_id,
        primary_mac_address_id_n=primary_mac_address_id_n,
        q=q,
        rack=rack,
        rack_n=rack_n,
        rack_id=rack_id,
        rack_id_n=rack_id_n,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        rf_channel=rf_channel,
        rf_channel_empty=rf_channel_empty,
        rf_channel_ic=rf_channel_ic,
        rf_channel_ie=rf_channel_ie,
        rf_channel_iew=rf_channel_iew,
        rf_channel_isw=rf_channel_isw,
        rf_channel_n=rf_channel_n,
        rf_channel_nic=rf_channel_nic,
        rf_channel_nie=rf_channel_nie,
        rf_channel_niew=rf_channel_niew,
        rf_channel_nisw=rf_channel_nisw,
        rf_channel_frequency=rf_channel_frequency,
        rf_channel_frequency_empty=rf_channel_frequency_empty,
        rf_channel_frequency_gt=rf_channel_frequency_gt,
        rf_channel_frequency_gte=rf_channel_frequency_gte,
        rf_channel_frequency_lt=rf_channel_frequency_lt,
        rf_channel_frequency_lte=rf_channel_frequency_lte,
        rf_channel_frequency_n=rf_channel_frequency_n,
        rf_channel_width=rf_channel_width,
        rf_channel_width_empty=rf_channel_width_empty,
        rf_channel_width_gt=rf_channel_width_gt,
        rf_channel_width_gte=rf_channel_width_gte,
        rf_channel_width_lt=rf_channel_width_lt,
        rf_channel_width_lte=rf_channel_width_lte,
        rf_channel_width_n=rf_channel_width_n,
        rf_role=rf_role,
        rf_role_empty=rf_role_empty,
        rf_role_ic=rf_role_ic,
        rf_role_ie=rf_role_ie,
        rf_role_iew=rf_role_iew,
        rf_role_isw=rf_role_isw,
        rf_role_n=rf_role_n,
        rf_role_nic=rf_role_nic,
        rf_role_nie=rf_role_nie,
        rf_role_niew=rf_role_niew,
        rf_role_nisw=rf_role_nisw,
        site=site,
        site_n=site_n,
        site_group=site_group,
        site_group_n=site_group_n,
        site_group_id=site_group_id,
        site_group_id_n=site_group_id_n,
        site_id=site_id,
        site_id_n=site_id_n,
        speed=speed,
        speed_empty=speed_empty,
        speed_gt=speed_gt,
        speed_gte=speed_gte,
        speed_lt=speed_lt,
        speed_lte=speed_lte,
        speed_n=speed_n,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        tx_power=tx_power,
        tx_power_empty=tx_power_empty,
        tx_power_gt=tx_power_gt,
        tx_power_gte=tx_power_gte,
        tx_power_lt=tx_power_lt,
        tx_power_lte=tx_power_lte,
        tx_power_n=tx_power_n,
        type_=type_,
        type_empty=type_empty,
        type_ic=type_ic,
        type_ie=type_ie,
        type_iew=type_iew,
        type_isw=type_isw,
        type_n=type_n,
        type_nic=type_nic,
        type_nie=type_nie,
        type_niew=type_niew,
        type_nisw=type_nisw,
        updated_by_request=updated_by_request,
        vdc=vdc,
        vdc_n=vdc_n,
        vdc_id=vdc_id,
        vdc_id_n=vdc_id_n,
        vdc_identifier=vdc_identifier,
        vdc_identifier_n=vdc_identifier_n,
        virtual_chassis=virtual_chassis,
        virtual_chassis_n=virtual_chassis_n,
        virtual_chassis_id=virtual_chassis_id,
        virtual_chassis_id_n=virtual_chassis_id_n,
        virtual_chassis_member=virtual_chassis_member,
        virtual_chassis_member_id=virtual_chassis_member_id,
        virtual_circuit_id=virtual_circuit_id,
        virtual_circuit_id_n=virtual_circuit_id_n,
        virtual_circuit_termination_id=virtual_circuit_termination_id,
        virtual_circuit_termination_id_n=virtual_circuit_termination_id_n,
        vlan=vlan,
        vlan_id=vlan_id,
        vlan_translation_policy=vlan_translation_policy,
        vlan_translation_policy_n=vlan_translation_policy_n,
        vlan_translation_policy_id=vlan_translation_policy_id,
        vlan_translation_policy_id_n=vlan_translation_policy_id_n,
        vrf=vrf,
        vrf_n=vrf_n,
        vrf_id=vrf_id,
        vrf_id_n=vrf_id_n,
        wireless_lan_id=wireless_lan_id,
        wireless_lan_id_n=wireless_lan_id_n,
        wireless_link_id=wireless_link_id,
        wireless_link_id_n=wireless_link_id_n,
        wwn=wwn,
        wwn_ic=wwn_ic,
        wwn_ie=wwn_ie,
        wwn_iew=wwn_iew,
        wwn_isw=wwn_isw,
        wwn_n=wwn_n,
        wwn_nic=wwn_nic,
        wwn_nie=wwn_nie,
        wwn_niew=wwn_niew,
        wwn_nisw=wwn_nisw,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    bridge_id: Union[Unset, list[int]] = UNSET,
    bridge_id_n: Union[Unset, list[int]] = UNSET,
    cable_end: Union[Unset, DcimInterfacesListCableEnd] = UNSET,
    cable_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cable_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cabled: Union[Unset, bool] = UNSET,
    connected: Union[Unset, bool] = UNSET,
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
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    device_id_n: Union[Unset, list[int]] = UNSET,
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_id: Union[Unset, list[int]] = UNSET,
    device_role_id_n: Union[Unset, list[int]] = UNSET,
    device_status: Union[Unset, list[str]] = UNSET,
    device_status_empty: Union[Unset, bool] = UNSET,
    device_status_ic: Union[Unset, list[str]] = UNSET,
    device_status_ie: Union[Unset, list[str]] = UNSET,
    device_status_iew: Union[Unset, list[str]] = UNSET,
    device_status_isw: Union[Unset, list[str]] = UNSET,
    device_status_n: Union[Unset, list[str]] = UNSET,
    device_status_nic: Union[Unset, list[str]] = UNSET,
    device_status_nie: Union[Unset, list[str]] = UNSET,
    device_status_niew: Union[Unset, list[str]] = UNSET,
    device_status_nisw: Union[Unset, list[str]] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    duplex: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_empty: Union[Unset, bool] = UNSET,
    duplex_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_n: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    kind: Union[Unset, str] = UNSET,
    l2vpn: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_n: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_id: Union[Unset, list[int]] = UNSET,
    l2vpn_id_n: Union[Unset, list[int]] = UNSET,
    label: Union[Unset, list[str]] = UNSET,
    label_empty: Union[Unset, bool] = UNSET,
    label_ic: Union[Unset, list[str]] = UNSET,
    label_ie: Union[Unset, list[str]] = UNSET,
    label_iew: Union[Unset, list[str]] = UNSET,
    label_isw: Union[Unset, list[str]] = UNSET,
    label_n: Union[Unset, list[str]] = UNSET,
    label_nic: Union[Unset, list[str]] = UNSET,
    label_nie: Union[Unset, list[str]] = UNSET,
    label_niew: Union[Unset, list[str]] = UNSET,
    label_nisw: Union[Unset, list[str]] = UNSET,
    lag_id: Union[Unset, list[int]] = UNSET,
    lag_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
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
    mark_connected: Union[Unset, bool] = UNSET,
    mgmt_only: Union[Unset, bool] = UNSET,
    mode: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_empty: Union[Unset, bool] = UNSET,
    mode_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_n: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_id: Union[Unset, list[Union[None, int]]] = UNSET,
    module_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    mtu: Union[Unset, list[int]] = UNSET,
    mtu_empty: Union[Unset, bool] = UNSET,
    mtu_gt: Union[Unset, list[int]] = UNSET,
    mtu_gte: Union[Unset, list[int]] = UNSET,
    mtu_lt: Union[Unset, list[int]] = UNSET,
    mtu_lte: Union[Unset, list[int]] = UNSET,
    mtu_n: Union[Unset, list[int]] = UNSET,
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
    occupied: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, list[int]] = UNSET,
    parent_id_n: Union[Unset, list[int]] = UNSET,
    poe_mode: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_empty: Union[Unset, bool] = UNSET,
    poe_mode_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_n: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_empty: Union[Unset, bool] = UNSET,
    poe_type_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_n: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    primary_mac_address: Union[Unset, list[str]] = UNSET,
    primary_mac_address_n: Union[Unset, list[str]] = UNSET,
    primary_mac_address_id: Union[Unset, list[int]] = UNSET,
    primary_mac_address_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    rf_channel: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_empty: Union[Unset, bool] = UNSET,
    rf_channel_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_n: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_frequency: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_empty: Union[Unset, bool] = UNSET,
    rf_channel_frequency_gt: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_gte: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_lt: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_lte: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_n: Union[Unset, list[float]] = UNSET,
    rf_channel_width: Union[Unset, list[float]] = UNSET,
    rf_channel_width_empty: Union[Unset, bool] = UNSET,
    rf_channel_width_gt: Union[Unset, list[float]] = UNSET,
    rf_channel_width_gte: Union[Unset, list[float]] = UNSET,
    rf_channel_width_lt: Union[Unset, list[float]] = UNSET,
    rf_channel_width_lte: Union[Unset, list[float]] = UNSET,
    rf_channel_width_n: Union[Unset, list[float]] = UNSET,
    rf_role: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_empty: Union[Unset, bool] = UNSET,
    rf_role_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_n: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    speed: Union[Unset, list[int]] = UNSET,
    speed_empty: Union[Unset, list[int]] = UNSET,
    speed_gt: Union[Unset, list[int]] = UNSET,
    speed_gte: Union[Unset, list[int]] = UNSET,
    speed_lt: Union[Unset, list[int]] = UNSET,
    speed_lte: Union[Unset, list[int]] = UNSET,
    speed_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tx_power: Union[Unset, list[int]] = UNSET,
    tx_power_empty: Union[Unset, bool] = UNSET,
    tx_power_gt: Union[Unset, list[int]] = UNSET,
    tx_power_gte: Union[Unset, list[int]] = UNSET,
    tx_power_lt: Union[Unset, list[int]] = UNSET,
    tx_power_lte: Union[Unset, list[int]] = UNSET,
    tx_power_n: Union[Unset, list[int]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    type_empty: Union[Unset, bool] = UNSET,
    type_ic: Union[Unset, list[str]] = UNSET,
    type_ie: Union[Unset, list[str]] = UNSET,
    type_iew: Union[Unset, list[str]] = UNSET,
    type_isw: Union[Unset, list[str]] = UNSET,
    type_n: Union[Unset, list[str]] = UNSET,
    type_nic: Union[Unset, list[str]] = UNSET,
    type_nie: Union[Unset, list[str]] = UNSET,
    type_niew: Union[Unset, list[str]] = UNSET,
    type_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    vdc: Union[Unset, list[str]] = UNSET,
    vdc_n: Union[Unset, list[str]] = UNSET,
    vdc_id: Union[Unset, list[int]] = UNSET,
    vdc_id_n: Union[Unset, list[int]] = UNSET,
    vdc_identifier: Union[Unset, list[Union[None, int]]] = UNSET,
    vdc_identifier_n: Union[Unset, list[Union[None, int]]] = UNSET,
    virtual_chassis: Union[Unset, list[str]] = UNSET,
    virtual_chassis_n: Union[Unset, list[str]] = UNSET,
    virtual_chassis_id: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id_n: Union[Unset, list[int]] = UNSET,
    virtual_chassis_member: Union[Unset, list[str]] = UNSET,
    virtual_chassis_member_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_id_n: Union[Unset, list[int]] = UNSET,
    virtual_circuit_termination_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_termination_id_n: Union[Unset, list[int]] = UNSET,
    vlan: Union[Unset, str] = UNSET,
    vlan_id: Union[Unset, str] = UNSET,
    vlan_translation_policy: Union[Unset, list[str]] = UNSET,
    vlan_translation_policy_n: Union[Unset, list[str]] = UNSET,
    vlan_translation_policy_id: Union[Unset, list[int]] = UNSET,
    vlan_translation_policy_id_n: Union[Unset, list[int]] = UNSET,
    vrf: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_n: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_id: Union[Unset, list[int]] = UNSET,
    vrf_id_n: Union[Unset, list[int]] = UNSET,
    wireless_lan_id: Union[Unset, list[int]] = UNSET,
    wireless_lan_id_n: Union[Unset, list[int]] = UNSET,
    wireless_link_id: Union[Unset, list[Union[None, int]]] = UNSET,
    wireless_link_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    wwn: Union[Unset, list[str]] = UNSET,
    wwn_ic: Union[Unset, list[str]] = UNSET,
    wwn_ie: Union[Unset, list[str]] = UNSET,
    wwn_iew: Union[Unset, list[str]] = UNSET,
    wwn_isw: Union[Unset, list[str]] = UNSET,
    wwn_n: Union[Unset, list[str]] = UNSET,
    wwn_nic: Union[Unset, list[str]] = UNSET,
    wwn_nie: Union[Unset, list[str]] = UNSET,
    wwn_niew: Union[Unset, list[str]] = UNSET,
    wwn_nisw: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedInterfaceList]:
    """Get a list of interface objects.

    Args:
        bridge_id (Union[Unset, list[int]]):
        bridge_id_n (Union[Unset, list[int]]):
        cable_end (Union[Unset, DcimInterfacesListCableEnd]):
        cable_id (Union[Unset, list[Union[None, int]]]):
        cable_id_n (Union[Unset, list[Union[None, int]]]):
        cabled (Union[Unset, bool]):
        connected (Union[Unset, bool]):
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
        device (Union[Unset, list[Union[None, str]]]):
        device_n (Union[Unset, list[Union[None, str]]]):
        device_id (Union[Unset, list[int]]):
        device_id_n (Union[Unset, list[int]]):
        device_role (Union[Unset, list[str]]):
        device_role_n (Union[Unset, list[str]]):
        device_role_id (Union[Unset, list[int]]):
        device_role_id_n (Union[Unset, list[int]]):
        device_status (Union[Unset, list[str]]):
        device_status_empty (Union[Unset, bool]):
        device_status_ic (Union[Unset, list[str]]):
        device_status_ie (Union[Unset, list[str]]):
        device_status_iew (Union[Unset, list[str]]):
        device_status_isw (Union[Unset, list[str]]):
        device_status_n (Union[Unset, list[str]]):
        device_status_nic (Union[Unset, list[str]]):
        device_status_nie (Union[Unset, list[str]]):
        device_status_niew (Union[Unset, list[str]]):
        device_status_nisw (Union[Unset, list[str]]):
        device_type (Union[Unset, list[str]]):
        device_type_n (Union[Unset, list[str]]):
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
        duplex (Union[Unset, list[Union[None, str]]]):
        duplex_empty (Union[Unset, bool]):
        duplex_ic (Union[Unset, list[Union[None, str]]]):
        duplex_ie (Union[Unset, list[Union[None, str]]]):
        duplex_iew (Union[Unset, list[Union[None, str]]]):
        duplex_isw (Union[Unset, list[Union[None, str]]]):
        duplex_n (Union[Unset, list[Union[None, str]]]):
        duplex_nic (Union[Unset, list[Union[None, str]]]):
        duplex_nie (Union[Unset, list[Union[None, str]]]):
        duplex_niew (Union[Unset, list[Union[None, str]]]):
        duplex_nisw (Union[Unset, list[Union[None, str]]]):
        enabled (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        kind (Union[Unset, str]):
        l2vpn (Union[Unset, list[Union[None, int]]]):
        l2vpn_n (Union[Unset, list[Union[None, int]]]):
        l2vpn_id (Union[Unset, list[int]]):
        l2vpn_id_n (Union[Unset, list[int]]):
        label (Union[Unset, list[str]]):
        label_empty (Union[Unset, bool]):
        label_ic (Union[Unset, list[str]]):
        label_ie (Union[Unset, list[str]]):
        label_iew (Union[Unset, list[str]]):
        label_isw (Union[Unset, list[str]]):
        label_n (Union[Unset, list[str]]):
        label_nic (Union[Unset, list[str]]):
        label_nie (Union[Unset, list[str]]):
        label_niew (Union[Unset, list[str]]):
        label_nisw (Union[Unset, list[str]]):
        lag_id (Union[Unset, list[int]]):
        lag_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_id (Union[Unset, list[int]]):
        location_id_n (Union[Unset, list[int]]):
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
        mark_connected (Union[Unset, bool]):
        mgmt_only (Union[Unset, bool]):
        mode (Union[Unset, list[Union[None, str]]]):
        mode_empty (Union[Unset, bool]):
        mode_ic (Union[Unset, list[Union[None, str]]]):
        mode_ie (Union[Unset, list[Union[None, str]]]):
        mode_iew (Union[Unset, list[Union[None, str]]]):
        mode_isw (Union[Unset, list[Union[None, str]]]):
        mode_n (Union[Unset, list[Union[None, str]]]):
        mode_nic (Union[Unset, list[Union[None, str]]]):
        mode_nie (Union[Unset, list[Union[None, str]]]):
        mode_niew (Union[Unset, list[Union[None, str]]]):
        mode_nisw (Union[Unset, list[Union[None, str]]]):
        modified_by_request (Union[Unset, UUID]):
        module_id (Union[Unset, list[Union[None, int]]]):
        module_id_n (Union[Unset, list[Union[None, int]]]):
        mtu (Union[Unset, list[int]]):
        mtu_empty (Union[Unset, bool]):
        mtu_gt (Union[Unset, list[int]]):
        mtu_gte (Union[Unset, list[int]]):
        mtu_lt (Union[Unset, list[int]]):
        mtu_lte (Union[Unset, list[int]]):
        mtu_n (Union[Unset, list[int]]):
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
        occupied (Union[Unset, bool]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        parent_id (Union[Unset, list[int]]):
        parent_id_n (Union[Unset, list[int]]):
        poe_mode (Union[Unset, list[Union[None, str]]]):
        poe_mode_empty (Union[Unset, bool]):
        poe_mode_ic (Union[Unset, list[Union[None, str]]]):
        poe_mode_ie (Union[Unset, list[Union[None, str]]]):
        poe_mode_iew (Union[Unset, list[Union[None, str]]]):
        poe_mode_isw (Union[Unset, list[Union[None, str]]]):
        poe_mode_n (Union[Unset, list[Union[None, str]]]):
        poe_mode_nic (Union[Unset, list[Union[None, str]]]):
        poe_mode_nie (Union[Unset, list[Union[None, str]]]):
        poe_mode_niew (Union[Unset, list[Union[None, str]]]):
        poe_mode_nisw (Union[Unset, list[Union[None, str]]]):
        poe_type (Union[Unset, list[Union[None, str]]]):
        poe_type_empty (Union[Unset, bool]):
        poe_type_ic (Union[Unset, list[Union[None, str]]]):
        poe_type_ie (Union[Unset, list[Union[None, str]]]):
        poe_type_iew (Union[Unset, list[Union[None, str]]]):
        poe_type_isw (Union[Unset, list[Union[None, str]]]):
        poe_type_n (Union[Unset, list[Union[None, str]]]):
        poe_type_nic (Union[Unset, list[Union[None, str]]]):
        poe_type_nie (Union[Unset, list[Union[None, str]]]):
        poe_type_niew (Union[Unset, list[Union[None, str]]]):
        poe_type_nisw (Union[Unset, list[Union[None, str]]]):
        primary_mac_address (Union[Unset, list[str]]):
        primary_mac_address_n (Union[Unset, list[str]]):
        primary_mac_address_id (Union[Unset, list[int]]):
        primary_mac_address_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_n (Union[Unset, list[str]]):
        rack_id (Union[Unset, list[int]]):
        rack_id_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        rf_channel (Union[Unset, list[Union[None, str]]]):
        rf_channel_empty (Union[Unset, bool]):
        rf_channel_ic (Union[Unset, list[Union[None, str]]]):
        rf_channel_ie (Union[Unset, list[Union[None, str]]]):
        rf_channel_iew (Union[Unset, list[Union[None, str]]]):
        rf_channel_isw (Union[Unset, list[Union[None, str]]]):
        rf_channel_n (Union[Unset, list[Union[None, str]]]):
        rf_channel_nic (Union[Unset, list[Union[None, str]]]):
        rf_channel_nie (Union[Unset, list[Union[None, str]]]):
        rf_channel_niew (Union[Unset, list[Union[None, str]]]):
        rf_channel_nisw (Union[Unset, list[Union[None, str]]]):
        rf_channel_frequency (Union[Unset, list[float]]):
        rf_channel_frequency_empty (Union[Unset, bool]):
        rf_channel_frequency_gt (Union[Unset, list[float]]):
        rf_channel_frequency_gte (Union[Unset, list[float]]):
        rf_channel_frequency_lt (Union[Unset, list[float]]):
        rf_channel_frequency_lte (Union[Unset, list[float]]):
        rf_channel_frequency_n (Union[Unset, list[float]]):
        rf_channel_width (Union[Unset, list[float]]):
        rf_channel_width_empty (Union[Unset, bool]):
        rf_channel_width_gt (Union[Unset, list[float]]):
        rf_channel_width_gte (Union[Unset, list[float]]):
        rf_channel_width_lt (Union[Unset, list[float]]):
        rf_channel_width_lte (Union[Unset, list[float]]):
        rf_channel_width_n (Union[Unset, list[float]]):
        rf_role (Union[Unset, list[Union[None, str]]]):
        rf_role_empty (Union[Unset, bool]):
        rf_role_ic (Union[Unset, list[Union[None, str]]]):
        rf_role_ie (Union[Unset, list[Union[None, str]]]):
        rf_role_iew (Union[Unset, list[Union[None, str]]]):
        rf_role_isw (Union[Unset, list[Union[None, str]]]):
        rf_role_n (Union[Unset, list[Union[None, str]]]):
        rf_role_nic (Union[Unset, list[Union[None, str]]]):
        rf_role_nie (Union[Unset, list[Union[None, str]]]):
        rf_role_niew (Union[Unset, list[Union[None, str]]]):
        rf_role_nisw (Union[Unset, list[Union[None, str]]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
        speed (Union[Unset, list[int]]):
        speed_empty (Union[Unset, list[int]]):
        speed_gt (Union[Unset, list[int]]):
        speed_gte (Union[Unset, list[int]]):
        speed_lt (Union[Unset, list[int]]):
        speed_lte (Union[Unset, list[int]]):
        speed_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        tx_power (Union[Unset, list[int]]):
        tx_power_empty (Union[Unset, bool]):
        tx_power_gt (Union[Unset, list[int]]):
        tx_power_gte (Union[Unset, list[int]]):
        tx_power_lt (Union[Unset, list[int]]):
        tx_power_lte (Union[Unset, list[int]]):
        tx_power_n (Union[Unset, list[int]]):
        type_ (Union[Unset, list[str]]):
        type_empty (Union[Unset, bool]):
        type_ic (Union[Unset, list[str]]):
        type_ie (Union[Unset, list[str]]):
        type_iew (Union[Unset, list[str]]):
        type_isw (Union[Unset, list[str]]):
        type_n (Union[Unset, list[str]]):
        type_nic (Union[Unset, list[str]]):
        type_nie (Union[Unset, list[str]]):
        type_niew (Union[Unset, list[str]]):
        type_nisw (Union[Unset, list[str]]):
        updated_by_request (Union[Unset, UUID]):
        vdc (Union[Unset, list[str]]):
        vdc_n (Union[Unset, list[str]]):
        vdc_id (Union[Unset, list[int]]):
        vdc_id_n (Union[Unset, list[int]]):
        vdc_identifier (Union[Unset, list[Union[None, int]]]):
        vdc_identifier_n (Union[Unset, list[Union[None, int]]]):
        virtual_chassis (Union[Unset, list[str]]):
        virtual_chassis_n (Union[Unset, list[str]]):
        virtual_chassis_id (Union[Unset, list[int]]):
        virtual_chassis_id_n (Union[Unset, list[int]]):
        virtual_chassis_member (Union[Unset, list[str]]):
        virtual_chassis_member_id (Union[Unset, list[int]]):
        virtual_circuit_id (Union[Unset, list[int]]):
        virtual_circuit_id_n (Union[Unset, list[int]]):
        virtual_circuit_termination_id (Union[Unset, list[int]]):
        virtual_circuit_termination_id_n (Union[Unset, list[int]]):
        vlan (Union[Unset, str]):
        vlan_id (Union[Unset, str]):
        vlan_translation_policy (Union[Unset, list[str]]):
        vlan_translation_policy_n (Union[Unset, list[str]]):
        vlan_translation_policy_id (Union[Unset, list[int]]):
        vlan_translation_policy_id_n (Union[Unset, list[int]]):
        vrf (Union[Unset, list[Union[None, str]]]):
        vrf_n (Union[Unset, list[Union[None, str]]]):
        vrf_id (Union[Unset, list[int]]):
        vrf_id_n (Union[Unset, list[int]]):
        wireless_lan_id (Union[Unset, list[int]]):
        wireless_lan_id_n (Union[Unset, list[int]]):
        wireless_link_id (Union[Unset, list[Union[None, int]]]):
        wireless_link_id_n (Union[Unset, list[Union[None, int]]]):
        wwn (Union[Unset, list[str]]):
        wwn_ic (Union[Unset, list[str]]):
        wwn_ie (Union[Unset, list[str]]):
        wwn_iew (Union[Unset, list[str]]):
        wwn_isw (Union[Unset, list[str]]):
        wwn_n (Union[Unset, list[str]]):
        wwn_nic (Union[Unset, list[str]]):
        wwn_nie (Union[Unset, list[str]]):
        wwn_niew (Union[Unset, list[str]]):
        wwn_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedInterfaceList
    """

    return sync_detailed(
        client=client,
        bridge_id=bridge_id,
        bridge_id_n=bridge_id_n,
        cable_end=cable_end,
        cable_id=cable_id,
        cable_id_n=cable_id_n,
        cabled=cabled,
        connected=connected,
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
        device=device,
        device_n=device_n,
        device_id=device_id,
        device_id_n=device_id_n,
        device_role=device_role,
        device_role_n=device_role_n,
        device_role_id=device_role_id,
        device_role_id_n=device_role_id_n,
        device_status=device_status,
        device_status_empty=device_status_empty,
        device_status_ic=device_status_ic,
        device_status_ie=device_status_ie,
        device_status_iew=device_status_iew,
        device_status_isw=device_status_isw,
        device_status_n=device_status_n,
        device_status_nic=device_status_nic,
        device_status_nie=device_status_nie,
        device_status_niew=device_status_niew,
        device_status_nisw=device_status_nisw,
        device_type=device_type,
        device_type_n=device_type_n,
        device_type_id=device_type_id,
        device_type_id_n=device_type_id_n,
        duplex=duplex,
        duplex_empty=duplex_empty,
        duplex_ic=duplex_ic,
        duplex_ie=duplex_ie,
        duplex_iew=duplex_iew,
        duplex_isw=duplex_isw,
        duplex_n=duplex_n,
        duplex_nic=duplex_nic,
        duplex_nie=duplex_nie,
        duplex_niew=duplex_niew,
        duplex_nisw=duplex_nisw,
        enabled=enabled,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        kind=kind,
        l2vpn=l2vpn,
        l2vpn_n=l2vpn_n,
        l2vpn_id=l2vpn_id,
        l2vpn_id_n=l2vpn_id_n,
        label=label,
        label_empty=label_empty,
        label_ic=label_ic,
        label_ie=label_ie,
        label_iew=label_iew,
        label_isw=label_isw,
        label_n=label_n,
        label_nic=label_nic,
        label_nie=label_nie,
        label_niew=label_niew,
        label_nisw=label_nisw,
        lag_id=lag_id,
        lag_id_n=lag_id_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        location=location,
        location_n=location_n,
        location_id=location_id,
        location_id_n=location_id_n,
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
        mark_connected=mark_connected,
        mgmt_only=mgmt_only,
        mode=mode,
        mode_empty=mode_empty,
        mode_ic=mode_ic,
        mode_ie=mode_ie,
        mode_iew=mode_iew,
        mode_isw=mode_isw,
        mode_n=mode_n,
        mode_nic=mode_nic,
        mode_nie=mode_nie,
        mode_niew=mode_niew,
        mode_nisw=mode_nisw,
        modified_by_request=modified_by_request,
        module_id=module_id,
        module_id_n=module_id_n,
        mtu=mtu,
        mtu_empty=mtu_empty,
        mtu_gt=mtu_gt,
        mtu_gte=mtu_gte,
        mtu_lt=mtu_lt,
        mtu_lte=mtu_lte,
        mtu_n=mtu_n,
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
        occupied=occupied,
        offset=offset,
        ordering=ordering,
        parent_id=parent_id,
        parent_id_n=parent_id_n,
        poe_mode=poe_mode,
        poe_mode_empty=poe_mode_empty,
        poe_mode_ic=poe_mode_ic,
        poe_mode_ie=poe_mode_ie,
        poe_mode_iew=poe_mode_iew,
        poe_mode_isw=poe_mode_isw,
        poe_mode_n=poe_mode_n,
        poe_mode_nic=poe_mode_nic,
        poe_mode_nie=poe_mode_nie,
        poe_mode_niew=poe_mode_niew,
        poe_mode_nisw=poe_mode_nisw,
        poe_type=poe_type,
        poe_type_empty=poe_type_empty,
        poe_type_ic=poe_type_ic,
        poe_type_ie=poe_type_ie,
        poe_type_iew=poe_type_iew,
        poe_type_isw=poe_type_isw,
        poe_type_n=poe_type_n,
        poe_type_nic=poe_type_nic,
        poe_type_nie=poe_type_nie,
        poe_type_niew=poe_type_niew,
        poe_type_nisw=poe_type_nisw,
        primary_mac_address=primary_mac_address,
        primary_mac_address_n=primary_mac_address_n,
        primary_mac_address_id=primary_mac_address_id,
        primary_mac_address_id_n=primary_mac_address_id_n,
        q=q,
        rack=rack,
        rack_n=rack_n,
        rack_id=rack_id,
        rack_id_n=rack_id_n,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        rf_channel=rf_channel,
        rf_channel_empty=rf_channel_empty,
        rf_channel_ic=rf_channel_ic,
        rf_channel_ie=rf_channel_ie,
        rf_channel_iew=rf_channel_iew,
        rf_channel_isw=rf_channel_isw,
        rf_channel_n=rf_channel_n,
        rf_channel_nic=rf_channel_nic,
        rf_channel_nie=rf_channel_nie,
        rf_channel_niew=rf_channel_niew,
        rf_channel_nisw=rf_channel_nisw,
        rf_channel_frequency=rf_channel_frequency,
        rf_channel_frequency_empty=rf_channel_frequency_empty,
        rf_channel_frequency_gt=rf_channel_frequency_gt,
        rf_channel_frequency_gte=rf_channel_frequency_gte,
        rf_channel_frequency_lt=rf_channel_frequency_lt,
        rf_channel_frequency_lte=rf_channel_frequency_lte,
        rf_channel_frequency_n=rf_channel_frequency_n,
        rf_channel_width=rf_channel_width,
        rf_channel_width_empty=rf_channel_width_empty,
        rf_channel_width_gt=rf_channel_width_gt,
        rf_channel_width_gte=rf_channel_width_gte,
        rf_channel_width_lt=rf_channel_width_lt,
        rf_channel_width_lte=rf_channel_width_lte,
        rf_channel_width_n=rf_channel_width_n,
        rf_role=rf_role,
        rf_role_empty=rf_role_empty,
        rf_role_ic=rf_role_ic,
        rf_role_ie=rf_role_ie,
        rf_role_iew=rf_role_iew,
        rf_role_isw=rf_role_isw,
        rf_role_n=rf_role_n,
        rf_role_nic=rf_role_nic,
        rf_role_nie=rf_role_nie,
        rf_role_niew=rf_role_niew,
        rf_role_nisw=rf_role_nisw,
        site=site,
        site_n=site_n,
        site_group=site_group,
        site_group_n=site_group_n,
        site_group_id=site_group_id,
        site_group_id_n=site_group_id_n,
        site_id=site_id,
        site_id_n=site_id_n,
        speed=speed,
        speed_empty=speed_empty,
        speed_gt=speed_gt,
        speed_gte=speed_gte,
        speed_lt=speed_lt,
        speed_lte=speed_lte,
        speed_n=speed_n,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        tx_power=tx_power,
        tx_power_empty=tx_power_empty,
        tx_power_gt=tx_power_gt,
        tx_power_gte=tx_power_gte,
        tx_power_lt=tx_power_lt,
        tx_power_lte=tx_power_lte,
        tx_power_n=tx_power_n,
        type_=type_,
        type_empty=type_empty,
        type_ic=type_ic,
        type_ie=type_ie,
        type_iew=type_iew,
        type_isw=type_isw,
        type_n=type_n,
        type_nic=type_nic,
        type_nie=type_nie,
        type_niew=type_niew,
        type_nisw=type_nisw,
        updated_by_request=updated_by_request,
        vdc=vdc,
        vdc_n=vdc_n,
        vdc_id=vdc_id,
        vdc_id_n=vdc_id_n,
        vdc_identifier=vdc_identifier,
        vdc_identifier_n=vdc_identifier_n,
        virtual_chassis=virtual_chassis,
        virtual_chassis_n=virtual_chassis_n,
        virtual_chassis_id=virtual_chassis_id,
        virtual_chassis_id_n=virtual_chassis_id_n,
        virtual_chassis_member=virtual_chassis_member,
        virtual_chassis_member_id=virtual_chassis_member_id,
        virtual_circuit_id=virtual_circuit_id,
        virtual_circuit_id_n=virtual_circuit_id_n,
        virtual_circuit_termination_id=virtual_circuit_termination_id,
        virtual_circuit_termination_id_n=virtual_circuit_termination_id_n,
        vlan=vlan,
        vlan_id=vlan_id,
        vlan_translation_policy=vlan_translation_policy,
        vlan_translation_policy_n=vlan_translation_policy_n,
        vlan_translation_policy_id=vlan_translation_policy_id,
        vlan_translation_policy_id_n=vlan_translation_policy_id_n,
        vrf=vrf,
        vrf_n=vrf_n,
        vrf_id=vrf_id,
        vrf_id_n=vrf_id_n,
        wireless_lan_id=wireless_lan_id,
        wireless_lan_id_n=wireless_lan_id_n,
        wireless_link_id=wireless_link_id,
        wireless_link_id_n=wireless_link_id_n,
        wwn=wwn,
        wwn_ic=wwn_ic,
        wwn_ie=wwn_ie,
        wwn_iew=wwn_iew,
        wwn_isw=wwn_isw,
        wwn_n=wwn_n,
        wwn_nic=wwn_nic,
        wwn_nie=wwn_nie,
        wwn_niew=wwn_niew,
        wwn_nisw=wwn_nisw,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    bridge_id: Union[Unset, list[int]] = UNSET,
    bridge_id_n: Union[Unset, list[int]] = UNSET,
    cable_end: Union[Unset, DcimInterfacesListCableEnd] = UNSET,
    cable_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cable_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cabled: Union[Unset, bool] = UNSET,
    connected: Union[Unset, bool] = UNSET,
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
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    device_id_n: Union[Unset, list[int]] = UNSET,
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_id: Union[Unset, list[int]] = UNSET,
    device_role_id_n: Union[Unset, list[int]] = UNSET,
    device_status: Union[Unset, list[str]] = UNSET,
    device_status_empty: Union[Unset, bool] = UNSET,
    device_status_ic: Union[Unset, list[str]] = UNSET,
    device_status_ie: Union[Unset, list[str]] = UNSET,
    device_status_iew: Union[Unset, list[str]] = UNSET,
    device_status_isw: Union[Unset, list[str]] = UNSET,
    device_status_n: Union[Unset, list[str]] = UNSET,
    device_status_nic: Union[Unset, list[str]] = UNSET,
    device_status_nie: Union[Unset, list[str]] = UNSET,
    device_status_niew: Union[Unset, list[str]] = UNSET,
    device_status_nisw: Union[Unset, list[str]] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    duplex: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_empty: Union[Unset, bool] = UNSET,
    duplex_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_n: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    kind: Union[Unset, str] = UNSET,
    l2vpn: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_n: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_id: Union[Unset, list[int]] = UNSET,
    l2vpn_id_n: Union[Unset, list[int]] = UNSET,
    label: Union[Unset, list[str]] = UNSET,
    label_empty: Union[Unset, bool] = UNSET,
    label_ic: Union[Unset, list[str]] = UNSET,
    label_ie: Union[Unset, list[str]] = UNSET,
    label_iew: Union[Unset, list[str]] = UNSET,
    label_isw: Union[Unset, list[str]] = UNSET,
    label_n: Union[Unset, list[str]] = UNSET,
    label_nic: Union[Unset, list[str]] = UNSET,
    label_nie: Union[Unset, list[str]] = UNSET,
    label_niew: Union[Unset, list[str]] = UNSET,
    label_nisw: Union[Unset, list[str]] = UNSET,
    lag_id: Union[Unset, list[int]] = UNSET,
    lag_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
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
    mark_connected: Union[Unset, bool] = UNSET,
    mgmt_only: Union[Unset, bool] = UNSET,
    mode: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_empty: Union[Unset, bool] = UNSET,
    mode_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_n: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_id: Union[Unset, list[Union[None, int]]] = UNSET,
    module_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    mtu: Union[Unset, list[int]] = UNSET,
    mtu_empty: Union[Unset, bool] = UNSET,
    mtu_gt: Union[Unset, list[int]] = UNSET,
    mtu_gte: Union[Unset, list[int]] = UNSET,
    mtu_lt: Union[Unset, list[int]] = UNSET,
    mtu_lte: Union[Unset, list[int]] = UNSET,
    mtu_n: Union[Unset, list[int]] = UNSET,
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
    occupied: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, list[int]] = UNSET,
    parent_id_n: Union[Unset, list[int]] = UNSET,
    poe_mode: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_empty: Union[Unset, bool] = UNSET,
    poe_mode_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_n: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_empty: Union[Unset, bool] = UNSET,
    poe_type_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_n: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    primary_mac_address: Union[Unset, list[str]] = UNSET,
    primary_mac_address_n: Union[Unset, list[str]] = UNSET,
    primary_mac_address_id: Union[Unset, list[int]] = UNSET,
    primary_mac_address_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    rf_channel: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_empty: Union[Unset, bool] = UNSET,
    rf_channel_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_n: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_frequency: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_empty: Union[Unset, bool] = UNSET,
    rf_channel_frequency_gt: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_gte: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_lt: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_lte: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_n: Union[Unset, list[float]] = UNSET,
    rf_channel_width: Union[Unset, list[float]] = UNSET,
    rf_channel_width_empty: Union[Unset, bool] = UNSET,
    rf_channel_width_gt: Union[Unset, list[float]] = UNSET,
    rf_channel_width_gte: Union[Unset, list[float]] = UNSET,
    rf_channel_width_lt: Union[Unset, list[float]] = UNSET,
    rf_channel_width_lte: Union[Unset, list[float]] = UNSET,
    rf_channel_width_n: Union[Unset, list[float]] = UNSET,
    rf_role: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_empty: Union[Unset, bool] = UNSET,
    rf_role_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_n: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    speed: Union[Unset, list[int]] = UNSET,
    speed_empty: Union[Unset, list[int]] = UNSET,
    speed_gt: Union[Unset, list[int]] = UNSET,
    speed_gte: Union[Unset, list[int]] = UNSET,
    speed_lt: Union[Unset, list[int]] = UNSET,
    speed_lte: Union[Unset, list[int]] = UNSET,
    speed_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tx_power: Union[Unset, list[int]] = UNSET,
    tx_power_empty: Union[Unset, bool] = UNSET,
    tx_power_gt: Union[Unset, list[int]] = UNSET,
    tx_power_gte: Union[Unset, list[int]] = UNSET,
    tx_power_lt: Union[Unset, list[int]] = UNSET,
    tx_power_lte: Union[Unset, list[int]] = UNSET,
    tx_power_n: Union[Unset, list[int]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    type_empty: Union[Unset, bool] = UNSET,
    type_ic: Union[Unset, list[str]] = UNSET,
    type_ie: Union[Unset, list[str]] = UNSET,
    type_iew: Union[Unset, list[str]] = UNSET,
    type_isw: Union[Unset, list[str]] = UNSET,
    type_n: Union[Unset, list[str]] = UNSET,
    type_nic: Union[Unset, list[str]] = UNSET,
    type_nie: Union[Unset, list[str]] = UNSET,
    type_niew: Union[Unset, list[str]] = UNSET,
    type_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    vdc: Union[Unset, list[str]] = UNSET,
    vdc_n: Union[Unset, list[str]] = UNSET,
    vdc_id: Union[Unset, list[int]] = UNSET,
    vdc_id_n: Union[Unset, list[int]] = UNSET,
    vdc_identifier: Union[Unset, list[Union[None, int]]] = UNSET,
    vdc_identifier_n: Union[Unset, list[Union[None, int]]] = UNSET,
    virtual_chassis: Union[Unset, list[str]] = UNSET,
    virtual_chassis_n: Union[Unset, list[str]] = UNSET,
    virtual_chassis_id: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id_n: Union[Unset, list[int]] = UNSET,
    virtual_chassis_member: Union[Unset, list[str]] = UNSET,
    virtual_chassis_member_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_id_n: Union[Unset, list[int]] = UNSET,
    virtual_circuit_termination_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_termination_id_n: Union[Unset, list[int]] = UNSET,
    vlan: Union[Unset, str] = UNSET,
    vlan_id: Union[Unset, str] = UNSET,
    vlan_translation_policy: Union[Unset, list[str]] = UNSET,
    vlan_translation_policy_n: Union[Unset, list[str]] = UNSET,
    vlan_translation_policy_id: Union[Unset, list[int]] = UNSET,
    vlan_translation_policy_id_n: Union[Unset, list[int]] = UNSET,
    vrf: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_n: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_id: Union[Unset, list[int]] = UNSET,
    vrf_id_n: Union[Unset, list[int]] = UNSET,
    wireless_lan_id: Union[Unset, list[int]] = UNSET,
    wireless_lan_id_n: Union[Unset, list[int]] = UNSET,
    wireless_link_id: Union[Unset, list[Union[None, int]]] = UNSET,
    wireless_link_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    wwn: Union[Unset, list[str]] = UNSET,
    wwn_ic: Union[Unset, list[str]] = UNSET,
    wwn_ie: Union[Unset, list[str]] = UNSET,
    wwn_iew: Union[Unset, list[str]] = UNSET,
    wwn_isw: Union[Unset, list[str]] = UNSET,
    wwn_n: Union[Unset, list[str]] = UNSET,
    wwn_nic: Union[Unset, list[str]] = UNSET,
    wwn_nie: Union[Unset, list[str]] = UNSET,
    wwn_niew: Union[Unset, list[str]] = UNSET,
    wwn_nisw: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedInterfaceList]:
    """Get a list of interface objects.

    Args:
        bridge_id (Union[Unset, list[int]]):
        bridge_id_n (Union[Unset, list[int]]):
        cable_end (Union[Unset, DcimInterfacesListCableEnd]):
        cable_id (Union[Unset, list[Union[None, int]]]):
        cable_id_n (Union[Unset, list[Union[None, int]]]):
        cabled (Union[Unset, bool]):
        connected (Union[Unset, bool]):
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
        device (Union[Unset, list[Union[None, str]]]):
        device_n (Union[Unset, list[Union[None, str]]]):
        device_id (Union[Unset, list[int]]):
        device_id_n (Union[Unset, list[int]]):
        device_role (Union[Unset, list[str]]):
        device_role_n (Union[Unset, list[str]]):
        device_role_id (Union[Unset, list[int]]):
        device_role_id_n (Union[Unset, list[int]]):
        device_status (Union[Unset, list[str]]):
        device_status_empty (Union[Unset, bool]):
        device_status_ic (Union[Unset, list[str]]):
        device_status_ie (Union[Unset, list[str]]):
        device_status_iew (Union[Unset, list[str]]):
        device_status_isw (Union[Unset, list[str]]):
        device_status_n (Union[Unset, list[str]]):
        device_status_nic (Union[Unset, list[str]]):
        device_status_nie (Union[Unset, list[str]]):
        device_status_niew (Union[Unset, list[str]]):
        device_status_nisw (Union[Unset, list[str]]):
        device_type (Union[Unset, list[str]]):
        device_type_n (Union[Unset, list[str]]):
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
        duplex (Union[Unset, list[Union[None, str]]]):
        duplex_empty (Union[Unset, bool]):
        duplex_ic (Union[Unset, list[Union[None, str]]]):
        duplex_ie (Union[Unset, list[Union[None, str]]]):
        duplex_iew (Union[Unset, list[Union[None, str]]]):
        duplex_isw (Union[Unset, list[Union[None, str]]]):
        duplex_n (Union[Unset, list[Union[None, str]]]):
        duplex_nic (Union[Unset, list[Union[None, str]]]):
        duplex_nie (Union[Unset, list[Union[None, str]]]):
        duplex_niew (Union[Unset, list[Union[None, str]]]):
        duplex_nisw (Union[Unset, list[Union[None, str]]]):
        enabled (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        kind (Union[Unset, str]):
        l2vpn (Union[Unset, list[Union[None, int]]]):
        l2vpn_n (Union[Unset, list[Union[None, int]]]):
        l2vpn_id (Union[Unset, list[int]]):
        l2vpn_id_n (Union[Unset, list[int]]):
        label (Union[Unset, list[str]]):
        label_empty (Union[Unset, bool]):
        label_ic (Union[Unset, list[str]]):
        label_ie (Union[Unset, list[str]]):
        label_iew (Union[Unset, list[str]]):
        label_isw (Union[Unset, list[str]]):
        label_n (Union[Unset, list[str]]):
        label_nic (Union[Unset, list[str]]):
        label_nie (Union[Unset, list[str]]):
        label_niew (Union[Unset, list[str]]):
        label_nisw (Union[Unset, list[str]]):
        lag_id (Union[Unset, list[int]]):
        lag_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_id (Union[Unset, list[int]]):
        location_id_n (Union[Unset, list[int]]):
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
        mark_connected (Union[Unset, bool]):
        mgmt_only (Union[Unset, bool]):
        mode (Union[Unset, list[Union[None, str]]]):
        mode_empty (Union[Unset, bool]):
        mode_ic (Union[Unset, list[Union[None, str]]]):
        mode_ie (Union[Unset, list[Union[None, str]]]):
        mode_iew (Union[Unset, list[Union[None, str]]]):
        mode_isw (Union[Unset, list[Union[None, str]]]):
        mode_n (Union[Unset, list[Union[None, str]]]):
        mode_nic (Union[Unset, list[Union[None, str]]]):
        mode_nie (Union[Unset, list[Union[None, str]]]):
        mode_niew (Union[Unset, list[Union[None, str]]]):
        mode_nisw (Union[Unset, list[Union[None, str]]]):
        modified_by_request (Union[Unset, UUID]):
        module_id (Union[Unset, list[Union[None, int]]]):
        module_id_n (Union[Unset, list[Union[None, int]]]):
        mtu (Union[Unset, list[int]]):
        mtu_empty (Union[Unset, bool]):
        mtu_gt (Union[Unset, list[int]]):
        mtu_gte (Union[Unset, list[int]]):
        mtu_lt (Union[Unset, list[int]]):
        mtu_lte (Union[Unset, list[int]]):
        mtu_n (Union[Unset, list[int]]):
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
        occupied (Union[Unset, bool]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        parent_id (Union[Unset, list[int]]):
        parent_id_n (Union[Unset, list[int]]):
        poe_mode (Union[Unset, list[Union[None, str]]]):
        poe_mode_empty (Union[Unset, bool]):
        poe_mode_ic (Union[Unset, list[Union[None, str]]]):
        poe_mode_ie (Union[Unset, list[Union[None, str]]]):
        poe_mode_iew (Union[Unset, list[Union[None, str]]]):
        poe_mode_isw (Union[Unset, list[Union[None, str]]]):
        poe_mode_n (Union[Unset, list[Union[None, str]]]):
        poe_mode_nic (Union[Unset, list[Union[None, str]]]):
        poe_mode_nie (Union[Unset, list[Union[None, str]]]):
        poe_mode_niew (Union[Unset, list[Union[None, str]]]):
        poe_mode_nisw (Union[Unset, list[Union[None, str]]]):
        poe_type (Union[Unset, list[Union[None, str]]]):
        poe_type_empty (Union[Unset, bool]):
        poe_type_ic (Union[Unset, list[Union[None, str]]]):
        poe_type_ie (Union[Unset, list[Union[None, str]]]):
        poe_type_iew (Union[Unset, list[Union[None, str]]]):
        poe_type_isw (Union[Unset, list[Union[None, str]]]):
        poe_type_n (Union[Unset, list[Union[None, str]]]):
        poe_type_nic (Union[Unset, list[Union[None, str]]]):
        poe_type_nie (Union[Unset, list[Union[None, str]]]):
        poe_type_niew (Union[Unset, list[Union[None, str]]]):
        poe_type_nisw (Union[Unset, list[Union[None, str]]]):
        primary_mac_address (Union[Unset, list[str]]):
        primary_mac_address_n (Union[Unset, list[str]]):
        primary_mac_address_id (Union[Unset, list[int]]):
        primary_mac_address_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_n (Union[Unset, list[str]]):
        rack_id (Union[Unset, list[int]]):
        rack_id_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        rf_channel (Union[Unset, list[Union[None, str]]]):
        rf_channel_empty (Union[Unset, bool]):
        rf_channel_ic (Union[Unset, list[Union[None, str]]]):
        rf_channel_ie (Union[Unset, list[Union[None, str]]]):
        rf_channel_iew (Union[Unset, list[Union[None, str]]]):
        rf_channel_isw (Union[Unset, list[Union[None, str]]]):
        rf_channel_n (Union[Unset, list[Union[None, str]]]):
        rf_channel_nic (Union[Unset, list[Union[None, str]]]):
        rf_channel_nie (Union[Unset, list[Union[None, str]]]):
        rf_channel_niew (Union[Unset, list[Union[None, str]]]):
        rf_channel_nisw (Union[Unset, list[Union[None, str]]]):
        rf_channel_frequency (Union[Unset, list[float]]):
        rf_channel_frequency_empty (Union[Unset, bool]):
        rf_channel_frequency_gt (Union[Unset, list[float]]):
        rf_channel_frequency_gte (Union[Unset, list[float]]):
        rf_channel_frequency_lt (Union[Unset, list[float]]):
        rf_channel_frequency_lte (Union[Unset, list[float]]):
        rf_channel_frequency_n (Union[Unset, list[float]]):
        rf_channel_width (Union[Unset, list[float]]):
        rf_channel_width_empty (Union[Unset, bool]):
        rf_channel_width_gt (Union[Unset, list[float]]):
        rf_channel_width_gte (Union[Unset, list[float]]):
        rf_channel_width_lt (Union[Unset, list[float]]):
        rf_channel_width_lte (Union[Unset, list[float]]):
        rf_channel_width_n (Union[Unset, list[float]]):
        rf_role (Union[Unset, list[Union[None, str]]]):
        rf_role_empty (Union[Unset, bool]):
        rf_role_ic (Union[Unset, list[Union[None, str]]]):
        rf_role_ie (Union[Unset, list[Union[None, str]]]):
        rf_role_iew (Union[Unset, list[Union[None, str]]]):
        rf_role_isw (Union[Unset, list[Union[None, str]]]):
        rf_role_n (Union[Unset, list[Union[None, str]]]):
        rf_role_nic (Union[Unset, list[Union[None, str]]]):
        rf_role_nie (Union[Unset, list[Union[None, str]]]):
        rf_role_niew (Union[Unset, list[Union[None, str]]]):
        rf_role_nisw (Union[Unset, list[Union[None, str]]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
        speed (Union[Unset, list[int]]):
        speed_empty (Union[Unset, list[int]]):
        speed_gt (Union[Unset, list[int]]):
        speed_gte (Union[Unset, list[int]]):
        speed_lt (Union[Unset, list[int]]):
        speed_lte (Union[Unset, list[int]]):
        speed_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        tx_power (Union[Unset, list[int]]):
        tx_power_empty (Union[Unset, bool]):
        tx_power_gt (Union[Unset, list[int]]):
        tx_power_gte (Union[Unset, list[int]]):
        tx_power_lt (Union[Unset, list[int]]):
        tx_power_lte (Union[Unset, list[int]]):
        tx_power_n (Union[Unset, list[int]]):
        type_ (Union[Unset, list[str]]):
        type_empty (Union[Unset, bool]):
        type_ic (Union[Unset, list[str]]):
        type_ie (Union[Unset, list[str]]):
        type_iew (Union[Unset, list[str]]):
        type_isw (Union[Unset, list[str]]):
        type_n (Union[Unset, list[str]]):
        type_nic (Union[Unset, list[str]]):
        type_nie (Union[Unset, list[str]]):
        type_niew (Union[Unset, list[str]]):
        type_nisw (Union[Unset, list[str]]):
        updated_by_request (Union[Unset, UUID]):
        vdc (Union[Unset, list[str]]):
        vdc_n (Union[Unset, list[str]]):
        vdc_id (Union[Unset, list[int]]):
        vdc_id_n (Union[Unset, list[int]]):
        vdc_identifier (Union[Unset, list[Union[None, int]]]):
        vdc_identifier_n (Union[Unset, list[Union[None, int]]]):
        virtual_chassis (Union[Unset, list[str]]):
        virtual_chassis_n (Union[Unset, list[str]]):
        virtual_chassis_id (Union[Unset, list[int]]):
        virtual_chassis_id_n (Union[Unset, list[int]]):
        virtual_chassis_member (Union[Unset, list[str]]):
        virtual_chassis_member_id (Union[Unset, list[int]]):
        virtual_circuit_id (Union[Unset, list[int]]):
        virtual_circuit_id_n (Union[Unset, list[int]]):
        virtual_circuit_termination_id (Union[Unset, list[int]]):
        virtual_circuit_termination_id_n (Union[Unset, list[int]]):
        vlan (Union[Unset, str]):
        vlan_id (Union[Unset, str]):
        vlan_translation_policy (Union[Unset, list[str]]):
        vlan_translation_policy_n (Union[Unset, list[str]]):
        vlan_translation_policy_id (Union[Unset, list[int]]):
        vlan_translation_policy_id_n (Union[Unset, list[int]]):
        vrf (Union[Unset, list[Union[None, str]]]):
        vrf_n (Union[Unset, list[Union[None, str]]]):
        vrf_id (Union[Unset, list[int]]):
        vrf_id_n (Union[Unset, list[int]]):
        wireless_lan_id (Union[Unset, list[int]]):
        wireless_lan_id_n (Union[Unset, list[int]]):
        wireless_link_id (Union[Unset, list[Union[None, int]]]):
        wireless_link_id_n (Union[Unset, list[Union[None, int]]]):
        wwn (Union[Unset, list[str]]):
        wwn_ic (Union[Unset, list[str]]):
        wwn_ie (Union[Unset, list[str]]):
        wwn_iew (Union[Unset, list[str]]):
        wwn_isw (Union[Unset, list[str]]):
        wwn_n (Union[Unset, list[str]]):
        wwn_nic (Union[Unset, list[str]]):
        wwn_nie (Union[Unset, list[str]]):
        wwn_niew (Union[Unset, list[str]]):
        wwn_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedInterfaceList]
    """

    kwargs = _get_kwargs(
        bridge_id=bridge_id,
        bridge_id_n=bridge_id_n,
        cable_end=cable_end,
        cable_id=cable_id,
        cable_id_n=cable_id_n,
        cabled=cabled,
        connected=connected,
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
        device=device,
        device_n=device_n,
        device_id=device_id,
        device_id_n=device_id_n,
        device_role=device_role,
        device_role_n=device_role_n,
        device_role_id=device_role_id,
        device_role_id_n=device_role_id_n,
        device_status=device_status,
        device_status_empty=device_status_empty,
        device_status_ic=device_status_ic,
        device_status_ie=device_status_ie,
        device_status_iew=device_status_iew,
        device_status_isw=device_status_isw,
        device_status_n=device_status_n,
        device_status_nic=device_status_nic,
        device_status_nie=device_status_nie,
        device_status_niew=device_status_niew,
        device_status_nisw=device_status_nisw,
        device_type=device_type,
        device_type_n=device_type_n,
        device_type_id=device_type_id,
        device_type_id_n=device_type_id_n,
        duplex=duplex,
        duplex_empty=duplex_empty,
        duplex_ic=duplex_ic,
        duplex_ie=duplex_ie,
        duplex_iew=duplex_iew,
        duplex_isw=duplex_isw,
        duplex_n=duplex_n,
        duplex_nic=duplex_nic,
        duplex_nie=duplex_nie,
        duplex_niew=duplex_niew,
        duplex_nisw=duplex_nisw,
        enabled=enabled,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        kind=kind,
        l2vpn=l2vpn,
        l2vpn_n=l2vpn_n,
        l2vpn_id=l2vpn_id,
        l2vpn_id_n=l2vpn_id_n,
        label=label,
        label_empty=label_empty,
        label_ic=label_ic,
        label_ie=label_ie,
        label_iew=label_iew,
        label_isw=label_isw,
        label_n=label_n,
        label_nic=label_nic,
        label_nie=label_nie,
        label_niew=label_niew,
        label_nisw=label_nisw,
        lag_id=lag_id,
        lag_id_n=lag_id_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        location=location,
        location_n=location_n,
        location_id=location_id,
        location_id_n=location_id_n,
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
        mark_connected=mark_connected,
        mgmt_only=mgmt_only,
        mode=mode,
        mode_empty=mode_empty,
        mode_ic=mode_ic,
        mode_ie=mode_ie,
        mode_iew=mode_iew,
        mode_isw=mode_isw,
        mode_n=mode_n,
        mode_nic=mode_nic,
        mode_nie=mode_nie,
        mode_niew=mode_niew,
        mode_nisw=mode_nisw,
        modified_by_request=modified_by_request,
        module_id=module_id,
        module_id_n=module_id_n,
        mtu=mtu,
        mtu_empty=mtu_empty,
        mtu_gt=mtu_gt,
        mtu_gte=mtu_gte,
        mtu_lt=mtu_lt,
        mtu_lte=mtu_lte,
        mtu_n=mtu_n,
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
        occupied=occupied,
        offset=offset,
        ordering=ordering,
        parent_id=parent_id,
        parent_id_n=parent_id_n,
        poe_mode=poe_mode,
        poe_mode_empty=poe_mode_empty,
        poe_mode_ic=poe_mode_ic,
        poe_mode_ie=poe_mode_ie,
        poe_mode_iew=poe_mode_iew,
        poe_mode_isw=poe_mode_isw,
        poe_mode_n=poe_mode_n,
        poe_mode_nic=poe_mode_nic,
        poe_mode_nie=poe_mode_nie,
        poe_mode_niew=poe_mode_niew,
        poe_mode_nisw=poe_mode_nisw,
        poe_type=poe_type,
        poe_type_empty=poe_type_empty,
        poe_type_ic=poe_type_ic,
        poe_type_ie=poe_type_ie,
        poe_type_iew=poe_type_iew,
        poe_type_isw=poe_type_isw,
        poe_type_n=poe_type_n,
        poe_type_nic=poe_type_nic,
        poe_type_nie=poe_type_nie,
        poe_type_niew=poe_type_niew,
        poe_type_nisw=poe_type_nisw,
        primary_mac_address=primary_mac_address,
        primary_mac_address_n=primary_mac_address_n,
        primary_mac_address_id=primary_mac_address_id,
        primary_mac_address_id_n=primary_mac_address_id_n,
        q=q,
        rack=rack,
        rack_n=rack_n,
        rack_id=rack_id,
        rack_id_n=rack_id_n,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        rf_channel=rf_channel,
        rf_channel_empty=rf_channel_empty,
        rf_channel_ic=rf_channel_ic,
        rf_channel_ie=rf_channel_ie,
        rf_channel_iew=rf_channel_iew,
        rf_channel_isw=rf_channel_isw,
        rf_channel_n=rf_channel_n,
        rf_channel_nic=rf_channel_nic,
        rf_channel_nie=rf_channel_nie,
        rf_channel_niew=rf_channel_niew,
        rf_channel_nisw=rf_channel_nisw,
        rf_channel_frequency=rf_channel_frequency,
        rf_channel_frequency_empty=rf_channel_frequency_empty,
        rf_channel_frequency_gt=rf_channel_frequency_gt,
        rf_channel_frequency_gte=rf_channel_frequency_gte,
        rf_channel_frequency_lt=rf_channel_frequency_lt,
        rf_channel_frequency_lte=rf_channel_frequency_lte,
        rf_channel_frequency_n=rf_channel_frequency_n,
        rf_channel_width=rf_channel_width,
        rf_channel_width_empty=rf_channel_width_empty,
        rf_channel_width_gt=rf_channel_width_gt,
        rf_channel_width_gte=rf_channel_width_gte,
        rf_channel_width_lt=rf_channel_width_lt,
        rf_channel_width_lte=rf_channel_width_lte,
        rf_channel_width_n=rf_channel_width_n,
        rf_role=rf_role,
        rf_role_empty=rf_role_empty,
        rf_role_ic=rf_role_ic,
        rf_role_ie=rf_role_ie,
        rf_role_iew=rf_role_iew,
        rf_role_isw=rf_role_isw,
        rf_role_n=rf_role_n,
        rf_role_nic=rf_role_nic,
        rf_role_nie=rf_role_nie,
        rf_role_niew=rf_role_niew,
        rf_role_nisw=rf_role_nisw,
        site=site,
        site_n=site_n,
        site_group=site_group,
        site_group_n=site_group_n,
        site_group_id=site_group_id,
        site_group_id_n=site_group_id_n,
        site_id=site_id,
        site_id_n=site_id_n,
        speed=speed,
        speed_empty=speed_empty,
        speed_gt=speed_gt,
        speed_gte=speed_gte,
        speed_lt=speed_lt,
        speed_lte=speed_lte,
        speed_n=speed_n,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        tx_power=tx_power,
        tx_power_empty=tx_power_empty,
        tx_power_gt=tx_power_gt,
        tx_power_gte=tx_power_gte,
        tx_power_lt=tx_power_lt,
        tx_power_lte=tx_power_lte,
        tx_power_n=tx_power_n,
        type_=type_,
        type_empty=type_empty,
        type_ic=type_ic,
        type_ie=type_ie,
        type_iew=type_iew,
        type_isw=type_isw,
        type_n=type_n,
        type_nic=type_nic,
        type_nie=type_nie,
        type_niew=type_niew,
        type_nisw=type_nisw,
        updated_by_request=updated_by_request,
        vdc=vdc,
        vdc_n=vdc_n,
        vdc_id=vdc_id,
        vdc_id_n=vdc_id_n,
        vdc_identifier=vdc_identifier,
        vdc_identifier_n=vdc_identifier_n,
        virtual_chassis=virtual_chassis,
        virtual_chassis_n=virtual_chassis_n,
        virtual_chassis_id=virtual_chassis_id,
        virtual_chassis_id_n=virtual_chassis_id_n,
        virtual_chassis_member=virtual_chassis_member,
        virtual_chassis_member_id=virtual_chassis_member_id,
        virtual_circuit_id=virtual_circuit_id,
        virtual_circuit_id_n=virtual_circuit_id_n,
        virtual_circuit_termination_id=virtual_circuit_termination_id,
        virtual_circuit_termination_id_n=virtual_circuit_termination_id_n,
        vlan=vlan,
        vlan_id=vlan_id,
        vlan_translation_policy=vlan_translation_policy,
        vlan_translation_policy_n=vlan_translation_policy_n,
        vlan_translation_policy_id=vlan_translation_policy_id,
        vlan_translation_policy_id_n=vlan_translation_policy_id_n,
        vrf=vrf,
        vrf_n=vrf_n,
        vrf_id=vrf_id,
        vrf_id_n=vrf_id_n,
        wireless_lan_id=wireless_lan_id,
        wireless_lan_id_n=wireless_lan_id_n,
        wireless_link_id=wireless_link_id,
        wireless_link_id_n=wireless_link_id_n,
        wwn=wwn,
        wwn_ic=wwn_ic,
        wwn_ie=wwn_ie,
        wwn_iew=wwn_iew,
        wwn_isw=wwn_isw,
        wwn_n=wwn_n,
        wwn_nic=wwn_nic,
        wwn_nie=wwn_nie,
        wwn_niew=wwn_niew,
        wwn_nisw=wwn_nisw,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    bridge_id: Union[Unset, list[int]] = UNSET,
    bridge_id_n: Union[Unset, list[int]] = UNSET,
    cable_end: Union[Unset, DcimInterfacesListCableEnd] = UNSET,
    cable_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cable_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cabled: Union[Unset, bool] = UNSET,
    connected: Union[Unset, bool] = UNSET,
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
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    device_id_n: Union[Unset, list[int]] = UNSET,
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_id: Union[Unset, list[int]] = UNSET,
    device_role_id_n: Union[Unset, list[int]] = UNSET,
    device_status: Union[Unset, list[str]] = UNSET,
    device_status_empty: Union[Unset, bool] = UNSET,
    device_status_ic: Union[Unset, list[str]] = UNSET,
    device_status_ie: Union[Unset, list[str]] = UNSET,
    device_status_iew: Union[Unset, list[str]] = UNSET,
    device_status_isw: Union[Unset, list[str]] = UNSET,
    device_status_n: Union[Unset, list[str]] = UNSET,
    device_status_nic: Union[Unset, list[str]] = UNSET,
    device_status_nie: Union[Unset, list[str]] = UNSET,
    device_status_niew: Union[Unset, list[str]] = UNSET,
    device_status_nisw: Union[Unset, list[str]] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    duplex: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_empty: Union[Unset, bool] = UNSET,
    duplex_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_n: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    duplex_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    kind: Union[Unset, str] = UNSET,
    l2vpn: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_n: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_id: Union[Unset, list[int]] = UNSET,
    l2vpn_id_n: Union[Unset, list[int]] = UNSET,
    label: Union[Unset, list[str]] = UNSET,
    label_empty: Union[Unset, bool] = UNSET,
    label_ic: Union[Unset, list[str]] = UNSET,
    label_ie: Union[Unset, list[str]] = UNSET,
    label_iew: Union[Unset, list[str]] = UNSET,
    label_isw: Union[Unset, list[str]] = UNSET,
    label_n: Union[Unset, list[str]] = UNSET,
    label_nic: Union[Unset, list[str]] = UNSET,
    label_nie: Union[Unset, list[str]] = UNSET,
    label_niew: Union[Unset, list[str]] = UNSET,
    label_nisw: Union[Unset, list[str]] = UNSET,
    lag_id: Union[Unset, list[int]] = UNSET,
    lag_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
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
    mark_connected: Union[Unset, bool] = UNSET,
    mgmt_only: Union[Unset, bool] = UNSET,
    mode: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_empty: Union[Unset, bool] = UNSET,
    mode_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_n: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_id: Union[Unset, list[Union[None, int]]] = UNSET,
    module_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    mtu: Union[Unset, list[int]] = UNSET,
    mtu_empty: Union[Unset, bool] = UNSET,
    mtu_gt: Union[Unset, list[int]] = UNSET,
    mtu_gte: Union[Unset, list[int]] = UNSET,
    mtu_lt: Union[Unset, list[int]] = UNSET,
    mtu_lte: Union[Unset, list[int]] = UNSET,
    mtu_n: Union[Unset, list[int]] = UNSET,
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
    occupied: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, list[int]] = UNSET,
    parent_id_n: Union[Unset, list[int]] = UNSET,
    poe_mode: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_empty: Union[Unset, bool] = UNSET,
    poe_mode_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_n: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_mode_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_empty: Union[Unset, bool] = UNSET,
    poe_type_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_n: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    poe_type_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    primary_mac_address: Union[Unset, list[str]] = UNSET,
    primary_mac_address_n: Union[Unset, list[str]] = UNSET,
    primary_mac_address_id: Union[Unset, list[int]] = UNSET,
    primary_mac_address_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    rf_channel: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_empty: Union[Unset, bool] = UNSET,
    rf_channel_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_n: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_channel_frequency: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_empty: Union[Unset, bool] = UNSET,
    rf_channel_frequency_gt: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_gte: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_lt: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_lte: Union[Unset, list[float]] = UNSET,
    rf_channel_frequency_n: Union[Unset, list[float]] = UNSET,
    rf_channel_width: Union[Unset, list[float]] = UNSET,
    rf_channel_width_empty: Union[Unset, bool] = UNSET,
    rf_channel_width_gt: Union[Unset, list[float]] = UNSET,
    rf_channel_width_gte: Union[Unset, list[float]] = UNSET,
    rf_channel_width_lt: Union[Unset, list[float]] = UNSET,
    rf_channel_width_lte: Union[Unset, list[float]] = UNSET,
    rf_channel_width_n: Union[Unset, list[float]] = UNSET,
    rf_role: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_empty: Union[Unset, bool] = UNSET,
    rf_role_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_n: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    rf_role_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    speed: Union[Unset, list[int]] = UNSET,
    speed_empty: Union[Unset, list[int]] = UNSET,
    speed_gt: Union[Unset, list[int]] = UNSET,
    speed_gte: Union[Unset, list[int]] = UNSET,
    speed_lt: Union[Unset, list[int]] = UNSET,
    speed_lte: Union[Unset, list[int]] = UNSET,
    speed_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tx_power: Union[Unset, list[int]] = UNSET,
    tx_power_empty: Union[Unset, bool] = UNSET,
    tx_power_gt: Union[Unset, list[int]] = UNSET,
    tx_power_gte: Union[Unset, list[int]] = UNSET,
    tx_power_lt: Union[Unset, list[int]] = UNSET,
    tx_power_lte: Union[Unset, list[int]] = UNSET,
    tx_power_n: Union[Unset, list[int]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    type_empty: Union[Unset, bool] = UNSET,
    type_ic: Union[Unset, list[str]] = UNSET,
    type_ie: Union[Unset, list[str]] = UNSET,
    type_iew: Union[Unset, list[str]] = UNSET,
    type_isw: Union[Unset, list[str]] = UNSET,
    type_n: Union[Unset, list[str]] = UNSET,
    type_nic: Union[Unset, list[str]] = UNSET,
    type_nie: Union[Unset, list[str]] = UNSET,
    type_niew: Union[Unset, list[str]] = UNSET,
    type_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    vdc: Union[Unset, list[str]] = UNSET,
    vdc_n: Union[Unset, list[str]] = UNSET,
    vdc_id: Union[Unset, list[int]] = UNSET,
    vdc_id_n: Union[Unset, list[int]] = UNSET,
    vdc_identifier: Union[Unset, list[Union[None, int]]] = UNSET,
    vdc_identifier_n: Union[Unset, list[Union[None, int]]] = UNSET,
    virtual_chassis: Union[Unset, list[str]] = UNSET,
    virtual_chassis_n: Union[Unset, list[str]] = UNSET,
    virtual_chassis_id: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id_n: Union[Unset, list[int]] = UNSET,
    virtual_chassis_member: Union[Unset, list[str]] = UNSET,
    virtual_chassis_member_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_id_n: Union[Unset, list[int]] = UNSET,
    virtual_circuit_termination_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_termination_id_n: Union[Unset, list[int]] = UNSET,
    vlan: Union[Unset, str] = UNSET,
    vlan_id: Union[Unset, str] = UNSET,
    vlan_translation_policy: Union[Unset, list[str]] = UNSET,
    vlan_translation_policy_n: Union[Unset, list[str]] = UNSET,
    vlan_translation_policy_id: Union[Unset, list[int]] = UNSET,
    vlan_translation_policy_id_n: Union[Unset, list[int]] = UNSET,
    vrf: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_n: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_id: Union[Unset, list[int]] = UNSET,
    vrf_id_n: Union[Unset, list[int]] = UNSET,
    wireless_lan_id: Union[Unset, list[int]] = UNSET,
    wireless_lan_id_n: Union[Unset, list[int]] = UNSET,
    wireless_link_id: Union[Unset, list[Union[None, int]]] = UNSET,
    wireless_link_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    wwn: Union[Unset, list[str]] = UNSET,
    wwn_ic: Union[Unset, list[str]] = UNSET,
    wwn_ie: Union[Unset, list[str]] = UNSET,
    wwn_iew: Union[Unset, list[str]] = UNSET,
    wwn_isw: Union[Unset, list[str]] = UNSET,
    wwn_n: Union[Unset, list[str]] = UNSET,
    wwn_nic: Union[Unset, list[str]] = UNSET,
    wwn_nie: Union[Unset, list[str]] = UNSET,
    wwn_niew: Union[Unset, list[str]] = UNSET,
    wwn_nisw: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedInterfaceList]:
    """Get a list of interface objects.

    Args:
        bridge_id (Union[Unset, list[int]]):
        bridge_id_n (Union[Unset, list[int]]):
        cable_end (Union[Unset, DcimInterfacesListCableEnd]):
        cable_id (Union[Unset, list[Union[None, int]]]):
        cable_id_n (Union[Unset, list[Union[None, int]]]):
        cabled (Union[Unset, bool]):
        connected (Union[Unset, bool]):
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
        device (Union[Unset, list[Union[None, str]]]):
        device_n (Union[Unset, list[Union[None, str]]]):
        device_id (Union[Unset, list[int]]):
        device_id_n (Union[Unset, list[int]]):
        device_role (Union[Unset, list[str]]):
        device_role_n (Union[Unset, list[str]]):
        device_role_id (Union[Unset, list[int]]):
        device_role_id_n (Union[Unset, list[int]]):
        device_status (Union[Unset, list[str]]):
        device_status_empty (Union[Unset, bool]):
        device_status_ic (Union[Unset, list[str]]):
        device_status_ie (Union[Unset, list[str]]):
        device_status_iew (Union[Unset, list[str]]):
        device_status_isw (Union[Unset, list[str]]):
        device_status_n (Union[Unset, list[str]]):
        device_status_nic (Union[Unset, list[str]]):
        device_status_nie (Union[Unset, list[str]]):
        device_status_niew (Union[Unset, list[str]]):
        device_status_nisw (Union[Unset, list[str]]):
        device_type (Union[Unset, list[str]]):
        device_type_n (Union[Unset, list[str]]):
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
        duplex (Union[Unset, list[Union[None, str]]]):
        duplex_empty (Union[Unset, bool]):
        duplex_ic (Union[Unset, list[Union[None, str]]]):
        duplex_ie (Union[Unset, list[Union[None, str]]]):
        duplex_iew (Union[Unset, list[Union[None, str]]]):
        duplex_isw (Union[Unset, list[Union[None, str]]]):
        duplex_n (Union[Unset, list[Union[None, str]]]):
        duplex_nic (Union[Unset, list[Union[None, str]]]):
        duplex_nie (Union[Unset, list[Union[None, str]]]):
        duplex_niew (Union[Unset, list[Union[None, str]]]):
        duplex_nisw (Union[Unset, list[Union[None, str]]]):
        enabled (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        kind (Union[Unset, str]):
        l2vpn (Union[Unset, list[Union[None, int]]]):
        l2vpn_n (Union[Unset, list[Union[None, int]]]):
        l2vpn_id (Union[Unset, list[int]]):
        l2vpn_id_n (Union[Unset, list[int]]):
        label (Union[Unset, list[str]]):
        label_empty (Union[Unset, bool]):
        label_ic (Union[Unset, list[str]]):
        label_ie (Union[Unset, list[str]]):
        label_iew (Union[Unset, list[str]]):
        label_isw (Union[Unset, list[str]]):
        label_n (Union[Unset, list[str]]):
        label_nic (Union[Unset, list[str]]):
        label_nie (Union[Unset, list[str]]):
        label_niew (Union[Unset, list[str]]):
        label_nisw (Union[Unset, list[str]]):
        lag_id (Union[Unset, list[int]]):
        lag_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_id (Union[Unset, list[int]]):
        location_id_n (Union[Unset, list[int]]):
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
        mark_connected (Union[Unset, bool]):
        mgmt_only (Union[Unset, bool]):
        mode (Union[Unset, list[Union[None, str]]]):
        mode_empty (Union[Unset, bool]):
        mode_ic (Union[Unset, list[Union[None, str]]]):
        mode_ie (Union[Unset, list[Union[None, str]]]):
        mode_iew (Union[Unset, list[Union[None, str]]]):
        mode_isw (Union[Unset, list[Union[None, str]]]):
        mode_n (Union[Unset, list[Union[None, str]]]):
        mode_nic (Union[Unset, list[Union[None, str]]]):
        mode_nie (Union[Unset, list[Union[None, str]]]):
        mode_niew (Union[Unset, list[Union[None, str]]]):
        mode_nisw (Union[Unset, list[Union[None, str]]]):
        modified_by_request (Union[Unset, UUID]):
        module_id (Union[Unset, list[Union[None, int]]]):
        module_id_n (Union[Unset, list[Union[None, int]]]):
        mtu (Union[Unset, list[int]]):
        mtu_empty (Union[Unset, bool]):
        mtu_gt (Union[Unset, list[int]]):
        mtu_gte (Union[Unset, list[int]]):
        mtu_lt (Union[Unset, list[int]]):
        mtu_lte (Union[Unset, list[int]]):
        mtu_n (Union[Unset, list[int]]):
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
        occupied (Union[Unset, bool]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        parent_id (Union[Unset, list[int]]):
        parent_id_n (Union[Unset, list[int]]):
        poe_mode (Union[Unset, list[Union[None, str]]]):
        poe_mode_empty (Union[Unset, bool]):
        poe_mode_ic (Union[Unset, list[Union[None, str]]]):
        poe_mode_ie (Union[Unset, list[Union[None, str]]]):
        poe_mode_iew (Union[Unset, list[Union[None, str]]]):
        poe_mode_isw (Union[Unset, list[Union[None, str]]]):
        poe_mode_n (Union[Unset, list[Union[None, str]]]):
        poe_mode_nic (Union[Unset, list[Union[None, str]]]):
        poe_mode_nie (Union[Unset, list[Union[None, str]]]):
        poe_mode_niew (Union[Unset, list[Union[None, str]]]):
        poe_mode_nisw (Union[Unset, list[Union[None, str]]]):
        poe_type (Union[Unset, list[Union[None, str]]]):
        poe_type_empty (Union[Unset, bool]):
        poe_type_ic (Union[Unset, list[Union[None, str]]]):
        poe_type_ie (Union[Unset, list[Union[None, str]]]):
        poe_type_iew (Union[Unset, list[Union[None, str]]]):
        poe_type_isw (Union[Unset, list[Union[None, str]]]):
        poe_type_n (Union[Unset, list[Union[None, str]]]):
        poe_type_nic (Union[Unset, list[Union[None, str]]]):
        poe_type_nie (Union[Unset, list[Union[None, str]]]):
        poe_type_niew (Union[Unset, list[Union[None, str]]]):
        poe_type_nisw (Union[Unset, list[Union[None, str]]]):
        primary_mac_address (Union[Unset, list[str]]):
        primary_mac_address_n (Union[Unset, list[str]]):
        primary_mac_address_id (Union[Unset, list[int]]):
        primary_mac_address_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_n (Union[Unset, list[str]]):
        rack_id (Union[Unset, list[int]]):
        rack_id_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        rf_channel (Union[Unset, list[Union[None, str]]]):
        rf_channel_empty (Union[Unset, bool]):
        rf_channel_ic (Union[Unset, list[Union[None, str]]]):
        rf_channel_ie (Union[Unset, list[Union[None, str]]]):
        rf_channel_iew (Union[Unset, list[Union[None, str]]]):
        rf_channel_isw (Union[Unset, list[Union[None, str]]]):
        rf_channel_n (Union[Unset, list[Union[None, str]]]):
        rf_channel_nic (Union[Unset, list[Union[None, str]]]):
        rf_channel_nie (Union[Unset, list[Union[None, str]]]):
        rf_channel_niew (Union[Unset, list[Union[None, str]]]):
        rf_channel_nisw (Union[Unset, list[Union[None, str]]]):
        rf_channel_frequency (Union[Unset, list[float]]):
        rf_channel_frequency_empty (Union[Unset, bool]):
        rf_channel_frequency_gt (Union[Unset, list[float]]):
        rf_channel_frequency_gte (Union[Unset, list[float]]):
        rf_channel_frequency_lt (Union[Unset, list[float]]):
        rf_channel_frequency_lte (Union[Unset, list[float]]):
        rf_channel_frequency_n (Union[Unset, list[float]]):
        rf_channel_width (Union[Unset, list[float]]):
        rf_channel_width_empty (Union[Unset, bool]):
        rf_channel_width_gt (Union[Unset, list[float]]):
        rf_channel_width_gte (Union[Unset, list[float]]):
        rf_channel_width_lt (Union[Unset, list[float]]):
        rf_channel_width_lte (Union[Unset, list[float]]):
        rf_channel_width_n (Union[Unset, list[float]]):
        rf_role (Union[Unset, list[Union[None, str]]]):
        rf_role_empty (Union[Unset, bool]):
        rf_role_ic (Union[Unset, list[Union[None, str]]]):
        rf_role_ie (Union[Unset, list[Union[None, str]]]):
        rf_role_iew (Union[Unset, list[Union[None, str]]]):
        rf_role_isw (Union[Unset, list[Union[None, str]]]):
        rf_role_n (Union[Unset, list[Union[None, str]]]):
        rf_role_nic (Union[Unset, list[Union[None, str]]]):
        rf_role_nie (Union[Unset, list[Union[None, str]]]):
        rf_role_niew (Union[Unset, list[Union[None, str]]]):
        rf_role_nisw (Union[Unset, list[Union[None, str]]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
        speed (Union[Unset, list[int]]):
        speed_empty (Union[Unset, list[int]]):
        speed_gt (Union[Unset, list[int]]):
        speed_gte (Union[Unset, list[int]]):
        speed_lt (Union[Unset, list[int]]):
        speed_lte (Union[Unset, list[int]]):
        speed_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        tx_power (Union[Unset, list[int]]):
        tx_power_empty (Union[Unset, bool]):
        tx_power_gt (Union[Unset, list[int]]):
        tx_power_gte (Union[Unset, list[int]]):
        tx_power_lt (Union[Unset, list[int]]):
        tx_power_lte (Union[Unset, list[int]]):
        tx_power_n (Union[Unset, list[int]]):
        type_ (Union[Unset, list[str]]):
        type_empty (Union[Unset, bool]):
        type_ic (Union[Unset, list[str]]):
        type_ie (Union[Unset, list[str]]):
        type_iew (Union[Unset, list[str]]):
        type_isw (Union[Unset, list[str]]):
        type_n (Union[Unset, list[str]]):
        type_nic (Union[Unset, list[str]]):
        type_nie (Union[Unset, list[str]]):
        type_niew (Union[Unset, list[str]]):
        type_nisw (Union[Unset, list[str]]):
        updated_by_request (Union[Unset, UUID]):
        vdc (Union[Unset, list[str]]):
        vdc_n (Union[Unset, list[str]]):
        vdc_id (Union[Unset, list[int]]):
        vdc_id_n (Union[Unset, list[int]]):
        vdc_identifier (Union[Unset, list[Union[None, int]]]):
        vdc_identifier_n (Union[Unset, list[Union[None, int]]]):
        virtual_chassis (Union[Unset, list[str]]):
        virtual_chassis_n (Union[Unset, list[str]]):
        virtual_chassis_id (Union[Unset, list[int]]):
        virtual_chassis_id_n (Union[Unset, list[int]]):
        virtual_chassis_member (Union[Unset, list[str]]):
        virtual_chassis_member_id (Union[Unset, list[int]]):
        virtual_circuit_id (Union[Unset, list[int]]):
        virtual_circuit_id_n (Union[Unset, list[int]]):
        virtual_circuit_termination_id (Union[Unset, list[int]]):
        virtual_circuit_termination_id_n (Union[Unset, list[int]]):
        vlan (Union[Unset, str]):
        vlan_id (Union[Unset, str]):
        vlan_translation_policy (Union[Unset, list[str]]):
        vlan_translation_policy_n (Union[Unset, list[str]]):
        vlan_translation_policy_id (Union[Unset, list[int]]):
        vlan_translation_policy_id_n (Union[Unset, list[int]]):
        vrf (Union[Unset, list[Union[None, str]]]):
        vrf_n (Union[Unset, list[Union[None, str]]]):
        vrf_id (Union[Unset, list[int]]):
        vrf_id_n (Union[Unset, list[int]]):
        wireless_lan_id (Union[Unset, list[int]]):
        wireless_lan_id_n (Union[Unset, list[int]]):
        wireless_link_id (Union[Unset, list[Union[None, int]]]):
        wireless_link_id_n (Union[Unset, list[Union[None, int]]]):
        wwn (Union[Unset, list[str]]):
        wwn_ic (Union[Unset, list[str]]):
        wwn_ie (Union[Unset, list[str]]):
        wwn_iew (Union[Unset, list[str]]):
        wwn_isw (Union[Unset, list[str]]):
        wwn_n (Union[Unset, list[str]]):
        wwn_nic (Union[Unset, list[str]]):
        wwn_nie (Union[Unset, list[str]]):
        wwn_niew (Union[Unset, list[str]]):
        wwn_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedInterfaceList
    """

    return (
        await asyncio_detailed(
            client=client,
            bridge_id=bridge_id,
            bridge_id_n=bridge_id_n,
            cable_end=cable_end,
            cable_id=cable_id,
            cable_id_n=cable_id_n,
            cabled=cabled,
            connected=connected,
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
            device=device,
            device_n=device_n,
            device_id=device_id,
            device_id_n=device_id_n,
            device_role=device_role,
            device_role_n=device_role_n,
            device_role_id=device_role_id,
            device_role_id_n=device_role_id_n,
            device_status=device_status,
            device_status_empty=device_status_empty,
            device_status_ic=device_status_ic,
            device_status_ie=device_status_ie,
            device_status_iew=device_status_iew,
            device_status_isw=device_status_isw,
            device_status_n=device_status_n,
            device_status_nic=device_status_nic,
            device_status_nie=device_status_nie,
            device_status_niew=device_status_niew,
            device_status_nisw=device_status_nisw,
            device_type=device_type,
            device_type_n=device_type_n,
            device_type_id=device_type_id,
            device_type_id_n=device_type_id_n,
            duplex=duplex,
            duplex_empty=duplex_empty,
            duplex_ic=duplex_ic,
            duplex_ie=duplex_ie,
            duplex_iew=duplex_iew,
            duplex_isw=duplex_isw,
            duplex_n=duplex_n,
            duplex_nic=duplex_nic,
            duplex_nie=duplex_nie,
            duplex_niew=duplex_niew,
            duplex_nisw=duplex_nisw,
            enabled=enabled,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            kind=kind,
            l2vpn=l2vpn,
            l2vpn_n=l2vpn_n,
            l2vpn_id=l2vpn_id,
            l2vpn_id_n=l2vpn_id_n,
            label=label,
            label_empty=label_empty,
            label_ic=label_ic,
            label_ie=label_ie,
            label_iew=label_iew,
            label_isw=label_isw,
            label_n=label_n,
            label_nic=label_nic,
            label_nie=label_nie,
            label_niew=label_niew,
            label_nisw=label_nisw,
            lag_id=lag_id,
            lag_id_n=lag_id_n,
            last_updated=last_updated,
            last_updated_empty=last_updated_empty,
            last_updated_gt=last_updated_gt,
            last_updated_gte=last_updated_gte,
            last_updated_lt=last_updated_lt,
            last_updated_lte=last_updated_lte,
            last_updated_n=last_updated_n,
            limit=limit,
            location=location,
            location_n=location_n,
            location_id=location_id,
            location_id_n=location_id_n,
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
            mark_connected=mark_connected,
            mgmt_only=mgmt_only,
            mode=mode,
            mode_empty=mode_empty,
            mode_ic=mode_ic,
            mode_ie=mode_ie,
            mode_iew=mode_iew,
            mode_isw=mode_isw,
            mode_n=mode_n,
            mode_nic=mode_nic,
            mode_nie=mode_nie,
            mode_niew=mode_niew,
            mode_nisw=mode_nisw,
            modified_by_request=modified_by_request,
            module_id=module_id,
            module_id_n=module_id_n,
            mtu=mtu,
            mtu_empty=mtu_empty,
            mtu_gt=mtu_gt,
            mtu_gte=mtu_gte,
            mtu_lt=mtu_lt,
            mtu_lte=mtu_lte,
            mtu_n=mtu_n,
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
            occupied=occupied,
            offset=offset,
            ordering=ordering,
            parent_id=parent_id,
            parent_id_n=parent_id_n,
            poe_mode=poe_mode,
            poe_mode_empty=poe_mode_empty,
            poe_mode_ic=poe_mode_ic,
            poe_mode_ie=poe_mode_ie,
            poe_mode_iew=poe_mode_iew,
            poe_mode_isw=poe_mode_isw,
            poe_mode_n=poe_mode_n,
            poe_mode_nic=poe_mode_nic,
            poe_mode_nie=poe_mode_nie,
            poe_mode_niew=poe_mode_niew,
            poe_mode_nisw=poe_mode_nisw,
            poe_type=poe_type,
            poe_type_empty=poe_type_empty,
            poe_type_ic=poe_type_ic,
            poe_type_ie=poe_type_ie,
            poe_type_iew=poe_type_iew,
            poe_type_isw=poe_type_isw,
            poe_type_n=poe_type_n,
            poe_type_nic=poe_type_nic,
            poe_type_nie=poe_type_nie,
            poe_type_niew=poe_type_niew,
            poe_type_nisw=poe_type_nisw,
            primary_mac_address=primary_mac_address,
            primary_mac_address_n=primary_mac_address_n,
            primary_mac_address_id=primary_mac_address_id,
            primary_mac_address_id_n=primary_mac_address_id_n,
            q=q,
            rack=rack,
            rack_n=rack_n,
            rack_id=rack_id,
            rack_id_n=rack_id_n,
            region=region,
            region_n=region_n,
            region_id=region_id,
            region_id_n=region_id_n,
            rf_channel=rf_channel,
            rf_channel_empty=rf_channel_empty,
            rf_channel_ic=rf_channel_ic,
            rf_channel_ie=rf_channel_ie,
            rf_channel_iew=rf_channel_iew,
            rf_channel_isw=rf_channel_isw,
            rf_channel_n=rf_channel_n,
            rf_channel_nic=rf_channel_nic,
            rf_channel_nie=rf_channel_nie,
            rf_channel_niew=rf_channel_niew,
            rf_channel_nisw=rf_channel_nisw,
            rf_channel_frequency=rf_channel_frequency,
            rf_channel_frequency_empty=rf_channel_frequency_empty,
            rf_channel_frequency_gt=rf_channel_frequency_gt,
            rf_channel_frequency_gte=rf_channel_frequency_gte,
            rf_channel_frequency_lt=rf_channel_frequency_lt,
            rf_channel_frequency_lte=rf_channel_frequency_lte,
            rf_channel_frequency_n=rf_channel_frequency_n,
            rf_channel_width=rf_channel_width,
            rf_channel_width_empty=rf_channel_width_empty,
            rf_channel_width_gt=rf_channel_width_gt,
            rf_channel_width_gte=rf_channel_width_gte,
            rf_channel_width_lt=rf_channel_width_lt,
            rf_channel_width_lte=rf_channel_width_lte,
            rf_channel_width_n=rf_channel_width_n,
            rf_role=rf_role,
            rf_role_empty=rf_role_empty,
            rf_role_ic=rf_role_ic,
            rf_role_ie=rf_role_ie,
            rf_role_iew=rf_role_iew,
            rf_role_isw=rf_role_isw,
            rf_role_n=rf_role_n,
            rf_role_nic=rf_role_nic,
            rf_role_nie=rf_role_nie,
            rf_role_niew=rf_role_niew,
            rf_role_nisw=rf_role_nisw,
            site=site,
            site_n=site_n,
            site_group=site_group,
            site_group_n=site_group_n,
            site_group_id=site_group_id,
            site_group_id_n=site_group_id_n,
            site_id=site_id,
            site_id_n=site_id_n,
            speed=speed,
            speed_empty=speed_empty,
            speed_gt=speed_gt,
            speed_gte=speed_gte,
            speed_lt=speed_lt,
            speed_lte=speed_lte,
            speed_n=speed_n,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
            tx_power=tx_power,
            tx_power_empty=tx_power_empty,
            tx_power_gt=tx_power_gt,
            tx_power_gte=tx_power_gte,
            tx_power_lt=tx_power_lt,
            tx_power_lte=tx_power_lte,
            tx_power_n=tx_power_n,
            type_=type_,
            type_empty=type_empty,
            type_ic=type_ic,
            type_ie=type_ie,
            type_iew=type_iew,
            type_isw=type_isw,
            type_n=type_n,
            type_nic=type_nic,
            type_nie=type_nie,
            type_niew=type_niew,
            type_nisw=type_nisw,
            updated_by_request=updated_by_request,
            vdc=vdc,
            vdc_n=vdc_n,
            vdc_id=vdc_id,
            vdc_id_n=vdc_id_n,
            vdc_identifier=vdc_identifier,
            vdc_identifier_n=vdc_identifier_n,
            virtual_chassis=virtual_chassis,
            virtual_chassis_n=virtual_chassis_n,
            virtual_chassis_id=virtual_chassis_id,
            virtual_chassis_id_n=virtual_chassis_id_n,
            virtual_chassis_member=virtual_chassis_member,
            virtual_chassis_member_id=virtual_chassis_member_id,
            virtual_circuit_id=virtual_circuit_id,
            virtual_circuit_id_n=virtual_circuit_id_n,
            virtual_circuit_termination_id=virtual_circuit_termination_id,
            virtual_circuit_termination_id_n=virtual_circuit_termination_id_n,
            vlan=vlan,
            vlan_id=vlan_id,
            vlan_translation_policy=vlan_translation_policy,
            vlan_translation_policy_n=vlan_translation_policy_n,
            vlan_translation_policy_id=vlan_translation_policy_id,
            vlan_translation_policy_id_n=vlan_translation_policy_id_n,
            vrf=vrf,
            vrf_n=vrf_n,
            vrf_id=vrf_id,
            vrf_id_n=vrf_id_n,
            wireless_lan_id=wireless_lan_id,
            wireless_lan_id_n=wireless_lan_id_n,
            wireless_link_id=wireless_link_id,
            wireless_link_id_n=wireless_link_id_n,
            wwn=wwn,
            wwn_ic=wwn_ic,
            wwn_ie=wwn_ie,
            wwn_iew=wwn_iew,
            wwn_isw=wwn_isw,
            wwn_n=wwn_n,
            wwn_nic=wwn_nic,
            wwn_nie=wwn_nie,
            wwn_niew=wwn_niew,
            wwn_nisw=wwn_nisw,
        )
    ).parsed
