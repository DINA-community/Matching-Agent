from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ike_policy import IKEPolicy
from ...models.writable_ike_policy_request import WritableIKEPolicyRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        WritableIKEPolicyRequest,
        WritableIKEPolicyRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/vpn/ike-policies/",
    }

    if isinstance(body, WritableIKEPolicyRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, WritableIKEPolicyRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[IKEPolicy]:
    if response.status_code == 201:
        response_201 = IKEPolicy.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[IKEPolicy]:
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
        WritableIKEPolicyRequest,
        WritableIKEPolicyRequest,
    ],
) -> Response[IKEPolicy]:
    """Post a list of IKE policy objects.

    Args:
        body (WritableIKEPolicyRequest): Adds support for custom fields and tags.
        body (WritableIKEPolicyRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IKEPolicy]
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
        WritableIKEPolicyRequest,
        WritableIKEPolicyRequest,
    ],
) -> Optional[IKEPolicy]:
    """Post a list of IKE policy objects.

    Args:
        body (WritableIKEPolicyRequest): Adds support for custom fields and tags.
        body (WritableIKEPolicyRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IKEPolicy
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        WritableIKEPolicyRequest,
        WritableIKEPolicyRequest,
    ],
) -> Response[IKEPolicy]:
    """Post a list of IKE policy objects.

    Args:
        body (WritableIKEPolicyRequest): Adds support for custom fields and tags.
        body (WritableIKEPolicyRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IKEPolicy]
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
        WritableIKEPolicyRequest,
        WritableIKEPolicyRequest,
    ],
) -> Optional[IKEPolicy]:
    """Post a list of IKE policy objects.

    Args:
        body (WritableIKEPolicyRequest): Adds support for custom fields and tags.
        body (WritableIKEPolicyRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IKEPolicy
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
