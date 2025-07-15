from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.l2vpn_termination import L2VPNTermination
from ...models.l2vpn_termination_request import L2VPNTerminationRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        list["L2VPNTerminationRequest"],
        list["L2VPNTerminationRequest"],
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/vpn/l2vpn-terminations/",
    }

    if isinstance(body, list["L2VPNTerminationRequest"]):
        _json_body = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _json_body.append(body_item)

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, list["L2VPNTerminationRequest"]):
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
) -> Optional[list["L2VPNTermination"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = L2VPNTermination.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["L2VPNTermination"]]:
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
        list["L2VPNTerminationRequest"],
        list["L2VPNTerminationRequest"],
    ],
) -> Response[list["L2VPNTermination"]]:
    """Put a list of L2VPN termination objects.

    Args:
        body (list['L2VPNTerminationRequest']):
        body (list['L2VPNTerminationRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['L2VPNTermination']]
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
        list["L2VPNTerminationRequest"],
        list["L2VPNTerminationRequest"],
    ],
) -> Optional[list["L2VPNTermination"]]:
    """Put a list of L2VPN termination objects.

    Args:
        body (list['L2VPNTerminationRequest']):
        body (list['L2VPNTerminationRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['L2VPNTermination']
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        list["L2VPNTerminationRequest"],
        list["L2VPNTerminationRequest"],
    ],
) -> Response[list["L2VPNTermination"]]:
    """Put a list of L2VPN termination objects.

    Args:
        body (list['L2VPNTerminationRequest']):
        body (list['L2VPNTerminationRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['L2VPNTermination']]
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
        list["L2VPNTerminationRequest"],
        list["L2VPNTerminationRequest"],
    ],
) -> Optional[list["L2VPNTermination"]]:
    """Put a list of L2VPN termination objects.

    Args:
        body (list['L2VPNTerminationRequest']):
        body (list['L2VPNTerminationRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['L2VPNTermination']
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
