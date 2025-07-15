import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_file_hash_list import PaginatedFileHashList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    algorithm: Union[Unset, list[str]] = UNSET,
    algorithm_empty: Union[Unset, bool] = UNSET,
    algorithm_ic: Union[Unset, list[str]] = UNSET,
    algorithm_ie: Union[Unset, list[str]] = UNSET,
    algorithm_iew: Union[Unset, list[str]] = UNSET,
    algorithm_isw: Union[Unset, list[str]] = UNSET,
    algorithm_n: Union[Unset, list[str]] = UNSET,
    algorithm_nic: Union[Unset, list[str]] = UNSET,
    algorithm_nie: Union[Unset, list[str]] = UNSET,
    algorithm_niew: Union[Unset, list[str]] = UNSET,
    algorithm_nisw: Union[Unset, list[str]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    hash_: Union[Unset, int] = UNSET,
    hash_n: Union[Unset, int] = UNSET,
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
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    value: Union[Unset, list[str]] = UNSET,
    value_empty: Union[Unset, bool] = UNSET,
    value_ic: Union[Unset, list[str]] = UNSET,
    value_ie: Union[Unset, list[str]] = UNSET,
    value_iew: Union[Unset, list[str]] = UNSET,
    value_isw: Union[Unset, list[str]] = UNSET,
    value_n: Union[Unset, list[str]] = UNSET,
    value_nic: Union[Unset, list[str]] = UNSET,
    value_nie: Union[Unset, list[str]] = UNSET,
    value_niew: Union[Unset, list[str]] = UNSET,
    value_nisw: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_algorithm: Union[Unset, list[str]] = UNSET
    if not isinstance(algorithm, Unset):
        json_algorithm = algorithm

    params["algorithm"] = json_algorithm

    params["algorithm__empty"] = algorithm_empty

    json_algorithm_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(algorithm_ic, Unset):
        json_algorithm_ic = algorithm_ic

    params["algorithm__ic"] = json_algorithm_ic

    json_algorithm_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(algorithm_ie, Unset):
        json_algorithm_ie = algorithm_ie

    params["algorithm__ie"] = json_algorithm_ie

    json_algorithm_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(algorithm_iew, Unset):
        json_algorithm_iew = algorithm_iew

    params["algorithm__iew"] = json_algorithm_iew

    json_algorithm_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(algorithm_isw, Unset):
        json_algorithm_isw = algorithm_isw

    params["algorithm__isw"] = json_algorithm_isw

    json_algorithm_n: Union[Unset, list[str]] = UNSET
    if not isinstance(algorithm_n, Unset):
        json_algorithm_n = algorithm_n

    params["algorithm__n"] = json_algorithm_n

    json_algorithm_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(algorithm_nic, Unset):
        json_algorithm_nic = algorithm_nic

    params["algorithm__nic"] = json_algorithm_nic

    json_algorithm_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(algorithm_nie, Unset):
        json_algorithm_nie = algorithm_nie

    params["algorithm__nie"] = json_algorithm_nie

    json_algorithm_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(algorithm_niew, Unset):
        json_algorithm_niew = algorithm_niew

    params["algorithm__niew"] = json_algorithm_niew

    json_algorithm_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(algorithm_nisw, Unset):
        json_algorithm_nisw = algorithm_nisw

    params["algorithm__nisw"] = json_algorithm_nisw

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

    params["hash"] = hash_

    params["hash__n"] = hash_n

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

    json_value: Union[Unset, list[str]] = UNSET
    if not isinstance(value, Unset):
        json_value = value

    params["value"] = json_value

    params["value__empty"] = value_empty

    json_value_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(value_ic, Unset):
        json_value_ic = value_ic

    params["value__ic"] = json_value_ic

    json_value_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(value_ie, Unset):
        json_value_ie = value_ie

    params["value__ie"] = json_value_ie

    json_value_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(value_iew, Unset):
        json_value_iew = value_iew

    params["value__iew"] = json_value_iew

    json_value_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(value_isw, Unset):
        json_value_isw = value_isw

    params["value__isw"] = json_value_isw

    json_value_n: Union[Unset, list[str]] = UNSET
    if not isinstance(value_n, Unset):
        json_value_n = value_n

    params["value__n"] = json_value_n

    json_value_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(value_nic, Unset):
        json_value_nic = value_nic

    params["value__nic"] = json_value_nic

    json_value_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(value_nie, Unset):
        json_value_nie = value_nie

    params["value__nie"] = json_value_nie

    json_value_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(value_niew, Unset):
        json_value_niew = value_niew

    params["value__niew"] = json_value_niew

    json_value_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(value_nisw, Unset):
        json_value_nisw = value_nisw

    params["value__nisw"] = json_value_nisw

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/plugins/d3c/filehash-list/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedFileHashList]:
    if response.status_code == 200:
        response_200 = PaginatedFileHashList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedFileHashList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    algorithm: Union[Unset, list[str]] = UNSET,
    algorithm_empty: Union[Unset, bool] = UNSET,
    algorithm_ic: Union[Unset, list[str]] = UNSET,
    algorithm_ie: Union[Unset, list[str]] = UNSET,
    algorithm_iew: Union[Unset, list[str]] = UNSET,
    algorithm_isw: Union[Unset, list[str]] = UNSET,
    algorithm_n: Union[Unset, list[str]] = UNSET,
    algorithm_nic: Union[Unset, list[str]] = UNSET,
    algorithm_nie: Union[Unset, list[str]] = UNSET,
    algorithm_niew: Union[Unset, list[str]] = UNSET,
    algorithm_nisw: Union[Unset, list[str]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    hash_: Union[Unset, int] = UNSET,
    hash_n: Union[Unset, int] = UNSET,
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
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    value: Union[Unset, list[str]] = UNSET,
    value_empty: Union[Unset, bool] = UNSET,
    value_ic: Union[Unset, list[str]] = UNSET,
    value_ie: Union[Unset, list[str]] = UNSET,
    value_iew: Union[Unset, list[str]] = UNSET,
    value_isw: Union[Unset, list[str]] = UNSET,
    value_n: Union[Unset, list[str]] = UNSET,
    value_nic: Union[Unset, list[str]] = UNSET,
    value_nie: Union[Unset, list[str]] = UNSET,
    value_niew: Union[Unset, list[str]] = UNSET,
    value_nisw: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedFileHashList]:
    """ViewSet for XGenericUri.

    Args:
        algorithm (Union[Unset, list[str]]):
        algorithm_empty (Union[Unset, bool]):
        algorithm_ic (Union[Unset, list[str]]):
        algorithm_ie (Union[Unset, list[str]]):
        algorithm_iew (Union[Unset, list[str]]):
        algorithm_isw (Union[Unset, list[str]]):
        algorithm_n (Union[Unset, list[str]]):
        algorithm_nic (Union[Unset, list[str]]):
        algorithm_nie (Union[Unset, list[str]]):
        algorithm_niew (Union[Unset, list[str]]):
        algorithm_nisw (Union[Unset, list[str]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        hash_ (Union[Unset, int]):
        hash_n (Union[Unset, int]):
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
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        value (Union[Unset, list[str]]):
        value_empty (Union[Unset, bool]):
        value_ic (Union[Unset, list[str]]):
        value_ie (Union[Unset, list[str]]):
        value_iew (Union[Unset, list[str]]):
        value_isw (Union[Unset, list[str]]):
        value_n (Union[Unset, list[str]]):
        value_nic (Union[Unset, list[str]]):
        value_nie (Union[Unset, list[str]]):
        value_niew (Union[Unset, list[str]]):
        value_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedFileHashList]
    """

    kwargs = _get_kwargs(
        algorithm=algorithm,
        algorithm_empty=algorithm_empty,
        algorithm_ic=algorithm_ic,
        algorithm_ie=algorithm_ie,
        algorithm_iew=algorithm_iew,
        algorithm_isw=algorithm_isw,
        algorithm_n=algorithm_n,
        algorithm_nic=algorithm_nic,
        algorithm_nie=algorithm_nie,
        algorithm_niew=algorithm_niew,
        algorithm_nisw=algorithm_nisw,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        hash_=hash_,
        hash_n=hash_n,
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
        q=q,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
        value=value,
        value_empty=value_empty,
        value_ic=value_ic,
        value_ie=value_ie,
        value_iew=value_iew,
        value_isw=value_isw,
        value_n=value_n,
        value_nic=value_nic,
        value_nie=value_nie,
        value_niew=value_niew,
        value_nisw=value_nisw,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    algorithm: Union[Unset, list[str]] = UNSET,
    algorithm_empty: Union[Unset, bool] = UNSET,
    algorithm_ic: Union[Unset, list[str]] = UNSET,
    algorithm_ie: Union[Unset, list[str]] = UNSET,
    algorithm_iew: Union[Unset, list[str]] = UNSET,
    algorithm_isw: Union[Unset, list[str]] = UNSET,
    algorithm_n: Union[Unset, list[str]] = UNSET,
    algorithm_nic: Union[Unset, list[str]] = UNSET,
    algorithm_nie: Union[Unset, list[str]] = UNSET,
    algorithm_niew: Union[Unset, list[str]] = UNSET,
    algorithm_nisw: Union[Unset, list[str]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    hash_: Union[Unset, int] = UNSET,
    hash_n: Union[Unset, int] = UNSET,
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
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    value: Union[Unset, list[str]] = UNSET,
    value_empty: Union[Unset, bool] = UNSET,
    value_ic: Union[Unset, list[str]] = UNSET,
    value_ie: Union[Unset, list[str]] = UNSET,
    value_iew: Union[Unset, list[str]] = UNSET,
    value_isw: Union[Unset, list[str]] = UNSET,
    value_n: Union[Unset, list[str]] = UNSET,
    value_nic: Union[Unset, list[str]] = UNSET,
    value_nie: Union[Unset, list[str]] = UNSET,
    value_niew: Union[Unset, list[str]] = UNSET,
    value_nisw: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedFileHashList]:
    """ViewSet for XGenericUri.

    Args:
        algorithm (Union[Unset, list[str]]):
        algorithm_empty (Union[Unset, bool]):
        algorithm_ic (Union[Unset, list[str]]):
        algorithm_ie (Union[Unset, list[str]]):
        algorithm_iew (Union[Unset, list[str]]):
        algorithm_isw (Union[Unset, list[str]]):
        algorithm_n (Union[Unset, list[str]]):
        algorithm_nic (Union[Unset, list[str]]):
        algorithm_nie (Union[Unset, list[str]]):
        algorithm_niew (Union[Unset, list[str]]):
        algorithm_nisw (Union[Unset, list[str]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        hash_ (Union[Unset, int]):
        hash_n (Union[Unset, int]):
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
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        value (Union[Unset, list[str]]):
        value_empty (Union[Unset, bool]):
        value_ic (Union[Unset, list[str]]):
        value_ie (Union[Unset, list[str]]):
        value_iew (Union[Unset, list[str]]):
        value_isw (Union[Unset, list[str]]):
        value_n (Union[Unset, list[str]]):
        value_nic (Union[Unset, list[str]]):
        value_nie (Union[Unset, list[str]]):
        value_niew (Union[Unset, list[str]]):
        value_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedFileHashList
    """

    return sync_detailed(
        client=client,
        algorithm=algorithm,
        algorithm_empty=algorithm_empty,
        algorithm_ic=algorithm_ic,
        algorithm_ie=algorithm_ie,
        algorithm_iew=algorithm_iew,
        algorithm_isw=algorithm_isw,
        algorithm_n=algorithm_n,
        algorithm_nic=algorithm_nic,
        algorithm_nie=algorithm_nie,
        algorithm_niew=algorithm_niew,
        algorithm_nisw=algorithm_nisw,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        hash_=hash_,
        hash_n=hash_n,
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
        q=q,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
        value=value,
        value_empty=value_empty,
        value_ic=value_ic,
        value_ie=value_ie,
        value_iew=value_iew,
        value_isw=value_isw,
        value_n=value_n,
        value_nic=value_nic,
        value_nie=value_nie,
        value_niew=value_niew,
        value_nisw=value_nisw,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    algorithm: Union[Unset, list[str]] = UNSET,
    algorithm_empty: Union[Unset, bool] = UNSET,
    algorithm_ic: Union[Unset, list[str]] = UNSET,
    algorithm_ie: Union[Unset, list[str]] = UNSET,
    algorithm_iew: Union[Unset, list[str]] = UNSET,
    algorithm_isw: Union[Unset, list[str]] = UNSET,
    algorithm_n: Union[Unset, list[str]] = UNSET,
    algorithm_nic: Union[Unset, list[str]] = UNSET,
    algorithm_nie: Union[Unset, list[str]] = UNSET,
    algorithm_niew: Union[Unset, list[str]] = UNSET,
    algorithm_nisw: Union[Unset, list[str]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    hash_: Union[Unset, int] = UNSET,
    hash_n: Union[Unset, int] = UNSET,
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
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    value: Union[Unset, list[str]] = UNSET,
    value_empty: Union[Unset, bool] = UNSET,
    value_ic: Union[Unset, list[str]] = UNSET,
    value_ie: Union[Unset, list[str]] = UNSET,
    value_iew: Union[Unset, list[str]] = UNSET,
    value_isw: Union[Unset, list[str]] = UNSET,
    value_n: Union[Unset, list[str]] = UNSET,
    value_nic: Union[Unset, list[str]] = UNSET,
    value_nie: Union[Unset, list[str]] = UNSET,
    value_niew: Union[Unset, list[str]] = UNSET,
    value_nisw: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedFileHashList]:
    """ViewSet for XGenericUri.

    Args:
        algorithm (Union[Unset, list[str]]):
        algorithm_empty (Union[Unset, bool]):
        algorithm_ic (Union[Unset, list[str]]):
        algorithm_ie (Union[Unset, list[str]]):
        algorithm_iew (Union[Unset, list[str]]):
        algorithm_isw (Union[Unset, list[str]]):
        algorithm_n (Union[Unset, list[str]]):
        algorithm_nic (Union[Unset, list[str]]):
        algorithm_nie (Union[Unset, list[str]]):
        algorithm_niew (Union[Unset, list[str]]):
        algorithm_nisw (Union[Unset, list[str]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        hash_ (Union[Unset, int]):
        hash_n (Union[Unset, int]):
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
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        value (Union[Unset, list[str]]):
        value_empty (Union[Unset, bool]):
        value_ic (Union[Unset, list[str]]):
        value_ie (Union[Unset, list[str]]):
        value_iew (Union[Unset, list[str]]):
        value_isw (Union[Unset, list[str]]):
        value_n (Union[Unset, list[str]]):
        value_nic (Union[Unset, list[str]]):
        value_nie (Union[Unset, list[str]]):
        value_niew (Union[Unset, list[str]]):
        value_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedFileHashList]
    """

    kwargs = _get_kwargs(
        algorithm=algorithm,
        algorithm_empty=algorithm_empty,
        algorithm_ic=algorithm_ic,
        algorithm_ie=algorithm_ie,
        algorithm_iew=algorithm_iew,
        algorithm_isw=algorithm_isw,
        algorithm_n=algorithm_n,
        algorithm_nic=algorithm_nic,
        algorithm_nie=algorithm_nie,
        algorithm_niew=algorithm_niew,
        algorithm_nisw=algorithm_nisw,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        hash_=hash_,
        hash_n=hash_n,
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
        q=q,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
        value=value,
        value_empty=value_empty,
        value_ic=value_ic,
        value_ie=value_ie,
        value_iew=value_iew,
        value_isw=value_isw,
        value_n=value_n,
        value_nic=value_nic,
        value_nie=value_nie,
        value_niew=value_niew,
        value_nisw=value_nisw,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    algorithm: Union[Unset, list[str]] = UNSET,
    algorithm_empty: Union[Unset, bool] = UNSET,
    algorithm_ic: Union[Unset, list[str]] = UNSET,
    algorithm_ie: Union[Unset, list[str]] = UNSET,
    algorithm_iew: Union[Unset, list[str]] = UNSET,
    algorithm_isw: Union[Unset, list[str]] = UNSET,
    algorithm_n: Union[Unset, list[str]] = UNSET,
    algorithm_nic: Union[Unset, list[str]] = UNSET,
    algorithm_nie: Union[Unset, list[str]] = UNSET,
    algorithm_niew: Union[Unset, list[str]] = UNSET,
    algorithm_nisw: Union[Unset, list[str]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    hash_: Union[Unset, int] = UNSET,
    hash_n: Union[Unset, int] = UNSET,
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
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    value: Union[Unset, list[str]] = UNSET,
    value_empty: Union[Unset, bool] = UNSET,
    value_ic: Union[Unset, list[str]] = UNSET,
    value_ie: Union[Unset, list[str]] = UNSET,
    value_iew: Union[Unset, list[str]] = UNSET,
    value_isw: Union[Unset, list[str]] = UNSET,
    value_n: Union[Unset, list[str]] = UNSET,
    value_nic: Union[Unset, list[str]] = UNSET,
    value_nie: Union[Unset, list[str]] = UNSET,
    value_niew: Union[Unset, list[str]] = UNSET,
    value_nisw: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedFileHashList]:
    """ViewSet for XGenericUri.

    Args:
        algorithm (Union[Unset, list[str]]):
        algorithm_empty (Union[Unset, bool]):
        algorithm_ic (Union[Unset, list[str]]):
        algorithm_ie (Union[Unset, list[str]]):
        algorithm_iew (Union[Unset, list[str]]):
        algorithm_isw (Union[Unset, list[str]]):
        algorithm_n (Union[Unset, list[str]]):
        algorithm_nic (Union[Unset, list[str]]):
        algorithm_nie (Union[Unset, list[str]]):
        algorithm_niew (Union[Unset, list[str]]):
        algorithm_nisw (Union[Unset, list[str]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        hash_ (Union[Unset, int]):
        hash_n (Union[Unset, int]):
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
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        value (Union[Unset, list[str]]):
        value_empty (Union[Unset, bool]):
        value_ic (Union[Unset, list[str]]):
        value_ie (Union[Unset, list[str]]):
        value_iew (Union[Unset, list[str]]):
        value_isw (Union[Unset, list[str]]):
        value_n (Union[Unset, list[str]]):
        value_nic (Union[Unset, list[str]]):
        value_nie (Union[Unset, list[str]]):
        value_niew (Union[Unset, list[str]]):
        value_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedFileHashList
    """

    return (
        await asyncio_detailed(
            client=client,
            algorithm=algorithm,
            algorithm_empty=algorithm_empty,
            algorithm_ic=algorithm_ic,
            algorithm_ie=algorithm_ie,
            algorithm_iew=algorithm_iew,
            algorithm_isw=algorithm_isw,
            algorithm_n=algorithm_n,
            algorithm_nic=algorithm_nic,
            algorithm_nie=algorithm_nie,
            algorithm_niew=algorithm_niew,
            algorithm_nisw=algorithm_nisw,
            created=created,
            created_empty=created_empty,
            created_gt=created_gt,
            created_gte=created_gte,
            created_lt=created_lt,
            created_lte=created_lte,
            created_n=created_n,
            created_by_request=created_by_request,
            hash_=hash_,
            hash_n=hash_n,
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
            q=q,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
            updated_by_request=updated_by_request,
            value=value,
            value_empty=value_empty,
            value_ic=value_ic,
            value_ie=value_ie,
            value_iew=value_iew,
            value_isw=value_isw,
            value_n=value_n,
            value_nic=value_nic,
            value_nie=value_nie,
            value_niew=value_niew,
            value_nisw=value_nisw,
        )
    ).parsed
