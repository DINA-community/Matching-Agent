from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.interface_template import InterfaceTemplate
from ...models.writable_interface_template_request import WritableInterfaceTemplateRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        WritableInterfaceTemplateRequest,
        WritableInterfaceTemplateRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/dcim/interface-templates/",
    }

    if isinstance(body, WritableInterfaceTemplateRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, WritableInterfaceTemplateRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[InterfaceTemplate]:
    if response.status_code == 201:
        response_201 = InterfaceTemplate.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[InterfaceTemplate]:
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
        WritableInterfaceTemplateRequest,
        WritableInterfaceTemplateRequest,
    ],
) -> Response[InterfaceTemplate]:
    """Post a list of interface template objects.

    Args:
        body (WritableInterfaceTemplateRequest): Extends the built-in ModelSerializer to enforce
            calling full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)
        body (WritableInterfaceTemplateRequest): Extends the built-in ModelSerializer to enforce
            calling full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InterfaceTemplate]
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
        WritableInterfaceTemplateRequest,
        WritableInterfaceTemplateRequest,
    ],
) -> Optional[InterfaceTemplate]:
    """Post a list of interface template objects.

    Args:
        body (WritableInterfaceTemplateRequest): Extends the built-in ModelSerializer to enforce
            calling full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)
        body (WritableInterfaceTemplateRequest): Extends the built-in ModelSerializer to enforce
            calling full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InterfaceTemplate
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        WritableInterfaceTemplateRequest,
        WritableInterfaceTemplateRequest,
    ],
) -> Response[InterfaceTemplate]:
    """Post a list of interface template objects.

    Args:
        body (WritableInterfaceTemplateRequest): Extends the built-in ModelSerializer to enforce
            calling full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)
        body (WritableInterfaceTemplateRequest): Extends the built-in ModelSerializer to enforce
            calling full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InterfaceTemplate]
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
        WritableInterfaceTemplateRequest,
        WritableInterfaceTemplateRequest,
    ],
) -> Optional[InterfaceTemplate]:
    """Post a list of interface template objects.

    Args:
        body (WritableInterfaceTemplateRequest): Extends the built-in ModelSerializer to enforce
            calling full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)
        body (WritableInterfaceTemplateRequest): Extends the built-in ModelSerializer to enforce
            calling full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InterfaceTemplate
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
