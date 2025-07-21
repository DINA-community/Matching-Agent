import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_product_relationship_list import (
    PaginatedProductRelationshipList,
)
from ...models.plugins_d3c_productrelationship_list_list_category import (
    PluginsD3CProductrelationshipListListCategory,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category: Union[Unset, PluginsD3CProductrelationshipListListCategory] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    destination_id: Union[Unset, list[int]] = UNSET,
    destination_id_empty: Union[Unset, bool] = UNSET,
    destination_id_gt: Union[Unset, list[int]] = UNSET,
    destination_id_gte: Union[Unset, list[int]] = UNSET,
    destination_id_lt: Union[Unset, list[int]] = UNSET,
    destination_id_lte: Union[Unset, list[int]] = UNSET,
    destination_id_n: Union[Unset, list[int]] = UNSET,
    destination_type: Union[Unset, int] = UNSET,
    destination_type_n: Union[Unset, int] = UNSET,
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
    source_id: Union[Unset, list[int]] = UNSET,
    source_id_empty: Union[Unset, bool] = UNSET,
    source_id_gt: Union[Unset, list[int]] = UNSET,
    source_id_gte: Union[Unset, list[int]] = UNSET,
    source_id_lt: Union[Unset, list[int]] = UNSET,
    source_id_lte: Union[Unset, list[int]] = UNSET,
    source_id_n: Union[Unset, list[int]] = UNSET,
    source_type: Union[Unset, int] = UNSET,
    source_type_n: Union[Unset, int] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_category: Union[Unset, str] = UNSET
    if not isinstance(category, Unset):
        json_category = category.value

    params["category"] = json_category

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

    json_destination_id: Union[Unset, list[int]] = UNSET
    if not isinstance(destination_id, Unset):
        json_destination_id = destination_id

    params["destination_id"] = json_destination_id

    params["destination_id__empty"] = destination_id_empty

    json_destination_id_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(destination_id_gt, Unset):
        json_destination_id_gt = destination_id_gt

    params["destination_id__gt"] = json_destination_id_gt

    json_destination_id_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(destination_id_gte, Unset):
        json_destination_id_gte = destination_id_gte

    params["destination_id__gte"] = json_destination_id_gte

    json_destination_id_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(destination_id_lt, Unset):
        json_destination_id_lt = destination_id_lt

    params["destination_id__lt"] = json_destination_id_lt

    json_destination_id_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(destination_id_lte, Unset):
        json_destination_id_lte = destination_id_lte

    params["destination_id__lte"] = json_destination_id_lte

    json_destination_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(destination_id_n, Unset):
        json_destination_id_n = destination_id_n

    params["destination_id__n"] = json_destination_id_n

    params["destination_type"] = destination_type

    params["destination_type__n"] = destination_type_n

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

    json_source_id: Union[Unset, list[int]] = UNSET
    if not isinstance(source_id, Unset):
        json_source_id = source_id

    params["source_id"] = json_source_id

    params["source_id__empty"] = source_id_empty

    json_source_id_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(source_id_gt, Unset):
        json_source_id_gt = source_id_gt

    params["source_id__gt"] = json_source_id_gt

    json_source_id_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(source_id_gte, Unset):
        json_source_id_gte = source_id_gte

    params["source_id__gte"] = json_source_id_gte

    json_source_id_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(source_id_lt, Unset):
        json_source_id_lt = source_id_lt

    params["source_id__lt"] = json_source_id_lt

    json_source_id_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(source_id_lte, Unset):
        json_source_id_lte = source_id_lte

    params["source_id__lte"] = json_source_id_lte

    json_source_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(source_id_n, Unset):
        json_source_id_n = source_id_n

    params["source_id__n"] = json_source_id_n

    params["source_type"] = source_type

    params["source_type__n"] = source_type_n

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
        "url": "/api/plugins/d3c/productrelationship-list/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedProductRelationshipList]:
    if response.status_code == 200:
        response_200 = PaginatedProductRelationshipList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedProductRelationshipList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    category: Union[Unset, PluginsD3CProductrelationshipListListCategory] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    destination_id: Union[Unset, list[int]] = UNSET,
    destination_id_empty: Union[Unset, bool] = UNSET,
    destination_id_gt: Union[Unset, list[int]] = UNSET,
    destination_id_gte: Union[Unset, list[int]] = UNSET,
    destination_id_lt: Union[Unset, list[int]] = UNSET,
    destination_id_lte: Union[Unset, list[int]] = UNSET,
    destination_id_n: Union[Unset, list[int]] = UNSET,
    destination_type: Union[Unset, int] = UNSET,
    destination_type_n: Union[Unset, int] = UNSET,
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
    source_id: Union[Unset, list[int]] = UNSET,
    source_id_empty: Union[Unset, bool] = UNSET,
    source_id_gt: Union[Unset, list[int]] = UNSET,
    source_id_gte: Union[Unset, list[int]] = UNSET,
    source_id_lt: Union[Unset, list[int]] = UNSET,
    source_id_lte: Union[Unset, list[int]] = UNSET,
    source_id_n: Union[Unset, list[int]] = UNSET,
    source_type: Union[Unset, int] = UNSET,
    source_type_n: Union[Unset, int] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedProductRelationshipList]:
    """ViewSet for ProductRelationships.

    Args:
        category (Union[Unset, PluginsD3CProductrelationshipListListCategory]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        destination_id (Union[Unset, list[int]]):
        destination_id_empty (Union[Unset, bool]):
        destination_id_gt (Union[Unset, list[int]]):
        destination_id_gte (Union[Unset, list[int]]):
        destination_id_lt (Union[Unset, list[int]]):
        destination_id_lte (Union[Unset, list[int]]):
        destination_id_n (Union[Unset, list[int]]):
        destination_type (Union[Unset, int]):
        destination_type_n (Union[Unset, int]):
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
        source_id (Union[Unset, list[int]]):
        source_id_empty (Union[Unset, bool]):
        source_id_gt (Union[Unset, list[int]]):
        source_id_gte (Union[Unset, list[int]]):
        source_id_lt (Union[Unset, list[int]]):
        source_id_lte (Union[Unset, list[int]]):
        source_id_n (Union[Unset, list[int]]):
        source_type (Union[Unset, int]):
        source_type_n (Union[Unset, int]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedProductRelationshipList]
    """

    kwargs = _get_kwargs(
        category=category,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        destination_id=destination_id,
        destination_id_empty=destination_id_empty,
        destination_id_gt=destination_id_gt,
        destination_id_gte=destination_id_gte,
        destination_id_lt=destination_id_lt,
        destination_id_lte=destination_id_lte,
        destination_id_n=destination_id_n,
        destination_type=destination_type,
        destination_type_n=destination_type_n,
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
        source_id=source_id,
        source_id_empty=source_id_empty,
        source_id_gt=source_id_gt,
        source_id_gte=source_id_gte,
        source_id_lt=source_id_lt,
        source_id_lte=source_id_lte,
        source_id_n=source_id_n,
        source_type=source_type,
        source_type_n=source_type_n,
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
    category: Union[Unset, PluginsD3CProductrelationshipListListCategory] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    destination_id: Union[Unset, list[int]] = UNSET,
    destination_id_empty: Union[Unset, bool] = UNSET,
    destination_id_gt: Union[Unset, list[int]] = UNSET,
    destination_id_gte: Union[Unset, list[int]] = UNSET,
    destination_id_lt: Union[Unset, list[int]] = UNSET,
    destination_id_lte: Union[Unset, list[int]] = UNSET,
    destination_id_n: Union[Unset, list[int]] = UNSET,
    destination_type: Union[Unset, int] = UNSET,
    destination_type_n: Union[Unset, int] = UNSET,
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
    source_id: Union[Unset, list[int]] = UNSET,
    source_id_empty: Union[Unset, bool] = UNSET,
    source_id_gt: Union[Unset, list[int]] = UNSET,
    source_id_gte: Union[Unset, list[int]] = UNSET,
    source_id_lt: Union[Unset, list[int]] = UNSET,
    source_id_lte: Union[Unset, list[int]] = UNSET,
    source_id_n: Union[Unset, list[int]] = UNSET,
    source_type: Union[Unset, int] = UNSET,
    source_type_n: Union[Unset, int] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedProductRelationshipList]:
    """ViewSet for ProductRelationships.

    Args:
        category (Union[Unset, PluginsD3CProductrelationshipListListCategory]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        destination_id (Union[Unset, list[int]]):
        destination_id_empty (Union[Unset, bool]):
        destination_id_gt (Union[Unset, list[int]]):
        destination_id_gte (Union[Unset, list[int]]):
        destination_id_lt (Union[Unset, list[int]]):
        destination_id_lte (Union[Unset, list[int]]):
        destination_id_n (Union[Unset, list[int]]):
        destination_type (Union[Unset, int]):
        destination_type_n (Union[Unset, int]):
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
        source_id (Union[Unset, list[int]]):
        source_id_empty (Union[Unset, bool]):
        source_id_gt (Union[Unset, list[int]]):
        source_id_gte (Union[Unset, list[int]]):
        source_id_lt (Union[Unset, list[int]]):
        source_id_lte (Union[Unset, list[int]]):
        source_id_n (Union[Unset, list[int]]):
        source_type (Union[Unset, int]):
        source_type_n (Union[Unset, int]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedProductRelationshipList
    """

    return sync_detailed(
        client=client,
        category=category,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        destination_id=destination_id,
        destination_id_empty=destination_id_empty,
        destination_id_gt=destination_id_gt,
        destination_id_gte=destination_id_gte,
        destination_id_lt=destination_id_lt,
        destination_id_lte=destination_id_lte,
        destination_id_n=destination_id_n,
        destination_type=destination_type,
        destination_type_n=destination_type_n,
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
        source_id=source_id,
        source_id_empty=source_id_empty,
        source_id_gt=source_id_gt,
        source_id_gte=source_id_gte,
        source_id_lt=source_id_lt,
        source_id_lte=source_id_lte,
        source_id_n=source_id_n,
        source_type=source_type,
        source_type_n=source_type_n,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    category: Union[Unset, PluginsD3CProductrelationshipListListCategory] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    destination_id: Union[Unset, list[int]] = UNSET,
    destination_id_empty: Union[Unset, bool] = UNSET,
    destination_id_gt: Union[Unset, list[int]] = UNSET,
    destination_id_gte: Union[Unset, list[int]] = UNSET,
    destination_id_lt: Union[Unset, list[int]] = UNSET,
    destination_id_lte: Union[Unset, list[int]] = UNSET,
    destination_id_n: Union[Unset, list[int]] = UNSET,
    destination_type: Union[Unset, int] = UNSET,
    destination_type_n: Union[Unset, int] = UNSET,
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
    source_id: Union[Unset, list[int]] = UNSET,
    source_id_empty: Union[Unset, bool] = UNSET,
    source_id_gt: Union[Unset, list[int]] = UNSET,
    source_id_gte: Union[Unset, list[int]] = UNSET,
    source_id_lt: Union[Unset, list[int]] = UNSET,
    source_id_lte: Union[Unset, list[int]] = UNSET,
    source_id_n: Union[Unset, list[int]] = UNSET,
    source_type: Union[Unset, int] = UNSET,
    source_type_n: Union[Unset, int] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedProductRelationshipList]:
    """ViewSet for ProductRelationships.

    Args:
        category (Union[Unset, PluginsD3CProductrelationshipListListCategory]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        destination_id (Union[Unset, list[int]]):
        destination_id_empty (Union[Unset, bool]):
        destination_id_gt (Union[Unset, list[int]]):
        destination_id_gte (Union[Unset, list[int]]):
        destination_id_lt (Union[Unset, list[int]]):
        destination_id_lte (Union[Unset, list[int]]):
        destination_id_n (Union[Unset, list[int]]):
        destination_type (Union[Unset, int]):
        destination_type_n (Union[Unset, int]):
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
        source_id (Union[Unset, list[int]]):
        source_id_empty (Union[Unset, bool]):
        source_id_gt (Union[Unset, list[int]]):
        source_id_gte (Union[Unset, list[int]]):
        source_id_lt (Union[Unset, list[int]]):
        source_id_lte (Union[Unset, list[int]]):
        source_id_n (Union[Unset, list[int]]):
        source_type (Union[Unset, int]):
        source_type_n (Union[Unset, int]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedProductRelationshipList]
    """

    kwargs = _get_kwargs(
        category=category,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        destination_id=destination_id,
        destination_id_empty=destination_id_empty,
        destination_id_gt=destination_id_gt,
        destination_id_gte=destination_id_gte,
        destination_id_lt=destination_id_lt,
        destination_id_lte=destination_id_lte,
        destination_id_n=destination_id_n,
        destination_type=destination_type,
        destination_type_n=destination_type_n,
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
        source_id=source_id,
        source_id_empty=source_id_empty,
        source_id_gt=source_id_gt,
        source_id_gte=source_id_gte,
        source_id_lt=source_id_lt,
        source_id_lte=source_id_lte,
        source_id_n=source_id_n,
        source_type=source_type,
        source_type_n=source_type_n,
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
    category: Union[Unset, PluginsD3CProductrelationshipListListCategory] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    destination_id: Union[Unset, list[int]] = UNSET,
    destination_id_empty: Union[Unset, bool] = UNSET,
    destination_id_gt: Union[Unset, list[int]] = UNSET,
    destination_id_gte: Union[Unset, list[int]] = UNSET,
    destination_id_lt: Union[Unset, list[int]] = UNSET,
    destination_id_lte: Union[Unset, list[int]] = UNSET,
    destination_id_n: Union[Unset, list[int]] = UNSET,
    destination_type: Union[Unset, int] = UNSET,
    destination_type_n: Union[Unset, int] = UNSET,
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
    source_id: Union[Unset, list[int]] = UNSET,
    source_id_empty: Union[Unset, bool] = UNSET,
    source_id_gt: Union[Unset, list[int]] = UNSET,
    source_id_gte: Union[Unset, list[int]] = UNSET,
    source_id_lt: Union[Unset, list[int]] = UNSET,
    source_id_lte: Union[Unset, list[int]] = UNSET,
    source_id_n: Union[Unset, list[int]] = UNSET,
    source_type: Union[Unset, int] = UNSET,
    source_type_n: Union[Unset, int] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedProductRelationshipList]:
    """ViewSet for ProductRelationships.

    Args:
        category (Union[Unset, PluginsD3CProductrelationshipListListCategory]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        destination_id (Union[Unset, list[int]]):
        destination_id_empty (Union[Unset, bool]):
        destination_id_gt (Union[Unset, list[int]]):
        destination_id_gte (Union[Unset, list[int]]):
        destination_id_lt (Union[Unset, list[int]]):
        destination_id_lte (Union[Unset, list[int]]):
        destination_id_n (Union[Unset, list[int]]):
        destination_type (Union[Unset, int]):
        destination_type_n (Union[Unset, int]):
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
        source_id (Union[Unset, list[int]]):
        source_id_empty (Union[Unset, bool]):
        source_id_gt (Union[Unset, list[int]]):
        source_id_gte (Union[Unset, list[int]]):
        source_id_lt (Union[Unset, list[int]]):
        source_id_lte (Union[Unset, list[int]]):
        source_id_n (Union[Unset, list[int]]):
        source_type (Union[Unset, int]):
        source_type_n (Union[Unset, int]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedProductRelationshipList
    """

    return (
        await asyncio_detailed(
            client=client,
            category=category,
            created=created,
            created_empty=created_empty,
            created_gt=created_gt,
            created_gte=created_gte,
            created_lt=created_lt,
            created_lte=created_lte,
            created_n=created_n,
            created_by_request=created_by_request,
            destination_id=destination_id,
            destination_id_empty=destination_id_empty,
            destination_id_gt=destination_id_gt,
            destination_id_gte=destination_id_gte,
            destination_id_lt=destination_id_lt,
            destination_id_lte=destination_id_lte,
            destination_id_n=destination_id_n,
            destination_type=destination_type,
            destination_type_n=destination_type_n,
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
            source_id=source_id,
            source_id_empty=source_id_empty,
            source_id_gt=source_id_gt,
            source_id_gte=source_id_gte,
            source_id_lt=source_id_lt,
            source_id_lte=source_id_lte,
            source_id_n=source_id_n,
            source_type=source_type,
            source_type_n=source_type_n,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
            updated_by_request=updated_by_request,
        )
    ).parsed
