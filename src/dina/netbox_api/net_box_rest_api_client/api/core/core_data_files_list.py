import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_data_file_list import PaginatedDataFileList
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
    hash_: Union[Unset, list[str]] = UNSET,
    hash_empty: Union[Unset, bool] = UNSET,
    hash_ic: Union[Unset, list[str]] = UNSET,
    hash_ie: Union[Unset, list[str]] = UNSET,
    hash_iew: Union[Unset, list[str]] = UNSET,
    hash_isw: Union[Unset, list[str]] = UNSET,
    hash_n: Union[Unset, list[str]] = UNSET,
    hash_nic: Union[Unset, list[str]] = UNSET,
    hash_nie: Union[Unset, list[str]] = UNSET,
    hash_niew: Union[Unset, list[str]] = UNSET,
    hash_nisw: Union[Unset, list[str]] = UNSET,
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
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    path: Union[Unset, list[str]] = UNSET,
    path_empty: Union[Unset, bool] = UNSET,
    path_ic: Union[Unset, list[str]] = UNSET,
    path_ie: Union[Unset, list[str]] = UNSET,
    path_iew: Union[Unset, list[str]] = UNSET,
    path_isw: Union[Unset, list[str]] = UNSET,
    path_n: Union[Unset, list[str]] = UNSET,
    path_nic: Union[Unset, list[str]] = UNSET,
    path_nie: Union[Unset, list[str]] = UNSET,
    path_niew: Union[Unset, list[str]] = UNSET,
    path_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    size: Union[Unset, list[int]] = UNSET,
    size_empty: Union[Unset, bool] = UNSET,
    size_gt: Union[Unset, list[int]] = UNSET,
    size_gte: Union[Unset, list[int]] = UNSET,
    size_lt: Union[Unset, list[int]] = UNSET,
    size_lte: Union[Unset, list[int]] = UNSET,
    size_n: Union[Unset, list[int]] = UNSET,
    source: Union[Unset, list[str]] = UNSET,
    source_n: Union[Unset, list[str]] = UNSET,
    source_id: Union[Unset, list[int]] = UNSET,
    source_id_n: Union[Unset, list[int]] = UNSET,
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

    json_hash_: Union[Unset, list[str]] = UNSET
    if not isinstance(hash_, Unset):
        json_hash_ = hash_

    params["hash"] = json_hash_

    params["hash__empty"] = hash_empty

    json_hash_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(hash_ic, Unset):
        json_hash_ic = hash_ic

    params["hash__ic"] = json_hash_ic

    json_hash_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(hash_ie, Unset):
        json_hash_ie = hash_ie

    params["hash__ie"] = json_hash_ie

    json_hash_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(hash_iew, Unset):
        json_hash_iew = hash_iew

    params["hash__iew"] = json_hash_iew

    json_hash_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(hash_isw, Unset):
        json_hash_isw = hash_isw

    params["hash__isw"] = json_hash_isw

    json_hash_n: Union[Unset, list[str]] = UNSET
    if not isinstance(hash_n, Unset):
        json_hash_n = hash_n

    params["hash__n"] = json_hash_n

    json_hash_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(hash_nic, Unset):
        json_hash_nic = hash_nic

    params["hash__nic"] = json_hash_nic

    json_hash_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(hash_nie, Unset):
        json_hash_nie = hash_nie

    params["hash__nie"] = json_hash_nie

    json_hash_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(hash_niew, Unset):
        json_hash_niew = hash_niew

    params["hash__niew"] = json_hash_niew

    json_hash_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(hash_nisw, Unset):
        json_hash_nisw = hash_nisw

    params["hash__nisw"] = json_hash_nisw

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

    params["offset"] = offset

    params["ordering"] = ordering

    json_path: Union[Unset, list[str]] = UNSET
    if not isinstance(path, Unset):
        json_path = path

    params["path"] = json_path

    params["path__empty"] = path_empty

    json_path_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(path_ic, Unset):
        json_path_ic = path_ic

    params["path__ic"] = json_path_ic

    json_path_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(path_ie, Unset):
        json_path_ie = path_ie

    params["path__ie"] = json_path_ie

    json_path_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(path_iew, Unset):
        json_path_iew = path_iew

    params["path__iew"] = json_path_iew

    json_path_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(path_isw, Unset):
        json_path_isw = path_isw

    params["path__isw"] = json_path_isw

    json_path_n: Union[Unset, list[str]] = UNSET
    if not isinstance(path_n, Unset):
        json_path_n = path_n

    params["path__n"] = json_path_n

    json_path_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(path_nic, Unset):
        json_path_nic = path_nic

    params["path__nic"] = json_path_nic

    json_path_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(path_nie, Unset):
        json_path_nie = path_nie

    params["path__nie"] = json_path_nie

    json_path_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(path_niew, Unset):
        json_path_niew = path_niew

    params["path__niew"] = json_path_niew

    json_path_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(path_nisw, Unset):
        json_path_nisw = path_nisw

    params["path__nisw"] = json_path_nisw

    params["q"] = q

    json_size: Union[Unset, list[int]] = UNSET
    if not isinstance(size, Unset):
        json_size = size

    params["size"] = json_size

    params["size__empty"] = size_empty

    json_size_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(size_gt, Unset):
        json_size_gt = size_gt

    params["size__gt"] = json_size_gt

    json_size_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(size_gte, Unset):
        json_size_gte = size_gte

    params["size__gte"] = json_size_gte

    json_size_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(size_lt, Unset):
        json_size_lt = size_lt

    params["size__lt"] = json_size_lt

    json_size_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(size_lte, Unset):
        json_size_lte = size_lte

    params["size__lte"] = json_size_lte

    json_size_n: Union[Unset, list[int]] = UNSET
    if not isinstance(size_n, Unset):
        json_size_n = size_n

    params["size__n"] = json_size_n

    json_source: Union[Unset, list[str]] = UNSET
    if not isinstance(source, Unset):
        json_source = source

    params["source"] = json_source

    json_source_n: Union[Unset, list[str]] = UNSET
    if not isinstance(source_n, Unset):
        json_source_n = source_n

    params["source__n"] = json_source_n

    json_source_id: Union[Unset, list[int]] = UNSET
    if not isinstance(source_id, Unset):
        json_source_id = source_id

    params["source_id"] = json_source_id

    json_source_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(source_id_n, Unset):
        json_source_id_n = source_id_n

    params["source_id__n"] = json_source_id_n

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/core/data-files/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedDataFileList]:
    if response.status_code == 200:
        response_200 = PaginatedDataFileList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedDataFileList]:
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
    hash_: Union[Unset, list[str]] = UNSET,
    hash_empty: Union[Unset, bool] = UNSET,
    hash_ic: Union[Unset, list[str]] = UNSET,
    hash_ie: Union[Unset, list[str]] = UNSET,
    hash_iew: Union[Unset, list[str]] = UNSET,
    hash_isw: Union[Unset, list[str]] = UNSET,
    hash_n: Union[Unset, list[str]] = UNSET,
    hash_nic: Union[Unset, list[str]] = UNSET,
    hash_nie: Union[Unset, list[str]] = UNSET,
    hash_niew: Union[Unset, list[str]] = UNSET,
    hash_nisw: Union[Unset, list[str]] = UNSET,
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
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    path: Union[Unset, list[str]] = UNSET,
    path_empty: Union[Unset, bool] = UNSET,
    path_ic: Union[Unset, list[str]] = UNSET,
    path_ie: Union[Unset, list[str]] = UNSET,
    path_iew: Union[Unset, list[str]] = UNSET,
    path_isw: Union[Unset, list[str]] = UNSET,
    path_n: Union[Unset, list[str]] = UNSET,
    path_nic: Union[Unset, list[str]] = UNSET,
    path_nie: Union[Unset, list[str]] = UNSET,
    path_niew: Union[Unset, list[str]] = UNSET,
    path_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    size: Union[Unset, list[int]] = UNSET,
    size_empty: Union[Unset, bool] = UNSET,
    size_gt: Union[Unset, list[int]] = UNSET,
    size_gte: Union[Unset, list[int]] = UNSET,
    size_lt: Union[Unset, list[int]] = UNSET,
    size_lte: Union[Unset, list[int]] = UNSET,
    size_n: Union[Unset, list[int]] = UNSET,
    source: Union[Unset, list[str]] = UNSET,
    source_n: Union[Unset, list[str]] = UNSET,
    source_id: Union[Unset, list[int]] = UNSET,
    source_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedDataFileList]:
    """Get a list of data file objects.

    Args:
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        hash_ (Union[Unset, list[str]]):
        hash_empty (Union[Unset, bool]):
        hash_ic (Union[Unset, list[str]]):
        hash_ie (Union[Unset, list[str]]):
        hash_iew (Union[Unset, list[str]]):
        hash_isw (Union[Unset, list[str]]):
        hash_n (Union[Unset, list[str]]):
        hash_nic (Union[Unset, list[str]]):
        hash_nie (Union[Unset, list[str]]):
        hash_niew (Union[Unset, list[str]]):
        hash_nisw (Union[Unset, list[str]]):
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
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        path (Union[Unset, list[str]]):
        path_empty (Union[Unset, bool]):
        path_ic (Union[Unset, list[str]]):
        path_ie (Union[Unset, list[str]]):
        path_iew (Union[Unset, list[str]]):
        path_isw (Union[Unset, list[str]]):
        path_n (Union[Unset, list[str]]):
        path_nic (Union[Unset, list[str]]):
        path_nie (Union[Unset, list[str]]):
        path_niew (Union[Unset, list[str]]):
        path_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        size (Union[Unset, list[int]]):
        size_empty (Union[Unset, bool]):
        size_gt (Union[Unset, list[int]]):
        size_gte (Union[Unset, list[int]]):
        size_lt (Union[Unset, list[int]]):
        size_lte (Union[Unset, list[int]]):
        size_n (Union[Unset, list[int]]):
        source (Union[Unset, list[str]]):
        source_n (Union[Unset, list[str]]):
        source_id (Union[Unset, list[int]]):
        source_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDataFileList]
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
        hash_=hash_,
        hash_empty=hash_empty,
        hash_ic=hash_ic,
        hash_ie=hash_ie,
        hash_iew=hash_iew,
        hash_isw=hash_isw,
        hash_n=hash_n,
        hash_nic=hash_nic,
        hash_nie=hash_nie,
        hash_niew=hash_niew,
        hash_nisw=hash_nisw,
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
        offset=offset,
        ordering=ordering,
        path=path,
        path_empty=path_empty,
        path_ic=path_ic,
        path_ie=path_ie,
        path_iew=path_iew,
        path_isw=path_isw,
        path_n=path_n,
        path_nic=path_nic,
        path_nie=path_nie,
        path_niew=path_niew,
        path_nisw=path_nisw,
        q=q,
        size=size,
        size_empty=size_empty,
        size_gt=size_gt,
        size_gte=size_gte,
        size_lt=size_lt,
        size_lte=size_lte,
        size_n=size_n,
        source=source,
        source_n=source_n,
        source_id=source_id,
        source_id_n=source_id_n,
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
    hash_: Union[Unset, list[str]] = UNSET,
    hash_empty: Union[Unset, bool] = UNSET,
    hash_ic: Union[Unset, list[str]] = UNSET,
    hash_ie: Union[Unset, list[str]] = UNSET,
    hash_iew: Union[Unset, list[str]] = UNSET,
    hash_isw: Union[Unset, list[str]] = UNSET,
    hash_n: Union[Unset, list[str]] = UNSET,
    hash_nic: Union[Unset, list[str]] = UNSET,
    hash_nie: Union[Unset, list[str]] = UNSET,
    hash_niew: Union[Unset, list[str]] = UNSET,
    hash_nisw: Union[Unset, list[str]] = UNSET,
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
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    path: Union[Unset, list[str]] = UNSET,
    path_empty: Union[Unset, bool] = UNSET,
    path_ic: Union[Unset, list[str]] = UNSET,
    path_ie: Union[Unset, list[str]] = UNSET,
    path_iew: Union[Unset, list[str]] = UNSET,
    path_isw: Union[Unset, list[str]] = UNSET,
    path_n: Union[Unset, list[str]] = UNSET,
    path_nic: Union[Unset, list[str]] = UNSET,
    path_nie: Union[Unset, list[str]] = UNSET,
    path_niew: Union[Unset, list[str]] = UNSET,
    path_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    size: Union[Unset, list[int]] = UNSET,
    size_empty: Union[Unset, bool] = UNSET,
    size_gt: Union[Unset, list[int]] = UNSET,
    size_gte: Union[Unset, list[int]] = UNSET,
    size_lt: Union[Unset, list[int]] = UNSET,
    size_lte: Union[Unset, list[int]] = UNSET,
    size_n: Union[Unset, list[int]] = UNSET,
    source: Union[Unset, list[str]] = UNSET,
    source_n: Union[Unset, list[str]] = UNSET,
    source_id: Union[Unset, list[int]] = UNSET,
    source_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedDataFileList]:
    """Get a list of data file objects.

    Args:
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        hash_ (Union[Unset, list[str]]):
        hash_empty (Union[Unset, bool]):
        hash_ic (Union[Unset, list[str]]):
        hash_ie (Union[Unset, list[str]]):
        hash_iew (Union[Unset, list[str]]):
        hash_isw (Union[Unset, list[str]]):
        hash_n (Union[Unset, list[str]]):
        hash_nic (Union[Unset, list[str]]):
        hash_nie (Union[Unset, list[str]]):
        hash_niew (Union[Unset, list[str]]):
        hash_nisw (Union[Unset, list[str]]):
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
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        path (Union[Unset, list[str]]):
        path_empty (Union[Unset, bool]):
        path_ic (Union[Unset, list[str]]):
        path_ie (Union[Unset, list[str]]):
        path_iew (Union[Unset, list[str]]):
        path_isw (Union[Unset, list[str]]):
        path_n (Union[Unset, list[str]]):
        path_nic (Union[Unset, list[str]]):
        path_nie (Union[Unset, list[str]]):
        path_niew (Union[Unset, list[str]]):
        path_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        size (Union[Unset, list[int]]):
        size_empty (Union[Unset, bool]):
        size_gt (Union[Unset, list[int]]):
        size_gte (Union[Unset, list[int]]):
        size_lt (Union[Unset, list[int]]):
        size_lte (Union[Unset, list[int]]):
        size_n (Union[Unset, list[int]]):
        source (Union[Unset, list[str]]):
        source_n (Union[Unset, list[str]]):
        source_id (Union[Unset, list[int]]):
        source_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDataFileList
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
        hash_=hash_,
        hash_empty=hash_empty,
        hash_ic=hash_ic,
        hash_ie=hash_ie,
        hash_iew=hash_iew,
        hash_isw=hash_isw,
        hash_n=hash_n,
        hash_nic=hash_nic,
        hash_nie=hash_nie,
        hash_niew=hash_niew,
        hash_nisw=hash_nisw,
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
        offset=offset,
        ordering=ordering,
        path=path,
        path_empty=path_empty,
        path_ic=path_ic,
        path_ie=path_ie,
        path_iew=path_iew,
        path_isw=path_isw,
        path_n=path_n,
        path_nic=path_nic,
        path_nie=path_nie,
        path_niew=path_niew,
        path_nisw=path_nisw,
        q=q,
        size=size,
        size_empty=size_empty,
        size_gt=size_gt,
        size_gte=size_gte,
        size_lt=size_lt,
        size_lte=size_lte,
        size_n=size_n,
        source=source,
        source_n=source_n,
        source_id=source_id,
        source_id_n=source_id_n,
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
    hash_: Union[Unset, list[str]] = UNSET,
    hash_empty: Union[Unset, bool] = UNSET,
    hash_ic: Union[Unset, list[str]] = UNSET,
    hash_ie: Union[Unset, list[str]] = UNSET,
    hash_iew: Union[Unset, list[str]] = UNSET,
    hash_isw: Union[Unset, list[str]] = UNSET,
    hash_n: Union[Unset, list[str]] = UNSET,
    hash_nic: Union[Unset, list[str]] = UNSET,
    hash_nie: Union[Unset, list[str]] = UNSET,
    hash_niew: Union[Unset, list[str]] = UNSET,
    hash_nisw: Union[Unset, list[str]] = UNSET,
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
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    path: Union[Unset, list[str]] = UNSET,
    path_empty: Union[Unset, bool] = UNSET,
    path_ic: Union[Unset, list[str]] = UNSET,
    path_ie: Union[Unset, list[str]] = UNSET,
    path_iew: Union[Unset, list[str]] = UNSET,
    path_isw: Union[Unset, list[str]] = UNSET,
    path_n: Union[Unset, list[str]] = UNSET,
    path_nic: Union[Unset, list[str]] = UNSET,
    path_nie: Union[Unset, list[str]] = UNSET,
    path_niew: Union[Unset, list[str]] = UNSET,
    path_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    size: Union[Unset, list[int]] = UNSET,
    size_empty: Union[Unset, bool] = UNSET,
    size_gt: Union[Unset, list[int]] = UNSET,
    size_gte: Union[Unset, list[int]] = UNSET,
    size_lt: Union[Unset, list[int]] = UNSET,
    size_lte: Union[Unset, list[int]] = UNSET,
    size_n: Union[Unset, list[int]] = UNSET,
    source: Union[Unset, list[str]] = UNSET,
    source_n: Union[Unset, list[str]] = UNSET,
    source_id: Union[Unset, list[int]] = UNSET,
    source_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedDataFileList]:
    """Get a list of data file objects.

    Args:
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        hash_ (Union[Unset, list[str]]):
        hash_empty (Union[Unset, bool]):
        hash_ic (Union[Unset, list[str]]):
        hash_ie (Union[Unset, list[str]]):
        hash_iew (Union[Unset, list[str]]):
        hash_isw (Union[Unset, list[str]]):
        hash_n (Union[Unset, list[str]]):
        hash_nic (Union[Unset, list[str]]):
        hash_nie (Union[Unset, list[str]]):
        hash_niew (Union[Unset, list[str]]):
        hash_nisw (Union[Unset, list[str]]):
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
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        path (Union[Unset, list[str]]):
        path_empty (Union[Unset, bool]):
        path_ic (Union[Unset, list[str]]):
        path_ie (Union[Unset, list[str]]):
        path_iew (Union[Unset, list[str]]):
        path_isw (Union[Unset, list[str]]):
        path_n (Union[Unset, list[str]]):
        path_nic (Union[Unset, list[str]]):
        path_nie (Union[Unset, list[str]]):
        path_niew (Union[Unset, list[str]]):
        path_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        size (Union[Unset, list[int]]):
        size_empty (Union[Unset, bool]):
        size_gt (Union[Unset, list[int]]):
        size_gte (Union[Unset, list[int]]):
        size_lt (Union[Unset, list[int]]):
        size_lte (Union[Unset, list[int]]):
        size_n (Union[Unset, list[int]]):
        source (Union[Unset, list[str]]):
        source_n (Union[Unset, list[str]]):
        source_id (Union[Unset, list[int]]):
        source_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDataFileList]
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
        hash_=hash_,
        hash_empty=hash_empty,
        hash_ic=hash_ic,
        hash_ie=hash_ie,
        hash_iew=hash_iew,
        hash_isw=hash_isw,
        hash_n=hash_n,
        hash_nic=hash_nic,
        hash_nie=hash_nie,
        hash_niew=hash_niew,
        hash_nisw=hash_nisw,
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
        offset=offset,
        ordering=ordering,
        path=path,
        path_empty=path_empty,
        path_ic=path_ic,
        path_ie=path_ie,
        path_iew=path_iew,
        path_isw=path_isw,
        path_n=path_n,
        path_nic=path_nic,
        path_nie=path_nie,
        path_niew=path_niew,
        path_nisw=path_nisw,
        q=q,
        size=size,
        size_empty=size_empty,
        size_gt=size_gt,
        size_gte=size_gte,
        size_lt=size_lt,
        size_lte=size_lte,
        size_n=size_n,
        source=source,
        source_n=source_n,
        source_id=source_id,
        source_id_n=source_id_n,
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
    hash_: Union[Unset, list[str]] = UNSET,
    hash_empty: Union[Unset, bool] = UNSET,
    hash_ic: Union[Unset, list[str]] = UNSET,
    hash_ie: Union[Unset, list[str]] = UNSET,
    hash_iew: Union[Unset, list[str]] = UNSET,
    hash_isw: Union[Unset, list[str]] = UNSET,
    hash_n: Union[Unset, list[str]] = UNSET,
    hash_nic: Union[Unset, list[str]] = UNSET,
    hash_nie: Union[Unset, list[str]] = UNSET,
    hash_niew: Union[Unset, list[str]] = UNSET,
    hash_nisw: Union[Unset, list[str]] = UNSET,
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
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    path: Union[Unset, list[str]] = UNSET,
    path_empty: Union[Unset, bool] = UNSET,
    path_ic: Union[Unset, list[str]] = UNSET,
    path_ie: Union[Unset, list[str]] = UNSET,
    path_iew: Union[Unset, list[str]] = UNSET,
    path_isw: Union[Unset, list[str]] = UNSET,
    path_n: Union[Unset, list[str]] = UNSET,
    path_nic: Union[Unset, list[str]] = UNSET,
    path_nie: Union[Unset, list[str]] = UNSET,
    path_niew: Union[Unset, list[str]] = UNSET,
    path_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    size: Union[Unset, list[int]] = UNSET,
    size_empty: Union[Unset, bool] = UNSET,
    size_gt: Union[Unset, list[int]] = UNSET,
    size_gte: Union[Unset, list[int]] = UNSET,
    size_lt: Union[Unset, list[int]] = UNSET,
    size_lte: Union[Unset, list[int]] = UNSET,
    size_n: Union[Unset, list[int]] = UNSET,
    source: Union[Unset, list[str]] = UNSET,
    source_n: Union[Unset, list[str]] = UNSET,
    source_id: Union[Unset, list[int]] = UNSET,
    source_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedDataFileList]:
    """Get a list of data file objects.

    Args:
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        hash_ (Union[Unset, list[str]]):
        hash_empty (Union[Unset, bool]):
        hash_ic (Union[Unset, list[str]]):
        hash_ie (Union[Unset, list[str]]):
        hash_iew (Union[Unset, list[str]]):
        hash_isw (Union[Unset, list[str]]):
        hash_n (Union[Unset, list[str]]):
        hash_nic (Union[Unset, list[str]]):
        hash_nie (Union[Unset, list[str]]):
        hash_niew (Union[Unset, list[str]]):
        hash_nisw (Union[Unset, list[str]]):
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
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        path (Union[Unset, list[str]]):
        path_empty (Union[Unset, bool]):
        path_ic (Union[Unset, list[str]]):
        path_ie (Union[Unset, list[str]]):
        path_iew (Union[Unset, list[str]]):
        path_isw (Union[Unset, list[str]]):
        path_n (Union[Unset, list[str]]):
        path_nic (Union[Unset, list[str]]):
        path_nie (Union[Unset, list[str]]):
        path_niew (Union[Unset, list[str]]):
        path_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        size (Union[Unset, list[int]]):
        size_empty (Union[Unset, bool]):
        size_gt (Union[Unset, list[int]]):
        size_gte (Union[Unset, list[int]]):
        size_lt (Union[Unset, list[int]]):
        size_lte (Union[Unset, list[int]]):
        size_n (Union[Unset, list[int]]):
        source (Union[Unset, list[str]]):
        source_n (Union[Unset, list[str]]):
        source_id (Union[Unset, list[int]]):
        source_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDataFileList
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
            hash_=hash_,
            hash_empty=hash_empty,
            hash_ic=hash_ic,
            hash_ie=hash_ie,
            hash_iew=hash_iew,
            hash_isw=hash_isw,
            hash_n=hash_n,
            hash_nic=hash_nic,
            hash_nie=hash_nie,
            hash_niew=hash_niew,
            hash_nisw=hash_nisw,
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
            offset=offset,
            ordering=ordering,
            path=path,
            path_empty=path_empty,
            path_ic=path_ic,
            path_ie=path_ie,
            path_iew=path_iew,
            path_isw=path_isw,
            path_n=path_n,
            path_nic=path_nic,
            path_nie=path_nie,
            path_niew=path_niew,
            path_nisw=path_nisw,
            q=q,
            size=size,
            size_empty=size_empty,
            size_gt=size_gt,
            size_gte=size_gte,
            size_lt=size_lt,
            size_lte=size_lte,
            size_n=size_n,
            source=source,
            source_n=source_n,
            source_id=source_id,
            source_id_n=source_id_n,
            updated_by_request=updated_by_request,
        )
    ).parsed
