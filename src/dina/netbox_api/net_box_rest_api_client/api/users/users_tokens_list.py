import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_token_list import PaginatedTokenList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created: Union[Unset, datetime.datetime] = UNSET,
    created_gte: Union[Unset, datetime.datetime] = UNSET,
    created_lte: Union[Unset, datetime.datetime] = UNSET,
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
    expires: Union[Unset, datetime.datetime] = UNSET,
    expires_gte: Union[Unset, datetime.datetime] = UNSET,
    expires_lte: Union[Unset, datetime.datetime] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    key: Union[Unset, list[str]] = UNSET,
    key_empty: Union[Unset, bool] = UNSET,
    key_ic: Union[Unset, list[str]] = UNSET,
    key_ie: Union[Unset, list[str]] = UNSET,
    key_iew: Union[Unset, list[str]] = UNSET,
    key_isw: Union[Unset, list[str]] = UNSET,
    key_n: Union[Unset, list[str]] = UNSET,
    key_nic: Union[Unset, list[str]] = UNSET,
    key_nie: Union[Unset, list[str]] = UNSET,
    key_niew: Union[Unset, list[str]] = UNSET,
    key_nisw: Union[Unset, list[str]] = UNSET,
    last_used: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_empty: Union[Unset, bool] = UNSET,
    last_used_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[int]] = UNSET,
    user_id_n: Union[Unset, list[int]] = UNSET,
    write_enabled: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_created: Union[Unset, str] = UNSET
    if not isinstance(created, Unset):
        json_created = created.isoformat()
    params["created"] = json_created

    json_created_gte: Union[Unset, str] = UNSET
    if not isinstance(created_gte, Unset):
        json_created_gte = created_gte.isoformat()
    params["created__gte"] = json_created_gte

    json_created_lte: Union[Unset, str] = UNSET
    if not isinstance(created_lte, Unset):
        json_created_lte = created_lte.isoformat()
    params["created__lte"] = json_created_lte

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

    json_expires: Union[Unset, str] = UNSET
    if not isinstance(expires, Unset):
        json_expires = expires.isoformat()
    params["expires"] = json_expires

    json_expires_gte: Union[Unset, str] = UNSET
    if not isinstance(expires_gte, Unset):
        json_expires_gte = expires_gte.isoformat()
    params["expires__gte"] = json_expires_gte

    json_expires_lte: Union[Unset, str] = UNSET
    if not isinstance(expires_lte, Unset):
        json_expires_lte = expires_lte.isoformat()
    params["expires__lte"] = json_expires_lte

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

    json_key: Union[Unset, list[str]] = UNSET
    if not isinstance(key, Unset):
        json_key = key

    params["key"] = json_key

    params["key__empty"] = key_empty

    json_key_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(key_ic, Unset):
        json_key_ic = key_ic

    params["key__ic"] = json_key_ic

    json_key_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(key_ie, Unset):
        json_key_ie = key_ie

    params["key__ie"] = json_key_ie

    json_key_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(key_iew, Unset):
        json_key_iew = key_iew

    params["key__iew"] = json_key_iew

    json_key_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(key_isw, Unset):
        json_key_isw = key_isw

    params["key__isw"] = json_key_isw

    json_key_n: Union[Unset, list[str]] = UNSET
    if not isinstance(key_n, Unset):
        json_key_n = key_n

    params["key__n"] = json_key_n

    json_key_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(key_nic, Unset):
        json_key_nic = key_nic

    params["key__nic"] = json_key_nic

    json_key_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(key_nie, Unset):
        json_key_nie = key_nie

    params["key__nie"] = json_key_nie

    json_key_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(key_niew, Unset):
        json_key_niew = key_niew

    params["key__niew"] = json_key_niew

    json_key_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(key_nisw, Unset):
        json_key_nisw = key_nisw

    params["key__nisw"] = json_key_nisw

    json_last_used: Union[Unset, list[str]] = UNSET
    if not isinstance(last_used, Unset):
        json_last_used = []
        for last_used_item_data in last_used:
            last_used_item = last_used_item_data.isoformat()
            json_last_used.append(last_used_item)

    params["last_used"] = json_last_used

    params["last_used__empty"] = last_used_empty

    json_last_used_gt: Union[Unset, list[str]] = UNSET
    if not isinstance(last_used_gt, Unset):
        json_last_used_gt = []
        for last_used_gt_item_data in last_used_gt:
            last_used_gt_item = last_used_gt_item_data.isoformat()
            json_last_used_gt.append(last_used_gt_item)

    params["last_used__gt"] = json_last_used_gt

    json_last_used_gte: Union[Unset, list[str]] = UNSET
    if not isinstance(last_used_gte, Unset):
        json_last_used_gte = []
        for last_used_gte_item_data in last_used_gte:
            last_used_gte_item = last_used_gte_item_data.isoformat()
            json_last_used_gte.append(last_used_gte_item)

    params["last_used__gte"] = json_last_used_gte

    json_last_used_lt: Union[Unset, list[str]] = UNSET
    if not isinstance(last_used_lt, Unset):
        json_last_used_lt = []
        for last_used_lt_item_data in last_used_lt:
            last_used_lt_item = last_used_lt_item_data.isoformat()
            json_last_used_lt.append(last_used_lt_item)

    params["last_used__lt"] = json_last_used_lt

    json_last_used_lte: Union[Unset, list[str]] = UNSET
    if not isinstance(last_used_lte, Unset):
        json_last_used_lte = []
        for last_used_lte_item_data in last_used_lte:
            last_used_lte_item = last_used_lte_item_data.isoformat()
            json_last_used_lte.append(last_used_lte_item)

    params["last_used__lte"] = json_last_used_lte

    json_last_used_n: Union[Unset, list[str]] = UNSET
    if not isinstance(last_used_n, Unset):
        json_last_used_n = []
        for last_used_n_item_data in last_used_n:
            last_used_n_item = last_used_n_item_data.isoformat()
            json_last_used_n.append(last_used_n_item)

    params["last_used__n"] = json_last_used_n

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    params["q"] = q

    json_user: Union[Unset, list[str]] = UNSET
    if not isinstance(user, Unset):
        json_user = user

    params["user"] = json_user

    json_user_n: Union[Unset, list[str]] = UNSET
    if not isinstance(user_n, Unset):
        json_user_n = user_n

    params["user__n"] = json_user_n

    json_user_id: Union[Unset, list[int]] = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = user_id

    params["user_id"] = json_user_id

    json_user_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(user_id_n, Unset):
        json_user_id_n = user_id_n

    params["user_id__n"] = json_user_id_n

    params["write_enabled"] = write_enabled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/users/tokens/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedTokenList]:
    if response.status_code == 200:
        response_200 = PaginatedTokenList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedTokenList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, datetime.datetime] = UNSET,
    created_gte: Union[Unset, datetime.datetime] = UNSET,
    created_lte: Union[Unset, datetime.datetime] = UNSET,
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
    expires: Union[Unset, datetime.datetime] = UNSET,
    expires_gte: Union[Unset, datetime.datetime] = UNSET,
    expires_lte: Union[Unset, datetime.datetime] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    key: Union[Unset, list[str]] = UNSET,
    key_empty: Union[Unset, bool] = UNSET,
    key_ic: Union[Unset, list[str]] = UNSET,
    key_ie: Union[Unset, list[str]] = UNSET,
    key_iew: Union[Unset, list[str]] = UNSET,
    key_isw: Union[Unset, list[str]] = UNSET,
    key_n: Union[Unset, list[str]] = UNSET,
    key_nic: Union[Unset, list[str]] = UNSET,
    key_nie: Union[Unset, list[str]] = UNSET,
    key_niew: Union[Unset, list[str]] = UNSET,
    key_nisw: Union[Unset, list[str]] = UNSET,
    last_used: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_empty: Union[Unset, bool] = UNSET,
    last_used_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[int]] = UNSET,
    user_id_n: Union[Unset, list[int]] = UNSET,
    write_enabled: Union[Unset, bool] = UNSET,
) -> Response[PaginatedTokenList]:
    """Get a list of token objects.

    Args:
        created (Union[Unset, datetime.datetime]):
        created_gte (Union[Unset, datetime.datetime]):
        created_lte (Union[Unset, datetime.datetime]):
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
        expires (Union[Unset, datetime.datetime]):
        expires_gte (Union[Unset, datetime.datetime]):
        expires_lte (Union[Unset, datetime.datetime]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        key (Union[Unset, list[str]]):
        key_empty (Union[Unset, bool]):
        key_ic (Union[Unset, list[str]]):
        key_ie (Union[Unset, list[str]]):
        key_iew (Union[Unset, list[str]]):
        key_isw (Union[Unset, list[str]]):
        key_n (Union[Unset, list[str]]):
        key_nic (Union[Unset, list[str]]):
        key_nie (Union[Unset, list[str]]):
        key_niew (Union[Unset, list[str]]):
        key_nisw (Union[Unset, list[str]]):
        last_used (Union[Unset, list[datetime.datetime]]):
        last_used_empty (Union[Unset, bool]):
        last_used_gt (Union[Unset, list[datetime.datetime]]):
        last_used_gte (Union[Unset, list[datetime.datetime]]):
        last_used_lt (Union[Unset, list[datetime.datetime]]):
        last_used_lte (Union[Unset, list[datetime.datetime]]):
        last_used_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        user (Union[Unset, list[str]]):
        user_n (Union[Unset, list[str]]):
        user_id (Union[Unset, list[int]]):
        user_id_n (Union[Unset, list[int]]):
        write_enabled (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTokenList]
    """

    kwargs = _get_kwargs(
        created=created,
        created_gte=created_gte,
        created_lte=created_lte,
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
        expires=expires,
        expires_gte=expires_gte,
        expires_lte=expires_lte,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        key=key,
        key_empty=key_empty,
        key_ic=key_ic,
        key_ie=key_ie,
        key_iew=key_iew,
        key_isw=key_isw,
        key_n=key_n,
        key_nic=key_nic,
        key_nie=key_nie,
        key_niew=key_niew,
        key_nisw=key_nisw,
        last_used=last_used,
        last_used_empty=last_used_empty,
        last_used_gt=last_used_gt,
        last_used_gte=last_used_gte,
        last_used_lt=last_used_lt,
        last_used_lte=last_used_lte,
        last_used_n=last_used_n,
        limit=limit,
        offset=offset,
        ordering=ordering,
        q=q,
        user=user,
        user_n=user_n,
        user_id=user_id,
        user_id_n=user_id_n,
        write_enabled=write_enabled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, datetime.datetime] = UNSET,
    created_gte: Union[Unset, datetime.datetime] = UNSET,
    created_lte: Union[Unset, datetime.datetime] = UNSET,
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
    expires: Union[Unset, datetime.datetime] = UNSET,
    expires_gte: Union[Unset, datetime.datetime] = UNSET,
    expires_lte: Union[Unset, datetime.datetime] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    key: Union[Unset, list[str]] = UNSET,
    key_empty: Union[Unset, bool] = UNSET,
    key_ic: Union[Unset, list[str]] = UNSET,
    key_ie: Union[Unset, list[str]] = UNSET,
    key_iew: Union[Unset, list[str]] = UNSET,
    key_isw: Union[Unset, list[str]] = UNSET,
    key_n: Union[Unset, list[str]] = UNSET,
    key_nic: Union[Unset, list[str]] = UNSET,
    key_nie: Union[Unset, list[str]] = UNSET,
    key_niew: Union[Unset, list[str]] = UNSET,
    key_nisw: Union[Unset, list[str]] = UNSET,
    last_used: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_empty: Union[Unset, bool] = UNSET,
    last_used_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[int]] = UNSET,
    user_id_n: Union[Unset, list[int]] = UNSET,
    write_enabled: Union[Unset, bool] = UNSET,
) -> Optional[PaginatedTokenList]:
    """Get a list of token objects.

    Args:
        created (Union[Unset, datetime.datetime]):
        created_gte (Union[Unset, datetime.datetime]):
        created_lte (Union[Unset, datetime.datetime]):
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
        expires (Union[Unset, datetime.datetime]):
        expires_gte (Union[Unset, datetime.datetime]):
        expires_lte (Union[Unset, datetime.datetime]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        key (Union[Unset, list[str]]):
        key_empty (Union[Unset, bool]):
        key_ic (Union[Unset, list[str]]):
        key_ie (Union[Unset, list[str]]):
        key_iew (Union[Unset, list[str]]):
        key_isw (Union[Unset, list[str]]):
        key_n (Union[Unset, list[str]]):
        key_nic (Union[Unset, list[str]]):
        key_nie (Union[Unset, list[str]]):
        key_niew (Union[Unset, list[str]]):
        key_nisw (Union[Unset, list[str]]):
        last_used (Union[Unset, list[datetime.datetime]]):
        last_used_empty (Union[Unset, bool]):
        last_used_gt (Union[Unset, list[datetime.datetime]]):
        last_used_gte (Union[Unset, list[datetime.datetime]]):
        last_used_lt (Union[Unset, list[datetime.datetime]]):
        last_used_lte (Union[Unset, list[datetime.datetime]]):
        last_used_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        user (Union[Unset, list[str]]):
        user_n (Union[Unset, list[str]]):
        user_id (Union[Unset, list[int]]):
        user_id_n (Union[Unset, list[int]]):
        write_enabled (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTokenList
    """

    return sync_detailed(
        client=client,
        created=created,
        created_gte=created_gte,
        created_lte=created_lte,
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
        expires=expires,
        expires_gte=expires_gte,
        expires_lte=expires_lte,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        key=key,
        key_empty=key_empty,
        key_ic=key_ic,
        key_ie=key_ie,
        key_iew=key_iew,
        key_isw=key_isw,
        key_n=key_n,
        key_nic=key_nic,
        key_nie=key_nie,
        key_niew=key_niew,
        key_nisw=key_nisw,
        last_used=last_used,
        last_used_empty=last_used_empty,
        last_used_gt=last_used_gt,
        last_used_gte=last_used_gte,
        last_used_lt=last_used_lt,
        last_used_lte=last_used_lte,
        last_used_n=last_used_n,
        limit=limit,
        offset=offset,
        ordering=ordering,
        q=q,
        user=user,
        user_n=user_n,
        user_id=user_id,
        user_id_n=user_id_n,
        write_enabled=write_enabled,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, datetime.datetime] = UNSET,
    created_gte: Union[Unset, datetime.datetime] = UNSET,
    created_lte: Union[Unset, datetime.datetime] = UNSET,
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
    expires: Union[Unset, datetime.datetime] = UNSET,
    expires_gte: Union[Unset, datetime.datetime] = UNSET,
    expires_lte: Union[Unset, datetime.datetime] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    key: Union[Unset, list[str]] = UNSET,
    key_empty: Union[Unset, bool] = UNSET,
    key_ic: Union[Unset, list[str]] = UNSET,
    key_ie: Union[Unset, list[str]] = UNSET,
    key_iew: Union[Unset, list[str]] = UNSET,
    key_isw: Union[Unset, list[str]] = UNSET,
    key_n: Union[Unset, list[str]] = UNSET,
    key_nic: Union[Unset, list[str]] = UNSET,
    key_nie: Union[Unset, list[str]] = UNSET,
    key_niew: Union[Unset, list[str]] = UNSET,
    key_nisw: Union[Unset, list[str]] = UNSET,
    last_used: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_empty: Union[Unset, bool] = UNSET,
    last_used_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[int]] = UNSET,
    user_id_n: Union[Unset, list[int]] = UNSET,
    write_enabled: Union[Unset, bool] = UNSET,
) -> Response[PaginatedTokenList]:
    """Get a list of token objects.

    Args:
        created (Union[Unset, datetime.datetime]):
        created_gte (Union[Unset, datetime.datetime]):
        created_lte (Union[Unset, datetime.datetime]):
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
        expires (Union[Unset, datetime.datetime]):
        expires_gte (Union[Unset, datetime.datetime]):
        expires_lte (Union[Unset, datetime.datetime]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        key (Union[Unset, list[str]]):
        key_empty (Union[Unset, bool]):
        key_ic (Union[Unset, list[str]]):
        key_ie (Union[Unset, list[str]]):
        key_iew (Union[Unset, list[str]]):
        key_isw (Union[Unset, list[str]]):
        key_n (Union[Unset, list[str]]):
        key_nic (Union[Unset, list[str]]):
        key_nie (Union[Unset, list[str]]):
        key_niew (Union[Unset, list[str]]):
        key_nisw (Union[Unset, list[str]]):
        last_used (Union[Unset, list[datetime.datetime]]):
        last_used_empty (Union[Unset, bool]):
        last_used_gt (Union[Unset, list[datetime.datetime]]):
        last_used_gte (Union[Unset, list[datetime.datetime]]):
        last_used_lt (Union[Unset, list[datetime.datetime]]):
        last_used_lte (Union[Unset, list[datetime.datetime]]):
        last_used_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        user (Union[Unset, list[str]]):
        user_n (Union[Unset, list[str]]):
        user_id (Union[Unset, list[int]]):
        user_id_n (Union[Unset, list[int]]):
        write_enabled (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTokenList]
    """

    kwargs = _get_kwargs(
        created=created,
        created_gte=created_gte,
        created_lte=created_lte,
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
        expires=expires,
        expires_gte=expires_gte,
        expires_lte=expires_lte,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        key=key,
        key_empty=key_empty,
        key_ic=key_ic,
        key_ie=key_ie,
        key_iew=key_iew,
        key_isw=key_isw,
        key_n=key_n,
        key_nic=key_nic,
        key_nie=key_nie,
        key_niew=key_niew,
        key_nisw=key_nisw,
        last_used=last_used,
        last_used_empty=last_used_empty,
        last_used_gt=last_used_gt,
        last_used_gte=last_used_gte,
        last_used_lt=last_used_lt,
        last_used_lte=last_used_lte,
        last_used_n=last_used_n,
        limit=limit,
        offset=offset,
        ordering=ordering,
        q=q,
        user=user,
        user_n=user_n,
        user_id=user_id,
        user_id_n=user_id_n,
        write_enabled=write_enabled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, datetime.datetime] = UNSET,
    created_gte: Union[Unset, datetime.datetime] = UNSET,
    created_lte: Union[Unset, datetime.datetime] = UNSET,
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
    expires: Union[Unset, datetime.datetime] = UNSET,
    expires_gte: Union[Unset, datetime.datetime] = UNSET,
    expires_lte: Union[Unset, datetime.datetime] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    key: Union[Unset, list[str]] = UNSET,
    key_empty: Union[Unset, bool] = UNSET,
    key_ic: Union[Unset, list[str]] = UNSET,
    key_ie: Union[Unset, list[str]] = UNSET,
    key_iew: Union[Unset, list[str]] = UNSET,
    key_isw: Union[Unset, list[str]] = UNSET,
    key_n: Union[Unset, list[str]] = UNSET,
    key_nic: Union[Unset, list[str]] = UNSET,
    key_nie: Union[Unset, list[str]] = UNSET,
    key_niew: Union[Unset, list[str]] = UNSET,
    key_nisw: Union[Unset, list[str]] = UNSET,
    last_used: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_empty: Union[Unset, bool] = UNSET,
    last_used_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_used_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[int]] = UNSET,
    user_id_n: Union[Unset, list[int]] = UNSET,
    write_enabled: Union[Unset, bool] = UNSET,
) -> Optional[PaginatedTokenList]:
    """Get a list of token objects.

    Args:
        created (Union[Unset, datetime.datetime]):
        created_gte (Union[Unset, datetime.datetime]):
        created_lte (Union[Unset, datetime.datetime]):
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
        expires (Union[Unset, datetime.datetime]):
        expires_gte (Union[Unset, datetime.datetime]):
        expires_lte (Union[Unset, datetime.datetime]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        key (Union[Unset, list[str]]):
        key_empty (Union[Unset, bool]):
        key_ic (Union[Unset, list[str]]):
        key_ie (Union[Unset, list[str]]):
        key_iew (Union[Unset, list[str]]):
        key_isw (Union[Unset, list[str]]):
        key_n (Union[Unset, list[str]]):
        key_nic (Union[Unset, list[str]]):
        key_nie (Union[Unset, list[str]]):
        key_niew (Union[Unset, list[str]]):
        key_nisw (Union[Unset, list[str]]):
        last_used (Union[Unset, list[datetime.datetime]]):
        last_used_empty (Union[Unset, bool]):
        last_used_gt (Union[Unset, list[datetime.datetime]]):
        last_used_gte (Union[Unset, list[datetime.datetime]]):
        last_used_lt (Union[Unset, list[datetime.datetime]]):
        last_used_lte (Union[Unset, list[datetime.datetime]]):
        last_used_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        user (Union[Unset, list[str]]):
        user_n (Union[Unset, list[str]]):
        user_id (Union[Unset, list[int]]):
        user_id_n (Union[Unset, list[int]]):
        write_enabled (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTokenList
    """

    return (
        await asyncio_detailed(
            client=client,
            created=created,
            created_gte=created_gte,
            created_lte=created_lte,
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
            expires=expires,
            expires_gte=expires_gte,
            expires_lte=expires_lte,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            key=key,
            key_empty=key_empty,
            key_ic=key_ic,
            key_ie=key_ie,
            key_iew=key_iew,
            key_isw=key_isw,
            key_n=key_n,
            key_nic=key_nic,
            key_nie=key_nie,
            key_niew=key_niew,
            key_nisw=key_nisw,
            last_used=last_used,
            last_used_empty=last_used_empty,
            last_used_gt=last_used_gt,
            last_used_gte=last_used_gte,
            last_used_lt=last_used_lt,
            last_used_lte=last_used_lte,
            last_used_n=last_used_n,
            limit=limit,
            offset=offset,
            ordering=ordering,
            q=q,
            user=user,
            user_n=user_n,
            user_id=user_id,
            user_id_n=user_id_n,
            write_enabled=write_enabled,
        )
    ).parsed
