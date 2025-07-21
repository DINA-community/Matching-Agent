import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dcim_device_types_list_airflow import DcimDeviceTypesListAirflow
from ...models.dcim_device_types_list_parentchild_status import (
    DcimDeviceTypesListParentchildStatus,
)
from ...models.dcim_device_types_list_weight_unit import DcimDeviceTypesListWeightUnit
from ...models.paginated_device_type_list import PaginatedDeviceTypeList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    airflow: Union[Unset, DcimDeviceTypesListAirflow] = UNSET,
    console_port_template_count: Union[Unset, list[int]] = UNSET,
    console_port_template_count_empty: Union[Unset, bool] = UNSET,
    console_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    console_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    console_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    console_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    console_port_template_count_n: Union[Unset, list[int]] = UNSET,
    console_ports: Union[Unset, bool] = UNSET,
    console_server_port_template_count: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_empty: Union[Unset, bool] = UNSET,
    console_server_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_n: Union[Unset, list[int]] = UNSET,
    console_server_ports: Union[Unset, bool] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    default_platform: Union[Unset, list[str]] = UNSET,
    default_platform_n: Union[Unset, list[str]] = UNSET,
    default_platform_id: Union[Unset, list[Union[None, int]]] = UNSET,
    default_platform_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    device_bay_template_count: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_empty: Union[Unset, bool] = UNSET,
    device_bay_template_count_gt: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_gte: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_lt: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_lte: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_n: Union[Unset, list[int]] = UNSET,
    device_bays: Union[Unset, bool] = UNSET,
    exclude_from_utilization: Union[Unset, bool] = UNSET,
    front_port_template_count: Union[Unset, list[int]] = UNSET,
    front_port_template_count_empty: Union[Unset, bool] = UNSET,
    front_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    front_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    front_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    front_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    front_port_template_count_n: Union[Unset, list[int]] = UNSET,
    has_front_image: Union[Unset, bool] = UNSET,
    has_rear_image: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_template_count: Union[Unset, list[int]] = UNSET,
    interface_template_count_empty: Union[Unset, bool] = UNSET,
    interface_template_count_gt: Union[Unset, list[int]] = UNSET,
    interface_template_count_gte: Union[Unset, list[int]] = UNSET,
    interface_template_count_lt: Union[Unset, list[int]] = UNSET,
    interface_template_count_lte: Union[Unset, list[int]] = UNSET,
    interface_template_count_n: Union[Unset, list[int]] = UNSET,
    interfaces: Union[Unset, bool] = UNSET,
    inventory_item_template_count: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_empty: Union[Unset, bool] = UNSET,
    inventory_item_template_count_gt: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_gte: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_lt: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_lte: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_n: Union[Unset, list[int]] = UNSET,
    inventory_items: Union[Unset, bool] = UNSET,
    is_full_depth: Union[Unset, bool] = UNSET,
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
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    model: Union[Unset, list[str]] = UNSET,
    model_empty: Union[Unset, bool] = UNSET,
    model_ic: Union[Unset, list[str]] = UNSET,
    model_ie: Union[Unset, list[str]] = UNSET,
    model_iew: Union[Unset, list[str]] = UNSET,
    model_isw: Union[Unset, list[str]] = UNSET,
    model_n: Union[Unset, list[str]] = UNSET,
    model_nic: Union[Unset, list[str]] = UNSET,
    model_nie: Union[Unset, list[str]] = UNSET,
    model_niew: Union[Unset, list[str]] = UNSET,
    model_nisw: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_bay_template_count: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_empty: Union[Unset, bool] = UNSET,
    module_bay_template_count_gt: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_gte: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_lt: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_lte: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_n: Union[Unset, list[int]] = UNSET,
    module_bays: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    part_number: Union[Unset, list[str]] = UNSET,
    part_number_empty: Union[Unset, bool] = UNSET,
    part_number_ic: Union[Unset, list[str]] = UNSET,
    part_number_ie: Union[Unset, list[str]] = UNSET,
    part_number_iew: Union[Unset, list[str]] = UNSET,
    part_number_isw: Union[Unset, list[str]] = UNSET,
    part_number_n: Union[Unset, list[str]] = UNSET,
    part_number_nic: Union[Unset, list[str]] = UNSET,
    part_number_nie: Union[Unset, list[str]] = UNSET,
    part_number_niew: Union[Unset, list[str]] = UNSET,
    part_number_nisw: Union[Unset, list[str]] = UNSET,
    pass_through_ports: Union[Unset, bool] = UNSET,
    power_outlet_template_count: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_empty: Union[Unset, bool] = UNSET,
    power_outlet_template_count_gt: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_gte: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_lt: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_lte: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_n: Union[Unset, list[int]] = UNSET,
    power_outlets: Union[Unset, bool] = UNSET,
    power_port_template_count: Union[Unset, list[int]] = UNSET,
    power_port_template_count_empty: Union[Unset, bool] = UNSET,
    power_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    power_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    power_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    power_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    power_port_template_count_n: Union[Unset, list[int]] = UNSET,
    power_ports: Union[Unset, bool] = UNSET,
    q: Union[Unset, str] = UNSET,
    rear_port_template_count: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_empty: Union[Unset, bool] = UNSET,
    rear_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_n: Union[Unset, list[int]] = UNSET,
    slug: Union[Unset, list[str]] = UNSET,
    slug_empty: Union[Unset, bool] = UNSET,
    slug_ic: Union[Unset, list[str]] = UNSET,
    slug_ie: Union[Unset, list[str]] = UNSET,
    slug_iew: Union[Unset, list[str]] = UNSET,
    slug_isw: Union[Unset, list[str]] = UNSET,
    slug_n: Union[Unset, list[str]] = UNSET,
    slug_nic: Union[Unset, list[str]] = UNSET,
    slug_nie: Union[Unset, list[str]] = UNSET,
    slug_niew: Union[Unset, list[str]] = UNSET,
    slug_nisw: Union[Unset, list[str]] = UNSET,
    subdevice_role: Union[Unset, DcimDeviceTypesListParentchildStatus] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    u_height: Union[Unset, list[float]] = UNSET,
    u_height_empty: Union[Unset, bool] = UNSET,
    u_height_gt: Union[Unset, list[float]] = UNSET,
    u_height_gte: Union[Unset, list[float]] = UNSET,
    u_height_lt: Union[Unset, list[float]] = UNSET,
    u_height_lte: Union[Unset, list[float]] = UNSET,
    u_height_n: Union[Unset, list[float]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    weight: Union[Unset, list[float]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[float]] = UNSET,
    weight_gte: Union[Unset, list[float]] = UNSET,
    weight_lt: Union[Unset, list[float]] = UNSET,
    weight_lte: Union[Unset, list[float]] = UNSET,
    weight_n: Union[Unset, list[float]] = UNSET,
    weight_unit: Union[Unset, DcimDeviceTypesListWeightUnit] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_airflow: Union[Unset, str] = UNSET
    if not isinstance(airflow, Unset):
        json_airflow = airflow.value

    params["airflow"] = json_airflow

    json_console_port_template_count: Union[Unset, list[int]] = UNSET
    if not isinstance(console_port_template_count, Unset):
        json_console_port_template_count = console_port_template_count

    params["console_port_template_count"] = json_console_port_template_count

    params["console_port_template_count__empty"] = console_port_template_count_empty

    json_console_port_template_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(console_port_template_count_gt, Unset):
        json_console_port_template_count_gt = console_port_template_count_gt

    params["console_port_template_count__gt"] = json_console_port_template_count_gt

    json_console_port_template_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(console_port_template_count_gte, Unset):
        json_console_port_template_count_gte = console_port_template_count_gte

    params["console_port_template_count__gte"] = json_console_port_template_count_gte

    json_console_port_template_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(console_port_template_count_lt, Unset):
        json_console_port_template_count_lt = console_port_template_count_lt

    params["console_port_template_count__lt"] = json_console_port_template_count_lt

    json_console_port_template_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(console_port_template_count_lte, Unset):
        json_console_port_template_count_lte = console_port_template_count_lte

    params["console_port_template_count__lte"] = json_console_port_template_count_lte

    json_console_port_template_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(console_port_template_count_n, Unset):
        json_console_port_template_count_n = console_port_template_count_n

    params["console_port_template_count__n"] = json_console_port_template_count_n

    params["console_ports"] = console_ports

    json_console_server_port_template_count: Union[Unset, list[int]] = UNSET
    if not isinstance(console_server_port_template_count, Unset):
        json_console_server_port_template_count = console_server_port_template_count

    params["console_server_port_template_count"] = (
        json_console_server_port_template_count
    )

    params["console_server_port_template_count__empty"] = (
        console_server_port_template_count_empty
    )

    json_console_server_port_template_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(console_server_port_template_count_gt, Unset):
        json_console_server_port_template_count_gt = (
            console_server_port_template_count_gt
        )

    params["console_server_port_template_count__gt"] = (
        json_console_server_port_template_count_gt
    )

    json_console_server_port_template_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(console_server_port_template_count_gte, Unset):
        json_console_server_port_template_count_gte = (
            console_server_port_template_count_gte
        )

    params["console_server_port_template_count__gte"] = (
        json_console_server_port_template_count_gte
    )

    json_console_server_port_template_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(console_server_port_template_count_lt, Unset):
        json_console_server_port_template_count_lt = (
            console_server_port_template_count_lt
        )

    params["console_server_port_template_count__lt"] = (
        json_console_server_port_template_count_lt
    )

    json_console_server_port_template_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(console_server_port_template_count_lte, Unset):
        json_console_server_port_template_count_lte = (
            console_server_port_template_count_lte
        )

    params["console_server_port_template_count__lte"] = (
        json_console_server_port_template_count_lte
    )

    json_console_server_port_template_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(console_server_port_template_count_n, Unset):
        json_console_server_port_template_count_n = console_server_port_template_count_n

    params["console_server_port_template_count__n"] = (
        json_console_server_port_template_count_n
    )

    params["console_server_ports"] = console_server_ports

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

    json_default_platform: Union[Unset, list[str]] = UNSET
    if not isinstance(default_platform, Unset):
        json_default_platform = default_platform

    params["default_platform"] = json_default_platform

    json_default_platform_n: Union[Unset, list[str]] = UNSET
    if not isinstance(default_platform_n, Unset):
        json_default_platform_n = default_platform_n

    params["default_platform__n"] = json_default_platform_n

    json_default_platform_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(default_platform_id, Unset):
        json_default_platform_id = []
        for default_platform_id_item_data in default_platform_id:
            default_platform_id_item: Union[None, int]
            default_platform_id_item = default_platform_id_item_data
            json_default_platform_id.append(default_platform_id_item)

    params["default_platform_id"] = json_default_platform_id

    json_default_platform_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(default_platform_id_n, Unset):
        json_default_platform_id_n = []
        for default_platform_id_n_item_data in default_platform_id_n:
            default_platform_id_n_item: Union[None, int]
            default_platform_id_n_item = default_platform_id_n_item_data
            json_default_platform_id_n.append(default_platform_id_n_item)

    params["default_platform_id__n"] = json_default_platform_id_n

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

    json_device_bay_template_count: Union[Unset, list[int]] = UNSET
    if not isinstance(device_bay_template_count, Unset):
        json_device_bay_template_count = device_bay_template_count

    params["device_bay_template_count"] = json_device_bay_template_count

    params["device_bay_template_count__empty"] = device_bay_template_count_empty

    json_device_bay_template_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(device_bay_template_count_gt, Unset):
        json_device_bay_template_count_gt = device_bay_template_count_gt

    params["device_bay_template_count__gt"] = json_device_bay_template_count_gt

    json_device_bay_template_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(device_bay_template_count_gte, Unset):
        json_device_bay_template_count_gte = device_bay_template_count_gte

    params["device_bay_template_count__gte"] = json_device_bay_template_count_gte

    json_device_bay_template_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(device_bay_template_count_lt, Unset):
        json_device_bay_template_count_lt = device_bay_template_count_lt

    params["device_bay_template_count__lt"] = json_device_bay_template_count_lt

    json_device_bay_template_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(device_bay_template_count_lte, Unset):
        json_device_bay_template_count_lte = device_bay_template_count_lte

    params["device_bay_template_count__lte"] = json_device_bay_template_count_lte

    json_device_bay_template_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(device_bay_template_count_n, Unset):
        json_device_bay_template_count_n = device_bay_template_count_n

    params["device_bay_template_count__n"] = json_device_bay_template_count_n

    params["device_bays"] = device_bays

    params["exclude_from_utilization"] = exclude_from_utilization

    json_front_port_template_count: Union[Unset, list[int]] = UNSET
    if not isinstance(front_port_template_count, Unset):
        json_front_port_template_count = front_port_template_count

    params["front_port_template_count"] = json_front_port_template_count

    params["front_port_template_count__empty"] = front_port_template_count_empty

    json_front_port_template_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(front_port_template_count_gt, Unset):
        json_front_port_template_count_gt = front_port_template_count_gt

    params["front_port_template_count__gt"] = json_front_port_template_count_gt

    json_front_port_template_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(front_port_template_count_gte, Unset):
        json_front_port_template_count_gte = front_port_template_count_gte

    params["front_port_template_count__gte"] = json_front_port_template_count_gte

    json_front_port_template_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(front_port_template_count_lt, Unset):
        json_front_port_template_count_lt = front_port_template_count_lt

    params["front_port_template_count__lt"] = json_front_port_template_count_lt

    json_front_port_template_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(front_port_template_count_lte, Unset):
        json_front_port_template_count_lte = front_port_template_count_lte

    params["front_port_template_count__lte"] = json_front_port_template_count_lte

    json_front_port_template_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(front_port_template_count_n, Unset):
        json_front_port_template_count_n = front_port_template_count_n

    params["front_port_template_count__n"] = json_front_port_template_count_n

    params["has_front_image"] = has_front_image

    params["has_rear_image"] = has_rear_image

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

    json_interface_template_count: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_template_count, Unset):
        json_interface_template_count = interface_template_count

    params["interface_template_count"] = json_interface_template_count

    params["interface_template_count__empty"] = interface_template_count_empty

    json_interface_template_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_template_count_gt, Unset):
        json_interface_template_count_gt = interface_template_count_gt

    params["interface_template_count__gt"] = json_interface_template_count_gt

    json_interface_template_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_template_count_gte, Unset):
        json_interface_template_count_gte = interface_template_count_gte

    params["interface_template_count__gte"] = json_interface_template_count_gte

    json_interface_template_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_template_count_lt, Unset):
        json_interface_template_count_lt = interface_template_count_lt

    params["interface_template_count__lt"] = json_interface_template_count_lt

    json_interface_template_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_template_count_lte, Unset):
        json_interface_template_count_lte = interface_template_count_lte

    params["interface_template_count__lte"] = json_interface_template_count_lte

    json_interface_template_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_template_count_n, Unset):
        json_interface_template_count_n = interface_template_count_n

    params["interface_template_count__n"] = json_interface_template_count_n

    params["interfaces"] = interfaces

    json_inventory_item_template_count: Union[Unset, list[int]] = UNSET
    if not isinstance(inventory_item_template_count, Unset):
        json_inventory_item_template_count = inventory_item_template_count

    params["inventory_item_template_count"] = json_inventory_item_template_count

    params["inventory_item_template_count__empty"] = inventory_item_template_count_empty

    json_inventory_item_template_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(inventory_item_template_count_gt, Unset):
        json_inventory_item_template_count_gt = inventory_item_template_count_gt

    params["inventory_item_template_count__gt"] = json_inventory_item_template_count_gt

    json_inventory_item_template_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(inventory_item_template_count_gte, Unset):
        json_inventory_item_template_count_gte = inventory_item_template_count_gte

    params["inventory_item_template_count__gte"] = (
        json_inventory_item_template_count_gte
    )

    json_inventory_item_template_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(inventory_item_template_count_lt, Unset):
        json_inventory_item_template_count_lt = inventory_item_template_count_lt

    params["inventory_item_template_count__lt"] = json_inventory_item_template_count_lt

    json_inventory_item_template_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(inventory_item_template_count_lte, Unset):
        json_inventory_item_template_count_lte = inventory_item_template_count_lte

    params["inventory_item_template_count__lte"] = (
        json_inventory_item_template_count_lte
    )

    json_inventory_item_template_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(inventory_item_template_count_n, Unset):
        json_inventory_item_template_count_n = inventory_item_template_count_n

    params["inventory_item_template_count__n"] = json_inventory_item_template_count_n

    params["inventory_items"] = inventory_items

    params["is_full_depth"] = is_full_depth

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

    json_manufacturer_id: Union[Unset, list[int]] = UNSET
    if not isinstance(manufacturer_id, Unset):
        json_manufacturer_id = manufacturer_id

    params["manufacturer_id"] = json_manufacturer_id

    json_manufacturer_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(manufacturer_id_n, Unset):
        json_manufacturer_id_n = manufacturer_id_n

    params["manufacturer_id__n"] = json_manufacturer_id_n

    json_model: Union[Unset, list[str]] = UNSET
    if not isinstance(model, Unset):
        json_model = model

    params["model"] = json_model

    params["model__empty"] = model_empty

    json_model_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(model_ic, Unset):
        json_model_ic = model_ic

    params["model__ic"] = json_model_ic

    json_model_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(model_ie, Unset):
        json_model_ie = model_ie

    params["model__ie"] = json_model_ie

    json_model_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(model_iew, Unset):
        json_model_iew = model_iew

    params["model__iew"] = json_model_iew

    json_model_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(model_isw, Unset):
        json_model_isw = model_isw

    params["model__isw"] = json_model_isw

    json_model_n: Union[Unset, list[str]] = UNSET
    if not isinstance(model_n, Unset):
        json_model_n = model_n

    params["model__n"] = json_model_n

    json_model_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(model_nic, Unset):
        json_model_nic = model_nic

    params["model__nic"] = json_model_nic

    json_model_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(model_nie, Unset):
        json_model_nie = model_nie

    params["model__nie"] = json_model_nie

    json_model_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(model_niew, Unset):
        json_model_niew = model_niew

    params["model__niew"] = json_model_niew

    json_model_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(model_nisw, Unset):
        json_model_nisw = model_nisw

    params["model__nisw"] = json_model_nisw

    json_modified_by_request: Union[Unset, str] = UNSET
    if not isinstance(modified_by_request, Unset):
        json_modified_by_request = str(modified_by_request)
    params["modified_by_request"] = json_modified_by_request

    json_module_bay_template_count: Union[Unset, list[int]] = UNSET
    if not isinstance(module_bay_template_count, Unset):
        json_module_bay_template_count = module_bay_template_count

    params["module_bay_template_count"] = json_module_bay_template_count

    params["module_bay_template_count__empty"] = module_bay_template_count_empty

    json_module_bay_template_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(module_bay_template_count_gt, Unset):
        json_module_bay_template_count_gt = module_bay_template_count_gt

    params["module_bay_template_count__gt"] = json_module_bay_template_count_gt

    json_module_bay_template_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(module_bay_template_count_gte, Unset):
        json_module_bay_template_count_gte = module_bay_template_count_gte

    params["module_bay_template_count__gte"] = json_module_bay_template_count_gte

    json_module_bay_template_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(module_bay_template_count_lt, Unset):
        json_module_bay_template_count_lt = module_bay_template_count_lt

    params["module_bay_template_count__lt"] = json_module_bay_template_count_lt

    json_module_bay_template_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(module_bay_template_count_lte, Unset):
        json_module_bay_template_count_lte = module_bay_template_count_lte

    params["module_bay_template_count__lte"] = json_module_bay_template_count_lte

    json_module_bay_template_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(module_bay_template_count_n, Unset):
        json_module_bay_template_count_n = module_bay_template_count_n

    params["module_bay_template_count__n"] = json_module_bay_template_count_n

    params["module_bays"] = module_bays

    params["offset"] = offset

    params["ordering"] = ordering

    json_part_number: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number, Unset):
        json_part_number = part_number

    params["part_number"] = json_part_number

    params["part_number__empty"] = part_number_empty

    json_part_number_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number_ic, Unset):
        json_part_number_ic = part_number_ic

    params["part_number__ic"] = json_part_number_ic

    json_part_number_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number_ie, Unset):
        json_part_number_ie = part_number_ie

    params["part_number__ie"] = json_part_number_ie

    json_part_number_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number_iew, Unset):
        json_part_number_iew = part_number_iew

    params["part_number__iew"] = json_part_number_iew

    json_part_number_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number_isw, Unset):
        json_part_number_isw = part_number_isw

    params["part_number__isw"] = json_part_number_isw

    json_part_number_n: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number_n, Unset):
        json_part_number_n = part_number_n

    params["part_number__n"] = json_part_number_n

    json_part_number_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number_nic, Unset):
        json_part_number_nic = part_number_nic

    params["part_number__nic"] = json_part_number_nic

    json_part_number_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number_nie, Unset):
        json_part_number_nie = part_number_nie

    params["part_number__nie"] = json_part_number_nie

    json_part_number_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number_niew, Unset):
        json_part_number_niew = part_number_niew

    params["part_number__niew"] = json_part_number_niew

    json_part_number_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number_nisw, Unset):
        json_part_number_nisw = part_number_nisw

    params["part_number__nisw"] = json_part_number_nisw

    params["pass_through_ports"] = pass_through_ports

    json_power_outlet_template_count: Union[Unset, list[int]] = UNSET
    if not isinstance(power_outlet_template_count, Unset):
        json_power_outlet_template_count = power_outlet_template_count

    params["power_outlet_template_count"] = json_power_outlet_template_count

    params["power_outlet_template_count__empty"] = power_outlet_template_count_empty

    json_power_outlet_template_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(power_outlet_template_count_gt, Unset):
        json_power_outlet_template_count_gt = power_outlet_template_count_gt

    params["power_outlet_template_count__gt"] = json_power_outlet_template_count_gt

    json_power_outlet_template_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(power_outlet_template_count_gte, Unset):
        json_power_outlet_template_count_gte = power_outlet_template_count_gte

    params["power_outlet_template_count__gte"] = json_power_outlet_template_count_gte

    json_power_outlet_template_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(power_outlet_template_count_lt, Unset):
        json_power_outlet_template_count_lt = power_outlet_template_count_lt

    params["power_outlet_template_count__lt"] = json_power_outlet_template_count_lt

    json_power_outlet_template_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(power_outlet_template_count_lte, Unset):
        json_power_outlet_template_count_lte = power_outlet_template_count_lte

    params["power_outlet_template_count__lte"] = json_power_outlet_template_count_lte

    json_power_outlet_template_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(power_outlet_template_count_n, Unset):
        json_power_outlet_template_count_n = power_outlet_template_count_n

    params["power_outlet_template_count__n"] = json_power_outlet_template_count_n

    params["power_outlets"] = power_outlets

    json_power_port_template_count: Union[Unset, list[int]] = UNSET
    if not isinstance(power_port_template_count, Unset):
        json_power_port_template_count = power_port_template_count

    params["power_port_template_count"] = json_power_port_template_count

    params["power_port_template_count__empty"] = power_port_template_count_empty

    json_power_port_template_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(power_port_template_count_gt, Unset):
        json_power_port_template_count_gt = power_port_template_count_gt

    params["power_port_template_count__gt"] = json_power_port_template_count_gt

    json_power_port_template_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(power_port_template_count_gte, Unset):
        json_power_port_template_count_gte = power_port_template_count_gte

    params["power_port_template_count__gte"] = json_power_port_template_count_gte

    json_power_port_template_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(power_port_template_count_lt, Unset):
        json_power_port_template_count_lt = power_port_template_count_lt

    params["power_port_template_count__lt"] = json_power_port_template_count_lt

    json_power_port_template_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(power_port_template_count_lte, Unset):
        json_power_port_template_count_lte = power_port_template_count_lte

    params["power_port_template_count__lte"] = json_power_port_template_count_lte

    json_power_port_template_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(power_port_template_count_n, Unset):
        json_power_port_template_count_n = power_port_template_count_n

    params["power_port_template_count__n"] = json_power_port_template_count_n

    params["power_ports"] = power_ports

    params["q"] = q

    json_rear_port_template_count: Union[Unset, list[int]] = UNSET
    if not isinstance(rear_port_template_count, Unset):
        json_rear_port_template_count = rear_port_template_count

    params["rear_port_template_count"] = json_rear_port_template_count

    params["rear_port_template_count__empty"] = rear_port_template_count_empty

    json_rear_port_template_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(rear_port_template_count_gt, Unset):
        json_rear_port_template_count_gt = rear_port_template_count_gt

    params["rear_port_template_count__gt"] = json_rear_port_template_count_gt

    json_rear_port_template_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(rear_port_template_count_gte, Unset):
        json_rear_port_template_count_gte = rear_port_template_count_gte

    params["rear_port_template_count__gte"] = json_rear_port_template_count_gte

    json_rear_port_template_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(rear_port_template_count_lt, Unset):
        json_rear_port_template_count_lt = rear_port_template_count_lt

    params["rear_port_template_count__lt"] = json_rear_port_template_count_lt

    json_rear_port_template_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(rear_port_template_count_lte, Unset):
        json_rear_port_template_count_lte = rear_port_template_count_lte

    params["rear_port_template_count__lte"] = json_rear_port_template_count_lte

    json_rear_port_template_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(rear_port_template_count_n, Unset):
        json_rear_port_template_count_n = rear_port_template_count_n

    params["rear_port_template_count__n"] = json_rear_port_template_count_n

    json_slug: Union[Unset, list[str]] = UNSET
    if not isinstance(slug, Unset):
        json_slug = slug

    params["slug"] = json_slug

    params["slug__empty"] = slug_empty

    json_slug_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(slug_ic, Unset):
        json_slug_ic = slug_ic

    params["slug__ic"] = json_slug_ic

    json_slug_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(slug_ie, Unset):
        json_slug_ie = slug_ie

    params["slug__ie"] = json_slug_ie

    json_slug_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(slug_iew, Unset):
        json_slug_iew = slug_iew

    params["slug__iew"] = json_slug_iew

    json_slug_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(slug_isw, Unset):
        json_slug_isw = slug_isw

    params["slug__isw"] = json_slug_isw

    json_slug_n: Union[Unset, list[str]] = UNSET
    if not isinstance(slug_n, Unset):
        json_slug_n = slug_n

    params["slug__n"] = json_slug_n

    json_slug_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(slug_nic, Unset):
        json_slug_nic = slug_nic

    params["slug__nic"] = json_slug_nic

    json_slug_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(slug_nie, Unset):
        json_slug_nie = slug_nie

    params["slug__nie"] = json_slug_nie

    json_slug_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(slug_niew, Unset):
        json_slug_niew = slug_niew

    params["slug__niew"] = json_slug_niew

    json_slug_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(slug_nisw, Unset):
        json_slug_nisw = slug_nisw

    params["slug__nisw"] = json_slug_nisw

    json_subdevice_role: Union[Unset, str] = UNSET
    if not isinstance(subdevice_role, Unset):
        json_subdevice_role = subdevice_role.value

    params["subdevice_role"] = json_subdevice_role

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

    json_u_height: Union[Unset, list[float]] = UNSET
    if not isinstance(u_height, Unset):
        json_u_height = u_height

    params["u_height"] = json_u_height

    params["u_height__empty"] = u_height_empty

    json_u_height_gt: Union[Unset, list[float]] = UNSET
    if not isinstance(u_height_gt, Unset):
        json_u_height_gt = u_height_gt

    params["u_height__gt"] = json_u_height_gt

    json_u_height_gte: Union[Unset, list[float]] = UNSET
    if not isinstance(u_height_gte, Unset):
        json_u_height_gte = u_height_gte

    params["u_height__gte"] = json_u_height_gte

    json_u_height_lt: Union[Unset, list[float]] = UNSET
    if not isinstance(u_height_lt, Unset):
        json_u_height_lt = u_height_lt

    params["u_height__lt"] = json_u_height_lt

    json_u_height_lte: Union[Unset, list[float]] = UNSET
    if not isinstance(u_height_lte, Unset):
        json_u_height_lte = u_height_lte

    params["u_height__lte"] = json_u_height_lte

    json_u_height_n: Union[Unset, list[float]] = UNSET
    if not isinstance(u_height_n, Unset):
        json_u_height_n = u_height_n

    params["u_height__n"] = json_u_height_n

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    json_weight: Union[Unset, list[float]] = UNSET
    if not isinstance(weight, Unset):
        json_weight = weight

    params["weight"] = json_weight

    params["weight__empty"] = weight_empty

    json_weight_gt: Union[Unset, list[float]] = UNSET
    if not isinstance(weight_gt, Unset):
        json_weight_gt = weight_gt

    params["weight__gt"] = json_weight_gt

    json_weight_gte: Union[Unset, list[float]] = UNSET
    if not isinstance(weight_gte, Unset):
        json_weight_gte = weight_gte

    params["weight__gte"] = json_weight_gte

    json_weight_lt: Union[Unset, list[float]] = UNSET
    if not isinstance(weight_lt, Unset):
        json_weight_lt = weight_lt

    params["weight__lt"] = json_weight_lt

    json_weight_lte: Union[Unset, list[float]] = UNSET
    if not isinstance(weight_lte, Unset):
        json_weight_lte = weight_lte

    params["weight__lte"] = json_weight_lte

    json_weight_n: Union[Unset, list[float]] = UNSET
    if not isinstance(weight_n, Unset):
        json_weight_n = weight_n

    params["weight__n"] = json_weight_n

    json_weight_unit: Union[Unset, str] = UNSET
    if not isinstance(weight_unit, Unset):
        json_weight_unit = weight_unit.value

    params["weight_unit"] = json_weight_unit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/dcim/device-types/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedDeviceTypeList]:
    if response.status_code == 200:
        response_200 = PaginatedDeviceTypeList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedDeviceTypeList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    airflow: Union[Unset, DcimDeviceTypesListAirflow] = UNSET,
    console_port_template_count: Union[Unset, list[int]] = UNSET,
    console_port_template_count_empty: Union[Unset, bool] = UNSET,
    console_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    console_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    console_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    console_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    console_port_template_count_n: Union[Unset, list[int]] = UNSET,
    console_ports: Union[Unset, bool] = UNSET,
    console_server_port_template_count: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_empty: Union[Unset, bool] = UNSET,
    console_server_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_n: Union[Unset, list[int]] = UNSET,
    console_server_ports: Union[Unset, bool] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    default_platform: Union[Unset, list[str]] = UNSET,
    default_platform_n: Union[Unset, list[str]] = UNSET,
    default_platform_id: Union[Unset, list[Union[None, int]]] = UNSET,
    default_platform_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    device_bay_template_count: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_empty: Union[Unset, bool] = UNSET,
    device_bay_template_count_gt: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_gte: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_lt: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_lte: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_n: Union[Unset, list[int]] = UNSET,
    device_bays: Union[Unset, bool] = UNSET,
    exclude_from_utilization: Union[Unset, bool] = UNSET,
    front_port_template_count: Union[Unset, list[int]] = UNSET,
    front_port_template_count_empty: Union[Unset, bool] = UNSET,
    front_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    front_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    front_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    front_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    front_port_template_count_n: Union[Unset, list[int]] = UNSET,
    has_front_image: Union[Unset, bool] = UNSET,
    has_rear_image: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_template_count: Union[Unset, list[int]] = UNSET,
    interface_template_count_empty: Union[Unset, bool] = UNSET,
    interface_template_count_gt: Union[Unset, list[int]] = UNSET,
    interface_template_count_gte: Union[Unset, list[int]] = UNSET,
    interface_template_count_lt: Union[Unset, list[int]] = UNSET,
    interface_template_count_lte: Union[Unset, list[int]] = UNSET,
    interface_template_count_n: Union[Unset, list[int]] = UNSET,
    interfaces: Union[Unset, bool] = UNSET,
    inventory_item_template_count: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_empty: Union[Unset, bool] = UNSET,
    inventory_item_template_count_gt: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_gte: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_lt: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_lte: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_n: Union[Unset, list[int]] = UNSET,
    inventory_items: Union[Unset, bool] = UNSET,
    is_full_depth: Union[Unset, bool] = UNSET,
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
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    model: Union[Unset, list[str]] = UNSET,
    model_empty: Union[Unset, bool] = UNSET,
    model_ic: Union[Unset, list[str]] = UNSET,
    model_ie: Union[Unset, list[str]] = UNSET,
    model_iew: Union[Unset, list[str]] = UNSET,
    model_isw: Union[Unset, list[str]] = UNSET,
    model_n: Union[Unset, list[str]] = UNSET,
    model_nic: Union[Unset, list[str]] = UNSET,
    model_nie: Union[Unset, list[str]] = UNSET,
    model_niew: Union[Unset, list[str]] = UNSET,
    model_nisw: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_bay_template_count: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_empty: Union[Unset, bool] = UNSET,
    module_bay_template_count_gt: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_gte: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_lt: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_lte: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_n: Union[Unset, list[int]] = UNSET,
    module_bays: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    part_number: Union[Unset, list[str]] = UNSET,
    part_number_empty: Union[Unset, bool] = UNSET,
    part_number_ic: Union[Unset, list[str]] = UNSET,
    part_number_ie: Union[Unset, list[str]] = UNSET,
    part_number_iew: Union[Unset, list[str]] = UNSET,
    part_number_isw: Union[Unset, list[str]] = UNSET,
    part_number_n: Union[Unset, list[str]] = UNSET,
    part_number_nic: Union[Unset, list[str]] = UNSET,
    part_number_nie: Union[Unset, list[str]] = UNSET,
    part_number_niew: Union[Unset, list[str]] = UNSET,
    part_number_nisw: Union[Unset, list[str]] = UNSET,
    pass_through_ports: Union[Unset, bool] = UNSET,
    power_outlet_template_count: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_empty: Union[Unset, bool] = UNSET,
    power_outlet_template_count_gt: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_gte: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_lt: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_lte: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_n: Union[Unset, list[int]] = UNSET,
    power_outlets: Union[Unset, bool] = UNSET,
    power_port_template_count: Union[Unset, list[int]] = UNSET,
    power_port_template_count_empty: Union[Unset, bool] = UNSET,
    power_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    power_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    power_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    power_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    power_port_template_count_n: Union[Unset, list[int]] = UNSET,
    power_ports: Union[Unset, bool] = UNSET,
    q: Union[Unset, str] = UNSET,
    rear_port_template_count: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_empty: Union[Unset, bool] = UNSET,
    rear_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_n: Union[Unset, list[int]] = UNSET,
    slug: Union[Unset, list[str]] = UNSET,
    slug_empty: Union[Unset, bool] = UNSET,
    slug_ic: Union[Unset, list[str]] = UNSET,
    slug_ie: Union[Unset, list[str]] = UNSET,
    slug_iew: Union[Unset, list[str]] = UNSET,
    slug_isw: Union[Unset, list[str]] = UNSET,
    slug_n: Union[Unset, list[str]] = UNSET,
    slug_nic: Union[Unset, list[str]] = UNSET,
    slug_nie: Union[Unset, list[str]] = UNSET,
    slug_niew: Union[Unset, list[str]] = UNSET,
    slug_nisw: Union[Unset, list[str]] = UNSET,
    subdevice_role: Union[Unset, DcimDeviceTypesListParentchildStatus] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    u_height: Union[Unset, list[float]] = UNSET,
    u_height_empty: Union[Unset, bool] = UNSET,
    u_height_gt: Union[Unset, list[float]] = UNSET,
    u_height_gte: Union[Unset, list[float]] = UNSET,
    u_height_lt: Union[Unset, list[float]] = UNSET,
    u_height_lte: Union[Unset, list[float]] = UNSET,
    u_height_n: Union[Unset, list[float]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    weight: Union[Unset, list[float]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[float]] = UNSET,
    weight_gte: Union[Unset, list[float]] = UNSET,
    weight_lt: Union[Unset, list[float]] = UNSET,
    weight_lte: Union[Unset, list[float]] = UNSET,
    weight_n: Union[Unset, list[float]] = UNSET,
    weight_unit: Union[Unset, DcimDeviceTypesListWeightUnit] = UNSET,
) -> Response[PaginatedDeviceTypeList]:
    """Get a list of device type objects.

    Args:
        airflow (Union[Unset, DcimDeviceTypesListAirflow]):
        console_port_template_count (Union[Unset, list[int]]):
        console_port_template_count_empty (Union[Unset, bool]):
        console_port_template_count_gt (Union[Unset, list[int]]):
        console_port_template_count_gte (Union[Unset, list[int]]):
        console_port_template_count_lt (Union[Unset, list[int]]):
        console_port_template_count_lte (Union[Unset, list[int]]):
        console_port_template_count_n (Union[Unset, list[int]]):
        console_ports (Union[Unset, bool]):
        console_server_port_template_count (Union[Unset, list[int]]):
        console_server_port_template_count_empty (Union[Unset, bool]):
        console_server_port_template_count_gt (Union[Unset, list[int]]):
        console_server_port_template_count_gte (Union[Unset, list[int]]):
        console_server_port_template_count_lt (Union[Unset, list[int]]):
        console_server_port_template_count_lte (Union[Unset, list[int]]):
        console_server_port_template_count_n (Union[Unset, list[int]]):
        console_server_ports (Union[Unset, bool]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        default_platform (Union[Unset, list[str]]):
        default_platform_n (Union[Unset, list[str]]):
        default_platform_id (Union[Unset, list[Union[None, int]]]):
        default_platform_id_n (Union[Unset, list[Union[None, int]]]):
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
        device_bay_template_count (Union[Unset, list[int]]):
        device_bay_template_count_empty (Union[Unset, bool]):
        device_bay_template_count_gt (Union[Unset, list[int]]):
        device_bay_template_count_gte (Union[Unset, list[int]]):
        device_bay_template_count_lt (Union[Unset, list[int]]):
        device_bay_template_count_lte (Union[Unset, list[int]]):
        device_bay_template_count_n (Union[Unset, list[int]]):
        device_bays (Union[Unset, bool]):
        exclude_from_utilization (Union[Unset, bool]):
        front_port_template_count (Union[Unset, list[int]]):
        front_port_template_count_empty (Union[Unset, bool]):
        front_port_template_count_gt (Union[Unset, list[int]]):
        front_port_template_count_gte (Union[Unset, list[int]]):
        front_port_template_count_lt (Union[Unset, list[int]]):
        front_port_template_count_lte (Union[Unset, list[int]]):
        front_port_template_count_n (Union[Unset, list[int]]):
        has_front_image (Union[Unset, bool]):
        has_rear_image (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_template_count (Union[Unset, list[int]]):
        interface_template_count_empty (Union[Unset, bool]):
        interface_template_count_gt (Union[Unset, list[int]]):
        interface_template_count_gte (Union[Unset, list[int]]):
        interface_template_count_lt (Union[Unset, list[int]]):
        interface_template_count_lte (Union[Unset, list[int]]):
        interface_template_count_n (Union[Unset, list[int]]):
        interfaces (Union[Unset, bool]):
        inventory_item_template_count (Union[Unset, list[int]]):
        inventory_item_template_count_empty (Union[Unset, bool]):
        inventory_item_template_count_gt (Union[Unset, list[int]]):
        inventory_item_template_count_gte (Union[Unset, list[int]]):
        inventory_item_template_count_lt (Union[Unset, list[int]]):
        inventory_item_template_count_lte (Union[Unset, list[int]]):
        inventory_item_template_count_n (Union[Unset, list[int]]):
        inventory_items (Union[Unset, bool]):
        is_full_depth (Union[Unset, bool]):
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
        manufacturer_id (Union[Unset, list[int]]):
        manufacturer_id_n (Union[Unset, list[int]]):
        model (Union[Unset, list[str]]):
        model_empty (Union[Unset, bool]):
        model_ic (Union[Unset, list[str]]):
        model_ie (Union[Unset, list[str]]):
        model_iew (Union[Unset, list[str]]):
        model_isw (Union[Unset, list[str]]):
        model_n (Union[Unset, list[str]]):
        model_nic (Union[Unset, list[str]]):
        model_nie (Union[Unset, list[str]]):
        model_niew (Union[Unset, list[str]]):
        model_nisw (Union[Unset, list[str]]):
        modified_by_request (Union[Unset, UUID]):
        module_bay_template_count (Union[Unset, list[int]]):
        module_bay_template_count_empty (Union[Unset, bool]):
        module_bay_template_count_gt (Union[Unset, list[int]]):
        module_bay_template_count_gte (Union[Unset, list[int]]):
        module_bay_template_count_lt (Union[Unset, list[int]]):
        module_bay_template_count_lte (Union[Unset, list[int]]):
        module_bay_template_count_n (Union[Unset, list[int]]):
        module_bays (Union[Unset, bool]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        part_number (Union[Unset, list[str]]):
        part_number_empty (Union[Unset, bool]):
        part_number_ic (Union[Unset, list[str]]):
        part_number_ie (Union[Unset, list[str]]):
        part_number_iew (Union[Unset, list[str]]):
        part_number_isw (Union[Unset, list[str]]):
        part_number_n (Union[Unset, list[str]]):
        part_number_nic (Union[Unset, list[str]]):
        part_number_nie (Union[Unset, list[str]]):
        part_number_niew (Union[Unset, list[str]]):
        part_number_nisw (Union[Unset, list[str]]):
        pass_through_ports (Union[Unset, bool]):
        power_outlet_template_count (Union[Unset, list[int]]):
        power_outlet_template_count_empty (Union[Unset, bool]):
        power_outlet_template_count_gt (Union[Unset, list[int]]):
        power_outlet_template_count_gte (Union[Unset, list[int]]):
        power_outlet_template_count_lt (Union[Unset, list[int]]):
        power_outlet_template_count_lte (Union[Unset, list[int]]):
        power_outlet_template_count_n (Union[Unset, list[int]]):
        power_outlets (Union[Unset, bool]):
        power_port_template_count (Union[Unset, list[int]]):
        power_port_template_count_empty (Union[Unset, bool]):
        power_port_template_count_gt (Union[Unset, list[int]]):
        power_port_template_count_gte (Union[Unset, list[int]]):
        power_port_template_count_lt (Union[Unset, list[int]]):
        power_port_template_count_lte (Union[Unset, list[int]]):
        power_port_template_count_n (Union[Unset, list[int]]):
        power_ports (Union[Unset, bool]):
        q (Union[Unset, str]):
        rear_port_template_count (Union[Unset, list[int]]):
        rear_port_template_count_empty (Union[Unset, bool]):
        rear_port_template_count_gt (Union[Unset, list[int]]):
        rear_port_template_count_gte (Union[Unset, list[int]]):
        rear_port_template_count_lt (Union[Unset, list[int]]):
        rear_port_template_count_lte (Union[Unset, list[int]]):
        rear_port_template_count_n (Union[Unset, list[int]]):
        slug (Union[Unset, list[str]]):
        slug_empty (Union[Unset, bool]):
        slug_ic (Union[Unset, list[str]]):
        slug_ie (Union[Unset, list[str]]):
        slug_iew (Union[Unset, list[str]]):
        slug_isw (Union[Unset, list[str]]):
        slug_n (Union[Unset, list[str]]):
        slug_nic (Union[Unset, list[str]]):
        slug_nie (Union[Unset, list[str]]):
        slug_niew (Union[Unset, list[str]]):
        slug_nisw (Union[Unset, list[str]]):
        subdevice_role (Union[Unset, DcimDeviceTypesListParentchildStatus]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        u_height (Union[Unset, list[float]]):
        u_height_empty (Union[Unset, bool]):
        u_height_gt (Union[Unset, list[float]]):
        u_height_gte (Union[Unset, list[float]]):
        u_height_lt (Union[Unset, list[float]]):
        u_height_lte (Union[Unset, list[float]]):
        u_height_n (Union[Unset, list[float]]):
        updated_by_request (Union[Unset, UUID]):
        weight (Union[Unset, list[float]]):
        weight_empty (Union[Unset, bool]):
        weight_gt (Union[Unset, list[float]]):
        weight_gte (Union[Unset, list[float]]):
        weight_lt (Union[Unset, list[float]]):
        weight_lte (Union[Unset, list[float]]):
        weight_n (Union[Unset, list[float]]):
        weight_unit (Union[Unset, DcimDeviceTypesListWeightUnit]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDeviceTypeList]
    """

    kwargs = _get_kwargs(
        airflow=airflow,
        console_port_template_count=console_port_template_count,
        console_port_template_count_empty=console_port_template_count_empty,
        console_port_template_count_gt=console_port_template_count_gt,
        console_port_template_count_gte=console_port_template_count_gte,
        console_port_template_count_lt=console_port_template_count_lt,
        console_port_template_count_lte=console_port_template_count_lte,
        console_port_template_count_n=console_port_template_count_n,
        console_ports=console_ports,
        console_server_port_template_count=console_server_port_template_count,
        console_server_port_template_count_empty=console_server_port_template_count_empty,
        console_server_port_template_count_gt=console_server_port_template_count_gt,
        console_server_port_template_count_gte=console_server_port_template_count_gte,
        console_server_port_template_count_lt=console_server_port_template_count_lt,
        console_server_port_template_count_lte=console_server_port_template_count_lte,
        console_server_port_template_count_n=console_server_port_template_count_n,
        console_server_ports=console_server_ports,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        default_platform=default_platform,
        default_platform_n=default_platform_n,
        default_platform_id=default_platform_id,
        default_platform_id_n=default_platform_id_n,
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
        device_bay_template_count=device_bay_template_count,
        device_bay_template_count_empty=device_bay_template_count_empty,
        device_bay_template_count_gt=device_bay_template_count_gt,
        device_bay_template_count_gte=device_bay_template_count_gte,
        device_bay_template_count_lt=device_bay_template_count_lt,
        device_bay_template_count_lte=device_bay_template_count_lte,
        device_bay_template_count_n=device_bay_template_count_n,
        device_bays=device_bays,
        exclude_from_utilization=exclude_from_utilization,
        front_port_template_count=front_port_template_count,
        front_port_template_count_empty=front_port_template_count_empty,
        front_port_template_count_gt=front_port_template_count_gt,
        front_port_template_count_gte=front_port_template_count_gte,
        front_port_template_count_lt=front_port_template_count_lt,
        front_port_template_count_lte=front_port_template_count_lte,
        front_port_template_count_n=front_port_template_count_n,
        has_front_image=has_front_image,
        has_rear_image=has_rear_image,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface_template_count=interface_template_count,
        interface_template_count_empty=interface_template_count_empty,
        interface_template_count_gt=interface_template_count_gt,
        interface_template_count_gte=interface_template_count_gte,
        interface_template_count_lt=interface_template_count_lt,
        interface_template_count_lte=interface_template_count_lte,
        interface_template_count_n=interface_template_count_n,
        interfaces=interfaces,
        inventory_item_template_count=inventory_item_template_count,
        inventory_item_template_count_empty=inventory_item_template_count_empty,
        inventory_item_template_count_gt=inventory_item_template_count_gt,
        inventory_item_template_count_gte=inventory_item_template_count_gte,
        inventory_item_template_count_lt=inventory_item_template_count_lt,
        inventory_item_template_count_lte=inventory_item_template_count_lte,
        inventory_item_template_count_n=inventory_item_template_count_n,
        inventory_items=inventory_items,
        is_full_depth=is_full_depth,
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
        model=model,
        model_empty=model_empty,
        model_ic=model_ic,
        model_ie=model_ie,
        model_iew=model_iew,
        model_isw=model_isw,
        model_n=model_n,
        model_nic=model_nic,
        model_nie=model_nie,
        model_niew=model_niew,
        model_nisw=model_nisw,
        modified_by_request=modified_by_request,
        module_bay_template_count=module_bay_template_count,
        module_bay_template_count_empty=module_bay_template_count_empty,
        module_bay_template_count_gt=module_bay_template_count_gt,
        module_bay_template_count_gte=module_bay_template_count_gte,
        module_bay_template_count_lt=module_bay_template_count_lt,
        module_bay_template_count_lte=module_bay_template_count_lte,
        module_bay_template_count_n=module_bay_template_count_n,
        module_bays=module_bays,
        offset=offset,
        ordering=ordering,
        part_number=part_number,
        part_number_empty=part_number_empty,
        part_number_ic=part_number_ic,
        part_number_ie=part_number_ie,
        part_number_iew=part_number_iew,
        part_number_isw=part_number_isw,
        part_number_n=part_number_n,
        part_number_nic=part_number_nic,
        part_number_nie=part_number_nie,
        part_number_niew=part_number_niew,
        part_number_nisw=part_number_nisw,
        pass_through_ports=pass_through_ports,
        power_outlet_template_count=power_outlet_template_count,
        power_outlet_template_count_empty=power_outlet_template_count_empty,
        power_outlet_template_count_gt=power_outlet_template_count_gt,
        power_outlet_template_count_gte=power_outlet_template_count_gte,
        power_outlet_template_count_lt=power_outlet_template_count_lt,
        power_outlet_template_count_lte=power_outlet_template_count_lte,
        power_outlet_template_count_n=power_outlet_template_count_n,
        power_outlets=power_outlets,
        power_port_template_count=power_port_template_count,
        power_port_template_count_empty=power_port_template_count_empty,
        power_port_template_count_gt=power_port_template_count_gt,
        power_port_template_count_gte=power_port_template_count_gte,
        power_port_template_count_lt=power_port_template_count_lt,
        power_port_template_count_lte=power_port_template_count_lte,
        power_port_template_count_n=power_port_template_count_n,
        power_ports=power_ports,
        q=q,
        rear_port_template_count=rear_port_template_count,
        rear_port_template_count_empty=rear_port_template_count_empty,
        rear_port_template_count_gt=rear_port_template_count_gt,
        rear_port_template_count_gte=rear_port_template_count_gte,
        rear_port_template_count_lt=rear_port_template_count_lt,
        rear_port_template_count_lte=rear_port_template_count_lte,
        rear_port_template_count_n=rear_port_template_count_n,
        slug=slug,
        slug_empty=slug_empty,
        slug_ic=slug_ic,
        slug_ie=slug_ie,
        slug_iew=slug_iew,
        slug_isw=slug_isw,
        slug_n=slug_n,
        slug_nic=slug_nic,
        slug_nie=slug_nie,
        slug_niew=slug_niew,
        slug_nisw=slug_nisw,
        subdevice_role=subdevice_role,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        u_height=u_height,
        u_height_empty=u_height_empty,
        u_height_gt=u_height_gt,
        u_height_gte=u_height_gte,
        u_height_lt=u_height_lt,
        u_height_lte=u_height_lte,
        u_height_n=u_height_n,
        updated_by_request=updated_by_request,
        weight=weight,
        weight_empty=weight_empty,
        weight_gt=weight_gt,
        weight_gte=weight_gte,
        weight_lt=weight_lt,
        weight_lte=weight_lte,
        weight_n=weight_n,
        weight_unit=weight_unit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    airflow: Union[Unset, DcimDeviceTypesListAirflow] = UNSET,
    console_port_template_count: Union[Unset, list[int]] = UNSET,
    console_port_template_count_empty: Union[Unset, bool] = UNSET,
    console_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    console_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    console_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    console_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    console_port_template_count_n: Union[Unset, list[int]] = UNSET,
    console_ports: Union[Unset, bool] = UNSET,
    console_server_port_template_count: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_empty: Union[Unset, bool] = UNSET,
    console_server_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_n: Union[Unset, list[int]] = UNSET,
    console_server_ports: Union[Unset, bool] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    default_platform: Union[Unset, list[str]] = UNSET,
    default_platform_n: Union[Unset, list[str]] = UNSET,
    default_platform_id: Union[Unset, list[Union[None, int]]] = UNSET,
    default_platform_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    device_bay_template_count: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_empty: Union[Unset, bool] = UNSET,
    device_bay_template_count_gt: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_gte: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_lt: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_lte: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_n: Union[Unset, list[int]] = UNSET,
    device_bays: Union[Unset, bool] = UNSET,
    exclude_from_utilization: Union[Unset, bool] = UNSET,
    front_port_template_count: Union[Unset, list[int]] = UNSET,
    front_port_template_count_empty: Union[Unset, bool] = UNSET,
    front_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    front_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    front_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    front_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    front_port_template_count_n: Union[Unset, list[int]] = UNSET,
    has_front_image: Union[Unset, bool] = UNSET,
    has_rear_image: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_template_count: Union[Unset, list[int]] = UNSET,
    interface_template_count_empty: Union[Unset, bool] = UNSET,
    interface_template_count_gt: Union[Unset, list[int]] = UNSET,
    interface_template_count_gte: Union[Unset, list[int]] = UNSET,
    interface_template_count_lt: Union[Unset, list[int]] = UNSET,
    interface_template_count_lte: Union[Unset, list[int]] = UNSET,
    interface_template_count_n: Union[Unset, list[int]] = UNSET,
    interfaces: Union[Unset, bool] = UNSET,
    inventory_item_template_count: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_empty: Union[Unset, bool] = UNSET,
    inventory_item_template_count_gt: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_gte: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_lt: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_lte: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_n: Union[Unset, list[int]] = UNSET,
    inventory_items: Union[Unset, bool] = UNSET,
    is_full_depth: Union[Unset, bool] = UNSET,
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
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    model: Union[Unset, list[str]] = UNSET,
    model_empty: Union[Unset, bool] = UNSET,
    model_ic: Union[Unset, list[str]] = UNSET,
    model_ie: Union[Unset, list[str]] = UNSET,
    model_iew: Union[Unset, list[str]] = UNSET,
    model_isw: Union[Unset, list[str]] = UNSET,
    model_n: Union[Unset, list[str]] = UNSET,
    model_nic: Union[Unset, list[str]] = UNSET,
    model_nie: Union[Unset, list[str]] = UNSET,
    model_niew: Union[Unset, list[str]] = UNSET,
    model_nisw: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_bay_template_count: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_empty: Union[Unset, bool] = UNSET,
    module_bay_template_count_gt: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_gte: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_lt: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_lte: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_n: Union[Unset, list[int]] = UNSET,
    module_bays: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    part_number: Union[Unset, list[str]] = UNSET,
    part_number_empty: Union[Unset, bool] = UNSET,
    part_number_ic: Union[Unset, list[str]] = UNSET,
    part_number_ie: Union[Unset, list[str]] = UNSET,
    part_number_iew: Union[Unset, list[str]] = UNSET,
    part_number_isw: Union[Unset, list[str]] = UNSET,
    part_number_n: Union[Unset, list[str]] = UNSET,
    part_number_nic: Union[Unset, list[str]] = UNSET,
    part_number_nie: Union[Unset, list[str]] = UNSET,
    part_number_niew: Union[Unset, list[str]] = UNSET,
    part_number_nisw: Union[Unset, list[str]] = UNSET,
    pass_through_ports: Union[Unset, bool] = UNSET,
    power_outlet_template_count: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_empty: Union[Unset, bool] = UNSET,
    power_outlet_template_count_gt: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_gte: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_lt: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_lte: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_n: Union[Unset, list[int]] = UNSET,
    power_outlets: Union[Unset, bool] = UNSET,
    power_port_template_count: Union[Unset, list[int]] = UNSET,
    power_port_template_count_empty: Union[Unset, bool] = UNSET,
    power_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    power_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    power_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    power_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    power_port_template_count_n: Union[Unset, list[int]] = UNSET,
    power_ports: Union[Unset, bool] = UNSET,
    q: Union[Unset, str] = UNSET,
    rear_port_template_count: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_empty: Union[Unset, bool] = UNSET,
    rear_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_n: Union[Unset, list[int]] = UNSET,
    slug: Union[Unset, list[str]] = UNSET,
    slug_empty: Union[Unset, bool] = UNSET,
    slug_ic: Union[Unset, list[str]] = UNSET,
    slug_ie: Union[Unset, list[str]] = UNSET,
    slug_iew: Union[Unset, list[str]] = UNSET,
    slug_isw: Union[Unset, list[str]] = UNSET,
    slug_n: Union[Unset, list[str]] = UNSET,
    slug_nic: Union[Unset, list[str]] = UNSET,
    slug_nie: Union[Unset, list[str]] = UNSET,
    slug_niew: Union[Unset, list[str]] = UNSET,
    slug_nisw: Union[Unset, list[str]] = UNSET,
    subdevice_role: Union[Unset, DcimDeviceTypesListParentchildStatus] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    u_height: Union[Unset, list[float]] = UNSET,
    u_height_empty: Union[Unset, bool] = UNSET,
    u_height_gt: Union[Unset, list[float]] = UNSET,
    u_height_gte: Union[Unset, list[float]] = UNSET,
    u_height_lt: Union[Unset, list[float]] = UNSET,
    u_height_lte: Union[Unset, list[float]] = UNSET,
    u_height_n: Union[Unset, list[float]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    weight: Union[Unset, list[float]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[float]] = UNSET,
    weight_gte: Union[Unset, list[float]] = UNSET,
    weight_lt: Union[Unset, list[float]] = UNSET,
    weight_lte: Union[Unset, list[float]] = UNSET,
    weight_n: Union[Unset, list[float]] = UNSET,
    weight_unit: Union[Unset, DcimDeviceTypesListWeightUnit] = UNSET,
) -> Optional[PaginatedDeviceTypeList]:
    """Get a list of device type objects.

    Args:
        airflow (Union[Unset, DcimDeviceTypesListAirflow]):
        console_port_template_count (Union[Unset, list[int]]):
        console_port_template_count_empty (Union[Unset, bool]):
        console_port_template_count_gt (Union[Unset, list[int]]):
        console_port_template_count_gte (Union[Unset, list[int]]):
        console_port_template_count_lt (Union[Unset, list[int]]):
        console_port_template_count_lte (Union[Unset, list[int]]):
        console_port_template_count_n (Union[Unset, list[int]]):
        console_ports (Union[Unset, bool]):
        console_server_port_template_count (Union[Unset, list[int]]):
        console_server_port_template_count_empty (Union[Unset, bool]):
        console_server_port_template_count_gt (Union[Unset, list[int]]):
        console_server_port_template_count_gte (Union[Unset, list[int]]):
        console_server_port_template_count_lt (Union[Unset, list[int]]):
        console_server_port_template_count_lte (Union[Unset, list[int]]):
        console_server_port_template_count_n (Union[Unset, list[int]]):
        console_server_ports (Union[Unset, bool]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        default_platform (Union[Unset, list[str]]):
        default_platform_n (Union[Unset, list[str]]):
        default_platform_id (Union[Unset, list[Union[None, int]]]):
        default_platform_id_n (Union[Unset, list[Union[None, int]]]):
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
        device_bay_template_count (Union[Unset, list[int]]):
        device_bay_template_count_empty (Union[Unset, bool]):
        device_bay_template_count_gt (Union[Unset, list[int]]):
        device_bay_template_count_gte (Union[Unset, list[int]]):
        device_bay_template_count_lt (Union[Unset, list[int]]):
        device_bay_template_count_lte (Union[Unset, list[int]]):
        device_bay_template_count_n (Union[Unset, list[int]]):
        device_bays (Union[Unset, bool]):
        exclude_from_utilization (Union[Unset, bool]):
        front_port_template_count (Union[Unset, list[int]]):
        front_port_template_count_empty (Union[Unset, bool]):
        front_port_template_count_gt (Union[Unset, list[int]]):
        front_port_template_count_gte (Union[Unset, list[int]]):
        front_port_template_count_lt (Union[Unset, list[int]]):
        front_port_template_count_lte (Union[Unset, list[int]]):
        front_port_template_count_n (Union[Unset, list[int]]):
        has_front_image (Union[Unset, bool]):
        has_rear_image (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_template_count (Union[Unset, list[int]]):
        interface_template_count_empty (Union[Unset, bool]):
        interface_template_count_gt (Union[Unset, list[int]]):
        interface_template_count_gte (Union[Unset, list[int]]):
        interface_template_count_lt (Union[Unset, list[int]]):
        interface_template_count_lte (Union[Unset, list[int]]):
        interface_template_count_n (Union[Unset, list[int]]):
        interfaces (Union[Unset, bool]):
        inventory_item_template_count (Union[Unset, list[int]]):
        inventory_item_template_count_empty (Union[Unset, bool]):
        inventory_item_template_count_gt (Union[Unset, list[int]]):
        inventory_item_template_count_gte (Union[Unset, list[int]]):
        inventory_item_template_count_lt (Union[Unset, list[int]]):
        inventory_item_template_count_lte (Union[Unset, list[int]]):
        inventory_item_template_count_n (Union[Unset, list[int]]):
        inventory_items (Union[Unset, bool]):
        is_full_depth (Union[Unset, bool]):
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
        manufacturer_id (Union[Unset, list[int]]):
        manufacturer_id_n (Union[Unset, list[int]]):
        model (Union[Unset, list[str]]):
        model_empty (Union[Unset, bool]):
        model_ic (Union[Unset, list[str]]):
        model_ie (Union[Unset, list[str]]):
        model_iew (Union[Unset, list[str]]):
        model_isw (Union[Unset, list[str]]):
        model_n (Union[Unset, list[str]]):
        model_nic (Union[Unset, list[str]]):
        model_nie (Union[Unset, list[str]]):
        model_niew (Union[Unset, list[str]]):
        model_nisw (Union[Unset, list[str]]):
        modified_by_request (Union[Unset, UUID]):
        module_bay_template_count (Union[Unset, list[int]]):
        module_bay_template_count_empty (Union[Unset, bool]):
        module_bay_template_count_gt (Union[Unset, list[int]]):
        module_bay_template_count_gte (Union[Unset, list[int]]):
        module_bay_template_count_lt (Union[Unset, list[int]]):
        module_bay_template_count_lte (Union[Unset, list[int]]):
        module_bay_template_count_n (Union[Unset, list[int]]):
        module_bays (Union[Unset, bool]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        part_number (Union[Unset, list[str]]):
        part_number_empty (Union[Unset, bool]):
        part_number_ic (Union[Unset, list[str]]):
        part_number_ie (Union[Unset, list[str]]):
        part_number_iew (Union[Unset, list[str]]):
        part_number_isw (Union[Unset, list[str]]):
        part_number_n (Union[Unset, list[str]]):
        part_number_nic (Union[Unset, list[str]]):
        part_number_nie (Union[Unset, list[str]]):
        part_number_niew (Union[Unset, list[str]]):
        part_number_nisw (Union[Unset, list[str]]):
        pass_through_ports (Union[Unset, bool]):
        power_outlet_template_count (Union[Unset, list[int]]):
        power_outlet_template_count_empty (Union[Unset, bool]):
        power_outlet_template_count_gt (Union[Unset, list[int]]):
        power_outlet_template_count_gte (Union[Unset, list[int]]):
        power_outlet_template_count_lt (Union[Unset, list[int]]):
        power_outlet_template_count_lte (Union[Unset, list[int]]):
        power_outlet_template_count_n (Union[Unset, list[int]]):
        power_outlets (Union[Unset, bool]):
        power_port_template_count (Union[Unset, list[int]]):
        power_port_template_count_empty (Union[Unset, bool]):
        power_port_template_count_gt (Union[Unset, list[int]]):
        power_port_template_count_gte (Union[Unset, list[int]]):
        power_port_template_count_lt (Union[Unset, list[int]]):
        power_port_template_count_lte (Union[Unset, list[int]]):
        power_port_template_count_n (Union[Unset, list[int]]):
        power_ports (Union[Unset, bool]):
        q (Union[Unset, str]):
        rear_port_template_count (Union[Unset, list[int]]):
        rear_port_template_count_empty (Union[Unset, bool]):
        rear_port_template_count_gt (Union[Unset, list[int]]):
        rear_port_template_count_gte (Union[Unset, list[int]]):
        rear_port_template_count_lt (Union[Unset, list[int]]):
        rear_port_template_count_lte (Union[Unset, list[int]]):
        rear_port_template_count_n (Union[Unset, list[int]]):
        slug (Union[Unset, list[str]]):
        slug_empty (Union[Unset, bool]):
        slug_ic (Union[Unset, list[str]]):
        slug_ie (Union[Unset, list[str]]):
        slug_iew (Union[Unset, list[str]]):
        slug_isw (Union[Unset, list[str]]):
        slug_n (Union[Unset, list[str]]):
        slug_nic (Union[Unset, list[str]]):
        slug_nie (Union[Unset, list[str]]):
        slug_niew (Union[Unset, list[str]]):
        slug_nisw (Union[Unset, list[str]]):
        subdevice_role (Union[Unset, DcimDeviceTypesListParentchildStatus]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        u_height (Union[Unset, list[float]]):
        u_height_empty (Union[Unset, bool]):
        u_height_gt (Union[Unset, list[float]]):
        u_height_gte (Union[Unset, list[float]]):
        u_height_lt (Union[Unset, list[float]]):
        u_height_lte (Union[Unset, list[float]]):
        u_height_n (Union[Unset, list[float]]):
        updated_by_request (Union[Unset, UUID]):
        weight (Union[Unset, list[float]]):
        weight_empty (Union[Unset, bool]):
        weight_gt (Union[Unset, list[float]]):
        weight_gte (Union[Unset, list[float]]):
        weight_lt (Union[Unset, list[float]]):
        weight_lte (Union[Unset, list[float]]):
        weight_n (Union[Unset, list[float]]):
        weight_unit (Union[Unset, DcimDeviceTypesListWeightUnit]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDeviceTypeList
    """

    return sync_detailed(
        client=client,
        airflow=airflow,
        console_port_template_count=console_port_template_count,
        console_port_template_count_empty=console_port_template_count_empty,
        console_port_template_count_gt=console_port_template_count_gt,
        console_port_template_count_gte=console_port_template_count_gte,
        console_port_template_count_lt=console_port_template_count_lt,
        console_port_template_count_lte=console_port_template_count_lte,
        console_port_template_count_n=console_port_template_count_n,
        console_ports=console_ports,
        console_server_port_template_count=console_server_port_template_count,
        console_server_port_template_count_empty=console_server_port_template_count_empty,
        console_server_port_template_count_gt=console_server_port_template_count_gt,
        console_server_port_template_count_gte=console_server_port_template_count_gte,
        console_server_port_template_count_lt=console_server_port_template_count_lt,
        console_server_port_template_count_lte=console_server_port_template_count_lte,
        console_server_port_template_count_n=console_server_port_template_count_n,
        console_server_ports=console_server_ports,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        default_platform=default_platform,
        default_platform_n=default_platform_n,
        default_platform_id=default_platform_id,
        default_platform_id_n=default_platform_id_n,
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
        device_bay_template_count=device_bay_template_count,
        device_bay_template_count_empty=device_bay_template_count_empty,
        device_bay_template_count_gt=device_bay_template_count_gt,
        device_bay_template_count_gte=device_bay_template_count_gte,
        device_bay_template_count_lt=device_bay_template_count_lt,
        device_bay_template_count_lte=device_bay_template_count_lte,
        device_bay_template_count_n=device_bay_template_count_n,
        device_bays=device_bays,
        exclude_from_utilization=exclude_from_utilization,
        front_port_template_count=front_port_template_count,
        front_port_template_count_empty=front_port_template_count_empty,
        front_port_template_count_gt=front_port_template_count_gt,
        front_port_template_count_gte=front_port_template_count_gte,
        front_port_template_count_lt=front_port_template_count_lt,
        front_port_template_count_lte=front_port_template_count_lte,
        front_port_template_count_n=front_port_template_count_n,
        has_front_image=has_front_image,
        has_rear_image=has_rear_image,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface_template_count=interface_template_count,
        interface_template_count_empty=interface_template_count_empty,
        interface_template_count_gt=interface_template_count_gt,
        interface_template_count_gte=interface_template_count_gte,
        interface_template_count_lt=interface_template_count_lt,
        interface_template_count_lte=interface_template_count_lte,
        interface_template_count_n=interface_template_count_n,
        interfaces=interfaces,
        inventory_item_template_count=inventory_item_template_count,
        inventory_item_template_count_empty=inventory_item_template_count_empty,
        inventory_item_template_count_gt=inventory_item_template_count_gt,
        inventory_item_template_count_gte=inventory_item_template_count_gte,
        inventory_item_template_count_lt=inventory_item_template_count_lt,
        inventory_item_template_count_lte=inventory_item_template_count_lte,
        inventory_item_template_count_n=inventory_item_template_count_n,
        inventory_items=inventory_items,
        is_full_depth=is_full_depth,
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
        model=model,
        model_empty=model_empty,
        model_ic=model_ic,
        model_ie=model_ie,
        model_iew=model_iew,
        model_isw=model_isw,
        model_n=model_n,
        model_nic=model_nic,
        model_nie=model_nie,
        model_niew=model_niew,
        model_nisw=model_nisw,
        modified_by_request=modified_by_request,
        module_bay_template_count=module_bay_template_count,
        module_bay_template_count_empty=module_bay_template_count_empty,
        module_bay_template_count_gt=module_bay_template_count_gt,
        module_bay_template_count_gte=module_bay_template_count_gte,
        module_bay_template_count_lt=module_bay_template_count_lt,
        module_bay_template_count_lte=module_bay_template_count_lte,
        module_bay_template_count_n=module_bay_template_count_n,
        module_bays=module_bays,
        offset=offset,
        ordering=ordering,
        part_number=part_number,
        part_number_empty=part_number_empty,
        part_number_ic=part_number_ic,
        part_number_ie=part_number_ie,
        part_number_iew=part_number_iew,
        part_number_isw=part_number_isw,
        part_number_n=part_number_n,
        part_number_nic=part_number_nic,
        part_number_nie=part_number_nie,
        part_number_niew=part_number_niew,
        part_number_nisw=part_number_nisw,
        pass_through_ports=pass_through_ports,
        power_outlet_template_count=power_outlet_template_count,
        power_outlet_template_count_empty=power_outlet_template_count_empty,
        power_outlet_template_count_gt=power_outlet_template_count_gt,
        power_outlet_template_count_gte=power_outlet_template_count_gte,
        power_outlet_template_count_lt=power_outlet_template_count_lt,
        power_outlet_template_count_lte=power_outlet_template_count_lte,
        power_outlet_template_count_n=power_outlet_template_count_n,
        power_outlets=power_outlets,
        power_port_template_count=power_port_template_count,
        power_port_template_count_empty=power_port_template_count_empty,
        power_port_template_count_gt=power_port_template_count_gt,
        power_port_template_count_gte=power_port_template_count_gte,
        power_port_template_count_lt=power_port_template_count_lt,
        power_port_template_count_lte=power_port_template_count_lte,
        power_port_template_count_n=power_port_template_count_n,
        power_ports=power_ports,
        q=q,
        rear_port_template_count=rear_port_template_count,
        rear_port_template_count_empty=rear_port_template_count_empty,
        rear_port_template_count_gt=rear_port_template_count_gt,
        rear_port_template_count_gte=rear_port_template_count_gte,
        rear_port_template_count_lt=rear_port_template_count_lt,
        rear_port_template_count_lte=rear_port_template_count_lte,
        rear_port_template_count_n=rear_port_template_count_n,
        slug=slug,
        slug_empty=slug_empty,
        slug_ic=slug_ic,
        slug_ie=slug_ie,
        slug_iew=slug_iew,
        slug_isw=slug_isw,
        slug_n=slug_n,
        slug_nic=slug_nic,
        slug_nie=slug_nie,
        slug_niew=slug_niew,
        slug_nisw=slug_nisw,
        subdevice_role=subdevice_role,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        u_height=u_height,
        u_height_empty=u_height_empty,
        u_height_gt=u_height_gt,
        u_height_gte=u_height_gte,
        u_height_lt=u_height_lt,
        u_height_lte=u_height_lte,
        u_height_n=u_height_n,
        updated_by_request=updated_by_request,
        weight=weight,
        weight_empty=weight_empty,
        weight_gt=weight_gt,
        weight_gte=weight_gte,
        weight_lt=weight_lt,
        weight_lte=weight_lte,
        weight_n=weight_n,
        weight_unit=weight_unit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    airflow: Union[Unset, DcimDeviceTypesListAirflow] = UNSET,
    console_port_template_count: Union[Unset, list[int]] = UNSET,
    console_port_template_count_empty: Union[Unset, bool] = UNSET,
    console_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    console_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    console_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    console_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    console_port_template_count_n: Union[Unset, list[int]] = UNSET,
    console_ports: Union[Unset, bool] = UNSET,
    console_server_port_template_count: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_empty: Union[Unset, bool] = UNSET,
    console_server_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_n: Union[Unset, list[int]] = UNSET,
    console_server_ports: Union[Unset, bool] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    default_platform: Union[Unset, list[str]] = UNSET,
    default_platform_n: Union[Unset, list[str]] = UNSET,
    default_platform_id: Union[Unset, list[Union[None, int]]] = UNSET,
    default_platform_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    device_bay_template_count: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_empty: Union[Unset, bool] = UNSET,
    device_bay_template_count_gt: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_gte: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_lt: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_lte: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_n: Union[Unset, list[int]] = UNSET,
    device_bays: Union[Unset, bool] = UNSET,
    exclude_from_utilization: Union[Unset, bool] = UNSET,
    front_port_template_count: Union[Unset, list[int]] = UNSET,
    front_port_template_count_empty: Union[Unset, bool] = UNSET,
    front_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    front_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    front_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    front_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    front_port_template_count_n: Union[Unset, list[int]] = UNSET,
    has_front_image: Union[Unset, bool] = UNSET,
    has_rear_image: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_template_count: Union[Unset, list[int]] = UNSET,
    interface_template_count_empty: Union[Unset, bool] = UNSET,
    interface_template_count_gt: Union[Unset, list[int]] = UNSET,
    interface_template_count_gte: Union[Unset, list[int]] = UNSET,
    interface_template_count_lt: Union[Unset, list[int]] = UNSET,
    interface_template_count_lte: Union[Unset, list[int]] = UNSET,
    interface_template_count_n: Union[Unset, list[int]] = UNSET,
    interfaces: Union[Unset, bool] = UNSET,
    inventory_item_template_count: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_empty: Union[Unset, bool] = UNSET,
    inventory_item_template_count_gt: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_gte: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_lt: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_lte: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_n: Union[Unset, list[int]] = UNSET,
    inventory_items: Union[Unset, bool] = UNSET,
    is_full_depth: Union[Unset, bool] = UNSET,
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
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    model: Union[Unset, list[str]] = UNSET,
    model_empty: Union[Unset, bool] = UNSET,
    model_ic: Union[Unset, list[str]] = UNSET,
    model_ie: Union[Unset, list[str]] = UNSET,
    model_iew: Union[Unset, list[str]] = UNSET,
    model_isw: Union[Unset, list[str]] = UNSET,
    model_n: Union[Unset, list[str]] = UNSET,
    model_nic: Union[Unset, list[str]] = UNSET,
    model_nie: Union[Unset, list[str]] = UNSET,
    model_niew: Union[Unset, list[str]] = UNSET,
    model_nisw: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_bay_template_count: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_empty: Union[Unset, bool] = UNSET,
    module_bay_template_count_gt: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_gte: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_lt: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_lte: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_n: Union[Unset, list[int]] = UNSET,
    module_bays: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    part_number: Union[Unset, list[str]] = UNSET,
    part_number_empty: Union[Unset, bool] = UNSET,
    part_number_ic: Union[Unset, list[str]] = UNSET,
    part_number_ie: Union[Unset, list[str]] = UNSET,
    part_number_iew: Union[Unset, list[str]] = UNSET,
    part_number_isw: Union[Unset, list[str]] = UNSET,
    part_number_n: Union[Unset, list[str]] = UNSET,
    part_number_nic: Union[Unset, list[str]] = UNSET,
    part_number_nie: Union[Unset, list[str]] = UNSET,
    part_number_niew: Union[Unset, list[str]] = UNSET,
    part_number_nisw: Union[Unset, list[str]] = UNSET,
    pass_through_ports: Union[Unset, bool] = UNSET,
    power_outlet_template_count: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_empty: Union[Unset, bool] = UNSET,
    power_outlet_template_count_gt: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_gte: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_lt: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_lte: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_n: Union[Unset, list[int]] = UNSET,
    power_outlets: Union[Unset, bool] = UNSET,
    power_port_template_count: Union[Unset, list[int]] = UNSET,
    power_port_template_count_empty: Union[Unset, bool] = UNSET,
    power_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    power_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    power_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    power_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    power_port_template_count_n: Union[Unset, list[int]] = UNSET,
    power_ports: Union[Unset, bool] = UNSET,
    q: Union[Unset, str] = UNSET,
    rear_port_template_count: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_empty: Union[Unset, bool] = UNSET,
    rear_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_n: Union[Unset, list[int]] = UNSET,
    slug: Union[Unset, list[str]] = UNSET,
    slug_empty: Union[Unset, bool] = UNSET,
    slug_ic: Union[Unset, list[str]] = UNSET,
    slug_ie: Union[Unset, list[str]] = UNSET,
    slug_iew: Union[Unset, list[str]] = UNSET,
    slug_isw: Union[Unset, list[str]] = UNSET,
    slug_n: Union[Unset, list[str]] = UNSET,
    slug_nic: Union[Unset, list[str]] = UNSET,
    slug_nie: Union[Unset, list[str]] = UNSET,
    slug_niew: Union[Unset, list[str]] = UNSET,
    slug_nisw: Union[Unset, list[str]] = UNSET,
    subdevice_role: Union[Unset, DcimDeviceTypesListParentchildStatus] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    u_height: Union[Unset, list[float]] = UNSET,
    u_height_empty: Union[Unset, bool] = UNSET,
    u_height_gt: Union[Unset, list[float]] = UNSET,
    u_height_gte: Union[Unset, list[float]] = UNSET,
    u_height_lt: Union[Unset, list[float]] = UNSET,
    u_height_lte: Union[Unset, list[float]] = UNSET,
    u_height_n: Union[Unset, list[float]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    weight: Union[Unset, list[float]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[float]] = UNSET,
    weight_gte: Union[Unset, list[float]] = UNSET,
    weight_lt: Union[Unset, list[float]] = UNSET,
    weight_lte: Union[Unset, list[float]] = UNSET,
    weight_n: Union[Unset, list[float]] = UNSET,
    weight_unit: Union[Unset, DcimDeviceTypesListWeightUnit] = UNSET,
) -> Response[PaginatedDeviceTypeList]:
    """Get a list of device type objects.

    Args:
        airflow (Union[Unset, DcimDeviceTypesListAirflow]):
        console_port_template_count (Union[Unset, list[int]]):
        console_port_template_count_empty (Union[Unset, bool]):
        console_port_template_count_gt (Union[Unset, list[int]]):
        console_port_template_count_gte (Union[Unset, list[int]]):
        console_port_template_count_lt (Union[Unset, list[int]]):
        console_port_template_count_lte (Union[Unset, list[int]]):
        console_port_template_count_n (Union[Unset, list[int]]):
        console_ports (Union[Unset, bool]):
        console_server_port_template_count (Union[Unset, list[int]]):
        console_server_port_template_count_empty (Union[Unset, bool]):
        console_server_port_template_count_gt (Union[Unset, list[int]]):
        console_server_port_template_count_gte (Union[Unset, list[int]]):
        console_server_port_template_count_lt (Union[Unset, list[int]]):
        console_server_port_template_count_lte (Union[Unset, list[int]]):
        console_server_port_template_count_n (Union[Unset, list[int]]):
        console_server_ports (Union[Unset, bool]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        default_platform (Union[Unset, list[str]]):
        default_platform_n (Union[Unset, list[str]]):
        default_platform_id (Union[Unset, list[Union[None, int]]]):
        default_platform_id_n (Union[Unset, list[Union[None, int]]]):
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
        device_bay_template_count (Union[Unset, list[int]]):
        device_bay_template_count_empty (Union[Unset, bool]):
        device_bay_template_count_gt (Union[Unset, list[int]]):
        device_bay_template_count_gte (Union[Unset, list[int]]):
        device_bay_template_count_lt (Union[Unset, list[int]]):
        device_bay_template_count_lte (Union[Unset, list[int]]):
        device_bay_template_count_n (Union[Unset, list[int]]):
        device_bays (Union[Unset, bool]):
        exclude_from_utilization (Union[Unset, bool]):
        front_port_template_count (Union[Unset, list[int]]):
        front_port_template_count_empty (Union[Unset, bool]):
        front_port_template_count_gt (Union[Unset, list[int]]):
        front_port_template_count_gte (Union[Unset, list[int]]):
        front_port_template_count_lt (Union[Unset, list[int]]):
        front_port_template_count_lte (Union[Unset, list[int]]):
        front_port_template_count_n (Union[Unset, list[int]]):
        has_front_image (Union[Unset, bool]):
        has_rear_image (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_template_count (Union[Unset, list[int]]):
        interface_template_count_empty (Union[Unset, bool]):
        interface_template_count_gt (Union[Unset, list[int]]):
        interface_template_count_gte (Union[Unset, list[int]]):
        interface_template_count_lt (Union[Unset, list[int]]):
        interface_template_count_lte (Union[Unset, list[int]]):
        interface_template_count_n (Union[Unset, list[int]]):
        interfaces (Union[Unset, bool]):
        inventory_item_template_count (Union[Unset, list[int]]):
        inventory_item_template_count_empty (Union[Unset, bool]):
        inventory_item_template_count_gt (Union[Unset, list[int]]):
        inventory_item_template_count_gte (Union[Unset, list[int]]):
        inventory_item_template_count_lt (Union[Unset, list[int]]):
        inventory_item_template_count_lte (Union[Unset, list[int]]):
        inventory_item_template_count_n (Union[Unset, list[int]]):
        inventory_items (Union[Unset, bool]):
        is_full_depth (Union[Unset, bool]):
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
        manufacturer_id (Union[Unset, list[int]]):
        manufacturer_id_n (Union[Unset, list[int]]):
        model (Union[Unset, list[str]]):
        model_empty (Union[Unset, bool]):
        model_ic (Union[Unset, list[str]]):
        model_ie (Union[Unset, list[str]]):
        model_iew (Union[Unset, list[str]]):
        model_isw (Union[Unset, list[str]]):
        model_n (Union[Unset, list[str]]):
        model_nic (Union[Unset, list[str]]):
        model_nie (Union[Unset, list[str]]):
        model_niew (Union[Unset, list[str]]):
        model_nisw (Union[Unset, list[str]]):
        modified_by_request (Union[Unset, UUID]):
        module_bay_template_count (Union[Unset, list[int]]):
        module_bay_template_count_empty (Union[Unset, bool]):
        module_bay_template_count_gt (Union[Unset, list[int]]):
        module_bay_template_count_gte (Union[Unset, list[int]]):
        module_bay_template_count_lt (Union[Unset, list[int]]):
        module_bay_template_count_lte (Union[Unset, list[int]]):
        module_bay_template_count_n (Union[Unset, list[int]]):
        module_bays (Union[Unset, bool]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        part_number (Union[Unset, list[str]]):
        part_number_empty (Union[Unset, bool]):
        part_number_ic (Union[Unset, list[str]]):
        part_number_ie (Union[Unset, list[str]]):
        part_number_iew (Union[Unset, list[str]]):
        part_number_isw (Union[Unset, list[str]]):
        part_number_n (Union[Unset, list[str]]):
        part_number_nic (Union[Unset, list[str]]):
        part_number_nie (Union[Unset, list[str]]):
        part_number_niew (Union[Unset, list[str]]):
        part_number_nisw (Union[Unset, list[str]]):
        pass_through_ports (Union[Unset, bool]):
        power_outlet_template_count (Union[Unset, list[int]]):
        power_outlet_template_count_empty (Union[Unset, bool]):
        power_outlet_template_count_gt (Union[Unset, list[int]]):
        power_outlet_template_count_gte (Union[Unset, list[int]]):
        power_outlet_template_count_lt (Union[Unset, list[int]]):
        power_outlet_template_count_lte (Union[Unset, list[int]]):
        power_outlet_template_count_n (Union[Unset, list[int]]):
        power_outlets (Union[Unset, bool]):
        power_port_template_count (Union[Unset, list[int]]):
        power_port_template_count_empty (Union[Unset, bool]):
        power_port_template_count_gt (Union[Unset, list[int]]):
        power_port_template_count_gte (Union[Unset, list[int]]):
        power_port_template_count_lt (Union[Unset, list[int]]):
        power_port_template_count_lte (Union[Unset, list[int]]):
        power_port_template_count_n (Union[Unset, list[int]]):
        power_ports (Union[Unset, bool]):
        q (Union[Unset, str]):
        rear_port_template_count (Union[Unset, list[int]]):
        rear_port_template_count_empty (Union[Unset, bool]):
        rear_port_template_count_gt (Union[Unset, list[int]]):
        rear_port_template_count_gte (Union[Unset, list[int]]):
        rear_port_template_count_lt (Union[Unset, list[int]]):
        rear_port_template_count_lte (Union[Unset, list[int]]):
        rear_port_template_count_n (Union[Unset, list[int]]):
        slug (Union[Unset, list[str]]):
        slug_empty (Union[Unset, bool]):
        slug_ic (Union[Unset, list[str]]):
        slug_ie (Union[Unset, list[str]]):
        slug_iew (Union[Unset, list[str]]):
        slug_isw (Union[Unset, list[str]]):
        slug_n (Union[Unset, list[str]]):
        slug_nic (Union[Unset, list[str]]):
        slug_nie (Union[Unset, list[str]]):
        slug_niew (Union[Unset, list[str]]):
        slug_nisw (Union[Unset, list[str]]):
        subdevice_role (Union[Unset, DcimDeviceTypesListParentchildStatus]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        u_height (Union[Unset, list[float]]):
        u_height_empty (Union[Unset, bool]):
        u_height_gt (Union[Unset, list[float]]):
        u_height_gte (Union[Unset, list[float]]):
        u_height_lt (Union[Unset, list[float]]):
        u_height_lte (Union[Unset, list[float]]):
        u_height_n (Union[Unset, list[float]]):
        updated_by_request (Union[Unset, UUID]):
        weight (Union[Unset, list[float]]):
        weight_empty (Union[Unset, bool]):
        weight_gt (Union[Unset, list[float]]):
        weight_gte (Union[Unset, list[float]]):
        weight_lt (Union[Unset, list[float]]):
        weight_lte (Union[Unset, list[float]]):
        weight_n (Union[Unset, list[float]]):
        weight_unit (Union[Unset, DcimDeviceTypesListWeightUnit]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDeviceTypeList]
    """

    kwargs = _get_kwargs(
        airflow=airflow,
        console_port_template_count=console_port_template_count,
        console_port_template_count_empty=console_port_template_count_empty,
        console_port_template_count_gt=console_port_template_count_gt,
        console_port_template_count_gte=console_port_template_count_gte,
        console_port_template_count_lt=console_port_template_count_lt,
        console_port_template_count_lte=console_port_template_count_lte,
        console_port_template_count_n=console_port_template_count_n,
        console_ports=console_ports,
        console_server_port_template_count=console_server_port_template_count,
        console_server_port_template_count_empty=console_server_port_template_count_empty,
        console_server_port_template_count_gt=console_server_port_template_count_gt,
        console_server_port_template_count_gte=console_server_port_template_count_gte,
        console_server_port_template_count_lt=console_server_port_template_count_lt,
        console_server_port_template_count_lte=console_server_port_template_count_lte,
        console_server_port_template_count_n=console_server_port_template_count_n,
        console_server_ports=console_server_ports,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        default_platform=default_platform,
        default_platform_n=default_platform_n,
        default_platform_id=default_platform_id,
        default_platform_id_n=default_platform_id_n,
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
        device_bay_template_count=device_bay_template_count,
        device_bay_template_count_empty=device_bay_template_count_empty,
        device_bay_template_count_gt=device_bay_template_count_gt,
        device_bay_template_count_gte=device_bay_template_count_gte,
        device_bay_template_count_lt=device_bay_template_count_lt,
        device_bay_template_count_lte=device_bay_template_count_lte,
        device_bay_template_count_n=device_bay_template_count_n,
        device_bays=device_bays,
        exclude_from_utilization=exclude_from_utilization,
        front_port_template_count=front_port_template_count,
        front_port_template_count_empty=front_port_template_count_empty,
        front_port_template_count_gt=front_port_template_count_gt,
        front_port_template_count_gte=front_port_template_count_gte,
        front_port_template_count_lt=front_port_template_count_lt,
        front_port_template_count_lte=front_port_template_count_lte,
        front_port_template_count_n=front_port_template_count_n,
        has_front_image=has_front_image,
        has_rear_image=has_rear_image,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface_template_count=interface_template_count,
        interface_template_count_empty=interface_template_count_empty,
        interface_template_count_gt=interface_template_count_gt,
        interface_template_count_gte=interface_template_count_gte,
        interface_template_count_lt=interface_template_count_lt,
        interface_template_count_lte=interface_template_count_lte,
        interface_template_count_n=interface_template_count_n,
        interfaces=interfaces,
        inventory_item_template_count=inventory_item_template_count,
        inventory_item_template_count_empty=inventory_item_template_count_empty,
        inventory_item_template_count_gt=inventory_item_template_count_gt,
        inventory_item_template_count_gte=inventory_item_template_count_gte,
        inventory_item_template_count_lt=inventory_item_template_count_lt,
        inventory_item_template_count_lte=inventory_item_template_count_lte,
        inventory_item_template_count_n=inventory_item_template_count_n,
        inventory_items=inventory_items,
        is_full_depth=is_full_depth,
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
        model=model,
        model_empty=model_empty,
        model_ic=model_ic,
        model_ie=model_ie,
        model_iew=model_iew,
        model_isw=model_isw,
        model_n=model_n,
        model_nic=model_nic,
        model_nie=model_nie,
        model_niew=model_niew,
        model_nisw=model_nisw,
        modified_by_request=modified_by_request,
        module_bay_template_count=module_bay_template_count,
        module_bay_template_count_empty=module_bay_template_count_empty,
        module_bay_template_count_gt=module_bay_template_count_gt,
        module_bay_template_count_gte=module_bay_template_count_gte,
        module_bay_template_count_lt=module_bay_template_count_lt,
        module_bay_template_count_lte=module_bay_template_count_lte,
        module_bay_template_count_n=module_bay_template_count_n,
        module_bays=module_bays,
        offset=offset,
        ordering=ordering,
        part_number=part_number,
        part_number_empty=part_number_empty,
        part_number_ic=part_number_ic,
        part_number_ie=part_number_ie,
        part_number_iew=part_number_iew,
        part_number_isw=part_number_isw,
        part_number_n=part_number_n,
        part_number_nic=part_number_nic,
        part_number_nie=part_number_nie,
        part_number_niew=part_number_niew,
        part_number_nisw=part_number_nisw,
        pass_through_ports=pass_through_ports,
        power_outlet_template_count=power_outlet_template_count,
        power_outlet_template_count_empty=power_outlet_template_count_empty,
        power_outlet_template_count_gt=power_outlet_template_count_gt,
        power_outlet_template_count_gte=power_outlet_template_count_gte,
        power_outlet_template_count_lt=power_outlet_template_count_lt,
        power_outlet_template_count_lte=power_outlet_template_count_lte,
        power_outlet_template_count_n=power_outlet_template_count_n,
        power_outlets=power_outlets,
        power_port_template_count=power_port_template_count,
        power_port_template_count_empty=power_port_template_count_empty,
        power_port_template_count_gt=power_port_template_count_gt,
        power_port_template_count_gte=power_port_template_count_gte,
        power_port_template_count_lt=power_port_template_count_lt,
        power_port_template_count_lte=power_port_template_count_lte,
        power_port_template_count_n=power_port_template_count_n,
        power_ports=power_ports,
        q=q,
        rear_port_template_count=rear_port_template_count,
        rear_port_template_count_empty=rear_port_template_count_empty,
        rear_port_template_count_gt=rear_port_template_count_gt,
        rear_port_template_count_gte=rear_port_template_count_gte,
        rear_port_template_count_lt=rear_port_template_count_lt,
        rear_port_template_count_lte=rear_port_template_count_lte,
        rear_port_template_count_n=rear_port_template_count_n,
        slug=slug,
        slug_empty=slug_empty,
        slug_ic=slug_ic,
        slug_ie=slug_ie,
        slug_iew=slug_iew,
        slug_isw=slug_isw,
        slug_n=slug_n,
        slug_nic=slug_nic,
        slug_nie=slug_nie,
        slug_niew=slug_niew,
        slug_nisw=slug_nisw,
        subdevice_role=subdevice_role,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        u_height=u_height,
        u_height_empty=u_height_empty,
        u_height_gt=u_height_gt,
        u_height_gte=u_height_gte,
        u_height_lt=u_height_lt,
        u_height_lte=u_height_lte,
        u_height_n=u_height_n,
        updated_by_request=updated_by_request,
        weight=weight,
        weight_empty=weight_empty,
        weight_gt=weight_gt,
        weight_gte=weight_gte,
        weight_lt=weight_lt,
        weight_lte=weight_lte,
        weight_n=weight_n,
        weight_unit=weight_unit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    airflow: Union[Unset, DcimDeviceTypesListAirflow] = UNSET,
    console_port_template_count: Union[Unset, list[int]] = UNSET,
    console_port_template_count_empty: Union[Unset, bool] = UNSET,
    console_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    console_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    console_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    console_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    console_port_template_count_n: Union[Unset, list[int]] = UNSET,
    console_ports: Union[Unset, bool] = UNSET,
    console_server_port_template_count: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_empty: Union[Unset, bool] = UNSET,
    console_server_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    console_server_port_template_count_n: Union[Unset, list[int]] = UNSET,
    console_server_ports: Union[Unset, bool] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    default_platform: Union[Unset, list[str]] = UNSET,
    default_platform_n: Union[Unset, list[str]] = UNSET,
    default_platform_id: Union[Unset, list[Union[None, int]]] = UNSET,
    default_platform_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    device_bay_template_count: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_empty: Union[Unset, bool] = UNSET,
    device_bay_template_count_gt: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_gte: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_lt: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_lte: Union[Unset, list[int]] = UNSET,
    device_bay_template_count_n: Union[Unset, list[int]] = UNSET,
    device_bays: Union[Unset, bool] = UNSET,
    exclude_from_utilization: Union[Unset, bool] = UNSET,
    front_port_template_count: Union[Unset, list[int]] = UNSET,
    front_port_template_count_empty: Union[Unset, bool] = UNSET,
    front_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    front_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    front_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    front_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    front_port_template_count_n: Union[Unset, list[int]] = UNSET,
    has_front_image: Union[Unset, bool] = UNSET,
    has_rear_image: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_template_count: Union[Unset, list[int]] = UNSET,
    interface_template_count_empty: Union[Unset, bool] = UNSET,
    interface_template_count_gt: Union[Unset, list[int]] = UNSET,
    interface_template_count_gte: Union[Unset, list[int]] = UNSET,
    interface_template_count_lt: Union[Unset, list[int]] = UNSET,
    interface_template_count_lte: Union[Unset, list[int]] = UNSET,
    interface_template_count_n: Union[Unset, list[int]] = UNSET,
    interfaces: Union[Unset, bool] = UNSET,
    inventory_item_template_count: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_empty: Union[Unset, bool] = UNSET,
    inventory_item_template_count_gt: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_gte: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_lt: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_lte: Union[Unset, list[int]] = UNSET,
    inventory_item_template_count_n: Union[Unset, list[int]] = UNSET,
    inventory_items: Union[Unset, bool] = UNSET,
    is_full_depth: Union[Unset, bool] = UNSET,
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
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    model: Union[Unset, list[str]] = UNSET,
    model_empty: Union[Unset, bool] = UNSET,
    model_ic: Union[Unset, list[str]] = UNSET,
    model_ie: Union[Unset, list[str]] = UNSET,
    model_iew: Union[Unset, list[str]] = UNSET,
    model_isw: Union[Unset, list[str]] = UNSET,
    model_n: Union[Unset, list[str]] = UNSET,
    model_nic: Union[Unset, list[str]] = UNSET,
    model_nie: Union[Unset, list[str]] = UNSET,
    model_niew: Union[Unset, list[str]] = UNSET,
    model_nisw: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    module_bay_template_count: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_empty: Union[Unset, bool] = UNSET,
    module_bay_template_count_gt: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_gte: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_lt: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_lte: Union[Unset, list[int]] = UNSET,
    module_bay_template_count_n: Union[Unset, list[int]] = UNSET,
    module_bays: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    part_number: Union[Unset, list[str]] = UNSET,
    part_number_empty: Union[Unset, bool] = UNSET,
    part_number_ic: Union[Unset, list[str]] = UNSET,
    part_number_ie: Union[Unset, list[str]] = UNSET,
    part_number_iew: Union[Unset, list[str]] = UNSET,
    part_number_isw: Union[Unset, list[str]] = UNSET,
    part_number_n: Union[Unset, list[str]] = UNSET,
    part_number_nic: Union[Unset, list[str]] = UNSET,
    part_number_nie: Union[Unset, list[str]] = UNSET,
    part_number_niew: Union[Unset, list[str]] = UNSET,
    part_number_nisw: Union[Unset, list[str]] = UNSET,
    pass_through_ports: Union[Unset, bool] = UNSET,
    power_outlet_template_count: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_empty: Union[Unset, bool] = UNSET,
    power_outlet_template_count_gt: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_gte: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_lt: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_lte: Union[Unset, list[int]] = UNSET,
    power_outlet_template_count_n: Union[Unset, list[int]] = UNSET,
    power_outlets: Union[Unset, bool] = UNSET,
    power_port_template_count: Union[Unset, list[int]] = UNSET,
    power_port_template_count_empty: Union[Unset, bool] = UNSET,
    power_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    power_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    power_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    power_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    power_port_template_count_n: Union[Unset, list[int]] = UNSET,
    power_ports: Union[Unset, bool] = UNSET,
    q: Union[Unset, str] = UNSET,
    rear_port_template_count: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_empty: Union[Unset, bool] = UNSET,
    rear_port_template_count_gt: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_gte: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_lt: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_lte: Union[Unset, list[int]] = UNSET,
    rear_port_template_count_n: Union[Unset, list[int]] = UNSET,
    slug: Union[Unset, list[str]] = UNSET,
    slug_empty: Union[Unset, bool] = UNSET,
    slug_ic: Union[Unset, list[str]] = UNSET,
    slug_ie: Union[Unset, list[str]] = UNSET,
    slug_iew: Union[Unset, list[str]] = UNSET,
    slug_isw: Union[Unset, list[str]] = UNSET,
    slug_n: Union[Unset, list[str]] = UNSET,
    slug_nic: Union[Unset, list[str]] = UNSET,
    slug_nie: Union[Unset, list[str]] = UNSET,
    slug_niew: Union[Unset, list[str]] = UNSET,
    slug_nisw: Union[Unset, list[str]] = UNSET,
    subdevice_role: Union[Unset, DcimDeviceTypesListParentchildStatus] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    u_height: Union[Unset, list[float]] = UNSET,
    u_height_empty: Union[Unset, bool] = UNSET,
    u_height_gt: Union[Unset, list[float]] = UNSET,
    u_height_gte: Union[Unset, list[float]] = UNSET,
    u_height_lt: Union[Unset, list[float]] = UNSET,
    u_height_lte: Union[Unset, list[float]] = UNSET,
    u_height_n: Union[Unset, list[float]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    weight: Union[Unset, list[float]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[float]] = UNSET,
    weight_gte: Union[Unset, list[float]] = UNSET,
    weight_lt: Union[Unset, list[float]] = UNSET,
    weight_lte: Union[Unset, list[float]] = UNSET,
    weight_n: Union[Unset, list[float]] = UNSET,
    weight_unit: Union[Unset, DcimDeviceTypesListWeightUnit] = UNSET,
) -> Optional[PaginatedDeviceTypeList]:
    """Get a list of device type objects.

    Args:
        airflow (Union[Unset, DcimDeviceTypesListAirflow]):
        console_port_template_count (Union[Unset, list[int]]):
        console_port_template_count_empty (Union[Unset, bool]):
        console_port_template_count_gt (Union[Unset, list[int]]):
        console_port_template_count_gte (Union[Unset, list[int]]):
        console_port_template_count_lt (Union[Unset, list[int]]):
        console_port_template_count_lte (Union[Unset, list[int]]):
        console_port_template_count_n (Union[Unset, list[int]]):
        console_ports (Union[Unset, bool]):
        console_server_port_template_count (Union[Unset, list[int]]):
        console_server_port_template_count_empty (Union[Unset, bool]):
        console_server_port_template_count_gt (Union[Unset, list[int]]):
        console_server_port_template_count_gte (Union[Unset, list[int]]):
        console_server_port_template_count_lt (Union[Unset, list[int]]):
        console_server_port_template_count_lte (Union[Unset, list[int]]):
        console_server_port_template_count_n (Union[Unset, list[int]]):
        console_server_ports (Union[Unset, bool]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        default_platform (Union[Unset, list[str]]):
        default_platform_n (Union[Unset, list[str]]):
        default_platform_id (Union[Unset, list[Union[None, int]]]):
        default_platform_id_n (Union[Unset, list[Union[None, int]]]):
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
        device_bay_template_count (Union[Unset, list[int]]):
        device_bay_template_count_empty (Union[Unset, bool]):
        device_bay_template_count_gt (Union[Unset, list[int]]):
        device_bay_template_count_gte (Union[Unset, list[int]]):
        device_bay_template_count_lt (Union[Unset, list[int]]):
        device_bay_template_count_lte (Union[Unset, list[int]]):
        device_bay_template_count_n (Union[Unset, list[int]]):
        device_bays (Union[Unset, bool]):
        exclude_from_utilization (Union[Unset, bool]):
        front_port_template_count (Union[Unset, list[int]]):
        front_port_template_count_empty (Union[Unset, bool]):
        front_port_template_count_gt (Union[Unset, list[int]]):
        front_port_template_count_gte (Union[Unset, list[int]]):
        front_port_template_count_lt (Union[Unset, list[int]]):
        front_port_template_count_lte (Union[Unset, list[int]]):
        front_port_template_count_n (Union[Unset, list[int]]):
        has_front_image (Union[Unset, bool]):
        has_rear_image (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_template_count (Union[Unset, list[int]]):
        interface_template_count_empty (Union[Unset, bool]):
        interface_template_count_gt (Union[Unset, list[int]]):
        interface_template_count_gte (Union[Unset, list[int]]):
        interface_template_count_lt (Union[Unset, list[int]]):
        interface_template_count_lte (Union[Unset, list[int]]):
        interface_template_count_n (Union[Unset, list[int]]):
        interfaces (Union[Unset, bool]):
        inventory_item_template_count (Union[Unset, list[int]]):
        inventory_item_template_count_empty (Union[Unset, bool]):
        inventory_item_template_count_gt (Union[Unset, list[int]]):
        inventory_item_template_count_gte (Union[Unset, list[int]]):
        inventory_item_template_count_lt (Union[Unset, list[int]]):
        inventory_item_template_count_lte (Union[Unset, list[int]]):
        inventory_item_template_count_n (Union[Unset, list[int]]):
        inventory_items (Union[Unset, bool]):
        is_full_depth (Union[Unset, bool]):
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
        manufacturer_id (Union[Unset, list[int]]):
        manufacturer_id_n (Union[Unset, list[int]]):
        model (Union[Unset, list[str]]):
        model_empty (Union[Unset, bool]):
        model_ic (Union[Unset, list[str]]):
        model_ie (Union[Unset, list[str]]):
        model_iew (Union[Unset, list[str]]):
        model_isw (Union[Unset, list[str]]):
        model_n (Union[Unset, list[str]]):
        model_nic (Union[Unset, list[str]]):
        model_nie (Union[Unset, list[str]]):
        model_niew (Union[Unset, list[str]]):
        model_nisw (Union[Unset, list[str]]):
        modified_by_request (Union[Unset, UUID]):
        module_bay_template_count (Union[Unset, list[int]]):
        module_bay_template_count_empty (Union[Unset, bool]):
        module_bay_template_count_gt (Union[Unset, list[int]]):
        module_bay_template_count_gte (Union[Unset, list[int]]):
        module_bay_template_count_lt (Union[Unset, list[int]]):
        module_bay_template_count_lte (Union[Unset, list[int]]):
        module_bay_template_count_n (Union[Unset, list[int]]):
        module_bays (Union[Unset, bool]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        part_number (Union[Unset, list[str]]):
        part_number_empty (Union[Unset, bool]):
        part_number_ic (Union[Unset, list[str]]):
        part_number_ie (Union[Unset, list[str]]):
        part_number_iew (Union[Unset, list[str]]):
        part_number_isw (Union[Unset, list[str]]):
        part_number_n (Union[Unset, list[str]]):
        part_number_nic (Union[Unset, list[str]]):
        part_number_nie (Union[Unset, list[str]]):
        part_number_niew (Union[Unset, list[str]]):
        part_number_nisw (Union[Unset, list[str]]):
        pass_through_ports (Union[Unset, bool]):
        power_outlet_template_count (Union[Unset, list[int]]):
        power_outlet_template_count_empty (Union[Unset, bool]):
        power_outlet_template_count_gt (Union[Unset, list[int]]):
        power_outlet_template_count_gte (Union[Unset, list[int]]):
        power_outlet_template_count_lt (Union[Unset, list[int]]):
        power_outlet_template_count_lte (Union[Unset, list[int]]):
        power_outlet_template_count_n (Union[Unset, list[int]]):
        power_outlets (Union[Unset, bool]):
        power_port_template_count (Union[Unset, list[int]]):
        power_port_template_count_empty (Union[Unset, bool]):
        power_port_template_count_gt (Union[Unset, list[int]]):
        power_port_template_count_gte (Union[Unset, list[int]]):
        power_port_template_count_lt (Union[Unset, list[int]]):
        power_port_template_count_lte (Union[Unset, list[int]]):
        power_port_template_count_n (Union[Unset, list[int]]):
        power_ports (Union[Unset, bool]):
        q (Union[Unset, str]):
        rear_port_template_count (Union[Unset, list[int]]):
        rear_port_template_count_empty (Union[Unset, bool]):
        rear_port_template_count_gt (Union[Unset, list[int]]):
        rear_port_template_count_gte (Union[Unset, list[int]]):
        rear_port_template_count_lt (Union[Unset, list[int]]):
        rear_port_template_count_lte (Union[Unset, list[int]]):
        rear_port_template_count_n (Union[Unset, list[int]]):
        slug (Union[Unset, list[str]]):
        slug_empty (Union[Unset, bool]):
        slug_ic (Union[Unset, list[str]]):
        slug_ie (Union[Unset, list[str]]):
        slug_iew (Union[Unset, list[str]]):
        slug_isw (Union[Unset, list[str]]):
        slug_n (Union[Unset, list[str]]):
        slug_nic (Union[Unset, list[str]]):
        slug_nie (Union[Unset, list[str]]):
        slug_niew (Union[Unset, list[str]]):
        slug_nisw (Union[Unset, list[str]]):
        subdevice_role (Union[Unset, DcimDeviceTypesListParentchildStatus]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        u_height (Union[Unset, list[float]]):
        u_height_empty (Union[Unset, bool]):
        u_height_gt (Union[Unset, list[float]]):
        u_height_gte (Union[Unset, list[float]]):
        u_height_lt (Union[Unset, list[float]]):
        u_height_lte (Union[Unset, list[float]]):
        u_height_n (Union[Unset, list[float]]):
        updated_by_request (Union[Unset, UUID]):
        weight (Union[Unset, list[float]]):
        weight_empty (Union[Unset, bool]):
        weight_gt (Union[Unset, list[float]]):
        weight_gte (Union[Unset, list[float]]):
        weight_lt (Union[Unset, list[float]]):
        weight_lte (Union[Unset, list[float]]):
        weight_n (Union[Unset, list[float]]):
        weight_unit (Union[Unset, DcimDeviceTypesListWeightUnit]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDeviceTypeList
    """

    return (
        await asyncio_detailed(
            client=client,
            airflow=airflow,
            console_port_template_count=console_port_template_count,
            console_port_template_count_empty=console_port_template_count_empty,
            console_port_template_count_gt=console_port_template_count_gt,
            console_port_template_count_gte=console_port_template_count_gte,
            console_port_template_count_lt=console_port_template_count_lt,
            console_port_template_count_lte=console_port_template_count_lte,
            console_port_template_count_n=console_port_template_count_n,
            console_ports=console_ports,
            console_server_port_template_count=console_server_port_template_count,
            console_server_port_template_count_empty=console_server_port_template_count_empty,
            console_server_port_template_count_gt=console_server_port_template_count_gt,
            console_server_port_template_count_gte=console_server_port_template_count_gte,
            console_server_port_template_count_lt=console_server_port_template_count_lt,
            console_server_port_template_count_lte=console_server_port_template_count_lte,
            console_server_port_template_count_n=console_server_port_template_count_n,
            console_server_ports=console_server_ports,
            created=created,
            created_empty=created_empty,
            created_gt=created_gt,
            created_gte=created_gte,
            created_lt=created_lt,
            created_lte=created_lte,
            created_n=created_n,
            created_by_request=created_by_request,
            default_platform=default_platform,
            default_platform_n=default_platform_n,
            default_platform_id=default_platform_id,
            default_platform_id_n=default_platform_id_n,
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
            device_bay_template_count=device_bay_template_count,
            device_bay_template_count_empty=device_bay_template_count_empty,
            device_bay_template_count_gt=device_bay_template_count_gt,
            device_bay_template_count_gte=device_bay_template_count_gte,
            device_bay_template_count_lt=device_bay_template_count_lt,
            device_bay_template_count_lte=device_bay_template_count_lte,
            device_bay_template_count_n=device_bay_template_count_n,
            device_bays=device_bays,
            exclude_from_utilization=exclude_from_utilization,
            front_port_template_count=front_port_template_count,
            front_port_template_count_empty=front_port_template_count_empty,
            front_port_template_count_gt=front_port_template_count_gt,
            front_port_template_count_gte=front_port_template_count_gte,
            front_port_template_count_lt=front_port_template_count_lt,
            front_port_template_count_lte=front_port_template_count_lte,
            front_port_template_count_n=front_port_template_count_n,
            has_front_image=has_front_image,
            has_rear_image=has_rear_image,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            interface_template_count=interface_template_count,
            interface_template_count_empty=interface_template_count_empty,
            interface_template_count_gt=interface_template_count_gt,
            interface_template_count_gte=interface_template_count_gte,
            interface_template_count_lt=interface_template_count_lt,
            interface_template_count_lte=interface_template_count_lte,
            interface_template_count_n=interface_template_count_n,
            interfaces=interfaces,
            inventory_item_template_count=inventory_item_template_count,
            inventory_item_template_count_empty=inventory_item_template_count_empty,
            inventory_item_template_count_gt=inventory_item_template_count_gt,
            inventory_item_template_count_gte=inventory_item_template_count_gte,
            inventory_item_template_count_lt=inventory_item_template_count_lt,
            inventory_item_template_count_lte=inventory_item_template_count_lte,
            inventory_item_template_count_n=inventory_item_template_count_n,
            inventory_items=inventory_items,
            is_full_depth=is_full_depth,
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
            model=model,
            model_empty=model_empty,
            model_ic=model_ic,
            model_ie=model_ie,
            model_iew=model_iew,
            model_isw=model_isw,
            model_n=model_n,
            model_nic=model_nic,
            model_nie=model_nie,
            model_niew=model_niew,
            model_nisw=model_nisw,
            modified_by_request=modified_by_request,
            module_bay_template_count=module_bay_template_count,
            module_bay_template_count_empty=module_bay_template_count_empty,
            module_bay_template_count_gt=module_bay_template_count_gt,
            module_bay_template_count_gte=module_bay_template_count_gte,
            module_bay_template_count_lt=module_bay_template_count_lt,
            module_bay_template_count_lte=module_bay_template_count_lte,
            module_bay_template_count_n=module_bay_template_count_n,
            module_bays=module_bays,
            offset=offset,
            ordering=ordering,
            part_number=part_number,
            part_number_empty=part_number_empty,
            part_number_ic=part_number_ic,
            part_number_ie=part_number_ie,
            part_number_iew=part_number_iew,
            part_number_isw=part_number_isw,
            part_number_n=part_number_n,
            part_number_nic=part_number_nic,
            part_number_nie=part_number_nie,
            part_number_niew=part_number_niew,
            part_number_nisw=part_number_nisw,
            pass_through_ports=pass_through_ports,
            power_outlet_template_count=power_outlet_template_count,
            power_outlet_template_count_empty=power_outlet_template_count_empty,
            power_outlet_template_count_gt=power_outlet_template_count_gt,
            power_outlet_template_count_gte=power_outlet_template_count_gte,
            power_outlet_template_count_lt=power_outlet_template_count_lt,
            power_outlet_template_count_lte=power_outlet_template_count_lte,
            power_outlet_template_count_n=power_outlet_template_count_n,
            power_outlets=power_outlets,
            power_port_template_count=power_port_template_count,
            power_port_template_count_empty=power_port_template_count_empty,
            power_port_template_count_gt=power_port_template_count_gt,
            power_port_template_count_gte=power_port_template_count_gte,
            power_port_template_count_lt=power_port_template_count_lt,
            power_port_template_count_lte=power_port_template_count_lte,
            power_port_template_count_n=power_port_template_count_n,
            power_ports=power_ports,
            q=q,
            rear_port_template_count=rear_port_template_count,
            rear_port_template_count_empty=rear_port_template_count_empty,
            rear_port_template_count_gt=rear_port_template_count_gt,
            rear_port_template_count_gte=rear_port_template_count_gte,
            rear_port_template_count_lt=rear_port_template_count_lt,
            rear_port_template_count_lte=rear_port_template_count_lte,
            rear_port_template_count_n=rear_port_template_count_n,
            slug=slug,
            slug_empty=slug_empty,
            slug_ic=slug_ic,
            slug_ie=slug_ie,
            slug_iew=slug_iew,
            slug_isw=slug_isw,
            slug_n=slug_n,
            slug_nic=slug_nic,
            slug_nie=slug_nie,
            slug_niew=slug_niew,
            slug_nisw=slug_nisw,
            subdevice_role=subdevice_role,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
            u_height=u_height,
            u_height_empty=u_height_empty,
            u_height_gt=u_height_gt,
            u_height_gte=u_height_gte,
            u_height_lt=u_height_lt,
            u_height_lte=u_height_lte,
            u_height_n=u_height_n,
            updated_by_request=updated_by_request,
            weight=weight,
            weight_empty=weight_empty,
            weight_gt=weight_gt,
            weight_gte=weight_gte,
            weight_lt=weight_lt,
            weight_lte=weight_lte,
            weight_n=weight_n,
            weight_unit=weight_unit,
        )
    ).parsed
