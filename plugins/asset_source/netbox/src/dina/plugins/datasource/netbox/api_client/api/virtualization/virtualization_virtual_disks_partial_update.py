from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_virtual_disk_request import PatchedVirtualDiskRequest
from ...models.virtual_disk import VirtualDisk
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: Union[
        PatchedVirtualDiskRequest,
        PatchedVirtualDiskRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/virtualization/virtual-disks/{id}/",
    }

    if isinstance(body, PatchedVirtualDiskRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedVirtualDiskRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[VirtualDisk]:
    if response.status_code == 200:
        response_200 = VirtualDisk.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[VirtualDisk]:
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
        PatchedVirtualDiskRequest,
        PatchedVirtualDiskRequest,
    ],
) -> Response[VirtualDisk]:
    """Patch a virtual disk object.

    Args:
        id (int):
        body (PatchedVirtualDiskRequest): Adds support for custom fields and tags.
        body (PatchedVirtualDiskRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VirtualDisk]
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
        PatchedVirtualDiskRequest,
        PatchedVirtualDiskRequest,
    ],
) -> Optional[VirtualDisk]:
    """Patch a virtual disk object.

    Args:
        id (int):
        body (PatchedVirtualDiskRequest): Adds support for custom fields and tags.
        body (PatchedVirtualDiskRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VirtualDisk
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
        PatchedVirtualDiskRequest,
        PatchedVirtualDiskRequest,
    ],
) -> Response[VirtualDisk]:
    """Patch a virtual disk object.

    Args:
        id (int):
        body (PatchedVirtualDiskRequest): Adds support for custom fields and tags.
        body (PatchedVirtualDiskRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VirtualDisk]
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
        PatchedVirtualDiskRequest,
        PatchedVirtualDiskRequest,
    ],
) -> Optional[VirtualDisk]:
    """Patch a virtual disk object.

    Args:
        id (int):
        body (PatchedVirtualDiskRequest): Adds support for custom fields and tags.
        body (PatchedVirtualDiskRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VirtualDisk
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
