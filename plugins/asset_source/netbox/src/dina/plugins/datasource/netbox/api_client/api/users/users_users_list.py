import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_user_list import PaginatedUserList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date_joined: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_empty: Union[Unset, bool] = UNSET,
    date_joined_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_n: Union[Unset, list[datetime.datetime]] = UNSET,
    email: Union[Unset, list[str]] = UNSET,
    email_empty: Union[Unset, bool] = UNSET,
    email_ic: Union[Unset, list[str]] = UNSET,
    email_ie: Union[Unset, list[str]] = UNSET,
    email_iew: Union[Unset, list[str]] = UNSET,
    email_isw: Union[Unset, list[str]] = UNSET,
    email_n: Union[Unset, list[str]] = UNSET,
    email_nic: Union[Unset, list[str]] = UNSET,
    email_nie: Union[Unset, list[str]] = UNSET,
    email_niew: Union[Unset, list[str]] = UNSET,
    email_nisw: Union[Unset, list[str]] = UNSET,
    first_name: Union[Unset, list[str]] = UNSET,
    first_name_empty: Union[Unset, bool] = UNSET,
    first_name_ic: Union[Unset, list[str]] = UNSET,
    first_name_ie: Union[Unset, list[str]] = UNSET,
    first_name_iew: Union[Unset, list[str]] = UNSET,
    first_name_isw: Union[Unset, list[str]] = UNSET,
    first_name_n: Union[Unset, list[str]] = UNSET,
    first_name_nic: Union[Unset, list[str]] = UNSET,
    first_name_nie: Union[Unset, list[str]] = UNSET,
    first_name_niew: Union[Unset, list[str]] = UNSET,
    first_name_nisw: Union[Unset, list[str]] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[int]] = UNSET,
    group_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    is_staff: Union[Unset, bool] = UNSET,
    is_superuser: Union[Unset, bool] = UNSET,
    last_login: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_empty: Union[Unset, bool] = UNSET,
    last_login_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_n: Union[Unset, list[datetime.datetime]] = UNSET,
    last_name: Union[Unset, list[str]] = UNSET,
    last_name_empty: Union[Unset, bool] = UNSET,
    last_name_ic: Union[Unset, list[str]] = UNSET,
    last_name_ie: Union[Unset, list[str]] = UNSET,
    last_name_iew: Union[Unset, list[str]] = UNSET,
    last_name_isw: Union[Unset, list[str]] = UNSET,
    last_name_n: Union[Unset, list[str]] = UNSET,
    last_name_nic: Union[Unset, list[str]] = UNSET,
    last_name_nie: Union[Unset, list[str]] = UNSET,
    last_name_niew: Union[Unset, list[str]] = UNSET,
    last_name_nisw: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    notification_group_id: Union[Unset, list[int]] = UNSET,
    notification_group_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    permission_id: Union[Unset, list[int]] = UNSET,
    permission_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    username: Union[Unset, list[str]] = UNSET,
    username_empty: Union[Unset, bool] = UNSET,
    username_ic: Union[Unset, list[str]] = UNSET,
    username_ie: Union[Unset, list[str]] = UNSET,
    username_iew: Union[Unset, list[str]] = UNSET,
    username_isw: Union[Unset, list[str]] = UNSET,
    username_n: Union[Unset, list[str]] = UNSET,
    username_nic: Union[Unset, list[str]] = UNSET,
    username_nie: Union[Unset, list[str]] = UNSET,
    username_niew: Union[Unset, list[str]] = UNSET,
    username_nisw: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date_joined: Union[Unset, list[str]] = UNSET
    if not isinstance(date_joined, Unset):
        json_date_joined = []
        for date_joined_item_data in date_joined:
            date_joined_item = date_joined_item_data.isoformat()
            json_date_joined.append(date_joined_item)

    params["date_joined"] = json_date_joined

    params["date_joined__empty"] = date_joined_empty

    json_date_joined_gt: Union[Unset, list[str]] = UNSET
    if not isinstance(date_joined_gt, Unset):
        json_date_joined_gt = []
        for date_joined_gt_item_data in date_joined_gt:
            date_joined_gt_item = date_joined_gt_item_data.isoformat()
            json_date_joined_gt.append(date_joined_gt_item)

    params["date_joined__gt"] = json_date_joined_gt

    json_date_joined_gte: Union[Unset, list[str]] = UNSET
    if not isinstance(date_joined_gte, Unset):
        json_date_joined_gte = []
        for date_joined_gte_item_data in date_joined_gte:
            date_joined_gte_item = date_joined_gte_item_data.isoformat()
            json_date_joined_gte.append(date_joined_gte_item)

    params["date_joined__gte"] = json_date_joined_gte

    json_date_joined_lt: Union[Unset, list[str]] = UNSET
    if not isinstance(date_joined_lt, Unset):
        json_date_joined_lt = []
        for date_joined_lt_item_data in date_joined_lt:
            date_joined_lt_item = date_joined_lt_item_data.isoformat()
            json_date_joined_lt.append(date_joined_lt_item)

    params["date_joined__lt"] = json_date_joined_lt

    json_date_joined_lte: Union[Unset, list[str]] = UNSET
    if not isinstance(date_joined_lte, Unset):
        json_date_joined_lte = []
        for date_joined_lte_item_data in date_joined_lte:
            date_joined_lte_item = date_joined_lte_item_data.isoformat()
            json_date_joined_lte.append(date_joined_lte_item)

    params["date_joined__lte"] = json_date_joined_lte

    json_date_joined_n: Union[Unset, list[str]] = UNSET
    if not isinstance(date_joined_n, Unset):
        json_date_joined_n = []
        for date_joined_n_item_data in date_joined_n:
            date_joined_n_item = date_joined_n_item_data.isoformat()
            json_date_joined_n.append(date_joined_n_item)

    params["date_joined__n"] = json_date_joined_n

    json_email: Union[Unset, list[str]] = UNSET
    if not isinstance(email, Unset):
        json_email = email

    params["email"] = json_email

    params["email__empty"] = email_empty

    json_email_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(email_ic, Unset):
        json_email_ic = email_ic

    params["email__ic"] = json_email_ic

    json_email_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(email_ie, Unset):
        json_email_ie = email_ie

    params["email__ie"] = json_email_ie

    json_email_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(email_iew, Unset):
        json_email_iew = email_iew

    params["email__iew"] = json_email_iew

    json_email_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(email_isw, Unset):
        json_email_isw = email_isw

    params["email__isw"] = json_email_isw

    json_email_n: Union[Unset, list[str]] = UNSET
    if not isinstance(email_n, Unset):
        json_email_n = email_n

    params["email__n"] = json_email_n

    json_email_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(email_nic, Unset):
        json_email_nic = email_nic

    params["email__nic"] = json_email_nic

    json_email_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(email_nie, Unset):
        json_email_nie = email_nie

    params["email__nie"] = json_email_nie

    json_email_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(email_niew, Unset):
        json_email_niew = email_niew

    params["email__niew"] = json_email_niew

    json_email_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(email_nisw, Unset):
        json_email_nisw = email_nisw

    params["email__nisw"] = json_email_nisw

    json_first_name: Union[Unset, list[str]] = UNSET
    if not isinstance(first_name, Unset):
        json_first_name = first_name

    params["first_name"] = json_first_name

    params["first_name__empty"] = first_name_empty

    json_first_name_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(first_name_ic, Unset):
        json_first_name_ic = first_name_ic

    params["first_name__ic"] = json_first_name_ic

    json_first_name_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(first_name_ie, Unset):
        json_first_name_ie = first_name_ie

    params["first_name__ie"] = json_first_name_ie

    json_first_name_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(first_name_iew, Unset):
        json_first_name_iew = first_name_iew

    params["first_name__iew"] = json_first_name_iew

    json_first_name_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(first_name_isw, Unset):
        json_first_name_isw = first_name_isw

    params["first_name__isw"] = json_first_name_isw

    json_first_name_n: Union[Unset, list[str]] = UNSET
    if not isinstance(first_name_n, Unset):
        json_first_name_n = first_name_n

    params["first_name__n"] = json_first_name_n

    json_first_name_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(first_name_nic, Unset):
        json_first_name_nic = first_name_nic

    params["first_name__nic"] = json_first_name_nic

    json_first_name_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(first_name_nie, Unset):
        json_first_name_nie = first_name_nie

    params["first_name__nie"] = json_first_name_nie

    json_first_name_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(first_name_niew, Unset):
        json_first_name_niew = first_name_niew

    params["first_name__niew"] = json_first_name_niew

    json_first_name_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(first_name_nisw, Unset):
        json_first_name_nisw = first_name_nisw

    params["first_name__nisw"] = json_first_name_nisw

    json_group: Union[Unset, list[str]] = UNSET
    if not isinstance(group, Unset):
        json_group = group

    params["group"] = json_group

    json_group_n: Union[Unset, list[str]] = UNSET
    if not isinstance(group_n, Unset):
        json_group_n = group_n

    params["group__n"] = json_group_n

    json_group_id: Union[Unset, list[int]] = UNSET
    if not isinstance(group_id, Unset):
        json_group_id = group_id

    params["group_id"] = json_group_id

    json_group_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(group_id_n, Unset):
        json_group_id_n = group_id_n

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

    params["is_active"] = is_active

    params["is_staff"] = is_staff

    params["is_superuser"] = is_superuser

    json_last_login: Union[Unset, list[str]] = UNSET
    if not isinstance(last_login, Unset):
        json_last_login = []
        for last_login_item_data in last_login:
            last_login_item = last_login_item_data.isoformat()
            json_last_login.append(last_login_item)

    params["last_login"] = json_last_login

    params["last_login__empty"] = last_login_empty

    json_last_login_gt: Union[Unset, list[str]] = UNSET
    if not isinstance(last_login_gt, Unset):
        json_last_login_gt = []
        for last_login_gt_item_data in last_login_gt:
            last_login_gt_item = last_login_gt_item_data.isoformat()
            json_last_login_gt.append(last_login_gt_item)

    params["last_login__gt"] = json_last_login_gt

    json_last_login_gte: Union[Unset, list[str]] = UNSET
    if not isinstance(last_login_gte, Unset):
        json_last_login_gte = []
        for last_login_gte_item_data in last_login_gte:
            last_login_gte_item = last_login_gte_item_data.isoformat()
            json_last_login_gte.append(last_login_gte_item)

    params["last_login__gte"] = json_last_login_gte

    json_last_login_lt: Union[Unset, list[str]] = UNSET
    if not isinstance(last_login_lt, Unset):
        json_last_login_lt = []
        for last_login_lt_item_data in last_login_lt:
            last_login_lt_item = last_login_lt_item_data.isoformat()
            json_last_login_lt.append(last_login_lt_item)

    params["last_login__lt"] = json_last_login_lt

    json_last_login_lte: Union[Unset, list[str]] = UNSET
    if not isinstance(last_login_lte, Unset):
        json_last_login_lte = []
        for last_login_lte_item_data in last_login_lte:
            last_login_lte_item = last_login_lte_item_data.isoformat()
            json_last_login_lte.append(last_login_lte_item)

    params["last_login__lte"] = json_last_login_lte

    json_last_login_n: Union[Unset, list[str]] = UNSET
    if not isinstance(last_login_n, Unset):
        json_last_login_n = []
        for last_login_n_item_data in last_login_n:
            last_login_n_item = last_login_n_item_data.isoformat()
            json_last_login_n.append(last_login_n_item)

    params["last_login__n"] = json_last_login_n

    json_last_name: Union[Unset, list[str]] = UNSET
    if not isinstance(last_name, Unset):
        json_last_name = last_name

    params["last_name"] = json_last_name

    params["last_name__empty"] = last_name_empty

    json_last_name_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(last_name_ic, Unset):
        json_last_name_ic = last_name_ic

    params["last_name__ic"] = json_last_name_ic

    json_last_name_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(last_name_ie, Unset):
        json_last_name_ie = last_name_ie

    params["last_name__ie"] = json_last_name_ie

    json_last_name_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(last_name_iew, Unset):
        json_last_name_iew = last_name_iew

    params["last_name__iew"] = json_last_name_iew

    json_last_name_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(last_name_isw, Unset):
        json_last_name_isw = last_name_isw

    params["last_name__isw"] = json_last_name_isw

    json_last_name_n: Union[Unset, list[str]] = UNSET
    if not isinstance(last_name_n, Unset):
        json_last_name_n = last_name_n

    params["last_name__n"] = json_last_name_n

    json_last_name_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(last_name_nic, Unset):
        json_last_name_nic = last_name_nic

    params["last_name__nic"] = json_last_name_nic

    json_last_name_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(last_name_nie, Unset):
        json_last_name_nie = last_name_nie

    params["last_name__nie"] = json_last_name_nie

    json_last_name_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(last_name_niew, Unset):
        json_last_name_niew = last_name_niew

    params["last_name__niew"] = json_last_name_niew

    json_last_name_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(last_name_nisw, Unset):
        json_last_name_nisw = last_name_nisw

    params["last_name__nisw"] = json_last_name_nisw

    params["limit"] = limit

    json_notification_group_id: Union[Unset, list[int]] = UNSET
    if not isinstance(notification_group_id, Unset):
        json_notification_group_id = notification_group_id

    params["notification_group_id"] = json_notification_group_id

    json_notification_group_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(notification_group_id_n, Unset):
        json_notification_group_id_n = notification_group_id_n

    params["notification_group_id__n"] = json_notification_group_id_n

    params["offset"] = offset

    params["ordering"] = ordering

    json_permission_id: Union[Unset, list[int]] = UNSET
    if not isinstance(permission_id, Unset):
        json_permission_id = permission_id

    params["permission_id"] = json_permission_id

    json_permission_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(permission_id_n, Unset):
        json_permission_id_n = permission_id_n

    params["permission_id__n"] = json_permission_id_n

    params["q"] = q

    json_username: Union[Unset, list[str]] = UNSET
    if not isinstance(username, Unset):
        json_username = username

    params["username"] = json_username

    params["username__empty"] = username_empty

    json_username_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(username_ic, Unset):
        json_username_ic = username_ic

    params["username__ic"] = json_username_ic

    json_username_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(username_ie, Unset):
        json_username_ie = username_ie

    params["username__ie"] = json_username_ie

    json_username_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(username_iew, Unset):
        json_username_iew = username_iew

    params["username__iew"] = json_username_iew

    json_username_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(username_isw, Unset):
        json_username_isw = username_isw

    params["username__isw"] = json_username_isw

    json_username_n: Union[Unset, list[str]] = UNSET
    if not isinstance(username_n, Unset):
        json_username_n = username_n

    params["username__n"] = json_username_n

    json_username_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(username_nic, Unset):
        json_username_nic = username_nic

    params["username__nic"] = json_username_nic

    json_username_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(username_nie, Unset):
        json_username_nie = username_nie

    params["username__nie"] = json_username_nie

    json_username_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(username_niew, Unset):
        json_username_niew = username_niew

    params["username__niew"] = json_username_niew

    json_username_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(username_nisw, Unset):
        json_username_nisw = username_nisw

    params["username__nisw"] = json_username_nisw

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/users/users/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedUserList]:
    if response.status_code == 200:
        response_200 = PaginatedUserList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedUserList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    date_joined: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_empty: Union[Unset, bool] = UNSET,
    date_joined_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_n: Union[Unset, list[datetime.datetime]] = UNSET,
    email: Union[Unset, list[str]] = UNSET,
    email_empty: Union[Unset, bool] = UNSET,
    email_ic: Union[Unset, list[str]] = UNSET,
    email_ie: Union[Unset, list[str]] = UNSET,
    email_iew: Union[Unset, list[str]] = UNSET,
    email_isw: Union[Unset, list[str]] = UNSET,
    email_n: Union[Unset, list[str]] = UNSET,
    email_nic: Union[Unset, list[str]] = UNSET,
    email_nie: Union[Unset, list[str]] = UNSET,
    email_niew: Union[Unset, list[str]] = UNSET,
    email_nisw: Union[Unset, list[str]] = UNSET,
    first_name: Union[Unset, list[str]] = UNSET,
    first_name_empty: Union[Unset, bool] = UNSET,
    first_name_ic: Union[Unset, list[str]] = UNSET,
    first_name_ie: Union[Unset, list[str]] = UNSET,
    first_name_iew: Union[Unset, list[str]] = UNSET,
    first_name_isw: Union[Unset, list[str]] = UNSET,
    first_name_n: Union[Unset, list[str]] = UNSET,
    first_name_nic: Union[Unset, list[str]] = UNSET,
    first_name_nie: Union[Unset, list[str]] = UNSET,
    first_name_niew: Union[Unset, list[str]] = UNSET,
    first_name_nisw: Union[Unset, list[str]] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[int]] = UNSET,
    group_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    is_staff: Union[Unset, bool] = UNSET,
    is_superuser: Union[Unset, bool] = UNSET,
    last_login: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_empty: Union[Unset, bool] = UNSET,
    last_login_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_n: Union[Unset, list[datetime.datetime]] = UNSET,
    last_name: Union[Unset, list[str]] = UNSET,
    last_name_empty: Union[Unset, bool] = UNSET,
    last_name_ic: Union[Unset, list[str]] = UNSET,
    last_name_ie: Union[Unset, list[str]] = UNSET,
    last_name_iew: Union[Unset, list[str]] = UNSET,
    last_name_isw: Union[Unset, list[str]] = UNSET,
    last_name_n: Union[Unset, list[str]] = UNSET,
    last_name_nic: Union[Unset, list[str]] = UNSET,
    last_name_nie: Union[Unset, list[str]] = UNSET,
    last_name_niew: Union[Unset, list[str]] = UNSET,
    last_name_nisw: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    notification_group_id: Union[Unset, list[int]] = UNSET,
    notification_group_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    permission_id: Union[Unset, list[int]] = UNSET,
    permission_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    username: Union[Unset, list[str]] = UNSET,
    username_empty: Union[Unset, bool] = UNSET,
    username_ic: Union[Unset, list[str]] = UNSET,
    username_ie: Union[Unset, list[str]] = UNSET,
    username_iew: Union[Unset, list[str]] = UNSET,
    username_isw: Union[Unset, list[str]] = UNSET,
    username_n: Union[Unset, list[str]] = UNSET,
    username_nic: Union[Unset, list[str]] = UNSET,
    username_nie: Union[Unset, list[str]] = UNSET,
    username_niew: Union[Unset, list[str]] = UNSET,
    username_nisw: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedUserList]:
    """Get a list of user objects.

    Args:
        date_joined (Union[Unset, list[datetime.datetime]]):
        date_joined_empty (Union[Unset, bool]):
        date_joined_gt (Union[Unset, list[datetime.datetime]]):
        date_joined_gte (Union[Unset, list[datetime.datetime]]):
        date_joined_lt (Union[Unset, list[datetime.datetime]]):
        date_joined_lte (Union[Unset, list[datetime.datetime]]):
        date_joined_n (Union[Unset, list[datetime.datetime]]):
        email (Union[Unset, list[str]]):
        email_empty (Union[Unset, bool]):
        email_ic (Union[Unset, list[str]]):
        email_ie (Union[Unset, list[str]]):
        email_iew (Union[Unset, list[str]]):
        email_isw (Union[Unset, list[str]]):
        email_n (Union[Unset, list[str]]):
        email_nic (Union[Unset, list[str]]):
        email_nie (Union[Unset, list[str]]):
        email_niew (Union[Unset, list[str]]):
        email_nisw (Union[Unset, list[str]]):
        first_name (Union[Unset, list[str]]):
        first_name_empty (Union[Unset, bool]):
        first_name_ic (Union[Unset, list[str]]):
        first_name_ie (Union[Unset, list[str]]):
        first_name_iew (Union[Unset, list[str]]):
        first_name_isw (Union[Unset, list[str]]):
        first_name_n (Union[Unset, list[str]]):
        first_name_nic (Union[Unset, list[str]]):
        first_name_nie (Union[Unset, list[str]]):
        first_name_niew (Union[Unset, list[str]]):
        first_name_nisw (Union[Unset, list[str]]):
        group (Union[Unset, list[str]]):
        group_n (Union[Unset, list[str]]):
        group_id (Union[Unset, list[int]]):
        group_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_active (Union[Unset, bool]):
        is_staff (Union[Unset, bool]):
        is_superuser (Union[Unset, bool]):
        last_login (Union[Unset, list[datetime.datetime]]):
        last_login_empty (Union[Unset, bool]):
        last_login_gt (Union[Unset, list[datetime.datetime]]):
        last_login_gte (Union[Unset, list[datetime.datetime]]):
        last_login_lt (Union[Unset, list[datetime.datetime]]):
        last_login_lte (Union[Unset, list[datetime.datetime]]):
        last_login_n (Union[Unset, list[datetime.datetime]]):
        last_name (Union[Unset, list[str]]):
        last_name_empty (Union[Unset, bool]):
        last_name_ic (Union[Unset, list[str]]):
        last_name_ie (Union[Unset, list[str]]):
        last_name_iew (Union[Unset, list[str]]):
        last_name_isw (Union[Unset, list[str]]):
        last_name_n (Union[Unset, list[str]]):
        last_name_nic (Union[Unset, list[str]]):
        last_name_nie (Union[Unset, list[str]]):
        last_name_niew (Union[Unset, list[str]]):
        last_name_nisw (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        notification_group_id (Union[Unset, list[int]]):
        notification_group_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        permission_id (Union[Unset, list[int]]):
        permission_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        username (Union[Unset, list[str]]):
        username_empty (Union[Unset, bool]):
        username_ic (Union[Unset, list[str]]):
        username_ie (Union[Unset, list[str]]):
        username_iew (Union[Unset, list[str]]):
        username_isw (Union[Unset, list[str]]):
        username_n (Union[Unset, list[str]]):
        username_nic (Union[Unset, list[str]]):
        username_nie (Union[Unset, list[str]]):
        username_niew (Union[Unset, list[str]]):
        username_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserList]
    """

    kwargs = _get_kwargs(
        date_joined=date_joined,
        date_joined_empty=date_joined_empty,
        date_joined_gt=date_joined_gt,
        date_joined_gte=date_joined_gte,
        date_joined_lt=date_joined_lt,
        date_joined_lte=date_joined_lte,
        date_joined_n=date_joined_n,
        email=email,
        email_empty=email_empty,
        email_ic=email_ic,
        email_ie=email_ie,
        email_iew=email_iew,
        email_isw=email_isw,
        email_n=email_n,
        email_nic=email_nic,
        email_nie=email_nie,
        email_niew=email_niew,
        email_nisw=email_nisw,
        first_name=first_name,
        first_name_empty=first_name_empty,
        first_name_ic=first_name_ic,
        first_name_ie=first_name_ie,
        first_name_iew=first_name_iew,
        first_name_isw=first_name_isw,
        first_name_n=first_name_n,
        first_name_nic=first_name_nic,
        first_name_nie=first_name_nie,
        first_name_niew=first_name_niew,
        first_name_nisw=first_name_nisw,
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
        is_active=is_active,
        is_staff=is_staff,
        is_superuser=is_superuser,
        last_login=last_login,
        last_login_empty=last_login_empty,
        last_login_gt=last_login_gt,
        last_login_gte=last_login_gte,
        last_login_lt=last_login_lt,
        last_login_lte=last_login_lte,
        last_login_n=last_login_n,
        last_name=last_name,
        last_name_empty=last_name_empty,
        last_name_ic=last_name_ic,
        last_name_ie=last_name_ie,
        last_name_iew=last_name_iew,
        last_name_isw=last_name_isw,
        last_name_n=last_name_n,
        last_name_nic=last_name_nic,
        last_name_nie=last_name_nie,
        last_name_niew=last_name_niew,
        last_name_nisw=last_name_nisw,
        limit=limit,
        notification_group_id=notification_group_id,
        notification_group_id_n=notification_group_id_n,
        offset=offset,
        ordering=ordering,
        permission_id=permission_id,
        permission_id_n=permission_id_n,
        q=q,
        username=username,
        username_empty=username_empty,
        username_ic=username_ic,
        username_ie=username_ie,
        username_iew=username_iew,
        username_isw=username_isw,
        username_n=username_n,
        username_nic=username_nic,
        username_nie=username_nie,
        username_niew=username_niew,
        username_nisw=username_nisw,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    date_joined: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_empty: Union[Unset, bool] = UNSET,
    date_joined_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_n: Union[Unset, list[datetime.datetime]] = UNSET,
    email: Union[Unset, list[str]] = UNSET,
    email_empty: Union[Unset, bool] = UNSET,
    email_ic: Union[Unset, list[str]] = UNSET,
    email_ie: Union[Unset, list[str]] = UNSET,
    email_iew: Union[Unset, list[str]] = UNSET,
    email_isw: Union[Unset, list[str]] = UNSET,
    email_n: Union[Unset, list[str]] = UNSET,
    email_nic: Union[Unset, list[str]] = UNSET,
    email_nie: Union[Unset, list[str]] = UNSET,
    email_niew: Union[Unset, list[str]] = UNSET,
    email_nisw: Union[Unset, list[str]] = UNSET,
    first_name: Union[Unset, list[str]] = UNSET,
    first_name_empty: Union[Unset, bool] = UNSET,
    first_name_ic: Union[Unset, list[str]] = UNSET,
    first_name_ie: Union[Unset, list[str]] = UNSET,
    first_name_iew: Union[Unset, list[str]] = UNSET,
    first_name_isw: Union[Unset, list[str]] = UNSET,
    first_name_n: Union[Unset, list[str]] = UNSET,
    first_name_nic: Union[Unset, list[str]] = UNSET,
    first_name_nie: Union[Unset, list[str]] = UNSET,
    first_name_niew: Union[Unset, list[str]] = UNSET,
    first_name_nisw: Union[Unset, list[str]] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[int]] = UNSET,
    group_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    is_staff: Union[Unset, bool] = UNSET,
    is_superuser: Union[Unset, bool] = UNSET,
    last_login: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_empty: Union[Unset, bool] = UNSET,
    last_login_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_n: Union[Unset, list[datetime.datetime]] = UNSET,
    last_name: Union[Unset, list[str]] = UNSET,
    last_name_empty: Union[Unset, bool] = UNSET,
    last_name_ic: Union[Unset, list[str]] = UNSET,
    last_name_ie: Union[Unset, list[str]] = UNSET,
    last_name_iew: Union[Unset, list[str]] = UNSET,
    last_name_isw: Union[Unset, list[str]] = UNSET,
    last_name_n: Union[Unset, list[str]] = UNSET,
    last_name_nic: Union[Unset, list[str]] = UNSET,
    last_name_nie: Union[Unset, list[str]] = UNSET,
    last_name_niew: Union[Unset, list[str]] = UNSET,
    last_name_nisw: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    notification_group_id: Union[Unset, list[int]] = UNSET,
    notification_group_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    permission_id: Union[Unset, list[int]] = UNSET,
    permission_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    username: Union[Unset, list[str]] = UNSET,
    username_empty: Union[Unset, bool] = UNSET,
    username_ic: Union[Unset, list[str]] = UNSET,
    username_ie: Union[Unset, list[str]] = UNSET,
    username_iew: Union[Unset, list[str]] = UNSET,
    username_isw: Union[Unset, list[str]] = UNSET,
    username_n: Union[Unset, list[str]] = UNSET,
    username_nic: Union[Unset, list[str]] = UNSET,
    username_nie: Union[Unset, list[str]] = UNSET,
    username_niew: Union[Unset, list[str]] = UNSET,
    username_nisw: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedUserList]:
    """Get a list of user objects.

    Args:
        date_joined (Union[Unset, list[datetime.datetime]]):
        date_joined_empty (Union[Unset, bool]):
        date_joined_gt (Union[Unset, list[datetime.datetime]]):
        date_joined_gte (Union[Unset, list[datetime.datetime]]):
        date_joined_lt (Union[Unset, list[datetime.datetime]]):
        date_joined_lte (Union[Unset, list[datetime.datetime]]):
        date_joined_n (Union[Unset, list[datetime.datetime]]):
        email (Union[Unset, list[str]]):
        email_empty (Union[Unset, bool]):
        email_ic (Union[Unset, list[str]]):
        email_ie (Union[Unset, list[str]]):
        email_iew (Union[Unset, list[str]]):
        email_isw (Union[Unset, list[str]]):
        email_n (Union[Unset, list[str]]):
        email_nic (Union[Unset, list[str]]):
        email_nie (Union[Unset, list[str]]):
        email_niew (Union[Unset, list[str]]):
        email_nisw (Union[Unset, list[str]]):
        first_name (Union[Unset, list[str]]):
        first_name_empty (Union[Unset, bool]):
        first_name_ic (Union[Unset, list[str]]):
        first_name_ie (Union[Unset, list[str]]):
        first_name_iew (Union[Unset, list[str]]):
        first_name_isw (Union[Unset, list[str]]):
        first_name_n (Union[Unset, list[str]]):
        first_name_nic (Union[Unset, list[str]]):
        first_name_nie (Union[Unset, list[str]]):
        first_name_niew (Union[Unset, list[str]]):
        first_name_nisw (Union[Unset, list[str]]):
        group (Union[Unset, list[str]]):
        group_n (Union[Unset, list[str]]):
        group_id (Union[Unset, list[int]]):
        group_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_active (Union[Unset, bool]):
        is_staff (Union[Unset, bool]):
        is_superuser (Union[Unset, bool]):
        last_login (Union[Unset, list[datetime.datetime]]):
        last_login_empty (Union[Unset, bool]):
        last_login_gt (Union[Unset, list[datetime.datetime]]):
        last_login_gte (Union[Unset, list[datetime.datetime]]):
        last_login_lt (Union[Unset, list[datetime.datetime]]):
        last_login_lte (Union[Unset, list[datetime.datetime]]):
        last_login_n (Union[Unset, list[datetime.datetime]]):
        last_name (Union[Unset, list[str]]):
        last_name_empty (Union[Unset, bool]):
        last_name_ic (Union[Unset, list[str]]):
        last_name_ie (Union[Unset, list[str]]):
        last_name_iew (Union[Unset, list[str]]):
        last_name_isw (Union[Unset, list[str]]):
        last_name_n (Union[Unset, list[str]]):
        last_name_nic (Union[Unset, list[str]]):
        last_name_nie (Union[Unset, list[str]]):
        last_name_niew (Union[Unset, list[str]]):
        last_name_nisw (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        notification_group_id (Union[Unset, list[int]]):
        notification_group_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        permission_id (Union[Unset, list[int]]):
        permission_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        username (Union[Unset, list[str]]):
        username_empty (Union[Unset, bool]):
        username_ic (Union[Unset, list[str]]):
        username_ie (Union[Unset, list[str]]):
        username_iew (Union[Unset, list[str]]):
        username_isw (Union[Unset, list[str]]):
        username_n (Union[Unset, list[str]]):
        username_nic (Union[Unset, list[str]]):
        username_nie (Union[Unset, list[str]]):
        username_niew (Union[Unset, list[str]]):
        username_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserList
    """

    return sync_detailed(
        client=client,
        date_joined=date_joined,
        date_joined_empty=date_joined_empty,
        date_joined_gt=date_joined_gt,
        date_joined_gte=date_joined_gte,
        date_joined_lt=date_joined_lt,
        date_joined_lte=date_joined_lte,
        date_joined_n=date_joined_n,
        email=email,
        email_empty=email_empty,
        email_ic=email_ic,
        email_ie=email_ie,
        email_iew=email_iew,
        email_isw=email_isw,
        email_n=email_n,
        email_nic=email_nic,
        email_nie=email_nie,
        email_niew=email_niew,
        email_nisw=email_nisw,
        first_name=first_name,
        first_name_empty=first_name_empty,
        first_name_ic=first_name_ic,
        first_name_ie=first_name_ie,
        first_name_iew=first_name_iew,
        first_name_isw=first_name_isw,
        first_name_n=first_name_n,
        first_name_nic=first_name_nic,
        first_name_nie=first_name_nie,
        first_name_niew=first_name_niew,
        first_name_nisw=first_name_nisw,
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
        is_active=is_active,
        is_staff=is_staff,
        is_superuser=is_superuser,
        last_login=last_login,
        last_login_empty=last_login_empty,
        last_login_gt=last_login_gt,
        last_login_gte=last_login_gte,
        last_login_lt=last_login_lt,
        last_login_lte=last_login_lte,
        last_login_n=last_login_n,
        last_name=last_name,
        last_name_empty=last_name_empty,
        last_name_ic=last_name_ic,
        last_name_ie=last_name_ie,
        last_name_iew=last_name_iew,
        last_name_isw=last_name_isw,
        last_name_n=last_name_n,
        last_name_nic=last_name_nic,
        last_name_nie=last_name_nie,
        last_name_niew=last_name_niew,
        last_name_nisw=last_name_nisw,
        limit=limit,
        notification_group_id=notification_group_id,
        notification_group_id_n=notification_group_id_n,
        offset=offset,
        ordering=ordering,
        permission_id=permission_id,
        permission_id_n=permission_id_n,
        q=q,
        username=username,
        username_empty=username_empty,
        username_ic=username_ic,
        username_ie=username_ie,
        username_iew=username_iew,
        username_isw=username_isw,
        username_n=username_n,
        username_nic=username_nic,
        username_nie=username_nie,
        username_niew=username_niew,
        username_nisw=username_nisw,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    date_joined: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_empty: Union[Unset, bool] = UNSET,
    date_joined_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_n: Union[Unset, list[datetime.datetime]] = UNSET,
    email: Union[Unset, list[str]] = UNSET,
    email_empty: Union[Unset, bool] = UNSET,
    email_ic: Union[Unset, list[str]] = UNSET,
    email_ie: Union[Unset, list[str]] = UNSET,
    email_iew: Union[Unset, list[str]] = UNSET,
    email_isw: Union[Unset, list[str]] = UNSET,
    email_n: Union[Unset, list[str]] = UNSET,
    email_nic: Union[Unset, list[str]] = UNSET,
    email_nie: Union[Unset, list[str]] = UNSET,
    email_niew: Union[Unset, list[str]] = UNSET,
    email_nisw: Union[Unset, list[str]] = UNSET,
    first_name: Union[Unset, list[str]] = UNSET,
    first_name_empty: Union[Unset, bool] = UNSET,
    first_name_ic: Union[Unset, list[str]] = UNSET,
    first_name_ie: Union[Unset, list[str]] = UNSET,
    first_name_iew: Union[Unset, list[str]] = UNSET,
    first_name_isw: Union[Unset, list[str]] = UNSET,
    first_name_n: Union[Unset, list[str]] = UNSET,
    first_name_nic: Union[Unset, list[str]] = UNSET,
    first_name_nie: Union[Unset, list[str]] = UNSET,
    first_name_niew: Union[Unset, list[str]] = UNSET,
    first_name_nisw: Union[Unset, list[str]] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[int]] = UNSET,
    group_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    is_staff: Union[Unset, bool] = UNSET,
    is_superuser: Union[Unset, bool] = UNSET,
    last_login: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_empty: Union[Unset, bool] = UNSET,
    last_login_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_n: Union[Unset, list[datetime.datetime]] = UNSET,
    last_name: Union[Unset, list[str]] = UNSET,
    last_name_empty: Union[Unset, bool] = UNSET,
    last_name_ic: Union[Unset, list[str]] = UNSET,
    last_name_ie: Union[Unset, list[str]] = UNSET,
    last_name_iew: Union[Unset, list[str]] = UNSET,
    last_name_isw: Union[Unset, list[str]] = UNSET,
    last_name_n: Union[Unset, list[str]] = UNSET,
    last_name_nic: Union[Unset, list[str]] = UNSET,
    last_name_nie: Union[Unset, list[str]] = UNSET,
    last_name_niew: Union[Unset, list[str]] = UNSET,
    last_name_nisw: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    notification_group_id: Union[Unset, list[int]] = UNSET,
    notification_group_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    permission_id: Union[Unset, list[int]] = UNSET,
    permission_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    username: Union[Unset, list[str]] = UNSET,
    username_empty: Union[Unset, bool] = UNSET,
    username_ic: Union[Unset, list[str]] = UNSET,
    username_ie: Union[Unset, list[str]] = UNSET,
    username_iew: Union[Unset, list[str]] = UNSET,
    username_isw: Union[Unset, list[str]] = UNSET,
    username_n: Union[Unset, list[str]] = UNSET,
    username_nic: Union[Unset, list[str]] = UNSET,
    username_nie: Union[Unset, list[str]] = UNSET,
    username_niew: Union[Unset, list[str]] = UNSET,
    username_nisw: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedUserList]:
    """Get a list of user objects.

    Args:
        date_joined (Union[Unset, list[datetime.datetime]]):
        date_joined_empty (Union[Unset, bool]):
        date_joined_gt (Union[Unset, list[datetime.datetime]]):
        date_joined_gte (Union[Unset, list[datetime.datetime]]):
        date_joined_lt (Union[Unset, list[datetime.datetime]]):
        date_joined_lte (Union[Unset, list[datetime.datetime]]):
        date_joined_n (Union[Unset, list[datetime.datetime]]):
        email (Union[Unset, list[str]]):
        email_empty (Union[Unset, bool]):
        email_ic (Union[Unset, list[str]]):
        email_ie (Union[Unset, list[str]]):
        email_iew (Union[Unset, list[str]]):
        email_isw (Union[Unset, list[str]]):
        email_n (Union[Unset, list[str]]):
        email_nic (Union[Unset, list[str]]):
        email_nie (Union[Unset, list[str]]):
        email_niew (Union[Unset, list[str]]):
        email_nisw (Union[Unset, list[str]]):
        first_name (Union[Unset, list[str]]):
        first_name_empty (Union[Unset, bool]):
        first_name_ic (Union[Unset, list[str]]):
        first_name_ie (Union[Unset, list[str]]):
        first_name_iew (Union[Unset, list[str]]):
        first_name_isw (Union[Unset, list[str]]):
        first_name_n (Union[Unset, list[str]]):
        first_name_nic (Union[Unset, list[str]]):
        first_name_nie (Union[Unset, list[str]]):
        first_name_niew (Union[Unset, list[str]]):
        first_name_nisw (Union[Unset, list[str]]):
        group (Union[Unset, list[str]]):
        group_n (Union[Unset, list[str]]):
        group_id (Union[Unset, list[int]]):
        group_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_active (Union[Unset, bool]):
        is_staff (Union[Unset, bool]):
        is_superuser (Union[Unset, bool]):
        last_login (Union[Unset, list[datetime.datetime]]):
        last_login_empty (Union[Unset, bool]):
        last_login_gt (Union[Unset, list[datetime.datetime]]):
        last_login_gte (Union[Unset, list[datetime.datetime]]):
        last_login_lt (Union[Unset, list[datetime.datetime]]):
        last_login_lte (Union[Unset, list[datetime.datetime]]):
        last_login_n (Union[Unset, list[datetime.datetime]]):
        last_name (Union[Unset, list[str]]):
        last_name_empty (Union[Unset, bool]):
        last_name_ic (Union[Unset, list[str]]):
        last_name_ie (Union[Unset, list[str]]):
        last_name_iew (Union[Unset, list[str]]):
        last_name_isw (Union[Unset, list[str]]):
        last_name_n (Union[Unset, list[str]]):
        last_name_nic (Union[Unset, list[str]]):
        last_name_nie (Union[Unset, list[str]]):
        last_name_niew (Union[Unset, list[str]]):
        last_name_nisw (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        notification_group_id (Union[Unset, list[int]]):
        notification_group_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        permission_id (Union[Unset, list[int]]):
        permission_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        username (Union[Unset, list[str]]):
        username_empty (Union[Unset, bool]):
        username_ic (Union[Unset, list[str]]):
        username_ie (Union[Unset, list[str]]):
        username_iew (Union[Unset, list[str]]):
        username_isw (Union[Unset, list[str]]):
        username_n (Union[Unset, list[str]]):
        username_nic (Union[Unset, list[str]]):
        username_nie (Union[Unset, list[str]]):
        username_niew (Union[Unset, list[str]]):
        username_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserList]
    """

    kwargs = _get_kwargs(
        date_joined=date_joined,
        date_joined_empty=date_joined_empty,
        date_joined_gt=date_joined_gt,
        date_joined_gte=date_joined_gte,
        date_joined_lt=date_joined_lt,
        date_joined_lte=date_joined_lte,
        date_joined_n=date_joined_n,
        email=email,
        email_empty=email_empty,
        email_ic=email_ic,
        email_ie=email_ie,
        email_iew=email_iew,
        email_isw=email_isw,
        email_n=email_n,
        email_nic=email_nic,
        email_nie=email_nie,
        email_niew=email_niew,
        email_nisw=email_nisw,
        first_name=first_name,
        first_name_empty=first_name_empty,
        first_name_ic=first_name_ic,
        first_name_ie=first_name_ie,
        first_name_iew=first_name_iew,
        first_name_isw=first_name_isw,
        first_name_n=first_name_n,
        first_name_nic=first_name_nic,
        first_name_nie=first_name_nie,
        first_name_niew=first_name_niew,
        first_name_nisw=first_name_nisw,
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
        is_active=is_active,
        is_staff=is_staff,
        is_superuser=is_superuser,
        last_login=last_login,
        last_login_empty=last_login_empty,
        last_login_gt=last_login_gt,
        last_login_gte=last_login_gte,
        last_login_lt=last_login_lt,
        last_login_lte=last_login_lte,
        last_login_n=last_login_n,
        last_name=last_name,
        last_name_empty=last_name_empty,
        last_name_ic=last_name_ic,
        last_name_ie=last_name_ie,
        last_name_iew=last_name_iew,
        last_name_isw=last_name_isw,
        last_name_n=last_name_n,
        last_name_nic=last_name_nic,
        last_name_nie=last_name_nie,
        last_name_niew=last_name_niew,
        last_name_nisw=last_name_nisw,
        limit=limit,
        notification_group_id=notification_group_id,
        notification_group_id_n=notification_group_id_n,
        offset=offset,
        ordering=ordering,
        permission_id=permission_id,
        permission_id_n=permission_id_n,
        q=q,
        username=username,
        username_empty=username_empty,
        username_ic=username_ic,
        username_ie=username_ie,
        username_iew=username_iew,
        username_isw=username_isw,
        username_n=username_n,
        username_nic=username_nic,
        username_nie=username_nie,
        username_niew=username_niew,
        username_nisw=username_nisw,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    date_joined: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_empty: Union[Unset, bool] = UNSET,
    date_joined_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    date_joined_n: Union[Unset, list[datetime.datetime]] = UNSET,
    email: Union[Unset, list[str]] = UNSET,
    email_empty: Union[Unset, bool] = UNSET,
    email_ic: Union[Unset, list[str]] = UNSET,
    email_ie: Union[Unset, list[str]] = UNSET,
    email_iew: Union[Unset, list[str]] = UNSET,
    email_isw: Union[Unset, list[str]] = UNSET,
    email_n: Union[Unset, list[str]] = UNSET,
    email_nic: Union[Unset, list[str]] = UNSET,
    email_nie: Union[Unset, list[str]] = UNSET,
    email_niew: Union[Unset, list[str]] = UNSET,
    email_nisw: Union[Unset, list[str]] = UNSET,
    first_name: Union[Unset, list[str]] = UNSET,
    first_name_empty: Union[Unset, bool] = UNSET,
    first_name_ic: Union[Unset, list[str]] = UNSET,
    first_name_ie: Union[Unset, list[str]] = UNSET,
    first_name_iew: Union[Unset, list[str]] = UNSET,
    first_name_isw: Union[Unset, list[str]] = UNSET,
    first_name_n: Union[Unset, list[str]] = UNSET,
    first_name_nic: Union[Unset, list[str]] = UNSET,
    first_name_nie: Union[Unset, list[str]] = UNSET,
    first_name_niew: Union[Unset, list[str]] = UNSET,
    first_name_nisw: Union[Unset, list[str]] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[int]] = UNSET,
    group_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    is_staff: Union[Unset, bool] = UNSET,
    is_superuser: Union[Unset, bool] = UNSET,
    last_login: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_empty: Union[Unset, bool] = UNSET,
    last_login_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_login_n: Union[Unset, list[datetime.datetime]] = UNSET,
    last_name: Union[Unset, list[str]] = UNSET,
    last_name_empty: Union[Unset, bool] = UNSET,
    last_name_ic: Union[Unset, list[str]] = UNSET,
    last_name_ie: Union[Unset, list[str]] = UNSET,
    last_name_iew: Union[Unset, list[str]] = UNSET,
    last_name_isw: Union[Unset, list[str]] = UNSET,
    last_name_n: Union[Unset, list[str]] = UNSET,
    last_name_nic: Union[Unset, list[str]] = UNSET,
    last_name_nie: Union[Unset, list[str]] = UNSET,
    last_name_niew: Union[Unset, list[str]] = UNSET,
    last_name_nisw: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    notification_group_id: Union[Unset, list[int]] = UNSET,
    notification_group_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    permission_id: Union[Unset, list[int]] = UNSET,
    permission_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    username: Union[Unset, list[str]] = UNSET,
    username_empty: Union[Unset, bool] = UNSET,
    username_ic: Union[Unset, list[str]] = UNSET,
    username_ie: Union[Unset, list[str]] = UNSET,
    username_iew: Union[Unset, list[str]] = UNSET,
    username_isw: Union[Unset, list[str]] = UNSET,
    username_n: Union[Unset, list[str]] = UNSET,
    username_nic: Union[Unset, list[str]] = UNSET,
    username_nie: Union[Unset, list[str]] = UNSET,
    username_niew: Union[Unset, list[str]] = UNSET,
    username_nisw: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedUserList]:
    """Get a list of user objects.

    Args:
        date_joined (Union[Unset, list[datetime.datetime]]):
        date_joined_empty (Union[Unset, bool]):
        date_joined_gt (Union[Unset, list[datetime.datetime]]):
        date_joined_gte (Union[Unset, list[datetime.datetime]]):
        date_joined_lt (Union[Unset, list[datetime.datetime]]):
        date_joined_lte (Union[Unset, list[datetime.datetime]]):
        date_joined_n (Union[Unset, list[datetime.datetime]]):
        email (Union[Unset, list[str]]):
        email_empty (Union[Unset, bool]):
        email_ic (Union[Unset, list[str]]):
        email_ie (Union[Unset, list[str]]):
        email_iew (Union[Unset, list[str]]):
        email_isw (Union[Unset, list[str]]):
        email_n (Union[Unset, list[str]]):
        email_nic (Union[Unset, list[str]]):
        email_nie (Union[Unset, list[str]]):
        email_niew (Union[Unset, list[str]]):
        email_nisw (Union[Unset, list[str]]):
        first_name (Union[Unset, list[str]]):
        first_name_empty (Union[Unset, bool]):
        first_name_ic (Union[Unset, list[str]]):
        first_name_ie (Union[Unset, list[str]]):
        first_name_iew (Union[Unset, list[str]]):
        first_name_isw (Union[Unset, list[str]]):
        first_name_n (Union[Unset, list[str]]):
        first_name_nic (Union[Unset, list[str]]):
        first_name_nie (Union[Unset, list[str]]):
        first_name_niew (Union[Unset, list[str]]):
        first_name_nisw (Union[Unset, list[str]]):
        group (Union[Unset, list[str]]):
        group_n (Union[Unset, list[str]]):
        group_id (Union[Unset, list[int]]):
        group_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_active (Union[Unset, bool]):
        is_staff (Union[Unset, bool]):
        is_superuser (Union[Unset, bool]):
        last_login (Union[Unset, list[datetime.datetime]]):
        last_login_empty (Union[Unset, bool]):
        last_login_gt (Union[Unset, list[datetime.datetime]]):
        last_login_gte (Union[Unset, list[datetime.datetime]]):
        last_login_lt (Union[Unset, list[datetime.datetime]]):
        last_login_lte (Union[Unset, list[datetime.datetime]]):
        last_login_n (Union[Unset, list[datetime.datetime]]):
        last_name (Union[Unset, list[str]]):
        last_name_empty (Union[Unset, bool]):
        last_name_ic (Union[Unset, list[str]]):
        last_name_ie (Union[Unset, list[str]]):
        last_name_iew (Union[Unset, list[str]]):
        last_name_isw (Union[Unset, list[str]]):
        last_name_n (Union[Unset, list[str]]):
        last_name_nic (Union[Unset, list[str]]):
        last_name_nie (Union[Unset, list[str]]):
        last_name_niew (Union[Unset, list[str]]):
        last_name_nisw (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        notification_group_id (Union[Unset, list[int]]):
        notification_group_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        permission_id (Union[Unset, list[int]]):
        permission_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        username (Union[Unset, list[str]]):
        username_empty (Union[Unset, bool]):
        username_ic (Union[Unset, list[str]]):
        username_ie (Union[Unset, list[str]]):
        username_iew (Union[Unset, list[str]]):
        username_isw (Union[Unset, list[str]]):
        username_n (Union[Unset, list[str]]):
        username_nic (Union[Unset, list[str]]):
        username_nie (Union[Unset, list[str]]):
        username_niew (Union[Unset, list[str]]):
        username_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserList
    """

    return (
        await asyncio_detailed(
            client=client,
            date_joined=date_joined,
            date_joined_empty=date_joined_empty,
            date_joined_gt=date_joined_gt,
            date_joined_gte=date_joined_gte,
            date_joined_lt=date_joined_lt,
            date_joined_lte=date_joined_lte,
            date_joined_n=date_joined_n,
            email=email,
            email_empty=email_empty,
            email_ic=email_ic,
            email_ie=email_ie,
            email_iew=email_iew,
            email_isw=email_isw,
            email_n=email_n,
            email_nic=email_nic,
            email_nie=email_nie,
            email_niew=email_niew,
            email_nisw=email_nisw,
            first_name=first_name,
            first_name_empty=first_name_empty,
            first_name_ic=first_name_ic,
            first_name_ie=first_name_ie,
            first_name_iew=first_name_iew,
            first_name_isw=first_name_isw,
            first_name_n=first_name_n,
            first_name_nic=first_name_nic,
            first_name_nie=first_name_nie,
            first_name_niew=first_name_niew,
            first_name_nisw=first_name_nisw,
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
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=last_login,
            last_login_empty=last_login_empty,
            last_login_gt=last_login_gt,
            last_login_gte=last_login_gte,
            last_login_lt=last_login_lt,
            last_login_lte=last_login_lte,
            last_login_n=last_login_n,
            last_name=last_name,
            last_name_empty=last_name_empty,
            last_name_ic=last_name_ic,
            last_name_ie=last_name_ie,
            last_name_iew=last_name_iew,
            last_name_isw=last_name_isw,
            last_name_n=last_name_n,
            last_name_nic=last_name_nic,
            last_name_nie=last_name_nie,
            last_name_niew=last_name_niew,
            last_name_nisw=last_name_nisw,
            limit=limit,
            notification_group_id=notification_group_id,
            notification_group_id_n=notification_group_id_n,
            offset=offset,
            ordering=ordering,
            permission_id=permission_id,
            permission_id_n=permission_id_n,
            q=q,
            username=username,
            username_empty=username_empty,
            username_ic=username_ic,
            username_ie=username_ie,
            username_iew=username_iew,
            username_isw=username_isw,
            username_n=username_n,
            username_nic=username_nic,
            username_nie=username_nie,
            username_niew=username_niew,
            username_nisw=username_nisw,
        )
    ).parsed
