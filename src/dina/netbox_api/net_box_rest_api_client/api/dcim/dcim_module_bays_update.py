from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.module_bay import ModuleBay
from ...models.module_bay_request import ModuleBayRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: Union[
        ModuleBayRequest,
        ModuleBayRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/dcim/module-bays/{id}/",
    }

    if isinstance(body, ModuleBayRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, ModuleBayRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ModuleBay]:
    if response.status_code == 200:
        response_200 = ModuleBay.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ModuleBay]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        ModuleBayRequest,
        ModuleBayRequest,
    ],
) -> Response[ModuleBay]:
    """Put a module bay object.

    Args:
        id (int):
        body (ModuleBayRequest): Adds support for custom fields and tags.
        body (ModuleBayRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModuleBay]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        ModuleBayRequest,
        ModuleBayRequest,
    ],
) -> Optional[ModuleBay]:
    """Put a module bay object.

    Args:
        id (int):
        body (ModuleBayRequest): Adds support for custom fields and tags.
        body (ModuleBayRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModuleBay
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        ModuleBayRequest,
        ModuleBayRequest,
    ],
) -> Response[ModuleBay]:
    """Put a module bay object.

    Args:
        id (int):
        body (ModuleBayRequest): Adds support for custom fields and tags.
        body (ModuleBayRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModuleBay]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        ModuleBayRequest,
        ModuleBayRequest,
    ],
) -> Optional[ModuleBay]:
    """Put a module bay object.

    Args:
        id (int):
        body (ModuleBayRequest): Adds support for custom fields and tags.
        body (ModuleBayRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModuleBay
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
