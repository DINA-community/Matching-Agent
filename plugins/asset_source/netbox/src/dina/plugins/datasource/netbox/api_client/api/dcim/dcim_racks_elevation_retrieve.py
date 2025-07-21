from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dcim_racks_elevation_retrieve_render import (
    DcimRacksElevationRetrieveRender,
)
from ...models.paginated_rack_unit_list import PaginatedRackUnitList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    exclude: Union[Unset, int] = UNSET,
    expand_devices: Union[Unset, bool] = True,
    include_images: Union[Unset, bool] = True,
    legend_width: Union[Unset, int] = 30,
    limit: Union[Unset, int] = UNSET,
    margin_width: Union[Unset, int] = 15,
    offset: Union[Unset, int] = UNSET,
    q: Union[Unset, str] = UNSET,
    render: Union[
        Unset, DcimRacksElevationRetrieveRender
    ] = DcimRacksElevationRetrieveRender.JSON,
    unit_height: Union[Unset, int] = UNSET,
    unit_width: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["exclude"] = exclude

    params["expand_devices"] = expand_devices

    params["include_images"] = include_images

    params["legend_width"] = legend_width

    params["limit"] = limit

    params["margin_width"] = margin_width

    params["offset"] = offset

    params["q"] = q

    json_render: Union[Unset, str] = UNSET
    if not isinstance(render, Unset):
        json_render = render.value

    params["render"] = json_render

    params["unit_height"] = unit_height

    params["unit_width"] = unit_width

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/dcim/racks/{id}/elevation/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedRackUnitList]:
    if response.status_code == 200:
        response_200 = PaginatedRackUnitList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedRackUnitList]:
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
    exclude: Union[Unset, int] = UNSET,
    expand_devices: Union[Unset, bool] = True,
    include_images: Union[Unset, bool] = True,
    legend_width: Union[Unset, int] = 30,
    limit: Union[Unset, int] = UNSET,
    margin_width: Union[Unset, int] = 15,
    offset: Union[Unset, int] = UNSET,
    q: Union[Unset, str] = UNSET,
    render: Union[
        Unset, DcimRacksElevationRetrieveRender
    ] = DcimRacksElevationRetrieveRender.JSON,
    unit_height: Union[Unset, int] = UNSET,
    unit_width: Union[Unset, int] = UNSET,
) -> Response[PaginatedRackUnitList]:
    """Rack elevation representing the list of rack units. Also supports rendering the elevation as an SVG.

    Args:
        id (int):
        exclude (Union[Unset, int]):
        expand_devices (Union[Unset, bool]):  Default: True.
        include_images (Union[Unset, bool]):  Default: True.
        legend_width (Union[Unset, int]):  Default: 30.
        limit (Union[Unset, int]):
        margin_width (Union[Unset, int]):  Default: 15.
        offset (Union[Unset, int]):
        q (Union[Unset, str]):
        render (Union[Unset, DcimRacksElevationRetrieveRender]):  Default:
            DcimRacksElevationRetrieveRender.JSON.
        unit_height (Union[Unset, int]):
        unit_width (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRackUnitList]
    """

    kwargs = _get_kwargs(
        id=id,
        exclude=exclude,
        expand_devices=expand_devices,
        include_images=include_images,
        legend_width=legend_width,
        limit=limit,
        margin_width=margin_width,
        offset=offset,
        q=q,
        render=render,
        unit_height=unit_height,
        unit_width=unit_width,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    exclude: Union[Unset, int] = UNSET,
    expand_devices: Union[Unset, bool] = True,
    include_images: Union[Unset, bool] = True,
    legend_width: Union[Unset, int] = 30,
    limit: Union[Unset, int] = UNSET,
    margin_width: Union[Unset, int] = 15,
    offset: Union[Unset, int] = UNSET,
    q: Union[Unset, str] = UNSET,
    render: Union[
        Unset, DcimRacksElevationRetrieveRender
    ] = DcimRacksElevationRetrieveRender.JSON,
    unit_height: Union[Unset, int] = UNSET,
    unit_width: Union[Unset, int] = UNSET,
) -> Optional[PaginatedRackUnitList]:
    """Rack elevation representing the list of rack units. Also supports rendering the elevation as an SVG.

    Args:
        id (int):
        exclude (Union[Unset, int]):
        expand_devices (Union[Unset, bool]):  Default: True.
        include_images (Union[Unset, bool]):  Default: True.
        legend_width (Union[Unset, int]):  Default: 30.
        limit (Union[Unset, int]):
        margin_width (Union[Unset, int]):  Default: 15.
        offset (Union[Unset, int]):
        q (Union[Unset, str]):
        render (Union[Unset, DcimRacksElevationRetrieveRender]):  Default:
            DcimRacksElevationRetrieveRender.JSON.
        unit_height (Union[Unset, int]):
        unit_width (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRackUnitList
    """

    return sync_detailed(
        id=id,
        client=client,
        exclude=exclude,
        expand_devices=expand_devices,
        include_images=include_images,
        legend_width=legend_width,
        limit=limit,
        margin_width=margin_width,
        offset=offset,
        q=q,
        render=render,
        unit_height=unit_height,
        unit_width=unit_width,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    exclude: Union[Unset, int] = UNSET,
    expand_devices: Union[Unset, bool] = True,
    include_images: Union[Unset, bool] = True,
    legend_width: Union[Unset, int] = 30,
    limit: Union[Unset, int] = UNSET,
    margin_width: Union[Unset, int] = 15,
    offset: Union[Unset, int] = UNSET,
    q: Union[Unset, str] = UNSET,
    render: Union[
        Unset, DcimRacksElevationRetrieveRender
    ] = DcimRacksElevationRetrieveRender.JSON,
    unit_height: Union[Unset, int] = UNSET,
    unit_width: Union[Unset, int] = UNSET,
) -> Response[PaginatedRackUnitList]:
    """Rack elevation representing the list of rack units. Also supports rendering the elevation as an SVG.

    Args:
        id (int):
        exclude (Union[Unset, int]):
        expand_devices (Union[Unset, bool]):  Default: True.
        include_images (Union[Unset, bool]):  Default: True.
        legend_width (Union[Unset, int]):  Default: 30.
        limit (Union[Unset, int]):
        margin_width (Union[Unset, int]):  Default: 15.
        offset (Union[Unset, int]):
        q (Union[Unset, str]):
        render (Union[Unset, DcimRacksElevationRetrieveRender]):  Default:
            DcimRacksElevationRetrieveRender.JSON.
        unit_height (Union[Unset, int]):
        unit_width (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRackUnitList]
    """

    kwargs = _get_kwargs(
        id=id,
        exclude=exclude,
        expand_devices=expand_devices,
        include_images=include_images,
        legend_width=legend_width,
        limit=limit,
        margin_width=margin_width,
        offset=offset,
        q=q,
        render=render,
        unit_height=unit_height,
        unit_width=unit_width,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    exclude: Union[Unset, int] = UNSET,
    expand_devices: Union[Unset, bool] = True,
    include_images: Union[Unset, bool] = True,
    legend_width: Union[Unset, int] = 30,
    limit: Union[Unset, int] = UNSET,
    margin_width: Union[Unset, int] = 15,
    offset: Union[Unset, int] = UNSET,
    q: Union[Unset, str] = UNSET,
    render: Union[
        Unset, DcimRacksElevationRetrieveRender
    ] = DcimRacksElevationRetrieveRender.JSON,
    unit_height: Union[Unset, int] = UNSET,
    unit_width: Union[Unset, int] = UNSET,
) -> Optional[PaginatedRackUnitList]:
    """Rack elevation representing the list of rack units. Also supports rendering the elevation as an SVG.

    Args:
        id (int):
        exclude (Union[Unset, int]):
        expand_devices (Union[Unset, bool]):  Default: True.
        include_images (Union[Unset, bool]):  Default: True.
        legend_width (Union[Unset, int]):  Default: 30.
        limit (Union[Unset, int]):
        margin_width (Union[Unset, int]):  Default: 15.
        offset (Union[Unset, int]):
        q (Union[Unset, str]):
        render (Union[Unset, DcimRacksElevationRetrieveRender]):  Default:
            DcimRacksElevationRetrieveRender.JSON.
        unit_height (Union[Unset, int]):
        unit_width (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRackUnitList
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            exclude=exclude,
            expand_devices=expand_devices,
            include_images=include_images,
            legend_width=legend_width,
            limit=limit,
            margin_width=margin_width,
            offset=offset,
            q=q,
            render=render,
            unit_height=unit_height,
            unit_width=unit_width,
        )
    ).parsed
