import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_rack_reservation_list import PaginatedRackReservationList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    description: Union[Unset, list[str]] = UNSET,
    description_empty: Union[Unset, bool] = UNSET,
    description_ic: Union[Unset, list[str]] = UNSET,
    description_ie: Union[Unset, list[str]] = UNSET,
    description_iew: Union[Unset, list[str]] = UNSET,
    description_isw: Union[Unset, list[str]] = UNSET,
    description_n: Union[Unset, list[str]] = UNSET,
    description_nic: Union[Unset, list[str]] = UNSET,
    description_nie: Union[Unset, list[str]] = UNSET,
    description_niew: Union[Unset, list[str]] = UNSET,
    description_nisw: Union[Unset, list[str]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[str]] = UNSET,
    location_id_n: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tenant: Union[Unset, list[str]] = UNSET,
    tenant_n: Union[Unset, list[str]] = UNSET,
    tenant_group: Union[Unset, list[str]] = UNSET,
    tenant_group_n: Union[Unset, list[str]] = UNSET,
    tenant_group_id: Union[Unset, list[str]] = UNSET,
    tenant_group_id_n: Union[Unset, list[str]] = UNSET,
    tenant_id: Union[Unset, list[Union[None, int]]] = UNSET,
    tenant_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    unit: Union[Unset, float] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[int]] = UNSET,
    user_id_n: Union[Unset, list[int]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_created: Union[Unset, list[str]] = UNSET
    if not isinstance(created, Unset):
        json_created = []
        for created_item_data in created:
            created_item = created_item_data.isoformat()
            json_created.append(created_item)

    params["created"] = json_created

    json_created_empty: Union[Unset, list[str]] = UNSET
    if not isinstance(created_empty, Unset):
        json_created_empty = []
        for created_empty_item_data in created_empty:
            created_empty_item = created_empty_item_data.isoformat()
            json_created_empty.append(created_empty_item)

    params["created__empty"] = json_created_empty

    json_created_gt: Union[Unset, list[str]] = UNSET
    if not isinstance(created_gt, Unset):
        json_created_gt = []
        for created_gt_item_data in created_gt:
            created_gt_item = created_gt_item_data.isoformat()
            json_created_gt.append(created_gt_item)

    params["created__gt"] = json_created_gt

    json_created_gte: Union[Unset, list[str]] = UNSET
    if not isinstance(created_gte, Unset):
        json_created_gte = []
        for created_gte_item_data in created_gte:
            created_gte_item = created_gte_item_data.isoformat()
            json_created_gte.append(created_gte_item)

    params["created__gte"] = json_created_gte

    json_created_lt: Union[Unset, list[str]] = UNSET
    if not isinstance(created_lt, Unset):
        json_created_lt = []
        for created_lt_item_data in created_lt:
            created_lt_item = created_lt_item_data.isoformat()
            json_created_lt.append(created_lt_item)

    params["created__lt"] = json_created_lt

    json_created_lte: Union[Unset, list[str]] = UNSET
    if not isinstance(created_lte, Unset):
        json_created_lte = []
        for created_lte_item_data in created_lte:
            created_lte_item = created_lte_item_data.isoformat()
            json_created_lte.append(created_lte_item)

    params["created__lte"] = json_created_lte

    json_created_n: Union[Unset, list[str]] = UNSET
    if not isinstance(created_n, Unset):
        json_created_n = []
        for created_n_item_data in created_n:
            created_n_item = created_n_item_data.isoformat()
            json_created_n.append(created_n_item)

    params["created__n"] = json_created_n

    json_created_by_request: Union[Unset, str] = UNSET
    if not isinstance(created_by_request, Unset):
        json_created_by_request = str(created_by_request)
    params["created_by_request"] = json_created_by_request

    json_description: Union[Unset, list[str]] = UNSET
    if not isinstance(description, Unset):
        json_description = description

    params["description"] = json_description

    params["description__empty"] = description_empty

    json_description_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(description_ic, Unset):
        json_description_ic = description_ic

    params["description__ic"] = json_description_ic

    json_description_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(description_ie, Unset):
        json_description_ie = description_ie

    params["description__ie"] = json_description_ie

    json_description_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(description_iew, Unset):
        json_description_iew = description_iew

    params["description__iew"] = json_description_iew

    json_description_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(description_isw, Unset):
        json_description_isw = description_isw

    params["description__isw"] = json_description_isw

    json_description_n: Union[Unset, list[str]] = UNSET
    if not isinstance(description_n, Unset):
        json_description_n = description_n

    params["description__n"] = json_description_n

    json_description_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(description_nic, Unset):
        json_description_nic = description_nic

    params["description__nic"] = json_description_nic

    json_description_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(description_nie, Unset):
        json_description_nie = description_nie

    params["description__nie"] = json_description_nie

    json_description_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(description_niew, Unset):
        json_description_niew = description_niew

    params["description__niew"] = json_description_niew

    json_description_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(description_nisw, Unset):
        json_description_nisw = description_nisw

    params["description__nisw"] = json_description_nisw

    json_id: Union[Unset, list[int]] = UNSET
    if not isinstance(id, Unset):
        json_id = id

    params["id"] = json_id

    params["id__empty"] = id_empty

    json_id_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(id_gt, Unset):
        json_id_gt = id_gt

    params["id__gt"] = json_id_gt

    json_id_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(id_gte, Unset):
        json_id_gte = id_gte

    params["id__gte"] = json_id_gte

    json_id_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(id_lt, Unset):
        json_id_lt = id_lt

    params["id__lt"] = json_id_lt

    json_id_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(id_lte, Unset):
        json_id_lte = id_lte

    params["id__lte"] = json_id_lte

    json_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(id_n, Unset):
        json_id_n = id_n

    params["id__n"] = json_id_n

    json_last_updated: Union[Unset, list[str]] = UNSET
    if not isinstance(last_updated, Unset):
        json_last_updated = []
        for last_updated_item_data in last_updated:
            last_updated_item = last_updated_item_data.isoformat()
            json_last_updated.append(last_updated_item)

    params["last_updated"] = json_last_updated

    json_last_updated_empty: Union[Unset, list[str]] = UNSET
    if not isinstance(last_updated_empty, Unset):
        json_last_updated_empty = []
        for last_updated_empty_item_data in last_updated_empty:
            last_updated_empty_item = last_updated_empty_item_data.isoformat()
            json_last_updated_empty.append(last_updated_empty_item)

    params["last_updated__empty"] = json_last_updated_empty

    json_last_updated_gt: Union[Unset, list[str]] = UNSET
    if not isinstance(last_updated_gt, Unset):
        json_last_updated_gt = []
        for last_updated_gt_item_data in last_updated_gt:
            last_updated_gt_item = last_updated_gt_item_data.isoformat()
            json_last_updated_gt.append(last_updated_gt_item)

    params["last_updated__gt"] = json_last_updated_gt

    json_last_updated_gte: Union[Unset, list[str]] = UNSET
    if not isinstance(last_updated_gte, Unset):
        json_last_updated_gte = []
        for last_updated_gte_item_data in last_updated_gte:
            last_updated_gte_item = last_updated_gte_item_data.isoformat()
            json_last_updated_gte.append(last_updated_gte_item)

    params["last_updated__gte"] = json_last_updated_gte

    json_last_updated_lt: Union[Unset, list[str]] = UNSET
    if not isinstance(last_updated_lt, Unset):
        json_last_updated_lt = []
        for last_updated_lt_item_data in last_updated_lt:
            last_updated_lt_item = last_updated_lt_item_data.isoformat()
            json_last_updated_lt.append(last_updated_lt_item)

    params["last_updated__lt"] = json_last_updated_lt

    json_last_updated_lte: Union[Unset, list[str]] = UNSET
    if not isinstance(last_updated_lte, Unset):
        json_last_updated_lte = []
        for last_updated_lte_item_data in last_updated_lte:
            last_updated_lte_item = last_updated_lte_item_data.isoformat()
            json_last_updated_lte.append(last_updated_lte_item)

    params["last_updated__lte"] = json_last_updated_lte

    json_last_updated_n: Union[Unset, list[str]] = UNSET
    if not isinstance(last_updated_n, Unset):
        json_last_updated_n = []
        for last_updated_n_item_data in last_updated_n:
            last_updated_n_item = last_updated_n_item_data.isoformat()
            json_last_updated_n.append(last_updated_n_item)

    params["last_updated__n"] = json_last_updated_n

    params["limit"] = limit

    json_location: Union[Unset, list[str]] = UNSET
    if not isinstance(location, Unset):
        json_location = location

    params["location"] = json_location

    json_location_n: Union[Unset, list[str]] = UNSET
    if not isinstance(location_n, Unset):
        json_location_n = location_n

    params["location__n"] = json_location_n

    json_location_id: Union[Unset, list[str]] = UNSET
    if not isinstance(location_id, Unset):
        json_location_id = location_id

    params["location_id"] = json_location_id

    json_location_id_n: Union[Unset, list[str]] = UNSET
    if not isinstance(location_id_n, Unset):
        json_location_id_n = location_id_n

    params["location_id__n"] = json_location_id_n

    json_modified_by_request: Union[Unset, str] = UNSET
    if not isinstance(modified_by_request, Unset):
        json_modified_by_request = str(modified_by_request)
    params["modified_by_request"] = json_modified_by_request

    params["offset"] = offset

    params["ordering"] = ordering

    params["q"] = q

    json_rack_id: Union[Unset, list[int]] = UNSET
    if not isinstance(rack_id, Unset):
        json_rack_id = rack_id

    params["rack_id"] = json_rack_id

    json_rack_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(rack_id_n, Unset):
        json_rack_id_n = rack_id_n

    params["rack_id__n"] = json_rack_id_n

    json_region: Union[Unset, list[str]] = UNSET
    if not isinstance(region, Unset):
        json_region = region

    params["region"] = json_region

    json_region_n: Union[Unset, list[str]] = UNSET
    if not isinstance(region_n, Unset):
        json_region_n = region_n

    params["region__n"] = json_region_n

    json_region_id: Union[Unset, list[str]] = UNSET
    if not isinstance(region_id, Unset):
        json_region_id = region_id

    params["region_id"] = json_region_id

    json_region_id_n: Union[Unset, list[str]] = UNSET
    if not isinstance(region_id_n, Unset):
        json_region_id_n = region_id_n

    params["region_id__n"] = json_region_id_n

    json_site: Union[Unset, list[str]] = UNSET
    if not isinstance(site, Unset):
        json_site = site

    params["site"] = json_site

    json_site_n: Union[Unset, list[str]] = UNSET
    if not isinstance(site_n, Unset):
        json_site_n = site_n

    params["site__n"] = json_site_n

    json_site_group: Union[Unset, list[str]] = UNSET
    if not isinstance(site_group, Unset):
        json_site_group = site_group

    params["site_group"] = json_site_group

    json_site_group_n: Union[Unset, list[str]] = UNSET
    if not isinstance(site_group_n, Unset):
        json_site_group_n = site_group_n

    params["site_group__n"] = json_site_group_n

    json_site_group_id: Union[Unset, list[str]] = UNSET
    if not isinstance(site_group_id, Unset):
        json_site_group_id = site_group_id

    params["site_group_id"] = json_site_group_id

    json_site_group_id_n: Union[Unset, list[str]] = UNSET
    if not isinstance(site_group_id_n, Unset):
        json_site_group_id_n = site_group_id_n

    params["site_group_id__n"] = json_site_group_id_n

    json_site_id: Union[Unset, list[int]] = UNSET
    if not isinstance(site_id, Unset):
        json_site_id = site_id

    params["site_id"] = json_site_id

    json_site_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(site_id_n, Unset):
        json_site_id_n = site_id_n

    params["site_id__n"] = json_site_id_n

    json_tag: Union[Unset, list[str]] = UNSET
    if not isinstance(tag, Unset):
        json_tag = tag

    params["tag"] = json_tag

    json_tag_n: Union[Unset, list[str]] = UNSET
    if not isinstance(tag_n, Unset):
        json_tag_n = tag_n

    params["tag__n"] = json_tag_n

    json_tag_id: Union[Unset, list[int]] = UNSET
    if not isinstance(tag_id, Unset):
        json_tag_id = tag_id

    params["tag_id"] = json_tag_id

    json_tag_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(tag_id_n, Unset):
        json_tag_id_n = tag_id_n

    params["tag_id__n"] = json_tag_id_n

    json_tenant: Union[Unset, list[str]] = UNSET
    if not isinstance(tenant, Unset):
        json_tenant = tenant

    params["tenant"] = json_tenant

    json_tenant_n: Union[Unset, list[str]] = UNSET
    if not isinstance(tenant_n, Unset):
        json_tenant_n = tenant_n

    params["tenant__n"] = json_tenant_n

    json_tenant_group: Union[Unset, list[str]] = UNSET
    if not isinstance(tenant_group, Unset):
        json_tenant_group = tenant_group

    params["tenant_group"] = json_tenant_group

    json_tenant_group_n: Union[Unset, list[str]] = UNSET
    if not isinstance(tenant_group_n, Unset):
        json_tenant_group_n = tenant_group_n

    params["tenant_group__n"] = json_tenant_group_n

    json_tenant_group_id: Union[Unset, list[str]] = UNSET
    if not isinstance(tenant_group_id, Unset):
        json_tenant_group_id = tenant_group_id

    params["tenant_group_id"] = json_tenant_group_id

    json_tenant_group_id_n: Union[Unset, list[str]] = UNSET
    if not isinstance(tenant_group_id_n, Unset):
        json_tenant_group_id_n = tenant_group_id_n

    params["tenant_group_id__n"] = json_tenant_group_id_n

    json_tenant_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(tenant_id, Unset):
        json_tenant_id = []
        for tenant_id_item_data in tenant_id:
            tenant_id_item: Union[None, int]
            tenant_id_item = tenant_id_item_data
            json_tenant_id.append(tenant_id_item)

    params["tenant_id"] = json_tenant_id

    json_tenant_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(tenant_id_n, Unset):
        json_tenant_id_n = []
        for tenant_id_n_item_data in tenant_id_n:
            tenant_id_n_item: Union[None, int]
            tenant_id_n_item = tenant_id_n_item_data
            json_tenant_id_n.append(tenant_id_n_item)

    params["tenant_id__n"] = json_tenant_id_n

    params["unit"] = unit

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    json_user: Union[Unset, list[str]] = UNSET
    if not isinstance(user, Unset):
        json_user = user

    params["user"] = json_user

    json_user_n: Union[Unset, list[str]] = UNSET
    if not isinstance(user_n, Unset):
        json_user_n = user_n

    params["user__n"] = json_user_n

    json_user_id: Union[Unset, list[int]] = UNSET
    if not isinstance(user_id, Unset):
        json_user_id = user_id

    params["user_id"] = json_user_id

    json_user_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(user_id_n, Unset):
        json_user_id_n = user_id_n

    params["user_id__n"] = json_user_id_n

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/dcim/rack-reservations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedRackReservationList]:
    if response.status_code == 200:
        response_200 = PaginatedRackReservationList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedRackReservationList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    description: Union[Unset, list[str]] = UNSET,
    description_empty: Union[Unset, bool] = UNSET,
    description_ic: Union[Unset, list[str]] = UNSET,
    description_ie: Union[Unset, list[str]] = UNSET,
    description_iew: Union[Unset, list[str]] = UNSET,
    description_isw: Union[Unset, list[str]] = UNSET,
    description_n: Union[Unset, list[str]] = UNSET,
    description_nic: Union[Unset, list[str]] = UNSET,
    description_nie: Union[Unset, list[str]] = UNSET,
    description_niew: Union[Unset, list[str]] = UNSET,
    description_nisw: Union[Unset, list[str]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[str]] = UNSET,
    location_id_n: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tenant: Union[Unset, list[str]] = UNSET,
    tenant_n: Union[Unset, list[str]] = UNSET,
    tenant_group: Union[Unset, list[str]] = UNSET,
    tenant_group_n: Union[Unset, list[str]] = UNSET,
    tenant_group_id: Union[Unset, list[str]] = UNSET,
    tenant_group_id_n: Union[Unset, list[str]] = UNSET,
    tenant_id: Union[Unset, list[Union[None, int]]] = UNSET,
    tenant_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    unit: Union[Unset, float] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[int]] = UNSET,
    user_id_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedRackReservationList]:
    """Get a list of rack reservation objects.

    Args:
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        description (Union[Unset, list[str]]):
        description_empty (Union[Unset, bool]):
        description_ic (Union[Unset, list[str]]):
        description_ie (Union[Unset, list[str]]):
        description_iew (Union[Unset, list[str]]):
        description_isw (Union[Unset, list[str]]):
        description_n (Union[Unset, list[str]]):
        description_nic (Union[Unset, list[str]]):
        description_nie (Union[Unset, list[str]]):
        description_niew (Union[Unset, list[str]]):
        description_nisw (Union[Unset, list[str]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_id (Union[Unset, list[str]]):
        location_id_n (Union[Unset, list[str]]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        rack_id (Union[Unset, list[int]]):
        rack_id_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        tenant (Union[Unset, list[str]]):
        tenant_n (Union[Unset, list[str]]):
        tenant_group (Union[Unset, list[str]]):
        tenant_group_n (Union[Unset, list[str]]):
        tenant_group_id (Union[Unset, list[str]]):
        tenant_group_id_n (Union[Unset, list[str]]):
        tenant_id (Union[Unset, list[Union[None, int]]]):
        tenant_id_n (Union[Unset, list[Union[None, int]]]):
        unit (Union[Unset, float]):
        updated_by_request (Union[Unset, UUID]):
        user (Union[Unset, list[str]]):
        user_n (Union[Unset, list[str]]):
        user_id (Union[Unset, list[int]]):
        user_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRackReservationList]
    """

    kwargs = _get_kwargs(
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        description=description,
        description_empty=description_empty,
        description_ic=description_ic,
        description_ie=description_ie,
        description_iew=description_iew,
        description_isw=description_isw,
        description_n=description_n,
        description_nic=description_nic,
        description_nie=description_nie,
        description_niew=description_niew,
        description_nisw=description_nisw,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        location=location,
        location_n=location_n,
        location_id=location_id,
        location_id_n=location_id_n,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        q=q,
        rack_id=rack_id,
        rack_id_n=rack_id_n,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        site=site,
        site_n=site_n,
        site_group=site_group,
        site_group_n=site_group_n,
        site_group_id=site_group_id,
        site_group_id_n=site_group_id_n,
        site_id=site_id,
        site_id_n=site_id_n,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        tenant=tenant,
        tenant_n=tenant_n,
        tenant_group=tenant_group,
        tenant_group_n=tenant_group_n,
        tenant_group_id=tenant_group_id,
        tenant_group_id_n=tenant_group_id_n,
        tenant_id=tenant_id,
        tenant_id_n=tenant_id_n,
        unit=unit,
        updated_by_request=updated_by_request,
        user=user,
        user_n=user_n,
        user_id=user_id,
        user_id_n=user_id_n,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    description: Union[Unset, list[str]] = UNSET,
    description_empty: Union[Unset, bool] = UNSET,
    description_ic: Union[Unset, list[str]] = UNSET,
    description_ie: Union[Unset, list[str]] = UNSET,
    description_iew: Union[Unset, list[str]] = UNSET,
    description_isw: Union[Unset, list[str]] = UNSET,
    description_n: Union[Unset, list[str]] = UNSET,
    description_nic: Union[Unset, list[str]] = UNSET,
    description_nie: Union[Unset, list[str]] = UNSET,
    description_niew: Union[Unset, list[str]] = UNSET,
    description_nisw: Union[Unset, list[str]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[str]] = UNSET,
    location_id_n: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tenant: Union[Unset, list[str]] = UNSET,
    tenant_n: Union[Unset, list[str]] = UNSET,
    tenant_group: Union[Unset, list[str]] = UNSET,
    tenant_group_n: Union[Unset, list[str]] = UNSET,
    tenant_group_id: Union[Unset, list[str]] = UNSET,
    tenant_group_id_n: Union[Unset, list[str]] = UNSET,
    tenant_id: Union[Unset, list[Union[None, int]]] = UNSET,
    tenant_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    unit: Union[Unset, float] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[int]] = UNSET,
    user_id_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedRackReservationList]:
    """Get a list of rack reservation objects.

    Args:
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        description (Union[Unset, list[str]]):
        description_empty (Union[Unset, bool]):
        description_ic (Union[Unset, list[str]]):
        description_ie (Union[Unset, list[str]]):
        description_iew (Union[Unset, list[str]]):
        description_isw (Union[Unset, list[str]]):
        description_n (Union[Unset, list[str]]):
        description_nic (Union[Unset, list[str]]):
        description_nie (Union[Unset, list[str]]):
        description_niew (Union[Unset, list[str]]):
        description_nisw (Union[Unset, list[str]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_id (Union[Unset, list[str]]):
        location_id_n (Union[Unset, list[str]]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        rack_id (Union[Unset, list[int]]):
        rack_id_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        tenant (Union[Unset, list[str]]):
        tenant_n (Union[Unset, list[str]]):
        tenant_group (Union[Unset, list[str]]):
        tenant_group_n (Union[Unset, list[str]]):
        tenant_group_id (Union[Unset, list[str]]):
        tenant_group_id_n (Union[Unset, list[str]]):
        tenant_id (Union[Unset, list[Union[None, int]]]):
        tenant_id_n (Union[Unset, list[Union[None, int]]]):
        unit (Union[Unset, float]):
        updated_by_request (Union[Unset, UUID]):
        user (Union[Unset, list[str]]):
        user_n (Union[Unset, list[str]]):
        user_id (Union[Unset, list[int]]):
        user_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRackReservationList
    """

    return sync_detailed(
        client=client,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        description=description,
        description_empty=description_empty,
        description_ic=description_ic,
        description_ie=description_ie,
        description_iew=description_iew,
        description_isw=description_isw,
        description_n=description_n,
        description_nic=description_nic,
        description_nie=description_nie,
        description_niew=description_niew,
        description_nisw=description_nisw,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        location=location,
        location_n=location_n,
        location_id=location_id,
        location_id_n=location_id_n,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        q=q,
        rack_id=rack_id,
        rack_id_n=rack_id_n,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        site=site,
        site_n=site_n,
        site_group=site_group,
        site_group_n=site_group_n,
        site_group_id=site_group_id,
        site_group_id_n=site_group_id_n,
        site_id=site_id,
        site_id_n=site_id_n,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        tenant=tenant,
        tenant_n=tenant_n,
        tenant_group=tenant_group,
        tenant_group_n=tenant_group_n,
        tenant_group_id=tenant_group_id,
        tenant_group_id_n=tenant_group_id_n,
        tenant_id=tenant_id,
        tenant_id_n=tenant_id_n,
        unit=unit,
        updated_by_request=updated_by_request,
        user=user,
        user_n=user_n,
        user_id=user_id,
        user_id_n=user_id_n,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    description: Union[Unset, list[str]] = UNSET,
    description_empty: Union[Unset, bool] = UNSET,
    description_ic: Union[Unset, list[str]] = UNSET,
    description_ie: Union[Unset, list[str]] = UNSET,
    description_iew: Union[Unset, list[str]] = UNSET,
    description_isw: Union[Unset, list[str]] = UNSET,
    description_n: Union[Unset, list[str]] = UNSET,
    description_nic: Union[Unset, list[str]] = UNSET,
    description_nie: Union[Unset, list[str]] = UNSET,
    description_niew: Union[Unset, list[str]] = UNSET,
    description_nisw: Union[Unset, list[str]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[str]] = UNSET,
    location_id_n: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tenant: Union[Unset, list[str]] = UNSET,
    tenant_n: Union[Unset, list[str]] = UNSET,
    tenant_group: Union[Unset, list[str]] = UNSET,
    tenant_group_n: Union[Unset, list[str]] = UNSET,
    tenant_group_id: Union[Unset, list[str]] = UNSET,
    tenant_group_id_n: Union[Unset, list[str]] = UNSET,
    tenant_id: Union[Unset, list[Union[None, int]]] = UNSET,
    tenant_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    unit: Union[Unset, float] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[int]] = UNSET,
    user_id_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedRackReservationList]:
    """Get a list of rack reservation objects.

    Args:
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        description (Union[Unset, list[str]]):
        description_empty (Union[Unset, bool]):
        description_ic (Union[Unset, list[str]]):
        description_ie (Union[Unset, list[str]]):
        description_iew (Union[Unset, list[str]]):
        description_isw (Union[Unset, list[str]]):
        description_n (Union[Unset, list[str]]):
        description_nic (Union[Unset, list[str]]):
        description_nie (Union[Unset, list[str]]):
        description_niew (Union[Unset, list[str]]):
        description_nisw (Union[Unset, list[str]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_id (Union[Unset, list[str]]):
        location_id_n (Union[Unset, list[str]]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        rack_id (Union[Unset, list[int]]):
        rack_id_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        tenant (Union[Unset, list[str]]):
        tenant_n (Union[Unset, list[str]]):
        tenant_group (Union[Unset, list[str]]):
        tenant_group_n (Union[Unset, list[str]]):
        tenant_group_id (Union[Unset, list[str]]):
        tenant_group_id_n (Union[Unset, list[str]]):
        tenant_id (Union[Unset, list[Union[None, int]]]):
        tenant_id_n (Union[Unset, list[Union[None, int]]]):
        unit (Union[Unset, float]):
        updated_by_request (Union[Unset, UUID]):
        user (Union[Unset, list[str]]):
        user_n (Union[Unset, list[str]]):
        user_id (Union[Unset, list[int]]):
        user_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRackReservationList]
    """

    kwargs = _get_kwargs(
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        description=description,
        description_empty=description_empty,
        description_ic=description_ic,
        description_ie=description_ie,
        description_iew=description_iew,
        description_isw=description_isw,
        description_n=description_n,
        description_nic=description_nic,
        description_nie=description_nie,
        description_niew=description_niew,
        description_nisw=description_nisw,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        location=location,
        location_n=location_n,
        location_id=location_id,
        location_id_n=location_id_n,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        q=q,
        rack_id=rack_id,
        rack_id_n=rack_id_n,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        site=site,
        site_n=site_n,
        site_group=site_group,
        site_group_n=site_group_n,
        site_group_id=site_group_id,
        site_group_id_n=site_group_id_n,
        site_id=site_id,
        site_id_n=site_id_n,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        tenant=tenant,
        tenant_n=tenant_n,
        tenant_group=tenant_group,
        tenant_group_n=tenant_group_n,
        tenant_group_id=tenant_group_id,
        tenant_group_id_n=tenant_group_id_n,
        tenant_id=tenant_id,
        tenant_id_n=tenant_id_n,
        unit=unit,
        updated_by_request=updated_by_request,
        user=user,
        user_n=user_n,
        user_id=user_id,
        user_id_n=user_id_n,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    description: Union[Unset, list[str]] = UNSET,
    description_empty: Union[Unset, bool] = UNSET,
    description_ic: Union[Unset, list[str]] = UNSET,
    description_ie: Union[Unset, list[str]] = UNSET,
    description_iew: Union[Unset, list[str]] = UNSET,
    description_isw: Union[Unset, list[str]] = UNSET,
    description_n: Union[Unset, list[str]] = UNSET,
    description_nic: Union[Unset, list[str]] = UNSET,
    description_nie: Union[Unset, list[str]] = UNSET,
    description_niew: Union[Unset, list[str]] = UNSET,
    description_nisw: Union[Unset, list[str]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[str]] = UNSET,
    location_id_n: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    tenant: Union[Unset, list[str]] = UNSET,
    tenant_n: Union[Unset, list[str]] = UNSET,
    tenant_group: Union[Unset, list[str]] = UNSET,
    tenant_group_n: Union[Unset, list[str]] = UNSET,
    tenant_group_id: Union[Unset, list[str]] = UNSET,
    tenant_group_id_n: Union[Unset, list[str]] = UNSET,
    tenant_id: Union[Unset, list[Union[None, int]]] = UNSET,
    tenant_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    unit: Union[Unset, float] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    user: Union[Unset, list[str]] = UNSET,
    user_n: Union[Unset, list[str]] = UNSET,
    user_id: Union[Unset, list[int]] = UNSET,
    user_id_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedRackReservationList]:
    """Get a list of rack reservation objects.

    Args:
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        description (Union[Unset, list[str]]):
        description_empty (Union[Unset, bool]):
        description_ic (Union[Unset, list[str]]):
        description_ie (Union[Unset, list[str]]):
        description_iew (Union[Unset, list[str]]):
        description_isw (Union[Unset, list[str]]):
        description_n (Union[Unset, list[str]]):
        description_nic (Union[Unset, list[str]]):
        description_nie (Union[Unset, list[str]]):
        description_niew (Union[Unset, list[str]]):
        description_nisw (Union[Unset, list[str]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_id (Union[Unset, list[str]]):
        location_id_n (Union[Unset, list[str]]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        rack_id (Union[Unset, list[int]]):
        rack_id_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        tenant (Union[Unset, list[str]]):
        tenant_n (Union[Unset, list[str]]):
        tenant_group (Union[Unset, list[str]]):
        tenant_group_n (Union[Unset, list[str]]):
        tenant_group_id (Union[Unset, list[str]]):
        tenant_group_id_n (Union[Unset, list[str]]):
        tenant_id (Union[Unset, list[Union[None, int]]]):
        tenant_id_n (Union[Unset, list[Union[None, int]]]):
        unit (Union[Unset, float]):
        updated_by_request (Union[Unset, UUID]):
        user (Union[Unset, list[str]]):
        user_n (Union[Unset, list[str]]):
        user_id (Union[Unset, list[int]]):
        user_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRackReservationList
    """

    return (
        await asyncio_detailed(
            client=client,
            created=created,
            created_empty=created_empty,
            created_gt=created_gt,
            created_gte=created_gte,
            created_lt=created_lt,
            created_lte=created_lte,
            created_n=created_n,
            created_by_request=created_by_request,
            description=description,
            description_empty=description_empty,
            description_ic=description_ic,
            description_ie=description_ie,
            description_iew=description_iew,
            description_isw=description_isw,
            description_n=description_n,
            description_nic=description_nic,
            description_nie=description_nie,
            description_niew=description_niew,
            description_nisw=description_nisw,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            last_updated=last_updated,
            last_updated_empty=last_updated_empty,
            last_updated_gt=last_updated_gt,
            last_updated_gte=last_updated_gte,
            last_updated_lt=last_updated_lt,
            last_updated_lte=last_updated_lte,
            last_updated_n=last_updated_n,
            limit=limit,
            location=location,
            location_n=location_n,
            location_id=location_id,
            location_id_n=location_id_n,
            modified_by_request=modified_by_request,
            offset=offset,
            ordering=ordering,
            q=q,
            rack_id=rack_id,
            rack_id_n=rack_id_n,
            region=region,
            region_n=region_n,
            region_id=region_id,
            region_id_n=region_id_n,
            site=site,
            site_n=site_n,
            site_group=site_group,
            site_group_n=site_group_n,
            site_group_id=site_group_id,
            site_group_id_n=site_group_id_n,
            site_id=site_id,
            site_id_n=site_id_n,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
            tenant=tenant,
            tenant_n=tenant_n,
            tenant_group=tenant_group,
            tenant_group_n=tenant_group_n,
            tenant_group_id=tenant_group_id,
            tenant_group_id_n=tenant_group_id_n,
            tenant_id=tenant_id,
            tenant_id_n=tenant_id_n,
            unit=unit,
            updated_by_request=updated_by_request,
            user=user,
            user_n=user_n,
            user_id=user_id,
            user_id_n=user_id_n,
        )
    ).parsed
