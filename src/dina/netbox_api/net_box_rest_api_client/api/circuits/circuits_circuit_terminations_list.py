import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.circuits_circuit_terminations_list_cable_end import CircuitsCircuitTerminationsListCableEnd
from ...models.circuits_circuit_terminations_list_termination_side import CircuitsCircuitTerminationsListTerminationSide
from ...models.paginated_circuit_termination_list import PaginatedCircuitTerminationList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cable_end: Union[Unset, CircuitsCircuitTerminationsListCableEnd] = UNSET,
    cable_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cable_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cabled: Union[Unset, bool] = UNSET,
    circuit_id: Union[Unset, list[int]] = UNSET,
    circuit_id_n: Union[Unset, list[int]] = UNSET,
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
    mark_connected: Union[Unset, bool] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    occupied: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    port_speed: Union[Unset, list[int]] = UNSET,
    port_speed_empty: Union[Unset, bool] = UNSET,
    port_speed_gt: Union[Unset, list[int]] = UNSET,
    port_speed_gte: Union[Unset, list[int]] = UNSET,
    port_speed_lt: Union[Unset, list[int]] = UNSET,
    port_speed_lte: Union[Unset, list[int]] = UNSET,
    port_speed_n: Union[Unset, list[int]] = UNSET,
    pp_info: Union[Unset, list[str]] = UNSET,
    pp_info_empty: Union[Unset, bool] = UNSET,
    pp_info_ic: Union[Unset, list[str]] = UNSET,
    pp_info_ie: Union[Unset, list[str]] = UNSET,
    pp_info_iew: Union[Unset, list[str]] = UNSET,
    pp_info_isw: Union[Unset, list[str]] = UNSET,
    pp_info_n: Union[Unset, list[str]] = UNSET,
    pp_info_nic: Union[Unset, list[str]] = UNSET,
    pp_info_nie: Union[Unset, list[str]] = UNSET,
    pp_info_niew: Union[Unset, list[str]] = UNSET,
    pp_info_nisw: Union[Unset, list[str]] = UNSET,
    provider: Union[Unset, list[str]] = UNSET,
    provider_n: Union[Unset, list[str]] = UNSET,
    provider_id: Union[Unset, list[int]] = UNSET,
    provider_id_n: Union[Unset, list[int]] = UNSET,
    provider_network_id: Union[Unset, list[int]] = UNSET,
    provider_network_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
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
    term_side: Union[Unset, CircuitsCircuitTerminationsListTerminationSide] = UNSET,
    termination_id: Union[Unset, list[int]] = UNSET,
    termination_id_empty: Union[Unset, bool] = UNSET,
    termination_id_gt: Union[Unset, list[int]] = UNSET,
    termination_id_gte: Union[Unset, list[int]] = UNSET,
    termination_id_lt: Union[Unset, list[int]] = UNSET,
    termination_id_lte: Union[Unset, list[int]] = UNSET,
    termination_id_n: Union[Unset, list[int]] = UNSET,
    termination_type: Union[Unset, str] = UNSET,
    termination_type_n: Union[Unset, str] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    upstream_speed: Union[Unset, list[int]] = UNSET,
    upstream_speed_empty: Union[Unset, bool] = UNSET,
    upstream_speed_gt: Union[Unset, list[int]] = UNSET,
    upstream_speed_gte: Union[Unset, list[int]] = UNSET,
    upstream_speed_lt: Union[Unset, list[int]] = UNSET,
    upstream_speed_lte: Union[Unset, list[int]] = UNSET,
    upstream_speed_n: Union[Unset, list[int]] = UNSET,
    xconnect_id: Union[Unset, list[str]] = UNSET,
    xconnect_id_empty: Union[Unset, bool] = UNSET,
    xconnect_id_ic: Union[Unset, list[str]] = UNSET,
    xconnect_id_ie: Union[Unset, list[str]] = UNSET,
    xconnect_id_iew: Union[Unset, list[str]] = UNSET,
    xconnect_id_isw: Union[Unset, list[str]] = UNSET,
    xconnect_id_n: Union[Unset, list[str]] = UNSET,
    xconnect_id_nic: Union[Unset, list[str]] = UNSET,
    xconnect_id_nie: Union[Unset, list[str]] = UNSET,
    xconnect_id_niew: Union[Unset, list[str]] = UNSET,
    xconnect_id_nisw: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_cable_end: Union[Unset, str] = UNSET
    if not isinstance(cable_end, Unset):
        json_cable_end = cable_end.value

    params["cable_end"] = json_cable_end

    json_cable_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(cable_id, Unset):
        json_cable_id = []
        for cable_id_item_data in cable_id:
            cable_id_item: Union[None, int]
            cable_id_item = cable_id_item_data
            json_cable_id.append(cable_id_item)

    params["cable_id"] = json_cable_id

    json_cable_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(cable_id_n, Unset):
        json_cable_id_n = []
        for cable_id_n_item_data in cable_id_n:
            cable_id_n_item: Union[None, int]
            cable_id_n_item = cable_id_n_item_data
            json_cable_id_n.append(cable_id_n_item)

    params["cable_id__n"] = json_cable_id_n

    params["cabled"] = cabled

    json_circuit_id: Union[Unset, list[int]] = UNSET
    if not isinstance(circuit_id, Unset):
        json_circuit_id = circuit_id

    params["circuit_id"] = json_circuit_id

    json_circuit_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(circuit_id_n, Unset):
        json_circuit_id_n = circuit_id_n

    params["circuit_id__n"] = json_circuit_id_n

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

    params["mark_connected"] = mark_connected

    json_modified_by_request: Union[Unset, str] = UNSET
    if not isinstance(modified_by_request, Unset):
        json_modified_by_request = str(modified_by_request)
    params["modified_by_request"] = json_modified_by_request

    params["occupied"] = occupied

    params["offset"] = offset

    params["ordering"] = ordering

    json_port_speed: Union[Unset, list[int]] = UNSET
    if not isinstance(port_speed, Unset):
        json_port_speed = port_speed

    params["port_speed"] = json_port_speed

    params["port_speed__empty"] = port_speed_empty

    json_port_speed_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(port_speed_gt, Unset):
        json_port_speed_gt = port_speed_gt

    params["port_speed__gt"] = json_port_speed_gt

    json_port_speed_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(port_speed_gte, Unset):
        json_port_speed_gte = port_speed_gte

    params["port_speed__gte"] = json_port_speed_gte

    json_port_speed_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(port_speed_lt, Unset):
        json_port_speed_lt = port_speed_lt

    params["port_speed__lt"] = json_port_speed_lt

    json_port_speed_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(port_speed_lte, Unset):
        json_port_speed_lte = port_speed_lte

    params["port_speed__lte"] = json_port_speed_lte

    json_port_speed_n: Union[Unset, list[int]] = UNSET
    if not isinstance(port_speed_n, Unset):
        json_port_speed_n = port_speed_n

    params["port_speed__n"] = json_port_speed_n

    json_pp_info: Union[Unset, list[str]] = UNSET
    if not isinstance(pp_info, Unset):
        json_pp_info = pp_info

    params["pp_info"] = json_pp_info

    params["pp_info__empty"] = pp_info_empty

    json_pp_info_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(pp_info_ic, Unset):
        json_pp_info_ic = pp_info_ic

    params["pp_info__ic"] = json_pp_info_ic

    json_pp_info_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(pp_info_ie, Unset):
        json_pp_info_ie = pp_info_ie

    params["pp_info__ie"] = json_pp_info_ie

    json_pp_info_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(pp_info_iew, Unset):
        json_pp_info_iew = pp_info_iew

    params["pp_info__iew"] = json_pp_info_iew

    json_pp_info_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(pp_info_isw, Unset):
        json_pp_info_isw = pp_info_isw

    params["pp_info__isw"] = json_pp_info_isw

    json_pp_info_n: Union[Unset, list[str]] = UNSET
    if not isinstance(pp_info_n, Unset):
        json_pp_info_n = pp_info_n

    params["pp_info__n"] = json_pp_info_n

    json_pp_info_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(pp_info_nic, Unset):
        json_pp_info_nic = pp_info_nic

    params["pp_info__nic"] = json_pp_info_nic

    json_pp_info_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(pp_info_nie, Unset):
        json_pp_info_nie = pp_info_nie

    params["pp_info__nie"] = json_pp_info_nie

    json_pp_info_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(pp_info_niew, Unset):
        json_pp_info_niew = pp_info_niew

    params["pp_info__niew"] = json_pp_info_niew

    json_pp_info_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(pp_info_nisw, Unset):
        json_pp_info_nisw = pp_info_nisw

    params["pp_info__nisw"] = json_pp_info_nisw

    json_provider: Union[Unset, list[str]] = UNSET
    if not isinstance(provider, Unset):
        json_provider = provider

    params["provider"] = json_provider

    json_provider_n: Union[Unset, list[str]] = UNSET
    if not isinstance(provider_n, Unset):
        json_provider_n = provider_n

    params["provider__n"] = json_provider_n

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

    json_term_side: Union[Unset, str] = UNSET
    if not isinstance(term_side, Unset):
        json_term_side = term_side.value

    params["term_side"] = json_term_side

    json_termination_id: Union[Unset, list[int]] = UNSET
    if not isinstance(termination_id, Unset):
        json_termination_id = termination_id

    params["termination_id"] = json_termination_id

    params["termination_id__empty"] = termination_id_empty

    json_termination_id_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(termination_id_gt, Unset):
        json_termination_id_gt = termination_id_gt

    params["termination_id__gt"] = json_termination_id_gt

    json_termination_id_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(termination_id_gte, Unset):
        json_termination_id_gte = termination_id_gte

    params["termination_id__gte"] = json_termination_id_gte

    json_termination_id_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(termination_id_lt, Unset):
        json_termination_id_lt = termination_id_lt

    params["termination_id__lt"] = json_termination_id_lt

    json_termination_id_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(termination_id_lte, Unset):
        json_termination_id_lte = termination_id_lte

    params["termination_id__lte"] = json_termination_id_lte

    json_termination_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(termination_id_n, Unset):
        json_termination_id_n = termination_id_n

    params["termination_id__n"] = json_termination_id_n

    params["termination_type"] = termination_type

    params["termination_type__n"] = termination_type_n

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    json_upstream_speed: Union[Unset, list[int]] = UNSET
    if not isinstance(upstream_speed, Unset):
        json_upstream_speed = upstream_speed

    params["upstream_speed"] = json_upstream_speed

    params["upstream_speed__empty"] = upstream_speed_empty

    json_upstream_speed_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(upstream_speed_gt, Unset):
        json_upstream_speed_gt = upstream_speed_gt

    params["upstream_speed__gt"] = json_upstream_speed_gt

    json_upstream_speed_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(upstream_speed_gte, Unset):
        json_upstream_speed_gte = upstream_speed_gte

    params["upstream_speed__gte"] = json_upstream_speed_gte

    json_upstream_speed_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(upstream_speed_lt, Unset):
        json_upstream_speed_lt = upstream_speed_lt

    params["upstream_speed__lt"] = json_upstream_speed_lt

    json_upstream_speed_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(upstream_speed_lte, Unset):
        json_upstream_speed_lte = upstream_speed_lte

    params["upstream_speed__lte"] = json_upstream_speed_lte

    json_upstream_speed_n: Union[Unset, list[int]] = UNSET
    if not isinstance(upstream_speed_n, Unset):
        json_upstream_speed_n = upstream_speed_n

    params["upstream_speed__n"] = json_upstream_speed_n

    json_xconnect_id: Union[Unset, list[str]] = UNSET
    if not isinstance(xconnect_id, Unset):
        json_xconnect_id = xconnect_id

    params["xconnect_id"] = json_xconnect_id

    params["xconnect_id__empty"] = xconnect_id_empty

    json_xconnect_id_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(xconnect_id_ic, Unset):
        json_xconnect_id_ic = xconnect_id_ic

    params["xconnect_id__ic"] = json_xconnect_id_ic

    json_xconnect_id_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(xconnect_id_ie, Unset):
        json_xconnect_id_ie = xconnect_id_ie

    params["xconnect_id__ie"] = json_xconnect_id_ie

    json_xconnect_id_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(xconnect_id_iew, Unset):
        json_xconnect_id_iew = xconnect_id_iew

    params["xconnect_id__iew"] = json_xconnect_id_iew

    json_xconnect_id_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(xconnect_id_isw, Unset):
        json_xconnect_id_isw = xconnect_id_isw

    params["xconnect_id__isw"] = json_xconnect_id_isw

    json_xconnect_id_n: Union[Unset, list[str]] = UNSET
    if not isinstance(xconnect_id_n, Unset):
        json_xconnect_id_n = xconnect_id_n

    params["xconnect_id__n"] = json_xconnect_id_n

    json_xconnect_id_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(xconnect_id_nic, Unset):
        json_xconnect_id_nic = xconnect_id_nic

    params["xconnect_id__nic"] = json_xconnect_id_nic

    json_xconnect_id_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(xconnect_id_nie, Unset):
        json_xconnect_id_nie = xconnect_id_nie

    params["xconnect_id__nie"] = json_xconnect_id_nie

    json_xconnect_id_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(xconnect_id_niew, Unset):
        json_xconnect_id_niew = xconnect_id_niew

    params["xconnect_id__niew"] = json_xconnect_id_niew

    json_xconnect_id_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(xconnect_id_nisw, Unset):
        json_xconnect_id_nisw = xconnect_id_nisw

    params["xconnect_id__nisw"] = json_xconnect_id_nisw

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/circuits/circuit-terminations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedCircuitTerminationList]:
    if response.status_code == 200:
        response_200 = PaginatedCircuitTerminationList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedCircuitTerminationList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cable_end: Union[Unset, CircuitsCircuitTerminationsListCableEnd] = UNSET,
    cable_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cable_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cabled: Union[Unset, bool] = UNSET,
    circuit_id: Union[Unset, list[int]] = UNSET,
    circuit_id_n: Union[Unset, list[int]] = UNSET,
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
    mark_connected: Union[Unset, bool] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    occupied: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    port_speed: Union[Unset, list[int]] = UNSET,
    port_speed_empty: Union[Unset, bool] = UNSET,
    port_speed_gt: Union[Unset, list[int]] = UNSET,
    port_speed_gte: Union[Unset, list[int]] = UNSET,
    port_speed_lt: Union[Unset, list[int]] = UNSET,
    port_speed_lte: Union[Unset, list[int]] = UNSET,
    port_speed_n: Union[Unset, list[int]] = UNSET,
    pp_info: Union[Unset, list[str]] = UNSET,
    pp_info_empty: Union[Unset, bool] = UNSET,
    pp_info_ic: Union[Unset, list[str]] = UNSET,
    pp_info_ie: Union[Unset, list[str]] = UNSET,
    pp_info_iew: Union[Unset, list[str]] = UNSET,
    pp_info_isw: Union[Unset, list[str]] = UNSET,
    pp_info_n: Union[Unset, list[str]] = UNSET,
    pp_info_nic: Union[Unset, list[str]] = UNSET,
    pp_info_nie: Union[Unset, list[str]] = UNSET,
    pp_info_niew: Union[Unset, list[str]] = UNSET,
    pp_info_nisw: Union[Unset, list[str]] = UNSET,
    provider: Union[Unset, list[str]] = UNSET,
    provider_n: Union[Unset, list[str]] = UNSET,
    provider_id: Union[Unset, list[int]] = UNSET,
    provider_id_n: Union[Unset, list[int]] = UNSET,
    provider_network_id: Union[Unset, list[int]] = UNSET,
    provider_network_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
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
    term_side: Union[Unset, CircuitsCircuitTerminationsListTerminationSide] = UNSET,
    termination_id: Union[Unset, list[int]] = UNSET,
    termination_id_empty: Union[Unset, bool] = UNSET,
    termination_id_gt: Union[Unset, list[int]] = UNSET,
    termination_id_gte: Union[Unset, list[int]] = UNSET,
    termination_id_lt: Union[Unset, list[int]] = UNSET,
    termination_id_lte: Union[Unset, list[int]] = UNSET,
    termination_id_n: Union[Unset, list[int]] = UNSET,
    termination_type: Union[Unset, str] = UNSET,
    termination_type_n: Union[Unset, str] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    upstream_speed: Union[Unset, list[int]] = UNSET,
    upstream_speed_empty: Union[Unset, bool] = UNSET,
    upstream_speed_gt: Union[Unset, list[int]] = UNSET,
    upstream_speed_gte: Union[Unset, list[int]] = UNSET,
    upstream_speed_lt: Union[Unset, list[int]] = UNSET,
    upstream_speed_lte: Union[Unset, list[int]] = UNSET,
    upstream_speed_n: Union[Unset, list[int]] = UNSET,
    xconnect_id: Union[Unset, list[str]] = UNSET,
    xconnect_id_empty: Union[Unset, bool] = UNSET,
    xconnect_id_ic: Union[Unset, list[str]] = UNSET,
    xconnect_id_ie: Union[Unset, list[str]] = UNSET,
    xconnect_id_iew: Union[Unset, list[str]] = UNSET,
    xconnect_id_isw: Union[Unset, list[str]] = UNSET,
    xconnect_id_n: Union[Unset, list[str]] = UNSET,
    xconnect_id_nic: Union[Unset, list[str]] = UNSET,
    xconnect_id_nie: Union[Unset, list[str]] = UNSET,
    xconnect_id_niew: Union[Unset, list[str]] = UNSET,
    xconnect_id_nisw: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedCircuitTerminationList]:
    """Get a list of circuit termination objects.

    Args:
        cable_end (Union[Unset, CircuitsCircuitTerminationsListCableEnd]):
        cable_id (Union[Unset, list[Union[None, int]]]):
        cable_id_n (Union[Unset, list[Union[None, int]]]):
        cabled (Union[Unset, bool]):
        circuit_id (Union[Unset, list[int]]):
        circuit_id_n (Union[Unset, list[int]]):
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
        mark_connected (Union[Unset, bool]):
        modified_by_request (Union[Unset, UUID]):
        occupied (Union[Unset, bool]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        port_speed (Union[Unset, list[int]]):
        port_speed_empty (Union[Unset, bool]):
        port_speed_gt (Union[Unset, list[int]]):
        port_speed_gte (Union[Unset, list[int]]):
        port_speed_lt (Union[Unset, list[int]]):
        port_speed_lte (Union[Unset, list[int]]):
        port_speed_n (Union[Unset, list[int]]):
        pp_info (Union[Unset, list[str]]):
        pp_info_empty (Union[Unset, bool]):
        pp_info_ic (Union[Unset, list[str]]):
        pp_info_ie (Union[Unset, list[str]]):
        pp_info_iew (Union[Unset, list[str]]):
        pp_info_isw (Union[Unset, list[str]]):
        pp_info_n (Union[Unset, list[str]]):
        pp_info_nic (Union[Unset, list[str]]):
        pp_info_nie (Union[Unset, list[str]]):
        pp_info_niew (Union[Unset, list[str]]):
        pp_info_nisw (Union[Unset, list[str]]):
        provider (Union[Unset, list[str]]):
        provider_n (Union[Unset, list[str]]):
        provider_id (Union[Unset, list[int]]):
        provider_id_n (Union[Unset, list[int]]):
        provider_network_id (Union[Unset, list[int]]):
        provider_network_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
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
        term_side (Union[Unset, CircuitsCircuitTerminationsListTerminationSide]):
        termination_id (Union[Unset, list[int]]):
        termination_id_empty (Union[Unset, bool]):
        termination_id_gt (Union[Unset, list[int]]):
        termination_id_gte (Union[Unset, list[int]]):
        termination_id_lt (Union[Unset, list[int]]):
        termination_id_lte (Union[Unset, list[int]]):
        termination_id_n (Union[Unset, list[int]]):
        termination_type (Union[Unset, str]):
        termination_type_n (Union[Unset, str]):
        updated_by_request (Union[Unset, UUID]):
        upstream_speed (Union[Unset, list[int]]):
        upstream_speed_empty (Union[Unset, bool]):
        upstream_speed_gt (Union[Unset, list[int]]):
        upstream_speed_gte (Union[Unset, list[int]]):
        upstream_speed_lt (Union[Unset, list[int]]):
        upstream_speed_lte (Union[Unset, list[int]]):
        upstream_speed_n (Union[Unset, list[int]]):
        xconnect_id (Union[Unset, list[str]]):
        xconnect_id_empty (Union[Unset, bool]):
        xconnect_id_ic (Union[Unset, list[str]]):
        xconnect_id_ie (Union[Unset, list[str]]):
        xconnect_id_iew (Union[Unset, list[str]]):
        xconnect_id_isw (Union[Unset, list[str]]):
        xconnect_id_n (Union[Unset, list[str]]):
        xconnect_id_nic (Union[Unset, list[str]]):
        xconnect_id_nie (Union[Unset, list[str]]):
        xconnect_id_niew (Union[Unset, list[str]]):
        xconnect_id_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCircuitTerminationList]
    """

    kwargs = _get_kwargs(
        cable_end=cable_end,
        cable_id=cable_id,
        cable_id_n=cable_id_n,
        cabled=cabled,
        circuit_id=circuit_id,
        circuit_id_n=circuit_id_n,
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
        mark_connected=mark_connected,
        modified_by_request=modified_by_request,
        occupied=occupied,
        offset=offset,
        ordering=ordering,
        port_speed=port_speed,
        port_speed_empty=port_speed_empty,
        port_speed_gt=port_speed_gt,
        port_speed_gte=port_speed_gte,
        port_speed_lt=port_speed_lt,
        port_speed_lte=port_speed_lte,
        port_speed_n=port_speed_n,
        pp_info=pp_info,
        pp_info_empty=pp_info_empty,
        pp_info_ic=pp_info_ic,
        pp_info_ie=pp_info_ie,
        pp_info_iew=pp_info_iew,
        pp_info_isw=pp_info_isw,
        pp_info_n=pp_info_n,
        pp_info_nic=pp_info_nic,
        pp_info_nie=pp_info_nie,
        pp_info_niew=pp_info_niew,
        pp_info_nisw=pp_info_nisw,
        provider=provider,
        provider_n=provider_n,
        provider_id=provider_id,
        provider_id_n=provider_id_n,
        provider_network_id=provider_network_id,
        provider_network_id_n=provider_network_id_n,
        q=q,
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
        term_side=term_side,
        termination_id=termination_id,
        termination_id_empty=termination_id_empty,
        termination_id_gt=termination_id_gt,
        termination_id_gte=termination_id_gte,
        termination_id_lt=termination_id_lt,
        termination_id_lte=termination_id_lte,
        termination_id_n=termination_id_n,
        termination_type=termination_type,
        termination_type_n=termination_type_n,
        updated_by_request=updated_by_request,
        upstream_speed=upstream_speed,
        upstream_speed_empty=upstream_speed_empty,
        upstream_speed_gt=upstream_speed_gt,
        upstream_speed_gte=upstream_speed_gte,
        upstream_speed_lt=upstream_speed_lt,
        upstream_speed_lte=upstream_speed_lte,
        upstream_speed_n=upstream_speed_n,
        xconnect_id=xconnect_id,
        xconnect_id_empty=xconnect_id_empty,
        xconnect_id_ic=xconnect_id_ic,
        xconnect_id_ie=xconnect_id_ie,
        xconnect_id_iew=xconnect_id_iew,
        xconnect_id_isw=xconnect_id_isw,
        xconnect_id_n=xconnect_id_n,
        xconnect_id_nic=xconnect_id_nic,
        xconnect_id_nie=xconnect_id_nie,
        xconnect_id_niew=xconnect_id_niew,
        xconnect_id_nisw=xconnect_id_nisw,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cable_end: Union[Unset, CircuitsCircuitTerminationsListCableEnd] = UNSET,
    cable_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cable_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cabled: Union[Unset, bool] = UNSET,
    circuit_id: Union[Unset, list[int]] = UNSET,
    circuit_id_n: Union[Unset, list[int]] = UNSET,
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
    mark_connected: Union[Unset, bool] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    occupied: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    port_speed: Union[Unset, list[int]] = UNSET,
    port_speed_empty: Union[Unset, bool] = UNSET,
    port_speed_gt: Union[Unset, list[int]] = UNSET,
    port_speed_gte: Union[Unset, list[int]] = UNSET,
    port_speed_lt: Union[Unset, list[int]] = UNSET,
    port_speed_lte: Union[Unset, list[int]] = UNSET,
    port_speed_n: Union[Unset, list[int]] = UNSET,
    pp_info: Union[Unset, list[str]] = UNSET,
    pp_info_empty: Union[Unset, bool] = UNSET,
    pp_info_ic: Union[Unset, list[str]] = UNSET,
    pp_info_ie: Union[Unset, list[str]] = UNSET,
    pp_info_iew: Union[Unset, list[str]] = UNSET,
    pp_info_isw: Union[Unset, list[str]] = UNSET,
    pp_info_n: Union[Unset, list[str]] = UNSET,
    pp_info_nic: Union[Unset, list[str]] = UNSET,
    pp_info_nie: Union[Unset, list[str]] = UNSET,
    pp_info_niew: Union[Unset, list[str]] = UNSET,
    pp_info_nisw: Union[Unset, list[str]] = UNSET,
    provider: Union[Unset, list[str]] = UNSET,
    provider_n: Union[Unset, list[str]] = UNSET,
    provider_id: Union[Unset, list[int]] = UNSET,
    provider_id_n: Union[Unset, list[int]] = UNSET,
    provider_network_id: Union[Unset, list[int]] = UNSET,
    provider_network_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
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
    term_side: Union[Unset, CircuitsCircuitTerminationsListTerminationSide] = UNSET,
    termination_id: Union[Unset, list[int]] = UNSET,
    termination_id_empty: Union[Unset, bool] = UNSET,
    termination_id_gt: Union[Unset, list[int]] = UNSET,
    termination_id_gte: Union[Unset, list[int]] = UNSET,
    termination_id_lt: Union[Unset, list[int]] = UNSET,
    termination_id_lte: Union[Unset, list[int]] = UNSET,
    termination_id_n: Union[Unset, list[int]] = UNSET,
    termination_type: Union[Unset, str] = UNSET,
    termination_type_n: Union[Unset, str] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    upstream_speed: Union[Unset, list[int]] = UNSET,
    upstream_speed_empty: Union[Unset, bool] = UNSET,
    upstream_speed_gt: Union[Unset, list[int]] = UNSET,
    upstream_speed_gte: Union[Unset, list[int]] = UNSET,
    upstream_speed_lt: Union[Unset, list[int]] = UNSET,
    upstream_speed_lte: Union[Unset, list[int]] = UNSET,
    upstream_speed_n: Union[Unset, list[int]] = UNSET,
    xconnect_id: Union[Unset, list[str]] = UNSET,
    xconnect_id_empty: Union[Unset, bool] = UNSET,
    xconnect_id_ic: Union[Unset, list[str]] = UNSET,
    xconnect_id_ie: Union[Unset, list[str]] = UNSET,
    xconnect_id_iew: Union[Unset, list[str]] = UNSET,
    xconnect_id_isw: Union[Unset, list[str]] = UNSET,
    xconnect_id_n: Union[Unset, list[str]] = UNSET,
    xconnect_id_nic: Union[Unset, list[str]] = UNSET,
    xconnect_id_nie: Union[Unset, list[str]] = UNSET,
    xconnect_id_niew: Union[Unset, list[str]] = UNSET,
    xconnect_id_nisw: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedCircuitTerminationList]:
    """Get a list of circuit termination objects.

    Args:
        cable_end (Union[Unset, CircuitsCircuitTerminationsListCableEnd]):
        cable_id (Union[Unset, list[Union[None, int]]]):
        cable_id_n (Union[Unset, list[Union[None, int]]]):
        cabled (Union[Unset, bool]):
        circuit_id (Union[Unset, list[int]]):
        circuit_id_n (Union[Unset, list[int]]):
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
        mark_connected (Union[Unset, bool]):
        modified_by_request (Union[Unset, UUID]):
        occupied (Union[Unset, bool]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        port_speed (Union[Unset, list[int]]):
        port_speed_empty (Union[Unset, bool]):
        port_speed_gt (Union[Unset, list[int]]):
        port_speed_gte (Union[Unset, list[int]]):
        port_speed_lt (Union[Unset, list[int]]):
        port_speed_lte (Union[Unset, list[int]]):
        port_speed_n (Union[Unset, list[int]]):
        pp_info (Union[Unset, list[str]]):
        pp_info_empty (Union[Unset, bool]):
        pp_info_ic (Union[Unset, list[str]]):
        pp_info_ie (Union[Unset, list[str]]):
        pp_info_iew (Union[Unset, list[str]]):
        pp_info_isw (Union[Unset, list[str]]):
        pp_info_n (Union[Unset, list[str]]):
        pp_info_nic (Union[Unset, list[str]]):
        pp_info_nie (Union[Unset, list[str]]):
        pp_info_niew (Union[Unset, list[str]]):
        pp_info_nisw (Union[Unset, list[str]]):
        provider (Union[Unset, list[str]]):
        provider_n (Union[Unset, list[str]]):
        provider_id (Union[Unset, list[int]]):
        provider_id_n (Union[Unset, list[int]]):
        provider_network_id (Union[Unset, list[int]]):
        provider_network_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
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
        term_side (Union[Unset, CircuitsCircuitTerminationsListTerminationSide]):
        termination_id (Union[Unset, list[int]]):
        termination_id_empty (Union[Unset, bool]):
        termination_id_gt (Union[Unset, list[int]]):
        termination_id_gte (Union[Unset, list[int]]):
        termination_id_lt (Union[Unset, list[int]]):
        termination_id_lte (Union[Unset, list[int]]):
        termination_id_n (Union[Unset, list[int]]):
        termination_type (Union[Unset, str]):
        termination_type_n (Union[Unset, str]):
        updated_by_request (Union[Unset, UUID]):
        upstream_speed (Union[Unset, list[int]]):
        upstream_speed_empty (Union[Unset, bool]):
        upstream_speed_gt (Union[Unset, list[int]]):
        upstream_speed_gte (Union[Unset, list[int]]):
        upstream_speed_lt (Union[Unset, list[int]]):
        upstream_speed_lte (Union[Unset, list[int]]):
        upstream_speed_n (Union[Unset, list[int]]):
        xconnect_id (Union[Unset, list[str]]):
        xconnect_id_empty (Union[Unset, bool]):
        xconnect_id_ic (Union[Unset, list[str]]):
        xconnect_id_ie (Union[Unset, list[str]]):
        xconnect_id_iew (Union[Unset, list[str]]):
        xconnect_id_isw (Union[Unset, list[str]]):
        xconnect_id_n (Union[Unset, list[str]]):
        xconnect_id_nic (Union[Unset, list[str]]):
        xconnect_id_nie (Union[Unset, list[str]]):
        xconnect_id_niew (Union[Unset, list[str]]):
        xconnect_id_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCircuitTerminationList
    """

    return sync_detailed(
        client=client,
        cable_end=cable_end,
        cable_id=cable_id,
        cable_id_n=cable_id_n,
        cabled=cabled,
        circuit_id=circuit_id,
        circuit_id_n=circuit_id_n,
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
        mark_connected=mark_connected,
        modified_by_request=modified_by_request,
        occupied=occupied,
        offset=offset,
        ordering=ordering,
        port_speed=port_speed,
        port_speed_empty=port_speed_empty,
        port_speed_gt=port_speed_gt,
        port_speed_gte=port_speed_gte,
        port_speed_lt=port_speed_lt,
        port_speed_lte=port_speed_lte,
        port_speed_n=port_speed_n,
        pp_info=pp_info,
        pp_info_empty=pp_info_empty,
        pp_info_ic=pp_info_ic,
        pp_info_ie=pp_info_ie,
        pp_info_iew=pp_info_iew,
        pp_info_isw=pp_info_isw,
        pp_info_n=pp_info_n,
        pp_info_nic=pp_info_nic,
        pp_info_nie=pp_info_nie,
        pp_info_niew=pp_info_niew,
        pp_info_nisw=pp_info_nisw,
        provider=provider,
        provider_n=provider_n,
        provider_id=provider_id,
        provider_id_n=provider_id_n,
        provider_network_id=provider_network_id,
        provider_network_id_n=provider_network_id_n,
        q=q,
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
        term_side=term_side,
        termination_id=termination_id,
        termination_id_empty=termination_id_empty,
        termination_id_gt=termination_id_gt,
        termination_id_gte=termination_id_gte,
        termination_id_lt=termination_id_lt,
        termination_id_lte=termination_id_lte,
        termination_id_n=termination_id_n,
        termination_type=termination_type,
        termination_type_n=termination_type_n,
        updated_by_request=updated_by_request,
        upstream_speed=upstream_speed,
        upstream_speed_empty=upstream_speed_empty,
        upstream_speed_gt=upstream_speed_gt,
        upstream_speed_gte=upstream_speed_gte,
        upstream_speed_lt=upstream_speed_lt,
        upstream_speed_lte=upstream_speed_lte,
        upstream_speed_n=upstream_speed_n,
        xconnect_id=xconnect_id,
        xconnect_id_empty=xconnect_id_empty,
        xconnect_id_ic=xconnect_id_ic,
        xconnect_id_ie=xconnect_id_ie,
        xconnect_id_iew=xconnect_id_iew,
        xconnect_id_isw=xconnect_id_isw,
        xconnect_id_n=xconnect_id_n,
        xconnect_id_nic=xconnect_id_nic,
        xconnect_id_nie=xconnect_id_nie,
        xconnect_id_niew=xconnect_id_niew,
        xconnect_id_nisw=xconnect_id_nisw,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cable_end: Union[Unset, CircuitsCircuitTerminationsListCableEnd] = UNSET,
    cable_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cable_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cabled: Union[Unset, bool] = UNSET,
    circuit_id: Union[Unset, list[int]] = UNSET,
    circuit_id_n: Union[Unset, list[int]] = UNSET,
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
    mark_connected: Union[Unset, bool] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    occupied: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    port_speed: Union[Unset, list[int]] = UNSET,
    port_speed_empty: Union[Unset, bool] = UNSET,
    port_speed_gt: Union[Unset, list[int]] = UNSET,
    port_speed_gte: Union[Unset, list[int]] = UNSET,
    port_speed_lt: Union[Unset, list[int]] = UNSET,
    port_speed_lte: Union[Unset, list[int]] = UNSET,
    port_speed_n: Union[Unset, list[int]] = UNSET,
    pp_info: Union[Unset, list[str]] = UNSET,
    pp_info_empty: Union[Unset, bool] = UNSET,
    pp_info_ic: Union[Unset, list[str]] = UNSET,
    pp_info_ie: Union[Unset, list[str]] = UNSET,
    pp_info_iew: Union[Unset, list[str]] = UNSET,
    pp_info_isw: Union[Unset, list[str]] = UNSET,
    pp_info_n: Union[Unset, list[str]] = UNSET,
    pp_info_nic: Union[Unset, list[str]] = UNSET,
    pp_info_nie: Union[Unset, list[str]] = UNSET,
    pp_info_niew: Union[Unset, list[str]] = UNSET,
    pp_info_nisw: Union[Unset, list[str]] = UNSET,
    provider: Union[Unset, list[str]] = UNSET,
    provider_n: Union[Unset, list[str]] = UNSET,
    provider_id: Union[Unset, list[int]] = UNSET,
    provider_id_n: Union[Unset, list[int]] = UNSET,
    provider_network_id: Union[Unset, list[int]] = UNSET,
    provider_network_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
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
    term_side: Union[Unset, CircuitsCircuitTerminationsListTerminationSide] = UNSET,
    termination_id: Union[Unset, list[int]] = UNSET,
    termination_id_empty: Union[Unset, bool] = UNSET,
    termination_id_gt: Union[Unset, list[int]] = UNSET,
    termination_id_gte: Union[Unset, list[int]] = UNSET,
    termination_id_lt: Union[Unset, list[int]] = UNSET,
    termination_id_lte: Union[Unset, list[int]] = UNSET,
    termination_id_n: Union[Unset, list[int]] = UNSET,
    termination_type: Union[Unset, str] = UNSET,
    termination_type_n: Union[Unset, str] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    upstream_speed: Union[Unset, list[int]] = UNSET,
    upstream_speed_empty: Union[Unset, bool] = UNSET,
    upstream_speed_gt: Union[Unset, list[int]] = UNSET,
    upstream_speed_gte: Union[Unset, list[int]] = UNSET,
    upstream_speed_lt: Union[Unset, list[int]] = UNSET,
    upstream_speed_lte: Union[Unset, list[int]] = UNSET,
    upstream_speed_n: Union[Unset, list[int]] = UNSET,
    xconnect_id: Union[Unset, list[str]] = UNSET,
    xconnect_id_empty: Union[Unset, bool] = UNSET,
    xconnect_id_ic: Union[Unset, list[str]] = UNSET,
    xconnect_id_ie: Union[Unset, list[str]] = UNSET,
    xconnect_id_iew: Union[Unset, list[str]] = UNSET,
    xconnect_id_isw: Union[Unset, list[str]] = UNSET,
    xconnect_id_n: Union[Unset, list[str]] = UNSET,
    xconnect_id_nic: Union[Unset, list[str]] = UNSET,
    xconnect_id_nie: Union[Unset, list[str]] = UNSET,
    xconnect_id_niew: Union[Unset, list[str]] = UNSET,
    xconnect_id_nisw: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedCircuitTerminationList]:
    """Get a list of circuit termination objects.

    Args:
        cable_end (Union[Unset, CircuitsCircuitTerminationsListCableEnd]):
        cable_id (Union[Unset, list[Union[None, int]]]):
        cable_id_n (Union[Unset, list[Union[None, int]]]):
        cabled (Union[Unset, bool]):
        circuit_id (Union[Unset, list[int]]):
        circuit_id_n (Union[Unset, list[int]]):
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
        mark_connected (Union[Unset, bool]):
        modified_by_request (Union[Unset, UUID]):
        occupied (Union[Unset, bool]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        port_speed (Union[Unset, list[int]]):
        port_speed_empty (Union[Unset, bool]):
        port_speed_gt (Union[Unset, list[int]]):
        port_speed_gte (Union[Unset, list[int]]):
        port_speed_lt (Union[Unset, list[int]]):
        port_speed_lte (Union[Unset, list[int]]):
        port_speed_n (Union[Unset, list[int]]):
        pp_info (Union[Unset, list[str]]):
        pp_info_empty (Union[Unset, bool]):
        pp_info_ic (Union[Unset, list[str]]):
        pp_info_ie (Union[Unset, list[str]]):
        pp_info_iew (Union[Unset, list[str]]):
        pp_info_isw (Union[Unset, list[str]]):
        pp_info_n (Union[Unset, list[str]]):
        pp_info_nic (Union[Unset, list[str]]):
        pp_info_nie (Union[Unset, list[str]]):
        pp_info_niew (Union[Unset, list[str]]):
        pp_info_nisw (Union[Unset, list[str]]):
        provider (Union[Unset, list[str]]):
        provider_n (Union[Unset, list[str]]):
        provider_id (Union[Unset, list[int]]):
        provider_id_n (Union[Unset, list[int]]):
        provider_network_id (Union[Unset, list[int]]):
        provider_network_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
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
        term_side (Union[Unset, CircuitsCircuitTerminationsListTerminationSide]):
        termination_id (Union[Unset, list[int]]):
        termination_id_empty (Union[Unset, bool]):
        termination_id_gt (Union[Unset, list[int]]):
        termination_id_gte (Union[Unset, list[int]]):
        termination_id_lt (Union[Unset, list[int]]):
        termination_id_lte (Union[Unset, list[int]]):
        termination_id_n (Union[Unset, list[int]]):
        termination_type (Union[Unset, str]):
        termination_type_n (Union[Unset, str]):
        updated_by_request (Union[Unset, UUID]):
        upstream_speed (Union[Unset, list[int]]):
        upstream_speed_empty (Union[Unset, bool]):
        upstream_speed_gt (Union[Unset, list[int]]):
        upstream_speed_gte (Union[Unset, list[int]]):
        upstream_speed_lt (Union[Unset, list[int]]):
        upstream_speed_lte (Union[Unset, list[int]]):
        upstream_speed_n (Union[Unset, list[int]]):
        xconnect_id (Union[Unset, list[str]]):
        xconnect_id_empty (Union[Unset, bool]):
        xconnect_id_ic (Union[Unset, list[str]]):
        xconnect_id_ie (Union[Unset, list[str]]):
        xconnect_id_iew (Union[Unset, list[str]]):
        xconnect_id_isw (Union[Unset, list[str]]):
        xconnect_id_n (Union[Unset, list[str]]):
        xconnect_id_nic (Union[Unset, list[str]]):
        xconnect_id_nie (Union[Unset, list[str]]):
        xconnect_id_niew (Union[Unset, list[str]]):
        xconnect_id_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCircuitTerminationList]
    """

    kwargs = _get_kwargs(
        cable_end=cable_end,
        cable_id=cable_id,
        cable_id_n=cable_id_n,
        cabled=cabled,
        circuit_id=circuit_id,
        circuit_id_n=circuit_id_n,
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
        mark_connected=mark_connected,
        modified_by_request=modified_by_request,
        occupied=occupied,
        offset=offset,
        ordering=ordering,
        port_speed=port_speed,
        port_speed_empty=port_speed_empty,
        port_speed_gt=port_speed_gt,
        port_speed_gte=port_speed_gte,
        port_speed_lt=port_speed_lt,
        port_speed_lte=port_speed_lte,
        port_speed_n=port_speed_n,
        pp_info=pp_info,
        pp_info_empty=pp_info_empty,
        pp_info_ic=pp_info_ic,
        pp_info_ie=pp_info_ie,
        pp_info_iew=pp_info_iew,
        pp_info_isw=pp_info_isw,
        pp_info_n=pp_info_n,
        pp_info_nic=pp_info_nic,
        pp_info_nie=pp_info_nie,
        pp_info_niew=pp_info_niew,
        pp_info_nisw=pp_info_nisw,
        provider=provider,
        provider_n=provider_n,
        provider_id=provider_id,
        provider_id_n=provider_id_n,
        provider_network_id=provider_network_id,
        provider_network_id_n=provider_network_id_n,
        q=q,
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
        term_side=term_side,
        termination_id=termination_id,
        termination_id_empty=termination_id_empty,
        termination_id_gt=termination_id_gt,
        termination_id_gte=termination_id_gte,
        termination_id_lt=termination_id_lt,
        termination_id_lte=termination_id_lte,
        termination_id_n=termination_id_n,
        termination_type=termination_type,
        termination_type_n=termination_type_n,
        updated_by_request=updated_by_request,
        upstream_speed=upstream_speed,
        upstream_speed_empty=upstream_speed_empty,
        upstream_speed_gt=upstream_speed_gt,
        upstream_speed_gte=upstream_speed_gte,
        upstream_speed_lt=upstream_speed_lt,
        upstream_speed_lte=upstream_speed_lte,
        upstream_speed_n=upstream_speed_n,
        xconnect_id=xconnect_id,
        xconnect_id_empty=xconnect_id_empty,
        xconnect_id_ic=xconnect_id_ic,
        xconnect_id_ie=xconnect_id_ie,
        xconnect_id_iew=xconnect_id_iew,
        xconnect_id_isw=xconnect_id_isw,
        xconnect_id_n=xconnect_id_n,
        xconnect_id_nic=xconnect_id_nic,
        xconnect_id_nie=xconnect_id_nie,
        xconnect_id_niew=xconnect_id_niew,
        xconnect_id_nisw=xconnect_id_nisw,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cable_end: Union[Unset, CircuitsCircuitTerminationsListCableEnd] = UNSET,
    cable_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cable_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cabled: Union[Unset, bool] = UNSET,
    circuit_id: Union[Unset, list[int]] = UNSET,
    circuit_id_n: Union[Unset, list[int]] = UNSET,
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
    mark_connected: Union[Unset, bool] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    occupied: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    port_speed: Union[Unset, list[int]] = UNSET,
    port_speed_empty: Union[Unset, bool] = UNSET,
    port_speed_gt: Union[Unset, list[int]] = UNSET,
    port_speed_gte: Union[Unset, list[int]] = UNSET,
    port_speed_lt: Union[Unset, list[int]] = UNSET,
    port_speed_lte: Union[Unset, list[int]] = UNSET,
    port_speed_n: Union[Unset, list[int]] = UNSET,
    pp_info: Union[Unset, list[str]] = UNSET,
    pp_info_empty: Union[Unset, bool] = UNSET,
    pp_info_ic: Union[Unset, list[str]] = UNSET,
    pp_info_ie: Union[Unset, list[str]] = UNSET,
    pp_info_iew: Union[Unset, list[str]] = UNSET,
    pp_info_isw: Union[Unset, list[str]] = UNSET,
    pp_info_n: Union[Unset, list[str]] = UNSET,
    pp_info_nic: Union[Unset, list[str]] = UNSET,
    pp_info_nie: Union[Unset, list[str]] = UNSET,
    pp_info_niew: Union[Unset, list[str]] = UNSET,
    pp_info_nisw: Union[Unset, list[str]] = UNSET,
    provider: Union[Unset, list[str]] = UNSET,
    provider_n: Union[Unset, list[str]] = UNSET,
    provider_id: Union[Unset, list[int]] = UNSET,
    provider_id_n: Union[Unset, list[int]] = UNSET,
    provider_network_id: Union[Unset, list[int]] = UNSET,
    provider_network_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
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
    term_side: Union[Unset, CircuitsCircuitTerminationsListTerminationSide] = UNSET,
    termination_id: Union[Unset, list[int]] = UNSET,
    termination_id_empty: Union[Unset, bool] = UNSET,
    termination_id_gt: Union[Unset, list[int]] = UNSET,
    termination_id_gte: Union[Unset, list[int]] = UNSET,
    termination_id_lt: Union[Unset, list[int]] = UNSET,
    termination_id_lte: Union[Unset, list[int]] = UNSET,
    termination_id_n: Union[Unset, list[int]] = UNSET,
    termination_type: Union[Unset, str] = UNSET,
    termination_type_n: Union[Unset, str] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    upstream_speed: Union[Unset, list[int]] = UNSET,
    upstream_speed_empty: Union[Unset, bool] = UNSET,
    upstream_speed_gt: Union[Unset, list[int]] = UNSET,
    upstream_speed_gte: Union[Unset, list[int]] = UNSET,
    upstream_speed_lt: Union[Unset, list[int]] = UNSET,
    upstream_speed_lte: Union[Unset, list[int]] = UNSET,
    upstream_speed_n: Union[Unset, list[int]] = UNSET,
    xconnect_id: Union[Unset, list[str]] = UNSET,
    xconnect_id_empty: Union[Unset, bool] = UNSET,
    xconnect_id_ic: Union[Unset, list[str]] = UNSET,
    xconnect_id_ie: Union[Unset, list[str]] = UNSET,
    xconnect_id_iew: Union[Unset, list[str]] = UNSET,
    xconnect_id_isw: Union[Unset, list[str]] = UNSET,
    xconnect_id_n: Union[Unset, list[str]] = UNSET,
    xconnect_id_nic: Union[Unset, list[str]] = UNSET,
    xconnect_id_nie: Union[Unset, list[str]] = UNSET,
    xconnect_id_niew: Union[Unset, list[str]] = UNSET,
    xconnect_id_nisw: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedCircuitTerminationList]:
    """Get a list of circuit termination objects.

    Args:
        cable_end (Union[Unset, CircuitsCircuitTerminationsListCableEnd]):
        cable_id (Union[Unset, list[Union[None, int]]]):
        cable_id_n (Union[Unset, list[Union[None, int]]]):
        cabled (Union[Unset, bool]):
        circuit_id (Union[Unset, list[int]]):
        circuit_id_n (Union[Unset, list[int]]):
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
        mark_connected (Union[Unset, bool]):
        modified_by_request (Union[Unset, UUID]):
        occupied (Union[Unset, bool]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        port_speed (Union[Unset, list[int]]):
        port_speed_empty (Union[Unset, bool]):
        port_speed_gt (Union[Unset, list[int]]):
        port_speed_gte (Union[Unset, list[int]]):
        port_speed_lt (Union[Unset, list[int]]):
        port_speed_lte (Union[Unset, list[int]]):
        port_speed_n (Union[Unset, list[int]]):
        pp_info (Union[Unset, list[str]]):
        pp_info_empty (Union[Unset, bool]):
        pp_info_ic (Union[Unset, list[str]]):
        pp_info_ie (Union[Unset, list[str]]):
        pp_info_iew (Union[Unset, list[str]]):
        pp_info_isw (Union[Unset, list[str]]):
        pp_info_n (Union[Unset, list[str]]):
        pp_info_nic (Union[Unset, list[str]]):
        pp_info_nie (Union[Unset, list[str]]):
        pp_info_niew (Union[Unset, list[str]]):
        pp_info_nisw (Union[Unset, list[str]]):
        provider (Union[Unset, list[str]]):
        provider_n (Union[Unset, list[str]]):
        provider_id (Union[Unset, list[int]]):
        provider_id_n (Union[Unset, list[int]]):
        provider_network_id (Union[Unset, list[int]]):
        provider_network_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
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
        term_side (Union[Unset, CircuitsCircuitTerminationsListTerminationSide]):
        termination_id (Union[Unset, list[int]]):
        termination_id_empty (Union[Unset, bool]):
        termination_id_gt (Union[Unset, list[int]]):
        termination_id_gte (Union[Unset, list[int]]):
        termination_id_lt (Union[Unset, list[int]]):
        termination_id_lte (Union[Unset, list[int]]):
        termination_id_n (Union[Unset, list[int]]):
        termination_type (Union[Unset, str]):
        termination_type_n (Union[Unset, str]):
        updated_by_request (Union[Unset, UUID]):
        upstream_speed (Union[Unset, list[int]]):
        upstream_speed_empty (Union[Unset, bool]):
        upstream_speed_gt (Union[Unset, list[int]]):
        upstream_speed_gte (Union[Unset, list[int]]):
        upstream_speed_lt (Union[Unset, list[int]]):
        upstream_speed_lte (Union[Unset, list[int]]):
        upstream_speed_n (Union[Unset, list[int]]):
        xconnect_id (Union[Unset, list[str]]):
        xconnect_id_empty (Union[Unset, bool]):
        xconnect_id_ic (Union[Unset, list[str]]):
        xconnect_id_ie (Union[Unset, list[str]]):
        xconnect_id_iew (Union[Unset, list[str]]):
        xconnect_id_isw (Union[Unset, list[str]]):
        xconnect_id_n (Union[Unset, list[str]]):
        xconnect_id_nic (Union[Unset, list[str]]):
        xconnect_id_nie (Union[Unset, list[str]]):
        xconnect_id_niew (Union[Unset, list[str]]):
        xconnect_id_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCircuitTerminationList
    """

    return (
        await asyncio_detailed(
            client=client,
            cable_end=cable_end,
            cable_id=cable_id,
            cable_id_n=cable_id_n,
            cabled=cabled,
            circuit_id=circuit_id,
            circuit_id_n=circuit_id_n,
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
            mark_connected=mark_connected,
            modified_by_request=modified_by_request,
            occupied=occupied,
            offset=offset,
            ordering=ordering,
            port_speed=port_speed,
            port_speed_empty=port_speed_empty,
            port_speed_gt=port_speed_gt,
            port_speed_gte=port_speed_gte,
            port_speed_lt=port_speed_lt,
            port_speed_lte=port_speed_lte,
            port_speed_n=port_speed_n,
            pp_info=pp_info,
            pp_info_empty=pp_info_empty,
            pp_info_ic=pp_info_ic,
            pp_info_ie=pp_info_ie,
            pp_info_iew=pp_info_iew,
            pp_info_isw=pp_info_isw,
            pp_info_n=pp_info_n,
            pp_info_nic=pp_info_nic,
            pp_info_nie=pp_info_nie,
            pp_info_niew=pp_info_niew,
            pp_info_nisw=pp_info_nisw,
            provider=provider,
            provider_n=provider_n,
            provider_id=provider_id,
            provider_id_n=provider_id_n,
            provider_network_id=provider_network_id,
            provider_network_id_n=provider_network_id_n,
            q=q,
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
            term_side=term_side,
            termination_id=termination_id,
            termination_id_empty=termination_id_empty,
            termination_id_gt=termination_id_gt,
            termination_id_gte=termination_id_gte,
            termination_id_lt=termination_id_lt,
            termination_id_lte=termination_id_lte,
            termination_id_n=termination_id_n,
            termination_type=termination_type,
            termination_type_n=termination_type_n,
            updated_by_request=updated_by_request,
            upstream_speed=upstream_speed,
            upstream_speed_empty=upstream_speed_empty,
            upstream_speed_gt=upstream_speed_gt,
            upstream_speed_gte=upstream_speed_gte,
            upstream_speed_lt=upstream_speed_lt,
            upstream_speed_lte=upstream_speed_lte,
            upstream_speed_n=upstream_speed_n,
            xconnect_id=xconnect_id,
            xconnect_id_empty=xconnect_id_empty,
            xconnect_id_ic=xconnect_id_ic,
            xconnect_id_ie=xconnect_id_ie,
            xconnect_id_iew=xconnect_id_iew,
            xconnect_id_isw=xconnect_id_isw,
            xconnect_id_n=xconnect_id_n,
            xconnect_id_nic=xconnect_id_nic,
            xconnect_id_nie=xconnect_id_nie,
            xconnect_id_niew=xconnect_id_niew,
            xconnect_id_nisw=xconnect_id_nisw,
        )
    ).parsed
