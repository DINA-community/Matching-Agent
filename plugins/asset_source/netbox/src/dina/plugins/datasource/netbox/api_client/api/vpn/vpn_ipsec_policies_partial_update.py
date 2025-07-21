from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ip_sec_policy import IPSecPolicy
from ...models.patched_writable_ip_sec_policy_request import (
    PatchedWritableIPSecPolicyRequest,
)
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: Union[
        PatchedWritableIPSecPolicyRequest,
        PatchedWritableIPSecPolicyRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/vpn/ipsec-policies/{id}/",
    }

    if isinstance(body, PatchedWritableIPSecPolicyRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedWritableIPSecPolicyRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IPSecPolicy]:
    if response.status_code == 200:
        response_200 = IPSecPolicy.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IPSecPolicy]:
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
        PatchedWritableIPSecPolicyRequest,
        PatchedWritableIPSecPolicyRequest,
    ],
) -> Response[IPSecPolicy]:
    """Patch a IPSec policy object.

    Args:
        id (int):
        body (PatchedWritableIPSecPolicyRequest): Adds support for custom fields and tags.
        body (PatchedWritableIPSecPolicyRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IPSecPolicy]
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
        PatchedWritableIPSecPolicyRequest,
        PatchedWritableIPSecPolicyRequest,
    ],
) -> Optional[IPSecPolicy]:
    """Patch a IPSec policy object.

    Args:
        id (int):
        body (PatchedWritableIPSecPolicyRequest): Adds support for custom fields and tags.
        body (PatchedWritableIPSecPolicyRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IPSecPolicy
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
        PatchedWritableIPSecPolicyRequest,
        PatchedWritableIPSecPolicyRequest,
    ],
) -> Response[IPSecPolicy]:
    """Patch a IPSec policy object.

    Args:
        id (int):
        body (PatchedWritableIPSecPolicyRequest): Adds support for custom fields and tags.
        body (PatchedWritableIPSecPolicyRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IPSecPolicy]
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
        PatchedWritableIPSecPolicyRequest,
        PatchedWritableIPSecPolicyRequest,
    ],
) -> Optional[IPSecPolicy]:
    """Patch a IPSec policy object.

    Args:
        id (int):
        body (PatchedWritableIPSecPolicyRequest): Adds support for custom fields and tags.
        body (PatchedWritableIPSecPolicyRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IPSecPolicy
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
