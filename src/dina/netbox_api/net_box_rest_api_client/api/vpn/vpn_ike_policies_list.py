import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_ike_policy_list import PaginatedIKEPolicyList
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
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    ike_proposal: Union[Unset, list[str]] = UNSET,
    ike_proposal_n: Union[Unset, list[str]] = UNSET,
    ike_proposal_id: Union[Unset, list[int]] = UNSET,
    ike_proposal_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    mode: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_empty: Union[Unset, bool] = UNSET,
    mode_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_n: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    preshared_key: Union[Unset, str] = UNSET,
    preshared_key_ic: Union[Unset, str] = UNSET,
    preshared_key_ie: Union[Unset, str] = UNSET,
    preshared_key_iew: Union[Unset, str] = UNSET,
    preshared_key_isw: Union[Unset, str] = UNSET,
    preshared_key_n: Union[Unset, str] = UNSET,
    preshared_key_nic: Union[Unset, str] = UNSET,
    preshared_key_nie: Union[Unset, str] = UNSET,
    preshared_key_niew: Union[Unset, str] = UNSET,
    preshared_key_nisw: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    version: Union[Unset, list[int]] = UNSET,
    version_ic: Union[Unset, list[int]] = UNSET,
    version_ie: Union[Unset, list[int]] = UNSET,
    version_iew: Union[Unset, list[int]] = UNSET,
    version_isw: Union[Unset, list[int]] = UNSET,
    version_n: Union[Unset, list[int]] = UNSET,
    version_nic: Union[Unset, list[int]] = UNSET,
    version_nie: Union[Unset, list[int]] = UNSET,
    version_niew: Union[Unset, list[int]] = UNSET,
    version_nisw: Union[Unset, list[int]] = UNSET,
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

    json_ike_proposal: Union[Unset, list[str]] = UNSET
    if not isinstance(ike_proposal, Unset):
        json_ike_proposal = ike_proposal

    params["ike_proposal"] = json_ike_proposal

    json_ike_proposal_n: Union[Unset, list[str]] = UNSET
    if not isinstance(ike_proposal_n, Unset):
        json_ike_proposal_n = ike_proposal_n

    params["ike_proposal__n"] = json_ike_proposal_n

    json_ike_proposal_id: Union[Unset, list[int]] = UNSET
    if not isinstance(ike_proposal_id, Unset):
        json_ike_proposal_id = ike_proposal_id

    params["ike_proposal_id"] = json_ike_proposal_id

    json_ike_proposal_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(ike_proposal_id_n, Unset):
        json_ike_proposal_id_n = ike_proposal_id_n

    params["ike_proposal_id__n"] = json_ike_proposal_id_n

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

    json_mode: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode, Unset):
        json_mode = []
        for mode_item_data in mode:
            mode_item: Union[None, str]
            mode_item = mode_item_data
            json_mode.append(mode_item)

    params["mode"] = json_mode

    params["mode__empty"] = mode_empty

    json_mode_ic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode_ic, Unset):
        json_mode_ic = []
        for mode_ic_item_data in mode_ic:
            mode_ic_item: Union[None, str]
            mode_ic_item = mode_ic_item_data
            json_mode_ic.append(mode_ic_item)

    params["mode__ic"] = json_mode_ic

    json_mode_ie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode_ie, Unset):
        json_mode_ie = []
        for mode_ie_item_data in mode_ie:
            mode_ie_item: Union[None, str]
            mode_ie_item = mode_ie_item_data
            json_mode_ie.append(mode_ie_item)

    params["mode__ie"] = json_mode_ie

    json_mode_iew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode_iew, Unset):
        json_mode_iew = []
        for mode_iew_item_data in mode_iew:
            mode_iew_item: Union[None, str]
            mode_iew_item = mode_iew_item_data
            json_mode_iew.append(mode_iew_item)

    params["mode__iew"] = json_mode_iew

    json_mode_isw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode_isw, Unset):
        json_mode_isw = []
        for mode_isw_item_data in mode_isw:
            mode_isw_item: Union[None, str]
            mode_isw_item = mode_isw_item_data
            json_mode_isw.append(mode_isw_item)

    params["mode__isw"] = json_mode_isw

    json_mode_n: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode_n, Unset):
        json_mode_n = []
        for mode_n_item_data in mode_n:
            mode_n_item: Union[None, str]
            mode_n_item = mode_n_item_data
            json_mode_n.append(mode_n_item)

    params["mode__n"] = json_mode_n

    json_mode_nic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode_nic, Unset):
        json_mode_nic = []
        for mode_nic_item_data in mode_nic:
            mode_nic_item: Union[None, str]
            mode_nic_item = mode_nic_item_data
            json_mode_nic.append(mode_nic_item)

    params["mode__nic"] = json_mode_nic

    json_mode_nie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode_nie, Unset):
        json_mode_nie = []
        for mode_nie_item_data in mode_nie:
            mode_nie_item: Union[None, str]
            mode_nie_item = mode_nie_item_data
            json_mode_nie.append(mode_nie_item)

    params["mode__nie"] = json_mode_nie

    json_mode_niew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode_niew, Unset):
        json_mode_niew = []
        for mode_niew_item_data in mode_niew:
            mode_niew_item: Union[None, str]
            mode_niew_item = mode_niew_item_data
            json_mode_niew.append(mode_niew_item)

    params["mode__niew"] = json_mode_niew

    json_mode_nisw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(mode_nisw, Unset):
        json_mode_nisw = []
        for mode_nisw_item_data in mode_nisw:
            mode_nisw_item: Union[None, str]
            mode_nisw_item = mode_nisw_item_data
            json_mode_nisw.append(mode_nisw_item)

    params["mode__nisw"] = json_mode_nisw

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

    params["preshared_key"] = preshared_key

    params["preshared_key__ic"] = preshared_key_ic

    params["preshared_key__ie"] = preshared_key_ie

    params["preshared_key__iew"] = preshared_key_iew

    params["preshared_key__isw"] = preshared_key_isw

    params["preshared_key__n"] = preshared_key_n

    params["preshared_key__nic"] = preshared_key_nic

    params["preshared_key__nie"] = preshared_key_nie

    params["preshared_key__niew"] = preshared_key_niew

    params["preshared_key__nisw"] = preshared_key_nisw

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

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    json_version: Union[Unset, list[int]] = UNSET
    if not isinstance(version, Unset):
        json_version = version

    params["version"] = json_version

    json_version_ic: Union[Unset, list[int]] = UNSET
    if not isinstance(version_ic, Unset):
        json_version_ic = version_ic

    params["version__ic"] = json_version_ic

    json_version_ie: Union[Unset, list[int]] = UNSET
    if not isinstance(version_ie, Unset):
        json_version_ie = version_ie

    params["version__ie"] = json_version_ie

    json_version_iew: Union[Unset, list[int]] = UNSET
    if not isinstance(version_iew, Unset):
        json_version_iew = version_iew

    params["version__iew"] = json_version_iew

    json_version_isw: Union[Unset, list[int]] = UNSET
    if not isinstance(version_isw, Unset):
        json_version_isw = version_isw

    params["version__isw"] = json_version_isw

    json_version_n: Union[Unset, list[int]] = UNSET
    if not isinstance(version_n, Unset):
        json_version_n = version_n

    params["version__n"] = json_version_n

    json_version_nic: Union[Unset, list[int]] = UNSET
    if not isinstance(version_nic, Unset):
        json_version_nic = version_nic

    params["version__nic"] = json_version_nic

    json_version_nie: Union[Unset, list[int]] = UNSET
    if not isinstance(version_nie, Unset):
        json_version_nie = version_nie

    params["version__nie"] = json_version_nie

    json_version_niew: Union[Unset, list[int]] = UNSET
    if not isinstance(version_niew, Unset):
        json_version_niew = version_niew

    params["version__niew"] = json_version_niew

    json_version_nisw: Union[Unset, list[int]] = UNSET
    if not isinstance(version_nisw, Unset):
        json_version_nisw = version_nisw

    params["version__nisw"] = json_version_nisw

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/vpn/ike-policies/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedIKEPolicyList]:
    if response.status_code == 200:
        response_200 = PaginatedIKEPolicyList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedIKEPolicyList]:
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
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    ike_proposal: Union[Unset, list[str]] = UNSET,
    ike_proposal_n: Union[Unset, list[str]] = UNSET,
    ike_proposal_id: Union[Unset, list[int]] = UNSET,
    ike_proposal_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    mode: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_empty: Union[Unset, bool] = UNSET,
    mode_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_n: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    preshared_key: Union[Unset, str] = UNSET,
    preshared_key_ic: Union[Unset, str] = UNSET,
    preshared_key_ie: Union[Unset, str] = UNSET,
    preshared_key_iew: Union[Unset, str] = UNSET,
    preshared_key_isw: Union[Unset, str] = UNSET,
    preshared_key_n: Union[Unset, str] = UNSET,
    preshared_key_nic: Union[Unset, str] = UNSET,
    preshared_key_nie: Union[Unset, str] = UNSET,
    preshared_key_niew: Union[Unset, str] = UNSET,
    preshared_key_nisw: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    version: Union[Unset, list[int]] = UNSET,
    version_ic: Union[Unset, list[int]] = UNSET,
    version_ie: Union[Unset, list[int]] = UNSET,
    version_iew: Union[Unset, list[int]] = UNSET,
    version_isw: Union[Unset, list[int]] = UNSET,
    version_n: Union[Unset, list[int]] = UNSET,
    version_nic: Union[Unset, list[int]] = UNSET,
    version_nie: Union[Unset, list[int]] = UNSET,
    version_niew: Union[Unset, list[int]] = UNSET,
    version_nisw: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedIKEPolicyList]:
    """Get a list of IKE policy objects.

    Args:
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
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        ike_proposal (Union[Unset, list[str]]):
        ike_proposal_n (Union[Unset, list[str]]):
        ike_proposal_id (Union[Unset, list[int]]):
        ike_proposal_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        mode (Union[Unset, list[Union[None, str]]]):
        mode_empty (Union[Unset, bool]):
        mode_ic (Union[Unset, list[Union[None, str]]]):
        mode_ie (Union[Unset, list[Union[None, str]]]):
        mode_iew (Union[Unset, list[Union[None, str]]]):
        mode_isw (Union[Unset, list[Union[None, str]]]):
        mode_n (Union[Unset, list[Union[None, str]]]):
        mode_nic (Union[Unset, list[Union[None, str]]]):
        mode_nie (Union[Unset, list[Union[None, str]]]):
        mode_niew (Union[Unset, list[Union[None, str]]]):
        mode_nisw (Union[Unset, list[Union[None, str]]]):
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
        preshared_key (Union[Unset, str]):
        preshared_key_ic (Union[Unset, str]):
        preshared_key_ie (Union[Unset, str]):
        preshared_key_iew (Union[Unset, str]):
        preshared_key_isw (Union[Unset, str]):
        preshared_key_n (Union[Unset, str]):
        preshared_key_nic (Union[Unset, str]):
        preshared_key_nie (Union[Unset, str]):
        preshared_key_niew (Union[Unset, str]):
        preshared_key_nisw (Union[Unset, str]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        version (Union[Unset, list[int]]):
        version_ic (Union[Unset, list[int]]):
        version_ie (Union[Unset, list[int]]):
        version_iew (Union[Unset, list[int]]):
        version_isw (Union[Unset, list[int]]):
        version_n (Union[Unset, list[int]]):
        version_nic (Union[Unset, list[int]]):
        version_nie (Union[Unset, list[int]]):
        version_niew (Union[Unset, list[int]]):
        version_nisw (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedIKEPolicyList]
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
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        ike_proposal=ike_proposal,
        ike_proposal_n=ike_proposal_n,
        ike_proposal_id=ike_proposal_id,
        ike_proposal_id_n=ike_proposal_id_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        mode=mode,
        mode_empty=mode_empty,
        mode_ic=mode_ic,
        mode_ie=mode_ie,
        mode_iew=mode_iew,
        mode_isw=mode_isw,
        mode_n=mode_n,
        mode_nic=mode_nic,
        mode_nie=mode_nie,
        mode_niew=mode_niew,
        mode_nisw=mode_nisw,
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
        preshared_key=preshared_key,
        preshared_key_ic=preshared_key_ic,
        preshared_key_ie=preshared_key_ie,
        preshared_key_iew=preshared_key_iew,
        preshared_key_isw=preshared_key_isw,
        preshared_key_n=preshared_key_n,
        preshared_key_nic=preshared_key_nic,
        preshared_key_nie=preshared_key_nie,
        preshared_key_niew=preshared_key_niew,
        preshared_key_nisw=preshared_key_nisw,
        q=q,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
        version=version,
        version_ic=version_ic,
        version_ie=version_ie,
        version_iew=version_iew,
        version_isw=version_isw,
        version_n=version_n,
        version_nic=version_nic,
        version_nie=version_nie,
        version_niew=version_niew,
        version_nisw=version_nisw,
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
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    ike_proposal: Union[Unset, list[str]] = UNSET,
    ike_proposal_n: Union[Unset, list[str]] = UNSET,
    ike_proposal_id: Union[Unset, list[int]] = UNSET,
    ike_proposal_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    mode: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_empty: Union[Unset, bool] = UNSET,
    mode_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_n: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    preshared_key: Union[Unset, str] = UNSET,
    preshared_key_ic: Union[Unset, str] = UNSET,
    preshared_key_ie: Union[Unset, str] = UNSET,
    preshared_key_iew: Union[Unset, str] = UNSET,
    preshared_key_isw: Union[Unset, str] = UNSET,
    preshared_key_n: Union[Unset, str] = UNSET,
    preshared_key_nic: Union[Unset, str] = UNSET,
    preshared_key_nie: Union[Unset, str] = UNSET,
    preshared_key_niew: Union[Unset, str] = UNSET,
    preshared_key_nisw: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    version: Union[Unset, list[int]] = UNSET,
    version_ic: Union[Unset, list[int]] = UNSET,
    version_ie: Union[Unset, list[int]] = UNSET,
    version_iew: Union[Unset, list[int]] = UNSET,
    version_isw: Union[Unset, list[int]] = UNSET,
    version_n: Union[Unset, list[int]] = UNSET,
    version_nic: Union[Unset, list[int]] = UNSET,
    version_nie: Union[Unset, list[int]] = UNSET,
    version_niew: Union[Unset, list[int]] = UNSET,
    version_nisw: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedIKEPolicyList]:
    """Get a list of IKE policy objects.

    Args:
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
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        ike_proposal (Union[Unset, list[str]]):
        ike_proposal_n (Union[Unset, list[str]]):
        ike_proposal_id (Union[Unset, list[int]]):
        ike_proposal_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        mode (Union[Unset, list[Union[None, str]]]):
        mode_empty (Union[Unset, bool]):
        mode_ic (Union[Unset, list[Union[None, str]]]):
        mode_ie (Union[Unset, list[Union[None, str]]]):
        mode_iew (Union[Unset, list[Union[None, str]]]):
        mode_isw (Union[Unset, list[Union[None, str]]]):
        mode_n (Union[Unset, list[Union[None, str]]]):
        mode_nic (Union[Unset, list[Union[None, str]]]):
        mode_nie (Union[Unset, list[Union[None, str]]]):
        mode_niew (Union[Unset, list[Union[None, str]]]):
        mode_nisw (Union[Unset, list[Union[None, str]]]):
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
        preshared_key (Union[Unset, str]):
        preshared_key_ic (Union[Unset, str]):
        preshared_key_ie (Union[Unset, str]):
        preshared_key_iew (Union[Unset, str]):
        preshared_key_isw (Union[Unset, str]):
        preshared_key_n (Union[Unset, str]):
        preshared_key_nic (Union[Unset, str]):
        preshared_key_nie (Union[Unset, str]):
        preshared_key_niew (Union[Unset, str]):
        preshared_key_nisw (Union[Unset, str]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        version (Union[Unset, list[int]]):
        version_ic (Union[Unset, list[int]]):
        version_ie (Union[Unset, list[int]]):
        version_iew (Union[Unset, list[int]]):
        version_isw (Union[Unset, list[int]]):
        version_n (Union[Unset, list[int]]):
        version_nic (Union[Unset, list[int]]):
        version_nie (Union[Unset, list[int]]):
        version_niew (Union[Unset, list[int]]):
        version_nisw (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedIKEPolicyList
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
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        ike_proposal=ike_proposal,
        ike_proposal_n=ike_proposal_n,
        ike_proposal_id=ike_proposal_id,
        ike_proposal_id_n=ike_proposal_id_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        mode=mode,
        mode_empty=mode_empty,
        mode_ic=mode_ic,
        mode_ie=mode_ie,
        mode_iew=mode_iew,
        mode_isw=mode_isw,
        mode_n=mode_n,
        mode_nic=mode_nic,
        mode_nie=mode_nie,
        mode_niew=mode_niew,
        mode_nisw=mode_nisw,
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
        preshared_key=preshared_key,
        preshared_key_ic=preshared_key_ic,
        preshared_key_ie=preshared_key_ie,
        preshared_key_iew=preshared_key_iew,
        preshared_key_isw=preshared_key_isw,
        preshared_key_n=preshared_key_n,
        preshared_key_nic=preshared_key_nic,
        preshared_key_nie=preshared_key_nie,
        preshared_key_niew=preshared_key_niew,
        preshared_key_nisw=preshared_key_nisw,
        q=q,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
        version=version,
        version_ic=version_ic,
        version_ie=version_ie,
        version_iew=version_iew,
        version_isw=version_isw,
        version_n=version_n,
        version_nic=version_nic,
        version_nie=version_nie,
        version_niew=version_niew,
        version_nisw=version_nisw,
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
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    ike_proposal: Union[Unset, list[str]] = UNSET,
    ike_proposal_n: Union[Unset, list[str]] = UNSET,
    ike_proposal_id: Union[Unset, list[int]] = UNSET,
    ike_proposal_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    mode: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_empty: Union[Unset, bool] = UNSET,
    mode_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_n: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    preshared_key: Union[Unset, str] = UNSET,
    preshared_key_ic: Union[Unset, str] = UNSET,
    preshared_key_ie: Union[Unset, str] = UNSET,
    preshared_key_iew: Union[Unset, str] = UNSET,
    preshared_key_isw: Union[Unset, str] = UNSET,
    preshared_key_n: Union[Unset, str] = UNSET,
    preshared_key_nic: Union[Unset, str] = UNSET,
    preshared_key_nie: Union[Unset, str] = UNSET,
    preshared_key_niew: Union[Unset, str] = UNSET,
    preshared_key_nisw: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    version: Union[Unset, list[int]] = UNSET,
    version_ic: Union[Unset, list[int]] = UNSET,
    version_ie: Union[Unset, list[int]] = UNSET,
    version_iew: Union[Unset, list[int]] = UNSET,
    version_isw: Union[Unset, list[int]] = UNSET,
    version_n: Union[Unset, list[int]] = UNSET,
    version_nic: Union[Unset, list[int]] = UNSET,
    version_nie: Union[Unset, list[int]] = UNSET,
    version_niew: Union[Unset, list[int]] = UNSET,
    version_nisw: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedIKEPolicyList]:
    """Get a list of IKE policy objects.

    Args:
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
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        ike_proposal (Union[Unset, list[str]]):
        ike_proposal_n (Union[Unset, list[str]]):
        ike_proposal_id (Union[Unset, list[int]]):
        ike_proposal_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        mode (Union[Unset, list[Union[None, str]]]):
        mode_empty (Union[Unset, bool]):
        mode_ic (Union[Unset, list[Union[None, str]]]):
        mode_ie (Union[Unset, list[Union[None, str]]]):
        mode_iew (Union[Unset, list[Union[None, str]]]):
        mode_isw (Union[Unset, list[Union[None, str]]]):
        mode_n (Union[Unset, list[Union[None, str]]]):
        mode_nic (Union[Unset, list[Union[None, str]]]):
        mode_nie (Union[Unset, list[Union[None, str]]]):
        mode_niew (Union[Unset, list[Union[None, str]]]):
        mode_nisw (Union[Unset, list[Union[None, str]]]):
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
        preshared_key (Union[Unset, str]):
        preshared_key_ic (Union[Unset, str]):
        preshared_key_ie (Union[Unset, str]):
        preshared_key_iew (Union[Unset, str]):
        preshared_key_isw (Union[Unset, str]):
        preshared_key_n (Union[Unset, str]):
        preshared_key_nic (Union[Unset, str]):
        preshared_key_nie (Union[Unset, str]):
        preshared_key_niew (Union[Unset, str]):
        preshared_key_nisw (Union[Unset, str]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        version (Union[Unset, list[int]]):
        version_ic (Union[Unset, list[int]]):
        version_ie (Union[Unset, list[int]]):
        version_iew (Union[Unset, list[int]]):
        version_isw (Union[Unset, list[int]]):
        version_n (Union[Unset, list[int]]):
        version_nic (Union[Unset, list[int]]):
        version_nie (Union[Unset, list[int]]):
        version_niew (Union[Unset, list[int]]):
        version_nisw (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedIKEPolicyList]
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
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        ike_proposal=ike_proposal,
        ike_proposal_n=ike_proposal_n,
        ike_proposal_id=ike_proposal_id,
        ike_proposal_id_n=ike_proposal_id_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        mode=mode,
        mode_empty=mode_empty,
        mode_ic=mode_ic,
        mode_ie=mode_ie,
        mode_iew=mode_iew,
        mode_isw=mode_isw,
        mode_n=mode_n,
        mode_nic=mode_nic,
        mode_nie=mode_nie,
        mode_niew=mode_niew,
        mode_nisw=mode_nisw,
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
        preshared_key=preshared_key,
        preshared_key_ic=preshared_key_ic,
        preshared_key_ie=preshared_key_ie,
        preshared_key_iew=preshared_key_iew,
        preshared_key_isw=preshared_key_isw,
        preshared_key_n=preshared_key_n,
        preshared_key_nic=preshared_key_nic,
        preshared_key_nie=preshared_key_nie,
        preshared_key_niew=preshared_key_niew,
        preshared_key_nisw=preshared_key_nisw,
        q=q,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
        version=version,
        version_ic=version_ic,
        version_ie=version_ie,
        version_iew=version_iew,
        version_isw=version_isw,
        version_n=version_n,
        version_nic=version_nic,
        version_nie=version_nie,
        version_niew=version_niew,
        version_nisw=version_nisw,
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
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    ike_proposal: Union[Unset, list[str]] = UNSET,
    ike_proposal_n: Union[Unset, list[str]] = UNSET,
    ike_proposal_id: Union[Unset, list[int]] = UNSET,
    ike_proposal_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    mode: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_empty: Union[Unset, bool] = UNSET,
    mode_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_n: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    mode_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    preshared_key: Union[Unset, str] = UNSET,
    preshared_key_ic: Union[Unset, str] = UNSET,
    preshared_key_ie: Union[Unset, str] = UNSET,
    preshared_key_iew: Union[Unset, str] = UNSET,
    preshared_key_isw: Union[Unset, str] = UNSET,
    preshared_key_n: Union[Unset, str] = UNSET,
    preshared_key_nic: Union[Unset, str] = UNSET,
    preshared_key_nie: Union[Unset, str] = UNSET,
    preshared_key_niew: Union[Unset, str] = UNSET,
    preshared_key_nisw: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    version: Union[Unset, list[int]] = UNSET,
    version_ic: Union[Unset, list[int]] = UNSET,
    version_ie: Union[Unset, list[int]] = UNSET,
    version_iew: Union[Unset, list[int]] = UNSET,
    version_isw: Union[Unset, list[int]] = UNSET,
    version_n: Union[Unset, list[int]] = UNSET,
    version_nic: Union[Unset, list[int]] = UNSET,
    version_nie: Union[Unset, list[int]] = UNSET,
    version_niew: Union[Unset, list[int]] = UNSET,
    version_nisw: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedIKEPolicyList]:
    """Get a list of IKE policy objects.

    Args:
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
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        ike_proposal (Union[Unset, list[str]]):
        ike_proposal_n (Union[Unset, list[str]]):
        ike_proposal_id (Union[Unset, list[int]]):
        ike_proposal_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        mode (Union[Unset, list[Union[None, str]]]):
        mode_empty (Union[Unset, bool]):
        mode_ic (Union[Unset, list[Union[None, str]]]):
        mode_ie (Union[Unset, list[Union[None, str]]]):
        mode_iew (Union[Unset, list[Union[None, str]]]):
        mode_isw (Union[Unset, list[Union[None, str]]]):
        mode_n (Union[Unset, list[Union[None, str]]]):
        mode_nic (Union[Unset, list[Union[None, str]]]):
        mode_nie (Union[Unset, list[Union[None, str]]]):
        mode_niew (Union[Unset, list[Union[None, str]]]):
        mode_nisw (Union[Unset, list[Union[None, str]]]):
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
        preshared_key (Union[Unset, str]):
        preshared_key_ic (Union[Unset, str]):
        preshared_key_ie (Union[Unset, str]):
        preshared_key_iew (Union[Unset, str]):
        preshared_key_isw (Union[Unset, str]):
        preshared_key_n (Union[Unset, str]):
        preshared_key_nic (Union[Unset, str]):
        preshared_key_nie (Union[Unset, str]):
        preshared_key_niew (Union[Unset, str]):
        preshared_key_nisw (Union[Unset, str]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        version (Union[Unset, list[int]]):
        version_ic (Union[Unset, list[int]]):
        version_ie (Union[Unset, list[int]]):
        version_iew (Union[Unset, list[int]]):
        version_isw (Union[Unset, list[int]]):
        version_n (Union[Unset, list[int]]):
        version_nic (Union[Unset, list[int]]):
        version_nie (Union[Unset, list[int]]):
        version_niew (Union[Unset, list[int]]):
        version_nisw (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedIKEPolicyList
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
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            ike_proposal=ike_proposal,
            ike_proposal_n=ike_proposal_n,
            ike_proposal_id=ike_proposal_id,
            ike_proposal_id_n=ike_proposal_id_n,
            last_updated=last_updated,
            last_updated_empty=last_updated_empty,
            last_updated_gt=last_updated_gt,
            last_updated_gte=last_updated_gte,
            last_updated_lt=last_updated_lt,
            last_updated_lte=last_updated_lte,
            last_updated_n=last_updated_n,
            limit=limit,
            mode=mode,
            mode_empty=mode_empty,
            mode_ic=mode_ic,
            mode_ie=mode_ie,
            mode_iew=mode_iew,
            mode_isw=mode_isw,
            mode_n=mode_n,
            mode_nic=mode_nic,
            mode_nie=mode_nie,
            mode_niew=mode_niew,
            mode_nisw=mode_nisw,
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
            preshared_key=preshared_key,
            preshared_key_ic=preshared_key_ic,
            preshared_key_ie=preshared_key_ie,
            preshared_key_iew=preshared_key_iew,
            preshared_key_isw=preshared_key_isw,
            preshared_key_n=preshared_key_n,
            preshared_key_nic=preshared_key_nic,
            preshared_key_nie=preshared_key_nie,
            preshared_key_niew=preshared_key_niew,
            preshared_key_nisw=preshared_key_nisw,
            q=q,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
            updated_by_request=updated_by_request,
            version=version,
            version_ic=version_ic,
            version_ie=version_ie,
            version_iew=version_iew,
            version_isw=version_isw,
            version_n=version_n,
            version_nic=version_nic,
            version_nie=version_nie,
            version_niew=version_niew,
            version_nisw=version_nisw,
        )
    ).parsed
