import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_prefix_list import PaginatedPrefixList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    children: Union[Unset, list[int]] = UNSET,
    children_empty: Union[Unset, list[int]] = UNSET,
    children_gt: Union[Unset, list[int]] = UNSET,
    children_gte: Union[Unset, list[int]] = UNSET,
    children_lt: Union[Unset, list[int]] = UNSET,
    children_lte: Union[Unset, list[int]] = UNSET,
    children_n: Union[Unset, list[int]] = UNSET,
    contact: Union[Unset, list[int]] = UNSET,
    contact_n: Union[Unset, list[int]] = UNSET,
    contact_group: Union[Unset, list[str]] = UNSET,
    contact_group_n: Union[Unset, list[str]] = UNSET,
    contact_role: Union[Unset, list[int]] = UNSET,
    contact_role_n: Union[Unset, list[int]] = UNSET,
    contains: Union[Unset, str] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    depth: Union[Unset, list[int]] = UNSET,
    depth_empty: Union[Unset, list[int]] = UNSET,
    depth_gt: Union[Unset, list[int]] = UNSET,
    depth_gte: Union[Unset, list[int]] = UNSET,
    depth_lt: Union[Unset, list[int]] = UNSET,
    depth_lte: Union[Unset, list[int]] = UNSET,
    depth_n: Union[Unset, list[int]] = UNSET,
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
    family: Union[Unset, float] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_pool: Union[Unset, bool] = UNSET,
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
    location_id: Union[Unset, list[str]] = UNSET,
    location_id_n: Union[Unset, list[str]] = UNSET,
    mark_utilized: Union[Unset, bool] = UNSET,
    mask_length: Union[Unset, list[int]] = UNSET,
    mask_length_gte: Union[Unset, float] = UNSET,
    mask_length_lte: Union[Unset, float] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    prefix: Union[Unset, list[str]] = UNSET,
    present_in_vrf: Union[Unset, str] = UNSET,
    present_in_vrf_id: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    scope_id: Union[Unset, list[int]] = UNSET,
    scope_id_empty: Union[Unset, bool] = UNSET,
    scope_id_gt: Union[Unset, list[int]] = UNSET,
    scope_id_gte: Union[Unset, list[int]] = UNSET,
    scope_id_lt: Union[Unset, list[int]] = UNSET,
    scope_id_lte: Union[Unset, list[int]] = UNSET,
    scope_id_n: Union[Unset, list[int]] = UNSET,
    scope_type: Union[Unset, str] = UNSET,
    scope_type_n: Union[Unset, str] = UNSET,
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
    vlan_group: Union[Unset, list[str]] = UNSET,
    vlan_group_n: Union[Unset, list[str]] = UNSET,
    vlan_group_id: Union[Unset, list[int]] = UNSET,
    vlan_group_id_n: Union[Unset, list[int]] = UNSET,
    vlan_id: Union[Unset, list[Union[None, int]]] = UNSET,
    vlan_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    vlan_vid: Union[Unset, int] = UNSET,
    vlan_vid_empty: Union[Unset, int] = UNSET,
    vlan_vid_gt: Union[Unset, int] = UNSET,
    vlan_vid_gte: Union[Unset, int] = UNSET,
    vlan_vid_lt: Union[Unset, int] = UNSET,
    vlan_vid_lte: Union[Unset, int] = UNSET,
    vlan_vid_n: Union[Unset, int] = UNSET,
    vrf: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_n: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_id: Union[Unset, list[Union[None, int]]] = UNSET,
    vrf_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    within: Union[Unset, str] = UNSET,
    within_include: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_children: Union[Unset, list[int]] = UNSET
    if not isinstance(children, Unset):
        json_children = children

    params["children"] = json_children

    json_children_empty: Union[Unset, list[int]] = UNSET
    if not isinstance(children_empty, Unset):
        json_children_empty = children_empty

    params["children__empty"] = json_children_empty

    json_children_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(children_gt, Unset):
        json_children_gt = children_gt

    params["children__gt"] = json_children_gt

    json_children_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(children_gte, Unset):
        json_children_gte = children_gte

    params["children__gte"] = json_children_gte

    json_children_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(children_lt, Unset):
        json_children_lt = children_lt

    params["children__lt"] = json_children_lt

    json_children_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(children_lte, Unset):
        json_children_lte = children_lte

    params["children__lte"] = json_children_lte

    json_children_n: Union[Unset, list[int]] = UNSET
    if not isinstance(children_n, Unset):
        json_children_n = children_n

    params["children__n"] = json_children_n

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

    params["contains"] = contains

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

    json_depth: Union[Unset, list[int]] = UNSET
    if not isinstance(depth, Unset):
        json_depth = depth

    params["depth"] = json_depth

    json_depth_empty: Union[Unset, list[int]] = UNSET
    if not isinstance(depth_empty, Unset):
        json_depth_empty = depth_empty

    params["depth__empty"] = json_depth_empty

    json_depth_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(depth_gt, Unset):
        json_depth_gt = depth_gt

    params["depth__gt"] = json_depth_gt

    json_depth_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(depth_gte, Unset):
        json_depth_gte = depth_gte

    params["depth__gte"] = json_depth_gte

    json_depth_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(depth_lt, Unset):
        json_depth_lt = depth_lt

    params["depth__lt"] = json_depth_lt

    json_depth_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(depth_lte, Unset):
        json_depth_lte = depth_lte

    params["depth__lte"] = json_depth_lte

    json_depth_n: Union[Unset, list[int]] = UNSET
    if not isinstance(depth_n, Unset):
        json_depth_n = depth_n

    params["depth__n"] = json_depth_n

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

    params["family"] = family

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

    params["is_pool"] = is_pool

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

    json_location_id: Union[Unset, list[str]] = UNSET
    if not isinstance(location_id, Unset):
        json_location_id = location_id

    params["location_id"] = json_location_id

    json_location_id_n: Union[Unset, list[str]] = UNSET
    if not isinstance(location_id_n, Unset):
        json_location_id_n = location_id_n

    params["location_id__n"] = json_location_id_n

    params["mark_utilized"] = mark_utilized

    json_mask_length: Union[Unset, list[int]] = UNSET
    if not isinstance(mask_length, Unset):
        json_mask_length = mask_length

    params["mask_length"] = json_mask_length

    params["mask_length__gte"] = mask_length_gte

    params["mask_length__lte"] = mask_length_lte

    json_modified_by_request: Union[Unset, str] = UNSET
    if not isinstance(modified_by_request, Unset):
        json_modified_by_request = str(modified_by_request)
    params["modified_by_request"] = json_modified_by_request

    params["offset"] = offset

    params["ordering"] = ordering

    json_prefix: Union[Unset, list[str]] = UNSET
    if not isinstance(prefix, Unset):
        json_prefix = prefix

    params["prefix"] = json_prefix

    params["present_in_vrf"] = present_in_vrf

    params["present_in_vrf_id"] = present_in_vrf_id

    params["q"] = q

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

    json_scope_id: Union[Unset, list[int]] = UNSET
    if not isinstance(scope_id, Unset):
        json_scope_id = scope_id

    params["scope_id"] = json_scope_id

    params["scope_id__empty"] = scope_id_empty

    json_scope_id_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(scope_id_gt, Unset):
        json_scope_id_gt = scope_id_gt

    params["scope_id__gt"] = json_scope_id_gt

    json_scope_id_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(scope_id_gte, Unset):
        json_scope_id_gte = scope_id_gte

    params["scope_id__gte"] = json_scope_id_gte

    json_scope_id_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(scope_id_lt, Unset):
        json_scope_id_lt = scope_id_lt

    params["scope_id__lt"] = json_scope_id_lt

    json_scope_id_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(scope_id_lte, Unset):
        json_scope_id_lte = scope_id_lte

    params["scope_id__lte"] = json_scope_id_lte

    json_scope_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(scope_id_n, Unset):
        json_scope_id_n = scope_id_n

    params["scope_id__n"] = json_scope_id_n

    params["scope_type"] = scope_type

    params["scope_type__n"] = scope_type_n

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

    json_vlan_group: Union[Unset, list[str]] = UNSET
    if not isinstance(vlan_group, Unset):
        json_vlan_group = vlan_group

    params["vlan_group"] = json_vlan_group

    json_vlan_group_n: Union[Unset, list[str]] = UNSET
    if not isinstance(vlan_group_n, Unset):
        json_vlan_group_n = vlan_group_n

    params["vlan_group__n"] = json_vlan_group_n

    json_vlan_group_id: Union[Unset, list[int]] = UNSET
    if not isinstance(vlan_group_id, Unset):
        json_vlan_group_id = vlan_group_id

    params["vlan_group_id"] = json_vlan_group_id

    json_vlan_group_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(vlan_group_id_n, Unset):
        json_vlan_group_id_n = vlan_group_id_n

    params["vlan_group_id__n"] = json_vlan_group_id_n

    json_vlan_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(vlan_id, Unset):
        json_vlan_id = []
        for vlan_id_item_data in vlan_id:
            vlan_id_item: Union[None, int]
            vlan_id_item = vlan_id_item_data
            json_vlan_id.append(vlan_id_item)

    params["vlan_id"] = json_vlan_id

    json_vlan_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(vlan_id_n, Unset):
        json_vlan_id_n = []
        for vlan_id_n_item_data in vlan_id_n:
            vlan_id_n_item: Union[None, int]
            vlan_id_n_item = vlan_id_n_item_data
            json_vlan_id_n.append(vlan_id_n_item)

    params["vlan_id__n"] = json_vlan_id_n

    params["vlan_vid"] = vlan_vid

    params["vlan_vid__empty"] = vlan_vid_empty

    params["vlan_vid__gt"] = vlan_vid_gt

    params["vlan_vid__gte"] = vlan_vid_gte

    params["vlan_vid__lt"] = vlan_vid_lt

    params["vlan_vid__lte"] = vlan_vid_lte

    params["vlan_vid__n"] = vlan_vid_n

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

    json_vrf_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(vrf_id, Unset):
        json_vrf_id = []
        for vrf_id_item_data in vrf_id:
            vrf_id_item: Union[None, int]
            vrf_id_item = vrf_id_item_data
            json_vrf_id.append(vrf_id_item)

    params["vrf_id"] = json_vrf_id

    json_vrf_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(vrf_id_n, Unset):
        json_vrf_id_n = []
        for vrf_id_n_item_data in vrf_id_n:
            vrf_id_n_item: Union[None, int]
            vrf_id_n_item = vrf_id_n_item_data
            json_vrf_id_n.append(vrf_id_n_item)

    params["vrf_id__n"] = json_vrf_id_n

    params["within"] = within

    params["within_include"] = within_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/ipam/prefixes/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedPrefixList]:
    if response.status_code == 200:
        response_200 = PaginatedPrefixList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedPrefixList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    children: Union[Unset, list[int]] = UNSET,
    children_empty: Union[Unset, list[int]] = UNSET,
    children_gt: Union[Unset, list[int]] = UNSET,
    children_gte: Union[Unset, list[int]] = UNSET,
    children_lt: Union[Unset, list[int]] = UNSET,
    children_lte: Union[Unset, list[int]] = UNSET,
    children_n: Union[Unset, list[int]] = UNSET,
    contact: Union[Unset, list[int]] = UNSET,
    contact_n: Union[Unset, list[int]] = UNSET,
    contact_group: Union[Unset, list[str]] = UNSET,
    contact_group_n: Union[Unset, list[str]] = UNSET,
    contact_role: Union[Unset, list[int]] = UNSET,
    contact_role_n: Union[Unset, list[int]] = UNSET,
    contains: Union[Unset, str] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    depth: Union[Unset, list[int]] = UNSET,
    depth_empty: Union[Unset, list[int]] = UNSET,
    depth_gt: Union[Unset, list[int]] = UNSET,
    depth_gte: Union[Unset, list[int]] = UNSET,
    depth_lt: Union[Unset, list[int]] = UNSET,
    depth_lte: Union[Unset, list[int]] = UNSET,
    depth_n: Union[Unset, list[int]] = UNSET,
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
    family: Union[Unset, float] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_pool: Union[Unset, bool] = UNSET,
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
    location_id: Union[Unset, list[str]] = UNSET,
    location_id_n: Union[Unset, list[str]] = UNSET,
    mark_utilized: Union[Unset, bool] = UNSET,
    mask_length: Union[Unset, list[int]] = UNSET,
    mask_length_gte: Union[Unset, float] = UNSET,
    mask_length_lte: Union[Unset, float] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    prefix: Union[Unset, list[str]] = UNSET,
    present_in_vrf: Union[Unset, str] = UNSET,
    present_in_vrf_id: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    scope_id: Union[Unset, list[int]] = UNSET,
    scope_id_empty: Union[Unset, bool] = UNSET,
    scope_id_gt: Union[Unset, list[int]] = UNSET,
    scope_id_gte: Union[Unset, list[int]] = UNSET,
    scope_id_lt: Union[Unset, list[int]] = UNSET,
    scope_id_lte: Union[Unset, list[int]] = UNSET,
    scope_id_n: Union[Unset, list[int]] = UNSET,
    scope_type: Union[Unset, str] = UNSET,
    scope_type_n: Union[Unset, str] = UNSET,
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
    vlan_group: Union[Unset, list[str]] = UNSET,
    vlan_group_n: Union[Unset, list[str]] = UNSET,
    vlan_group_id: Union[Unset, list[int]] = UNSET,
    vlan_group_id_n: Union[Unset, list[int]] = UNSET,
    vlan_id: Union[Unset, list[Union[None, int]]] = UNSET,
    vlan_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    vlan_vid: Union[Unset, int] = UNSET,
    vlan_vid_empty: Union[Unset, int] = UNSET,
    vlan_vid_gt: Union[Unset, int] = UNSET,
    vlan_vid_gte: Union[Unset, int] = UNSET,
    vlan_vid_lt: Union[Unset, int] = UNSET,
    vlan_vid_lte: Union[Unset, int] = UNSET,
    vlan_vid_n: Union[Unset, int] = UNSET,
    vrf: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_n: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_id: Union[Unset, list[Union[None, int]]] = UNSET,
    vrf_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    within: Union[Unset, str] = UNSET,
    within_include: Union[Unset, str] = UNSET,
) -> Response[PaginatedPrefixList]:
    """Get a list of prefix objects.

    Args:
        children (Union[Unset, list[int]]):
        children_empty (Union[Unset, list[int]]):
        children_gt (Union[Unset, list[int]]):
        children_gte (Union[Unset, list[int]]):
        children_lt (Union[Unset, list[int]]):
        children_lte (Union[Unset, list[int]]):
        children_n (Union[Unset, list[int]]):
        contact (Union[Unset, list[int]]):
        contact_n (Union[Unset, list[int]]):
        contact_group (Union[Unset, list[str]]):
        contact_group_n (Union[Unset, list[str]]):
        contact_role (Union[Unset, list[int]]):
        contact_role_n (Union[Unset, list[int]]):
        contains (Union[Unset, str]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        depth (Union[Unset, list[int]]):
        depth_empty (Union[Unset, list[int]]):
        depth_gt (Union[Unset, list[int]]):
        depth_gte (Union[Unset, list[int]]):
        depth_lt (Union[Unset, list[int]]):
        depth_lte (Union[Unset, list[int]]):
        depth_n (Union[Unset, list[int]]):
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
        family (Union[Unset, float]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_pool (Union[Unset, bool]):
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
        location_id (Union[Unset, list[str]]):
        location_id_n (Union[Unset, list[str]]):
        mark_utilized (Union[Unset, bool]):
        mask_length (Union[Unset, list[int]]):
        mask_length_gte (Union[Unset, float]):
        mask_length_lte (Union[Unset, float]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        prefix (Union[Unset, list[str]]):
        present_in_vrf (Union[Unset, str]):
        present_in_vrf_id (Union[Unset, str]):
        q (Union[Unset, str]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[Union[None, int]]]):
        role_id_n (Union[Unset, list[Union[None, int]]]):
        scope_id (Union[Unset, list[int]]):
        scope_id_empty (Union[Unset, bool]):
        scope_id_gt (Union[Unset, list[int]]):
        scope_id_gte (Union[Unset, list[int]]):
        scope_id_lt (Union[Unset, list[int]]):
        scope_id_lte (Union[Unset, list[int]]):
        scope_id_n (Union[Unset, list[int]]):
        scope_type (Union[Unset, str]):
        scope_type_n (Union[Unset, str]):
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
        vlan_group (Union[Unset, list[str]]):
        vlan_group_n (Union[Unset, list[str]]):
        vlan_group_id (Union[Unset, list[int]]):
        vlan_group_id_n (Union[Unset, list[int]]):
        vlan_id (Union[Unset, list[Union[None, int]]]):
        vlan_id_n (Union[Unset, list[Union[None, int]]]):
        vlan_vid (Union[Unset, int]):
        vlan_vid_empty (Union[Unset, int]):
        vlan_vid_gt (Union[Unset, int]):
        vlan_vid_gte (Union[Unset, int]):
        vlan_vid_lt (Union[Unset, int]):
        vlan_vid_lte (Union[Unset, int]):
        vlan_vid_n (Union[Unset, int]):
        vrf (Union[Unset, list[Union[None, str]]]):
        vrf_n (Union[Unset, list[Union[None, str]]]):
        vrf_id (Union[Unset, list[Union[None, int]]]):
        vrf_id_n (Union[Unset, list[Union[None, int]]]):
        within (Union[Unset, str]):
        within_include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPrefixList]
    """

    kwargs = _get_kwargs(
        children=children,
        children_empty=children_empty,
        children_gt=children_gt,
        children_gte=children_gte,
        children_lt=children_lt,
        children_lte=children_lte,
        children_n=children_n,
        contact=contact,
        contact_n=contact_n,
        contact_group=contact_group,
        contact_group_n=contact_group_n,
        contact_role=contact_role,
        contact_role_n=contact_role_n,
        contains=contains,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        depth=depth,
        depth_empty=depth_empty,
        depth_gt=depth_gt,
        depth_gte=depth_gte,
        depth_lt=depth_lt,
        depth_lte=depth_lte,
        depth_n=depth_n,
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
        family=family,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        is_pool=is_pool,
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
        mark_utilized=mark_utilized,
        mask_length=mask_length,
        mask_length_gte=mask_length_gte,
        mask_length_lte=mask_length_lte,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        prefix=prefix,
        present_in_vrf=present_in_vrf,
        present_in_vrf_id=present_in_vrf_id,
        q=q,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
        scope_id=scope_id,
        scope_id_empty=scope_id_empty,
        scope_id_gt=scope_id_gt,
        scope_id_gte=scope_id_gte,
        scope_id_lt=scope_id_lt,
        scope_id_lte=scope_id_lte,
        scope_id_n=scope_id_n,
        scope_type=scope_type,
        scope_type_n=scope_type_n,
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
        vlan_group=vlan_group,
        vlan_group_n=vlan_group_n,
        vlan_group_id=vlan_group_id,
        vlan_group_id_n=vlan_group_id_n,
        vlan_id=vlan_id,
        vlan_id_n=vlan_id_n,
        vlan_vid=vlan_vid,
        vlan_vid_empty=vlan_vid_empty,
        vlan_vid_gt=vlan_vid_gt,
        vlan_vid_gte=vlan_vid_gte,
        vlan_vid_lt=vlan_vid_lt,
        vlan_vid_lte=vlan_vid_lte,
        vlan_vid_n=vlan_vid_n,
        vrf=vrf,
        vrf_n=vrf_n,
        vrf_id=vrf_id,
        vrf_id_n=vrf_id_n,
        within=within,
        within_include=within_include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    children: Union[Unset, list[int]] = UNSET,
    children_empty: Union[Unset, list[int]] = UNSET,
    children_gt: Union[Unset, list[int]] = UNSET,
    children_gte: Union[Unset, list[int]] = UNSET,
    children_lt: Union[Unset, list[int]] = UNSET,
    children_lte: Union[Unset, list[int]] = UNSET,
    children_n: Union[Unset, list[int]] = UNSET,
    contact: Union[Unset, list[int]] = UNSET,
    contact_n: Union[Unset, list[int]] = UNSET,
    contact_group: Union[Unset, list[str]] = UNSET,
    contact_group_n: Union[Unset, list[str]] = UNSET,
    contact_role: Union[Unset, list[int]] = UNSET,
    contact_role_n: Union[Unset, list[int]] = UNSET,
    contains: Union[Unset, str] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    depth: Union[Unset, list[int]] = UNSET,
    depth_empty: Union[Unset, list[int]] = UNSET,
    depth_gt: Union[Unset, list[int]] = UNSET,
    depth_gte: Union[Unset, list[int]] = UNSET,
    depth_lt: Union[Unset, list[int]] = UNSET,
    depth_lte: Union[Unset, list[int]] = UNSET,
    depth_n: Union[Unset, list[int]] = UNSET,
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
    family: Union[Unset, float] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_pool: Union[Unset, bool] = UNSET,
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
    location_id: Union[Unset, list[str]] = UNSET,
    location_id_n: Union[Unset, list[str]] = UNSET,
    mark_utilized: Union[Unset, bool] = UNSET,
    mask_length: Union[Unset, list[int]] = UNSET,
    mask_length_gte: Union[Unset, float] = UNSET,
    mask_length_lte: Union[Unset, float] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    prefix: Union[Unset, list[str]] = UNSET,
    present_in_vrf: Union[Unset, str] = UNSET,
    present_in_vrf_id: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    scope_id: Union[Unset, list[int]] = UNSET,
    scope_id_empty: Union[Unset, bool] = UNSET,
    scope_id_gt: Union[Unset, list[int]] = UNSET,
    scope_id_gte: Union[Unset, list[int]] = UNSET,
    scope_id_lt: Union[Unset, list[int]] = UNSET,
    scope_id_lte: Union[Unset, list[int]] = UNSET,
    scope_id_n: Union[Unset, list[int]] = UNSET,
    scope_type: Union[Unset, str] = UNSET,
    scope_type_n: Union[Unset, str] = UNSET,
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
    vlan_group: Union[Unset, list[str]] = UNSET,
    vlan_group_n: Union[Unset, list[str]] = UNSET,
    vlan_group_id: Union[Unset, list[int]] = UNSET,
    vlan_group_id_n: Union[Unset, list[int]] = UNSET,
    vlan_id: Union[Unset, list[Union[None, int]]] = UNSET,
    vlan_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    vlan_vid: Union[Unset, int] = UNSET,
    vlan_vid_empty: Union[Unset, int] = UNSET,
    vlan_vid_gt: Union[Unset, int] = UNSET,
    vlan_vid_gte: Union[Unset, int] = UNSET,
    vlan_vid_lt: Union[Unset, int] = UNSET,
    vlan_vid_lte: Union[Unset, int] = UNSET,
    vlan_vid_n: Union[Unset, int] = UNSET,
    vrf: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_n: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_id: Union[Unset, list[Union[None, int]]] = UNSET,
    vrf_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    within: Union[Unset, str] = UNSET,
    within_include: Union[Unset, str] = UNSET,
) -> Optional[PaginatedPrefixList]:
    """Get a list of prefix objects.

    Args:
        children (Union[Unset, list[int]]):
        children_empty (Union[Unset, list[int]]):
        children_gt (Union[Unset, list[int]]):
        children_gte (Union[Unset, list[int]]):
        children_lt (Union[Unset, list[int]]):
        children_lte (Union[Unset, list[int]]):
        children_n (Union[Unset, list[int]]):
        contact (Union[Unset, list[int]]):
        contact_n (Union[Unset, list[int]]):
        contact_group (Union[Unset, list[str]]):
        contact_group_n (Union[Unset, list[str]]):
        contact_role (Union[Unset, list[int]]):
        contact_role_n (Union[Unset, list[int]]):
        contains (Union[Unset, str]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        depth (Union[Unset, list[int]]):
        depth_empty (Union[Unset, list[int]]):
        depth_gt (Union[Unset, list[int]]):
        depth_gte (Union[Unset, list[int]]):
        depth_lt (Union[Unset, list[int]]):
        depth_lte (Union[Unset, list[int]]):
        depth_n (Union[Unset, list[int]]):
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
        family (Union[Unset, float]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_pool (Union[Unset, bool]):
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
        location_id (Union[Unset, list[str]]):
        location_id_n (Union[Unset, list[str]]):
        mark_utilized (Union[Unset, bool]):
        mask_length (Union[Unset, list[int]]):
        mask_length_gte (Union[Unset, float]):
        mask_length_lte (Union[Unset, float]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        prefix (Union[Unset, list[str]]):
        present_in_vrf (Union[Unset, str]):
        present_in_vrf_id (Union[Unset, str]):
        q (Union[Unset, str]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[Union[None, int]]]):
        role_id_n (Union[Unset, list[Union[None, int]]]):
        scope_id (Union[Unset, list[int]]):
        scope_id_empty (Union[Unset, bool]):
        scope_id_gt (Union[Unset, list[int]]):
        scope_id_gte (Union[Unset, list[int]]):
        scope_id_lt (Union[Unset, list[int]]):
        scope_id_lte (Union[Unset, list[int]]):
        scope_id_n (Union[Unset, list[int]]):
        scope_type (Union[Unset, str]):
        scope_type_n (Union[Unset, str]):
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
        vlan_group (Union[Unset, list[str]]):
        vlan_group_n (Union[Unset, list[str]]):
        vlan_group_id (Union[Unset, list[int]]):
        vlan_group_id_n (Union[Unset, list[int]]):
        vlan_id (Union[Unset, list[Union[None, int]]]):
        vlan_id_n (Union[Unset, list[Union[None, int]]]):
        vlan_vid (Union[Unset, int]):
        vlan_vid_empty (Union[Unset, int]):
        vlan_vid_gt (Union[Unset, int]):
        vlan_vid_gte (Union[Unset, int]):
        vlan_vid_lt (Union[Unset, int]):
        vlan_vid_lte (Union[Unset, int]):
        vlan_vid_n (Union[Unset, int]):
        vrf (Union[Unset, list[Union[None, str]]]):
        vrf_n (Union[Unset, list[Union[None, str]]]):
        vrf_id (Union[Unset, list[Union[None, int]]]):
        vrf_id_n (Union[Unset, list[Union[None, int]]]):
        within (Union[Unset, str]):
        within_include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedPrefixList
    """

    return sync_detailed(
        client=client,
        children=children,
        children_empty=children_empty,
        children_gt=children_gt,
        children_gte=children_gte,
        children_lt=children_lt,
        children_lte=children_lte,
        children_n=children_n,
        contact=contact,
        contact_n=contact_n,
        contact_group=contact_group,
        contact_group_n=contact_group_n,
        contact_role=contact_role,
        contact_role_n=contact_role_n,
        contains=contains,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        depth=depth,
        depth_empty=depth_empty,
        depth_gt=depth_gt,
        depth_gte=depth_gte,
        depth_lt=depth_lt,
        depth_lte=depth_lte,
        depth_n=depth_n,
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
        family=family,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        is_pool=is_pool,
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
        mark_utilized=mark_utilized,
        mask_length=mask_length,
        mask_length_gte=mask_length_gte,
        mask_length_lte=mask_length_lte,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        prefix=prefix,
        present_in_vrf=present_in_vrf,
        present_in_vrf_id=present_in_vrf_id,
        q=q,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
        scope_id=scope_id,
        scope_id_empty=scope_id_empty,
        scope_id_gt=scope_id_gt,
        scope_id_gte=scope_id_gte,
        scope_id_lt=scope_id_lt,
        scope_id_lte=scope_id_lte,
        scope_id_n=scope_id_n,
        scope_type=scope_type,
        scope_type_n=scope_type_n,
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
        vlan_group=vlan_group,
        vlan_group_n=vlan_group_n,
        vlan_group_id=vlan_group_id,
        vlan_group_id_n=vlan_group_id_n,
        vlan_id=vlan_id,
        vlan_id_n=vlan_id_n,
        vlan_vid=vlan_vid,
        vlan_vid_empty=vlan_vid_empty,
        vlan_vid_gt=vlan_vid_gt,
        vlan_vid_gte=vlan_vid_gte,
        vlan_vid_lt=vlan_vid_lt,
        vlan_vid_lte=vlan_vid_lte,
        vlan_vid_n=vlan_vid_n,
        vrf=vrf,
        vrf_n=vrf_n,
        vrf_id=vrf_id,
        vrf_id_n=vrf_id_n,
        within=within,
        within_include=within_include,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    children: Union[Unset, list[int]] = UNSET,
    children_empty: Union[Unset, list[int]] = UNSET,
    children_gt: Union[Unset, list[int]] = UNSET,
    children_gte: Union[Unset, list[int]] = UNSET,
    children_lt: Union[Unset, list[int]] = UNSET,
    children_lte: Union[Unset, list[int]] = UNSET,
    children_n: Union[Unset, list[int]] = UNSET,
    contact: Union[Unset, list[int]] = UNSET,
    contact_n: Union[Unset, list[int]] = UNSET,
    contact_group: Union[Unset, list[str]] = UNSET,
    contact_group_n: Union[Unset, list[str]] = UNSET,
    contact_role: Union[Unset, list[int]] = UNSET,
    contact_role_n: Union[Unset, list[int]] = UNSET,
    contains: Union[Unset, str] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    depth: Union[Unset, list[int]] = UNSET,
    depth_empty: Union[Unset, list[int]] = UNSET,
    depth_gt: Union[Unset, list[int]] = UNSET,
    depth_gte: Union[Unset, list[int]] = UNSET,
    depth_lt: Union[Unset, list[int]] = UNSET,
    depth_lte: Union[Unset, list[int]] = UNSET,
    depth_n: Union[Unset, list[int]] = UNSET,
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
    family: Union[Unset, float] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_pool: Union[Unset, bool] = UNSET,
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
    location_id: Union[Unset, list[str]] = UNSET,
    location_id_n: Union[Unset, list[str]] = UNSET,
    mark_utilized: Union[Unset, bool] = UNSET,
    mask_length: Union[Unset, list[int]] = UNSET,
    mask_length_gte: Union[Unset, float] = UNSET,
    mask_length_lte: Union[Unset, float] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    prefix: Union[Unset, list[str]] = UNSET,
    present_in_vrf: Union[Unset, str] = UNSET,
    present_in_vrf_id: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    scope_id: Union[Unset, list[int]] = UNSET,
    scope_id_empty: Union[Unset, bool] = UNSET,
    scope_id_gt: Union[Unset, list[int]] = UNSET,
    scope_id_gte: Union[Unset, list[int]] = UNSET,
    scope_id_lt: Union[Unset, list[int]] = UNSET,
    scope_id_lte: Union[Unset, list[int]] = UNSET,
    scope_id_n: Union[Unset, list[int]] = UNSET,
    scope_type: Union[Unset, str] = UNSET,
    scope_type_n: Union[Unset, str] = UNSET,
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
    vlan_group: Union[Unset, list[str]] = UNSET,
    vlan_group_n: Union[Unset, list[str]] = UNSET,
    vlan_group_id: Union[Unset, list[int]] = UNSET,
    vlan_group_id_n: Union[Unset, list[int]] = UNSET,
    vlan_id: Union[Unset, list[Union[None, int]]] = UNSET,
    vlan_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    vlan_vid: Union[Unset, int] = UNSET,
    vlan_vid_empty: Union[Unset, int] = UNSET,
    vlan_vid_gt: Union[Unset, int] = UNSET,
    vlan_vid_gte: Union[Unset, int] = UNSET,
    vlan_vid_lt: Union[Unset, int] = UNSET,
    vlan_vid_lte: Union[Unset, int] = UNSET,
    vlan_vid_n: Union[Unset, int] = UNSET,
    vrf: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_n: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_id: Union[Unset, list[Union[None, int]]] = UNSET,
    vrf_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    within: Union[Unset, str] = UNSET,
    within_include: Union[Unset, str] = UNSET,
) -> Response[PaginatedPrefixList]:
    """Get a list of prefix objects.

    Args:
        children (Union[Unset, list[int]]):
        children_empty (Union[Unset, list[int]]):
        children_gt (Union[Unset, list[int]]):
        children_gte (Union[Unset, list[int]]):
        children_lt (Union[Unset, list[int]]):
        children_lte (Union[Unset, list[int]]):
        children_n (Union[Unset, list[int]]):
        contact (Union[Unset, list[int]]):
        contact_n (Union[Unset, list[int]]):
        contact_group (Union[Unset, list[str]]):
        contact_group_n (Union[Unset, list[str]]):
        contact_role (Union[Unset, list[int]]):
        contact_role_n (Union[Unset, list[int]]):
        contains (Union[Unset, str]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        depth (Union[Unset, list[int]]):
        depth_empty (Union[Unset, list[int]]):
        depth_gt (Union[Unset, list[int]]):
        depth_gte (Union[Unset, list[int]]):
        depth_lt (Union[Unset, list[int]]):
        depth_lte (Union[Unset, list[int]]):
        depth_n (Union[Unset, list[int]]):
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
        family (Union[Unset, float]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_pool (Union[Unset, bool]):
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
        location_id (Union[Unset, list[str]]):
        location_id_n (Union[Unset, list[str]]):
        mark_utilized (Union[Unset, bool]):
        mask_length (Union[Unset, list[int]]):
        mask_length_gte (Union[Unset, float]):
        mask_length_lte (Union[Unset, float]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        prefix (Union[Unset, list[str]]):
        present_in_vrf (Union[Unset, str]):
        present_in_vrf_id (Union[Unset, str]):
        q (Union[Unset, str]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[Union[None, int]]]):
        role_id_n (Union[Unset, list[Union[None, int]]]):
        scope_id (Union[Unset, list[int]]):
        scope_id_empty (Union[Unset, bool]):
        scope_id_gt (Union[Unset, list[int]]):
        scope_id_gte (Union[Unset, list[int]]):
        scope_id_lt (Union[Unset, list[int]]):
        scope_id_lte (Union[Unset, list[int]]):
        scope_id_n (Union[Unset, list[int]]):
        scope_type (Union[Unset, str]):
        scope_type_n (Union[Unset, str]):
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
        vlan_group (Union[Unset, list[str]]):
        vlan_group_n (Union[Unset, list[str]]):
        vlan_group_id (Union[Unset, list[int]]):
        vlan_group_id_n (Union[Unset, list[int]]):
        vlan_id (Union[Unset, list[Union[None, int]]]):
        vlan_id_n (Union[Unset, list[Union[None, int]]]):
        vlan_vid (Union[Unset, int]):
        vlan_vid_empty (Union[Unset, int]):
        vlan_vid_gt (Union[Unset, int]):
        vlan_vid_gte (Union[Unset, int]):
        vlan_vid_lt (Union[Unset, int]):
        vlan_vid_lte (Union[Unset, int]):
        vlan_vid_n (Union[Unset, int]):
        vrf (Union[Unset, list[Union[None, str]]]):
        vrf_n (Union[Unset, list[Union[None, str]]]):
        vrf_id (Union[Unset, list[Union[None, int]]]):
        vrf_id_n (Union[Unset, list[Union[None, int]]]):
        within (Union[Unset, str]):
        within_include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPrefixList]
    """

    kwargs = _get_kwargs(
        children=children,
        children_empty=children_empty,
        children_gt=children_gt,
        children_gte=children_gte,
        children_lt=children_lt,
        children_lte=children_lte,
        children_n=children_n,
        contact=contact,
        contact_n=contact_n,
        contact_group=contact_group,
        contact_group_n=contact_group_n,
        contact_role=contact_role,
        contact_role_n=contact_role_n,
        contains=contains,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        depth=depth,
        depth_empty=depth_empty,
        depth_gt=depth_gt,
        depth_gte=depth_gte,
        depth_lt=depth_lt,
        depth_lte=depth_lte,
        depth_n=depth_n,
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
        family=family,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        is_pool=is_pool,
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
        mark_utilized=mark_utilized,
        mask_length=mask_length,
        mask_length_gte=mask_length_gte,
        mask_length_lte=mask_length_lte,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        prefix=prefix,
        present_in_vrf=present_in_vrf,
        present_in_vrf_id=present_in_vrf_id,
        q=q,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
        scope_id=scope_id,
        scope_id_empty=scope_id_empty,
        scope_id_gt=scope_id_gt,
        scope_id_gte=scope_id_gte,
        scope_id_lt=scope_id_lt,
        scope_id_lte=scope_id_lte,
        scope_id_n=scope_id_n,
        scope_type=scope_type,
        scope_type_n=scope_type_n,
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
        vlan_group=vlan_group,
        vlan_group_n=vlan_group_n,
        vlan_group_id=vlan_group_id,
        vlan_group_id_n=vlan_group_id_n,
        vlan_id=vlan_id,
        vlan_id_n=vlan_id_n,
        vlan_vid=vlan_vid,
        vlan_vid_empty=vlan_vid_empty,
        vlan_vid_gt=vlan_vid_gt,
        vlan_vid_gte=vlan_vid_gte,
        vlan_vid_lt=vlan_vid_lt,
        vlan_vid_lte=vlan_vid_lte,
        vlan_vid_n=vlan_vid_n,
        vrf=vrf,
        vrf_n=vrf_n,
        vrf_id=vrf_id,
        vrf_id_n=vrf_id_n,
        within=within,
        within_include=within_include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    children: Union[Unset, list[int]] = UNSET,
    children_empty: Union[Unset, list[int]] = UNSET,
    children_gt: Union[Unset, list[int]] = UNSET,
    children_gte: Union[Unset, list[int]] = UNSET,
    children_lt: Union[Unset, list[int]] = UNSET,
    children_lte: Union[Unset, list[int]] = UNSET,
    children_n: Union[Unset, list[int]] = UNSET,
    contact: Union[Unset, list[int]] = UNSET,
    contact_n: Union[Unset, list[int]] = UNSET,
    contact_group: Union[Unset, list[str]] = UNSET,
    contact_group_n: Union[Unset, list[str]] = UNSET,
    contact_role: Union[Unset, list[int]] = UNSET,
    contact_role_n: Union[Unset, list[int]] = UNSET,
    contains: Union[Unset, str] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    depth: Union[Unset, list[int]] = UNSET,
    depth_empty: Union[Unset, list[int]] = UNSET,
    depth_gt: Union[Unset, list[int]] = UNSET,
    depth_gte: Union[Unset, list[int]] = UNSET,
    depth_lt: Union[Unset, list[int]] = UNSET,
    depth_lte: Union[Unset, list[int]] = UNSET,
    depth_n: Union[Unset, list[int]] = UNSET,
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
    family: Union[Unset, float] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_pool: Union[Unset, bool] = UNSET,
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
    location_id: Union[Unset, list[str]] = UNSET,
    location_id_n: Union[Unset, list[str]] = UNSET,
    mark_utilized: Union[Unset, bool] = UNSET,
    mask_length: Union[Unset, list[int]] = UNSET,
    mask_length_gte: Union[Unset, float] = UNSET,
    mask_length_lte: Union[Unset, float] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    prefix: Union[Unset, list[str]] = UNSET,
    present_in_vrf: Union[Unset, str] = UNSET,
    present_in_vrf_id: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    scope_id: Union[Unset, list[int]] = UNSET,
    scope_id_empty: Union[Unset, bool] = UNSET,
    scope_id_gt: Union[Unset, list[int]] = UNSET,
    scope_id_gte: Union[Unset, list[int]] = UNSET,
    scope_id_lt: Union[Unset, list[int]] = UNSET,
    scope_id_lte: Union[Unset, list[int]] = UNSET,
    scope_id_n: Union[Unset, list[int]] = UNSET,
    scope_type: Union[Unset, str] = UNSET,
    scope_type_n: Union[Unset, str] = UNSET,
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
    vlan_group: Union[Unset, list[str]] = UNSET,
    vlan_group_n: Union[Unset, list[str]] = UNSET,
    vlan_group_id: Union[Unset, list[int]] = UNSET,
    vlan_group_id_n: Union[Unset, list[int]] = UNSET,
    vlan_id: Union[Unset, list[Union[None, int]]] = UNSET,
    vlan_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    vlan_vid: Union[Unset, int] = UNSET,
    vlan_vid_empty: Union[Unset, int] = UNSET,
    vlan_vid_gt: Union[Unset, int] = UNSET,
    vlan_vid_gte: Union[Unset, int] = UNSET,
    vlan_vid_lt: Union[Unset, int] = UNSET,
    vlan_vid_lte: Union[Unset, int] = UNSET,
    vlan_vid_n: Union[Unset, int] = UNSET,
    vrf: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_n: Union[Unset, list[Union[None, str]]] = UNSET,
    vrf_id: Union[Unset, list[Union[None, int]]] = UNSET,
    vrf_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    within: Union[Unset, str] = UNSET,
    within_include: Union[Unset, str] = UNSET,
) -> Optional[PaginatedPrefixList]:
    """Get a list of prefix objects.

    Args:
        children (Union[Unset, list[int]]):
        children_empty (Union[Unset, list[int]]):
        children_gt (Union[Unset, list[int]]):
        children_gte (Union[Unset, list[int]]):
        children_lt (Union[Unset, list[int]]):
        children_lte (Union[Unset, list[int]]):
        children_n (Union[Unset, list[int]]):
        contact (Union[Unset, list[int]]):
        contact_n (Union[Unset, list[int]]):
        contact_group (Union[Unset, list[str]]):
        contact_group_n (Union[Unset, list[str]]):
        contact_role (Union[Unset, list[int]]):
        contact_role_n (Union[Unset, list[int]]):
        contains (Union[Unset, str]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        depth (Union[Unset, list[int]]):
        depth_empty (Union[Unset, list[int]]):
        depth_gt (Union[Unset, list[int]]):
        depth_gte (Union[Unset, list[int]]):
        depth_lt (Union[Unset, list[int]]):
        depth_lte (Union[Unset, list[int]]):
        depth_n (Union[Unset, list[int]]):
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
        family (Union[Unset, float]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_pool (Union[Unset, bool]):
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
        location_id (Union[Unset, list[str]]):
        location_id_n (Union[Unset, list[str]]):
        mark_utilized (Union[Unset, bool]):
        mask_length (Union[Unset, list[int]]):
        mask_length_gte (Union[Unset, float]):
        mask_length_lte (Union[Unset, float]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        prefix (Union[Unset, list[str]]):
        present_in_vrf (Union[Unset, str]):
        present_in_vrf_id (Union[Unset, str]):
        q (Union[Unset, str]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[Union[None, int]]]):
        role_id_n (Union[Unset, list[Union[None, int]]]):
        scope_id (Union[Unset, list[int]]):
        scope_id_empty (Union[Unset, bool]):
        scope_id_gt (Union[Unset, list[int]]):
        scope_id_gte (Union[Unset, list[int]]):
        scope_id_lt (Union[Unset, list[int]]):
        scope_id_lte (Union[Unset, list[int]]):
        scope_id_n (Union[Unset, list[int]]):
        scope_type (Union[Unset, str]):
        scope_type_n (Union[Unset, str]):
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
        vlan_group (Union[Unset, list[str]]):
        vlan_group_n (Union[Unset, list[str]]):
        vlan_group_id (Union[Unset, list[int]]):
        vlan_group_id_n (Union[Unset, list[int]]):
        vlan_id (Union[Unset, list[Union[None, int]]]):
        vlan_id_n (Union[Unset, list[Union[None, int]]]):
        vlan_vid (Union[Unset, int]):
        vlan_vid_empty (Union[Unset, int]):
        vlan_vid_gt (Union[Unset, int]):
        vlan_vid_gte (Union[Unset, int]):
        vlan_vid_lt (Union[Unset, int]):
        vlan_vid_lte (Union[Unset, int]):
        vlan_vid_n (Union[Unset, int]):
        vrf (Union[Unset, list[Union[None, str]]]):
        vrf_n (Union[Unset, list[Union[None, str]]]):
        vrf_id (Union[Unset, list[Union[None, int]]]):
        vrf_id_n (Union[Unset, list[Union[None, int]]]):
        within (Union[Unset, str]):
        within_include (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedPrefixList
    """

    return (
        await asyncio_detailed(
            client=client,
            children=children,
            children_empty=children_empty,
            children_gt=children_gt,
            children_gte=children_gte,
            children_lt=children_lt,
            children_lte=children_lte,
            children_n=children_n,
            contact=contact,
            contact_n=contact_n,
            contact_group=contact_group,
            contact_group_n=contact_group_n,
            contact_role=contact_role,
            contact_role_n=contact_role_n,
            contains=contains,
            created=created,
            created_empty=created_empty,
            created_gt=created_gt,
            created_gte=created_gte,
            created_lt=created_lt,
            created_lte=created_lte,
            created_n=created_n,
            created_by_request=created_by_request,
            depth=depth,
            depth_empty=depth_empty,
            depth_gt=depth_gt,
            depth_gte=depth_gte,
            depth_lt=depth_lt,
            depth_lte=depth_lte,
            depth_n=depth_n,
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
            family=family,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            is_pool=is_pool,
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
            mark_utilized=mark_utilized,
            mask_length=mask_length,
            mask_length_gte=mask_length_gte,
            mask_length_lte=mask_length_lte,
            modified_by_request=modified_by_request,
            offset=offset,
            ordering=ordering,
            prefix=prefix,
            present_in_vrf=present_in_vrf,
            present_in_vrf_id=present_in_vrf_id,
            q=q,
            region=region,
            region_n=region_n,
            region_id=region_id,
            region_id_n=region_id_n,
            role=role,
            role_n=role_n,
            role_id=role_id,
            role_id_n=role_id_n,
            scope_id=scope_id,
            scope_id_empty=scope_id_empty,
            scope_id_gt=scope_id_gt,
            scope_id_gte=scope_id_gte,
            scope_id_lt=scope_id_lt,
            scope_id_lte=scope_id_lte,
            scope_id_n=scope_id_n,
            scope_type=scope_type,
            scope_type_n=scope_type_n,
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
            vlan_group=vlan_group,
            vlan_group_n=vlan_group_n,
            vlan_group_id=vlan_group_id,
            vlan_group_id_n=vlan_group_id_n,
            vlan_id=vlan_id,
            vlan_id_n=vlan_id_n,
            vlan_vid=vlan_vid,
            vlan_vid_empty=vlan_vid_empty,
            vlan_vid_gt=vlan_vid_gt,
            vlan_vid_gte=vlan_vid_gte,
            vlan_vid_lt=vlan_vid_lt,
            vlan_vid_lte=vlan_vid_lte,
            vlan_vid_n=vlan_vid_n,
            vrf=vrf,
            vrf_n=vrf_n,
            vrf_id=vrf_id,
            vrf_id_n=vrf_id_n,
            within=within,
            within_include=within_include,
        )
    ).parsed
