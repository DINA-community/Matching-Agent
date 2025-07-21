from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.device import Device
from ...types import UNSET, Response


def _get_kwargs(
    *,
    peer_device: str,
    peer_interface: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["peer_device"] = peer_device

    params["peer_interface"] = peer_interface

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/dcim/connected-device/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["Device"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Device.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["Device"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    peer_device: str,
    peer_interface: str,
) -> Response[list["Device"]]:
    """This endpoint allows a user to determine what device (if any) is connected to a given peer device
    and peer
    interface. This is useful in a situation where a device boots with no configuration, but can detect
    its neighbors
    via a protocol such as LLDP. Two query parameters must be included in the request:

    * `peer_device`: The name of the peer device
    * `peer_interface`: The name of the peer interface

    Args:
        peer_device (str):
        peer_interface (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Device']]
    """

    kwargs = _get_kwargs(
        peer_device=peer_device,
        peer_interface=peer_interface,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    peer_device: str,
    peer_interface: str,
) -> Optional[list["Device"]]:
    """This endpoint allows a user to determine what device (if any) is connected to a given peer device
    and peer
    interface. This is useful in a situation where a device boots with no configuration, but can detect
    its neighbors
    via a protocol such as LLDP. Two query parameters must be included in the request:

    * `peer_device`: The name of the peer device
    * `peer_interface`: The name of the peer interface

    Args:
        peer_device (str):
        peer_interface (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Device']
    """

    return sync_detailed(
        client=client,
        peer_device=peer_device,
        peer_interface=peer_interface,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    peer_device: str,
    peer_interface: str,
) -> Response[list["Device"]]:
    """This endpoint allows a user to determine what device (if any) is connected to a given peer device
    and peer
    interface. This is useful in a situation where a device boots with no configuration, but can detect
    its neighbors
    via a protocol such as LLDP. Two query parameters must be included in the request:

    * `peer_device`: The name of the peer device
    * `peer_interface`: The name of the peer interface

    Args:
        peer_device (str):
        peer_interface (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['Device']]
    """

    kwargs = _get_kwargs(
        peer_device=peer_device,
        peer_interface=peer_interface,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    peer_device: str,
    peer_interface: str,
) -> Optional[list["Device"]]:
    """This endpoint allows a user to determine what device (if any) is connected to a given peer device
    and peer
    interface. This is useful in a situation where a device boots with no configuration, but can detect
    its neighbors
    via a protocol such as LLDP. Two query parameters must be included in the request:

    * `peer_device`: The name of the peer device
    * `peer_interface`: The name of the peer interface

    Args:
        peer_device (str):
        peer_interface (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['Device']
    """

    return (
        await asyncio_detailed(
            client=client,
            peer_device=peer_device,
            peer_interface=peer_interface,
        )
    ).parsed
