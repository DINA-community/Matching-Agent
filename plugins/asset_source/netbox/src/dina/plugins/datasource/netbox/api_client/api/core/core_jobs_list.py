import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_job_list import PaginatedJobList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    completed: Union[Unset, datetime.datetime] = UNSET,
    completed_after: Union[Unset, datetime.datetime] = UNSET,
    completed_before: Union[Unset, datetime.datetime] = UNSET,
    created: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interval: Union[Unset, list[int]] = UNSET,
    interval_empty: Union[Unset, bool] = UNSET,
    interval_gt: Union[Unset, list[int]] = UNSET,
    interval_gte: Union[Unset, list[int]] = UNSET,
    interval_lt: Union[Unset, list[int]] = UNSET,
    interval_lte: Union[Unset, list[int]] = UNSET,
    interval_n: Union[Unset, list[int]] = UNSET,
    job_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
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
    object_id: Union[Unset, list[int]] = UNSET,
    object_id_empty: Union[Unset, bool] = UNSET,
    object_id_gt: Union[Unset, list[int]] = UNSET,
    object_id_gte: Union[Unset, list[int]] = UNSET,
    object_id_lt: Union[Unset, list[int]] = UNSET,
    object_id_lte: Union[Unset, list[int]] = UNSET,
    object_id_n: Union[Unset, list[int]] = UNSET,
    object_type: Union[Unset, int] = UNSET,
    object_type_n: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    scheduled: Union[Unset, datetime.datetime] = UNSET,
    scheduled_after: Union[Unset, datetime.datetime] = UNSET,
    scheduled_before: Union[Unset, datetime.datetime] = UNSET,
    started: Union[Unset, datetime.datetime] = UNSET,
    started_after: Union[Unset, datetime.datetime] = UNSET,
    started_before: Union[Unset, datetime.datetime] = UNSET,
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
    user: Union[Unset, int] = UNSET,
    user_n: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_completed: Union[Unset, str] = UNSET
    if not isinstance(completed, Unset):
        json_completed = completed.isoformat()
    params["completed"] = json_completed

    json_completed_after: Union[Unset, str] = UNSET
    if not isinstance(completed_after, Unset):
        json_completed_after = completed_after.isoformat()
    params["completed__after"] = json_completed_after

    json_completed_before: Union[Unset, str] = UNSET
    if not isinstance(completed_before, Unset):
        json_completed_before = completed_before.isoformat()
    params["completed__before"] = json_completed_before

    json_created: Union[Unset, str] = UNSET
    if not isinstance(created, Unset):
        json_created = created.isoformat()
    params["created"] = json_created

    json_created_after: Union[Unset, str] = UNSET
    if not isinstance(created_after, Unset):
        json_created_after = created_after.isoformat()
    params["created__after"] = json_created_after

    json_created_before: Union[Unset, str] = UNSET
    if not isinstance(created_before, Unset):
        json_created_before = created_before.isoformat()
    params["created__before"] = json_created_before

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

    json_interval: Union[Unset, list[int]] = UNSET
    if not isinstance(interval, Unset):
        json_interval = interval

    params["interval"] = json_interval

    params["interval__empty"] = interval_empty

    json_interval_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(interval_gt, Unset):
        json_interval_gt = interval_gt

    params["interval__gt"] = json_interval_gt

    json_interval_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(interval_gte, Unset):
        json_interval_gte = interval_gte

    params["interval__gte"] = json_interval_gte

    json_interval_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(interval_lt, Unset):
        json_interval_lt = interval_lt

    params["interval__lt"] = json_interval_lt

    json_interval_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(interval_lte, Unset):
        json_interval_lte = interval_lte

    params["interval__lte"] = json_interval_lte

    json_interval_n: Union[Unset, list[int]] = UNSET
    if not isinstance(interval_n, Unset):
        json_interval_n = interval_n

    params["interval__n"] = json_interval_n

    json_job_id: Union[Unset, str] = UNSET
    if not isinstance(job_id, Unset):
        json_job_id = str(job_id)
    params["job_id"] = json_job_id

    params["limit"] = limit

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

    json_object_id: Union[Unset, list[int]] = UNSET
    if not isinstance(object_id, Unset):
        json_object_id = object_id

    params["object_id"] = json_object_id

    params["object_id__empty"] = object_id_empty

    json_object_id_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(object_id_gt, Unset):
        json_object_id_gt = object_id_gt

    params["object_id__gt"] = json_object_id_gt

    json_object_id_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(object_id_gte, Unset):
        json_object_id_gte = object_id_gte

    params["object_id__gte"] = json_object_id_gte

    json_object_id_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(object_id_lt, Unset):
        json_object_id_lt = object_id_lt

    params["object_id__lt"] = json_object_id_lt

    json_object_id_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(object_id_lte, Unset):
        json_object_id_lte = object_id_lte

    params["object_id__lte"] = json_object_id_lte

    json_object_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(object_id_n, Unset):
        json_object_id_n = object_id_n

    params["object_id__n"] = json_object_id_n

    params["object_type"] = object_type

    params["object_type__n"] = object_type_n

    params["offset"] = offset

    params["ordering"] = ordering

    params["q"] = q

    json_scheduled: Union[Unset, str] = UNSET
    if not isinstance(scheduled, Unset):
        json_scheduled = scheduled.isoformat()
    params["scheduled"] = json_scheduled

    json_scheduled_after: Union[Unset, str] = UNSET
    if not isinstance(scheduled_after, Unset):
        json_scheduled_after = scheduled_after.isoformat()
    params["scheduled__after"] = json_scheduled_after

    json_scheduled_before: Union[Unset, str] = UNSET
    if not isinstance(scheduled_before, Unset):
        json_scheduled_before = scheduled_before.isoformat()
    params["scheduled__before"] = json_scheduled_before

    json_started: Union[Unset, str] = UNSET
    if not isinstance(started, Unset):
        json_started = started.isoformat()
    params["started"] = json_started

    json_started_after: Union[Unset, str] = UNSET
    if not isinstance(started_after, Unset):
        json_started_after = started_after.isoformat()
    params["started__after"] = json_started_after

    json_started_before: Union[Unset, str] = UNSET
    if not isinstance(started_before, Unset):
        json_started_before = started_before.isoformat()
    params["started__before"] = json_started_before

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

    params["user"] = user

    params["user__n"] = user_n

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/jobs/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedJobList]:
    if response.status_code == 200:
        response_200 = PaginatedJobList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedJobList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    completed: Union[Unset, datetime.datetime] = UNSET,
    completed_after: Union[Unset, datetime.datetime] = UNSET,
    completed_before: Union[Unset, datetime.datetime] = UNSET,
    created: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interval: Union[Unset, list[int]] = UNSET,
    interval_empty: Union[Unset, bool] = UNSET,
    interval_gt: Union[Unset, list[int]] = UNSET,
    interval_gte: Union[Unset, list[int]] = UNSET,
    interval_lt: Union[Unset, list[int]] = UNSET,
    interval_lte: Union[Unset, list[int]] = UNSET,
    interval_n: Union[Unset, list[int]] = UNSET,
    job_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
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
    object_id: Union[Unset, list[int]] = UNSET,
    object_id_empty: Union[Unset, bool] = UNSET,
    object_id_gt: Union[Unset, list[int]] = UNSET,
    object_id_gte: Union[Unset, list[int]] = UNSET,
    object_id_lt: Union[Unset, list[int]] = UNSET,
    object_id_lte: Union[Unset, list[int]] = UNSET,
    object_id_n: Union[Unset, list[int]] = UNSET,
    object_type: Union[Unset, int] = UNSET,
    object_type_n: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    scheduled: Union[Unset, datetime.datetime] = UNSET,
    scheduled_after: Union[Unset, datetime.datetime] = UNSET,
    scheduled_before: Union[Unset, datetime.datetime] = UNSET,
    started: Union[Unset, datetime.datetime] = UNSET,
    started_after: Union[Unset, datetime.datetime] = UNSET,
    started_before: Union[Unset, datetime.datetime] = UNSET,
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
    user: Union[Unset, int] = UNSET,
    user_n: Union[Unset, int] = UNSET,
) -> Response[PaginatedJobList]:
    """Retrieve a list of job results

    Args:
        completed (Union[Unset, datetime.datetime]):
        completed_after (Union[Unset, datetime.datetime]):
        completed_before (Union[Unset, datetime.datetime]):
        created (Union[Unset, datetime.datetime]):
        created_after (Union[Unset, datetime.datetime]):
        created_before (Union[Unset, datetime.datetime]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interval (Union[Unset, list[int]]):
        interval_empty (Union[Unset, bool]):
        interval_gt (Union[Unset, list[int]]):
        interval_gte (Union[Unset, list[int]]):
        interval_lt (Union[Unset, list[int]]):
        interval_lte (Union[Unset, list[int]]):
        interval_n (Union[Unset, list[int]]):
        job_id (Union[Unset, UUID]):
        limit (Union[Unset, int]):
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
        object_id (Union[Unset, list[int]]):
        object_id_empty (Union[Unset, bool]):
        object_id_gt (Union[Unset, list[int]]):
        object_id_gte (Union[Unset, list[int]]):
        object_id_lt (Union[Unset, list[int]]):
        object_id_lte (Union[Unset, list[int]]):
        object_id_n (Union[Unset, list[int]]):
        object_type (Union[Unset, int]):
        object_type_n (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        scheduled (Union[Unset, datetime.datetime]):
        scheduled_after (Union[Unset, datetime.datetime]):
        scheduled_before (Union[Unset, datetime.datetime]):
        started (Union[Unset, datetime.datetime]):
        started_after (Union[Unset, datetime.datetime]):
        started_before (Union[Unset, datetime.datetime]):
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
        user (Union[Unset, int]):
        user_n (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedJobList]
    """

    kwargs = _get_kwargs(
        completed=completed,
        completed_after=completed_after,
        completed_before=completed_before,
        created=created,
        created_after=created_after,
        created_before=created_before,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interval=interval,
        interval_empty=interval_empty,
        interval_gt=interval_gt,
        interval_gte=interval_gte,
        interval_lt=interval_lt,
        interval_lte=interval_lte,
        interval_n=interval_n,
        job_id=job_id,
        limit=limit,
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
        object_id=object_id,
        object_id_empty=object_id_empty,
        object_id_gt=object_id_gt,
        object_id_gte=object_id_gte,
        object_id_lt=object_id_lt,
        object_id_lte=object_id_lte,
        object_id_n=object_id_n,
        object_type=object_type,
        object_type_n=object_type_n,
        offset=offset,
        ordering=ordering,
        q=q,
        scheduled=scheduled,
        scheduled_after=scheduled_after,
        scheduled_before=scheduled_before,
        started=started,
        started_after=started_after,
        started_before=started_before,
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
        user=user,
        user_n=user_n,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    completed: Union[Unset, datetime.datetime] = UNSET,
    completed_after: Union[Unset, datetime.datetime] = UNSET,
    completed_before: Union[Unset, datetime.datetime] = UNSET,
    created: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interval: Union[Unset, list[int]] = UNSET,
    interval_empty: Union[Unset, bool] = UNSET,
    interval_gt: Union[Unset, list[int]] = UNSET,
    interval_gte: Union[Unset, list[int]] = UNSET,
    interval_lt: Union[Unset, list[int]] = UNSET,
    interval_lte: Union[Unset, list[int]] = UNSET,
    interval_n: Union[Unset, list[int]] = UNSET,
    job_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
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
    object_id: Union[Unset, list[int]] = UNSET,
    object_id_empty: Union[Unset, bool] = UNSET,
    object_id_gt: Union[Unset, list[int]] = UNSET,
    object_id_gte: Union[Unset, list[int]] = UNSET,
    object_id_lt: Union[Unset, list[int]] = UNSET,
    object_id_lte: Union[Unset, list[int]] = UNSET,
    object_id_n: Union[Unset, list[int]] = UNSET,
    object_type: Union[Unset, int] = UNSET,
    object_type_n: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    scheduled: Union[Unset, datetime.datetime] = UNSET,
    scheduled_after: Union[Unset, datetime.datetime] = UNSET,
    scheduled_before: Union[Unset, datetime.datetime] = UNSET,
    started: Union[Unset, datetime.datetime] = UNSET,
    started_after: Union[Unset, datetime.datetime] = UNSET,
    started_before: Union[Unset, datetime.datetime] = UNSET,
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
    user: Union[Unset, int] = UNSET,
    user_n: Union[Unset, int] = UNSET,
) -> Optional[PaginatedJobList]:
    """Retrieve a list of job results

    Args:
        completed (Union[Unset, datetime.datetime]):
        completed_after (Union[Unset, datetime.datetime]):
        completed_before (Union[Unset, datetime.datetime]):
        created (Union[Unset, datetime.datetime]):
        created_after (Union[Unset, datetime.datetime]):
        created_before (Union[Unset, datetime.datetime]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interval (Union[Unset, list[int]]):
        interval_empty (Union[Unset, bool]):
        interval_gt (Union[Unset, list[int]]):
        interval_gte (Union[Unset, list[int]]):
        interval_lt (Union[Unset, list[int]]):
        interval_lte (Union[Unset, list[int]]):
        interval_n (Union[Unset, list[int]]):
        job_id (Union[Unset, UUID]):
        limit (Union[Unset, int]):
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
        object_id (Union[Unset, list[int]]):
        object_id_empty (Union[Unset, bool]):
        object_id_gt (Union[Unset, list[int]]):
        object_id_gte (Union[Unset, list[int]]):
        object_id_lt (Union[Unset, list[int]]):
        object_id_lte (Union[Unset, list[int]]):
        object_id_n (Union[Unset, list[int]]):
        object_type (Union[Unset, int]):
        object_type_n (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        scheduled (Union[Unset, datetime.datetime]):
        scheduled_after (Union[Unset, datetime.datetime]):
        scheduled_before (Union[Unset, datetime.datetime]):
        started (Union[Unset, datetime.datetime]):
        started_after (Union[Unset, datetime.datetime]):
        started_before (Union[Unset, datetime.datetime]):
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
        user (Union[Unset, int]):
        user_n (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedJobList
    """

    return sync_detailed(
        client=client,
        completed=completed,
        completed_after=completed_after,
        completed_before=completed_before,
        created=created,
        created_after=created_after,
        created_before=created_before,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interval=interval,
        interval_empty=interval_empty,
        interval_gt=interval_gt,
        interval_gte=interval_gte,
        interval_lt=interval_lt,
        interval_lte=interval_lte,
        interval_n=interval_n,
        job_id=job_id,
        limit=limit,
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
        object_id=object_id,
        object_id_empty=object_id_empty,
        object_id_gt=object_id_gt,
        object_id_gte=object_id_gte,
        object_id_lt=object_id_lt,
        object_id_lte=object_id_lte,
        object_id_n=object_id_n,
        object_type=object_type,
        object_type_n=object_type_n,
        offset=offset,
        ordering=ordering,
        q=q,
        scheduled=scheduled,
        scheduled_after=scheduled_after,
        scheduled_before=scheduled_before,
        started=started,
        started_after=started_after,
        started_before=started_before,
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
        user=user,
        user_n=user_n,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    completed: Union[Unset, datetime.datetime] = UNSET,
    completed_after: Union[Unset, datetime.datetime] = UNSET,
    completed_before: Union[Unset, datetime.datetime] = UNSET,
    created: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interval: Union[Unset, list[int]] = UNSET,
    interval_empty: Union[Unset, bool] = UNSET,
    interval_gt: Union[Unset, list[int]] = UNSET,
    interval_gte: Union[Unset, list[int]] = UNSET,
    interval_lt: Union[Unset, list[int]] = UNSET,
    interval_lte: Union[Unset, list[int]] = UNSET,
    interval_n: Union[Unset, list[int]] = UNSET,
    job_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
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
    object_id: Union[Unset, list[int]] = UNSET,
    object_id_empty: Union[Unset, bool] = UNSET,
    object_id_gt: Union[Unset, list[int]] = UNSET,
    object_id_gte: Union[Unset, list[int]] = UNSET,
    object_id_lt: Union[Unset, list[int]] = UNSET,
    object_id_lte: Union[Unset, list[int]] = UNSET,
    object_id_n: Union[Unset, list[int]] = UNSET,
    object_type: Union[Unset, int] = UNSET,
    object_type_n: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    scheduled: Union[Unset, datetime.datetime] = UNSET,
    scheduled_after: Union[Unset, datetime.datetime] = UNSET,
    scheduled_before: Union[Unset, datetime.datetime] = UNSET,
    started: Union[Unset, datetime.datetime] = UNSET,
    started_after: Union[Unset, datetime.datetime] = UNSET,
    started_before: Union[Unset, datetime.datetime] = UNSET,
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
    user: Union[Unset, int] = UNSET,
    user_n: Union[Unset, int] = UNSET,
) -> Response[PaginatedJobList]:
    """Retrieve a list of job results

    Args:
        completed (Union[Unset, datetime.datetime]):
        completed_after (Union[Unset, datetime.datetime]):
        completed_before (Union[Unset, datetime.datetime]):
        created (Union[Unset, datetime.datetime]):
        created_after (Union[Unset, datetime.datetime]):
        created_before (Union[Unset, datetime.datetime]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interval (Union[Unset, list[int]]):
        interval_empty (Union[Unset, bool]):
        interval_gt (Union[Unset, list[int]]):
        interval_gte (Union[Unset, list[int]]):
        interval_lt (Union[Unset, list[int]]):
        interval_lte (Union[Unset, list[int]]):
        interval_n (Union[Unset, list[int]]):
        job_id (Union[Unset, UUID]):
        limit (Union[Unset, int]):
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
        object_id (Union[Unset, list[int]]):
        object_id_empty (Union[Unset, bool]):
        object_id_gt (Union[Unset, list[int]]):
        object_id_gte (Union[Unset, list[int]]):
        object_id_lt (Union[Unset, list[int]]):
        object_id_lte (Union[Unset, list[int]]):
        object_id_n (Union[Unset, list[int]]):
        object_type (Union[Unset, int]):
        object_type_n (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        scheduled (Union[Unset, datetime.datetime]):
        scheduled_after (Union[Unset, datetime.datetime]):
        scheduled_before (Union[Unset, datetime.datetime]):
        started (Union[Unset, datetime.datetime]):
        started_after (Union[Unset, datetime.datetime]):
        started_before (Union[Unset, datetime.datetime]):
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
        user (Union[Unset, int]):
        user_n (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedJobList]
    """

    kwargs = _get_kwargs(
        completed=completed,
        completed_after=completed_after,
        completed_before=completed_before,
        created=created,
        created_after=created_after,
        created_before=created_before,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interval=interval,
        interval_empty=interval_empty,
        interval_gt=interval_gt,
        interval_gte=interval_gte,
        interval_lt=interval_lt,
        interval_lte=interval_lte,
        interval_n=interval_n,
        job_id=job_id,
        limit=limit,
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
        object_id=object_id,
        object_id_empty=object_id_empty,
        object_id_gt=object_id_gt,
        object_id_gte=object_id_gte,
        object_id_lt=object_id_lt,
        object_id_lte=object_id_lte,
        object_id_n=object_id_n,
        object_type=object_type,
        object_type_n=object_type_n,
        offset=offset,
        ordering=ordering,
        q=q,
        scheduled=scheduled,
        scheduled_after=scheduled_after,
        scheduled_before=scheduled_before,
        started=started,
        started_after=started_after,
        started_before=started_before,
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
        user=user,
        user_n=user_n,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    completed: Union[Unset, datetime.datetime] = UNSET,
    completed_after: Union[Unset, datetime.datetime] = UNSET,
    completed_before: Union[Unset, datetime.datetime] = UNSET,
    created: Union[Unset, datetime.datetime] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interval: Union[Unset, list[int]] = UNSET,
    interval_empty: Union[Unset, bool] = UNSET,
    interval_gt: Union[Unset, list[int]] = UNSET,
    interval_gte: Union[Unset, list[int]] = UNSET,
    interval_lt: Union[Unset, list[int]] = UNSET,
    interval_lte: Union[Unset, list[int]] = UNSET,
    interval_n: Union[Unset, list[int]] = UNSET,
    job_id: Union[Unset, UUID] = UNSET,
    limit: Union[Unset, int] = UNSET,
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
    object_id: Union[Unset, list[int]] = UNSET,
    object_id_empty: Union[Unset, bool] = UNSET,
    object_id_gt: Union[Unset, list[int]] = UNSET,
    object_id_gte: Union[Unset, list[int]] = UNSET,
    object_id_lt: Union[Unset, list[int]] = UNSET,
    object_id_lte: Union[Unset, list[int]] = UNSET,
    object_id_n: Union[Unset, list[int]] = UNSET,
    object_type: Union[Unset, int] = UNSET,
    object_type_n: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    scheduled: Union[Unset, datetime.datetime] = UNSET,
    scheduled_after: Union[Unset, datetime.datetime] = UNSET,
    scheduled_before: Union[Unset, datetime.datetime] = UNSET,
    started: Union[Unset, datetime.datetime] = UNSET,
    started_after: Union[Unset, datetime.datetime] = UNSET,
    started_before: Union[Unset, datetime.datetime] = UNSET,
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
    user: Union[Unset, int] = UNSET,
    user_n: Union[Unset, int] = UNSET,
) -> Optional[PaginatedJobList]:
    """Retrieve a list of job results

    Args:
        completed (Union[Unset, datetime.datetime]):
        completed_after (Union[Unset, datetime.datetime]):
        completed_before (Union[Unset, datetime.datetime]):
        created (Union[Unset, datetime.datetime]):
        created_after (Union[Unset, datetime.datetime]):
        created_before (Union[Unset, datetime.datetime]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interval (Union[Unset, list[int]]):
        interval_empty (Union[Unset, bool]):
        interval_gt (Union[Unset, list[int]]):
        interval_gte (Union[Unset, list[int]]):
        interval_lt (Union[Unset, list[int]]):
        interval_lte (Union[Unset, list[int]]):
        interval_n (Union[Unset, list[int]]):
        job_id (Union[Unset, UUID]):
        limit (Union[Unset, int]):
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
        object_id (Union[Unset, list[int]]):
        object_id_empty (Union[Unset, bool]):
        object_id_gt (Union[Unset, list[int]]):
        object_id_gte (Union[Unset, list[int]]):
        object_id_lt (Union[Unset, list[int]]):
        object_id_lte (Union[Unset, list[int]]):
        object_id_n (Union[Unset, list[int]]):
        object_type (Union[Unset, int]):
        object_type_n (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        scheduled (Union[Unset, datetime.datetime]):
        scheduled_after (Union[Unset, datetime.datetime]):
        scheduled_before (Union[Unset, datetime.datetime]):
        started (Union[Unset, datetime.datetime]):
        started_after (Union[Unset, datetime.datetime]):
        started_before (Union[Unset, datetime.datetime]):
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
        user (Union[Unset, int]):
        user_n (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedJobList
    """

    return (
        await asyncio_detailed(
            client=client,
            completed=completed,
            completed_after=completed_after,
            completed_before=completed_before,
            created=created,
            created_after=created_after,
            created_before=created_before,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            interval=interval,
            interval_empty=interval_empty,
            interval_gt=interval_gt,
            interval_gte=interval_gte,
            interval_lt=interval_lt,
            interval_lte=interval_lte,
            interval_n=interval_n,
            job_id=job_id,
            limit=limit,
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
            object_id=object_id,
            object_id_empty=object_id_empty,
            object_id_gt=object_id_gt,
            object_id_gte=object_id_gte,
            object_id_lt=object_id_lt,
            object_id_lte=object_id_lte,
            object_id_n=object_id_n,
            object_type=object_type,
            object_type_n=object_type_n,
            offset=offset,
            ordering=ordering,
            q=q,
            scheduled=scheduled,
            scheduled_after=scheduled_after,
            scheduled_before=scheduled_before,
            started=started,
            started_after=started_after,
            started_before=started_before,
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
            user=user,
            user_n=user_n,
        )
    ).parsed
