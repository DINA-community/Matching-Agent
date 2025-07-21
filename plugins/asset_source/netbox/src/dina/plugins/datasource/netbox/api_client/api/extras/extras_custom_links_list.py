import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.extras_custom_links_list_button_class import (
    ExtrasCustomLinksListButtonClass,
)
from ...models.paginated_custom_link_list import PaginatedCustomLinkList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    button_class: Union[Unset, ExtrasCustomLinksListButtonClass] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    group_name: Union[Unset, list[str]] = UNSET,
    group_name_empty: Union[Unset, bool] = UNSET,
    group_name_ic: Union[Unset, list[str]] = UNSET,
    group_name_ie: Union[Unset, list[str]] = UNSET,
    group_name_iew: Union[Unset, list[str]] = UNSET,
    group_name_isw: Union[Unset, list[str]] = UNSET,
    group_name_n: Union[Unset, list[str]] = UNSET,
    group_name_nic: Union[Unset, list[str]] = UNSET,
    group_name_nie: Union[Unset, list[str]] = UNSET,
    group_name_niew: Union[Unset, list[str]] = UNSET,
    group_name_nisw: Union[Unset, list[str]] = UNSET,
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
    link_text: Union[Unset, str] = UNSET,
    link_text_ic: Union[Unset, str] = UNSET,
    link_text_ie: Union[Unset, str] = UNSET,
    link_text_iew: Union[Unset, str] = UNSET,
    link_text_isw: Union[Unset, str] = UNSET,
    link_text_n: Union[Unset, str] = UNSET,
    link_text_nic: Union[Unset, str] = UNSET,
    link_text_nie: Union[Unset, str] = UNSET,
    link_text_niew: Union[Unset, str] = UNSET,
    link_text_nisw: Union[Unset, str] = UNSET,
    link_url: Union[Unset, str] = UNSET,
    link_url_ic: Union[Unset, str] = UNSET,
    link_url_ie: Union[Unset, str] = UNSET,
    link_url_iew: Union[Unset, str] = UNSET,
    link_url_isw: Union[Unset, str] = UNSET,
    link_url_n: Union[Unset, str] = UNSET,
    link_url_nic: Union[Unset, str] = UNSET,
    link_url_nie: Union[Unset, str] = UNSET,
    link_url_niew: Union[Unset, str] = UNSET,
    link_url_nisw: Union[Unset, str] = UNSET,
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
    new_window: Union[Unset, bool] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    object_type_ic: Union[Unset, str] = UNSET,
    object_type_ie: Union[Unset, str] = UNSET,
    object_type_iew: Union[Unset, str] = UNSET,
    object_type_isw: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_nic: Union[Unset, str] = UNSET,
    object_type_nie: Union[Unset, str] = UNSET,
    object_type_niew: Union[Unset, str] = UNSET,
    object_type_nisw: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
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

    json_button_class: Union[Unset, str] = UNSET
    if not isinstance(button_class, Unset):
        json_button_class = button_class.value

    params["button_class"] = json_button_class

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

    params["enabled"] = enabled

    json_group_name: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name, Unset):
        json_group_name = group_name

    params["group_name"] = json_group_name

    params["group_name__empty"] = group_name_empty

    json_group_name_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name_ic, Unset):
        json_group_name_ic = group_name_ic

    params["group_name__ic"] = json_group_name_ic

    json_group_name_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name_ie, Unset):
        json_group_name_ie = group_name_ie

    params["group_name__ie"] = json_group_name_ie

    json_group_name_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name_iew, Unset):
        json_group_name_iew = group_name_iew

    params["group_name__iew"] = json_group_name_iew

    json_group_name_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name_isw, Unset):
        json_group_name_isw = group_name_isw

    params["group_name__isw"] = json_group_name_isw

    json_group_name_n: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name_n, Unset):
        json_group_name_n = group_name_n

    params["group_name__n"] = json_group_name_n

    json_group_name_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name_nic, Unset):
        json_group_name_nic = group_name_nic

    params["group_name__nic"] = json_group_name_nic

    json_group_name_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name_nie, Unset):
        json_group_name_nie = group_name_nie

    params["group_name__nie"] = json_group_name_nie

    json_group_name_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name_niew, Unset):
        json_group_name_niew = group_name_niew

    params["group_name__niew"] = json_group_name_niew

    json_group_name_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name_nisw, Unset):
        json_group_name_nisw = group_name_nisw

    params["group_name__nisw"] = json_group_name_nisw

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

    params["link_text"] = link_text

    params["link_text__ic"] = link_text_ic

    params["link_text__ie"] = link_text_ie

    params["link_text__iew"] = link_text_iew

    params["link_text__isw"] = link_text_isw

    params["link_text__n"] = link_text_n

    params["link_text__nic"] = link_text_nic

    params["link_text__nie"] = link_text_nie

    params["link_text__niew"] = link_text_niew

    params["link_text__nisw"] = link_text_nisw

    params["link_url"] = link_url

    params["link_url__ic"] = link_url_ic

    params["link_url__ie"] = link_url_ie

    params["link_url__iew"] = link_url_iew

    params["link_url__isw"] = link_url_isw

    params["link_url__n"] = link_url_n

    params["link_url__nic"] = link_url_nic

    params["link_url__nie"] = link_url_nie

    params["link_url__niew"] = link_url_niew

    params["link_url__nisw"] = link_url_nisw

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

    params["new_window"] = new_window

    params["object_type"] = object_type

    params["object_type__ic"] = object_type_ic

    params["object_type__ie"] = object_type_ie

    params["object_type__iew"] = object_type_iew

    params["object_type__isw"] = object_type_isw

    params["object_type__n"] = object_type_n

    params["object_type__nic"] = object_type_nic

    params["object_type__nie"] = object_type_nie

    params["object_type__niew"] = object_type_niew

    params["object_type__nisw"] = object_type_nisw

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
        "url": "/api/extras/custom-links/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedCustomLinkList]:
    if response.status_code == 200:
        response_200 = PaginatedCustomLinkList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedCustomLinkList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    button_class: Union[Unset, ExtrasCustomLinksListButtonClass] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    group_name: Union[Unset, list[str]] = UNSET,
    group_name_empty: Union[Unset, bool] = UNSET,
    group_name_ic: Union[Unset, list[str]] = UNSET,
    group_name_ie: Union[Unset, list[str]] = UNSET,
    group_name_iew: Union[Unset, list[str]] = UNSET,
    group_name_isw: Union[Unset, list[str]] = UNSET,
    group_name_n: Union[Unset, list[str]] = UNSET,
    group_name_nic: Union[Unset, list[str]] = UNSET,
    group_name_nie: Union[Unset, list[str]] = UNSET,
    group_name_niew: Union[Unset, list[str]] = UNSET,
    group_name_nisw: Union[Unset, list[str]] = UNSET,
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
    link_text: Union[Unset, str] = UNSET,
    link_text_ic: Union[Unset, str] = UNSET,
    link_text_ie: Union[Unset, str] = UNSET,
    link_text_iew: Union[Unset, str] = UNSET,
    link_text_isw: Union[Unset, str] = UNSET,
    link_text_n: Union[Unset, str] = UNSET,
    link_text_nic: Union[Unset, str] = UNSET,
    link_text_nie: Union[Unset, str] = UNSET,
    link_text_niew: Union[Unset, str] = UNSET,
    link_text_nisw: Union[Unset, str] = UNSET,
    link_url: Union[Unset, str] = UNSET,
    link_url_ic: Union[Unset, str] = UNSET,
    link_url_ie: Union[Unset, str] = UNSET,
    link_url_iew: Union[Unset, str] = UNSET,
    link_url_isw: Union[Unset, str] = UNSET,
    link_url_n: Union[Unset, str] = UNSET,
    link_url_nic: Union[Unset, str] = UNSET,
    link_url_nie: Union[Unset, str] = UNSET,
    link_url_niew: Union[Unset, str] = UNSET,
    link_url_nisw: Union[Unset, str] = UNSET,
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
    new_window: Union[Unset, bool] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    object_type_ic: Union[Unset, str] = UNSET,
    object_type_ie: Union[Unset, str] = UNSET,
    object_type_iew: Union[Unset, str] = UNSET,
    object_type_isw: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_nic: Union[Unset, str] = UNSET,
    object_type_nie: Union[Unset, str] = UNSET,
    object_type_niew: Union[Unset, str] = UNSET,
    object_type_nisw: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    weight: Union[Unset, list[int]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[int]] = UNSET,
    weight_gte: Union[Unset, list[int]] = UNSET,
    weight_lt: Union[Unset, list[int]] = UNSET,
    weight_lte: Union[Unset, list[int]] = UNSET,
    weight_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedCustomLinkList]:
    """Get a list of custom link objects.

    Args:
        button_class (Union[Unset, ExtrasCustomLinksListButtonClass]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        enabled (Union[Unset, bool]):
        group_name (Union[Unset, list[str]]):
        group_name_empty (Union[Unset, bool]):
        group_name_ic (Union[Unset, list[str]]):
        group_name_ie (Union[Unset, list[str]]):
        group_name_iew (Union[Unset, list[str]]):
        group_name_isw (Union[Unset, list[str]]):
        group_name_n (Union[Unset, list[str]]):
        group_name_nic (Union[Unset, list[str]]):
        group_name_nie (Union[Unset, list[str]]):
        group_name_niew (Union[Unset, list[str]]):
        group_name_nisw (Union[Unset, list[str]]):
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
        link_text (Union[Unset, str]):
        link_text_ic (Union[Unset, str]):
        link_text_ie (Union[Unset, str]):
        link_text_iew (Union[Unset, str]):
        link_text_isw (Union[Unset, str]):
        link_text_n (Union[Unset, str]):
        link_text_nic (Union[Unset, str]):
        link_text_nie (Union[Unset, str]):
        link_text_niew (Union[Unset, str]):
        link_text_nisw (Union[Unset, str]):
        link_url (Union[Unset, str]):
        link_url_ic (Union[Unset, str]):
        link_url_ie (Union[Unset, str]):
        link_url_iew (Union[Unset, str]):
        link_url_isw (Union[Unset, str]):
        link_url_n (Union[Unset, str]):
        link_url_nic (Union[Unset, str]):
        link_url_nie (Union[Unset, str]):
        link_url_niew (Union[Unset, str]):
        link_url_nisw (Union[Unset, str]):
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
        new_window (Union[Unset, bool]):
        object_type (Union[Unset, str]):
        object_type_ic (Union[Unset, str]):
        object_type_ie (Union[Unset, str]):
        object_type_iew (Union[Unset, str]):
        object_type_isw (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_nic (Union[Unset, str]):
        object_type_nie (Union[Unset, str]):
        object_type_niew (Union[Unset, str]):
        object_type_nisw (Union[Unset, str]):
        object_type_id (Union[Unset, list[int]]):
        object_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
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
        Response[PaginatedCustomLinkList]
    """

    kwargs = _get_kwargs(
        button_class=button_class,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        enabled=enabled,
        group_name=group_name,
        group_name_empty=group_name_empty,
        group_name_ic=group_name_ic,
        group_name_ie=group_name_ie,
        group_name_iew=group_name_iew,
        group_name_isw=group_name_isw,
        group_name_n=group_name_n,
        group_name_nic=group_name_nic,
        group_name_nie=group_name_nie,
        group_name_niew=group_name_niew,
        group_name_nisw=group_name_nisw,
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
        link_text=link_text,
        link_text_ic=link_text_ic,
        link_text_ie=link_text_ie,
        link_text_iew=link_text_iew,
        link_text_isw=link_text_isw,
        link_text_n=link_text_n,
        link_text_nic=link_text_nic,
        link_text_nie=link_text_nie,
        link_text_niew=link_text_niew,
        link_text_nisw=link_text_nisw,
        link_url=link_url,
        link_url_ic=link_url_ic,
        link_url_ie=link_url_ie,
        link_url_iew=link_url_iew,
        link_url_isw=link_url_isw,
        link_url_n=link_url_n,
        link_url_nic=link_url_nic,
        link_url_nie=link_url_nie,
        link_url_niew=link_url_niew,
        link_url_nisw=link_url_nisw,
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
        new_window=new_window,
        object_type=object_type,
        object_type_ic=object_type_ic,
        object_type_ie=object_type_ie,
        object_type_iew=object_type_iew,
        object_type_isw=object_type_isw,
        object_type_n=object_type_n,
        object_type_nic=object_type_nic,
        object_type_nie=object_type_nie,
        object_type_niew=object_type_niew,
        object_type_nisw=object_type_nisw,
        object_type_id=object_type_id,
        object_type_id_n=object_type_id_n,
        offset=offset,
        ordering=ordering,
        q=q,
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
    button_class: Union[Unset, ExtrasCustomLinksListButtonClass] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    group_name: Union[Unset, list[str]] = UNSET,
    group_name_empty: Union[Unset, bool] = UNSET,
    group_name_ic: Union[Unset, list[str]] = UNSET,
    group_name_ie: Union[Unset, list[str]] = UNSET,
    group_name_iew: Union[Unset, list[str]] = UNSET,
    group_name_isw: Union[Unset, list[str]] = UNSET,
    group_name_n: Union[Unset, list[str]] = UNSET,
    group_name_nic: Union[Unset, list[str]] = UNSET,
    group_name_nie: Union[Unset, list[str]] = UNSET,
    group_name_niew: Union[Unset, list[str]] = UNSET,
    group_name_nisw: Union[Unset, list[str]] = UNSET,
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
    link_text: Union[Unset, str] = UNSET,
    link_text_ic: Union[Unset, str] = UNSET,
    link_text_ie: Union[Unset, str] = UNSET,
    link_text_iew: Union[Unset, str] = UNSET,
    link_text_isw: Union[Unset, str] = UNSET,
    link_text_n: Union[Unset, str] = UNSET,
    link_text_nic: Union[Unset, str] = UNSET,
    link_text_nie: Union[Unset, str] = UNSET,
    link_text_niew: Union[Unset, str] = UNSET,
    link_text_nisw: Union[Unset, str] = UNSET,
    link_url: Union[Unset, str] = UNSET,
    link_url_ic: Union[Unset, str] = UNSET,
    link_url_ie: Union[Unset, str] = UNSET,
    link_url_iew: Union[Unset, str] = UNSET,
    link_url_isw: Union[Unset, str] = UNSET,
    link_url_n: Union[Unset, str] = UNSET,
    link_url_nic: Union[Unset, str] = UNSET,
    link_url_nie: Union[Unset, str] = UNSET,
    link_url_niew: Union[Unset, str] = UNSET,
    link_url_nisw: Union[Unset, str] = UNSET,
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
    new_window: Union[Unset, bool] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    object_type_ic: Union[Unset, str] = UNSET,
    object_type_ie: Union[Unset, str] = UNSET,
    object_type_iew: Union[Unset, str] = UNSET,
    object_type_isw: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_nic: Union[Unset, str] = UNSET,
    object_type_nie: Union[Unset, str] = UNSET,
    object_type_niew: Union[Unset, str] = UNSET,
    object_type_nisw: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    weight: Union[Unset, list[int]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[int]] = UNSET,
    weight_gte: Union[Unset, list[int]] = UNSET,
    weight_lt: Union[Unset, list[int]] = UNSET,
    weight_lte: Union[Unset, list[int]] = UNSET,
    weight_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedCustomLinkList]:
    """Get a list of custom link objects.

    Args:
        button_class (Union[Unset, ExtrasCustomLinksListButtonClass]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        enabled (Union[Unset, bool]):
        group_name (Union[Unset, list[str]]):
        group_name_empty (Union[Unset, bool]):
        group_name_ic (Union[Unset, list[str]]):
        group_name_ie (Union[Unset, list[str]]):
        group_name_iew (Union[Unset, list[str]]):
        group_name_isw (Union[Unset, list[str]]):
        group_name_n (Union[Unset, list[str]]):
        group_name_nic (Union[Unset, list[str]]):
        group_name_nie (Union[Unset, list[str]]):
        group_name_niew (Union[Unset, list[str]]):
        group_name_nisw (Union[Unset, list[str]]):
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
        link_text (Union[Unset, str]):
        link_text_ic (Union[Unset, str]):
        link_text_ie (Union[Unset, str]):
        link_text_iew (Union[Unset, str]):
        link_text_isw (Union[Unset, str]):
        link_text_n (Union[Unset, str]):
        link_text_nic (Union[Unset, str]):
        link_text_nie (Union[Unset, str]):
        link_text_niew (Union[Unset, str]):
        link_text_nisw (Union[Unset, str]):
        link_url (Union[Unset, str]):
        link_url_ic (Union[Unset, str]):
        link_url_ie (Union[Unset, str]):
        link_url_iew (Union[Unset, str]):
        link_url_isw (Union[Unset, str]):
        link_url_n (Union[Unset, str]):
        link_url_nic (Union[Unset, str]):
        link_url_nie (Union[Unset, str]):
        link_url_niew (Union[Unset, str]):
        link_url_nisw (Union[Unset, str]):
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
        new_window (Union[Unset, bool]):
        object_type (Union[Unset, str]):
        object_type_ic (Union[Unset, str]):
        object_type_ie (Union[Unset, str]):
        object_type_iew (Union[Unset, str]):
        object_type_isw (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_nic (Union[Unset, str]):
        object_type_nie (Union[Unset, str]):
        object_type_niew (Union[Unset, str]):
        object_type_nisw (Union[Unset, str]):
        object_type_id (Union[Unset, list[int]]):
        object_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
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
        PaginatedCustomLinkList
    """

    return sync_detailed(
        client=client,
        button_class=button_class,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        enabled=enabled,
        group_name=group_name,
        group_name_empty=group_name_empty,
        group_name_ic=group_name_ic,
        group_name_ie=group_name_ie,
        group_name_iew=group_name_iew,
        group_name_isw=group_name_isw,
        group_name_n=group_name_n,
        group_name_nic=group_name_nic,
        group_name_nie=group_name_nie,
        group_name_niew=group_name_niew,
        group_name_nisw=group_name_nisw,
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
        link_text=link_text,
        link_text_ic=link_text_ic,
        link_text_ie=link_text_ie,
        link_text_iew=link_text_iew,
        link_text_isw=link_text_isw,
        link_text_n=link_text_n,
        link_text_nic=link_text_nic,
        link_text_nie=link_text_nie,
        link_text_niew=link_text_niew,
        link_text_nisw=link_text_nisw,
        link_url=link_url,
        link_url_ic=link_url_ic,
        link_url_ie=link_url_ie,
        link_url_iew=link_url_iew,
        link_url_isw=link_url_isw,
        link_url_n=link_url_n,
        link_url_nic=link_url_nic,
        link_url_nie=link_url_nie,
        link_url_niew=link_url_niew,
        link_url_nisw=link_url_nisw,
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
        new_window=new_window,
        object_type=object_type,
        object_type_ic=object_type_ic,
        object_type_ie=object_type_ie,
        object_type_iew=object_type_iew,
        object_type_isw=object_type_isw,
        object_type_n=object_type_n,
        object_type_nic=object_type_nic,
        object_type_nie=object_type_nie,
        object_type_niew=object_type_niew,
        object_type_nisw=object_type_nisw,
        object_type_id=object_type_id,
        object_type_id_n=object_type_id_n,
        offset=offset,
        ordering=ordering,
        q=q,
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
    button_class: Union[Unset, ExtrasCustomLinksListButtonClass] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    group_name: Union[Unset, list[str]] = UNSET,
    group_name_empty: Union[Unset, bool] = UNSET,
    group_name_ic: Union[Unset, list[str]] = UNSET,
    group_name_ie: Union[Unset, list[str]] = UNSET,
    group_name_iew: Union[Unset, list[str]] = UNSET,
    group_name_isw: Union[Unset, list[str]] = UNSET,
    group_name_n: Union[Unset, list[str]] = UNSET,
    group_name_nic: Union[Unset, list[str]] = UNSET,
    group_name_nie: Union[Unset, list[str]] = UNSET,
    group_name_niew: Union[Unset, list[str]] = UNSET,
    group_name_nisw: Union[Unset, list[str]] = UNSET,
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
    link_text: Union[Unset, str] = UNSET,
    link_text_ic: Union[Unset, str] = UNSET,
    link_text_ie: Union[Unset, str] = UNSET,
    link_text_iew: Union[Unset, str] = UNSET,
    link_text_isw: Union[Unset, str] = UNSET,
    link_text_n: Union[Unset, str] = UNSET,
    link_text_nic: Union[Unset, str] = UNSET,
    link_text_nie: Union[Unset, str] = UNSET,
    link_text_niew: Union[Unset, str] = UNSET,
    link_text_nisw: Union[Unset, str] = UNSET,
    link_url: Union[Unset, str] = UNSET,
    link_url_ic: Union[Unset, str] = UNSET,
    link_url_ie: Union[Unset, str] = UNSET,
    link_url_iew: Union[Unset, str] = UNSET,
    link_url_isw: Union[Unset, str] = UNSET,
    link_url_n: Union[Unset, str] = UNSET,
    link_url_nic: Union[Unset, str] = UNSET,
    link_url_nie: Union[Unset, str] = UNSET,
    link_url_niew: Union[Unset, str] = UNSET,
    link_url_nisw: Union[Unset, str] = UNSET,
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
    new_window: Union[Unset, bool] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    object_type_ic: Union[Unset, str] = UNSET,
    object_type_ie: Union[Unset, str] = UNSET,
    object_type_iew: Union[Unset, str] = UNSET,
    object_type_isw: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_nic: Union[Unset, str] = UNSET,
    object_type_nie: Union[Unset, str] = UNSET,
    object_type_niew: Union[Unset, str] = UNSET,
    object_type_nisw: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    weight: Union[Unset, list[int]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[int]] = UNSET,
    weight_gte: Union[Unset, list[int]] = UNSET,
    weight_lt: Union[Unset, list[int]] = UNSET,
    weight_lte: Union[Unset, list[int]] = UNSET,
    weight_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedCustomLinkList]:
    """Get a list of custom link objects.

    Args:
        button_class (Union[Unset, ExtrasCustomLinksListButtonClass]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        enabled (Union[Unset, bool]):
        group_name (Union[Unset, list[str]]):
        group_name_empty (Union[Unset, bool]):
        group_name_ic (Union[Unset, list[str]]):
        group_name_ie (Union[Unset, list[str]]):
        group_name_iew (Union[Unset, list[str]]):
        group_name_isw (Union[Unset, list[str]]):
        group_name_n (Union[Unset, list[str]]):
        group_name_nic (Union[Unset, list[str]]):
        group_name_nie (Union[Unset, list[str]]):
        group_name_niew (Union[Unset, list[str]]):
        group_name_nisw (Union[Unset, list[str]]):
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
        link_text (Union[Unset, str]):
        link_text_ic (Union[Unset, str]):
        link_text_ie (Union[Unset, str]):
        link_text_iew (Union[Unset, str]):
        link_text_isw (Union[Unset, str]):
        link_text_n (Union[Unset, str]):
        link_text_nic (Union[Unset, str]):
        link_text_nie (Union[Unset, str]):
        link_text_niew (Union[Unset, str]):
        link_text_nisw (Union[Unset, str]):
        link_url (Union[Unset, str]):
        link_url_ic (Union[Unset, str]):
        link_url_ie (Union[Unset, str]):
        link_url_iew (Union[Unset, str]):
        link_url_isw (Union[Unset, str]):
        link_url_n (Union[Unset, str]):
        link_url_nic (Union[Unset, str]):
        link_url_nie (Union[Unset, str]):
        link_url_niew (Union[Unset, str]):
        link_url_nisw (Union[Unset, str]):
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
        new_window (Union[Unset, bool]):
        object_type (Union[Unset, str]):
        object_type_ic (Union[Unset, str]):
        object_type_ie (Union[Unset, str]):
        object_type_iew (Union[Unset, str]):
        object_type_isw (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_nic (Union[Unset, str]):
        object_type_nie (Union[Unset, str]):
        object_type_niew (Union[Unset, str]):
        object_type_nisw (Union[Unset, str]):
        object_type_id (Union[Unset, list[int]]):
        object_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
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
        Response[PaginatedCustomLinkList]
    """

    kwargs = _get_kwargs(
        button_class=button_class,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        enabled=enabled,
        group_name=group_name,
        group_name_empty=group_name_empty,
        group_name_ic=group_name_ic,
        group_name_ie=group_name_ie,
        group_name_iew=group_name_iew,
        group_name_isw=group_name_isw,
        group_name_n=group_name_n,
        group_name_nic=group_name_nic,
        group_name_nie=group_name_nie,
        group_name_niew=group_name_niew,
        group_name_nisw=group_name_nisw,
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
        link_text=link_text,
        link_text_ic=link_text_ic,
        link_text_ie=link_text_ie,
        link_text_iew=link_text_iew,
        link_text_isw=link_text_isw,
        link_text_n=link_text_n,
        link_text_nic=link_text_nic,
        link_text_nie=link_text_nie,
        link_text_niew=link_text_niew,
        link_text_nisw=link_text_nisw,
        link_url=link_url,
        link_url_ic=link_url_ic,
        link_url_ie=link_url_ie,
        link_url_iew=link_url_iew,
        link_url_isw=link_url_isw,
        link_url_n=link_url_n,
        link_url_nic=link_url_nic,
        link_url_nie=link_url_nie,
        link_url_niew=link_url_niew,
        link_url_nisw=link_url_nisw,
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
        new_window=new_window,
        object_type=object_type,
        object_type_ic=object_type_ic,
        object_type_ie=object_type_ie,
        object_type_iew=object_type_iew,
        object_type_isw=object_type_isw,
        object_type_n=object_type_n,
        object_type_nic=object_type_nic,
        object_type_nie=object_type_nie,
        object_type_niew=object_type_niew,
        object_type_nisw=object_type_nisw,
        object_type_id=object_type_id,
        object_type_id_n=object_type_id_n,
        offset=offset,
        ordering=ordering,
        q=q,
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
    button_class: Union[Unset, ExtrasCustomLinksListButtonClass] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    group_name: Union[Unset, list[str]] = UNSET,
    group_name_empty: Union[Unset, bool] = UNSET,
    group_name_ic: Union[Unset, list[str]] = UNSET,
    group_name_ie: Union[Unset, list[str]] = UNSET,
    group_name_iew: Union[Unset, list[str]] = UNSET,
    group_name_isw: Union[Unset, list[str]] = UNSET,
    group_name_n: Union[Unset, list[str]] = UNSET,
    group_name_nic: Union[Unset, list[str]] = UNSET,
    group_name_nie: Union[Unset, list[str]] = UNSET,
    group_name_niew: Union[Unset, list[str]] = UNSET,
    group_name_nisw: Union[Unset, list[str]] = UNSET,
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
    link_text: Union[Unset, str] = UNSET,
    link_text_ic: Union[Unset, str] = UNSET,
    link_text_ie: Union[Unset, str] = UNSET,
    link_text_iew: Union[Unset, str] = UNSET,
    link_text_isw: Union[Unset, str] = UNSET,
    link_text_n: Union[Unset, str] = UNSET,
    link_text_nic: Union[Unset, str] = UNSET,
    link_text_nie: Union[Unset, str] = UNSET,
    link_text_niew: Union[Unset, str] = UNSET,
    link_text_nisw: Union[Unset, str] = UNSET,
    link_url: Union[Unset, str] = UNSET,
    link_url_ic: Union[Unset, str] = UNSET,
    link_url_ie: Union[Unset, str] = UNSET,
    link_url_iew: Union[Unset, str] = UNSET,
    link_url_isw: Union[Unset, str] = UNSET,
    link_url_n: Union[Unset, str] = UNSET,
    link_url_nic: Union[Unset, str] = UNSET,
    link_url_nie: Union[Unset, str] = UNSET,
    link_url_niew: Union[Unset, str] = UNSET,
    link_url_nisw: Union[Unset, str] = UNSET,
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
    new_window: Union[Unset, bool] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    object_type_ic: Union[Unset, str] = UNSET,
    object_type_ie: Union[Unset, str] = UNSET,
    object_type_iew: Union[Unset, str] = UNSET,
    object_type_isw: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_nic: Union[Unset, str] = UNSET,
    object_type_nie: Union[Unset, str] = UNSET,
    object_type_niew: Union[Unset, str] = UNSET,
    object_type_nisw: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    weight: Union[Unset, list[int]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[int]] = UNSET,
    weight_gte: Union[Unset, list[int]] = UNSET,
    weight_lt: Union[Unset, list[int]] = UNSET,
    weight_lte: Union[Unset, list[int]] = UNSET,
    weight_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedCustomLinkList]:
    """Get a list of custom link objects.

    Args:
        button_class (Union[Unset, ExtrasCustomLinksListButtonClass]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        enabled (Union[Unset, bool]):
        group_name (Union[Unset, list[str]]):
        group_name_empty (Union[Unset, bool]):
        group_name_ic (Union[Unset, list[str]]):
        group_name_ie (Union[Unset, list[str]]):
        group_name_iew (Union[Unset, list[str]]):
        group_name_isw (Union[Unset, list[str]]):
        group_name_n (Union[Unset, list[str]]):
        group_name_nic (Union[Unset, list[str]]):
        group_name_nie (Union[Unset, list[str]]):
        group_name_niew (Union[Unset, list[str]]):
        group_name_nisw (Union[Unset, list[str]]):
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
        link_text (Union[Unset, str]):
        link_text_ic (Union[Unset, str]):
        link_text_ie (Union[Unset, str]):
        link_text_iew (Union[Unset, str]):
        link_text_isw (Union[Unset, str]):
        link_text_n (Union[Unset, str]):
        link_text_nic (Union[Unset, str]):
        link_text_nie (Union[Unset, str]):
        link_text_niew (Union[Unset, str]):
        link_text_nisw (Union[Unset, str]):
        link_url (Union[Unset, str]):
        link_url_ic (Union[Unset, str]):
        link_url_ie (Union[Unset, str]):
        link_url_iew (Union[Unset, str]):
        link_url_isw (Union[Unset, str]):
        link_url_n (Union[Unset, str]):
        link_url_nic (Union[Unset, str]):
        link_url_nie (Union[Unset, str]):
        link_url_niew (Union[Unset, str]):
        link_url_nisw (Union[Unset, str]):
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
        new_window (Union[Unset, bool]):
        object_type (Union[Unset, str]):
        object_type_ic (Union[Unset, str]):
        object_type_ie (Union[Unset, str]):
        object_type_iew (Union[Unset, str]):
        object_type_isw (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_nic (Union[Unset, str]):
        object_type_nie (Union[Unset, str]):
        object_type_niew (Union[Unset, str]):
        object_type_nisw (Union[Unset, str]):
        object_type_id (Union[Unset, list[int]]):
        object_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
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
        PaginatedCustomLinkList
    """

    return (
        await asyncio_detailed(
            client=client,
            button_class=button_class,
            created=created,
            created_empty=created_empty,
            created_gt=created_gt,
            created_gte=created_gte,
            created_lt=created_lt,
            created_lte=created_lte,
            created_n=created_n,
            created_by_request=created_by_request,
            enabled=enabled,
            group_name=group_name,
            group_name_empty=group_name_empty,
            group_name_ic=group_name_ic,
            group_name_ie=group_name_ie,
            group_name_iew=group_name_iew,
            group_name_isw=group_name_isw,
            group_name_n=group_name_n,
            group_name_nic=group_name_nic,
            group_name_nie=group_name_nie,
            group_name_niew=group_name_niew,
            group_name_nisw=group_name_nisw,
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
            link_text=link_text,
            link_text_ic=link_text_ic,
            link_text_ie=link_text_ie,
            link_text_iew=link_text_iew,
            link_text_isw=link_text_isw,
            link_text_n=link_text_n,
            link_text_nic=link_text_nic,
            link_text_nie=link_text_nie,
            link_text_niew=link_text_niew,
            link_text_nisw=link_text_nisw,
            link_url=link_url,
            link_url_ic=link_url_ic,
            link_url_ie=link_url_ie,
            link_url_iew=link_url_iew,
            link_url_isw=link_url_isw,
            link_url_n=link_url_n,
            link_url_nic=link_url_nic,
            link_url_nie=link_url_nie,
            link_url_niew=link_url_niew,
            link_url_nisw=link_url_nisw,
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
            new_window=new_window,
            object_type=object_type,
            object_type_ic=object_type_ic,
            object_type_ie=object_type_ie,
            object_type_iew=object_type_iew,
            object_type_isw=object_type_isw,
            object_type_n=object_type_n,
            object_type_nic=object_type_nic,
            object_type_nie=object_type_nie,
            object_type_niew=object_type_niew,
            object_type_nisw=object_type_nisw,
            object_type_id=object_type_id,
            object_type_id_n=object_type_id_n,
            offset=offset,
            ordering=ordering,
            q=q,
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
