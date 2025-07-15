from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_tagged_item_list import PaginatedTaggedItemList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    object_id: Union[Unset, list[int]] = UNSET,
    object_id_empty: Union[Unset, bool] = UNSET,
    object_id_gt: Union[Unset, list[int]] = UNSET,
    object_id_gte: Union[Unset, list[int]] = UNSET,
    object_id_lt: Union[Unset, list[int]] = UNSET,
    object_id_lte: Union[Unset, list[int]] = UNSET,
    object_id_n: Union[Unset, list[int]] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

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

    params["limit"] = limit

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/extras/tagged-objects/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedTaggedItemList]:
    if response.status_code == 200:
        response_200 = PaginatedTaggedItemList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedTaggedItemList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    object_id: Union[Unset, list[int]] = UNSET,
    object_id_empty: Union[Unset, bool] = UNSET,
    object_id_gt: Union[Unset, list[int]] = UNSET,
    object_id_gte: Union[Unset, list[int]] = UNSET,
    object_id_lt: Union[Unset, list[int]] = UNSET,
    object_id_lte: Union[Unset, list[int]] = UNSET,
    object_id_n: Union[Unset, list[int]] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedTaggedItemList]:
    """Get a list of tagged item objects.

    Args:
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        limit (Union[Unset, int]):
        object_id (Union[Unset, list[int]]):
        object_id_empty (Union[Unset, bool]):
        object_id_gt (Union[Unset, list[int]]):
        object_id_gte (Union[Unset, list[int]]):
        object_id_lt (Union[Unset, list[int]]):
        object_id_lte (Union[Unset, list[int]]):
        object_id_n (Union[Unset, list[int]]):
        object_type (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_id (Union[Unset, list[int]]):
        object_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTaggedItemList]
    """

    kwargs = _get_kwargs(
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        limit=limit,
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
        q=q,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    object_id: Union[Unset, list[int]] = UNSET,
    object_id_empty: Union[Unset, bool] = UNSET,
    object_id_gt: Union[Unset, list[int]] = UNSET,
    object_id_gte: Union[Unset, list[int]] = UNSET,
    object_id_lt: Union[Unset, list[int]] = UNSET,
    object_id_lte: Union[Unset, list[int]] = UNSET,
    object_id_n: Union[Unset, list[int]] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedTaggedItemList]:
    """Get a list of tagged item objects.

    Args:
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        limit (Union[Unset, int]):
        object_id (Union[Unset, list[int]]):
        object_id_empty (Union[Unset, bool]):
        object_id_gt (Union[Unset, list[int]]):
        object_id_gte (Union[Unset, list[int]]):
        object_id_lt (Union[Unset, list[int]]):
        object_id_lte (Union[Unset, list[int]]):
        object_id_n (Union[Unset, list[int]]):
        object_type (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_id (Union[Unset, list[int]]):
        object_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTaggedItemList
    """

    return sync_detailed(
        client=client,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        limit=limit,
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
        q=q,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    object_id: Union[Unset, list[int]] = UNSET,
    object_id_empty: Union[Unset, bool] = UNSET,
    object_id_gt: Union[Unset, list[int]] = UNSET,
    object_id_gte: Union[Unset, list[int]] = UNSET,
    object_id_lt: Union[Unset, list[int]] = UNSET,
    object_id_lte: Union[Unset, list[int]] = UNSET,
    object_id_n: Union[Unset, list[int]] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedTaggedItemList]:
    """Get a list of tagged item objects.

    Args:
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        limit (Union[Unset, int]):
        object_id (Union[Unset, list[int]]):
        object_id_empty (Union[Unset, bool]):
        object_id_gt (Union[Unset, list[int]]):
        object_id_gte (Union[Unset, list[int]]):
        object_id_lt (Union[Unset, list[int]]):
        object_id_lte (Union[Unset, list[int]]):
        object_id_n (Union[Unset, list[int]]):
        object_type (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_id (Union[Unset, list[int]]):
        object_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTaggedItemList]
    """

    kwargs = _get_kwargs(
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        limit=limit,
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
        q=q,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    object_id: Union[Unset, list[int]] = UNSET,
    object_id_empty: Union[Unset, bool] = UNSET,
    object_id_gt: Union[Unset, list[int]] = UNSET,
    object_id_gte: Union[Unset, list[int]] = UNSET,
    object_id_lt: Union[Unset, list[int]] = UNSET,
    object_id_lte: Union[Unset, list[int]] = UNSET,
    object_id_n: Union[Unset, list[int]] = UNSET,
    object_type: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedTaggedItemList]:
    """Get a list of tagged item objects.

    Args:
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        limit (Union[Unset, int]):
        object_id (Union[Unset, list[int]]):
        object_id_empty (Union[Unset, bool]):
        object_id_gt (Union[Unset, list[int]]):
        object_id_gte (Union[Unset, list[int]]):
        object_id_lt (Union[Unset, list[int]]):
        object_id_lte (Union[Unset, list[int]]):
        object_id_n (Union[Unset, list[int]]):
        object_type (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_id (Union[Unset, list[int]]):
        object_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTaggedItemList
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            limit=limit,
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
            q=q,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
        )
    ).parsed
