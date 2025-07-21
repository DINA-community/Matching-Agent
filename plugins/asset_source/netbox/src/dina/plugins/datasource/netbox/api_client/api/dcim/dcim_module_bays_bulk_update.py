from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.module_bay import ModuleBay
from ...models.module_bay_request import ModuleBayRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        list["ModuleBayRequest"],
        list["ModuleBayRequest"],
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/dcim/module-bays/",
    }

    if isinstance(body, list["ModuleBayRequest"]):
        _json_body = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _json_body.append(body_item)

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, list["ModuleBayRequest"]):
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
) -> Optional[list["ModuleBay"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModuleBay.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["ModuleBay"]]:
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
        list["ModuleBayRequest"],
        list["ModuleBayRequest"],
    ],
) -> Response[list["ModuleBay"]]:
    """Put a list of module bay objects.

    Args:
        body (list['ModuleBayRequest']):
        body (list['ModuleBayRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ModuleBay']]
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
        list["ModuleBayRequest"],
        list["ModuleBayRequest"],
    ],
) -> Optional[list["ModuleBay"]]:
    """Put a list of module bay objects.

    Args:
        body (list['ModuleBayRequest']):
        body (list['ModuleBayRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ModuleBay']
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        list["ModuleBayRequest"],
        list["ModuleBayRequest"],
    ],
) -> Response[list["ModuleBay"]]:
    """Put a list of module bay objects.

    Args:
        body (list['ModuleBayRequest']):
        body (list['ModuleBayRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ModuleBay']]
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
        list["ModuleBayRequest"],
        list["ModuleBayRequest"],
    ],
) -> Optional[list["ModuleBay"]]:
    """Put a list of module bay objects.

    Args:
        body (list['ModuleBayRequest']):
        body (list['ModuleBayRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ModuleBay']
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
