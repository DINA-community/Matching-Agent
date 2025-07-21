import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_journal_entry_list import PaginatedJournalEntryList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    assigned_object_id: Union[Unset, list[int]] = UNSET,
    assigned_object_id_empty: Union[Unset, bool] = UNSET,
    assigned_object_id_gt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_gte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_n: Union[Unset, list[int]] = UNSET,
    assigned_object_type: Union[Unset, str] = UNSET,
    assigned_object_type_n: Union[Unset, str] = UNSET,
    assigned_object_type_id: Union[Unset, list[int]] = UNSET,
    assigned_object_type_id_n: Union[Unset, list[int]] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    created_by: Union[Unset, list[str]] = UNSET,
    created_by_n: Union[Unset, list[str]] = UNSET,
    created_by_id: Union[Unset, list[Union[None, int]]] = UNSET,
    created_by_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    kind: Union[Unset, list[str]] = UNSET,
    kind_empty: Union[Unset, bool] = UNSET,
    kind_ic: Union[Unset, list[str]] = UNSET,
    kind_ie: Union[Unset, list[str]] = UNSET,
    kind_iew: Union[Unset, list[str]] = UNSET,
    kind_isw: Union[Unset, list[str]] = UNSET,
    kind_n: Union[Unset, list[str]] = UNSET,
    kind_nic: Union[Unset, list[str]] = UNSET,
    kind_nie: Union[Unset, list[str]] = UNSET,
    kind_niew: Union[Unset, list[str]] = UNSET,
    kind_nisw: Union[Unset, list[str]] = UNSET,
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
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_assigned_object_id: Union[Unset, list[int]] = UNSET
    if not isinstance(assigned_object_id, Unset):
        json_assigned_object_id = assigned_object_id

    params["assigned_object_id"] = json_assigned_object_id

    params["assigned_object_id__empty"] = assigned_object_id_empty

    json_assigned_object_id_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(assigned_object_id_gt, Unset):
        json_assigned_object_id_gt = assigned_object_id_gt

    params["assigned_object_id__gt"] = json_assigned_object_id_gt

    json_assigned_object_id_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(assigned_object_id_gte, Unset):
        json_assigned_object_id_gte = assigned_object_id_gte

    params["assigned_object_id__gte"] = json_assigned_object_id_gte

    json_assigned_object_id_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(assigned_object_id_lt, Unset):
        json_assigned_object_id_lt = assigned_object_id_lt

    params["assigned_object_id__lt"] = json_assigned_object_id_lt

    json_assigned_object_id_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(assigned_object_id_lte, Unset):
        json_assigned_object_id_lte = assigned_object_id_lte

    params["assigned_object_id__lte"] = json_assigned_object_id_lte

    json_assigned_object_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(assigned_object_id_n, Unset):
        json_assigned_object_id_n = assigned_object_id_n

    params["assigned_object_id__n"] = json_assigned_object_id_n

    params["assigned_object_type"] = assigned_object_type

    params["assigned_object_type__n"] = assigned_object_type_n

    json_assigned_object_type_id: Union[Unset, list[int]] = UNSET
    if not isinstance(assigned_object_type_id, Unset):
        json_assigned_object_type_id = assigned_object_type_id

    params["assigned_object_type_id"] = json_assigned_object_type_id

    json_assigned_object_type_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(assigned_object_type_id_n, Unset):
        json_assigned_object_type_id_n = assigned_object_type_id_n

    params["assigned_object_type_id__n"] = json_assigned_object_type_id_n

    json_created_after: Union[Unset, str] = UNSET
    if not isinstance(created_after, Unset):
        json_created_after = created_after.isoformat()
    params["created_after"] = json_created_after

    json_created_before: Union[Unset, str] = UNSET
    if not isinstance(created_before, Unset):
        json_created_before = created_before.isoformat()
    params["created_before"] = json_created_before

    json_created_by: Union[Unset, list[str]] = UNSET
    if not isinstance(created_by, Unset):
        json_created_by = created_by

    params["created_by"] = json_created_by

    json_created_by_n: Union[Unset, list[str]] = UNSET
    if not isinstance(created_by_n, Unset):
        json_created_by_n = created_by_n

    params["created_by__n"] = json_created_by_n

    json_created_by_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(created_by_id, Unset):
        json_created_by_id = []
        for created_by_id_item_data in created_by_id:
            created_by_id_item: Union[None, int]
            created_by_id_item = created_by_id_item_data
            json_created_by_id.append(created_by_id_item)

    params["created_by_id"] = json_created_by_id

    json_created_by_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(created_by_id_n, Unset):
        json_created_by_id_n = []
        for created_by_id_n_item_data in created_by_id_n:
            created_by_id_n_item: Union[None, int]
            created_by_id_n_item = created_by_id_n_item_data
            json_created_by_id_n.append(created_by_id_n_item)

    params["created_by_id__n"] = json_created_by_id_n

    json_created_by_request: Union[Unset, str] = UNSET
    if not isinstance(created_by_request, Unset):
        json_created_by_request = str(created_by_request)
    params["created_by_request"] = json_created_by_request

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

    json_kind: Union[Unset, list[str]] = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind

    params["kind"] = json_kind

    params["kind__empty"] = kind_empty

    json_kind_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(kind_ic, Unset):
        json_kind_ic = kind_ic

    params["kind__ic"] = json_kind_ic

    json_kind_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(kind_ie, Unset):
        json_kind_ie = kind_ie

    params["kind__ie"] = json_kind_ie

    json_kind_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(kind_iew, Unset):
        json_kind_iew = kind_iew

    params["kind__iew"] = json_kind_iew

    json_kind_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(kind_isw, Unset):
        json_kind_isw = kind_isw

    params["kind__isw"] = json_kind_isw

    json_kind_n: Union[Unset, list[str]] = UNSET
    if not isinstance(kind_n, Unset):
        json_kind_n = kind_n

    params["kind__n"] = json_kind_n

    json_kind_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(kind_nic, Unset):
        json_kind_nic = kind_nic

    params["kind__nic"] = json_kind_nic

    json_kind_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(kind_nie, Unset):
        json_kind_nie = kind_nie

    params["kind__nie"] = json_kind_nie

    json_kind_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(kind_niew, Unset):
        json_kind_niew = kind_niew

    params["kind__niew"] = json_kind_niew

    json_kind_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(kind_nisw, Unset):
        json_kind_nisw = kind_nisw

    params["kind__nisw"] = json_kind_nisw

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

    params["q"] = q

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
        "url": "/api/extras/journal-entries/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedJournalEntryList]:
    if response.status_code == 200:
        response_200 = PaginatedJournalEntryList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedJournalEntryList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    assigned_object_id: Union[Unset, list[int]] = UNSET,
    assigned_object_id_empty: Union[Unset, bool] = UNSET,
    assigned_object_id_gt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_gte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_n: Union[Unset, list[int]] = UNSET,
    assigned_object_type: Union[Unset, str] = UNSET,
    assigned_object_type_n: Union[Unset, str] = UNSET,
    assigned_object_type_id: Union[Unset, list[int]] = UNSET,
    assigned_object_type_id_n: Union[Unset, list[int]] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    created_by: Union[Unset, list[str]] = UNSET,
    created_by_n: Union[Unset, list[str]] = UNSET,
    created_by_id: Union[Unset, list[Union[None, int]]] = UNSET,
    created_by_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    kind: Union[Unset, list[str]] = UNSET,
    kind_empty: Union[Unset, bool] = UNSET,
    kind_ic: Union[Unset, list[str]] = UNSET,
    kind_ie: Union[Unset, list[str]] = UNSET,
    kind_iew: Union[Unset, list[str]] = UNSET,
    kind_isw: Union[Unset, list[str]] = UNSET,
    kind_n: Union[Unset, list[str]] = UNSET,
    kind_nic: Union[Unset, list[str]] = UNSET,
    kind_nie: Union[Unset, list[str]] = UNSET,
    kind_niew: Union[Unset, list[str]] = UNSET,
    kind_nisw: Union[Unset, list[str]] = UNSET,
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
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedJournalEntryList]:
    """Get a list of journal entry objects.

    Args:
        assigned_object_id (Union[Unset, list[int]]):
        assigned_object_id_empty (Union[Unset, bool]):
        assigned_object_id_gt (Union[Unset, list[int]]):
        assigned_object_id_gte (Union[Unset, list[int]]):
        assigned_object_id_lt (Union[Unset, list[int]]):
        assigned_object_id_lte (Union[Unset, list[int]]):
        assigned_object_id_n (Union[Unset, list[int]]):
        assigned_object_type (Union[Unset, str]):
        assigned_object_type_n (Union[Unset, str]):
        assigned_object_type_id (Union[Unset, list[int]]):
        assigned_object_type_id_n (Union[Unset, list[int]]):
        created_after (Union[Unset, datetime.datetime]):
        created_before (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, list[str]]):
        created_by_n (Union[Unset, list[str]]):
        created_by_id (Union[Unset, list[Union[None, int]]]):
        created_by_id_n (Union[Unset, list[Union[None, int]]]):
        created_by_request (Union[Unset, UUID]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        kind (Union[Unset, list[str]]):
        kind_empty (Union[Unset, bool]):
        kind_ic (Union[Unset, list[str]]):
        kind_ie (Union[Unset, list[str]]):
        kind_iew (Union[Unset, list[str]]):
        kind_isw (Union[Unset, list[str]]):
        kind_n (Union[Unset, list[str]]):
        kind_nic (Union[Unset, list[str]]):
        kind_nie (Union[Unset, list[str]]):
        kind_niew (Union[Unset, list[str]]):
        kind_nisw (Union[Unset, list[str]]):
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
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedJournalEntryList]
    """

    kwargs = _get_kwargs(
        assigned_object_id=assigned_object_id,
        assigned_object_id_empty=assigned_object_id_empty,
        assigned_object_id_gt=assigned_object_id_gt,
        assigned_object_id_gte=assigned_object_id_gte,
        assigned_object_id_lt=assigned_object_id_lt,
        assigned_object_id_lte=assigned_object_id_lte,
        assigned_object_id_n=assigned_object_id_n,
        assigned_object_type=assigned_object_type,
        assigned_object_type_n=assigned_object_type_n,
        assigned_object_type_id=assigned_object_type_id,
        assigned_object_type_id_n=assigned_object_type_id_n,
        created_after=created_after,
        created_before=created_before,
        created_by=created_by,
        created_by_n=created_by_n,
        created_by_id=created_by_id,
        created_by_id_n=created_by_id_n,
        created_by_request=created_by_request,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        kind=kind,
        kind_empty=kind_empty,
        kind_ic=kind_ic,
        kind_ie=kind_ie,
        kind_iew=kind_iew,
        kind_isw=kind_isw,
        kind_n=kind_n,
        kind_nic=kind_nic,
        kind_nie=kind_nie,
        kind_niew=kind_niew,
        kind_nisw=kind_nisw,
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
        q=q,
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
    assigned_object_id: Union[Unset, list[int]] = UNSET,
    assigned_object_id_empty: Union[Unset, bool] = UNSET,
    assigned_object_id_gt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_gte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_n: Union[Unset, list[int]] = UNSET,
    assigned_object_type: Union[Unset, str] = UNSET,
    assigned_object_type_n: Union[Unset, str] = UNSET,
    assigned_object_type_id: Union[Unset, list[int]] = UNSET,
    assigned_object_type_id_n: Union[Unset, list[int]] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    created_by: Union[Unset, list[str]] = UNSET,
    created_by_n: Union[Unset, list[str]] = UNSET,
    created_by_id: Union[Unset, list[Union[None, int]]] = UNSET,
    created_by_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    kind: Union[Unset, list[str]] = UNSET,
    kind_empty: Union[Unset, bool] = UNSET,
    kind_ic: Union[Unset, list[str]] = UNSET,
    kind_ie: Union[Unset, list[str]] = UNSET,
    kind_iew: Union[Unset, list[str]] = UNSET,
    kind_isw: Union[Unset, list[str]] = UNSET,
    kind_n: Union[Unset, list[str]] = UNSET,
    kind_nic: Union[Unset, list[str]] = UNSET,
    kind_nie: Union[Unset, list[str]] = UNSET,
    kind_niew: Union[Unset, list[str]] = UNSET,
    kind_nisw: Union[Unset, list[str]] = UNSET,
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
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedJournalEntryList]:
    """Get a list of journal entry objects.

    Args:
        assigned_object_id (Union[Unset, list[int]]):
        assigned_object_id_empty (Union[Unset, bool]):
        assigned_object_id_gt (Union[Unset, list[int]]):
        assigned_object_id_gte (Union[Unset, list[int]]):
        assigned_object_id_lt (Union[Unset, list[int]]):
        assigned_object_id_lte (Union[Unset, list[int]]):
        assigned_object_id_n (Union[Unset, list[int]]):
        assigned_object_type (Union[Unset, str]):
        assigned_object_type_n (Union[Unset, str]):
        assigned_object_type_id (Union[Unset, list[int]]):
        assigned_object_type_id_n (Union[Unset, list[int]]):
        created_after (Union[Unset, datetime.datetime]):
        created_before (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, list[str]]):
        created_by_n (Union[Unset, list[str]]):
        created_by_id (Union[Unset, list[Union[None, int]]]):
        created_by_id_n (Union[Unset, list[Union[None, int]]]):
        created_by_request (Union[Unset, UUID]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        kind (Union[Unset, list[str]]):
        kind_empty (Union[Unset, bool]):
        kind_ic (Union[Unset, list[str]]):
        kind_ie (Union[Unset, list[str]]):
        kind_iew (Union[Unset, list[str]]):
        kind_isw (Union[Unset, list[str]]):
        kind_n (Union[Unset, list[str]]):
        kind_nic (Union[Unset, list[str]]):
        kind_nie (Union[Unset, list[str]]):
        kind_niew (Union[Unset, list[str]]):
        kind_nisw (Union[Unset, list[str]]):
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
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedJournalEntryList
    """

    return sync_detailed(
        client=client,
        assigned_object_id=assigned_object_id,
        assigned_object_id_empty=assigned_object_id_empty,
        assigned_object_id_gt=assigned_object_id_gt,
        assigned_object_id_gte=assigned_object_id_gte,
        assigned_object_id_lt=assigned_object_id_lt,
        assigned_object_id_lte=assigned_object_id_lte,
        assigned_object_id_n=assigned_object_id_n,
        assigned_object_type=assigned_object_type,
        assigned_object_type_n=assigned_object_type_n,
        assigned_object_type_id=assigned_object_type_id,
        assigned_object_type_id_n=assigned_object_type_id_n,
        created_after=created_after,
        created_before=created_before,
        created_by=created_by,
        created_by_n=created_by_n,
        created_by_id=created_by_id,
        created_by_id_n=created_by_id_n,
        created_by_request=created_by_request,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        kind=kind,
        kind_empty=kind_empty,
        kind_ic=kind_ic,
        kind_ie=kind_ie,
        kind_iew=kind_iew,
        kind_isw=kind_isw,
        kind_n=kind_n,
        kind_nic=kind_nic,
        kind_nie=kind_nie,
        kind_niew=kind_niew,
        kind_nisw=kind_nisw,
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
        q=q,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    assigned_object_id: Union[Unset, list[int]] = UNSET,
    assigned_object_id_empty: Union[Unset, bool] = UNSET,
    assigned_object_id_gt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_gte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_n: Union[Unset, list[int]] = UNSET,
    assigned_object_type: Union[Unset, str] = UNSET,
    assigned_object_type_n: Union[Unset, str] = UNSET,
    assigned_object_type_id: Union[Unset, list[int]] = UNSET,
    assigned_object_type_id_n: Union[Unset, list[int]] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    created_by: Union[Unset, list[str]] = UNSET,
    created_by_n: Union[Unset, list[str]] = UNSET,
    created_by_id: Union[Unset, list[Union[None, int]]] = UNSET,
    created_by_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    kind: Union[Unset, list[str]] = UNSET,
    kind_empty: Union[Unset, bool] = UNSET,
    kind_ic: Union[Unset, list[str]] = UNSET,
    kind_ie: Union[Unset, list[str]] = UNSET,
    kind_iew: Union[Unset, list[str]] = UNSET,
    kind_isw: Union[Unset, list[str]] = UNSET,
    kind_n: Union[Unset, list[str]] = UNSET,
    kind_nic: Union[Unset, list[str]] = UNSET,
    kind_nie: Union[Unset, list[str]] = UNSET,
    kind_niew: Union[Unset, list[str]] = UNSET,
    kind_nisw: Union[Unset, list[str]] = UNSET,
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
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedJournalEntryList]:
    """Get a list of journal entry objects.

    Args:
        assigned_object_id (Union[Unset, list[int]]):
        assigned_object_id_empty (Union[Unset, bool]):
        assigned_object_id_gt (Union[Unset, list[int]]):
        assigned_object_id_gte (Union[Unset, list[int]]):
        assigned_object_id_lt (Union[Unset, list[int]]):
        assigned_object_id_lte (Union[Unset, list[int]]):
        assigned_object_id_n (Union[Unset, list[int]]):
        assigned_object_type (Union[Unset, str]):
        assigned_object_type_n (Union[Unset, str]):
        assigned_object_type_id (Union[Unset, list[int]]):
        assigned_object_type_id_n (Union[Unset, list[int]]):
        created_after (Union[Unset, datetime.datetime]):
        created_before (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, list[str]]):
        created_by_n (Union[Unset, list[str]]):
        created_by_id (Union[Unset, list[Union[None, int]]]):
        created_by_id_n (Union[Unset, list[Union[None, int]]]):
        created_by_request (Union[Unset, UUID]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        kind (Union[Unset, list[str]]):
        kind_empty (Union[Unset, bool]):
        kind_ic (Union[Unset, list[str]]):
        kind_ie (Union[Unset, list[str]]):
        kind_iew (Union[Unset, list[str]]):
        kind_isw (Union[Unset, list[str]]):
        kind_n (Union[Unset, list[str]]):
        kind_nic (Union[Unset, list[str]]):
        kind_nie (Union[Unset, list[str]]):
        kind_niew (Union[Unset, list[str]]):
        kind_nisw (Union[Unset, list[str]]):
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
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedJournalEntryList]
    """

    kwargs = _get_kwargs(
        assigned_object_id=assigned_object_id,
        assigned_object_id_empty=assigned_object_id_empty,
        assigned_object_id_gt=assigned_object_id_gt,
        assigned_object_id_gte=assigned_object_id_gte,
        assigned_object_id_lt=assigned_object_id_lt,
        assigned_object_id_lte=assigned_object_id_lte,
        assigned_object_id_n=assigned_object_id_n,
        assigned_object_type=assigned_object_type,
        assigned_object_type_n=assigned_object_type_n,
        assigned_object_type_id=assigned_object_type_id,
        assigned_object_type_id_n=assigned_object_type_id_n,
        created_after=created_after,
        created_before=created_before,
        created_by=created_by,
        created_by_n=created_by_n,
        created_by_id=created_by_id,
        created_by_id_n=created_by_id_n,
        created_by_request=created_by_request,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        kind=kind,
        kind_empty=kind_empty,
        kind_ic=kind_ic,
        kind_ie=kind_ie,
        kind_iew=kind_iew,
        kind_isw=kind_isw,
        kind_n=kind_n,
        kind_nic=kind_nic,
        kind_nie=kind_nie,
        kind_niew=kind_niew,
        kind_nisw=kind_nisw,
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
        q=q,
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
    assigned_object_id: Union[Unset, list[int]] = UNSET,
    assigned_object_id_empty: Union[Unset, bool] = UNSET,
    assigned_object_id_gt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_gte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_n: Union[Unset, list[int]] = UNSET,
    assigned_object_type: Union[Unset, str] = UNSET,
    assigned_object_type_n: Union[Unset, str] = UNSET,
    assigned_object_type_id: Union[Unset, list[int]] = UNSET,
    assigned_object_type_id_n: Union[Unset, list[int]] = UNSET,
    created_after: Union[Unset, datetime.datetime] = UNSET,
    created_before: Union[Unset, datetime.datetime] = UNSET,
    created_by: Union[Unset, list[str]] = UNSET,
    created_by_n: Union[Unset, list[str]] = UNSET,
    created_by_id: Union[Unset, list[Union[None, int]]] = UNSET,
    created_by_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    kind: Union[Unset, list[str]] = UNSET,
    kind_empty: Union[Unset, bool] = UNSET,
    kind_ic: Union[Unset, list[str]] = UNSET,
    kind_ie: Union[Unset, list[str]] = UNSET,
    kind_iew: Union[Unset, list[str]] = UNSET,
    kind_isw: Union[Unset, list[str]] = UNSET,
    kind_n: Union[Unset, list[str]] = UNSET,
    kind_nic: Union[Unset, list[str]] = UNSET,
    kind_nie: Union[Unset, list[str]] = UNSET,
    kind_niew: Union[Unset, list[str]] = UNSET,
    kind_nisw: Union[Unset, list[str]] = UNSET,
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
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedJournalEntryList]:
    """Get a list of journal entry objects.

    Args:
        assigned_object_id (Union[Unset, list[int]]):
        assigned_object_id_empty (Union[Unset, bool]):
        assigned_object_id_gt (Union[Unset, list[int]]):
        assigned_object_id_gte (Union[Unset, list[int]]):
        assigned_object_id_lt (Union[Unset, list[int]]):
        assigned_object_id_lte (Union[Unset, list[int]]):
        assigned_object_id_n (Union[Unset, list[int]]):
        assigned_object_type (Union[Unset, str]):
        assigned_object_type_n (Union[Unset, str]):
        assigned_object_type_id (Union[Unset, list[int]]):
        assigned_object_type_id_n (Union[Unset, list[int]]):
        created_after (Union[Unset, datetime.datetime]):
        created_before (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, list[str]]):
        created_by_n (Union[Unset, list[str]]):
        created_by_id (Union[Unset, list[Union[None, int]]]):
        created_by_id_n (Union[Unset, list[Union[None, int]]]):
        created_by_request (Union[Unset, UUID]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        kind (Union[Unset, list[str]]):
        kind_empty (Union[Unset, bool]):
        kind_ic (Union[Unset, list[str]]):
        kind_ie (Union[Unset, list[str]]):
        kind_iew (Union[Unset, list[str]]):
        kind_isw (Union[Unset, list[str]]):
        kind_n (Union[Unset, list[str]]):
        kind_nic (Union[Unset, list[str]]):
        kind_nie (Union[Unset, list[str]]):
        kind_niew (Union[Unset, list[str]]):
        kind_nisw (Union[Unset, list[str]]):
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
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedJournalEntryList
    """

    return (
        await asyncio_detailed(
            client=client,
            assigned_object_id=assigned_object_id,
            assigned_object_id_empty=assigned_object_id_empty,
            assigned_object_id_gt=assigned_object_id_gt,
            assigned_object_id_gte=assigned_object_id_gte,
            assigned_object_id_lt=assigned_object_id_lt,
            assigned_object_id_lte=assigned_object_id_lte,
            assigned_object_id_n=assigned_object_id_n,
            assigned_object_type=assigned_object_type,
            assigned_object_type_n=assigned_object_type_n,
            assigned_object_type_id=assigned_object_type_id,
            assigned_object_type_id_n=assigned_object_type_id_n,
            created_after=created_after,
            created_before=created_before,
            created_by=created_by,
            created_by_n=created_by_n,
            created_by_id=created_by_id,
            created_by_id_n=created_by_id_n,
            created_by_request=created_by_request,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            kind=kind,
            kind_empty=kind_empty,
            kind_ic=kind_ic,
            kind_ie=kind_ie,
            kind_iew=kind_iew,
            kind_isw=kind_isw,
            kind_n=kind_n,
            kind_nic=kind_nic,
            kind_nie=kind_nie,
            kind_niew=kind_niew,
            kind_nisw=kind_nisw,
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
            q=q,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
            updated_by_request=updated_by_request,
        )
    ).parsed
