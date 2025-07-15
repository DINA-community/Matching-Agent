import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_webhook_list import PaginatedWebhookList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ca_file_path: Union[Unset, list[str]] = UNSET,
    ca_file_path_empty: Union[Unset, bool] = UNSET,
    ca_file_path_ic: Union[Unset, list[str]] = UNSET,
    ca_file_path_ie: Union[Unset, list[str]] = UNSET,
    ca_file_path_iew: Union[Unset, list[str]] = UNSET,
    ca_file_path_isw: Union[Unset, list[str]] = UNSET,
    ca_file_path_n: Union[Unset, list[str]] = UNSET,
    ca_file_path_nic: Union[Unset, list[str]] = UNSET,
    ca_file_path_nie: Union[Unset, list[str]] = UNSET,
    ca_file_path_niew: Union[Unset, list[str]] = UNSET,
    ca_file_path_nisw: Union[Unset, list[str]] = UNSET,
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
    http_content_type: Union[Unset, list[str]] = UNSET,
    http_content_type_empty: Union[Unset, bool] = UNSET,
    http_content_type_ic: Union[Unset, list[str]] = UNSET,
    http_content_type_ie: Union[Unset, list[str]] = UNSET,
    http_content_type_iew: Union[Unset, list[str]] = UNSET,
    http_content_type_isw: Union[Unset, list[str]] = UNSET,
    http_content_type_n: Union[Unset, list[str]] = UNSET,
    http_content_type_nic: Union[Unset, list[str]] = UNSET,
    http_content_type_nie: Union[Unset, list[str]] = UNSET,
    http_content_type_niew: Union[Unset, list[str]] = UNSET,
    http_content_type_nisw: Union[Unset, list[str]] = UNSET,
    http_method: Union[Unset, list[str]] = UNSET,
    http_method_empty: Union[Unset, bool] = UNSET,
    http_method_ic: Union[Unset, list[str]] = UNSET,
    http_method_ie: Union[Unset, list[str]] = UNSET,
    http_method_iew: Union[Unset, list[str]] = UNSET,
    http_method_isw: Union[Unset, list[str]] = UNSET,
    http_method_n: Union[Unset, list[str]] = UNSET,
    http_method_nic: Union[Unset, list[str]] = UNSET,
    http_method_nie: Union[Unset, list[str]] = UNSET,
    http_method_niew: Union[Unset, list[str]] = UNSET,
    http_method_nisw: Union[Unset, list[str]] = UNSET,
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
    payload_url: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    secret: Union[Unset, list[str]] = UNSET,
    secret_empty: Union[Unset, bool] = UNSET,
    secret_ic: Union[Unset, list[str]] = UNSET,
    secret_ie: Union[Unset, list[str]] = UNSET,
    secret_iew: Union[Unset, list[str]] = UNSET,
    secret_isw: Union[Unset, list[str]] = UNSET,
    secret_n: Union[Unset, list[str]] = UNSET,
    secret_nic: Union[Unset, list[str]] = UNSET,
    secret_nie: Union[Unset, list[str]] = UNSET,
    secret_niew: Union[Unset, list[str]] = UNSET,
    secret_nisw: Union[Unset, list[str]] = UNSET,
    ssl_verification: Union[Unset, bool] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_ca_file_path: Union[Unset, list[str]] = UNSET
    if not isinstance(ca_file_path, Unset):
        json_ca_file_path = ca_file_path

    params["ca_file_path"] = json_ca_file_path

    params["ca_file_path__empty"] = ca_file_path_empty

    json_ca_file_path_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(ca_file_path_ic, Unset):
        json_ca_file_path_ic = ca_file_path_ic

    params["ca_file_path__ic"] = json_ca_file_path_ic

    json_ca_file_path_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(ca_file_path_ie, Unset):
        json_ca_file_path_ie = ca_file_path_ie

    params["ca_file_path__ie"] = json_ca_file_path_ie

    json_ca_file_path_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(ca_file_path_iew, Unset):
        json_ca_file_path_iew = ca_file_path_iew

    params["ca_file_path__iew"] = json_ca_file_path_iew

    json_ca_file_path_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(ca_file_path_isw, Unset):
        json_ca_file_path_isw = ca_file_path_isw

    params["ca_file_path__isw"] = json_ca_file_path_isw

    json_ca_file_path_n: Union[Unset, list[str]] = UNSET
    if not isinstance(ca_file_path_n, Unset):
        json_ca_file_path_n = ca_file_path_n

    params["ca_file_path__n"] = json_ca_file_path_n

    json_ca_file_path_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(ca_file_path_nic, Unset):
        json_ca_file_path_nic = ca_file_path_nic

    params["ca_file_path__nic"] = json_ca_file_path_nic

    json_ca_file_path_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(ca_file_path_nie, Unset):
        json_ca_file_path_nie = ca_file_path_nie

    params["ca_file_path__nie"] = json_ca_file_path_nie

    json_ca_file_path_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(ca_file_path_niew, Unset):
        json_ca_file_path_niew = ca_file_path_niew

    params["ca_file_path__niew"] = json_ca_file_path_niew

    json_ca_file_path_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(ca_file_path_nisw, Unset):
        json_ca_file_path_nisw = ca_file_path_nisw

    params["ca_file_path__nisw"] = json_ca_file_path_nisw

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

    json_http_content_type: Union[Unset, list[str]] = UNSET
    if not isinstance(http_content_type, Unset):
        json_http_content_type = http_content_type

    params["http_content_type"] = json_http_content_type

    params["http_content_type__empty"] = http_content_type_empty

    json_http_content_type_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(http_content_type_ic, Unset):
        json_http_content_type_ic = http_content_type_ic

    params["http_content_type__ic"] = json_http_content_type_ic

    json_http_content_type_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(http_content_type_ie, Unset):
        json_http_content_type_ie = http_content_type_ie

    params["http_content_type__ie"] = json_http_content_type_ie

    json_http_content_type_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(http_content_type_iew, Unset):
        json_http_content_type_iew = http_content_type_iew

    params["http_content_type__iew"] = json_http_content_type_iew

    json_http_content_type_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(http_content_type_isw, Unset):
        json_http_content_type_isw = http_content_type_isw

    params["http_content_type__isw"] = json_http_content_type_isw

    json_http_content_type_n: Union[Unset, list[str]] = UNSET
    if not isinstance(http_content_type_n, Unset):
        json_http_content_type_n = http_content_type_n

    params["http_content_type__n"] = json_http_content_type_n

    json_http_content_type_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(http_content_type_nic, Unset):
        json_http_content_type_nic = http_content_type_nic

    params["http_content_type__nic"] = json_http_content_type_nic

    json_http_content_type_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(http_content_type_nie, Unset):
        json_http_content_type_nie = http_content_type_nie

    params["http_content_type__nie"] = json_http_content_type_nie

    json_http_content_type_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(http_content_type_niew, Unset):
        json_http_content_type_niew = http_content_type_niew

    params["http_content_type__niew"] = json_http_content_type_niew

    json_http_content_type_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(http_content_type_nisw, Unset):
        json_http_content_type_nisw = http_content_type_nisw

    params["http_content_type__nisw"] = json_http_content_type_nisw

    json_http_method: Union[Unset, list[str]] = UNSET
    if not isinstance(http_method, Unset):
        json_http_method = http_method

    params["http_method"] = json_http_method

    params["http_method__empty"] = http_method_empty

    json_http_method_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(http_method_ic, Unset):
        json_http_method_ic = http_method_ic

    params["http_method__ic"] = json_http_method_ic

    json_http_method_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(http_method_ie, Unset):
        json_http_method_ie = http_method_ie

    params["http_method__ie"] = json_http_method_ie

    json_http_method_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(http_method_iew, Unset):
        json_http_method_iew = http_method_iew

    params["http_method__iew"] = json_http_method_iew

    json_http_method_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(http_method_isw, Unset):
        json_http_method_isw = http_method_isw

    params["http_method__isw"] = json_http_method_isw

    json_http_method_n: Union[Unset, list[str]] = UNSET
    if not isinstance(http_method_n, Unset):
        json_http_method_n = http_method_n

    params["http_method__n"] = json_http_method_n

    json_http_method_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(http_method_nic, Unset):
        json_http_method_nic = http_method_nic

    params["http_method__nic"] = json_http_method_nic

    json_http_method_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(http_method_nie, Unset):
        json_http_method_nie = http_method_nie

    params["http_method__nie"] = json_http_method_nie

    json_http_method_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(http_method_niew, Unset):
        json_http_method_niew = http_method_niew

    params["http_method__niew"] = json_http_method_niew

    json_http_method_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(http_method_nisw, Unset):
        json_http_method_nisw = http_method_nisw

    params["http_method__nisw"] = json_http_method_nisw

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

    json_payload_url: Union[Unset, list[str]] = UNSET
    if not isinstance(payload_url, Unset):
        json_payload_url = payload_url

    params["payload_url"] = json_payload_url

    params["q"] = q

    json_secret: Union[Unset, list[str]] = UNSET
    if not isinstance(secret, Unset):
        json_secret = secret

    params["secret"] = json_secret

    params["secret__empty"] = secret_empty

    json_secret_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(secret_ic, Unset):
        json_secret_ic = secret_ic

    params["secret__ic"] = json_secret_ic

    json_secret_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(secret_ie, Unset):
        json_secret_ie = secret_ie

    params["secret__ie"] = json_secret_ie

    json_secret_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(secret_iew, Unset):
        json_secret_iew = secret_iew

    params["secret__iew"] = json_secret_iew

    json_secret_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(secret_isw, Unset):
        json_secret_isw = secret_isw

    params["secret__isw"] = json_secret_isw

    json_secret_n: Union[Unset, list[str]] = UNSET
    if not isinstance(secret_n, Unset):
        json_secret_n = secret_n

    params["secret__n"] = json_secret_n

    json_secret_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(secret_nic, Unset):
        json_secret_nic = secret_nic

    params["secret__nic"] = json_secret_nic

    json_secret_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(secret_nie, Unset):
        json_secret_nie = secret_nie

    params["secret__nie"] = json_secret_nie

    json_secret_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(secret_niew, Unset):
        json_secret_niew = secret_niew

    params["secret__niew"] = json_secret_niew

    json_secret_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(secret_nisw, Unset):
        json_secret_nisw = secret_nisw

    params["secret__nisw"] = json_secret_nisw

    params["ssl_verification"] = ssl_verification

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
        "url": "/api/extras/webhooks/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedWebhookList]:
    if response.status_code == 200:
        response_200 = PaginatedWebhookList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedWebhookList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ca_file_path: Union[Unset, list[str]] = UNSET,
    ca_file_path_empty: Union[Unset, bool] = UNSET,
    ca_file_path_ic: Union[Unset, list[str]] = UNSET,
    ca_file_path_ie: Union[Unset, list[str]] = UNSET,
    ca_file_path_iew: Union[Unset, list[str]] = UNSET,
    ca_file_path_isw: Union[Unset, list[str]] = UNSET,
    ca_file_path_n: Union[Unset, list[str]] = UNSET,
    ca_file_path_nic: Union[Unset, list[str]] = UNSET,
    ca_file_path_nie: Union[Unset, list[str]] = UNSET,
    ca_file_path_niew: Union[Unset, list[str]] = UNSET,
    ca_file_path_nisw: Union[Unset, list[str]] = UNSET,
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
    http_content_type: Union[Unset, list[str]] = UNSET,
    http_content_type_empty: Union[Unset, bool] = UNSET,
    http_content_type_ic: Union[Unset, list[str]] = UNSET,
    http_content_type_ie: Union[Unset, list[str]] = UNSET,
    http_content_type_iew: Union[Unset, list[str]] = UNSET,
    http_content_type_isw: Union[Unset, list[str]] = UNSET,
    http_content_type_n: Union[Unset, list[str]] = UNSET,
    http_content_type_nic: Union[Unset, list[str]] = UNSET,
    http_content_type_nie: Union[Unset, list[str]] = UNSET,
    http_content_type_niew: Union[Unset, list[str]] = UNSET,
    http_content_type_nisw: Union[Unset, list[str]] = UNSET,
    http_method: Union[Unset, list[str]] = UNSET,
    http_method_empty: Union[Unset, bool] = UNSET,
    http_method_ic: Union[Unset, list[str]] = UNSET,
    http_method_ie: Union[Unset, list[str]] = UNSET,
    http_method_iew: Union[Unset, list[str]] = UNSET,
    http_method_isw: Union[Unset, list[str]] = UNSET,
    http_method_n: Union[Unset, list[str]] = UNSET,
    http_method_nic: Union[Unset, list[str]] = UNSET,
    http_method_nie: Union[Unset, list[str]] = UNSET,
    http_method_niew: Union[Unset, list[str]] = UNSET,
    http_method_nisw: Union[Unset, list[str]] = UNSET,
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
    payload_url: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    secret: Union[Unset, list[str]] = UNSET,
    secret_empty: Union[Unset, bool] = UNSET,
    secret_ic: Union[Unset, list[str]] = UNSET,
    secret_ie: Union[Unset, list[str]] = UNSET,
    secret_iew: Union[Unset, list[str]] = UNSET,
    secret_isw: Union[Unset, list[str]] = UNSET,
    secret_n: Union[Unset, list[str]] = UNSET,
    secret_nic: Union[Unset, list[str]] = UNSET,
    secret_nie: Union[Unset, list[str]] = UNSET,
    secret_niew: Union[Unset, list[str]] = UNSET,
    secret_nisw: Union[Unset, list[str]] = UNSET,
    ssl_verification: Union[Unset, bool] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedWebhookList]:
    """Get a list of webhook objects.

    Args:
        ca_file_path (Union[Unset, list[str]]):
        ca_file_path_empty (Union[Unset, bool]):
        ca_file_path_ic (Union[Unset, list[str]]):
        ca_file_path_ie (Union[Unset, list[str]]):
        ca_file_path_iew (Union[Unset, list[str]]):
        ca_file_path_isw (Union[Unset, list[str]]):
        ca_file_path_n (Union[Unset, list[str]]):
        ca_file_path_nic (Union[Unset, list[str]]):
        ca_file_path_nie (Union[Unset, list[str]]):
        ca_file_path_niew (Union[Unset, list[str]]):
        ca_file_path_nisw (Union[Unset, list[str]]):
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
        http_content_type (Union[Unset, list[str]]):
        http_content_type_empty (Union[Unset, bool]):
        http_content_type_ic (Union[Unset, list[str]]):
        http_content_type_ie (Union[Unset, list[str]]):
        http_content_type_iew (Union[Unset, list[str]]):
        http_content_type_isw (Union[Unset, list[str]]):
        http_content_type_n (Union[Unset, list[str]]):
        http_content_type_nic (Union[Unset, list[str]]):
        http_content_type_nie (Union[Unset, list[str]]):
        http_content_type_niew (Union[Unset, list[str]]):
        http_content_type_nisw (Union[Unset, list[str]]):
        http_method (Union[Unset, list[str]]):
        http_method_empty (Union[Unset, bool]):
        http_method_ic (Union[Unset, list[str]]):
        http_method_ie (Union[Unset, list[str]]):
        http_method_iew (Union[Unset, list[str]]):
        http_method_isw (Union[Unset, list[str]]):
        http_method_n (Union[Unset, list[str]]):
        http_method_nic (Union[Unset, list[str]]):
        http_method_nie (Union[Unset, list[str]]):
        http_method_niew (Union[Unset, list[str]]):
        http_method_nisw (Union[Unset, list[str]]):
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
        payload_url (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        secret (Union[Unset, list[str]]):
        secret_empty (Union[Unset, bool]):
        secret_ic (Union[Unset, list[str]]):
        secret_ie (Union[Unset, list[str]]):
        secret_iew (Union[Unset, list[str]]):
        secret_isw (Union[Unset, list[str]]):
        secret_n (Union[Unset, list[str]]):
        secret_nic (Union[Unset, list[str]]):
        secret_nie (Union[Unset, list[str]]):
        secret_niew (Union[Unset, list[str]]):
        secret_nisw (Union[Unset, list[str]]):
        ssl_verification (Union[Unset, bool]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWebhookList]
    """

    kwargs = _get_kwargs(
        ca_file_path=ca_file_path,
        ca_file_path_empty=ca_file_path_empty,
        ca_file_path_ic=ca_file_path_ic,
        ca_file_path_ie=ca_file_path_ie,
        ca_file_path_iew=ca_file_path_iew,
        ca_file_path_isw=ca_file_path_isw,
        ca_file_path_n=ca_file_path_n,
        ca_file_path_nic=ca_file_path_nic,
        ca_file_path_nie=ca_file_path_nie,
        ca_file_path_niew=ca_file_path_niew,
        ca_file_path_nisw=ca_file_path_nisw,
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
        http_content_type=http_content_type,
        http_content_type_empty=http_content_type_empty,
        http_content_type_ic=http_content_type_ic,
        http_content_type_ie=http_content_type_ie,
        http_content_type_iew=http_content_type_iew,
        http_content_type_isw=http_content_type_isw,
        http_content_type_n=http_content_type_n,
        http_content_type_nic=http_content_type_nic,
        http_content_type_nie=http_content_type_nie,
        http_content_type_niew=http_content_type_niew,
        http_content_type_nisw=http_content_type_nisw,
        http_method=http_method,
        http_method_empty=http_method_empty,
        http_method_ic=http_method_ic,
        http_method_ie=http_method_ie,
        http_method_iew=http_method_iew,
        http_method_isw=http_method_isw,
        http_method_n=http_method_n,
        http_method_nic=http_method_nic,
        http_method_nie=http_method_nie,
        http_method_niew=http_method_niew,
        http_method_nisw=http_method_nisw,
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
        payload_url=payload_url,
        q=q,
        secret=secret,
        secret_empty=secret_empty,
        secret_ic=secret_ic,
        secret_ie=secret_ie,
        secret_iew=secret_iew,
        secret_isw=secret_isw,
        secret_n=secret_n,
        secret_nic=secret_nic,
        secret_nie=secret_nie,
        secret_niew=secret_niew,
        secret_nisw=secret_nisw,
        ssl_verification=ssl_verification,
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
    ca_file_path: Union[Unset, list[str]] = UNSET,
    ca_file_path_empty: Union[Unset, bool] = UNSET,
    ca_file_path_ic: Union[Unset, list[str]] = UNSET,
    ca_file_path_ie: Union[Unset, list[str]] = UNSET,
    ca_file_path_iew: Union[Unset, list[str]] = UNSET,
    ca_file_path_isw: Union[Unset, list[str]] = UNSET,
    ca_file_path_n: Union[Unset, list[str]] = UNSET,
    ca_file_path_nic: Union[Unset, list[str]] = UNSET,
    ca_file_path_nie: Union[Unset, list[str]] = UNSET,
    ca_file_path_niew: Union[Unset, list[str]] = UNSET,
    ca_file_path_nisw: Union[Unset, list[str]] = UNSET,
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
    http_content_type: Union[Unset, list[str]] = UNSET,
    http_content_type_empty: Union[Unset, bool] = UNSET,
    http_content_type_ic: Union[Unset, list[str]] = UNSET,
    http_content_type_ie: Union[Unset, list[str]] = UNSET,
    http_content_type_iew: Union[Unset, list[str]] = UNSET,
    http_content_type_isw: Union[Unset, list[str]] = UNSET,
    http_content_type_n: Union[Unset, list[str]] = UNSET,
    http_content_type_nic: Union[Unset, list[str]] = UNSET,
    http_content_type_nie: Union[Unset, list[str]] = UNSET,
    http_content_type_niew: Union[Unset, list[str]] = UNSET,
    http_content_type_nisw: Union[Unset, list[str]] = UNSET,
    http_method: Union[Unset, list[str]] = UNSET,
    http_method_empty: Union[Unset, bool] = UNSET,
    http_method_ic: Union[Unset, list[str]] = UNSET,
    http_method_ie: Union[Unset, list[str]] = UNSET,
    http_method_iew: Union[Unset, list[str]] = UNSET,
    http_method_isw: Union[Unset, list[str]] = UNSET,
    http_method_n: Union[Unset, list[str]] = UNSET,
    http_method_nic: Union[Unset, list[str]] = UNSET,
    http_method_nie: Union[Unset, list[str]] = UNSET,
    http_method_niew: Union[Unset, list[str]] = UNSET,
    http_method_nisw: Union[Unset, list[str]] = UNSET,
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
    payload_url: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    secret: Union[Unset, list[str]] = UNSET,
    secret_empty: Union[Unset, bool] = UNSET,
    secret_ic: Union[Unset, list[str]] = UNSET,
    secret_ie: Union[Unset, list[str]] = UNSET,
    secret_iew: Union[Unset, list[str]] = UNSET,
    secret_isw: Union[Unset, list[str]] = UNSET,
    secret_n: Union[Unset, list[str]] = UNSET,
    secret_nic: Union[Unset, list[str]] = UNSET,
    secret_nie: Union[Unset, list[str]] = UNSET,
    secret_niew: Union[Unset, list[str]] = UNSET,
    secret_nisw: Union[Unset, list[str]] = UNSET,
    ssl_verification: Union[Unset, bool] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedWebhookList]:
    """Get a list of webhook objects.

    Args:
        ca_file_path (Union[Unset, list[str]]):
        ca_file_path_empty (Union[Unset, bool]):
        ca_file_path_ic (Union[Unset, list[str]]):
        ca_file_path_ie (Union[Unset, list[str]]):
        ca_file_path_iew (Union[Unset, list[str]]):
        ca_file_path_isw (Union[Unset, list[str]]):
        ca_file_path_n (Union[Unset, list[str]]):
        ca_file_path_nic (Union[Unset, list[str]]):
        ca_file_path_nie (Union[Unset, list[str]]):
        ca_file_path_niew (Union[Unset, list[str]]):
        ca_file_path_nisw (Union[Unset, list[str]]):
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
        http_content_type (Union[Unset, list[str]]):
        http_content_type_empty (Union[Unset, bool]):
        http_content_type_ic (Union[Unset, list[str]]):
        http_content_type_ie (Union[Unset, list[str]]):
        http_content_type_iew (Union[Unset, list[str]]):
        http_content_type_isw (Union[Unset, list[str]]):
        http_content_type_n (Union[Unset, list[str]]):
        http_content_type_nic (Union[Unset, list[str]]):
        http_content_type_nie (Union[Unset, list[str]]):
        http_content_type_niew (Union[Unset, list[str]]):
        http_content_type_nisw (Union[Unset, list[str]]):
        http_method (Union[Unset, list[str]]):
        http_method_empty (Union[Unset, bool]):
        http_method_ic (Union[Unset, list[str]]):
        http_method_ie (Union[Unset, list[str]]):
        http_method_iew (Union[Unset, list[str]]):
        http_method_isw (Union[Unset, list[str]]):
        http_method_n (Union[Unset, list[str]]):
        http_method_nic (Union[Unset, list[str]]):
        http_method_nie (Union[Unset, list[str]]):
        http_method_niew (Union[Unset, list[str]]):
        http_method_nisw (Union[Unset, list[str]]):
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
        payload_url (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        secret (Union[Unset, list[str]]):
        secret_empty (Union[Unset, bool]):
        secret_ic (Union[Unset, list[str]]):
        secret_ie (Union[Unset, list[str]]):
        secret_iew (Union[Unset, list[str]]):
        secret_isw (Union[Unset, list[str]]):
        secret_n (Union[Unset, list[str]]):
        secret_nic (Union[Unset, list[str]]):
        secret_nie (Union[Unset, list[str]]):
        secret_niew (Union[Unset, list[str]]):
        secret_nisw (Union[Unset, list[str]]):
        ssl_verification (Union[Unset, bool]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWebhookList
    """

    return sync_detailed(
        client=client,
        ca_file_path=ca_file_path,
        ca_file_path_empty=ca_file_path_empty,
        ca_file_path_ic=ca_file_path_ic,
        ca_file_path_ie=ca_file_path_ie,
        ca_file_path_iew=ca_file_path_iew,
        ca_file_path_isw=ca_file_path_isw,
        ca_file_path_n=ca_file_path_n,
        ca_file_path_nic=ca_file_path_nic,
        ca_file_path_nie=ca_file_path_nie,
        ca_file_path_niew=ca_file_path_niew,
        ca_file_path_nisw=ca_file_path_nisw,
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
        http_content_type=http_content_type,
        http_content_type_empty=http_content_type_empty,
        http_content_type_ic=http_content_type_ic,
        http_content_type_ie=http_content_type_ie,
        http_content_type_iew=http_content_type_iew,
        http_content_type_isw=http_content_type_isw,
        http_content_type_n=http_content_type_n,
        http_content_type_nic=http_content_type_nic,
        http_content_type_nie=http_content_type_nie,
        http_content_type_niew=http_content_type_niew,
        http_content_type_nisw=http_content_type_nisw,
        http_method=http_method,
        http_method_empty=http_method_empty,
        http_method_ic=http_method_ic,
        http_method_ie=http_method_ie,
        http_method_iew=http_method_iew,
        http_method_isw=http_method_isw,
        http_method_n=http_method_n,
        http_method_nic=http_method_nic,
        http_method_nie=http_method_nie,
        http_method_niew=http_method_niew,
        http_method_nisw=http_method_nisw,
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
        payload_url=payload_url,
        q=q,
        secret=secret,
        secret_empty=secret_empty,
        secret_ic=secret_ic,
        secret_ie=secret_ie,
        secret_iew=secret_iew,
        secret_isw=secret_isw,
        secret_n=secret_n,
        secret_nic=secret_nic,
        secret_nie=secret_nie,
        secret_niew=secret_niew,
        secret_nisw=secret_nisw,
        ssl_verification=ssl_verification,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ca_file_path: Union[Unset, list[str]] = UNSET,
    ca_file_path_empty: Union[Unset, bool] = UNSET,
    ca_file_path_ic: Union[Unset, list[str]] = UNSET,
    ca_file_path_ie: Union[Unset, list[str]] = UNSET,
    ca_file_path_iew: Union[Unset, list[str]] = UNSET,
    ca_file_path_isw: Union[Unset, list[str]] = UNSET,
    ca_file_path_n: Union[Unset, list[str]] = UNSET,
    ca_file_path_nic: Union[Unset, list[str]] = UNSET,
    ca_file_path_nie: Union[Unset, list[str]] = UNSET,
    ca_file_path_niew: Union[Unset, list[str]] = UNSET,
    ca_file_path_nisw: Union[Unset, list[str]] = UNSET,
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
    http_content_type: Union[Unset, list[str]] = UNSET,
    http_content_type_empty: Union[Unset, bool] = UNSET,
    http_content_type_ic: Union[Unset, list[str]] = UNSET,
    http_content_type_ie: Union[Unset, list[str]] = UNSET,
    http_content_type_iew: Union[Unset, list[str]] = UNSET,
    http_content_type_isw: Union[Unset, list[str]] = UNSET,
    http_content_type_n: Union[Unset, list[str]] = UNSET,
    http_content_type_nic: Union[Unset, list[str]] = UNSET,
    http_content_type_nie: Union[Unset, list[str]] = UNSET,
    http_content_type_niew: Union[Unset, list[str]] = UNSET,
    http_content_type_nisw: Union[Unset, list[str]] = UNSET,
    http_method: Union[Unset, list[str]] = UNSET,
    http_method_empty: Union[Unset, bool] = UNSET,
    http_method_ic: Union[Unset, list[str]] = UNSET,
    http_method_ie: Union[Unset, list[str]] = UNSET,
    http_method_iew: Union[Unset, list[str]] = UNSET,
    http_method_isw: Union[Unset, list[str]] = UNSET,
    http_method_n: Union[Unset, list[str]] = UNSET,
    http_method_nic: Union[Unset, list[str]] = UNSET,
    http_method_nie: Union[Unset, list[str]] = UNSET,
    http_method_niew: Union[Unset, list[str]] = UNSET,
    http_method_nisw: Union[Unset, list[str]] = UNSET,
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
    payload_url: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    secret: Union[Unset, list[str]] = UNSET,
    secret_empty: Union[Unset, bool] = UNSET,
    secret_ic: Union[Unset, list[str]] = UNSET,
    secret_ie: Union[Unset, list[str]] = UNSET,
    secret_iew: Union[Unset, list[str]] = UNSET,
    secret_isw: Union[Unset, list[str]] = UNSET,
    secret_n: Union[Unset, list[str]] = UNSET,
    secret_nic: Union[Unset, list[str]] = UNSET,
    secret_nie: Union[Unset, list[str]] = UNSET,
    secret_niew: Union[Unset, list[str]] = UNSET,
    secret_nisw: Union[Unset, list[str]] = UNSET,
    ssl_verification: Union[Unset, bool] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedWebhookList]:
    """Get a list of webhook objects.

    Args:
        ca_file_path (Union[Unset, list[str]]):
        ca_file_path_empty (Union[Unset, bool]):
        ca_file_path_ic (Union[Unset, list[str]]):
        ca_file_path_ie (Union[Unset, list[str]]):
        ca_file_path_iew (Union[Unset, list[str]]):
        ca_file_path_isw (Union[Unset, list[str]]):
        ca_file_path_n (Union[Unset, list[str]]):
        ca_file_path_nic (Union[Unset, list[str]]):
        ca_file_path_nie (Union[Unset, list[str]]):
        ca_file_path_niew (Union[Unset, list[str]]):
        ca_file_path_nisw (Union[Unset, list[str]]):
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
        http_content_type (Union[Unset, list[str]]):
        http_content_type_empty (Union[Unset, bool]):
        http_content_type_ic (Union[Unset, list[str]]):
        http_content_type_ie (Union[Unset, list[str]]):
        http_content_type_iew (Union[Unset, list[str]]):
        http_content_type_isw (Union[Unset, list[str]]):
        http_content_type_n (Union[Unset, list[str]]):
        http_content_type_nic (Union[Unset, list[str]]):
        http_content_type_nie (Union[Unset, list[str]]):
        http_content_type_niew (Union[Unset, list[str]]):
        http_content_type_nisw (Union[Unset, list[str]]):
        http_method (Union[Unset, list[str]]):
        http_method_empty (Union[Unset, bool]):
        http_method_ic (Union[Unset, list[str]]):
        http_method_ie (Union[Unset, list[str]]):
        http_method_iew (Union[Unset, list[str]]):
        http_method_isw (Union[Unset, list[str]]):
        http_method_n (Union[Unset, list[str]]):
        http_method_nic (Union[Unset, list[str]]):
        http_method_nie (Union[Unset, list[str]]):
        http_method_niew (Union[Unset, list[str]]):
        http_method_nisw (Union[Unset, list[str]]):
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
        payload_url (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        secret (Union[Unset, list[str]]):
        secret_empty (Union[Unset, bool]):
        secret_ic (Union[Unset, list[str]]):
        secret_ie (Union[Unset, list[str]]):
        secret_iew (Union[Unset, list[str]]):
        secret_isw (Union[Unset, list[str]]):
        secret_n (Union[Unset, list[str]]):
        secret_nic (Union[Unset, list[str]]):
        secret_nie (Union[Unset, list[str]]):
        secret_niew (Union[Unset, list[str]]):
        secret_nisw (Union[Unset, list[str]]):
        ssl_verification (Union[Unset, bool]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWebhookList]
    """

    kwargs = _get_kwargs(
        ca_file_path=ca_file_path,
        ca_file_path_empty=ca_file_path_empty,
        ca_file_path_ic=ca_file_path_ic,
        ca_file_path_ie=ca_file_path_ie,
        ca_file_path_iew=ca_file_path_iew,
        ca_file_path_isw=ca_file_path_isw,
        ca_file_path_n=ca_file_path_n,
        ca_file_path_nic=ca_file_path_nic,
        ca_file_path_nie=ca_file_path_nie,
        ca_file_path_niew=ca_file_path_niew,
        ca_file_path_nisw=ca_file_path_nisw,
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
        http_content_type=http_content_type,
        http_content_type_empty=http_content_type_empty,
        http_content_type_ic=http_content_type_ic,
        http_content_type_ie=http_content_type_ie,
        http_content_type_iew=http_content_type_iew,
        http_content_type_isw=http_content_type_isw,
        http_content_type_n=http_content_type_n,
        http_content_type_nic=http_content_type_nic,
        http_content_type_nie=http_content_type_nie,
        http_content_type_niew=http_content_type_niew,
        http_content_type_nisw=http_content_type_nisw,
        http_method=http_method,
        http_method_empty=http_method_empty,
        http_method_ic=http_method_ic,
        http_method_ie=http_method_ie,
        http_method_iew=http_method_iew,
        http_method_isw=http_method_isw,
        http_method_n=http_method_n,
        http_method_nic=http_method_nic,
        http_method_nie=http_method_nie,
        http_method_niew=http_method_niew,
        http_method_nisw=http_method_nisw,
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
        payload_url=payload_url,
        q=q,
        secret=secret,
        secret_empty=secret_empty,
        secret_ic=secret_ic,
        secret_ie=secret_ie,
        secret_iew=secret_iew,
        secret_isw=secret_isw,
        secret_n=secret_n,
        secret_nic=secret_nic,
        secret_nie=secret_nie,
        secret_niew=secret_niew,
        secret_nisw=secret_nisw,
        ssl_verification=ssl_verification,
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
    ca_file_path: Union[Unset, list[str]] = UNSET,
    ca_file_path_empty: Union[Unset, bool] = UNSET,
    ca_file_path_ic: Union[Unset, list[str]] = UNSET,
    ca_file_path_ie: Union[Unset, list[str]] = UNSET,
    ca_file_path_iew: Union[Unset, list[str]] = UNSET,
    ca_file_path_isw: Union[Unset, list[str]] = UNSET,
    ca_file_path_n: Union[Unset, list[str]] = UNSET,
    ca_file_path_nic: Union[Unset, list[str]] = UNSET,
    ca_file_path_nie: Union[Unset, list[str]] = UNSET,
    ca_file_path_niew: Union[Unset, list[str]] = UNSET,
    ca_file_path_nisw: Union[Unset, list[str]] = UNSET,
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
    http_content_type: Union[Unset, list[str]] = UNSET,
    http_content_type_empty: Union[Unset, bool] = UNSET,
    http_content_type_ic: Union[Unset, list[str]] = UNSET,
    http_content_type_ie: Union[Unset, list[str]] = UNSET,
    http_content_type_iew: Union[Unset, list[str]] = UNSET,
    http_content_type_isw: Union[Unset, list[str]] = UNSET,
    http_content_type_n: Union[Unset, list[str]] = UNSET,
    http_content_type_nic: Union[Unset, list[str]] = UNSET,
    http_content_type_nie: Union[Unset, list[str]] = UNSET,
    http_content_type_niew: Union[Unset, list[str]] = UNSET,
    http_content_type_nisw: Union[Unset, list[str]] = UNSET,
    http_method: Union[Unset, list[str]] = UNSET,
    http_method_empty: Union[Unset, bool] = UNSET,
    http_method_ic: Union[Unset, list[str]] = UNSET,
    http_method_ie: Union[Unset, list[str]] = UNSET,
    http_method_iew: Union[Unset, list[str]] = UNSET,
    http_method_isw: Union[Unset, list[str]] = UNSET,
    http_method_n: Union[Unset, list[str]] = UNSET,
    http_method_nic: Union[Unset, list[str]] = UNSET,
    http_method_nie: Union[Unset, list[str]] = UNSET,
    http_method_niew: Union[Unset, list[str]] = UNSET,
    http_method_nisw: Union[Unset, list[str]] = UNSET,
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
    payload_url: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    secret: Union[Unset, list[str]] = UNSET,
    secret_empty: Union[Unset, bool] = UNSET,
    secret_ic: Union[Unset, list[str]] = UNSET,
    secret_ie: Union[Unset, list[str]] = UNSET,
    secret_iew: Union[Unset, list[str]] = UNSET,
    secret_isw: Union[Unset, list[str]] = UNSET,
    secret_n: Union[Unset, list[str]] = UNSET,
    secret_nic: Union[Unset, list[str]] = UNSET,
    secret_nie: Union[Unset, list[str]] = UNSET,
    secret_niew: Union[Unset, list[str]] = UNSET,
    secret_nisw: Union[Unset, list[str]] = UNSET,
    ssl_verification: Union[Unset, bool] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedWebhookList]:
    """Get a list of webhook objects.

    Args:
        ca_file_path (Union[Unset, list[str]]):
        ca_file_path_empty (Union[Unset, bool]):
        ca_file_path_ic (Union[Unset, list[str]]):
        ca_file_path_ie (Union[Unset, list[str]]):
        ca_file_path_iew (Union[Unset, list[str]]):
        ca_file_path_isw (Union[Unset, list[str]]):
        ca_file_path_n (Union[Unset, list[str]]):
        ca_file_path_nic (Union[Unset, list[str]]):
        ca_file_path_nie (Union[Unset, list[str]]):
        ca_file_path_niew (Union[Unset, list[str]]):
        ca_file_path_nisw (Union[Unset, list[str]]):
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
        http_content_type (Union[Unset, list[str]]):
        http_content_type_empty (Union[Unset, bool]):
        http_content_type_ic (Union[Unset, list[str]]):
        http_content_type_ie (Union[Unset, list[str]]):
        http_content_type_iew (Union[Unset, list[str]]):
        http_content_type_isw (Union[Unset, list[str]]):
        http_content_type_n (Union[Unset, list[str]]):
        http_content_type_nic (Union[Unset, list[str]]):
        http_content_type_nie (Union[Unset, list[str]]):
        http_content_type_niew (Union[Unset, list[str]]):
        http_content_type_nisw (Union[Unset, list[str]]):
        http_method (Union[Unset, list[str]]):
        http_method_empty (Union[Unset, bool]):
        http_method_ic (Union[Unset, list[str]]):
        http_method_ie (Union[Unset, list[str]]):
        http_method_iew (Union[Unset, list[str]]):
        http_method_isw (Union[Unset, list[str]]):
        http_method_n (Union[Unset, list[str]]):
        http_method_nic (Union[Unset, list[str]]):
        http_method_nie (Union[Unset, list[str]]):
        http_method_niew (Union[Unset, list[str]]):
        http_method_nisw (Union[Unset, list[str]]):
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
        payload_url (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        secret (Union[Unset, list[str]]):
        secret_empty (Union[Unset, bool]):
        secret_ic (Union[Unset, list[str]]):
        secret_ie (Union[Unset, list[str]]):
        secret_iew (Union[Unset, list[str]]):
        secret_isw (Union[Unset, list[str]]):
        secret_n (Union[Unset, list[str]]):
        secret_nic (Union[Unset, list[str]]):
        secret_nie (Union[Unset, list[str]]):
        secret_niew (Union[Unset, list[str]]):
        secret_nisw (Union[Unset, list[str]]):
        ssl_verification (Union[Unset, bool]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWebhookList
    """

    return (
        await asyncio_detailed(
            client=client,
            ca_file_path=ca_file_path,
            ca_file_path_empty=ca_file_path_empty,
            ca_file_path_ic=ca_file_path_ic,
            ca_file_path_ie=ca_file_path_ie,
            ca_file_path_iew=ca_file_path_iew,
            ca_file_path_isw=ca_file_path_isw,
            ca_file_path_n=ca_file_path_n,
            ca_file_path_nic=ca_file_path_nic,
            ca_file_path_nie=ca_file_path_nie,
            ca_file_path_niew=ca_file_path_niew,
            ca_file_path_nisw=ca_file_path_nisw,
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
            http_content_type=http_content_type,
            http_content_type_empty=http_content_type_empty,
            http_content_type_ic=http_content_type_ic,
            http_content_type_ie=http_content_type_ie,
            http_content_type_iew=http_content_type_iew,
            http_content_type_isw=http_content_type_isw,
            http_content_type_n=http_content_type_n,
            http_content_type_nic=http_content_type_nic,
            http_content_type_nie=http_content_type_nie,
            http_content_type_niew=http_content_type_niew,
            http_content_type_nisw=http_content_type_nisw,
            http_method=http_method,
            http_method_empty=http_method_empty,
            http_method_ic=http_method_ic,
            http_method_ie=http_method_ie,
            http_method_iew=http_method_iew,
            http_method_isw=http_method_isw,
            http_method_n=http_method_n,
            http_method_nic=http_method_nic,
            http_method_nie=http_method_nie,
            http_method_niew=http_method_niew,
            http_method_nisw=http_method_nisw,
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
            payload_url=payload_url,
            q=q,
            secret=secret,
            secret_empty=secret_empty,
            secret_ic=secret_ic,
            secret_ie=secret_ie,
            secret_iew=secret_iew,
            secret_isw=secret_isw,
            secret_n=secret_n,
            secret_nic=secret_nic,
            secret_nie=secret_nie,
            secret_niew=secret_niew,
            secret_nisw=secret_nisw,
            ssl_verification=ssl_verification,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
            updated_by_request=updated_by_request,
        )
    ).parsed
