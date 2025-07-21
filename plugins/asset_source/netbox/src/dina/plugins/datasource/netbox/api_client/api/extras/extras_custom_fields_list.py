import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.extras_custom_fields_list_filter_logic import (
    ExtrasCustomFieldsListFilterLogic,
)
from ...models.extras_custom_fields_list_ui_editable import (
    ExtrasCustomFieldsListUiEditable,
)
from ...models.extras_custom_fields_list_ui_visible import (
    ExtrasCustomFieldsListUiVisible,
)
from ...models.paginated_custom_field_list import PaginatedCustomFieldList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    choice_set: Union[Unset, list[str]] = UNSET,
    choice_set_n: Union[Unset, list[str]] = UNSET,
    choice_set_id: Union[Unset, list[Union[None, int]]] = UNSET,
    choice_set_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    filter_logic: Union[Unset, ExtrasCustomFieldsListFilterLogic] = UNSET,
    group_name: Union[Unset, list[str]] = UNSET,
    group_name_empty: Union[Unset, bool] = UNSET,
    group_name_ic: Union[Unset, list[str]] = UNSET,
    group_name_ie: Union[Unset, list[str]] = UNSET,
    group_name_iew: Union[Unset, list[str]] = UNSET,
    group_name_isw: Union[Unset, list[str]] = UNSET,
    group_name_n: Union[Unset, list[str]] = UNSET,
    group_name_nic: Union[Unset, list[str]] = UNSET,
    group_name_nie: Union[Unset, list[str]] = UNSET,
    group_name_niew: Union[Unset, list[str]] = UNSET,
    group_name_nisw: Union[Unset, list[str]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_cloneable: Union[Unset, bool] = UNSET,
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
    object_type: Union[Unset, str] = UNSET,
    object_type_ic: Union[Unset, str] = UNSET,
    object_type_ie: Union[Unset, str] = UNSET,
    object_type_iew: Union[Unset, str] = UNSET,
    object_type_isw: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_nic: Union[Unset, str] = UNSET,
    object_type_nie: Union[Unset, str] = UNSET,
    object_type_niew: Union[Unset, str] = UNSET,
    object_type_nisw: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    related_object_type: Union[Unset, str] = UNSET,
    related_object_type_n: Union[Unset, str] = UNSET,
    related_object_type_id: Union[Unset, list[int]] = UNSET,
    related_object_type_id_n: Union[Unset, list[int]] = UNSET,
    required: Union[Unset, bool] = UNSET,
    search_weight: Union[Unset, list[int]] = UNSET,
    search_weight_empty: Union[Unset, bool] = UNSET,
    search_weight_gt: Union[Unset, list[int]] = UNSET,
    search_weight_gte: Union[Unset, list[int]] = UNSET,
    search_weight_lt: Union[Unset, list[int]] = UNSET,
    search_weight_lte: Union[Unset, list[int]] = UNSET,
    search_weight_n: Union[Unset, list[int]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    type_empty: Union[Unset, bool] = UNSET,
    type_ic: Union[Unset, list[str]] = UNSET,
    type_ie: Union[Unset, list[str]] = UNSET,
    type_iew: Union[Unset, list[str]] = UNSET,
    type_isw: Union[Unset, list[str]] = UNSET,
    type_n: Union[Unset, list[str]] = UNSET,
    type_nic: Union[Unset, list[str]] = UNSET,
    type_nie: Union[Unset, list[str]] = UNSET,
    type_niew: Union[Unset, list[str]] = UNSET,
    type_nisw: Union[Unset, list[str]] = UNSET,
    ui_editable: Union[Unset, ExtrasCustomFieldsListUiEditable] = UNSET,
    ui_visible: Union[Unset, ExtrasCustomFieldsListUiVisible] = UNSET,
    unique: Union[Unset, bool] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    validation_maximum: Union[Unset, list[int]] = UNSET,
    validation_maximum_empty: Union[Unset, bool] = UNSET,
    validation_maximum_gt: Union[Unset, list[int]] = UNSET,
    validation_maximum_gte: Union[Unset, list[int]] = UNSET,
    validation_maximum_lt: Union[Unset, list[int]] = UNSET,
    validation_maximum_lte: Union[Unset, list[int]] = UNSET,
    validation_maximum_n: Union[Unset, list[int]] = UNSET,
    validation_minimum: Union[Unset, list[int]] = UNSET,
    validation_minimum_empty: Union[Unset, bool] = UNSET,
    validation_minimum_gt: Union[Unset, list[int]] = UNSET,
    validation_minimum_gte: Union[Unset, list[int]] = UNSET,
    validation_minimum_lt: Union[Unset, list[int]] = UNSET,
    validation_minimum_lte: Union[Unset, list[int]] = UNSET,
    validation_minimum_n: Union[Unset, list[int]] = UNSET,
    validation_regex: Union[Unset, list[str]] = UNSET,
    validation_regex_empty: Union[Unset, bool] = UNSET,
    validation_regex_ic: Union[Unset, list[str]] = UNSET,
    validation_regex_ie: Union[Unset, list[str]] = UNSET,
    validation_regex_iew: Union[Unset, list[str]] = UNSET,
    validation_regex_isw: Union[Unset, list[str]] = UNSET,
    validation_regex_n: Union[Unset, list[str]] = UNSET,
    validation_regex_nic: Union[Unset, list[str]] = UNSET,
    validation_regex_nie: Union[Unset, list[str]] = UNSET,
    validation_regex_niew: Union[Unset, list[str]] = UNSET,
    validation_regex_nisw: Union[Unset, list[str]] = UNSET,
    weight: Union[Unset, list[int]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[int]] = UNSET,
    weight_gte: Union[Unset, list[int]] = UNSET,
    weight_lt: Union[Unset, list[int]] = UNSET,
    weight_lte: Union[Unset, list[int]] = UNSET,
    weight_n: Union[Unset, list[int]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_choice_set: Union[Unset, list[str]] = UNSET
    if not isinstance(choice_set, Unset):
        json_choice_set = choice_set

    params["choice_set"] = json_choice_set

    json_choice_set_n: Union[Unset, list[str]] = UNSET
    if not isinstance(choice_set_n, Unset):
        json_choice_set_n = choice_set_n

    params["choice_set__n"] = json_choice_set_n

    json_choice_set_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(choice_set_id, Unset):
        json_choice_set_id = []
        for choice_set_id_item_data in choice_set_id:
            choice_set_id_item: Union[None, int]
            choice_set_id_item = choice_set_id_item_data
            json_choice_set_id.append(choice_set_id_item)

    params["choice_set_id"] = json_choice_set_id

    json_choice_set_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(choice_set_id_n, Unset):
        json_choice_set_id_n = []
        for choice_set_id_n_item_data in choice_set_id_n:
            choice_set_id_n_item: Union[None, int]
            choice_set_id_n_item = choice_set_id_n_item_data
            json_choice_set_id_n.append(choice_set_id_n_item)

    params["choice_set_id__n"] = json_choice_set_id_n

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

    json_filter_logic: Union[Unset, str] = UNSET
    if not isinstance(filter_logic, Unset):
        json_filter_logic = filter_logic.value

    params["filter_logic"] = json_filter_logic

    json_group_name: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name, Unset):
        json_group_name = group_name

    params["group_name"] = json_group_name

    params["group_name__empty"] = group_name_empty

    json_group_name_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name_ic, Unset):
        json_group_name_ic = group_name_ic

    params["group_name__ic"] = json_group_name_ic

    json_group_name_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name_ie, Unset):
        json_group_name_ie = group_name_ie

    params["group_name__ie"] = json_group_name_ie

    json_group_name_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name_iew, Unset):
        json_group_name_iew = group_name_iew

    params["group_name__iew"] = json_group_name_iew

    json_group_name_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name_isw, Unset):
        json_group_name_isw = group_name_isw

    params["group_name__isw"] = json_group_name_isw

    json_group_name_n: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name_n, Unset):
        json_group_name_n = group_name_n

    params["group_name__n"] = json_group_name_n

    json_group_name_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name_nic, Unset):
        json_group_name_nic = group_name_nic

    params["group_name__nic"] = json_group_name_nic

    json_group_name_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name_nie, Unset):
        json_group_name_nie = group_name_nie

    params["group_name__nie"] = json_group_name_nie

    json_group_name_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name_niew, Unset):
        json_group_name_niew = group_name_niew

    params["group_name__niew"] = json_group_name_niew

    json_group_name_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(group_name_nisw, Unset):
        json_group_name_nisw = group_name_nisw

    params["group_name__nisw"] = json_group_name_nisw

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

    params["is_cloneable"] = is_cloneable

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

    params["object_type"] = object_type

    params["object_type__ic"] = object_type_ic

    params["object_type__ie"] = object_type_ie

    params["object_type__iew"] = object_type_iew

    params["object_type__isw"] = object_type_isw

    params["object_type__n"] = object_type_n

    params["object_type__nic"] = object_type_nic

    params["object_type__nie"] = object_type_nie

    params["object_type__niew"] = object_type_niew

    params["object_type__nisw"] = object_type_nisw

    json_object_type_id: Union[Unset, list[int]] = UNSET
    if not isinstance(object_type_id, Unset):
        json_object_type_id = object_type_id

    params["object_type_id"] = json_object_type_id

    json_object_type_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(object_type_id_n, Unset):
        json_object_type_id_n = object_type_id_n

    params["object_type_id__n"] = json_object_type_id_n

    params["offset"] = offset

    params["ordering"] = ordering

    params["q"] = q

    params["related_object_type"] = related_object_type

    params["related_object_type__n"] = related_object_type_n

    json_related_object_type_id: Union[Unset, list[int]] = UNSET
    if not isinstance(related_object_type_id, Unset):
        json_related_object_type_id = related_object_type_id

    params["related_object_type_id"] = json_related_object_type_id

    json_related_object_type_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(related_object_type_id_n, Unset):
        json_related_object_type_id_n = related_object_type_id_n

    params["related_object_type_id__n"] = json_related_object_type_id_n

    params["required"] = required

    json_search_weight: Union[Unset, list[int]] = UNSET
    if not isinstance(search_weight, Unset):
        json_search_weight = search_weight

    params["search_weight"] = json_search_weight

    params["search_weight__empty"] = search_weight_empty

    json_search_weight_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(search_weight_gt, Unset):
        json_search_weight_gt = search_weight_gt

    params["search_weight__gt"] = json_search_weight_gt

    json_search_weight_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(search_weight_gte, Unset):
        json_search_weight_gte = search_weight_gte

    params["search_weight__gte"] = json_search_weight_gte

    json_search_weight_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(search_weight_lt, Unset):
        json_search_weight_lt = search_weight_lt

    params["search_weight__lt"] = json_search_weight_lt

    json_search_weight_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(search_weight_lte, Unset):
        json_search_weight_lte = search_weight_lte

    params["search_weight__lte"] = json_search_weight_lte

    json_search_weight_n: Union[Unset, list[int]] = UNSET
    if not isinstance(search_weight_n, Unset):
        json_search_weight_n = search_weight_n

    params["search_weight__n"] = json_search_weight_n

    json_type_: Union[Unset, list[str]] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    params["type__empty"] = type_empty

    json_type_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(type_ic, Unset):
        json_type_ic = type_ic

    params["type__ic"] = json_type_ic

    json_type_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(type_ie, Unset):
        json_type_ie = type_ie

    params["type__ie"] = json_type_ie

    json_type_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(type_iew, Unset):
        json_type_iew = type_iew

    params["type__iew"] = json_type_iew

    json_type_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(type_isw, Unset):
        json_type_isw = type_isw

    params["type__isw"] = json_type_isw

    json_type_n: Union[Unset, list[str]] = UNSET
    if not isinstance(type_n, Unset):
        json_type_n = type_n

    params["type__n"] = json_type_n

    json_type_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(type_nic, Unset):
        json_type_nic = type_nic

    params["type__nic"] = json_type_nic

    json_type_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(type_nie, Unset):
        json_type_nie = type_nie

    params["type__nie"] = json_type_nie

    json_type_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(type_niew, Unset):
        json_type_niew = type_niew

    params["type__niew"] = json_type_niew

    json_type_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(type_nisw, Unset):
        json_type_nisw = type_nisw

    params["type__nisw"] = json_type_nisw

    json_ui_editable: Union[Unset, str] = UNSET
    if not isinstance(ui_editable, Unset):
        json_ui_editable = ui_editable.value

    params["ui_editable"] = json_ui_editable

    json_ui_visible: Union[Unset, str] = UNSET
    if not isinstance(ui_visible, Unset):
        json_ui_visible = ui_visible.value

    params["ui_visible"] = json_ui_visible

    params["unique"] = unique

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    json_validation_maximum: Union[Unset, list[int]] = UNSET
    if not isinstance(validation_maximum, Unset):
        json_validation_maximum = validation_maximum

    params["validation_maximum"] = json_validation_maximum

    params["validation_maximum__empty"] = validation_maximum_empty

    json_validation_maximum_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(validation_maximum_gt, Unset):
        json_validation_maximum_gt = validation_maximum_gt

    params["validation_maximum__gt"] = json_validation_maximum_gt

    json_validation_maximum_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(validation_maximum_gte, Unset):
        json_validation_maximum_gte = validation_maximum_gte

    params["validation_maximum__gte"] = json_validation_maximum_gte

    json_validation_maximum_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(validation_maximum_lt, Unset):
        json_validation_maximum_lt = validation_maximum_lt

    params["validation_maximum__lt"] = json_validation_maximum_lt

    json_validation_maximum_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(validation_maximum_lte, Unset):
        json_validation_maximum_lte = validation_maximum_lte

    params["validation_maximum__lte"] = json_validation_maximum_lte

    json_validation_maximum_n: Union[Unset, list[int]] = UNSET
    if not isinstance(validation_maximum_n, Unset):
        json_validation_maximum_n = validation_maximum_n

    params["validation_maximum__n"] = json_validation_maximum_n

    json_validation_minimum: Union[Unset, list[int]] = UNSET
    if not isinstance(validation_minimum, Unset):
        json_validation_minimum = validation_minimum

    params["validation_minimum"] = json_validation_minimum

    params["validation_minimum__empty"] = validation_minimum_empty

    json_validation_minimum_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(validation_minimum_gt, Unset):
        json_validation_minimum_gt = validation_minimum_gt

    params["validation_minimum__gt"] = json_validation_minimum_gt

    json_validation_minimum_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(validation_minimum_gte, Unset):
        json_validation_minimum_gte = validation_minimum_gte

    params["validation_minimum__gte"] = json_validation_minimum_gte

    json_validation_minimum_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(validation_minimum_lt, Unset):
        json_validation_minimum_lt = validation_minimum_lt

    params["validation_minimum__lt"] = json_validation_minimum_lt

    json_validation_minimum_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(validation_minimum_lte, Unset):
        json_validation_minimum_lte = validation_minimum_lte

    params["validation_minimum__lte"] = json_validation_minimum_lte

    json_validation_minimum_n: Union[Unset, list[int]] = UNSET
    if not isinstance(validation_minimum_n, Unset):
        json_validation_minimum_n = validation_minimum_n

    params["validation_minimum__n"] = json_validation_minimum_n

    json_validation_regex: Union[Unset, list[str]] = UNSET
    if not isinstance(validation_regex, Unset):
        json_validation_regex = validation_regex

    params["validation_regex"] = json_validation_regex

    params["validation_regex__empty"] = validation_regex_empty

    json_validation_regex_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(validation_regex_ic, Unset):
        json_validation_regex_ic = validation_regex_ic

    params["validation_regex__ic"] = json_validation_regex_ic

    json_validation_regex_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(validation_regex_ie, Unset):
        json_validation_regex_ie = validation_regex_ie

    params["validation_regex__ie"] = json_validation_regex_ie

    json_validation_regex_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(validation_regex_iew, Unset):
        json_validation_regex_iew = validation_regex_iew

    params["validation_regex__iew"] = json_validation_regex_iew

    json_validation_regex_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(validation_regex_isw, Unset):
        json_validation_regex_isw = validation_regex_isw

    params["validation_regex__isw"] = json_validation_regex_isw

    json_validation_regex_n: Union[Unset, list[str]] = UNSET
    if not isinstance(validation_regex_n, Unset):
        json_validation_regex_n = validation_regex_n

    params["validation_regex__n"] = json_validation_regex_n

    json_validation_regex_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(validation_regex_nic, Unset):
        json_validation_regex_nic = validation_regex_nic

    params["validation_regex__nic"] = json_validation_regex_nic

    json_validation_regex_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(validation_regex_nie, Unset):
        json_validation_regex_nie = validation_regex_nie

    params["validation_regex__nie"] = json_validation_regex_nie

    json_validation_regex_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(validation_regex_niew, Unset):
        json_validation_regex_niew = validation_regex_niew

    params["validation_regex__niew"] = json_validation_regex_niew

    json_validation_regex_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(validation_regex_nisw, Unset):
        json_validation_regex_nisw = validation_regex_nisw

    params["validation_regex__nisw"] = json_validation_regex_nisw

    json_weight: Union[Unset, list[int]] = UNSET
    if not isinstance(weight, Unset):
        json_weight = weight

    params["weight"] = json_weight

    params["weight__empty"] = weight_empty

    json_weight_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(weight_gt, Unset):
        json_weight_gt = weight_gt

    params["weight__gt"] = json_weight_gt

    json_weight_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(weight_gte, Unset):
        json_weight_gte = weight_gte

    params["weight__gte"] = json_weight_gte

    json_weight_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(weight_lt, Unset):
        json_weight_lt = weight_lt

    params["weight__lt"] = json_weight_lt

    json_weight_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(weight_lte, Unset):
        json_weight_lte = weight_lte

    params["weight__lte"] = json_weight_lte

    json_weight_n: Union[Unset, list[int]] = UNSET
    if not isinstance(weight_n, Unset):
        json_weight_n = weight_n

    params["weight__n"] = json_weight_n

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/extras/custom-fields/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedCustomFieldList]:
    if response.status_code == 200:
        response_200 = PaginatedCustomFieldList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedCustomFieldList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    choice_set: Union[Unset, list[str]] = UNSET,
    choice_set_n: Union[Unset, list[str]] = UNSET,
    choice_set_id: Union[Unset, list[Union[None, int]]] = UNSET,
    choice_set_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    filter_logic: Union[Unset, ExtrasCustomFieldsListFilterLogic] = UNSET,
    group_name: Union[Unset, list[str]] = UNSET,
    group_name_empty: Union[Unset, bool] = UNSET,
    group_name_ic: Union[Unset, list[str]] = UNSET,
    group_name_ie: Union[Unset, list[str]] = UNSET,
    group_name_iew: Union[Unset, list[str]] = UNSET,
    group_name_isw: Union[Unset, list[str]] = UNSET,
    group_name_n: Union[Unset, list[str]] = UNSET,
    group_name_nic: Union[Unset, list[str]] = UNSET,
    group_name_nie: Union[Unset, list[str]] = UNSET,
    group_name_niew: Union[Unset, list[str]] = UNSET,
    group_name_nisw: Union[Unset, list[str]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_cloneable: Union[Unset, bool] = UNSET,
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
    object_type: Union[Unset, str] = UNSET,
    object_type_ic: Union[Unset, str] = UNSET,
    object_type_ie: Union[Unset, str] = UNSET,
    object_type_iew: Union[Unset, str] = UNSET,
    object_type_isw: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_nic: Union[Unset, str] = UNSET,
    object_type_nie: Union[Unset, str] = UNSET,
    object_type_niew: Union[Unset, str] = UNSET,
    object_type_nisw: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    related_object_type: Union[Unset, str] = UNSET,
    related_object_type_n: Union[Unset, str] = UNSET,
    related_object_type_id: Union[Unset, list[int]] = UNSET,
    related_object_type_id_n: Union[Unset, list[int]] = UNSET,
    required: Union[Unset, bool] = UNSET,
    search_weight: Union[Unset, list[int]] = UNSET,
    search_weight_empty: Union[Unset, bool] = UNSET,
    search_weight_gt: Union[Unset, list[int]] = UNSET,
    search_weight_gte: Union[Unset, list[int]] = UNSET,
    search_weight_lt: Union[Unset, list[int]] = UNSET,
    search_weight_lte: Union[Unset, list[int]] = UNSET,
    search_weight_n: Union[Unset, list[int]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    type_empty: Union[Unset, bool] = UNSET,
    type_ic: Union[Unset, list[str]] = UNSET,
    type_ie: Union[Unset, list[str]] = UNSET,
    type_iew: Union[Unset, list[str]] = UNSET,
    type_isw: Union[Unset, list[str]] = UNSET,
    type_n: Union[Unset, list[str]] = UNSET,
    type_nic: Union[Unset, list[str]] = UNSET,
    type_nie: Union[Unset, list[str]] = UNSET,
    type_niew: Union[Unset, list[str]] = UNSET,
    type_nisw: Union[Unset, list[str]] = UNSET,
    ui_editable: Union[Unset, ExtrasCustomFieldsListUiEditable] = UNSET,
    ui_visible: Union[Unset, ExtrasCustomFieldsListUiVisible] = UNSET,
    unique: Union[Unset, bool] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    validation_maximum: Union[Unset, list[int]] = UNSET,
    validation_maximum_empty: Union[Unset, bool] = UNSET,
    validation_maximum_gt: Union[Unset, list[int]] = UNSET,
    validation_maximum_gte: Union[Unset, list[int]] = UNSET,
    validation_maximum_lt: Union[Unset, list[int]] = UNSET,
    validation_maximum_lte: Union[Unset, list[int]] = UNSET,
    validation_maximum_n: Union[Unset, list[int]] = UNSET,
    validation_minimum: Union[Unset, list[int]] = UNSET,
    validation_minimum_empty: Union[Unset, bool] = UNSET,
    validation_minimum_gt: Union[Unset, list[int]] = UNSET,
    validation_minimum_gte: Union[Unset, list[int]] = UNSET,
    validation_minimum_lt: Union[Unset, list[int]] = UNSET,
    validation_minimum_lte: Union[Unset, list[int]] = UNSET,
    validation_minimum_n: Union[Unset, list[int]] = UNSET,
    validation_regex: Union[Unset, list[str]] = UNSET,
    validation_regex_empty: Union[Unset, bool] = UNSET,
    validation_regex_ic: Union[Unset, list[str]] = UNSET,
    validation_regex_ie: Union[Unset, list[str]] = UNSET,
    validation_regex_iew: Union[Unset, list[str]] = UNSET,
    validation_regex_isw: Union[Unset, list[str]] = UNSET,
    validation_regex_n: Union[Unset, list[str]] = UNSET,
    validation_regex_nic: Union[Unset, list[str]] = UNSET,
    validation_regex_nie: Union[Unset, list[str]] = UNSET,
    validation_regex_niew: Union[Unset, list[str]] = UNSET,
    validation_regex_nisw: Union[Unset, list[str]] = UNSET,
    weight: Union[Unset, list[int]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[int]] = UNSET,
    weight_gte: Union[Unset, list[int]] = UNSET,
    weight_lt: Union[Unset, list[int]] = UNSET,
    weight_lte: Union[Unset, list[int]] = UNSET,
    weight_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedCustomFieldList]:
    """Get a list of custom field objects.

    Args:
        choice_set (Union[Unset, list[str]]):
        choice_set_n (Union[Unset, list[str]]):
        choice_set_id (Union[Unset, list[Union[None, int]]]):
        choice_set_id_n (Union[Unset, list[Union[None, int]]]):
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
        filter_logic (Union[Unset, ExtrasCustomFieldsListFilterLogic]):
        group_name (Union[Unset, list[str]]):
        group_name_empty (Union[Unset, bool]):
        group_name_ic (Union[Unset, list[str]]):
        group_name_ie (Union[Unset, list[str]]):
        group_name_iew (Union[Unset, list[str]]):
        group_name_isw (Union[Unset, list[str]]):
        group_name_n (Union[Unset, list[str]]):
        group_name_nic (Union[Unset, list[str]]):
        group_name_nie (Union[Unset, list[str]]):
        group_name_niew (Union[Unset, list[str]]):
        group_name_nisw (Union[Unset, list[str]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_cloneable (Union[Unset, bool]):
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
        object_type (Union[Unset, str]):
        object_type_ic (Union[Unset, str]):
        object_type_ie (Union[Unset, str]):
        object_type_iew (Union[Unset, str]):
        object_type_isw (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_nic (Union[Unset, str]):
        object_type_nie (Union[Unset, str]):
        object_type_niew (Union[Unset, str]):
        object_type_nisw (Union[Unset, str]):
        object_type_id (Union[Unset, list[int]]):
        object_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        related_object_type (Union[Unset, str]):
        related_object_type_n (Union[Unset, str]):
        related_object_type_id (Union[Unset, list[int]]):
        related_object_type_id_n (Union[Unset, list[int]]):
        required (Union[Unset, bool]):
        search_weight (Union[Unset, list[int]]):
        search_weight_empty (Union[Unset, bool]):
        search_weight_gt (Union[Unset, list[int]]):
        search_weight_gte (Union[Unset, list[int]]):
        search_weight_lt (Union[Unset, list[int]]):
        search_weight_lte (Union[Unset, list[int]]):
        search_weight_n (Union[Unset, list[int]]):
        type_ (Union[Unset, list[str]]):
        type_empty (Union[Unset, bool]):
        type_ic (Union[Unset, list[str]]):
        type_ie (Union[Unset, list[str]]):
        type_iew (Union[Unset, list[str]]):
        type_isw (Union[Unset, list[str]]):
        type_n (Union[Unset, list[str]]):
        type_nic (Union[Unset, list[str]]):
        type_nie (Union[Unset, list[str]]):
        type_niew (Union[Unset, list[str]]):
        type_nisw (Union[Unset, list[str]]):
        ui_editable (Union[Unset, ExtrasCustomFieldsListUiEditable]):
        ui_visible (Union[Unset, ExtrasCustomFieldsListUiVisible]):
        unique (Union[Unset, bool]):
        updated_by_request (Union[Unset, UUID]):
        validation_maximum (Union[Unset, list[int]]):
        validation_maximum_empty (Union[Unset, bool]):
        validation_maximum_gt (Union[Unset, list[int]]):
        validation_maximum_gte (Union[Unset, list[int]]):
        validation_maximum_lt (Union[Unset, list[int]]):
        validation_maximum_lte (Union[Unset, list[int]]):
        validation_maximum_n (Union[Unset, list[int]]):
        validation_minimum (Union[Unset, list[int]]):
        validation_minimum_empty (Union[Unset, bool]):
        validation_minimum_gt (Union[Unset, list[int]]):
        validation_minimum_gte (Union[Unset, list[int]]):
        validation_minimum_lt (Union[Unset, list[int]]):
        validation_minimum_lte (Union[Unset, list[int]]):
        validation_minimum_n (Union[Unset, list[int]]):
        validation_regex (Union[Unset, list[str]]):
        validation_regex_empty (Union[Unset, bool]):
        validation_regex_ic (Union[Unset, list[str]]):
        validation_regex_ie (Union[Unset, list[str]]):
        validation_regex_iew (Union[Unset, list[str]]):
        validation_regex_isw (Union[Unset, list[str]]):
        validation_regex_n (Union[Unset, list[str]]):
        validation_regex_nic (Union[Unset, list[str]]):
        validation_regex_nie (Union[Unset, list[str]]):
        validation_regex_niew (Union[Unset, list[str]]):
        validation_regex_nisw (Union[Unset, list[str]]):
        weight (Union[Unset, list[int]]):
        weight_empty (Union[Unset, bool]):
        weight_gt (Union[Unset, list[int]]):
        weight_gte (Union[Unset, list[int]]):
        weight_lt (Union[Unset, list[int]]):
        weight_lte (Union[Unset, list[int]]):
        weight_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCustomFieldList]
    """

    kwargs = _get_kwargs(
        choice_set=choice_set,
        choice_set_n=choice_set_n,
        choice_set_id=choice_set_id,
        choice_set_id_n=choice_set_id_n,
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
        filter_logic=filter_logic,
        group_name=group_name,
        group_name_empty=group_name_empty,
        group_name_ic=group_name_ic,
        group_name_ie=group_name_ie,
        group_name_iew=group_name_iew,
        group_name_isw=group_name_isw,
        group_name_n=group_name_n,
        group_name_nic=group_name_nic,
        group_name_nie=group_name_nie,
        group_name_niew=group_name_niew,
        group_name_nisw=group_name_nisw,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        is_cloneable=is_cloneable,
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
        object_type=object_type,
        object_type_ic=object_type_ic,
        object_type_ie=object_type_ie,
        object_type_iew=object_type_iew,
        object_type_isw=object_type_isw,
        object_type_n=object_type_n,
        object_type_nic=object_type_nic,
        object_type_nie=object_type_nie,
        object_type_niew=object_type_niew,
        object_type_nisw=object_type_nisw,
        object_type_id=object_type_id,
        object_type_id_n=object_type_id_n,
        offset=offset,
        ordering=ordering,
        q=q,
        related_object_type=related_object_type,
        related_object_type_n=related_object_type_n,
        related_object_type_id=related_object_type_id,
        related_object_type_id_n=related_object_type_id_n,
        required=required,
        search_weight=search_weight,
        search_weight_empty=search_weight_empty,
        search_weight_gt=search_weight_gt,
        search_weight_gte=search_weight_gte,
        search_weight_lt=search_weight_lt,
        search_weight_lte=search_weight_lte,
        search_weight_n=search_weight_n,
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
        ui_editable=ui_editable,
        ui_visible=ui_visible,
        unique=unique,
        updated_by_request=updated_by_request,
        validation_maximum=validation_maximum,
        validation_maximum_empty=validation_maximum_empty,
        validation_maximum_gt=validation_maximum_gt,
        validation_maximum_gte=validation_maximum_gte,
        validation_maximum_lt=validation_maximum_lt,
        validation_maximum_lte=validation_maximum_lte,
        validation_maximum_n=validation_maximum_n,
        validation_minimum=validation_minimum,
        validation_minimum_empty=validation_minimum_empty,
        validation_minimum_gt=validation_minimum_gt,
        validation_minimum_gte=validation_minimum_gte,
        validation_minimum_lt=validation_minimum_lt,
        validation_minimum_lte=validation_minimum_lte,
        validation_minimum_n=validation_minimum_n,
        validation_regex=validation_regex,
        validation_regex_empty=validation_regex_empty,
        validation_regex_ic=validation_regex_ic,
        validation_regex_ie=validation_regex_ie,
        validation_regex_iew=validation_regex_iew,
        validation_regex_isw=validation_regex_isw,
        validation_regex_n=validation_regex_n,
        validation_regex_nic=validation_regex_nic,
        validation_regex_nie=validation_regex_nie,
        validation_regex_niew=validation_regex_niew,
        validation_regex_nisw=validation_regex_nisw,
        weight=weight,
        weight_empty=weight_empty,
        weight_gt=weight_gt,
        weight_gte=weight_gte,
        weight_lt=weight_lt,
        weight_lte=weight_lte,
        weight_n=weight_n,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    choice_set: Union[Unset, list[str]] = UNSET,
    choice_set_n: Union[Unset, list[str]] = UNSET,
    choice_set_id: Union[Unset, list[Union[None, int]]] = UNSET,
    choice_set_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    filter_logic: Union[Unset, ExtrasCustomFieldsListFilterLogic] = UNSET,
    group_name: Union[Unset, list[str]] = UNSET,
    group_name_empty: Union[Unset, bool] = UNSET,
    group_name_ic: Union[Unset, list[str]] = UNSET,
    group_name_ie: Union[Unset, list[str]] = UNSET,
    group_name_iew: Union[Unset, list[str]] = UNSET,
    group_name_isw: Union[Unset, list[str]] = UNSET,
    group_name_n: Union[Unset, list[str]] = UNSET,
    group_name_nic: Union[Unset, list[str]] = UNSET,
    group_name_nie: Union[Unset, list[str]] = UNSET,
    group_name_niew: Union[Unset, list[str]] = UNSET,
    group_name_nisw: Union[Unset, list[str]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_cloneable: Union[Unset, bool] = UNSET,
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
    object_type: Union[Unset, str] = UNSET,
    object_type_ic: Union[Unset, str] = UNSET,
    object_type_ie: Union[Unset, str] = UNSET,
    object_type_iew: Union[Unset, str] = UNSET,
    object_type_isw: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_nic: Union[Unset, str] = UNSET,
    object_type_nie: Union[Unset, str] = UNSET,
    object_type_niew: Union[Unset, str] = UNSET,
    object_type_nisw: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    related_object_type: Union[Unset, str] = UNSET,
    related_object_type_n: Union[Unset, str] = UNSET,
    related_object_type_id: Union[Unset, list[int]] = UNSET,
    related_object_type_id_n: Union[Unset, list[int]] = UNSET,
    required: Union[Unset, bool] = UNSET,
    search_weight: Union[Unset, list[int]] = UNSET,
    search_weight_empty: Union[Unset, bool] = UNSET,
    search_weight_gt: Union[Unset, list[int]] = UNSET,
    search_weight_gte: Union[Unset, list[int]] = UNSET,
    search_weight_lt: Union[Unset, list[int]] = UNSET,
    search_weight_lte: Union[Unset, list[int]] = UNSET,
    search_weight_n: Union[Unset, list[int]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    type_empty: Union[Unset, bool] = UNSET,
    type_ic: Union[Unset, list[str]] = UNSET,
    type_ie: Union[Unset, list[str]] = UNSET,
    type_iew: Union[Unset, list[str]] = UNSET,
    type_isw: Union[Unset, list[str]] = UNSET,
    type_n: Union[Unset, list[str]] = UNSET,
    type_nic: Union[Unset, list[str]] = UNSET,
    type_nie: Union[Unset, list[str]] = UNSET,
    type_niew: Union[Unset, list[str]] = UNSET,
    type_nisw: Union[Unset, list[str]] = UNSET,
    ui_editable: Union[Unset, ExtrasCustomFieldsListUiEditable] = UNSET,
    ui_visible: Union[Unset, ExtrasCustomFieldsListUiVisible] = UNSET,
    unique: Union[Unset, bool] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    validation_maximum: Union[Unset, list[int]] = UNSET,
    validation_maximum_empty: Union[Unset, bool] = UNSET,
    validation_maximum_gt: Union[Unset, list[int]] = UNSET,
    validation_maximum_gte: Union[Unset, list[int]] = UNSET,
    validation_maximum_lt: Union[Unset, list[int]] = UNSET,
    validation_maximum_lte: Union[Unset, list[int]] = UNSET,
    validation_maximum_n: Union[Unset, list[int]] = UNSET,
    validation_minimum: Union[Unset, list[int]] = UNSET,
    validation_minimum_empty: Union[Unset, bool] = UNSET,
    validation_minimum_gt: Union[Unset, list[int]] = UNSET,
    validation_minimum_gte: Union[Unset, list[int]] = UNSET,
    validation_minimum_lt: Union[Unset, list[int]] = UNSET,
    validation_minimum_lte: Union[Unset, list[int]] = UNSET,
    validation_minimum_n: Union[Unset, list[int]] = UNSET,
    validation_regex: Union[Unset, list[str]] = UNSET,
    validation_regex_empty: Union[Unset, bool] = UNSET,
    validation_regex_ic: Union[Unset, list[str]] = UNSET,
    validation_regex_ie: Union[Unset, list[str]] = UNSET,
    validation_regex_iew: Union[Unset, list[str]] = UNSET,
    validation_regex_isw: Union[Unset, list[str]] = UNSET,
    validation_regex_n: Union[Unset, list[str]] = UNSET,
    validation_regex_nic: Union[Unset, list[str]] = UNSET,
    validation_regex_nie: Union[Unset, list[str]] = UNSET,
    validation_regex_niew: Union[Unset, list[str]] = UNSET,
    validation_regex_nisw: Union[Unset, list[str]] = UNSET,
    weight: Union[Unset, list[int]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[int]] = UNSET,
    weight_gte: Union[Unset, list[int]] = UNSET,
    weight_lt: Union[Unset, list[int]] = UNSET,
    weight_lte: Union[Unset, list[int]] = UNSET,
    weight_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedCustomFieldList]:
    """Get a list of custom field objects.

    Args:
        choice_set (Union[Unset, list[str]]):
        choice_set_n (Union[Unset, list[str]]):
        choice_set_id (Union[Unset, list[Union[None, int]]]):
        choice_set_id_n (Union[Unset, list[Union[None, int]]]):
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
        filter_logic (Union[Unset, ExtrasCustomFieldsListFilterLogic]):
        group_name (Union[Unset, list[str]]):
        group_name_empty (Union[Unset, bool]):
        group_name_ic (Union[Unset, list[str]]):
        group_name_ie (Union[Unset, list[str]]):
        group_name_iew (Union[Unset, list[str]]):
        group_name_isw (Union[Unset, list[str]]):
        group_name_n (Union[Unset, list[str]]):
        group_name_nic (Union[Unset, list[str]]):
        group_name_nie (Union[Unset, list[str]]):
        group_name_niew (Union[Unset, list[str]]):
        group_name_nisw (Union[Unset, list[str]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_cloneable (Union[Unset, bool]):
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
        object_type (Union[Unset, str]):
        object_type_ic (Union[Unset, str]):
        object_type_ie (Union[Unset, str]):
        object_type_iew (Union[Unset, str]):
        object_type_isw (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_nic (Union[Unset, str]):
        object_type_nie (Union[Unset, str]):
        object_type_niew (Union[Unset, str]):
        object_type_nisw (Union[Unset, str]):
        object_type_id (Union[Unset, list[int]]):
        object_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        related_object_type (Union[Unset, str]):
        related_object_type_n (Union[Unset, str]):
        related_object_type_id (Union[Unset, list[int]]):
        related_object_type_id_n (Union[Unset, list[int]]):
        required (Union[Unset, bool]):
        search_weight (Union[Unset, list[int]]):
        search_weight_empty (Union[Unset, bool]):
        search_weight_gt (Union[Unset, list[int]]):
        search_weight_gte (Union[Unset, list[int]]):
        search_weight_lt (Union[Unset, list[int]]):
        search_weight_lte (Union[Unset, list[int]]):
        search_weight_n (Union[Unset, list[int]]):
        type_ (Union[Unset, list[str]]):
        type_empty (Union[Unset, bool]):
        type_ic (Union[Unset, list[str]]):
        type_ie (Union[Unset, list[str]]):
        type_iew (Union[Unset, list[str]]):
        type_isw (Union[Unset, list[str]]):
        type_n (Union[Unset, list[str]]):
        type_nic (Union[Unset, list[str]]):
        type_nie (Union[Unset, list[str]]):
        type_niew (Union[Unset, list[str]]):
        type_nisw (Union[Unset, list[str]]):
        ui_editable (Union[Unset, ExtrasCustomFieldsListUiEditable]):
        ui_visible (Union[Unset, ExtrasCustomFieldsListUiVisible]):
        unique (Union[Unset, bool]):
        updated_by_request (Union[Unset, UUID]):
        validation_maximum (Union[Unset, list[int]]):
        validation_maximum_empty (Union[Unset, bool]):
        validation_maximum_gt (Union[Unset, list[int]]):
        validation_maximum_gte (Union[Unset, list[int]]):
        validation_maximum_lt (Union[Unset, list[int]]):
        validation_maximum_lte (Union[Unset, list[int]]):
        validation_maximum_n (Union[Unset, list[int]]):
        validation_minimum (Union[Unset, list[int]]):
        validation_minimum_empty (Union[Unset, bool]):
        validation_minimum_gt (Union[Unset, list[int]]):
        validation_minimum_gte (Union[Unset, list[int]]):
        validation_minimum_lt (Union[Unset, list[int]]):
        validation_minimum_lte (Union[Unset, list[int]]):
        validation_minimum_n (Union[Unset, list[int]]):
        validation_regex (Union[Unset, list[str]]):
        validation_regex_empty (Union[Unset, bool]):
        validation_regex_ic (Union[Unset, list[str]]):
        validation_regex_ie (Union[Unset, list[str]]):
        validation_regex_iew (Union[Unset, list[str]]):
        validation_regex_isw (Union[Unset, list[str]]):
        validation_regex_n (Union[Unset, list[str]]):
        validation_regex_nic (Union[Unset, list[str]]):
        validation_regex_nie (Union[Unset, list[str]]):
        validation_regex_niew (Union[Unset, list[str]]):
        validation_regex_nisw (Union[Unset, list[str]]):
        weight (Union[Unset, list[int]]):
        weight_empty (Union[Unset, bool]):
        weight_gt (Union[Unset, list[int]]):
        weight_gte (Union[Unset, list[int]]):
        weight_lt (Union[Unset, list[int]]):
        weight_lte (Union[Unset, list[int]]):
        weight_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCustomFieldList
    """

    return sync_detailed(
        client=client,
        choice_set=choice_set,
        choice_set_n=choice_set_n,
        choice_set_id=choice_set_id,
        choice_set_id_n=choice_set_id_n,
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
        filter_logic=filter_logic,
        group_name=group_name,
        group_name_empty=group_name_empty,
        group_name_ic=group_name_ic,
        group_name_ie=group_name_ie,
        group_name_iew=group_name_iew,
        group_name_isw=group_name_isw,
        group_name_n=group_name_n,
        group_name_nic=group_name_nic,
        group_name_nie=group_name_nie,
        group_name_niew=group_name_niew,
        group_name_nisw=group_name_nisw,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        is_cloneable=is_cloneable,
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
        object_type=object_type,
        object_type_ic=object_type_ic,
        object_type_ie=object_type_ie,
        object_type_iew=object_type_iew,
        object_type_isw=object_type_isw,
        object_type_n=object_type_n,
        object_type_nic=object_type_nic,
        object_type_nie=object_type_nie,
        object_type_niew=object_type_niew,
        object_type_nisw=object_type_nisw,
        object_type_id=object_type_id,
        object_type_id_n=object_type_id_n,
        offset=offset,
        ordering=ordering,
        q=q,
        related_object_type=related_object_type,
        related_object_type_n=related_object_type_n,
        related_object_type_id=related_object_type_id,
        related_object_type_id_n=related_object_type_id_n,
        required=required,
        search_weight=search_weight,
        search_weight_empty=search_weight_empty,
        search_weight_gt=search_weight_gt,
        search_weight_gte=search_weight_gte,
        search_weight_lt=search_weight_lt,
        search_weight_lte=search_weight_lte,
        search_weight_n=search_weight_n,
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
        ui_editable=ui_editable,
        ui_visible=ui_visible,
        unique=unique,
        updated_by_request=updated_by_request,
        validation_maximum=validation_maximum,
        validation_maximum_empty=validation_maximum_empty,
        validation_maximum_gt=validation_maximum_gt,
        validation_maximum_gte=validation_maximum_gte,
        validation_maximum_lt=validation_maximum_lt,
        validation_maximum_lte=validation_maximum_lte,
        validation_maximum_n=validation_maximum_n,
        validation_minimum=validation_minimum,
        validation_minimum_empty=validation_minimum_empty,
        validation_minimum_gt=validation_minimum_gt,
        validation_minimum_gte=validation_minimum_gte,
        validation_minimum_lt=validation_minimum_lt,
        validation_minimum_lte=validation_minimum_lte,
        validation_minimum_n=validation_minimum_n,
        validation_regex=validation_regex,
        validation_regex_empty=validation_regex_empty,
        validation_regex_ic=validation_regex_ic,
        validation_regex_ie=validation_regex_ie,
        validation_regex_iew=validation_regex_iew,
        validation_regex_isw=validation_regex_isw,
        validation_regex_n=validation_regex_n,
        validation_regex_nic=validation_regex_nic,
        validation_regex_nie=validation_regex_nie,
        validation_regex_niew=validation_regex_niew,
        validation_regex_nisw=validation_regex_nisw,
        weight=weight,
        weight_empty=weight_empty,
        weight_gt=weight_gt,
        weight_gte=weight_gte,
        weight_lt=weight_lt,
        weight_lte=weight_lte,
        weight_n=weight_n,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    choice_set: Union[Unset, list[str]] = UNSET,
    choice_set_n: Union[Unset, list[str]] = UNSET,
    choice_set_id: Union[Unset, list[Union[None, int]]] = UNSET,
    choice_set_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    filter_logic: Union[Unset, ExtrasCustomFieldsListFilterLogic] = UNSET,
    group_name: Union[Unset, list[str]] = UNSET,
    group_name_empty: Union[Unset, bool] = UNSET,
    group_name_ic: Union[Unset, list[str]] = UNSET,
    group_name_ie: Union[Unset, list[str]] = UNSET,
    group_name_iew: Union[Unset, list[str]] = UNSET,
    group_name_isw: Union[Unset, list[str]] = UNSET,
    group_name_n: Union[Unset, list[str]] = UNSET,
    group_name_nic: Union[Unset, list[str]] = UNSET,
    group_name_nie: Union[Unset, list[str]] = UNSET,
    group_name_niew: Union[Unset, list[str]] = UNSET,
    group_name_nisw: Union[Unset, list[str]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_cloneable: Union[Unset, bool] = UNSET,
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
    object_type: Union[Unset, str] = UNSET,
    object_type_ic: Union[Unset, str] = UNSET,
    object_type_ie: Union[Unset, str] = UNSET,
    object_type_iew: Union[Unset, str] = UNSET,
    object_type_isw: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_nic: Union[Unset, str] = UNSET,
    object_type_nie: Union[Unset, str] = UNSET,
    object_type_niew: Union[Unset, str] = UNSET,
    object_type_nisw: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    related_object_type: Union[Unset, str] = UNSET,
    related_object_type_n: Union[Unset, str] = UNSET,
    related_object_type_id: Union[Unset, list[int]] = UNSET,
    related_object_type_id_n: Union[Unset, list[int]] = UNSET,
    required: Union[Unset, bool] = UNSET,
    search_weight: Union[Unset, list[int]] = UNSET,
    search_weight_empty: Union[Unset, bool] = UNSET,
    search_weight_gt: Union[Unset, list[int]] = UNSET,
    search_weight_gte: Union[Unset, list[int]] = UNSET,
    search_weight_lt: Union[Unset, list[int]] = UNSET,
    search_weight_lte: Union[Unset, list[int]] = UNSET,
    search_weight_n: Union[Unset, list[int]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    type_empty: Union[Unset, bool] = UNSET,
    type_ic: Union[Unset, list[str]] = UNSET,
    type_ie: Union[Unset, list[str]] = UNSET,
    type_iew: Union[Unset, list[str]] = UNSET,
    type_isw: Union[Unset, list[str]] = UNSET,
    type_n: Union[Unset, list[str]] = UNSET,
    type_nic: Union[Unset, list[str]] = UNSET,
    type_nie: Union[Unset, list[str]] = UNSET,
    type_niew: Union[Unset, list[str]] = UNSET,
    type_nisw: Union[Unset, list[str]] = UNSET,
    ui_editable: Union[Unset, ExtrasCustomFieldsListUiEditable] = UNSET,
    ui_visible: Union[Unset, ExtrasCustomFieldsListUiVisible] = UNSET,
    unique: Union[Unset, bool] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    validation_maximum: Union[Unset, list[int]] = UNSET,
    validation_maximum_empty: Union[Unset, bool] = UNSET,
    validation_maximum_gt: Union[Unset, list[int]] = UNSET,
    validation_maximum_gte: Union[Unset, list[int]] = UNSET,
    validation_maximum_lt: Union[Unset, list[int]] = UNSET,
    validation_maximum_lte: Union[Unset, list[int]] = UNSET,
    validation_maximum_n: Union[Unset, list[int]] = UNSET,
    validation_minimum: Union[Unset, list[int]] = UNSET,
    validation_minimum_empty: Union[Unset, bool] = UNSET,
    validation_minimum_gt: Union[Unset, list[int]] = UNSET,
    validation_minimum_gte: Union[Unset, list[int]] = UNSET,
    validation_minimum_lt: Union[Unset, list[int]] = UNSET,
    validation_minimum_lte: Union[Unset, list[int]] = UNSET,
    validation_minimum_n: Union[Unset, list[int]] = UNSET,
    validation_regex: Union[Unset, list[str]] = UNSET,
    validation_regex_empty: Union[Unset, bool] = UNSET,
    validation_regex_ic: Union[Unset, list[str]] = UNSET,
    validation_regex_ie: Union[Unset, list[str]] = UNSET,
    validation_regex_iew: Union[Unset, list[str]] = UNSET,
    validation_regex_isw: Union[Unset, list[str]] = UNSET,
    validation_regex_n: Union[Unset, list[str]] = UNSET,
    validation_regex_nic: Union[Unset, list[str]] = UNSET,
    validation_regex_nie: Union[Unset, list[str]] = UNSET,
    validation_regex_niew: Union[Unset, list[str]] = UNSET,
    validation_regex_nisw: Union[Unset, list[str]] = UNSET,
    weight: Union[Unset, list[int]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[int]] = UNSET,
    weight_gte: Union[Unset, list[int]] = UNSET,
    weight_lt: Union[Unset, list[int]] = UNSET,
    weight_lte: Union[Unset, list[int]] = UNSET,
    weight_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedCustomFieldList]:
    """Get a list of custom field objects.

    Args:
        choice_set (Union[Unset, list[str]]):
        choice_set_n (Union[Unset, list[str]]):
        choice_set_id (Union[Unset, list[Union[None, int]]]):
        choice_set_id_n (Union[Unset, list[Union[None, int]]]):
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
        filter_logic (Union[Unset, ExtrasCustomFieldsListFilterLogic]):
        group_name (Union[Unset, list[str]]):
        group_name_empty (Union[Unset, bool]):
        group_name_ic (Union[Unset, list[str]]):
        group_name_ie (Union[Unset, list[str]]):
        group_name_iew (Union[Unset, list[str]]):
        group_name_isw (Union[Unset, list[str]]):
        group_name_n (Union[Unset, list[str]]):
        group_name_nic (Union[Unset, list[str]]):
        group_name_nie (Union[Unset, list[str]]):
        group_name_niew (Union[Unset, list[str]]):
        group_name_nisw (Union[Unset, list[str]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_cloneable (Union[Unset, bool]):
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
        object_type (Union[Unset, str]):
        object_type_ic (Union[Unset, str]):
        object_type_ie (Union[Unset, str]):
        object_type_iew (Union[Unset, str]):
        object_type_isw (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_nic (Union[Unset, str]):
        object_type_nie (Union[Unset, str]):
        object_type_niew (Union[Unset, str]):
        object_type_nisw (Union[Unset, str]):
        object_type_id (Union[Unset, list[int]]):
        object_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        related_object_type (Union[Unset, str]):
        related_object_type_n (Union[Unset, str]):
        related_object_type_id (Union[Unset, list[int]]):
        related_object_type_id_n (Union[Unset, list[int]]):
        required (Union[Unset, bool]):
        search_weight (Union[Unset, list[int]]):
        search_weight_empty (Union[Unset, bool]):
        search_weight_gt (Union[Unset, list[int]]):
        search_weight_gte (Union[Unset, list[int]]):
        search_weight_lt (Union[Unset, list[int]]):
        search_weight_lte (Union[Unset, list[int]]):
        search_weight_n (Union[Unset, list[int]]):
        type_ (Union[Unset, list[str]]):
        type_empty (Union[Unset, bool]):
        type_ic (Union[Unset, list[str]]):
        type_ie (Union[Unset, list[str]]):
        type_iew (Union[Unset, list[str]]):
        type_isw (Union[Unset, list[str]]):
        type_n (Union[Unset, list[str]]):
        type_nic (Union[Unset, list[str]]):
        type_nie (Union[Unset, list[str]]):
        type_niew (Union[Unset, list[str]]):
        type_nisw (Union[Unset, list[str]]):
        ui_editable (Union[Unset, ExtrasCustomFieldsListUiEditable]):
        ui_visible (Union[Unset, ExtrasCustomFieldsListUiVisible]):
        unique (Union[Unset, bool]):
        updated_by_request (Union[Unset, UUID]):
        validation_maximum (Union[Unset, list[int]]):
        validation_maximum_empty (Union[Unset, bool]):
        validation_maximum_gt (Union[Unset, list[int]]):
        validation_maximum_gte (Union[Unset, list[int]]):
        validation_maximum_lt (Union[Unset, list[int]]):
        validation_maximum_lte (Union[Unset, list[int]]):
        validation_maximum_n (Union[Unset, list[int]]):
        validation_minimum (Union[Unset, list[int]]):
        validation_minimum_empty (Union[Unset, bool]):
        validation_minimum_gt (Union[Unset, list[int]]):
        validation_minimum_gte (Union[Unset, list[int]]):
        validation_minimum_lt (Union[Unset, list[int]]):
        validation_minimum_lte (Union[Unset, list[int]]):
        validation_minimum_n (Union[Unset, list[int]]):
        validation_regex (Union[Unset, list[str]]):
        validation_regex_empty (Union[Unset, bool]):
        validation_regex_ic (Union[Unset, list[str]]):
        validation_regex_ie (Union[Unset, list[str]]):
        validation_regex_iew (Union[Unset, list[str]]):
        validation_regex_isw (Union[Unset, list[str]]):
        validation_regex_n (Union[Unset, list[str]]):
        validation_regex_nic (Union[Unset, list[str]]):
        validation_regex_nie (Union[Unset, list[str]]):
        validation_regex_niew (Union[Unset, list[str]]):
        validation_regex_nisw (Union[Unset, list[str]]):
        weight (Union[Unset, list[int]]):
        weight_empty (Union[Unset, bool]):
        weight_gt (Union[Unset, list[int]]):
        weight_gte (Union[Unset, list[int]]):
        weight_lt (Union[Unset, list[int]]):
        weight_lte (Union[Unset, list[int]]):
        weight_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCustomFieldList]
    """

    kwargs = _get_kwargs(
        choice_set=choice_set,
        choice_set_n=choice_set_n,
        choice_set_id=choice_set_id,
        choice_set_id_n=choice_set_id_n,
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
        filter_logic=filter_logic,
        group_name=group_name,
        group_name_empty=group_name_empty,
        group_name_ic=group_name_ic,
        group_name_ie=group_name_ie,
        group_name_iew=group_name_iew,
        group_name_isw=group_name_isw,
        group_name_n=group_name_n,
        group_name_nic=group_name_nic,
        group_name_nie=group_name_nie,
        group_name_niew=group_name_niew,
        group_name_nisw=group_name_nisw,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        is_cloneable=is_cloneable,
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
        object_type=object_type,
        object_type_ic=object_type_ic,
        object_type_ie=object_type_ie,
        object_type_iew=object_type_iew,
        object_type_isw=object_type_isw,
        object_type_n=object_type_n,
        object_type_nic=object_type_nic,
        object_type_nie=object_type_nie,
        object_type_niew=object_type_niew,
        object_type_nisw=object_type_nisw,
        object_type_id=object_type_id,
        object_type_id_n=object_type_id_n,
        offset=offset,
        ordering=ordering,
        q=q,
        related_object_type=related_object_type,
        related_object_type_n=related_object_type_n,
        related_object_type_id=related_object_type_id,
        related_object_type_id_n=related_object_type_id_n,
        required=required,
        search_weight=search_weight,
        search_weight_empty=search_weight_empty,
        search_weight_gt=search_weight_gt,
        search_weight_gte=search_weight_gte,
        search_weight_lt=search_weight_lt,
        search_weight_lte=search_weight_lte,
        search_weight_n=search_weight_n,
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
        ui_editable=ui_editable,
        ui_visible=ui_visible,
        unique=unique,
        updated_by_request=updated_by_request,
        validation_maximum=validation_maximum,
        validation_maximum_empty=validation_maximum_empty,
        validation_maximum_gt=validation_maximum_gt,
        validation_maximum_gte=validation_maximum_gte,
        validation_maximum_lt=validation_maximum_lt,
        validation_maximum_lte=validation_maximum_lte,
        validation_maximum_n=validation_maximum_n,
        validation_minimum=validation_minimum,
        validation_minimum_empty=validation_minimum_empty,
        validation_minimum_gt=validation_minimum_gt,
        validation_minimum_gte=validation_minimum_gte,
        validation_minimum_lt=validation_minimum_lt,
        validation_minimum_lte=validation_minimum_lte,
        validation_minimum_n=validation_minimum_n,
        validation_regex=validation_regex,
        validation_regex_empty=validation_regex_empty,
        validation_regex_ic=validation_regex_ic,
        validation_regex_ie=validation_regex_ie,
        validation_regex_iew=validation_regex_iew,
        validation_regex_isw=validation_regex_isw,
        validation_regex_n=validation_regex_n,
        validation_regex_nic=validation_regex_nic,
        validation_regex_nie=validation_regex_nie,
        validation_regex_niew=validation_regex_niew,
        validation_regex_nisw=validation_regex_nisw,
        weight=weight,
        weight_empty=weight_empty,
        weight_gt=weight_gt,
        weight_gte=weight_gte,
        weight_lt=weight_lt,
        weight_lte=weight_lte,
        weight_n=weight_n,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    choice_set: Union[Unset, list[str]] = UNSET,
    choice_set_n: Union[Unset, list[str]] = UNSET,
    choice_set_id: Union[Unset, list[Union[None, int]]] = UNSET,
    choice_set_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    filter_logic: Union[Unset, ExtrasCustomFieldsListFilterLogic] = UNSET,
    group_name: Union[Unset, list[str]] = UNSET,
    group_name_empty: Union[Unset, bool] = UNSET,
    group_name_ic: Union[Unset, list[str]] = UNSET,
    group_name_ie: Union[Unset, list[str]] = UNSET,
    group_name_iew: Union[Unset, list[str]] = UNSET,
    group_name_isw: Union[Unset, list[str]] = UNSET,
    group_name_n: Union[Unset, list[str]] = UNSET,
    group_name_nic: Union[Unset, list[str]] = UNSET,
    group_name_nie: Union[Unset, list[str]] = UNSET,
    group_name_niew: Union[Unset, list[str]] = UNSET,
    group_name_nisw: Union[Unset, list[str]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_cloneable: Union[Unset, bool] = UNSET,
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
    object_type: Union[Unset, str] = UNSET,
    object_type_ic: Union[Unset, str] = UNSET,
    object_type_ie: Union[Unset, str] = UNSET,
    object_type_iew: Union[Unset, str] = UNSET,
    object_type_isw: Union[Unset, str] = UNSET,
    object_type_n: Union[Unset, str] = UNSET,
    object_type_nic: Union[Unset, str] = UNSET,
    object_type_nie: Union[Unset, str] = UNSET,
    object_type_niew: Union[Unset, str] = UNSET,
    object_type_nisw: Union[Unset, str] = UNSET,
    object_type_id: Union[Unset, list[int]] = UNSET,
    object_type_id_n: Union[Unset, list[int]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    related_object_type: Union[Unset, str] = UNSET,
    related_object_type_n: Union[Unset, str] = UNSET,
    related_object_type_id: Union[Unset, list[int]] = UNSET,
    related_object_type_id_n: Union[Unset, list[int]] = UNSET,
    required: Union[Unset, bool] = UNSET,
    search_weight: Union[Unset, list[int]] = UNSET,
    search_weight_empty: Union[Unset, bool] = UNSET,
    search_weight_gt: Union[Unset, list[int]] = UNSET,
    search_weight_gte: Union[Unset, list[int]] = UNSET,
    search_weight_lt: Union[Unset, list[int]] = UNSET,
    search_weight_lte: Union[Unset, list[int]] = UNSET,
    search_weight_n: Union[Unset, list[int]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    type_empty: Union[Unset, bool] = UNSET,
    type_ic: Union[Unset, list[str]] = UNSET,
    type_ie: Union[Unset, list[str]] = UNSET,
    type_iew: Union[Unset, list[str]] = UNSET,
    type_isw: Union[Unset, list[str]] = UNSET,
    type_n: Union[Unset, list[str]] = UNSET,
    type_nic: Union[Unset, list[str]] = UNSET,
    type_nie: Union[Unset, list[str]] = UNSET,
    type_niew: Union[Unset, list[str]] = UNSET,
    type_nisw: Union[Unset, list[str]] = UNSET,
    ui_editable: Union[Unset, ExtrasCustomFieldsListUiEditable] = UNSET,
    ui_visible: Union[Unset, ExtrasCustomFieldsListUiVisible] = UNSET,
    unique: Union[Unset, bool] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    validation_maximum: Union[Unset, list[int]] = UNSET,
    validation_maximum_empty: Union[Unset, bool] = UNSET,
    validation_maximum_gt: Union[Unset, list[int]] = UNSET,
    validation_maximum_gte: Union[Unset, list[int]] = UNSET,
    validation_maximum_lt: Union[Unset, list[int]] = UNSET,
    validation_maximum_lte: Union[Unset, list[int]] = UNSET,
    validation_maximum_n: Union[Unset, list[int]] = UNSET,
    validation_minimum: Union[Unset, list[int]] = UNSET,
    validation_minimum_empty: Union[Unset, bool] = UNSET,
    validation_minimum_gt: Union[Unset, list[int]] = UNSET,
    validation_minimum_gte: Union[Unset, list[int]] = UNSET,
    validation_minimum_lt: Union[Unset, list[int]] = UNSET,
    validation_minimum_lte: Union[Unset, list[int]] = UNSET,
    validation_minimum_n: Union[Unset, list[int]] = UNSET,
    validation_regex: Union[Unset, list[str]] = UNSET,
    validation_regex_empty: Union[Unset, bool] = UNSET,
    validation_regex_ic: Union[Unset, list[str]] = UNSET,
    validation_regex_ie: Union[Unset, list[str]] = UNSET,
    validation_regex_iew: Union[Unset, list[str]] = UNSET,
    validation_regex_isw: Union[Unset, list[str]] = UNSET,
    validation_regex_n: Union[Unset, list[str]] = UNSET,
    validation_regex_nic: Union[Unset, list[str]] = UNSET,
    validation_regex_nie: Union[Unset, list[str]] = UNSET,
    validation_regex_niew: Union[Unset, list[str]] = UNSET,
    validation_regex_nisw: Union[Unset, list[str]] = UNSET,
    weight: Union[Unset, list[int]] = UNSET,
    weight_empty: Union[Unset, bool] = UNSET,
    weight_gt: Union[Unset, list[int]] = UNSET,
    weight_gte: Union[Unset, list[int]] = UNSET,
    weight_lt: Union[Unset, list[int]] = UNSET,
    weight_lte: Union[Unset, list[int]] = UNSET,
    weight_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedCustomFieldList]:
    """Get a list of custom field objects.

    Args:
        choice_set (Union[Unset, list[str]]):
        choice_set_n (Union[Unset, list[str]]):
        choice_set_id (Union[Unset, list[Union[None, int]]]):
        choice_set_id_n (Union[Unset, list[Union[None, int]]]):
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
        filter_logic (Union[Unset, ExtrasCustomFieldsListFilterLogic]):
        group_name (Union[Unset, list[str]]):
        group_name_empty (Union[Unset, bool]):
        group_name_ic (Union[Unset, list[str]]):
        group_name_ie (Union[Unset, list[str]]):
        group_name_iew (Union[Unset, list[str]]):
        group_name_isw (Union[Unset, list[str]]):
        group_name_n (Union[Unset, list[str]]):
        group_name_nic (Union[Unset, list[str]]):
        group_name_nie (Union[Unset, list[str]]):
        group_name_niew (Union[Unset, list[str]]):
        group_name_nisw (Union[Unset, list[str]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_cloneable (Union[Unset, bool]):
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
        object_type (Union[Unset, str]):
        object_type_ic (Union[Unset, str]):
        object_type_ie (Union[Unset, str]):
        object_type_iew (Union[Unset, str]):
        object_type_isw (Union[Unset, str]):
        object_type_n (Union[Unset, str]):
        object_type_nic (Union[Unset, str]):
        object_type_nie (Union[Unset, str]):
        object_type_niew (Union[Unset, str]):
        object_type_nisw (Union[Unset, str]):
        object_type_id (Union[Unset, list[int]]):
        object_type_id_n (Union[Unset, list[int]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        related_object_type (Union[Unset, str]):
        related_object_type_n (Union[Unset, str]):
        related_object_type_id (Union[Unset, list[int]]):
        related_object_type_id_n (Union[Unset, list[int]]):
        required (Union[Unset, bool]):
        search_weight (Union[Unset, list[int]]):
        search_weight_empty (Union[Unset, bool]):
        search_weight_gt (Union[Unset, list[int]]):
        search_weight_gte (Union[Unset, list[int]]):
        search_weight_lt (Union[Unset, list[int]]):
        search_weight_lte (Union[Unset, list[int]]):
        search_weight_n (Union[Unset, list[int]]):
        type_ (Union[Unset, list[str]]):
        type_empty (Union[Unset, bool]):
        type_ic (Union[Unset, list[str]]):
        type_ie (Union[Unset, list[str]]):
        type_iew (Union[Unset, list[str]]):
        type_isw (Union[Unset, list[str]]):
        type_n (Union[Unset, list[str]]):
        type_nic (Union[Unset, list[str]]):
        type_nie (Union[Unset, list[str]]):
        type_niew (Union[Unset, list[str]]):
        type_nisw (Union[Unset, list[str]]):
        ui_editable (Union[Unset, ExtrasCustomFieldsListUiEditable]):
        ui_visible (Union[Unset, ExtrasCustomFieldsListUiVisible]):
        unique (Union[Unset, bool]):
        updated_by_request (Union[Unset, UUID]):
        validation_maximum (Union[Unset, list[int]]):
        validation_maximum_empty (Union[Unset, bool]):
        validation_maximum_gt (Union[Unset, list[int]]):
        validation_maximum_gte (Union[Unset, list[int]]):
        validation_maximum_lt (Union[Unset, list[int]]):
        validation_maximum_lte (Union[Unset, list[int]]):
        validation_maximum_n (Union[Unset, list[int]]):
        validation_minimum (Union[Unset, list[int]]):
        validation_minimum_empty (Union[Unset, bool]):
        validation_minimum_gt (Union[Unset, list[int]]):
        validation_minimum_gte (Union[Unset, list[int]]):
        validation_minimum_lt (Union[Unset, list[int]]):
        validation_minimum_lte (Union[Unset, list[int]]):
        validation_minimum_n (Union[Unset, list[int]]):
        validation_regex (Union[Unset, list[str]]):
        validation_regex_empty (Union[Unset, bool]):
        validation_regex_ic (Union[Unset, list[str]]):
        validation_regex_ie (Union[Unset, list[str]]):
        validation_regex_iew (Union[Unset, list[str]]):
        validation_regex_isw (Union[Unset, list[str]]):
        validation_regex_n (Union[Unset, list[str]]):
        validation_regex_nic (Union[Unset, list[str]]):
        validation_regex_nie (Union[Unset, list[str]]):
        validation_regex_niew (Union[Unset, list[str]]):
        validation_regex_nisw (Union[Unset, list[str]]):
        weight (Union[Unset, list[int]]):
        weight_empty (Union[Unset, bool]):
        weight_gt (Union[Unset, list[int]]):
        weight_gte (Union[Unset, list[int]]):
        weight_lt (Union[Unset, list[int]]):
        weight_lte (Union[Unset, list[int]]):
        weight_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCustomFieldList
    """

    return (
        await asyncio_detailed(
            client=client,
            choice_set=choice_set,
            choice_set_n=choice_set_n,
            choice_set_id=choice_set_id,
            choice_set_id_n=choice_set_id_n,
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
            filter_logic=filter_logic,
            group_name=group_name,
            group_name_empty=group_name_empty,
            group_name_ic=group_name_ic,
            group_name_ie=group_name_ie,
            group_name_iew=group_name_iew,
            group_name_isw=group_name_isw,
            group_name_n=group_name_n,
            group_name_nic=group_name_nic,
            group_name_nie=group_name_nie,
            group_name_niew=group_name_niew,
            group_name_nisw=group_name_nisw,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            is_cloneable=is_cloneable,
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
            object_type=object_type,
            object_type_ic=object_type_ic,
            object_type_ie=object_type_ie,
            object_type_iew=object_type_iew,
            object_type_isw=object_type_isw,
            object_type_n=object_type_n,
            object_type_nic=object_type_nic,
            object_type_nie=object_type_nie,
            object_type_niew=object_type_niew,
            object_type_nisw=object_type_nisw,
            object_type_id=object_type_id,
            object_type_id_n=object_type_id_n,
            offset=offset,
            ordering=ordering,
            q=q,
            related_object_type=related_object_type,
            related_object_type_n=related_object_type_n,
            related_object_type_id=related_object_type_id,
            related_object_type_id_n=related_object_type_id_n,
            required=required,
            search_weight=search_weight,
            search_weight_empty=search_weight_empty,
            search_weight_gt=search_weight_gt,
            search_weight_gte=search_weight_gte,
            search_weight_lt=search_weight_lt,
            search_weight_lte=search_weight_lte,
            search_weight_n=search_weight_n,
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
            ui_editable=ui_editable,
            ui_visible=ui_visible,
            unique=unique,
            updated_by_request=updated_by_request,
            validation_maximum=validation_maximum,
            validation_maximum_empty=validation_maximum_empty,
            validation_maximum_gt=validation_maximum_gt,
            validation_maximum_gte=validation_maximum_gte,
            validation_maximum_lt=validation_maximum_lt,
            validation_maximum_lte=validation_maximum_lte,
            validation_maximum_n=validation_maximum_n,
            validation_minimum=validation_minimum,
            validation_minimum_empty=validation_minimum_empty,
            validation_minimum_gt=validation_minimum_gt,
            validation_minimum_gte=validation_minimum_gte,
            validation_minimum_lt=validation_minimum_lt,
            validation_minimum_lte=validation_minimum_lte,
            validation_minimum_n=validation_minimum_n,
            validation_regex=validation_regex,
            validation_regex_empty=validation_regex_empty,
            validation_regex_ic=validation_regex_ic,
            validation_regex_ie=validation_regex_ie,
            validation_regex_iew=validation_regex_iew,
            validation_regex_isw=validation_regex_isw,
            validation_regex_n=validation_regex_n,
            validation_regex_nic=validation_regex_nic,
            validation_regex_nie=validation_regex_nie,
            validation_regex_niew=validation_regex_niew,
            validation_regex_nisw=validation_regex_nisw,
            weight=weight,
            weight_empty=weight_empty,
            weight_gt=weight_gt,
            weight_gte=weight_gte,
            weight_lt=weight_lt,
            weight_lte=weight_lte,
            weight_n=weight_n,
        )
    ).parsed
