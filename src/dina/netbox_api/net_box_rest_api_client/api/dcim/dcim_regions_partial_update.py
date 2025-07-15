from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_writable_region_request import PatchedWritableRegionRequest
from ...models.region import Region
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: Union[
        PatchedWritableRegionRequest,
        PatchedWritableRegionRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/dcim/regions/{id}/",
    }

    if isinstance(body, PatchedWritableRegionRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedWritableRegionRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Region]:
    if response.status_code == 200:
        response_200 = Region.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Region]:
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
        PatchedWritableRegionRequest,
        PatchedWritableRegionRequest,
    ],
) -> Response[Region]:
    """Patch a region object.

    Args:
        id (int):
        body (PatchedWritableRegionRequest): Extends PrimaryModelSerializer to include MPTT
            support.
        body (PatchedWritableRegionRequest): Extends PrimaryModelSerializer to include MPTT
            support.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Region]
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
        PatchedWritableRegionRequest,
        PatchedWritableRegionRequest,
    ],
) -> Optional[Region]:
    """Patch a region object.

    Args:
        id (int):
        body (PatchedWritableRegionRequest): Extends PrimaryModelSerializer to include MPTT
            support.
        body (PatchedWritableRegionRequest): Extends PrimaryModelSerializer to include MPTT
            support.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Region
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
        PatchedWritableRegionRequest,
        PatchedWritableRegionRequest,
    ],
) -> Response[Region]:
    """Patch a region object.

    Args:
        id (int):
        body (PatchedWritableRegionRequest): Extends PrimaryModelSerializer to include MPTT
            support.
        body (PatchedWritableRegionRequest): Extends PrimaryModelSerializer to include MPTT
            support.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Region]
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
        PatchedWritableRegionRequest,
        PatchedWritableRegionRequest,
    ],
) -> Optional[Region]:
    """Patch a region object.

    Args:
        id (int):
        body (PatchedWritableRegionRequest): Extends PrimaryModelSerializer to include MPTT
            support.
        body (PatchedWritableRegionRequest): Extends PrimaryModelSerializer to include MPTT
            support.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Region
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
