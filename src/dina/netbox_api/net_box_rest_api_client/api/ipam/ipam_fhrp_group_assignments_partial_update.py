from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fhrp_group_assignment import FHRPGroupAssignment
from ...models.patched_fhrp_group_assignment_request import PatchedFHRPGroupAssignmentRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: Union[
        PatchedFHRPGroupAssignmentRequest,
        PatchedFHRPGroupAssignmentRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/ipam/fhrp-group-assignments/{id}/",
    }

    if isinstance(body, PatchedFHRPGroupAssignmentRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedFHRPGroupAssignmentRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[FHRPGroupAssignment]:
    if response.status_code == 200:
        response_200 = FHRPGroupAssignment.from_dict(response.json())

        return response_200
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
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        PatchedFHRPGroupAssignmentRequest,
        PatchedFHRPGroupAssignmentRequest,
    ],
) -> Response[FHRPGroupAssignment]:
    """Patch a FHRP group assignment object.

    Args:
        id (int):
        body (PatchedFHRPGroupAssignmentRequest): Adds support for custom fields and tags.
        body (PatchedFHRPGroupAssignmentRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FHRPGroupAssignment]
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
        PatchedFHRPGroupAssignmentRequest,
        PatchedFHRPGroupAssignmentRequest,
    ],
) -> Optional[FHRPGroupAssignment]:
    """Patch a FHRP group assignment object.

    Args:
        id (int):
        body (PatchedFHRPGroupAssignmentRequest): Adds support for custom fields and tags.
        body (PatchedFHRPGroupAssignmentRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FHRPGroupAssignment
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
        PatchedFHRPGroupAssignmentRequest,
        PatchedFHRPGroupAssignmentRequest,
    ],
) -> Response[FHRPGroupAssignment]:
    """Patch a FHRP group assignment object.

    Args:
        id (int):
        body (PatchedFHRPGroupAssignmentRequest): Adds support for custom fields and tags.
        body (PatchedFHRPGroupAssignmentRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FHRPGroupAssignment]
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
        PatchedFHRPGroupAssignmentRequest,
        PatchedFHRPGroupAssignmentRequest,
    ],
) -> Optional[FHRPGroupAssignment]:
    """Patch a FHRP group assignment object.

    Args:
        id (int):
        body (PatchedFHRPGroupAssignmentRequest): Adds support for custom fields and tags.
        body (PatchedFHRPGroupAssignmentRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FHRPGroupAssignment
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
