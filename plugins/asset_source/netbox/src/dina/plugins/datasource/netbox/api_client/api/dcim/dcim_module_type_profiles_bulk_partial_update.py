from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.module_type_profile import ModuleTypeProfile
from ...models.module_type_profile_request import ModuleTypeProfileRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        list["ModuleTypeProfileRequest"],
        list["ModuleTypeProfileRequest"],
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/dcim/module-type-profiles/",
    }

    if isinstance(body, list["ModuleTypeProfileRequest"]):
        _json_body = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _json_body.append(body_item)

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, list["ModuleTypeProfileRequest"]):
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
) -> Optional[list["ModuleTypeProfile"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModuleTypeProfile.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["ModuleTypeProfile"]]:
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
        list["ModuleTypeProfileRequest"],
        list["ModuleTypeProfileRequest"],
    ],
) -> Response[list["ModuleTypeProfile"]]:
    """Patch a list of module type profile objects.

    Args:
        body (list['ModuleTypeProfileRequest']):
        body (list['ModuleTypeProfileRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ModuleTypeProfile']]
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
        list["ModuleTypeProfileRequest"],
        list["ModuleTypeProfileRequest"],
    ],
) -> Optional[list["ModuleTypeProfile"]]:
    """Patch a list of module type profile objects.

    Args:
        body (list['ModuleTypeProfileRequest']):
        body (list['ModuleTypeProfileRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ModuleTypeProfile']
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        list["ModuleTypeProfileRequest"],
        list["ModuleTypeProfileRequest"],
    ],
) -> Response[list["ModuleTypeProfile"]]:
    """Patch a list of module type profile objects.

    Args:
        body (list['ModuleTypeProfileRequest']):
        body (list['ModuleTypeProfileRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['ModuleTypeProfile']]
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
        list["ModuleTypeProfileRequest"],
        list["ModuleTypeProfileRequest"],
    ],
) -> Optional[list["ModuleTypeProfile"]]:
    """Patch a list of module type profile objects.

    Args:
        body (list['ModuleTypeProfileRequest']):
        body (list['ModuleTypeProfileRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['ModuleTypeProfile']
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
