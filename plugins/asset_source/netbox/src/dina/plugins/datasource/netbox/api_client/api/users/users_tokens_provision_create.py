from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.token_provision import TokenProvision
from ...models.token_provision_request import TokenProvisionRequest
from ...models.users_tokens_provision_create_response_401 import (
    UsersTokensProvisionCreateResponse401,
)
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        TokenProvisionRequest,
        TokenProvisionRequest,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/users/tokens/provision/",
    }

    if isinstance(body, TokenProvisionRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, TokenProvisionRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[TokenProvision, UsersTokensProvisionCreateResponse401]]:
    if response.status_code == 201:
        response_201 = TokenProvision.from_dict(response.json())

        return response_201
    if response.status_code == 401:
        response_401 = UsersTokensProvisionCreateResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[TokenProvision, UsersTokensProvisionCreateResponse401]]:
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
        TokenProvisionRequest,
        TokenProvisionRequest,
    ],
) -> Response[Union[TokenProvision, UsersTokensProvisionCreateResponse401]]:
    """Non-authenticated REST API endpoint via which a user may create a Token.

    Args:
        body (TokenProvisionRequest): Extends the built-in ModelSerializer to enforce calling
            full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)
        body (TokenProvisionRequest): Extends the built-in ModelSerializer to enforce calling
            full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TokenProvision, UsersTokensProvisionCreateResponse401]]
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
        TokenProvisionRequest,
        TokenProvisionRequest,
    ],
) -> Optional[Union[TokenProvision, UsersTokensProvisionCreateResponse401]]:
    """Non-authenticated REST API endpoint via which a user may create a Token.

    Args:
        body (TokenProvisionRequest): Extends the built-in ModelSerializer to enforce calling
            full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)
        body (TokenProvisionRequest): Extends the built-in ModelSerializer to enforce calling
            full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TokenProvision, UsersTokensProvisionCreateResponse401]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        TokenProvisionRequest,
        TokenProvisionRequest,
    ],
) -> Response[Union[TokenProvision, UsersTokensProvisionCreateResponse401]]:
    """Non-authenticated REST API endpoint via which a user may create a Token.

    Args:
        body (TokenProvisionRequest): Extends the built-in ModelSerializer to enforce calling
            full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)
        body (TokenProvisionRequest): Extends the built-in ModelSerializer to enforce calling
            full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TokenProvision, UsersTokensProvisionCreateResponse401]]
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
        TokenProvisionRequest,
        TokenProvisionRequest,
    ],
) -> Optional[Union[TokenProvision, UsersTokensProvisionCreateResponse401]]:
    """Non-authenticated REST API endpoint via which a user may create a Token.

    Args:
        body (TokenProvisionRequest): Extends the built-in ModelSerializer to enforce calling
            full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)
        body (TokenProvisionRequest): Extends the built-in ModelSerializer to enforce calling
            full_clean() on a copy of the associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-
            framework/issues/3144)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TokenProvision, UsersTokensProvisionCreateResponse401]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
