from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.virtual_machine_with_config_context import (
    VirtualMachineWithConfigContext,
)
from ...models.virtual_machine_with_config_context_request import (
    VirtualMachineWithConfigContextRequest,
)
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        list["VirtualMachineWithConfigContextRequest"],
        list["VirtualMachineWithConfigContextRequest"],
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/virtualization/virtual-machines/",
    }

    if isinstance(body, list["VirtualMachineWithConfigContextRequest"]):
        _json_body = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _json_body.append(body_item)

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, list["VirtualMachineWithConfigContextRequest"]):
        _files_body = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _files_body.append(body_item)

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["VirtualMachineWithConfigContext"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = VirtualMachineWithConfigContext.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["VirtualMachineWithConfigContext"]]:
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
        list["VirtualMachineWithConfigContextRequest"],
        list["VirtualMachineWithConfigContextRequest"],
    ],
) -> Response[list["VirtualMachineWithConfigContext"]]:
    """Put a list of virtual machine objects.

    Args:
        body (list['VirtualMachineWithConfigContextRequest']):
        body (list['VirtualMachineWithConfigContextRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['VirtualMachineWithConfigContext']]
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
        list["VirtualMachineWithConfigContextRequest"],
        list["VirtualMachineWithConfigContextRequest"],
    ],
) -> Optional[list["VirtualMachineWithConfigContext"]]:
    """Put a list of virtual machine objects.

    Args:
        body (list['VirtualMachineWithConfigContextRequest']):
        body (list['VirtualMachineWithConfigContextRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['VirtualMachineWithConfigContext']
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        list["VirtualMachineWithConfigContextRequest"],
        list["VirtualMachineWithConfigContextRequest"],
    ],
) -> Response[list["VirtualMachineWithConfigContext"]]:
    """Put a list of virtual machine objects.

    Args:
        body (list['VirtualMachineWithConfigContextRequest']):
        body (list['VirtualMachineWithConfigContextRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['VirtualMachineWithConfigContext']]
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
        list["VirtualMachineWithConfigContextRequest"],
        list["VirtualMachineWithConfigContextRequest"],
    ],
) -> Optional[list["VirtualMachineWithConfigContext"]]:
    """Put a list of virtual machine objects.

    Args:
        body (list['VirtualMachineWithConfigContextRequest']):
        body (list['VirtualMachineWithConfigContextRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['VirtualMachineWithConfigContext']
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
