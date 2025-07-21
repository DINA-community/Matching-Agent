from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.virtual_chassis import VirtualChassis
from ...models.writable_virtual_chassis_request import WritableVirtualChassisRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        WritableVirtualChassisRequest,
        WritableVirtualChassisRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/dcim/virtual-chassis/",
    }

    if isinstance(body, WritableVirtualChassisRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, WritableVirtualChassisRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[VirtualChassis]:
    if response.status_code == 201:
        response_201 = VirtualChassis.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[VirtualChassis]:
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
        WritableVirtualChassisRequest,
        WritableVirtualChassisRequest,
    ],
) -> Response[VirtualChassis]:
    """Post a list of virtual chassis objects.

    Args:
        body (WritableVirtualChassisRequest): Adds support for custom fields and tags.
        body (WritableVirtualChassisRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VirtualChassis]
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
        WritableVirtualChassisRequest,
        WritableVirtualChassisRequest,
    ],
) -> Optional[VirtualChassis]:
    """Post a list of virtual chassis objects.

    Args:
        body (WritableVirtualChassisRequest): Adds support for custom fields and tags.
        body (WritableVirtualChassisRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VirtualChassis
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        WritableVirtualChassisRequest,
        WritableVirtualChassisRequest,
    ],
) -> Response[VirtualChassis]:
    """Post a list of virtual chassis objects.

    Args:
        body (WritableVirtualChassisRequest): Adds support for custom fields and tags.
        body (WritableVirtualChassisRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VirtualChassis]
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
        WritableVirtualChassisRequest,
        WritableVirtualChassisRequest,
    ],
) -> Optional[VirtualChassis]:
    """Post a list of virtual chassis objects.

    Args:
        body (WritableVirtualChassisRequest): Adds support for custom fields and tags.
        body (WritableVirtualChassisRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VirtualChassis
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
