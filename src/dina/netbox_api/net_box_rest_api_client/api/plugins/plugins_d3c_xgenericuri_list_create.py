from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.x_generic_uri import XGenericUri
from ...models.x_generic_uri_request import XGenericUriRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        XGenericUriRequest,
        XGenericUriRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/plugins/d3c/xgenericuri-list/",
    }

    if isinstance(body, XGenericUriRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, XGenericUriRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[XGenericUri]:
    if response.status_code == 201:
        response_201 = XGenericUri.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[XGenericUri]:
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
        XGenericUriRequest,
        XGenericUriRequest,
    ],
) -> Response[XGenericUri]:
    """ViewSet for XGenericUri.

    Args:
        body (XGenericUriRequest): REST API Model Serializer for XGenericUri.
        body (XGenericUriRequest): REST API Model Serializer for XGenericUri.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[XGenericUri]
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
        XGenericUriRequest,
        XGenericUriRequest,
    ],
) -> Optional[XGenericUri]:
    """ViewSet for XGenericUri.

    Args:
        body (XGenericUriRequest): REST API Model Serializer for XGenericUri.
        body (XGenericUriRequest): REST API Model Serializer for XGenericUri.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        XGenericUri
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        XGenericUriRequest,
        XGenericUriRequest,
    ],
) -> Response[XGenericUri]:
    """ViewSet for XGenericUri.

    Args:
        body (XGenericUriRequest): REST API Model Serializer for XGenericUri.
        body (XGenericUriRequest): REST API Model Serializer for XGenericUri.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[XGenericUri]
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
        XGenericUriRequest,
        XGenericUriRequest,
    ],
) -> Optional[XGenericUri]:
    """ViewSet for XGenericUri.

    Args:
        body (XGenericUriRequest): REST API Model Serializer for XGenericUri.
        body (XGenericUriRequest): REST API Model Serializer for XGenericUri.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        XGenericUri
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
