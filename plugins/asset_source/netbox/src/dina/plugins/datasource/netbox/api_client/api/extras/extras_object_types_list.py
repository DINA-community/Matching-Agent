from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_object_type_list import PaginatedObjectTypeList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    app_label: Union[Unset, str] = UNSET,
    id: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    model: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["app_label"] = app_label

    params["id"] = id

    params["limit"] = limit

    params["model"] = model

    params["offset"] = offset

    params["ordering"] = ordering

    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/extras/object-types/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedObjectTypeList]:
    if response.status_code == 200:
        response_200 = PaginatedObjectTypeList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedObjectTypeList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    app_label: Union[Unset, str] = UNSET,
    id: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    model: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
) -> Response[PaginatedObjectTypeList]:
    """Read-only list of ObjectTypes.

    Args:
        app_label (Union[Unset, str]):
        id (Union[Unset, int]):
        limit (Union[Unset, int]):
        model (Union[Unset, str]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedObjectTypeList]
    """

    kwargs = _get_kwargs(
        app_label=app_label,
        id=id,
        limit=limit,
        model=model,
        offset=offset,
        ordering=ordering,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    app_label: Union[Unset, str] = UNSET,
    id: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    model: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
) -> Optional[PaginatedObjectTypeList]:
    """Read-only list of ObjectTypes.

    Args:
        app_label (Union[Unset, str]):
        id (Union[Unset, int]):
        limit (Union[Unset, int]):
        model (Union[Unset, str]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedObjectTypeList
    """

    return sync_detailed(
        client=client,
        app_label=app_label,
        id=id,
        limit=limit,
        model=model,
        offset=offset,
        ordering=ordering,
        q=q,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    app_label: Union[Unset, str] = UNSET,
    id: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    model: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
) -> Response[PaginatedObjectTypeList]:
    """Read-only list of ObjectTypes.

    Args:
        app_label (Union[Unset, str]):
        id (Union[Unset, int]):
        limit (Union[Unset, int]):
        model (Union[Unset, str]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedObjectTypeList]
    """

    kwargs = _get_kwargs(
        app_label=app_label,
        id=id,
        limit=limit,
        model=model,
        offset=offset,
        ordering=ordering,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    app_label: Union[Unset, str] = UNSET,
    id: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    model: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
) -> Optional[PaginatedObjectTypeList]:
    """Read-only list of ObjectTypes.

    Args:
        app_label (Union[Unset, str]):
        id (Union[Unset, int]):
        limit (Union[Unset, int]):
        model (Union[Unset, str]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedObjectTypeList
    """

    return (
        await asyncio_detailed(
            client=client,
            app_label=app_label,
            id=id,
            limit=limit,
            model=model,
            offset=offset,
            ordering=ordering,
            q=q,
        )
    ).parsed
