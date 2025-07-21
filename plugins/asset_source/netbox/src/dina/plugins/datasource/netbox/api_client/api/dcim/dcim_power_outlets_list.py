import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dcim_power_outlets_list_cable_end import DcimPowerOutletsListCableEnd
from ...models.paginated_power_outlet_list import PaginatedPowerOutletList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cable_end: Union[Unset, DcimPowerOutletsListCableEnd] = UNSET,
    cable_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cable_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cabled: Union[Unset, bool] = UNSET,
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
    connected: Union[Unset, bool] = UNSET,
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
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    device_id_n: Union[Unset, list[int]] = UNSET,
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_id: Union[Unset, list[int]] = UNSET,
    device_role_id_n: Union[Unset, list[int]] = UNSET,
    device_status: Union[Unset, list[str]] = UNSET,
    device_status_empty: Union[Unset, bool] = UNSET,
    device_status_ic: Union[Unset, list[str]] = UNSET,
    device_status_ie: Union[Unset, list[str]] = UNSET,
    device_status_iew: Union[Unset, list[str]] = UNSET,
    device_status_isw: Union[Unset, list[str]] = UNSET,
    device_status_n: Union[Unset, list[str]] = UNSET,
    device_status_nic: Union[Unset, list[str]] = UNSET,
    device_status_nie: Union[Unset, list[str]] = UNSET,
    device_status_niew: Union[Unset, list[str]] = UNSET,
    device_status_nisw: Union[Unset, list[str]] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    feed_leg: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_empty: Union[Unset, bool] = UNSET,
    feed_leg_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_n: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
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
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
    mark_connected: Union[Unset, bool] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_id: Union[Unset, list[Union[None, int]]] = UNSET,
    module_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    name: Union[Unset, list[str]] = UNSET,
    name_empty: Union[Unset, bool] = UNSET,
    name_ic: Union[Unset, list[str]] = UNSET,
    name_ie: Union[Unset, list[str]] = UNSET,
    name_iew: Union[Unset, list[str]] = UNSET,
    name_isw: Union[Unset, list[str]] = UNSET,
    name_n: Union[Unset, list[str]] = UNSET,
    name_nic: Union[Unset, list[str]] = UNSET,
    name_nie: Union[Unset, list[str]] = UNSET,
    name_niew: Union[Unset, list[str]] = UNSET,
    name_nisw: Union[Unset, list[str]] = UNSET,
    occupied: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    power_port_id: Union[Unset, list[Union[None, int]]] = UNSET,
    power_port_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_chassis: Union[Unset, list[str]] = UNSET,
    virtual_chassis_n: Union[Unset, list[str]] = UNSET,
    virtual_chassis_id: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id_n: Union[Unset, list[int]] = UNSET,
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

    params["connected"] = connected

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

    json_device: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(device, Unset):
        json_device = []
        for device_item_data in device:
            device_item: Union[None, str]
            device_item = device_item_data
            json_device.append(device_item)

    params["device"] = json_device

    json_device_n: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(device_n, Unset):
        json_device_n = []
        for device_n_item_data in device_n:
            device_n_item: Union[None, str]
            device_n_item = device_n_item_data
            json_device_n.append(device_n_item)

    params["device__n"] = json_device_n

    json_device_id: Union[Unset, list[int]] = UNSET
    if not isinstance(device_id, Unset):
        json_device_id = device_id

    params["device_id"] = json_device_id

    json_device_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(device_id_n, Unset):
        json_device_id_n = device_id_n

    params["device_id__n"] = json_device_id_n

    json_device_role: Union[Unset, list[str]] = UNSET
    if not isinstance(device_role, Unset):
        json_device_role = device_role

    params["device_role"] = json_device_role

    json_device_role_n: Union[Unset, list[str]] = UNSET
    if not isinstance(device_role_n, Unset):
        json_device_role_n = device_role_n

    params["device_role__n"] = json_device_role_n

    json_device_role_id: Union[Unset, list[int]] = UNSET
    if not isinstance(device_role_id, Unset):
        json_device_role_id = device_role_id

    params["device_role_id"] = json_device_role_id

    json_device_role_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(device_role_id_n, Unset):
        json_device_role_id_n = device_role_id_n

    params["device_role_id__n"] = json_device_role_id_n

    json_device_status: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status, Unset):
        json_device_status = device_status

    params["device_status"] = json_device_status

    params["device_status__empty"] = device_status_empty

    json_device_status_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status_ic, Unset):
        json_device_status_ic = device_status_ic

    params["device_status__ic"] = json_device_status_ic

    json_device_status_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status_ie, Unset):
        json_device_status_ie = device_status_ie

    params["device_status__ie"] = json_device_status_ie

    json_device_status_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status_iew, Unset):
        json_device_status_iew = device_status_iew

    params["device_status__iew"] = json_device_status_iew

    json_device_status_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status_isw, Unset):
        json_device_status_isw = device_status_isw

    params["device_status__isw"] = json_device_status_isw

    json_device_status_n: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status_n, Unset):
        json_device_status_n = device_status_n

    params["device_status__n"] = json_device_status_n

    json_device_status_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status_nic, Unset):
        json_device_status_nic = device_status_nic

    params["device_status__nic"] = json_device_status_nic

    json_device_status_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status_nie, Unset):
        json_device_status_nie = device_status_nie

    params["device_status__nie"] = json_device_status_nie

    json_device_status_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status_niew, Unset):
        json_device_status_niew = device_status_niew

    params["device_status__niew"] = json_device_status_niew

    json_device_status_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(device_status_nisw, Unset):
        json_device_status_nisw = device_status_nisw

    params["device_status__nisw"] = json_device_status_nisw

    json_device_type: Union[Unset, list[str]] = UNSET
    if not isinstance(device_type, Unset):
        json_device_type = device_type

    params["device_type"] = json_device_type

    json_device_type_n: Union[Unset, list[str]] = UNSET
    if not isinstance(device_type_n, Unset):
        json_device_type_n = device_type_n

    params["device_type__n"] = json_device_type_n

    json_device_type_id: Union[Unset, list[int]] = UNSET
    if not isinstance(device_type_id, Unset):
        json_device_type_id = device_type_id

    params["device_type_id"] = json_device_type_id

    json_device_type_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(device_type_id_n, Unset):
        json_device_type_id_n = device_type_id_n

    params["device_type_id__n"] = json_device_type_id_n

    json_feed_leg: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(feed_leg, Unset):
        json_feed_leg = []
        for feed_leg_item_data in feed_leg:
            feed_leg_item: Union[None, str]
            feed_leg_item = feed_leg_item_data
            json_feed_leg.append(feed_leg_item)

    params["feed_leg"] = json_feed_leg

    params["feed_leg__empty"] = feed_leg_empty

    json_feed_leg_ic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(feed_leg_ic, Unset):
        json_feed_leg_ic = []
        for feed_leg_ic_item_data in feed_leg_ic:
            feed_leg_ic_item: Union[None, str]
            feed_leg_ic_item = feed_leg_ic_item_data
            json_feed_leg_ic.append(feed_leg_ic_item)

    params["feed_leg__ic"] = json_feed_leg_ic

    json_feed_leg_ie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(feed_leg_ie, Unset):
        json_feed_leg_ie = []
        for feed_leg_ie_item_data in feed_leg_ie:
            feed_leg_ie_item: Union[None, str]
            feed_leg_ie_item = feed_leg_ie_item_data
            json_feed_leg_ie.append(feed_leg_ie_item)

    params["feed_leg__ie"] = json_feed_leg_ie

    json_feed_leg_iew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(feed_leg_iew, Unset):
        json_feed_leg_iew = []
        for feed_leg_iew_item_data in feed_leg_iew:
            feed_leg_iew_item: Union[None, str]
            feed_leg_iew_item = feed_leg_iew_item_data
            json_feed_leg_iew.append(feed_leg_iew_item)

    params["feed_leg__iew"] = json_feed_leg_iew

    json_feed_leg_isw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(feed_leg_isw, Unset):
        json_feed_leg_isw = []
        for feed_leg_isw_item_data in feed_leg_isw:
            feed_leg_isw_item: Union[None, str]
            feed_leg_isw_item = feed_leg_isw_item_data
            json_feed_leg_isw.append(feed_leg_isw_item)

    params["feed_leg__isw"] = json_feed_leg_isw

    json_feed_leg_n: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(feed_leg_n, Unset):
        json_feed_leg_n = []
        for feed_leg_n_item_data in feed_leg_n:
            feed_leg_n_item: Union[None, str]
            feed_leg_n_item = feed_leg_n_item_data
            json_feed_leg_n.append(feed_leg_n_item)

    params["feed_leg__n"] = json_feed_leg_n

    json_feed_leg_nic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(feed_leg_nic, Unset):
        json_feed_leg_nic = []
        for feed_leg_nic_item_data in feed_leg_nic:
            feed_leg_nic_item: Union[None, str]
            feed_leg_nic_item = feed_leg_nic_item_data
            json_feed_leg_nic.append(feed_leg_nic_item)

    params["feed_leg__nic"] = json_feed_leg_nic

    json_feed_leg_nie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(feed_leg_nie, Unset):
        json_feed_leg_nie = []
        for feed_leg_nie_item_data in feed_leg_nie:
            feed_leg_nie_item: Union[None, str]
            feed_leg_nie_item = feed_leg_nie_item_data
            json_feed_leg_nie.append(feed_leg_nie_item)

    params["feed_leg__nie"] = json_feed_leg_nie

    json_feed_leg_niew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(feed_leg_niew, Unset):
        json_feed_leg_niew = []
        for feed_leg_niew_item_data in feed_leg_niew:
            feed_leg_niew_item: Union[None, str]
            feed_leg_niew_item = feed_leg_niew_item_data
            json_feed_leg_niew.append(feed_leg_niew_item)

    params["feed_leg__niew"] = json_feed_leg_niew

    json_feed_leg_nisw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(feed_leg_nisw, Unset):
        json_feed_leg_nisw = []
        for feed_leg_nisw_item_data in feed_leg_nisw:
            feed_leg_nisw_item: Union[None, str]
            feed_leg_nisw_item = feed_leg_nisw_item_data
            json_feed_leg_nisw.append(feed_leg_nisw_item)

    params["feed_leg__nisw"] = json_feed_leg_nisw

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

    params["limit"] = limit

    json_location: Union[Unset, list[str]] = UNSET
    if not isinstance(location, Unset):
        json_location = location

    params["location"] = json_location

    json_location_n: Union[Unset, list[str]] = UNSET
    if not isinstance(location_n, Unset):
        json_location_n = location_n

    params["location__n"] = json_location_n

    json_location_id: Union[Unset, list[int]] = UNSET
    if not isinstance(location_id, Unset):
        json_location_id = location_id

    params["location_id"] = json_location_id

    json_location_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(location_id_n, Unset):
        json_location_id_n = location_id_n

    params["location_id__n"] = json_location_id_n

    params["mark_connected"] = mark_connected

    json_modified_by_request: Union[Unset, str] = UNSET
    if not isinstance(modified_by_request, Unset):
        json_modified_by_request = str(modified_by_request)
    params["modified_by_request"] = json_modified_by_request

    json_module_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(module_id, Unset):
        json_module_id = []
        for module_id_item_data in module_id:
            module_id_item: Union[None, int]
            module_id_item = module_id_item_data
            json_module_id.append(module_id_item)

    params["module_id"] = json_module_id

    json_module_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(module_id_n, Unset):
        json_module_id_n = []
        for module_id_n_item_data in module_id_n:
            module_id_n_item: Union[None, int]
            module_id_n_item = module_id_n_item_data
            json_module_id_n.append(module_id_n_item)

    params["module_id__n"] = json_module_id_n

    json_name: Union[Unset, list[str]] = UNSET
    if not isinstance(name, Unset):
        json_name = name

    params["name"] = json_name

    params["name__empty"] = name_empty

    json_name_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(name_ic, Unset):
        json_name_ic = name_ic

    params["name__ic"] = json_name_ic

    json_name_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(name_ie, Unset):
        json_name_ie = name_ie

    params["name__ie"] = json_name_ie

    json_name_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(name_iew, Unset):
        json_name_iew = name_iew

    params["name__iew"] = json_name_iew

    json_name_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(name_isw, Unset):
        json_name_isw = name_isw

    params["name__isw"] = json_name_isw

    json_name_n: Union[Unset, list[str]] = UNSET
    if not isinstance(name_n, Unset):
        json_name_n = name_n

    params["name__n"] = json_name_n

    json_name_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(name_nic, Unset):
        json_name_nic = name_nic

    params["name__nic"] = json_name_nic

    json_name_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(name_nie, Unset):
        json_name_nie = name_nie

    params["name__nie"] = json_name_nie

    json_name_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(name_niew, Unset):
        json_name_niew = name_niew

    params["name__niew"] = json_name_niew

    json_name_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(name_nisw, Unset):
        json_name_nisw = name_nisw

    params["name__nisw"] = json_name_nisw

    params["occupied"] = occupied

    params["offset"] = offset

    params["ordering"] = ordering

    json_power_port_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(power_port_id, Unset):
        json_power_port_id = []
        for power_port_id_item_data in power_port_id:
            power_port_id_item: Union[None, int]
            power_port_id_item = power_port_id_item_data
            json_power_port_id.append(power_port_id_item)

    params["power_port_id"] = json_power_port_id

    json_power_port_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(power_port_id_n, Unset):
        json_power_port_id_n = []
        for power_port_id_n_item_data in power_port_id_n:
            power_port_id_n_item: Union[None, int]
            power_port_id_n_item = power_port_id_n_item_data
            json_power_port_id_n.append(power_port_id_n_item)

    params["power_port_id__n"] = json_power_port_id_n

    params["q"] = q

    json_rack: Union[Unset, list[str]] = UNSET
    if not isinstance(rack, Unset):
        json_rack = rack

    params["rack"] = json_rack

    json_rack_n: Union[Unset, list[str]] = UNSET
    if not isinstance(rack_n, Unset):
        json_rack_n = rack_n

    params["rack__n"] = json_rack_n

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

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    json_virtual_chassis: Union[Unset, list[str]] = UNSET
    if not isinstance(virtual_chassis, Unset):
        json_virtual_chassis = virtual_chassis

    params["virtual_chassis"] = json_virtual_chassis

    json_virtual_chassis_n: Union[Unset, list[str]] = UNSET
    if not isinstance(virtual_chassis_n, Unset):
        json_virtual_chassis_n = virtual_chassis_n

    params["virtual_chassis__n"] = json_virtual_chassis_n

    json_virtual_chassis_id: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_chassis_id, Unset):
        json_virtual_chassis_id = virtual_chassis_id

    params["virtual_chassis_id"] = json_virtual_chassis_id

    json_virtual_chassis_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_chassis_id_n, Unset):
        json_virtual_chassis_id_n = virtual_chassis_id_n

    params["virtual_chassis_id__n"] = json_virtual_chassis_id_n

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/dcim/power-outlets/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedPowerOutletList]:
    if response.status_code == 200:
        response_200 = PaginatedPowerOutletList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedPowerOutletList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cable_end: Union[Unset, DcimPowerOutletsListCableEnd] = UNSET,
    cable_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cable_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cabled: Union[Unset, bool] = UNSET,
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
    connected: Union[Unset, bool] = UNSET,
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
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    device_id_n: Union[Unset, list[int]] = UNSET,
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_id: Union[Unset, list[int]] = UNSET,
    device_role_id_n: Union[Unset, list[int]] = UNSET,
    device_status: Union[Unset, list[str]] = UNSET,
    device_status_empty: Union[Unset, bool] = UNSET,
    device_status_ic: Union[Unset, list[str]] = UNSET,
    device_status_ie: Union[Unset, list[str]] = UNSET,
    device_status_iew: Union[Unset, list[str]] = UNSET,
    device_status_isw: Union[Unset, list[str]] = UNSET,
    device_status_n: Union[Unset, list[str]] = UNSET,
    device_status_nic: Union[Unset, list[str]] = UNSET,
    device_status_nie: Union[Unset, list[str]] = UNSET,
    device_status_niew: Union[Unset, list[str]] = UNSET,
    device_status_nisw: Union[Unset, list[str]] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    feed_leg: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_empty: Union[Unset, bool] = UNSET,
    feed_leg_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_n: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
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
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
    mark_connected: Union[Unset, bool] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_id: Union[Unset, list[Union[None, int]]] = UNSET,
    module_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    name: Union[Unset, list[str]] = UNSET,
    name_empty: Union[Unset, bool] = UNSET,
    name_ic: Union[Unset, list[str]] = UNSET,
    name_ie: Union[Unset, list[str]] = UNSET,
    name_iew: Union[Unset, list[str]] = UNSET,
    name_isw: Union[Unset, list[str]] = UNSET,
    name_n: Union[Unset, list[str]] = UNSET,
    name_nic: Union[Unset, list[str]] = UNSET,
    name_nie: Union[Unset, list[str]] = UNSET,
    name_niew: Union[Unset, list[str]] = UNSET,
    name_nisw: Union[Unset, list[str]] = UNSET,
    occupied: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    power_port_id: Union[Unset, list[Union[None, int]]] = UNSET,
    power_port_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_chassis: Union[Unset, list[str]] = UNSET,
    virtual_chassis_n: Union[Unset, list[str]] = UNSET,
    virtual_chassis_id: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedPowerOutletList]:
    """Get a list of power outlet objects.

    Args:
        cable_end (Union[Unset, DcimPowerOutletsListCableEnd]):
        cable_id (Union[Unset, list[Union[None, int]]]):
        cable_id_n (Union[Unset, list[Union[None, int]]]):
        cabled (Union[Unset, bool]):
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
        connected (Union[Unset, bool]):
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
        device (Union[Unset, list[Union[None, str]]]):
        device_n (Union[Unset, list[Union[None, str]]]):
        device_id (Union[Unset, list[int]]):
        device_id_n (Union[Unset, list[int]]):
        device_role (Union[Unset, list[str]]):
        device_role_n (Union[Unset, list[str]]):
        device_role_id (Union[Unset, list[int]]):
        device_role_id_n (Union[Unset, list[int]]):
        device_status (Union[Unset, list[str]]):
        device_status_empty (Union[Unset, bool]):
        device_status_ic (Union[Unset, list[str]]):
        device_status_ie (Union[Unset, list[str]]):
        device_status_iew (Union[Unset, list[str]]):
        device_status_isw (Union[Unset, list[str]]):
        device_status_n (Union[Unset, list[str]]):
        device_status_nic (Union[Unset, list[str]]):
        device_status_nie (Union[Unset, list[str]]):
        device_status_niew (Union[Unset, list[str]]):
        device_status_nisw (Union[Unset, list[str]]):
        device_type (Union[Unset, list[str]]):
        device_type_n (Union[Unset, list[str]]):
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
        feed_leg (Union[Unset, list[Union[None, str]]]):
        feed_leg_empty (Union[Unset, bool]):
        feed_leg_ic (Union[Unset, list[Union[None, str]]]):
        feed_leg_ie (Union[Unset, list[Union[None, str]]]):
        feed_leg_iew (Union[Unset, list[Union[None, str]]]):
        feed_leg_isw (Union[Unset, list[Union[None, str]]]):
        feed_leg_n (Union[Unset, list[Union[None, str]]]):
        feed_leg_nic (Union[Unset, list[Union[None, str]]]):
        feed_leg_nie (Union[Unset, list[Union[None, str]]]):
        feed_leg_niew (Union[Unset, list[Union[None, str]]]):
        feed_leg_nisw (Union[Unset, list[Union[None, str]]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
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
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_id (Union[Unset, list[int]]):
        location_id_n (Union[Unset, list[int]]):
        mark_connected (Union[Unset, bool]):
        modified_by_request (Union[Unset, UUID]):
        module_id (Union[Unset, list[Union[None, int]]]):
        module_id_n (Union[Unset, list[Union[None, int]]]):
        name (Union[Unset, list[str]]):
        name_empty (Union[Unset, bool]):
        name_ic (Union[Unset, list[str]]):
        name_ie (Union[Unset, list[str]]):
        name_iew (Union[Unset, list[str]]):
        name_isw (Union[Unset, list[str]]):
        name_n (Union[Unset, list[str]]):
        name_nic (Union[Unset, list[str]]):
        name_nie (Union[Unset, list[str]]):
        name_niew (Union[Unset, list[str]]):
        name_nisw (Union[Unset, list[str]]):
        occupied (Union[Unset, bool]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        power_port_id (Union[Unset, list[Union[None, int]]]):
        power_port_id_n (Union[Unset, list[Union[None, int]]]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_n (Union[Unset, list[str]]):
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
        updated_by_request (Union[Unset, UUID]):
        virtual_chassis (Union[Unset, list[str]]):
        virtual_chassis_n (Union[Unset, list[str]]):
        virtual_chassis_id (Union[Unset, list[int]]):
        virtual_chassis_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPowerOutletList]
    """

    kwargs = _get_kwargs(
        cable_end=cable_end,
        cable_id=cable_id,
        cable_id_n=cable_id_n,
        cabled=cabled,
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
        connected=connected,
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
        device_n=device_n,
        device_id=device_id,
        device_id_n=device_id_n,
        device_role=device_role,
        device_role_n=device_role_n,
        device_role_id=device_role_id,
        device_role_id_n=device_role_id_n,
        device_status=device_status,
        device_status_empty=device_status_empty,
        device_status_ic=device_status_ic,
        device_status_ie=device_status_ie,
        device_status_iew=device_status_iew,
        device_status_isw=device_status_isw,
        device_status_n=device_status_n,
        device_status_nic=device_status_nic,
        device_status_nie=device_status_nie,
        device_status_niew=device_status_niew,
        device_status_nisw=device_status_nisw,
        device_type=device_type,
        device_type_n=device_type_n,
        device_type_id=device_type_id,
        device_type_id_n=device_type_id_n,
        feed_leg=feed_leg,
        feed_leg_empty=feed_leg_empty,
        feed_leg_ic=feed_leg_ic,
        feed_leg_ie=feed_leg_ie,
        feed_leg_iew=feed_leg_iew,
        feed_leg_isw=feed_leg_isw,
        feed_leg_n=feed_leg_n,
        feed_leg_nic=feed_leg_nic,
        feed_leg_nie=feed_leg_nie,
        feed_leg_niew=feed_leg_niew,
        feed_leg_nisw=feed_leg_nisw,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
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
        limit=limit,
        location=location,
        location_n=location_n,
        location_id=location_id,
        location_id_n=location_id_n,
        mark_connected=mark_connected,
        modified_by_request=modified_by_request,
        module_id=module_id,
        module_id_n=module_id_n,
        name=name,
        name_empty=name_empty,
        name_ic=name_ic,
        name_ie=name_ie,
        name_iew=name_iew,
        name_isw=name_isw,
        name_n=name_n,
        name_nic=name_nic,
        name_nie=name_nie,
        name_niew=name_niew,
        name_nisw=name_nisw,
        occupied=occupied,
        offset=offset,
        ordering=ordering,
        power_port_id=power_port_id,
        power_port_id_n=power_port_id_n,
        q=q,
        rack=rack,
        rack_n=rack_n,
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
        updated_by_request=updated_by_request,
        virtual_chassis=virtual_chassis,
        virtual_chassis_n=virtual_chassis_n,
        virtual_chassis_id=virtual_chassis_id,
        virtual_chassis_id_n=virtual_chassis_id_n,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cable_end: Union[Unset, DcimPowerOutletsListCableEnd] = UNSET,
    cable_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cable_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cabled: Union[Unset, bool] = UNSET,
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
    connected: Union[Unset, bool] = UNSET,
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
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    device_id_n: Union[Unset, list[int]] = UNSET,
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_id: Union[Unset, list[int]] = UNSET,
    device_role_id_n: Union[Unset, list[int]] = UNSET,
    device_status: Union[Unset, list[str]] = UNSET,
    device_status_empty: Union[Unset, bool] = UNSET,
    device_status_ic: Union[Unset, list[str]] = UNSET,
    device_status_ie: Union[Unset, list[str]] = UNSET,
    device_status_iew: Union[Unset, list[str]] = UNSET,
    device_status_isw: Union[Unset, list[str]] = UNSET,
    device_status_n: Union[Unset, list[str]] = UNSET,
    device_status_nic: Union[Unset, list[str]] = UNSET,
    device_status_nie: Union[Unset, list[str]] = UNSET,
    device_status_niew: Union[Unset, list[str]] = UNSET,
    device_status_nisw: Union[Unset, list[str]] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    feed_leg: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_empty: Union[Unset, bool] = UNSET,
    feed_leg_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_n: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
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
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
    mark_connected: Union[Unset, bool] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_id: Union[Unset, list[Union[None, int]]] = UNSET,
    module_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    name: Union[Unset, list[str]] = UNSET,
    name_empty: Union[Unset, bool] = UNSET,
    name_ic: Union[Unset, list[str]] = UNSET,
    name_ie: Union[Unset, list[str]] = UNSET,
    name_iew: Union[Unset, list[str]] = UNSET,
    name_isw: Union[Unset, list[str]] = UNSET,
    name_n: Union[Unset, list[str]] = UNSET,
    name_nic: Union[Unset, list[str]] = UNSET,
    name_nie: Union[Unset, list[str]] = UNSET,
    name_niew: Union[Unset, list[str]] = UNSET,
    name_nisw: Union[Unset, list[str]] = UNSET,
    occupied: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    power_port_id: Union[Unset, list[Union[None, int]]] = UNSET,
    power_port_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_chassis: Union[Unset, list[str]] = UNSET,
    virtual_chassis_n: Union[Unset, list[str]] = UNSET,
    virtual_chassis_id: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedPowerOutletList]:
    """Get a list of power outlet objects.

    Args:
        cable_end (Union[Unset, DcimPowerOutletsListCableEnd]):
        cable_id (Union[Unset, list[Union[None, int]]]):
        cable_id_n (Union[Unset, list[Union[None, int]]]):
        cabled (Union[Unset, bool]):
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
        connected (Union[Unset, bool]):
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
        device (Union[Unset, list[Union[None, str]]]):
        device_n (Union[Unset, list[Union[None, str]]]):
        device_id (Union[Unset, list[int]]):
        device_id_n (Union[Unset, list[int]]):
        device_role (Union[Unset, list[str]]):
        device_role_n (Union[Unset, list[str]]):
        device_role_id (Union[Unset, list[int]]):
        device_role_id_n (Union[Unset, list[int]]):
        device_status (Union[Unset, list[str]]):
        device_status_empty (Union[Unset, bool]):
        device_status_ic (Union[Unset, list[str]]):
        device_status_ie (Union[Unset, list[str]]):
        device_status_iew (Union[Unset, list[str]]):
        device_status_isw (Union[Unset, list[str]]):
        device_status_n (Union[Unset, list[str]]):
        device_status_nic (Union[Unset, list[str]]):
        device_status_nie (Union[Unset, list[str]]):
        device_status_niew (Union[Unset, list[str]]):
        device_status_nisw (Union[Unset, list[str]]):
        device_type (Union[Unset, list[str]]):
        device_type_n (Union[Unset, list[str]]):
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
        feed_leg (Union[Unset, list[Union[None, str]]]):
        feed_leg_empty (Union[Unset, bool]):
        feed_leg_ic (Union[Unset, list[Union[None, str]]]):
        feed_leg_ie (Union[Unset, list[Union[None, str]]]):
        feed_leg_iew (Union[Unset, list[Union[None, str]]]):
        feed_leg_isw (Union[Unset, list[Union[None, str]]]):
        feed_leg_n (Union[Unset, list[Union[None, str]]]):
        feed_leg_nic (Union[Unset, list[Union[None, str]]]):
        feed_leg_nie (Union[Unset, list[Union[None, str]]]):
        feed_leg_niew (Union[Unset, list[Union[None, str]]]):
        feed_leg_nisw (Union[Unset, list[Union[None, str]]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
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
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_id (Union[Unset, list[int]]):
        location_id_n (Union[Unset, list[int]]):
        mark_connected (Union[Unset, bool]):
        modified_by_request (Union[Unset, UUID]):
        module_id (Union[Unset, list[Union[None, int]]]):
        module_id_n (Union[Unset, list[Union[None, int]]]):
        name (Union[Unset, list[str]]):
        name_empty (Union[Unset, bool]):
        name_ic (Union[Unset, list[str]]):
        name_ie (Union[Unset, list[str]]):
        name_iew (Union[Unset, list[str]]):
        name_isw (Union[Unset, list[str]]):
        name_n (Union[Unset, list[str]]):
        name_nic (Union[Unset, list[str]]):
        name_nie (Union[Unset, list[str]]):
        name_niew (Union[Unset, list[str]]):
        name_nisw (Union[Unset, list[str]]):
        occupied (Union[Unset, bool]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        power_port_id (Union[Unset, list[Union[None, int]]]):
        power_port_id_n (Union[Unset, list[Union[None, int]]]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_n (Union[Unset, list[str]]):
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
        updated_by_request (Union[Unset, UUID]):
        virtual_chassis (Union[Unset, list[str]]):
        virtual_chassis_n (Union[Unset, list[str]]):
        virtual_chassis_id (Union[Unset, list[int]]):
        virtual_chassis_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedPowerOutletList
    """

    return sync_detailed(
        client=client,
        cable_end=cable_end,
        cable_id=cable_id,
        cable_id_n=cable_id_n,
        cabled=cabled,
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
        connected=connected,
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
        device_n=device_n,
        device_id=device_id,
        device_id_n=device_id_n,
        device_role=device_role,
        device_role_n=device_role_n,
        device_role_id=device_role_id,
        device_role_id_n=device_role_id_n,
        device_status=device_status,
        device_status_empty=device_status_empty,
        device_status_ic=device_status_ic,
        device_status_ie=device_status_ie,
        device_status_iew=device_status_iew,
        device_status_isw=device_status_isw,
        device_status_n=device_status_n,
        device_status_nic=device_status_nic,
        device_status_nie=device_status_nie,
        device_status_niew=device_status_niew,
        device_status_nisw=device_status_nisw,
        device_type=device_type,
        device_type_n=device_type_n,
        device_type_id=device_type_id,
        device_type_id_n=device_type_id_n,
        feed_leg=feed_leg,
        feed_leg_empty=feed_leg_empty,
        feed_leg_ic=feed_leg_ic,
        feed_leg_ie=feed_leg_ie,
        feed_leg_iew=feed_leg_iew,
        feed_leg_isw=feed_leg_isw,
        feed_leg_n=feed_leg_n,
        feed_leg_nic=feed_leg_nic,
        feed_leg_nie=feed_leg_nie,
        feed_leg_niew=feed_leg_niew,
        feed_leg_nisw=feed_leg_nisw,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
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
        limit=limit,
        location=location,
        location_n=location_n,
        location_id=location_id,
        location_id_n=location_id_n,
        mark_connected=mark_connected,
        modified_by_request=modified_by_request,
        module_id=module_id,
        module_id_n=module_id_n,
        name=name,
        name_empty=name_empty,
        name_ic=name_ic,
        name_ie=name_ie,
        name_iew=name_iew,
        name_isw=name_isw,
        name_n=name_n,
        name_nic=name_nic,
        name_nie=name_nie,
        name_niew=name_niew,
        name_nisw=name_nisw,
        occupied=occupied,
        offset=offset,
        ordering=ordering,
        power_port_id=power_port_id,
        power_port_id_n=power_port_id_n,
        q=q,
        rack=rack,
        rack_n=rack_n,
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
        updated_by_request=updated_by_request,
        virtual_chassis=virtual_chassis,
        virtual_chassis_n=virtual_chassis_n,
        virtual_chassis_id=virtual_chassis_id,
        virtual_chassis_id_n=virtual_chassis_id_n,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cable_end: Union[Unset, DcimPowerOutletsListCableEnd] = UNSET,
    cable_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cable_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cabled: Union[Unset, bool] = UNSET,
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
    connected: Union[Unset, bool] = UNSET,
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
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    device_id_n: Union[Unset, list[int]] = UNSET,
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_id: Union[Unset, list[int]] = UNSET,
    device_role_id_n: Union[Unset, list[int]] = UNSET,
    device_status: Union[Unset, list[str]] = UNSET,
    device_status_empty: Union[Unset, bool] = UNSET,
    device_status_ic: Union[Unset, list[str]] = UNSET,
    device_status_ie: Union[Unset, list[str]] = UNSET,
    device_status_iew: Union[Unset, list[str]] = UNSET,
    device_status_isw: Union[Unset, list[str]] = UNSET,
    device_status_n: Union[Unset, list[str]] = UNSET,
    device_status_nic: Union[Unset, list[str]] = UNSET,
    device_status_nie: Union[Unset, list[str]] = UNSET,
    device_status_niew: Union[Unset, list[str]] = UNSET,
    device_status_nisw: Union[Unset, list[str]] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    feed_leg: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_empty: Union[Unset, bool] = UNSET,
    feed_leg_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_n: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
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
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
    mark_connected: Union[Unset, bool] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_id: Union[Unset, list[Union[None, int]]] = UNSET,
    module_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    name: Union[Unset, list[str]] = UNSET,
    name_empty: Union[Unset, bool] = UNSET,
    name_ic: Union[Unset, list[str]] = UNSET,
    name_ie: Union[Unset, list[str]] = UNSET,
    name_iew: Union[Unset, list[str]] = UNSET,
    name_isw: Union[Unset, list[str]] = UNSET,
    name_n: Union[Unset, list[str]] = UNSET,
    name_nic: Union[Unset, list[str]] = UNSET,
    name_nie: Union[Unset, list[str]] = UNSET,
    name_niew: Union[Unset, list[str]] = UNSET,
    name_nisw: Union[Unset, list[str]] = UNSET,
    occupied: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    power_port_id: Union[Unset, list[Union[None, int]]] = UNSET,
    power_port_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_chassis: Union[Unset, list[str]] = UNSET,
    virtual_chassis_n: Union[Unset, list[str]] = UNSET,
    virtual_chassis_id: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedPowerOutletList]:
    """Get a list of power outlet objects.

    Args:
        cable_end (Union[Unset, DcimPowerOutletsListCableEnd]):
        cable_id (Union[Unset, list[Union[None, int]]]):
        cable_id_n (Union[Unset, list[Union[None, int]]]):
        cabled (Union[Unset, bool]):
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
        connected (Union[Unset, bool]):
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
        device (Union[Unset, list[Union[None, str]]]):
        device_n (Union[Unset, list[Union[None, str]]]):
        device_id (Union[Unset, list[int]]):
        device_id_n (Union[Unset, list[int]]):
        device_role (Union[Unset, list[str]]):
        device_role_n (Union[Unset, list[str]]):
        device_role_id (Union[Unset, list[int]]):
        device_role_id_n (Union[Unset, list[int]]):
        device_status (Union[Unset, list[str]]):
        device_status_empty (Union[Unset, bool]):
        device_status_ic (Union[Unset, list[str]]):
        device_status_ie (Union[Unset, list[str]]):
        device_status_iew (Union[Unset, list[str]]):
        device_status_isw (Union[Unset, list[str]]):
        device_status_n (Union[Unset, list[str]]):
        device_status_nic (Union[Unset, list[str]]):
        device_status_nie (Union[Unset, list[str]]):
        device_status_niew (Union[Unset, list[str]]):
        device_status_nisw (Union[Unset, list[str]]):
        device_type (Union[Unset, list[str]]):
        device_type_n (Union[Unset, list[str]]):
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
        feed_leg (Union[Unset, list[Union[None, str]]]):
        feed_leg_empty (Union[Unset, bool]):
        feed_leg_ic (Union[Unset, list[Union[None, str]]]):
        feed_leg_ie (Union[Unset, list[Union[None, str]]]):
        feed_leg_iew (Union[Unset, list[Union[None, str]]]):
        feed_leg_isw (Union[Unset, list[Union[None, str]]]):
        feed_leg_n (Union[Unset, list[Union[None, str]]]):
        feed_leg_nic (Union[Unset, list[Union[None, str]]]):
        feed_leg_nie (Union[Unset, list[Union[None, str]]]):
        feed_leg_niew (Union[Unset, list[Union[None, str]]]):
        feed_leg_nisw (Union[Unset, list[Union[None, str]]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
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
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_id (Union[Unset, list[int]]):
        location_id_n (Union[Unset, list[int]]):
        mark_connected (Union[Unset, bool]):
        modified_by_request (Union[Unset, UUID]):
        module_id (Union[Unset, list[Union[None, int]]]):
        module_id_n (Union[Unset, list[Union[None, int]]]):
        name (Union[Unset, list[str]]):
        name_empty (Union[Unset, bool]):
        name_ic (Union[Unset, list[str]]):
        name_ie (Union[Unset, list[str]]):
        name_iew (Union[Unset, list[str]]):
        name_isw (Union[Unset, list[str]]):
        name_n (Union[Unset, list[str]]):
        name_nic (Union[Unset, list[str]]):
        name_nie (Union[Unset, list[str]]):
        name_niew (Union[Unset, list[str]]):
        name_nisw (Union[Unset, list[str]]):
        occupied (Union[Unset, bool]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        power_port_id (Union[Unset, list[Union[None, int]]]):
        power_port_id_n (Union[Unset, list[Union[None, int]]]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_n (Union[Unset, list[str]]):
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
        updated_by_request (Union[Unset, UUID]):
        virtual_chassis (Union[Unset, list[str]]):
        virtual_chassis_n (Union[Unset, list[str]]):
        virtual_chassis_id (Union[Unset, list[int]]):
        virtual_chassis_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPowerOutletList]
    """

    kwargs = _get_kwargs(
        cable_end=cable_end,
        cable_id=cable_id,
        cable_id_n=cable_id_n,
        cabled=cabled,
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
        connected=connected,
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
        device_n=device_n,
        device_id=device_id,
        device_id_n=device_id_n,
        device_role=device_role,
        device_role_n=device_role_n,
        device_role_id=device_role_id,
        device_role_id_n=device_role_id_n,
        device_status=device_status,
        device_status_empty=device_status_empty,
        device_status_ic=device_status_ic,
        device_status_ie=device_status_ie,
        device_status_iew=device_status_iew,
        device_status_isw=device_status_isw,
        device_status_n=device_status_n,
        device_status_nic=device_status_nic,
        device_status_nie=device_status_nie,
        device_status_niew=device_status_niew,
        device_status_nisw=device_status_nisw,
        device_type=device_type,
        device_type_n=device_type_n,
        device_type_id=device_type_id,
        device_type_id_n=device_type_id_n,
        feed_leg=feed_leg,
        feed_leg_empty=feed_leg_empty,
        feed_leg_ic=feed_leg_ic,
        feed_leg_ie=feed_leg_ie,
        feed_leg_iew=feed_leg_iew,
        feed_leg_isw=feed_leg_isw,
        feed_leg_n=feed_leg_n,
        feed_leg_nic=feed_leg_nic,
        feed_leg_nie=feed_leg_nie,
        feed_leg_niew=feed_leg_niew,
        feed_leg_nisw=feed_leg_nisw,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
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
        limit=limit,
        location=location,
        location_n=location_n,
        location_id=location_id,
        location_id_n=location_id_n,
        mark_connected=mark_connected,
        modified_by_request=modified_by_request,
        module_id=module_id,
        module_id_n=module_id_n,
        name=name,
        name_empty=name_empty,
        name_ic=name_ic,
        name_ie=name_ie,
        name_iew=name_iew,
        name_isw=name_isw,
        name_n=name_n,
        name_nic=name_nic,
        name_nie=name_nie,
        name_niew=name_niew,
        name_nisw=name_nisw,
        occupied=occupied,
        offset=offset,
        ordering=ordering,
        power_port_id=power_port_id,
        power_port_id_n=power_port_id_n,
        q=q,
        rack=rack,
        rack_n=rack_n,
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
        updated_by_request=updated_by_request,
        virtual_chassis=virtual_chassis,
        virtual_chassis_n=virtual_chassis_n,
        virtual_chassis_id=virtual_chassis_id,
        virtual_chassis_id_n=virtual_chassis_id_n,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cable_end: Union[Unset, DcimPowerOutletsListCableEnd] = UNSET,
    cable_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cable_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cabled: Union[Unset, bool] = UNSET,
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
    connected: Union[Unset, bool] = UNSET,
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
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    device_id_n: Union[Unset, list[int]] = UNSET,
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_id: Union[Unset, list[int]] = UNSET,
    device_role_id_n: Union[Unset, list[int]] = UNSET,
    device_status: Union[Unset, list[str]] = UNSET,
    device_status_empty: Union[Unset, bool] = UNSET,
    device_status_ic: Union[Unset, list[str]] = UNSET,
    device_status_ie: Union[Unset, list[str]] = UNSET,
    device_status_iew: Union[Unset, list[str]] = UNSET,
    device_status_isw: Union[Unset, list[str]] = UNSET,
    device_status_n: Union[Unset, list[str]] = UNSET,
    device_status_nic: Union[Unset, list[str]] = UNSET,
    device_status_nie: Union[Unset, list[str]] = UNSET,
    device_status_niew: Union[Unset, list[str]] = UNSET,
    device_status_nisw: Union[Unset, list[str]] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
    feed_leg: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_empty: Union[Unset, bool] = UNSET,
    feed_leg_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_n: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    feed_leg_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
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
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
    mark_connected: Union[Unset, bool] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_id: Union[Unset, list[Union[None, int]]] = UNSET,
    module_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    name: Union[Unset, list[str]] = UNSET,
    name_empty: Union[Unset, bool] = UNSET,
    name_ic: Union[Unset, list[str]] = UNSET,
    name_ie: Union[Unset, list[str]] = UNSET,
    name_iew: Union[Unset, list[str]] = UNSET,
    name_isw: Union[Unset, list[str]] = UNSET,
    name_n: Union[Unset, list[str]] = UNSET,
    name_nic: Union[Unset, list[str]] = UNSET,
    name_nie: Union[Unset, list[str]] = UNSET,
    name_niew: Union[Unset, list[str]] = UNSET,
    name_nisw: Union[Unset, list[str]] = UNSET,
    occupied: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    power_port_id: Union[Unset, list[Union[None, int]]] = UNSET,
    power_port_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_chassis: Union[Unset, list[str]] = UNSET,
    virtual_chassis_n: Union[Unset, list[str]] = UNSET,
    virtual_chassis_id: Union[Unset, list[int]] = UNSET,
    virtual_chassis_id_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedPowerOutletList]:
    """Get a list of power outlet objects.

    Args:
        cable_end (Union[Unset, DcimPowerOutletsListCableEnd]):
        cable_id (Union[Unset, list[Union[None, int]]]):
        cable_id_n (Union[Unset, list[Union[None, int]]]):
        cabled (Union[Unset, bool]):
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
        connected (Union[Unset, bool]):
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
        device (Union[Unset, list[Union[None, str]]]):
        device_n (Union[Unset, list[Union[None, str]]]):
        device_id (Union[Unset, list[int]]):
        device_id_n (Union[Unset, list[int]]):
        device_role (Union[Unset, list[str]]):
        device_role_n (Union[Unset, list[str]]):
        device_role_id (Union[Unset, list[int]]):
        device_role_id_n (Union[Unset, list[int]]):
        device_status (Union[Unset, list[str]]):
        device_status_empty (Union[Unset, bool]):
        device_status_ic (Union[Unset, list[str]]):
        device_status_ie (Union[Unset, list[str]]):
        device_status_iew (Union[Unset, list[str]]):
        device_status_isw (Union[Unset, list[str]]):
        device_status_n (Union[Unset, list[str]]):
        device_status_nic (Union[Unset, list[str]]):
        device_status_nie (Union[Unset, list[str]]):
        device_status_niew (Union[Unset, list[str]]):
        device_status_nisw (Union[Unset, list[str]]):
        device_type (Union[Unset, list[str]]):
        device_type_n (Union[Unset, list[str]]):
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
        feed_leg (Union[Unset, list[Union[None, str]]]):
        feed_leg_empty (Union[Unset, bool]):
        feed_leg_ic (Union[Unset, list[Union[None, str]]]):
        feed_leg_ie (Union[Unset, list[Union[None, str]]]):
        feed_leg_iew (Union[Unset, list[Union[None, str]]]):
        feed_leg_isw (Union[Unset, list[Union[None, str]]]):
        feed_leg_n (Union[Unset, list[Union[None, str]]]):
        feed_leg_nic (Union[Unset, list[Union[None, str]]]):
        feed_leg_nie (Union[Unset, list[Union[None, str]]]):
        feed_leg_niew (Union[Unset, list[Union[None, str]]]):
        feed_leg_nisw (Union[Unset, list[Union[None, str]]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
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
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_id (Union[Unset, list[int]]):
        location_id_n (Union[Unset, list[int]]):
        mark_connected (Union[Unset, bool]):
        modified_by_request (Union[Unset, UUID]):
        module_id (Union[Unset, list[Union[None, int]]]):
        module_id_n (Union[Unset, list[Union[None, int]]]):
        name (Union[Unset, list[str]]):
        name_empty (Union[Unset, bool]):
        name_ic (Union[Unset, list[str]]):
        name_ie (Union[Unset, list[str]]):
        name_iew (Union[Unset, list[str]]):
        name_isw (Union[Unset, list[str]]):
        name_n (Union[Unset, list[str]]):
        name_nic (Union[Unset, list[str]]):
        name_nie (Union[Unset, list[str]]):
        name_niew (Union[Unset, list[str]]):
        name_nisw (Union[Unset, list[str]]):
        occupied (Union[Unset, bool]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        power_port_id (Union[Unset, list[Union[None, int]]]):
        power_port_id_n (Union[Unset, list[Union[None, int]]]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_n (Union[Unset, list[str]]):
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
        updated_by_request (Union[Unset, UUID]):
        virtual_chassis (Union[Unset, list[str]]):
        virtual_chassis_n (Union[Unset, list[str]]):
        virtual_chassis_id (Union[Unset, list[int]]):
        virtual_chassis_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedPowerOutletList
    """

    return (
        await asyncio_detailed(
            client=client,
            cable_end=cable_end,
            cable_id=cable_id,
            cable_id_n=cable_id_n,
            cabled=cabled,
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
            connected=connected,
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
            device_n=device_n,
            device_id=device_id,
            device_id_n=device_id_n,
            device_role=device_role,
            device_role_n=device_role_n,
            device_role_id=device_role_id,
            device_role_id_n=device_role_id_n,
            device_status=device_status,
            device_status_empty=device_status_empty,
            device_status_ic=device_status_ic,
            device_status_ie=device_status_ie,
            device_status_iew=device_status_iew,
            device_status_isw=device_status_isw,
            device_status_n=device_status_n,
            device_status_nic=device_status_nic,
            device_status_nie=device_status_nie,
            device_status_niew=device_status_niew,
            device_status_nisw=device_status_nisw,
            device_type=device_type,
            device_type_n=device_type_n,
            device_type_id=device_type_id,
            device_type_id_n=device_type_id_n,
            feed_leg=feed_leg,
            feed_leg_empty=feed_leg_empty,
            feed_leg_ic=feed_leg_ic,
            feed_leg_ie=feed_leg_ie,
            feed_leg_iew=feed_leg_iew,
            feed_leg_isw=feed_leg_isw,
            feed_leg_n=feed_leg_n,
            feed_leg_nic=feed_leg_nic,
            feed_leg_nie=feed_leg_nie,
            feed_leg_niew=feed_leg_niew,
            feed_leg_nisw=feed_leg_nisw,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
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
            limit=limit,
            location=location,
            location_n=location_n,
            location_id=location_id,
            location_id_n=location_id_n,
            mark_connected=mark_connected,
            modified_by_request=modified_by_request,
            module_id=module_id,
            module_id_n=module_id_n,
            name=name,
            name_empty=name_empty,
            name_ic=name_ic,
            name_ie=name_ie,
            name_iew=name_iew,
            name_isw=name_isw,
            name_n=name_n,
            name_nic=name_nic,
            name_nie=name_nie,
            name_niew=name_niew,
            name_nisw=name_nisw,
            occupied=occupied,
            offset=offset,
            ordering=ordering,
            power_port_id=power_port_id,
            power_port_id_n=power_port_id_n,
            q=q,
            rack=rack,
            rack_n=rack_n,
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
            updated_by_request=updated_by_request,
            virtual_chassis=virtual_chassis,
            virtual_chassis_n=virtual_chassis_n,
            virtual_chassis_id=virtual_chassis_id,
            virtual_chassis_id_n=virtual_chassis_id_n,
        )
    ).parsed
