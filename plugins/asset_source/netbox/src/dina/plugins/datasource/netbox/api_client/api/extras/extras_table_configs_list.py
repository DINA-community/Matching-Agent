import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_table_config_list import PaginatedTableConfigList
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
    object_type: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    table: Union[Unset, list[str]] = UNSET,
    table_empty: Union[Unset, bool] = UNSET,
    table_ic: Union[Unset, list[str]] = UNSET,
    table_ie: Union[Unset, list[str]] = UNSET,
    table_iew: Union[Unset, list[str]] = UNSET,
    table_isw: Union[Unset, list[str]] = UNSET,
    table_n: Union[Unset, list[str]] = UNSET,
    table_nic: Union[Unset, list[str]] = UNSET,
    table_nie: Union[Unset, list[str]] = UNSET,
    table_niew: Union[Unset, list[str]] = UNSET,
    table_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    usable: Union[Unset, bool] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[Union[None, int]]] = UNSET,
    user_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    weight: Union[Unset, list[int]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[int]] = UNSET,
    weight_gte: Union[Unset, list[int]] = UNSET,
    weight_lt: Union[Unset, list[int]] = UNSET,
    weight_lte: Union[Unset, list[int]] = UNSET,
    weight_n: Union[Unset, list[int]] = UNSET,
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

    params["object_type"] = object_type

    params["object_type__n"] = object_type_n

    json_object_type_id: Union[Unset, list[int]] = UNSET
    if not isinstance(object_type_id, Unset):
        json_object_type_id = object_type_id

    params["object_type_id"] = json_object_type_id

    json_object_type_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(object_type_id_n, Unset):
        json_object_type_id_n = object_type_id_n

    params["object_type_id__n"] = json_object_type_id_n

    params["offset"] = offset

    params["ordering"] = ordering

    params["q"] = q

    params["shared"] = shared

    json_table: Union[Unset, list[str]] = UNSET
    if not isinstance(table, Unset):
        json_table = table

    params["table"] = json_table

    params["table__empty"] = table_empty

    json_table_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(table_ic, Unset):
        json_table_ic = table_ic

    params["table__ic"] = json_table_ic

    json_table_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(table_ie, Unset):
        json_table_ie = table_ie

    params["table__ie"] = json_table_ie

    json_table_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(table_iew, Unset):
        json_table_iew = table_iew

    params["table__iew"] = json_table_iew

    json_table_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(table_isw, Unset):
        json_table_isw = table_isw

    params["table__isw"] = json_table_isw

    json_table_n: Union[Unset, list[str]] = UNSET
    if not isinstance(table_n, Unset):
        json_table_n = table_n

    params["table__n"] = json_table_n

    json_table_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(table_nic, Unset):
        json_table_nic = table_nic

    params["table__nic"] = json_table_nic

    json_table_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(table_nie, Unset):
        json_table_nie = table_nie

    params["table__nie"] = json_table_nie

    json_table_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(table_niew, Unset):
        json_table_niew = table_niew

    params["table__niew"] = json_table_niew

    json_table_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(table_nisw, Unset):
        json_table_nisw = table_nisw

    params["table__nisw"] = json_table_nisw

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    params["usable"] = usable

    json_user: Union[Unset, list[str]] = UNSET
    if not isinstance(user, Unset):
        json_user = user

    params["user"] = json_user

    json_user_n: Union[Unset, list[str]] = UNSET
    if not isinstance(user_n, Unset):
        json_user_n = user_n

    params["user__n"] = json_user_n

    json_user_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = []
        for user_id_item_data in user_id:
            user_id_item: Union[None, int]
            user_id_item = user_id_item_data
            json_user_id.append(user_id_item)

    params["user_id"] = json_user_id

    json_user_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(user_id_n, Unset):
        json_user_id_n = []
        for user_id_n_item_data in user_id_n:
            user_id_n_item: Union[None, int]
            user_id_n_item = user_id_n_item_data
            json_user_id_n.append(user_id_n_item)

    params["user_id__n"] = json_user_id_n

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
        "url": "/api/extras/table-configs/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedTableConfigList]:
    if response.status_code == 200:
        response_200 = PaginatedTableConfigList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedTableConfigList]:
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
    object_type: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    table: Union[Unset, list[str]] = UNSET,
    table_empty: Union[Unset, bool] = UNSET,
    table_ic: Union[Unset, list[str]] = UNSET,
    table_ie: Union[Unset, list[str]] = UNSET,
    table_iew: Union[Unset, list[str]] = UNSET,
    table_isw: Union[Unset, list[str]] = UNSET,
    table_n: Union[Unset, list[str]] = UNSET,
    table_nic: Union[Unset, list[str]] = UNSET,
    table_nie: Union[Unset, list[str]] = UNSET,
    table_niew: Union[Unset, list[str]] = UNSET,
    table_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    usable: Union[Unset, bool] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[Union[None, int]]] = UNSET,
    user_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    weight: Union[Unset, list[int]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[int]] = UNSET,
    weight_gte: Union[Unset, list[int]] = UNSET,
    weight_lt: Union[Unset, list[int]] = UNSET,
    weight_lte: Union[Unset, list[int]] = UNSET,
    weight_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedTableConfigList]:
    """Get a list of table config objects.

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
        object_type (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_id (Union[Unset, list[int]]):
        object_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        shared (Union[Unset, bool]):
        table (Union[Unset, list[str]]):
        table_empty (Union[Unset, bool]):
        table_ic (Union[Unset, list[str]]):
        table_ie (Union[Unset, list[str]]):
        table_iew (Union[Unset, list[str]]):
        table_isw (Union[Unset, list[str]]):
        table_n (Union[Unset, list[str]]):
        table_nic (Union[Unset, list[str]]):
        table_nie (Union[Unset, list[str]]):
        table_niew (Union[Unset, list[str]]):
        table_nisw (Union[Unset, list[str]]):
        updated_by_request (Union[Unset, UUID]):
        usable (Union[Unset, bool]):
        user (Union[Unset, list[str]]):
        user_n (Union[Unset, list[str]]):
        user_id (Union[Unset, list[Union[None, int]]]):
        user_id_n (Union[Unset, list[Union[None, int]]]):
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
        Response[PaginatedTableConfigList]
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
        object_type=object_type,
        object_type_n=object_type_n,
        object_type_id=object_type_id,
        object_type_id_n=object_type_id_n,
        offset=offset,
        ordering=ordering,
        q=q,
        shared=shared,
        table=table,
        table_empty=table_empty,
        table_ic=table_ic,
        table_ie=table_ie,
        table_iew=table_iew,
        table_isw=table_isw,
        table_n=table_n,
        table_nic=table_nic,
        table_nie=table_nie,
        table_niew=table_niew,
        table_nisw=table_nisw,
        updated_by_request=updated_by_request,
        usable=usable,
        user=user,
        user_n=user_n,
        user_id=user_id,
        user_id_n=user_id_n,
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
    object_type: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    table: Union[Unset, list[str]] = UNSET,
    table_empty: Union[Unset, bool] = UNSET,
    table_ic: Union[Unset, list[str]] = UNSET,
    table_ie: Union[Unset, list[str]] = UNSET,
    table_iew: Union[Unset, list[str]] = UNSET,
    table_isw: Union[Unset, list[str]] = UNSET,
    table_n: Union[Unset, list[str]] = UNSET,
    table_nic: Union[Unset, list[str]] = UNSET,
    table_nie: Union[Unset, list[str]] = UNSET,
    table_niew: Union[Unset, list[str]] = UNSET,
    table_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    usable: Union[Unset, bool] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[Union[None, int]]] = UNSET,
    user_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    weight: Union[Unset, list[int]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[int]] = UNSET,
    weight_gte: Union[Unset, list[int]] = UNSET,
    weight_lt: Union[Unset, list[int]] = UNSET,
    weight_lte: Union[Unset, list[int]] = UNSET,
    weight_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedTableConfigList]:
    """Get a list of table config objects.

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
        object_type (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_id (Union[Unset, list[int]]):
        object_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        shared (Union[Unset, bool]):
        table (Union[Unset, list[str]]):
        table_empty (Union[Unset, bool]):
        table_ic (Union[Unset, list[str]]):
        table_ie (Union[Unset, list[str]]):
        table_iew (Union[Unset, list[str]]):
        table_isw (Union[Unset, list[str]]):
        table_n (Union[Unset, list[str]]):
        table_nic (Union[Unset, list[str]]):
        table_nie (Union[Unset, list[str]]):
        table_niew (Union[Unset, list[str]]):
        table_nisw (Union[Unset, list[str]]):
        updated_by_request (Union[Unset, UUID]):
        usable (Union[Unset, bool]):
        user (Union[Unset, list[str]]):
        user_n (Union[Unset, list[str]]):
        user_id (Union[Unset, list[Union[None, int]]]):
        user_id_n (Union[Unset, list[Union[None, int]]]):
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
        PaginatedTableConfigList
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
        object_type=object_type,
        object_type_n=object_type_n,
        object_type_id=object_type_id,
        object_type_id_n=object_type_id_n,
        offset=offset,
        ordering=ordering,
        q=q,
        shared=shared,
        table=table,
        table_empty=table_empty,
        table_ic=table_ic,
        table_ie=table_ie,
        table_iew=table_iew,
        table_isw=table_isw,
        table_n=table_n,
        table_nic=table_nic,
        table_nie=table_nie,
        table_niew=table_niew,
        table_nisw=table_nisw,
        updated_by_request=updated_by_request,
        usable=usable,
        user=user,
        user_n=user_n,
        user_id=user_id,
        user_id_n=user_id_n,
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
    object_type: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    table: Union[Unset, list[str]] = UNSET,
    table_empty: Union[Unset, bool] = UNSET,
    table_ic: Union[Unset, list[str]] = UNSET,
    table_ie: Union[Unset, list[str]] = UNSET,
    table_iew: Union[Unset, list[str]] = UNSET,
    table_isw: Union[Unset, list[str]] = UNSET,
    table_n: Union[Unset, list[str]] = UNSET,
    table_nic: Union[Unset, list[str]] = UNSET,
    table_nie: Union[Unset, list[str]] = UNSET,
    table_niew: Union[Unset, list[str]] = UNSET,
    table_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    usable: Union[Unset, bool] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[Union[None, int]]] = UNSET,
    user_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    weight: Union[Unset, list[int]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[int]] = UNSET,
    weight_gte: Union[Unset, list[int]] = UNSET,
    weight_lt: Union[Unset, list[int]] = UNSET,
    weight_lte: Union[Unset, list[int]] = UNSET,
    weight_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedTableConfigList]:
    """Get a list of table config objects.

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
        object_type (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_id (Union[Unset, list[int]]):
        object_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        shared (Union[Unset, bool]):
        table (Union[Unset, list[str]]):
        table_empty (Union[Unset, bool]):
        table_ic (Union[Unset, list[str]]):
        table_ie (Union[Unset, list[str]]):
        table_iew (Union[Unset, list[str]]):
        table_isw (Union[Unset, list[str]]):
        table_n (Union[Unset, list[str]]):
        table_nic (Union[Unset, list[str]]):
        table_nie (Union[Unset, list[str]]):
        table_niew (Union[Unset, list[str]]):
        table_nisw (Union[Unset, list[str]]):
        updated_by_request (Union[Unset, UUID]):
        usable (Union[Unset, bool]):
        user (Union[Unset, list[str]]):
        user_n (Union[Unset, list[str]]):
        user_id (Union[Unset, list[Union[None, int]]]):
        user_id_n (Union[Unset, list[Union[None, int]]]):
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
        Response[PaginatedTableConfigList]
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
        object_type=object_type,
        object_type_n=object_type_n,
        object_type_id=object_type_id,
        object_type_id_n=object_type_id_n,
        offset=offset,
        ordering=ordering,
        q=q,
        shared=shared,
        table=table,
        table_empty=table_empty,
        table_ic=table_ic,
        table_ie=table_ie,
        table_iew=table_iew,
        table_isw=table_isw,
        table_n=table_n,
        table_nic=table_nic,
        table_nie=table_nie,
        table_niew=table_niew,
        table_nisw=table_nisw,
        updated_by_request=updated_by_request,
        usable=usable,
        user=user,
        user_n=user_n,
        user_id=user_id,
        user_id_n=user_id_n,
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
    object_type: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    shared: Union[Unset, bool] = UNSET,
    table: Union[Unset, list[str]] = UNSET,
    table_empty: Union[Unset, bool] = UNSET,
    table_ic: Union[Unset, list[str]] = UNSET,
    table_ie: Union[Unset, list[str]] = UNSET,
    table_iew: Union[Unset, list[str]] = UNSET,
    table_isw: Union[Unset, list[str]] = UNSET,
    table_n: Union[Unset, list[str]] = UNSET,
    table_nic: Union[Unset, list[str]] = UNSET,
    table_nie: Union[Unset, list[str]] = UNSET,
    table_niew: Union[Unset, list[str]] = UNSET,
    table_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    usable: Union[Unset, bool] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[Union[None, int]]] = UNSET,
    user_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    weight: Union[Unset, list[int]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[int]] = UNSET,
    weight_gte: Union[Unset, list[int]] = UNSET,
    weight_lt: Union[Unset, list[int]] = UNSET,
    weight_lte: Union[Unset, list[int]] = UNSET,
    weight_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedTableConfigList]:
    """Get a list of table config objects.

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
        object_type (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_id (Union[Unset, list[int]]):
        object_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        shared (Union[Unset, bool]):
        table (Union[Unset, list[str]]):
        table_empty (Union[Unset, bool]):
        table_ic (Union[Unset, list[str]]):
        table_ie (Union[Unset, list[str]]):
        table_iew (Union[Unset, list[str]]):
        table_isw (Union[Unset, list[str]]):
        table_n (Union[Unset, list[str]]):
        table_nic (Union[Unset, list[str]]):
        table_nie (Union[Unset, list[str]]):
        table_niew (Union[Unset, list[str]]):
        table_nisw (Union[Unset, list[str]]):
        updated_by_request (Union[Unset, UUID]):
        usable (Union[Unset, bool]):
        user (Union[Unset, list[str]]):
        user_n (Union[Unset, list[str]]):
        user_id (Union[Unset, list[Union[None, int]]]):
        user_id_n (Union[Unset, list[Union[None, int]]]):
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
        PaginatedTableConfigList
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
            object_type=object_type,
            object_type_n=object_type_n,
            object_type_id=object_type_id,
            object_type_id_n=object_type_id_n,
            offset=offset,
            ordering=ordering,
            q=q,
            shared=shared,
            table=table,
            table_empty=table_empty,
            table_ic=table_ic,
            table_ie=table_ie,
            table_iew=table_iew,
            table_isw=table_isw,
            table_n=table_n,
            table_nic=table_nic,
            table_nie=table_nie,
            table_niew=table_niew,
            table_nisw=table_nisw,
            updated_by_request=updated_by_request,
            usable=usable,
            user=user,
            user_n=user_n,
            user_id=user_id,
            user_id_n=user_id_n,
            weight=weight,
            weight_empty=weight_empty,
            weight_gt=weight_gt,
            weight_gte=weight_gte,
            weight_lt=weight_lt,
            weight_lte=weight_lte,
            weight_n=weight_n,
        )
    ).parsed
