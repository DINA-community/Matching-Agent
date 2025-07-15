from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_writable_virtual_chassis_request import PatchedWritableVirtualChassisRequest
from ...models.virtual_chassis import VirtualChassis
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: Union[
        PatchedWritableVirtualChassisRequest,
        PatchedWritableVirtualChassisRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/dcim/virtual-chassis/{id}/",
    }

    if isinstance(body, PatchedWritableVirtualChassisRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedWritableVirtualChassisRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[VirtualChassis]:
    if response.status_code == 200:
        response_200 = VirtualChassis.from_dict(response.json())

        return response_200
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
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedWritableVirtualChassisRequest,
        PatchedWritableVirtualChassisRequest,
    ],
) -> Response[VirtualChassis]:
    """Patch a virtual chassis object.

    Args:
        id (int):
        body (PatchedWritableVirtualChassisRequest): Adds support for custom fields and tags.
        body (PatchedWritableVirtualChassisRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VirtualChassis]
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
        PatchedWritableVirtualChassisRequest,
        PatchedWritableVirtualChassisRequest,
    ],
) -> Optional[VirtualChassis]:
    """Patch a virtual chassis object.

    Args:
        id (int):
        body (PatchedWritableVirtualChassisRequest): Adds support for custom fields and tags.
        body (PatchedWritableVirtualChassisRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VirtualChassis
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
        PatchedWritableVirtualChassisRequest,
        PatchedWritableVirtualChassisRequest,
    ],
) -> Response[VirtualChassis]:
    """Patch a virtual chassis object.

    Args:
        id (int):
        body (PatchedWritableVirtualChassisRequest): Adds support for custom fields and tags.
        body (PatchedWritableVirtualChassisRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VirtualChassis]
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
        PatchedWritableVirtualChassisRequest,
        PatchedWritableVirtualChassisRequest,
    ],
) -> Optional[VirtualChassis]:
    """Patch a virtual chassis object.

    Args:
        id (int):
        body (PatchedWritableVirtualChassisRequest): Adds support for custom fields and tags.
        body (PatchedWritableVirtualChassisRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VirtualChassis
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
