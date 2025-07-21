import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_inventory_item_template_list import (
    PaginatedInventoryItemTemplateList,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    component_id: Union[Unset, list[int]] = UNSET,
    component_id_empty: Union[Unset, list[int]] = UNSET,
    component_id_gt: Union[Unset, list[int]] = UNSET,
    component_id_gte: Union[Unset, list[int]] = UNSET,
    component_id_lt: Union[Unset, list[int]] = UNSET,
    component_id_lte: Union[Unset, list[int]] = UNSET,
    component_id_n: Union[Unset, list[int]] = UNSET,
    component_type: Union[Unset, str] = UNSET,
    component_type_n: Union[Unset, str] = UNSET,
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
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
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
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[Union[None, int]]] = UNSET,
    manufacturer_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
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
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, list[Union[None, int]]] = UNSET,
    parent_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    part_id: Union[Unset, list[str]] = UNSET,
    part_id_empty: Union[Unset, bool] = UNSET,
    part_id_ic: Union[Unset, list[str]] = UNSET,
    part_id_ie: Union[Unset, list[str]] = UNSET,
    part_id_iew: Union[Unset, list[str]] = UNSET,
    part_id_isw: Union[Unset, list[str]] = UNSET,
    part_id_n: Union[Unset, list[str]] = UNSET,
    part_id_nic: Union[Unset, list[str]] = UNSET,
    part_id_nie: Union[Unset, list[str]] = UNSET,
    part_id_niew: Union[Unset, list[str]] = UNSET,
    part_id_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_component_id: Union[Unset, list[int]] = UNSET
    if not isinstance(component_id, Unset):
        json_component_id = component_id

    params["component_id"] = json_component_id

    json_component_id_empty: Union[Unset, list[int]] = UNSET
    if not isinstance(component_id_empty, Unset):
        json_component_id_empty = component_id_empty

    params["component_id__empty"] = json_component_id_empty

    json_component_id_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(component_id_gt, Unset):
        json_component_id_gt = component_id_gt

    params["component_id__gt"] = json_component_id_gt

    json_component_id_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(component_id_gte, Unset):
        json_component_id_gte = component_id_gte

    params["component_id__gte"] = json_component_id_gte

    json_component_id_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(component_id_lt, Unset):
        json_component_id_lt = component_id_lt

    params["component_id__lt"] = json_component_id_lt

    json_component_id_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(component_id_lte, Unset):
        json_component_id_lte = component_id_lte

    params["component_id__lte"] = json_component_id_lte

    json_component_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(component_id_n, Unset):
        json_component_id_n = component_id_n

    params["component_id__n"] = json_component_id_n

    params["component_type"] = component_type

    params["component_type__n"] = component_type_n

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

    json_device_type_id: Union[Unset, list[int]] = UNSET
    if not isinstance(device_type_id, Unset):
        json_device_type_id = device_type_id

    params["device_type_id"] = json_device_type_id

    json_device_type_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(device_type_id_n, Unset):
        json_device_type_id_n = device_type_id_n

    params["device_type_id__n"] = json_device_type_id_n

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

    json_manufacturer: Union[Unset, list[str]] = UNSET
    if not isinstance(manufacturer, Unset):
        json_manufacturer = manufacturer

    params["manufacturer"] = json_manufacturer

    json_manufacturer_n: Union[Unset, list[str]] = UNSET
    if not isinstance(manufacturer_n, Unset):
        json_manufacturer_n = manufacturer_n

    params["manufacturer__n"] = json_manufacturer_n

    json_manufacturer_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(manufacturer_id, Unset):
        json_manufacturer_id = []
        for manufacturer_id_item_data in manufacturer_id:
            manufacturer_id_item: Union[None, int]
            manufacturer_id_item = manufacturer_id_item_data
            json_manufacturer_id.append(manufacturer_id_item)

    params["manufacturer_id"] = json_manufacturer_id

    json_manufacturer_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(manufacturer_id_n, Unset):
        json_manufacturer_id_n = []
        for manufacturer_id_n_item_data in manufacturer_id_n:
            manufacturer_id_n_item: Union[None, int]
            manufacturer_id_n_item = manufacturer_id_n_item_data
            json_manufacturer_id_n.append(manufacturer_id_n_item)

    params["manufacturer_id__n"] = json_manufacturer_id_n

    json_modified_by_request: Union[Unset, str] = UNSET
    if not isinstance(modified_by_request, Unset):
        json_modified_by_request = str(modified_by_request)
    params["modified_by_request"] = json_modified_by_request

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

    params["offset"] = offset

    params["ordering"] = ordering

    json_parent_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(parent_id, Unset):
        json_parent_id = []
        for parent_id_item_data in parent_id:
            parent_id_item: Union[None, int]
            parent_id_item = parent_id_item_data
            json_parent_id.append(parent_id_item)

    params["parent_id"] = json_parent_id

    json_parent_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(parent_id_n, Unset):
        json_parent_id_n = []
        for parent_id_n_item_data in parent_id_n:
            parent_id_n_item: Union[None, int]
            parent_id_n_item = parent_id_n_item_data
            json_parent_id_n.append(parent_id_n_item)

    params["parent_id__n"] = json_parent_id_n

    json_part_id: Union[Unset, list[str]] = UNSET
    if not isinstance(part_id, Unset):
        json_part_id = part_id

    params["part_id"] = json_part_id

    params["part_id__empty"] = part_id_empty

    json_part_id_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(part_id_ic, Unset):
        json_part_id_ic = part_id_ic

    params["part_id__ic"] = json_part_id_ic

    json_part_id_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(part_id_ie, Unset):
        json_part_id_ie = part_id_ie

    params["part_id__ie"] = json_part_id_ie

    json_part_id_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(part_id_iew, Unset):
        json_part_id_iew = part_id_iew

    params["part_id__iew"] = json_part_id_iew

    json_part_id_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(part_id_isw, Unset):
        json_part_id_isw = part_id_isw

    params["part_id__isw"] = json_part_id_isw

    json_part_id_n: Union[Unset, list[str]] = UNSET
    if not isinstance(part_id_n, Unset):
        json_part_id_n = part_id_n

    params["part_id__n"] = json_part_id_n

    json_part_id_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(part_id_nic, Unset):
        json_part_id_nic = part_id_nic

    params["part_id__nic"] = json_part_id_nic

    json_part_id_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(part_id_nie, Unset):
        json_part_id_nie = part_id_nie

    params["part_id__nie"] = json_part_id_nie

    json_part_id_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(part_id_niew, Unset):
        json_part_id_niew = part_id_niew

    params["part_id__niew"] = json_part_id_niew

    json_part_id_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(part_id_nisw, Unset):
        json_part_id_nisw = part_id_nisw

    params["part_id__nisw"] = json_part_id_nisw

    params["q"] = q

    json_role: Union[Unset, list[str]] = UNSET
    if not isinstance(role, Unset):
        json_role = role

    params["role"] = json_role

    json_role_n: Union[Unset, list[str]] = UNSET
    if not isinstance(role_n, Unset):
        json_role_n = role_n

    params["role__n"] = json_role_n

    json_role_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(role_id, Unset):
        json_role_id = []
        for role_id_item_data in role_id:
            role_id_item: Union[None, int]
            role_id_item = role_id_item_data
            json_role_id.append(role_id_item)

    params["role_id"] = json_role_id

    json_role_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(role_id_n, Unset):
        json_role_id_n = []
        for role_id_n_item_data in role_id_n:
            role_id_n_item: Union[None, int]
            role_id_n_item = role_id_n_item_data
            json_role_id_n.append(role_id_n_item)

    params["role_id__n"] = json_role_id_n

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/dcim/inventory-item-templates/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedInventoryItemTemplateList]:
    if response.status_code == 200:
        response_200 = PaginatedInventoryItemTemplateList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedInventoryItemTemplateList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    component_id: Union[Unset, list[int]] = UNSET,
    component_id_empty: Union[Unset, list[int]] = UNSET,
    component_id_gt: Union[Unset, list[int]] = UNSET,
    component_id_gte: Union[Unset, list[int]] = UNSET,
    component_id_lt: Union[Unset, list[int]] = UNSET,
    component_id_lte: Union[Unset, list[int]] = UNSET,
    component_id_n: Union[Unset, list[int]] = UNSET,
    component_type: Union[Unset, str] = UNSET,
    component_type_n: Union[Unset, str] = UNSET,
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
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
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
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[Union[None, int]]] = UNSET,
    manufacturer_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
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
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, list[Union[None, int]]] = UNSET,
    parent_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    part_id: Union[Unset, list[str]] = UNSET,
    part_id_empty: Union[Unset, bool] = UNSET,
    part_id_ic: Union[Unset, list[str]] = UNSET,
    part_id_ie: Union[Unset, list[str]] = UNSET,
    part_id_iew: Union[Unset, list[str]] = UNSET,
    part_id_isw: Union[Unset, list[str]] = UNSET,
    part_id_n: Union[Unset, list[str]] = UNSET,
    part_id_nic: Union[Unset, list[str]] = UNSET,
    part_id_nie: Union[Unset, list[str]] = UNSET,
    part_id_niew: Union[Unset, list[str]] = UNSET,
    part_id_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedInventoryItemTemplateList]:
    """Get a list of inventory item template objects.

    Args:
        component_id (Union[Unset, list[int]]):
        component_id_empty (Union[Unset, list[int]]):
        component_id_gt (Union[Unset, list[int]]):
        component_id_gte (Union[Unset, list[int]]):
        component_id_lt (Union[Unset, list[int]]):
        component_id_lte (Union[Unset, list[int]]):
        component_id_n (Union[Unset, list[int]]):
        component_type (Union[Unset, str]):
        component_type_n (Union[Unset, str]):
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
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
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
        manufacturer (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_id (Union[Unset, list[Union[None, int]]]):
        manufacturer_id_n (Union[Unset, list[Union[None, int]]]):
        modified_by_request (Union[Unset, UUID]):
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
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        parent_id (Union[Unset, list[Union[None, int]]]):
        parent_id_n (Union[Unset, list[Union[None, int]]]):
        part_id (Union[Unset, list[str]]):
        part_id_empty (Union[Unset, bool]):
        part_id_ic (Union[Unset, list[str]]):
        part_id_ie (Union[Unset, list[str]]):
        part_id_iew (Union[Unset, list[str]]):
        part_id_isw (Union[Unset, list[str]]):
        part_id_n (Union[Unset, list[str]]):
        part_id_nic (Union[Unset, list[str]]):
        part_id_nie (Union[Unset, list[str]]):
        part_id_niew (Union[Unset, list[str]]):
        part_id_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[Union[None, int]]]):
        role_id_n (Union[Unset, list[Union[None, int]]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedInventoryItemTemplateList]
    """

    kwargs = _get_kwargs(
        component_id=component_id,
        component_id_empty=component_id_empty,
        component_id_gt=component_id_gt,
        component_id_gte=component_id_gte,
        component_id_lt=component_id_lt,
        component_id_lte=component_id_lte,
        component_id_n=component_id_n,
        component_type=component_type,
        component_type_n=component_type_n,
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
        device_type_id=device_type_id,
        device_type_id_n=device_type_id_n,
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
        manufacturer=manufacturer,
        manufacturer_n=manufacturer_n,
        manufacturer_id=manufacturer_id,
        manufacturer_id_n=manufacturer_id_n,
        modified_by_request=modified_by_request,
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
        offset=offset,
        ordering=ordering,
        parent_id=parent_id,
        parent_id_n=parent_id_n,
        part_id=part_id,
        part_id_empty=part_id_empty,
        part_id_ic=part_id_ic,
        part_id_ie=part_id_ie,
        part_id_iew=part_id_iew,
        part_id_isw=part_id_isw,
        part_id_n=part_id_n,
        part_id_nic=part_id_nic,
        part_id_nie=part_id_nie,
        part_id_niew=part_id_niew,
        part_id_nisw=part_id_nisw,
        q=q,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
        updated_by_request=updated_by_request,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    component_id: Union[Unset, list[int]] = UNSET,
    component_id_empty: Union[Unset, list[int]] = UNSET,
    component_id_gt: Union[Unset, list[int]] = UNSET,
    component_id_gte: Union[Unset, list[int]] = UNSET,
    component_id_lt: Union[Unset, list[int]] = UNSET,
    component_id_lte: Union[Unset, list[int]] = UNSET,
    component_id_n: Union[Unset, list[int]] = UNSET,
    component_type: Union[Unset, str] = UNSET,
    component_type_n: Union[Unset, str] = UNSET,
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
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
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
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[Union[None, int]]] = UNSET,
    manufacturer_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
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
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, list[Union[None, int]]] = UNSET,
    parent_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    part_id: Union[Unset, list[str]] = UNSET,
    part_id_empty: Union[Unset, bool] = UNSET,
    part_id_ic: Union[Unset, list[str]] = UNSET,
    part_id_ie: Union[Unset, list[str]] = UNSET,
    part_id_iew: Union[Unset, list[str]] = UNSET,
    part_id_isw: Union[Unset, list[str]] = UNSET,
    part_id_n: Union[Unset, list[str]] = UNSET,
    part_id_nic: Union[Unset, list[str]] = UNSET,
    part_id_nie: Union[Unset, list[str]] = UNSET,
    part_id_niew: Union[Unset, list[str]] = UNSET,
    part_id_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedInventoryItemTemplateList]:
    """Get a list of inventory item template objects.

    Args:
        component_id (Union[Unset, list[int]]):
        component_id_empty (Union[Unset, list[int]]):
        component_id_gt (Union[Unset, list[int]]):
        component_id_gte (Union[Unset, list[int]]):
        component_id_lt (Union[Unset, list[int]]):
        component_id_lte (Union[Unset, list[int]]):
        component_id_n (Union[Unset, list[int]]):
        component_type (Union[Unset, str]):
        component_type_n (Union[Unset, str]):
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
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
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
        manufacturer (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_id (Union[Unset, list[Union[None, int]]]):
        manufacturer_id_n (Union[Unset, list[Union[None, int]]]):
        modified_by_request (Union[Unset, UUID]):
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
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        parent_id (Union[Unset, list[Union[None, int]]]):
        parent_id_n (Union[Unset, list[Union[None, int]]]):
        part_id (Union[Unset, list[str]]):
        part_id_empty (Union[Unset, bool]):
        part_id_ic (Union[Unset, list[str]]):
        part_id_ie (Union[Unset, list[str]]):
        part_id_iew (Union[Unset, list[str]]):
        part_id_isw (Union[Unset, list[str]]):
        part_id_n (Union[Unset, list[str]]):
        part_id_nic (Union[Unset, list[str]]):
        part_id_nie (Union[Unset, list[str]]):
        part_id_niew (Union[Unset, list[str]]):
        part_id_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[Union[None, int]]]):
        role_id_n (Union[Unset, list[Union[None, int]]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedInventoryItemTemplateList
    """

    return sync_detailed(
        client=client,
        component_id=component_id,
        component_id_empty=component_id_empty,
        component_id_gt=component_id_gt,
        component_id_gte=component_id_gte,
        component_id_lt=component_id_lt,
        component_id_lte=component_id_lte,
        component_id_n=component_id_n,
        component_type=component_type,
        component_type_n=component_type_n,
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
        device_type_id=device_type_id,
        device_type_id_n=device_type_id_n,
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
        manufacturer=manufacturer,
        manufacturer_n=manufacturer_n,
        manufacturer_id=manufacturer_id,
        manufacturer_id_n=manufacturer_id_n,
        modified_by_request=modified_by_request,
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
        offset=offset,
        ordering=ordering,
        parent_id=parent_id,
        parent_id_n=parent_id_n,
        part_id=part_id,
        part_id_empty=part_id_empty,
        part_id_ic=part_id_ic,
        part_id_ie=part_id_ie,
        part_id_iew=part_id_iew,
        part_id_isw=part_id_isw,
        part_id_n=part_id_n,
        part_id_nic=part_id_nic,
        part_id_nie=part_id_nie,
        part_id_niew=part_id_niew,
        part_id_nisw=part_id_nisw,
        q=q,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
        updated_by_request=updated_by_request,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    component_id: Union[Unset, list[int]] = UNSET,
    component_id_empty: Union[Unset, list[int]] = UNSET,
    component_id_gt: Union[Unset, list[int]] = UNSET,
    component_id_gte: Union[Unset, list[int]] = UNSET,
    component_id_lt: Union[Unset, list[int]] = UNSET,
    component_id_lte: Union[Unset, list[int]] = UNSET,
    component_id_n: Union[Unset, list[int]] = UNSET,
    component_type: Union[Unset, str] = UNSET,
    component_type_n: Union[Unset, str] = UNSET,
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
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
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
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[Union[None, int]]] = UNSET,
    manufacturer_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
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
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, list[Union[None, int]]] = UNSET,
    parent_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    part_id: Union[Unset, list[str]] = UNSET,
    part_id_empty: Union[Unset, bool] = UNSET,
    part_id_ic: Union[Unset, list[str]] = UNSET,
    part_id_ie: Union[Unset, list[str]] = UNSET,
    part_id_iew: Union[Unset, list[str]] = UNSET,
    part_id_isw: Union[Unset, list[str]] = UNSET,
    part_id_n: Union[Unset, list[str]] = UNSET,
    part_id_nic: Union[Unset, list[str]] = UNSET,
    part_id_nie: Union[Unset, list[str]] = UNSET,
    part_id_niew: Union[Unset, list[str]] = UNSET,
    part_id_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedInventoryItemTemplateList]:
    """Get a list of inventory item template objects.

    Args:
        component_id (Union[Unset, list[int]]):
        component_id_empty (Union[Unset, list[int]]):
        component_id_gt (Union[Unset, list[int]]):
        component_id_gte (Union[Unset, list[int]]):
        component_id_lt (Union[Unset, list[int]]):
        component_id_lte (Union[Unset, list[int]]):
        component_id_n (Union[Unset, list[int]]):
        component_type (Union[Unset, str]):
        component_type_n (Union[Unset, str]):
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
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
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
        manufacturer (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_id (Union[Unset, list[Union[None, int]]]):
        manufacturer_id_n (Union[Unset, list[Union[None, int]]]):
        modified_by_request (Union[Unset, UUID]):
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
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        parent_id (Union[Unset, list[Union[None, int]]]):
        parent_id_n (Union[Unset, list[Union[None, int]]]):
        part_id (Union[Unset, list[str]]):
        part_id_empty (Union[Unset, bool]):
        part_id_ic (Union[Unset, list[str]]):
        part_id_ie (Union[Unset, list[str]]):
        part_id_iew (Union[Unset, list[str]]):
        part_id_isw (Union[Unset, list[str]]):
        part_id_n (Union[Unset, list[str]]):
        part_id_nic (Union[Unset, list[str]]):
        part_id_nie (Union[Unset, list[str]]):
        part_id_niew (Union[Unset, list[str]]):
        part_id_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[Union[None, int]]]):
        role_id_n (Union[Unset, list[Union[None, int]]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedInventoryItemTemplateList]
    """

    kwargs = _get_kwargs(
        component_id=component_id,
        component_id_empty=component_id_empty,
        component_id_gt=component_id_gt,
        component_id_gte=component_id_gte,
        component_id_lt=component_id_lt,
        component_id_lte=component_id_lte,
        component_id_n=component_id_n,
        component_type=component_type,
        component_type_n=component_type_n,
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
        device_type_id=device_type_id,
        device_type_id_n=device_type_id_n,
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
        manufacturer=manufacturer,
        manufacturer_n=manufacturer_n,
        manufacturer_id=manufacturer_id,
        manufacturer_id_n=manufacturer_id_n,
        modified_by_request=modified_by_request,
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
        offset=offset,
        ordering=ordering,
        parent_id=parent_id,
        parent_id_n=parent_id_n,
        part_id=part_id,
        part_id_empty=part_id_empty,
        part_id_ic=part_id_ic,
        part_id_ie=part_id_ie,
        part_id_iew=part_id_iew,
        part_id_isw=part_id_isw,
        part_id_n=part_id_n,
        part_id_nic=part_id_nic,
        part_id_nie=part_id_nie,
        part_id_niew=part_id_niew,
        part_id_nisw=part_id_nisw,
        q=q,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
        updated_by_request=updated_by_request,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    component_id: Union[Unset, list[int]] = UNSET,
    component_id_empty: Union[Unset, list[int]] = UNSET,
    component_id_gt: Union[Unset, list[int]] = UNSET,
    component_id_gte: Union[Unset, list[int]] = UNSET,
    component_id_lt: Union[Unset, list[int]] = UNSET,
    component_id_lte: Union[Unset, list[int]] = UNSET,
    component_id_n: Union[Unset, list[int]] = UNSET,
    component_type: Union[Unset, str] = UNSET,
    component_type_n: Union[Unset, str] = UNSET,
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
    device_type_id: Union[Unset, list[int]] = UNSET,
    device_type_id_n: Union[Unset, list[int]] = UNSET,
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
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[Union[None, int]]] = UNSET,
    manufacturer_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
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
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    parent_id: Union[Unset, list[Union[None, int]]] = UNSET,
    parent_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    part_id: Union[Unset, list[str]] = UNSET,
    part_id_empty: Union[Unset, bool] = UNSET,
    part_id_ic: Union[Unset, list[str]] = UNSET,
    part_id_ie: Union[Unset, list[str]] = UNSET,
    part_id_iew: Union[Unset, list[str]] = UNSET,
    part_id_isw: Union[Unset, list[str]] = UNSET,
    part_id_n: Union[Unset, list[str]] = UNSET,
    part_id_nic: Union[Unset, list[str]] = UNSET,
    part_id_nie: Union[Unset, list[str]] = UNSET,
    part_id_niew: Union[Unset, list[str]] = UNSET,
    part_id_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedInventoryItemTemplateList]:
    """Get a list of inventory item template objects.

    Args:
        component_id (Union[Unset, list[int]]):
        component_id_empty (Union[Unset, list[int]]):
        component_id_gt (Union[Unset, list[int]]):
        component_id_gte (Union[Unset, list[int]]):
        component_id_lt (Union[Unset, list[int]]):
        component_id_lte (Union[Unset, list[int]]):
        component_id_n (Union[Unset, list[int]]):
        component_type (Union[Unset, str]):
        component_type_n (Union[Unset, str]):
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
        device_type_id (Union[Unset, list[int]]):
        device_type_id_n (Union[Unset, list[int]]):
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
        manufacturer (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_id (Union[Unset, list[Union[None, int]]]):
        manufacturer_id_n (Union[Unset, list[Union[None, int]]]):
        modified_by_request (Union[Unset, UUID]):
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
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        parent_id (Union[Unset, list[Union[None, int]]]):
        parent_id_n (Union[Unset, list[Union[None, int]]]):
        part_id (Union[Unset, list[str]]):
        part_id_empty (Union[Unset, bool]):
        part_id_ic (Union[Unset, list[str]]):
        part_id_ie (Union[Unset, list[str]]):
        part_id_iew (Union[Unset, list[str]]):
        part_id_isw (Union[Unset, list[str]]):
        part_id_n (Union[Unset, list[str]]):
        part_id_nic (Union[Unset, list[str]]):
        part_id_nie (Union[Unset, list[str]]):
        part_id_niew (Union[Unset, list[str]]):
        part_id_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[Union[None, int]]]):
        role_id_n (Union[Unset, list[Union[None, int]]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedInventoryItemTemplateList
    """

    return (
        await asyncio_detailed(
            client=client,
            component_id=component_id,
            component_id_empty=component_id_empty,
            component_id_gt=component_id_gt,
            component_id_gte=component_id_gte,
            component_id_lt=component_id_lt,
            component_id_lte=component_id_lte,
            component_id_n=component_id_n,
            component_type=component_type,
            component_type_n=component_type_n,
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
            device_type_id=device_type_id,
            device_type_id_n=device_type_id_n,
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
            manufacturer=manufacturer,
            manufacturer_n=manufacturer_n,
            manufacturer_id=manufacturer_id,
            manufacturer_id_n=manufacturer_id_n,
            modified_by_request=modified_by_request,
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
            offset=offset,
            ordering=ordering,
            parent_id=parent_id,
            parent_id_n=parent_id_n,
            part_id=part_id,
            part_id_empty=part_id_empty,
            part_id_ic=part_id_ic,
            part_id_ie=part_id_ie,
            part_id_iew=part_id_iew,
            part_id_isw=part_id_isw,
            part_id_n=part_id_n,
            part_id_nic=part_id_nic,
            part_id_nie=part_id_nie,
            part_id_niew=part_id_niew,
            part_id_nisw=part_id_nisw,
            q=q,
            role=role,
            role_n=role_n,
            role_id=role_id,
            role_id_n=role_id_n,
            updated_by_request=updated_by_request,
        )
    ).parsed
