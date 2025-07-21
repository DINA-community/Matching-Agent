import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_contact_assignment_list import PaginatedContactAssignmentList
from ...models.tenancy_contact_assignments_list_priority import (
    TenancyContactAssignmentsListPriority,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    contact_id: Union[Unset, list[int]] = UNSET,
    contact_id_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[str]] = UNSET,
    group_id_n: Union[Unset, list[str]] = UNSET,
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
    object_id: Union[Unset, list[int]] = UNSET,
    object_id_empty: Union[Unset, bool] = UNSET,
    object_id_gt: Union[Unset, list[int]] = UNSET,
    object_id_gte: Union[Unset, list[int]] = UNSET,
    object_id_lt: Union[Unset, list[int]] = UNSET,
    object_id_lte: Union[Unset, list[int]] = UNSET,
    object_id_n: Union[Unset, list[int]] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, int] = UNSET,
    object_type_id_n: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    priority: Union[Unset, TenancyContactAssignmentsListPriority] = UNSET,
    q: Union[Unset, str] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[int]] = UNSET,
    role_id_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_contact_id: Union[Unset, list[int]] = UNSET
    if not isinstance(contact_id, Unset):
        json_contact_id = contact_id

    params["contact_id"] = json_contact_id

    json_contact_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(contact_id_n, Unset):
        json_contact_id_n = contact_id_n

    params["contact_id__n"] = json_contact_id_n

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

    json_group: Union[Unset, list[str]] = UNSET
    if not isinstance(group, Unset):
        json_group = group

    params["group"] = json_group

    json_group_n: Union[Unset, list[str]] = UNSET
    if not isinstance(group_n, Unset):
        json_group_n = group_n

    params["group__n"] = json_group_n

    json_group_id: Union[Unset, list[str]] = UNSET
    if not isinstance(group_id, Unset):
        json_group_id = group_id

    params["group_id"] = json_group_id

    json_group_id_n: Union[Unset, list[str]] = UNSET
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

    params["object_type_id"] = object_type_id

    params["object_type_id__n"] = object_type_id_n

    params["offset"] = offset

    params["ordering"] = ordering

    json_priority: Union[Unset, str] = UNSET
    if not isinstance(priority, Unset):
        json_priority = priority.value

    params["priority"] = json_priority

    params["q"] = q

    json_role: Union[Unset, list[str]] = UNSET
    if not isinstance(role, Unset):
        json_role = role

    params["role"] = json_role

    json_role_n: Union[Unset, list[str]] = UNSET
    if not isinstance(role_n, Unset):
        json_role_n = role_n

    params["role__n"] = json_role_n

    json_role_id: Union[Unset, list[int]] = UNSET
    if not isinstance(role_id, Unset):
        json_role_id = role_id

    params["role_id"] = json_role_id

    json_role_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(role_id_n, Unset):
        json_role_id_n = role_id_n

    params["role_id__n"] = json_role_id_n

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

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tenancy/contact-assignments/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedContactAssignmentList]:
    if response.status_code == 200:
        response_200 = PaginatedContactAssignmentList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedContactAssignmentList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    contact_id: Union[Unset, list[int]] = UNSET,
    contact_id_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[str]] = UNSET,
    group_id_n: Union[Unset, list[str]] = UNSET,
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
    object_id: Union[Unset, list[int]] = UNSET,
    object_id_empty: Union[Unset, bool] = UNSET,
    object_id_gt: Union[Unset, list[int]] = UNSET,
    object_id_gte: Union[Unset, list[int]] = UNSET,
    object_id_lt: Union[Unset, list[int]] = UNSET,
    object_id_lte: Union[Unset, list[int]] = UNSET,
    object_id_n: Union[Unset, list[int]] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, int] = UNSET,
    object_type_id_n: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    priority: Union[Unset, TenancyContactAssignmentsListPriority] = UNSET,
    q: Union[Unset, str] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[int]] = UNSET,
    role_id_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedContactAssignmentList]:
    """Get a list of contact assignment objects.

    Args:
        contact_id (Union[Unset, list[int]]):
        contact_id_n (Union[Unset, list[int]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        group (Union[Unset, list[str]]):
        group_n (Union[Unset, list[str]]):
        group_id (Union[Unset, list[str]]):
        group_id_n (Union[Unset, list[str]]):
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
        object_id (Union[Unset, list[int]]):
        object_id_empty (Union[Unset, bool]):
        object_id_gt (Union[Unset, list[int]]):
        object_id_gte (Union[Unset, list[int]]):
        object_id_lt (Union[Unset, list[int]]):
        object_id_lte (Union[Unset, list[int]]):
        object_id_n (Union[Unset, list[int]]):
        object_type (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_id (Union[Unset, int]):
        object_type_id_n (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        priority (Union[Unset, TenancyContactAssignmentsListPriority]):
        q (Union[Unset, str]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[int]]):
        role_id_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedContactAssignmentList]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        contact_id_n=contact_id_n,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
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
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        modified_by_request=modified_by_request,
        object_id=object_id,
        object_id_empty=object_id_empty,
        object_id_gt=object_id_gt,
        object_id_gte=object_id_gte,
        object_id_lt=object_id_lt,
        object_id_lte=object_id_lte,
        object_id_n=object_id_n,
        object_type=object_type,
        object_type_n=object_type_n,
        object_type_id=object_type_id,
        object_type_id_n=object_type_id_n,
        offset=offset,
        ordering=ordering,
        priority=priority,
        q=q,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    contact_id: Union[Unset, list[int]] = UNSET,
    contact_id_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[str]] = UNSET,
    group_id_n: Union[Unset, list[str]] = UNSET,
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
    object_id: Union[Unset, list[int]] = UNSET,
    object_id_empty: Union[Unset, bool] = UNSET,
    object_id_gt: Union[Unset, list[int]] = UNSET,
    object_id_gte: Union[Unset, list[int]] = UNSET,
    object_id_lt: Union[Unset, list[int]] = UNSET,
    object_id_lte: Union[Unset, list[int]] = UNSET,
    object_id_n: Union[Unset, list[int]] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, int] = UNSET,
    object_type_id_n: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    priority: Union[Unset, TenancyContactAssignmentsListPriority] = UNSET,
    q: Union[Unset, str] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[int]] = UNSET,
    role_id_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedContactAssignmentList]:
    """Get a list of contact assignment objects.

    Args:
        contact_id (Union[Unset, list[int]]):
        contact_id_n (Union[Unset, list[int]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        group (Union[Unset, list[str]]):
        group_n (Union[Unset, list[str]]):
        group_id (Union[Unset, list[str]]):
        group_id_n (Union[Unset, list[str]]):
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
        object_id (Union[Unset, list[int]]):
        object_id_empty (Union[Unset, bool]):
        object_id_gt (Union[Unset, list[int]]):
        object_id_gte (Union[Unset, list[int]]):
        object_id_lt (Union[Unset, list[int]]):
        object_id_lte (Union[Unset, list[int]]):
        object_id_n (Union[Unset, list[int]]):
        object_type (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_id (Union[Unset, int]):
        object_type_id_n (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        priority (Union[Unset, TenancyContactAssignmentsListPriority]):
        q (Union[Unset, str]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[int]]):
        role_id_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedContactAssignmentList
    """

    return sync_detailed(
        client=client,
        contact_id=contact_id,
        contact_id_n=contact_id_n,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
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
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        modified_by_request=modified_by_request,
        object_id=object_id,
        object_id_empty=object_id_empty,
        object_id_gt=object_id_gt,
        object_id_gte=object_id_gte,
        object_id_lt=object_id_lt,
        object_id_lte=object_id_lte,
        object_id_n=object_id_n,
        object_type=object_type,
        object_type_n=object_type_n,
        object_type_id=object_type_id,
        object_type_id_n=object_type_id_n,
        offset=offset,
        ordering=ordering,
        priority=priority,
        q=q,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    contact_id: Union[Unset, list[int]] = UNSET,
    contact_id_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[str]] = UNSET,
    group_id_n: Union[Unset, list[str]] = UNSET,
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
    object_id: Union[Unset, list[int]] = UNSET,
    object_id_empty: Union[Unset, bool] = UNSET,
    object_id_gt: Union[Unset, list[int]] = UNSET,
    object_id_gte: Union[Unset, list[int]] = UNSET,
    object_id_lt: Union[Unset, list[int]] = UNSET,
    object_id_lte: Union[Unset, list[int]] = UNSET,
    object_id_n: Union[Unset, list[int]] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, int] = UNSET,
    object_type_id_n: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    priority: Union[Unset, TenancyContactAssignmentsListPriority] = UNSET,
    q: Union[Unset, str] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[int]] = UNSET,
    role_id_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedContactAssignmentList]:
    """Get a list of contact assignment objects.

    Args:
        contact_id (Union[Unset, list[int]]):
        contact_id_n (Union[Unset, list[int]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        group (Union[Unset, list[str]]):
        group_n (Union[Unset, list[str]]):
        group_id (Union[Unset, list[str]]):
        group_id_n (Union[Unset, list[str]]):
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
        object_id (Union[Unset, list[int]]):
        object_id_empty (Union[Unset, bool]):
        object_id_gt (Union[Unset, list[int]]):
        object_id_gte (Union[Unset, list[int]]):
        object_id_lt (Union[Unset, list[int]]):
        object_id_lte (Union[Unset, list[int]]):
        object_id_n (Union[Unset, list[int]]):
        object_type (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_id (Union[Unset, int]):
        object_type_id_n (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        priority (Union[Unset, TenancyContactAssignmentsListPriority]):
        q (Union[Unset, str]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[int]]):
        role_id_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedContactAssignmentList]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        contact_id_n=contact_id_n,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
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
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        modified_by_request=modified_by_request,
        object_id=object_id,
        object_id_empty=object_id_empty,
        object_id_gt=object_id_gt,
        object_id_gte=object_id_gte,
        object_id_lt=object_id_lt,
        object_id_lte=object_id_lte,
        object_id_n=object_id_n,
        object_type=object_type,
        object_type_n=object_type_n,
        object_type_id=object_type_id,
        object_type_id_n=object_type_id_n,
        offset=offset,
        ordering=ordering,
        priority=priority,
        q=q,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    contact_id: Union[Unset, list[int]] = UNSET,
    contact_id_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[str]] = UNSET,
    group_id_n: Union[Unset, list[str]] = UNSET,
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
    object_id: Union[Unset, list[int]] = UNSET,
    object_id_empty: Union[Unset, bool] = UNSET,
    object_id_gt: Union[Unset, list[int]] = UNSET,
    object_id_gte: Union[Unset, list[int]] = UNSET,
    object_id_lt: Union[Unset, list[int]] = UNSET,
    object_id_lte: Union[Unset, list[int]] = UNSET,
    object_id_n: Union[Unset, list[int]] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, int] = UNSET,
    object_type_id_n: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    priority: Union[Unset, TenancyContactAssignmentsListPriority] = UNSET,
    q: Union[Unset, str] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[int]] = UNSET,
    role_id_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedContactAssignmentList]:
    """Get a list of contact assignment objects.

    Args:
        contact_id (Union[Unset, list[int]]):
        contact_id_n (Union[Unset, list[int]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        group (Union[Unset, list[str]]):
        group_n (Union[Unset, list[str]]):
        group_id (Union[Unset, list[str]]):
        group_id_n (Union[Unset, list[str]]):
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
        object_id (Union[Unset, list[int]]):
        object_id_empty (Union[Unset, bool]):
        object_id_gt (Union[Unset, list[int]]):
        object_id_gte (Union[Unset, list[int]]):
        object_id_lt (Union[Unset, list[int]]):
        object_id_lte (Union[Unset, list[int]]):
        object_id_n (Union[Unset, list[int]]):
        object_type (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_id (Union[Unset, int]):
        object_type_id_n (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        priority (Union[Unset, TenancyContactAssignmentsListPriority]):
        q (Union[Unset, str]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[int]]):
        role_id_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedContactAssignmentList
    """

    return (
        await asyncio_detailed(
            client=client,
            contact_id=contact_id,
            contact_id_n=contact_id_n,
            created=created,
            created_empty=created_empty,
            created_gt=created_gt,
            created_gte=created_gte,
            created_lt=created_lt,
            created_lte=created_lte,
            created_n=created_n,
            created_by_request=created_by_request,
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
            last_updated=last_updated,
            last_updated_empty=last_updated_empty,
            last_updated_gt=last_updated_gt,
            last_updated_gte=last_updated_gte,
            last_updated_lt=last_updated_lt,
            last_updated_lte=last_updated_lte,
            last_updated_n=last_updated_n,
            limit=limit,
            modified_by_request=modified_by_request,
            object_id=object_id,
            object_id_empty=object_id_empty,
            object_id_gt=object_id_gt,
            object_id_gte=object_id_gte,
            object_id_lt=object_id_lt,
            object_id_lte=object_id_lte,
            object_id_n=object_id_n,
            object_type=object_type,
            object_type_n=object_type_n,
            object_type_id=object_type_id,
            object_type_id_n=object_type_id_n,
            offset=offset,
            ordering=ordering,
            priority=priority,
            q=q,
            role=role,
            role_n=role_n,
            role_id=role_id,
            role_id_n=role_id_n,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
            updated_by_request=updated_by_request,
        )
    ).parsed
