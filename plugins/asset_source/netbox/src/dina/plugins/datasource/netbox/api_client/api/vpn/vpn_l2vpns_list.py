import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_l2vpn_list import PaginatedL2VPNList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
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
    export_target: Union[Unset, list[str]] = UNSET,
    export_target_n: Union[Unset, list[str]] = UNSET,
    export_target_id: Union[Unset, list[int]] = UNSET,
    export_target_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    identifier: Union[Unset, list[int]] = UNSET,
    identifier_empty: Union[Unset, bool] = UNSET,
    identifier_gt: Union[Unset, list[int]] = UNSET,
    identifier_gte: Union[Unset, list[int]] = UNSET,
    identifier_lt: Union[Unset, list[int]] = UNSET,
    identifier_lte: Union[Unset, list[int]] = UNSET,
    identifier_n: Union[Unset, list[int]] = UNSET,
    import_target: Union[Unset, list[str]] = UNSET,
    import_target_n: Union[Unset, list[str]] = UNSET,
    import_target_id: Union[Unset, list[int]] = UNSET,
    import_target_id_n: Union[Unset, list[int]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

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

    json_export_target: Union[Unset, list[str]] = UNSET
    if not isinstance(export_target, Unset):
        json_export_target = export_target

    params["export_target"] = json_export_target

    json_export_target_n: Union[Unset, list[str]] = UNSET
    if not isinstance(export_target_n, Unset):
        json_export_target_n = export_target_n

    params["export_target__n"] = json_export_target_n

    json_export_target_id: Union[Unset, list[int]] = UNSET
    if not isinstance(export_target_id, Unset):
        json_export_target_id = export_target_id

    params["export_target_id"] = json_export_target_id

    json_export_target_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(export_target_id_n, Unset):
        json_export_target_id_n = export_target_id_n

    params["export_target_id__n"] = json_export_target_id_n

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

    json_identifier: Union[Unset, list[int]] = UNSET
    if not isinstance(identifier, Unset):
        json_identifier = identifier

    params["identifier"] = json_identifier

    params["identifier__empty"] = identifier_empty

    json_identifier_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(identifier_gt, Unset):
        json_identifier_gt = identifier_gt

    params["identifier__gt"] = json_identifier_gt

    json_identifier_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(identifier_gte, Unset):
        json_identifier_gte = identifier_gte

    params["identifier__gte"] = json_identifier_gte

    json_identifier_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(identifier_lt, Unset):
        json_identifier_lt = identifier_lt

    params["identifier__lt"] = json_identifier_lt

    json_identifier_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(identifier_lte, Unset):
        json_identifier_lte = identifier_lte

    params["identifier__lte"] = json_identifier_lte

    json_identifier_n: Union[Unset, list[int]] = UNSET
    if not isinstance(identifier_n, Unset):
        json_identifier_n = identifier_n

    params["identifier__n"] = json_identifier_n

    json_import_target: Union[Unset, list[str]] = UNSET
    if not isinstance(import_target, Unset):
        json_import_target = import_target

    params["import_target"] = json_import_target

    json_import_target_n: Union[Unset, list[str]] = UNSET
    if not isinstance(import_target_n, Unset):
        json_import_target_n = import_target_n

    params["import_target__n"] = json_import_target_n

    json_import_target_id: Union[Unset, list[int]] = UNSET
    if not isinstance(import_target_id, Unset):
        json_import_target_id = import_target_id

    params["import_target_id"] = json_import_target_id

    json_import_target_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(import_target_id_n, Unset):
        json_import_target_id_n = import_target_id_n

    params["import_target_id__n"] = json_import_target_id_n

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

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/vpn/l2vpns/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedL2VPNList]:
    if response.status_code == 200:
        response_200 = PaginatedL2VPNList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedL2VPNList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
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
    export_target: Union[Unset, list[str]] = UNSET,
    export_target_n: Union[Unset, list[str]] = UNSET,
    export_target_id: Union[Unset, list[int]] = UNSET,
    export_target_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    identifier: Union[Unset, list[int]] = UNSET,
    identifier_empty: Union[Unset, bool] = UNSET,
    identifier_gt: Union[Unset, list[int]] = UNSET,
    identifier_gte: Union[Unset, list[int]] = UNSET,
    identifier_lt: Union[Unset, list[int]] = UNSET,
    identifier_lte: Union[Unset, list[int]] = UNSET,
    identifier_n: Union[Unset, list[int]] = UNSET,
    import_target: Union[Unset, list[str]] = UNSET,
    import_target_n: Union[Unset, list[str]] = UNSET,
    import_target_id: Union[Unset, list[int]] = UNSET,
    import_target_id_n: Union[Unset, list[int]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedL2VPNList]:
    """Get a list of L2VPN objects.

    Args:
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
        export_target (Union[Unset, list[str]]):
        export_target_n (Union[Unset, list[str]]):
        export_target_id (Union[Unset, list[int]]):
        export_target_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        identifier (Union[Unset, list[int]]):
        identifier_empty (Union[Unset, bool]):
        identifier_gt (Union[Unset, list[int]]):
        identifier_gte (Union[Unset, list[int]]):
        identifier_lt (Union[Unset, list[int]]):
        identifier_lte (Union[Unset, list[int]]):
        identifier_n (Union[Unset, list[int]]):
        import_target (Union[Unset, list[str]]):
        import_target_n (Union[Unset, list[str]]):
        import_target_id (Union[Unset, list[int]]):
        import_target_id_n (Union[Unset, list[int]]):
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
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedL2VPNList]
    """

    kwargs = _get_kwargs(
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
        export_target=export_target,
        export_target_n=export_target_n,
        export_target_id=export_target_id,
        export_target_id_n=export_target_id_n,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        identifier=identifier,
        identifier_empty=identifier_empty,
        identifier_gt=identifier_gt,
        identifier_gte=identifier_gte,
        identifier_lt=identifier_lt,
        identifier_lte=identifier_lte,
        identifier_n=identifier_n,
        import_target=import_target,
        import_target_n=import_target_n,
        import_target_id=import_target_id,
        import_target_id_n=import_target_id_n,
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
        updated_by_request=updated_by_request,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
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
    export_target: Union[Unset, list[str]] = UNSET,
    export_target_n: Union[Unset, list[str]] = UNSET,
    export_target_id: Union[Unset, list[int]] = UNSET,
    export_target_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    identifier: Union[Unset, list[int]] = UNSET,
    identifier_empty: Union[Unset, bool] = UNSET,
    identifier_gt: Union[Unset, list[int]] = UNSET,
    identifier_gte: Union[Unset, list[int]] = UNSET,
    identifier_lt: Union[Unset, list[int]] = UNSET,
    identifier_lte: Union[Unset, list[int]] = UNSET,
    identifier_n: Union[Unset, list[int]] = UNSET,
    import_target: Union[Unset, list[str]] = UNSET,
    import_target_n: Union[Unset, list[str]] = UNSET,
    import_target_id: Union[Unset, list[int]] = UNSET,
    import_target_id_n: Union[Unset, list[int]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedL2VPNList]:
    """Get a list of L2VPN objects.

    Args:
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
        export_target (Union[Unset, list[str]]):
        export_target_n (Union[Unset, list[str]]):
        export_target_id (Union[Unset, list[int]]):
        export_target_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        identifier (Union[Unset, list[int]]):
        identifier_empty (Union[Unset, bool]):
        identifier_gt (Union[Unset, list[int]]):
        identifier_gte (Union[Unset, list[int]]):
        identifier_lt (Union[Unset, list[int]]):
        identifier_lte (Union[Unset, list[int]]):
        identifier_n (Union[Unset, list[int]]):
        import_target (Union[Unset, list[str]]):
        import_target_n (Union[Unset, list[str]]):
        import_target_id (Union[Unset, list[int]]):
        import_target_id_n (Union[Unset, list[int]]):
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
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedL2VPNList
    """

    return sync_detailed(
        client=client,
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
        export_target=export_target,
        export_target_n=export_target_n,
        export_target_id=export_target_id,
        export_target_id_n=export_target_id_n,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        identifier=identifier,
        identifier_empty=identifier_empty,
        identifier_gt=identifier_gt,
        identifier_gte=identifier_gte,
        identifier_lt=identifier_lt,
        identifier_lte=identifier_lte,
        identifier_n=identifier_n,
        import_target=import_target,
        import_target_n=import_target_n,
        import_target_id=import_target_id,
        import_target_id_n=import_target_id_n,
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
        updated_by_request=updated_by_request,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
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
    export_target: Union[Unset, list[str]] = UNSET,
    export_target_n: Union[Unset, list[str]] = UNSET,
    export_target_id: Union[Unset, list[int]] = UNSET,
    export_target_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    identifier: Union[Unset, list[int]] = UNSET,
    identifier_empty: Union[Unset, bool] = UNSET,
    identifier_gt: Union[Unset, list[int]] = UNSET,
    identifier_gte: Union[Unset, list[int]] = UNSET,
    identifier_lt: Union[Unset, list[int]] = UNSET,
    identifier_lte: Union[Unset, list[int]] = UNSET,
    identifier_n: Union[Unset, list[int]] = UNSET,
    import_target: Union[Unset, list[str]] = UNSET,
    import_target_n: Union[Unset, list[str]] = UNSET,
    import_target_id: Union[Unset, list[int]] = UNSET,
    import_target_id_n: Union[Unset, list[int]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedL2VPNList]:
    """Get a list of L2VPN objects.

    Args:
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
        export_target (Union[Unset, list[str]]):
        export_target_n (Union[Unset, list[str]]):
        export_target_id (Union[Unset, list[int]]):
        export_target_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        identifier (Union[Unset, list[int]]):
        identifier_empty (Union[Unset, bool]):
        identifier_gt (Union[Unset, list[int]]):
        identifier_gte (Union[Unset, list[int]]):
        identifier_lt (Union[Unset, list[int]]):
        identifier_lte (Union[Unset, list[int]]):
        identifier_n (Union[Unset, list[int]]):
        import_target (Union[Unset, list[str]]):
        import_target_n (Union[Unset, list[str]]):
        import_target_id (Union[Unset, list[int]]):
        import_target_id_n (Union[Unset, list[int]]):
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
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedL2VPNList]
    """

    kwargs = _get_kwargs(
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
        export_target=export_target,
        export_target_n=export_target_n,
        export_target_id=export_target_id,
        export_target_id_n=export_target_id_n,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        identifier=identifier,
        identifier_empty=identifier_empty,
        identifier_gt=identifier_gt,
        identifier_gte=identifier_gte,
        identifier_lt=identifier_lt,
        identifier_lte=identifier_lte,
        identifier_n=identifier_n,
        import_target=import_target,
        import_target_n=import_target_n,
        import_target_id=import_target_id,
        import_target_id_n=import_target_id_n,
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
        updated_by_request=updated_by_request,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
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
    export_target: Union[Unset, list[str]] = UNSET,
    export_target_n: Union[Unset, list[str]] = UNSET,
    export_target_id: Union[Unset, list[int]] = UNSET,
    export_target_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    identifier: Union[Unset, list[int]] = UNSET,
    identifier_empty: Union[Unset, bool] = UNSET,
    identifier_gt: Union[Unset, list[int]] = UNSET,
    identifier_gte: Union[Unset, list[int]] = UNSET,
    identifier_lt: Union[Unset, list[int]] = UNSET,
    identifier_lte: Union[Unset, list[int]] = UNSET,
    identifier_n: Union[Unset, list[int]] = UNSET,
    import_target: Union[Unset, list[str]] = UNSET,
    import_target_n: Union[Unset, list[str]] = UNSET,
    import_target_id: Union[Unset, list[int]] = UNSET,
    import_target_id_n: Union[Unset, list[int]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedL2VPNList]:
    """Get a list of L2VPN objects.

    Args:
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
        export_target (Union[Unset, list[str]]):
        export_target_n (Union[Unset, list[str]]):
        export_target_id (Union[Unset, list[int]]):
        export_target_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        identifier (Union[Unset, list[int]]):
        identifier_empty (Union[Unset, bool]):
        identifier_gt (Union[Unset, list[int]]):
        identifier_gte (Union[Unset, list[int]]):
        identifier_lt (Union[Unset, list[int]]):
        identifier_lte (Union[Unset, list[int]]):
        identifier_n (Union[Unset, list[int]]):
        import_target (Union[Unset, list[str]]):
        import_target_n (Union[Unset, list[str]]):
        import_target_id (Union[Unset, list[int]]):
        import_target_id_n (Union[Unset, list[int]]):
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
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedL2VPNList
    """

    return (
        await asyncio_detailed(
            client=client,
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
            export_target=export_target,
            export_target_n=export_target_n,
            export_target_id=export_target_id,
            export_target_id_n=export_target_id_n,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            identifier=identifier,
            identifier_empty=identifier_empty,
            identifier_gt=identifier_gt,
            identifier_gte=identifier_gte,
            identifier_lt=identifier_lt,
            identifier_lte=identifier_lte,
            identifier_n=identifier_n,
            import_target=import_target,
            import_target_n=import_target_n,
            import_target_id=import_target_id,
            import_target_id_n=import_target_id_n,
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
            updated_by_request=updated_by_request,
        )
    ).parsed
