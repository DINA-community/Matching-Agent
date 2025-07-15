from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hash_ import Hash
from ...models.hash_request import HashRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        HashRequest,
        HashRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/plugins/d3c/hash-list/",
    }

    if isinstance(body, HashRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, HashRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Hash]:
    if response.status_code == 201:
        response_201 = Hash.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Hash]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        HashRequest,
        HashRequest,
    ],
) -> Response[Hash]:
    """ViewSet for XGenericUri.

    Args:
        body (HashRequest): REST API Model Serializer for Hash.
        body (HashRequest): REST API Model Serializer for Hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Hash]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        HashRequest,
        HashRequest,
    ],
) -> Optional[Hash]:
    """ViewSet for XGenericUri.

    Args:
        body (HashRequest): REST API Model Serializer for Hash.
        body (HashRequest): REST API Model Serializer for Hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Hash
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        HashRequest,
        HashRequest,
    ],
) -> Response[Hash]:
    """ViewSet for XGenericUri.

    Args:
        body (HashRequest): REST API Model Serializer for Hash.
        body (HashRequest): REST API Model Serializer for Hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Hash]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        HashRequest,
        HashRequest,
    ],
) -> Optional[Hash]:
    """ViewSet for XGenericUri.

    Args:
        body (HashRequest): REST API Model Serializer for Hash.
        body (HashRequest): REST API Model Serializer for Hash.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Hash
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
