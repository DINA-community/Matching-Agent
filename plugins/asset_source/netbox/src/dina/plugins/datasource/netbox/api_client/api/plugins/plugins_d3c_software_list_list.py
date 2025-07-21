import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_software_list import PaginatedSoftwareList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cpe: Union[Unset, list[str]] = UNSET,
    cpe_empty: Union[Unset, bool] = UNSET,
    cpe_ic: Union[Unset, list[str]] = UNSET,
    cpe_ie: Union[Unset, list[str]] = UNSET,
    cpe_iew: Union[Unset, list[str]] = UNSET,
    cpe_isw: Union[Unset, list[str]] = UNSET,
    cpe_n: Union[Unset, list[str]] = UNSET,
    cpe_nic: Union[Unset, list[str]] = UNSET,
    cpe_nie: Union[Unset, list[str]] = UNSET,
    cpe_niew: Union[Unset, list[str]] = UNSET,
    cpe_nisw: Union[Unset, list[str]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_firmware: Union[Unset, bool] = UNSET,
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
    purl: Union[Unset, list[str]] = UNSET,
    purl_empty: Union[Unset, bool] = UNSET,
    purl_ic: Union[Unset, list[str]] = UNSET,
    purl_ie: Union[Unset, list[str]] = UNSET,
    purl_iew: Union[Unset, list[str]] = UNSET,
    purl_isw: Union[Unset, list[str]] = UNSET,
    purl_n: Union[Unset, list[str]] = UNSET,
    purl_nic: Union[Unset, list[str]] = UNSET,
    purl_nie: Union[Unset, list[str]] = UNSET,
    purl_niew: Union[Unset, list[str]] = UNSET,
    purl_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    version: Union[Unset, list[str]] = UNSET,
    version_empty: Union[Unset, bool] = UNSET,
    version_ic: Union[Unset, list[str]] = UNSET,
    version_ie: Union[Unset, list[str]] = UNSET,
    version_iew: Union[Unset, list[str]] = UNSET,
    version_isw: Union[Unset, list[str]] = UNSET,
    version_n: Union[Unset, list[str]] = UNSET,
    version_nic: Union[Unset, list[str]] = UNSET,
    version_nie: Union[Unset, list[str]] = UNSET,
    version_niew: Union[Unset, list[str]] = UNSET,
    version_nisw: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_cpe: Union[Unset, list[str]] = UNSET
    if not isinstance(cpe, Unset):
        json_cpe = cpe

    params["cpe"] = json_cpe

    params["cpe__empty"] = cpe_empty

    json_cpe_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(cpe_ic, Unset):
        json_cpe_ic = cpe_ic

    params["cpe__ic"] = json_cpe_ic

    json_cpe_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(cpe_ie, Unset):
        json_cpe_ie = cpe_ie

    params["cpe__ie"] = json_cpe_ie

    json_cpe_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(cpe_iew, Unset):
        json_cpe_iew = cpe_iew

    params["cpe__iew"] = json_cpe_iew

    json_cpe_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(cpe_isw, Unset):
        json_cpe_isw = cpe_isw

    params["cpe__isw"] = json_cpe_isw

    json_cpe_n: Union[Unset, list[str]] = UNSET
    if not isinstance(cpe_n, Unset):
        json_cpe_n = cpe_n

    params["cpe__n"] = json_cpe_n

    json_cpe_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(cpe_nic, Unset):
        json_cpe_nic = cpe_nic

    params["cpe__nic"] = json_cpe_nic

    json_cpe_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(cpe_nie, Unset):
        json_cpe_nie = cpe_nie

    params["cpe__nie"] = json_cpe_nie

    json_cpe_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(cpe_niew, Unset):
        json_cpe_niew = cpe_niew

    params["cpe__niew"] = json_cpe_niew

    json_cpe_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(cpe_nisw, Unset):
        json_cpe_nisw = cpe_nisw

    params["cpe__nisw"] = json_cpe_nisw

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

    params["is_firmware"] = is_firmware

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

    json_purl: Union[Unset, list[str]] = UNSET
    if not isinstance(purl, Unset):
        json_purl = purl

    params["purl"] = json_purl

    params["purl__empty"] = purl_empty

    json_purl_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(purl_ic, Unset):
        json_purl_ic = purl_ic

    params["purl__ic"] = json_purl_ic

    json_purl_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(purl_ie, Unset):
        json_purl_ie = purl_ie

    params["purl__ie"] = json_purl_ie

    json_purl_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(purl_iew, Unset):
        json_purl_iew = purl_iew

    params["purl__iew"] = json_purl_iew

    json_purl_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(purl_isw, Unset):
        json_purl_isw = purl_isw

    params["purl__isw"] = json_purl_isw

    json_purl_n: Union[Unset, list[str]] = UNSET
    if not isinstance(purl_n, Unset):
        json_purl_n = purl_n

    params["purl__n"] = json_purl_n

    json_purl_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(purl_nic, Unset):
        json_purl_nic = purl_nic

    params["purl__nic"] = json_purl_nic

    json_purl_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(purl_nie, Unset):
        json_purl_nie = purl_nie

    params["purl__nie"] = json_purl_nie

    json_purl_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(purl_niew, Unset):
        json_purl_niew = purl_niew

    params["purl__niew"] = json_purl_niew

    json_purl_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(purl_nisw, Unset):
        json_purl_nisw = purl_nisw

    params["purl__nisw"] = json_purl_nisw

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

    json_version: Union[Unset, list[str]] = UNSET
    if not isinstance(version, Unset):
        json_version = version

    params["version"] = json_version

    params["version__empty"] = version_empty

    json_version_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(version_ic, Unset):
        json_version_ic = version_ic

    params["version__ic"] = json_version_ic

    json_version_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(version_ie, Unset):
        json_version_ie = version_ie

    params["version__ie"] = json_version_ie

    json_version_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(version_iew, Unset):
        json_version_iew = version_iew

    params["version__iew"] = json_version_iew

    json_version_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(version_isw, Unset):
        json_version_isw = version_isw

    params["version__isw"] = json_version_isw

    json_version_n: Union[Unset, list[str]] = UNSET
    if not isinstance(version_n, Unset):
        json_version_n = version_n

    params["version__n"] = json_version_n

    json_version_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(version_nic, Unset):
        json_version_nic = version_nic

    params["version__nic"] = json_version_nic

    json_version_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(version_nie, Unset):
        json_version_nie = version_nie

    params["version__nie"] = json_version_nie

    json_version_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(version_niew, Unset):
        json_version_niew = version_niew

    params["version__niew"] = json_version_niew

    json_version_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(version_nisw, Unset):
        json_version_nisw = version_nisw

    params["version__nisw"] = json_version_nisw

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/plugins/d3c/software-list/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedSoftwareList]:
    if response.status_code == 200:
        response_200 = PaginatedSoftwareList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedSoftwareList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cpe: Union[Unset, list[str]] = UNSET,
    cpe_empty: Union[Unset, bool] = UNSET,
    cpe_ic: Union[Unset, list[str]] = UNSET,
    cpe_ie: Union[Unset, list[str]] = UNSET,
    cpe_iew: Union[Unset, list[str]] = UNSET,
    cpe_isw: Union[Unset, list[str]] = UNSET,
    cpe_n: Union[Unset, list[str]] = UNSET,
    cpe_nic: Union[Unset, list[str]] = UNSET,
    cpe_nie: Union[Unset, list[str]] = UNSET,
    cpe_niew: Union[Unset, list[str]] = UNSET,
    cpe_nisw: Union[Unset, list[str]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_firmware: Union[Unset, bool] = UNSET,
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
    purl: Union[Unset, list[str]] = UNSET,
    purl_empty: Union[Unset, bool] = UNSET,
    purl_ic: Union[Unset, list[str]] = UNSET,
    purl_ie: Union[Unset, list[str]] = UNSET,
    purl_iew: Union[Unset, list[str]] = UNSET,
    purl_isw: Union[Unset, list[str]] = UNSET,
    purl_n: Union[Unset, list[str]] = UNSET,
    purl_nic: Union[Unset, list[str]] = UNSET,
    purl_nie: Union[Unset, list[str]] = UNSET,
    purl_niew: Union[Unset, list[str]] = UNSET,
    purl_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    version: Union[Unset, list[str]] = UNSET,
    version_empty: Union[Unset, bool] = UNSET,
    version_ic: Union[Unset, list[str]] = UNSET,
    version_ie: Union[Unset, list[str]] = UNSET,
    version_iew: Union[Unset, list[str]] = UNSET,
    version_isw: Union[Unset, list[str]] = UNSET,
    version_n: Union[Unset, list[str]] = UNSET,
    version_nic: Union[Unset, list[str]] = UNSET,
    version_nie: Union[Unset, list[str]] = UNSET,
    version_niew: Union[Unset, list[str]] = UNSET,
    version_nisw: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedSoftwareList]:
    """ViewSet for Software.

    Args:
        cpe (Union[Unset, list[str]]):
        cpe_empty (Union[Unset, bool]):
        cpe_ic (Union[Unset, list[str]]):
        cpe_ie (Union[Unset, list[str]]):
        cpe_iew (Union[Unset, list[str]]):
        cpe_isw (Union[Unset, list[str]]):
        cpe_n (Union[Unset, list[str]]):
        cpe_nic (Union[Unset, list[str]]):
        cpe_nie (Union[Unset, list[str]]):
        cpe_niew (Union[Unset, list[str]]):
        cpe_nisw (Union[Unset, list[str]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_firmware (Union[Unset, bool]):
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
        purl (Union[Unset, list[str]]):
        purl_empty (Union[Unset, bool]):
        purl_ic (Union[Unset, list[str]]):
        purl_ie (Union[Unset, list[str]]):
        purl_iew (Union[Unset, list[str]]):
        purl_isw (Union[Unset, list[str]]):
        purl_n (Union[Unset, list[str]]):
        purl_nic (Union[Unset, list[str]]):
        purl_nie (Union[Unset, list[str]]):
        purl_niew (Union[Unset, list[str]]):
        purl_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        version (Union[Unset, list[str]]):
        version_empty (Union[Unset, bool]):
        version_ic (Union[Unset, list[str]]):
        version_ie (Union[Unset, list[str]]):
        version_iew (Union[Unset, list[str]]):
        version_isw (Union[Unset, list[str]]):
        version_n (Union[Unset, list[str]]):
        version_nic (Union[Unset, list[str]]):
        version_nie (Union[Unset, list[str]]):
        version_niew (Union[Unset, list[str]]):
        version_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedSoftwareList]
    """

    kwargs = _get_kwargs(
        cpe=cpe,
        cpe_empty=cpe_empty,
        cpe_ic=cpe_ic,
        cpe_ie=cpe_ie,
        cpe_iew=cpe_iew,
        cpe_isw=cpe_isw,
        cpe_n=cpe_n,
        cpe_nic=cpe_nic,
        cpe_nie=cpe_nie,
        cpe_niew=cpe_niew,
        cpe_nisw=cpe_nisw,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        is_firmware=is_firmware,
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
        purl=purl,
        purl_empty=purl_empty,
        purl_ic=purl_ic,
        purl_ie=purl_ie,
        purl_iew=purl_iew,
        purl_isw=purl_isw,
        purl_n=purl_n,
        purl_nic=purl_nic,
        purl_nie=purl_nie,
        purl_niew=purl_niew,
        purl_nisw=purl_nisw,
        q=q,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
        version=version,
        version_empty=version_empty,
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
    cpe: Union[Unset, list[str]] = UNSET,
    cpe_empty: Union[Unset, bool] = UNSET,
    cpe_ic: Union[Unset, list[str]] = UNSET,
    cpe_ie: Union[Unset, list[str]] = UNSET,
    cpe_iew: Union[Unset, list[str]] = UNSET,
    cpe_isw: Union[Unset, list[str]] = UNSET,
    cpe_n: Union[Unset, list[str]] = UNSET,
    cpe_nic: Union[Unset, list[str]] = UNSET,
    cpe_nie: Union[Unset, list[str]] = UNSET,
    cpe_niew: Union[Unset, list[str]] = UNSET,
    cpe_nisw: Union[Unset, list[str]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_firmware: Union[Unset, bool] = UNSET,
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
    purl: Union[Unset, list[str]] = UNSET,
    purl_empty: Union[Unset, bool] = UNSET,
    purl_ic: Union[Unset, list[str]] = UNSET,
    purl_ie: Union[Unset, list[str]] = UNSET,
    purl_iew: Union[Unset, list[str]] = UNSET,
    purl_isw: Union[Unset, list[str]] = UNSET,
    purl_n: Union[Unset, list[str]] = UNSET,
    purl_nic: Union[Unset, list[str]] = UNSET,
    purl_nie: Union[Unset, list[str]] = UNSET,
    purl_niew: Union[Unset, list[str]] = UNSET,
    purl_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    version: Union[Unset, list[str]] = UNSET,
    version_empty: Union[Unset, bool] = UNSET,
    version_ic: Union[Unset, list[str]] = UNSET,
    version_ie: Union[Unset, list[str]] = UNSET,
    version_iew: Union[Unset, list[str]] = UNSET,
    version_isw: Union[Unset, list[str]] = UNSET,
    version_n: Union[Unset, list[str]] = UNSET,
    version_nic: Union[Unset, list[str]] = UNSET,
    version_nie: Union[Unset, list[str]] = UNSET,
    version_niew: Union[Unset, list[str]] = UNSET,
    version_nisw: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedSoftwareList]:
    """ViewSet for Software.

    Args:
        cpe (Union[Unset, list[str]]):
        cpe_empty (Union[Unset, bool]):
        cpe_ic (Union[Unset, list[str]]):
        cpe_ie (Union[Unset, list[str]]):
        cpe_iew (Union[Unset, list[str]]):
        cpe_isw (Union[Unset, list[str]]):
        cpe_n (Union[Unset, list[str]]):
        cpe_nic (Union[Unset, list[str]]):
        cpe_nie (Union[Unset, list[str]]):
        cpe_niew (Union[Unset, list[str]]):
        cpe_nisw (Union[Unset, list[str]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_firmware (Union[Unset, bool]):
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
        purl (Union[Unset, list[str]]):
        purl_empty (Union[Unset, bool]):
        purl_ic (Union[Unset, list[str]]):
        purl_ie (Union[Unset, list[str]]):
        purl_iew (Union[Unset, list[str]]):
        purl_isw (Union[Unset, list[str]]):
        purl_n (Union[Unset, list[str]]):
        purl_nic (Union[Unset, list[str]]):
        purl_nie (Union[Unset, list[str]]):
        purl_niew (Union[Unset, list[str]]):
        purl_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        version (Union[Unset, list[str]]):
        version_empty (Union[Unset, bool]):
        version_ic (Union[Unset, list[str]]):
        version_ie (Union[Unset, list[str]]):
        version_iew (Union[Unset, list[str]]):
        version_isw (Union[Unset, list[str]]):
        version_n (Union[Unset, list[str]]):
        version_nic (Union[Unset, list[str]]):
        version_nie (Union[Unset, list[str]]):
        version_niew (Union[Unset, list[str]]):
        version_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedSoftwareList
    """

    return sync_detailed(
        client=client,
        cpe=cpe,
        cpe_empty=cpe_empty,
        cpe_ic=cpe_ic,
        cpe_ie=cpe_ie,
        cpe_iew=cpe_iew,
        cpe_isw=cpe_isw,
        cpe_n=cpe_n,
        cpe_nic=cpe_nic,
        cpe_nie=cpe_nie,
        cpe_niew=cpe_niew,
        cpe_nisw=cpe_nisw,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        is_firmware=is_firmware,
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
        purl=purl,
        purl_empty=purl_empty,
        purl_ic=purl_ic,
        purl_ie=purl_ie,
        purl_iew=purl_iew,
        purl_isw=purl_isw,
        purl_n=purl_n,
        purl_nic=purl_nic,
        purl_nie=purl_nie,
        purl_niew=purl_niew,
        purl_nisw=purl_nisw,
        q=q,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
        version=version,
        version_empty=version_empty,
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
    cpe: Union[Unset, list[str]] = UNSET,
    cpe_empty: Union[Unset, bool] = UNSET,
    cpe_ic: Union[Unset, list[str]] = UNSET,
    cpe_ie: Union[Unset, list[str]] = UNSET,
    cpe_iew: Union[Unset, list[str]] = UNSET,
    cpe_isw: Union[Unset, list[str]] = UNSET,
    cpe_n: Union[Unset, list[str]] = UNSET,
    cpe_nic: Union[Unset, list[str]] = UNSET,
    cpe_nie: Union[Unset, list[str]] = UNSET,
    cpe_niew: Union[Unset, list[str]] = UNSET,
    cpe_nisw: Union[Unset, list[str]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_firmware: Union[Unset, bool] = UNSET,
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
    purl: Union[Unset, list[str]] = UNSET,
    purl_empty: Union[Unset, bool] = UNSET,
    purl_ic: Union[Unset, list[str]] = UNSET,
    purl_ie: Union[Unset, list[str]] = UNSET,
    purl_iew: Union[Unset, list[str]] = UNSET,
    purl_isw: Union[Unset, list[str]] = UNSET,
    purl_n: Union[Unset, list[str]] = UNSET,
    purl_nic: Union[Unset, list[str]] = UNSET,
    purl_nie: Union[Unset, list[str]] = UNSET,
    purl_niew: Union[Unset, list[str]] = UNSET,
    purl_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    version: Union[Unset, list[str]] = UNSET,
    version_empty: Union[Unset, bool] = UNSET,
    version_ic: Union[Unset, list[str]] = UNSET,
    version_ie: Union[Unset, list[str]] = UNSET,
    version_iew: Union[Unset, list[str]] = UNSET,
    version_isw: Union[Unset, list[str]] = UNSET,
    version_n: Union[Unset, list[str]] = UNSET,
    version_nic: Union[Unset, list[str]] = UNSET,
    version_nie: Union[Unset, list[str]] = UNSET,
    version_niew: Union[Unset, list[str]] = UNSET,
    version_nisw: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedSoftwareList]:
    """ViewSet for Software.

    Args:
        cpe (Union[Unset, list[str]]):
        cpe_empty (Union[Unset, bool]):
        cpe_ic (Union[Unset, list[str]]):
        cpe_ie (Union[Unset, list[str]]):
        cpe_iew (Union[Unset, list[str]]):
        cpe_isw (Union[Unset, list[str]]):
        cpe_n (Union[Unset, list[str]]):
        cpe_nic (Union[Unset, list[str]]):
        cpe_nie (Union[Unset, list[str]]):
        cpe_niew (Union[Unset, list[str]]):
        cpe_nisw (Union[Unset, list[str]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_firmware (Union[Unset, bool]):
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
        purl (Union[Unset, list[str]]):
        purl_empty (Union[Unset, bool]):
        purl_ic (Union[Unset, list[str]]):
        purl_ie (Union[Unset, list[str]]):
        purl_iew (Union[Unset, list[str]]):
        purl_isw (Union[Unset, list[str]]):
        purl_n (Union[Unset, list[str]]):
        purl_nic (Union[Unset, list[str]]):
        purl_nie (Union[Unset, list[str]]):
        purl_niew (Union[Unset, list[str]]):
        purl_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        version (Union[Unset, list[str]]):
        version_empty (Union[Unset, bool]):
        version_ic (Union[Unset, list[str]]):
        version_ie (Union[Unset, list[str]]):
        version_iew (Union[Unset, list[str]]):
        version_isw (Union[Unset, list[str]]):
        version_n (Union[Unset, list[str]]):
        version_nic (Union[Unset, list[str]]):
        version_nie (Union[Unset, list[str]]):
        version_niew (Union[Unset, list[str]]):
        version_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedSoftwareList]
    """

    kwargs = _get_kwargs(
        cpe=cpe,
        cpe_empty=cpe_empty,
        cpe_ic=cpe_ic,
        cpe_ie=cpe_ie,
        cpe_iew=cpe_iew,
        cpe_isw=cpe_isw,
        cpe_n=cpe_n,
        cpe_nic=cpe_nic,
        cpe_nie=cpe_nie,
        cpe_niew=cpe_niew,
        cpe_nisw=cpe_nisw,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        is_firmware=is_firmware,
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
        purl=purl,
        purl_empty=purl_empty,
        purl_ic=purl_ic,
        purl_ie=purl_ie,
        purl_iew=purl_iew,
        purl_isw=purl_isw,
        purl_n=purl_n,
        purl_nic=purl_nic,
        purl_nie=purl_nie,
        purl_niew=purl_niew,
        purl_nisw=purl_nisw,
        q=q,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
        version=version,
        version_empty=version_empty,
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
    cpe: Union[Unset, list[str]] = UNSET,
    cpe_empty: Union[Unset, bool] = UNSET,
    cpe_ic: Union[Unset, list[str]] = UNSET,
    cpe_ie: Union[Unset, list[str]] = UNSET,
    cpe_iew: Union[Unset, list[str]] = UNSET,
    cpe_isw: Union[Unset, list[str]] = UNSET,
    cpe_n: Union[Unset, list[str]] = UNSET,
    cpe_nic: Union[Unset, list[str]] = UNSET,
    cpe_nie: Union[Unset, list[str]] = UNSET,
    cpe_niew: Union[Unset, list[str]] = UNSET,
    cpe_nisw: Union[Unset, list[str]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    is_firmware: Union[Unset, bool] = UNSET,
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
    purl: Union[Unset, list[str]] = UNSET,
    purl_empty: Union[Unset, bool] = UNSET,
    purl_ic: Union[Unset, list[str]] = UNSET,
    purl_ie: Union[Unset, list[str]] = UNSET,
    purl_iew: Union[Unset, list[str]] = UNSET,
    purl_isw: Union[Unset, list[str]] = UNSET,
    purl_n: Union[Unset, list[str]] = UNSET,
    purl_nic: Union[Unset, list[str]] = UNSET,
    purl_nie: Union[Unset, list[str]] = UNSET,
    purl_niew: Union[Unset, list[str]] = UNSET,
    purl_nisw: Union[Unset, list[str]] = UNSET,
    q: Union[Unset, str] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    version: Union[Unset, list[str]] = UNSET,
    version_empty: Union[Unset, bool] = UNSET,
    version_ic: Union[Unset, list[str]] = UNSET,
    version_ie: Union[Unset, list[str]] = UNSET,
    version_iew: Union[Unset, list[str]] = UNSET,
    version_isw: Union[Unset, list[str]] = UNSET,
    version_n: Union[Unset, list[str]] = UNSET,
    version_nic: Union[Unset, list[str]] = UNSET,
    version_nie: Union[Unset, list[str]] = UNSET,
    version_niew: Union[Unset, list[str]] = UNSET,
    version_nisw: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedSoftwareList]:
    """ViewSet for Software.

    Args:
        cpe (Union[Unset, list[str]]):
        cpe_empty (Union[Unset, bool]):
        cpe_ic (Union[Unset, list[str]]):
        cpe_ie (Union[Unset, list[str]]):
        cpe_iew (Union[Unset, list[str]]):
        cpe_isw (Union[Unset, list[str]]):
        cpe_n (Union[Unset, list[str]]):
        cpe_nic (Union[Unset, list[str]]):
        cpe_nie (Union[Unset, list[str]]):
        cpe_niew (Union[Unset, list[str]]):
        cpe_nisw (Union[Unset, list[str]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        is_firmware (Union[Unset, bool]):
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
        purl (Union[Unset, list[str]]):
        purl_empty (Union[Unset, bool]):
        purl_ic (Union[Unset, list[str]]):
        purl_ie (Union[Unset, list[str]]):
        purl_iew (Union[Unset, list[str]]):
        purl_isw (Union[Unset, list[str]]):
        purl_n (Union[Unset, list[str]]):
        purl_nic (Union[Unset, list[str]]):
        purl_nie (Union[Unset, list[str]]):
        purl_niew (Union[Unset, list[str]]):
        purl_nisw (Union[Unset, list[str]]):
        q (Union[Unset, str]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        version (Union[Unset, list[str]]):
        version_empty (Union[Unset, bool]):
        version_ic (Union[Unset, list[str]]):
        version_ie (Union[Unset, list[str]]):
        version_iew (Union[Unset, list[str]]):
        version_isw (Union[Unset, list[str]]):
        version_n (Union[Unset, list[str]]):
        version_nic (Union[Unset, list[str]]):
        version_nie (Union[Unset, list[str]]):
        version_niew (Union[Unset, list[str]]):
        version_nisw (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedSoftwareList
    """

    return (
        await asyncio_detailed(
            client=client,
            cpe=cpe,
            cpe_empty=cpe_empty,
            cpe_ic=cpe_ic,
            cpe_ie=cpe_ie,
            cpe_iew=cpe_iew,
            cpe_isw=cpe_isw,
            cpe_n=cpe_n,
            cpe_nic=cpe_nic,
            cpe_nie=cpe_nie,
            cpe_niew=cpe_niew,
            cpe_nisw=cpe_nisw,
            created=created,
            created_empty=created_empty,
            created_gt=created_gt,
            created_gte=created_gte,
            created_lt=created_lt,
            created_lte=created_lte,
            created_n=created_n,
            created_by_request=created_by_request,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            is_firmware=is_firmware,
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
            purl=purl,
            purl_empty=purl_empty,
            purl_ic=purl_ic,
            purl_ie=purl_ie,
            purl_iew=purl_iew,
            purl_isw=purl_isw,
            purl_n=purl_n,
            purl_nic=purl_nic,
            purl_nie=purl_nie,
            purl_niew=purl_niew,
            purl_nisw=purl_nisw,
            q=q,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
            updated_by_request=updated_by_request,
            version=version,
            version_empty=version_empty,
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
