import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_fhrp_group_list import PaginatedFHRPGroupList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    auth_key: Union[Unset, list[str]] = UNSET,
    auth_key_empty: Union[Unset, bool] = UNSET,
    auth_key_ic: Union[Unset, list[str]] = UNSET,
    auth_key_ie: Union[Unset, list[str]] = UNSET,
    auth_key_iew: Union[Unset, list[str]] = UNSET,
    auth_key_isw: Union[Unset, list[str]] = UNSET,
    auth_key_n: Union[Unset, list[str]] = UNSET,
    auth_key_nic: Union[Unset, list[str]] = UNSET,
    auth_key_nie: Union[Unset, list[str]] = UNSET,
    auth_key_niew: Union[Unset, list[str]] = UNSET,
    auth_key_nisw: Union[Unset, list[str]] = UNSET,
    auth_type: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_empty: Union[Unset, bool] = UNSET,
    auth_type_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_n: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    group_id: Union[Unset, list[int]] = UNSET,
    group_id_empty: Union[Unset, bool] = UNSET,
    group_id_gt: Union[Unset, list[int]] = UNSET,
    group_id_gte: Union[Unset, list[int]] = UNSET,
    group_id_lt: Union[Unset, list[int]] = UNSET,
    group_id_lte: Union[Unset, list[int]] = UNSET,
    group_id_n: Union[Unset, list[int]] = UNSET,
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
    protocol: Union[Unset, list[str]] = UNSET,
    protocol_empty: Union[Unset, bool] = UNSET,
    protocol_ic: Union[Unset, list[str]] = UNSET,
    protocol_ie: Union[Unset, list[str]] = UNSET,
    protocol_iew: Union[Unset, list[str]] = UNSET,
    protocol_isw: Union[Unset, list[str]] = UNSET,
    protocol_n: Union[Unset, list[str]] = UNSET,
    protocol_nic: Union[Unset, list[str]] = UNSET,
    protocol_nie: Union[Unset, list[str]] = UNSET,
    protocol_niew: Union[Unset, list[str]] = UNSET,
    protocol_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    related_ip: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_auth_key: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_key, Unset):
        json_auth_key = auth_key

    params["auth_key"] = json_auth_key

    params["auth_key__empty"] = auth_key_empty

    json_auth_key_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_key_ic, Unset):
        json_auth_key_ic = auth_key_ic

    params["auth_key__ic"] = json_auth_key_ic

    json_auth_key_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_key_ie, Unset):
        json_auth_key_ie = auth_key_ie

    params["auth_key__ie"] = json_auth_key_ie

    json_auth_key_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_key_iew, Unset):
        json_auth_key_iew = auth_key_iew

    params["auth_key__iew"] = json_auth_key_iew

    json_auth_key_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_key_isw, Unset):
        json_auth_key_isw = auth_key_isw

    params["auth_key__isw"] = json_auth_key_isw

    json_auth_key_n: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_key_n, Unset):
        json_auth_key_n = auth_key_n

    params["auth_key__n"] = json_auth_key_n

    json_auth_key_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_key_nic, Unset):
        json_auth_key_nic = auth_key_nic

    params["auth_key__nic"] = json_auth_key_nic

    json_auth_key_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_key_nie, Unset):
        json_auth_key_nie = auth_key_nie

    params["auth_key__nie"] = json_auth_key_nie

    json_auth_key_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_key_niew, Unset):
        json_auth_key_niew = auth_key_niew

    params["auth_key__niew"] = json_auth_key_niew

    json_auth_key_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_key_nisw, Unset):
        json_auth_key_nisw = auth_key_nisw

    params["auth_key__nisw"] = json_auth_key_nisw

    json_auth_type: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_type, Unset):
        json_auth_type = []
        for auth_type_item_data in auth_type:
            auth_type_item: Union[None, str]
            auth_type_item = auth_type_item_data
            json_auth_type.append(auth_type_item)

    params["auth_type"] = json_auth_type

    params["auth_type__empty"] = auth_type_empty

    json_auth_type_ic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_type_ic, Unset):
        json_auth_type_ic = []
        for auth_type_ic_item_data in auth_type_ic:
            auth_type_ic_item: Union[None, str]
            auth_type_ic_item = auth_type_ic_item_data
            json_auth_type_ic.append(auth_type_ic_item)

    params["auth_type__ic"] = json_auth_type_ic

    json_auth_type_ie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_type_ie, Unset):
        json_auth_type_ie = []
        for auth_type_ie_item_data in auth_type_ie:
            auth_type_ie_item: Union[None, str]
            auth_type_ie_item = auth_type_ie_item_data
            json_auth_type_ie.append(auth_type_ie_item)

    params["auth_type__ie"] = json_auth_type_ie

    json_auth_type_iew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_type_iew, Unset):
        json_auth_type_iew = []
        for auth_type_iew_item_data in auth_type_iew:
            auth_type_iew_item: Union[None, str]
            auth_type_iew_item = auth_type_iew_item_data
            json_auth_type_iew.append(auth_type_iew_item)

    params["auth_type__iew"] = json_auth_type_iew

    json_auth_type_isw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_type_isw, Unset):
        json_auth_type_isw = []
        for auth_type_isw_item_data in auth_type_isw:
            auth_type_isw_item: Union[None, str]
            auth_type_isw_item = auth_type_isw_item_data
            json_auth_type_isw.append(auth_type_isw_item)

    params["auth_type__isw"] = json_auth_type_isw

    json_auth_type_n: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_type_n, Unset):
        json_auth_type_n = []
        for auth_type_n_item_data in auth_type_n:
            auth_type_n_item: Union[None, str]
            auth_type_n_item = auth_type_n_item_data
            json_auth_type_n.append(auth_type_n_item)

    params["auth_type__n"] = json_auth_type_n

    json_auth_type_nic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_type_nic, Unset):
        json_auth_type_nic = []
        for auth_type_nic_item_data in auth_type_nic:
            auth_type_nic_item: Union[None, str]
            auth_type_nic_item = auth_type_nic_item_data
            json_auth_type_nic.append(auth_type_nic_item)

    params["auth_type__nic"] = json_auth_type_nic

    json_auth_type_nie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_type_nie, Unset):
        json_auth_type_nie = []
        for auth_type_nie_item_data in auth_type_nie:
            auth_type_nie_item: Union[None, str]
            auth_type_nie_item = auth_type_nie_item_data
            json_auth_type_nie.append(auth_type_nie_item)

    params["auth_type__nie"] = json_auth_type_nie

    json_auth_type_niew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_type_niew, Unset):
        json_auth_type_niew = []
        for auth_type_niew_item_data in auth_type_niew:
            auth_type_niew_item: Union[None, str]
            auth_type_niew_item = auth_type_niew_item_data
            json_auth_type_niew.append(auth_type_niew_item)

    params["auth_type__niew"] = json_auth_type_niew

    json_auth_type_nisw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_type_nisw, Unset):
        json_auth_type_nisw = []
        for auth_type_nisw_item_data in auth_type_nisw:
            auth_type_nisw_item: Union[None, str]
            auth_type_nisw_item = auth_type_nisw_item_data
            json_auth_type_nisw.append(auth_type_nisw_item)

    params["auth_type__nisw"] = json_auth_type_nisw

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

    json_group_id: Union[Unset, list[int]] = UNSET
    if not isinstance(group_id, Unset):
        json_group_id = group_id

    params["group_id"] = json_group_id

    params["group_id__empty"] = group_id_empty

    json_group_id_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(group_id_gt, Unset):
        json_group_id_gt = group_id_gt

    params["group_id__gt"] = json_group_id_gt

    json_group_id_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(group_id_gte, Unset):
        json_group_id_gte = group_id_gte

    params["group_id__gte"] = json_group_id_gte

    json_group_id_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(group_id_lt, Unset):
        json_group_id_lt = group_id_lt

    params["group_id__lt"] = json_group_id_lt

    json_group_id_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(group_id_lte, Unset):
        json_group_id_lte = group_id_lte

    params["group_id__lte"] = json_group_id_lte

    json_group_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(group_id_n, Unset):
        json_group_id_n = group_id_n

    params["group_id__n"] = json_group_id_n

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

    json_protocol: Union[Unset, list[str]] = UNSET
    if not isinstance(protocol, Unset):
        json_protocol = protocol

    params["protocol"] = json_protocol

    params["protocol__empty"] = protocol_empty

    json_protocol_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(protocol_ic, Unset):
        json_protocol_ic = protocol_ic

    params["protocol__ic"] = json_protocol_ic

    json_protocol_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(protocol_ie, Unset):
        json_protocol_ie = protocol_ie

    params["protocol__ie"] = json_protocol_ie

    json_protocol_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(protocol_iew, Unset):
        json_protocol_iew = protocol_iew

    params["protocol__iew"] = json_protocol_iew

    json_protocol_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(protocol_isw, Unset):
        json_protocol_isw = protocol_isw

    params["protocol__isw"] = json_protocol_isw

    json_protocol_n: Union[Unset, list[str]] = UNSET
    if not isinstance(protocol_n, Unset):
        json_protocol_n = protocol_n

    params["protocol__n"] = json_protocol_n

    json_protocol_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(protocol_nic, Unset):
        json_protocol_nic = protocol_nic

    params["protocol__nic"] = json_protocol_nic

    json_protocol_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(protocol_nie, Unset):
        json_protocol_nie = protocol_nie

    params["protocol__nie"] = json_protocol_nie

    json_protocol_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(protocol_niew, Unset):
        json_protocol_niew = protocol_niew

    params["protocol__niew"] = json_protocol_niew

    json_protocol_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(protocol_nisw, Unset):
        json_protocol_nisw = protocol_nisw

    params["protocol__nisw"] = json_protocol_nisw

    params["q"] = q

    json_related_ip: Union[Unset, list[str]] = UNSET
    if not isinstance(related_ip, Unset):
        json_related_ip = related_ip

    params["related_ip"] = json_related_ip

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
        "url": "/api/ipam/fhrp-groups/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedFHRPGroupList]:
    if response.status_code == 200:
        response_200 = PaginatedFHRPGroupList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedFHRPGroupList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    auth_key: Union[Unset, list[str]] = UNSET,
    auth_key_empty: Union[Unset, bool] = UNSET,
    auth_key_ic: Union[Unset, list[str]] = UNSET,
    auth_key_ie: Union[Unset, list[str]] = UNSET,
    auth_key_iew: Union[Unset, list[str]] = UNSET,
    auth_key_isw: Union[Unset, list[str]] = UNSET,
    auth_key_n: Union[Unset, list[str]] = UNSET,
    auth_key_nic: Union[Unset, list[str]] = UNSET,
    auth_key_nie: Union[Unset, list[str]] = UNSET,
    auth_key_niew: Union[Unset, list[str]] = UNSET,
    auth_key_nisw: Union[Unset, list[str]] = UNSET,
    auth_type: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_empty: Union[Unset, bool] = UNSET,
    auth_type_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_n: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    group_id: Union[Unset, list[int]] = UNSET,
    group_id_empty: Union[Unset, bool] = UNSET,
    group_id_gt: Union[Unset, list[int]] = UNSET,
    group_id_gte: Union[Unset, list[int]] = UNSET,
    group_id_lt: Union[Unset, list[int]] = UNSET,
    group_id_lte: Union[Unset, list[int]] = UNSET,
    group_id_n: Union[Unset, list[int]] = UNSET,
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
    protocol: Union[Unset, list[str]] = UNSET,
    protocol_empty: Union[Unset, bool] = UNSET,
    protocol_ic: Union[Unset, list[str]] = UNSET,
    protocol_ie: Union[Unset, list[str]] = UNSET,
    protocol_iew: Union[Unset, list[str]] = UNSET,
    protocol_isw: Union[Unset, list[str]] = UNSET,
    protocol_n: Union[Unset, list[str]] = UNSET,
    protocol_nic: Union[Unset, list[str]] = UNSET,
    protocol_nie: Union[Unset, list[str]] = UNSET,
    protocol_niew: Union[Unset, list[str]] = UNSET,
    protocol_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    related_ip: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedFHRPGroupList]:
    """Get a list of FHRP group objects.

    Args:
        auth_key (Union[Unset, list[str]]):
        auth_key_empty (Union[Unset, bool]):
        auth_key_ic (Union[Unset, list[str]]):
        auth_key_ie (Union[Unset, list[str]]):
        auth_key_iew (Union[Unset, list[str]]):
        auth_key_isw (Union[Unset, list[str]]):
        auth_key_n (Union[Unset, list[str]]):
        auth_key_nic (Union[Unset, list[str]]):
        auth_key_nie (Union[Unset, list[str]]):
        auth_key_niew (Union[Unset, list[str]]):
        auth_key_nisw (Union[Unset, list[str]]):
        auth_type (Union[Unset, list[Union[None, str]]]):
        auth_type_empty (Union[Unset, bool]):
        auth_type_ic (Union[Unset, list[Union[None, str]]]):
        auth_type_ie (Union[Unset, list[Union[None, str]]]):
        auth_type_iew (Union[Unset, list[Union[None, str]]]):
        auth_type_isw (Union[Unset, list[Union[None, str]]]):
        auth_type_n (Union[Unset, list[Union[None, str]]]):
        auth_type_nic (Union[Unset, list[Union[None, str]]]):
        auth_type_nie (Union[Unset, list[Union[None, str]]]):
        auth_type_niew (Union[Unset, list[Union[None, str]]]):
        auth_type_nisw (Union[Unset, list[Union[None, str]]]):
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
        group_id (Union[Unset, list[int]]):
        group_id_empty (Union[Unset, bool]):
        group_id_gt (Union[Unset, list[int]]):
        group_id_gte (Union[Unset, list[int]]):
        group_id_lt (Union[Unset, list[int]]):
        group_id_lte (Union[Unset, list[int]]):
        group_id_n (Union[Unset, list[int]]):
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
        protocol (Union[Unset, list[str]]):
        protocol_empty (Union[Unset, bool]):
        protocol_ic (Union[Unset, list[str]]):
        protocol_ie (Union[Unset, list[str]]):
        protocol_iew (Union[Unset, list[str]]):
        protocol_isw (Union[Unset, list[str]]):
        protocol_n (Union[Unset, list[str]]):
        protocol_nic (Union[Unset, list[str]]):
        protocol_nie (Union[Unset, list[str]]):
        protocol_niew (Union[Unset, list[str]]):
        protocol_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        related_ip (Union[Unset, list[str]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedFHRPGroupList]
    """

    kwargs = _get_kwargs(
        auth_key=auth_key,
        auth_key_empty=auth_key_empty,
        auth_key_ic=auth_key_ic,
        auth_key_ie=auth_key_ie,
        auth_key_iew=auth_key_iew,
        auth_key_isw=auth_key_isw,
        auth_key_n=auth_key_n,
        auth_key_nic=auth_key_nic,
        auth_key_nie=auth_key_nie,
        auth_key_niew=auth_key_niew,
        auth_key_nisw=auth_key_nisw,
        auth_type=auth_type,
        auth_type_empty=auth_type_empty,
        auth_type_ic=auth_type_ic,
        auth_type_ie=auth_type_ie,
        auth_type_iew=auth_type_iew,
        auth_type_isw=auth_type_isw,
        auth_type_n=auth_type_n,
        auth_type_nic=auth_type_nic,
        auth_type_nie=auth_type_nie,
        auth_type_niew=auth_type_niew,
        auth_type_nisw=auth_type_nisw,
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
        group_id=group_id,
        group_id_empty=group_id_empty,
        group_id_gt=group_id_gt,
        group_id_gte=group_id_gte,
        group_id_lt=group_id_lt,
        group_id_lte=group_id_lte,
        group_id_n=group_id_n,
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
        protocol=protocol,
        protocol_empty=protocol_empty,
        protocol_ic=protocol_ic,
        protocol_ie=protocol_ie,
        protocol_iew=protocol_iew,
        protocol_isw=protocol_isw,
        protocol_n=protocol_n,
        protocol_nic=protocol_nic,
        protocol_nie=protocol_nie,
        protocol_niew=protocol_niew,
        protocol_nisw=protocol_nisw,
        q=q,
        related_ip=related_ip,
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
    auth_key: Union[Unset, list[str]] = UNSET,
    auth_key_empty: Union[Unset, bool] = UNSET,
    auth_key_ic: Union[Unset, list[str]] = UNSET,
    auth_key_ie: Union[Unset, list[str]] = UNSET,
    auth_key_iew: Union[Unset, list[str]] = UNSET,
    auth_key_isw: Union[Unset, list[str]] = UNSET,
    auth_key_n: Union[Unset, list[str]] = UNSET,
    auth_key_nic: Union[Unset, list[str]] = UNSET,
    auth_key_nie: Union[Unset, list[str]] = UNSET,
    auth_key_niew: Union[Unset, list[str]] = UNSET,
    auth_key_nisw: Union[Unset, list[str]] = UNSET,
    auth_type: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_empty: Union[Unset, bool] = UNSET,
    auth_type_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_n: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    group_id: Union[Unset, list[int]] = UNSET,
    group_id_empty: Union[Unset, bool] = UNSET,
    group_id_gt: Union[Unset, list[int]] = UNSET,
    group_id_gte: Union[Unset, list[int]] = UNSET,
    group_id_lt: Union[Unset, list[int]] = UNSET,
    group_id_lte: Union[Unset, list[int]] = UNSET,
    group_id_n: Union[Unset, list[int]] = UNSET,
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
    protocol: Union[Unset, list[str]] = UNSET,
    protocol_empty: Union[Unset, bool] = UNSET,
    protocol_ic: Union[Unset, list[str]] = UNSET,
    protocol_ie: Union[Unset, list[str]] = UNSET,
    protocol_iew: Union[Unset, list[str]] = UNSET,
    protocol_isw: Union[Unset, list[str]] = UNSET,
    protocol_n: Union[Unset, list[str]] = UNSET,
    protocol_nic: Union[Unset, list[str]] = UNSET,
    protocol_nie: Union[Unset, list[str]] = UNSET,
    protocol_niew: Union[Unset, list[str]] = UNSET,
    protocol_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    related_ip: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedFHRPGroupList]:
    """Get a list of FHRP group objects.

    Args:
        auth_key (Union[Unset, list[str]]):
        auth_key_empty (Union[Unset, bool]):
        auth_key_ic (Union[Unset, list[str]]):
        auth_key_ie (Union[Unset, list[str]]):
        auth_key_iew (Union[Unset, list[str]]):
        auth_key_isw (Union[Unset, list[str]]):
        auth_key_n (Union[Unset, list[str]]):
        auth_key_nic (Union[Unset, list[str]]):
        auth_key_nie (Union[Unset, list[str]]):
        auth_key_niew (Union[Unset, list[str]]):
        auth_key_nisw (Union[Unset, list[str]]):
        auth_type (Union[Unset, list[Union[None, str]]]):
        auth_type_empty (Union[Unset, bool]):
        auth_type_ic (Union[Unset, list[Union[None, str]]]):
        auth_type_ie (Union[Unset, list[Union[None, str]]]):
        auth_type_iew (Union[Unset, list[Union[None, str]]]):
        auth_type_isw (Union[Unset, list[Union[None, str]]]):
        auth_type_n (Union[Unset, list[Union[None, str]]]):
        auth_type_nic (Union[Unset, list[Union[None, str]]]):
        auth_type_nie (Union[Unset, list[Union[None, str]]]):
        auth_type_niew (Union[Unset, list[Union[None, str]]]):
        auth_type_nisw (Union[Unset, list[Union[None, str]]]):
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
        group_id (Union[Unset, list[int]]):
        group_id_empty (Union[Unset, bool]):
        group_id_gt (Union[Unset, list[int]]):
        group_id_gte (Union[Unset, list[int]]):
        group_id_lt (Union[Unset, list[int]]):
        group_id_lte (Union[Unset, list[int]]):
        group_id_n (Union[Unset, list[int]]):
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
        protocol (Union[Unset, list[str]]):
        protocol_empty (Union[Unset, bool]):
        protocol_ic (Union[Unset, list[str]]):
        protocol_ie (Union[Unset, list[str]]):
        protocol_iew (Union[Unset, list[str]]):
        protocol_isw (Union[Unset, list[str]]):
        protocol_n (Union[Unset, list[str]]):
        protocol_nic (Union[Unset, list[str]]):
        protocol_nie (Union[Unset, list[str]]):
        protocol_niew (Union[Unset, list[str]]):
        protocol_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        related_ip (Union[Unset, list[str]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedFHRPGroupList
    """

    return sync_detailed(
        client=client,
        auth_key=auth_key,
        auth_key_empty=auth_key_empty,
        auth_key_ic=auth_key_ic,
        auth_key_ie=auth_key_ie,
        auth_key_iew=auth_key_iew,
        auth_key_isw=auth_key_isw,
        auth_key_n=auth_key_n,
        auth_key_nic=auth_key_nic,
        auth_key_nie=auth_key_nie,
        auth_key_niew=auth_key_niew,
        auth_key_nisw=auth_key_nisw,
        auth_type=auth_type,
        auth_type_empty=auth_type_empty,
        auth_type_ic=auth_type_ic,
        auth_type_ie=auth_type_ie,
        auth_type_iew=auth_type_iew,
        auth_type_isw=auth_type_isw,
        auth_type_n=auth_type_n,
        auth_type_nic=auth_type_nic,
        auth_type_nie=auth_type_nie,
        auth_type_niew=auth_type_niew,
        auth_type_nisw=auth_type_nisw,
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
        group_id=group_id,
        group_id_empty=group_id_empty,
        group_id_gt=group_id_gt,
        group_id_gte=group_id_gte,
        group_id_lt=group_id_lt,
        group_id_lte=group_id_lte,
        group_id_n=group_id_n,
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
        protocol=protocol,
        protocol_empty=protocol_empty,
        protocol_ic=protocol_ic,
        protocol_ie=protocol_ie,
        protocol_iew=protocol_iew,
        protocol_isw=protocol_isw,
        protocol_n=protocol_n,
        protocol_nic=protocol_nic,
        protocol_nie=protocol_nie,
        protocol_niew=protocol_niew,
        protocol_nisw=protocol_nisw,
        q=q,
        related_ip=related_ip,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    auth_key: Union[Unset, list[str]] = UNSET,
    auth_key_empty: Union[Unset, bool] = UNSET,
    auth_key_ic: Union[Unset, list[str]] = UNSET,
    auth_key_ie: Union[Unset, list[str]] = UNSET,
    auth_key_iew: Union[Unset, list[str]] = UNSET,
    auth_key_isw: Union[Unset, list[str]] = UNSET,
    auth_key_n: Union[Unset, list[str]] = UNSET,
    auth_key_nic: Union[Unset, list[str]] = UNSET,
    auth_key_nie: Union[Unset, list[str]] = UNSET,
    auth_key_niew: Union[Unset, list[str]] = UNSET,
    auth_key_nisw: Union[Unset, list[str]] = UNSET,
    auth_type: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_empty: Union[Unset, bool] = UNSET,
    auth_type_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_n: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    group_id: Union[Unset, list[int]] = UNSET,
    group_id_empty: Union[Unset, bool] = UNSET,
    group_id_gt: Union[Unset, list[int]] = UNSET,
    group_id_gte: Union[Unset, list[int]] = UNSET,
    group_id_lt: Union[Unset, list[int]] = UNSET,
    group_id_lte: Union[Unset, list[int]] = UNSET,
    group_id_n: Union[Unset, list[int]] = UNSET,
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
    protocol: Union[Unset, list[str]] = UNSET,
    protocol_empty: Union[Unset, bool] = UNSET,
    protocol_ic: Union[Unset, list[str]] = UNSET,
    protocol_ie: Union[Unset, list[str]] = UNSET,
    protocol_iew: Union[Unset, list[str]] = UNSET,
    protocol_isw: Union[Unset, list[str]] = UNSET,
    protocol_n: Union[Unset, list[str]] = UNSET,
    protocol_nic: Union[Unset, list[str]] = UNSET,
    protocol_nie: Union[Unset, list[str]] = UNSET,
    protocol_niew: Union[Unset, list[str]] = UNSET,
    protocol_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    related_ip: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedFHRPGroupList]:
    """Get a list of FHRP group objects.

    Args:
        auth_key (Union[Unset, list[str]]):
        auth_key_empty (Union[Unset, bool]):
        auth_key_ic (Union[Unset, list[str]]):
        auth_key_ie (Union[Unset, list[str]]):
        auth_key_iew (Union[Unset, list[str]]):
        auth_key_isw (Union[Unset, list[str]]):
        auth_key_n (Union[Unset, list[str]]):
        auth_key_nic (Union[Unset, list[str]]):
        auth_key_nie (Union[Unset, list[str]]):
        auth_key_niew (Union[Unset, list[str]]):
        auth_key_nisw (Union[Unset, list[str]]):
        auth_type (Union[Unset, list[Union[None, str]]]):
        auth_type_empty (Union[Unset, bool]):
        auth_type_ic (Union[Unset, list[Union[None, str]]]):
        auth_type_ie (Union[Unset, list[Union[None, str]]]):
        auth_type_iew (Union[Unset, list[Union[None, str]]]):
        auth_type_isw (Union[Unset, list[Union[None, str]]]):
        auth_type_n (Union[Unset, list[Union[None, str]]]):
        auth_type_nic (Union[Unset, list[Union[None, str]]]):
        auth_type_nie (Union[Unset, list[Union[None, str]]]):
        auth_type_niew (Union[Unset, list[Union[None, str]]]):
        auth_type_nisw (Union[Unset, list[Union[None, str]]]):
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
        group_id (Union[Unset, list[int]]):
        group_id_empty (Union[Unset, bool]):
        group_id_gt (Union[Unset, list[int]]):
        group_id_gte (Union[Unset, list[int]]):
        group_id_lt (Union[Unset, list[int]]):
        group_id_lte (Union[Unset, list[int]]):
        group_id_n (Union[Unset, list[int]]):
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
        protocol (Union[Unset, list[str]]):
        protocol_empty (Union[Unset, bool]):
        protocol_ic (Union[Unset, list[str]]):
        protocol_ie (Union[Unset, list[str]]):
        protocol_iew (Union[Unset, list[str]]):
        protocol_isw (Union[Unset, list[str]]):
        protocol_n (Union[Unset, list[str]]):
        protocol_nic (Union[Unset, list[str]]):
        protocol_nie (Union[Unset, list[str]]):
        protocol_niew (Union[Unset, list[str]]):
        protocol_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        related_ip (Union[Unset, list[str]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedFHRPGroupList]
    """

    kwargs = _get_kwargs(
        auth_key=auth_key,
        auth_key_empty=auth_key_empty,
        auth_key_ic=auth_key_ic,
        auth_key_ie=auth_key_ie,
        auth_key_iew=auth_key_iew,
        auth_key_isw=auth_key_isw,
        auth_key_n=auth_key_n,
        auth_key_nic=auth_key_nic,
        auth_key_nie=auth_key_nie,
        auth_key_niew=auth_key_niew,
        auth_key_nisw=auth_key_nisw,
        auth_type=auth_type,
        auth_type_empty=auth_type_empty,
        auth_type_ic=auth_type_ic,
        auth_type_ie=auth_type_ie,
        auth_type_iew=auth_type_iew,
        auth_type_isw=auth_type_isw,
        auth_type_n=auth_type_n,
        auth_type_nic=auth_type_nic,
        auth_type_nie=auth_type_nie,
        auth_type_niew=auth_type_niew,
        auth_type_nisw=auth_type_nisw,
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
        group_id=group_id,
        group_id_empty=group_id_empty,
        group_id_gt=group_id_gt,
        group_id_gte=group_id_gte,
        group_id_lt=group_id_lt,
        group_id_lte=group_id_lte,
        group_id_n=group_id_n,
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
        protocol=protocol,
        protocol_empty=protocol_empty,
        protocol_ic=protocol_ic,
        protocol_ie=protocol_ie,
        protocol_iew=protocol_iew,
        protocol_isw=protocol_isw,
        protocol_n=protocol_n,
        protocol_nic=protocol_nic,
        protocol_nie=protocol_nie,
        protocol_niew=protocol_niew,
        protocol_nisw=protocol_nisw,
        q=q,
        related_ip=related_ip,
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
    auth_key: Union[Unset, list[str]] = UNSET,
    auth_key_empty: Union[Unset, bool] = UNSET,
    auth_key_ic: Union[Unset, list[str]] = UNSET,
    auth_key_ie: Union[Unset, list[str]] = UNSET,
    auth_key_iew: Union[Unset, list[str]] = UNSET,
    auth_key_isw: Union[Unset, list[str]] = UNSET,
    auth_key_n: Union[Unset, list[str]] = UNSET,
    auth_key_nic: Union[Unset, list[str]] = UNSET,
    auth_key_nie: Union[Unset, list[str]] = UNSET,
    auth_key_niew: Union[Unset, list[str]] = UNSET,
    auth_key_nisw: Union[Unset, list[str]] = UNSET,
    auth_type: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_empty: Union[Unset, bool] = UNSET,
    auth_type_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_n: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_type_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    group_id: Union[Unset, list[int]] = UNSET,
    group_id_empty: Union[Unset, bool] = UNSET,
    group_id_gt: Union[Unset, list[int]] = UNSET,
    group_id_gte: Union[Unset, list[int]] = UNSET,
    group_id_lt: Union[Unset, list[int]] = UNSET,
    group_id_lte: Union[Unset, list[int]] = UNSET,
    group_id_n: Union[Unset, list[int]] = UNSET,
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
    protocol: Union[Unset, list[str]] = UNSET,
    protocol_empty: Union[Unset, bool] = UNSET,
    protocol_ic: Union[Unset, list[str]] = UNSET,
    protocol_ie: Union[Unset, list[str]] = UNSET,
    protocol_iew: Union[Unset, list[str]] = UNSET,
    protocol_isw: Union[Unset, list[str]] = UNSET,
    protocol_n: Union[Unset, list[str]] = UNSET,
    protocol_nic: Union[Unset, list[str]] = UNSET,
    protocol_nie: Union[Unset, list[str]] = UNSET,
    protocol_niew: Union[Unset, list[str]] = UNSET,
    protocol_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    related_ip: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedFHRPGroupList]:
    """Get a list of FHRP group objects.

    Args:
        auth_key (Union[Unset, list[str]]):
        auth_key_empty (Union[Unset, bool]):
        auth_key_ic (Union[Unset, list[str]]):
        auth_key_ie (Union[Unset, list[str]]):
        auth_key_iew (Union[Unset, list[str]]):
        auth_key_isw (Union[Unset, list[str]]):
        auth_key_n (Union[Unset, list[str]]):
        auth_key_nic (Union[Unset, list[str]]):
        auth_key_nie (Union[Unset, list[str]]):
        auth_key_niew (Union[Unset, list[str]]):
        auth_key_nisw (Union[Unset, list[str]]):
        auth_type (Union[Unset, list[Union[None, str]]]):
        auth_type_empty (Union[Unset, bool]):
        auth_type_ic (Union[Unset, list[Union[None, str]]]):
        auth_type_ie (Union[Unset, list[Union[None, str]]]):
        auth_type_iew (Union[Unset, list[Union[None, str]]]):
        auth_type_isw (Union[Unset, list[Union[None, str]]]):
        auth_type_n (Union[Unset, list[Union[None, str]]]):
        auth_type_nic (Union[Unset, list[Union[None, str]]]):
        auth_type_nie (Union[Unset, list[Union[None, str]]]):
        auth_type_niew (Union[Unset, list[Union[None, str]]]):
        auth_type_nisw (Union[Unset, list[Union[None, str]]]):
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
        group_id (Union[Unset, list[int]]):
        group_id_empty (Union[Unset, bool]):
        group_id_gt (Union[Unset, list[int]]):
        group_id_gte (Union[Unset, list[int]]):
        group_id_lt (Union[Unset, list[int]]):
        group_id_lte (Union[Unset, list[int]]):
        group_id_n (Union[Unset, list[int]]):
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
        protocol (Union[Unset, list[str]]):
        protocol_empty (Union[Unset, bool]):
        protocol_ic (Union[Unset, list[str]]):
        protocol_ie (Union[Unset, list[str]]):
        protocol_iew (Union[Unset, list[str]]):
        protocol_isw (Union[Unset, list[str]]):
        protocol_n (Union[Unset, list[str]]):
        protocol_nic (Union[Unset, list[str]]):
        protocol_nie (Union[Unset, list[str]]):
        protocol_niew (Union[Unset, list[str]]):
        protocol_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        related_ip (Union[Unset, list[str]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedFHRPGroupList
    """

    return (
        await asyncio_detailed(
            client=client,
            auth_key=auth_key,
            auth_key_empty=auth_key_empty,
            auth_key_ic=auth_key_ic,
            auth_key_ie=auth_key_ie,
            auth_key_iew=auth_key_iew,
            auth_key_isw=auth_key_isw,
            auth_key_n=auth_key_n,
            auth_key_nic=auth_key_nic,
            auth_key_nie=auth_key_nie,
            auth_key_niew=auth_key_niew,
            auth_key_nisw=auth_key_nisw,
            auth_type=auth_type,
            auth_type_empty=auth_type_empty,
            auth_type_ic=auth_type_ic,
            auth_type_ie=auth_type_ie,
            auth_type_iew=auth_type_iew,
            auth_type_isw=auth_type_isw,
            auth_type_n=auth_type_n,
            auth_type_nic=auth_type_nic,
            auth_type_nie=auth_type_nie,
            auth_type_niew=auth_type_niew,
            auth_type_nisw=auth_type_nisw,
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
            group_id=group_id,
            group_id_empty=group_id_empty,
            group_id_gt=group_id_gt,
            group_id_gte=group_id_gte,
            group_id_lt=group_id_lt,
            group_id_lte=group_id_lte,
            group_id_n=group_id_n,
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
            protocol=protocol,
            protocol_empty=protocol_empty,
            protocol_ic=protocol_ic,
            protocol_ie=protocol_ie,
            protocol_iew=protocol_iew,
            protocol_isw=protocol_isw,
            protocol_n=protocol_n,
            protocol_nic=protocol_nic,
            protocol_nie=protocol_nie,
            protocol_niew=protocol_niew,
            protocol_nisw=protocol_nisw,
            q=q,
            related_ip=related_ip,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
            updated_by_request=updated_by_request,
        )
    ).parsed
