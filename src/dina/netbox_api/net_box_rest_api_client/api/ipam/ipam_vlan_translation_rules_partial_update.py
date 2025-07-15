from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_vlan_translation_rule_request import PatchedVLANTranslationRuleRequest
from ...models.vlan_translation_rule import VLANTranslationRule
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: Union[
        PatchedVLANTranslationRuleRequest,
        PatchedVLANTranslationRuleRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/ipam/vlan-translation-rules/{id}/",
    }

    if isinstance(body, PatchedVLANTranslationRuleRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedVLANTranslationRuleRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[VLANTranslationRule]:
    if response.status_code == 200:
        response_200 = VLANTranslationRule.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[VLANTranslationRule]:
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
        PatchedVLANTranslationRuleRequest,
        PatchedVLANTranslationRuleRequest,
    ],
) -> Response[VLANTranslationRule]:
    """Patch a VLAN translation rule object.

    Args:
        id (int):
        body (PatchedVLANTranslationRuleRequest): Adds support for custom fields and tags.
        body (PatchedVLANTranslationRuleRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VLANTranslationRule]
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
        PatchedVLANTranslationRuleRequest,
        PatchedVLANTranslationRuleRequest,
    ],
) -> Optional[VLANTranslationRule]:
    """Patch a VLAN translation rule object.

    Args:
        id (int):
        body (PatchedVLANTranslationRuleRequest): Adds support for custom fields and tags.
        body (PatchedVLANTranslationRuleRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VLANTranslationRule
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
        PatchedVLANTranslationRuleRequest,
        PatchedVLANTranslationRuleRequest,
    ],
) -> Response[VLANTranslationRule]:
    """Patch a VLAN translation rule object.

    Args:
        id (int):
        body (PatchedVLANTranslationRuleRequest): Adds support for custom fields and tags.
        body (PatchedVLANTranslationRuleRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VLANTranslationRule]
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
        PatchedVLANTranslationRuleRequest,
        PatchedVLANTranslationRuleRequest,
    ],
) -> Optional[VLANTranslationRule]:
    """Patch a VLAN translation rule object.

    Args:
        id (int):
        body (PatchedVLANTranslationRuleRequest): Adds support for custom fields and tags.
        body (PatchedVLANTranslationRuleRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VLANTranslationRule
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
