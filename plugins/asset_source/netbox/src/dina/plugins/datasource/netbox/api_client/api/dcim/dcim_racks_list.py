import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dcim_racks_list_airflow import DcimRacksListAirflow
from ...models.dcim_racks_list_outer_unit import DcimRacksListOuterUnit
from ...models.dcim_racks_list_weight_unit import DcimRacksListWeightUnit
from ...models.paginated_rack_list import PaginatedRackList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    airflow: Union[Unset, DcimRacksListAirflow] = UNSET,
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
    contact: Union[Unset, list[int]] = UNSET,
    contact_n: Union[Unset, list[int]] = UNSET,
    contact_group: Union[Unset, list[str]] = UNSET,
    contact_group_n: Union[Unset, list[str]] = UNSET,
    contact_role: Union[Unset, list[int]] = UNSET,
    contact_role_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    desc_units: Union[Unset, bool] = UNSET,
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
    facility_id: Union[Unset, list[str]] = UNSET,
    facility_id_empty: Union[Unset, bool] = UNSET,
    facility_id_ic: Union[Unset, list[str]] = UNSET,
    facility_id_ie: Union[Unset, list[str]] = UNSET,
    facility_id_iew: Union[Unset, list[str]] = UNSET,
    facility_id_isw: Union[Unset, list[str]] = UNSET,
    facility_id_n: Union[Unset, list[str]] = UNSET,
    facility_id_nic: Union[Unset, list[str]] = UNSET,
    facility_id_nie: Union[Unset, list[str]] = UNSET,
    facility_id_niew: Union[Unset, list[str]] = UNSET,
    facility_id_nisw: Union[Unset, list[str]] = UNSET,
    form_factor: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_empty: Union[Unset, bool] = UNSET,
    form_factor_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_n: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    max_weight: Union[Unset, list[int]] = UNSET,
    max_weight_empty: Union[Unset, bool] = UNSET,
    max_weight_gt: Union[Unset, list[int]] = UNSET,
    max_weight_gte: Union[Unset, list[int]] = UNSET,
    max_weight_lt: Union[Unset, list[int]] = UNSET,
    max_weight_lte: Union[Unset, list[int]] = UNSET,
    max_weight_n: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    mounting_depth: Union[Unset, list[int]] = UNSET,
    mounting_depth_empty: Union[Unset, bool] = UNSET,
    mounting_depth_gt: Union[Unset, list[int]] = UNSET,
    mounting_depth_gte: Union[Unset, list[int]] = UNSET,
    mounting_depth_lt: Union[Unset, list[int]] = UNSET,
    mounting_depth_lte: Union[Unset, list[int]] = UNSET,
    mounting_depth_n: Union[Unset, list[int]] = UNSET,
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
    outer_depth: Union[Unset, list[int]] = UNSET,
    outer_depth_empty: Union[Unset, bool] = UNSET,
    outer_depth_gt: Union[Unset, list[int]] = UNSET,
    outer_depth_gte: Union[Unset, list[int]] = UNSET,
    outer_depth_lt: Union[Unset, list[int]] = UNSET,
    outer_depth_lte: Union[Unset, list[int]] = UNSET,
    outer_depth_n: Union[Unset, list[int]] = UNSET,
    outer_height: Union[Unset, list[int]] = UNSET,
    outer_height_empty: Union[Unset, bool] = UNSET,
    outer_height_gt: Union[Unset, list[int]] = UNSET,
    outer_height_gte: Union[Unset, list[int]] = UNSET,
    outer_height_lt: Union[Unset, list[int]] = UNSET,
    outer_height_lte: Union[Unset, list[int]] = UNSET,
    outer_height_n: Union[Unset, list[int]] = UNSET,
    outer_unit: Union[Unset, DcimRacksListOuterUnit] = UNSET,
    outer_width: Union[Unset, list[int]] = UNSET,
    outer_width_empty: Union[Unset, bool] = UNSET,
    outer_width_gt: Union[Unset, list[int]] = UNSET,
    outer_width_gte: Union[Unset, list[int]] = UNSET,
    outer_width_lt: Union[Unset, list[int]] = UNSET,
    outer_width_lte: Union[Unset, list[int]] = UNSET,
    outer_width_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack_type: Union[Unset, list[str]] = UNSET,
    rack_type_n: Union[Unset, list[str]] = UNSET,
    rack_type_id: Union[Unset, list[Union[None, int]]] = UNSET,
    rack_type_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    starting_unit: Union[Unset, list[int]] = UNSET,
    starting_unit_empty: Union[Unset, bool] = UNSET,
    starting_unit_gt: Union[Unset, list[int]] = UNSET,
    starting_unit_gte: Union[Unset, list[int]] = UNSET,
    starting_unit_lt: Union[Unset, list[int]] = UNSET,
    starting_unit_lte: Union[Unset, list[int]] = UNSET,
    starting_unit_n: Union[Unset, list[int]] = UNSET,
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
    u_height: Union[Unset, list[int]] = UNSET,
    u_height_empty: Union[Unset, bool] = UNSET,
    u_height_gt: Union[Unset, list[int]] = UNSET,
    u_height_gte: Union[Unset, list[int]] = UNSET,
    u_height_lt: Union[Unset, list[int]] = UNSET,
    u_height_lte: Union[Unset, list[int]] = UNSET,
    u_height_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    weight: Union[Unset, list[float]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[float]] = UNSET,
    weight_gte: Union[Unset, list[float]] = UNSET,
    weight_lt: Union[Unset, list[float]] = UNSET,
    weight_lte: Union[Unset, list[float]] = UNSET,
    weight_n: Union[Unset, list[float]] = UNSET,
    weight_unit: Union[Unset, DcimRacksListWeightUnit] = UNSET,
    width: Union[Unset, list[int]] = UNSET,
    width_ic: Union[Unset, list[int]] = UNSET,
    width_ie: Union[Unset, list[int]] = UNSET,
    width_iew: Union[Unset, list[int]] = UNSET,
    width_isw: Union[Unset, list[int]] = UNSET,
    width_n: Union[Unset, list[int]] = UNSET,
    width_nic: Union[Unset, list[int]] = UNSET,
    width_nie: Union[Unset, list[int]] = UNSET,
    width_niew: Union[Unset, list[int]] = UNSET,
    width_nisw: Union[Unset, list[int]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_airflow: Union[Unset, str] = UNSET
    if not isinstance(airflow, Unset):
        json_airflow = airflow.value

    params["airflow"] = json_airflow

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

    json_contact: Union[Unset, list[int]] = UNSET
    if not isinstance(contact, Unset):
        json_contact = contact

    params["contact"] = json_contact

    json_contact_n: Union[Unset, list[int]] = UNSET
    if not isinstance(contact_n, Unset):
        json_contact_n = contact_n

    params["contact__n"] = json_contact_n

    json_contact_group: Union[Unset, list[str]] = UNSET
    if not isinstance(contact_group, Unset):
        json_contact_group = contact_group

    params["contact_group"] = json_contact_group

    json_contact_group_n: Union[Unset, list[str]] = UNSET
    if not isinstance(contact_group_n, Unset):
        json_contact_group_n = contact_group_n

    params["contact_group__n"] = json_contact_group_n

    json_contact_role: Union[Unset, list[int]] = UNSET
    if not isinstance(contact_role, Unset):
        json_contact_role = contact_role

    params["contact_role"] = json_contact_role

    json_contact_role_n: Union[Unset, list[int]] = UNSET
    if not isinstance(contact_role_n, Unset):
        json_contact_role_n = contact_role_n

    params["contact_role__n"] = json_contact_role_n

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

    params["desc_units"] = desc_units

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

    json_facility_id: Union[Unset, list[str]] = UNSET
    if not isinstance(facility_id, Unset):
        json_facility_id = facility_id

    params["facility_id"] = json_facility_id

    params["facility_id__empty"] = facility_id_empty

    json_facility_id_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(facility_id_ic, Unset):
        json_facility_id_ic = facility_id_ic

    params["facility_id__ic"] = json_facility_id_ic

    json_facility_id_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(facility_id_ie, Unset):
        json_facility_id_ie = facility_id_ie

    params["facility_id__ie"] = json_facility_id_ie

    json_facility_id_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(facility_id_iew, Unset):
        json_facility_id_iew = facility_id_iew

    params["facility_id__iew"] = json_facility_id_iew

    json_facility_id_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(facility_id_isw, Unset):
        json_facility_id_isw = facility_id_isw

    params["facility_id__isw"] = json_facility_id_isw

    json_facility_id_n: Union[Unset, list[str]] = UNSET
    if not isinstance(facility_id_n, Unset):
        json_facility_id_n = facility_id_n

    params["facility_id__n"] = json_facility_id_n

    json_facility_id_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(facility_id_nic, Unset):
        json_facility_id_nic = facility_id_nic

    params["facility_id__nic"] = json_facility_id_nic

    json_facility_id_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(facility_id_nie, Unset):
        json_facility_id_nie = facility_id_nie

    params["facility_id__nie"] = json_facility_id_nie

    json_facility_id_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(facility_id_niew, Unset):
        json_facility_id_niew = facility_id_niew

    params["facility_id__niew"] = json_facility_id_niew

    json_facility_id_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(facility_id_nisw, Unset):
        json_facility_id_nisw = facility_id_nisw

    params["facility_id__nisw"] = json_facility_id_nisw

    json_form_factor: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(form_factor, Unset):
        json_form_factor = []
        for form_factor_item_data in form_factor:
            form_factor_item: Union[None, str]
            form_factor_item = form_factor_item_data
            json_form_factor.append(form_factor_item)

    params["form_factor"] = json_form_factor

    params["form_factor__empty"] = form_factor_empty

    json_form_factor_ic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(form_factor_ic, Unset):
        json_form_factor_ic = []
        for form_factor_ic_item_data in form_factor_ic:
            form_factor_ic_item: Union[None, str]
            form_factor_ic_item = form_factor_ic_item_data
            json_form_factor_ic.append(form_factor_ic_item)

    params["form_factor__ic"] = json_form_factor_ic

    json_form_factor_ie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(form_factor_ie, Unset):
        json_form_factor_ie = []
        for form_factor_ie_item_data in form_factor_ie:
            form_factor_ie_item: Union[None, str]
            form_factor_ie_item = form_factor_ie_item_data
            json_form_factor_ie.append(form_factor_ie_item)

    params["form_factor__ie"] = json_form_factor_ie

    json_form_factor_iew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(form_factor_iew, Unset):
        json_form_factor_iew = []
        for form_factor_iew_item_data in form_factor_iew:
            form_factor_iew_item: Union[None, str]
            form_factor_iew_item = form_factor_iew_item_data
            json_form_factor_iew.append(form_factor_iew_item)

    params["form_factor__iew"] = json_form_factor_iew

    json_form_factor_isw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(form_factor_isw, Unset):
        json_form_factor_isw = []
        for form_factor_isw_item_data in form_factor_isw:
            form_factor_isw_item: Union[None, str]
            form_factor_isw_item = form_factor_isw_item_data
            json_form_factor_isw.append(form_factor_isw_item)

    params["form_factor__isw"] = json_form_factor_isw

    json_form_factor_n: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(form_factor_n, Unset):
        json_form_factor_n = []
        for form_factor_n_item_data in form_factor_n:
            form_factor_n_item: Union[None, str]
            form_factor_n_item = form_factor_n_item_data
            json_form_factor_n.append(form_factor_n_item)

    params["form_factor__n"] = json_form_factor_n

    json_form_factor_nic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(form_factor_nic, Unset):
        json_form_factor_nic = []
        for form_factor_nic_item_data in form_factor_nic:
            form_factor_nic_item: Union[None, str]
            form_factor_nic_item = form_factor_nic_item_data
            json_form_factor_nic.append(form_factor_nic_item)

    params["form_factor__nic"] = json_form_factor_nic

    json_form_factor_nie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(form_factor_nie, Unset):
        json_form_factor_nie = []
        for form_factor_nie_item_data in form_factor_nie:
            form_factor_nie_item: Union[None, str]
            form_factor_nie_item = form_factor_nie_item_data
            json_form_factor_nie.append(form_factor_nie_item)

    params["form_factor__nie"] = json_form_factor_nie

    json_form_factor_niew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(form_factor_niew, Unset):
        json_form_factor_niew = []
        for form_factor_niew_item_data in form_factor_niew:
            form_factor_niew_item: Union[None, str]
            form_factor_niew_item = form_factor_niew_item_data
            json_form_factor_niew.append(form_factor_niew_item)

    params["form_factor__niew"] = json_form_factor_niew

    json_form_factor_nisw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(form_factor_nisw, Unset):
        json_form_factor_nisw = []
        for form_factor_nisw_item_data in form_factor_nisw:
            form_factor_nisw_item: Union[None, str]
            form_factor_nisw_item = form_factor_nisw_item_data
            json_form_factor_nisw.append(form_factor_nisw_item)

    params["form_factor__nisw"] = json_form_factor_nisw

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

    json_max_weight: Union[Unset, list[int]] = UNSET
    if not isinstance(max_weight, Unset):
        json_max_weight = max_weight

    params["max_weight"] = json_max_weight

    params["max_weight__empty"] = max_weight_empty

    json_max_weight_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(max_weight_gt, Unset):
        json_max_weight_gt = max_weight_gt

    params["max_weight__gt"] = json_max_weight_gt

    json_max_weight_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(max_weight_gte, Unset):
        json_max_weight_gte = max_weight_gte

    params["max_weight__gte"] = json_max_weight_gte

    json_max_weight_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(max_weight_lt, Unset):
        json_max_weight_lt = max_weight_lt

    params["max_weight__lt"] = json_max_weight_lt

    json_max_weight_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(max_weight_lte, Unset):
        json_max_weight_lte = max_weight_lte

    params["max_weight__lte"] = json_max_weight_lte

    json_max_weight_n: Union[Unset, list[int]] = UNSET
    if not isinstance(max_weight_n, Unset):
        json_max_weight_n = max_weight_n

    params["max_weight__n"] = json_max_weight_n

    json_modified_by_request: Union[Unset, str] = UNSET
    if not isinstance(modified_by_request, Unset):
        json_modified_by_request = str(modified_by_request)
    params["modified_by_request"] = json_modified_by_request

    json_mounting_depth: Union[Unset, list[int]] = UNSET
    if not isinstance(mounting_depth, Unset):
        json_mounting_depth = mounting_depth

    params["mounting_depth"] = json_mounting_depth

    params["mounting_depth__empty"] = mounting_depth_empty

    json_mounting_depth_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(mounting_depth_gt, Unset):
        json_mounting_depth_gt = mounting_depth_gt

    params["mounting_depth__gt"] = json_mounting_depth_gt

    json_mounting_depth_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(mounting_depth_gte, Unset):
        json_mounting_depth_gte = mounting_depth_gte

    params["mounting_depth__gte"] = json_mounting_depth_gte

    json_mounting_depth_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(mounting_depth_lt, Unset):
        json_mounting_depth_lt = mounting_depth_lt

    params["mounting_depth__lt"] = json_mounting_depth_lt

    json_mounting_depth_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(mounting_depth_lte, Unset):
        json_mounting_depth_lte = mounting_depth_lte

    params["mounting_depth__lte"] = json_mounting_depth_lte

    json_mounting_depth_n: Union[Unset, list[int]] = UNSET
    if not isinstance(mounting_depth_n, Unset):
        json_mounting_depth_n = mounting_depth_n

    params["mounting_depth__n"] = json_mounting_depth_n

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

    json_outer_depth: Union[Unset, list[int]] = UNSET
    if not isinstance(outer_depth, Unset):
        json_outer_depth = outer_depth

    params["outer_depth"] = json_outer_depth

    params["outer_depth__empty"] = outer_depth_empty

    json_outer_depth_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(outer_depth_gt, Unset):
        json_outer_depth_gt = outer_depth_gt

    params["outer_depth__gt"] = json_outer_depth_gt

    json_outer_depth_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(outer_depth_gte, Unset):
        json_outer_depth_gte = outer_depth_gte

    params["outer_depth__gte"] = json_outer_depth_gte

    json_outer_depth_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(outer_depth_lt, Unset):
        json_outer_depth_lt = outer_depth_lt

    params["outer_depth__lt"] = json_outer_depth_lt

    json_outer_depth_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(outer_depth_lte, Unset):
        json_outer_depth_lte = outer_depth_lte

    params["outer_depth__lte"] = json_outer_depth_lte

    json_outer_depth_n: Union[Unset, list[int]] = UNSET
    if not isinstance(outer_depth_n, Unset):
        json_outer_depth_n = outer_depth_n

    params["outer_depth__n"] = json_outer_depth_n

    json_outer_height: Union[Unset, list[int]] = UNSET
    if not isinstance(outer_height, Unset):
        json_outer_height = outer_height

    params["outer_height"] = json_outer_height

    params["outer_height__empty"] = outer_height_empty

    json_outer_height_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(outer_height_gt, Unset):
        json_outer_height_gt = outer_height_gt

    params["outer_height__gt"] = json_outer_height_gt

    json_outer_height_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(outer_height_gte, Unset):
        json_outer_height_gte = outer_height_gte

    params["outer_height__gte"] = json_outer_height_gte

    json_outer_height_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(outer_height_lt, Unset):
        json_outer_height_lt = outer_height_lt

    params["outer_height__lt"] = json_outer_height_lt

    json_outer_height_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(outer_height_lte, Unset):
        json_outer_height_lte = outer_height_lte

    params["outer_height__lte"] = json_outer_height_lte

    json_outer_height_n: Union[Unset, list[int]] = UNSET
    if not isinstance(outer_height_n, Unset):
        json_outer_height_n = outer_height_n

    params["outer_height__n"] = json_outer_height_n

    json_outer_unit: Union[Unset, str] = UNSET
    if not isinstance(outer_unit, Unset):
        json_outer_unit = outer_unit.value

    params["outer_unit"] = json_outer_unit

    json_outer_width: Union[Unset, list[int]] = UNSET
    if not isinstance(outer_width, Unset):
        json_outer_width = outer_width

    params["outer_width"] = json_outer_width

    params["outer_width__empty"] = outer_width_empty

    json_outer_width_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(outer_width_gt, Unset):
        json_outer_width_gt = outer_width_gt

    params["outer_width__gt"] = json_outer_width_gt

    json_outer_width_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(outer_width_gte, Unset):
        json_outer_width_gte = outer_width_gte

    params["outer_width__gte"] = json_outer_width_gte

    json_outer_width_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(outer_width_lt, Unset):
        json_outer_width_lt = outer_width_lt

    params["outer_width__lt"] = json_outer_width_lt

    json_outer_width_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(outer_width_lte, Unset):
        json_outer_width_lte = outer_width_lte

    params["outer_width__lte"] = json_outer_width_lte

    json_outer_width_n: Union[Unset, list[int]] = UNSET
    if not isinstance(outer_width_n, Unset):
        json_outer_width_n = outer_width_n

    params["outer_width__n"] = json_outer_width_n

    params["q"] = q

    json_rack_type: Union[Unset, list[str]] = UNSET
    if not isinstance(rack_type, Unset):
        json_rack_type = rack_type

    params["rack_type"] = json_rack_type

    json_rack_type_n: Union[Unset, list[str]] = UNSET
    if not isinstance(rack_type_n, Unset):
        json_rack_type_n = rack_type_n

    params["rack_type__n"] = json_rack_type_n

    json_rack_type_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(rack_type_id, Unset):
        json_rack_type_id = []
        for rack_type_id_item_data in rack_type_id:
            rack_type_id_item: Union[None, int]
            rack_type_id_item = rack_type_id_item_data
            json_rack_type_id.append(rack_type_id_item)

    params["rack_type_id"] = json_rack_type_id

    json_rack_type_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(rack_type_id_n, Unset):
        json_rack_type_id_n = []
        for rack_type_id_n_item_data in rack_type_id_n:
            rack_type_id_n_item: Union[None, int]
            rack_type_id_n_item = rack_type_id_n_item_data
            json_rack_type_id_n.append(rack_type_id_n_item)

    params["rack_type_id__n"] = json_rack_type_id_n

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

    json_starting_unit: Union[Unset, list[int]] = UNSET
    if not isinstance(starting_unit, Unset):
        json_starting_unit = starting_unit

    params["starting_unit"] = json_starting_unit

    params["starting_unit__empty"] = starting_unit_empty

    json_starting_unit_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(starting_unit_gt, Unset):
        json_starting_unit_gt = starting_unit_gt

    params["starting_unit__gt"] = json_starting_unit_gt

    json_starting_unit_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(starting_unit_gte, Unset):
        json_starting_unit_gte = starting_unit_gte

    params["starting_unit__gte"] = json_starting_unit_gte

    json_starting_unit_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(starting_unit_lt, Unset):
        json_starting_unit_lt = starting_unit_lt

    params["starting_unit__lt"] = json_starting_unit_lt

    json_starting_unit_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(starting_unit_lte, Unset):
        json_starting_unit_lte = starting_unit_lte

    params["starting_unit__lte"] = json_starting_unit_lte

    json_starting_unit_n: Union[Unset, list[int]] = UNSET
    if not isinstance(starting_unit_n, Unset):
        json_starting_unit_n = starting_unit_n

    params["starting_unit__n"] = json_starting_unit_n

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

    json_u_height: Union[Unset, list[int]] = UNSET
    if not isinstance(u_height, Unset):
        json_u_height = u_height

    params["u_height"] = json_u_height

    params["u_height__empty"] = u_height_empty

    json_u_height_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(u_height_gt, Unset):
        json_u_height_gt = u_height_gt

    params["u_height__gt"] = json_u_height_gt

    json_u_height_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(u_height_gte, Unset):
        json_u_height_gte = u_height_gte

    params["u_height__gte"] = json_u_height_gte

    json_u_height_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(u_height_lt, Unset):
        json_u_height_lt = u_height_lt

    params["u_height__lt"] = json_u_height_lt

    json_u_height_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(u_height_lte, Unset):
        json_u_height_lte = u_height_lte

    params["u_height__lte"] = json_u_height_lte

    json_u_height_n: Union[Unset, list[int]] = UNSET
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

    json_width: Union[Unset, list[int]] = UNSET
    if not isinstance(width, Unset):
        json_width = width

    params["width"] = json_width

    json_width_ic: Union[Unset, list[int]] = UNSET
    if not isinstance(width_ic, Unset):
        json_width_ic = width_ic

    params["width__ic"] = json_width_ic

    json_width_ie: Union[Unset, list[int]] = UNSET
    if not isinstance(width_ie, Unset):
        json_width_ie = width_ie

    params["width__ie"] = json_width_ie

    json_width_iew: Union[Unset, list[int]] = UNSET
    if not isinstance(width_iew, Unset):
        json_width_iew = width_iew

    params["width__iew"] = json_width_iew

    json_width_isw: Union[Unset, list[int]] = UNSET
    if not isinstance(width_isw, Unset):
        json_width_isw = width_isw

    params["width__isw"] = json_width_isw

    json_width_n: Union[Unset, list[int]] = UNSET
    if not isinstance(width_n, Unset):
        json_width_n = width_n

    params["width__n"] = json_width_n

    json_width_nic: Union[Unset, list[int]] = UNSET
    if not isinstance(width_nic, Unset):
        json_width_nic = width_nic

    params["width__nic"] = json_width_nic

    json_width_nie: Union[Unset, list[int]] = UNSET
    if not isinstance(width_nie, Unset):
        json_width_nie = width_nie

    params["width__nie"] = json_width_nie

    json_width_niew: Union[Unset, list[int]] = UNSET
    if not isinstance(width_niew, Unset):
        json_width_niew = width_niew

    params["width__niew"] = json_width_niew

    json_width_nisw: Union[Unset, list[int]] = UNSET
    if not isinstance(width_nisw, Unset):
        json_width_nisw = width_nisw

    params["width__nisw"] = json_width_nisw

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/dcim/racks/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedRackList]:
    if response.status_code == 200:
        response_200 = PaginatedRackList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedRackList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    airflow: Union[Unset, DcimRacksListAirflow] = UNSET,
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
    contact: Union[Unset, list[int]] = UNSET,
    contact_n: Union[Unset, list[int]] = UNSET,
    contact_group: Union[Unset, list[str]] = UNSET,
    contact_group_n: Union[Unset, list[str]] = UNSET,
    contact_role: Union[Unset, list[int]] = UNSET,
    contact_role_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    desc_units: Union[Unset, bool] = UNSET,
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
    facility_id: Union[Unset, list[str]] = UNSET,
    facility_id_empty: Union[Unset, bool] = UNSET,
    facility_id_ic: Union[Unset, list[str]] = UNSET,
    facility_id_ie: Union[Unset, list[str]] = UNSET,
    facility_id_iew: Union[Unset, list[str]] = UNSET,
    facility_id_isw: Union[Unset, list[str]] = UNSET,
    facility_id_n: Union[Unset, list[str]] = UNSET,
    facility_id_nic: Union[Unset, list[str]] = UNSET,
    facility_id_nie: Union[Unset, list[str]] = UNSET,
    facility_id_niew: Union[Unset, list[str]] = UNSET,
    facility_id_nisw: Union[Unset, list[str]] = UNSET,
    form_factor: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_empty: Union[Unset, bool] = UNSET,
    form_factor_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_n: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    max_weight: Union[Unset, list[int]] = UNSET,
    max_weight_empty: Union[Unset, bool] = UNSET,
    max_weight_gt: Union[Unset, list[int]] = UNSET,
    max_weight_gte: Union[Unset, list[int]] = UNSET,
    max_weight_lt: Union[Unset, list[int]] = UNSET,
    max_weight_lte: Union[Unset, list[int]] = UNSET,
    max_weight_n: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    mounting_depth: Union[Unset, list[int]] = UNSET,
    mounting_depth_empty: Union[Unset, bool] = UNSET,
    mounting_depth_gt: Union[Unset, list[int]] = UNSET,
    mounting_depth_gte: Union[Unset, list[int]] = UNSET,
    mounting_depth_lt: Union[Unset, list[int]] = UNSET,
    mounting_depth_lte: Union[Unset, list[int]] = UNSET,
    mounting_depth_n: Union[Unset, list[int]] = UNSET,
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
    outer_depth: Union[Unset, list[int]] = UNSET,
    outer_depth_empty: Union[Unset, bool] = UNSET,
    outer_depth_gt: Union[Unset, list[int]] = UNSET,
    outer_depth_gte: Union[Unset, list[int]] = UNSET,
    outer_depth_lt: Union[Unset, list[int]] = UNSET,
    outer_depth_lte: Union[Unset, list[int]] = UNSET,
    outer_depth_n: Union[Unset, list[int]] = UNSET,
    outer_height: Union[Unset, list[int]] = UNSET,
    outer_height_empty: Union[Unset, bool] = UNSET,
    outer_height_gt: Union[Unset, list[int]] = UNSET,
    outer_height_gte: Union[Unset, list[int]] = UNSET,
    outer_height_lt: Union[Unset, list[int]] = UNSET,
    outer_height_lte: Union[Unset, list[int]] = UNSET,
    outer_height_n: Union[Unset, list[int]] = UNSET,
    outer_unit: Union[Unset, DcimRacksListOuterUnit] = UNSET,
    outer_width: Union[Unset, list[int]] = UNSET,
    outer_width_empty: Union[Unset, bool] = UNSET,
    outer_width_gt: Union[Unset, list[int]] = UNSET,
    outer_width_gte: Union[Unset, list[int]] = UNSET,
    outer_width_lt: Union[Unset, list[int]] = UNSET,
    outer_width_lte: Union[Unset, list[int]] = UNSET,
    outer_width_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack_type: Union[Unset, list[str]] = UNSET,
    rack_type_n: Union[Unset, list[str]] = UNSET,
    rack_type_id: Union[Unset, list[Union[None, int]]] = UNSET,
    rack_type_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    starting_unit: Union[Unset, list[int]] = UNSET,
    starting_unit_empty: Union[Unset, bool] = UNSET,
    starting_unit_gt: Union[Unset, list[int]] = UNSET,
    starting_unit_gte: Union[Unset, list[int]] = UNSET,
    starting_unit_lt: Union[Unset, list[int]] = UNSET,
    starting_unit_lte: Union[Unset, list[int]] = UNSET,
    starting_unit_n: Union[Unset, list[int]] = UNSET,
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
    u_height: Union[Unset, list[int]] = UNSET,
    u_height_empty: Union[Unset, bool] = UNSET,
    u_height_gt: Union[Unset, list[int]] = UNSET,
    u_height_gte: Union[Unset, list[int]] = UNSET,
    u_height_lt: Union[Unset, list[int]] = UNSET,
    u_height_lte: Union[Unset, list[int]] = UNSET,
    u_height_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    weight: Union[Unset, list[float]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[float]] = UNSET,
    weight_gte: Union[Unset, list[float]] = UNSET,
    weight_lt: Union[Unset, list[float]] = UNSET,
    weight_lte: Union[Unset, list[float]] = UNSET,
    weight_n: Union[Unset, list[float]] = UNSET,
    weight_unit: Union[Unset, DcimRacksListWeightUnit] = UNSET,
    width: Union[Unset, list[int]] = UNSET,
    width_ic: Union[Unset, list[int]] = UNSET,
    width_ie: Union[Unset, list[int]] = UNSET,
    width_iew: Union[Unset, list[int]] = UNSET,
    width_isw: Union[Unset, list[int]] = UNSET,
    width_n: Union[Unset, list[int]] = UNSET,
    width_nic: Union[Unset, list[int]] = UNSET,
    width_nie: Union[Unset, list[int]] = UNSET,
    width_niew: Union[Unset, list[int]] = UNSET,
    width_nisw: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedRackList]:
    """Get a list of rack objects.

    Args:
        airflow (Union[Unset, DcimRacksListAirflow]):
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
        contact (Union[Unset, list[int]]):
        contact_n (Union[Unset, list[int]]):
        contact_group (Union[Unset, list[str]]):
        contact_group_n (Union[Unset, list[str]]):
        contact_role (Union[Unset, list[int]]):
        contact_role_n (Union[Unset, list[int]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        desc_units (Union[Unset, bool]):
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
        facility_id (Union[Unset, list[str]]):
        facility_id_empty (Union[Unset, bool]):
        facility_id_ic (Union[Unset, list[str]]):
        facility_id_ie (Union[Unset, list[str]]):
        facility_id_iew (Union[Unset, list[str]]):
        facility_id_isw (Union[Unset, list[str]]):
        facility_id_n (Union[Unset, list[str]]):
        facility_id_nic (Union[Unset, list[str]]):
        facility_id_nie (Union[Unset, list[str]]):
        facility_id_niew (Union[Unset, list[str]]):
        facility_id_nisw (Union[Unset, list[str]]):
        form_factor (Union[Unset, list[Union[None, str]]]):
        form_factor_empty (Union[Unset, bool]):
        form_factor_ic (Union[Unset, list[Union[None, str]]]):
        form_factor_ie (Union[Unset, list[Union[None, str]]]):
        form_factor_iew (Union[Unset, list[Union[None, str]]]):
        form_factor_isw (Union[Unset, list[Union[None, str]]]):
        form_factor_n (Union[Unset, list[Union[None, str]]]):
        form_factor_nic (Union[Unset, list[Union[None, str]]]):
        form_factor_nie (Union[Unset, list[Union[None, str]]]):
        form_factor_niew (Union[Unset, list[Union[None, str]]]):
        form_factor_nisw (Union[Unset, list[Union[None, str]]]):
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
        manufacturer (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_id (Union[Unset, list[int]]):
        manufacturer_id_n (Union[Unset, list[int]]):
        max_weight (Union[Unset, list[int]]):
        max_weight_empty (Union[Unset, bool]):
        max_weight_gt (Union[Unset, list[int]]):
        max_weight_gte (Union[Unset, list[int]]):
        max_weight_lt (Union[Unset, list[int]]):
        max_weight_lte (Union[Unset, list[int]]):
        max_weight_n (Union[Unset, list[int]]):
        modified_by_request (Union[Unset, UUID]):
        mounting_depth (Union[Unset, list[int]]):
        mounting_depth_empty (Union[Unset, bool]):
        mounting_depth_gt (Union[Unset, list[int]]):
        mounting_depth_gte (Union[Unset, list[int]]):
        mounting_depth_lt (Union[Unset, list[int]]):
        mounting_depth_lte (Union[Unset, list[int]]):
        mounting_depth_n (Union[Unset, list[int]]):
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
        outer_depth (Union[Unset, list[int]]):
        outer_depth_empty (Union[Unset, bool]):
        outer_depth_gt (Union[Unset, list[int]]):
        outer_depth_gte (Union[Unset, list[int]]):
        outer_depth_lt (Union[Unset, list[int]]):
        outer_depth_lte (Union[Unset, list[int]]):
        outer_depth_n (Union[Unset, list[int]]):
        outer_height (Union[Unset, list[int]]):
        outer_height_empty (Union[Unset, bool]):
        outer_height_gt (Union[Unset, list[int]]):
        outer_height_gte (Union[Unset, list[int]]):
        outer_height_lt (Union[Unset, list[int]]):
        outer_height_lte (Union[Unset, list[int]]):
        outer_height_n (Union[Unset, list[int]]):
        outer_unit (Union[Unset, DcimRacksListOuterUnit]):
        outer_width (Union[Unset, list[int]]):
        outer_width_empty (Union[Unset, bool]):
        outer_width_gt (Union[Unset, list[int]]):
        outer_width_gte (Union[Unset, list[int]]):
        outer_width_lt (Union[Unset, list[int]]):
        outer_width_lte (Union[Unset, list[int]]):
        outer_width_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        rack_type (Union[Unset, list[str]]):
        rack_type_n (Union[Unset, list[str]]):
        rack_type_id (Union[Unset, list[Union[None, int]]]):
        rack_type_id_n (Union[Unset, list[Union[None, int]]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[Union[None, int]]]):
        role_id_n (Union[Unset, list[Union[None, int]]]):
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
        starting_unit (Union[Unset, list[int]]):
        starting_unit_empty (Union[Unset, bool]):
        starting_unit_gt (Union[Unset, list[int]]):
        starting_unit_gte (Union[Unset, list[int]]):
        starting_unit_lt (Union[Unset, list[int]]):
        starting_unit_lte (Union[Unset, list[int]]):
        starting_unit_n (Union[Unset, list[int]]):
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
        u_height (Union[Unset, list[int]]):
        u_height_empty (Union[Unset, bool]):
        u_height_gt (Union[Unset, list[int]]):
        u_height_gte (Union[Unset, list[int]]):
        u_height_lt (Union[Unset, list[int]]):
        u_height_lte (Union[Unset, list[int]]):
        u_height_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        weight (Union[Unset, list[float]]):
        weight_empty (Union[Unset, bool]):
        weight_gt (Union[Unset, list[float]]):
        weight_gte (Union[Unset, list[float]]):
        weight_lt (Union[Unset, list[float]]):
        weight_lte (Union[Unset, list[float]]):
        weight_n (Union[Unset, list[float]]):
        weight_unit (Union[Unset, DcimRacksListWeightUnit]):
        width (Union[Unset, list[int]]):
        width_ic (Union[Unset, list[int]]):
        width_ie (Union[Unset, list[int]]):
        width_iew (Union[Unset, list[int]]):
        width_isw (Union[Unset, list[int]]):
        width_n (Union[Unset, list[int]]):
        width_nic (Union[Unset, list[int]]):
        width_nie (Union[Unset, list[int]]):
        width_niew (Union[Unset, list[int]]):
        width_nisw (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRackList]
    """

    kwargs = _get_kwargs(
        airflow=airflow,
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
        contact=contact,
        contact_n=contact_n,
        contact_group=contact_group,
        contact_group_n=contact_group_n,
        contact_role=contact_role,
        contact_role_n=contact_role_n,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        desc_units=desc_units,
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
        facility_id=facility_id,
        facility_id_empty=facility_id_empty,
        facility_id_ic=facility_id_ic,
        facility_id_ie=facility_id_ie,
        facility_id_iew=facility_id_iew,
        facility_id_isw=facility_id_isw,
        facility_id_n=facility_id_n,
        facility_id_nic=facility_id_nic,
        facility_id_nie=facility_id_nie,
        facility_id_niew=facility_id_niew,
        facility_id_nisw=facility_id_nisw,
        form_factor=form_factor,
        form_factor_empty=form_factor_empty,
        form_factor_ic=form_factor_ic,
        form_factor_ie=form_factor_ie,
        form_factor_iew=form_factor_iew,
        form_factor_isw=form_factor_isw,
        form_factor_n=form_factor_n,
        form_factor_nic=form_factor_nic,
        form_factor_nie=form_factor_nie,
        form_factor_niew=form_factor_niew,
        form_factor_nisw=form_factor_nisw,
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
        max_weight=max_weight,
        max_weight_empty=max_weight_empty,
        max_weight_gt=max_weight_gt,
        max_weight_gte=max_weight_gte,
        max_weight_lt=max_weight_lt,
        max_weight_lte=max_weight_lte,
        max_weight_n=max_weight_n,
        modified_by_request=modified_by_request,
        mounting_depth=mounting_depth,
        mounting_depth_empty=mounting_depth_empty,
        mounting_depth_gt=mounting_depth_gt,
        mounting_depth_gte=mounting_depth_gte,
        mounting_depth_lt=mounting_depth_lt,
        mounting_depth_lte=mounting_depth_lte,
        mounting_depth_n=mounting_depth_n,
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
        outer_depth=outer_depth,
        outer_depth_empty=outer_depth_empty,
        outer_depth_gt=outer_depth_gt,
        outer_depth_gte=outer_depth_gte,
        outer_depth_lt=outer_depth_lt,
        outer_depth_lte=outer_depth_lte,
        outer_depth_n=outer_depth_n,
        outer_height=outer_height,
        outer_height_empty=outer_height_empty,
        outer_height_gt=outer_height_gt,
        outer_height_gte=outer_height_gte,
        outer_height_lt=outer_height_lt,
        outer_height_lte=outer_height_lte,
        outer_height_n=outer_height_n,
        outer_unit=outer_unit,
        outer_width=outer_width,
        outer_width_empty=outer_width_empty,
        outer_width_gt=outer_width_gt,
        outer_width_gte=outer_width_gte,
        outer_width_lt=outer_width_lt,
        outer_width_lte=outer_width_lte,
        outer_width_n=outer_width_n,
        q=q,
        rack_type=rack_type,
        rack_type_n=rack_type_n,
        rack_type_id=rack_type_id,
        rack_type_id_n=rack_type_id_n,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
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
        starting_unit=starting_unit,
        starting_unit_empty=starting_unit_empty,
        starting_unit_gt=starting_unit_gt,
        starting_unit_gte=starting_unit_gte,
        starting_unit_lt=starting_unit_lt,
        starting_unit_lte=starting_unit_lte,
        starting_unit_n=starting_unit_n,
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
        width=width,
        width_ic=width_ic,
        width_ie=width_ie,
        width_iew=width_iew,
        width_isw=width_isw,
        width_n=width_n,
        width_nic=width_nic,
        width_nie=width_nie,
        width_niew=width_niew,
        width_nisw=width_nisw,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    airflow: Union[Unset, DcimRacksListAirflow] = UNSET,
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
    contact: Union[Unset, list[int]] = UNSET,
    contact_n: Union[Unset, list[int]] = UNSET,
    contact_group: Union[Unset, list[str]] = UNSET,
    contact_group_n: Union[Unset, list[str]] = UNSET,
    contact_role: Union[Unset, list[int]] = UNSET,
    contact_role_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    desc_units: Union[Unset, bool] = UNSET,
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
    facility_id: Union[Unset, list[str]] = UNSET,
    facility_id_empty: Union[Unset, bool] = UNSET,
    facility_id_ic: Union[Unset, list[str]] = UNSET,
    facility_id_ie: Union[Unset, list[str]] = UNSET,
    facility_id_iew: Union[Unset, list[str]] = UNSET,
    facility_id_isw: Union[Unset, list[str]] = UNSET,
    facility_id_n: Union[Unset, list[str]] = UNSET,
    facility_id_nic: Union[Unset, list[str]] = UNSET,
    facility_id_nie: Union[Unset, list[str]] = UNSET,
    facility_id_niew: Union[Unset, list[str]] = UNSET,
    facility_id_nisw: Union[Unset, list[str]] = UNSET,
    form_factor: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_empty: Union[Unset, bool] = UNSET,
    form_factor_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_n: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    max_weight: Union[Unset, list[int]] = UNSET,
    max_weight_empty: Union[Unset, bool] = UNSET,
    max_weight_gt: Union[Unset, list[int]] = UNSET,
    max_weight_gte: Union[Unset, list[int]] = UNSET,
    max_weight_lt: Union[Unset, list[int]] = UNSET,
    max_weight_lte: Union[Unset, list[int]] = UNSET,
    max_weight_n: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    mounting_depth: Union[Unset, list[int]] = UNSET,
    mounting_depth_empty: Union[Unset, bool] = UNSET,
    mounting_depth_gt: Union[Unset, list[int]] = UNSET,
    mounting_depth_gte: Union[Unset, list[int]] = UNSET,
    mounting_depth_lt: Union[Unset, list[int]] = UNSET,
    mounting_depth_lte: Union[Unset, list[int]] = UNSET,
    mounting_depth_n: Union[Unset, list[int]] = UNSET,
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
    outer_depth: Union[Unset, list[int]] = UNSET,
    outer_depth_empty: Union[Unset, bool] = UNSET,
    outer_depth_gt: Union[Unset, list[int]] = UNSET,
    outer_depth_gte: Union[Unset, list[int]] = UNSET,
    outer_depth_lt: Union[Unset, list[int]] = UNSET,
    outer_depth_lte: Union[Unset, list[int]] = UNSET,
    outer_depth_n: Union[Unset, list[int]] = UNSET,
    outer_height: Union[Unset, list[int]] = UNSET,
    outer_height_empty: Union[Unset, bool] = UNSET,
    outer_height_gt: Union[Unset, list[int]] = UNSET,
    outer_height_gte: Union[Unset, list[int]] = UNSET,
    outer_height_lt: Union[Unset, list[int]] = UNSET,
    outer_height_lte: Union[Unset, list[int]] = UNSET,
    outer_height_n: Union[Unset, list[int]] = UNSET,
    outer_unit: Union[Unset, DcimRacksListOuterUnit] = UNSET,
    outer_width: Union[Unset, list[int]] = UNSET,
    outer_width_empty: Union[Unset, bool] = UNSET,
    outer_width_gt: Union[Unset, list[int]] = UNSET,
    outer_width_gte: Union[Unset, list[int]] = UNSET,
    outer_width_lt: Union[Unset, list[int]] = UNSET,
    outer_width_lte: Union[Unset, list[int]] = UNSET,
    outer_width_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack_type: Union[Unset, list[str]] = UNSET,
    rack_type_n: Union[Unset, list[str]] = UNSET,
    rack_type_id: Union[Unset, list[Union[None, int]]] = UNSET,
    rack_type_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    starting_unit: Union[Unset, list[int]] = UNSET,
    starting_unit_empty: Union[Unset, bool] = UNSET,
    starting_unit_gt: Union[Unset, list[int]] = UNSET,
    starting_unit_gte: Union[Unset, list[int]] = UNSET,
    starting_unit_lt: Union[Unset, list[int]] = UNSET,
    starting_unit_lte: Union[Unset, list[int]] = UNSET,
    starting_unit_n: Union[Unset, list[int]] = UNSET,
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
    u_height: Union[Unset, list[int]] = UNSET,
    u_height_empty: Union[Unset, bool] = UNSET,
    u_height_gt: Union[Unset, list[int]] = UNSET,
    u_height_gte: Union[Unset, list[int]] = UNSET,
    u_height_lt: Union[Unset, list[int]] = UNSET,
    u_height_lte: Union[Unset, list[int]] = UNSET,
    u_height_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    weight: Union[Unset, list[float]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[float]] = UNSET,
    weight_gte: Union[Unset, list[float]] = UNSET,
    weight_lt: Union[Unset, list[float]] = UNSET,
    weight_lte: Union[Unset, list[float]] = UNSET,
    weight_n: Union[Unset, list[float]] = UNSET,
    weight_unit: Union[Unset, DcimRacksListWeightUnit] = UNSET,
    width: Union[Unset, list[int]] = UNSET,
    width_ic: Union[Unset, list[int]] = UNSET,
    width_ie: Union[Unset, list[int]] = UNSET,
    width_iew: Union[Unset, list[int]] = UNSET,
    width_isw: Union[Unset, list[int]] = UNSET,
    width_n: Union[Unset, list[int]] = UNSET,
    width_nic: Union[Unset, list[int]] = UNSET,
    width_nie: Union[Unset, list[int]] = UNSET,
    width_niew: Union[Unset, list[int]] = UNSET,
    width_nisw: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedRackList]:
    """Get a list of rack objects.

    Args:
        airflow (Union[Unset, DcimRacksListAirflow]):
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
        contact (Union[Unset, list[int]]):
        contact_n (Union[Unset, list[int]]):
        contact_group (Union[Unset, list[str]]):
        contact_group_n (Union[Unset, list[str]]):
        contact_role (Union[Unset, list[int]]):
        contact_role_n (Union[Unset, list[int]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        desc_units (Union[Unset, bool]):
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
        facility_id (Union[Unset, list[str]]):
        facility_id_empty (Union[Unset, bool]):
        facility_id_ic (Union[Unset, list[str]]):
        facility_id_ie (Union[Unset, list[str]]):
        facility_id_iew (Union[Unset, list[str]]):
        facility_id_isw (Union[Unset, list[str]]):
        facility_id_n (Union[Unset, list[str]]):
        facility_id_nic (Union[Unset, list[str]]):
        facility_id_nie (Union[Unset, list[str]]):
        facility_id_niew (Union[Unset, list[str]]):
        facility_id_nisw (Union[Unset, list[str]]):
        form_factor (Union[Unset, list[Union[None, str]]]):
        form_factor_empty (Union[Unset, bool]):
        form_factor_ic (Union[Unset, list[Union[None, str]]]):
        form_factor_ie (Union[Unset, list[Union[None, str]]]):
        form_factor_iew (Union[Unset, list[Union[None, str]]]):
        form_factor_isw (Union[Unset, list[Union[None, str]]]):
        form_factor_n (Union[Unset, list[Union[None, str]]]):
        form_factor_nic (Union[Unset, list[Union[None, str]]]):
        form_factor_nie (Union[Unset, list[Union[None, str]]]):
        form_factor_niew (Union[Unset, list[Union[None, str]]]):
        form_factor_nisw (Union[Unset, list[Union[None, str]]]):
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
        manufacturer (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_id (Union[Unset, list[int]]):
        manufacturer_id_n (Union[Unset, list[int]]):
        max_weight (Union[Unset, list[int]]):
        max_weight_empty (Union[Unset, bool]):
        max_weight_gt (Union[Unset, list[int]]):
        max_weight_gte (Union[Unset, list[int]]):
        max_weight_lt (Union[Unset, list[int]]):
        max_weight_lte (Union[Unset, list[int]]):
        max_weight_n (Union[Unset, list[int]]):
        modified_by_request (Union[Unset, UUID]):
        mounting_depth (Union[Unset, list[int]]):
        mounting_depth_empty (Union[Unset, bool]):
        mounting_depth_gt (Union[Unset, list[int]]):
        mounting_depth_gte (Union[Unset, list[int]]):
        mounting_depth_lt (Union[Unset, list[int]]):
        mounting_depth_lte (Union[Unset, list[int]]):
        mounting_depth_n (Union[Unset, list[int]]):
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
        outer_depth (Union[Unset, list[int]]):
        outer_depth_empty (Union[Unset, bool]):
        outer_depth_gt (Union[Unset, list[int]]):
        outer_depth_gte (Union[Unset, list[int]]):
        outer_depth_lt (Union[Unset, list[int]]):
        outer_depth_lte (Union[Unset, list[int]]):
        outer_depth_n (Union[Unset, list[int]]):
        outer_height (Union[Unset, list[int]]):
        outer_height_empty (Union[Unset, bool]):
        outer_height_gt (Union[Unset, list[int]]):
        outer_height_gte (Union[Unset, list[int]]):
        outer_height_lt (Union[Unset, list[int]]):
        outer_height_lte (Union[Unset, list[int]]):
        outer_height_n (Union[Unset, list[int]]):
        outer_unit (Union[Unset, DcimRacksListOuterUnit]):
        outer_width (Union[Unset, list[int]]):
        outer_width_empty (Union[Unset, bool]):
        outer_width_gt (Union[Unset, list[int]]):
        outer_width_gte (Union[Unset, list[int]]):
        outer_width_lt (Union[Unset, list[int]]):
        outer_width_lte (Union[Unset, list[int]]):
        outer_width_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        rack_type (Union[Unset, list[str]]):
        rack_type_n (Union[Unset, list[str]]):
        rack_type_id (Union[Unset, list[Union[None, int]]]):
        rack_type_id_n (Union[Unset, list[Union[None, int]]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[Union[None, int]]]):
        role_id_n (Union[Unset, list[Union[None, int]]]):
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
        starting_unit (Union[Unset, list[int]]):
        starting_unit_empty (Union[Unset, bool]):
        starting_unit_gt (Union[Unset, list[int]]):
        starting_unit_gte (Union[Unset, list[int]]):
        starting_unit_lt (Union[Unset, list[int]]):
        starting_unit_lte (Union[Unset, list[int]]):
        starting_unit_n (Union[Unset, list[int]]):
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
        u_height (Union[Unset, list[int]]):
        u_height_empty (Union[Unset, bool]):
        u_height_gt (Union[Unset, list[int]]):
        u_height_gte (Union[Unset, list[int]]):
        u_height_lt (Union[Unset, list[int]]):
        u_height_lte (Union[Unset, list[int]]):
        u_height_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        weight (Union[Unset, list[float]]):
        weight_empty (Union[Unset, bool]):
        weight_gt (Union[Unset, list[float]]):
        weight_gte (Union[Unset, list[float]]):
        weight_lt (Union[Unset, list[float]]):
        weight_lte (Union[Unset, list[float]]):
        weight_n (Union[Unset, list[float]]):
        weight_unit (Union[Unset, DcimRacksListWeightUnit]):
        width (Union[Unset, list[int]]):
        width_ic (Union[Unset, list[int]]):
        width_ie (Union[Unset, list[int]]):
        width_iew (Union[Unset, list[int]]):
        width_isw (Union[Unset, list[int]]):
        width_n (Union[Unset, list[int]]):
        width_nic (Union[Unset, list[int]]):
        width_nie (Union[Unset, list[int]]):
        width_niew (Union[Unset, list[int]]):
        width_nisw (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRackList
    """

    return sync_detailed(
        client=client,
        airflow=airflow,
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
        contact=contact,
        contact_n=contact_n,
        contact_group=contact_group,
        contact_group_n=contact_group_n,
        contact_role=contact_role,
        contact_role_n=contact_role_n,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        desc_units=desc_units,
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
        facility_id=facility_id,
        facility_id_empty=facility_id_empty,
        facility_id_ic=facility_id_ic,
        facility_id_ie=facility_id_ie,
        facility_id_iew=facility_id_iew,
        facility_id_isw=facility_id_isw,
        facility_id_n=facility_id_n,
        facility_id_nic=facility_id_nic,
        facility_id_nie=facility_id_nie,
        facility_id_niew=facility_id_niew,
        facility_id_nisw=facility_id_nisw,
        form_factor=form_factor,
        form_factor_empty=form_factor_empty,
        form_factor_ic=form_factor_ic,
        form_factor_ie=form_factor_ie,
        form_factor_iew=form_factor_iew,
        form_factor_isw=form_factor_isw,
        form_factor_n=form_factor_n,
        form_factor_nic=form_factor_nic,
        form_factor_nie=form_factor_nie,
        form_factor_niew=form_factor_niew,
        form_factor_nisw=form_factor_nisw,
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
        max_weight=max_weight,
        max_weight_empty=max_weight_empty,
        max_weight_gt=max_weight_gt,
        max_weight_gte=max_weight_gte,
        max_weight_lt=max_weight_lt,
        max_weight_lte=max_weight_lte,
        max_weight_n=max_weight_n,
        modified_by_request=modified_by_request,
        mounting_depth=mounting_depth,
        mounting_depth_empty=mounting_depth_empty,
        mounting_depth_gt=mounting_depth_gt,
        mounting_depth_gte=mounting_depth_gte,
        mounting_depth_lt=mounting_depth_lt,
        mounting_depth_lte=mounting_depth_lte,
        mounting_depth_n=mounting_depth_n,
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
        outer_depth=outer_depth,
        outer_depth_empty=outer_depth_empty,
        outer_depth_gt=outer_depth_gt,
        outer_depth_gte=outer_depth_gte,
        outer_depth_lt=outer_depth_lt,
        outer_depth_lte=outer_depth_lte,
        outer_depth_n=outer_depth_n,
        outer_height=outer_height,
        outer_height_empty=outer_height_empty,
        outer_height_gt=outer_height_gt,
        outer_height_gte=outer_height_gte,
        outer_height_lt=outer_height_lt,
        outer_height_lte=outer_height_lte,
        outer_height_n=outer_height_n,
        outer_unit=outer_unit,
        outer_width=outer_width,
        outer_width_empty=outer_width_empty,
        outer_width_gt=outer_width_gt,
        outer_width_gte=outer_width_gte,
        outer_width_lt=outer_width_lt,
        outer_width_lte=outer_width_lte,
        outer_width_n=outer_width_n,
        q=q,
        rack_type=rack_type,
        rack_type_n=rack_type_n,
        rack_type_id=rack_type_id,
        rack_type_id_n=rack_type_id_n,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
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
        starting_unit=starting_unit,
        starting_unit_empty=starting_unit_empty,
        starting_unit_gt=starting_unit_gt,
        starting_unit_gte=starting_unit_gte,
        starting_unit_lt=starting_unit_lt,
        starting_unit_lte=starting_unit_lte,
        starting_unit_n=starting_unit_n,
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
        width=width,
        width_ic=width_ic,
        width_ie=width_ie,
        width_iew=width_iew,
        width_isw=width_isw,
        width_n=width_n,
        width_nic=width_nic,
        width_nie=width_nie,
        width_niew=width_niew,
        width_nisw=width_nisw,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    airflow: Union[Unset, DcimRacksListAirflow] = UNSET,
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
    contact: Union[Unset, list[int]] = UNSET,
    contact_n: Union[Unset, list[int]] = UNSET,
    contact_group: Union[Unset, list[str]] = UNSET,
    contact_group_n: Union[Unset, list[str]] = UNSET,
    contact_role: Union[Unset, list[int]] = UNSET,
    contact_role_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    desc_units: Union[Unset, bool] = UNSET,
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
    facility_id: Union[Unset, list[str]] = UNSET,
    facility_id_empty: Union[Unset, bool] = UNSET,
    facility_id_ic: Union[Unset, list[str]] = UNSET,
    facility_id_ie: Union[Unset, list[str]] = UNSET,
    facility_id_iew: Union[Unset, list[str]] = UNSET,
    facility_id_isw: Union[Unset, list[str]] = UNSET,
    facility_id_n: Union[Unset, list[str]] = UNSET,
    facility_id_nic: Union[Unset, list[str]] = UNSET,
    facility_id_nie: Union[Unset, list[str]] = UNSET,
    facility_id_niew: Union[Unset, list[str]] = UNSET,
    facility_id_nisw: Union[Unset, list[str]] = UNSET,
    form_factor: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_empty: Union[Unset, bool] = UNSET,
    form_factor_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_n: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    max_weight: Union[Unset, list[int]] = UNSET,
    max_weight_empty: Union[Unset, bool] = UNSET,
    max_weight_gt: Union[Unset, list[int]] = UNSET,
    max_weight_gte: Union[Unset, list[int]] = UNSET,
    max_weight_lt: Union[Unset, list[int]] = UNSET,
    max_weight_lte: Union[Unset, list[int]] = UNSET,
    max_weight_n: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    mounting_depth: Union[Unset, list[int]] = UNSET,
    mounting_depth_empty: Union[Unset, bool] = UNSET,
    mounting_depth_gt: Union[Unset, list[int]] = UNSET,
    mounting_depth_gte: Union[Unset, list[int]] = UNSET,
    mounting_depth_lt: Union[Unset, list[int]] = UNSET,
    mounting_depth_lte: Union[Unset, list[int]] = UNSET,
    mounting_depth_n: Union[Unset, list[int]] = UNSET,
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
    outer_depth: Union[Unset, list[int]] = UNSET,
    outer_depth_empty: Union[Unset, bool] = UNSET,
    outer_depth_gt: Union[Unset, list[int]] = UNSET,
    outer_depth_gte: Union[Unset, list[int]] = UNSET,
    outer_depth_lt: Union[Unset, list[int]] = UNSET,
    outer_depth_lte: Union[Unset, list[int]] = UNSET,
    outer_depth_n: Union[Unset, list[int]] = UNSET,
    outer_height: Union[Unset, list[int]] = UNSET,
    outer_height_empty: Union[Unset, bool] = UNSET,
    outer_height_gt: Union[Unset, list[int]] = UNSET,
    outer_height_gte: Union[Unset, list[int]] = UNSET,
    outer_height_lt: Union[Unset, list[int]] = UNSET,
    outer_height_lte: Union[Unset, list[int]] = UNSET,
    outer_height_n: Union[Unset, list[int]] = UNSET,
    outer_unit: Union[Unset, DcimRacksListOuterUnit] = UNSET,
    outer_width: Union[Unset, list[int]] = UNSET,
    outer_width_empty: Union[Unset, bool] = UNSET,
    outer_width_gt: Union[Unset, list[int]] = UNSET,
    outer_width_gte: Union[Unset, list[int]] = UNSET,
    outer_width_lt: Union[Unset, list[int]] = UNSET,
    outer_width_lte: Union[Unset, list[int]] = UNSET,
    outer_width_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack_type: Union[Unset, list[str]] = UNSET,
    rack_type_n: Union[Unset, list[str]] = UNSET,
    rack_type_id: Union[Unset, list[Union[None, int]]] = UNSET,
    rack_type_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    starting_unit: Union[Unset, list[int]] = UNSET,
    starting_unit_empty: Union[Unset, bool] = UNSET,
    starting_unit_gt: Union[Unset, list[int]] = UNSET,
    starting_unit_gte: Union[Unset, list[int]] = UNSET,
    starting_unit_lt: Union[Unset, list[int]] = UNSET,
    starting_unit_lte: Union[Unset, list[int]] = UNSET,
    starting_unit_n: Union[Unset, list[int]] = UNSET,
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
    u_height: Union[Unset, list[int]] = UNSET,
    u_height_empty: Union[Unset, bool] = UNSET,
    u_height_gt: Union[Unset, list[int]] = UNSET,
    u_height_gte: Union[Unset, list[int]] = UNSET,
    u_height_lt: Union[Unset, list[int]] = UNSET,
    u_height_lte: Union[Unset, list[int]] = UNSET,
    u_height_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    weight: Union[Unset, list[float]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[float]] = UNSET,
    weight_gte: Union[Unset, list[float]] = UNSET,
    weight_lt: Union[Unset, list[float]] = UNSET,
    weight_lte: Union[Unset, list[float]] = UNSET,
    weight_n: Union[Unset, list[float]] = UNSET,
    weight_unit: Union[Unset, DcimRacksListWeightUnit] = UNSET,
    width: Union[Unset, list[int]] = UNSET,
    width_ic: Union[Unset, list[int]] = UNSET,
    width_ie: Union[Unset, list[int]] = UNSET,
    width_iew: Union[Unset, list[int]] = UNSET,
    width_isw: Union[Unset, list[int]] = UNSET,
    width_n: Union[Unset, list[int]] = UNSET,
    width_nic: Union[Unset, list[int]] = UNSET,
    width_nie: Union[Unset, list[int]] = UNSET,
    width_niew: Union[Unset, list[int]] = UNSET,
    width_nisw: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedRackList]:
    """Get a list of rack objects.

    Args:
        airflow (Union[Unset, DcimRacksListAirflow]):
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
        contact (Union[Unset, list[int]]):
        contact_n (Union[Unset, list[int]]):
        contact_group (Union[Unset, list[str]]):
        contact_group_n (Union[Unset, list[str]]):
        contact_role (Union[Unset, list[int]]):
        contact_role_n (Union[Unset, list[int]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        desc_units (Union[Unset, bool]):
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
        facility_id (Union[Unset, list[str]]):
        facility_id_empty (Union[Unset, bool]):
        facility_id_ic (Union[Unset, list[str]]):
        facility_id_ie (Union[Unset, list[str]]):
        facility_id_iew (Union[Unset, list[str]]):
        facility_id_isw (Union[Unset, list[str]]):
        facility_id_n (Union[Unset, list[str]]):
        facility_id_nic (Union[Unset, list[str]]):
        facility_id_nie (Union[Unset, list[str]]):
        facility_id_niew (Union[Unset, list[str]]):
        facility_id_nisw (Union[Unset, list[str]]):
        form_factor (Union[Unset, list[Union[None, str]]]):
        form_factor_empty (Union[Unset, bool]):
        form_factor_ic (Union[Unset, list[Union[None, str]]]):
        form_factor_ie (Union[Unset, list[Union[None, str]]]):
        form_factor_iew (Union[Unset, list[Union[None, str]]]):
        form_factor_isw (Union[Unset, list[Union[None, str]]]):
        form_factor_n (Union[Unset, list[Union[None, str]]]):
        form_factor_nic (Union[Unset, list[Union[None, str]]]):
        form_factor_nie (Union[Unset, list[Union[None, str]]]):
        form_factor_niew (Union[Unset, list[Union[None, str]]]):
        form_factor_nisw (Union[Unset, list[Union[None, str]]]):
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
        manufacturer (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_id (Union[Unset, list[int]]):
        manufacturer_id_n (Union[Unset, list[int]]):
        max_weight (Union[Unset, list[int]]):
        max_weight_empty (Union[Unset, bool]):
        max_weight_gt (Union[Unset, list[int]]):
        max_weight_gte (Union[Unset, list[int]]):
        max_weight_lt (Union[Unset, list[int]]):
        max_weight_lte (Union[Unset, list[int]]):
        max_weight_n (Union[Unset, list[int]]):
        modified_by_request (Union[Unset, UUID]):
        mounting_depth (Union[Unset, list[int]]):
        mounting_depth_empty (Union[Unset, bool]):
        mounting_depth_gt (Union[Unset, list[int]]):
        mounting_depth_gte (Union[Unset, list[int]]):
        mounting_depth_lt (Union[Unset, list[int]]):
        mounting_depth_lte (Union[Unset, list[int]]):
        mounting_depth_n (Union[Unset, list[int]]):
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
        outer_depth (Union[Unset, list[int]]):
        outer_depth_empty (Union[Unset, bool]):
        outer_depth_gt (Union[Unset, list[int]]):
        outer_depth_gte (Union[Unset, list[int]]):
        outer_depth_lt (Union[Unset, list[int]]):
        outer_depth_lte (Union[Unset, list[int]]):
        outer_depth_n (Union[Unset, list[int]]):
        outer_height (Union[Unset, list[int]]):
        outer_height_empty (Union[Unset, bool]):
        outer_height_gt (Union[Unset, list[int]]):
        outer_height_gte (Union[Unset, list[int]]):
        outer_height_lt (Union[Unset, list[int]]):
        outer_height_lte (Union[Unset, list[int]]):
        outer_height_n (Union[Unset, list[int]]):
        outer_unit (Union[Unset, DcimRacksListOuterUnit]):
        outer_width (Union[Unset, list[int]]):
        outer_width_empty (Union[Unset, bool]):
        outer_width_gt (Union[Unset, list[int]]):
        outer_width_gte (Union[Unset, list[int]]):
        outer_width_lt (Union[Unset, list[int]]):
        outer_width_lte (Union[Unset, list[int]]):
        outer_width_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        rack_type (Union[Unset, list[str]]):
        rack_type_n (Union[Unset, list[str]]):
        rack_type_id (Union[Unset, list[Union[None, int]]]):
        rack_type_id_n (Union[Unset, list[Union[None, int]]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[Union[None, int]]]):
        role_id_n (Union[Unset, list[Union[None, int]]]):
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
        starting_unit (Union[Unset, list[int]]):
        starting_unit_empty (Union[Unset, bool]):
        starting_unit_gt (Union[Unset, list[int]]):
        starting_unit_gte (Union[Unset, list[int]]):
        starting_unit_lt (Union[Unset, list[int]]):
        starting_unit_lte (Union[Unset, list[int]]):
        starting_unit_n (Union[Unset, list[int]]):
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
        u_height (Union[Unset, list[int]]):
        u_height_empty (Union[Unset, bool]):
        u_height_gt (Union[Unset, list[int]]):
        u_height_gte (Union[Unset, list[int]]):
        u_height_lt (Union[Unset, list[int]]):
        u_height_lte (Union[Unset, list[int]]):
        u_height_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        weight (Union[Unset, list[float]]):
        weight_empty (Union[Unset, bool]):
        weight_gt (Union[Unset, list[float]]):
        weight_gte (Union[Unset, list[float]]):
        weight_lt (Union[Unset, list[float]]):
        weight_lte (Union[Unset, list[float]]):
        weight_n (Union[Unset, list[float]]):
        weight_unit (Union[Unset, DcimRacksListWeightUnit]):
        width (Union[Unset, list[int]]):
        width_ic (Union[Unset, list[int]]):
        width_ie (Union[Unset, list[int]]):
        width_iew (Union[Unset, list[int]]):
        width_isw (Union[Unset, list[int]]):
        width_n (Union[Unset, list[int]]):
        width_nic (Union[Unset, list[int]]):
        width_nie (Union[Unset, list[int]]):
        width_niew (Union[Unset, list[int]]):
        width_nisw (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRackList]
    """

    kwargs = _get_kwargs(
        airflow=airflow,
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
        contact=contact,
        contact_n=contact_n,
        contact_group=contact_group,
        contact_group_n=contact_group_n,
        contact_role=contact_role,
        contact_role_n=contact_role_n,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        desc_units=desc_units,
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
        facility_id=facility_id,
        facility_id_empty=facility_id_empty,
        facility_id_ic=facility_id_ic,
        facility_id_ie=facility_id_ie,
        facility_id_iew=facility_id_iew,
        facility_id_isw=facility_id_isw,
        facility_id_n=facility_id_n,
        facility_id_nic=facility_id_nic,
        facility_id_nie=facility_id_nie,
        facility_id_niew=facility_id_niew,
        facility_id_nisw=facility_id_nisw,
        form_factor=form_factor,
        form_factor_empty=form_factor_empty,
        form_factor_ic=form_factor_ic,
        form_factor_ie=form_factor_ie,
        form_factor_iew=form_factor_iew,
        form_factor_isw=form_factor_isw,
        form_factor_n=form_factor_n,
        form_factor_nic=form_factor_nic,
        form_factor_nie=form_factor_nie,
        form_factor_niew=form_factor_niew,
        form_factor_nisw=form_factor_nisw,
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
        max_weight=max_weight,
        max_weight_empty=max_weight_empty,
        max_weight_gt=max_weight_gt,
        max_weight_gte=max_weight_gte,
        max_weight_lt=max_weight_lt,
        max_weight_lte=max_weight_lte,
        max_weight_n=max_weight_n,
        modified_by_request=modified_by_request,
        mounting_depth=mounting_depth,
        mounting_depth_empty=mounting_depth_empty,
        mounting_depth_gt=mounting_depth_gt,
        mounting_depth_gte=mounting_depth_gte,
        mounting_depth_lt=mounting_depth_lt,
        mounting_depth_lte=mounting_depth_lte,
        mounting_depth_n=mounting_depth_n,
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
        outer_depth=outer_depth,
        outer_depth_empty=outer_depth_empty,
        outer_depth_gt=outer_depth_gt,
        outer_depth_gte=outer_depth_gte,
        outer_depth_lt=outer_depth_lt,
        outer_depth_lte=outer_depth_lte,
        outer_depth_n=outer_depth_n,
        outer_height=outer_height,
        outer_height_empty=outer_height_empty,
        outer_height_gt=outer_height_gt,
        outer_height_gte=outer_height_gte,
        outer_height_lt=outer_height_lt,
        outer_height_lte=outer_height_lte,
        outer_height_n=outer_height_n,
        outer_unit=outer_unit,
        outer_width=outer_width,
        outer_width_empty=outer_width_empty,
        outer_width_gt=outer_width_gt,
        outer_width_gte=outer_width_gte,
        outer_width_lt=outer_width_lt,
        outer_width_lte=outer_width_lte,
        outer_width_n=outer_width_n,
        q=q,
        rack_type=rack_type,
        rack_type_n=rack_type_n,
        rack_type_id=rack_type_id,
        rack_type_id_n=rack_type_id_n,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
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
        starting_unit=starting_unit,
        starting_unit_empty=starting_unit_empty,
        starting_unit_gt=starting_unit_gt,
        starting_unit_gte=starting_unit_gte,
        starting_unit_lt=starting_unit_lt,
        starting_unit_lte=starting_unit_lte,
        starting_unit_n=starting_unit_n,
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
        width=width,
        width_ic=width_ic,
        width_ie=width_ie,
        width_iew=width_iew,
        width_isw=width_isw,
        width_n=width_n,
        width_nic=width_nic,
        width_nie=width_nie,
        width_niew=width_niew,
        width_nisw=width_nisw,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    airflow: Union[Unset, DcimRacksListAirflow] = UNSET,
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
    contact: Union[Unset, list[int]] = UNSET,
    contact_n: Union[Unset, list[int]] = UNSET,
    contact_group: Union[Unset, list[str]] = UNSET,
    contact_group_n: Union[Unset, list[str]] = UNSET,
    contact_role: Union[Unset, list[int]] = UNSET,
    contact_role_n: Union[Unset, list[int]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    desc_units: Union[Unset, bool] = UNSET,
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
    facility_id: Union[Unset, list[str]] = UNSET,
    facility_id_empty: Union[Unset, bool] = UNSET,
    facility_id_ic: Union[Unset, list[str]] = UNSET,
    facility_id_ie: Union[Unset, list[str]] = UNSET,
    facility_id_iew: Union[Unset, list[str]] = UNSET,
    facility_id_isw: Union[Unset, list[str]] = UNSET,
    facility_id_n: Union[Unset, list[str]] = UNSET,
    facility_id_nic: Union[Unset, list[str]] = UNSET,
    facility_id_nie: Union[Unset, list[str]] = UNSET,
    facility_id_niew: Union[Unset, list[str]] = UNSET,
    facility_id_nisw: Union[Unset, list[str]] = UNSET,
    form_factor: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_empty: Union[Unset, bool] = UNSET,
    form_factor_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_n: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    form_factor_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_id: Union[Unset, list[int]] = UNSET,
    manufacturer_id_n: Union[Unset, list[int]] = UNSET,
    max_weight: Union[Unset, list[int]] = UNSET,
    max_weight_empty: Union[Unset, bool] = UNSET,
    max_weight_gt: Union[Unset, list[int]] = UNSET,
    max_weight_gte: Union[Unset, list[int]] = UNSET,
    max_weight_lt: Union[Unset, list[int]] = UNSET,
    max_weight_lte: Union[Unset, list[int]] = UNSET,
    max_weight_n: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    mounting_depth: Union[Unset, list[int]] = UNSET,
    mounting_depth_empty: Union[Unset, bool] = UNSET,
    mounting_depth_gt: Union[Unset, list[int]] = UNSET,
    mounting_depth_gte: Union[Unset, list[int]] = UNSET,
    mounting_depth_lt: Union[Unset, list[int]] = UNSET,
    mounting_depth_lte: Union[Unset, list[int]] = UNSET,
    mounting_depth_n: Union[Unset, list[int]] = UNSET,
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
    outer_depth: Union[Unset, list[int]] = UNSET,
    outer_depth_empty: Union[Unset, bool] = UNSET,
    outer_depth_gt: Union[Unset, list[int]] = UNSET,
    outer_depth_gte: Union[Unset, list[int]] = UNSET,
    outer_depth_lt: Union[Unset, list[int]] = UNSET,
    outer_depth_lte: Union[Unset, list[int]] = UNSET,
    outer_depth_n: Union[Unset, list[int]] = UNSET,
    outer_height: Union[Unset, list[int]] = UNSET,
    outer_height_empty: Union[Unset, bool] = UNSET,
    outer_height_gt: Union[Unset, list[int]] = UNSET,
    outer_height_gte: Union[Unset, list[int]] = UNSET,
    outer_height_lt: Union[Unset, list[int]] = UNSET,
    outer_height_lte: Union[Unset, list[int]] = UNSET,
    outer_height_n: Union[Unset, list[int]] = UNSET,
    outer_unit: Union[Unset, DcimRacksListOuterUnit] = UNSET,
    outer_width: Union[Unset, list[int]] = UNSET,
    outer_width_empty: Union[Unset, bool] = UNSET,
    outer_width_gt: Union[Unset, list[int]] = UNSET,
    outer_width_gte: Union[Unset, list[int]] = UNSET,
    outer_width_lt: Union[Unset, list[int]] = UNSET,
    outer_width_lte: Union[Unset, list[int]] = UNSET,
    outer_width_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack_type: Union[Unset, list[str]] = UNSET,
    rack_type_n: Union[Unset, list[str]] = UNSET,
    rack_type_id: Union[Unset, list[Union[None, int]]] = UNSET,
    rack_type_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[Union[None, int]]] = UNSET,
    role_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    starting_unit: Union[Unset, list[int]] = UNSET,
    starting_unit_empty: Union[Unset, bool] = UNSET,
    starting_unit_gt: Union[Unset, list[int]] = UNSET,
    starting_unit_gte: Union[Unset, list[int]] = UNSET,
    starting_unit_lt: Union[Unset, list[int]] = UNSET,
    starting_unit_lte: Union[Unset, list[int]] = UNSET,
    starting_unit_n: Union[Unset, list[int]] = UNSET,
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
    u_height: Union[Unset, list[int]] = UNSET,
    u_height_empty: Union[Unset, bool] = UNSET,
    u_height_gt: Union[Unset, list[int]] = UNSET,
    u_height_gte: Union[Unset, list[int]] = UNSET,
    u_height_lt: Union[Unset, list[int]] = UNSET,
    u_height_lte: Union[Unset, list[int]] = UNSET,
    u_height_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    weight: Union[Unset, list[float]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[float]] = UNSET,
    weight_gte: Union[Unset, list[float]] = UNSET,
    weight_lt: Union[Unset, list[float]] = UNSET,
    weight_lte: Union[Unset, list[float]] = UNSET,
    weight_n: Union[Unset, list[float]] = UNSET,
    weight_unit: Union[Unset, DcimRacksListWeightUnit] = UNSET,
    width: Union[Unset, list[int]] = UNSET,
    width_ic: Union[Unset, list[int]] = UNSET,
    width_ie: Union[Unset, list[int]] = UNSET,
    width_iew: Union[Unset, list[int]] = UNSET,
    width_isw: Union[Unset, list[int]] = UNSET,
    width_n: Union[Unset, list[int]] = UNSET,
    width_nic: Union[Unset, list[int]] = UNSET,
    width_nie: Union[Unset, list[int]] = UNSET,
    width_niew: Union[Unset, list[int]] = UNSET,
    width_nisw: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedRackList]:
    """Get a list of rack objects.

    Args:
        airflow (Union[Unset, DcimRacksListAirflow]):
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
        contact (Union[Unset, list[int]]):
        contact_n (Union[Unset, list[int]]):
        contact_group (Union[Unset, list[str]]):
        contact_group_n (Union[Unset, list[str]]):
        contact_role (Union[Unset, list[int]]):
        contact_role_n (Union[Unset, list[int]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        desc_units (Union[Unset, bool]):
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
        facility_id (Union[Unset, list[str]]):
        facility_id_empty (Union[Unset, bool]):
        facility_id_ic (Union[Unset, list[str]]):
        facility_id_ie (Union[Unset, list[str]]):
        facility_id_iew (Union[Unset, list[str]]):
        facility_id_isw (Union[Unset, list[str]]):
        facility_id_n (Union[Unset, list[str]]):
        facility_id_nic (Union[Unset, list[str]]):
        facility_id_nie (Union[Unset, list[str]]):
        facility_id_niew (Union[Unset, list[str]]):
        facility_id_nisw (Union[Unset, list[str]]):
        form_factor (Union[Unset, list[Union[None, str]]]):
        form_factor_empty (Union[Unset, bool]):
        form_factor_ic (Union[Unset, list[Union[None, str]]]):
        form_factor_ie (Union[Unset, list[Union[None, str]]]):
        form_factor_iew (Union[Unset, list[Union[None, str]]]):
        form_factor_isw (Union[Unset, list[Union[None, str]]]):
        form_factor_n (Union[Unset, list[Union[None, str]]]):
        form_factor_nic (Union[Unset, list[Union[None, str]]]):
        form_factor_nie (Union[Unset, list[Union[None, str]]]):
        form_factor_niew (Union[Unset, list[Union[None, str]]]):
        form_factor_nisw (Union[Unset, list[Union[None, str]]]):
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
        manufacturer (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_id (Union[Unset, list[int]]):
        manufacturer_id_n (Union[Unset, list[int]]):
        max_weight (Union[Unset, list[int]]):
        max_weight_empty (Union[Unset, bool]):
        max_weight_gt (Union[Unset, list[int]]):
        max_weight_gte (Union[Unset, list[int]]):
        max_weight_lt (Union[Unset, list[int]]):
        max_weight_lte (Union[Unset, list[int]]):
        max_weight_n (Union[Unset, list[int]]):
        modified_by_request (Union[Unset, UUID]):
        mounting_depth (Union[Unset, list[int]]):
        mounting_depth_empty (Union[Unset, bool]):
        mounting_depth_gt (Union[Unset, list[int]]):
        mounting_depth_gte (Union[Unset, list[int]]):
        mounting_depth_lt (Union[Unset, list[int]]):
        mounting_depth_lte (Union[Unset, list[int]]):
        mounting_depth_n (Union[Unset, list[int]]):
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
        outer_depth (Union[Unset, list[int]]):
        outer_depth_empty (Union[Unset, bool]):
        outer_depth_gt (Union[Unset, list[int]]):
        outer_depth_gte (Union[Unset, list[int]]):
        outer_depth_lt (Union[Unset, list[int]]):
        outer_depth_lte (Union[Unset, list[int]]):
        outer_depth_n (Union[Unset, list[int]]):
        outer_height (Union[Unset, list[int]]):
        outer_height_empty (Union[Unset, bool]):
        outer_height_gt (Union[Unset, list[int]]):
        outer_height_gte (Union[Unset, list[int]]):
        outer_height_lt (Union[Unset, list[int]]):
        outer_height_lte (Union[Unset, list[int]]):
        outer_height_n (Union[Unset, list[int]]):
        outer_unit (Union[Unset, DcimRacksListOuterUnit]):
        outer_width (Union[Unset, list[int]]):
        outer_width_empty (Union[Unset, bool]):
        outer_width_gt (Union[Unset, list[int]]):
        outer_width_gte (Union[Unset, list[int]]):
        outer_width_lt (Union[Unset, list[int]]):
        outer_width_lte (Union[Unset, list[int]]):
        outer_width_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        rack_type (Union[Unset, list[str]]):
        rack_type_n (Union[Unset, list[str]]):
        rack_type_id (Union[Unset, list[Union[None, int]]]):
        rack_type_id_n (Union[Unset, list[Union[None, int]]]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[Union[None, int]]]):
        role_id_n (Union[Unset, list[Union[None, int]]]):
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
        starting_unit (Union[Unset, list[int]]):
        starting_unit_empty (Union[Unset, bool]):
        starting_unit_gt (Union[Unset, list[int]]):
        starting_unit_gte (Union[Unset, list[int]]):
        starting_unit_lt (Union[Unset, list[int]]):
        starting_unit_lte (Union[Unset, list[int]]):
        starting_unit_n (Union[Unset, list[int]]):
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
        u_height (Union[Unset, list[int]]):
        u_height_empty (Union[Unset, bool]):
        u_height_gt (Union[Unset, list[int]]):
        u_height_gte (Union[Unset, list[int]]):
        u_height_lt (Union[Unset, list[int]]):
        u_height_lte (Union[Unset, list[int]]):
        u_height_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        weight (Union[Unset, list[float]]):
        weight_empty (Union[Unset, bool]):
        weight_gt (Union[Unset, list[float]]):
        weight_gte (Union[Unset, list[float]]):
        weight_lt (Union[Unset, list[float]]):
        weight_lte (Union[Unset, list[float]]):
        weight_n (Union[Unset, list[float]]):
        weight_unit (Union[Unset, DcimRacksListWeightUnit]):
        width (Union[Unset, list[int]]):
        width_ic (Union[Unset, list[int]]):
        width_ie (Union[Unset, list[int]]):
        width_iew (Union[Unset, list[int]]):
        width_isw (Union[Unset, list[int]]):
        width_n (Union[Unset, list[int]]):
        width_nic (Union[Unset, list[int]]):
        width_nie (Union[Unset, list[int]]):
        width_niew (Union[Unset, list[int]]):
        width_nisw (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRackList
    """

    return (
        await asyncio_detailed(
            client=client,
            airflow=airflow,
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
            contact=contact,
            contact_n=contact_n,
            contact_group=contact_group,
            contact_group_n=contact_group_n,
            contact_role=contact_role,
            contact_role_n=contact_role_n,
            created=created,
            created_empty=created_empty,
            created_gt=created_gt,
            created_gte=created_gte,
            created_lt=created_lt,
            created_lte=created_lte,
            created_n=created_n,
            created_by_request=created_by_request,
            desc_units=desc_units,
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
            facility_id=facility_id,
            facility_id_empty=facility_id_empty,
            facility_id_ic=facility_id_ic,
            facility_id_ie=facility_id_ie,
            facility_id_iew=facility_id_iew,
            facility_id_isw=facility_id_isw,
            facility_id_n=facility_id_n,
            facility_id_nic=facility_id_nic,
            facility_id_nie=facility_id_nie,
            facility_id_niew=facility_id_niew,
            facility_id_nisw=facility_id_nisw,
            form_factor=form_factor,
            form_factor_empty=form_factor_empty,
            form_factor_ic=form_factor_ic,
            form_factor_ie=form_factor_ie,
            form_factor_iew=form_factor_iew,
            form_factor_isw=form_factor_isw,
            form_factor_n=form_factor_n,
            form_factor_nic=form_factor_nic,
            form_factor_nie=form_factor_nie,
            form_factor_niew=form_factor_niew,
            form_factor_nisw=form_factor_nisw,
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
            max_weight=max_weight,
            max_weight_empty=max_weight_empty,
            max_weight_gt=max_weight_gt,
            max_weight_gte=max_weight_gte,
            max_weight_lt=max_weight_lt,
            max_weight_lte=max_weight_lte,
            max_weight_n=max_weight_n,
            modified_by_request=modified_by_request,
            mounting_depth=mounting_depth,
            mounting_depth_empty=mounting_depth_empty,
            mounting_depth_gt=mounting_depth_gt,
            mounting_depth_gte=mounting_depth_gte,
            mounting_depth_lt=mounting_depth_lt,
            mounting_depth_lte=mounting_depth_lte,
            mounting_depth_n=mounting_depth_n,
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
            outer_depth=outer_depth,
            outer_depth_empty=outer_depth_empty,
            outer_depth_gt=outer_depth_gt,
            outer_depth_gte=outer_depth_gte,
            outer_depth_lt=outer_depth_lt,
            outer_depth_lte=outer_depth_lte,
            outer_depth_n=outer_depth_n,
            outer_height=outer_height,
            outer_height_empty=outer_height_empty,
            outer_height_gt=outer_height_gt,
            outer_height_gte=outer_height_gte,
            outer_height_lt=outer_height_lt,
            outer_height_lte=outer_height_lte,
            outer_height_n=outer_height_n,
            outer_unit=outer_unit,
            outer_width=outer_width,
            outer_width_empty=outer_width_empty,
            outer_width_gt=outer_width_gt,
            outer_width_gte=outer_width_gte,
            outer_width_lt=outer_width_lt,
            outer_width_lte=outer_width_lte,
            outer_width_n=outer_width_n,
            q=q,
            rack_type=rack_type,
            rack_type_n=rack_type_n,
            rack_type_id=rack_type_id,
            rack_type_id_n=rack_type_id_n,
            region=region,
            region_n=region_n,
            region_id=region_id,
            region_id_n=region_id_n,
            role=role,
            role_n=role_n,
            role_id=role_id,
            role_id_n=role_id_n,
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
            starting_unit=starting_unit,
            starting_unit_empty=starting_unit_empty,
            starting_unit_gt=starting_unit_gt,
            starting_unit_gte=starting_unit_gte,
            starting_unit_lt=starting_unit_lt,
            starting_unit_lte=starting_unit_lte,
            starting_unit_n=starting_unit_n,
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
            width=width,
            width_ic=width_ic,
            width_ie=width_ie,
            width_iew=width_iew,
            width_isw=width_isw,
            width_n=width_n,
            width_nic=width_nic,
            width_nie=width_nie,
            width_niew=width_niew,
            width_nisw=width_nisw,
        )
    ).parsed
