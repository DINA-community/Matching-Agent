from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.config_template import ConfigTemplate
from ...models.config_template_request import ConfigTemplateRequest
from ...models.extras_config_templates_render_create_format import ExtrasConfigTemplatesRenderCreateFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: Union[
        ConfigTemplateRequest,
        ConfigTemplateRequest,
    ],
    format_: Union[Unset, ExtrasConfigTemplatesRenderCreateFormat] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/extras/config-templates/{id}/render/",
        "params": params,
    }

    if isinstance(body, ConfigTemplateRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, ConfigTemplateRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ConfigTemplate]:
    if response.status_code == 200:
        response_200 = ConfigTemplate.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ConfigTemplate]:
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
        ConfigTemplateRequest,
        ConfigTemplateRequest,
    ],
    format_: Union[Unset, ExtrasConfigTemplatesRenderCreateFormat] = UNSET,
) -> Response[ConfigTemplate]:
    r"""Render a ConfigTemplate using the context data provided (if any). If the client requests
    \"text/plain\" data,
    return the raw rendered content, rather than serialized JSON.

    Args:
        id (int):
        format_ (Union[Unset, ExtrasConfigTemplatesRenderCreateFormat]):
        body (ConfigTemplateRequest): Introduces support for Tag assignment. Adds `tags`
            serialization, and handles tag assignment
            on create() and update().
        body (ConfigTemplateRequest): Introduces support for Tag assignment. Adds `tags`
            serialization, and handles tag assignment
            on create() and update().

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigTemplate]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        format_=format_,
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
        ConfigTemplateRequest,
        ConfigTemplateRequest,
    ],
    format_: Union[Unset, ExtrasConfigTemplatesRenderCreateFormat] = UNSET,
) -> Optional[ConfigTemplate]:
    r"""Render a ConfigTemplate using the context data provided (if any). If the client requests
    \"text/plain\" data,
    return the raw rendered content, rather than serialized JSON.

    Args:
        id (int):
        format_ (Union[Unset, ExtrasConfigTemplatesRenderCreateFormat]):
        body (ConfigTemplateRequest): Introduces support for Tag assignment. Adds `tags`
            serialization, and handles tag assignment
            on create() and update().
        body (ConfigTemplateRequest): Introduces support for Tag assignment. Adds `tags`
            serialization, and handles tag assignment
            on create() and update().

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigTemplate
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        ConfigTemplateRequest,
        ConfigTemplateRequest,
    ],
    format_: Union[Unset, ExtrasConfigTemplatesRenderCreateFormat] = UNSET,
) -> Response[ConfigTemplate]:
    r"""Render a ConfigTemplate using the context data provided (if any). If the client requests
    \"text/plain\" data,
    return the raw rendered content, rather than serialized JSON.

    Args:
        id (int):
        format_ (Union[Unset, ExtrasConfigTemplatesRenderCreateFormat]):
        body (ConfigTemplateRequest): Introduces support for Tag assignment. Adds `tags`
            serialization, and handles tag assignment
            on create() and update().
        body (ConfigTemplateRequest): Introduces support for Tag assignment. Adds `tags`
            serialization, and handles tag assignment
            on create() and update().

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConfigTemplate]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: Union[
        ConfigTemplateRequest,
        ConfigTemplateRequest,
    ],
    format_: Union[Unset, ExtrasConfigTemplatesRenderCreateFormat] = UNSET,
) -> Optional[ConfigTemplate]:
    r"""Render a ConfigTemplate using the context data provided (if any). If the client requests
    \"text/plain\" data,
    return the raw rendered content, rather than serialized JSON.

    Args:
        id (int):
        format_ (Union[Unset, ExtrasConfigTemplatesRenderCreateFormat]):
        body (ConfigTemplateRequest): Introduces support for Tag assignment. Adds `tags`
            serialization, and handles tag assignment
            on create() and update().
        body (ConfigTemplateRequest): Introduces support for Tag assignment. Adds `tags`
            serialization, and handles tag assignment
            on create() and update().

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConfigTemplate
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            format_=format_,
        )
    ).parsed
