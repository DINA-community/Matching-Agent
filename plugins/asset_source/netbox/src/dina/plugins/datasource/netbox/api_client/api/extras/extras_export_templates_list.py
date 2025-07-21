import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_export_template_list import PaginatedExportTemplateList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    as_attachment: Union[Unset, bool] = UNSET,
    auto_sync_enabled: Union[Unset, bool] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    data_file_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_file_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_synced: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_empty: Union[Unset, bool] = UNSET,
    data_synced_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_n: Union[Unset, list[datetime.datetime]] = UNSET,
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
    file_extension: Union[Unset, list[str]] = UNSET,
    file_extension_empty: Union[Unset, bool] = UNSET,
    file_extension_ic: Union[Unset, list[str]] = UNSET,
    file_extension_ie: Union[Unset, list[str]] = UNSET,
    file_extension_iew: Union[Unset, list[str]] = UNSET,
    file_extension_isw: Union[Unset, list[str]] = UNSET,
    file_extension_n: Union[Unset, list[str]] = UNSET,
    file_extension_nic: Union[Unset, list[str]] = UNSET,
    file_extension_nie: Union[Unset, list[str]] = UNSET,
    file_extension_niew: Union[Unset, list[str]] = UNSET,
    file_extension_nisw: Union[Unset, list[str]] = UNSET,
    file_name: Union[Unset, list[str]] = UNSET,
    file_name_empty: Union[Unset, bool] = UNSET,
    file_name_ic: Union[Unset, list[str]] = UNSET,
    file_name_ie: Union[Unset, list[str]] = UNSET,
    file_name_iew: Union[Unset, list[str]] = UNSET,
    file_name_isw: Union[Unset, list[str]] = UNSET,
    file_name_n: Union[Unset, list[str]] = UNSET,
    file_name_nic: Union[Unset, list[str]] = UNSET,
    file_name_nie: Union[Unset, list[str]] = UNSET,
    file_name_niew: Union[Unset, list[str]] = UNSET,
    file_name_nisw: Union[Unset, list[str]] = UNSET,
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
    mime_type: Union[Unset, list[str]] = UNSET,
    mime_type_empty: Union[Unset, bool] = UNSET,
    mime_type_ic: Union[Unset, list[str]] = UNSET,
    mime_type_ie: Union[Unset, list[str]] = UNSET,
    mime_type_iew: Union[Unset, list[str]] = UNSET,
    mime_type_isw: Union[Unset, list[str]] = UNSET,
    mime_type_n: Union[Unset, list[str]] = UNSET,
    mime_type_nic: Union[Unset, list[str]] = UNSET,
    mime_type_nie: Union[Unset, list[str]] = UNSET,
    mime_type_niew: Union[Unset, list[str]] = UNSET,
    mime_type_nisw: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["as_attachment"] = as_attachment

    params["auto_sync_enabled"] = auto_sync_enabled

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

    json_data_file_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(data_file_id, Unset):
        json_data_file_id = []
        for data_file_id_item_data in data_file_id:
            data_file_id_item: Union[None, int]
            data_file_id_item = data_file_id_item_data
            json_data_file_id.append(data_file_id_item)

    params["data_file_id"] = json_data_file_id

    json_data_file_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(data_file_id_n, Unset):
        json_data_file_id_n = []
        for data_file_id_n_item_data in data_file_id_n:
            data_file_id_n_item: Union[None, int]
            data_file_id_n_item = data_file_id_n_item_data
            json_data_file_id_n.append(data_file_id_n_item)

    params["data_file_id__n"] = json_data_file_id_n

    json_data_source_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(data_source_id, Unset):
        json_data_source_id = []
        for data_source_id_item_data in data_source_id:
            data_source_id_item: Union[None, int]
            data_source_id_item = data_source_id_item_data
            json_data_source_id.append(data_source_id_item)

    params["data_source_id"] = json_data_source_id

    json_data_source_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(data_source_id_n, Unset):
        json_data_source_id_n = []
        for data_source_id_n_item_data in data_source_id_n:
            data_source_id_n_item: Union[None, int]
            data_source_id_n_item = data_source_id_n_item_data
            json_data_source_id_n.append(data_source_id_n_item)

    params["data_source_id__n"] = json_data_source_id_n

    json_data_synced: Union[Unset, list[str]] = UNSET
    if not isinstance(data_synced, Unset):
        json_data_synced = []
        for data_synced_item_data in data_synced:
            data_synced_item = data_synced_item_data.isoformat()
            json_data_synced.append(data_synced_item)

    params["data_synced"] = json_data_synced

    params["data_synced__empty"] = data_synced_empty

    json_data_synced_gt: Union[Unset, list[str]] = UNSET
    if not isinstance(data_synced_gt, Unset):
        json_data_synced_gt = []
        for data_synced_gt_item_data in data_synced_gt:
            data_synced_gt_item = data_synced_gt_item_data.isoformat()
            json_data_synced_gt.append(data_synced_gt_item)

    params["data_synced__gt"] = json_data_synced_gt

    json_data_synced_gte: Union[Unset, list[str]] = UNSET
    if not isinstance(data_synced_gte, Unset):
        json_data_synced_gte = []
        for data_synced_gte_item_data in data_synced_gte:
            data_synced_gte_item = data_synced_gte_item_data.isoformat()
            json_data_synced_gte.append(data_synced_gte_item)

    params["data_synced__gte"] = json_data_synced_gte

    json_data_synced_lt: Union[Unset, list[str]] = UNSET
    if not isinstance(data_synced_lt, Unset):
        json_data_synced_lt = []
        for data_synced_lt_item_data in data_synced_lt:
            data_synced_lt_item = data_synced_lt_item_data.isoformat()
            json_data_synced_lt.append(data_synced_lt_item)

    params["data_synced__lt"] = json_data_synced_lt

    json_data_synced_lte: Union[Unset, list[str]] = UNSET
    if not isinstance(data_synced_lte, Unset):
        json_data_synced_lte = []
        for data_synced_lte_item_data in data_synced_lte:
            data_synced_lte_item = data_synced_lte_item_data.isoformat()
            json_data_synced_lte.append(data_synced_lte_item)

    params["data_synced__lte"] = json_data_synced_lte

    json_data_synced_n: Union[Unset, list[str]] = UNSET
    if not isinstance(data_synced_n, Unset):
        json_data_synced_n = []
        for data_synced_n_item_data in data_synced_n:
            data_synced_n_item = data_synced_n_item_data.isoformat()
            json_data_synced_n.append(data_synced_n_item)

    params["data_synced__n"] = json_data_synced_n

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

    json_file_extension: Union[Unset, list[str]] = UNSET
    if not isinstance(file_extension, Unset):
        json_file_extension = file_extension

    params["file_extension"] = json_file_extension

    params["file_extension__empty"] = file_extension_empty

    json_file_extension_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(file_extension_ic, Unset):
        json_file_extension_ic = file_extension_ic

    params["file_extension__ic"] = json_file_extension_ic

    json_file_extension_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(file_extension_ie, Unset):
        json_file_extension_ie = file_extension_ie

    params["file_extension__ie"] = json_file_extension_ie

    json_file_extension_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(file_extension_iew, Unset):
        json_file_extension_iew = file_extension_iew

    params["file_extension__iew"] = json_file_extension_iew

    json_file_extension_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(file_extension_isw, Unset):
        json_file_extension_isw = file_extension_isw

    params["file_extension__isw"] = json_file_extension_isw

    json_file_extension_n: Union[Unset, list[str]] = UNSET
    if not isinstance(file_extension_n, Unset):
        json_file_extension_n = file_extension_n

    params["file_extension__n"] = json_file_extension_n

    json_file_extension_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(file_extension_nic, Unset):
        json_file_extension_nic = file_extension_nic

    params["file_extension__nic"] = json_file_extension_nic

    json_file_extension_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(file_extension_nie, Unset):
        json_file_extension_nie = file_extension_nie

    params["file_extension__nie"] = json_file_extension_nie

    json_file_extension_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(file_extension_niew, Unset):
        json_file_extension_niew = file_extension_niew

    params["file_extension__niew"] = json_file_extension_niew

    json_file_extension_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(file_extension_nisw, Unset):
        json_file_extension_nisw = file_extension_nisw

    params["file_extension__nisw"] = json_file_extension_nisw

    json_file_name: Union[Unset, list[str]] = UNSET
    if not isinstance(file_name, Unset):
        json_file_name = file_name

    params["file_name"] = json_file_name

    params["file_name__empty"] = file_name_empty

    json_file_name_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(file_name_ic, Unset):
        json_file_name_ic = file_name_ic

    params["file_name__ic"] = json_file_name_ic

    json_file_name_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(file_name_ie, Unset):
        json_file_name_ie = file_name_ie

    params["file_name__ie"] = json_file_name_ie

    json_file_name_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(file_name_iew, Unset):
        json_file_name_iew = file_name_iew

    params["file_name__iew"] = json_file_name_iew

    json_file_name_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(file_name_isw, Unset):
        json_file_name_isw = file_name_isw

    params["file_name__isw"] = json_file_name_isw

    json_file_name_n: Union[Unset, list[str]] = UNSET
    if not isinstance(file_name_n, Unset):
        json_file_name_n = file_name_n

    params["file_name__n"] = json_file_name_n

    json_file_name_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(file_name_nic, Unset):
        json_file_name_nic = file_name_nic

    params["file_name__nic"] = json_file_name_nic

    json_file_name_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(file_name_nie, Unset):
        json_file_name_nie = file_name_nie

    params["file_name__nie"] = json_file_name_nie

    json_file_name_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(file_name_niew, Unset):
        json_file_name_niew = file_name_niew

    params["file_name__niew"] = json_file_name_niew

    json_file_name_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(file_name_nisw, Unset):
        json_file_name_nisw = file_name_nisw

    params["file_name__nisw"] = json_file_name_nisw

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

    json_mime_type: Union[Unset, list[str]] = UNSET
    if not isinstance(mime_type, Unset):
        json_mime_type = mime_type

    params["mime_type"] = json_mime_type

    params["mime_type__empty"] = mime_type_empty

    json_mime_type_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(mime_type_ic, Unset):
        json_mime_type_ic = mime_type_ic

    params["mime_type__ic"] = json_mime_type_ic

    json_mime_type_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(mime_type_ie, Unset):
        json_mime_type_ie = mime_type_ie

    params["mime_type__ie"] = json_mime_type_ie

    json_mime_type_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(mime_type_iew, Unset):
        json_mime_type_iew = mime_type_iew

    params["mime_type__iew"] = json_mime_type_iew

    json_mime_type_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(mime_type_isw, Unset):
        json_mime_type_isw = mime_type_isw

    params["mime_type__isw"] = json_mime_type_isw

    json_mime_type_n: Union[Unset, list[str]] = UNSET
    if not isinstance(mime_type_n, Unset):
        json_mime_type_n = mime_type_n

    params["mime_type__n"] = json_mime_type_n

    json_mime_type_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(mime_type_nic, Unset):
        json_mime_type_nic = mime_type_nic

    params["mime_type__nic"] = json_mime_type_nic

    json_mime_type_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(mime_type_nie, Unset):
        json_mime_type_nie = mime_type_nie

    params["mime_type__nie"] = json_mime_type_nie

    json_mime_type_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(mime_type_niew, Unset):
        json_mime_type_niew = mime_type_niew

    params["mime_type__niew"] = json_mime_type_niew

    json_mime_type_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(mime_type_nisw, Unset):
        json_mime_type_nisw = mime_type_nisw

    params["mime_type__nisw"] = json_mime_type_nisw

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

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/extras/export-templates/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedExportTemplateList]:
    if response.status_code == 200:
        response_200 = PaginatedExportTemplateList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedExportTemplateList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    as_attachment: Union[Unset, bool] = UNSET,
    auto_sync_enabled: Union[Unset, bool] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    data_file_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_file_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_synced: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_empty: Union[Unset, bool] = UNSET,
    data_synced_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_n: Union[Unset, list[datetime.datetime]] = UNSET,
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
    file_extension: Union[Unset, list[str]] = UNSET,
    file_extension_empty: Union[Unset, bool] = UNSET,
    file_extension_ic: Union[Unset, list[str]] = UNSET,
    file_extension_ie: Union[Unset, list[str]] = UNSET,
    file_extension_iew: Union[Unset, list[str]] = UNSET,
    file_extension_isw: Union[Unset, list[str]] = UNSET,
    file_extension_n: Union[Unset, list[str]] = UNSET,
    file_extension_nic: Union[Unset, list[str]] = UNSET,
    file_extension_nie: Union[Unset, list[str]] = UNSET,
    file_extension_niew: Union[Unset, list[str]] = UNSET,
    file_extension_nisw: Union[Unset, list[str]] = UNSET,
    file_name: Union[Unset, list[str]] = UNSET,
    file_name_empty: Union[Unset, bool] = UNSET,
    file_name_ic: Union[Unset, list[str]] = UNSET,
    file_name_ie: Union[Unset, list[str]] = UNSET,
    file_name_iew: Union[Unset, list[str]] = UNSET,
    file_name_isw: Union[Unset, list[str]] = UNSET,
    file_name_n: Union[Unset, list[str]] = UNSET,
    file_name_nic: Union[Unset, list[str]] = UNSET,
    file_name_nie: Union[Unset, list[str]] = UNSET,
    file_name_niew: Union[Unset, list[str]] = UNSET,
    file_name_nisw: Union[Unset, list[str]] = UNSET,
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
    mime_type: Union[Unset, list[str]] = UNSET,
    mime_type_empty: Union[Unset, bool] = UNSET,
    mime_type_ic: Union[Unset, list[str]] = UNSET,
    mime_type_ie: Union[Unset, list[str]] = UNSET,
    mime_type_iew: Union[Unset, list[str]] = UNSET,
    mime_type_isw: Union[Unset, list[str]] = UNSET,
    mime_type_n: Union[Unset, list[str]] = UNSET,
    mime_type_nic: Union[Unset, list[str]] = UNSET,
    mime_type_nie: Union[Unset, list[str]] = UNSET,
    mime_type_niew: Union[Unset, list[str]] = UNSET,
    mime_type_nisw: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedExportTemplateList]:
    """Get a list of export template objects.

    Args:
        as_attachment (Union[Unset, bool]):
        auto_sync_enabled (Union[Unset, bool]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        data_file_id (Union[Unset, list[Union[None, int]]]):
        data_file_id_n (Union[Unset, list[Union[None, int]]]):
        data_source_id (Union[Unset, list[Union[None, int]]]):
        data_source_id_n (Union[Unset, list[Union[None, int]]]):
        data_synced (Union[Unset, list[datetime.datetime]]):
        data_synced_empty (Union[Unset, bool]):
        data_synced_gt (Union[Unset, list[datetime.datetime]]):
        data_synced_gte (Union[Unset, list[datetime.datetime]]):
        data_synced_lt (Union[Unset, list[datetime.datetime]]):
        data_synced_lte (Union[Unset, list[datetime.datetime]]):
        data_synced_n (Union[Unset, list[datetime.datetime]]):
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
        file_extension (Union[Unset, list[str]]):
        file_extension_empty (Union[Unset, bool]):
        file_extension_ic (Union[Unset, list[str]]):
        file_extension_ie (Union[Unset, list[str]]):
        file_extension_iew (Union[Unset, list[str]]):
        file_extension_isw (Union[Unset, list[str]]):
        file_extension_n (Union[Unset, list[str]]):
        file_extension_nic (Union[Unset, list[str]]):
        file_extension_nie (Union[Unset, list[str]]):
        file_extension_niew (Union[Unset, list[str]]):
        file_extension_nisw (Union[Unset, list[str]]):
        file_name (Union[Unset, list[str]]):
        file_name_empty (Union[Unset, bool]):
        file_name_ic (Union[Unset, list[str]]):
        file_name_ie (Union[Unset, list[str]]):
        file_name_iew (Union[Unset, list[str]]):
        file_name_isw (Union[Unset, list[str]]):
        file_name_n (Union[Unset, list[str]]):
        file_name_nic (Union[Unset, list[str]]):
        file_name_nie (Union[Unset, list[str]]):
        file_name_niew (Union[Unset, list[str]]):
        file_name_nisw (Union[Unset, list[str]]):
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
        mime_type (Union[Unset, list[str]]):
        mime_type_empty (Union[Unset, bool]):
        mime_type_ic (Union[Unset, list[str]]):
        mime_type_ie (Union[Unset, list[str]]):
        mime_type_iew (Union[Unset, list[str]]):
        mime_type_isw (Union[Unset, list[str]]):
        mime_type_n (Union[Unset, list[str]]):
        mime_type_nic (Union[Unset, list[str]]):
        mime_type_nie (Union[Unset, list[str]]):
        mime_type_niew (Union[Unset, list[str]]):
        mime_type_nisw (Union[Unset, list[str]]):
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
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedExportTemplateList]
    """

    kwargs = _get_kwargs(
        as_attachment=as_attachment,
        auto_sync_enabled=auto_sync_enabled,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        data_file_id=data_file_id,
        data_file_id_n=data_file_id_n,
        data_source_id=data_source_id,
        data_source_id_n=data_source_id_n,
        data_synced=data_synced,
        data_synced_empty=data_synced_empty,
        data_synced_gt=data_synced_gt,
        data_synced_gte=data_synced_gte,
        data_synced_lt=data_synced_lt,
        data_synced_lte=data_synced_lte,
        data_synced_n=data_synced_n,
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
        file_extension=file_extension,
        file_extension_empty=file_extension_empty,
        file_extension_ic=file_extension_ic,
        file_extension_ie=file_extension_ie,
        file_extension_iew=file_extension_iew,
        file_extension_isw=file_extension_isw,
        file_extension_n=file_extension_n,
        file_extension_nic=file_extension_nic,
        file_extension_nie=file_extension_nie,
        file_extension_niew=file_extension_niew,
        file_extension_nisw=file_extension_nisw,
        file_name=file_name,
        file_name_empty=file_name_empty,
        file_name_ic=file_name_ic,
        file_name_ie=file_name_ie,
        file_name_iew=file_name_iew,
        file_name_isw=file_name_isw,
        file_name_n=file_name_n,
        file_name_nic=file_name_nic,
        file_name_nie=file_name_nie,
        file_name_niew=file_name_niew,
        file_name_nisw=file_name_nisw,
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
        mime_type=mime_type,
        mime_type_empty=mime_type_empty,
        mime_type_ic=mime_type_ic,
        mime_type_ie=mime_type_ie,
        mime_type_iew=mime_type_iew,
        mime_type_isw=mime_type_isw,
        mime_type_n=mime_type_n,
        mime_type_nic=mime_type_nic,
        mime_type_nie=mime_type_nie,
        mime_type_niew=mime_type_niew,
        mime_type_nisw=mime_type_nisw,
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
        updated_by_request=updated_by_request,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    as_attachment: Union[Unset, bool] = UNSET,
    auto_sync_enabled: Union[Unset, bool] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    data_file_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_file_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_synced: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_empty: Union[Unset, bool] = UNSET,
    data_synced_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_n: Union[Unset, list[datetime.datetime]] = UNSET,
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
    file_extension: Union[Unset, list[str]] = UNSET,
    file_extension_empty: Union[Unset, bool] = UNSET,
    file_extension_ic: Union[Unset, list[str]] = UNSET,
    file_extension_ie: Union[Unset, list[str]] = UNSET,
    file_extension_iew: Union[Unset, list[str]] = UNSET,
    file_extension_isw: Union[Unset, list[str]] = UNSET,
    file_extension_n: Union[Unset, list[str]] = UNSET,
    file_extension_nic: Union[Unset, list[str]] = UNSET,
    file_extension_nie: Union[Unset, list[str]] = UNSET,
    file_extension_niew: Union[Unset, list[str]] = UNSET,
    file_extension_nisw: Union[Unset, list[str]] = UNSET,
    file_name: Union[Unset, list[str]] = UNSET,
    file_name_empty: Union[Unset, bool] = UNSET,
    file_name_ic: Union[Unset, list[str]] = UNSET,
    file_name_ie: Union[Unset, list[str]] = UNSET,
    file_name_iew: Union[Unset, list[str]] = UNSET,
    file_name_isw: Union[Unset, list[str]] = UNSET,
    file_name_n: Union[Unset, list[str]] = UNSET,
    file_name_nic: Union[Unset, list[str]] = UNSET,
    file_name_nie: Union[Unset, list[str]] = UNSET,
    file_name_niew: Union[Unset, list[str]] = UNSET,
    file_name_nisw: Union[Unset, list[str]] = UNSET,
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
    mime_type: Union[Unset, list[str]] = UNSET,
    mime_type_empty: Union[Unset, bool] = UNSET,
    mime_type_ic: Union[Unset, list[str]] = UNSET,
    mime_type_ie: Union[Unset, list[str]] = UNSET,
    mime_type_iew: Union[Unset, list[str]] = UNSET,
    mime_type_isw: Union[Unset, list[str]] = UNSET,
    mime_type_n: Union[Unset, list[str]] = UNSET,
    mime_type_nic: Union[Unset, list[str]] = UNSET,
    mime_type_nie: Union[Unset, list[str]] = UNSET,
    mime_type_niew: Union[Unset, list[str]] = UNSET,
    mime_type_nisw: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedExportTemplateList]:
    """Get a list of export template objects.

    Args:
        as_attachment (Union[Unset, bool]):
        auto_sync_enabled (Union[Unset, bool]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        data_file_id (Union[Unset, list[Union[None, int]]]):
        data_file_id_n (Union[Unset, list[Union[None, int]]]):
        data_source_id (Union[Unset, list[Union[None, int]]]):
        data_source_id_n (Union[Unset, list[Union[None, int]]]):
        data_synced (Union[Unset, list[datetime.datetime]]):
        data_synced_empty (Union[Unset, bool]):
        data_synced_gt (Union[Unset, list[datetime.datetime]]):
        data_synced_gte (Union[Unset, list[datetime.datetime]]):
        data_synced_lt (Union[Unset, list[datetime.datetime]]):
        data_synced_lte (Union[Unset, list[datetime.datetime]]):
        data_synced_n (Union[Unset, list[datetime.datetime]]):
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
        file_extension (Union[Unset, list[str]]):
        file_extension_empty (Union[Unset, bool]):
        file_extension_ic (Union[Unset, list[str]]):
        file_extension_ie (Union[Unset, list[str]]):
        file_extension_iew (Union[Unset, list[str]]):
        file_extension_isw (Union[Unset, list[str]]):
        file_extension_n (Union[Unset, list[str]]):
        file_extension_nic (Union[Unset, list[str]]):
        file_extension_nie (Union[Unset, list[str]]):
        file_extension_niew (Union[Unset, list[str]]):
        file_extension_nisw (Union[Unset, list[str]]):
        file_name (Union[Unset, list[str]]):
        file_name_empty (Union[Unset, bool]):
        file_name_ic (Union[Unset, list[str]]):
        file_name_ie (Union[Unset, list[str]]):
        file_name_iew (Union[Unset, list[str]]):
        file_name_isw (Union[Unset, list[str]]):
        file_name_n (Union[Unset, list[str]]):
        file_name_nic (Union[Unset, list[str]]):
        file_name_nie (Union[Unset, list[str]]):
        file_name_niew (Union[Unset, list[str]]):
        file_name_nisw (Union[Unset, list[str]]):
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
        mime_type (Union[Unset, list[str]]):
        mime_type_empty (Union[Unset, bool]):
        mime_type_ic (Union[Unset, list[str]]):
        mime_type_ie (Union[Unset, list[str]]):
        mime_type_iew (Union[Unset, list[str]]):
        mime_type_isw (Union[Unset, list[str]]):
        mime_type_n (Union[Unset, list[str]]):
        mime_type_nic (Union[Unset, list[str]]):
        mime_type_nie (Union[Unset, list[str]]):
        mime_type_niew (Union[Unset, list[str]]):
        mime_type_nisw (Union[Unset, list[str]]):
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
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedExportTemplateList
    """

    return sync_detailed(
        client=client,
        as_attachment=as_attachment,
        auto_sync_enabled=auto_sync_enabled,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        data_file_id=data_file_id,
        data_file_id_n=data_file_id_n,
        data_source_id=data_source_id,
        data_source_id_n=data_source_id_n,
        data_synced=data_synced,
        data_synced_empty=data_synced_empty,
        data_synced_gt=data_synced_gt,
        data_synced_gte=data_synced_gte,
        data_synced_lt=data_synced_lt,
        data_synced_lte=data_synced_lte,
        data_synced_n=data_synced_n,
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
        file_extension=file_extension,
        file_extension_empty=file_extension_empty,
        file_extension_ic=file_extension_ic,
        file_extension_ie=file_extension_ie,
        file_extension_iew=file_extension_iew,
        file_extension_isw=file_extension_isw,
        file_extension_n=file_extension_n,
        file_extension_nic=file_extension_nic,
        file_extension_nie=file_extension_nie,
        file_extension_niew=file_extension_niew,
        file_extension_nisw=file_extension_nisw,
        file_name=file_name,
        file_name_empty=file_name_empty,
        file_name_ic=file_name_ic,
        file_name_ie=file_name_ie,
        file_name_iew=file_name_iew,
        file_name_isw=file_name_isw,
        file_name_n=file_name_n,
        file_name_nic=file_name_nic,
        file_name_nie=file_name_nie,
        file_name_niew=file_name_niew,
        file_name_nisw=file_name_nisw,
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
        mime_type=mime_type,
        mime_type_empty=mime_type_empty,
        mime_type_ic=mime_type_ic,
        mime_type_ie=mime_type_ie,
        mime_type_iew=mime_type_iew,
        mime_type_isw=mime_type_isw,
        mime_type_n=mime_type_n,
        mime_type_nic=mime_type_nic,
        mime_type_nie=mime_type_nie,
        mime_type_niew=mime_type_niew,
        mime_type_nisw=mime_type_nisw,
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
        updated_by_request=updated_by_request,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    as_attachment: Union[Unset, bool] = UNSET,
    auto_sync_enabled: Union[Unset, bool] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    data_file_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_file_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_synced: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_empty: Union[Unset, bool] = UNSET,
    data_synced_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_n: Union[Unset, list[datetime.datetime]] = UNSET,
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
    file_extension: Union[Unset, list[str]] = UNSET,
    file_extension_empty: Union[Unset, bool] = UNSET,
    file_extension_ic: Union[Unset, list[str]] = UNSET,
    file_extension_ie: Union[Unset, list[str]] = UNSET,
    file_extension_iew: Union[Unset, list[str]] = UNSET,
    file_extension_isw: Union[Unset, list[str]] = UNSET,
    file_extension_n: Union[Unset, list[str]] = UNSET,
    file_extension_nic: Union[Unset, list[str]] = UNSET,
    file_extension_nie: Union[Unset, list[str]] = UNSET,
    file_extension_niew: Union[Unset, list[str]] = UNSET,
    file_extension_nisw: Union[Unset, list[str]] = UNSET,
    file_name: Union[Unset, list[str]] = UNSET,
    file_name_empty: Union[Unset, bool] = UNSET,
    file_name_ic: Union[Unset, list[str]] = UNSET,
    file_name_ie: Union[Unset, list[str]] = UNSET,
    file_name_iew: Union[Unset, list[str]] = UNSET,
    file_name_isw: Union[Unset, list[str]] = UNSET,
    file_name_n: Union[Unset, list[str]] = UNSET,
    file_name_nic: Union[Unset, list[str]] = UNSET,
    file_name_nie: Union[Unset, list[str]] = UNSET,
    file_name_niew: Union[Unset, list[str]] = UNSET,
    file_name_nisw: Union[Unset, list[str]] = UNSET,
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
    mime_type: Union[Unset, list[str]] = UNSET,
    mime_type_empty: Union[Unset, bool] = UNSET,
    mime_type_ic: Union[Unset, list[str]] = UNSET,
    mime_type_ie: Union[Unset, list[str]] = UNSET,
    mime_type_iew: Union[Unset, list[str]] = UNSET,
    mime_type_isw: Union[Unset, list[str]] = UNSET,
    mime_type_n: Union[Unset, list[str]] = UNSET,
    mime_type_nic: Union[Unset, list[str]] = UNSET,
    mime_type_nie: Union[Unset, list[str]] = UNSET,
    mime_type_niew: Union[Unset, list[str]] = UNSET,
    mime_type_nisw: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedExportTemplateList]:
    """Get a list of export template objects.

    Args:
        as_attachment (Union[Unset, bool]):
        auto_sync_enabled (Union[Unset, bool]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        data_file_id (Union[Unset, list[Union[None, int]]]):
        data_file_id_n (Union[Unset, list[Union[None, int]]]):
        data_source_id (Union[Unset, list[Union[None, int]]]):
        data_source_id_n (Union[Unset, list[Union[None, int]]]):
        data_synced (Union[Unset, list[datetime.datetime]]):
        data_synced_empty (Union[Unset, bool]):
        data_synced_gt (Union[Unset, list[datetime.datetime]]):
        data_synced_gte (Union[Unset, list[datetime.datetime]]):
        data_synced_lt (Union[Unset, list[datetime.datetime]]):
        data_synced_lte (Union[Unset, list[datetime.datetime]]):
        data_synced_n (Union[Unset, list[datetime.datetime]]):
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
        file_extension (Union[Unset, list[str]]):
        file_extension_empty (Union[Unset, bool]):
        file_extension_ic (Union[Unset, list[str]]):
        file_extension_ie (Union[Unset, list[str]]):
        file_extension_iew (Union[Unset, list[str]]):
        file_extension_isw (Union[Unset, list[str]]):
        file_extension_n (Union[Unset, list[str]]):
        file_extension_nic (Union[Unset, list[str]]):
        file_extension_nie (Union[Unset, list[str]]):
        file_extension_niew (Union[Unset, list[str]]):
        file_extension_nisw (Union[Unset, list[str]]):
        file_name (Union[Unset, list[str]]):
        file_name_empty (Union[Unset, bool]):
        file_name_ic (Union[Unset, list[str]]):
        file_name_ie (Union[Unset, list[str]]):
        file_name_iew (Union[Unset, list[str]]):
        file_name_isw (Union[Unset, list[str]]):
        file_name_n (Union[Unset, list[str]]):
        file_name_nic (Union[Unset, list[str]]):
        file_name_nie (Union[Unset, list[str]]):
        file_name_niew (Union[Unset, list[str]]):
        file_name_nisw (Union[Unset, list[str]]):
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
        mime_type (Union[Unset, list[str]]):
        mime_type_empty (Union[Unset, bool]):
        mime_type_ic (Union[Unset, list[str]]):
        mime_type_ie (Union[Unset, list[str]]):
        mime_type_iew (Union[Unset, list[str]]):
        mime_type_isw (Union[Unset, list[str]]):
        mime_type_n (Union[Unset, list[str]]):
        mime_type_nic (Union[Unset, list[str]]):
        mime_type_nie (Union[Unset, list[str]]):
        mime_type_niew (Union[Unset, list[str]]):
        mime_type_nisw (Union[Unset, list[str]]):
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
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedExportTemplateList]
    """

    kwargs = _get_kwargs(
        as_attachment=as_attachment,
        auto_sync_enabled=auto_sync_enabled,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        data_file_id=data_file_id,
        data_file_id_n=data_file_id_n,
        data_source_id=data_source_id,
        data_source_id_n=data_source_id_n,
        data_synced=data_synced,
        data_synced_empty=data_synced_empty,
        data_synced_gt=data_synced_gt,
        data_synced_gte=data_synced_gte,
        data_synced_lt=data_synced_lt,
        data_synced_lte=data_synced_lte,
        data_synced_n=data_synced_n,
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
        file_extension=file_extension,
        file_extension_empty=file_extension_empty,
        file_extension_ic=file_extension_ic,
        file_extension_ie=file_extension_ie,
        file_extension_iew=file_extension_iew,
        file_extension_isw=file_extension_isw,
        file_extension_n=file_extension_n,
        file_extension_nic=file_extension_nic,
        file_extension_nie=file_extension_nie,
        file_extension_niew=file_extension_niew,
        file_extension_nisw=file_extension_nisw,
        file_name=file_name,
        file_name_empty=file_name_empty,
        file_name_ic=file_name_ic,
        file_name_ie=file_name_ie,
        file_name_iew=file_name_iew,
        file_name_isw=file_name_isw,
        file_name_n=file_name_n,
        file_name_nic=file_name_nic,
        file_name_nie=file_name_nie,
        file_name_niew=file_name_niew,
        file_name_nisw=file_name_nisw,
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
        mime_type=mime_type,
        mime_type_empty=mime_type_empty,
        mime_type_ic=mime_type_ic,
        mime_type_ie=mime_type_ie,
        mime_type_iew=mime_type_iew,
        mime_type_isw=mime_type_isw,
        mime_type_n=mime_type_n,
        mime_type_nic=mime_type_nic,
        mime_type_nie=mime_type_nie,
        mime_type_niew=mime_type_niew,
        mime_type_nisw=mime_type_nisw,
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
        updated_by_request=updated_by_request,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    as_attachment: Union[Unset, bool] = UNSET,
    auto_sync_enabled: Union[Unset, bool] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    data_file_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_file_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id: Union[Unset, list[Union[None, int]]] = UNSET,
    data_source_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    data_synced: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_empty: Union[Unset, bool] = UNSET,
    data_synced_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    data_synced_n: Union[Unset, list[datetime.datetime]] = UNSET,
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
    file_extension: Union[Unset, list[str]] = UNSET,
    file_extension_empty: Union[Unset, bool] = UNSET,
    file_extension_ic: Union[Unset, list[str]] = UNSET,
    file_extension_ie: Union[Unset, list[str]] = UNSET,
    file_extension_iew: Union[Unset, list[str]] = UNSET,
    file_extension_isw: Union[Unset, list[str]] = UNSET,
    file_extension_n: Union[Unset, list[str]] = UNSET,
    file_extension_nic: Union[Unset, list[str]] = UNSET,
    file_extension_nie: Union[Unset, list[str]] = UNSET,
    file_extension_niew: Union[Unset, list[str]] = UNSET,
    file_extension_nisw: Union[Unset, list[str]] = UNSET,
    file_name: Union[Unset, list[str]] = UNSET,
    file_name_empty: Union[Unset, bool] = UNSET,
    file_name_ic: Union[Unset, list[str]] = UNSET,
    file_name_ie: Union[Unset, list[str]] = UNSET,
    file_name_iew: Union[Unset, list[str]] = UNSET,
    file_name_isw: Union[Unset, list[str]] = UNSET,
    file_name_n: Union[Unset, list[str]] = UNSET,
    file_name_nic: Union[Unset, list[str]] = UNSET,
    file_name_nie: Union[Unset, list[str]] = UNSET,
    file_name_niew: Union[Unset, list[str]] = UNSET,
    file_name_nisw: Union[Unset, list[str]] = UNSET,
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
    mime_type: Union[Unset, list[str]] = UNSET,
    mime_type_empty: Union[Unset, bool] = UNSET,
    mime_type_ic: Union[Unset, list[str]] = UNSET,
    mime_type_ie: Union[Unset, list[str]] = UNSET,
    mime_type_iew: Union[Unset, list[str]] = UNSET,
    mime_type_isw: Union[Unset, list[str]] = UNSET,
    mime_type_n: Union[Unset, list[str]] = UNSET,
    mime_type_nic: Union[Unset, list[str]] = UNSET,
    mime_type_nie: Union[Unset, list[str]] = UNSET,
    mime_type_niew: Union[Unset, list[str]] = UNSET,
    mime_type_nisw: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedExportTemplateList]:
    """Get a list of export template objects.

    Args:
        as_attachment (Union[Unset, bool]):
        auto_sync_enabled (Union[Unset, bool]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        data_file_id (Union[Unset, list[Union[None, int]]]):
        data_file_id_n (Union[Unset, list[Union[None, int]]]):
        data_source_id (Union[Unset, list[Union[None, int]]]):
        data_source_id_n (Union[Unset, list[Union[None, int]]]):
        data_synced (Union[Unset, list[datetime.datetime]]):
        data_synced_empty (Union[Unset, bool]):
        data_synced_gt (Union[Unset, list[datetime.datetime]]):
        data_synced_gte (Union[Unset, list[datetime.datetime]]):
        data_synced_lt (Union[Unset, list[datetime.datetime]]):
        data_synced_lte (Union[Unset, list[datetime.datetime]]):
        data_synced_n (Union[Unset, list[datetime.datetime]]):
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
        file_extension (Union[Unset, list[str]]):
        file_extension_empty (Union[Unset, bool]):
        file_extension_ic (Union[Unset, list[str]]):
        file_extension_ie (Union[Unset, list[str]]):
        file_extension_iew (Union[Unset, list[str]]):
        file_extension_isw (Union[Unset, list[str]]):
        file_extension_n (Union[Unset, list[str]]):
        file_extension_nic (Union[Unset, list[str]]):
        file_extension_nie (Union[Unset, list[str]]):
        file_extension_niew (Union[Unset, list[str]]):
        file_extension_nisw (Union[Unset, list[str]]):
        file_name (Union[Unset, list[str]]):
        file_name_empty (Union[Unset, bool]):
        file_name_ic (Union[Unset, list[str]]):
        file_name_ie (Union[Unset, list[str]]):
        file_name_iew (Union[Unset, list[str]]):
        file_name_isw (Union[Unset, list[str]]):
        file_name_n (Union[Unset, list[str]]):
        file_name_nic (Union[Unset, list[str]]):
        file_name_nie (Union[Unset, list[str]]):
        file_name_niew (Union[Unset, list[str]]):
        file_name_nisw (Union[Unset, list[str]]):
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
        mime_type (Union[Unset, list[str]]):
        mime_type_empty (Union[Unset, bool]):
        mime_type_ic (Union[Unset, list[str]]):
        mime_type_ie (Union[Unset, list[str]]):
        mime_type_iew (Union[Unset, list[str]]):
        mime_type_isw (Union[Unset, list[str]]):
        mime_type_n (Union[Unset, list[str]]):
        mime_type_nic (Union[Unset, list[str]]):
        mime_type_nie (Union[Unset, list[str]]):
        mime_type_niew (Union[Unset, list[str]]):
        mime_type_nisw (Union[Unset, list[str]]):
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
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedExportTemplateList
    """

    return (
        await asyncio_detailed(
            client=client,
            as_attachment=as_attachment,
            auto_sync_enabled=auto_sync_enabled,
            created=created,
            created_empty=created_empty,
            created_gt=created_gt,
            created_gte=created_gte,
            created_lt=created_lt,
            created_lte=created_lte,
            created_n=created_n,
            created_by_request=created_by_request,
            data_file_id=data_file_id,
            data_file_id_n=data_file_id_n,
            data_source_id=data_source_id,
            data_source_id_n=data_source_id_n,
            data_synced=data_synced,
            data_synced_empty=data_synced_empty,
            data_synced_gt=data_synced_gt,
            data_synced_gte=data_synced_gte,
            data_synced_lt=data_synced_lt,
            data_synced_lte=data_synced_lte,
            data_synced_n=data_synced_n,
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
            file_extension=file_extension,
            file_extension_empty=file_extension_empty,
            file_extension_ic=file_extension_ic,
            file_extension_ie=file_extension_ie,
            file_extension_iew=file_extension_iew,
            file_extension_isw=file_extension_isw,
            file_extension_n=file_extension_n,
            file_extension_nic=file_extension_nic,
            file_extension_nie=file_extension_nie,
            file_extension_niew=file_extension_niew,
            file_extension_nisw=file_extension_nisw,
            file_name=file_name,
            file_name_empty=file_name_empty,
            file_name_ic=file_name_ic,
            file_name_ie=file_name_ie,
            file_name_iew=file_name_iew,
            file_name_isw=file_name_isw,
            file_name_n=file_name_n,
            file_name_nic=file_name_nic,
            file_name_nie=file_name_nie,
            file_name_niew=file_name_niew,
            file_name_nisw=file_name_nisw,
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
            mime_type=mime_type,
            mime_type_empty=mime_type_empty,
            mime_type_ic=mime_type_ic,
            mime_type_ie=mime_type_ie,
            mime_type_iew=mime_type_iew,
            mime_type_isw=mime_type_isw,
            mime_type_n=mime_type_n,
            mime_type_nic=mime_type_nic,
            mime_type_nie=mime_type_nie,
            mime_type_niew=mime_type_niew,
            mime_type_nisw=mime_type_nisw,
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
            updated_by_request=updated_by_request,
        )
    ).parsed
