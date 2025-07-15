import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dcim_cables_list_length_unit import DcimCablesListLengthUnit
from ...models.paginated_cable_list import PaginatedCableList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    circuittermination_id: Union[Unset, list[int]] = UNSET,
    color: Union[Unset, list[str]] = UNSET,
    color_empty: Union[Unset, bool] = UNSET,
    color_ic: Union[Unset, list[str]] = UNSET,
    color_ie: Union[Unset, list[str]] = UNSET,
    color_iew: Union[Unset, list[str]] = UNSET,
    color_isw: Union[Unset, list[str]] = UNSET,
    color_n: Union[Unset, list[str]] = UNSET,
    color_nic: Union[Unset, list[str]] = UNSET,
    color_nie: Union[Unset, list[str]] = UNSET,
    color_niew: Union[Unset, list[str]] = UNSET,
    color_nisw: Union[Unset, list[str]] = UNSET,
    consoleport_id: Union[Unset, list[int]] = UNSET,
    consoleserverport_id: Union[Unset, list[int]] = UNSET,
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
    device: Union[Unset, list[str]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    frontport_id: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_id: Union[Unset, list[int]] = UNSET,
    label: Union[Unset, list[str]] = UNSET,
    label_empty: Union[Unset, bool] = UNSET,
    label_ic: Union[Unset, list[str]] = UNSET,
    label_ie: Union[Unset, list[str]] = UNSET,
    label_iew: Union[Unset, list[str]] = UNSET,
    label_isw: Union[Unset, list[str]] = UNSET,
    label_n: Union[Unset, list[str]] = UNSET,
    label_nic: Union[Unset, list[str]] = UNSET,
    label_nie: Union[Unset, list[str]] = UNSET,
    label_niew: Union[Unset, list[str]] = UNSET,
    label_nisw: Union[Unset, list[str]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    length: Union[Unset, list[float]] = UNSET,
    length_empty: Union[Unset, bool] = UNSET,
    length_gt: Union[Unset, list[float]] = UNSET,
    length_gte: Union[Unset, list[float]] = UNSET,
    length_lt: Union[Unset, list[float]] = UNSET,
    length_lte: Union[Unset, list[float]] = UNSET,
    length_n: Union[Unset, list[float]] = UNSET,
    length_unit: Union[Unset, DcimCablesListLengthUnit] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    powerfeed_id: Union[Unset, list[int]] = UNSET,
    poweroutlet_id: Union[Unset, list[int]] = UNSET,
    powerport_id: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rearport_id: Union[Unset, list[int]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    status: Union[Unset, list[str]] = UNSET,
    status_empty: Union[Unset, bool] = UNSET,
    status_ic: Union[Unset, list[str]] = UNSET,
    status_ie: Union[Unset, list[str]] = UNSET,
    status_iew: Union[Unset, list[str]] = UNSET,
    status_isw: Union[Unset, list[str]] = UNSET,
    status_n: Union[Unset, list[str]] = UNSET,
    status_nic: Union[Unset, list[str]] = UNSET,
    status_nie: Union[Unset, list[str]] = UNSET,
    status_niew: Union[Unset, list[str]] = UNSET,
    status_nisw: Union[Unset, list[str]] = UNSET,
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
    termination_a_id: Union[Unset, list[int]] = UNSET,
    termination_a_type: Union[Unset, str] = UNSET,
    termination_a_type_n: Union[Unset, str] = UNSET,
    termination_b_id: Union[Unset, list[int]] = UNSET,
    termination_b_type: Union[Unset, str] = UNSET,
    termination_b_type_n: Union[Unset, str] = UNSET,
    type_: Union[Unset, list[Union[None, str]]] = UNSET,
    type_empty: Union[Unset, bool] = UNSET,
    type_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    type_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    type_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    type_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    type_n: Union[Unset, list[Union[None, str]]] = UNSET,
    type_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    type_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    type_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    type_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    unterminated: Union[Unset, bool] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_circuittermination_id: Union[Unset, list[int]] = UNSET
    if not isinstance(circuittermination_id, Unset):
        json_circuittermination_id = circuittermination_id

    params["circuittermination_id"] = json_circuittermination_id

    json_color: Union[Unset, list[str]] = UNSET
    if not isinstance(color, Unset):
        json_color = color

    params["color"] = json_color

    params["color__empty"] = color_empty

    json_color_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(color_ic, Unset):
        json_color_ic = color_ic

    params["color__ic"] = json_color_ic

    json_color_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(color_ie, Unset):
        json_color_ie = color_ie

    params["color__ie"] = json_color_ie

    json_color_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(color_iew, Unset):
        json_color_iew = color_iew

    params["color__iew"] = json_color_iew

    json_color_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(color_isw, Unset):
        json_color_isw = color_isw

    params["color__isw"] = json_color_isw

    json_color_n: Union[Unset, list[str]] = UNSET
    if not isinstance(color_n, Unset):
        json_color_n = color_n

    params["color__n"] = json_color_n

    json_color_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(color_nic, Unset):
        json_color_nic = color_nic

    params["color__nic"] = json_color_nic

    json_color_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(color_nie, Unset):
        json_color_nie = color_nie

    params["color__nie"] = json_color_nie

    json_color_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(color_niew, Unset):
        json_color_niew = color_niew

    params["color__niew"] = json_color_niew

    json_color_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(color_nisw, Unset):
        json_color_nisw = color_nisw

    params["color__nisw"] = json_color_nisw

    json_consoleport_id: Union[Unset, list[int]] = UNSET
    if not isinstance(consoleport_id, Unset):
        json_consoleport_id = consoleport_id

    params["consoleport_id"] = json_consoleport_id

    json_consoleserverport_id: Union[Unset, list[int]] = UNSET
    if not isinstance(consoleserverport_id, Unset):
        json_consoleserverport_id = consoleserverport_id

    params["consoleserverport_id"] = json_consoleserverport_id

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

    json_device: Union[Unset, list[str]] = UNSET
    if not isinstance(device, Unset):
        json_device = device

    params["device"] = json_device

    json_device_id: Union[Unset, list[int]] = UNSET
    if not isinstance(device_id, Unset):
        json_device_id = device_id

    params["device_id"] = json_device_id

    json_frontport_id: Union[Unset, list[int]] = UNSET
    if not isinstance(frontport_id, Unset):
        json_frontport_id = frontport_id

    params["frontport_id"] = json_frontport_id

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

    json_label: Union[Unset, list[str]] = UNSET
    if not isinstance(label, Unset):
        json_label = label

    params["label"] = json_label

    params["label__empty"] = label_empty

    json_label_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(label_ic, Unset):
        json_label_ic = label_ic

    params["label__ic"] = json_label_ic

    json_label_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(label_ie, Unset):
        json_label_ie = label_ie

    params["label__ie"] = json_label_ie

    json_label_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(label_iew, Unset):
        json_label_iew = label_iew

    params["label__iew"] = json_label_iew

    json_label_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(label_isw, Unset):
        json_label_isw = label_isw

    params["label__isw"] = json_label_isw

    json_label_n: Union[Unset, list[str]] = UNSET
    if not isinstance(label_n, Unset):
        json_label_n = label_n

    params["label__n"] = json_label_n

    json_label_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(label_nic, Unset):
        json_label_nic = label_nic

    params["label__nic"] = json_label_nic

    json_label_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(label_nie, Unset):
        json_label_nie = label_nie

    params["label__nie"] = json_label_nie

    json_label_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(label_niew, Unset):
        json_label_niew = label_niew

    params["label__niew"] = json_label_niew

    json_label_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(label_nisw, Unset):
        json_label_nisw = label_nisw

    params["label__nisw"] = json_label_nisw

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

    json_length: Union[Unset, list[float]] = UNSET
    if not isinstance(length, Unset):
        json_length = length

    params["length"] = json_length

    params["length__empty"] = length_empty

    json_length_gt: Union[Unset, list[float]] = UNSET
    if not isinstance(length_gt, Unset):
        json_length_gt = length_gt

    params["length__gt"] = json_length_gt

    json_length_gte: Union[Unset, list[float]] = UNSET
    if not isinstance(length_gte, Unset):
        json_length_gte = length_gte

    params["length__gte"] = json_length_gte

    json_length_lt: Union[Unset, list[float]] = UNSET
    if not isinstance(length_lt, Unset):
        json_length_lt = length_lt

    params["length__lt"] = json_length_lt

    json_length_lte: Union[Unset, list[float]] = UNSET
    if not isinstance(length_lte, Unset):
        json_length_lte = length_lte

    params["length__lte"] = json_length_lte

    json_length_n: Union[Unset, list[float]] = UNSET
    if not isinstance(length_n, Unset):
        json_length_n = length_n

    params["length__n"] = json_length_n

    json_length_unit: Union[Unset, str] = UNSET
    if not isinstance(length_unit, Unset):
        json_length_unit = length_unit.value

    params["length_unit"] = json_length_unit

    params["limit"] = limit

    json_location: Union[Unset, list[str]] = UNSET
    if not isinstance(location, Unset):
        json_location = location

    params["location"] = json_location

    json_location_id: Union[Unset, list[int]] = UNSET
    if not isinstance(location_id, Unset):
        json_location_id = location_id

    params["location_id"] = json_location_id

    json_modified_by_request: Union[Unset, str] = UNSET
    if not isinstance(modified_by_request, Unset):
        json_modified_by_request = str(modified_by_request)
    params["modified_by_request"] = json_modified_by_request

    params["offset"] = offset

    params["ordering"] = ordering

    json_powerfeed_id: Union[Unset, list[int]] = UNSET
    if not isinstance(powerfeed_id, Unset):
        json_powerfeed_id = powerfeed_id

    params["powerfeed_id"] = json_powerfeed_id

    json_poweroutlet_id: Union[Unset, list[int]] = UNSET
    if not isinstance(poweroutlet_id, Unset):
        json_poweroutlet_id = poweroutlet_id

    params["poweroutlet_id"] = json_poweroutlet_id

    json_powerport_id: Union[Unset, list[int]] = UNSET
    if not isinstance(powerport_id, Unset):
        json_powerport_id = powerport_id

    params["powerport_id"] = json_powerport_id

    params["q"] = q

    json_rack: Union[Unset, list[str]] = UNSET
    if not isinstance(rack, Unset):
        json_rack = rack

    params["rack"] = json_rack

    json_rack_id: Union[Unset, list[int]] = UNSET
    if not isinstance(rack_id, Unset):
        json_rack_id = rack_id

    params["rack_id"] = json_rack_id

    json_rearport_id: Union[Unset, list[int]] = UNSET
    if not isinstance(rearport_id, Unset):
        json_rearport_id = rearport_id

    params["rearport_id"] = json_rearport_id

    json_site: Union[Unset, list[str]] = UNSET
    if not isinstance(site, Unset):
        json_site = site

    params["site"] = json_site

    json_site_id: Union[Unset, list[int]] = UNSET
    if not isinstance(site_id, Unset):
        json_site_id = site_id

    params["site_id"] = json_site_id

    json_status: Union[Unset, list[str]] = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    params["status__empty"] = status_empty

    json_status_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(status_ic, Unset):
        json_status_ic = status_ic

    params["status__ic"] = json_status_ic

    json_status_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(status_ie, Unset):
        json_status_ie = status_ie

    params["status__ie"] = json_status_ie

    json_status_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(status_iew, Unset):
        json_status_iew = status_iew

    params["status__iew"] = json_status_iew

    json_status_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(status_isw, Unset):
        json_status_isw = status_isw

    params["status__isw"] = json_status_isw

    json_status_n: Union[Unset, list[str]] = UNSET
    if not isinstance(status_n, Unset):
        json_status_n = status_n

    params["status__n"] = json_status_n

    json_status_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(status_nic, Unset):
        json_status_nic = status_nic

    params["status__nic"] = json_status_nic

    json_status_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(status_nie, Unset):
        json_status_nie = status_nie

    params["status__nie"] = json_status_nie

    json_status_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(status_niew, Unset):
        json_status_niew = status_niew

    params["status__niew"] = json_status_niew

    json_status_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(status_nisw, Unset):
        json_status_nisw = status_nisw

    params["status__nisw"] = json_status_nisw

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

    json_termination_a_id: Union[Unset, list[int]] = UNSET
    if not isinstance(termination_a_id, Unset):
        json_termination_a_id = termination_a_id

    params["termination_a_id"] = json_termination_a_id

    params["termination_a_type"] = termination_a_type

    params["termination_a_type__n"] = termination_a_type_n

    json_termination_b_id: Union[Unset, list[int]] = UNSET
    if not isinstance(termination_b_id, Unset):
        json_termination_b_id = termination_b_id

    params["termination_b_id"] = json_termination_b_id

    params["termination_b_type"] = termination_b_type

    params["termination_b_type__n"] = termination_b_type_n

    json_type_: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = []
        for type_item_data in type_:
            type_item: Union[None, str]
            type_item = type_item_data
            json_type_.append(type_item)

    params["type"] = json_type_

    params["type__empty"] = type_empty

    json_type_ic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(type_ic, Unset):
        json_type_ic = []
        for type_ic_item_data in type_ic:
            type_ic_item: Union[None, str]
            type_ic_item = type_ic_item_data
            json_type_ic.append(type_ic_item)

    params["type__ic"] = json_type_ic

    json_type_ie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(type_ie, Unset):
        json_type_ie = []
        for type_ie_item_data in type_ie:
            type_ie_item: Union[None, str]
            type_ie_item = type_ie_item_data
            json_type_ie.append(type_ie_item)

    params["type__ie"] = json_type_ie

    json_type_iew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(type_iew, Unset):
        json_type_iew = []
        for type_iew_item_data in type_iew:
            type_iew_item: Union[None, str]
            type_iew_item = type_iew_item_data
            json_type_iew.append(type_iew_item)

    params["type__iew"] = json_type_iew

    json_type_isw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(type_isw, Unset):
        json_type_isw = []
        for type_isw_item_data in type_isw:
            type_isw_item: Union[None, str]
            type_isw_item = type_isw_item_data
            json_type_isw.append(type_isw_item)

    params["type__isw"] = json_type_isw

    json_type_n: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(type_n, Unset):
        json_type_n = []
        for type_n_item_data in type_n:
            type_n_item: Union[None, str]
            type_n_item = type_n_item_data
            json_type_n.append(type_n_item)

    params["type__n"] = json_type_n

    json_type_nic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(type_nic, Unset):
        json_type_nic = []
        for type_nic_item_data in type_nic:
            type_nic_item: Union[None, str]
            type_nic_item = type_nic_item_data
            json_type_nic.append(type_nic_item)

    params["type__nic"] = json_type_nic

    json_type_nie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(type_nie, Unset):
        json_type_nie = []
        for type_nie_item_data in type_nie:
            type_nie_item: Union[None, str]
            type_nie_item = type_nie_item_data
            json_type_nie.append(type_nie_item)

    params["type__nie"] = json_type_nie

    json_type_niew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(type_niew, Unset):
        json_type_niew = []
        for type_niew_item_data in type_niew:
            type_niew_item: Union[None, str]
            type_niew_item = type_niew_item_data
            json_type_niew.append(type_niew_item)

    params["type__niew"] = json_type_niew

    json_type_nisw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(type_nisw, Unset):
        json_type_nisw = []
        for type_nisw_item_data in type_nisw:
            type_nisw_item: Union[None, str]
            type_nisw_item = type_nisw_item_data
            json_type_nisw.append(type_nisw_item)

    params["type__nisw"] = json_type_nisw

    params["unterminated"] = unterminated

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/dcim/cables/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedCableList]:
    if response.status_code == 200:
        response_200 = PaginatedCableList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedCableList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    circuittermination_id: Union[Unset, list[int]] = UNSET,
    color: Union[Unset, list[str]] = UNSET,
    color_empty: Union[Unset, bool] = UNSET,
    color_ic: Union[Unset, list[str]] = UNSET,
    color_ie: Union[Unset, list[str]] = UNSET,
    color_iew: Union[Unset, list[str]] = UNSET,
    color_isw: Union[Unset, list[str]] = UNSET,
    color_n: Union[Unset, list[str]] = UNSET,
    color_nic: Union[Unset, list[str]] = UNSET,
    color_nie: Union[Unset, list[str]] = UNSET,
    color_niew: Union[Unset, list[str]] = UNSET,
    color_nisw: Union[Unset, list[str]] = UNSET,
    consoleport_id: Union[Unset, list[int]] = UNSET,
    consoleserverport_id: Union[Unset, list[int]] = UNSET,
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
    device: Union[Unset, list[str]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    frontport_id: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_id: Union[Unset, list[int]] = UNSET,
    label: Union[Unset, list[str]] = UNSET,
    label_empty: Union[Unset, bool] = UNSET,
    label_ic: Union[Unset, list[str]] = UNSET,
    label_ie: Union[Unset, list[str]] = UNSET,
    label_iew: Union[Unset, list[str]] = UNSET,
    label_isw: Union[Unset, list[str]] = UNSET,
    label_n: Union[Unset, list[str]] = UNSET,
    label_nic: Union[Unset, list[str]] = UNSET,
    label_nie: Union[Unset, list[str]] = UNSET,
    label_niew: Union[Unset, list[str]] = UNSET,
    label_nisw: Union[Unset, list[str]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    length: Union[Unset, list[float]] = UNSET,
    length_empty: Union[Unset, bool] = UNSET,
    length_gt: Union[Unset, list[float]] = UNSET,
    length_gte: Union[Unset, list[float]] = UNSET,
    length_lt: Union[Unset, list[float]] = UNSET,
    length_lte: Union[Unset, list[float]] = UNSET,
    length_n: Union[Unset, list[float]] = UNSET,
    length_unit: Union[Unset, DcimCablesListLengthUnit] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    powerfeed_id: Union[Unset, list[int]] = UNSET,
    poweroutlet_id: Union[Unset, list[int]] = UNSET,
    powerport_id: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rearport_id: Union[Unset, list[int]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    status: Union[Unset, list[str]] = UNSET,
    status_empty: Union[Unset, bool] = UNSET,
    status_ic: Union[Unset, list[str]] = UNSET,
    status_ie: Union[Unset, list[str]] = UNSET,
    status_iew: Union[Unset, list[str]] = UNSET,
    status_isw: Union[Unset, list[str]] = UNSET,
    status_n: Union[Unset, list[str]] = UNSET,
    status_nic: Union[Unset, list[str]] = UNSET,
    status_nie: Union[Unset, list[str]] = UNSET,
    status_niew: Union[Unset, list[str]] = UNSET,
    status_nisw: Union[Unset, list[str]] = UNSET,
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
    termination_a_id: Union[Unset, list[int]] = UNSET,
    termination_a_type: Union[Unset, str] = UNSET,
    termination_a_type_n: Union[Unset, str] = UNSET,
    termination_b_id: Union[Unset, list[int]] = UNSET,
    termination_b_type: Union[Unset, str] = UNSET,
    termination_b_type_n: Union[Unset, str] = UNSET,
    type_: Union[Unset, list[Union[None, str]]] = UNSET,
    type_empty: Union[Unset, bool] = UNSET,
    type_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    type_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    type_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    type_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    type_n: Union[Unset, list[Union[None, str]]] = UNSET,
    type_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    type_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    type_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    type_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    unterminated: Union[Unset, bool] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedCableList]:
    """Get a list of cable objects.

    Args:
        circuittermination_id (Union[Unset, list[int]]):
        color (Union[Unset, list[str]]):
        color_empty (Union[Unset, bool]):
        color_ic (Union[Unset, list[str]]):
        color_ie (Union[Unset, list[str]]):
        color_iew (Union[Unset, list[str]]):
        color_isw (Union[Unset, list[str]]):
        color_n (Union[Unset, list[str]]):
        color_nic (Union[Unset, list[str]]):
        color_nie (Union[Unset, list[str]]):
        color_niew (Union[Unset, list[str]]):
        color_nisw (Union[Unset, list[str]]):
        consoleport_id (Union[Unset, list[int]]):
        consoleserverport_id (Union[Unset, list[int]]):
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
        device (Union[Unset, list[str]]):
        device_id (Union[Unset, list[int]]):
        frontport_id (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_id (Union[Unset, list[int]]):
        label (Union[Unset, list[str]]):
        label_empty (Union[Unset, bool]):
        label_ic (Union[Unset, list[str]]):
        label_ie (Union[Unset, list[str]]):
        label_iew (Union[Unset, list[str]]):
        label_isw (Union[Unset, list[str]]):
        label_n (Union[Unset, list[str]]):
        label_nic (Union[Unset, list[str]]):
        label_nie (Union[Unset, list[str]]):
        label_niew (Union[Unset, list[str]]):
        label_nisw (Union[Unset, list[str]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        length (Union[Unset, list[float]]):
        length_empty (Union[Unset, bool]):
        length_gt (Union[Unset, list[float]]):
        length_gte (Union[Unset, list[float]]):
        length_lt (Union[Unset, list[float]]):
        length_lte (Union[Unset, list[float]]):
        length_n (Union[Unset, list[float]]):
        length_unit (Union[Unset, DcimCablesListLengthUnit]):
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_id (Union[Unset, list[int]]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        powerfeed_id (Union[Unset, list[int]]):
        poweroutlet_id (Union[Unset, list[int]]):
        powerport_id (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_id (Union[Unset, list[int]]):
        rearport_id (Union[Unset, list[int]]):
        site (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        status (Union[Unset, list[str]]):
        status_empty (Union[Unset, bool]):
        status_ic (Union[Unset, list[str]]):
        status_ie (Union[Unset, list[str]]):
        status_iew (Union[Unset, list[str]]):
        status_isw (Union[Unset, list[str]]):
        status_n (Union[Unset, list[str]]):
        status_nic (Union[Unset, list[str]]):
        status_nie (Union[Unset, list[str]]):
        status_niew (Union[Unset, list[str]]):
        status_nisw (Union[Unset, list[str]]):
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
        termination_a_id (Union[Unset, list[int]]):
        termination_a_type (Union[Unset, str]):
        termination_a_type_n (Union[Unset, str]):
        termination_b_id (Union[Unset, list[int]]):
        termination_b_type (Union[Unset, str]):
        termination_b_type_n (Union[Unset, str]):
        type_ (Union[Unset, list[Union[None, str]]]):
        type_empty (Union[Unset, bool]):
        type_ic (Union[Unset, list[Union[None, str]]]):
        type_ie (Union[Unset, list[Union[None, str]]]):
        type_iew (Union[Unset, list[Union[None, str]]]):
        type_isw (Union[Unset, list[Union[None, str]]]):
        type_n (Union[Unset, list[Union[None, str]]]):
        type_nic (Union[Unset, list[Union[None, str]]]):
        type_nie (Union[Unset, list[Union[None, str]]]):
        type_niew (Union[Unset, list[Union[None, str]]]):
        type_nisw (Union[Unset, list[Union[None, str]]]):
        unterminated (Union[Unset, bool]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCableList]
    """

    kwargs = _get_kwargs(
        circuittermination_id=circuittermination_id,
        color=color,
        color_empty=color_empty,
        color_ic=color_ic,
        color_ie=color_ie,
        color_iew=color_iew,
        color_isw=color_isw,
        color_n=color_n,
        color_nic=color_nic,
        color_nie=color_nie,
        color_niew=color_niew,
        color_nisw=color_nisw,
        consoleport_id=consoleport_id,
        consoleserverport_id=consoleserverport_id,
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
        device=device,
        device_id=device_id,
        frontport_id=frontport_id,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface_id=interface_id,
        label=label,
        label_empty=label_empty,
        label_ic=label_ic,
        label_ie=label_ie,
        label_iew=label_iew,
        label_isw=label_isw,
        label_n=label_n,
        label_nic=label_nic,
        label_nie=label_nie,
        label_niew=label_niew,
        label_nisw=label_nisw,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        length=length,
        length_empty=length_empty,
        length_gt=length_gt,
        length_gte=length_gte,
        length_lt=length_lt,
        length_lte=length_lte,
        length_n=length_n,
        length_unit=length_unit,
        limit=limit,
        location=location,
        location_id=location_id,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        powerfeed_id=powerfeed_id,
        poweroutlet_id=poweroutlet_id,
        powerport_id=powerport_id,
        q=q,
        rack=rack,
        rack_id=rack_id,
        rearport_id=rearport_id,
        site=site,
        site_id=site_id,
        status=status,
        status_empty=status_empty,
        status_ic=status_ic,
        status_ie=status_ie,
        status_iew=status_iew,
        status_isw=status_isw,
        status_n=status_n,
        status_nic=status_nic,
        status_nie=status_nie,
        status_niew=status_niew,
        status_nisw=status_nisw,
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
        termination_a_id=termination_a_id,
        termination_a_type=termination_a_type,
        termination_a_type_n=termination_a_type_n,
        termination_b_id=termination_b_id,
        termination_b_type=termination_b_type,
        termination_b_type_n=termination_b_type_n,
        type_=type_,
        type_empty=type_empty,
        type_ic=type_ic,
        type_ie=type_ie,
        type_iew=type_iew,
        type_isw=type_isw,
        type_n=type_n,
        type_nic=type_nic,
        type_nie=type_nie,
        type_niew=type_niew,
        type_nisw=type_nisw,
        unterminated=unterminated,
        updated_by_request=updated_by_request,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    circuittermination_id: Union[Unset, list[int]] = UNSET,
    color: Union[Unset, list[str]] = UNSET,
    color_empty: Union[Unset, bool] = UNSET,
    color_ic: Union[Unset, list[str]] = UNSET,
    color_ie: Union[Unset, list[str]] = UNSET,
    color_iew: Union[Unset, list[str]] = UNSET,
    color_isw: Union[Unset, list[str]] = UNSET,
    color_n: Union[Unset, list[str]] = UNSET,
    color_nic: Union[Unset, list[str]] = UNSET,
    color_nie: Union[Unset, list[str]] = UNSET,
    color_niew: Union[Unset, list[str]] = UNSET,
    color_nisw: Union[Unset, list[str]] = UNSET,
    consoleport_id: Union[Unset, list[int]] = UNSET,
    consoleserverport_id: Union[Unset, list[int]] = UNSET,
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
    device: Union[Unset, list[str]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    frontport_id: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_id: Union[Unset, list[int]] = UNSET,
    label: Union[Unset, list[str]] = UNSET,
    label_empty: Union[Unset, bool] = UNSET,
    label_ic: Union[Unset, list[str]] = UNSET,
    label_ie: Union[Unset, list[str]] = UNSET,
    label_iew: Union[Unset, list[str]] = UNSET,
    label_isw: Union[Unset, list[str]] = UNSET,
    label_n: Union[Unset, list[str]] = UNSET,
    label_nic: Union[Unset, list[str]] = UNSET,
    label_nie: Union[Unset, list[str]] = UNSET,
    label_niew: Union[Unset, list[str]] = UNSET,
    label_nisw: Union[Unset, list[str]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    length: Union[Unset, list[float]] = UNSET,
    length_empty: Union[Unset, bool] = UNSET,
    length_gt: Union[Unset, list[float]] = UNSET,
    length_gte: Union[Unset, list[float]] = UNSET,
    length_lt: Union[Unset, list[float]] = UNSET,
    length_lte: Union[Unset, list[float]] = UNSET,
    length_n: Union[Unset, list[float]] = UNSET,
    length_unit: Union[Unset, DcimCablesListLengthUnit] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    powerfeed_id: Union[Unset, list[int]] = UNSET,
    poweroutlet_id: Union[Unset, list[int]] = UNSET,
    powerport_id: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rearport_id: Union[Unset, list[int]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    status: Union[Unset, list[str]] = UNSET,
    status_empty: Union[Unset, bool] = UNSET,
    status_ic: Union[Unset, list[str]] = UNSET,
    status_ie: Union[Unset, list[str]] = UNSET,
    status_iew: Union[Unset, list[str]] = UNSET,
    status_isw: Union[Unset, list[str]] = UNSET,
    status_n: Union[Unset, list[str]] = UNSET,
    status_nic: Union[Unset, list[str]] = UNSET,
    status_nie: Union[Unset, list[str]] = UNSET,
    status_niew: Union[Unset, list[str]] = UNSET,
    status_nisw: Union[Unset, list[str]] = UNSET,
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
    termination_a_id: Union[Unset, list[int]] = UNSET,
    termination_a_type: Union[Unset, str] = UNSET,
    termination_a_type_n: Union[Unset, str] = UNSET,
    termination_b_id: Union[Unset, list[int]] = UNSET,
    termination_b_type: Union[Unset, str] = UNSET,
    termination_b_type_n: Union[Unset, str] = UNSET,
    type_: Union[Unset, list[Union[None, str]]] = UNSET,
    type_empty: Union[Unset, bool] = UNSET,
    type_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    type_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    type_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    type_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    type_n: Union[Unset, list[Union[None, str]]] = UNSET,
    type_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    type_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    type_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    type_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    unterminated: Union[Unset, bool] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedCableList]:
    """Get a list of cable objects.

    Args:
        circuittermination_id (Union[Unset, list[int]]):
        color (Union[Unset, list[str]]):
        color_empty (Union[Unset, bool]):
        color_ic (Union[Unset, list[str]]):
        color_ie (Union[Unset, list[str]]):
        color_iew (Union[Unset, list[str]]):
        color_isw (Union[Unset, list[str]]):
        color_n (Union[Unset, list[str]]):
        color_nic (Union[Unset, list[str]]):
        color_nie (Union[Unset, list[str]]):
        color_niew (Union[Unset, list[str]]):
        color_nisw (Union[Unset, list[str]]):
        consoleport_id (Union[Unset, list[int]]):
        consoleserverport_id (Union[Unset, list[int]]):
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
        device (Union[Unset, list[str]]):
        device_id (Union[Unset, list[int]]):
        frontport_id (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_id (Union[Unset, list[int]]):
        label (Union[Unset, list[str]]):
        label_empty (Union[Unset, bool]):
        label_ic (Union[Unset, list[str]]):
        label_ie (Union[Unset, list[str]]):
        label_iew (Union[Unset, list[str]]):
        label_isw (Union[Unset, list[str]]):
        label_n (Union[Unset, list[str]]):
        label_nic (Union[Unset, list[str]]):
        label_nie (Union[Unset, list[str]]):
        label_niew (Union[Unset, list[str]]):
        label_nisw (Union[Unset, list[str]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        length (Union[Unset, list[float]]):
        length_empty (Union[Unset, bool]):
        length_gt (Union[Unset, list[float]]):
        length_gte (Union[Unset, list[float]]):
        length_lt (Union[Unset, list[float]]):
        length_lte (Union[Unset, list[float]]):
        length_n (Union[Unset, list[float]]):
        length_unit (Union[Unset, DcimCablesListLengthUnit]):
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_id (Union[Unset, list[int]]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        powerfeed_id (Union[Unset, list[int]]):
        poweroutlet_id (Union[Unset, list[int]]):
        powerport_id (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_id (Union[Unset, list[int]]):
        rearport_id (Union[Unset, list[int]]):
        site (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        status (Union[Unset, list[str]]):
        status_empty (Union[Unset, bool]):
        status_ic (Union[Unset, list[str]]):
        status_ie (Union[Unset, list[str]]):
        status_iew (Union[Unset, list[str]]):
        status_isw (Union[Unset, list[str]]):
        status_n (Union[Unset, list[str]]):
        status_nic (Union[Unset, list[str]]):
        status_nie (Union[Unset, list[str]]):
        status_niew (Union[Unset, list[str]]):
        status_nisw (Union[Unset, list[str]]):
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
        termination_a_id (Union[Unset, list[int]]):
        termination_a_type (Union[Unset, str]):
        termination_a_type_n (Union[Unset, str]):
        termination_b_id (Union[Unset, list[int]]):
        termination_b_type (Union[Unset, str]):
        termination_b_type_n (Union[Unset, str]):
        type_ (Union[Unset, list[Union[None, str]]]):
        type_empty (Union[Unset, bool]):
        type_ic (Union[Unset, list[Union[None, str]]]):
        type_ie (Union[Unset, list[Union[None, str]]]):
        type_iew (Union[Unset, list[Union[None, str]]]):
        type_isw (Union[Unset, list[Union[None, str]]]):
        type_n (Union[Unset, list[Union[None, str]]]):
        type_nic (Union[Unset, list[Union[None, str]]]):
        type_nie (Union[Unset, list[Union[None, str]]]):
        type_niew (Union[Unset, list[Union[None, str]]]):
        type_nisw (Union[Unset, list[Union[None, str]]]):
        unterminated (Union[Unset, bool]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCableList
    """

    return sync_detailed(
        client=client,
        circuittermination_id=circuittermination_id,
        color=color,
        color_empty=color_empty,
        color_ic=color_ic,
        color_ie=color_ie,
        color_iew=color_iew,
        color_isw=color_isw,
        color_n=color_n,
        color_nic=color_nic,
        color_nie=color_nie,
        color_niew=color_niew,
        color_nisw=color_nisw,
        consoleport_id=consoleport_id,
        consoleserverport_id=consoleserverport_id,
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
        device=device,
        device_id=device_id,
        frontport_id=frontport_id,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface_id=interface_id,
        label=label,
        label_empty=label_empty,
        label_ic=label_ic,
        label_ie=label_ie,
        label_iew=label_iew,
        label_isw=label_isw,
        label_n=label_n,
        label_nic=label_nic,
        label_nie=label_nie,
        label_niew=label_niew,
        label_nisw=label_nisw,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        length=length,
        length_empty=length_empty,
        length_gt=length_gt,
        length_gte=length_gte,
        length_lt=length_lt,
        length_lte=length_lte,
        length_n=length_n,
        length_unit=length_unit,
        limit=limit,
        location=location,
        location_id=location_id,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        powerfeed_id=powerfeed_id,
        poweroutlet_id=poweroutlet_id,
        powerport_id=powerport_id,
        q=q,
        rack=rack,
        rack_id=rack_id,
        rearport_id=rearport_id,
        site=site,
        site_id=site_id,
        status=status,
        status_empty=status_empty,
        status_ic=status_ic,
        status_ie=status_ie,
        status_iew=status_iew,
        status_isw=status_isw,
        status_n=status_n,
        status_nic=status_nic,
        status_nie=status_nie,
        status_niew=status_niew,
        status_nisw=status_nisw,
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
        termination_a_id=termination_a_id,
        termination_a_type=termination_a_type,
        termination_a_type_n=termination_a_type_n,
        termination_b_id=termination_b_id,
        termination_b_type=termination_b_type,
        termination_b_type_n=termination_b_type_n,
        type_=type_,
        type_empty=type_empty,
        type_ic=type_ic,
        type_ie=type_ie,
        type_iew=type_iew,
        type_isw=type_isw,
        type_n=type_n,
        type_nic=type_nic,
        type_nie=type_nie,
        type_niew=type_niew,
        type_nisw=type_nisw,
        unterminated=unterminated,
        updated_by_request=updated_by_request,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    circuittermination_id: Union[Unset, list[int]] = UNSET,
    color: Union[Unset, list[str]] = UNSET,
    color_empty: Union[Unset, bool] = UNSET,
    color_ic: Union[Unset, list[str]] = UNSET,
    color_ie: Union[Unset, list[str]] = UNSET,
    color_iew: Union[Unset, list[str]] = UNSET,
    color_isw: Union[Unset, list[str]] = UNSET,
    color_n: Union[Unset, list[str]] = UNSET,
    color_nic: Union[Unset, list[str]] = UNSET,
    color_nie: Union[Unset, list[str]] = UNSET,
    color_niew: Union[Unset, list[str]] = UNSET,
    color_nisw: Union[Unset, list[str]] = UNSET,
    consoleport_id: Union[Unset, list[int]] = UNSET,
    consoleserverport_id: Union[Unset, list[int]] = UNSET,
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
    device: Union[Unset, list[str]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    frontport_id: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_id: Union[Unset, list[int]] = UNSET,
    label: Union[Unset, list[str]] = UNSET,
    label_empty: Union[Unset, bool] = UNSET,
    label_ic: Union[Unset, list[str]] = UNSET,
    label_ie: Union[Unset, list[str]] = UNSET,
    label_iew: Union[Unset, list[str]] = UNSET,
    label_isw: Union[Unset, list[str]] = UNSET,
    label_n: Union[Unset, list[str]] = UNSET,
    label_nic: Union[Unset, list[str]] = UNSET,
    label_nie: Union[Unset, list[str]] = UNSET,
    label_niew: Union[Unset, list[str]] = UNSET,
    label_nisw: Union[Unset, list[str]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    length: Union[Unset, list[float]] = UNSET,
    length_empty: Union[Unset, bool] = UNSET,
    length_gt: Union[Unset, list[float]] = UNSET,
    length_gte: Union[Unset, list[float]] = UNSET,
    length_lt: Union[Unset, list[float]] = UNSET,
    length_lte: Union[Unset, list[float]] = UNSET,
    length_n: Union[Unset, list[float]] = UNSET,
    length_unit: Union[Unset, DcimCablesListLengthUnit] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    powerfeed_id: Union[Unset, list[int]] = UNSET,
    poweroutlet_id: Union[Unset, list[int]] = UNSET,
    powerport_id: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rearport_id: Union[Unset, list[int]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    status: Union[Unset, list[str]] = UNSET,
    status_empty: Union[Unset, bool] = UNSET,
    status_ic: Union[Unset, list[str]] = UNSET,
    status_ie: Union[Unset, list[str]] = UNSET,
    status_iew: Union[Unset, list[str]] = UNSET,
    status_isw: Union[Unset, list[str]] = UNSET,
    status_n: Union[Unset, list[str]] = UNSET,
    status_nic: Union[Unset, list[str]] = UNSET,
    status_nie: Union[Unset, list[str]] = UNSET,
    status_niew: Union[Unset, list[str]] = UNSET,
    status_nisw: Union[Unset, list[str]] = UNSET,
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
    termination_a_id: Union[Unset, list[int]] = UNSET,
    termination_a_type: Union[Unset, str] = UNSET,
    termination_a_type_n: Union[Unset, str] = UNSET,
    termination_b_id: Union[Unset, list[int]] = UNSET,
    termination_b_type: Union[Unset, str] = UNSET,
    termination_b_type_n: Union[Unset, str] = UNSET,
    type_: Union[Unset, list[Union[None, str]]] = UNSET,
    type_empty: Union[Unset, bool] = UNSET,
    type_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    type_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    type_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    type_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    type_n: Union[Unset, list[Union[None, str]]] = UNSET,
    type_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    type_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    type_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    type_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    unterminated: Union[Unset, bool] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedCableList]:
    """Get a list of cable objects.

    Args:
        circuittermination_id (Union[Unset, list[int]]):
        color (Union[Unset, list[str]]):
        color_empty (Union[Unset, bool]):
        color_ic (Union[Unset, list[str]]):
        color_ie (Union[Unset, list[str]]):
        color_iew (Union[Unset, list[str]]):
        color_isw (Union[Unset, list[str]]):
        color_n (Union[Unset, list[str]]):
        color_nic (Union[Unset, list[str]]):
        color_nie (Union[Unset, list[str]]):
        color_niew (Union[Unset, list[str]]):
        color_nisw (Union[Unset, list[str]]):
        consoleport_id (Union[Unset, list[int]]):
        consoleserverport_id (Union[Unset, list[int]]):
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
        device (Union[Unset, list[str]]):
        device_id (Union[Unset, list[int]]):
        frontport_id (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_id (Union[Unset, list[int]]):
        label (Union[Unset, list[str]]):
        label_empty (Union[Unset, bool]):
        label_ic (Union[Unset, list[str]]):
        label_ie (Union[Unset, list[str]]):
        label_iew (Union[Unset, list[str]]):
        label_isw (Union[Unset, list[str]]):
        label_n (Union[Unset, list[str]]):
        label_nic (Union[Unset, list[str]]):
        label_nie (Union[Unset, list[str]]):
        label_niew (Union[Unset, list[str]]):
        label_nisw (Union[Unset, list[str]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        length (Union[Unset, list[float]]):
        length_empty (Union[Unset, bool]):
        length_gt (Union[Unset, list[float]]):
        length_gte (Union[Unset, list[float]]):
        length_lt (Union[Unset, list[float]]):
        length_lte (Union[Unset, list[float]]):
        length_n (Union[Unset, list[float]]):
        length_unit (Union[Unset, DcimCablesListLengthUnit]):
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_id (Union[Unset, list[int]]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        powerfeed_id (Union[Unset, list[int]]):
        poweroutlet_id (Union[Unset, list[int]]):
        powerport_id (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_id (Union[Unset, list[int]]):
        rearport_id (Union[Unset, list[int]]):
        site (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        status (Union[Unset, list[str]]):
        status_empty (Union[Unset, bool]):
        status_ic (Union[Unset, list[str]]):
        status_ie (Union[Unset, list[str]]):
        status_iew (Union[Unset, list[str]]):
        status_isw (Union[Unset, list[str]]):
        status_n (Union[Unset, list[str]]):
        status_nic (Union[Unset, list[str]]):
        status_nie (Union[Unset, list[str]]):
        status_niew (Union[Unset, list[str]]):
        status_nisw (Union[Unset, list[str]]):
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
        termination_a_id (Union[Unset, list[int]]):
        termination_a_type (Union[Unset, str]):
        termination_a_type_n (Union[Unset, str]):
        termination_b_id (Union[Unset, list[int]]):
        termination_b_type (Union[Unset, str]):
        termination_b_type_n (Union[Unset, str]):
        type_ (Union[Unset, list[Union[None, str]]]):
        type_empty (Union[Unset, bool]):
        type_ic (Union[Unset, list[Union[None, str]]]):
        type_ie (Union[Unset, list[Union[None, str]]]):
        type_iew (Union[Unset, list[Union[None, str]]]):
        type_isw (Union[Unset, list[Union[None, str]]]):
        type_n (Union[Unset, list[Union[None, str]]]):
        type_nic (Union[Unset, list[Union[None, str]]]):
        type_nie (Union[Unset, list[Union[None, str]]]):
        type_niew (Union[Unset, list[Union[None, str]]]):
        type_nisw (Union[Unset, list[Union[None, str]]]):
        unterminated (Union[Unset, bool]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCableList]
    """

    kwargs = _get_kwargs(
        circuittermination_id=circuittermination_id,
        color=color,
        color_empty=color_empty,
        color_ic=color_ic,
        color_ie=color_ie,
        color_iew=color_iew,
        color_isw=color_isw,
        color_n=color_n,
        color_nic=color_nic,
        color_nie=color_nie,
        color_niew=color_niew,
        color_nisw=color_nisw,
        consoleport_id=consoleport_id,
        consoleserverport_id=consoleserverport_id,
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
        device=device,
        device_id=device_id,
        frontport_id=frontport_id,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface_id=interface_id,
        label=label,
        label_empty=label_empty,
        label_ic=label_ic,
        label_ie=label_ie,
        label_iew=label_iew,
        label_isw=label_isw,
        label_n=label_n,
        label_nic=label_nic,
        label_nie=label_nie,
        label_niew=label_niew,
        label_nisw=label_nisw,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        length=length,
        length_empty=length_empty,
        length_gt=length_gt,
        length_gte=length_gte,
        length_lt=length_lt,
        length_lte=length_lte,
        length_n=length_n,
        length_unit=length_unit,
        limit=limit,
        location=location,
        location_id=location_id,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        powerfeed_id=powerfeed_id,
        poweroutlet_id=poweroutlet_id,
        powerport_id=powerport_id,
        q=q,
        rack=rack,
        rack_id=rack_id,
        rearport_id=rearport_id,
        site=site,
        site_id=site_id,
        status=status,
        status_empty=status_empty,
        status_ic=status_ic,
        status_ie=status_ie,
        status_iew=status_iew,
        status_isw=status_isw,
        status_n=status_n,
        status_nic=status_nic,
        status_nie=status_nie,
        status_niew=status_niew,
        status_nisw=status_nisw,
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
        termination_a_id=termination_a_id,
        termination_a_type=termination_a_type,
        termination_a_type_n=termination_a_type_n,
        termination_b_id=termination_b_id,
        termination_b_type=termination_b_type,
        termination_b_type_n=termination_b_type_n,
        type_=type_,
        type_empty=type_empty,
        type_ic=type_ic,
        type_ie=type_ie,
        type_iew=type_iew,
        type_isw=type_isw,
        type_n=type_n,
        type_nic=type_nic,
        type_nie=type_nie,
        type_niew=type_niew,
        type_nisw=type_nisw,
        unterminated=unterminated,
        updated_by_request=updated_by_request,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    circuittermination_id: Union[Unset, list[int]] = UNSET,
    color: Union[Unset, list[str]] = UNSET,
    color_empty: Union[Unset, bool] = UNSET,
    color_ic: Union[Unset, list[str]] = UNSET,
    color_ie: Union[Unset, list[str]] = UNSET,
    color_iew: Union[Unset, list[str]] = UNSET,
    color_isw: Union[Unset, list[str]] = UNSET,
    color_n: Union[Unset, list[str]] = UNSET,
    color_nic: Union[Unset, list[str]] = UNSET,
    color_nie: Union[Unset, list[str]] = UNSET,
    color_niew: Union[Unset, list[str]] = UNSET,
    color_nisw: Union[Unset, list[str]] = UNSET,
    consoleport_id: Union[Unset, list[int]] = UNSET,
    consoleserverport_id: Union[Unset, list[int]] = UNSET,
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
    device: Union[Unset, list[str]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    frontport_id: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_id: Union[Unset, list[int]] = UNSET,
    label: Union[Unset, list[str]] = UNSET,
    label_empty: Union[Unset, bool] = UNSET,
    label_ic: Union[Unset, list[str]] = UNSET,
    label_ie: Union[Unset, list[str]] = UNSET,
    label_iew: Union[Unset, list[str]] = UNSET,
    label_isw: Union[Unset, list[str]] = UNSET,
    label_n: Union[Unset, list[str]] = UNSET,
    label_nic: Union[Unset, list[str]] = UNSET,
    label_nie: Union[Unset, list[str]] = UNSET,
    label_niew: Union[Unset, list[str]] = UNSET,
    label_nisw: Union[Unset, list[str]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    length: Union[Unset, list[float]] = UNSET,
    length_empty: Union[Unset, bool] = UNSET,
    length_gt: Union[Unset, list[float]] = UNSET,
    length_gte: Union[Unset, list[float]] = UNSET,
    length_lt: Union[Unset, list[float]] = UNSET,
    length_lte: Union[Unset, list[float]] = UNSET,
    length_n: Union[Unset, list[float]] = UNSET,
    length_unit: Union[Unset, DcimCablesListLengthUnit] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    powerfeed_id: Union[Unset, list[int]] = UNSET,
    poweroutlet_id: Union[Unset, list[int]] = UNSET,
    powerport_id: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rearport_id: Union[Unset, list[int]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    status: Union[Unset, list[str]] = UNSET,
    status_empty: Union[Unset, bool] = UNSET,
    status_ic: Union[Unset, list[str]] = UNSET,
    status_ie: Union[Unset, list[str]] = UNSET,
    status_iew: Union[Unset, list[str]] = UNSET,
    status_isw: Union[Unset, list[str]] = UNSET,
    status_n: Union[Unset, list[str]] = UNSET,
    status_nic: Union[Unset, list[str]] = UNSET,
    status_nie: Union[Unset, list[str]] = UNSET,
    status_niew: Union[Unset, list[str]] = UNSET,
    status_nisw: Union[Unset, list[str]] = UNSET,
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
    termination_a_id: Union[Unset, list[int]] = UNSET,
    termination_a_type: Union[Unset, str] = UNSET,
    termination_a_type_n: Union[Unset, str] = UNSET,
    termination_b_id: Union[Unset, list[int]] = UNSET,
    termination_b_type: Union[Unset, str] = UNSET,
    termination_b_type_n: Union[Unset, str] = UNSET,
    type_: Union[Unset, list[Union[None, str]]] = UNSET,
    type_empty: Union[Unset, bool] = UNSET,
    type_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    type_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    type_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    type_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    type_n: Union[Unset, list[Union[None, str]]] = UNSET,
    type_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    type_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    type_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    type_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    unterminated: Union[Unset, bool] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedCableList]:
    """Get a list of cable objects.

    Args:
        circuittermination_id (Union[Unset, list[int]]):
        color (Union[Unset, list[str]]):
        color_empty (Union[Unset, bool]):
        color_ic (Union[Unset, list[str]]):
        color_ie (Union[Unset, list[str]]):
        color_iew (Union[Unset, list[str]]):
        color_isw (Union[Unset, list[str]]):
        color_n (Union[Unset, list[str]]):
        color_nic (Union[Unset, list[str]]):
        color_nie (Union[Unset, list[str]]):
        color_niew (Union[Unset, list[str]]):
        color_nisw (Union[Unset, list[str]]):
        consoleport_id (Union[Unset, list[int]]):
        consoleserverport_id (Union[Unset, list[int]]):
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
        device (Union[Unset, list[str]]):
        device_id (Union[Unset, list[int]]):
        frontport_id (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_id (Union[Unset, list[int]]):
        label (Union[Unset, list[str]]):
        label_empty (Union[Unset, bool]):
        label_ic (Union[Unset, list[str]]):
        label_ie (Union[Unset, list[str]]):
        label_iew (Union[Unset, list[str]]):
        label_isw (Union[Unset, list[str]]):
        label_n (Union[Unset, list[str]]):
        label_nic (Union[Unset, list[str]]):
        label_nie (Union[Unset, list[str]]):
        label_niew (Union[Unset, list[str]]):
        label_nisw (Union[Unset, list[str]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        length (Union[Unset, list[float]]):
        length_empty (Union[Unset, bool]):
        length_gt (Union[Unset, list[float]]):
        length_gte (Union[Unset, list[float]]):
        length_lt (Union[Unset, list[float]]):
        length_lte (Union[Unset, list[float]]):
        length_n (Union[Unset, list[float]]):
        length_unit (Union[Unset, DcimCablesListLengthUnit]):
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_id (Union[Unset, list[int]]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        powerfeed_id (Union[Unset, list[int]]):
        poweroutlet_id (Union[Unset, list[int]]):
        powerport_id (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_id (Union[Unset, list[int]]):
        rearport_id (Union[Unset, list[int]]):
        site (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        status (Union[Unset, list[str]]):
        status_empty (Union[Unset, bool]):
        status_ic (Union[Unset, list[str]]):
        status_ie (Union[Unset, list[str]]):
        status_iew (Union[Unset, list[str]]):
        status_isw (Union[Unset, list[str]]):
        status_n (Union[Unset, list[str]]):
        status_nic (Union[Unset, list[str]]):
        status_nie (Union[Unset, list[str]]):
        status_niew (Union[Unset, list[str]]):
        status_nisw (Union[Unset, list[str]]):
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
        termination_a_id (Union[Unset, list[int]]):
        termination_a_type (Union[Unset, str]):
        termination_a_type_n (Union[Unset, str]):
        termination_b_id (Union[Unset, list[int]]):
        termination_b_type (Union[Unset, str]):
        termination_b_type_n (Union[Unset, str]):
        type_ (Union[Unset, list[Union[None, str]]]):
        type_empty (Union[Unset, bool]):
        type_ic (Union[Unset, list[Union[None, str]]]):
        type_ie (Union[Unset, list[Union[None, str]]]):
        type_iew (Union[Unset, list[Union[None, str]]]):
        type_isw (Union[Unset, list[Union[None, str]]]):
        type_n (Union[Unset, list[Union[None, str]]]):
        type_nic (Union[Unset, list[Union[None, str]]]):
        type_nie (Union[Unset, list[Union[None, str]]]):
        type_niew (Union[Unset, list[Union[None, str]]]):
        type_nisw (Union[Unset, list[Union[None, str]]]):
        unterminated (Union[Unset, bool]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCableList
    """

    return (
        await asyncio_detailed(
            client=client,
            circuittermination_id=circuittermination_id,
            color=color,
            color_empty=color_empty,
            color_ic=color_ic,
            color_ie=color_ie,
            color_iew=color_iew,
            color_isw=color_isw,
            color_n=color_n,
            color_nic=color_nic,
            color_nie=color_nie,
            color_niew=color_niew,
            color_nisw=color_nisw,
            consoleport_id=consoleport_id,
            consoleserverport_id=consoleserverport_id,
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
            device=device,
            device_id=device_id,
            frontport_id=frontport_id,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            interface_id=interface_id,
            label=label,
            label_empty=label_empty,
            label_ic=label_ic,
            label_ie=label_ie,
            label_iew=label_iew,
            label_isw=label_isw,
            label_n=label_n,
            label_nic=label_nic,
            label_nie=label_nie,
            label_niew=label_niew,
            label_nisw=label_nisw,
            last_updated=last_updated,
            last_updated_empty=last_updated_empty,
            last_updated_gt=last_updated_gt,
            last_updated_gte=last_updated_gte,
            last_updated_lt=last_updated_lt,
            last_updated_lte=last_updated_lte,
            last_updated_n=last_updated_n,
            length=length,
            length_empty=length_empty,
            length_gt=length_gt,
            length_gte=length_gte,
            length_lt=length_lt,
            length_lte=length_lte,
            length_n=length_n,
            length_unit=length_unit,
            limit=limit,
            location=location,
            location_id=location_id,
            modified_by_request=modified_by_request,
            offset=offset,
            ordering=ordering,
            powerfeed_id=powerfeed_id,
            poweroutlet_id=poweroutlet_id,
            powerport_id=powerport_id,
            q=q,
            rack=rack,
            rack_id=rack_id,
            rearport_id=rearport_id,
            site=site,
            site_id=site_id,
            status=status,
            status_empty=status_empty,
            status_ic=status_ic,
            status_ie=status_ie,
            status_iew=status_iew,
            status_isw=status_isw,
            status_n=status_n,
            status_nic=status_nic,
            status_nie=status_nie,
            status_niew=status_niew,
            status_nisw=status_nisw,
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
            termination_a_id=termination_a_id,
            termination_a_type=termination_a_type,
            termination_a_type_n=termination_a_type_n,
            termination_b_id=termination_b_id,
            termination_b_type=termination_b_type,
            termination_b_type_n=termination_b_type_n,
            type_=type_,
            type_empty=type_empty,
            type_ic=type_ic,
            type_ie=type_ie,
            type_iew=type_iew,
            type_isw=type_isw,
            type_n=type_n,
            type_nic=type_nic,
            type_nie=type_nie,
            type_niew=type_niew,
            type_nisw=type_nisw,
            unterminated=unterminated,
            updated_by_request=updated_by_request,
        )
    ).parsed
