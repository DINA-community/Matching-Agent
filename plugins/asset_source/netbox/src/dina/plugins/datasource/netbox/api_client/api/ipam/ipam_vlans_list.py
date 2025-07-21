import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_vlan_list import PaginatedVLANList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    available_at_site: Union[Unset, str] = UNSET,
    available_on_device: Union[Unset, str] = UNSET,
    available_on_virtualmachine: Union[Unset, str] = UNSET,
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
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[Union[None, int]]] = UNSET,
    group_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_id: Union[Unset, str] = UNSET,
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
    modified_by_request: Union[Unset, UUID] = UNSET,
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
    q: Union[Unset, str] = UNSET,
    qinq_role: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_empty: Union[Unset, bool] = UNSET,
    qinq_role_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_n: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_svlan_id: Union[Unset, list[Union[None, int]]] = UNSET,
    qinq_svlan_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    qinq_svlan_vid: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_empty: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_gt: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_gte: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_lt: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_lte: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[Union[None, int]]] = UNSET,
    site_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    vid: Union[Unset, list[int]] = UNSET,
    vid_empty: Union[Unset, bool] = UNSET,
    vid_gt: Union[Unset, list[int]] = UNSET,
    vid_gte: Union[Unset, list[int]] = UNSET,
    vid_lt: Union[Unset, list[int]] = UNSET,
    vid_lte: Union[Unset, list[int]] = UNSET,
    vid_n: Union[Unset, list[int]] = UNSET,
    vminterface_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["available_at_site"] = available_at_site

    params["available_on_device"] = available_on_device

    params["available_on_virtualmachine"] = available_on_virtualmachine

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

    json_group: Union[Unset, list[str]] = UNSET
    if not isinstance(group, Unset):
        json_group = group

    params["group"] = json_group

    json_group_n: Union[Unset, list[str]] = UNSET
    if not isinstance(group_n, Unset):
        json_group_n = group_n

    params["group__n"] = json_group_n

    json_group_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(group_id, Unset):
        json_group_id = []
        for group_id_item_data in group_id:
            group_id_item: Union[None, int]
            group_id_item = group_id_item_data
            json_group_id.append(group_id_item)

    params["group_id"] = json_group_id

    json_group_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(group_id_n, Unset):
        json_group_id_n = []
        for group_id_n_item_data in group_id_n:
            group_id_n_item: Union[None, int]
            group_id_n_item = group_id_n_item_data
            json_group_id_n.append(group_id_n_item)

    params["group_id__n"] = json_group_id_n

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

    params["interface_id"] = interface_id

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

    json_modified_by_request: Union[Unset, str] = UNSET
    if not isinstance(modified_by_request, Unset):
        json_modified_by_request = str(modified_by_request)
    params["modified_by_request"] = json_modified_by_request

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

    params["q"] = q

    json_qinq_role: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(qinq_role, Unset):
        json_qinq_role = []
        for qinq_role_item_data in qinq_role:
            qinq_role_item: Union[None, str]
            qinq_role_item = qinq_role_item_data
            json_qinq_role.append(qinq_role_item)

    params["qinq_role"] = json_qinq_role

    params["qinq_role__empty"] = qinq_role_empty

    json_qinq_role_ic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(qinq_role_ic, Unset):
        json_qinq_role_ic = []
        for qinq_role_ic_item_data in qinq_role_ic:
            qinq_role_ic_item: Union[None, str]
            qinq_role_ic_item = qinq_role_ic_item_data
            json_qinq_role_ic.append(qinq_role_ic_item)

    params["qinq_role__ic"] = json_qinq_role_ic

    json_qinq_role_ie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(qinq_role_ie, Unset):
        json_qinq_role_ie = []
        for qinq_role_ie_item_data in qinq_role_ie:
            qinq_role_ie_item: Union[None, str]
            qinq_role_ie_item = qinq_role_ie_item_data
            json_qinq_role_ie.append(qinq_role_ie_item)

    params["qinq_role__ie"] = json_qinq_role_ie

    json_qinq_role_iew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(qinq_role_iew, Unset):
        json_qinq_role_iew = []
        for qinq_role_iew_item_data in qinq_role_iew:
            qinq_role_iew_item: Union[None, str]
            qinq_role_iew_item = qinq_role_iew_item_data
            json_qinq_role_iew.append(qinq_role_iew_item)

    params["qinq_role__iew"] = json_qinq_role_iew

    json_qinq_role_isw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(qinq_role_isw, Unset):
        json_qinq_role_isw = []
        for qinq_role_isw_item_data in qinq_role_isw:
            qinq_role_isw_item: Union[None, str]
            qinq_role_isw_item = qinq_role_isw_item_data
            json_qinq_role_isw.append(qinq_role_isw_item)

    params["qinq_role__isw"] = json_qinq_role_isw

    json_qinq_role_n: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(qinq_role_n, Unset):
        json_qinq_role_n = []
        for qinq_role_n_item_data in qinq_role_n:
            qinq_role_n_item: Union[None, str]
            qinq_role_n_item = qinq_role_n_item_data
            json_qinq_role_n.append(qinq_role_n_item)

    params["qinq_role__n"] = json_qinq_role_n

    json_qinq_role_nic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(qinq_role_nic, Unset):
        json_qinq_role_nic = []
        for qinq_role_nic_item_data in qinq_role_nic:
            qinq_role_nic_item: Union[None, str]
            qinq_role_nic_item = qinq_role_nic_item_data
            json_qinq_role_nic.append(qinq_role_nic_item)

    params["qinq_role__nic"] = json_qinq_role_nic

    json_qinq_role_nie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(qinq_role_nie, Unset):
        json_qinq_role_nie = []
        for qinq_role_nie_item_data in qinq_role_nie:
            qinq_role_nie_item: Union[None, str]
            qinq_role_nie_item = qinq_role_nie_item_data
            json_qinq_role_nie.append(qinq_role_nie_item)

    params["qinq_role__nie"] = json_qinq_role_nie

    json_qinq_role_niew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(qinq_role_niew, Unset):
        json_qinq_role_niew = []
        for qinq_role_niew_item_data in qinq_role_niew:
            qinq_role_niew_item: Union[None, str]
            qinq_role_niew_item = qinq_role_niew_item_data
            json_qinq_role_niew.append(qinq_role_niew_item)

    params["qinq_role__niew"] = json_qinq_role_niew

    json_qinq_role_nisw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(qinq_role_nisw, Unset):
        json_qinq_role_nisw = []
        for qinq_role_nisw_item_data in qinq_role_nisw:
            qinq_role_nisw_item: Union[None, str]
            qinq_role_nisw_item = qinq_role_nisw_item_data
            json_qinq_role_nisw.append(qinq_role_nisw_item)

    params["qinq_role__nisw"] = json_qinq_role_nisw

    json_qinq_svlan_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(qinq_svlan_id, Unset):
        json_qinq_svlan_id = []
        for qinq_svlan_id_item_data in qinq_svlan_id:
            qinq_svlan_id_item: Union[None, int]
            qinq_svlan_id_item = qinq_svlan_id_item_data
            json_qinq_svlan_id.append(qinq_svlan_id_item)

    params["qinq_svlan_id"] = json_qinq_svlan_id

    json_qinq_svlan_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(qinq_svlan_id_n, Unset):
        json_qinq_svlan_id_n = []
        for qinq_svlan_id_n_item_data in qinq_svlan_id_n:
            qinq_svlan_id_n_item: Union[None, int]
            qinq_svlan_id_n_item = qinq_svlan_id_n_item_data
            json_qinq_svlan_id_n.append(qinq_svlan_id_n_item)

    params["qinq_svlan_id__n"] = json_qinq_svlan_id_n

    json_qinq_svlan_vid: Union[Unset, list[int]] = UNSET
    if not isinstance(qinq_svlan_vid, Unset):
        json_qinq_svlan_vid = qinq_svlan_vid

    params["qinq_svlan_vid"] = json_qinq_svlan_vid

    json_qinq_svlan_vid_empty: Union[Unset, list[int]] = UNSET
    if not isinstance(qinq_svlan_vid_empty, Unset):
        json_qinq_svlan_vid_empty = qinq_svlan_vid_empty

    params["qinq_svlan_vid__empty"] = json_qinq_svlan_vid_empty

    json_qinq_svlan_vid_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(qinq_svlan_vid_gt, Unset):
        json_qinq_svlan_vid_gt = qinq_svlan_vid_gt

    params["qinq_svlan_vid__gt"] = json_qinq_svlan_vid_gt

    json_qinq_svlan_vid_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(qinq_svlan_vid_gte, Unset):
        json_qinq_svlan_vid_gte = qinq_svlan_vid_gte

    params["qinq_svlan_vid__gte"] = json_qinq_svlan_vid_gte

    json_qinq_svlan_vid_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(qinq_svlan_vid_lt, Unset):
        json_qinq_svlan_vid_lt = qinq_svlan_vid_lt

    params["qinq_svlan_vid__lt"] = json_qinq_svlan_vid_lt

    json_qinq_svlan_vid_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(qinq_svlan_vid_lte, Unset):
        json_qinq_svlan_vid_lte = qinq_svlan_vid_lte

    params["qinq_svlan_vid__lte"] = json_qinq_svlan_vid_lte

    json_qinq_svlan_vid_n: Union[Unset, list[int]] = UNSET
    if not isinstance(qinq_svlan_vid_n, Unset):
        json_qinq_svlan_vid_n = qinq_svlan_vid_n

    params["qinq_svlan_vid__n"] = json_qinq_svlan_vid_n

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

    json_role_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(role_id, Unset):
        json_role_id = []
        for role_id_item_data in role_id:
            role_id_item: Union[None, int]
            role_id_item = role_id_item_data
            json_role_id.append(role_id_item)

    params["role_id"] = json_role_id

    json_role_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(role_id_n, Unset):
        json_role_id_n = []
        for role_id_n_item_data in role_id_n:
            role_id_n_item: Union[None, int]
            role_id_n_item = role_id_n_item_data
            json_role_id_n.append(role_id_n_item)

    params["role_id__n"] = json_role_id_n

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

    json_site_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(site_id, Unset):
        json_site_id = []
        for site_id_item_data in site_id:
            site_id_item: Union[None, int]
            site_id_item = site_id_item_data
            json_site_id.append(site_id_item)

    params["site_id"] = json_site_id

    json_site_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(site_id_n, Unset):
        json_site_id_n = []
        for site_id_n_item_data in site_id_n:
            site_id_n_item: Union[None, int]
            site_id_n_item = site_id_n_item_data
            json_site_id_n.append(site_id_n_item)

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

    json_vid: Union[Unset, list[int]] = UNSET
    if not isinstance(vid, Unset):
        json_vid = vid

    params["vid"] = json_vid

    params["vid__empty"] = vid_empty

    json_vid_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(vid_gt, Unset):
        json_vid_gt = vid_gt

    params["vid__gt"] = json_vid_gt

    json_vid_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(vid_gte, Unset):
        json_vid_gte = vid_gte

    params["vid__gte"] = json_vid_gte

    json_vid_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(vid_lt, Unset):
        json_vid_lt = vid_lt

    params["vid__lt"] = json_vid_lt

    json_vid_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(vid_lte, Unset):
        json_vid_lte = vid_lte

    params["vid__lte"] = json_vid_lte

    json_vid_n: Union[Unset, list[int]] = UNSET
    if not isinstance(vid_n, Unset):
        json_vid_n = vid_n

    params["vid__n"] = json_vid_n

    params["vminterface_id"] = vminterface_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/ipam/vlans/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedVLANList]:
    if response.status_code == 200:
        response_200 = PaginatedVLANList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedVLANList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    available_at_site: Union[Unset, str] = UNSET,
    available_on_device: Union[Unset, str] = UNSET,
    available_on_virtualmachine: Union[Unset, str] = UNSET,
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
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[Union[None, int]]] = UNSET,
    group_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_id: Union[Unset, str] = UNSET,
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
    modified_by_request: Union[Unset, UUID] = UNSET,
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
    q: Union[Unset, str] = UNSET,
    qinq_role: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_empty: Union[Unset, bool] = UNSET,
    qinq_role_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_n: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_svlan_id: Union[Unset, list[Union[None, int]]] = UNSET,
    qinq_svlan_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    qinq_svlan_vid: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_empty: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_gt: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_gte: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_lt: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_lte: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[Union[None, int]]] = UNSET,
    site_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    vid: Union[Unset, list[int]] = UNSET,
    vid_empty: Union[Unset, bool] = UNSET,
    vid_gt: Union[Unset, list[int]] = UNSET,
    vid_gte: Union[Unset, list[int]] = UNSET,
    vid_lt: Union[Unset, list[int]] = UNSET,
    vid_lte: Union[Unset, list[int]] = UNSET,
    vid_n: Union[Unset, list[int]] = UNSET,
    vminterface_id: Union[Unset, str] = UNSET,
) -> Response[PaginatedVLANList]:
    """Get a list of VLAN objects.

    Args:
        available_at_site (Union[Unset, str]):
        available_on_device (Union[Unset, str]):
        available_on_virtualmachine (Union[Unset, str]):
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
        group (Union[Unset, list[str]]):
        group_n (Union[Unset, list[str]]):
        group_id (Union[Unset, list[Union[None, int]]]):
        group_id_n (Union[Unset, list[Union[None, int]]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_id (Union[Unset, str]):
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
        modified_by_request (Union[Unset, UUID]):
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
        q (Union[Unset, str]):
        qinq_role (Union[Unset, list[Union[None, str]]]):
        qinq_role_empty (Union[Unset, bool]):
        qinq_role_ic (Union[Unset, list[Union[None, str]]]):
        qinq_role_ie (Union[Unset, list[Union[None, str]]]):
        qinq_role_iew (Union[Unset, list[Union[None, str]]]):
        qinq_role_isw (Union[Unset, list[Union[None, str]]]):
        qinq_role_n (Union[Unset, list[Union[None, str]]]):
        qinq_role_nic (Union[Unset, list[Union[None, str]]]):
        qinq_role_nie (Union[Unset, list[Union[None, str]]]):
        qinq_role_niew (Union[Unset, list[Union[None, str]]]):
        qinq_role_nisw (Union[Unset, list[Union[None, str]]]):
        qinq_svlan_id (Union[Unset, list[Union[None, int]]]):
        qinq_svlan_id_n (Union[Unset, list[Union[None, int]]]):
        qinq_svlan_vid (Union[Unset, list[int]]):
        qinq_svlan_vid_empty (Union[Unset, list[int]]):
        qinq_svlan_vid_gt (Union[Unset, list[int]]):
        qinq_svlan_vid_gte (Union[Unset, list[int]]):
        qinq_svlan_vid_lt (Union[Unset, list[int]]):
        qinq_svlan_vid_lte (Union[Unset, list[int]]):
        qinq_svlan_vid_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[Union[None, int]]]):
        role_id_n (Union[Unset, list[Union[None, int]]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[Union[None, int]]]):
        site_id_n (Union[Unset, list[Union[None, int]]]):
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
        vid (Union[Unset, list[int]]):
        vid_empty (Union[Unset, bool]):
        vid_gt (Union[Unset, list[int]]):
        vid_gte (Union[Unset, list[int]]):
        vid_lt (Union[Unset, list[int]]):
        vid_lte (Union[Unset, list[int]]):
        vid_n (Union[Unset, list[int]]):
        vminterface_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedVLANList]
    """

    kwargs = _get_kwargs(
        available_at_site=available_at_site,
        available_on_device=available_on_device,
        available_on_virtualmachine=available_on_virtualmachine,
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
        group=group,
        group_n=group_n,
        group_id=group_id,
        group_id_n=group_id_n,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface_id=interface_id,
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
        modified_by_request=modified_by_request,
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
        q=q,
        qinq_role=qinq_role,
        qinq_role_empty=qinq_role_empty,
        qinq_role_ic=qinq_role_ic,
        qinq_role_ie=qinq_role_ie,
        qinq_role_iew=qinq_role_iew,
        qinq_role_isw=qinq_role_isw,
        qinq_role_n=qinq_role_n,
        qinq_role_nic=qinq_role_nic,
        qinq_role_nie=qinq_role_nie,
        qinq_role_niew=qinq_role_niew,
        qinq_role_nisw=qinq_role_nisw,
        qinq_svlan_id=qinq_svlan_id,
        qinq_svlan_id_n=qinq_svlan_id_n,
        qinq_svlan_vid=qinq_svlan_vid,
        qinq_svlan_vid_empty=qinq_svlan_vid_empty,
        qinq_svlan_vid_gt=qinq_svlan_vid_gt,
        qinq_svlan_vid_gte=qinq_svlan_vid_gte,
        qinq_svlan_vid_lt=qinq_svlan_vid_lt,
        qinq_svlan_vid_lte=qinq_svlan_vid_lte,
        qinq_svlan_vid_n=qinq_svlan_vid_n,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
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
        vid=vid,
        vid_empty=vid_empty,
        vid_gt=vid_gt,
        vid_gte=vid_gte,
        vid_lt=vid_lt,
        vid_lte=vid_lte,
        vid_n=vid_n,
        vminterface_id=vminterface_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    available_at_site: Union[Unset, str] = UNSET,
    available_on_device: Union[Unset, str] = UNSET,
    available_on_virtualmachine: Union[Unset, str] = UNSET,
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
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[Union[None, int]]] = UNSET,
    group_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_id: Union[Unset, str] = UNSET,
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
    modified_by_request: Union[Unset, UUID] = UNSET,
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
    q: Union[Unset, str] = UNSET,
    qinq_role: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_empty: Union[Unset, bool] = UNSET,
    qinq_role_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_n: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_svlan_id: Union[Unset, list[Union[None, int]]] = UNSET,
    qinq_svlan_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    qinq_svlan_vid: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_empty: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_gt: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_gte: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_lt: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_lte: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[Union[None, int]]] = UNSET,
    site_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    vid: Union[Unset, list[int]] = UNSET,
    vid_empty: Union[Unset, bool] = UNSET,
    vid_gt: Union[Unset, list[int]] = UNSET,
    vid_gte: Union[Unset, list[int]] = UNSET,
    vid_lt: Union[Unset, list[int]] = UNSET,
    vid_lte: Union[Unset, list[int]] = UNSET,
    vid_n: Union[Unset, list[int]] = UNSET,
    vminterface_id: Union[Unset, str] = UNSET,
) -> Optional[PaginatedVLANList]:
    """Get a list of VLAN objects.

    Args:
        available_at_site (Union[Unset, str]):
        available_on_device (Union[Unset, str]):
        available_on_virtualmachine (Union[Unset, str]):
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
        group (Union[Unset, list[str]]):
        group_n (Union[Unset, list[str]]):
        group_id (Union[Unset, list[Union[None, int]]]):
        group_id_n (Union[Unset, list[Union[None, int]]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_id (Union[Unset, str]):
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
        modified_by_request (Union[Unset, UUID]):
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
        q (Union[Unset, str]):
        qinq_role (Union[Unset, list[Union[None, str]]]):
        qinq_role_empty (Union[Unset, bool]):
        qinq_role_ic (Union[Unset, list[Union[None, str]]]):
        qinq_role_ie (Union[Unset, list[Union[None, str]]]):
        qinq_role_iew (Union[Unset, list[Union[None, str]]]):
        qinq_role_isw (Union[Unset, list[Union[None, str]]]):
        qinq_role_n (Union[Unset, list[Union[None, str]]]):
        qinq_role_nic (Union[Unset, list[Union[None, str]]]):
        qinq_role_nie (Union[Unset, list[Union[None, str]]]):
        qinq_role_niew (Union[Unset, list[Union[None, str]]]):
        qinq_role_nisw (Union[Unset, list[Union[None, str]]]):
        qinq_svlan_id (Union[Unset, list[Union[None, int]]]):
        qinq_svlan_id_n (Union[Unset, list[Union[None, int]]]):
        qinq_svlan_vid (Union[Unset, list[int]]):
        qinq_svlan_vid_empty (Union[Unset, list[int]]):
        qinq_svlan_vid_gt (Union[Unset, list[int]]):
        qinq_svlan_vid_gte (Union[Unset, list[int]]):
        qinq_svlan_vid_lt (Union[Unset, list[int]]):
        qinq_svlan_vid_lte (Union[Unset, list[int]]):
        qinq_svlan_vid_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[Union[None, int]]]):
        role_id_n (Union[Unset, list[Union[None, int]]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[Union[None, int]]]):
        site_id_n (Union[Unset, list[Union[None, int]]]):
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
        vid (Union[Unset, list[int]]):
        vid_empty (Union[Unset, bool]):
        vid_gt (Union[Unset, list[int]]):
        vid_gte (Union[Unset, list[int]]):
        vid_lt (Union[Unset, list[int]]):
        vid_lte (Union[Unset, list[int]]):
        vid_n (Union[Unset, list[int]]):
        vminterface_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedVLANList
    """

    return sync_detailed(
        client=client,
        available_at_site=available_at_site,
        available_on_device=available_on_device,
        available_on_virtualmachine=available_on_virtualmachine,
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
        group=group,
        group_n=group_n,
        group_id=group_id,
        group_id_n=group_id_n,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface_id=interface_id,
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
        modified_by_request=modified_by_request,
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
        q=q,
        qinq_role=qinq_role,
        qinq_role_empty=qinq_role_empty,
        qinq_role_ic=qinq_role_ic,
        qinq_role_ie=qinq_role_ie,
        qinq_role_iew=qinq_role_iew,
        qinq_role_isw=qinq_role_isw,
        qinq_role_n=qinq_role_n,
        qinq_role_nic=qinq_role_nic,
        qinq_role_nie=qinq_role_nie,
        qinq_role_niew=qinq_role_niew,
        qinq_role_nisw=qinq_role_nisw,
        qinq_svlan_id=qinq_svlan_id,
        qinq_svlan_id_n=qinq_svlan_id_n,
        qinq_svlan_vid=qinq_svlan_vid,
        qinq_svlan_vid_empty=qinq_svlan_vid_empty,
        qinq_svlan_vid_gt=qinq_svlan_vid_gt,
        qinq_svlan_vid_gte=qinq_svlan_vid_gte,
        qinq_svlan_vid_lt=qinq_svlan_vid_lt,
        qinq_svlan_vid_lte=qinq_svlan_vid_lte,
        qinq_svlan_vid_n=qinq_svlan_vid_n,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
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
        vid=vid,
        vid_empty=vid_empty,
        vid_gt=vid_gt,
        vid_gte=vid_gte,
        vid_lt=vid_lt,
        vid_lte=vid_lte,
        vid_n=vid_n,
        vminterface_id=vminterface_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    available_at_site: Union[Unset, str] = UNSET,
    available_on_device: Union[Unset, str] = UNSET,
    available_on_virtualmachine: Union[Unset, str] = UNSET,
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
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[Union[None, int]]] = UNSET,
    group_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_id: Union[Unset, str] = UNSET,
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
    modified_by_request: Union[Unset, UUID] = UNSET,
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
    q: Union[Unset, str] = UNSET,
    qinq_role: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_empty: Union[Unset, bool] = UNSET,
    qinq_role_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_n: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_svlan_id: Union[Unset, list[Union[None, int]]] = UNSET,
    qinq_svlan_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    qinq_svlan_vid: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_empty: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_gt: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_gte: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_lt: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_lte: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[Union[None, int]]] = UNSET,
    site_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    vid: Union[Unset, list[int]] = UNSET,
    vid_empty: Union[Unset, bool] = UNSET,
    vid_gt: Union[Unset, list[int]] = UNSET,
    vid_gte: Union[Unset, list[int]] = UNSET,
    vid_lt: Union[Unset, list[int]] = UNSET,
    vid_lte: Union[Unset, list[int]] = UNSET,
    vid_n: Union[Unset, list[int]] = UNSET,
    vminterface_id: Union[Unset, str] = UNSET,
) -> Response[PaginatedVLANList]:
    """Get a list of VLAN objects.

    Args:
        available_at_site (Union[Unset, str]):
        available_on_device (Union[Unset, str]):
        available_on_virtualmachine (Union[Unset, str]):
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
        group (Union[Unset, list[str]]):
        group_n (Union[Unset, list[str]]):
        group_id (Union[Unset, list[Union[None, int]]]):
        group_id_n (Union[Unset, list[Union[None, int]]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_id (Union[Unset, str]):
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
        modified_by_request (Union[Unset, UUID]):
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
        q (Union[Unset, str]):
        qinq_role (Union[Unset, list[Union[None, str]]]):
        qinq_role_empty (Union[Unset, bool]):
        qinq_role_ic (Union[Unset, list[Union[None, str]]]):
        qinq_role_ie (Union[Unset, list[Union[None, str]]]):
        qinq_role_iew (Union[Unset, list[Union[None, str]]]):
        qinq_role_isw (Union[Unset, list[Union[None, str]]]):
        qinq_role_n (Union[Unset, list[Union[None, str]]]):
        qinq_role_nic (Union[Unset, list[Union[None, str]]]):
        qinq_role_nie (Union[Unset, list[Union[None, str]]]):
        qinq_role_niew (Union[Unset, list[Union[None, str]]]):
        qinq_role_nisw (Union[Unset, list[Union[None, str]]]):
        qinq_svlan_id (Union[Unset, list[Union[None, int]]]):
        qinq_svlan_id_n (Union[Unset, list[Union[None, int]]]):
        qinq_svlan_vid (Union[Unset, list[int]]):
        qinq_svlan_vid_empty (Union[Unset, list[int]]):
        qinq_svlan_vid_gt (Union[Unset, list[int]]):
        qinq_svlan_vid_gte (Union[Unset, list[int]]):
        qinq_svlan_vid_lt (Union[Unset, list[int]]):
        qinq_svlan_vid_lte (Union[Unset, list[int]]):
        qinq_svlan_vid_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[Union[None, int]]]):
        role_id_n (Union[Unset, list[Union[None, int]]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[Union[None, int]]]):
        site_id_n (Union[Unset, list[Union[None, int]]]):
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
        vid (Union[Unset, list[int]]):
        vid_empty (Union[Unset, bool]):
        vid_gt (Union[Unset, list[int]]):
        vid_gte (Union[Unset, list[int]]):
        vid_lt (Union[Unset, list[int]]):
        vid_lte (Union[Unset, list[int]]):
        vid_n (Union[Unset, list[int]]):
        vminterface_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedVLANList]
    """

    kwargs = _get_kwargs(
        available_at_site=available_at_site,
        available_on_device=available_on_device,
        available_on_virtualmachine=available_on_virtualmachine,
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
        group=group,
        group_n=group_n,
        group_id=group_id,
        group_id_n=group_id_n,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface_id=interface_id,
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
        modified_by_request=modified_by_request,
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
        q=q,
        qinq_role=qinq_role,
        qinq_role_empty=qinq_role_empty,
        qinq_role_ic=qinq_role_ic,
        qinq_role_ie=qinq_role_ie,
        qinq_role_iew=qinq_role_iew,
        qinq_role_isw=qinq_role_isw,
        qinq_role_n=qinq_role_n,
        qinq_role_nic=qinq_role_nic,
        qinq_role_nie=qinq_role_nie,
        qinq_role_niew=qinq_role_niew,
        qinq_role_nisw=qinq_role_nisw,
        qinq_svlan_id=qinq_svlan_id,
        qinq_svlan_id_n=qinq_svlan_id_n,
        qinq_svlan_vid=qinq_svlan_vid,
        qinq_svlan_vid_empty=qinq_svlan_vid_empty,
        qinq_svlan_vid_gt=qinq_svlan_vid_gt,
        qinq_svlan_vid_gte=qinq_svlan_vid_gte,
        qinq_svlan_vid_lt=qinq_svlan_vid_lt,
        qinq_svlan_vid_lte=qinq_svlan_vid_lte,
        qinq_svlan_vid_n=qinq_svlan_vid_n,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
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
        vid=vid,
        vid_empty=vid_empty,
        vid_gt=vid_gt,
        vid_gte=vid_gte,
        vid_lt=vid_lt,
        vid_lte=vid_lte,
        vid_n=vid_n,
        vminterface_id=vminterface_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    available_at_site: Union[Unset, str] = UNSET,
    available_on_device: Union[Unset, str] = UNSET,
    available_on_virtualmachine: Union[Unset, str] = UNSET,
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
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[Union[None, int]]] = UNSET,
    group_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_id: Union[Unset, str] = UNSET,
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
    modified_by_request: Union[Unset, UUID] = UNSET,
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
    q: Union[Unset, str] = UNSET,
    qinq_role: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_empty: Union[Unset, bool] = UNSET,
    qinq_role_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_n: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_role_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    qinq_svlan_id: Union[Unset, list[Union[None, int]]] = UNSET,
    qinq_svlan_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    qinq_svlan_vid: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_empty: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_gt: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_gte: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_lt: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_lte: Union[Unset, list[int]] = UNSET,
    qinq_svlan_vid_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[Union[None, int]]] = UNSET,
    site_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    vid: Union[Unset, list[int]] = UNSET,
    vid_empty: Union[Unset, bool] = UNSET,
    vid_gt: Union[Unset, list[int]] = UNSET,
    vid_gte: Union[Unset, list[int]] = UNSET,
    vid_lt: Union[Unset, list[int]] = UNSET,
    vid_lte: Union[Unset, list[int]] = UNSET,
    vid_n: Union[Unset, list[int]] = UNSET,
    vminterface_id: Union[Unset, str] = UNSET,
) -> Optional[PaginatedVLANList]:
    """Get a list of VLAN objects.

    Args:
        available_at_site (Union[Unset, str]):
        available_on_device (Union[Unset, str]):
        available_on_virtualmachine (Union[Unset, str]):
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
        group (Union[Unset, list[str]]):
        group_n (Union[Unset, list[str]]):
        group_id (Union[Unset, list[Union[None, int]]]):
        group_id_n (Union[Unset, list[Union[None, int]]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_id (Union[Unset, str]):
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
        modified_by_request (Union[Unset, UUID]):
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
        q (Union[Unset, str]):
        qinq_role (Union[Unset, list[Union[None, str]]]):
        qinq_role_empty (Union[Unset, bool]):
        qinq_role_ic (Union[Unset, list[Union[None, str]]]):
        qinq_role_ie (Union[Unset, list[Union[None, str]]]):
        qinq_role_iew (Union[Unset, list[Union[None, str]]]):
        qinq_role_isw (Union[Unset, list[Union[None, str]]]):
        qinq_role_n (Union[Unset, list[Union[None, str]]]):
        qinq_role_nic (Union[Unset, list[Union[None, str]]]):
        qinq_role_nie (Union[Unset, list[Union[None, str]]]):
        qinq_role_niew (Union[Unset, list[Union[None, str]]]):
        qinq_role_nisw (Union[Unset, list[Union[None, str]]]):
        qinq_svlan_id (Union[Unset, list[Union[None, int]]]):
        qinq_svlan_id_n (Union[Unset, list[Union[None, int]]]):
        qinq_svlan_vid (Union[Unset, list[int]]):
        qinq_svlan_vid_empty (Union[Unset, list[int]]):
        qinq_svlan_vid_gt (Union[Unset, list[int]]):
        qinq_svlan_vid_gte (Union[Unset, list[int]]):
        qinq_svlan_vid_lt (Union[Unset, list[int]]):
        qinq_svlan_vid_lte (Union[Unset, list[int]]):
        qinq_svlan_vid_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[Union[None, int]]]):
        role_id_n (Union[Unset, list[Union[None, int]]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[Union[None, int]]]):
        site_id_n (Union[Unset, list[Union[None, int]]]):
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
        vid (Union[Unset, list[int]]):
        vid_empty (Union[Unset, bool]):
        vid_gt (Union[Unset, list[int]]):
        vid_gte (Union[Unset, list[int]]):
        vid_lt (Union[Unset, list[int]]):
        vid_lte (Union[Unset, list[int]]):
        vid_n (Union[Unset, list[int]]):
        vminterface_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedVLANList
    """

    return (
        await asyncio_detailed(
            client=client,
            available_at_site=available_at_site,
            available_on_device=available_on_device,
            available_on_virtualmachine=available_on_virtualmachine,
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
            group=group,
            group_n=group_n,
            group_id=group_id,
            group_id_n=group_id_n,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            interface_id=interface_id,
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
            modified_by_request=modified_by_request,
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
            q=q,
            qinq_role=qinq_role,
            qinq_role_empty=qinq_role_empty,
            qinq_role_ic=qinq_role_ic,
            qinq_role_ie=qinq_role_ie,
            qinq_role_iew=qinq_role_iew,
            qinq_role_isw=qinq_role_isw,
            qinq_role_n=qinq_role_n,
            qinq_role_nic=qinq_role_nic,
            qinq_role_nie=qinq_role_nie,
            qinq_role_niew=qinq_role_niew,
            qinq_role_nisw=qinq_role_nisw,
            qinq_svlan_id=qinq_svlan_id,
            qinq_svlan_id_n=qinq_svlan_id_n,
            qinq_svlan_vid=qinq_svlan_vid,
            qinq_svlan_vid_empty=qinq_svlan_vid_empty,
            qinq_svlan_vid_gt=qinq_svlan_vid_gt,
            qinq_svlan_vid_gte=qinq_svlan_vid_gte,
            qinq_svlan_vid_lt=qinq_svlan_vid_lt,
            qinq_svlan_vid_lte=qinq_svlan_vid_lte,
            qinq_svlan_vid_n=qinq_svlan_vid_n,
            region=region,
            region_n=region_n,
            region_id=region_id,
            region_id_n=region_id_n,
            role=role,
            role_n=role_n,
            role_id=role_id,
            role_id_n=role_id_n,
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
            vid=vid,
            vid_empty=vid_empty,
            vid_gt=vid_gt,
            vid_gte=vid_gte,
            vid_lt=vid_lt,
            vid_lte=vid_lte,
            vid_n=vid_n,
            vminterface_id=vminterface_id,
        )
    ).parsed
