import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_config_context_list import PaginatedConfigContextList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    auto_sync_enabled: Union[Unset, bool] = UNSET,
    cluster_group: Union[Unset, list[str]] = UNSET,
    cluster_group_n: Union[Unset, list[str]] = UNSET,
    cluster_group_id: Union[Unset, list[int]] = UNSET,
    cluster_group_id_n: Union[Unset, list[int]] = UNSET,
    cluster_id: Union[Unset, list[int]] = UNSET,
    cluster_id_n: Union[Unset, list[int]] = UNSET,
    cluster_type: Union[Unset, list[str]] = UNSET,
    cluster_type_n: Union[Unset, list[str]] = UNSET,
    cluster_type_id: Union[Unset, list[int]] = UNSET,
    cluster_type_id_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    data_file_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_file_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_synced: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_empty: Union[Unset, bool] = UNSET,
    data_synced_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_n: Union[Unset, list[datetime.datetime]] = UNSET,
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
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_id: Union[Unset, list[int]] = UNSET,
    device_role_id_n: Union[Unset, list[int]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
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
    platform: Union[Unset, list[str]] = UNSET,
    platform_n: Union[Unset, list[str]] = UNSET,
    platform_id: Union[Unset, list[int]] = UNSET,
    platform_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[int]] = UNSET,
    region_id_n: Union[Unset, list[int]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[int]] = UNSET,
    site_group_id_n: Union[Unset, list[int]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tenant: Union[Unset, list[str]] = UNSET,
    tenant_n: Union[Unset, list[str]] = UNSET,
    tenant_group: Union[Unset, list[str]] = UNSET,
    tenant_group_n: Union[Unset, list[str]] = UNSET,
    tenant_group_id: Union[Unset, list[int]] = UNSET,
    tenant_group_id_n: Union[Unset, list[int]] = UNSET,
    tenant_id: Union[Unset, list[int]] = UNSET,
    tenant_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    weight: Union[Unset, list[int]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[int]] = UNSET,
    weight_gte: Union[Unset, list[int]] = UNSET,
    weight_lt: Union[Unset, list[int]] = UNSET,
    weight_lte: Union[Unset, list[int]] = UNSET,
    weight_n: Union[Unset, list[int]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["auto_sync_enabled"] = auto_sync_enabled

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

    json_cluster_id: Union[Unset, list[int]] = UNSET
    if not isinstance(cluster_id, Unset):
        json_cluster_id = cluster_id

    params["cluster_id"] = json_cluster_id

    json_cluster_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(cluster_id_n, Unset):
        json_cluster_id_n = cluster_id_n

    params["cluster_id__n"] = json_cluster_id_n

    json_cluster_type: Union[Unset, list[str]] = UNSET
    if not isinstance(cluster_type, Unset):
        json_cluster_type = cluster_type

    params["cluster_type"] = json_cluster_type

    json_cluster_type_n: Union[Unset, list[str]] = UNSET
    if not isinstance(cluster_type_n, Unset):
        json_cluster_type_n = cluster_type_n

    params["cluster_type__n"] = json_cluster_type_n

    json_cluster_type_id: Union[Unset, list[int]] = UNSET
    if not isinstance(cluster_type_id, Unset):
        json_cluster_type_id = cluster_type_id

    params["cluster_type_id"] = json_cluster_type_id

    json_cluster_type_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(cluster_type_id_n, Unset):
        json_cluster_type_id_n = cluster_type_id_n

    params["cluster_type_id__n"] = json_cluster_type_id_n

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

    json_data_file_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(data_file_id, Unset):
        json_data_file_id = []
        for data_file_id_item_data in data_file_id:
            data_file_id_item: Union[None, int]
            data_file_id_item = data_file_id_item_data
            json_data_file_id.append(data_file_id_item)

    params["data_file_id"] = json_data_file_id

    json_data_file_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(data_file_id_n, Unset):
        json_data_file_id_n = []
        for data_file_id_n_item_data in data_file_id_n:
            data_file_id_n_item: Union[None, int]
            data_file_id_n_item = data_file_id_n_item_data
            json_data_file_id_n.append(data_file_id_n_item)

    params["data_file_id__n"] = json_data_file_id_n

    json_data_source_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(data_source_id, Unset):
        json_data_source_id = []
        for data_source_id_item_data in data_source_id:
            data_source_id_item: Union[None, int]
            data_source_id_item = data_source_id_item_data
            json_data_source_id.append(data_source_id_item)

    params["data_source_id"] = json_data_source_id

    json_data_source_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(data_source_id_n, Unset):
        json_data_source_id_n = []
        for data_source_id_n_item_data in data_source_id_n:
            data_source_id_n_item: Union[None, int]
            data_source_id_n_item = data_source_id_n_item_data
            json_data_source_id_n.append(data_source_id_n_item)

    params["data_source_id__n"] = json_data_source_id_n

    json_data_synced: Union[Unset, list[str]] = UNSET
    if not isinstance(data_synced, Unset):
        json_data_synced = []
        for data_synced_item_data in data_synced:
            data_synced_item = data_synced_item_data.isoformat()
            json_data_synced.append(data_synced_item)

    params["data_synced"] = json_data_synced

    params["data_synced__empty"] = data_synced_empty

    json_data_synced_gt: Union[Unset, list[str]] = UNSET
    if not isinstance(data_synced_gt, Unset):
        json_data_synced_gt = []
        for data_synced_gt_item_data in data_synced_gt:
            data_synced_gt_item = data_synced_gt_item_data.isoformat()
            json_data_synced_gt.append(data_synced_gt_item)

    params["data_synced__gt"] = json_data_synced_gt

    json_data_synced_gte: Union[Unset, list[str]] = UNSET
    if not isinstance(data_synced_gte, Unset):
        json_data_synced_gte = []
        for data_synced_gte_item_data in data_synced_gte:
            data_synced_gte_item = data_synced_gte_item_data.isoformat()
            json_data_synced_gte.append(data_synced_gte_item)

    params["data_synced__gte"] = json_data_synced_gte

    json_data_synced_lt: Union[Unset, list[str]] = UNSET
    if not isinstance(data_synced_lt, Unset):
        json_data_synced_lt = []
        for data_synced_lt_item_data in data_synced_lt:
            data_synced_lt_item = data_synced_lt_item_data.isoformat()
            json_data_synced_lt.append(data_synced_lt_item)

    params["data_synced__lt"] = json_data_synced_lt

    json_data_synced_lte: Union[Unset, list[str]] = UNSET
    if not isinstance(data_synced_lte, Unset):
        json_data_synced_lte = []
        for data_synced_lte_item_data in data_synced_lte:
            data_synced_lte_item = data_synced_lte_item_data.isoformat()
            json_data_synced_lte.append(data_synced_lte_item)

    params["data_synced__lte"] = json_data_synced_lte

    json_data_synced_n: Union[Unset, list[str]] = UNSET
    if not isinstance(data_synced_n, Unset):
        json_data_synced_n = []
        for data_synced_n_item_data in data_synced_n:
            data_synced_n_item = data_synced_n_item_data.isoformat()
            json_data_synced_n.append(data_synced_n_item)

    params["data_synced__n"] = json_data_synced_n

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

    json_device_type_id: Union[Unset, list[int]] = UNSET
    if not isinstance(device_type_id, Unset):
        json_device_type_id = device_type_id

    params["device_type_id"] = json_device_type_id

    json_device_type_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(device_type_id_n, Unset):
        json_device_type_id_n = device_type_id_n

    params["device_type_id__n"] = json_device_type_id_n

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

    params["is_active"] = is_active

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

    json_platform: Union[Unset, list[str]] = UNSET
    if not isinstance(platform, Unset):
        json_platform = platform

    params["platform"] = json_platform

    json_platform_n: Union[Unset, list[str]] = UNSET
    if not isinstance(platform_n, Unset):
        json_platform_n = platform_n

    params["platform__n"] = json_platform_n

    json_platform_id: Union[Unset, list[int]] = UNSET
    if not isinstance(platform_id, Unset):
        json_platform_id = platform_id

    params["platform_id"] = json_platform_id

    json_platform_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(platform_id_n, Unset):
        json_platform_id_n = platform_id_n

    params["platform_id__n"] = json_platform_id_n

    params["q"] = q

    json_region: Union[Unset, list[str]] = UNSET
    if not isinstance(region, Unset):
        json_region = region

    params["region"] = json_region

    json_region_n: Union[Unset, list[str]] = UNSET
    if not isinstance(region_n, Unset):
        json_region_n = region_n

    params["region__n"] = json_region_n

    json_region_id: Union[Unset, list[int]] = UNSET
    if not isinstance(region_id, Unset):
        json_region_id = region_id

    params["region_id"] = json_region_id

    json_region_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(region_id_n, Unset):
        json_region_id_n = region_id_n

    params["region_id__n"] = json_region_id_n

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

    json_site_group_id: Union[Unset, list[int]] = UNSET
    if not isinstance(site_group_id, Unset):
        json_site_group_id = site_group_id

    params["site_group_id"] = json_site_group_id

    json_site_group_id_n: Union[Unset, list[int]] = UNSET
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

    json_tenant_group_id: Union[Unset, list[int]] = UNSET
    if not isinstance(tenant_group_id, Unset):
        json_tenant_group_id = tenant_group_id

    params["tenant_group_id"] = json_tenant_group_id

    json_tenant_group_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(tenant_group_id_n, Unset):
        json_tenant_group_id_n = tenant_group_id_n

    params["tenant_group_id__n"] = json_tenant_group_id_n

    json_tenant_id: Union[Unset, list[int]] = UNSET
    if not isinstance(tenant_id, Unset):
        json_tenant_id = tenant_id

    params["tenant_id"] = json_tenant_id

    json_tenant_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(tenant_id_n, Unset):
        json_tenant_id_n = tenant_id_n

    params["tenant_id__n"] = json_tenant_id_n

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    json_weight: Union[Unset, list[int]] = UNSET
    if not isinstance(weight, Unset):
        json_weight = weight

    params["weight"] = json_weight

    params["weight__empty"] = weight_empty

    json_weight_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(weight_gt, Unset):
        json_weight_gt = weight_gt

    params["weight__gt"] = json_weight_gt

    json_weight_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(weight_gte, Unset):
        json_weight_gte = weight_gte

    params["weight__gte"] = json_weight_gte

    json_weight_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(weight_lt, Unset):
        json_weight_lt = weight_lt

    params["weight__lt"] = json_weight_lt

    json_weight_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(weight_lte, Unset):
        json_weight_lte = weight_lte

    params["weight__lte"] = json_weight_lte

    json_weight_n: Union[Unset, list[int]] = UNSET
    if not isinstance(weight_n, Unset):
        json_weight_n = weight_n

    params["weight__n"] = json_weight_n

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/extras/config-contexts/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedConfigContextList]:
    if response.status_code == 200:
        response_200 = PaginatedConfigContextList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedConfigContextList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    auto_sync_enabled: Union[Unset, bool] = UNSET,
    cluster_group: Union[Unset, list[str]] = UNSET,
    cluster_group_n: Union[Unset, list[str]] = UNSET,
    cluster_group_id: Union[Unset, list[int]] = UNSET,
    cluster_group_id_n: Union[Unset, list[int]] = UNSET,
    cluster_id: Union[Unset, list[int]] = UNSET,
    cluster_id_n: Union[Unset, list[int]] = UNSET,
    cluster_type: Union[Unset, list[str]] = UNSET,
    cluster_type_n: Union[Unset, list[str]] = UNSET,
    cluster_type_id: Union[Unset, list[int]] = UNSET,
    cluster_type_id_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    data_file_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_file_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_synced: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_empty: Union[Unset, bool] = UNSET,
    data_synced_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_n: Union[Unset, list[datetime.datetime]] = UNSET,
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
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_id: Union[Unset, list[int]] = UNSET,
    device_role_id_n: Union[Unset, list[int]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
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
    platform: Union[Unset, list[str]] = UNSET,
    platform_n: Union[Unset, list[str]] = UNSET,
    platform_id: Union[Unset, list[int]] = UNSET,
    platform_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[int]] = UNSET,
    region_id_n: Union[Unset, list[int]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[int]] = UNSET,
    site_group_id_n: Union[Unset, list[int]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tenant: Union[Unset, list[str]] = UNSET,
    tenant_n: Union[Unset, list[str]] = UNSET,
    tenant_group: Union[Unset, list[str]] = UNSET,
    tenant_group_n: Union[Unset, list[str]] = UNSET,
    tenant_group_id: Union[Unset, list[int]] = UNSET,
    tenant_group_id_n: Union[Unset, list[int]] = UNSET,
    tenant_id: Union[Unset, list[int]] = UNSET,
    tenant_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    weight: Union[Unset, list[int]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[int]] = UNSET,
    weight_gte: Union[Unset, list[int]] = UNSET,
    weight_lt: Union[Unset, list[int]] = UNSET,
    weight_lte: Union[Unset, list[int]] = UNSET,
    weight_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedConfigContextList]:
    """Get a list of config context objects.

    Args:
        auto_sync_enabled (Union[Unset, bool]):
        cluster_group (Union[Unset, list[str]]):
        cluster_group_n (Union[Unset, list[str]]):
        cluster_group_id (Union[Unset, list[int]]):
        cluster_group_id_n (Union[Unset, list[int]]):
        cluster_id (Union[Unset, list[int]]):
        cluster_id_n (Union[Unset, list[int]]):
        cluster_type (Union[Unset, list[str]]):
        cluster_type_n (Union[Unset, list[str]]):
        cluster_type_id (Union[Unset, list[int]]):
        cluster_type_id_n (Union[Unset, list[int]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        data_file_id (Union[Unset, list[Union[None, int]]]):
        data_file_id_n (Union[Unset, list[Union[None, int]]]):
        data_source_id (Union[Unset, list[Union[None, int]]]):
        data_source_id_n (Union[Unset, list[Union[None, int]]]):
        data_synced (Union[Unset, list[datetime.datetime]]):
        data_synced_empty (Union[Unset, bool]):
        data_synced_gt (Union[Unset, list[datetime.datetime]]):
        data_synced_gte (Union[Unset, list[datetime.datetime]]):
        data_synced_lt (Union[Unset, list[datetime.datetime]]):
        data_synced_lte (Union[Unset, list[datetime.datetime]]):
        data_synced_n (Union[Unset, list[datetime.datetime]]):
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
        device_role (Union[Unset, list[str]]):
        device_role_n (Union[Unset, list[str]]):
        device_role_id (Union[Unset, list[int]]):
        device_role_id_n (Union[Unset, list[int]]):
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_active (Union[Unset, bool]):
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
        platform (Union[Unset, list[str]]):
        platform_n (Union[Unset, list[str]]):
        platform_id (Union[Unset, list[int]]):
        platform_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[int]]):
        region_id_n (Union[Unset, list[int]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[int]]):
        site_group_id_n (Union[Unset, list[int]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        tenant (Union[Unset, list[str]]):
        tenant_n (Union[Unset, list[str]]):
        tenant_group (Union[Unset, list[str]]):
        tenant_group_n (Union[Unset, list[str]]):
        tenant_group_id (Union[Unset, list[int]]):
        tenant_group_id_n (Union[Unset, list[int]]):
        tenant_id (Union[Unset, list[int]]):
        tenant_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        weight (Union[Unset, list[int]]):
        weight_empty (Union[Unset, bool]):
        weight_gt (Union[Unset, list[int]]):
        weight_gte (Union[Unset, list[int]]):
        weight_lt (Union[Unset, list[int]]):
        weight_lte (Union[Unset, list[int]]):
        weight_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConfigContextList]
    """

    kwargs = _get_kwargs(
        auto_sync_enabled=auto_sync_enabled,
        cluster_group=cluster_group,
        cluster_group_n=cluster_group_n,
        cluster_group_id=cluster_group_id,
        cluster_group_id_n=cluster_group_id_n,
        cluster_id=cluster_id,
        cluster_id_n=cluster_id_n,
        cluster_type=cluster_type,
        cluster_type_n=cluster_type_n,
        cluster_type_id=cluster_type_id,
        cluster_type_id_n=cluster_type_id_n,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        data_file_id=data_file_id,
        data_file_id_n=data_file_id_n,
        data_source_id=data_source_id,
        data_source_id_n=data_source_id_n,
        data_synced=data_synced,
        data_synced_empty=data_synced_empty,
        data_synced_gt=data_synced_gt,
        data_synced_gte=data_synced_gte,
        data_synced_lt=data_synced_lt,
        data_synced_lte=data_synced_lte,
        data_synced_n=data_synced_n,
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
        device_role=device_role,
        device_role_n=device_role_n,
        device_role_id=device_role_id,
        device_role_id_n=device_role_id_n,
        device_type_id=device_type_id,
        device_type_id_n=device_type_id_n,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        is_active=is_active,
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
        platform=platform,
        platform_n=platform_n,
        platform_id=platform_id,
        platform_id_n=platform_id_n,
        q=q,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        site=site,
        site_n=site_n,
        site_group=site_group,
        site_group_n=site_group_n,
        site_group_id=site_group_id,
        site_group_id_n=site_group_id_n,
        site_id=site_id,
        site_id_n=site_id_n,
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
        weight=weight,
        weight_empty=weight_empty,
        weight_gt=weight_gt,
        weight_gte=weight_gte,
        weight_lt=weight_lt,
        weight_lte=weight_lte,
        weight_n=weight_n,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    auto_sync_enabled: Union[Unset, bool] = UNSET,
    cluster_group: Union[Unset, list[str]] = UNSET,
    cluster_group_n: Union[Unset, list[str]] = UNSET,
    cluster_group_id: Union[Unset, list[int]] = UNSET,
    cluster_group_id_n: Union[Unset, list[int]] = UNSET,
    cluster_id: Union[Unset, list[int]] = UNSET,
    cluster_id_n: Union[Unset, list[int]] = UNSET,
    cluster_type: Union[Unset, list[str]] = UNSET,
    cluster_type_n: Union[Unset, list[str]] = UNSET,
    cluster_type_id: Union[Unset, list[int]] = UNSET,
    cluster_type_id_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    data_file_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_file_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_synced: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_empty: Union[Unset, bool] = UNSET,
    data_synced_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_n: Union[Unset, list[datetime.datetime]] = UNSET,
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
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_id: Union[Unset, list[int]] = UNSET,
    device_role_id_n: Union[Unset, list[int]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
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
    platform: Union[Unset, list[str]] = UNSET,
    platform_n: Union[Unset, list[str]] = UNSET,
    platform_id: Union[Unset, list[int]] = UNSET,
    platform_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[int]] = UNSET,
    region_id_n: Union[Unset, list[int]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[int]] = UNSET,
    site_group_id_n: Union[Unset, list[int]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tenant: Union[Unset, list[str]] = UNSET,
    tenant_n: Union[Unset, list[str]] = UNSET,
    tenant_group: Union[Unset, list[str]] = UNSET,
    tenant_group_n: Union[Unset, list[str]] = UNSET,
    tenant_group_id: Union[Unset, list[int]] = UNSET,
    tenant_group_id_n: Union[Unset, list[int]] = UNSET,
    tenant_id: Union[Unset, list[int]] = UNSET,
    tenant_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    weight: Union[Unset, list[int]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[int]] = UNSET,
    weight_gte: Union[Unset, list[int]] = UNSET,
    weight_lt: Union[Unset, list[int]] = UNSET,
    weight_lte: Union[Unset, list[int]] = UNSET,
    weight_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedConfigContextList]:
    """Get a list of config context objects.

    Args:
        auto_sync_enabled (Union[Unset, bool]):
        cluster_group (Union[Unset, list[str]]):
        cluster_group_n (Union[Unset, list[str]]):
        cluster_group_id (Union[Unset, list[int]]):
        cluster_group_id_n (Union[Unset, list[int]]):
        cluster_id (Union[Unset, list[int]]):
        cluster_id_n (Union[Unset, list[int]]):
        cluster_type (Union[Unset, list[str]]):
        cluster_type_n (Union[Unset, list[str]]):
        cluster_type_id (Union[Unset, list[int]]):
        cluster_type_id_n (Union[Unset, list[int]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        data_file_id (Union[Unset, list[Union[None, int]]]):
        data_file_id_n (Union[Unset, list[Union[None, int]]]):
        data_source_id (Union[Unset, list[Union[None, int]]]):
        data_source_id_n (Union[Unset, list[Union[None, int]]]):
        data_synced (Union[Unset, list[datetime.datetime]]):
        data_synced_empty (Union[Unset, bool]):
        data_synced_gt (Union[Unset, list[datetime.datetime]]):
        data_synced_gte (Union[Unset, list[datetime.datetime]]):
        data_synced_lt (Union[Unset, list[datetime.datetime]]):
        data_synced_lte (Union[Unset, list[datetime.datetime]]):
        data_synced_n (Union[Unset, list[datetime.datetime]]):
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
        device_role (Union[Unset, list[str]]):
        device_role_n (Union[Unset, list[str]]):
        device_role_id (Union[Unset, list[int]]):
        device_role_id_n (Union[Unset, list[int]]):
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_active (Union[Unset, bool]):
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
        platform (Union[Unset, list[str]]):
        platform_n (Union[Unset, list[str]]):
        platform_id (Union[Unset, list[int]]):
        platform_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[int]]):
        region_id_n (Union[Unset, list[int]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[int]]):
        site_group_id_n (Union[Unset, list[int]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        tenant (Union[Unset, list[str]]):
        tenant_n (Union[Unset, list[str]]):
        tenant_group (Union[Unset, list[str]]):
        tenant_group_n (Union[Unset, list[str]]):
        tenant_group_id (Union[Unset, list[int]]):
        tenant_group_id_n (Union[Unset, list[int]]):
        tenant_id (Union[Unset, list[int]]):
        tenant_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        weight (Union[Unset, list[int]]):
        weight_empty (Union[Unset, bool]):
        weight_gt (Union[Unset, list[int]]):
        weight_gte (Union[Unset, list[int]]):
        weight_lt (Union[Unset, list[int]]):
        weight_lte (Union[Unset, list[int]]):
        weight_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConfigContextList
    """

    return sync_detailed(
        client=client,
        auto_sync_enabled=auto_sync_enabled,
        cluster_group=cluster_group,
        cluster_group_n=cluster_group_n,
        cluster_group_id=cluster_group_id,
        cluster_group_id_n=cluster_group_id_n,
        cluster_id=cluster_id,
        cluster_id_n=cluster_id_n,
        cluster_type=cluster_type,
        cluster_type_n=cluster_type_n,
        cluster_type_id=cluster_type_id,
        cluster_type_id_n=cluster_type_id_n,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        data_file_id=data_file_id,
        data_file_id_n=data_file_id_n,
        data_source_id=data_source_id,
        data_source_id_n=data_source_id_n,
        data_synced=data_synced,
        data_synced_empty=data_synced_empty,
        data_synced_gt=data_synced_gt,
        data_synced_gte=data_synced_gte,
        data_synced_lt=data_synced_lt,
        data_synced_lte=data_synced_lte,
        data_synced_n=data_synced_n,
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
        device_role=device_role,
        device_role_n=device_role_n,
        device_role_id=device_role_id,
        device_role_id_n=device_role_id_n,
        device_type_id=device_type_id,
        device_type_id_n=device_type_id_n,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        is_active=is_active,
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
        platform=platform,
        platform_n=platform_n,
        platform_id=platform_id,
        platform_id_n=platform_id_n,
        q=q,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        site=site,
        site_n=site_n,
        site_group=site_group,
        site_group_n=site_group_n,
        site_group_id=site_group_id,
        site_group_id_n=site_group_id_n,
        site_id=site_id,
        site_id_n=site_id_n,
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
        weight=weight,
        weight_empty=weight_empty,
        weight_gt=weight_gt,
        weight_gte=weight_gte,
        weight_lt=weight_lt,
        weight_lte=weight_lte,
        weight_n=weight_n,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    auto_sync_enabled: Union[Unset, bool] = UNSET,
    cluster_group: Union[Unset, list[str]] = UNSET,
    cluster_group_n: Union[Unset, list[str]] = UNSET,
    cluster_group_id: Union[Unset, list[int]] = UNSET,
    cluster_group_id_n: Union[Unset, list[int]] = UNSET,
    cluster_id: Union[Unset, list[int]] = UNSET,
    cluster_id_n: Union[Unset, list[int]] = UNSET,
    cluster_type: Union[Unset, list[str]] = UNSET,
    cluster_type_n: Union[Unset, list[str]] = UNSET,
    cluster_type_id: Union[Unset, list[int]] = UNSET,
    cluster_type_id_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    data_file_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_file_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_synced: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_empty: Union[Unset, bool] = UNSET,
    data_synced_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_n: Union[Unset, list[datetime.datetime]] = UNSET,
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
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_id: Union[Unset, list[int]] = UNSET,
    device_role_id_n: Union[Unset, list[int]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
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
    platform: Union[Unset, list[str]] = UNSET,
    platform_n: Union[Unset, list[str]] = UNSET,
    platform_id: Union[Unset, list[int]] = UNSET,
    platform_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[int]] = UNSET,
    region_id_n: Union[Unset, list[int]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[int]] = UNSET,
    site_group_id_n: Union[Unset, list[int]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tenant: Union[Unset, list[str]] = UNSET,
    tenant_n: Union[Unset, list[str]] = UNSET,
    tenant_group: Union[Unset, list[str]] = UNSET,
    tenant_group_n: Union[Unset, list[str]] = UNSET,
    tenant_group_id: Union[Unset, list[int]] = UNSET,
    tenant_group_id_n: Union[Unset, list[int]] = UNSET,
    tenant_id: Union[Unset, list[int]] = UNSET,
    tenant_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    weight: Union[Unset, list[int]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[int]] = UNSET,
    weight_gte: Union[Unset, list[int]] = UNSET,
    weight_lt: Union[Unset, list[int]] = UNSET,
    weight_lte: Union[Unset, list[int]] = UNSET,
    weight_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedConfigContextList]:
    """Get a list of config context objects.

    Args:
        auto_sync_enabled (Union[Unset, bool]):
        cluster_group (Union[Unset, list[str]]):
        cluster_group_n (Union[Unset, list[str]]):
        cluster_group_id (Union[Unset, list[int]]):
        cluster_group_id_n (Union[Unset, list[int]]):
        cluster_id (Union[Unset, list[int]]):
        cluster_id_n (Union[Unset, list[int]]):
        cluster_type (Union[Unset, list[str]]):
        cluster_type_n (Union[Unset, list[str]]):
        cluster_type_id (Union[Unset, list[int]]):
        cluster_type_id_n (Union[Unset, list[int]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        data_file_id (Union[Unset, list[Union[None, int]]]):
        data_file_id_n (Union[Unset, list[Union[None, int]]]):
        data_source_id (Union[Unset, list[Union[None, int]]]):
        data_source_id_n (Union[Unset, list[Union[None, int]]]):
        data_synced (Union[Unset, list[datetime.datetime]]):
        data_synced_empty (Union[Unset, bool]):
        data_synced_gt (Union[Unset, list[datetime.datetime]]):
        data_synced_gte (Union[Unset, list[datetime.datetime]]):
        data_synced_lt (Union[Unset, list[datetime.datetime]]):
        data_synced_lte (Union[Unset, list[datetime.datetime]]):
        data_synced_n (Union[Unset, list[datetime.datetime]]):
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
        device_role (Union[Unset, list[str]]):
        device_role_n (Union[Unset, list[str]]):
        device_role_id (Union[Unset, list[int]]):
        device_role_id_n (Union[Unset, list[int]]):
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_active (Union[Unset, bool]):
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
        platform (Union[Unset, list[str]]):
        platform_n (Union[Unset, list[str]]):
        platform_id (Union[Unset, list[int]]):
        platform_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[int]]):
        region_id_n (Union[Unset, list[int]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[int]]):
        site_group_id_n (Union[Unset, list[int]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        tenant (Union[Unset, list[str]]):
        tenant_n (Union[Unset, list[str]]):
        tenant_group (Union[Unset, list[str]]):
        tenant_group_n (Union[Unset, list[str]]):
        tenant_group_id (Union[Unset, list[int]]):
        tenant_group_id_n (Union[Unset, list[int]]):
        tenant_id (Union[Unset, list[int]]):
        tenant_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        weight (Union[Unset, list[int]]):
        weight_empty (Union[Unset, bool]):
        weight_gt (Union[Unset, list[int]]):
        weight_gte (Union[Unset, list[int]]):
        weight_lt (Union[Unset, list[int]]):
        weight_lte (Union[Unset, list[int]]):
        weight_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConfigContextList]
    """

    kwargs = _get_kwargs(
        auto_sync_enabled=auto_sync_enabled,
        cluster_group=cluster_group,
        cluster_group_n=cluster_group_n,
        cluster_group_id=cluster_group_id,
        cluster_group_id_n=cluster_group_id_n,
        cluster_id=cluster_id,
        cluster_id_n=cluster_id_n,
        cluster_type=cluster_type,
        cluster_type_n=cluster_type_n,
        cluster_type_id=cluster_type_id,
        cluster_type_id_n=cluster_type_id_n,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        data_file_id=data_file_id,
        data_file_id_n=data_file_id_n,
        data_source_id=data_source_id,
        data_source_id_n=data_source_id_n,
        data_synced=data_synced,
        data_synced_empty=data_synced_empty,
        data_synced_gt=data_synced_gt,
        data_synced_gte=data_synced_gte,
        data_synced_lt=data_synced_lt,
        data_synced_lte=data_synced_lte,
        data_synced_n=data_synced_n,
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
        device_role=device_role,
        device_role_n=device_role_n,
        device_role_id=device_role_id,
        device_role_id_n=device_role_id_n,
        device_type_id=device_type_id,
        device_type_id_n=device_type_id_n,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        is_active=is_active,
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
        platform=platform,
        platform_n=platform_n,
        platform_id=platform_id,
        platform_id_n=platform_id_n,
        q=q,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        site=site,
        site_n=site_n,
        site_group=site_group,
        site_group_n=site_group_n,
        site_group_id=site_group_id,
        site_group_id_n=site_group_id_n,
        site_id=site_id,
        site_id_n=site_id_n,
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
        weight=weight,
        weight_empty=weight_empty,
        weight_gt=weight_gt,
        weight_gte=weight_gte,
        weight_lt=weight_lt,
        weight_lte=weight_lte,
        weight_n=weight_n,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    auto_sync_enabled: Union[Unset, bool] = UNSET,
    cluster_group: Union[Unset, list[str]] = UNSET,
    cluster_group_n: Union[Unset, list[str]] = UNSET,
    cluster_group_id: Union[Unset, list[int]] = UNSET,
    cluster_group_id_n: Union[Unset, list[int]] = UNSET,
    cluster_id: Union[Unset, list[int]] = UNSET,
    cluster_id_n: Union[Unset, list[int]] = UNSET,
    cluster_type: Union[Unset, list[str]] = UNSET,
    cluster_type_n: Union[Unset, list[str]] = UNSET,
    cluster_type_id: Union[Unset, list[int]] = UNSET,
    cluster_type_id_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    data_file_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_file_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_synced: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_empty: Union[Unset, bool] = UNSET,
    data_synced_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_n: Union[Unset, list[datetime.datetime]] = UNSET,
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
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_id: Union[Unset, list[int]] = UNSET,
    device_role_id_n: Union[Unset, list[int]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
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
    platform: Union[Unset, list[str]] = UNSET,
    platform_n: Union[Unset, list[str]] = UNSET,
    platform_id: Union[Unset, list[int]] = UNSET,
    platform_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[int]] = UNSET,
    region_id_n: Union[Unset, list[int]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[int]] = UNSET,
    site_group_id_n: Union[Unset, list[int]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tenant: Union[Unset, list[str]] = UNSET,
    tenant_n: Union[Unset, list[str]] = UNSET,
    tenant_group: Union[Unset, list[str]] = UNSET,
    tenant_group_n: Union[Unset, list[str]] = UNSET,
    tenant_group_id: Union[Unset, list[int]] = UNSET,
    tenant_group_id_n: Union[Unset, list[int]] = UNSET,
    tenant_id: Union[Unset, list[int]] = UNSET,
    tenant_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    weight: Union[Unset, list[int]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[int]] = UNSET,
    weight_gte: Union[Unset, list[int]] = UNSET,
    weight_lt: Union[Unset, list[int]] = UNSET,
    weight_lte: Union[Unset, list[int]] = UNSET,
    weight_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedConfigContextList]:
    """Get a list of config context objects.

    Args:
        auto_sync_enabled (Union[Unset, bool]):
        cluster_group (Union[Unset, list[str]]):
        cluster_group_n (Union[Unset, list[str]]):
        cluster_group_id (Union[Unset, list[int]]):
        cluster_group_id_n (Union[Unset, list[int]]):
        cluster_id (Union[Unset, list[int]]):
        cluster_id_n (Union[Unset, list[int]]):
        cluster_type (Union[Unset, list[str]]):
        cluster_type_n (Union[Unset, list[str]]):
        cluster_type_id (Union[Unset, list[int]]):
        cluster_type_id_n (Union[Unset, list[int]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        data_file_id (Union[Unset, list[Union[None, int]]]):
        data_file_id_n (Union[Unset, list[Union[None, int]]]):
        data_source_id (Union[Unset, list[Union[None, int]]]):
        data_source_id_n (Union[Unset, list[Union[None, int]]]):
        data_synced (Union[Unset, list[datetime.datetime]]):
        data_synced_empty (Union[Unset, bool]):
        data_synced_gt (Union[Unset, list[datetime.datetime]]):
        data_synced_gte (Union[Unset, list[datetime.datetime]]):
        data_synced_lt (Union[Unset, list[datetime.datetime]]):
        data_synced_lte (Union[Unset, list[datetime.datetime]]):
        data_synced_n (Union[Unset, list[datetime.datetime]]):
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
        device_role (Union[Unset, list[str]]):
        device_role_n (Union[Unset, list[str]]):
        device_role_id (Union[Unset, list[int]]):
        device_role_id_n (Union[Unset, list[int]]):
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_active (Union[Unset, bool]):
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
        platform (Union[Unset, list[str]]):
        platform_n (Union[Unset, list[str]]):
        platform_id (Union[Unset, list[int]]):
        platform_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[int]]):
        region_id_n (Union[Unset, list[int]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[int]]):
        site_group_id_n (Union[Unset, list[int]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        tenant (Union[Unset, list[str]]):
        tenant_n (Union[Unset, list[str]]):
        tenant_group (Union[Unset, list[str]]):
        tenant_group_n (Union[Unset, list[str]]):
        tenant_group_id (Union[Unset, list[int]]):
        tenant_group_id_n (Union[Unset, list[int]]):
        tenant_id (Union[Unset, list[int]]):
        tenant_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        weight (Union[Unset, list[int]]):
        weight_empty (Union[Unset, bool]):
        weight_gt (Union[Unset, list[int]]):
        weight_gte (Union[Unset, list[int]]):
        weight_lt (Union[Unset, list[int]]):
        weight_lte (Union[Unset, list[int]]):
        weight_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConfigContextList
    """

    return (
        await asyncio_detailed(
            client=client,
            auto_sync_enabled=auto_sync_enabled,
            cluster_group=cluster_group,
            cluster_group_n=cluster_group_n,
            cluster_group_id=cluster_group_id,
            cluster_group_id_n=cluster_group_id_n,
            cluster_id=cluster_id,
            cluster_id_n=cluster_id_n,
            cluster_type=cluster_type,
            cluster_type_n=cluster_type_n,
            cluster_type_id=cluster_type_id,
            cluster_type_id_n=cluster_type_id_n,
            created=created,
            created_empty=created_empty,
            created_gt=created_gt,
            created_gte=created_gte,
            created_lt=created_lt,
            created_lte=created_lte,
            created_n=created_n,
            created_by_request=created_by_request,
            data_file_id=data_file_id,
            data_file_id_n=data_file_id_n,
            data_source_id=data_source_id,
            data_source_id_n=data_source_id_n,
            data_synced=data_synced,
            data_synced_empty=data_synced_empty,
            data_synced_gt=data_synced_gt,
            data_synced_gte=data_synced_gte,
            data_synced_lt=data_synced_lt,
            data_synced_lte=data_synced_lte,
            data_synced_n=data_synced_n,
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
            device_role=device_role,
            device_role_n=device_role_n,
            device_role_id=device_role_id,
            device_role_id_n=device_role_id_n,
            device_type_id=device_type_id,
            device_type_id_n=device_type_id_n,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            is_active=is_active,
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
            platform=platform,
            platform_n=platform_n,
            platform_id=platform_id,
            platform_id_n=platform_id_n,
            q=q,
            region=region,
            region_n=region_n,
            region_id=region_id,
            region_id_n=region_id_n,
            site=site,
            site_n=site_n,
            site_group=site_group,
            site_group_n=site_group_n,
            site_group_id=site_group_id,
            site_group_id_n=site_group_id_n,
            site_id=site_id,
            site_id_n=site_id_n,
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
            weight=weight,
            weight_empty=weight_empty,
            weight_gt=weight_gt,
            weight_gte=weight_gte,
            weight_lt=weight_lt,
            weight_lte=weight_lte,
            weight_n=weight_n,
        )
    ).parsed
