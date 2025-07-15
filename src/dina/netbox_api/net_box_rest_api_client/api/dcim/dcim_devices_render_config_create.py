from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dcim_devices_render_config_create_format import DcimDevicesRenderConfigCreateFormat
from ...models.device_with_config_context import DeviceWithConfigContext
from ...models.writable_device_with_config_context_request import WritableDeviceWithConfigContextRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: Union[
        WritableDeviceWithConfigContextRequest,
        WritableDeviceWithConfigContextRequest,
    ],
    format_: Union[Unset, DcimDevicesRenderConfigCreateFormat] = UNSET,
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
        "url": f"/api/dcim/devices/{id}/render-config/",
        "params": params,
    }

    if isinstance(body, WritableDeviceWithConfigContextRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, WritableDeviceWithConfigContextRequest):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeviceWithConfigContext]:
    if response.status_code == 200:
        response_200 = DeviceWithConfigContext.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeviceWithConfigContext]:
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
        WritableDeviceWithConfigContextRequest,
        WritableDeviceWithConfigContextRequest,
    ],
    format_: Union[Unset, DcimDevicesRenderConfigCreateFormat] = UNSET,
) -> Response[DeviceWithConfigContext]:
    """Resolve and render the preferred ConfigTemplate for this Device.

    Args:
        id (int):
        format_ (Union[Unset, DcimDevicesRenderConfigCreateFormat]):
        body (WritableDeviceWithConfigContextRequest): Adds support for custom fields and tags.
        body (WritableDeviceWithConfigContextRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeviceWithConfigContext]
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
        WritableDeviceWithConfigContextRequest,
        WritableDeviceWithConfigContextRequest,
    ],
    format_: Union[Unset, DcimDevicesRenderConfigCreateFormat] = UNSET,
) -> Optional[DeviceWithConfigContext]:
    """Resolve and render the preferred ConfigTemplate for this Device.

    Args:
        id (int):
        format_ (Union[Unset, DcimDevicesRenderConfigCreateFormat]):
        body (WritableDeviceWithConfigContextRequest): Adds support for custom fields and tags.
        body (WritableDeviceWithConfigContextRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeviceWithConfigContext
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
        WritableDeviceWithConfigContextRequest,
        WritableDeviceWithConfigContextRequest,
    ],
    format_: Union[Unset, DcimDevicesRenderConfigCreateFormat] = UNSET,
) -> Response[DeviceWithConfigContext]:
    """Resolve and render the preferred ConfigTemplate for this Device.

    Args:
        id (int):
        format_ (Union[Unset, DcimDevicesRenderConfigCreateFormat]):
        body (WritableDeviceWithConfigContextRequest): Adds support for custom fields and tags.
        body (WritableDeviceWithConfigContextRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeviceWithConfigContext]
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
        WritableDeviceWithConfigContextRequest,
        WritableDeviceWithConfigContextRequest,
    ],
    format_: Union[Unset, DcimDevicesRenderConfigCreateFormat] = UNSET,
) -> Optional[DeviceWithConfigContext]:
    """Resolve and render the preferred ConfigTemplate for this Device.

    Args:
        id (int):
        format_ (Union[Unset, DcimDevicesRenderConfigCreateFormat]):
        body (WritableDeviceWithConfigContextRequest): Adds support for custom fields and tags.
        body (WritableDeviceWithConfigContextRequest): Adds support for custom fields and tags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeviceWithConfigContext
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            format_=format_,
        )
    ).parsed
