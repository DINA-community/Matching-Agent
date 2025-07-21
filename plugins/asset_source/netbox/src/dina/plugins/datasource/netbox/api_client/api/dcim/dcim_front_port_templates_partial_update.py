from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.front_port_template import FrontPortTemplate
from ...models.patched_writable_front_port_template_request import (
    PatchedWritableFrontPortTemplateRequest,
)
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: Union[
        PatchedWritableFrontPortTemplateRequest,
        PatchedWritableFrontPortTemplateRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/dcim/front-port-templates/{id}/",
    }

    if isinstance(body, PatchedWritableFrontPortTemplateRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedWritableFrontPortTemplateRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[FrontPortTemplate]:
    if response.status_code == 200:
        response_200 = FrontPortTemplate.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[FrontPortTemplate]:
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
        PatchedWritableFrontPortTemplateRequest,
        PatchedWritableFrontPortTemplateRequest,
    ],
) -> Response[FrontPortTemplate]:
    """Patch a front port template object.

    Args:
        id (int):
        body (PatchedWritableFrontPortTemplateRequest): Extends the built-in ModelSerializer to
            enforce calling full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)
        body (PatchedWritableFrontPortTemplateRequest): Extends the built-in ModelSerializer to
            enforce calling full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FrontPortTemplate]
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
        PatchedWritableFrontPortTemplateRequest,
        PatchedWritableFrontPortTemplateRequest,
    ],
) -> Optional[FrontPortTemplate]:
    """Patch a front port template object.

    Args:
        id (int):
        body (PatchedWritableFrontPortTemplateRequest): Extends the built-in ModelSerializer to
            enforce calling full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)
        body (PatchedWritableFrontPortTemplateRequest): Extends the built-in ModelSerializer to
            enforce calling full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FrontPortTemplate
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
        PatchedWritableFrontPortTemplateRequest,
        PatchedWritableFrontPortTemplateRequest,
    ],
) -> Response[FrontPortTemplate]:
    """Patch a front port template object.

    Args:
        id (int):
        body (PatchedWritableFrontPortTemplateRequest): Extends the built-in ModelSerializer to
            enforce calling full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)
        body (PatchedWritableFrontPortTemplateRequest): Extends the built-in ModelSerializer to
            enforce calling full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FrontPortTemplate]
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
        PatchedWritableFrontPortTemplateRequest,
        PatchedWritableFrontPortTemplateRequest,
    ],
) -> Optional[FrontPortTemplate]:
    """Patch a front port template object.

    Args:
        id (int):
        body (PatchedWritableFrontPortTemplateRequest): Extends the built-in ModelSerializer to
            enforce calling full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)
        body (PatchedWritableFrontPortTemplateRequest): Extends the built-in ModelSerializer to
            enforce calling full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FrontPortTemplate
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
