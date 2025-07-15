import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_fhrp_group_assignment_list import PaginatedFHRPGroupAssignmentList
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
    device: Union[Unset, list[str]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    group_id: Union[Unset, list[int]] = UNSET,
    group_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_id: Union[Unset, list[int]] = UNSET,
    interface_id_empty: Union[Unset, bool] = UNSET,
    interface_id_gt: Union[Unset, list[int]] = UNSET,
    interface_id_gte: Union[Unset, list[int]] = UNSET,
    interface_id_lt: Union[Unset, list[int]] = UNSET,
    interface_id_lte: Union[Unset, list[int]] = UNSET,
    interface_id_n: Union[Unset, list[int]] = UNSET,
    interface_type: Union[Unset, str] = UNSET,
    interface_type_n: Union[Unset, str] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    priority: Union[Unset, list[int]] = UNSET,
    priority_empty: Union[Unset, bool] = UNSET,
    priority_gt: Union[Unset, list[int]] = UNSET,
    priority_gte: Union[Unset, list[int]] = UNSET,
    priority_lt: Union[Unset, list[int]] = UNSET,
    priority_lte: Union[Unset, list[int]] = UNSET,
    priority_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_machine: Union[Unset, list[str]] = UNSET,
    virtual_machine_id: Union[Unset, list[int]] = UNSET,
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

    json_device: Union[Unset, list[str]] = UNSET
    if not isinstance(device, Unset):
        json_device = device

    params["device"] = json_device

    json_device_id: Union[Unset, list[int]] = UNSET
    if not isinstance(device_id, Unset):
        json_device_id = device_id

    params["device_id"] = json_device_id

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

    json_interface_id: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_id, Unset):
        json_interface_id = interface_id

    params["interface_id"] = json_interface_id

    params["interface_id__empty"] = interface_id_empty

    json_interface_id_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_id_gt, Unset):
        json_interface_id_gt = interface_id_gt

    params["interface_id__gt"] = json_interface_id_gt

    json_interface_id_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_id_gte, Unset):
        json_interface_id_gte = interface_id_gte

    params["interface_id__gte"] = json_interface_id_gte

    json_interface_id_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_id_lt, Unset):
        json_interface_id_lt = interface_id_lt

    params["interface_id__lt"] = json_interface_id_lt

    json_interface_id_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_id_lte, Unset):
        json_interface_id_lte = interface_id_lte

    params["interface_id__lte"] = json_interface_id_lte

    json_interface_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_id_n, Unset):
        json_interface_id_n = interface_id_n

    params["interface_id__n"] = json_interface_id_n

    params["interface_type"] = interface_type

    params["interface_type__n"] = interface_type_n

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

    params["offset"] = offset

    params["ordering"] = ordering

    json_priority: Union[Unset, list[int]] = UNSET
    if not isinstance(priority, Unset):
        json_priority = priority

    params["priority"] = json_priority

    params["priority__empty"] = priority_empty

    json_priority_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(priority_gt, Unset):
        json_priority_gt = priority_gt

    params["priority__gt"] = json_priority_gt

    json_priority_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(priority_gte, Unset):
        json_priority_gte = priority_gte

    params["priority__gte"] = json_priority_gte

    json_priority_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(priority_lt, Unset):
        json_priority_lt = priority_lt

    params["priority__lt"] = json_priority_lt

    json_priority_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(priority_lte, Unset):
        json_priority_lte = priority_lte

    params["priority__lte"] = json_priority_lte

    json_priority_n: Union[Unset, list[int]] = UNSET
    if not isinstance(priority_n, Unset):
        json_priority_n = priority_n

    params["priority__n"] = json_priority_n

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    json_virtual_machine: Union[Unset, list[str]] = UNSET
    if not isinstance(virtual_machine, Unset):
        json_virtual_machine = virtual_machine

    params["virtual_machine"] = json_virtual_machine

    json_virtual_machine_id: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_machine_id, Unset):
        json_virtual_machine_id = virtual_machine_id

    params["virtual_machine_id"] = json_virtual_machine_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/ipam/fhrp-group-assignments/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedFHRPGroupAssignmentList]:
    if response.status_code == 200:
        response_200 = PaginatedFHRPGroupAssignmentList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedFHRPGroupAssignmentList]:
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
    device: Union[Unset, list[str]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    group_id: Union[Unset, list[int]] = UNSET,
    group_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_id: Union[Unset, list[int]] = UNSET,
    interface_id_empty: Union[Unset, bool] = UNSET,
    interface_id_gt: Union[Unset, list[int]] = UNSET,
    interface_id_gte: Union[Unset, list[int]] = UNSET,
    interface_id_lt: Union[Unset, list[int]] = UNSET,
    interface_id_lte: Union[Unset, list[int]] = UNSET,
    interface_id_n: Union[Unset, list[int]] = UNSET,
    interface_type: Union[Unset, str] = UNSET,
    interface_type_n: Union[Unset, str] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    priority: Union[Unset, list[int]] = UNSET,
    priority_empty: Union[Unset, bool] = UNSET,
    priority_gt: Union[Unset, list[int]] = UNSET,
    priority_gte: Union[Unset, list[int]] = UNSET,
    priority_lt: Union[Unset, list[int]] = UNSET,
    priority_lte: Union[Unset, list[int]] = UNSET,
    priority_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_machine: Union[Unset, list[str]] = UNSET,
    virtual_machine_id: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedFHRPGroupAssignmentList]:
    """Get a list of FHRP group assignment objects.

    Args:
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        device (Union[Unset, list[str]]):
        device_id (Union[Unset, list[int]]):
        group_id (Union[Unset, list[int]]):
        group_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_id (Union[Unset, list[int]]):
        interface_id_empty (Union[Unset, bool]):
        interface_id_gt (Union[Unset, list[int]]):
        interface_id_gte (Union[Unset, list[int]]):
        interface_id_lt (Union[Unset, list[int]]):
        interface_id_lte (Union[Unset, list[int]]):
        interface_id_n (Union[Unset, list[int]]):
        interface_type (Union[Unset, str]):
        interface_type_n (Union[Unset, str]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        priority (Union[Unset, list[int]]):
        priority_empty (Union[Unset, bool]):
        priority_gt (Union[Unset, list[int]]):
        priority_gte (Union[Unset, list[int]]):
        priority_lt (Union[Unset, list[int]]):
        priority_lte (Union[Unset, list[int]]):
        priority_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        virtual_machine (Union[Unset, list[str]]):
        virtual_machine_id (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedFHRPGroupAssignmentList]
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
        device=device,
        device_id=device_id,
        group_id=group_id,
        group_id_n=group_id_n,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface_id=interface_id,
        interface_id_empty=interface_id_empty,
        interface_id_gt=interface_id_gt,
        interface_id_gte=interface_id_gte,
        interface_id_lt=interface_id_lt,
        interface_id_lte=interface_id_lte,
        interface_id_n=interface_id_n,
        interface_type=interface_type,
        interface_type_n=interface_type_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        priority=priority,
        priority_empty=priority_empty,
        priority_gt=priority_gt,
        priority_gte=priority_gte,
        priority_lt=priority_lt,
        priority_lte=priority_lte,
        priority_n=priority_n,
        updated_by_request=updated_by_request,
        virtual_machine=virtual_machine,
        virtual_machine_id=virtual_machine_id,
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
    device: Union[Unset, list[str]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    group_id: Union[Unset, list[int]] = UNSET,
    group_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_id: Union[Unset, list[int]] = UNSET,
    interface_id_empty: Union[Unset, bool] = UNSET,
    interface_id_gt: Union[Unset, list[int]] = UNSET,
    interface_id_gte: Union[Unset, list[int]] = UNSET,
    interface_id_lt: Union[Unset, list[int]] = UNSET,
    interface_id_lte: Union[Unset, list[int]] = UNSET,
    interface_id_n: Union[Unset, list[int]] = UNSET,
    interface_type: Union[Unset, str] = UNSET,
    interface_type_n: Union[Unset, str] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    priority: Union[Unset, list[int]] = UNSET,
    priority_empty: Union[Unset, bool] = UNSET,
    priority_gt: Union[Unset, list[int]] = UNSET,
    priority_gte: Union[Unset, list[int]] = UNSET,
    priority_lt: Union[Unset, list[int]] = UNSET,
    priority_lte: Union[Unset, list[int]] = UNSET,
    priority_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_machine: Union[Unset, list[str]] = UNSET,
    virtual_machine_id: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedFHRPGroupAssignmentList]:
    """Get a list of FHRP group assignment objects.

    Args:
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        device (Union[Unset, list[str]]):
        device_id (Union[Unset, list[int]]):
        group_id (Union[Unset, list[int]]):
        group_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_id (Union[Unset, list[int]]):
        interface_id_empty (Union[Unset, bool]):
        interface_id_gt (Union[Unset, list[int]]):
        interface_id_gte (Union[Unset, list[int]]):
        interface_id_lt (Union[Unset, list[int]]):
        interface_id_lte (Union[Unset, list[int]]):
        interface_id_n (Union[Unset, list[int]]):
        interface_type (Union[Unset, str]):
        interface_type_n (Union[Unset, str]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        priority (Union[Unset, list[int]]):
        priority_empty (Union[Unset, bool]):
        priority_gt (Union[Unset, list[int]]):
        priority_gte (Union[Unset, list[int]]):
        priority_lt (Union[Unset, list[int]]):
        priority_lte (Union[Unset, list[int]]):
        priority_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        virtual_machine (Union[Unset, list[str]]):
        virtual_machine_id (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedFHRPGroupAssignmentList
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
        device=device,
        device_id=device_id,
        group_id=group_id,
        group_id_n=group_id_n,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface_id=interface_id,
        interface_id_empty=interface_id_empty,
        interface_id_gt=interface_id_gt,
        interface_id_gte=interface_id_gte,
        interface_id_lt=interface_id_lt,
        interface_id_lte=interface_id_lte,
        interface_id_n=interface_id_n,
        interface_type=interface_type,
        interface_type_n=interface_type_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        priority=priority,
        priority_empty=priority_empty,
        priority_gt=priority_gt,
        priority_gte=priority_gte,
        priority_lt=priority_lt,
        priority_lte=priority_lte,
        priority_n=priority_n,
        updated_by_request=updated_by_request,
        virtual_machine=virtual_machine,
        virtual_machine_id=virtual_machine_id,
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
    device: Union[Unset, list[str]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    group_id: Union[Unset, list[int]] = UNSET,
    group_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_id: Union[Unset, list[int]] = UNSET,
    interface_id_empty: Union[Unset, bool] = UNSET,
    interface_id_gt: Union[Unset, list[int]] = UNSET,
    interface_id_gte: Union[Unset, list[int]] = UNSET,
    interface_id_lt: Union[Unset, list[int]] = UNSET,
    interface_id_lte: Union[Unset, list[int]] = UNSET,
    interface_id_n: Union[Unset, list[int]] = UNSET,
    interface_type: Union[Unset, str] = UNSET,
    interface_type_n: Union[Unset, str] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    priority: Union[Unset, list[int]] = UNSET,
    priority_empty: Union[Unset, bool] = UNSET,
    priority_gt: Union[Unset, list[int]] = UNSET,
    priority_gte: Union[Unset, list[int]] = UNSET,
    priority_lt: Union[Unset, list[int]] = UNSET,
    priority_lte: Union[Unset, list[int]] = UNSET,
    priority_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_machine: Union[Unset, list[str]] = UNSET,
    virtual_machine_id: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedFHRPGroupAssignmentList]:
    """Get a list of FHRP group assignment objects.

    Args:
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        device (Union[Unset, list[str]]):
        device_id (Union[Unset, list[int]]):
        group_id (Union[Unset, list[int]]):
        group_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_id (Union[Unset, list[int]]):
        interface_id_empty (Union[Unset, bool]):
        interface_id_gt (Union[Unset, list[int]]):
        interface_id_gte (Union[Unset, list[int]]):
        interface_id_lt (Union[Unset, list[int]]):
        interface_id_lte (Union[Unset, list[int]]):
        interface_id_n (Union[Unset, list[int]]):
        interface_type (Union[Unset, str]):
        interface_type_n (Union[Unset, str]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        priority (Union[Unset, list[int]]):
        priority_empty (Union[Unset, bool]):
        priority_gt (Union[Unset, list[int]]):
        priority_gte (Union[Unset, list[int]]):
        priority_lt (Union[Unset, list[int]]):
        priority_lte (Union[Unset, list[int]]):
        priority_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        virtual_machine (Union[Unset, list[str]]):
        virtual_machine_id (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedFHRPGroupAssignmentList]
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
        device=device,
        device_id=device_id,
        group_id=group_id,
        group_id_n=group_id_n,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface_id=interface_id,
        interface_id_empty=interface_id_empty,
        interface_id_gt=interface_id_gt,
        interface_id_gte=interface_id_gte,
        interface_id_lt=interface_id_lt,
        interface_id_lte=interface_id_lte,
        interface_id_n=interface_id_n,
        interface_type=interface_type,
        interface_type_n=interface_type_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        priority=priority,
        priority_empty=priority_empty,
        priority_gt=priority_gt,
        priority_gte=priority_gte,
        priority_lt=priority_lt,
        priority_lte=priority_lte,
        priority_n=priority_n,
        updated_by_request=updated_by_request,
        virtual_machine=virtual_machine,
        virtual_machine_id=virtual_machine_id,
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
    device: Union[Unset, list[str]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    group_id: Union[Unset, list[int]] = UNSET,
    group_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_id: Union[Unset, list[int]] = UNSET,
    interface_id_empty: Union[Unset, bool] = UNSET,
    interface_id_gt: Union[Unset, list[int]] = UNSET,
    interface_id_gte: Union[Unset, list[int]] = UNSET,
    interface_id_lt: Union[Unset, list[int]] = UNSET,
    interface_id_lte: Union[Unset, list[int]] = UNSET,
    interface_id_n: Union[Unset, list[int]] = UNSET,
    interface_type: Union[Unset, str] = UNSET,
    interface_type_n: Union[Unset, str] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    priority: Union[Unset, list[int]] = UNSET,
    priority_empty: Union[Unset, bool] = UNSET,
    priority_gt: Union[Unset, list[int]] = UNSET,
    priority_gte: Union[Unset, list[int]] = UNSET,
    priority_lt: Union[Unset, list[int]] = UNSET,
    priority_lte: Union[Unset, list[int]] = UNSET,
    priority_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_machine: Union[Unset, list[str]] = UNSET,
    virtual_machine_id: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedFHRPGroupAssignmentList]:
    """Get a list of FHRP group assignment objects.

    Args:
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        device (Union[Unset, list[str]]):
        device_id (Union[Unset, list[int]]):
        group_id (Union[Unset, list[int]]):
        group_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_id (Union[Unset, list[int]]):
        interface_id_empty (Union[Unset, bool]):
        interface_id_gt (Union[Unset, list[int]]):
        interface_id_gte (Union[Unset, list[int]]):
        interface_id_lt (Union[Unset, list[int]]):
        interface_id_lte (Union[Unset, list[int]]):
        interface_id_n (Union[Unset, list[int]]):
        interface_type (Union[Unset, str]):
        interface_type_n (Union[Unset, str]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        priority (Union[Unset, list[int]]):
        priority_empty (Union[Unset, bool]):
        priority_gt (Union[Unset, list[int]]):
        priority_gte (Union[Unset, list[int]]):
        priority_lt (Union[Unset, list[int]]):
        priority_lte (Union[Unset, list[int]]):
        priority_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        virtual_machine (Union[Unset, list[str]]):
        virtual_machine_id (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedFHRPGroupAssignmentList
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
            device=device,
            device_id=device_id,
            group_id=group_id,
            group_id_n=group_id_n,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            interface_id=interface_id,
            interface_id_empty=interface_id_empty,
            interface_id_gt=interface_id_gt,
            interface_id_gte=interface_id_gte,
            interface_id_lt=interface_id_lt,
            interface_id_lte=interface_id_lte,
            interface_id_n=interface_id_n,
            interface_type=interface_type,
            interface_type_n=interface_type_n,
            last_updated=last_updated,
            last_updated_empty=last_updated_empty,
            last_updated_gt=last_updated_gt,
            last_updated_gte=last_updated_gte,
            last_updated_lt=last_updated_lt,
            last_updated_lte=last_updated_lte,
            last_updated_n=last_updated_n,
            limit=limit,
            modified_by_request=modified_by_request,
            offset=offset,
            ordering=ordering,
            priority=priority,
            priority_empty=priority_empty,
            priority_gt=priority_gt,
            priority_gte=priority_gte,
            priority_lt=priority_lt,
            priority_lte=priority_lte,
            priority_n=priority_n,
            updated_by_request=updated_by_request,
            virtual_machine=virtual_machine,
            virtual_machine_id=virtual_machine_id,
        )
    ).parsed
