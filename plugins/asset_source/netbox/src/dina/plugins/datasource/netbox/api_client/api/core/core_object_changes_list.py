import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.core_object_changes_list_action import CoreObjectChangesListAction
from ...models.paginated_object_change_list import PaginatedObjectChangeList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    action: Union[Unset, CoreObjectChangesListAction] = UNSET,
    changed_object_id: Union[Unset, list[int]] = UNSET,
    changed_object_id_empty: Union[Unset, bool] = UNSET,
    changed_object_id_gt: Union[Unset, list[int]] = UNSET,
    changed_object_id_gte: Union[Unset, list[int]] = UNSET,
    changed_object_id_lt: Union[Unset, list[int]] = UNSET,
    changed_object_id_lte: Union[Unset, list[int]] = UNSET,
    changed_object_id_n: Union[Unset, list[int]] = UNSET,
    changed_object_type: Union[Unset, str] = UNSET,
    changed_object_type_n: Union[Unset, str] = UNSET,
    changed_object_type_id: Union[Unset, list[int]] = UNSET,
    changed_object_type_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    object_repr: Union[Unset, list[str]] = UNSET,
    object_repr_empty: Union[Unset, bool] = UNSET,
    object_repr_ic: Union[Unset, list[str]] = UNSET,
    object_repr_ie: Union[Unset, list[str]] = UNSET,
    object_repr_iew: Union[Unset, list[str]] = UNSET,
    object_repr_isw: Union[Unset, list[str]] = UNSET,
    object_repr_n: Union[Unset, list[str]] = UNSET,
    object_repr_nic: Union[Unset, list[str]] = UNSET,
    object_repr_nie: Union[Unset, list[str]] = UNSET,
    object_repr_niew: Union[Unset, list[str]] = UNSET,
    object_repr_nisw: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    related_object_id: Union[Unset, list[int]] = UNSET,
    related_object_id_empty: Union[Unset, bool] = UNSET,
    related_object_id_gt: Union[Unset, list[int]] = UNSET,
    related_object_id_gte: Union[Unset, list[int]] = UNSET,
    related_object_id_lt: Union[Unset, list[int]] = UNSET,
    related_object_id_lte: Union[Unset, list[int]] = UNSET,
    related_object_id_n: Union[Unset, list[int]] = UNSET,
    related_object_type: Union[Unset, int] = UNSET,
    related_object_type_n: Union[Unset, int] = UNSET,
    request_id: Union[Unset, UUID] = UNSET,
    time_after: Union[Unset, datetime.datetime] = UNSET,
    time_before: Union[Unset, datetime.datetime] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[Union[None, int]]] = UNSET,
    user_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    user_name: Union[Unset, list[str]] = UNSET,
    user_name_empty: Union[Unset, bool] = UNSET,
    user_name_ic: Union[Unset, list[str]] = UNSET,
    user_name_ie: Union[Unset, list[str]] = UNSET,
    user_name_iew: Union[Unset, list[str]] = UNSET,
    user_name_isw: Union[Unset, list[str]] = UNSET,
    user_name_n: Union[Unset, list[str]] = UNSET,
    user_name_nic: Union[Unset, list[str]] = UNSET,
    user_name_nie: Union[Unset, list[str]] = UNSET,
    user_name_niew: Union[Unset, list[str]] = UNSET,
    user_name_nisw: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_action: Union[Unset, str] = UNSET
    if not isinstance(action, Unset):
        json_action = action.value

    params["action"] = json_action

    json_changed_object_id: Union[Unset, list[int]] = UNSET
    if not isinstance(changed_object_id, Unset):
        json_changed_object_id = changed_object_id

    params["changed_object_id"] = json_changed_object_id

    params["changed_object_id__empty"] = changed_object_id_empty

    json_changed_object_id_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(changed_object_id_gt, Unset):
        json_changed_object_id_gt = changed_object_id_gt

    params["changed_object_id__gt"] = json_changed_object_id_gt

    json_changed_object_id_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(changed_object_id_gte, Unset):
        json_changed_object_id_gte = changed_object_id_gte

    params["changed_object_id__gte"] = json_changed_object_id_gte

    json_changed_object_id_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(changed_object_id_lt, Unset):
        json_changed_object_id_lt = changed_object_id_lt

    params["changed_object_id__lt"] = json_changed_object_id_lt

    json_changed_object_id_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(changed_object_id_lte, Unset):
        json_changed_object_id_lte = changed_object_id_lte

    params["changed_object_id__lte"] = json_changed_object_id_lte

    json_changed_object_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(changed_object_id_n, Unset):
        json_changed_object_id_n = changed_object_id_n

    params["changed_object_id__n"] = json_changed_object_id_n

    params["changed_object_type"] = changed_object_type

    params["changed_object_type__n"] = changed_object_type_n

    json_changed_object_type_id: Union[Unset, list[int]] = UNSET
    if not isinstance(changed_object_type_id, Unset):
        json_changed_object_type_id = changed_object_type_id

    params["changed_object_type_id"] = json_changed_object_type_id

    json_changed_object_type_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(changed_object_type_id_n, Unset):
        json_changed_object_type_id_n = changed_object_type_id_n

    params["changed_object_type_id__n"] = json_changed_object_type_id_n

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

    params["limit"] = limit

    json_object_repr: Union[Unset, list[str]] = UNSET
    if not isinstance(object_repr, Unset):
        json_object_repr = object_repr

    params["object_repr"] = json_object_repr

    params["object_repr__empty"] = object_repr_empty

    json_object_repr_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(object_repr_ic, Unset):
        json_object_repr_ic = object_repr_ic

    params["object_repr__ic"] = json_object_repr_ic

    json_object_repr_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(object_repr_ie, Unset):
        json_object_repr_ie = object_repr_ie

    params["object_repr__ie"] = json_object_repr_ie

    json_object_repr_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(object_repr_iew, Unset):
        json_object_repr_iew = object_repr_iew

    params["object_repr__iew"] = json_object_repr_iew

    json_object_repr_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(object_repr_isw, Unset):
        json_object_repr_isw = object_repr_isw

    params["object_repr__isw"] = json_object_repr_isw

    json_object_repr_n: Union[Unset, list[str]] = UNSET
    if not isinstance(object_repr_n, Unset):
        json_object_repr_n = object_repr_n

    params["object_repr__n"] = json_object_repr_n

    json_object_repr_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(object_repr_nic, Unset):
        json_object_repr_nic = object_repr_nic

    params["object_repr__nic"] = json_object_repr_nic

    json_object_repr_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(object_repr_nie, Unset):
        json_object_repr_nie = object_repr_nie

    params["object_repr__nie"] = json_object_repr_nie

    json_object_repr_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(object_repr_niew, Unset):
        json_object_repr_niew = object_repr_niew

    params["object_repr__niew"] = json_object_repr_niew

    json_object_repr_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(object_repr_nisw, Unset):
        json_object_repr_nisw = object_repr_nisw

    params["object_repr__nisw"] = json_object_repr_nisw

    params["offset"] = offset

    params["ordering"] = ordering

    params["q"] = q

    json_related_object_id: Union[Unset, list[int]] = UNSET
    if not isinstance(related_object_id, Unset):
        json_related_object_id = related_object_id

    params["related_object_id"] = json_related_object_id

    params["related_object_id__empty"] = related_object_id_empty

    json_related_object_id_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(related_object_id_gt, Unset):
        json_related_object_id_gt = related_object_id_gt

    params["related_object_id__gt"] = json_related_object_id_gt

    json_related_object_id_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(related_object_id_gte, Unset):
        json_related_object_id_gte = related_object_id_gte

    params["related_object_id__gte"] = json_related_object_id_gte

    json_related_object_id_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(related_object_id_lt, Unset):
        json_related_object_id_lt = related_object_id_lt

    params["related_object_id__lt"] = json_related_object_id_lt

    json_related_object_id_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(related_object_id_lte, Unset):
        json_related_object_id_lte = related_object_id_lte

    params["related_object_id__lte"] = json_related_object_id_lte

    json_related_object_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(related_object_id_n, Unset):
        json_related_object_id_n = related_object_id_n

    params["related_object_id__n"] = json_related_object_id_n

    params["related_object_type"] = related_object_type

    params["related_object_type__n"] = related_object_type_n

    json_request_id: Union[Unset, str] = UNSET
    if not isinstance(request_id, Unset):
        json_request_id = str(request_id)
    params["request_id"] = json_request_id

    json_time_after: Union[Unset, str] = UNSET
    if not isinstance(time_after, Unset):
        json_time_after = time_after.isoformat()
    params["time_after"] = json_time_after

    json_time_before: Union[Unset, str] = UNSET
    if not isinstance(time_before, Unset):
        json_time_before = time_before.isoformat()
    params["time_before"] = json_time_before

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

    json_user_name: Union[Unset, list[str]] = UNSET
    if not isinstance(user_name, Unset):
        json_user_name = user_name

    params["user_name"] = json_user_name

    params["user_name__empty"] = user_name_empty

    json_user_name_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(user_name_ic, Unset):
        json_user_name_ic = user_name_ic

    params["user_name__ic"] = json_user_name_ic

    json_user_name_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(user_name_ie, Unset):
        json_user_name_ie = user_name_ie

    params["user_name__ie"] = json_user_name_ie

    json_user_name_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(user_name_iew, Unset):
        json_user_name_iew = user_name_iew

    params["user_name__iew"] = json_user_name_iew

    json_user_name_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(user_name_isw, Unset):
        json_user_name_isw = user_name_isw

    params["user_name__isw"] = json_user_name_isw

    json_user_name_n: Union[Unset, list[str]] = UNSET
    if not isinstance(user_name_n, Unset):
        json_user_name_n = user_name_n

    params["user_name__n"] = json_user_name_n

    json_user_name_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(user_name_nic, Unset):
        json_user_name_nic = user_name_nic

    params["user_name__nic"] = json_user_name_nic

    json_user_name_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(user_name_nie, Unset):
        json_user_name_nie = user_name_nie

    params["user_name__nie"] = json_user_name_nie

    json_user_name_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(user_name_niew, Unset):
        json_user_name_niew = user_name_niew

    params["user_name__niew"] = json_user_name_niew

    json_user_name_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(user_name_nisw, Unset):
        json_user_name_nisw = user_name_nisw

    params["user_name__nisw"] = json_user_name_nisw

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/object-changes/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedObjectChangeList]:
    if response.status_code == 200:
        response_200 = PaginatedObjectChangeList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedObjectChangeList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    action: Union[Unset, CoreObjectChangesListAction] = UNSET,
    changed_object_id: Union[Unset, list[int]] = UNSET,
    changed_object_id_empty: Union[Unset, bool] = UNSET,
    changed_object_id_gt: Union[Unset, list[int]] = UNSET,
    changed_object_id_gte: Union[Unset, list[int]] = UNSET,
    changed_object_id_lt: Union[Unset, list[int]] = UNSET,
    changed_object_id_lte: Union[Unset, list[int]] = UNSET,
    changed_object_id_n: Union[Unset, list[int]] = UNSET,
    changed_object_type: Union[Unset, str] = UNSET,
    changed_object_type_n: Union[Unset, str] = UNSET,
    changed_object_type_id: Union[Unset, list[int]] = UNSET,
    changed_object_type_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    object_repr: Union[Unset, list[str]] = UNSET,
    object_repr_empty: Union[Unset, bool] = UNSET,
    object_repr_ic: Union[Unset, list[str]] = UNSET,
    object_repr_ie: Union[Unset, list[str]] = UNSET,
    object_repr_iew: Union[Unset, list[str]] = UNSET,
    object_repr_isw: Union[Unset, list[str]] = UNSET,
    object_repr_n: Union[Unset, list[str]] = UNSET,
    object_repr_nic: Union[Unset, list[str]] = UNSET,
    object_repr_nie: Union[Unset, list[str]] = UNSET,
    object_repr_niew: Union[Unset, list[str]] = UNSET,
    object_repr_nisw: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    related_object_id: Union[Unset, list[int]] = UNSET,
    related_object_id_empty: Union[Unset, bool] = UNSET,
    related_object_id_gt: Union[Unset, list[int]] = UNSET,
    related_object_id_gte: Union[Unset, list[int]] = UNSET,
    related_object_id_lt: Union[Unset, list[int]] = UNSET,
    related_object_id_lte: Union[Unset, list[int]] = UNSET,
    related_object_id_n: Union[Unset, list[int]] = UNSET,
    related_object_type: Union[Unset, int] = UNSET,
    related_object_type_n: Union[Unset, int] = UNSET,
    request_id: Union[Unset, UUID] = UNSET,
    time_after: Union[Unset, datetime.datetime] = UNSET,
    time_before: Union[Unset, datetime.datetime] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[Union[None, int]]] = UNSET,
    user_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    user_name: Union[Unset, list[str]] = UNSET,
    user_name_empty: Union[Unset, bool] = UNSET,
    user_name_ic: Union[Unset, list[str]] = UNSET,
    user_name_ie: Union[Unset, list[str]] = UNSET,
    user_name_iew: Union[Unset, list[str]] = UNSET,
    user_name_isw: Union[Unset, list[str]] = UNSET,
    user_name_n: Union[Unset, list[str]] = UNSET,
    user_name_nic: Union[Unset, list[str]] = UNSET,
    user_name_nie: Union[Unset, list[str]] = UNSET,
    user_name_niew: Union[Unset, list[str]] = UNSET,
    user_name_nisw: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedObjectChangeList]:
    """Retrieve a list of recent changes.

    Args:
        action (Union[Unset, CoreObjectChangesListAction]):
        changed_object_id (Union[Unset, list[int]]):
        changed_object_id_empty (Union[Unset, bool]):
        changed_object_id_gt (Union[Unset, list[int]]):
        changed_object_id_gte (Union[Unset, list[int]]):
        changed_object_id_lt (Union[Unset, list[int]]):
        changed_object_id_lte (Union[Unset, list[int]]):
        changed_object_id_n (Union[Unset, list[int]]):
        changed_object_type (Union[Unset, str]):
        changed_object_type_n (Union[Unset, str]):
        changed_object_type_id (Union[Unset, list[int]]):
        changed_object_type_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        limit (Union[Unset, int]):
        object_repr (Union[Unset, list[str]]):
        object_repr_empty (Union[Unset, bool]):
        object_repr_ic (Union[Unset, list[str]]):
        object_repr_ie (Union[Unset, list[str]]):
        object_repr_iew (Union[Unset, list[str]]):
        object_repr_isw (Union[Unset, list[str]]):
        object_repr_n (Union[Unset, list[str]]):
        object_repr_nic (Union[Unset, list[str]]):
        object_repr_nie (Union[Unset, list[str]]):
        object_repr_niew (Union[Unset, list[str]]):
        object_repr_nisw (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        related_object_id (Union[Unset, list[int]]):
        related_object_id_empty (Union[Unset, bool]):
        related_object_id_gt (Union[Unset, list[int]]):
        related_object_id_gte (Union[Unset, list[int]]):
        related_object_id_lt (Union[Unset, list[int]]):
        related_object_id_lte (Union[Unset, list[int]]):
        related_object_id_n (Union[Unset, list[int]]):
        related_object_type (Union[Unset, int]):
        related_object_type_n (Union[Unset, int]):
        request_id (Union[Unset, UUID]):
        time_after (Union[Unset, datetime.datetime]):
        time_before (Union[Unset, datetime.datetime]):
        user (Union[Unset, list[str]]):
        user_n (Union[Unset, list[str]]):
        user_id (Union[Unset, list[Union[None, int]]]):
        user_id_n (Union[Unset, list[Union[None, int]]]):
        user_name (Union[Unset, list[str]]):
        user_name_empty (Union[Unset, bool]):
        user_name_ic (Union[Unset, list[str]]):
        user_name_ie (Union[Unset, list[str]]):
        user_name_iew (Union[Unset, list[str]]):
        user_name_isw (Union[Unset, list[str]]):
        user_name_n (Union[Unset, list[str]]):
        user_name_nic (Union[Unset, list[str]]):
        user_name_nie (Union[Unset, list[str]]):
        user_name_niew (Union[Unset, list[str]]):
        user_name_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedObjectChangeList]
    """

    kwargs = _get_kwargs(
        action=action,
        changed_object_id=changed_object_id,
        changed_object_id_empty=changed_object_id_empty,
        changed_object_id_gt=changed_object_id_gt,
        changed_object_id_gte=changed_object_id_gte,
        changed_object_id_lt=changed_object_id_lt,
        changed_object_id_lte=changed_object_id_lte,
        changed_object_id_n=changed_object_id_n,
        changed_object_type=changed_object_type,
        changed_object_type_n=changed_object_type_n,
        changed_object_type_id=changed_object_type_id,
        changed_object_type_id_n=changed_object_type_id_n,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        limit=limit,
        object_repr=object_repr,
        object_repr_empty=object_repr_empty,
        object_repr_ic=object_repr_ic,
        object_repr_ie=object_repr_ie,
        object_repr_iew=object_repr_iew,
        object_repr_isw=object_repr_isw,
        object_repr_n=object_repr_n,
        object_repr_nic=object_repr_nic,
        object_repr_nie=object_repr_nie,
        object_repr_niew=object_repr_niew,
        object_repr_nisw=object_repr_nisw,
        offset=offset,
        ordering=ordering,
        q=q,
        related_object_id=related_object_id,
        related_object_id_empty=related_object_id_empty,
        related_object_id_gt=related_object_id_gt,
        related_object_id_gte=related_object_id_gte,
        related_object_id_lt=related_object_id_lt,
        related_object_id_lte=related_object_id_lte,
        related_object_id_n=related_object_id_n,
        related_object_type=related_object_type,
        related_object_type_n=related_object_type_n,
        request_id=request_id,
        time_after=time_after,
        time_before=time_before,
        user=user,
        user_n=user_n,
        user_id=user_id,
        user_id_n=user_id_n,
        user_name=user_name,
        user_name_empty=user_name_empty,
        user_name_ic=user_name_ic,
        user_name_ie=user_name_ie,
        user_name_iew=user_name_iew,
        user_name_isw=user_name_isw,
        user_name_n=user_name_n,
        user_name_nic=user_name_nic,
        user_name_nie=user_name_nie,
        user_name_niew=user_name_niew,
        user_name_nisw=user_name_nisw,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    action: Union[Unset, CoreObjectChangesListAction] = UNSET,
    changed_object_id: Union[Unset, list[int]] = UNSET,
    changed_object_id_empty: Union[Unset, bool] = UNSET,
    changed_object_id_gt: Union[Unset, list[int]] = UNSET,
    changed_object_id_gte: Union[Unset, list[int]] = UNSET,
    changed_object_id_lt: Union[Unset, list[int]] = UNSET,
    changed_object_id_lte: Union[Unset, list[int]] = UNSET,
    changed_object_id_n: Union[Unset, list[int]] = UNSET,
    changed_object_type: Union[Unset, str] = UNSET,
    changed_object_type_n: Union[Unset, str] = UNSET,
    changed_object_type_id: Union[Unset, list[int]] = UNSET,
    changed_object_type_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    object_repr: Union[Unset, list[str]] = UNSET,
    object_repr_empty: Union[Unset, bool] = UNSET,
    object_repr_ic: Union[Unset, list[str]] = UNSET,
    object_repr_ie: Union[Unset, list[str]] = UNSET,
    object_repr_iew: Union[Unset, list[str]] = UNSET,
    object_repr_isw: Union[Unset, list[str]] = UNSET,
    object_repr_n: Union[Unset, list[str]] = UNSET,
    object_repr_nic: Union[Unset, list[str]] = UNSET,
    object_repr_nie: Union[Unset, list[str]] = UNSET,
    object_repr_niew: Union[Unset, list[str]] = UNSET,
    object_repr_nisw: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    related_object_id: Union[Unset, list[int]] = UNSET,
    related_object_id_empty: Union[Unset, bool] = UNSET,
    related_object_id_gt: Union[Unset, list[int]] = UNSET,
    related_object_id_gte: Union[Unset, list[int]] = UNSET,
    related_object_id_lt: Union[Unset, list[int]] = UNSET,
    related_object_id_lte: Union[Unset, list[int]] = UNSET,
    related_object_id_n: Union[Unset, list[int]] = UNSET,
    related_object_type: Union[Unset, int] = UNSET,
    related_object_type_n: Union[Unset, int] = UNSET,
    request_id: Union[Unset, UUID] = UNSET,
    time_after: Union[Unset, datetime.datetime] = UNSET,
    time_before: Union[Unset, datetime.datetime] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[Union[None, int]]] = UNSET,
    user_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    user_name: Union[Unset, list[str]] = UNSET,
    user_name_empty: Union[Unset, bool] = UNSET,
    user_name_ic: Union[Unset, list[str]] = UNSET,
    user_name_ie: Union[Unset, list[str]] = UNSET,
    user_name_iew: Union[Unset, list[str]] = UNSET,
    user_name_isw: Union[Unset, list[str]] = UNSET,
    user_name_n: Union[Unset, list[str]] = UNSET,
    user_name_nic: Union[Unset, list[str]] = UNSET,
    user_name_nie: Union[Unset, list[str]] = UNSET,
    user_name_niew: Union[Unset, list[str]] = UNSET,
    user_name_nisw: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedObjectChangeList]:
    """Retrieve a list of recent changes.

    Args:
        action (Union[Unset, CoreObjectChangesListAction]):
        changed_object_id (Union[Unset, list[int]]):
        changed_object_id_empty (Union[Unset, bool]):
        changed_object_id_gt (Union[Unset, list[int]]):
        changed_object_id_gte (Union[Unset, list[int]]):
        changed_object_id_lt (Union[Unset, list[int]]):
        changed_object_id_lte (Union[Unset, list[int]]):
        changed_object_id_n (Union[Unset, list[int]]):
        changed_object_type (Union[Unset, str]):
        changed_object_type_n (Union[Unset, str]):
        changed_object_type_id (Union[Unset, list[int]]):
        changed_object_type_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        limit (Union[Unset, int]):
        object_repr (Union[Unset, list[str]]):
        object_repr_empty (Union[Unset, bool]):
        object_repr_ic (Union[Unset, list[str]]):
        object_repr_ie (Union[Unset, list[str]]):
        object_repr_iew (Union[Unset, list[str]]):
        object_repr_isw (Union[Unset, list[str]]):
        object_repr_n (Union[Unset, list[str]]):
        object_repr_nic (Union[Unset, list[str]]):
        object_repr_nie (Union[Unset, list[str]]):
        object_repr_niew (Union[Unset, list[str]]):
        object_repr_nisw (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        related_object_id (Union[Unset, list[int]]):
        related_object_id_empty (Union[Unset, bool]):
        related_object_id_gt (Union[Unset, list[int]]):
        related_object_id_gte (Union[Unset, list[int]]):
        related_object_id_lt (Union[Unset, list[int]]):
        related_object_id_lte (Union[Unset, list[int]]):
        related_object_id_n (Union[Unset, list[int]]):
        related_object_type (Union[Unset, int]):
        related_object_type_n (Union[Unset, int]):
        request_id (Union[Unset, UUID]):
        time_after (Union[Unset, datetime.datetime]):
        time_before (Union[Unset, datetime.datetime]):
        user (Union[Unset, list[str]]):
        user_n (Union[Unset, list[str]]):
        user_id (Union[Unset, list[Union[None, int]]]):
        user_id_n (Union[Unset, list[Union[None, int]]]):
        user_name (Union[Unset, list[str]]):
        user_name_empty (Union[Unset, bool]):
        user_name_ic (Union[Unset, list[str]]):
        user_name_ie (Union[Unset, list[str]]):
        user_name_iew (Union[Unset, list[str]]):
        user_name_isw (Union[Unset, list[str]]):
        user_name_n (Union[Unset, list[str]]):
        user_name_nic (Union[Unset, list[str]]):
        user_name_nie (Union[Unset, list[str]]):
        user_name_niew (Union[Unset, list[str]]):
        user_name_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedObjectChangeList
    """

    return sync_detailed(
        client=client,
        action=action,
        changed_object_id=changed_object_id,
        changed_object_id_empty=changed_object_id_empty,
        changed_object_id_gt=changed_object_id_gt,
        changed_object_id_gte=changed_object_id_gte,
        changed_object_id_lt=changed_object_id_lt,
        changed_object_id_lte=changed_object_id_lte,
        changed_object_id_n=changed_object_id_n,
        changed_object_type=changed_object_type,
        changed_object_type_n=changed_object_type_n,
        changed_object_type_id=changed_object_type_id,
        changed_object_type_id_n=changed_object_type_id_n,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        limit=limit,
        object_repr=object_repr,
        object_repr_empty=object_repr_empty,
        object_repr_ic=object_repr_ic,
        object_repr_ie=object_repr_ie,
        object_repr_iew=object_repr_iew,
        object_repr_isw=object_repr_isw,
        object_repr_n=object_repr_n,
        object_repr_nic=object_repr_nic,
        object_repr_nie=object_repr_nie,
        object_repr_niew=object_repr_niew,
        object_repr_nisw=object_repr_nisw,
        offset=offset,
        ordering=ordering,
        q=q,
        related_object_id=related_object_id,
        related_object_id_empty=related_object_id_empty,
        related_object_id_gt=related_object_id_gt,
        related_object_id_gte=related_object_id_gte,
        related_object_id_lt=related_object_id_lt,
        related_object_id_lte=related_object_id_lte,
        related_object_id_n=related_object_id_n,
        related_object_type=related_object_type,
        related_object_type_n=related_object_type_n,
        request_id=request_id,
        time_after=time_after,
        time_before=time_before,
        user=user,
        user_n=user_n,
        user_id=user_id,
        user_id_n=user_id_n,
        user_name=user_name,
        user_name_empty=user_name_empty,
        user_name_ic=user_name_ic,
        user_name_ie=user_name_ie,
        user_name_iew=user_name_iew,
        user_name_isw=user_name_isw,
        user_name_n=user_name_n,
        user_name_nic=user_name_nic,
        user_name_nie=user_name_nie,
        user_name_niew=user_name_niew,
        user_name_nisw=user_name_nisw,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    action: Union[Unset, CoreObjectChangesListAction] = UNSET,
    changed_object_id: Union[Unset, list[int]] = UNSET,
    changed_object_id_empty: Union[Unset, bool] = UNSET,
    changed_object_id_gt: Union[Unset, list[int]] = UNSET,
    changed_object_id_gte: Union[Unset, list[int]] = UNSET,
    changed_object_id_lt: Union[Unset, list[int]] = UNSET,
    changed_object_id_lte: Union[Unset, list[int]] = UNSET,
    changed_object_id_n: Union[Unset, list[int]] = UNSET,
    changed_object_type: Union[Unset, str] = UNSET,
    changed_object_type_n: Union[Unset, str] = UNSET,
    changed_object_type_id: Union[Unset, list[int]] = UNSET,
    changed_object_type_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    object_repr: Union[Unset, list[str]] = UNSET,
    object_repr_empty: Union[Unset, bool] = UNSET,
    object_repr_ic: Union[Unset, list[str]] = UNSET,
    object_repr_ie: Union[Unset, list[str]] = UNSET,
    object_repr_iew: Union[Unset, list[str]] = UNSET,
    object_repr_isw: Union[Unset, list[str]] = UNSET,
    object_repr_n: Union[Unset, list[str]] = UNSET,
    object_repr_nic: Union[Unset, list[str]] = UNSET,
    object_repr_nie: Union[Unset, list[str]] = UNSET,
    object_repr_niew: Union[Unset, list[str]] = UNSET,
    object_repr_nisw: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    related_object_id: Union[Unset, list[int]] = UNSET,
    related_object_id_empty: Union[Unset, bool] = UNSET,
    related_object_id_gt: Union[Unset, list[int]] = UNSET,
    related_object_id_gte: Union[Unset, list[int]] = UNSET,
    related_object_id_lt: Union[Unset, list[int]] = UNSET,
    related_object_id_lte: Union[Unset, list[int]] = UNSET,
    related_object_id_n: Union[Unset, list[int]] = UNSET,
    related_object_type: Union[Unset, int] = UNSET,
    related_object_type_n: Union[Unset, int] = UNSET,
    request_id: Union[Unset, UUID] = UNSET,
    time_after: Union[Unset, datetime.datetime] = UNSET,
    time_before: Union[Unset, datetime.datetime] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[Union[None, int]]] = UNSET,
    user_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    user_name: Union[Unset, list[str]] = UNSET,
    user_name_empty: Union[Unset, bool] = UNSET,
    user_name_ic: Union[Unset, list[str]] = UNSET,
    user_name_ie: Union[Unset, list[str]] = UNSET,
    user_name_iew: Union[Unset, list[str]] = UNSET,
    user_name_isw: Union[Unset, list[str]] = UNSET,
    user_name_n: Union[Unset, list[str]] = UNSET,
    user_name_nic: Union[Unset, list[str]] = UNSET,
    user_name_nie: Union[Unset, list[str]] = UNSET,
    user_name_niew: Union[Unset, list[str]] = UNSET,
    user_name_nisw: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedObjectChangeList]:
    """Retrieve a list of recent changes.

    Args:
        action (Union[Unset, CoreObjectChangesListAction]):
        changed_object_id (Union[Unset, list[int]]):
        changed_object_id_empty (Union[Unset, bool]):
        changed_object_id_gt (Union[Unset, list[int]]):
        changed_object_id_gte (Union[Unset, list[int]]):
        changed_object_id_lt (Union[Unset, list[int]]):
        changed_object_id_lte (Union[Unset, list[int]]):
        changed_object_id_n (Union[Unset, list[int]]):
        changed_object_type (Union[Unset, str]):
        changed_object_type_n (Union[Unset, str]):
        changed_object_type_id (Union[Unset, list[int]]):
        changed_object_type_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        limit (Union[Unset, int]):
        object_repr (Union[Unset, list[str]]):
        object_repr_empty (Union[Unset, bool]):
        object_repr_ic (Union[Unset, list[str]]):
        object_repr_ie (Union[Unset, list[str]]):
        object_repr_iew (Union[Unset, list[str]]):
        object_repr_isw (Union[Unset, list[str]]):
        object_repr_n (Union[Unset, list[str]]):
        object_repr_nic (Union[Unset, list[str]]):
        object_repr_nie (Union[Unset, list[str]]):
        object_repr_niew (Union[Unset, list[str]]):
        object_repr_nisw (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        related_object_id (Union[Unset, list[int]]):
        related_object_id_empty (Union[Unset, bool]):
        related_object_id_gt (Union[Unset, list[int]]):
        related_object_id_gte (Union[Unset, list[int]]):
        related_object_id_lt (Union[Unset, list[int]]):
        related_object_id_lte (Union[Unset, list[int]]):
        related_object_id_n (Union[Unset, list[int]]):
        related_object_type (Union[Unset, int]):
        related_object_type_n (Union[Unset, int]):
        request_id (Union[Unset, UUID]):
        time_after (Union[Unset, datetime.datetime]):
        time_before (Union[Unset, datetime.datetime]):
        user (Union[Unset, list[str]]):
        user_n (Union[Unset, list[str]]):
        user_id (Union[Unset, list[Union[None, int]]]):
        user_id_n (Union[Unset, list[Union[None, int]]]):
        user_name (Union[Unset, list[str]]):
        user_name_empty (Union[Unset, bool]):
        user_name_ic (Union[Unset, list[str]]):
        user_name_ie (Union[Unset, list[str]]):
        user_name_iew (Union[Unset, list[str]]):
        user_name_isw (Union[Unset, list[str]]):
        user_name_n (Union[Unset, list[str]]):
        user_name_nic (Union[Unset, list[str]]):
        user_name_nie (Union[Unset, list[str]]):
        user_name_niew (Union[Unset, list[str]]):
        user_name_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedObjectChangeList]
    """

    kwargs = _get_kwargs(
        action=action,
        changed_object_id=changed_object_id,
        changed_object_id_empty=changed_object_id_empty,
        changed_object_id_gt=changed_object_id_gt,
        changed_object_id_gte=changed_object_id_gte,
        changed_object_id_lt=changed_object_id_lt,
        changed_object_id_lte=changed_object_id_lte,
        changed_object_id_n=changed_object_id_n,
        changed_object_type=changed_object_type,
        changed_object_type_n=changed_object_type_n,
        changed_object_type_id=changed_object_type_id,
        changed_object_type_id_n=changed_object_type_id_n,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        limit=limit,
        object_repr=object_repr,
        object_repr_empty=object_repr_empty,
        object_repr_ic=object_repr_ic,
        object_repr_ie=object_repr_ie,
        object_repr_iew=object_repr_iew,
        object_repr_isw=object_repr_isw,
        object_repr_n=object_repr_n,
        object_repr_nic=object_repr_nic,
        object_repr_nie=object_repr_nie,
        object_repr_niew=object_repr_niew,
        object_repr_nisw=object_repr_nisw,
        offset=offset,
        ordering=ordering,
        q=q,
        related_object_id=related_object_id,
        related_object_id_empty=related_object_id_empty,
        related_object_id_gt=related_object_id_gt,
        related_object_id_gte=related_object_id_gte,
        related_object_id_lt=related_object_id_lt,
        related_object_id_lte=related_object_id_lte,
        related_object_id_n=related_object_id_n,
        related_object_type=related_object_type,
        related_object_type_n=related_object_type_n,
        request_id=request_id,
        time_after=time_after,
        time_before=time_before,
        user=user,
        user_n=user_n,
        user_id=user_id,
        user_id_n=user_id_n,
        user_name=user_name,
        user_name_empty=user_name_empty,
        user_name_ic=user_name_ic,
        user_name_ie=user_name_ie,
        user_name_iew=user_name_iew,
        user_name_isw=user_name_isw,
        user_name_n=user_name_n,
        user_name_nic=user_name_nic,
        user_name_nie=user_name_nie,
        user_name_niew=user_name_niew,
        user_name_nisw=user_name_nisw,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    action: Union[Unset, CoreObjectChangesListAction] = UNSET,
    changed_object_id: Union[Unset, list[int]] = UNSET,
    changed_object_id_empty: Union[Unset, bool] = UNSET,
    changed_object_id_gt: Union[Unset, list[int]] = UNSET,
    changed_object_id_gte: Union[Unset, list[int]] = UNSET,
    changed_object_id_lt: Union[Unset, list[int]] = UNSET,
    changed_object_id_lte: Union[Unset, list[int]] = UNSET,
    changed_object_id_n: Union[Unset, list[int]] = UNSET,
    changed_object_type: Union[Unset, str] = UNSET,
    changed_object_type_n: Union[Unset, str] = UNSET,
    changed_object_type_id: Union[Unset, list[int]] = UNSET,
    changed_object_type_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    object_repr: Union[Unset, list[str]] = UNSET,
    object_repr_empty: Union[Unset, bool] = UNSET,
    object_repr_ic: Union[Unset, list[str]] = UNSET,
    object_repr_ie: Union[Unset, list[str]] = UNSET,
    object_repr_iew: Union[Unset, list[str]] = UNSET,
    object_repr_isw: Union[Unset, list[str]] = UNSET,
    object_repr_n: Union[Unset, list[str]] = UNSET,
    object_repr_nic: Union[Unset, list[str]] = UNSET,
    object_repr_nie: Union[Unset, list[str]] = UNSET,
    object_repr_niew: Union[Unset, list[str]] = UNSET,
    object_repr_nisw: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    related_object_id: Union[Unset, list[int]] = UNSET,
    related_object_id_empty: Union[Unset, bool] = UNSET,
    related_object_id_gt: Union[Unset, list[int]] = UNSET,
    related_object_id_gte: Union[Unset, list[int]] = UNSET,
    related_object_id_lt: Union[Unset, list[int]] = UNSET,
    related_object_id_lte: Union[Unset, list[int]] = UNSET,
    related_object_id_n: Union[Unset, list[int]] = UNSET,
    related_object_type: Union[Unset, int] = UNSET,
    related_object_type_n: Union[Unset, int] = UNSET,
    request_id: Union[Unset, UUID] = UNSET,
    time_after: Union[Unset, datetime.datetime] = UNSET,
    time_before: Union[Unset, datetime.datetime] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[Union[None, int]]] = UNSET,
    user_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    user_name: Union[Unset, list[str]] = UNSET,
    user_name_empty: Union[Unset, bool] = UNSET,
    user_name_ic: Union[Unset, list[str]] = UNSET,
    user_name_ie: Union[Unset, list[str]] = UNSET,
    user_name_iew: Union[Unset, list[str]] = UNSET,
    user_name_isw: Union[Unset, list[str]] = UNSET,
    user_name_n: Union[Unset, list[str]] = UNSET,
    user_name_nic: Union[Unset, list[str]] = UNSET,
    user_name_nie: Union[Unset, list[str]] = UNSET,
    user_name_niew: Union[Unset, list[str]] = UNSET,
    user_name_nisw: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedObjectChangeList]:
    """Retrieve a list of recent changes.

    Args:
        action (Union[Unset, CoreObjectChangesListAction]):
        changed_object_id (Union[Unset, list[int]]):
        changed_object_id_empty (Union[Unset, bool]):
        changed_object_id_gt (Union[Unset, list[int]]):
        changed_object_id_gte (Union[Unset, list[int]]):
        changed_object_id_lt (Union[Unset, list[int]]):
        changed_object_id_lte (Union[Unset, list[int]]):
        changed_object_id_n (Union[Unset, list[int]]):
        changed_object_type (Union[Unset, str]):
        changed_object_type_n (Union[Unset, str]):
        changed_object_type_id (Union[Unset, list[int]]):
        changed_object_type_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        limit (Union[Unset, int]):
        object_repr (Union[Unset, list[str]]):
        object_repr_empty (Union[Unset, bool]):
        object_repr_ic (Union[Unset, list[str]]):
        object_repr_ie (Union[Unset, list[str]]):
        object_repr_iew (Union[Unset, list[str]]):
        object_repr_isw (Union[Unset, list[str]]):
        object_repr_n (Union[Unset, list[str]]):
        object_repr_nic (Union[Unset, list[str]]):
        object_repr_nie (Union[Unset, list[str]]):
        object_repr_niew (Union[Unset, list[str]]):
        object_repr_nisw (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        related_object_id (Union[Unset, list[int]]):
        related_object_id_empty (Union[Unset, bool]):
        related_object_id_gt (Union[Unset, list[int]]):
        related_object_id_gte (Union[Unset, list[int]]):
        related_object_id_lt (Union[Unset, list[int]]):
        related_object_id_lte (Union[Unset, list[int]]):
        related_object_id_n (Union[Unset, list[int]]):
        related_object_type (Union[Unset, int]):
        related_object_type_n (Union[Unset, int]):
        request_id (Union[Unset, UUID]):
        time_after (Union[Unset, datetime.datetime]):
        time_before (Union[Unset, datetime.datetime]):
        user (Union[Unset, list[str]]):
        user_n (Union[Unset, list[str]]):
        user_id (Union[Unset, list[Union[None, int]]]):
        user_id_n (Union[Unset, list[Union[None, int]]]):
        user_name (Union[Unset, list[str]]):
        user_name_empty (Union[Unset, bool]):
        user_name_ic (Union[Unset, list[str]]):
        user_name_ie (Union[Unset, list[str]]):
        user_name_iew (Union[Unset, list[str]]):
        user_name_isw (Union[Unset, list[str]]):
        user_name_n (Union[Unset, list[str]]):
        user_name_nic (Union[Unset, list[str]]):
        user_name_nie (Union[Unset, list[str]]):
        user_name_niew (Union[Unset, list[str]]):
        user_name_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedObjectChangeList
    """

    return (
        await asyncio_detailed(
            client=client,
            action=action,
            changed_object_id=changed_object_id,
            changed_object_id_empty=changed_object_id_empty,
            changed_object_id_gt=changed_object_id_gt,
            changed_object_id_gte=changed_object_id_gte,
            changed_object_id_lt=changed_object_id_lt,
            changed_object_id_lte=changed_object_id_lte,
            changed_object_id_n=changed_object_id_n,
            changed_object_type=changed_object_type,
            changed_object_type_n=changed_object_type_n,
            changed_object_type_id=changed_object_type_id,
            changed_object_type_id_n=changed_object_type_id_n,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            limit=limit,
            object_repr=object_repr,
            object_repr_empty=object_repr_empty,
            object_repr_ic=object_repr_ic,
            object_repr_ie=object_repr_ie,
            object_repr_iew=object_repr_iew,
            object_repr_isw=object_repr_isw,
            object_repr_n=object_repr_n,
            object_repr_nic=object_repr_nic,
            object_repr_nie=object_repr_nie,
            object_repr_niew=object_repr_niew,
            object_repr_nisw=object_repr_nisw,
            offset=offset,
            ordering=ordering,
            q=q,
            related_object_id=related_object_id,
            related_object_id_empty=related_object_id_empty,
            related_object_id_gt=related_object_id_gt,
            related_object_id_gte=related_object_id_gte,
            related_object_id_lt=related_object_id_lt,
            related_object_id_lte=related_object_id_lte,
            related_object_id_n=related_object_id_n,
            related_object_type=related_object_type,
            related_object_type_n=related_object_type_n,
            request_id=request_id,
            time_after=time_after,
            time_before=time_before,
            user=user,
            user_n=user_n,
            user_id=user_id,
            user_id_n=user_id_n,
            user_name=user_name,
            user_name_empty=user_name_empty,
            user_name_ic=user_name_ic,
            user_name_ie=user_name_ie,
            user_name_iew=user_name_iew,
            user_name_isw=user_name_isw,
            user_name_n=user_name_n,
            user_name_nic=user_name_nic,
            user_name_nie=user_name_nie,
            user_name_niew=user_name_niew,
            user_name_nisw=user_name_nisw,
        )
    ).parsed
