import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_virtual_circuit_termination_list import PaginatedVirtualCircuitTerminationList
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
    interface_id: Union[Unset, list[int]] = UNSET,
    interface_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    provider: Union[Unset, list[str]] = UNSET,
    provider_n: Union[Unset, list[str]] = UNSET,
    provider_account: Union[Unset, list[str]] = UNSET,
    provider_account_n: Union[Unset, list[str]] = UNSET,
    provider_account_id: Union[Unset, list[int]] = UNSET,
    provider_account_id_n: Union[Unset, list[int]] = UNSET,
    provider_id: Union[Unset, list[int]] = UNSET,
    provider_id_n: Union[Unset, list[int]] = UNSET,
    provider_network_id: Union[Unset, list[int]] = UNSET,
    provider_network_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_empty: Union[Unset, bool] = UNSET,
    role_ic: Union[Unset, list[str]] = UNSET,
    role_ie: Union[Unset, list[str]] = UNSET,
    role_iew: Union[Unset, list[str]] = UNSET,
    role_isw: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_nic: Union[Unset, list[str]] = UNSET,
    role_nie: Union[Unset, list[str]] = UNSET,
    role_niew: Union[Unset, list[str]] = UNSET,
    role_nisw: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_circuit_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_id_n: Union[Unset, list[int]] = UNSET,
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

    json_interface_id: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_id, Unset):
        json_interface_id = interface_id

    params["interface_id"] = json_interface_id

    json_interface_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_id_n, Unset):
        json_interface_id_n = interface_id_n

    params["interface_id__n"] = json_interface_id_n

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

    json_modified_by_request: Union[Unset, str] = UNSET
    if not isinstance(modified_by_request, Unset):
        json_modified_by_request = str(modified_by_request)
    params["modified_by_request"] = json_modified_by_request

    params["offset"] = offset

    params["ordering"] = ordering

    json_provider: Union[Unset, list[str]] = UNSET
    if not isinstance(provider, Unset):
        json_provider = provider

    params["provider"] = json_provider

    json_provider_n: Union[Unset, list[str]] = UNSET
    if not isinstance(provider_n, Unset):
        json_provider_n = provider_n

    params["provider__n"] = json_provider_n

    json_provider_account: Union[Unset, list[str]] = UNSET
    if not isinstance(provider_account, Unset):
        json_provider_account = provider_account

    params["provider_account"] = json_provider_account

    json_provider_account_n: Union[Unset, list[str]] = UNSET
    if not isinstance(provider_account_n, Unset):
        json_provider_account_n = provider_account_n

    params["provider_account__n"] = json_provider_account_n

    json_provider_account_id: Union[Unset, list[int]] = UNSET
    if not isinstance(provider_account_id, Unset):
        json_provider_account_id = provider_account_id

    params["provider_account_id"] = json_provider_account_id

    json_provider_account_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(provider_account_id_n, Unset):
        json_provider_account_id_n = provider_account_id_n

    params["provider_account_id__n"] = json_provider_account_id_n

    json_provider_id: Union[Unset, list[int]] = UNSET
    if not isinstance(provider_id, Unset):
        json_provider_id = provider_id

    params["provider_id"] = json_provider_id

    json_provider_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(provider_id_n, Unset):
        json_provider_id_n = provider_id_n

    params["provider_id__n"] = json_provider_id_n

    json_provider_network_id: Union[Unset, list[int]] = UNSET
    if not isinstance(provider_network_id, Unset):
        json_provider_network_id = provider_network_id

    params["provider_network_id"] = json_provider_network_id

    json_provider_network_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(provider_network_id_n, Unset):
        json_provider_network_id_n = provider_network_id_n

    params["provider_network_id__n"] = json_provider_network_id_n

    params["q"] = q

    json_role: Union[Unset, list[str]] = UNSET
    if not isinstance(role, Unset):
        json_role = role

    params["role"] = json_role

    params["role__empty"] = role_empty

    json_role_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(role_ic, Unset):
        json_role_ic = role_ic

    params["role__ic"] = json_role_ic

    json_role_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(role_ie, Unset):
        json_role_ie = role_ie

    params["role__ie"] = json_role_ie

    json_role_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(role_iew, Unset):
        json_role_iew = role_iew

    params["role__iew"] = json_role_iew

    json_role_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(role_isw, Unset):
        json_role_isw = role_isw

    params["role__isw"] = json_role_isw

    json_role_n: Union[Unset, list[str]] = UNSET
    if not isinstance(role_n, Unset):
        json_role_n = role_n

    params["role__n"] = json_role_n

    json_role_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(role_nic, Unset):
        json_role_nic = role_nic

    params["role__nic"] = json_role_nic

    json_role_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(role_nie, Unset):
        json_role_nie = role_nie

    params["role__nie"] = json_role_nie

    json_role_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(role_niew, Unset):
        json_role_niew = role_niew

    params["role__niew"] = json_role_niew

    json_role_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(role_nisw, Unset):
        json_role_nisw = role_nisw

    params["role__nisw"] = json_role_nisw

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

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    json_virtual_circuit_id: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_circuit_id, Unset):
        json_virtual_circuit_id = virtual_circuit_id

    params["virtual_circuit_id"] = json_virtual_circuit_id

    json_virtual_circuit_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_circuit_id_n, Unset):
        json_virtual_circuit_id_n = virtual_circuit_id_n

    params["virtual_circuit_id__n"] = json_virtual_circuit_id_n

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/circuits/virtual-circuit-terminations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedVirtualCircuitTerminationList]:
    if response.status_code == 200:
        response_200 = PaginatedVirtualCircuitTerminationList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedVirtualCircuitTerminationList]:
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
    interface_id: Union[Unset, list[int]] = UNSET,
    interface_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    provider: Union[Unset, list[str]] = UNSET,
    provider_n: Union[Unset, list[str]] = UNSET,
    provider_account: Union[Unset, list[str]] = UNSET,
    provider_account_n: Union[Unset, list[str]] = UNSET,
    provider_account_id: Union[Unset, list[int]] = UNSET,
    provider_account_id_n: Union[Unset, list[int]] = UNSET,
    provider_id: Union[Unset, list[int]] = UNSET,
    provider_id_n: Union[Unset, list[int]] = UNSET,
    provider_network_id: Union[Unset, list[int]] = UNSET,
    provider_network_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_empty: Union[Unset, bool] = UNSET,
    role_ic: Union[Unset, list[str]] = UNSET,
    role_ie: Union[Unset, list[str]] = UNSET,
    role_iew: Union[Unset, list[str]] = UNSET,
    role_isw: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_nic: Union[Unset, list[str]] = UNSET,
    role_nie: Union[Unset, list[str]] = UNSET,
    role_niew: Union[Unset, list[str]] = UNSET,
    role_nisw: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_circuit_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_id_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedVirtualCircuitTerminationList]:
    """Get a list of virtual circuit termination objects.

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
        interface_id (Union[Unset, list[int]]):
        interface_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        provider (Union[Unset, list[str]]):
        provider_n (Union[Unset, list[str]]):
        provider_account (Union[Unset, list[str]]):
        provider_account_n (Union[Unset, list[str]]):
        provider_account_id (Union[Unset, list[int]]):
        provider_account_id_n (Union[Unset, list[int]]):
        provider_id (Union[Unset, list[int]]):
        provider_id_n (Union[Unset, list[int]]):
        provider_network_id (Union[Unset, list[int]]):
        provider_network_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        role (Union[Unset, list[str]]):
        role_empty (Union[Unset, bool]):
        role_ic (Union[Unset, list[str]]):
        role_ie (Union[Unset, list[str]]):
        role_iew (Union[Unset, list[str]]):
        role_isw (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_nic (Union[Unset, list[str]]):
        role_nie (Union[Unset, list[str]]):
        role_niew (Union[Unset, list[str]]):
        role_nisw (Union[Unset, list[str]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        virtual_circuit_id (Union[Unset, list[int]]):
        virtual_circuit_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedVirtualCircuitTerminationList]
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
        interface_id=interface_id,
        interface_id_n=interface_id_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        provider=provider,
        provider_n=provider_n,
        provider_account=provider_account,
        provider_account_n=provider_account_n,
        provider_account_id=provider_account_id,
        provider_account_id_n=provider_account_id_n,
        provider_id=provider_id,
        provider_id_n=provider_id_n,
        provider_network_id=provider_network_id,
        provider_network_id_n=provider_network_id_n,
        q=q,
        role=role,
        role_empty=role_empty,
        role_ic=role_ic,
        role_ie=role_ie,
        role_iew=role_iew,
        role_isw=role_isw,
        role_n=role_n,
        role_nic=role_nic,
        role_nie=role_nie,
        role_niew=role_niew,
        role_nisw=role_nisw,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
        virtual_circuit_id=virtual_circuit_id,
        virtual_circuit_id_n=virtual_circuit_id_n,
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
    interface_id: Union[Unset, list[int]] = UNSET,
    interface_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    provider: Union[Unset, list[str]] = UNSET,
    provider_n: Union[Unset, list[str]] = UNSET,
    provider_account: Union[Unset, list[str]] = UNSET,
    provider_account_n: Union[Unset, list[str]] = UNSET,
    provider_account_id: Union[Unset, list[int]] = UNSET,
    provider_account_id_n: Union[Unset, list[int]] = UNSET,
    provider_id: Union[Unset, list[int]] = UNSET,
    provider_id_n: Union[Unset, list[int]] = UNSET,
    provider_network_id: Union[Unset, list[int]] = UNSET,
    provider_network_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_empty: Union[Unset, bool] = UNSET,
    role_ic: Union[Unset, list[str]] = UNSET,
    role_ie: Union[Unset, list[str]] = UNSET,
    role_iew: Union[Unset, list[str]] = UNSET,
    role_isw: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_nic: Union[Unset, list[str]] = UNSET,
    role_nie: Union[Unset, list[str]] = UNSET,
    role_niew: Union[Unset, list[str]] = UNSET,
    role_nisw: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_circuit_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_id_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedVirtualCircuitTerminationList]:
    """Get a list of virtual circuit termination objects.

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
        interface_id (Union[Unset, list[int]]):
        interface_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        provider (Union[Unset, list[str]]):
        provider_n (Union[Unset, list[str]]):
        provider_account (Union[Unset, list[str]]):
        provider_account_n (Union[Unset, list[str]]):
        provider_account_id (Union[Unset, list[int]]):
        provider_account_id_n (Union[Unset, list[int]]):
        provider_id (Union[Unset, list[int]]):
        provider_id_n (Union[Unset, list[int]]):
        provider_network_id (Union[Unset, list[int]]):
        provider_network_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        role (Union[Unset, list[str]]):
        role_empty (Union[Unset, bool]):
        role_ic (Union[Unset, list[str]]):
        role_ie (Union[Unset, list[str]]):
        role_iew (Union[Unset, list[str]]):
        role_isw (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_nic (Union[Unset, list[str]]):
        role_nie (Union[Unset, list[str]]):
        role_niew (Union[Unset, list[str]]):
        role_nisw (Union[Unset, list[str]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        virtual_circuit_id (Union[Unset, list[int]]):
        virtual_circuit_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedVirtualCircuitTerminationList
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
        interface_id=interface_id,
        interface_id_n=interface_id_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        provider=provider,
        provider_n=provider_n,
        provider_account=provider_account,
        provider_account_n=provider_account_n,
        provider_account_id=provider_account_id,
        provider_account_id_n=provider_account_id_n,
        provider_id=provider_id,
        provider_id_n=provider_id_n,
        provider_network_id=provider_network_id,
        provider_network_id_n=provider_network_id_n,
        q=q,
        role=role,
        role_empty=role_empty,
        role_ic=role_ic,
        role_ie=role_ie,
        role_iew=role_iew,
        role_isw=role_isw,
        role_n=role_n,
        role_nic=role_nic,
        role_nie=role_nie,
        role_niew=role_niew,
        role_nisw=role_nisw,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
        virtual_circuit_id=virtual_circuit_id,
        virtual_circuit_id_n=virtual_circuit_id_n,
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
    interface_id: Union[Unset, list[int]] = UNSET,
    interface_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    provider: Union[Unset, list[str]] = UNSET,
    provider_n: Union[Unset, list[str]] = UNSET,
    provider_account: Union[Unset, list[str]] = UNSET,
    provider_account_n: Union[Unset, list[str]] = UNSET,
    provider_account_id: Union[Unset, list[int]] = UNSET,
    provider_account_id_n: Union[Unset, list[int]] = UNSET,
    provider_id: Union[Unset, list[int]] = UNSET,
    provider_id_n: Union[Unset, list[int]] = UNSET,
    provider_network_id: Union[Unset, list[int]] = UNSET,
    provider_network_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_empty: Union[Unset, bool] = UNSET,
    role_ic: Union[Unset, list[str]] = UNSET,
    role_ie: Union[Unset, list[str]] = UNSET,
    role_iew: Union[Unset, list[str]] = UNSET,
    role_isw: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_nic: Union[Unset, list[str]] = UNSET,
    role_nie: Union[Unset, list[str]] = UNSET,
    role_niew: Union[Unset, list[str]] = UNSET,
    role_nisw: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_circuit_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_id_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedVirtualCircuitTerminationList]:
    """Get a list of virtual circuit termination objects.

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
        interface_id (Union[Unset, list[int]]):
        interface_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        provider (Union[Unset, list[str]]):
        provider_n (Union[Unset, list[str]]):
        provider_account (Union[Unset, list[str]]):
        provider_account_n (Union[Unset, list[str]]):
        provider_account_id (Union[Unset, list[int]]):
        provider_account_id_n (Union[Unset, list[int]]):
        provider_id (Union[Unset, list[int]]):
        provider_id_n (Union[Unset, list[int]]):
        provider_network_id (Union[Unset, list[int]]):
        provider_network_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        role (Union[Unset, list[str]]):
        role_empty (Union[Unset, bool]):
        role_ic (Union[Unset, list[str]]):
        role_ie (Union[Unset, list[str]]):
        role_iew (Union[Unset, list[str]]):
        role_isw (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_nic (Union[Unset, list[str]]):
        role_nie (Union[Unset, list[str]]):
        role_niew (Union[Unset, list[str]]):
        role_nisw (Union[Unset, list[str]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        virtual_circuit_id (Union[Unset, list[int]]):
        virtual_circuit_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedVirtualCircuitTerminationList]
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
        interface_id=interface_id,
        interface_id_n=interface_id_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        provider=provider,
        provider_n=provider_n,
        provider_account=provider_account,
        provider_account_n=provider_account_n,
        provider_account_id=provider_account_id,
        provider_account_id_n=provider_account_id_n,
        provider_id=provider_id,
        provider_id_n=provider_id_n,
        provider_network_id=provider_network_id,
        provider_network_id_n=provider_network_id_n,
        q=q,
        role=role,
        role_empty=role_empty,
        role_ic=role_ic,
        role_ie=role_ie,
        role_iew=role_iew,
        role_isw=role_isw,
        role_n=role_n,
        role_nic=role_nic,
        role_nie=role_nie,
        role_niew=role_niew,
        role_nisw=role_nisw,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
        virtual_circuit_id=virtual_circuit_id,
        virtual_circuit_id_n=virtual_circuit_id_n,
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
    interface_id: Union[Unset, list[int]] = UNSET,
    interface_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    provider: Union[Unset, list[str]] = UNSET,
    provider_n: Union[Unset, list[str]] = UNSET,
    provider_account: Union[Unset, list[str]] = UNSET,
    provider_account_n: Union[Unset, list[str]] = UNSET,
    provider_account_id: Union[Unset, list[int]] = UNSET,
    provider_account_id_n: Union[Unset, list[int]] = UNSET,
    provider_id: Union[Unset, list[int]] = UNSET,
    provider_id_n: Union[Unset, list[int]] = UNSET,
    provider_network_id: Union[Unset, list[int]] = UNSET,
    provider_network_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_empty: Union[Unset, bool] = UNSET,
    role_ic: Union[Unset, list[str]] = UNSET,
    role_ie: Union[Unset, list[str]] = UNSET,
    role_iew: Union[Unset, list[str]] = UNSET,
    role_isw: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_nic: Union[Unset, list[str]] = UNSET,
    role_nie: Union[Unset, list[str]] = UNSET,
    role_niew: Union[Unset, list[str]] = UNSET,
    role_nisw: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_circuit_id: Union[Unset, list[int]] = UNSET,
    virtual_circuit_id_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedVirtualCircuitTerminationList]:
    """Get a list of virtual circuit termination objects.

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
        interface_id (Union[Unset, list[int]]):
        interface_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        provider (Union[Unset, list[str]]):
        provider_n (Union[Unset, list[str]]):
        provider_account (Union[Unset, list[str]]):
        provider_account_n (Union[Unset, list[str]]):
        provider_account_id (Union[Unset, list[int]]):
        provider_account_id_n (Union[Unset, list[int]]):
        provider_id (Union[Unset, list[int]]):
        provider_id_n (Union[Unset, list[int]]):
        provider_network_id (Union[Unset, list[int]]):
        provider_network_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        role (Union[Unset, list[str]]):
        role_empty (Union[Unset, bool]):
        role_ic (Union[Unset, list[str]]):
        role_ie (Union[Unset, list[str]]):
        role_iew (Union[Unset, list[str]]):
        role_isw (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_nic (Union[Unset, list[str]]):
        role_nie (Union[Unset, list[str]]):
        role_niew (Union[Unset, list[str]]):
        role_nisw (Union[Unset, list[str]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        virtual_circuit_id (Union[Unset, list[int]]):
        virtual_circuit_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedVirtualCircuitTerminationList
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
            interface_id=interface_id,
            interface_id_n=interface_id_n,
            last_updated=last_updated,
            last_updated_empty=last_updated_empty,
            last_updated_gt=last_updated_gt,
            last_updated_gte=last_updated_gte,
            last_updated_lt=last_updated_lt,
            last_updated_lte=last_updated_lte,
            last_updated_n=last_updated_n,
            limit=limit,
            modified_by_request=modified_by_request,
            offset=offset,
            ordering=ordering,
            provider=provider,
            provider_n=provider_n,
            provider_account=provider_account,
            provider_account_n=provider_account_n,
            provider_account_id=provider_account_id,
            provider_account_id_n=provider_account_id_n,
            provider_id=provider_id,
            provider_id_n=provider_id_n,
            provider_network_id=provider_network_id,
            provider_network_id_n=provider_network_id_n,
            q=q,
            role=role,
            role_empty=role_empty,
            role_ic=role_ic,
            role_ie=role_ie,
            role_iew=role_iew,
            role_isw=role_isw,
            role_n=role_n,
            role_nic=role_nic,
            role_nie=role_nie,
            role_niew=role_niew,
            role_nisw=role_nisw,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
            updated_by_request=updated_by_request,
            virtual_circuit_id=virtual_circuit_id,
            virtual_circuit_id_n=virtual_circuit_id_n,
        )
    ).parsed
