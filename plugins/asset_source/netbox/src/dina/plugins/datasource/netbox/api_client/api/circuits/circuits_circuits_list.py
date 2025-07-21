import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.circuits_circuits_list_distance_unit import (
    CircuitsCircuitsListDistanceUnit,
)
from ...models.paginated_circuit_list import PaginatedCircuitList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cid: Union[Unset, list[str]] = UNSET,
    cid_empty: Union[Unset, bool] = UNSET,
    cid_ic: Union[Unset, list[str]] = UNSET,
    cid_ie: Union[Unset, list[str]] = UNSET,
    cid_iew: Union[Unset, list[str]] = UNSET,
    cid_isw: Union[Unset, list[str]] = UNSET,
    cid_n: Union[Unset, list[str]] = UNSET,
    cid_nic: Union[Unset, list[str]] = UNSET,
    cid_nie: Union[Unset, list[str]] = UNSET,
    cid_niew: Union[Unset, list[str]] = UNSET,
    cid_nisw: Union[Unset, list[str]] = UNSET,
    commit_rate: Union[Unset, list[int]] = UNSET,
    commit_rate_empty: Union[Unset, bool] = UNSET,
    commit_rate_gt: Union[Unset, list[int]] = UNSET,
    commit_rate_gte: Union[Unset, list[int]] = UNSET,
    commit_rate_lt: Union[Unset, list[int]] = UNSET,
    commit_rate_lte: Union[Unset, list[int]] = UNSET,
    commit_rate_n: Union[Unset, list[int]] = UNSET,
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
    distance: Union[Unset, list[float]] = UNSET,
    distance_empty: Union[Unset, bool] = UNSET,
    distance_gt: Union[Unset, list[float]] = UNSET,
    distance_gte: Union[Unset, list[float]] = UNSET,
    distance_lt: Union[Unset, list[float]] = UNSET,
    distance_lte: Union[Unset, list[float]] = UNSET,
    distance_n: Union[Unset, list[float]] = UNSET,
    distance_unit: Union[Unset, CircuitsCircuitsListDistanceUnit] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    install_date: Union[Unset, list[datetime.date]] = UNSET,
    install_date_empty: Union[Unset, bool] = UNSET,
    install_date_gt: Union[Unset, list[datetime.date]] = UNSET,
    install_date_gte: Union[Unset, list[datetime.date]] = UNSET,
    install_date_lt: Union[Unset, list[datetime.date]] = UNSET,
    install_date_lte: Union[Unset, list[datetime.date]] = UNSET,
    install_date_n: Union[Unset, list[datetime.date]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    provider: Union[Unset, list[str]] = UNSET,
    provider_n: Union[Unset, list[str]] = UNSET,
    provider_account: Union[Unset, list[str]] = UNSET,
    provider_account_n: Union[Unset, list[str]] = UNSET,
    provider_account_id: Union[Unset, list[int]] = UNSET,
    provider_account_id_n: Union[Unset, list[int]] = UNSET,
    provider_id: Union[Unset, list[int]] = UNSET,
    provider_id_n: Union[Unset, list[int]] = UNSET,
    provider_network_id: Union[Unset, list[int]] = UNSET,
    provider_network_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
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
    termination_a_id: Union[Unset, list[Union[None, int]]] = UNSET,
    termination_a_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    termination_date: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_empty: Union[Unset, bool] = UNSET,
    termination_date_gt: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_gte: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_lt: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_lte: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_n: Union[Unset, list[datetime.date]] = UNSET,
    termination_z_id: Union[Unset, list[Union[None, int]]] = UNSET,
    termination_z_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    type_n: Union[Unset, list[str]] = UNSET,
    type_id: Union[Unset, list[int]] = UNSET,
    type_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_cid: Union[Unset, list[str]] = UNSET
    if not isinstance(cid, Unset):
        json_cid = cid

    params["cid"] = json_cid

    params["cid__empty"] = cid_empty

    json_cid_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(cid_ic, Unset):
        json_cid_ic = cid_ic

    params["cid__ic"] = json_cid_ic

    json_cid_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(cid_ie, Unset):
        json_cid_ie = cid_ie

    params["cid__ie"] = json_cid_ie

    json_cid_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(cid_iew, Unset):
        json_cid_iew = cid_iew

    params["cid__iew"] = json_cid_iew

    json_cid_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(cid_isw, Unset):
        json_cid_isw = cid_isw

    params["cid__isw"] = json_cid_isw

    json_cid_n: Union[Unset, list[str]] = UNSET
    if not isinstance(cid_n, Unset):
        json_cid_n = cid_n

    params["cid__n"] = json_cid_n

    json_cid_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(cid_nic, Unset):
        json_cid_nic = cid_nic

    params["cid__nic"] = json_cid_nic

    json_cid_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(cid_nie, Unset):
        json_cid_nie = cid_nie

    params["cid__nie"] = json_cid_nie

    json_cid_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(cid_niew, Unset):
        json_cid_niew = cid_niew

    params["cid__niew"] = json_cid_niew

    json_cid_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(cid_nisw, Unset):
        json_cid_nisw = cid_nisw

    params["cid__nisw"] = json_cid_nisw

    json_commit_rate: Union[Unset, list[int]] = UNSET
    if not isinstance(commit_rate, Unset):
        json_commit_rate = commit_rate

    params["commit_rate"] = json_commit_rate

    params["commit_rate__empty"] = commit_rate_empty

    json_commit_rate_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(commit_rate_gt, Unset):
        json_commit_rate_gt = commit_rate_gt

    params["commit_rate__gt"] = json_commit_rate_gt

    json_commit_rate_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(commit_rate_gte, Unset):
        json_commit_rate_gte = commit_rate_gte

    params["commit_rate__gte"] = json_commit_rate_gte

    json_commit_rate_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(commit_rate_lt, Unset):
        json_commit_rate_lt = commit_rate_lt

    params["commit_rate__lt"] = json_commit_rate_lt

    json_commit_rate_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(commit_rate_lte, Unset):
        json_commit_rate_lte = commit_rate_lte

    params["commit_rate__lte"] = json_commit_rate_lte

    json_commit_rate_n: Union[Unset, list[int]] = UNSET
    if not isinstance(commit_rate_n, Unset):
        json_commit_rate_n = commit_rate_n

    params["commit_rate__n"] = json_commit_rate_n

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

    json_distance: Union[Unset, list[float]] = UNSET
    if not isinstance(distance, Unset):
        json_distance = distance

    params["distance"] = json_distance

    params["distance__empty"] = distance_empty

    json_distance_gt: Union[Unset, list[float]] = UNSET
    if not isinstance(distance_gt, Unset):
        json_distance_gt = distance_gt

    params["distance__gt"] = json_distance_gt

    json_distance_gte: Union[Unset, list[float]] = UNSET
    if not isinstance(distance_gte, Unset):
        json_distance_gte = distance_gte

    params["distance__gte"] = json_distance_gte

    json_distance_lt: Union[Unset, list[float]] = UNSET
    if not isinstance(distance_lt, Unset):
        json_distance_lt = distance_lt

    params["distance__lt"] = json_distance_lt

    json_distance_lte: Union[Unset, list[float]] = UNSET
    if not isinstance(distance_lte, Unset):
        json_distance_lte = distance_lte

    params["distance__lte"] = json_distance_lte

    json_distance_n: Union[Unset, list[float]] = UNSET
    if not isinstance(distance_n, Unset):
        json_distance_n = distance_n

    params["distance__n"] = json_distance_n

    json_distance_unit: Union[Unset, str] = UNSET
    if not isinstance(distance_unit, Unset):
        json_distance_unit = distance_unit.value

    params["distance_unit"] = json_distance_unit

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

    json_install_date: Union[Unset, list[str]] = UNSET
    if not isinstance(install_date, Unset):
        json_install_date = []
        for install_date_item_data in install_date:
            install_date_item = install_date_item_data.isoformat()
            json_install_date.append(install_date_item)

    params["install_date"] = json_install_date

    params["install_date__empty"] = install_date_empty

    json_install_date_gt: Union[Unset, list[str]] = UNSET
    if not isinstance(install_date_gt, Unset):
        json_install_date_gt = []
        for install_date_gt_item_data in install_date_gt:
            install_date_gt_item = install_date_gt_item_data.isoformat()
            json_install_date_gt.append(install_date_gt_item)

    params["install_date__gt"] = json_install_date_gt

    json_install_date_gte: Union[Unset, list[str]] = UNSET
    if not isinstance(install_date_gte, Unset):
        json_install_date_gte = []
        for install_date_gte_item_data in install_date_gte:
            install_date_gte_item = install_date_gte_item_data.isoformat()
            json_install_date_gte.append(install_date_gte_item)

    params["install_date__gte"] = json_install_date_gte

    json_install_date_lt: Union[Unset, list[str]] = UNSET
    if not isinstance(install_date_lt, Unset):
        json_install_date_lt = []
        for install_date_lt_item_data in install_date_lt:
            install_date_lt_item = install_date_lt_item_data.isoformat()
            json_install_date_lt.append(install_date_lt_item)

    params["install_date__lt"] = json_install_date_lt

    json_install_date_lte: Union[Unset, list[str]] = UNSET
    if not isinstance(install_date_lte, Unset):
        json_install_date_lte = []
        for install_date_lte_item_data in install_date_lte:
            install_date_lte_item = install_date_lte_item_data.isoformat()
            json_install_date_lte.append(install_date_lte_item)

    params["install_date__lte"] = json_install_date_lte

    json_install_date_n: Union[Unset, list[str]] = UNSET
    if not isinstance(install_date_n, Unset):
        json_install_date_n = []
        for install_date_n_item_data in install_date_n:
            install_date_n_item = install_date_n_item_data.isoformat()
            json_install_date_n.append(install_date_n_item)

    params["install_date__n"] = json_install_date_n

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

    json_location_id: Union[Unset, list[int]] = UNSET
    if not isinstance(location_id, Unset):
        json_location_id = location_id

    params["location_id"] = json_location_id

    json_location_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(location_id_n, Unset):
        json_location_id_n = location_id_n

    params["location_id__n"] = json_location_id_n

    json_modified_by_request: Union[Unset, str] = UNSET
    if not isinstance(modified_by_request, Unset):
        json_modified_by_request = str(modified_by_request)
    params["modified_by_request"] = json_modified_by_request

    params["offset"] = offset

    params["ordering"] = ordering

    json_provider: Union[Unset, list[str]] = UNSET
    if not isinstance(provider, Unset):
        json_provider = provider

    params["provider"] = json_provider

    json_provider_n: Union[Unset, list[str]] = UNSET
    if not isinstance(provider_n, Unset):
        json_provider_n = provider_n

    params["provider__n"] = json_provider_n

    json_provider_account: Union[Unset, list[str]] = UNSET
    if not isinstance(provider_account, Unset):
        json_provider_account = provider_account

    params["provider_account"] = json_provider_account

    json_provider_account_n: Union[Unset, list[str]] = UNSET
    if not isinstance(provider_account_n, Unset):
        json_provider_account_n = provider_account_n

    params["provider_account__n"] = json_provider_account_n

    json_provider_account_id: Union[Unset, list[int]] = UNSET
    if not isinstance(provider_account_id, Unset):
        json_provider_account_id = provider_account_id

    params["provider_account_id"] = json_provider_account_id

    json_provider_account_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(provider_account_id_n, Unset):
        json_provider_account_id_n = provider_account_id_n

    params["provider_account_id__n"] = json_provider_account_id_n

    json_provider_id: Union[Unset, list[int]] = UNSET
    if not isinstance(provider_id, Unset):
        json_provider_id = provider_id

    params["provider_id"] = json_provider_id

    json_provider_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(provider_id_n, Unset):
        json_provider_id_n = provider_id_n

    params["provider_id__n"] = json_provider_id_n

    json_provider_network_id: Union[Unset, list[int]] = UNSET
    if not isinstance(provider_network_id, Unset):
        json_provider_network_id = provider_network_id

    params["provider_network_id"] = json_provider_network_id

    json_provider_network_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(provider_network_id_n, Unset):
        json_provider_network_id_n = provider_network_id_n

    params["provider_network_id__n"] = json_provider_network_id_n

    params["q"] = q

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

    json_termination_a_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(termination_a_id, Unset):
        json_termination_a_id = []
        for termination_a_id_item_data in termination_a_id:
            termination_a_id_item: Union[None, int]
            termination_a_id_item = termination_a_id_item_data
            json_termination_a_id.append(termination_a_id_item)

    params["termination_a_id"] = json_termination_a_id

    json_termination_a_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(termination_a_id_n, Unset):
        json_termination_a_id_n = []
        for termination_a_id_n_item_data in termination_a_id_n:
            termination_a_id_n_item: Union[None, int]
            termination_a_id_n_item = termination_a_id_n_item_data
            json_termination_a_id_n.append(termination_a_id_n_item)

    params["termination_a_id__n"] = json_termination_a_id_n

    json_termination_date: Union[Unset, list[str]] = UNSET
    if not isinstance(termination_date, Unset):
        json_termination_date = []
        for termination_date_item_data in termination_date:
            termination_date_item = termination_date_item_data.isoformat()
            json_termination_date.append(termination_date_item)

    params["termination_date"] = json_termination_date

    params["termination_date__empty"] = termination_date_empty

    json_termination_date_gt: Union[Unset, list[str]] = UNSET
    if not isinstance(termination_date_gt, Unset):
        json_termination_date_gt = []
        for termination_date_gt_item_data in termination_date_gt:
            termination_date_gt_item = termination_date_gt_item_data.isoformat()
            json_termination_date_gt.append(termination_date_gt_item)

    params["termination_date__gt"] = json_termination_date_gt

    json_termination_date_gte: Union[Unset, list[str]] = UNSET
    if not isinstance(termination_date_gte, Unset):
        json_termination_date_gte = []
        for termination_date_gte_item_data in termination_date_gte:
            termination_date_gte_item = termination_date_gte_item_data.isoformat()
            json_termination_date_gte.append(termination_date_gte_item)

    params["termination_date__gte"] = json_termination_date_gte

    json_termination_date_lt: Union[Unset, list[str]] = UNSET
    if not isinstance(termination_date_lt, Unset):
        json_termination_date_lt = []
        for termination_date_lt_item_data in termination_date_lt:
            termination_date_lt_item = termination_date_lt_item_data.isoformat()
            json_termination_date_lt.append(termination_date_lt_item)

    params["termination_date__lt"] = json_termination_date_lt

    json_termination_date_lte: Union[Unset, list[str]] = UNSET
    if not isinstance(termination_date_lte, Unset):
        json_termination_date_lte = []
        for termination_date_lte_item_data in termination_date_lte:
            termination_date_lte_item = termination_date_lte_item_data.isoformat()
            json_termination_date_lte.append(termination_date_lte_item)

    params["termination_date__lte"] = json_termination_date_lte

    json_termination_date_n: Union[Unset, list[str]] = UNSET
    if not isinstance(termination_date_n, Unset):
        json_termination_date_n = []
        for termination_date_n_item_data in termination_date_n:
            termination_date_n_item = termination_date_n_item_data.isoformat()
            json_termination_date_n.append(termination_date_n_item)

    params["termination_date__n"] = json_termination_date_n

    json_termination_z_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(termination_z_id, Unset):
        json_termination_z_id = []
        for termination_z_id_item_data in termination_z_id:
            termination_z_id_item: Union[None, int]
            termination_z_id_item = termination_z_id_item_data
            json_termination_z_id.append(termination_z_id_item)

    params["termination_z_id"] = json_termination_z_id

    json_termination_z_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(termination_z_id_n, Unset):
        json_termination_z_id_n = []
        for termination_z_id_n_item_data in termination_z_id_n:
            termination_z_id_n_item: Union[None, int]
            termination_z_id_n_item = termination_z_id_n_item_data
            json_termination_z_id_n.append(termination_z_id_n_item)

    params["termination_z_id__n"] = json_termination_z_id_n

    json_type_: Union[Unset, list[str]] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_

    params["type"] = json_type_

    json_type_n: Union[Unset, list[str]] = UNSET
    if not isinstance(type_n, Unset):
        json_type_n = type_n

    params["type__n"] = json_type_n

    json_type_id: Union[Unset, list[int]] = UNSET
    if not isinstance(type_id, Unset):
        json_type_id = type_id

    params["type_id"] = json_type_id

    json_type_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(type_id_n, Unset):
        json_type_id_n = type_id_n

    params["type_id__n"] = json_type_id_n

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/circuits/circuits/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedCircuitList]:
    if response.status_code == 200:
        response_200 = PaginatedCircuitList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedCircuitList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cid: Union[Unset, list[str]] = UNSET,
    cid_empty: Union[Unset, bool] = UNSET,
    cid_ic: Union[Unset, list[str]] = UNSET,
    cid_ie: Union[Unset, list[str]] = UNSET,
    cid_iew: Union[Unset, list[str]] = UNSET,
    cid_isw: Union[Unset, list[str]] = UNSET,
    cid_n: Union[Unset, list[str]] = UNSET,
    cid_nic: Union[Unset, list[str]] = UNSET,
    cid_nie: Union[Unset, list[str]] = UNSET,
    cid_niew: Union[Unset, list[str]] = UNSET,
    cid_nisw: Union[Unset, list[str]] = UNSET,
    commit_rate: Union[Unset, list[int]] = UNSET,
    commit_rate_empty: Union[Unset, bool] = UNSET,
    commit_rate_gt: Union[Unset, list[int]] = UNSET,
    commit_rate_gte: Union[Unset, list[int]] = UNSET,
    commit_rate_lt: Union[Unset, list[int]] = UNSET,
    commit_rate_lte: Union[Unset, list[int]] = UNSET,
    commit_rate_n: Union[Unset, list[int]] = UNSET,
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
    distance: Union[Unset, list[float]] = UNSET,
    distance_empty: Union[Unset, bool] = UNSET,
    distance_gt: Union[Unset, list[float]] = UNSET,
    distance_gte: Union[Unset, list[float]] = UNSET,
    distance_lt: Union[Unset, list[float]] = UNSET,
    distance_lte: Union[Unset, list[float]] = UNSET,
    distance_n: Union[Unset, list[float]] = UNSET,
    distance_unit: Union[Unset, CircuitsCircuitsListDistanceUnit] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    install_date: Union[Unset, list[datetime.date]] = UNSET,
    install_date_empty: Union[Unset, bool] = UNSET,
    install_date_gt: Union[Unset, list[datetime.date]] = UNSET,
    install_date_gte: Union[Unset, list[datetime.date]] = UNSET,
    install_date_lt: Union[Unset, list[datetime.date]] = UNSET,
    install_date_lte: Union[Unset, list[datetime.date]] = UNSET,
    install_date_n: Union[Unset, list[datetime.date]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    provider: Union[Unset, list[str]] = UNSET,
    provider_n: Union[Unset, list[str]] = UNSET,
    provider_account: Union[Unset, list[str]] = UNSET,
    provider_account_n: Union[Unset, list[str]] = UNSET,
    provider_account_id: Union[Unset, list[int]] = UNSET,
    provider_account_id_n: Union[Unset, list[int]] = UNSET,
    provider_id: Union[Unset, list[int]] = UNSET,
    provider_id_n: Union[Unset, list[int]] = UNSET,
    provider_network_id: Union[Unset, list[int]] = UNSET,
    provider_network_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
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
    termination_a_id: Union[Unset, list[Union[None, int]]] = UNSET,
    termination_a_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    termination_date: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_empty: Union[Unset, bool] = UNSET,
    termination_date_gt: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_gte: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_lt: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_lte: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_n: Union[Unset, list[datetime.date]] = UNSET,
    termination_z_id: Union[Unset, list[Union[None, int]]] = UNSET,
    termination_z_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    type_n: Union[Unset, list[str]] = UNSET,
    type_id: Union[Unset, list[int]] = UNSET,
    type_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedCircuitList]:
    """Get a list of circuit objects.

    Args:
        cid (Union[Unset, list[str]]):
        cid_empty (Union[Unset, bool]):
        cid_ic (Union[Unset, list[str]]):
        cid_ie (Union[Unset, list[str]]):
        cid_iew (Union[Unset, list[str]]):
        cid_isw (Union[Unset, list[str]]):
        cid_n (Union[Unset, list[str]]):
        cid_nic (Union[Unset, list[str]]):
        cid_nie (Union[Unset, list[str]]):
        cid_niew (Union[Unset, list[str]]):
        cid_nisw (Union[Unset, list[str]]):
        commit_rate (Union[Unset, list[int]]):
        commit_rate_empty (Union[Unset, bool]):
        commit_rate_gt (Union[Unset, list[int]]):
        commit_rate_gte (Union[Unset, list[int]]):
        commit_rate_lt (Union[Unset, list[int]]):
        commit_rate_lte (Union[Unset, list[int]]):
        commit_rate_n (Union[Unset, list[int]]):
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
        distance (Union[Unset, list[float]]):
        distance_empty (Union[Unset, bool]):
        distance_gt (Union[Unset, list[float]]):
        distance_gte (Union[Unset, list[float]]):
        distance_lt (Union[Unset, list[float]]):
        distance_lte (Union[Unset, list[float]]):
        distance_n (Union[Unset, list[float]]):
        distance_unit (Union[Unset, CircuitsCircuitsListDistanceUnit]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        install_date (Union[Unset, list[datetime.date]]):
        install_date_empty (Union[Unset, bool]):
        install_date_gt (Union[Unset, list[datetime.date]]):
        install_date_gte (Union[Unset, list[datetime.date]]):
        install_date_lt (Union[Unset, list[datetime.date]]):
        install_date_lte (Union[Unset, list[datetime.date]]):
        install_date_n (Union[Unset, list[datetime.date]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        location_id (Union[Unset, list[int]]):
        location_id_n (Union[Unset, list[int]]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        provider (Union[Unset, list[str]]):
        provider_n (Union[Unset, list[str]]):
        provider_account (Union[Unset, list[str]]):
        provider_account_n (Union[Unset, list[str]]):
        provider_account_id (Union[Unset, list[int]]):
        provider_account_id_n (Union[Unset, list[int]]):
        provider_id (Union[Unset, list[int]]):
        provider_id_n (Union[Unset, list[int]]):
        provider_network_id (Union[Unset, list[int]]):
        provider_network_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
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
        termination_a_id (Union[Unset, list[Union[None, int]]]):
        termination_a_id_n (Union[Unset, list[Union[None, int]]]):
        termination_date (Union[Unset, list[datetime.date]]):
        termination_date_empty (Union[Unset, bool]):
        termination_date_gt (Union[Unset, list[datetime.date]]):
        termination_date_gte (Union[Unset, list[datetime.date]]):
        termination_date_lt (Union[Unset, list[datetime.date]]):
        termination_date_lte (Union[Unset, list[datetime.date]]):
        termination_date_n (Union[Unset, list[datetime.date]]):
        termination_z_id (Union[Unset, list[Union[None, int]]]):
        termination_z_id_n (Union[Unset, list[Union[None, int]]]):
        type_ (Union[Unset, list[str]]):
        type_n (Union[Unset, list[str]]):
        type_id (Union[Unset, list[int]]):
        type_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCircuitList]
    """

    kwargs = _get_kwargs(
        cid=cid,
        cid_empty=cid_empty,
        cid_ic=cid_ic,
        cid_ie=cid_ie,
        cid_iew=cid_iew,
        cid_isw=cid_isw,
        cid_n=cid_n,
        cid_nic=cid_nic,
        cid_nie=cid_nie,
        cid_niew=cid_niew,
        cid_nisw=cid_nisw,
        commit_rate=commit_rate,
        commit_rate_empty=commit_rate_empty,
        commit_rate_gt=commit_rate_gt,
        commit_rate_gte=commit_rate_gte,
        commit_rate_lt=commit_rate_lt,
        commit_rate_lte=commit_rate_lte,
        commit_rate_n=commit_rate_n,
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
        distance=distance,
        distance_empty=distance_empty,
        distance_gt=distance_gt,
        distance_gte=distance_gte,
        distance_lt=distance_lt,
        distance_lte=distance_lte,
        distance_n=distance_n,
        distance_unit=distance_unit,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        install_date=install_date,
        install_date_empty=install_date_empty,
        install_date_gt=install_date_gt,
        install_date_gte=install_date_gte,
        install_date_lt=install_date_lt,
        install_date_lte=install_date_lte,
        install_date_n=install_date_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        location_id=location_id,
        location_id_n=location_id_n,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        provider=provider,
        provider_n=provider_n,
        provider_account=provider_account,
        provider_account_n=provider_account_n,
        provider_account_id=provider_account_id,
        provider_account_id_n=provider_account_id_n,
        provider_id=provider_id,
        provider_id_n=provider_id_n,
        provider_network_id=provider_network_id,
        provider_network_id_n=provider_network_id_n,
        q=q,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        site=site,
        site_n=site_n,
        site_group=site_group,
        site_group_n=site_group_n,
        site_group_id=site_group_id,
        site_group_id_n=site_group_id_n,
        site_id=site_id,
        site_id_n=site_id_n,
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
        termination_a_id=termination_a_id,
        termination_a_id_n=termination_a_id_n,
        termination_date=termination_date,
        termination_date_empty=termination_date_empty,
        termination_date_gt=termination_date_gt,
        termination_date_gte=termination_date_gte,
        termination_date_lt=termination_date_lt,
        termination_date_lte=termination_date_lte,
        termination_date_n=termination_date_n,
        termination_z_id=termination_z_id,
        termination_z_id_n=termination_z_id_n,
        type_=type_,
        type_n=type_n,
        type_id=type_id,
        type_id_n=type_id_n,
        updated_by_request=updated_by_request,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cid: Union[Unset, list[str]] = UNSET,
    cid_empty: Union[Unset, bool] = UNSET,
    cid_ic: Union[Unset, list[str]] = UNSET,
    cid_ie: Union[Unset, list[str]] = UNSET,
    cid_iew: Union[Unset, list[str]] = UNSET,
    cid_isw: Union[Unset, list[str]] = UNSET,
    cid_n: Union[Unset, list[str]] = UNSET,
    cid_nic: Union[Unset, list[str]] = UNSET,
    cid_nie: Union[Unset, list[str]] = UNSET,
    cid_niew: Union[Unset, list[str]] = UNSET,
    cid_nisw: Union[Unset, list[str]] = UNSET,
    commit_rate: Union[Unset, list[int]] = UNSET,
    commit_rate_empty: Union[Unset, bool] = UNSET,
    commit_rate_gt: Union[Unset, list[int]] = UNSET,
    commit_rate_gte: Union[Unset, list[int]] = UNSET,
    commit_rate_lt: Union[Unset, list[int]] = UNSET,
    commit_rate_lte: Union[Unset, list[int]] = UNSET,
    commit_rate_n: Union[Unset, list[int]] = UNSET,
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
    distance: Union[Unset, list[float]] = UNSET,
    distance_empty: Union[Unset, bool] = UNSET,
    distance_gt: Union[Unset, list[float]] = UNSET,
    distance_gte: Union[Unset, list[float]] = UNSET,
    distance_lt: Union[Unset, list[float]] = UNSET,
    distance_lte: Union[Unset, list[float]] = UNSET,
    distance_n: Union[Unset, list[float]] = UNSET,
    distance_unit: Union[Unset, CircuitsCircuitsListDistanceUnit] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    install_date: Union[Unset, list[datetime.date]] = UNSET,
    install_date_empty: Union[Unset, bool] = UNSET,
    install_date_gt: Union[Unset, list[datetime.date]] = UNSET,
    install_date_gte: Union[Unset, list[datetime.date]] = UNSET,
    install_date_lt: Union[Unset, list[datetime.date]] = UNSET,
    install_date_lte: Union[Unset, list[datetime.date]] = UNSET,
    install_date_n: Union[Unset, list[datetime.date]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    provider: Union[Unset, list[str]] = UNSET,
    provider_n: Union[Unset, list[str]] = UNSET,
    provider_account: Union[Unset, list[str]] = UNSET,
    provider_account_n: Union[Unset, list[str]] = UNSET,
    provider_account_id: Union[Unset, list[int]] = UNSET,
    provider_account_id_n: Union[Unset, list[int]] = UNSET,
    provider_id: Union[Unset, list[int]] = UNSET,
    provider_id_n: Union[Unset, list[int]] = UNSET,
    provider_network_id: Union[Unset, list[int]] = UNSET,
    provider_network_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
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
    termination_a_id: Union[Unset, list[Union[None, int]]] = UNSET,
    termination_a_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    termination_date: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_empty: Union[Unset, bool] = UNSET,
    termination_date_gt: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_gte: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_lt: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_lte: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_n: Union[Unset, list[datetime.date]] = UNSET,
    termination_z_id: Union[Unset, list[Union[None, int]]] = UNSET,
    termination_z_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    type_n: Union[Unset, list[str]] = UNSET,
    type_id: Union[Unset, list[int]] = UNSET,
    type_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedCircuitList]:
    """Get a list of circuit objects.

    Args:
        cid (Union[Unset, list[str]]):
        cid_empty (Union[Unset, bool]):
        cid_ic (Union[Unset, list[str]]):
        cid_ie (Union[Unset, list[str]]):
        cid_iew (Union[Unset, list[str]]):
        cid_isw (Union[Unset, list[str]]):
        cid_n (Union[Unset, list[str]]):
        cid_nic (Union[Unset, list[str]]):
        cid_nie (Union[Unset, list[str]]):
        cid_niew (Union[Unset, list[str]]):
        cid_nisw (Union[Unset, list[str]]):
        commit_rate (Union[Unset, list[int]]):
        commit_rate_empty (Union[Unset, bool]):
        commit_rate_gt (Union[Unset, list[int]]):
        commit_rate_gte (Union[Unset, list[int]]):
        commit_rate_lt (Union[Unset, list[int]]):
        commit_rate_lte (Union[Unset, list[int]]):
        commit_rate_n (Union[Unset, list[int]]):
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
        distance (Union[Unset, list[float]]):
        distance_empty (Union[Unset, bool]):
        distance_gt (Union[Unset, list[float]]):
        distance_gte (Union[Unset, list[float]]):
        distance_lt (Union[Unset, list[float]]):
        distance_lte (Union[Unset, list[float]]):
        distance_n (Union[Unset, list[float]]):
        distance_unit (Union[Unset, CircuitsCircuitsListDistanceUnit]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        install_date (Union[Unset, list[datetime.date]]):
        install_date_empty (Union[Unset, bool]):
        install_date_gt (Union[Unset, list[datetime.date]]):
        install_date_gte (Union[Unset, list[datetime.date]]):
        install_date_lt (Union[Unset, list[datetime.date]]):
        install_date_lte (Union[Unset, list[datetime.date]]):
        install_date_n (Union[Unset, list[datetime.date]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        location_id (Union[Unset, list[int]]):
        location_id_n (Union[Unset, list[int]]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        provider (Union[Unset, list[str]]):
        provider_n (Union[Unset, list[str]]):
        provider_account (Union[Unset, list[str]]):
        provider_account_n (Union[Unset, list[str]]):
        provider_account_id (Union[Unset, list[int]]):
        provider_account_id_n (Union[Unset, list[int]]):
        provider_id (Union[Unset, list[int]]):
        provider_id_n (Union[Unset, list[int]]):
        provider_network_id (Union[Unset, list[int]]):
        provider_network_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
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
        termination_a_id (Union[Unset, list[Union[None, int]]]):
        termination_a_id_n (Union[Unset, list[Union[None, int]]]):
        termination_date (Union[Unset, list[datetime.date]]):
        termination_date_empty (Union[Unset, bool]):
        termination_date_gt (Union[Unset, list[datetime.date]]):
        termination_date_gte (Union[Unset, list[datetime.date]]):
        termination_date_lt (Union[Unset, list[datetime.date]]):
        termination_date_lte (Union[Unset, list[datetime.date]]):
        termination_date_n (Union[Unset, list[datetime.date]]):
        termination_z_id (Union[Unset, list[Union[None, int]]]):
        termination_z_id_n (Union[Unset, list[Union[None, int]]]):
        type_ (Union[Unset, list[str]]):
        type_n (Union[Unset, list[str]]):
        type_id (Union[Unset, list[int]]):
        type_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCircuitList
    """

    return sync_detailed(
        client=client,
        cid=cid,
        cid_empty=cid_empty,
        cid_ic=cid_ic,
        cid_ie=cid_ie,
        cid_iew=cid_iew,
        cid_isw=cid_isw,
        cid_n=cid_n,
        cid_nic=cid_nic,
        cid_nie=cid_nie,
        cid_niew=cid_niew,
        cid_nisw=cid_nisw,
        commit_rate=commit_rate,
        commit_rate_empty=commit_rate_empty,
        commit_rate_gt=commit_rate_gt,
        commit_rate_gte=commit_rate_gte,
        commit_rate_lt=commit_rate_lt,
        commit_rate_lte=commit_rate_lte,
        commit_rate_n=commit_rate_n,
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
        distance=distance,
        distance_empty=distance_empty,
        distance_gt=distance_gt,
        distance_gte=distance_gte,
        distance_lt=distance_lt,
        distance_lte=distance_lte,
        distance_n=distance_n,
        distance_unit=distance_unit,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        install_date=install_date,
        install_date_empty=install_date_empty,
        install_date_gt=install_date_gt,
        install_date_gte=install_date_gte,
        install_date_lt=install_date_lt,
        install_date_lte=install_date_lte,
        install_date_n=install_date_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        location_id=location_id,
        location_id_n=location_id_n,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        provider=provider,
        provider_n=provider_n,
        provider_account=provider_account,
        provider_account_n=provider_account_n,
        provider_account_id=provider_account_id,
        provider_account_id_n=provider_account_id_n,
        provider_id=provider_id,
        provider_id_n=provider_id_n,
        provider_network_id=provider_network_id,
        provider_network_id_n=provider_network_id_n,
        q=q,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        site=site,
        site_n=site_n,
        site_group=site_group,
        site_group_n=site_group_n,
        site_group_id=site_group_id,
        site_group_id_n=site_group_id_n,
        site_id=site_id,
        site_id_n=site_id_n,
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
        termination_a_id=termination_a_id,
        termination_a_id_n=termination_a_id_n,
        termination_date=termination_date,
        termination_date_empty=termination_date_empty,
        termination_date_gt=termination_date_gt,
        termination_date_gte=termination_date_gte,
        termination_date_lt=termination_date_lt,
        termination_date_lte=termination_date_lte,
        termination_date_n=termination_date_n,
        termination_z_id=termination_z_id,
        termination_z_id_n=termination_z_id_n,
        type_=type_,
        type_n=type_n,
        type_id=type_id,
        type_id_n=type_id_n,
        updated_by_request=updated_by_request,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cid: Union[Unset, list[str]] = UNSET,
    cid_empty: Union[Unset, bool] = UNSET,
    cid_ic: Union[Unset, list[str]] = UNSET,
    cid_ie: Union[Unset, list[str]] = UNSET,
    cid_iew: Union[Unset, list[str]] = UNSET,
    cid_isw: Union[Unset, list[str]] = UNSET,
    cid_n: Union[Unset, list[str]] = UNSET,
    cid_nic: Union[Unset, list[str]] = UNSET,
    cid_nie: Union[Unset, list[str]] = UNSET,
    cid_niew: Union[Unset, list[str]] = UNSET,
    cid_nisw: Union[Unset, list[str]] = UNSET,
    commit_rate: Union[Unset, list[int]] = UNSET,
    commit_rate_empty: Union[Unset, bool] = UNSET,
    commit_rate_gt: Union[Unset, list[int]] = UNSET,
    commit_rate_gte: Union[Unset, list[int]] = UNSET,
    commit_rate_lt: Union[Unset, list[int]] = UNSET,
    commit_rate_lte: Union[Unset, list[int]] = UNSET,
    commit_rate_n: Union[Unset, list[int]] = UNSET,
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
    distance: Union[Unset, list[float]] = UNSET,
    distance_empty: Union[Unset, bool] = UNSET,
    distance_gt: Union[Unset, list[float]] = UNSET,
    distance_gte: Union[Unset, list[float]] = UNSET,
    distance_lt: Union[Unset, list[float]] = UNSET,
    distance_lte: Union[Unset, list[float]] = UNSET,
    distance_n: Union[Unset, list[float]] = UNSET,
    distance_unit: Union[Unset, CircuitsCircuitsListDistanceUnit] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    install_date: Union[Unset, list[datetime.date]] = UNSET,
    install_date_empty: Union[Unset, bool] = UNSET,
    install_date_gt: Union[Unset, list[datetime.date]] = UNSET,
    install_date_gte: Union[Unset, list[datetime.date]] = UNSET,
    install_date_lt: Union[Unset, list[datetime.date]] = UNSET,
    install_date_lte: Union[Unset, list[datetime.date]] = UNSET,
    install_date_n: Union[Unset, list[datetime.date]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    provider: Union[Unset, list[str]] = UNSET,
    provider_n: Union[Unset, list[str]] = UNSET,
    provider_account: Union[Unset, list[str]] = UNSET,
    provider_account_n: Union[Unset, list[str]] = UNSET,
    provider_account_id: Union[Unset, list[int]] = UNSET,
    provider_account_id_n: Union[Unset, list[int]] = UNSET,
    provider_id: Union[Unset, list[int]] = UNSET,
    provider_id_n: Union[Unset, list[int]] = UNSET,
    provider_network_id: Union[Unset, list[int]] = UNSET,
    provider_network_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
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
    termination_a_id: Union[Unset, list[Union[None, int]]] = UNSET,
    termination_a_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    termination_date: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_empty: Union[Unset, bool] = UNSET,
    termination_date_gt: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_gte: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_lt: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_lte: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_n: Union[Unset, list[datetime.date]] = UNSET,
    termination_z_id: Union[Unset, list[Union[None, int]]] = UNSET,
    termination_z_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    type_n: Union[Unset, list[str]] = UNSET,
    type_id: Union[Unset, list[int]] = UNSET,
    type_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedCircuitList]:
    """Get a list of circuit objects.

    Args:
        cid (Union[Unset, list[str]]):
        cid_empty (Union[Unset, bool]):
        cid_ic (Union[Unset, list[str]]):
        cid_ie (Union[Unset, list[str]]):
        cid_iew (Union[Unset, list[str]]):
        cid_isw (Union[Unset, list[str]]):
        cid_n (Union[Unset, list[str]]):
        cid_nic (Union[Unset, list[str]]):
        cid_nie (Union[Unset, list[str]]):
        cid_niew (Union[Unset, list[str]]):
        cid_nisw (Union[Unset, list[str]]):
        commit_rate (Union[Unset, list[int]]):
        commit_rate_empty (Union[Unset, bool]):
        commit_rate_gt (Union[Unset, list[int]]):
        commit_rate_gte (Union[Unset, list[int]]):
        commit_rate_lt (Union[Unset, list[int]]):
        commit_rate_lte (Union[Unset, list[int]]):
        commit_rate_n (Union[Unset, list[int]]):
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
        distance (Union[Unset, list[float]]):
        distance_empty (Union[Unset, bool]):
        distance_gt (Union[Unset, list[float]]):
        distance_gte (Union[Unset, list[float]]):
        distance_lt (Union[Unset, list[float]]):
        distance_lte (Union[Unset, list[float]]):
        distance_n (Union[Unset, list[float]]):
        distance_unit (Union[Unset, CircuitsCircuitsListDistanceUnit]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        install_date (Union[Unset, list[datetime.date]]):
        install_date_empty (Union[Unset, bool]):
        install_date_gt (Union[Unset, list[datetime.date]]):
        install_date_gte (Union[Unset, list[datetime.date]]):
        install_date_lt (Union[Unset, list[datetime.date]]):
        install_date_lte (Union[Unset, list[datetime.date]]):
        install_date_n (Union[Unset, list[datetime.date]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        location_id (Union[Unset, list[int]]):
        location_id_n (Union[Unset, list[int]]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        provider (Union[Unset, list[str]]):
        provider_n (Union[Unset, list[str]]):
        provider_account (Union[Unset, list[str]]):
        provider_account_n (Union[Unset, list[str]]):
        provider_account_id (Union[Unset, list[int]]):
        provider_account_id_n (Union[Unset, list[int]]):
        provider_id (Union[Unset, list[int]]):
        provider_id_n (Union[Unset, list[int]]):
        provider_network_id (Union[Unset, list[int]]):
        provider_network_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
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
        termination_a_id (Union[Unset, list[Union[None, int]]]):
        termination_a_id_n (Union[Unset, list[Union[None, int]]]):
        termination_date (Union[Unset, list[datetime.date]]):
        termination_date_empty (Union[Unset, bool]):
        termination_date_gt (Union[Unset, list[datetime.date]]):
        termination_date_gte (Union[Unset, list[datetime.date]]):
        termination_date_lt (Union[Unset, list[datetime.date]]):
        termination_date_lte (Union[Unset, list[datetime.date]]):
        termination_date_n (Union[Unset, list[datetime.date]]):
        termination_z_id (Union[Unset, list[Union[None, int]]]):
        termination_z_id_n (Union[Unset, list[Union[None, int]]]):
        type_ (Union[Unset, list[str]]):
        type_n (Union[Unset, list[str]]):
        type_id (Union[Unset, list[int]]):
        type_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCircuitList]
    """

    kwargs = _get_kwargs(
        cid=cid,
        cid_empty=cid_empty,
        cid_ic=cid_ic,
        cid_ie=cid_ie,
        cid_iew=cid_iew,
        cid_isw=cid_isw,
        cid_n=cid_n,
        cid_nic=cid_nic,
        cid_nie=cid_nie,
        cid_niew=cid_niew,
        cid_nisw=cid_nisw,
        commit_rate=commit_rate,
        commit_rate_empty=commit_rate_empty,
        commit_rate_gt=commit_rate_gt,
        commit_rate_gte=commit_rate_gte,
        commit_rate_lt=commit_rate_lt,
        commit_rate_lte=commit_rate_lte,
        commit_rate_n=commit_rate_n,
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
        distance=distance,
        distance_empty=distance_empty,
        distance_gt=distance_gt,
        distance_gte=distance_gte,
        distance_lt=distance_lt,
        distance_lte=distance_lte,
        distance_n=distance_n,
        distance_unit=distance_unit,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        install_date=install_date,
        install_date_empty=install_date_empty,
        install_date_gt=install_date_gt,
        install_date_gte=install_date_gte,
        install_date_lt=install_date_lt,
        install_date_lte=install_date_lte,
        install_date_n=install_date_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        location_id=location_id,
        location_id_n=location_id_n,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        provider=provider,
        provider_n=provider_n,
        provider_account=provider_account,
        provider_account_n=provider_account_n,
        provider_account_id=provider_account_id,
        provider_account_id_n=provider_account_id_n,
        provider_id=provider_id,
        provider_id_n=provider_id_n,
        provider_network_id=provider_network_id,
        provider_network_id_n=provider_network_id_n,
        q=q,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        site=site,
        site_n=site_n,
        site_group=site_group,
        site_group_n=site_group_n,
        site_group_id=site_group_id,
        site_group_id_n=site_group_id_n,
        site_id=site_id,
        site_id_n=site_id_n,
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
        termination_a_id=termination_a_id,
        termination_a_id_n=termination_a_id_n,
        termination_date=termination_date,
        termination_date_empty=termination_date_empty,
        termination_date_gt=termination_date_gt,
        termination_date_gte=termination_date_gte,
        termination_date_lt=termination_date_lt,
        termination_date_lte=termination_date_lte,
        termination_date_n=termination_date_n,
        termination_z_id=termination_z_id,
        termination_z_id_n=termination_z_id_n,
        type_=type_,
        type_n=type_n,
        type_id=type_id,
        type_id_n=type_id_n,
        updated_by_request=updated_by_request,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cid: Union[Unset, list[str]] = UNSET,
    cid_empty: Union[Unset, bool] = UNSET,
    cid_ic: Union[Unset, list[str]] = UNSET,
    cid_ie: Union[Unset, list[str]] = UNSET,
    cid_iew: Union[Unset, list[str]] = UNSET,
    cid_isw: Union[Unset, list[str]] = UNSET,
    cid_n: Union[Unset, list[str]] = UNSET,
    cid_nic: Union[Unset, list[str]] = UNSET,
    cid_nie: Union[Unset, list[str]] = UNSET,
    cid_niew: Union[Unset, list[str]] = UNSET,
    cid_nisw: Union[Unset, list[str]] = UNSET,
    commit_rate: Union[Unset, list[int]] = UNSET,
    commit_rate_empty: Union[Unset, bool] = UNSET,
    commit_rate_gt: Union[Unset, list[int]] = UNSET,
    commit_rate_gte: Union[Unset, list[int]] = UNSET,
    commit_rate_lt: Union[Unset, list[int]] = UNSET,
    commit_rate_lte: Union[Unset, list[int]] = UNSET,
    commit_rate_n: Union[Unset, list[int]] = UNSET,
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
    distance: Union[Unset, list[float]] = UNSET,
    distance_empty: Union[Unset, bool] = UNSET,
    distance_gt: Union[Unset, list[float]] = UNSET,
    distance_gte: Union[Unset, list[float]] = UNSET,
    distance_lt: Union[Unset, list[float]] = UNSET,
    distance_lte: Union[Unset, list[float]] = UNSET,
    distance_n: Union[Unset, list[float]] = UNSET,
    distance_unit: Union[Unset, CircuitsCircuitsListDistanceUnit] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    install_date: Union[Unset, list[datetime.date]] = UNSET,
    install_date_empty: Union[Unset, bool] = UNSET,
    install_date_gt: Union[Unset, list[datetime.date]] = UNSET,
    install_date_gte: Union[Unset, list[datetime.date]] = UNSET,
    install_date_lt: Union[Unset, list[datetime.date]] = UNSET,
    install_date_lte: Union[Unset, list[datetime.date]] = UNSET,
    install_date_n: Union[Unset, list[datetime.date]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location_id: Union[Unset, list[int]] = UNSET,
    location_id_n: Union[Unset, list[int]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    provider: Union[Unset, list[str]] = UNSET,
    provider_n: Union[Unset, list[str]] = UNSET,
    provider_account: Union[Unset, list[str]] = UNSET,
    provider_account_n: Union[Unset, list[str]] = UNSET,
    provider_account_id: Union[Unset, list[int]] = UNSET,
    provider_account_id_n: Union[Unset, list[int]] = UNSET,
    provider_id: Union[Unset, list[int]] = UNSET,
    provider_id_n: Union[Unset, list[int]] = UNSET,
    provider_network_id: Union[Unset, list[int]] = UNSET,
    provider_network_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    site_id_n: Union[Unset, list[int]] = UNSET,
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
    termination_a_id: Union[Unset, list[Union[None, int]]] = UNSET,
    termination_a_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    termination_date: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_empty: Union[Unset, bool] = UNSET,
    termination_date_gt: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_gte: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_lt: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_lte: Union[Unset, list[datetime.date]] = UNSET,
    termination_date_n: Union[Unset, list[datetime.date]] = UNSET,
    termination_z_id: Union[Unset, list[Union[None, int]]] = UNSET,
    termination_z_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    type_: Union[Unset, list[str]] = UNSET,
    type_n: Union[Unset, list[str]] = UNSET,
    type_id: Union[Unset, list[int]] = UNSET,
    type_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedCircuitList]:
    """Get a list of circuit objects.

    Args:
        cid (Union[Unset, list[str]]):
        cid_empty (Union[Unset, bool]):
        cid_ic (Union[Unset, list[str]]):
        cid_ie (Union[Unset, list[str]]):
        cid_iew (Union[Unset, list[str]]):
        cid_isw (Union[Unset, list[str]]):
        cid_n (Union[Unset, list[str]]):
        cid_nic (Union[Unset, list[str]]):
        cid_nie (Union[Unset, list[str]]):
        cid_niew (Union[Unset, list[str]]):
        cid_nisw (Union[Unset, list[str]]):
        commit_rate (Union[Unset, list[int]]):
        commit_rate_empty (Union[Unset, bool]):
        commit_rate_gt (Union[Unset, list[int]]):
        commit_rate_gte (Union[Unset, list[int]]):
        commit_rate_lt (Union[Unset, list[int]]):
        commit_rate_lte (Union[Unset, list[int]]):
        commit_rate_n (Union[Unset, list[int]]):
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
        distance (Union[Unset, list[float]]):
        distance_empty (Union[Unset, bool]):
        distance_gt (Union[Unset, list[float]]):
        distance_gte (Union[Unset, list[float]]):
        distance_lt (Union[Unset, list[float]]):
        distance_lte (Union[Unset, list[float]]):
        distance_n (Union[Unset, list[float]]):
        distance_unit (Union[Unset, CircuitsCircuitsListDistanceUnit]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        install_date (Union[Unset, list[datetime.date]]):
        install_date_empty (Union[Unset, bool]):
        install_date_gt (Union[Unset, list[datetime.date]]):
        install_date_gte (Union[Unset, list[datetime.date]]):
        install_date_lt (Union[Unset, list[datetime.date]]):
        install_date_lte (Union[Unset, list[datetime.date]]):
        install_date_n (Union[Unset, list[datetime.date]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        location_id (Union[Unset, list[int]]):
        location_id_n (Union[Unset, list[int]]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        provider (Union[Unset, list[str]]):
        provider_n (Union[Unset, list[str]]):
        provider_account (Union[Unset, list[str]]):
        provider_account_n (Union[Unset, list[str]]):
        provider_account_id (Union[Unset, list[int]]):
        provider_account_id_n (Union[Unset, list[int]]):
        provider_id (Union[Unset, list[int]]):
        provider_id_n (Union[Unset, list[int]]):
        provider_network_id (Union[Unset, list[int]]):
        provider_network_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        site_id_n (Union[Unset, list[int]]):
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
        termination_a_id (Union[Unset, list[Union[None, int]]]):
        termination_a_id_n (Union[Unset, list[Union[None, int]]]):
        termination_date (Union[Unset, list[datetime.date]]):
        termination_date_empty (Union[Unset, bool]):
        termination_date_gt (Union[Unset, list[datetime.date]]):
        termination_date_gte (Union[Unset, list[datetime.date]]):
        termination_date_lt (Union[Unset, list[datetime.date]]):
        termination_date_lte (Union[Unset, list[datetime.date]]):
        termination_date_n (Union[Unset, list[datetime.date]]):
        termination_z_id (Union[Unset, list[Union[None, int]]]):
        termination_z_id_n (Union[Unset, list[Union[None, int]]]):
        type_ (Union[Unset, list[str]]):
        type_n (Union[Unset, list[str]]):
        type_id (Union[Unset, list[int]]):
        type_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCircuitList
    """

    return (
        await asyncio_detailed(
            client=client,
            cid=cid,
            cid_empty=cid_empty,
            cid_ic=cid_ic,
            cid_ie=cid_ie,
            cid_iew=cid_iew,
            cid_isw=cid_isw,
            cid_n=cid_n,
            cid_nic=cid_nic,
            cid_nie=cid_nie,
            cid_niew=cid_niew,
            cid_nisw=cid_nisw,
            commit_rate=commit_rate,
            commit_rate_empty=commit_rate_empty,
            commit_rate_gt=commit_rate_gt,
            commit_rate_gte=commit_rate_gte,
            commit_rate_lt=commit_rate_lt,
            commit_rate_lte=commit_rate_lte,
            commit_rate_n=commit_rate_n,
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
            distance=distance,
            distance_empty=distance_empty,
            distance_gt=distance_gt,
            distance_gte=distance_gte,
            distance_lt=distance_lt,
            distance_lte=distance_lte,
            distance_n=distance_n,
            distance_unit=distance_unit,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            install_date=install_date,
            install_date_empty=install_date_empty,
            install_date_gt=install_date_gt,
            install_date_gte=install_date_gte,
            install_date_lt=install_date_lt,
            install_date_lte=install_date_lte,
            install_date_n=install_date_n,
            last_updated=last_updated,
            last_updated_empty=last_updated_empty,
            last_updated_gt=last_updated_gt,
            last_updated_gte=last_updated_gte,
            last_updated_lt=last_updated_lt,
            last_updated_lte=last_updated_lte,
            last_updated_n=last_updated_n,
            limit=limit,
            location_id=location_id,
            location_id_n=location_id_n,
            modified_by_request=modified_by_request,
            offset=offset,
            ordering=ordering,
            provider=provider,
            provider_n=provider_n,
            provider_account=provider_account,
            provider_account_n=provider_account_n,
            provider_account_id=provider_account_id,
            provider_account_id_n=provider_account_id_n,
            provider_id=provider_id,
            provider_id_n=provider_id_n,
            provider_network_id=provider_network_id,
            provider_network_id_n=provider_network_id_n,
            q=q,
            region=region,
            region_n=region_n,
            region_id=region_id,
            region_id_n=region_id_n,
            site=site,
            site_n=site_n,
            site_group=site_group,
            site_group_n=site_group_n,
            site_group_id=site_group_id,
            site_group_id_n=site_group_id_n,
            site_id=site_id,
            site_id_n=site_id_n,
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
            termination_a_id=termination_a_id,
            termination_a_id_n=termination_a_id_n,
            termination_date=termination_date,
            termination_date_empty=termination_date_empty,
            termination_date_gt=termination_date_gt,
            termination_date_gte=termination_date_gte,
            termination_date_lt=termination_date_lt,
            termination_date_lte=termination_date_lte,
            termination_date_n=termination_date_n,
            termination_z_id=termination_z_id,
            termination_z_id_n=termination_z_id_n,
            type_=type_,
            type_n=type_n,
            type_id=type_id,
            type_id_n=type_id_n,
            updated_by_request=updated_by_request,
        )
    ).parsed
