import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_data_source_list import PaginatedDataSourceList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
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
    last_synced: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_empty: Union[Unset, bool] = UNSET,
    last_synced_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_n: Union[Unset, list[datetime.datetime]] = UNSET,
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
    source_url: Union[Unset, list[str]] = UNSET,
    source_url_empty: Union[Unset, bool] = UNSET,
    source_url_ic: Union[Unset, list[str]] = UNSET,
    source_url_ie: Union[Unset, list[str]] = UNSET,
    source_url_iew: Union[Unset, list[str]] = UNSET,
    source_url_isw: Union[Unset, list[str]] = UNSET,
    source_url_n: Union[Unset, list[str]] = UNSET,
    source_url_nic: Union[Unset, list[str]] = UNSET,
    source_url_nie: Union[Unset, list[str]] = UNSET,
    source_url_niew: Union[Unset, list[str]] = UNSET,
    source_url_nisw: Union[Unset, list[str]] = UNSET,
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
    sync_interval: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_ic: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_ie: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_iew: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_isw: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_n: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_nic: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_nie: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_niew: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_nisw: Union[Unset, list[Union[None, int]]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
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
) -> dict[str, Any]:
    params: dict[str, Any] = {}

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

    json_last_synced: Union[Unset, list[str]] = UNSET
    if not isinstance(last_synced, Unset):
        json_last_synced = []
        for last_synced_item_data in last_synced:
            last_synced_item = last_synced_item_data.isoformat()
            json_last_synced.append(last_synced_item)

    params["last_synced"] = json_last_synced

    params["last_synced__empty"] = last_synced_empty

    json_last_synced_gt: Union[Unset, list[str]] = UNSET
    if not isinstance(last_synced_gt, Unset):
        json_last_synced_gt = []
        for last_synced_gt_item_data in last_synced_gt:
            last_synced_gt_item = last_synced_gt_item_data.isoformat()
            json_last_synced_gt.append(last_synced_gt_item)

    params["last_synced__gt"] = json_last_synced_gt

    json_last_synced_gte: Union[Unset, list[str]] = UNSET
    if not isinstance(last_synced_gte, Unset):
        json_last_synced_gte = []
        for last_synced_gte_item_data in last_synced_gte:
            last_synced_gte_item = last_synced_gte_item_data.isoformat()
            json_last_synced_gte.append(last_synced_gte_item)

    params["last_synced__gte"] = json_last_synced_gte

    json_last_synced_lt: Union[Unset, list[str]] = UNSET
    if not isinstance(last_synced_lt, Unset):
        json_last_synced_lt = []
        for last_synced_lt_item_data in last_synced_lt:
            last_synced_lt_item = last_synced_lt_item_data.isoformat()
            json_last_synced_lt.append(last_synced_lt_item)

    params["last_synced__lt"] = json_last_synced_lt

    json_last_synced_lte: Union[Unset, list[str]] = UNSET
    if not isinstance(last_synced_lte, Unset):
        json_last_synced_lte = []
        for last_synced_lte_item_data in last_synced_lte:
            last_synced_lte_item = last_synced_lte_item_data.isoformat()
            json_last_synced_lte.append(last_synced_lte_item)

    params["last_synced__lte"] = json_last_synced_lte

    json_last_synced_n: Union[Unset, list[str]] = UNSET
    if not isinstance(last_synced_n, Unset):
        json_last_synced_n = []
        for last_synced_n_item_data in last_synced_n:
            last_synced_n_item = last_synced_n_item_data.isoformat()
            json_last_synced_n.append(last_synced_n_item)

    params["last_synced__n"] = json_last_synced_n

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

    json_source_url: Union[Unset, list[str]] = UNSET
    if not isinstance(source_url, Unset):
        json_source_url = source_url

    params["source_url"] = json_source_url

    params["source_url__empty"] = source_url_empty

    json_source_url_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(source_url_ic, Unset):
        json_source_url_ic = source_url_ic

    params["source_url__ic"] = json_source_url_ic

    json_source_url_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(source_url_ie, Unset):
        json_source_url_ie = source_url_ie

    params["source_url__ie"] = json_source_url_ie

    json_source_url_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(source_url_iew, Unset):
        json_source_url_iew = source_url_iew

    params["source_url__iew"] = json_source_url_iew

    json_source_url_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(source_url_isw, Unset):
        json_source_url_isw = source_url_isw

    params["source_url__isw"] = json_source_url_isw

    json_source_url_n: Union[Unset, list[str]] = UNSET
    if not isinstance(source_url_n, Unset):
        json_source_url_n = source_url_n

    params["source_url__n"] = json_source_url_n

    json_source_url_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(source_url_nic, Unset):
        json_source_url_nic = source_url_nic

    params["source_url__nic"] = json_source_url_nic

    json_source_url_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(source_url_nie, Unset):
        json_source_url_nie = source_url_nie

    params["source_url__nie"] = json_source_url_nie

    json_source_url_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(source_url_niew, Unset):
        json_source_url_niew = source_url_niew

    params["source_url__niew"] = json_source_url_niew

    json_source_url_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(source_url_nisw, Unset):
        json_source_url_nisw = source_url_nisw

    params["source_url__nisw"] = json_source_url_nisw

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

    json_sync_interval: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(sync_interval, Unset):
        json_sync_interval = []
        for sync_interval_item_data in sync_interval:
            sync_interval_item: Union[None, int]
            sync_interval_item = sync_interval_item_data
            json_sync_interval.append(sync_interval_item)

    params["sync_interval"] = json_sync_interval

    json_sync_interval_ic: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(sync_interval_ic, Unset):
        json_sync_interval_ic = []
        for sync_interval_ic_item_data in sync_interval_ic:
            sync_interval_ic_item: Union[None, int]
            sync_interval_ic_item = sync_interval_ic_item_data
            json_sync_interval_ic.append(sync_interval_ic_item)

    params["sync_interval__ic"] = json_sync_interval_ic

    json_sync_interval_ie: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(sync_interval_ie, Unset):
        json_sync_interval_ie = []
        for sync_interval_ie_item_data in sync_interval_ie:
            sync_interval_ie_item: Union[None, int]
            sync_interval_ie_item = sync_interval_ie_item_data
            json_sync_interval_ie.append(sync_interval_ie_item)

    params["sync_interval__ie"] = json_sync_interval_ie

    json_sync_interval_iew: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(sync_interval_iew, Unset):
        json_sync_interval_iew = []
        for sync_interval_iew_item_data in sync_interval_iew:
            sync_interval_iew_item: Union[None, int]
            sync_interval_iew_item = sync_interval_iew_item_data
            json_sync_interval_iew.append(sync_interval_iew_item)

    params["sync_interval__iew"] = json_sync_interval_iew

    json_sync_interval_isw: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(sync_interval_isw, Unset):
        json_sync_interval_isw = []
        for sync_interval_isw_item_data in sync_interval_isw:
            sync_interval_isw_item: Union[None, int]
            sync_interval_isw_item = sync_interval_isw_item_data
            json_sync_interval_isw.append(sync_interval_isw_item)

    params["sync_interval__isw"] = json_sync_interval_isw

    json_sync_interval_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(sync_interval_n, Unset):
        json_sync_interval_n = []
        for sync_interval_n_item_data in sync_interval_n:
            sync_interval_n_item: Union[None, int]
            sync_interval_n_item = sync_interval_n_item_data
            json_sync_interval_n.append(sync_interval_n_item)

    params["sync_interval__n"] = json_sync_interval_n

    json_sync_interval_nic: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(sync_interval_nic, Unset):
        json_sync_interval_nic = []
        for sync_interval_nic_item_data in sync_interval_nic:
            sync_interval_nic_item: Union[None, int]
            sync_interval_nic_item = sync_interval_nic_item_data
            json_sync_interval_nic.append(sync_interval_nic_item)

    params["sync_interval__nic"] = json_sync_interval_nic

    json_sync_interval_nie: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(sync_interval_nie, Unset):
        json_sync_interval_nie = []
        for sync_interval_nie_item_data in sync_interval_nie:
            sync_interval_nie_item: Union[None, int]
            sync_interval_nie_item = sync_interval_nie_item_data
            json_sync_interval_nie.append(sync_interval_nie_item)

    params["sync_interval__nie"] = json_sync_interval_nie

    json_sync_interval_niew: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(sync_interval_niew, Unset):
        json_sync_interval_niew = []
        for sync_interval_niew_item_data in sync_interval_niew:
            sync_interval_niew_item: Union[None, int]
            sync_interval_niew_item = sync_interval_niew_item_data
            json_sync_interval_niew.append(sync_interval_niew_item)

    params["sync_interval__niew"] = json_sync_interval_niew

    json_sync_interval_nisw: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(sync_interval_nisw, Unset):
        json_sync_interval_nisw = []
        for sync_interval_nisw_item_data in sync_interval_nisw:
            sync_interval_nisw_item: Union[None, int]
            sync_interval_nisw_item = sync_interval_nisw_item_data
            json_sync_interval_nisw.append(sync_interval_nisw_item)

    params["sync_interval__nisw"] = json_sync_interval_nisw

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/data-sources/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedDataSourceList]:
    if response.status_code == 200:
        response_200 = PaginatedDataSourceList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedDataSourceList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
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
    last_synced: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_empty: Union[Unset, bool] = UNSET,
    last_synced_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_n: Union[Unset, list[datetime.datetime]] = UNSET,
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
    source_url: Union[Unset, list[str]] = UNSET,
    source_url_empty: Union[Unset, bool] = UNSET,
    source_url_ic: Union[Unset, list[str]] = UNSET,
    source_url_ie: Union[Unset, list[str]] = UNSET,
    source_url_iew: Union[Unset, list[str]] = UNSET,
    source_url_isw: Union[Unset, list[str]] = UNSET,
    source_url_n: Union[Unset, list[str]] = UNSET,
    source_url_nic: Union[Unset, list[str]] = UNSET,
    source_url_nie: Union[Unset, list[str]] = UNSET,
    source_url_niew: Union[Unset, list[str]] = UNSET,
    source_url_nisw: Union[Unset, list[str]] = UNSET,
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
    sync_interval: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_ic: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_ie: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_iew: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_isw: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_n: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_nic: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_nie: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_niew: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_nisw: Union[Unset, list[Union[None, int]]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
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
) -> Response[PaginatedDataSourceList]:
    """Get a list of data source objects.

    Args:
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
        last_synced (Union[Unset, list[datetime.datetime]]):
        last_synced_empty (Union[Unset, bool]):
        last_synced_gt (Union[Unset, list[datetime.datetime]]):
        last_synced_gte (Union[Unset, list[datetime.datetime]]):
        last_synced_lt (Union[Unset, list[datetime.datetime]]):
        last_synced_lte (Union[Unset, list[datetime.datetime]]):
        last_synced_n (Union[Unset, list[datetime.datetime]]):
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
        source_url (Union[Unset, list[str]]):
        source_url_empty (Union[Unset, bool]):
        source_url_ic (Union[Unset, list[str]]):
        source_url_ie (Union[Unset, list[str]]):
        source_url_iew (Union[Unset, list[str]]):
        source_url_isw (Union[Unset, list[str]]):
        source_url_n (Union[Unset, list[str]]):
        source_url_nic (Union[Unset, list[str]]):
        source_url_nie (Union[Unset, list[str]]):
        source_url_niew (Union[Unset, list[str]]):
        source_url_nisw (Union[Unset, list[str]]):
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
        sync_interval (Union[Unset, list[Union[None, int]]]):
        sync_interval_ic (Union[Unset, list[Union[None, int]]]):
        sync_interval_ie (Union[Unset, list[Union[None, int]]]):
        sync_interval_iew (Union[Unset, list[Union[None, int]]]):
        sync_interval_isw (Union[Unset, list[Union[None, int]]]):
        sync_interval_n (Union[Unset, list[Union[None, int]]]):
        sync_interval_nic (Union[Unset, list[Union[None, int]]]):
        sync_interval_nie (Union[Unset, list[Union[None, int]]]):
        sync_interval_niew (Union[Unset, list[Union[None, int]]]):
        sync_interval_nisw (Union[Unset, list[Union[None, int]]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDataSourceList]
    """

    kwargs = _get_kwargs(
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
        last_synced=last_synced,
        last_synced_empty=last_synced_empty,
        last_synced_gt=last_synced_gt,
        last_synced_gte=last_synced_gte,
        last_synced_lt=last_synced_lt,
        last_synced_lte=last_synced_lte,
        last_synced_n=last_synced_n,
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
        source_url=source_url,
        source_url_empty=source_url_empty,
        source_url_ic=source_url_ic,
        source_url_ie=source_url_ie,
        source_url_iew=source_url_iew,
        source_url_isw=source_url_isw,
        source_url_n=source_url_n,
        source_url_nic=source_url_nic,
        source_url_nie=source_url_nie,
        source_url_niew=source_url_niew,
        source_url_nisw=source_url_nisw,
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
        sync_interval=sync_interval,
        sync_interval_ic=sync_interval_ic,
        sync_interval_ie=sync_interval_ie,
        sync_interval_iew=sync_interval_iew,
        sync_interval_isw=sync_interval_isw,
        sync_interval_n=sync_interval_n,
        sync_interval_nic=sync_interval_nic,
        sync_interval_nie=sync_interval_nie,
        sync_interval_niew=sync_interval_niew,
        sync_interval_nisw=sync_interval_nisw,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
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
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
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
    last_synced: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_empty: Union[Unset, bool] = UNSET,
    last_synced_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_n: Union[Unset, list[datetime.datetime]] = UNSET,
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
    source_url: Union[Unset, list[str]] = UNSET,
    source_url_empty: Union[Unset, bool] = UNSET,
    source_url_ic: Union[Unset, list[str]] = UNSET,
    source_url_ie: Union[Unset, list[str]] = UNSET,
    source_url_iew: Union[Unset, list[str]] = UNSET,
    source_url_isw: Union[Unset, list[str]] = UNSET,
    source_url_n: Union[Unset, list[str]] = UNSET,
    source_url_nic: Union[Unset, list[str]] = UNSET,
    source_url_nie: Union[Unset, list[str]] = UNSET,
    source_url_niew: Union[Unset, list[str]] = UNSET,
    source_url_nisw: Union[Unset, list[str]] = UNSET,
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
    sync_interval: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_ic: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_ie: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_iew: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_isw: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_n: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_nic: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_nie: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_niew: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_nisw: Union[Unset, list[Union[None, int]]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
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
) -> Optional[PaginatedDataSourceList]:
    """Get a list of data source objects.

    Args:
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
        last_synced (Union[Unset, list[datetime.datetime]]):
        last_synced_empty (Union[Unset, bool]):
        last_synced_gt (Union[Unset, list[datetime.datetime]]):
        last_synced_gte (Union[Unset, list[datetime.datetime]]):
        last_synced_lt (Union[Unset, list[datetime.datetime]]):
        last_synced_lte (Union[Unset, list[datetime.datetime]]):
        last_synced_n (Union[Unset, list[datetime.datetime]]):
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
        source_url (Union[Unset, list[str]]):
        source_url_empty (Union[Unset, bool]):
        source_url_ic (Union[Unset, list[str]]):
        source_url_ie (Union[Unset, list[str]]):
        source_url_iew (Union[Unset, list[str]]):
        source_url_isw (Union[Unset, list[str]]):
        source_url_n (Union[Unset, list[str]]):
        source_url_nic (Union[Unset, list[str]]):
        source_url_nie (Union[Unset, list[str]]):
        source_url_niew (Union[Unset, list[str]]):
        source_url_nisw (Union[Unset, list[str]]):
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
        sync_interval (Union[Unset, list[Union[None, int]]]):
        sync_interval_ic (Union[Unset, list[Union[None, int]]]):
        sync_interval_ie (Union[Unset, list[Union[None, int]]]):
        sync_interval_iew (Union[Unset, list[Union[None, int]]]):
        sync_interval_isw (Union[Unset, list[Union[None, int]]]):
        sync_interval_n (Union[Unset, list[Union[None, int]]]):
        sync_interval_nic (Union[Unset, list[Union[None, int]]]):
        sync_interval_nie (Union[Unset, list[Union[None, int]]]):
        sync_interval_niew (Union[Unset, list[Union[None, int]]]):
        sync_interval_nisw (Union[Unset, list[Union[None, int]]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDataSourceList
    """

    return sync_detailed(
        client=client,
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
        last_synced=last_synced,
        last_synced_empty=last_synced_empty,
        last_synced_gt=last_synced_gt,
        last_synced_gte=last_synced_gte,
        last_synced_lt=last_synced_lt,
        last_synced_lte=last_synced_lte,
        last_synced_n=last_synced_n,
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
        source_url=source_url,
        source_url_empty=source_url_empty,
        source_url_ic=source_url_ic,
        source_url_ie=source_url_ie,
        source_url_iew=source_url_iew,
        source_url_isw=source_url_isw,
        source_url_n=source_url_n,
        source_url_nic=source_url_nic,
        source_url_nie=source_url_nie,
        source_url_niew=source_url_niew,
        source_url_nisw=source_url_nisw,
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
        sync_interval=sync_interval,
        sync_interval_ic=sync_interval_ic,
        sync_interval_ie=sync_interval_ie,
        sync_interval_iew=sync_interval_iew,
        sync_interval_isw=sync_interval_isw,
        sync_interval_n=sync_interval_n,
        sync_interval_nic=sync_interval_nic,
        sync_interval_nie=sync_interval_nie,
        sync_interval_niew=sync_interval_niew,
        sync_interval_nisw=sync_interval_nisw,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
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
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
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
    last_synced: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_empty: Union[Unset, bool] = UNSET,
    last_synced_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_n: Union[Unset, list[datetime.datetime]] = UNSET,
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
    source_url: Union[Unset, list[str]] = UNSET,
    source_url_empty: Union[Unset, bool] = UNSET,
    source_url_ic: Union[Unset, list[str]] = UNSET,
    source_url_ie: Union[Unset, list[str]] = UNSET,
    source_url_iew: Union[Unset, list[str]] = UNSET,
    source_url_isw: Union[Unset, list[str]] = UNSET,
    source_url_n: Union[Unset, list[str]] = UNSET,
    source_url_nic: Union[Unset, list[str]] = UNSET,
    source_url_nie: Union[Unset, list[str]] = UNSET,
    source_url_niew: Union[Unset, list[str]] = UNSET,
    source_url_nisw: Union[Unset, list[str]] = UNSET,
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
    sync_interval: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_ic: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_ie: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_iew: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_isw: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_n: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_nic: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_nie: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_niew: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_nisw: Union[Unset, list[Union[None, int]]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
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
) -> Response[PaginatedDataSourceList]:
    """Get a list of data source objects.

    Args:
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
        last_synced (Union[Unset, list[datetime.datetime]]):
        last_synced_empty (Union[Unset, bool]):
        last_synced_gt (Union[Unset, list[datetime.datetime]]):
        last_synced_gte (Union[Unset, list[datetime.datetime]]):
        last_synced_lt (Union[Unset, list[datetime.datetime]]):
        last_synced_lte (Union[Unset, list[datetime.datetime]]):
        last_synced_n (Union[Unset, list[datetime.datetime]]):
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
        source_url (Union[Unset, list[str]]):
        source_url_empty (Union[Unset, bool]):
        source_url_ic (Union[Unset, list[str]]):
        source_url_ie (Union[Unset, list[str]]):
        source_url_iew (Union[Unset, list[str]]):
        source_url_isw (Union[Unset, list[str]]):
        source_url_n (Union[Unset, list[str]]):
        source_url_nic (Union[Unset, list[str]]):
        source_url_nie (Union[Unset, list[str]]):
        source_url_niew (Union[Unset, list[str]]):
        source_url_nisw (Union[Unset, list[str]]):
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
        sync_interval (Union[Unset, list[Union[None, int]]]):
        sync_interval_ic (Union[Unset, list[Union[None, int]]]):
        sync_interval_ie (Union[Unset, list[Union[None, int]]]):
        sync_interval_iew (Union[Unset, list[Union[None, int]]]):
        sync_interval_isw (Union[Unset, list[Union[None, int]]]):
        sync_interval_n (Union[Unset, list[Union[None, int]]]):
        sync_interval_nic (Union[Unset, list[Union[None, int]]]):
        sync_interval_nie (Union[Unset, list[Union[None, int]]]):
        sync_interval_niew (Union[Unset, list[Union[None, int]]]):
        sync_interval_nisw (Union[Unset, list[Union[None, int]]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDataSourceList]
    """

    kwargs = _get_kwargs(
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
        last_synced=last_synced,
        last_synced_empty=last_synced_empty,
        last_synced_gt=last_synced_gt,
        last_synced_gte=last_synced_gte,
        last_synced_lt=last_synced_lt,
        last_synced_lte=last_synced_lte,
        last_synced_n=last_synced_n,
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
        source_url=source_url,
        source_url_empty=source_url_empty,
        source_url_ic=source_url_ic,
        source_url_ie=source_url_ie,
        source_url_iew=source_url_iew,
        source_url_isw=source_url_isw,
        source_url_n=source_url_n,
        source_url_nic=source_url_nic,
        source_url_nie=source_url_nie,
        source_url_niew=source_url_niew,
        source_url_nisw=source_url_nisw,
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
        sync_interval=sync_interval,
        sync_interval_ic=sync_interval_ic,
        sync_interval_ie=sync_interval_ie,
        sync_interval_iew=sync_interval_iew,
        sync_interval_isw=sync_interval_isw,
        sync_interval_n=sync_interval_n,
        sync_interval_nic=sync_interval_nic,
        sync_interval_nie=sync_interval_nie,
        sync_interval_niew=sync_interval_niew,
        sync_interval_nisw=sync_interval_nisw,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
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
    last_synced: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_empty: Union[Unset, bool] = UNSET,
    last_synced_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_synced_n: Union[Unset, list[datetime.datetime]] = UNSET,
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
    source_url: Union[Unset, list[str]] = UNSET,
    source_url_empty: Union[Unset, bool] = UNSET,
    source_url_ic: Union[Unset, list[str]] = UNSET,
    source_url_ie: Union[Unset, list[str]] = UNSET,
    source_url_iew: Union[Unset, list[str]] = UNSET,
    source_url_isw: Union[Unset, list[str]] = UNSET,
    source_url_n: Union[Unset, list[str]] = UNSET,
    source_url_nic: Union[Unset, list[str]] = UNSET,
    source_url_nie: Union[Unset, list[str]] = UNSET,
    source_url_niew: Union[Unset, list[str]] = UNSET,
    source_url_nisw: Union[Unset, list[str]] = UNSET,
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
    sync_interval: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_ic: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_ie: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_iew: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_isw: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_n: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_nic: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_nie: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_niew: Union[Unset, list[Union[None, int]]] = UNSET,
    sync_interval_nisw: Union[Unset, list[Union[None, int]]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
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
) -> Optional[PaginatedDataSourceList]:
    """Get a list of data source objects.

    Args:
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
        last_synced (Union[Unset, list[datetime.datetime]]):
        last_synced_empty (Union[Unset, bool]):
        last_synced_gt (Union[Unset, list[datetime.datetime]]):
        last_synced_gte (Union[Unset, list[datetime.datetime]]):
        last_synced_lt (Union[Unset, list[datetime.datetime]]):
        last_synced_lte (Union[Unset, list[datetime.datetime]]):
        last_synced_n (Union[Unset, list[datetime.datetime]]):
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
        source_url (Union[Unset, list[str]]):
        source_url_empty (Union[Unset, bool]):
        source_url_ic (Union[Unset, list[str]]):
        source_url_ie (Union[Unset, list[str]]):
        source_url_iew (Union[Unset, list[str]]):
        source_url_isw (Union[Unset, list[str]]):
        source_url_n (Union[Unset, list[str]]):
        source_url_nic (Union[Unset, list[str]]):
        source_url_nie (Union[Unset, list[str]]):
        source_url_niew (Union[Unset, list[str]]):
        source_url_nisw (Union[Unset, list[str]]):
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
        sync_interval (Union[Unset, list[Union[None, int]]]):
        sync_interval_ic (Union[Unset, list[Union[None, int]]]):
        sync_interval_ie (Union[Unset, list[Union[None, int]]]):
        sync_interval_iew (Union[Unset, list[Union[None, int]]]):
        sync_interval_isw (Union[Unset, list[Union[None, int]]]):
        sync_interval_n (Union[Unset, list[Union[None, int]]]):
        sync_interval_nic (Union[Unset, list[Union[None, int]]]):
        sync_interval_nie (Union[Unset, list[Union[None, int]]]):
        sync_interval_niew (Union[Unset, list[Union[None, int]]]):
        sync_interval_nisw (Union[Unset, list[Union[None, int]]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDataSourceList
    """

    return (
        await asyncio_detailed(
            client=client,
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
            last_synced=last_synced,
            last_synced_empty=last_synced_empty,
            last_synced_gt=last_synced_gt,
            last_synced_gte=last_synced_gte,
            last_synced_lt=last_synced_lt,
            last_synced_lte=last_synced_lte,
            last_synced_n=last_synced_n,
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
            source_url=source_url,
            source_url_empty=source_url_empty,
            source_url_ic=source_url_ic,
            source_url_ie=source_url_ie,
            source_url_iew=source_url_iew,
            source_url_isw=source_url_isw,
            source_url_n=source_url_n,
            source_url_nic=source_url_nic,
            source_url_nie=source_url_nie,
            source_url_niew=source_url_niew,
            source_url_nisw=source_url_nisw,
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
            sync_interval=sync_interval,
            sync_interval_ic=sync_interval_ic,
            sync_interval_ie=sync_interval_ie,
            sync_interval_iew=sync_interval_iew,
            sync_interval_isw=sync_interval_isw,
            sync_interval_n=sync_interval_n,
            sync_interval_nic=sync_interval_nic,
            sync_interval_nie=sync_interval_nie,
            sync_interval_niew=sync_interval_niew,
            sync_interval_nisw=sync_interval_nisw,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
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
        )
    ).parsed
