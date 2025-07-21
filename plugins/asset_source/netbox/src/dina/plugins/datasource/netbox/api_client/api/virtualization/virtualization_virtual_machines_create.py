from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.virtual_machine_with_config_context import (
    VirtualMachineWithConfigContext,
)
from ...models.writable_virtual_machine_with_config_context_request import (
    WritableVirtualMachineWithConfigContextRequest,
)
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        WritableVirtualMachineWithConfigContextRequest,
        WritableVirtualMachineWithConfigContextRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/virtualization/virtual-machines/",
    }

    if isinstance(body, WritableVirtualMachineWithConfigContextRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, WritableVirtualMachineWithConfigContextRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[VirtualMachineWithConfigContext]:
    if response.status_code == 201:
        response_201 = VirtualMachineWithConfigContext.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[VirtualMachineWithConfigContext]:
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
        WritableVirtualMachineWithConfigContextRequest,
        WritableVirtualMachineWithConfigContextRequest,
    ],
) -> Response[VirtualMachineWithConfigContext]:
    """Post a list of virtual machine objects.

    Args:
        body (WritableVirtualMachineWithConfigContextRequest): Adds support for custom fields and
            tags.
        body (WritableVirtualMachineWithConfigContextRequest): Adds support for custom fields and
            tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VirtualMachineWithConfigContext]
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
        WritableVirtualMachineWithConfigContextRequest,
        WritableVirtualMachineWithConfigContextRequest,
    ],
) -> Optional[VirtualMachineWithConfigContext]:
    """Post a list of virtual machine objects.

    Args:
        body (WritableVirtualMachineWithConfigContextRequest): Adds support for custom fields and
            tags.
        body (WritableVirtualMachineWithConfigContextRequest): Adds support for custom fields and
            tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VirtualMachineWithConfigContext
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        WritableVirtualMachineWithConfigContextRequest,
        WritableVirtualMachineWithConfigContextRequest,
    ],
) -> Response[VirtualMachineWithConfigContext]:
    """Post a list of virtual machine objects.

    Args:
        body (WritableVirtualMachineWithConfigContextRequest): Adds support for custom fields and
            tags.
        body (WritableVirtualMachineWithConfigContextRequest): Adds support for custom fields and
            tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VirtualMachineWithConfigContext]
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
        WritableVirtualMachineWithConfigContextRequest,
        WritableVirtualMachineWithConfigContextRequest,
    ],
) -> Optional[VirtualMachineWithConfigContext]:
    """Post a list of virtual machine objects.

    Args:
        body (WritableVirtualMachineWithConfigContextRequest): Adds support for custom fields and
            tags.
        body (WritableVirtualMachineWithConfigContextRequest): Adds support for custom fields and
            tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VirtualMachineWithConfigContext
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
