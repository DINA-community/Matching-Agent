import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dcim_rack_types_list_outer_unit import DcimRackTypesListOuterUnit
from ...models.dcim_rack_types_list_weight_unit import DcimRackTypesListWeightUnit
from ...models.paginated_rack_type_list import PaginatedRackTypeList
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
    form_factor: Union[Unset, list[str]] = UNSET,
    form_factor_empty: Union[Unset, bool] = UNSET,
    form_factor_ic: Union[Unset, list[str]] = UNSET,
    form_factor_ie: Union[Unset, list[str]] = UNSET,
    form_factor_iew: Union[Unset, list[str]] = UNSET,
    form_factor_isw: Union[Unset, list[str]] = UNSET,
    form_factor_n: Union[Unset, list[str]] = UNSET,
    form_factor_nic: Union[Unset, list[str]] = UNSET,
    form_factor_nie: Union[Unset, list[str]] = UNSET,
    form_factor_niew: Union[Unset, list[str]] = UNSET,
    form_factor_nisw: Union[Unset, list[str]] = UNSET,
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
    mounting_depth: Union[Unset, list[int]] = UNSET,
    mounting_depth_empty: Union[Unset, bool] = UNSET,
    mounting_depth_gt: Union[Unset, list[int]] = UNSET,
    mounting_depth_gte: Union[Unset, list[int]] = UNSET,
    mounting_depth_lt: Union[Unset, list[int]] = UNSET,
    mounting_depth_lte: Union[Unset, list[int]] = UNSET,
    mounting_depth_n: Union[Unset, list[int]] = UNSET,
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
    outer_unit: Union[Unset, DcimRackTypesListOuterUnit] = UNSET,
    outer_width: Union[Unset, list[int]] = UNSET,
    outer_width_empty: Union[Unset, bool] = UNSET,
    outer_width_gt: Union[Unset, list[int]] = UNSET,
    outer_width_gte: Union[Unset, list[int]] = UNSET,
    outer_width_lt: Union[Unset, list[int]] = UNSET,
    outer_width_lte: Union[Unset, list[int]] = UNSET,
    outer_width_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
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
    starting_unit: Union[Unset, list[int]] = UNSET,
    starting_unit_empty: Union[Unset, bool] = UNSET,
    starting_unit_gt: Union[Unset, list[int]] = UNSET,
    starting_unit_gte: Union[Unset, list[int]] = UNSET,
    starting_unit_lt: Union[Unset, list[int]] = UNSET,
    starting_unit_lte: Union[Unset, list[int]] = UNSET,
    starting_unit_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
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
    weight_unit: Union[Unset, DcimRackTypesListWeightUnit] = UNSET,
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

    json_form_factor: Union[Unset, list[str]] = UNSET
    if not isinstance(form_factor, Unset):
        json_form_factor = form_factor

    params["form_factor"] = json_form_factor

    params["form_factor__empty"] = form_factor_empty

    json_form_factor_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(form_factor_ic, Unset):
        json_form_factor_ic = form_factor_ic

    params["form_factor__ic"] = json_form_factor_ic

    json_form_factor_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(form_factor_ie, Unset):
        json_form_factor_ie = form_factor_ie

    params["form_factor__ie"] = json_form_factor_ie

    json_form_factor_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(form_factor_iew, Unset):
        json_form_factor_iew = form_factor_iew

    params["form_factor__iew"] = json_form_factor_iew

    json_form_factor_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(form_factor_isw, Unset):
        json_form_factor_isw = form_factor_isw

    params["form_factor__isw"] = json_form_factor_isw

    json_form_factor_n: Union[Unset, list[str]] = UNSET
    if not isinstance(form_factor_n, Unset):
        json_form_factor_n = form_factor_n

    params["form_factor__n"] = json_form_factor_n

    json_form_factor_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(form_factor_nic, Unset):
        json_form_factor_nic = form_factor_nic

    params["form_factor__nic"] = json_form_factor_nic

    json_form_factor_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(form_factor_nie, Unset):
        json_form_factor_nie = form_factor_nie

    params["form_factor__nie"] = json_form_factor_nie

    json_form_factor_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(form_factor_niew, Unset):
        json_form_factor_niew = form_factor_niew

    params["form_factor__niew"] = json_form_factor_niew

    json_form_factor_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(form_factor_nisw, Unset):
        json_form_factor_nisw = form_factor_nisw

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
        "url": "/api/dcim/rack-types/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedRackTypeList]:
    if response.status_code == 200:
        response_200 = PaginatedRackTypeList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedRackTypeList]:
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
    form_factor: Union[Unset, list[str]] = UNSET,
    form_factor_empty: Union[Unset, bool] = UNSET,
    form_factor_ic: Union[Unset, list[str]] = UNSET,
    form_factor_ie: Union[Unset, list[str]] = UNSET,
    form_factor_iew: Union[Unset, list[str]] = UNSET,
    form_factor_isw: Union[Unset, list[str]] = UNSET,
    form_factor_n: Union[Unset, list[str]] = UNSET,
    form_factor_nic: Union[Unset, list[str]] = UNSET,
    form_factor_nie: Union[Unset, list[str]] = UNSET,
    form_factor_niew: Union[Unset, list[str]] = UNSET,
    form_factor_nisw: Union[Unset, list[str]] = UNSET,
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
    mounting_depth: Union[Unset, list[int]] = UNSET,
    mounting_depth_empty: Union[Unset, bool] = UNSET,
    mounting_depth_gt: Union[Unset, list[int]] = UNSET,
    mounting_depth_gte: Union[Unset, list[int]] = UNSET,
    mounting_depth_lt: Union[Unset, list[int]] = UNSET,
    mounting_depth_lte: Union[Unset, list[int]] = UNSET,
    mounting_depth_n: Union[Unset, list[int]] = UNSET,
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
    outer_unit: Union[Unset, DcimRackTypesListOuterUnit] = UNSET,
    outer_width: Union[Unset, list[int]] = UNSET,
    outer_width_empty: Union[Unset, bool] = UNSET,
    outer_width_gt: Union[Unset, list[int]] = UNSET,
    outer_width_gte: Union[Unset, list[int]] = UNSET,
    outer_width_lt: Union[Unset, list[int]] = UNSET,
    outer_width_lte: Union[Unset, list[int]] = UNSET,
    outer_width_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
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
    starting_unit: Union[Unset, list[int]] = UNSET,
    starting_unit_empty: Union[Unset, bool] = UNSET,
    starting_unit_gt: Union[Unset, list[int]] = UNSET,
    starting_unit_gte: Union[Unset, list[int]] = UNSET,
    starting_unit_lt: Union[Unset, list[int]] = UNSET,
    starting_unit_lte: Union[Unset, list[int]] = UNSET,
    starting_unit_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
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
    weight_unit: Union[Unset, DcimRackTypesListWeightUnit] = UNSET,
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
) -> Response[PaginatedRackTypeList]:
    """Get a list of rack type objects.

    Args:
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
        form_factor (Union[Unset, list[str]]):
        form_factor_empty (Union[Unset, bool]):
        form_factor_ic (Union[Unset, list[str]]):
        form_factor_ie (Union[Unset, list[str]]):
        form_factor_iew (Union[Unset, list[str]]):
        form_factor_isw (Union[Unset, list[str]]):
        form_factor_n (Union[Unset, list[str]]):
        form_factor_nic (Union[Unset, list[str]]):
        form_factor_nie (Union[Unset, list[str]]):
        form_factor_niew (Union[Unset, list[str]]):
        form_factor_nisw (Union[Unset, list[str]]):
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
        mounting_depth (Union[Unset, list[int]]):
        mounting_depth_empty (Union[Unset, bool]):
        mounting_depth_gt (Union[Unset, list[int]]):
        mounting_depth_gte (Union[Unset, list[int]]):
        mounting_depth_lt (Union[Unset, list[int]]):
        mounting_depth_lte (Union[Unset, list[int]]):
        mounting_depth_n (Union[Unset, list[int]]):
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
        outer_unit (Union[Unset, DcimRackTypesListOuterUnit]):
        outer_width (Union[Unset, list[int]]):
        outer_width_empty (Union[Unset, bool]):
        outer_width_gt (Union[Unset, list[int]]):
        outer_width_gte (Union[Unset, list[int]]):
        outer_width_lt (Union[Unset, list[int]]):
        outer_width_lte (Union[Unset, list[int]]):
        outer_width_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
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
        starting_unit (Union[Unset, list[int]]):
        starting_unit_empty (Union[Unset, bool]):
        starting_unit_gt (Union[Unset, list[int]]):
        starting_unit_gte (Union[Unset, list[int]]):
        starting_unit_lt (Union[Unset, list[int]]):
        starting_unit_lte (Union[Unset, list[int]]):
        starting_unit_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
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
        weight_unit (Union[Unset, DcimRackTypesListWeightUnit]):
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
        Response[PaginatedRackTypeList]
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
        mounting_depth=mounting_depth,
        mounting_depth_empty=mounting_depth_empty,
        mounting_depth_gt=mounting_depth_gt,
        mounting_depth_gte=mounting_depth_gte,
        mounting_depth_lt=mounting_depth_lt,
        mounting_depth_lte=mounting_depth_lte,
        mounting_depth_n=mounting_depth_n,
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
        starting_unit=starting_unit,
        starting_unit_empty=starting_unit_empty,
        starting_unit_gt=starting_unit_gt,
        starting_unit_gte=starting_unit_gte,
        starting_unit_lt=starting_unit_lt,
        starting_unit_lte=starting_unit_lte,
        starting_unit_n=starting_unit_n,
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
    form_factor: Union[Unset, list[str]] = UNSET,
    form_factor_empty: Union[Unset, bool] = UNSET,
    form_factor_ic: Union[Unset, list[str]] = UNSET,
    form_factor_ie: Union[Unset, list[str]] = UNSET,
    form_factor_iew: Union[Unset, list[str]] = UNSET,
    form_factor_isw: Union[Unset, list[str]] = UNSET,
    form_factor_n: Union[Unset, list[str]] = UNSET,
    form_factor_nic: Union[Unset, list[str]] = UNSET,
    form_factor_nie: Union[Unset, list[str]] = UNSET,
    form_factor_niew: Union[Unset, list[str]] = UNSET,
    form_factor_nisw: Union[Unset, list[str]] = UNSET,
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
    mounting_depth: Union[Unset, list[int]] = UNSET,
    mounting_depth_empty: Union[Unset, bool] = UNSET,
    mounting_depth_gt: Union[Unset, list[int]] = UNSET,
    mounting_depth_gte: Union[Unset, list[int]] = UNSET,
    mounting_depth_lt: Union[Unset, list[int]] = UNSET,
    mounting_depth_lte: Union[Unset, list[int]] = UNSET,
    mounting_depth_n: Union[Unset, list[int]] = UNSET,
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
    outer_unit: Union[Unset, DcimRackTypesListOuterUnit] = UNSET,
    outer_width: Union[Unset, list[int]] = UNSET,
    outer_width_empty: Union[Unset, bool] = UNSET,
    outer_width_gt: Union[Unset, list[int]] = UNSET,
    outer_width_gte: Union[Unset, list[int]] = UNSET,
    outer_width_lt: Union[Unset, list[int]] = UNSET,
    outer_width_lte: Union[Unset, list[int]] = UNSET,
    outer_width_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
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
    starting_unit: Union[Unset, list[int]] = UNSET,
    starting_unit_empty: Union[Unset, bool] = UNSET,
    starting_unit_gt: Union[Unset, list[int]] = UNSET,
    starting_unit_gte: Union[Unset, list[int]] = UNSET,
    starting_unit_lt: Union[Unset, list[int]] = UNSET,
    starting_unit_lte: Union[Unset, list[int]] = UNSET,
    starting_unit_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
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
    weight_unit: Union[Unset, DcimRackTypesListWeightUnit] = UNSET,
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
) -> Optional[PaginatedRackTypeList]:
    """Get a list of rack type objects.

    Args:
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
        form_factor (Union[Unset, list[str]]):
        form_factor_empty (Union[Unset, bool]):
        form_factor_ic (Union[Unset, list[str]]):
        form_factor_ie (Union[Unset, list[str]]):
        form_factor_iew (Union[Unset, list[str]]):
        form_factor_isw (Union[Unset, list[str]]):
        form_factor_n (Union[Unset, list[str]]):
        form_factor_nic (Union[Unset, list[str]]):
        form_factor_nie (Union[Unset, list[str]]):
        form_factor_niew (Union[Unset, list[str]]):
        form_factor_nisw (Union[Unset, list[str]]):
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
        mounting_depth (Union[Unset, list[int]]):
        mounting_depth_empty (Union[Unset, bool]):
        mounting_depth_gt (Union[Unset, list[int]]):
        mounting_depth_gte (Union[Unset, list[int]]):
        mounting_depth_lt (Union[Unset, list[int]]):
        mounting_depth_lte (Union[Unset, list[int]]):
        mounting_depth_n (Union[Unset, list[int]]):
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
        outer_unit (Union[Unset, DcimRackTypesListOuterUnit]):
        outer_width (Union[Unset, list[int]]):
        outer_width_empty (Union[Unset, bool]):
        outer_width_gt (Union[Unset, list[int]]):
        outer_width_gte (Union[Unset, list[int]]):
        outer_width_lt (Union[Unset, list[int]]):
        outer_width_lte (Union[Unset, list[int]]):
        outer_width_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
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
        starting_unit (Union[Unset, list[int]]):
        starting_unit_empty (Union[Unset, bool]):
        starting_unit_gt (Union[Unset, list[int]]):
        starting_unit_gte (Union[Unset, list[int]]):
        starting_unit_lt (Union[Unset, list[int]]):
        starting_unit_lte (Union[Unset, list[int]]):
        starting_unit_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
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
        weight_unit (Union[Unset, DcimRackTypesListWeightUnit]):
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
        PaginatedRackTypeList
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
        mounting_depth=mounting_depth,
        mounting_depth_empty=mounting_depth_empty,
        mounting_depth_gt=mounting_depth_gt,
        mounting_depth_gte=mounting_depth_gte,
        mounting_depth_lt=mounting_depth_lt,
        mounting_depth_lte=mounting_depth_lte,
        mounting_depth_n=mounting_depth_n,
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
        starting_unit=starting_unit,
        starting_unit_empty=starting_unit_empty,
        starting_unit_gt=starting_unit_gt,
        starting_unit_gte=starting_unit_gte,
        starting_unit_lt=starting_unit_lt,
        starting_unit_lte=starting_unit_lte,
        starting_unit_n=starting_unit_n,
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
    form_factor: Union[Unset, list[str]] = UNSET,
    form_factor_empty: Union[Unset, bool] = UNSET,
    form_factor_ic: Union[Unset, list[str]] = UNSET,
    form_factor_ie: Union[Unset, list[str]] = UNSET,
    form_factor_iew: Union[Unset, list[str]] = UNSET,
    form_factor_isw: Union[Unset, list[str]] = UNSET,
    form_factor_n: Union[Unset, list[str]] = UNSET,
    form_factor_nic: Union[Unset, list[str]] = UNSET,
    form_factor_nie: Union[Unset, list[str]] = UNSET,
    form_factor_niew: Union[Unset, list[str]] = UNSET,
    form_factor_nisw: Union[Unset, list[str]] = UNSET,
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
    mounting_depth: Union[Unset, list[int]] = UNSET,
    mounting_depth_empty: Union[Unset, bool] = UNSET,
    mounting_depth_gt: Union[Unset, list[int]] = UNSET,
    mounting_depth_gte: Union[Unset, list[int]] = UNSET,
    mounting_depth_lt: Union[Unset, list[int]] = UNSET,
    mounting_depth_lte: Union[Unset, list[int]] = UNSET,
    mounting_depth_n: Union[Unset, list[int]] = UNSET,
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
    outer_unit: Union[Unset, DcimRackTypesListOuterUnit] = UNSET,
    outer_width: Union[Unset, list[int]] = UNSET,
    outer_width_empty: Union[Unset, bool] = UNSET,
    outer_width_gt: Union[Unset, list[int]] = UNSET,
    outer_width_gte: Union[Unset, list[int]] = UNSET,
    outer_width_lt: Union[Unset, list[int]] = UNSET,
    outer_width_lte: Union[Unset, list[int]] = UNSET,
    outer_width_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
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
    starting_unit: Union[Unset, list[int]] = UNSET,
    starting_unit_empty: Union[Unset, bool] = UNSET,
    starting_unit_gt: Union[Unset, list[int]] = UNSET,
    starting_unit_gte: Union[Unset, list[int]] = UNSET,
    starting_unit_lt: Union[Unset, list[int]] = UNSET,
    starting_unit_lte: Union[Unset, list[int]] = UNSET,
    starting_unit_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
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
    weight_unit: Union[Unset, DcimRackTypesListWeightUnit] = UNSET,
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
) -> Response[PaginatedRackTypeList]:
    """Get a list of rack type objects.

    Args:
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
        form_factor (Union[Unset, list[str]]):
        form_factor_empty (Union[Unset, bool]):
        form_factor_ic (Union[Unset, list[str]]):
        form_factor_ie (Union[Unset, list[str]]):
        form_factor_iew (Union[Unset, list[str]]):
        form_factor_isw (Union[Unset, list[str]]):
        form_factor_n (Union[Unset, list[str]]):
        form_factor_nic (Union[Unset, list[str]]):
        form_factor_nie (Union[Unset, list[str]]):
        form_factor_niew (Union[Unset, list[str]]):
        form_factor_nisw (Union[Unset, list[str]]):
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
        mounting_depth (Union[Unset, list[int]]):
        mounting_depth_empty (Union[Unset, bool]):
        mounting_depth_gt (Union[Unset, list[int]]):
        mounting_depth_gte (Union[Unset, list[int]]):
        mounting_depth_lt (Union[Unset, list[int]]):
        mounting_depth_lte (Union[Unset, list[int]]):
        mounting_depth_n (Union[Unset, list[int]]):
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
        outer_unit (Union[Unset, DcimRackTypesListOuterUnit]):
        outer_width (Union[Unset, list[int]]):
        outer_width_empty (Union[Unset, bool]):
        outer_width_gt (Union[Unset, list[int]]):
        outer_width_gte (Union[Unset, list[int]]):
        outer_width_lt (Union[Unset, list[int]]):
        outer_width_lte (Union[Unset, list[int]]):
        outer_width_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
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
        starting_unit (Union[Unset, list[int]]):
        starting_unit_empty (Union[Unset, bool]):
        starting_unit_gt (Union[Unset, list[int]]):
        starting_unit_gte (Union[Unset, list[int]]):
        starting_unit_lt (Union[Unset, list[int]]):
        starting_unit_lte (Union[Unset, list[int]]):
        starting_unit_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
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
        weight_unit (Union[Unset, DcimRackTypesListWeightUnit]):
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
        Response[PaginatedRackTypeList]
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
        mounting_depth=mounting_depth,
        mounting_depth_empty=mounting_depth_empty,
        mounting_depth_gt=mounting_depth_gt,
        mounting_depth_gte=mounting_depth_gte,
        mounting_depth_lt=mounting_depth_lt,
        mounting_depth_lte=mounting_depth_lte,
        mounting_depth_n=mounting_depth_n,
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
        starting_unit=starting_unit,
        starting_unit_empty=starting_unit_empty,
        starting_unit_gt=starting_unit_gt,
        starting_unit_gte=starting_unit_gte,
        starting_unit_lt=starting_unit_lt,
        starting_unit_lte=starting_unit_lte,
        starting_unit_n=starting_unit_n,
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
    form_factor: Union[Unset, list[str]] = UNSET,
    form_factor_empty: Union[Unset, bool] = UNSET,
    form_factor_ic: Union[Unset, list[str]] = UNSET,
    form_factor_ie: Union[Unset, list[str]] = UNSET,
    form_factor_iew: Union[Unset, list[str]] = UNSET,
    form_factor_isw: Union[Unset, list[str]] = UNSET,
    form_factor_n: Union[Unset, list[str]] = UNSET,
    form_factor_nic: Union[Unset, list[str]] = UNSET,
    form_factor_nie: Union[Unset, list[str]] = UNSET,
    form_factor_niew: Union[Unset, list[str]] = UNSET,
    form_factor_nisw: Union[Unset, list[str]] = UNSET,
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
    mounting_depth: Union[Unset, list[int]] = UNSET,
    mounting_depth_empty: Union[Unset, bool] = UNSET,
    mounting_depth_gt: Union[Unset, list[int]] = UNSET,
    mounting_depth_gte: Union[Unset, list[int]] = UNSET,
    mounting_depth_lt: Union[Unset, list[int]] = UNSET,
    mounting_depth_lte: Union[Unset, list[int]] = UNSET,
    mounting_depth_n: Union[Unset, list[int]] = UNSET,
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
    outer_unit: Union[Unset, DcimRackTypesListOuterUnit] = UNSET,
    outer_width: Union[Unset, list[int]] = UNSET,
    outer_width_empty: Union[Unset, bool] = UNSET,
    outer_width_gt: Union[Unset, list[int]] = UNSET,
    outer_width_gte: Union[Unset, list[int]] = UNSET,
    outer_width_lt: Union[Unset, list[int]] = UNSET,
    outer_width_lte: Union[Unset, list[int]] = UNSET,
    outer_width_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
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
    starting_unit: Union[Unset, list[int]] = UNSET,
    starting_unit_empty: Union[Unset, bool] = UNSET,
    starting_unit_gt: Union[Unset, list[int]] = UNSET,
    starting_unit_gte: Union[Unset, list[int]] = UNSET,
    starting_unit_lt: Union[Unset, list[int]] = UNSET,
    starting_unit_lte: Union[Unset, list[int]] = UNSET,
    starting_unit_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
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
    weight_unit: Union[Unset, DcimRackTypesListWeightUnit] = UNSET,
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
) -> Optional[PaginatedRackTypeList]:
    """Get a list of rack type objects.

    Args:
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
        form_factor (Union[Unset, list[str]]):
        form_factor_empty (Union[Unset, bool]):
        form_factor_ic (Union[Unset, list[str]]):
        form_factor_ie (Union[Unset, list[str]]):
        form_factor_iew (Union[Unset, list[str]]):
        form_factor_isw (Union[Unset, list[str]]):
        form_factor_n (Union[Unset, list[str]]):
        form_factor_nic (Union[Unset, list[str]]):
        form_factor_nie (Union[Unset, list[str]]):
        form_factor_niew (Union[Unset, list[str]]):
        form_factor_nisw (Union[Unset, list[str]]):
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
        mounting_depth (Union[Unset, list[int]]):
        mounting_depth_empty (Union[Unset, bool]):
        mounting_depth_gt (Union[Unset, list[int]]):
        mounting_depth_gte (Union[Unset, list[int]]):
        mounting_depth_lt (Union[Unset, list[int]]):
        mounting_depth_lte (Union[Unset, list[int]]):
        mounting_depth_n (Union[Unset, list[int]]):
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
        outer_unit (Union[Unset, DcimRackTypesListOuterUnit]):
        outer_width (Union[Unset, list[int]]):
        outer_width_empty (Union[Unset, bool]):
        outer_width_gt (Union[Unset, list[int]]):
        outer_width_gte (Union[Unset, list[int]]):
        outer_width_lt (Union[Unset, list[int]]):
        outer_width_lte (Union[Unset, list[int]]):
        outer_width_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
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
        starting_unit (Union[Unset, list[int]]):
        starting_unit_empty (Union[Unset, bool]):
        starting_unit_gt (Union[Unset, list[int]]):
        starting_unit_gte (Union[Unset, list[int]]):
        starting_unit_lt (Union[Unset, list[int]]):
        starting_unit_lte (Union[Unset, list[int]]):
        starting_unit_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
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
        weight_unit (Union[Unset, DcimRackTypesListWeightUnit]):
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
        PaginatedRackTypeList
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
            mounting_depth=mounting_depth,
            mounting_depth_empty=mounting_depth_empty,
            mounting_depth_gt=mounting_depth_gt,
            mounting_depth_gte=mounting_depth_gte,
            mounting_depth_lt=mounting_depth_lt,
            mounting_depth_lte=mounting_depth_lte,
            mounting_depth_n=mounting_depth_n,
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
            starting_unit=starting_unit,
            starting_unit_empty=starting_unit_empty,
            starting_unit_gt=starting_unit_gt,
            starting_unit_gte=starting_unit_gte,
            starting_unit_lt=starting_unit_lt,
            starting_unit_lte=starting_unit_lte,
            starting_unit_n=starting_unit_n,
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
