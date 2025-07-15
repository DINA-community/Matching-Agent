from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.route_target import RouteTarget
from ...models.route_target_request import RouteTargetRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: Union[
        RouteTargetRequest,
        RouteTargetRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/ipam/route-targets/{id}/",
    }

    if isinstance(body, RouteTargetRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, RouteTargetRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[RouteTarget]:
    if response.status_code == 200:
        response_200 = RouteTarget.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[RouteTarget]:
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
        RouteTargetRequest,
        RouteTargetRequest,
    ],
) -> Response[RouteTarget]:
    """Put a route target object.

    Args:
        id (int):
        body (RouteTargetRequest): Adds support for custom fields and tags.
        body (RouteTargetRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RouteTarget]
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
        RouteTargetRequest,
        RouteTargetRequest,
    ],
) -> Optional[RouteTarget]:
    """Put a route target object.

    Args:
        id (int):
        body (RouteTargetRequest): Adds support for custom fields and tags.
        body (RouteTargetRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RouteTarget
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
        RouteTargetRequest,
        RouteTargetRequest,
    ],
) -> Response[RouteTarget]:
    """Put a route target object.

    Args:
        id (int):
        body (RouteTargetRequest): Adds support for custom fields and tags.
        body (RouteTargetRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RouteTarget]
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
        RouteTargetRequest,
        RouteTargetRequest,
    ],
) -> Optional[RouteTarget]:
    """Put a route target object.

    Args:
        id (int):
        body (RouteTargetRequest): Adds support for custom fields and tags.
        body (RouteTargetRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RouteTarget
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
