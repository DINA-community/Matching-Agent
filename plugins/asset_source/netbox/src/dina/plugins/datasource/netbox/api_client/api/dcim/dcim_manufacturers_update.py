from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.manufacturer import Manufacturer
from ...models.manufacturer_request import ManufacturerRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: Union[
        ManufacturerRequest,
        ManufacturerRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/dcim/manufacturers/{id}/",
    }

    if isinstance(body, ManufacturerRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, ManufacturerRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Manufacturer]:
    if response.status_code == 200:
        response_200 = Manufacturer.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Manufacturer]:
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
        ManufacturerRequest,
        ManufacturerRequest,
    ],
) -> Response[Manufacturer]:
    """Put a manufacturer object.

    Args:
        id (int):
        body (ManufacturerRequest): Adds support for custom fields and tags.
        body (ManufacturerRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Manufacturer]
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
        ManufacturerRequest,
        ManufacturerRequest,
    ],
) -> Optional[Manufacturer]:
    """Put a manufacturer object.

    Args:
        id (int):
        body (ManufacturerRequest): Adds support for custom fields and tags.
        body (ManufacturerRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Manufacturer
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
        ManufacturerRequest,
        ManufacturerRequest,
    ],
) -> Response[Manufacturer]:
    """Put a manufacturer object.

    Args:
        id (int):
        body (ManufacturerRequest): Adds support for custom fields and tags.
        body (ManufacturerRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Manufacturer]
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
        ManufacturerRequest,
        ManufacturerRequest,
    ],
) -> Optional[Manufacturer]:
    """Put a manufacturer object.

    Args:
        id (int):
        body (ManufacturerRequest): Adds support for custom fields and tags.
        body (ManufacturerRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Manufacturer
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
