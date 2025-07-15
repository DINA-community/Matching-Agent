from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fhrp_group_assignment import FHRPGroupAssignment
from ...models.fhrp_group_assignment_request import FHRPGroupAssignmentRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        FHRPGroupAssignmentRequest,
        FHRPGroupAssignmentRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/ipam/fhrp-group-assignments/",
    }

    if isinstance(body, FHRPGroupAssignmentRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, FHRPGroupAssignmentRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[FHRPGroupAssignment]:
    if response.status_code == 201:
        response_201 = FHRPGroupAssignment.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[FHRPGroupAssignment]:
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
        FHRPGroupAssignmentRequest,
        FHRPGroupAssignmentRequest,
    ],
) -> Response[FHRPGroupAssignment]:
    """Post a list of FHRP group assignment objects.

    Args:
        body (FHRPGroupAssignmentRequest): Adds support for custom fields and tags.
        body (FHRPGroupAssignmentRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FHRPGroupAssignment]
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
        FHRPGroupAssignmentRequest,
        FHRPGroupAssignmentRequest,
    ],
) -> Optional[FHRPGroupAssignment]:
    """Post a list of FHRP group assignment objects.

    Args:
        body (FHRPGroupAssignmentRequest): Adds support for custom fields and tags.
        body (FHRPGroupAssignmentRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FHRPGroupAssignment
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        FHRPGroupAssignmentRequest,
        FHRPGroupAssignmentRequest,
    ],
) -> Response[FHRPGroupAssignment]:
    """Post a list of FHRP group assignment objects.

    Args:
        body (FHRPGroupAssignmentRequest): Adds support for custom fields and tags.
        body (FHRPGroupAssignmentRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FHRPGroupAssignment]
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
        FHRPGroupAssignmentRequest,
        FHRPGroupAssignmentRequest,
    ],
) -> Optional[FHRPGroupAssignment]:
    """Post a list of FHRP group assignment objects.

    Args:
        body (FHRPGroupAssignmentRequest): Adds support for custom fields and tags.
        body (FHRPGroupAssignmentRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FHRPGroupAssignment
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
