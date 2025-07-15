from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.vlan_translation_policy import VLANTranslationPolicy
from ...models.vlan_translation_policy_request import VLANTranslationPolicyRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        list["VLANTranslationPolicyRequest"],
        list["VLANTranslationPolicyRequest"],
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/ipam/vlan-translation-policies/",
    }

    if isinstance(body, list["VLANTranslationPolicyRequest"]):
        _json_body = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _json_body.append(body_item)

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, list["VLANTranslationPolicyRequest"]):
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
) -> Optional[list["VLANTranslationPolicy"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = VLANTranslationPolicy.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["VLANTranslationPolicy"]]:
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
        list["VLANTranslationPolicyRequest"],
        list["VLANTranslationPolicyRequest"],
    ],
) -> Response[list["VLANTranslationPolicy"]]:
    """Put a list of VLAN translation policy objects.

    Args:
        body (list['VLANTranslationPolicyRequest']):
        body (list['VLANTranslationPolicyRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['VLANTranslationPolicy']]
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
        list["VLANTranslationPolicyRequest"],
        list["VLANTranslationPolicyRequest"],
    ],
) -> Optional[list["VLANTranslationPolicy"]]:
    """Put a list of VLAN translation policy objects.

    Args:
        body (list['VLANTranslationPolicyRequest']):
        body (list['VLANTranslationPolicyRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['VLANTranslationPolicy']
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        list["VLANTranslationPolicyRequest"],
        list["VLANTranslationPolicyRequest"],
    ],
) -> Response[list["VLANTranslationPolicy"]]:
    """Put a list of VLAN translation policy objects.

    Args:
        body (list['VLANTranslationPolicyRequest']):
        body (list['VLANTranslationPolicyRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['VLANTranslationPolicy']]
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
        list["VLANTranslationPolicyRequest"],
        list["VLANTranslationPolicyRequest"],
    ],
) -> Optional[list["VLANTranslationPolicy"]]:
    """Put a list of VLAN translation policy objects.

    Args:
        body (list['VLANTranslationPolicyRequest']):
        body (list['VLANTranslationPolicyRequest']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['VLANTranslationPolicy']
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
