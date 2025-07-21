import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_ip_sec_proposal_list import PaginatedIPSecProposalList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    authentication_algorithm: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_empty: Union[Unset, bool] = UNSET,
    authentication_algorithm_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_n: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    encryption_algorithm: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_empty: Union[Unset, bool] = UNSET,
    encryption_algorithm_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_n: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    ipsec_policy: Union[Unset, list[str]] = UNSET,
    ipsec_policy_n: Union[Unset, list[str]] = UNSET,
    ipsec_policy_id: Union[Unset, list[int]] = UNSET,
    ipsec_policy_id_n: Union[Unset, list[int]] = UNSET,
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
    sa_lifetime_data: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_empty: Union[Unset, bool] = UNSET,
    sa_lifetime_data_gt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_gte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_lt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_lte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_n: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_empty: Union[Unset, bool] = UNSET,
    sa_lifetime_seconds_gt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_gte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_lt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_lte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_authentication_algorithm: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(authentication_algorithm, Unset):
        json_authentication_algorithm = []
        for authentication_algorithm_item_data in authentication_algorithm:
            authentication_algorithm_item: Union[None, str]
            authentication_algorithm_item = authentication_algorithm_item_data
            json_authentication_algorithm.append(authentication_algorithm_item)

    params["authentication_algorithm"] = json_authentication_algorithm

    params["authentication_algorithm__empty"] = authentication_algorithm_empty

    json_authentication_algorithm_ic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(authentication_algorithm_ic, Unset):
        json_authentication_algorithm_ic = []
        for authentication_algorithm_ic_item_data in authentication_algorithm_ic:
            authentication_algorithm_ic_item: Union[None, str]
            authentication_algorithm_ic_item = authentication_algorithm_ic_item_data
            json_authentication_algorithm_ic.append(authentication_algorithm_ic_item)

    params["authentication_algorithm__ic"] = json_authentication_algorithm_ic

    json_authentication_algorithm_ie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(authentication_algorithm_ie, Unset):
        json_authentication_algorithm_ie = []
        for authentication_algorithm_ie_item_data in authentication_algorithm_ie:
            authentication_algorithm_ie_item: Union[None, str]
            authentication_algorithm_ie_item = authentication_algorithm_ie_item_data
            json_authentication_algorithm_ie.append(authentication_algorithm_ie_item)

    params["authentication_algorithm__ie"] = json_authentication_algorithm_ie

    json_authentication_algorithm_iew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(authentication_algorithm_iew, Unset):
        json_authentication_algorithm_iew = []
        for authentication_algorithm_iew_item_data in authentication_algorithm_iew:
            authentication_algorithm_iew_item: Union[None, str]
            authentication_algorithm_iew_item = authentication_algorithm_iew_item_data
            json_authentication_algorithm_iew.append(authentication_algorithm_iew_item)

    params["authentication_algorithm__iew"] = json_authentication_algorithm_iew

    json_authentication_algorithm_isw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(authentication_algorithm_isw, Unset):
        json_authentication_algorithm_isw = []
        for authentication_algorithm_isw_item_data in authentication_algorithm_isw:
            authentication_algorithm_isw_item: Union[None, str]
            authentication_algorithm_isw_item = authentication_algorithm_isw_item_data
            json_authentication_algorithm_isw.append(authentication_algorithm_isw_item)

    params["authentication_algorithm__isw"] = json_authentication_algorithm_isw

    json_authentication_algorithm_n: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(authentication_algorithm_n, Unset):
        json_authentication_algorithm_n = []
        for authentication_algorithm_n_item_data in authentication_algorithm_n:
            authentication_algorithm_n_item: Union[None, str]
            authentication_algorithm_n_item = authentication_algorithm_n_item_data
            json_authentication_algorithm_n.append(authentication_algorithm_n_item)

    params["authentication_algorithm__n"] = json_authentication_algorithm_n

    json_authentication_algorithm_nic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(authentication_algorithm_nic, Unset):
        json_authentication_algorithm_nic = []
        for authentication_algorithm_nic_item_data in authentication_algorithm_nic:
            authentication_algorithm_nic_item: Union[None, str]
            authentication_algorithm_nic_item = authentication_algorithm_nic_item_data
            json_authentication_algorithm_nic.append(authentication_algorithm_nic_item)

    params["authentication_algorithm__nic"] = json_authentication_algorithm_nic

    json_authentication_algorithm_nie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(authentication_algorithm_nie, Unset):
        json_authentication_algorithm_nie = []
        for authentication_algorithm_nie_item_data in authentication_algorithm_nie:
            authentication_algorithm_nie_item: Union[None, str]
            authentication_algorithm_nie_item = authentication_algorithm_nie_item_data
            json_authentication_algorithm_nie.append(authentication_algorithm_nie_item)

    params["authentication_algorithm__nie"] = json_authentication_algorithm_nie

    json_authentication_algorithm_niew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(authentication_algorithm_niew, Unset):
        json_authentication_algorithm_niew = []
        for authentication_algorithm_niew_item_data in authentication_algorithm_niew:
            authentication_algorithm_niew_item: Union[None, str]
            authentication_algorithm_niew_item = authentication_algorithm_niew_item_data
            json_authentication_algorithm_niew.append(
                authentication_algorithm_niew_item
            )

    params["authentication_algorithm__niew"] = json_authentication_algorithm_niew

    json_authentication_algorithm_nisw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(authentication_algorithm_nisw, Unset):
        json_authentication_algorithm_nisw = []
        for authentication_algorithm_nisw_item_data in authentication_algorithm_nisw:
            authentication_algorithm_nisw_item: Union[None, str]
            authentication_algorithm_nisw_item = authentication_algorithm_nisw_item_data
            json_authentication_algorithm_nisw.append(
                authentication_algorithm_nisw_item
            )

    params["authentication_algorithm__nisw"] = json_authentication_algorithm_nisw

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

    json_encryption_algorithm: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(encryption_algorithm, Unset):
        json_encryption_algorithm = []
        for encryption_algorithm_item_data in encryption_algorithm:
            encryption_algorithm_item: Union[None, str]
            encryption_algorithm_item = encryption_algorithm_item_data
            json_encryption_algorithm.append(encryption_algorithm_item)

    params["encryption_algorithm"] = json_encryption_algorithm

    params["encryption_algorithm__empty"] = encryption_algorithm_empty

    json_encryption_algorithm_ic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(encryption_algorithm_ic, Unset):
        json_encryption_algorithm_ic = []
        for encryption_algorithm_ic_item_data in encryption_algorithm_ic:
            encryption_algorithm_ic_item: Union[None, str]
            encryption_algorithm_ic_item = encryption_algorithm_ic_item_data
            json_encryption_algorithm_ic.append(encryption_algorithm_ic_item)

    params["encryption_algorithm__ic"] = json_encryption_algorithm_ic

    json_encryption_algorithm_ie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(encryption_algorithm_ie, Unset):
        json_encryption_algorithm_ie = []
        for encryption_algorithm_ie_item_data in encryption_algorithm_ie:
            encryption_algorithm_ie_item: Union[None, str]
            encryption_algorithm_ie_item = encryption_algorithm_ie_item_data
            json_encryption_algorithm_ie.append(encryption_algorithm_ie_item)

    params["encryption_algorithm__ie"] = json_encryption_algorithm_ie

    json_encryption_algorithm_iew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(encryption_algorithm_iew, Unset):
        json_encryption_algorithm_iew = []
        for encryption_algorithm_iew_item_data in encryption_algorithm_iew:
            encryption_algorithm_iew_item: Union[None, str]
            encryption_algorithm_iew_item = encryption_algorithm_iew_item_data
            json_encryption_algorithm_iew.append(encryption_algorithm_iew_item)

    params["encryption_algorithm__iew"] = json_encryption_algorithm_iew

    json_encryption_algorithm_isw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(encryption_algorithm_isw, Unset):
        json_encryption_algorithm_isw = []
        for encryption_algorithm_isw_item_data in encryption_algorithm_isw:
            encryption_algorithm_isw_item: Union[None, str]
            encryption_algorithm_isw_item = encryption_algorithm_isw_item_data
            json_encryption_algorithm_isw.append(encryption_algorithm_isw_item)

    params["encryption_algorithm__isw"] = json_encryption_algorithm_isw

    json_encryption_algorithm_n: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(encryption_algorithm_n, Unset):
        json_encryption_algorithm_n = []
        for encryption_algorithm_n_item_data in encryption_algorithm_n:
            encryption_algorithm_n_item: Union[None, str]
            encryption_algorithm_n_item = encryption_algorithm_n_item_data
            json_encryption_algorithm_n.append(encryption_algorithm_n_item)

    params["encryption_algorithm__n"] = json_encryption_algorithm_n

    json_encryption_algorithm_nic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(encryption_algorithm_nic, Unset):
        json_encryption_algorithm_nic = []
        for encryption_algorithm_nic_item_data in encryption_algorithm_nic:
            encryption_algorithm_nic_item: Union[None, str]
            encryption_algorithm_nic_item = encryption_algorithm_nic_item_data
            json_encryption_algorithm_nic.append(encryption_algorithm_nic_item)

    params["encryption_algorithm__nic"] = json_encryption_algorithm_nic

    json_encryption_algorithm_nie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(encryption_algorithm_nie, Unset):
        json_encryption_algorithm_nie = []
        for encryption_algorithm_nie_item_data in encryption_algorithm_nie:
            encryption_algorithm_nie_item: Union[None, str]
            encryption_algorithm_nie_item = encryption_algorithm_nie_item_data
            json_encryption_algorithm_nie.append(encryption_algorithm_nie_item)

    params["encryption_algorithm__nie"] = json_encryption_algorithm_nie

    json_encryption_algorithm_niew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(encryption_algorithm_niew, Unset):
        json_encryption_algorithm_niew = []
        for encryption_algorithm_niew_item_data in encryption_algorithm_niew:
            encryption_algorithm_niew_item: Union[None, str]
            encryption_algorithm_niew_item = encryption_algorithm_niew_item_data
            json_encryption_algorithm_niew.append(encryption_algorithm_niew_item)

    params["encryption_algorithm__niew"] = json_encryption_algorithm_niew

    json_encryption_algorithm_nisw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(encryption_algorithm_nisw, Unset):
        json_encryption_algorithm_nisw = []
        for encryption_algorithm_nisw_item_data in encryption_algorithm_nisw:
            encryption_algorithm_nisw_item: Union[None, str]
            encryption_algorithm_nisw_item = encryption_algorithm_nisw_item_data
            json_encryption_algorithm_nisw.append(encryption_algorithm_nisw_item)

    params["encryption_algorithm__nisw"] = json_encryption_algorithm_nisw

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

    json_ipsec_policy: Union[Unset, list[str]] = UNSET
    if not isinstance(ipsec_policy, Unset):
        json_ipsec_policy = ipsec_policy

    params["ipsec_policy"] = json_ipsec_policy

    json_ipsec_policy_n: Union[Unset, list[str]] = UNSET
    if not isinstance(ipsec_policy_n, Unset):
        json_ipsec_policy_n = ipsec_policy_n

    params["ipsec_policy__n"] = json_ipsec_policy_n

    json_ipsec_policy_id: Union[Unset, list[int]] = UNSET
    if not isinstance(ipsec_policy_id, Unset):
        json_ipsec_policy_id = ipsec_policy_id

    params["ipsec_policy_id"] = json_ipsec_policy_id

    json_ipsec_policy_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(ipsec_policy_id_n, Unset):
        json_ipsec_policy_id_n = ipsec_policy_id_n

    params["ipsec_policy_id__n"] = json_ipsec_policy_id_n

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

    json_sa_lifetime_data: Union[Unset, list[int]] = UNSET
    if not isinstance(sa_lifetime_data, Unset):
        json_sa_lifetime_data = sa_lifetime_data

    params["sa_lifetime_data"] = json_sa_lifetime_data

    params["sa_lifetime_data__empty"] = sa_lifetime_data_empty

    json_sa_lifetime_data_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(sa_lifetime_data_gt, Unset):
        json_sa_lifetime_data_gt = sa_lifetime_data_gt

    params["sa_lifetime_data__gt"] = json_sa_lifetime_data_gt

    json_sa_lifetime_data_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(sa_lifetime_data_gte, Unset):
        json_sa_lifetime_data_gte = sa_lifetime_data_gte

    params["sa_lifetime_data__gte"] = json_sa_lifetime_data_gte

    json_sa_lifetime_data_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(sa_lifetime_data_lt, Unset):
        json_sa_lifetime_data_lt = sa_lifetime_data_lt

    params["sa_lifetime_data__lt"] = json_sa_lifetime_data_lt

    json_sa_lifetime_data_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(sa_lifetime_data_lte, Unset):
        json_sa_lifetime_data_lte = sa_lifetime_data_lte

    params["sa_lifetime_data__lte"] = json_sa_lifetime_data_lte

    json_sa_lifetime_data_n: Union[Unset, list[int]] = UNSET
    if not isinstance(sa_lifetime_data_n, Unset):
        json_sa_lifetime_data_n = sa_lifetime_data_n

    params["sa_lifetime_data__n"] = json_sa_lifetime_data_n

    json_sa_lifetime_seconds: Union[Unset, list[int]] = UNSET
    if not isinstance(sa_lifetime_seconds, Unset):
        json_sa_lifetime_seconds = sa_lifetime_seconds

    params["sa_lifetime_seconds"] = json_sa_lifetime_seconds

    params["sa_lifetime_seconds__empty"] = sa_lifetime_seconds_empty

    json_sa_lifetime_seconds_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(sa_lifetime_seconds_gt, Unset):
        json_sa_lifetime_seconds_gt = sa_lifetime_seconds_gt

    params["sa_lifetime_seconds__gt"] = json_sa_lifetime_seconds_gt

    json_sa_lifetime_seconds_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(sa_lifetime_seconds_gte, Unset):
        json_sa_lifetime_seconds_gte = sa_lifetime_seconds_gte

    params["sa_lifetime_seconds__gte"] = json_sa_lifetime_seconds_gte

    json_sa_lifetime_seconds_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(sa_lifetime_seconds_lt, Unset):
        json_sa_lifetime_seconds_lt = sa_lifetime_seconds_lt

    params["sa_lifetime_seconds__lt"] = json_sa_lifetime_seconds_lt

    json_sa_lifetime_seconds_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(sa_lifetime_seconds_lte, Unset):
        json_sa_lifetime_seconds_lte = sa_lifetime_seconds_lte

    params["sa_lifetime_seconds__lte"] = json_sa_lifetime_seconds_lte

    json_sa_lifetime_seconds_n: Union[Unset, list[int]] = UNSET
    if not isinstance(sa_lifetime_seconds_n, Unset):
        json_sa_lifetime_seconds_n = sa_lifetime_seconds_n

    params["sa_lifetime_seconds__n"] = json_sa_lifetime_seconds_n

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
        "url": "/api/vpn/ipsec-proposals/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedIPSecProposalList]:
    if response.status_code == 200:
        response_200 = PaginatedIPSecProposalList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedIPSecProposalList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    authentication_algorithm: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_empty: Union[Unset, bool] = UNSET,
    authentication_algorithm_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_n: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    encryption_algorithm: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_empty: Union[Unset, bool] = UNSET,
    encryption_algorithm_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_n: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    ipsec_policy: Union[Unset, list[str]] = UNSET,
    ipsec_policy_n: Union[Unset, list[str]] = UNSET,
    ipsec_policy_id: Union[Unset, list[int]] = UNSET,
    ipsec_policy_id_n: Union[Unset, list[int]] = UNSET,
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
    sa_lifetime_data: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_empty: Union[Unset, bool] = UNSET,
    sa_lifetime_data_gt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_gte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_lt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_lte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_n: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_empty: Union[Unset, bool] = UNSET,
    sa_lifetime_seconds_gt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_gte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_lt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_lte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedIPSecProposalList]:
    """Get a list of IPSec proposal objects.

    Args:
        authentication_algorithm (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_empty (Union[Unset, bool]):
        authentication_algorithm_ic (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_ie (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_iew (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_isw (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_n (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_nic (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_nie (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_niew (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_nisw (Union[Unset, list[Union[None, str]]]):
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
        encryption_algorithm (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_empty (Union[Unset, bool]):
        encryption_algorithm_ic (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_ie (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_iew (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_isw (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_n (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_nic (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_nie (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_niew (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_nisw (Union[Unset, list[Union[None, str]]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        ipsec_policy (Union[Unset, list[str]]):
        ipsec_policy_n (Union[Unset, list[str]]):
        ipsec_policy_id (Union[Unset, list[int]]):
        ipsec_policy_id_n (Union[Unset, list[int]]):
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
        sa_lifetime_data (Union[Unset, list[int]]):
        sa_lifetime_data_empty (Union[Unset, bool]):
        sa_lifetime_data_gt (Union[Unset, list[int]]):
        sa_lifetime_data_gte (Union[Unset, list[int]]):
        sa_lifetime_data_lt (Union[Unset, list[int]]):
        sa_lifetime_data_lte (Union[Unset, list[int]]):
        sa_lifetime_data_n (Union[Unset, list[int]]):
        sa_lifetime_seconds (Union[Unset, list[int]]):
        sa_lifetime_seconds_empty (Union[Unset, bool]):
        sa_lifetime_seconds_gt (Union[Unset, list[int]]):
        sa_lifetime_seconds_gte (Union[Unset, list[int]]):
        sa_lifetime_seconds_lt (Union[Unset, list[int]]):
        sa_lifetime_seconds_lte (Union[Unset, list[int]]):
        sa_lifetime_seconds_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedIPSecProposalList]
    """

    kwargs = _get_kwargs(
        authentication_algorithm=authentication_algorithm,
        authentication_algorithm_empty=authentication_algorithm_empty,
        authentication_algorithm_ic=authentication_algorithm_ic,
        authentication_algorithm_ie=authentication_algorithm_ie,
        authentication_algorithm_iew=authentication_algorithm_iew,
        authentication_algorithm_isw=authentication_algorithm_isw,
        authentication_algorithm_n=authentication_algorithm_n,
        authentication_algorithm_nic=authentication_algorithm_nic,
        authentication_algorithm_nie=authentication_algorithm_nie,
        authentication_algorithm_niew=authentication_algorithm_niew,
        authentication_algorithm_nisw=authentication_algorithm_nisw,
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
        encryption_algorithm=encryption_algorithm,
        encryption_algorithm_empty=encryption_algorithm_empty,
        encryption_algorithm_ic=encryption_algorithm_ic,
        encryption_algorithm_ie=encryption_algorithm_ie,
        encryption_algorithm_iew=encryption_algorithm_iew,
        encryption_algorithm_isw=encryption_algorithm_isw,
        encryption_algorithm_n=encryption_algorithm_n,
        encryption_algorithm_nic=encryption_algorithm_nic,
        encryption_algorithm_nie=encryption_algorithm_nie,
        encryption_algorithm_niew=encryption_algorithm_niew,
        encryption_algorithm_nisw=encryption_algorithm_nisw,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        ipsec_policy=ipsec_policy,
        ipsec_policy_n=ipsec_policy_n,
        ipsec_policy_id=ipsec_policy_id,
        ipsec_policy_id_n=ipsec_policy_id_n,
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
        sa_lifetime_data=sa_lifetime_data,
        sa_lifetime_data_empty=sa_lifetime_data_empty,
        sa_lifetime_data_gt=sa_lifetime_data_gt,
        sa_lifetime_data_gte=sa_lifetime_data_gte,
        sa_lifetime_data_lt=sa_lifetime_data_lt,
        sa_lifetime_data_lte=sa_lifetime_data_lte,
        sa_lifetime_data_n=sa_lifetime_data_n,
        sa_lifetime_seconds=sa_lifetime_seconds,
        sa_lifetime_seconds_empty=sa_lifetime_seconds_empty,
        sa_lifetime_seconds_gt=sa_lifetime_seconds_gt,
        sa_lifetime_seconds_gte=sa_lifetime_seconds_gte,
        sa_lifetime_seconds_lt=sa_lifetime_seconds_lt,
        sa_lifetime_seconds_lte=sa_lifetime_seconds_lte,
        sa_lifetime_seconds_n=sa_lifetime_seconds_n,
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
    authentication_algorithm: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_empty: Union[Unset, bool] = UNSET,
    authentication_algorithm_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_n: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    encryption_algorithm: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_empty: Union[Unset, bool] = UNSET,
    encryption_algorithm_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_n: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    ipsec_policy: Union[Unset, list[str]] = UNSET,
    ipsec_policy_n: Union[Unset, list[str]] = UNSET,
    ipsec_policy_id: Union[Unset, list[int]] = UNSET,
    ipsec_policy_id_n: Union[Unset, list[int]] = UNSET,
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
    sa_lifetime_data: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_empty: Union[Unset, bool] = UNSET,
    sa_lifetime_data_gt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_gte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_lt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_lte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_n: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_empty: Union[Unset, bool] = UNSET,
    sa_lifetime_seconds_gt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_gte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_lt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_lte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedIPSecProposalList]:
    """Get a list of IPSec proposal objects.

    Args:
        authentication_algorithm (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_empty (Union[Unset, bool]):
        authentication_algorithm_ic (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_ie (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_iew (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_isw (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_n (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_nic (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_nie (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_niew (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_nisw (Union[Unset, list[Union[None, str]]]):
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
        encryption_algorithm (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_empty (Union[Unset, bool]):
        encryption_algorithm_ic (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_ie (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_iew (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_isw (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_n (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_nic (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_nie (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_niew (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_nisw (Union[Unset, list[Union[None, str]]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        ipsec_policy (Union[Unset, list[str]]):
        ipsec_policy_n (Union[Unset, list[str]]):
        ipsec_policy_id (Union[Unset, list[int]]):
        ipsec_policy_id_n (Union[Unset, list[int]]):
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
        sa_lifetime_data (Union[Unset, list[int]]):
        sa_lifetime_data_empty (Union[Unset, bool]):
        sa_lifetime_data_gt (Union[Unset, list[int]]):
        sa_lifetime_data_gte (Union[Unset, list[int]]):
        sa_lifetime_data_lt (Union[Unset, list[int]]):
        sa_lifetime_data_lte (Union[Unset, list[int]]):
        sa_lifetime_data_n (Union[Unset, list[int]]):
        sa_lifetime_seconds (Union[Unset, list[int]]):
        sa_lifetime_seconds_empty (Union[Unset, bool]):
        sa_lifetime_seconds_gt (Union[Unset, list[int]]):
        sa_lifetime_seconds_gte (Union[Unset, list[int]]):
        sa_lifetime_seconds_lt (Union[Unset, list[int]]):
        sa_lifetime_seconds_lte (Union[Unset, list[int]]):
        sa_lifetime_seconds_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedIPSecProposalList
    """

    return sync_detailed(
        client=client,
        authentication_algorithm=authentication_algorithm,
        authentication_algorithm_empty=authentication_algorithm_empty,
        authentication_algorithm_ic=authentication_algorithm_ic,
        authentication_algorithm_ie=authentication_algorithm_ie,
        authentication_algorithm_iew=authentication_algorithm_iew,
        authentication_algorithm_isw=authentication_algorithm_isw,
        authentication_algorithm_n=authentication_algorithm_n,
        authentication_algorithm_nic=authentication_algorithm_nic,
        authentication_algorithm_nie=authentication_algorithm_nie,
        authentication_algorithm_niew=authentication_algorithm_niew,
        authentication_algorithm_nisw=authentication_algorithm_nisw,
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
        encryption_algorithm=encryption_algorithm,
        encryption_algorithm_empty=encryption_algorithm_empty,
        encryption_algorithm_ic=encryption_algorithm_ic,
        encryption_algorithm_ie=encryption_algorithm_ie,
        encryption_algorithm_iew=encryption_algorithm_iew,
        encryption_algorithm_isw=encryption_algorithm_isw,
        encryption_algorithm_n=encryption_algorithm_n,
        encryption_algorithm_nic=encryption_algorithm_nic,
        encryption_algorithm_nie=encryption_algorithm_nie,
        encryption_algorithm_niew=encryption_algorithm_niew,
        encryption_algorithm_nisw=encryption_algorithm_nisw,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        ipsec_policy=ipsec_policy,
        ipsec_policy_n=ipsec_policy_n,
        ipsec_policy_id=ipsec_policy_id,
        ipsec_policy_id_n=ipsec_policy_id_n,
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
        sa_lifetime_data=sa_lifetime_data,
        sa_lifetime_data_empty=sa_lifetime_data_empty,
        sa_lifetime_data_gt=sa_lifetime_data_gt,
        sa_lifetime_data_gte=sa_lifetime_data_gte,
        sa_lifetime_data_lt=sa_lifetime_data_lt,
        sa_lifetime_data_lte=sa_lifetime_data_lte,
        sa_lifetime_data_n=sa_lifetime_data_n,
        sa_lifetime_seconds=sa_lifetime_seconds,
        sa_lifetime_seconds_empty=sa_lifetime_seconds_empty,
        sa_lifetime_seconds_gt=sa_lifetime_seconds_gt,
        sa_lifetime_seconds_gte=sa_lifetime_seconds_gte,
        sa_lifetime_seconds_lt=sa_lifetime_seconds_lt,
        sa_lifetime_seconds_lte=sa_lifetime_seconds_lte,
        sa_lifetime_seconds_n=sa_lifetime_seconds_n,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    authentication_algorithm: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_empty: Union[Unset, bool] = UNSET,
    authentication_algorithm_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_n: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    encryption_algorithm: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_empty: Union[Unset, bool] = UNSET,
    encryption_algorithm_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_n: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    ipsec_policy: Union[Unset, list[str]] = UNSET,
    ipsec_policy_n: Union[Unset, list[str]] = UNSET,
    ipsec_policy_id: Union[Unset, list[int]] = UNSET,
    ipsec_policy_id_n: Union[Unset, list[int]] = UNSET,
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
    sa_lifetime_data: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_empty: Union[Unset, bool] = UNSET,
    sa_lifetime_data_gt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_gte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_lt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_lte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_n: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_empty: Union[Unset, bool] = UNSET,
    sa_lifetime_seconds_gt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_gte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_lt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_lte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedIPSecProposalList]:
    """Get a list of IPSec proposal objects.

    Args:
        authentication_algorithm (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_empty (Union[Unset, bool]):
        authentication_algorithm_ic (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_ie (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_iew (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_isw (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_n (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_nic (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_nie (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_niew (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_nisw (Union[Unset, list[Union[None, str]]]):
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
        encryption_algorithm (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_empty (Union[Unset, bool]):
        encryption_algorithm_ic (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_ie (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_iew (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_isw (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_n (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_nic (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_nie (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_niew (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_nisw (Union[Unset, list[Union[None, str]]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        ipsec_policy (Union[Unset, list[str]]):
        ipsec_policy_n (Union[Unset, list[str]]):
        ipsec_policy_id (Union[Unset, list[int]]):
        ipsec_policy_id_n (Union[Unset, list[int]]):
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
        sa_lifetime_data (Union[Unset, list[int]]):
        sa_lifetime_data_empty (Union[Unset, bool]):
        sa_lifetime_data_gt (Union[Unset, list[int]]):
        sa_lifetime_data_gte (Union[Unset, list[int]]):
        sa_lifetime_data_lt (Union[Unset, list[int]]):
        sa_lifetime_data_lte (Union[Unset, list[int]]):
        sa_lifetime_data_n (Union[Unset, list[int]]):
        sa_lifetime_seconds (Union[Unset, list[int]]):
        sa_lifetime_seconds_empty (Union[Unset, bool]):
        sa_lifetime_seconds_gt (Union[Unset, list[int]]):
        sa_lifetime_seconds_gte (Union[Unset, list[int]]):
        sa_lifetime_seconds_lt (Union[Unset, list[int]]):
        sa_lifetime_seconds_lte (Union[Unset, list[int]]):
        sa_lifetime_seconds_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedIPSecProposalList]
    """

    kwargs = _get_kwargs(
        authentication_algorithm=authentication_algorithm,
        authentication_algorithm_empty=authentication_algorithm_empty,
        authentication_algorithm_ic=authentication_algorithm_ic,
        authentication_algorithm_ie=authentication_algorithm_ie,
        authentication_algorithm_iew=authentication_algorithm_iew,
        authentication_algorithm_isw=authentication_algorithm_isw,
        authentication_algorithm_n=authentication_algorithm_n,
        authentication_algorithm_nic=authentication_algorithm_nic,
        authentication_algorithm_nie=authentication_algorithm_nie,
        authentication_algorithm_niew=authentication_algorithm_niew,
        authentication_algorithm_nisw=authentication_algorithm_nisw,
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
        encryption_algorithm=encryption_algorithm,
        encryption_algorithm_empty=encryption_algorithm_empty,
        encryption_algorithm_ic=encryption_algorithm_ic,
        encryption_algorithm_ie=encryption_algorithm_ie,
        encryption_algorithm_iew=encryption_algorithm_iew,
        encryption_algorithm_isw=encryption_algorithm_isw,
        encryption_algorithm_n=encryption_algorithm_n,
        encryption_algorithm_nic=encryption_algorithm_nic,
        encryption_algorithm_nie=encryption_algorithm_nie,
        encryption_algorithm_niew=encryption_algorithm_niew,
        encryption_algorithm_nisw=encryption_algorithm_nisw,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        ipsec_policy=ipsec_policy,
        ipsec_policy_n=ipsec_policy_n,
        ipsec_policy_id=ipsec_policy_id,
        ipsec_policy_id_n=ipsec_policy_id_n,
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
        sa_lifetime_data=sa_lifetime_data,
        sa_lifetime_data_empty=sa_lifetime_data_empty,
        sa_lifetime_data_gt=sa_lifetime_data_gt,
        sa_lifetime_data_gte=sa_lifetime_data_gte,
        sa_lifetime_data_lt=sa_lifetime_data_lt,
        sa_lifetime_data_lte=sa_lifetime_data_lte,
        sa_lifetime_data_n=sa_lifetime_data_n,
        sa_lifetime_seconds=sa_lifetime_seconds,
        sa_lifetime_seconds_empty=sa_lifetime_seconds_empty,
        sa_lifetime_seconds_gt=sa_lifetime_seconds_gt,
        sa_lifetime_seconds_gte=sa_lifetime_seconds_gte,
        sa_lifetime_seconds_lt=sa_lifetime_seconds_lt,
        sa_lifetime_seconds_lte=sa_lifetime_seconds_lte,
        sa_lifetime_seconds_n=sa_lifetime_seconds_n,
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
    authentication_algorithm: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_empty: Union[Unset, bool] = UNSET,
    authentication_algorithm_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_n: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    authentication_algorithm_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
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
    encryption_algorithm: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_empty: Union[Unset, bool] = UNSET,
    encryption_algorithm_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_n: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    encryption_algorithm_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    ipsec_policy: Union[Unset, list[str]] = UNSET,
    ipsec_policy_n: Union[Unset, list[str]] = UNSET,
    ipsec_policy_id: Union[Unset, list[int]] = UNSET,
    ipsec_policy_id_n: Union[Unset, list[int]] = UNSET,
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
    sa_lifetime_data: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_empty: Union[Unset, bool] = UNSET,
    sa_lifetime_data_gt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_gte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_lt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_lte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_data_n: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_empty: Union[Unset, bool] = UNSET,
    sa_lifetime_seconds_gt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_gte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_lt: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_lte: Union[Unset, list[int]] = UNSET,
    sa_lifetime_seconds_n: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedIPSecProposalList]:
    """Get a list of IPSec proposal objects.

    Args:
        authentication_algorithm (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_empty (Union[Unset, bool]):
        authentication_algorithm_ic (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_ie (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_iew (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_isw (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_n (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_nic (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_nie (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_niew (Union[Unset, list[Union[None, str]]]):
        authentication_algorithm_nisw (Union[Unset, list[Union[None, str]]]):
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
        encryption_algorithm (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_empty (Union[Unset, bool]):
        encryption_algorithm_ic (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_ie (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_iew (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_isw (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_n (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_nic (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_nie (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_niew (Union[Unset, list[Union[None, str]]]):
        encryption_algorithm_nisw (Union[Unset, list[Union[None, str]]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        ipsec_policy (Union[Unset, list[str]]):
        ipsec_policy_n (Union[Unset, list[str]]):
        ipsec_policy_id (Union[Unset, list[int]]):
        ipsec_policy_id_n (Union[Unset, list[int]]):
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
        sa_lifetime_data (Union[Unset, list[int]]):
        sa_lifetime_data_empty (Union[Unset, bool]):
        sa_lifetime_data_gt (Union[Unset, list[int]]):
        sa_lifetime_data_gte (Union[Unset, list[int]]):
        sa_lifetime_data_lt (Union[Unset, list[int]]):
        sa_lifetime_data_lte (Union[Unset, list[int]]):
        sa_lifetime_data_n (Union[Unset, list[int]]):
        sa_lifetime_seconds (Union[Unset, list[int]]):
        sa_lifetime_seconds_empty (Union[Unset, bool]):
        sa_lifetime_seconds_gt (Union[Unset, list[int]]):
        sa_lifetime_seconds_gte (Union[Unset, list[int]]):
        sa_lifetime_seconds_lt (Union[Unset, list[int]]):
        sa_lifetime_seconds_lte (Union[Unset, list[int]]):
        sa_lifetime_seconds_n (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedIPSecProposalList
    """

    return (
        await asyncio_detailed(
            client=client,
            authentication_algorithm=authentication_algorithm,
            authentication_algorithm_empty=authentication_algorithm_empty,
            authentication_algorithm_ic=authentication_algorithm_ic,
            authentication_algorithm_ie=authentication_algorithm_ie,
            authentication_algorithm_iew=authentication_algorithm_iew,
            authentication_algorithm_isw=authentication_algorithm_isw,
            authentication_algorithm_n=authentication_algorithm_n,
            authentication_algorithm_nic=authentication_algorithm_nic,
            authentication_algorithm_nie=authentication_algorithm_nie,
            authentication_algorithm_niew=authentication_algorithm_niew,
            authentication_algorithm_nisw=authentication_algorithm_nisw,
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
            encryption_algorithm=encryption_algorithm,
            encryption_algorithm_empty=encryption_algorithm_empty,
            encryption_algorithm_ic=encryption_algorithm_ic,
            encryption_algorithm_ie=encryption_algorithm_ie,
            encryption_algorithm_iew=encryption_algorithm_iew,
            encryption_algorithm_isw=encryption_algorithm_isw,
            encryption_algorithm_n=encryption_algorithm_n,
            encryption_algorithm_nic=encryption_algorithm_nic,
            encryption_algorithm_nie=encryption_algorithm_nie,
            encryption_algorithm_niew=encryption_algorithm_niew,
            encryption_algorithm_nisw=encryption_algorithm_nisw,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            ipsec_policy=ipsec_policy,
            ipsec_policy_n=ipsec_policy_n,
            ipsec_policy_id=ipsec_policy_id,
            ipsec_policy_id_n=ipsec_policy_id_n,
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
            sa_lifetime_data=sa_lifetime_data,
            sa_lifetime_data_empty=sa_lifetime_data_empty,
            sa_lifetime_data_gt=sa_lifetime_data_gt,
            sa_lifetime_data_gte=sa_lifetime_data_gte,
            sa_lifetime_data_lt=sa_lifetime_data_lt,
            sa_lifetime_data_lte=sa_lifetime_data_lte,
            sa_lifetime_data_n=sa_lifetime_data_n,
            sa_lifetime_seconds=sa_lifetime_seconds,
            sa_lifetime_seconds_empty=sa_lifetime_seconds_empty,
            sa_lifetime_seconds_gt=sa_lifetime_seconds_gt,
            sa_lifetime_seconds_gte=sa_lifetime_seconds_gte,
            sa_lifetime_seconds_lt=sa_lifetime_seconds_lt,
            sa_lifetime_seconds_lte=sa_lifetime_seconds_lte,
            sa_lifetime_seconds_n=sa_lifetime_seconds_n,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
            updated_by_request=updated_by_request,
        )
    ).parsed
