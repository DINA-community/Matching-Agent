import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_module_list import PaginatedModuleList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    asset_tag: Union[Unset, list[str]] = UNSET,
    asset_tag_empty: Union[Unset, bool] = UNSET,
    asset_tag_ic: Union[Unset, list[str]] = UNSET,
    asset_tag_ie: Union[Unset, list[str]] = UNSET,
    asset_tag_iew: Union[Unset, list[str]] = UNSET,
    asset_tag_isw: Union[Unset, list[str]] = UNSET,
    asset_tag_n: Union[Unset, list[str]] = UNSET,
    asset_tag_nic: Union[Unset, list[str]] = UNSET,
    asset_tag_nie: Union[Unset, list[str]] = UNSET,
    asset_tag_niew: Union[Unset, list[str]] = UNSET,
    asset_tag_nisw: Union[Unset, list[str]] = UNSET,
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
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_bay_id: Union[Unset, list[str]] = UNSET,
    module_bay_id_n: Union[Unset, list[str]] = UNSET,
    module_type: Union[Unset, list[str]] = UNSET,
    module_type_n: Union[Unset, list[str]] = UNSET,
    module_type_id: Union[Unset, list[int]] = UNSET,
    module_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    serial: Union[Unset, list[str]] = UNSET,
    serial_empty: Union[Unset, bool] = UNSET,
    serial_ic: Union[Unset, list[str]] = UNSET,
    serial_ie: Union[Unset, list[str]] = UNSET,
    serial_iew: Union[Unset, list[str]] = UNSET,
    serial_isw: Union[Unset, list[str]] = UNSET,
    serial_n: Union[Unset, list[str]] = UNSET,
    serial_nic: Union[Unset, list[str]] = UNSET,
    serial_nie: Union[Unset, list[str]] = UNSET,
    serial_niew: Union[Unset, list[str]] = UNSET,
    serial_nisw: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_asset_tag: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag, Unset):
        json_asset_tag = asset_tag

    params["asset_tag"] = json_asset_tag

    params["asset_tag__empty"] = asset_tag_empty

    json_asset_tag_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag_ic, Unset):
        json_asset_tag_ic = asset_tag_ic

    params["asset_tag__ic"] = json_asset_tag_ic

    json_asset_tag_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag_ie, Unset):
        json_asset_tag_ie = asset_tag_ie

    params["asset_tag__ie"] = json_asset_tag_ie

    json_asset_tag_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag_iew, Unset):
        json_asset_tag_iew = asset_tag_iew

    params["asset_tag__iew"] = json_asset_tag_iew

    json_asset_tag_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag_isw, Unset):
        json_asset_tag_isw = asset_tag_isw

    params["asset_tag__isw"] = json_asset_tag_isw

    json_asset_tag_n: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag_n, Unset):
        json_asset_tag_n = asset_tag_n

    params["asset_tag__n"] = json_asset_tag_n

    json_asset_tag_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag_nic, Unset):
        json_asset_tag_nic = asset_tag_nic

    params["asset_tag__nic"] = json_asset_tag_nic

    json_asset_tag_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag_nie, Unset):
        json_asset_tag_nie = asset_tag_nie

    params["asset_tag__nie"] = json_asset_tag_nie

    json_asset_tag_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag_niew, Unset):
        json_asset_tag_niew = asset_tag_niew

    params["asset_tag__niew"] = json_asset_tag_niew

    json_asset_tag_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(asset_tag_nisw, Unset):
        json_asset_tag_nisw = asset_tag_nisw

    params["asset_tag__nisw"] = json_asset_tag_nisw

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

    json_location_id: Union[Unset, list[int]] = UNSET
    if not isinstance(location_id, Unset):
        json_location_id = location_id

    params["location_id"] = json_location_id

    json_location_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(location_id_n, Unset):
        json_location_id_n = location_id_n

    params["location_id__n"] = json_location_id_n

    json_manufacturer: Union[Unset, list[str]] = UNSET
    if not isinstance(manufacturer, Unset):
        json_manufacturer = manufacturer

    params["manufacturer"] = json_manufacturer

    json_manufacturer_n: Union[Unset, list[str]] = UNSET
    if not isinstance(manufacturer_n, Unset):
        json_manufacturer_n = manufacturer_n

    params["manufacturer__n"] = json_manufacturer_n

    json_manufacturer_id: Union[Unset, list[int]] = UNSET
    if not isinstance(manufacturer_id, Unset):
        json_manufacturer_id = manufacturer_id

    params["manufacturer_id"] = json_manufacturer_id

    json_manufacturer_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(manufacturer_id_n, Unset):
        json_manufacturer_id_n = manufacturer_id_n

    params["manufacturer_id__n"] = json_manufacturer_id_n

    json_modified_by_request: Union[Unset, str] = UNSET
    if not isinstance(modified_by_request, Unset):
        json_modified_by_request = str(modified_by_request)
    params["modified_by_request"] = json_modified_by_request

    json_module_bay_id: Union[Unset, list[str]] = UNSET
    if not isinstance(module_bay_id, Unset):
        json_module_bay_id = module_bay_id

    params["module_bay_id"] = json_module_bay_id

    json_module_bay_id_n: Union[Unset, list[str]] = UNSET
    if not isinstance(module_bay_id_n, Unset):
        json_module_bay_id_n = module_bay_id_n

    params["module_bay_id__n"] = json_module_bay_id_n

    json_module_type: Union[Unset, list[str]] = UNSET
    if not isinstance(module_type, Unset):
        json_module_type = module_type

    params["module_type"] = json_module_type

    json_module_type_n: Union[Unset, list[str]] = UNSET
    if not isinstance(module_type_n, Unset):
        json_module_type_n = module_type_n

    params["module_type__n"] = json_module_type_n

    json_module_type_id: Union[Unset, list[int]] = UNSET
    if not isinstance(module_type_id, Unset):
        json_module_type_id = module_type_id

    params["module_type_id"] = json_module_type_id

    json_module_type_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(module_type_id_n, Unset):
        json_module_type_id_n = module_type_id_n

    params["module_type_id__n"] = json_module_type_id_n

    params["offset"] = offset

    params["ordering"] = ordering

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

    json_serial: Union[Unset, list[str]] = UNSET
    if not isinstance(serial, Unset):
        json_serial = serial

    params["serial"] = json_serial

    params["serial__empty"] = serial_empty

    json_serial_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_ic, Unset):
        json_serial_ic = serial_ic

    params["serial__ic"] = json_serial_ic

    json_serial_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_ie, Unset):
        json_serial_ie = serial_ie

    params["serial__ie"] = json_serial_ie

    json_serial_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_iew, Unset):
        json_serial_iew = serial_iew

    params["serial__iew"] = json_serial_iew

    json_serial_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_isw, Unset):
        json_serial_isw = serial_isw

    params["serial__isw"] = json_serial_isw

    json_serial_n: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_n, Unset):
        json_serial_n = serial_n

    params["serial__n"] = json_serial_n

    json_serial_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_nic, Unset):
        json_serial_nic = serial_nic

    params["serial__nic"] = json_serial_nic

    json_serial_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_nie, Unset):
        json_serial_nie = serial_nie

    params["serial__nie"] = json_serial_nie

    json_serial_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_niew, Unset):
        json_serial_niew = serial_niew

    params["serial__niew"] = json_serial_niew

    json_serial_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_nisw, Unset):
        json_serial_nisw = serial_nisw

    params["serial__nisw"] = json_serial_nisw

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

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/dcim/modules/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedModuleList]:
    if response.status_code == 200:
        response_200 = PaginatedModuleList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedModuleList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    asset_tag: Union[Unset, list[str]] = UNSET,
    asset_tag_empty: Union[Unset, bool] = UNSET,
    asset_tag_ic: Union[Unset, list[str]] = UNSET,
    asset_tag_ie: Union[Unset, list[str]] = UNSET,
    asset_tag_iew: Union[Unset, list[str]] = UNSET,
    asset_tag_isw: Union[Unset, list[str]] = UNSET,
    asset_tag_n: Union[Unset, list[str]] = UNSET,
    asset_tag_nic: Union[Unset, list[str]] = UNSET,
    asset_tag_nie: Union[Unset, list[str]] = UNSET,
    asset_tag_niew: Union[Unset, list[str]] = UNSET,
    asset_tag_nisw: Union[Unset, list[str]] = UNSET,
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
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_bay_id: Union[Unset, list[str]] = UNSET,
    module_bay_id_n: Union[Unset, list[str]] = UNSET,
    module_type: Union[Unset, list[str]] = UNSET,
    module_type_n: Union[Unset, list[str]] = UNSET,
    module_type_id: Union[Unset, list[int]] = UNSET,
    module_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    serial: Union[Unset, list[str]] = UNSET,
    serial_empty: Union[Unset, bool] = UNSET,
    serial_ic: Union[Unset, list[str]] = UNSET,
    serial_ie: Union[Unset, list[str]] = UNSET,
    serial_iew: Union[Unset, list[str]] = UNSET,
    serial_isw: Union[Unset, list[str]] = UNSET,
    serial_n: Union[Unset, list[str]] = UNSET,
    serial_nic: Union[Unset, list[str]] = UNSET,
    serial_nie: Union[Unset, list[str]] = UNSET,
    serial_niew: Union[Unset, list[str]] = UNSET,
    serial_nisw: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedModuleList]:
    """Get a list of module objects.

    Args:
        asset_tag (Union[Unset, list[str]]):
        asset_tag_empty (Union[Unset, bool]):
        asset_tag_ic (Union[Unset, list[str]]):
        asset_tag_ie (Union[Unset, list[str]]):
        asset_tag_iew (Union[Unset, list[str]]):
        asset_tag_isw (Union[Unset, list[str]]):
        asset_tag_n (Union[Unset, list[str]]):
        asset_tag_nic (Union[Unset, list[str]]):
        asset_tag_nie (Union[Unset, list[str]]):
        asset_tag_niew (Union[Unset, list[str]]):
        asset_tag_nisw (Union[Unset, list[str]]):
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
        location_id (Union[Unset, list[int]]):
        location_id_n (Union[Unset, list[int]]):
        manufacturer (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_id (Union[Unset, list[int]]):
        manufacturer_id_n (Union[Unset, list[int]]):
        modified_by_request (Union[Unset, UUID]):
        module_bay_id (Union[Unset, list[str]]):
        module_bay_id_n (Union[Unset, list[str]]):
        module_type (Union[Unset, list[str]]):
        module_type_n (Union[Unset, list[str]]):
        module_type_id (Union[Unset, list[int]]):
        module_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_n (Union[Unset, list[str]]):
        rack_id (Union[Unset, list[int]]):
        rack_id_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        serial (Union[Unset, list[str]]):
        serial_empty (Union[Unset, bool]):
        serial_ic (Union[Unset, list[str]]):
        serial_ie (Union[Unset, list[str]]):
        serial_iew (Union[Unset, list[str]]):
        serial_isw (Union[Unset, list[str]]):
        serial_n (Union[Unset, list[str]]):
        serial_nic (Union[Unset, list[str]]):
        serial_nie (Union[Unset, list[str]]):
        serial_niew (Union[Unset, list[str]]):
        serial_nisw (Union[Unset, list[str]]):
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
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedModuleList]
    """

    kwargs = _get_kwargs(
        asset_tag=asset_tag,
        asset_tag_empty=asset_tag_empty,
        asset_tag_ic=asset_tag_ic,
        asset_tag_ie=asset_tag_ie,
        asset_tag_iew=asset_tag_iew,
        asset_tag_isw=asset_tag_isw,
        asset_tag_n=asset_tag_n,
        asset_tag_nic=asset_tag_nic,
        asset_tag_nie=asset_tag_nie,
        asset_tag_niew=asset_tag_niew,
        asset_tag_nisw=asset_tag_nisw,
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
        manufacturer=manufacturer,
        manufacturer_n=manufacturer_n,
        manufacturer_id=manufacturer_id,
        manufacturer_id_n=manufacturer_id_n,
        modified_by_request=modified_by_request,
        module_bay_id=module_bay_id,
        module_bay_id_n=module_bay_id_n,
        module_type=module_type,
        module_type_n=module_type_n,
        module_type_id=module_type_id,
        module_type_id_n=module_type_id_n,
        offset=offset,
        ordering=ordering,
        q=q,
        rack=rack,
        rack_n=rack_n,
        rack_id=rack_id,
        rack_id_n=rack_id_n,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        serial=serial,
        serial_empty=serial_empty,
        serial_ic=serial_ic,
        serial_ie=serial_ie,
        serial_iew=serial_iew,
        serial_isw=serial_isw,
        serial_n=serial_n,
        serial_nic=serial_nic,
        serial_nie=serial_nie,
        serial_niew=serial_niew,
        serial_nisw=serial_nisw,
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
        updated_by_request=updated_by_request,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    asset_tag: Union[Unset, list[str]] = UNSET,
    asset_tag_empty: Union[Unset, bool] = UNSET,
    asset_tag_ic: Union[Unset, list[str]] = UNSET,
    asset_tag_ie: Union[Unset, list[str]] = UNSET,
    asset_tag_iew: Union[Unset, list[str]] = UNSET,
    asset_tag_isw: Union[Unset, list[str]] = UNSET,
    asset_tag_n: Union[Unset, list[str]] = UNSET,
    asset_tag_nic: Union[Unset, list[str]] = UNSET,
    asset_tag_nie: Union[Unset, list[str]] = UNSET,
    asset_tag_niew: Union[Unset, list[str]] = UNSET,
    asset_tag_nisw: Union[Unset, list[str]] = UNSET,
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
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_bay_id: Union[Unset, list[str]] = UNSET,
    module_bay_id_n: Union[Unset, list[str]] = UNSET,
    module_type: Union[Unset, list[str]] = UNSET,
    module_type_n: Union[Unset, list[str]] = UNSET,
    module_type_id: Union[Unset, list[int]] = UNSET,
    module_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    serial: Union[Unset, list[str]] = UNSET,
    serial_empty: Union[Unset, bool] = UNSET,
    serial_ic: Union[Unset, list[str]] = UNSET,
    serial_ie: Union[Unset, list[str]] = UNSET,
    serial_iew: Union[Unset, list[str]] = UNSET,
    serial_isw: Union[Unset, list[str]] = UNSET,
    serial_n: Union[Unset, list[str]] = UNSET,
    serial_nic: Union[Unset, list[str]] = UNSET,
    serial_nie: Union[Unset, list[str]] = UNSET,
    serial_niew: Union[Unset, list[str]] = UNSET,
    serial_nisw: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedModuleList]:
    """Get a list of module objects.

    Args:
        asset_tag (Union[Unset, list[str]]):
        asset_tag_empty (Union[Unset, bool]):
        asset_tag_ic (Union[Unset, list[str]]):
        asset_tag_ie (Union[Unset, list[str]]):
        asset_tag_iew (Union[Unset, list[str]]):
        asset_tag_isw (Union[Unset, list[str]]):
        asset_tag_n (Union[Unset, list[str]]):
        asset_tag_nic (Union[Unset, list[str]]):
        asset_tag_nie (Union[Unset, list[str]]):
        asset_tag_niew (Union[Unset, list[str]]):
        asset_tag_nisw (Union[Unset, list[str]]):
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
        location_id (Union[Unset, list[int]]):
        location_id_n (Union[Unset, list[int]]):
        manufacturer (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_id (Union[Unset, list[int]]):
        manufacturer_id_n (Union[Unset, list[int]]):
        modified_by_request (Union[Unset, UUID]):
        module_bay_id (Union[Unset, list[str]]):
        module_bay_id_n (Union[Unset, list[str]]):
        module_type (Union[Unset, list[str]]):
        module_type_n (Union[Unset, list[str]]):
        module_type_id (Union[Unset, list[int]]):
        module_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_n (Union[Unset, list[str]]):
        rack_id (Union[Unset, list[int]]):
        rack_id_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        serial (Union[Unset, list[str]]):
        serial_empty (Union[Unset, bool]):
        serial_ic (Union[Unset, list[str]]):
        serial_ie (Union[Unset, list[str]]):
        serial_iew (Union[Unset, list[str]]):
        serial_isw (Union[Unset, list[str]]):
        serial_n (Union[Unset, list[str]]):
        serial_nic (Union[Unset, list[str]]):
        serial_nie (Union[Unset, list[str]]):
        serial_niew (Union[Unset, list[str]]):
        serial_nisw (Union[Unset, list[str]]):
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
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedModuleList
    """

    return sync_detailed(
        client=client,
        asset_tag=asset_tag,
        asset_tag_empty=asset_tag_empty,
        asset_tag_ic=asset_tag_ic,
        asset_tag_ie=asset_tag_ie,
        asset_tag_iew=asset_tag_iew,
        asset_tag_isw=asset_tag_isw,
        asset_tag_n=asset_tag_n,
        asset_tag_nic=asset_tag_nic,
        asset_tag_nie=asset_tag_nie,
        asset_tag_niew=asset_tag_niew,
        asset_tag_nisw=asset_tag_nisw,
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
        manufacturer=manufacturer,
        manufacturer_n=manufacturer_n,
        manufacturer_id=manufacturer_id,
        manufacturer_id_n=manufacturer_id_n,
        modified_by_request=modified_by_request,
        module_bay_id=module_bay_id,
        module_bay_id_n=module_bay_id_n,
        module_type=module_type,
        module_type_n=module_type_n,
        module_type_id=module_type_id,
        module_type_id_n=module_type_id_n,
        offset=offset,
        ordering=ordering,
        q=q,
        rack=rack,
        rack_n=rack_n,
        rack_id=rack_id,
        rack_id_n=rack_id_n,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        serial=serial,
        serial_empty=serial_empty,
        serial_ic=serial_ic,
        serial_ie=serial_ie,
        serial_iew=serial_iew,
        serial_isw=serial_isw,
        serial_n=serial_n,
        serial_nic=serial_nic,
        serial_nie=serial_nie,
        serial_niew=serial_niew,
        serial_nisw=serial_nisw,
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
        updated_by_request=updated_by_request,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    asset_tag: Union[Unset, list[str]] = UNSET,
    asset_tag_empty: Union[Unset, bool] = UNSET,
    asset_tag_ic: Union[Unset, list[str]] = UNSET,
    asset_tag_ie: Union[Unset, list[str]] = UNSET,
    asset_tag_iew: Union[Unset, list[str]] = UNSET,
    asset_tag_isw: Union[Unset, list[str]] = UNSET,
    asset_tag_n: Union[Unset, list[str]] = UNSET,
    asset_tag_nic: Union[Unset, list[str]] = UNSET,
    asset_tag_nie: Union[Unset, list[str]] = UNSET,
    asset_tag_niew: Union[Unset, list[str]] = UNSET,
    asset_tag_nisw: Union[Unset, list[str]] = UNSET,
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
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_bay_id: Union[Unset, list[str]] = UNSET,
    module_bay_id_n: Union[Unset, list[str]] = UNSET,
    module_type: Union[Unset, list[str]] = UNSET,
    module_type_n: Union[Unset, list[str]] = UNSET,
    module_type_id: Union[Unset, list[int]] = UNSET,
    module_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    serial: Union[Unset, list[str]] = UNSET,
    serial_empty: Union[Unset, bool] = UNSET,
    serial_ic: Union[Unset, list[str]] = UNSET,
    serial_ie: Union[Unset, list[str]] = UNSET,
    serial_iew: Union[Unset, list[str]] = UNSET,
    serial_isw: Union[Unset, list[str]] = UNSET,
    serial_n: Union[Unset, list[str]] = UNSET,
    serial_nic: Union[Unset, list[str]] = UNSET,
    serial_nie: Union[Unset, list[str]] = UNSET,
    serial_niew: Union[Unset, list[str]] = UNSET,
    serial_nisw: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedModuleList]:
    """Get a list of module objects.

    Args:
        asset_tag (Union[Unset, list[str]]):
        asset_tag_empty (Union[Unset, bool]):
        asset_tag_ic (Union[Unset, list[str]]):
        asset_tag_ie (Union[Unset, list[str]]):
        asset_tag_iew (Union[Unset, list[str]]):
        asset_tag_isw (Union[Unset, list[str]]):
        asset_tag_n (Union[Unset, list[str]]):
        asset_tag_nic (Union[Unset, list[str]]):
        asset_tag_nie (Union[Unset, list[str]]):
        asset_tag_niew (Union[Unset, list[str]]):
        asset_tag_nisw (Union[Unset, list[str]]):
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
        location_id (Union[Unset, list[int]]):
        location_id_n (Union[Unset, list[int]]):
        manufacturer (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_id (Union[Unset, list[int]]):
        manufacturer_id_n (Union[Unset, list[int]]):
        modified_by_request (Union[Unset, UUID]):
        module_bay_id (Union[Unset, list[str]]):
        module_bay_id_n (Union[Unset, list[str]]):
        module_type (Union[Unset, list[str]]):
        module_type_n (Union[Unset, list[str]]):
        module_type_id (Union[Unset, list[int]]):
        module_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_n (Union[Unset, list[str]]):
        rack_id (Union[Unset, list[int]]):
        rack_id_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        serial (Union[Unset, list[str]]):
        serial_empty (Union[Unset, bool]):
        serial_ic (Union[Unset, list[str]]):
        serial_ie (Union[Unset, list[str]]):
        serial_iew (Union[Unset, list[str]]):
        serial_isw (Union[Unset, list[str]]):
        serial_n (Union[Unset, list[str]]):
        serial_nic (Union[Unset, list[str]]):
        serial_nie (Union[Unset, list[str]]):
        serial_niew (Union[Unset, list[str]]):
        serial_nisw (Union[Unset, list[str]]):
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
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedModuleList]
    """

    kwargs = _get_kwargs(
        asset_tag=asset_tag,
        asset_tag_empty=asset_tag_empty,
        asset_tag_ic=asset_tag_ic,
        asset_tag_ie=asset_tag_ie,
        asset_tag_iew=asset_tag_iew,
        asset_tag_isw=asset_tag_isw,
        asset_tag_n=asset_tag_n,
        asset_tag_nic=asset_tag_nic,
        asset_tag_nie=asset_tag_nie,
        asset_tag_niew=asset_tag_niew,
        asset_tag_nisw=asset_tag_nisw,
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
        manufacturer=manufacturer,
        manufacturer_n=manufacturer_n,
        manufacturer_id=manufacturer_id,
        manufacturer_id_n=manufacturer_id_n,
        modified_by_request=modified_by_request,
        module_bay_id=module_bay_id,
        module_bay_id_n=module_bay_id_n,
        module_type=module_type,
        module_type_n=module_type_n,
        module_type_id=module_type_id,
        module_type_id_n=module_type_id_n,
        offset=offset,
        ordering=ordering,
        q=q,
        rack=rack,
        rack_n=rack_n,
        rack_id=rack_id,
        rack_id_n=rack_id_n,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        serial=serial,
        serial_empty=serial_empty,
        serial_ic=serial_ic,
        serial_ie=serial_ie,
        serial_iew=serial_iew,
        serial_isw=serial_isw,
        serial_n=serial_n,
        serial_nic=serial_nic,
        serial_nie=serial_nie,
        serial_niew=serial_niew,
        serial_nisw=serial_nisw,
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
        updated_by_request=updated_by_request,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    asset_tag: Union[Unset, list[str]] = UNSET,
    asset_tag_empty: Union[Unset, bool] = UNSET,
    asset_tag_ic: Union[Unset, list[str]] = UNSET,
    asset_tag_ie: Union[Unset, list[str]] = UNSET,
    asset_tag_iew: Union[Unset, list[str]] = UNSET,
    asset_tag_isw: Union[Unset, list[str]] = UNSET,
    asset_tag_n: Union[Unset, list[str]] = UNSET,
    asset_tag_nic: Union[Unset, list[str]] = UNSET,
    asset_tag_nie: Union[Unset, list[str]] = UNSET,
    asset_tag_niew: Union[Unset, list[str]] = UNSET,
    asset_tag_nisw: Union[Unset, list[str]] = UNSET,
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
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_bay_id: Union[Unset, list[str]] = UNSET,
    module_bay_id_n: Union[Unset, list[str]] = UNSET,
    module_type: Union[Unset, list[str]] = UNSET,
    module_type_n: Union[Unset, list[str]] = UNSET,
    module_type_id: Union[Unset, list[int]] = UNSET,
    module_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
    rack_id: Union[Unset, list[int]] = UNSET,
    rack_id_n: Union[Unset, list[int]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    serial: Union[Unset, list[str]] = UNSET,
    serial_empty: Union[Unset, bool] = UNSET,
    serial_ic: Union[Unset, list[str]] = UNSET,
    serial_ie: Union[Unset, list[str]] = UNSET,
    serial_iew: Union[Unset, list[str]] = UNSET,
    serial_isw: Union[Unset, list[str]] = UNSET,
    serial_n: Union[Unset, list[str]] = UNSET,
    serial_nic: Union[Unset, list[str]] = UNSET,
    serial_nie: Union[Unset, list[str]] = UNSET,
    serial_niew: Union[Unset, list[str]] = UNSET,
    serial_nisw: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedModuleList]:
    """Get a list of module objects.

    Args:
        asset_tag (Union[Unset, list[str]]):
        asset_tag_empty (Union[Unset, bool]):
        asset_tag_ic (Union[Unset, list[str]]):
        asset_tag_ie (Union[Unset, list[str]]):
        asset_tag_iew (Union[Unset, list[str]]):
        asset_tag_isw (Union[Unset, list[str]]):
        asset_tag_n (Union[Unset, list[str]]):
        asset_tag_nic (Union[Unset, list[str]]):
        asset_tag_nie (Union[Unset, list[str]]):
        asset_tag_niew (Union[Unset, list[str]]):
        asset_tag_nisw (Union[Unset, list[str]]):
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
        location_id (Union[Unset, list[int]]):
        location_id_n (Union[Unset, list[int]]):
        manufacturer (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_id (Union[Unset, list[int]]):
        manufacturer_id_n (Union[Unset, list[int]]):
        modified_by_request (Union[Unset, UUID]):
        module_bay_id (Union[Unset, list[str]]):
        module_bay_id_n (Union[Unset, list[str]]):
        module_type (Union[Unset, list[str]]):
        module_type_n (Union[Unset, list[str]]):
        module_type_id (Union[Unset, list[int]]):
        module_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_n (Union[Unset, list[str]]):
        rack_id (Union[Unset, list[int]]):
        rack_id_n (Union[Unset, list[int]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        serial (Union[Unset, list[str]]):
        serial_empty (Union[Unset, bool]):
        serial_ic (Union[Unset, list[str]]):
        serial_ie (Union[Unset, list[str]]):
        serial_iew (Union[Unset, list[str]]):
        serial_isw (Union[Unset, list[str]]):
        serial_n (Union[Unset, list[str]]):
        serial_nic (Union[Unset, list[str]]):
        serial_nie (Union[Unset, list[str]]):
        serial_niew (Union[Unset, list[str]]):
        serial_nisw (Union[Unset, list[str]]):
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
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedModuleList
    """

    return (
        await asyncio_detailed(
            client=client,
            asset_tag=asset_tag,
            asset_tag_empty=asset_tag_empty,
            asset_tag_ic=asset_tag_ic,
            asset_tag_ie=asset_tag_ie,
            asset_tag_iew=asset_tag_iew,
            asset_tag_isw=asset_tag_isw,
            asset_tag_n=asset_tag_n,
            asset_tag_nic=asset_tag_nic,
            asset_tag_nie=asset_tag_nie,
            asset_tag_niew=asset_tag_niew,
            asset_tag_nisw=asset_tag_nisw,
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
            manufacturer=manufacturer,
            manufacturer_n=manufacturer_n,
            manufacturer_id=manufacturer_id,
            manufacturer_id_n=manufacturer_id_n,
            modified_by_request=modified_by_request,
            module_bay_id=module_bay_id,
            module_bay_id_n=module_bay_id_n,
            module_type=module_type,
            module_type_n=module_type_n,
            module_type_id=module_type_id,
            module_type_id_n=module_type_id_n,
            offset=offset,
            ordering=ordering,
            q=q,
            rack=rack,
            rack_n=rack_n,
            rack_id=rack_id,
            rack_id_n=rack_id_n,
            region=region,
            region_n=region_n,
            region_id=region_id,
            region_id_n=region_id_n,
            serial=serial,
            serial_empty=serial_empty,
            serial_ic=serial_ic,
            serial_ie=serial_ie,
            serial_iew=serial_iew,
            serial_isw=serial_isw,
            serial_n=serial_n,
            serial_nic=serial_nic,
            serial_nie=serial_nie,
            serial_niew=serial_niew,
            serial_nisw=serial_nisw,
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
            updated_by_request=updated_by_request,
        )
    ).parsed
