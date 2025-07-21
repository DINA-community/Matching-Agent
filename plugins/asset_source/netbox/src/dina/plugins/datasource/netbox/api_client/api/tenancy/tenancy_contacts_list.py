import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_contact_list import PaginatedContactList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    address: Union[Unset, list[str]] = UNSET,
    address_empty: Union[Unset, bool] = UNSET,
    address_ic: Union[Unset, list[str]] = UNSET,
    address_ie: Union[Unset, list[str]] = UNSET,
    address_iew: Union[Unset, list[str]] = UNSET,
    address_isw: Union[Unset, list[str]] = UNSET,
    address_n: Union[Unset, list[str]] = UNSET,
    address_nic: Union[Unset, list[str]] = UNSET,
    address_nie: Union[Unset, list[str]] = UNSET,
    address_niew: Union[Unset, list[str]] = UNSET,
    address_nisw: Union[Unset, list[str]] = UNSET,
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
    email: Union[Unset, list[str]] = UNSET,
    email_empty: Union[Unset, bool] = UNSET,
    email_ic: Union[Unset, list[str]] = UNSET,
    email_ie: Union[Unset, list[str]] = UNSET,
    email_iew: Union[Unset, list[str]] = UNSET,
    email_isw: Union[Unset, list[str]] = UNSET,
    email_n: Union[Unset, list[str]] = UNSET,
    email_nic: Union[Unset, list[str]] = UNSET,
    email_nie: Union[Unset, list[str]] = UNSET,
    email_niew: Union[Unset, list[str]] = UNSET,
    email_nisw: Union[Unset, list[str]] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[str]] = UNSET,
    group_id_n: Union[Unset, list[str]] = UNSET,
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
    link: Union[Unset, list[str]] = UNSET,
    link_empty: Union[Unset, bool] = UNSET,
    link_ic: Union[Unset, list[str]] = UNSET,
    link_ie: Union[Unset, list[str]] = UNSET,
    link_iew: Union[Unset, list[str]] = UNSET,
    link_isw: Union[Unset, list[str]] = UNSET,
    link_n: Union[Unset, list[str]] = UNSET,
    link_nic: Union[Unset, list[str]] = UNSET,
    link_nie: Union[Unset, list[str]] = UNSET,
    link_niew: Union[Unset, list[str]] = UNSET,
    link_nisw: Union[Unset, list[str]] = UNSET,
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
    phone: Union[Unset, list[str]] = UNSET,
    phone_empty: Union[Unset, bool] = UNSET,
    phone_ic: Union[Unset, list[str]] = UNSET,
    phone_ie: Union[Unset, list[str]] = UNSET,
    phone_iew: Union[Unset, list[str]] = UNSET,
    phone_isw: Union[Unset, list[str]] = UNSET,
    phone_n: Union[Unset, list[str]] = UNSET,
    phone_nic: Union[Unset, list[str]] = UNSET,
    phone_nie: Union[Unset, list[str]] = UNSET,
    phone_niew: Union[Unset, list[str]] = UNSET,
    phone_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    title: Union[Unset, list[str]] = UNSET,
    title_empty: Union[Unset, bool] = UNSET,
    title_ic: Union[Unset, list[str]] = UNSET,
    title_ie: Union[Unset, list[str]] = UNSET,
    title_iew: Union[Unset, list[str]] = UNSET,
    title_isw: Union[Unset, list[str]] = UNSET,
    title_n: Union[Unset, list[str]] = UNSET,
    title_nic: Union[Unset, list[str]] = UNSET,
    title_nie: Union[Unset, list[str]] = UNSET,
    title_niew: Union[Unset, list[str]] = UNSET,
    title_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_address: Union[Unset, list[str]] = UNSET
    if not isinstance(address, Unset):
        json_address = address

    params["address"] = json_address

    params["address__empty"] = address_empty

    json_address_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(address_ic, Unset):
        json_address_ic = address_ic

    params["address__ic"] = json_address_ic

    json_address_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(address_ie, Unset):
        json_address_ie = address_ie

    params["address__ie"] = json_address_ie

    json_address_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(address_iew, Unset):
        json_address_iew = address_iew

    params["address__iew"] = json_address_iew

    json_address_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(address_isw, Unset):
        json_address_isw = address_isw

    params["address__isw"] = json_address_isw

    json_address_n: Union[Unset, list[str]] = UNSET
    if not isinstance(address_n, Unset):
        json_address_n = address_n

    params["address__n"] = json_address_n

    json_address_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(address_nic, Unset):
        json_address_nic = address_nic

    params["address__nic"] = json_address_nic

    json_address_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(address_nie, Unset):
        json_address_nie = address_nie

    params["address__nie"] = json_address_nie

    json_address_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(address_niew, Unset):
        json_address_niew = address_niew

    params["address__niew"] = json_address_niew

    json_address_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(address_nisw, Unset):
        json_address_nisw = address_nisw

    params["address__nisw"] = json_address_nisw

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

    json_email: Union[Unset, list[str]] = UNSET
    if not isinstance(email, Unset):
        json_email = email

    params["email"] = json_email

    params["email__empty"] = email_empty

    json_email_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(email_ic, Unset):
        json_email_ic = email_ic

    params["email__ic"] = json_email_ic

    json_email_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(email_ie, Unset):
        json_email_ie = email_ie

    params["email__ie"] = json_email_ie

    json_email_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(email_iew, Unset):
        json_email_iew = email_iew

    params["email__iew"] = json_email_iew

    json_email_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(email_isw, Unset):
        json_email_isw = email_isw

    params["email__isw"] = json_email_isw

    json_email_n: Union[Unset, list[str]] = UNSET
    if not isinstance(email_n, Unset):
        json_email_n = email_n

    params["email__n"] = json_email_n

    json_email_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(email_nic, Unset):
        json_email_nic = email_nic

    params["email__nic"] = json_email_nic

    json_email_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(email_nie, Unset):
        json_email_nie = email_nie

    params["email__nie"] = json_email_nie

    json_email_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(email_niew, Unset):
        json_email_niew = email_niew

    params["email__niew"] = json_email_niew

    json_email_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(email_nisw, Unset):
        json_email_nisw = email_nisw

    params["email__nisw"] = json_email_nisw

    json_group: Union[Unset, list[str]] = UNSET
    if not isinstance(group, Unset):
        json_group = group

    params["group"] = json_group

    json_group_n: Union[Unset, list[str]] = UNSET
    if not isinstance(group_n, Unset):
        json_group_n = group_n

    params["group__n"] = json_group_n

    json_group_id: Union[Unset, list[str]] = UNSET
    if not isinstance(group_id, Unset):
        json_group_id = group_id

    params["group_id"] = json_group_id

    json_group_id_n: Union[Unset, list[str]] = UNSET
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

    json_link: Union[Unset, list[str]] = UNSET
    if not isinstance(link, Unset):
        json_link = link

    params["link"] = json_link

    params["link__empty"] = link_empty

    json_link_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(link_ic, Unset):
        json_link_ic = link_ic

    params["link__ic"] = json_link_ic

    json_link_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(link_ie, Unset):
        json_link_ie = link_ie

    params["link__ie"] = json_link_ie

    json_link_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(link_iew, Unset):
        json_link_iew = link_iew

    params["link__iew"] = json_link_iew

    json_link_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(link_isw, Unset):
        json_link_isw = link_isw

    params["link__isw"] = json_link_isw

    json_link_n: Union[Unset, list[str]] = UNSET
    if not isinstance(link_n, Unset):
        json_link_n = link_n

    params["link__n"] = json_link_n

    json_link_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(link_nic, Unset):
        json_link_nic = link_nic

    params["link__nic"] = json_link_nic

    json_link_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(link_nie, Unset):
        json_link_nie = link_nie

    params["link__nie"] = json_link_nie

    json_link_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(link_niew, Unset):
        json_link_niew = link_niew

    params["link__niew"] = json_link_niew

    json_link_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(link_nisw, Unset):
        json_link_nisw = link_nisw

    params["link__nisw"] = json_link_nisw

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

    json_phone: Union[Unset, list[str]] = UNSET
    if not isinstance(phone, Unset):
        json_phone = phone

    params["phone"] = json_phone

    params["phone__empty"] = phone_empty

    json_phone_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(phone_ic, Unset):
        json_phone_ic = phone_ic

    params["phone__ic"] = json_phone_ic

    json_phone_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(phone_ie, Unset):
        json_phone_ie = phone_ie

    params["phone__ie"] = json_phone_ie

    json_phone_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(phone_iew, Unset):
        json_phone_iew = phone_iew

    params["phone__iew"] = json_phone_iew

    json_phone_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(phone_isw, Unset):
        json_phone_isw = phone_isw

    params["phone__isw"] = json_phone_isw

    json_phone_n: Union[Unset, list[str]] = UNSET
    if not isinstance(phone_n, Unset):
        json_phone_n = phone_n

    params["phone__n"] = json_phone_n

    json_phone_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(phone_nic, Unset):
        json_phone_nic = phone_nic

    params["phone__nic"] = json_phone_nic

    json_phone_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(phone_nie, Unset):
        json_phone_nie = phone_nie

    params["phone__nie"] = json_phone_nie

    json_phone_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(phone_niew, Unset):
        json_phone_niew = phone_niew

    params["phone__niew"] = json_phone_niew

    json_phone_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(phone_nisw, Unset):
        json_phone_nisw = phone_nisw

    params["phone__nisw"] = json_phone_nisw

    params["q"] = q

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

    json_title: Union[Unset, list[str]] = UNSET
    if not isinstance(title, Unset):
        json_title = title

    params["title"] = json_title

    params["title__empty"] = title_empty

    json_title_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(title_ic, Unset):
        json_title_ic = title_ic

    params["title__ic"] = json_title_ic

    json_title_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(title_ie, Unset):
        json_title_ie = title_ie

    params["title__ie"] = json_title_ie

    json_title_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(title_iew, Unset):
        json_title_iew = title_iew

    params["title__iew"] = json_title_iew

    json_title_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(title_isw, Unset):
        json_title_isw = title_isw

    params["title__isw"] = json_title_isw

    json_title_n: Union[Unset, list[str]] = UNSET
    if not isinstance(title_n, Unset):
        json_title_n = title_n

    params["title__n"] = json_title_n

    json_title_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(title_nic, Unset):
        json_title_nic = title_nic

    params["title__nic"] = json_title_nic

    json_title_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(title_nie, Unset):
        json_title_nie = title_nie

    params["title__nie"] = json_title_nie

    json_title_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(title_niew, Unset):
        json_title_niew = title_niew

    params["title__niew"] = json_title_niew

    json_title_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(title_nisw, Unset):
        json_title_nisw = title_nisw

    params["title__nisw"] = json_title_nisw

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tenancy/contacts/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedContactList]:
    if response.status_code == 200:
        response_200 = PaginatedContactList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedContactList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    address: Union[Unset, list[str]] = UNSET,
    address_empty: Union[Unset, bool] = UNSET,
    address_ic: Union[Unset, list[str]] = UNSET,
    address_ie: Union[Unset, list[str]] = UNSET,
    address_iew: Union[Unset, list[str]] = UNSET,
    address_isw: Union[Unset, list[str]] = UNSET,
    address_n: Union[Unset, list[str]] = UNSET,
    address_nic: Union[Unset, list[str]] = UNSET,
    address_nie: Union[Unset, list[str]] = UNSET,
    address_niew: Union[Unset, list[str]] = UNSET,
    address_nisw: Union[Unset, list[str]] = UNSET,
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
    email: Union[Unset, list[str]] = UNSET,
    email_empty: Union[Unset, bool] = UNSET,
    email_ic: Union[Unset, list[str]] = UNSET,
    email_ie: Union[Unset, list[str]] = UNSET,
    email_iew: Union[Unset, list[str]] = UNSET,
    email_isw: Union[Unset, list[str]] = UNSET,
    email_n: Union[Unset, list[str]] = UNSET,
    email_nic: Union[Unset, list[str]] = UNSET,
    email_nie: Union[Unset, list[str]] = UNSET,
    email_niew: Union[Unset, list[str]] = UNSET,
    email_nisw: Union[Unset, list[str]] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[str]] = UNSET,
    group_id_n: Union[Unset, list[str]] = UNSET,
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
    link: Union[Unset, list[str]] = UNSET,
    link_empty: Union[Unset, bool] = UNSET,
    link_ic: Union[Unset, list[str]] = UNSET,
    link_ie: Union[Unset, list[str]] = UNSET,
    link_iew: Union[Unset, list[str]] = UNSET,
    link_isw: Union[Unset, list[str]] = UNSET,
    link_n: Union[Unset, list[str]] = UNSET,
    link_nic: Union[Unset, list[str]] = UNSET,
    link_nie: Union[Unset, list[str]] = UNSET,
    link_niew: Union[Unset, list[str]] = UNSET,
    link_nisw: Union[Unset, list[str]] = UNSET,
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
    phone: Union[Unset, list[str]] = UNSET,
    phone_empty: Union[Unset, bool] = UNSET,
    phone_ic: Union[Unset, list[str]] = UNSET,
    phone_ie: Union[Unset, list[str]] = UNSET,
    phone_iew: Union[Unset, list[str]] = UNSET,
    phone_isw: Union[Unset, list[str]] = UNSET,
    phone_n: Union[Unset, list[str]] = UNSET,
    phone_nic: Union[Unset, list[str]] = UNSET,
    phone_nie: Union[Unset, list[str]] = UNSET,
    phone_niew: Union[Unset, list[str]] = UNSET,
    phone_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    title: Union[Unset, list[str]] = UNSET,
    title_empty: Union[Unset, bool] = UNSET,
    title_ic: Union[Unset, list[str]] = UNSET,
    title_ie: Union[Unset, list[str]] = UNSET,
    title_iew: Union[Unset, list[str]] = UNSET,
    title_isw: Union[Unset, list[str]] = UNSET,
    title_n: Union[Unset, list[str]] = UNSET,
    title_nic: Union[Unset, list[str]] = UNSET,
    title_nie: Union[Unset, list[str]] = UNSET,
    title_niew: Union[Unset, list[str]] = UNSET,
    title_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedContactList]:
    """Get a list of contact objects.

    Args:
        address (Union[Unset, list[str]]):
        address_empty (Union[Unset, bool]):
        address_ic (Union[Unset, list[str]]):
        address_ie (Union[Unset, list[str]]):
        address_iew (Union[Unset, list[str]]):
        address_isw (Union[Unset, list[str]]):
        address_n (Union[Unset, list[str]]):
        address_nic (Union[Unset, list[str]]):
        address_nie (Union[Unset, list[str]]):
        address_niew (Union[Unset, list[str]]):
        address_nisw (Union[Unset, list[str]]):
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
        email (Union[Unset, list[str]]):
        email_empty (Union[Unset, bool]):
        email_ic (Union[Unset, list[str]]):
        email_ie (Union[Unset, list[str]]):
        email_iew (Union[Unset, list[str]]):
        email_isw (Union[Unset, list[str]]):
        email_n (Union[Unset, list[str]]):
        email_nic (Union[Unset, list[str]]):
        email_nie (Union[Unset, list[str]]):
        email_niew (Union[Unset, list[str]]):
        email_nisw (Union[Unset, list[str]]):
        group (Union[Unset, list[str]]):
        group_n (Union[Unset, list[str]]):
        group_id (Union[Unset, list[str]]):
        group_id_n (Union[Unset, list[str]]):
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
        link (Union[Unset, list[str]]):
        link_empty (Union[Unset, bool]):
        link_ic (Union[Unset, list[str]]):
        link_ie (Union[Unset, list[str]]):
        link_iew (Union[Unset, list[str]]):
        link_isw (Union[Unset, list[str]]):
        link_n (Union[Unset, list[str]]):
        link_nic (Union[Unset, list[str]]):
        link_nie (Union[Unset, list[str]]):
        link_niew (Union[Unset, list[str]]):
        link_nisw (Union[Unset, list[str]]):
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
        phone (Union[Unset, list[str]]):
        phone_empty (Union[Unset, bool]):
        phone_ic (Union[Unset, list[str]]):
        phone_ie (Union[Unset, list[str]]):
        phone_iew (Union[Unset, list[str]]):
        phone_isw (Union[Unset, list[str]]):
        phone_n (Union[Unset, list[str]]):
        phone_nic (Union[Unset, list[str]]):
        phone_nie (Union[Unset, list[str]]):
        phone_niew (Union[Unset, list[str]]):
        phone_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        title (Union[Unset, list[str]]):
        title_empty (Union[Unset, bool]):
        title_ic (Union[Unset, list[str]]):
        title_ie (Union[Unset, list[str]]):
        title_iew (Union[Unset, list[str]]):
        title_isw (Union[Unset, list[str]]):
        title_n (Union[Unset, list[str]]):
        title_nic (Union[Unset, list[str]]):
        title_nie (Union[Unset, list[str]]):
        title_niew (Union[Unset, list[str]]):
        title_nisw (Union[Unset, list[str]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedContactList]
    """

    kwargs = _get_kwargs(
        address=address,
        address_empty=address_empty,
        address_ic=address_ic,
        address_ie=address_ie,
        address_iew=address_iew,
        address_isw=address_isw,
        address_n=address_n,
        address_nic=address_nic,
        address_nie=address_nie,
        address_niew=address_niew,
        address_nisw=address_nisw,
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
        email=email,
        email_empty=email_empty,
        email_ic=email_ic,
        email_ie=email_ie,
        email_iew=email_iew,
        email_isw=email_isw,
        email_n=email_n,
        email_nic=email_nic,
        email_nie=email_nie,
        email_niew=email_niew,
        email_nisw=email_nisw,
        group=group,
        group_n=group_n,
        group_id=group_id,
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
        link=link,
        link_empty=link_empty,
        link_ic=link_ic,
        link_ie=link_ie,
        link_iew=link_iew,
        link_isw=link_isw,
        link_n=link_n,
        link_nic=link_nic,
        link_nie=link_nie,
        link_niew=link_niew,
        link_nisw=link_nisw,
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
        phone=phone,
        phone_empty=phone_empty,
        phone_ic=phone_ic,
        phone_ie=phone_ie,
        phone_iew=phone_iew,
        phone_isw=phone_isw,
        phone_n=phone_n,
        phone_nic=phone_nic,
        phone_nie=phone_nie,
        phone_niew=phone_niew,
        phone_nisw=phone_nisw,
        q=q,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        title=title,
        title_empty=title_empty,
        title_ic=title_ic,
        title_ie=title_ie,
        title_iew=title_iew,
        title_isw=title_isw,
        title_n=title_n,
        title_nic=title_nic,
        title_nie=title_nie,
        title_niew=title_niew,
        title_nisw=title_nisw,
        updated_by_request=updated_by_request,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    address: Union[Unset, list[str]] = UNSET,
    address_empty: Union[Unset, bool] = UNSET,
    address_ic: Union[Unset, list[str]] = UNSET,
    address_ie: Union[Unset, list[str]] = UNSET,
    address_iew: Union[Unset, list[str]] = UNSET,
    address_isw: Union[Unset, list[str]] = UNSET,
    address_n: Union[Unset, list[str]] = UNSET,
    address_nic: Union[Unset, list[str]] = UNSET,
    address_nie: Union[Unset, list[str]] = UNSET,
    address_niew: Union[Unset, list[str]] = UNSET,
    address_nisw: Union[Unset, list[str]] = UNSET,
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
    email: Union[Unset, list[str]] = UNSET,
    email_empty: Union[Unset, bool] = UNSET,
    email_ic: Union[Unset, list[str]] = UNSET,
    email_ie: Union[Unset, list[str]] = UNSET,
    email_iew: Union[Unset, list[str]] = UNSET,
    email_isw: Union[Unset, list[str]] = UNSET,
    email_n: Union[Unset, list[str]] = UNSET,
    email_nic: Union[Unset, list[str]] = UNSET,
    email_nie: Union[Unset, list[str]] = UNSET,
    email_niew: Union[Unset, list[str]] = UNSET,
    email_nisw: Union[Unset, list[str]] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[str]] = UNSET,
    group_id_n: Union[Unset, list[str]] = UNSET,
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
    link: Union[Unset, list[str]] = UNSET,
    link_empty: Union[Unset, bool] = UNSET,
    link_ic: Union[Unset, list[str]] = UNSET,
    link_ie: Union[Unset, list[str]] = UNSET,
    link_iew: Union[Unset, list[str]] = UNSET,
    link_isw: Union[Unset, list[str]] = UNSET,
    link_n: Union[Unset, list[str]] = UNSET,
    link_nic: Union[Unset, list[str]] = UNSET,
    link_nie: Union[Unset, list[str]] = UNSET,
    link_niew: Union[Unset, list[str]] = UNSET,
    link_nisw: Union[Unset, list[str]] = UNSET,
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
    phone: Union[Unset, list[str]] = UNSET,
    phone_empty: Union[Unset, bool] = UNSET,
    phone_ic: Union[Unset, list[str]] = UNSET,
    phone_ie: Union[Unset, list[str]] = UNSET,
    phone_iew: Union[Unset, list[str]] = UNSET,
    phone_isw: Union[Unset, list[str]] = UNSET,
    phone_n: Union[Unset, list[str]] = UNSET,
    phone_nic: Union[Unset, list[str]] = UNSET,
    phone_nie: Union[Unset, list[str]] = UNSET,
    phone_niew: Union[Unset, list[str]] = UNSET,
    phone_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    title: Union[Unset, list[str]] = UNSET,
    title_empty: Union[Unset, bool] = UNSET,
    title_ic: Union[Unset, list[str]] = UNSET,
    title_ie: Union[Unset, list[str]] = UNSET,
    title_iew: Union[Unset, list[str]] = UNSET,
    title_isw: Union[Unset, list[str]] = UNSET,
    title_n: Union[Unset, list[str]] = UNSET,
    title_nic: Union[Unset, list[str]] = UNSET,
    title_nie: Union[Unset, list[str]] = UNSET,
    title_niew: Union[Unset, list[str]] = UNSET,
    title_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedContactList]:
    """Get a list of contact objects.

    Args:
        address (Union[Unset, list[str]]):
        address_empty (Union[Unset, bool]):
        address_ic (Union[Unset, list[str]]):
        address_ie (Union[Unset, list[str]]):
        address_iew (Union[Unset, list[str]]):
        address_isw (Union[Unset, list[str]]):
        address_n (Union[Unset, list[str]]):
        address_nic (Union[Unset, list[str]]):
        address_nie (Union[Unset, list[str]]):
        address_niew (Union[Unset, list[str]]):
        address_nisw (Union[Unset, list[str]]):
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
        email (Union[Unset, list[str]]):
        email_empty (Union[Unset, bool]):
        email_ic (Union[Unset, list[str]]):
        email_ie (Union[Unset, list[str]]):
        email_iew (Union[Unset, list[str]]):
        email_isw (Union[Unset, list[str]]):
        email_n (Union[Unset, list[str]]):
        email_nic (Union[Unset, list[str]]):
        email_nie (Union[Unset, list[str]]):
        email_niew (Union[Unset, list[str]]):
        email_nisw (Union[Unset, list[str]]):
        group (Union[Unset, list[str]]):
        group_n (Union[Unset, list[str]]):
        group_id (Union[Unset, list[str]]):
        group_id_n (Union[Unset, list[str]]):
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
        link (Union[Unset, list[str]]):
        link_empty (Union[Unset, bool]):
        link_ic (Union[Unset, list[str]]):
        link_ie (Union[Unset, list[str]]):
        link_iew (Union[Unset, list[str]]):
        link_isw (Union[Unset, list[str]]):
        link_n (Union[Unset, list[str]]):
        link_nic (Union[Unset, list[str]]):
        link_nie (Union[Unset, list[str]]):
        link_niew (Union[Unset, list[str]]):
        link_nisw (Union[Unset, list[str]]):
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
        phone (Union[Unset, list[str]]):
        phone_empty (Union[Unset, bool]):
        phone_ic (Union[Unset, list[str]]):
        phone_ie (Union[Unset, list[str]]):
        phone_iew (Union[Unset, list[str]]):
        phone_isw (Union[Unset, list[str]]):
        phone_n (Union[Unset, list[str]]):
        phone_nic (Union[Unset, list[str]]):
        phone_nie (Union[Unset, list[str]]):
        phone_niew (Union[Unset, list[str]]):
        phone_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        title (Union[Unset, list[str]]):
        title_empty (Union[Unset, bool]):
        title_ic (Union[Unset, list[str]]):
        title_ie (Union[Unset, list[str]]):
        title_iew (Union[Unset, list[str]]):
        title_isw (Union[Unset, list[str]]):
        title_n (Union[Unset, list[str]]):
        title_nic (Union[Unset, list[str]]):
        title_nie (Union[Unset, list[str]]):
        title_niew (Union[Unset, list[str]]):
        title_nisw (Union[Unset, list[str]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedContactList
    """

    return sync_detailed(
        client=client,
        address=address,
        address_empty=address_empty,
        address_ic=address_ic,
        address_ie=address_ie,
        address_iew=address_iew,
        address_isw=address_isw,
        address_n=address_n,
        address_nic=address_nic,
        address_nie=address_nie,
        address_niew=address_niew,
        address_nisw=address_nisw,
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
        email=email,
        email_empty=email_empty,
        email_ic=email_ic,
        email_ie=email_ie,
        email_iew=email_iew,
        email_isw=email_isw,
        email_n=email_n,
        email_nic=email_nic,
        email_nie=email_nie,
        email_niew=email_niew,
        email_nisw=email_nisw,
        group=group,
        group_n=group_n,
        group_id=group_id,
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
        link=link,
        link_empty=link_empty,
        link_ic=link_ic,
        link_ie=link_ie,
        link_iew=link_iew,
        link_isw=link_isw,
        link_n=link_n,
        link_nic=link_nic,
        link_nie=link_nie,
        link_niew=link_niew,
        link_nisw=link_nisw,
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
        phone=phone,
        phone_empty=phone_empty,
        phone_ic=phone_ic,
        phone_ie=phone_ie,
        phone_iew=phone_iew,
        phone_isw=phone_isw,
        phone_n=phone_n,
        phone_nic=phone_nic,
        phone_nie=phone_nie,
        phone_niew=phone_niew,
        phone_nisw=phone_nisw,
        q=q,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        title=title,
        title_empty=title_empty,
        title_ic=title_ic,
        title_ie=title_ie,
        title_iew=title_iew,
        title_isw=title_isw,
        title_n=title_n,
        title_nic=title_nic,
        title_nie=title_nie,
        title_niew=title_niew,
        title_nisw=title_nisw,
        updated_by_request=updated_by_request,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    address: Union[Unset, list[str]] = UNSET,
    address_empty: Union[Unset, bool] = UNSET,
    address_ic: Union[Unset, list[str]] = UNSET,
    address_ie: Union[Unset, list[str]] = UNSET,
    address_iew: Union[Unset, list[str]] = UNSET,
    address_isw: Union[Unset, list[str]] = UNSET,
    address_n: Union[Unset, list[str]] = UNSET,
    address_nic: Union[Unset, list[str]] = UNSET,
    address_nie: Union[Unset, list[str]] = UNSET,
    address_niew: Union[Unset, list[str]] = UNSET,
    address_nisw: Union[Unset, list[str]] = UNSET,
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
    email: Union[Unset, list[str]] = UNSET,
    email_empty: Union[Unset, bool] = UNSET,
    email_ic: Union[Unset, list[str]] = UNSET,
    email_ie: Union[Unset, list[str]] = UNSET,
    email_iew: Union[Unset, list[str]] = UNSET,
    email_isw: Union[Unset, list[str]] = UNSET,
    email_n: Union[Unset, list[str]] = UNSET,
    email_nic: Union[Unset, list[str]] = UNSET,
    email_nie: Union[Unset, list[str]] = UNSET,
    email_niew: Union[Unset, list[str]] = UNSET,
    email_nisw: Union[Unset, list[str]] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[str]] = UNSET,
    group_id_n: Union[Unset, list[str]] = UNSET,
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
    link: Union[Unset, list[str]] = UNSET,
    link_empty: Union[Unset, bool] = UNSET,
    link_ic: Union[Unset, list[str]] = UNSET,
    link_ie: Union[Unset, list[str]] = UNSET,
    link_iew: Union[Unset, list[str]] = UNSET,
    link_isw: Union[Unset, list[str]] = UNSET,
    link_n: Union[Unset, list[str]] = UNSET,
    link_nic: Union[Unset, list[str]] = UNSET,
    link_nie: Union[Unset, list[str]] = UNSET,
    link_niew: Union[Unset, list[str]] = UNSET,
    link_nisw: Union[Unset, list[str]] = UNSET,
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
    phone: Union[Unset, list[str]] = UNSET,
    phone_empty: Union[Unset, bool] = UNSET,
    phone_ic: Union[Unset, list[str]] = UNSET,
    phone_ie: Union[Unset, list[str]] = UNSET,
    phone_iew: Union[Unset, list[str]] = UNSET,
    phone_isw: Union[Unset, list[str]] = UNSET,
    phone_n: Union[Unset, list[str]] = UNSET,
    phone_nic: Union[Unset, list[str]] = UNSET,
    phone_nie: Union[Unset, list[str]] = UNSET,
    phone_niew: Union[Unset, list[str]] = UNSET,
    phone_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    title: Union[Unset, list[str]] = UNSET,
    title_empty: Union[Unset, bool] = UNSET,
    title_ic: Union[Unset, list[str]] = UNSET,
    title_ie: Union[Unset, list[str]] = UNSET,
    title_iew: Union[Unset, list[str]] = UNSET,
    title_isw: Union[Unset, list[str]] = UNSET,
    title_n: Union[Unset, list[str]] = UNSET,
    title_nic: Union[Unset, list[str]] = UNSET,
    title_nie: Union[Unset, list[str]] = UNSET,
    title_niew: Union[Unset, list[str]] = UNSET,
    title_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedContactList]:
    """Get a list of contact objects.

    Args:
        address (Union[Unset, list[str]]):
        address_empty (Union[Unset, bool]):
        address_ic (Union[Unset, list[str]]):
        address_ie (Union[Unset, list[str]]):
        address_iew (Union[Unset, list[str]]):
        address_isw (Union[Unset, list[str]]):
        address_n (Union[Unset, list[str]]):
        address_nic (Union[Unset, list[str]]):
        address_nie (Union[Unset, list[str]]):
        address_niew (Union[Unset, list[str]]):
        address_nisw (Union[Unset, list[str]]):
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
        email (Union[Unset, list[str]]):
        email_empty (Union[Unset, bool]):
        email_ic (Union[Unset, list[str]]):
        email_ie (Union[Unset, list[str]]):
        email_iew (Union[Unset, list[str]]):
        email_isw (Union[Unset, list[str]]):
        email_n (Union[Unset, list[str]]):
        email_nic (Union[Unset, list[str]]):
        email_nie (Union[Unset, list[str]]):
        email_niew (Union[Unset, list[str]]):
        email_nisw (Union[Unset, list[str]]):
        group (Union[Unset, list[str]]):
        group_n (Union[Unset, list[str]]):
        group_id (Union[Unset, list[str]]):
        group_id_n (Union[Unset, list[str]]):
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
        link (Union[Unset, list[str]]):
        link_empty (Union[Unset, bool]):
        link_ic (Union[Unset, list[str]]):
        link_ie (Union[Unset, list[str]]):
        link_iew (Union[Unset, list[str]]):
        link_isw (Union[Unset, list[str]]):
        link_n (Union[Unset, list[str]]):
        link_nic (Union[Unset, list[str]]):
        link_nie (Union[Unset, list[str]]):
        link_niew (Union[Unset, list[str]]):
        link_nisw (Union[Unset, list[str]]):
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
        phone (Union[Unset, list[str]]):
        phone_empty (Union[Unset, bool]):
        phone_ic (Union[Unset, list[str]]):
        phone_ie (Union[Unset, list[str]]):
        phone_iew (Union[Unset, list[str]]):
        phone_isw (Union[Unset, list[str]]):
        phone_n (Union[Unset, list[str]]):
        phone_nic (Union[Unset, list[str]]):
        phone_nie (Union[Unset, list[str]]):
        phone_niew (Union[Unset, list[str]]):
        phone_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        title (Union[Unset, list[str]]):
        title_empty (Union[Unset, bool]):
        title_ic (Union[Unset, list[str]]):
        title_ie (Union[Unset, list[str]]):
        title_iew (Union[Unset, list[str]]):
        title_isw (Union[Unset, list[str]]):
        title_n (Union[Unset, list[str]]):
        title_nic (Union[Unset, list[str]]):
        title_nie (Union[Unset, list[str]]):
        title_niew (Union[Unset, list[str]]):
        title_nisw (Union[Unset, list[str]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedContactList]
    """

    kwargs = _get_kwargs(
        address=address,
        address_empty=address_empty,
        address_ic=address_ic,
        address_ie=address_ie,
        address_iew=address_iew,
        address_isw=address_isw,
        address_n=address_n,
        address_nic=address_nic,
        address_nie=address_nie,
        address_niew=address_niew,
        address_nisw=address_nisw,
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
        email=email,
        email_empty=email_empty,
        email_ic=email_ic,
        email_ie=email_ie,
        email_iew=email_iew,
        email_isw=email_isw,
        email_n=email_n,
        email_nic=email_nic,
        email_nie=email_nie,
        email_niew=email_niew,
        email_nisw=email_nisw,
        group=group,
        group_n=group_n,
        group_id=group_id,
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
        link=link,
        link_empty=link_empty,
        link_ic=link_ic,
        link_ie=link_ie,
        link_iew=link_iew,
        link_isw=link_isw,
        link_n=link_n,
        link_nic=link_nic,
        link_nie=link_nie,
        link_niew=link_niew,
        link_nisw=link_nisw,
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
        phone=phone,
        phone_empty=phone_empty,
        phone_ic=phone_ic,
        phone_ie=phone_ie,
        phone_iew=phone_iew,
        phone_isw=phone_isw,
        phone_n=phone_n,
        phone_nic=phone_nic,
        phone_nie=phone_nie,
        phone_niew=phone_niew,
        phone_nisw=phone_nisw,
        q=q,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        title=title,
        title_empty=title_empty,
        title_ic=title_ic,
        title_ie=title_ie,
        title_iew=title_iew,
        title_isw=title_isw,
        title_n=title_n,
        title_nic=title_nic,
        title_nie=title_nie,
        title_niew=title_niew,
        title_nisw=title_nisw,
        updated_by_request=updated_by_request,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    address: Union[Unset, list[str]] = UNSET,
    address_empty: Union[Unset, bool] = UNSET,
    address_ic: Union[Unset, list[str]] = UNSET,
    address_ie: Union[Unset, list[str]] = UNSET,
    address_iew: Union[Unset, list[str]] = UNSET,
    address_isw: Union[Unset, list[str]] = UNSET,
    address_n: Union[Unset, list[str]] = UNSET,
    address_nic: Union[Unset, list[str]] = UNSET,
    address_nie: Union[Unset, list[str]] = UNSET,
    address_niew: Union[Unset, list[str]] = UNSET,
    address_nisw: Union[Unset, list[str]] = UNSET,
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
    email: Union[Unset, list[str]] = UNSET,
    email_empty: Union[Unset, bool] = UNSET,
    email_ic: Union[Unset, list[str]] = UNSET,
    email_ie: Union[Unset, list[str]] = UNSET,
    email_iew: Union[Unset, list[str]] = UNSET,
    email_isw: Union[Unset, list[str]] = UNSET,
    email_n: Union[Unset, list[str]] = UNSET,
    email_nic: Union[Unset, list[str]] = UNSET,
    email_nie: Union[Unset, list[str]] = UNSET,
    email_niew: Union[Unset, list[str]] = UNSET,
    email_nisw: Union[Unset, list[str]] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    group_n: Union[Unset, list[str]] = UNSET,
    group_id: Union[Unset, list[str]] = UNSET,
    group_id_n: Union[Unset, list[str]] = UNSET,
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
    link: Union[Unset, list[str]] = UNSET,
    link_empty: Union[Unset, bool] = UNSET,
    link_ic: Union[Unset, list[str]] = UNSET,
    link_ie: Union[Unset, list[str]] = UNSET,
    link_iew: Union[Unset, list[str]] = UNSET,
    link_isw: Union[Unset, list[str]] = UNSET,
    link_n: Union[Unset, list[str]] = UNSET,
    link_nic: Union[Unset, list[str]] = UNSET,
    link_nie: Union[Unset, list[str]] = UNSET,
    link_niew: Union[Unset, list[str]] = UNSET,
    link_nisw: Union[Unset, list[str]] = UNSET,
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
    phone: Union[Unset, list[str]] = UNSET,
    phone_empty: Union[Unset, bool] = UNSET,
    phone_ic: Union[Unset, list[str]] = UNSET,
    phone_ie: Union[Unset, list[str]] = UNSET,
    phone_iew: Union[Unset, list[str]] = UNSET,
    phone_isw: Union[Unset, list[str]] = UNSET,
    phone_n: Union[Unset, list[str]] = UNSET,
    phone_nic: Union[Unset, list[str]] = UNSET,
    phone_nie: Union[Unset, list[str]] = UNSET,
    phone_niew: Union[Unset, list[str]] = UNSET,
    phone_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    title: Union[Unset, list[str]] = UNSET,
    title_empty: Union[Unset, bool] = UNSET,
    title_ic: Union[Unset, list[str]] = UNSET,
    title_ie: Union[Unset, list[str]] = UNSET,
    title_iew: Union[Unset, list[str]] = UNSET,
    title_isw: Union[Unset, list[str]] = UNSET,
    title_n: Union[Unset, list[str]] = UNSET,
    title_nic: Union[Unset, list[str]] = UNSET,
    title_nie: Union[Unset, list[str]] = UNSET,
    title_niew: Union[Unset, list[str]] = UNSET,
    title_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedContactList]:
    """Get a list of contact objects.

    Args:
        address (Union[Unset, list[str]]):
        address_empty (Union[Unset, bool]):
        address_ic (Union[Unset, list[str]]):
        address_ie (Union[Unset, list[str]]):
        address_iew (Union[Unset, list[str]]):
        address_isw (Union[Unset, list[str]]):
        address_n (Union[Unset, list[str]]):
        address_nic (Union[Unset, list[str]]):
        address_nie (Union[Unset, list[str]]):
        address_niew (Union[Unset, list[str]]):
        address_nisw (Union[Unset, list[str]]):
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
        email (Union[Unset, list[str]]):
        email_empty (Union[Unset, bool]):
        email_ic (Union[Unset, list[str]]):
        email_ie (Union[Unset, list[str]]):
        email_iew (Union[Unset, list[str]]):
        email_isw (Union[Unset, list[str]]):
        email_n (Union[Unset, list[str]]):
        email_nic (Union[Unset, list[str]]):
        email_nie (Union[Unset, list[str]]):
        email_niew (Union[Unset, list[str]]):
        email_nisw (Union[Unset, list[str]]):
        group (Union[Unset, list[str]]):
        group_n (Union[Unset, list[str]]):
        group_id (Union[Unset, list[str]]):
        group_id_n (Union[Unset, list[str]]):
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
        link (Union[Unset, list[str]]):
        link_empty (Union[Unset, bool]):
        link_ic (Union[Unset, list[str]]):
        link_ie (Union[Unset, list[str]]):
        link_iew (Union[Unset, list[str]]):
        link_isw (Union[Unset, list[str]]):
        link_n (Union[Unset, list[str]]):
        link_nic (Union[Unset, list[str]]):
        link_nie (Union[Unset, list[str]]):
        link_niew (Union[Unset, list[str]]):
        link_nisw (Union[Unset, list[str]]):
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
        phone (Union[Unset, list[str]]):
        phone_empty (Union[Unset, bool]):
        phone_ic (Union[Unset, list[str]]):
        phone_ie (Union[Unset, list[str]]):
        phone_iew (Union[Unset, list[str]]):
        phone_isw (Union[Unset, list[str]]):
        phone_n (Union[Unset, list[str]]):
        phone_nic (Union[Unset, list[str]]):
        phone_nie (Union[Unset, list[str]]):
        phone_niew (Union[Unset, list[str]]):
        phone_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        title (Union[Unset, list[str]]):
        title_empty (Union[Unset, bool]):
        title_ic (Union[Unset, list[str]]):
        title_ie (Union[Unset, list[str]]):
        title_iew (Union[Unset, list[str]]):
        title_isw (Union[Unset, list[str]]):
        title_n (Union[Unset, list[str]]):
        title_nic (Union[Unset, list[str]]):
        title_nie (Union[Unset, list[str]]):
        title_niew (Union[Unset, list[str]]):
        title_nisw (Union[Unset, list[str]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedContactList
    """

    return (
        await asyncio_detailed(
            client=client,
            address=address,
            address_empty=address_empty,
            address_ic=address_ic,
            address_ie=address_ie,
            address_iew=address_iew,
            address_isw=address_isw,
            address_n=address_n,
            address_nic=address_nic,
            address_nie=address_nie,
            address_niew=address_niew,
            address_nisw=address_nisw,
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
            email=email,
            email_empty=email_empty,
            email_ic=email_ic,
            email_ie=email_ie,
            email_iew=email_iew,
            email_isw=email_isw,
            email_n=email_n,
            email_nic=email_nic,
            email_nie=email_nie,
            email_niew=email_niew,
            email_nisw=email_nisw,
            group=group,
            group_n=group_n,
            group_id=group_id,
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
            link=link,
            link_empty=link_empty,
            link_ic=link_ic,
            link_ie=link_ie,
            link_iew=link_iew,
            link_isw=link_isw,
            link_n=link_n,
            link_nic=link_nic,
            link_nie=link_nie,
            link_niew=link_niew,
            link_nisw=link_nisw,
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
            phone=phone,
            phone_empty=phone_empty,
            phone_ic=phone_ic,
            phone_ie=phone_ie,
            phone_iew=phone_iew,
            phone_isw=phone_isw,
            phone_n=phone_n,
            phone_nic=phone_nic,
            phone_nie=phone_nie,
            phone_niew=phone_niew,
            phone_nisw=phone_nisw,
            q=q,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
            title=title,
            title_empty=title_empty,
            title_ic=title_ic,
            title_ie=title_ie,
            title_iew=title_iew,
            title_isw=title_isw,
            title_n=title_n,
            title_nic=title_nic,
            title_nie=title_nie,
            title_niew=title_niew,
            title_nisw=title_nisw,
            updated_by_request=updated_by_request,
        )
    ).parsed
