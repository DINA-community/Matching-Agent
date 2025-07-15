import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_vm_interface_list import PaginatedVMInterfaceList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    bridge_id: Union[Unset, list[int]] = UNSET,
    bridge_id_n: Union[Unset, list[int]] = UNSET,
    cluster: Union[Unset, list[str]] = UNSET,
    cluster_n: Union[Unset, list[str]] = UNSET,
    cluster_id: Union[Unset, list[int]] = UNSET,
    cluster_id_n: Union[Unset, list[int]] = UNSET,
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
    enabled: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    l2vpn: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_n: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_id: Union[Unset, list[int]] = UNSET,
    l2vpn_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
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
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, list[int]] = UNSET,
    parent_id_n: Union[Unset, list[int]] = UNSET,
    primary_mac_address: Union[Unset, list[str]] = UNSET,
    primary_mac_address_n: Union[Unset, list[str]] = UNSET,
    primary_mac_address_id: Union[Unset, list[int]] = UNSET,
    primary_mac_address_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_machine: Union[Unset, list[str]] = UNSET,
    virtual_machine_n: Union[Unset, list[str]] = UNSET,
    virtual_machine_id: Union[Unset, list[int]] = UNSET,
    virtual_machine_id_n: Union[Unset, list[int]] = UNSET,
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

    json_cluster: Union[Unset, list[str]] = UNSET
    if not isinstance(cluster, Unset):
        json_cluster = cluster

    params["cluster"] = json_cluster

    json_cluster_n: Union[Unset, list[str]] = UNSET
    if not isinstance(cluster_n, Unset):
        json_cluster_n = cluster_n

    params["cluster__n"] = json_cluster_n

    json_cluster_id: Union[Unset, list[int]] = UNSET
    if not isinstance(cluster_id, Unset):
        json_cluster_id = cluster_id

    params["cluster_id"] = json_cluster_id

    json_cluster_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(cluster_id_n, Unset):
        json_cluster_id_n = cluster_id_n

    params["cluster_id__n"] = json_cluster_id_n

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

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    json_virtual_machine: Union[Unset, list[str]] = UNSET
    if not isinstance(virtual_machine, Unset):
        json_virtual_machine = virtual_machine

    params["virtual_machine"] = json_virtual_machine

    json_virtual_machine_n: Union[Unset, list[str]] = UNSET
    if not isinstance(virtual_machine_n, Unset):
        json_virtual_machine_n = virtual_machine_n

    params["virtual_machine__n"] = json_virtual_machine_n

    json_virtual_machine_id: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_machine_id, Unset):
        json_virtual_machine_id = virtual_machine_id

    params["virtual_machine_id"] = json_virtual_machine_id

    json_virtual_machine_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_machine_id_n, Unset):
        json_virtual_machine_id_n = virtual_machine_id_n

    params["virtual_machine_id__n"] = json_virtual_machine_id_n

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/virtualization/interfaces/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedVMInterfaceList]:
    if response.status_code == 200:
        response_200 = PaginatedVMInterfaceList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedVMInterfaceList]:
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
    cluster: Union[Unset, list[str]] = UNSET,
    cluster_n: Union[Unset, list[str]] = UNSET,
    cluster_id: Union[Unset, list[int]] = UNSET,
    cluster_id_n: Union[Unset, list[int]] = UNSET,
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
    enabled: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    l2vpn: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_n: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_id: Union[Unset, list[int]] = UNSET,
    l2vpn_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
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
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, list[int]] = UNSET,
    parent_id_n: Union[Unset, list[int]] = UNSET,
    primary_mac_address: Union[Unset, list[str]] = UNSET,
    primary_mac_address_n: Union[Unset, list[str]] = UNSET,
    primary_mac_address_id: Union[Unset, list[int]] = UNSET,
    primary_mac_address_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_machine: Union[Unset, list[str]] = UNSET,
    virtual_machine_n: Union[Unset, list[str]] = UNSET,
    virtual_machine_id: Union[Unset, list[int]] = UNSET,
    virtual_machine_id_n: Union[Unset, list[int]] = UNSET,
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
) -> Response[PaginatedVMInterfaceList]:
    """Get a list of interface objects.

    Args:
        bridge_id (Union[Unset, list[int]]):
        bridge_id_n (Union[Unset, list[int]]):
        cluster (Union[Unset, list[str]]):
        cluster_n (Union[Unset, list[str]]):
        cluster_id (Union[Unset, list[int]]):
        cluster_id_n (Union[Unset, list[int]]):
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
        enabled (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        l2vpn (Union[Unset, list[Union[None, int]]]):
        l2vpn_n (Union[Unset, list[Union[None, int]]]):
        l2vpn_id (Union[Unset, list[int]]):
        l2vpn_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
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
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        parent_id (Union[Unset, list[int]]):
        parent_id_n (Union[Unset, list[int]]):
        primary_mac_address (Union[Unset, list[str]]):
        primary_mac_address_n (Union[Unset, list[str]]):
        primary_mac_address_id (Union[Unset, list[int]]):
        primary_mac_address_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        virtual_machine (Union[Unset, list[str]]):
        virtual_machine_n (Union[Unset, list[str]]):
        virtual_machine_id (Union[Unset, list[int]]):
        virtual_machine_id_n (Union[Unset, list[int]]):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedVMInterfaceList]
    """

    kwargs = _get_kwargs(
        bridge_id=bridge_id,
        bridge_id_n=bridge_id_n,
        cluster=cluster,
        cluster_n=cluster_n,
        cluster_id=cluster_id,
        cluster_id_n=cluster_id_n,
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
        enabled=enabled,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        l2vpn=l2vpn,
        l2vpn_n=l2vpn_n,
        l2vpn_id=l2vpn_id,
        l2vpn_id_n=l2vpn_id_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
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
        offset=offset,
        ordering=ordering,
        parent_id=parent_id,
        parent_id_n=parent_id_n,
        primary_mac_address=primary_mac_address,
        primary_mac_address_n=primary_mac_address_n,
        primary_mac_address_id=primary_mac_address_id,
        primary_mac_address_id_n=primary_mac_address_id_n,
        q=q,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
        virtual_machine=virtual_machine,
        virtual_machine_n=virtual_machine_n,
        virtual_machine_id=virtual_machine_id,
        virtual_machine_id_n=virtual_machine_id_n,
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
    cluster: Union[Unset, list[str]] = UNSET,
    cluster_n: Union[Unset, list[str]] = UNSET,
    cluster_id: Union[Unset, list[int]] = UNSET,
    cluster_id_n: Union[Unset, list[int]] = UNSET,
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
    enabled: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    l2vpn: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_n: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_id: Union[Unset, list[int]] = UNSET,
    l2vpn_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
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
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, list[int]] = UNSET,
    parent_id_n: Union[Unset, list[int]] = UNSET,
    primary_mac_address: Union[Unset, list[str]] = UNSET,
    primary_mac_address_n: Union[Unset, list[str]] = UNSET,
    primary_mac_address_id: Union[Unset, list[int]] = UNSET,
    primary_mac_address_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_machine: Union[Unset, list[str]] = UNSET,
    virtual_machine_n: Union[Unset, list[str]] = UNSET,
    virtual_machine_id: Union[Unset, list[int]] = UNSET,
    virtual_machine_id_n: Union[Unset, list[int]] = UNSET,
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
) -> Optional[PaginatedVMInterfaceList]:
    """Get a list of interface objects.

    Args:
        bridge_id (Union[Unset, list[int]]):
        bridge_id_n (Union[Unset, list[int]]):
        cluster (Union[Unset, list[str]]):
        cluster_n (Union[Unset, list[str]]):
        cluster_id (Union[Unset, list[int]]):
        cluster_id_n (Union[Unset, list[int]]):
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
        enabled (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        l2vpn (Union[Unset, list[Union[None, int]]]):
        l2vpn_n (Union[Unset, list[Union[None, int]]]):
        l2vpn_id (Union[Unset, list[int]]):
        l2vpn_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
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
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        parent_id (Union[Unset, list[int]]):
        parent_id_n (Union[Unset, list[int]]):
        primary_mac_address (Union[Unset, list[str]]):
        primary_mac_address_n (Union[Unset, list[str]]):
        primary_mac_address_id (Union[Unset, list[int]]):
        primary_mac_address_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        virtual_machine (Union[Unset, list[str]]):
        virtual_machine_n (Union[Unset, list[str]]):
        virtual_machine_id (Union[Unset, list[int]]):
        virtual_machine_id_n (Union[Unset, list[int]]):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedVMInterfaceList
    """

    return sync_detailed(
        client=client,
        bridge_id=bridge_id,
        bridge_id_n=bridge_id_n,
        cluster=cluster,
        cluster_n=cluster_n,
        cluster_id=cluster_id,
        cluster_id_n=cluster_id_n,
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
        enabled=enabled,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        l2vpn=l2vpn,
        l2vpn_n=l2vpn_n,
        l2vpn_id=l2vpn_id,
        l2vpn_id_n=l2vpn_id_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
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
        offset=offset,
        ordering=ordering,
        parent_id=parent_id,
        parent_id_n=parent_id_n,
        primary_mac_address=primary_mac_address,
        primary_mac_address_n=primary_mac_address_n,
        primary_mac_address_id=primary_mac_address_id,
        primary_mac_address_id_n=primary_mac_address_id_n,
        q=q,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
        virtual_machine=virtual_machine,
        virtual_machine_n=virtual_machine_n,
        virtual_machine_id=virtual_machine_id,
        virtual_machine_id_n=virtual_machine_id_n,
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
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    bridge_id: Union[Unset, list[int]] = UNSET,
    bridge_id_n: Union[Unset, list[int]] = UNSET,
    cluster: Union[Unset, list[str]] = UNSET,
    cluster_n: Union[Unset, list[str]] = UNSET,
    cluster_id: Union[Unset, list[int]] = UNSET,
    cluster_id_n: Union[Unset, list[int]] = UNSET,
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
    enabled: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    l2vpn: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_n: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_id: Union[Unset, list[int]] = UNSET,
    l2vpn_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
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
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, list[int]] = UNSET,
    parent_id_n: Union[Unset, list[int]] = UNSET,
    primary_mac_address: Union[Unset, list[str]] = UNSET,
    primary_mac_address_n: Union[Unset, list[str]] = UNSET,
    primary_mac_address_id: Union[Unset, list[int]] = UNSET,
    primary_mac_address_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_machine: Union[Unset, list[str]] = UNSET,
    virtual_machine_n: Union[Unset, list[str]] = UNSET,
    virtual_machine_id: Union[Unset, list[int]] = UNSET,
    virtual_machine_id_n: Union[Unset, list[int]] = UNSET,
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
) -> Response[PaginatedVMInterfaceList]:
    """Get a list of interface objects.

    Args:
        bridge_id (Union[Unset, list[int]]):
        bridge_id_n (Union[Unset, list[int]]):
        cluster (Union[Unset, list[str]]):
        cluster_n (Union[Unset, list[str]]):
        cluster_id (Union[Unset, list[int]]):
        cluster_id_n (Union[Unset, list[int]]):
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
        enabled (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        l2vpn (Union[Unset, list[Union[None, int]]]):
        l2vpn_n (Union[Unset, list[Union[None, int]]]):
        l2vpn_id (Union[Unset, list[int]]):
        l2vpn_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
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
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        parent_id (Union[Unset, list[int]]):
        parent_id_n (Union[Unset, list[int]]):
        primary_mac_address (Union[Unset, list[str]]):
        primary_mac_address_n (Union[Unset, list[str]]):
        primary_mac_address_id (Union[Unset, list[int]]):
        primary_mac_address_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        virtual_machine (Union[Unset, list[str]]):
        virtual_machine_n (Union[Unset, list[str]]):
        virtual_machine_id (Union[Unset, list[int]]):
        virtual_machine_id_n (Union[Unset, list[int]]):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedVMInterfaceList]
    """

    kwargs = _get_kwargs(
        bridge_id=bridge_id,
        bridge_id_n=bridge_id_n,
        cluster=cluster,
        cluster_n=cluster_n,
        cluster_id=cluster_id,
        cluster_id_n=cluster_id_n,
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
        enabled=enabled,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        l2vpn=l2vpn,
        l2vpn_n=l2vpn_n,
        l2vpn_id=l2vpn_id,
        l2vpn_id_n=l2vpn_id_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
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
        offset=offset,
        ordering=ordering,
        parent_id=parent_id,
        parent_id_n=parent_id_n,
        primary_mac_address=primary_mac_address,
        primary_mac_address_n=primary_mac_address_n,
        primary_mac_address_id=primary_mac_address_id,
        primary_mac_address_id_n=primary_mac_address_id_n,
        q=q,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
        virtual_machine=virtual_machine,
        virtual_machine_n=virtual_machine_n,
        virtual_machine_id=virtual_machine_id,
        virtual_machine_id_n=virtual_machine_id_n,
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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    bridge_id: Union[Unset, list[int]] = UNSET,
    bridge_id_n: Union[Unset, list[int]] = UNSET,
    cluster: Union[Unset, list[str]] = UNSET,
    cluster_n: Union[Unset, list[str]] = UNSET,
    cluster_id: Union[Unset, list[int]] = UNSET,
    cluster_id_n: Union[Unset, list[int]] = UNSET,
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
    enabled: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    l2vpn: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_n: Union[Unset, list[Union[None, int]]] = UNSET,
    l2vpn_id: Union[Unset, list[int]] = UNSET,
    l2vpn_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
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
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, list[int]] = UNSET,
    parent_id_n: Union[Unset, list[int]] = UNSET,
    primary_mac_address: Union[Unset, list[str]] = UNSET,
    primary_mac_address_n: Union[Unset, list[str]] = UNSET,
    primary_mac_address_id: Union[Unset, list[int]] = UNSET,
    primary_mac_address_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_machine: Union[Unset, list[str]] = UNSET,
    virtual_machine_n: Union[Unset, list[str]] = UNSET,
    virtual_machine_id: Union[Unset, list[int]] = UNSET,
    virtual_machine_id_n: Union[Unset, list[int]] = UNSET,
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
) -> Optional[PaginatedVMInterfaceList]:
    """Get a list of interface objects.

    Args:
        bridge_id (Union[Unset, list[int]]):
        bridge_id_n (Union[Unset, list[int]]):
        cluster (Union[Unset, list[str]]):
        cluster_n (Union[Unset, list[str]]):
        cluster_id (Union[Unset, list[int]]):
        cluster_id_n (Union[Unset, list[int]]):
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
        enabled (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        l2vpn (Union[Unset, list[Union[None, int]]]):
        l2vpn_n (Union[Unset, list[Union[None, int]]]):
        l2vpn_id (Union[Unset, list[int]]):
        l2vpn_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
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
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        parent_id (Union[Unset, list[int]]):
        parent_id_n (Union[Unset, list[int]]):
        primary_mac_address (Union[Unset, list[str]]):
        primary_mac_address_n (Union[Unset, list[str]]):
        primary_mac_address_id (Union[Unset, list[int]]):
        primary_mac_address_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        virtual_machine (Union[Unset, list[str]]):
        virtual_machine_n (Union[Unset, list[str]]):
        virtual_machine_id (Union[Unset, list[int]]):
        virtual_machine_id_n (Union[Unset, list[int]]):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedVMInterfaceList
    """

    return (
        await asyncio_detailed(
            client=client,
            bridge_id=bridge_id,
            bridge_id_n=bridge_id_n,
            cluster=cluster,
            cluster_n=cluster_n,
            cluster_id=cluster_id,
            cluster_id_n=cluster_id_n,
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
            enabled=enabled,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            l2vpn=l2vpn,
            l2vpn_n=l2vpn_n,
            l2vpn_id=l2vpn_id,
            l2vpn_id_n=l2vpn_id_n,
            last_updated=last_updated,
            last_updated_empty=last_updated_empty,
            last_updated_gt=last_updated_gt,
            last_updated_gte=last_updated_gte,
            last_updated_lt=last_updated_lt,
            last_updated_lte=last_updated_lte,
            last_updated_n=last_updated_n,
            limit=limit,
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
            offset=offset,
            ordering=ordering,
            parent_id=parent_id,
            parent_id_n=parent_id_n,
            primary_mac_address=primary_mac_address,
            primary_mac_address_n=primary_mac_address_n,
            primary_mac_address_id=primary_mac_address_id,
            primary_mac_address_id_n=primary_mac_address_id_n,
            q=q,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
            updated_by_request=updated_by_request,
            virtual_machine=virtual_machine,
            virtual_machine_n=virtual_machine_n,
            virtual_machine_id=virtual_machine_id,
            virtual_machine_id_n=virtual_machine_id_n,
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
        )
    ).parsed
