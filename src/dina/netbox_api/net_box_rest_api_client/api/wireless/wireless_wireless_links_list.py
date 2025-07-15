import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_wireless_link_list import PaginatedWirelessLinkList
from ...models.wireless_wireless_links_list_distance_unit import WirelessWirelessLinksListDistanceUnit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    auth_cipher: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_empty: Union[Unset, bool] = UNSET,
    auth_cipher_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_n: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_psk: Union[Unset, list[str]] = UNSET,
    auth_psk_empty: Union[Unset, bool] = UNSET,
    auth_psk_ic: Union[Unset, list[str]] = UNSET,
    auth_psk_ie: Union[Unset, list[str]] = UNSET,
    auth_psk_iew: Union[Unset, list[str]] = UNSET,
    auth_psk_isw: Union[Unset, list[str]] = UNSET,
    auth_psk_n: Union[Unset, list[str]] = UNSET,
    auth_psk_nic: Union[Unset, list[str]] = UNSET,
    auth_psk_nie: Union[Unset, list[str]] = UNSET,
    auth_psk_niew: Union[Unset, list[str]] = UNSET,
    auth_psk_nisw: Union[Unset, list[str]] = UNSET,
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
    distance: Union[Unset, list[float]] = UNSET,
    distance_empty: Union[Unset, bool] = UNSET,
    distance_gt: Union[Unset, list[float]] = UNSET,
    distance_gte: Union[Unset, list[float]] = UNSET,
    distance_lt: Union[Unset, list[float]] = UNSET,
    distance_lte: Union[Unset, list[float]] = UNSET,
    distance_n: Union[Unset, list[float]] = UNSET,
    distance_unit: Union[Unset, WirelessWirelessLinksListDistanceUnit] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_a_id: Union[Unset, list[int]] = UNSET,
    interface_a_id_n: Union[Unset, list[int]] = UNSET,
    interface_b_id: Union[Unset, list[int]] = UNSET,
    interface_b_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    ssid: Union[Unset, list[str]] = UNSET,
    ssid_empty: Union[Unset, bool] = UNSET,
    ssid_ic: Union[Unset, list[str]] = UNSET,
    ssid_ie: Union[Unset, list[str]] = UNSET,
    ssid_iew: Union[Unset, list[str]] = UNSET,
    ssid_isw: Union[Unset, list[str]] = UNSET,
    ssid_n: Union[Unset, list[str]] = UNSET,
    ssid_nic: Union[Unset, list[str]] = UNSET,
    ssid_nie: Union[Unset, list[str]] = UNSET,
    ssid_niew: Union[Unset, list[str]] = UNSET,
    ssid_nisw: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_auth_cipher: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_cipher, Unset):
        json_auth_cipher = []
        for auth_cipher_item_data in auth_cipher:
            auth_cipher_item: Union[None, str]
            auth_cipher_item = auth_cipher_item_data
            json_auth_cipher.append(auth_cipher_item)

    params["auth_cipher"] = json_auth_cipher

    params["auth_cipher__empty"] = auth_cipher_empty

    json_auth_cipher_ic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_cipher_ic, Unset):
        json_auth_cipher_ic = []
        for auth_cipher_ic_item_data in auth_cipher_ic:
            auth_cipher_ic_item: Union[None, str]
            auth_cipher_ic_item = auth_cipher_ic_item_data
            json_auth_cipher_ic.append(auth_cipher_ic_item)

    params["auth_cipher__ic"] = json_auth_cipher_ic

    json_auth_cipher_ie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_cipher_ie, Unset):
        json_auth_cipher_ie = []
        for auth_cipher_ie_item_data in auth_cipher_ie:
            auth_cipher_ie_item: Union[None, str]
            auth_cipher_ie_item = auth_cipher_ie_item_data
            json_auth_cipher_ie.append(auth_cipher_ie_item)

    params["auth_cipher__ie"] = json_auth_cipher_ie

    json_auth_cipher_iew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_cipher_iew, Unset):
        json_auth_cipher_iew = []
        for auth_cipher_iew_item_data in auth_cipher_iew:
            auth_cipher_iew_item: Union[None, str]
            auth_cipher_iew_item = auth_cipher_iew_item_data
            json_auth_cipher_iew.append(auth_cipher_iew_item)

    params["auth_cipher__iew"] = json_auth_cipher_iew

    json_auth_cipher_isw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_cipher_isw, Unset):
        json_auth_cipher_isw = []
        for auth_cipher_isw_item_data in auth_cipher_isw:
            auth_cipher_isw_item: Union[None, str]
            auth_cipher_isw_item = auth_cipher_isw_item_data
            json_auth_cipher_isw.append(auth_cipher_isw_item)

    params["auth_cipher__isw"] = json_auth_cipher_isw

    json_auth_cipher_n: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_cipher_n, Unset):
        json_auth_cipher_n = []
        for auth_cipher_n_item_data in auth_cipher_n:
            auth_cipher_n_item: Union[None, str]
            auth_cipher_n_item = auth_cipher_n_item_data
            json_auth_cipher_n.append(auth_cipher_n_item)

    params["auth_cipher__n"] = json_auth_cipher_n

    json_auth_cipher_nic: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_cipher_nic, Unset):
        json_auth_cipher_nic = []
        for auth_cipher_nic_item_data in auth_cipher_nic:
            auth_cipher_nic_item: Union[None, str]
            auth_cipher_nic_item = auth_cipher_nic_item_data
            json_auth_cipher_nic.append(auth_cipher_nic_item)

    params["auth_cipher__nic"] = json_auth_cipher_nic

    json_auth_cipher_nie: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_cipher_nie, Unset):
        json_auth_cipher_nie = []
        for auth_cipher_nie_item_data in auth_cipher_nie:
            auth_cipher_nie_item: Union[None, str]
            auth_cipher_nie_item = auth_cipher_nie_item_data
            json_auth_cipher_nie.append(auth_cipher_nie_item)

    params["auth_cipher__nie"] = json_auth_cipher_nie

    json_auth_cipher_niew: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_cipher_niew, Unset):
        json_auth_cipher_niew = []
        for auth_cipher_niew_item_data in auth_cipher_niew:
            auth_cipher_niew_item: Union[None, str]
            auth_cipher_niew_item = auth_cipher_niew_item_data
            json_auth_cipher_niew.append(auth_cipher_niew_item)

    params["auth_cipher__niew"] = json_auth_cipher_niew

    json_auth_cipher_nisw: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(auth_cipher_nisw, Unset):
        json_auth_cipher_nisw = []
        for auth_cipher_nisw_item_data in auth_cipher_nisw:
            auth_cipher_nisw_item: Union[None, str]
            auth_cipher_nisw_item = auth_cipher_nisw_item_data
            json_auth_cipher_nisw.append(auth_cipher_nisw_item)

    params["auth_cipher__nisw"] = json_auth_cipher_nisw

    json_auth_psk: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_psk, Unset):
        json_auth_psk = auth_psk

    params["auth_psk"] = json_auth_psk

    params["auth_psk__empty"] = auth_psk_empty

    json_auth_psk_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_psk_ic, Unset):
        json_auth_psk_ic = auth_psk_ic

    params["auth_psk__ic"] = json_auth_psk_ic

    json_auth_psk_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_psk_ie, Unset):
        json_auth_psk_ie = auth_psk_ie

    params["auth_psk__ie"] = json_auth_psk_ie

    json_auth_psk_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_psk_iew, Unset):
        json_auth_psk_iew = auth_psk_iew

    params["auth_psk__iew"] = json_auth_psk_iew

    json_auth_psk_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_psk_isw, Unset):
        json_auth_psk_isw = auth_psk_isw

    params["auth_psk__isw"] = json_auth_psk_isw

    json_auth_psk_n: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_psk_n, Unset):
        json_auth_psk_n = auth_psk_n

    params["auth_psk__n"] = json_auth_psk_n

    json_auth_psk_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_psk_nic, Unset):
        json_auth_psk_nic = auth_psk_nic

    params["auth_psk__nic"] = json_auth_psk_nic

    json_auth_psk_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_psk_nie, Unset):
        json_auth_psk_nie = auth_psk_nie

    params["auth_psk__nie"] = json_auth_psk_nie

    json_auth_psk_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_psk_niew, Unset):
        json_auth_psk_niew = auth_psk_niew

    params["auth_psk__niew"] = json_auth_psk_niew

    json_auth_psk_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(auth_psk_nisw, Unset):
        json_auth_psk_nisw = auth_psk_nisw

    params["auth_psk__nisw"] = json_auth_psk_nisw

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

    json_interface_a_id: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_a_id, Unset):
        json_interface_a_id = interface_a_id

    params["interface_a_id"] = json_interface_a_id

    json_interface_a_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_a_id_n, Unset):
        json_interface_a_id_n = interface_a_id_n

    params["interface_a_id__n"] = json_interface_a_id_n

    json_interface_b_id: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_b_id, Unset):
        json_interface_b_id = interface_b_id

    params["interface_b_id"] = json_interface_b_id

    json_interface_b_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_b_id_n, Unset):
        json_interface_b_id_n = interface_b_id_n

    params["interface_b_id__n"] = json_interface_b_id_n

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

    params["offset"] = offset

    params["ordering"] = ordering

    params["q"] = q

    json_ssid: Union[Unset, list[str]] = UNSET
    if not isinstance(ssid, Unset):
        json_ssid = ssid

    params["ssid"] = json_ssid

    params["ssid__empty"] = ssid_empty

    json_ssid_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(ssid_ic, Unset):
        json_ssid_ic = ssid_ic

    params["ssid__ic"] = json_ssid_ic

    json_ssid_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(ssid_ie, Unset):
        json_ssid_ie = ssid_ie

    params["ssid__ie"] = json_ssid_ie

    json_ssid_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(ssid_iew, Unset):
        json_ssid_iew = ssid_iew

    params["ssid__iew"] = json_ssid_iew

    json_ssid_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(ssid_isw, Unset):
        json_ssid_isw = ssid_isw

    params["ssid__isw"] = json_ssid_isw

    json_ssid_n: Union[Unset, list[str]] = UNSET
    if not isinstance(ssid_n, Unset):
        json_ssid_n = ssid_n

    params["ssid__n"] = json_ssid_n

    json_ssid_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(ssid_nic, Unset):
        json_ssid_nic = ssid_nic

    params["ssid__nic"] = json_ssid_nic

    json_ssid_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(ssid_nie, Unset):
        json_ssid_nie = ssid_nie

    params["ssid__nie"] = json_ssid_nie

    json_ssid_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(ssid_niew, Unset):
        json_ssid_niew = ssid_niew

    params["ssid__niew"] = json_ssid_niew

    json_ssid_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(ssid_nisw, Unset):
        json_ssid_nisw = ssid_nisw

    params["ssid__nisw"] = json_ssid_nisw

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

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/wireless/wireless-links/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedWirelessLinkList]:
    if response.status_code == 200:
        response_200 = PaginatedWirelessLinkList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedWirelessLinkList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    auth_cipher: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_empty: Union[Unset, bool] = UNSET,
    auth_cipher_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_n: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_psk: Union[Unset, list[str]] = UNSET,
    auth_psk_empty: Union[Unset, bool] = UNSET,
    auth_psk_ic: Union[Unset, list[str]] = UNSET,
    auth_psk_ie: Union[Unset, list[str]] = UNSET,
    auth_psk_iew: Union[Unset, list[str]] = UNSET,
    auth_psk_isw: Union[Unset, list[str]] = UNSET,
    auth_psk_n: Union[Unset, list[str]] = UNSET,
    auth_psk_nic: Union[Unset, list[str]] = UNSET,
    auth_psk_nie: Union[Unset, list[str]] = UNSET,
    auth_psk_niew: Union[Unset, list[str]] = UNSET,
    auth_psk_nisw: Union[Unset, list[str]] = UNSET,
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
    distance: Union[Unset, list[float]] = UNSET,
    distance_empty: Union[Unset, bool] = UNSET,
    distance_gt: Union[Unset, list[float]] = UNSET,
    distance_gte: Union[Unset, list[float]] = UNSET,
    distance_lt: Union[Unset, list[float]] = UNSET,
    distance_lte: Union[Unset, list[float]] = UNSET,
    distance_n: Union[Unset, list[float]] = UNSET,
    distance_unit: Union[Unset, WirelessWirelessLinksListDistanceUnit] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_a_id: Union[Unset, list[int]] = UNSET,
    interface_a_id_n: Union[Unset, list[int]] = UNSET,
    interface_b_id: Union[Unset, list[int]] = UNSET,
    interface_b_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    ssid: Union[Unset, list[str]] = UNSET,
    ssid_empty: Union[Unset, bool] = UNSET,
    ssid_ic: Union[Unset, list[str]] = UNSET,
    ssid_ie: Union[Unset, list[str]] = UNSET,
    ssid_iew: Union[Unset, list[str]] = UNSET,
    ssid_isw: Union[Unset, list[str]] = UNSET,
    ssid_n: Union[Unset, list[str]] = UNSET,
    ssid_nic: Union[Unset, list[str]] = UNSET,
    ssid_nie: Union[Unset, list[str]] = UNSET,
    ssid_niew: Union[Unset, list[str]] = UNSET,
    ssid_nisw: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedWirelessLinkList]:
    """Get a list of wireless link objects.

    Args:
        auth_cipher (Union[Unset, list[Union[None, str]]]):
        auth_cipher_empty (Union[Unset, bool]):
        auth_cipher_ic (Union[Unset, list[Union[None, str]]]):
        auth_cipher_ie (Union[Unset, list[Union[None, str]]]):
        auth_cipher_iew (Union[Unset, list[Union[None, str]]]):
        auth_cipher_isw (Union[Unset, list[Union[None, str]]]):
        auth_cipher_n (Union[Unset, list[Union[None, str]]]):
        auth_cipher_nic (Union[Unset, list[Union[None, str]]]):
        auth_cipher_nie (Union[Unset, list[Union[None, str]]]):
        auth_cipher_niew (Union[Unset, list[Union[None, str]]]):
        auth_cipher_nisw (Union[Unset, list[Union[None, str]]]):
        auth_psk (Union[Unset, list[str]]):
        auth_psk_empty (Union[Unset, bool]):
        auth_psk_ic (Union[Unset, list[str]]):
        auth_psk_ie (Union[Unset, list[str]]):
        auth_psk_iew (Union[Unset, list[str]]):
        auth_psk_isw (Union[Unset, list[str]]):
        auth_psk_n (Union[Unset, list[str]]):
        auth_psk_nic (Union[Unset, list[str]]):
        auth_psk_nie (Union[Unset, list[str]]):
        auth_psk_niew (Union[Unset, list[str]]):
        auth_psk_nisw (Union[Unset, list[str]]):
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
        distance (Union[Unset, list[float]]):
        distance_empty (Union[Unset, bool]):
        distance_gt (Union[Unset, list[float]]):
        distance_gte (Union[Unset, list[float]]):
        distance_lt (Union[Unset, list[float]]):
        distance_lte (Union[Unset, list[float]]):
        distance_n (Union[Unset, list[float]]):
        distance_unit (Union[Unset, WirelessWirelessLinksListDistanceUnit]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_a_id (Union[Unset, list[int]]):
        interface_a_id_n (Union[Unset, list[int]]):
        interface_b_id (Union[Unset, list[int]]):
        interface_b_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        ssid (Union[Unset, list[str]]):
        ssid_empty (Union[Unset, bool]):
        ssid_ic (Union[Unset, list[str]]):
        ssid_ie (Union[Unset, list[str]]):
        ssid_iew (Union[Unset, list[str]]):
        ssid_isw (Union[Unset, list[str]]):
        ssid_n (Union[Unset, list[str]]):
        ssid_nic (Union[Unset, list[str]]):
        ssid_nie (Union[Unset, list[str]]):
        ssid_niew (Union[Unset, list[str]]):
        ssid_nisw (Union[Unset, list[str]]):
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
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWirelessLinkList]
    """

    kwargs = _get_kwargs(
        auth_cipher=auth_cipher,
        auth_cipher_empty=auth_cipher_empty,
        auth_cipher_ic=auth_cipher_ic,
        auth_cipher_ie=auth_cipher_ie,
        auth_cipher_iew=auth_cipher_iew,
        auth_cipher_isw=auth_cipher_isw,
        auth_cipher_n=auth_cipher_n,
        auth_cipher_nic=auth_cipher_nic,
        auth_cipher_nie=auth_cipher_nie,
        auth_cipher_niew=auth_cipher_niew,
        auth_cipher_nisw=auth_cipher_nisw,
        auth_psk=auth_psk,
        auth_psk_empty=auth_psk_empty,
        auth_psk_ic=auth_psk_ic,
        auth_psk_ie=auth_psk_ie,
        auth_psk_iew=auth_psk_iew,
        auth_psk_isw=auth_psk_isw,
        auth_psk_n=auth_psk_n,
        auth_psk_nic=auth_psk_nic,
        auth_psk_nie=auth_psk_nie,
        auth_psk_niew=auth_psk_niew,
        auth_psk_nisw=auth_psk_nisw,
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
        interface_a_id=interface_a_id,
        interface_a_id_n=interface_a_id_n,
        interface_b_id=interface_b_id,
        interface_b_id_n=interface_b_id_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        q=q,
        ssid=ssid,
        ssid_empty=ssid_empty,
        ssid_ic=ssid_ic,
        ssid_ie=ssid_ie,
        ssid_iew=ssid_iew,
        ssid_isw=ssid_isw,
        ssid_n=ssid_n,
        ssid_nic=ssid_nic,
        ssid_nie=ssid_nie,
        ssid_niew=ssid_niew,
        ssid_nisw=ssid_nisw,
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
        updated_by_request=updated_by_request,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    auth_cipher: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_empty: Union[Unset, bool] = UNSET,
    auth_cipher_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_n: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_psk: Union[Unset, list[str]] = UNSET,
    auth_psk_empty: Union[Unset, bool] = UNSET,
    auth_psk_ic: Union[Unset, list[str]] = UNSET,
    auth_psk_ie: Union[Unset, list[str]] = UNSET,
    auth_psk_iew: Union[Unset, list[str]] = UNSET,
    auth_psk_isw: Union[Unset, list[str]] = UNSET,
    auth_psk_n: Union[Unset, list[str]] = UNSET,
    auth_psk_nic: Union[Unset, list[str]] = UNSET,
    auth_psk_nie: Union[Unset, list[str]] = UNSET,
    auth_psk_niew: Union[Unset, list[str]] = UNSET,
    auth_psk_nisw: Union[Unset, list[str]] = UNSET,
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
    distance: Union[Unset, list[float]] = UNSET,
    distance_empty: Union[Unset, bool] = UNSET,
    distance_gt: Union[Unset, list[float]] = UNSET,
    distance_gte: Union[Unset, list[float]] = UNSET,
    distance_lt: Union[Unset, list[float]] = UNSET,
    distance_lte: Union[Unset, list[float]] = UNSET,
    distance_n: Union[Unset, list[float]] = UNSET,
    distance_unit: Union[Unset, WirelessWirelessLinksListDistanceUnit] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_a_id: Union[Unset, list[int]] = UNSET,
    interface_a_id_n: Union[Unset, list[int]] = UNSET,
    interface_b_id: Union[Unset, list[int]] = UNSET,
    interface_b_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    ssid: Union[Unset, list[str]] = UNSET,
    ssid_empty: Union[Unset, bool] = UNSET,
    ssid_ic: Union[Unset, list[str]] = UNSET,
    ssid_ie: Union[Unset, list[str]] = UNSET,
    ssid_iew: Union[Unset, list[str]] = UNSET,
    ssid_isw: Union[Unset, list[str]] = UNSET,
    ssid_n: Union[Unset, list[str]] = UNSET,
    ssid_nic: Union[Unset, list[str]] = UNSET,
    ssid_nie: Union[Unset, list[str]] = UNSET,
    ssid_niew: Union[Unset, list[str]] = UNSET,
    ssid_nisw: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedWirelessLinkList]:
    """Get a list of wireless link objects.

    Args:
        auth_cipher (Union[Unset, list[Union[None, str]]]):
        auth_cipher_empty (Union[Unset, bool]):
        auth_cipher_ic (Union[Unset, list[Union[None, str]]]):
        auth_cipher_ie (Union[Unset, list[Union[None, str]]]):
        auth_cipher_iew (Union[Unset, list[Union[None, str]]]):
        auth_cipher_isw (Union[Unset, list[Union[None, str]]]):
        auth_cipher_n (Union[Unset, list[Union[None, str]]]):
        auth_cipher_nic (Union[Unset, list[Union[None, str]]]):
        auth_cipher_nie (Union[Unset, list[Union[None, str]]]):
        auth_cipher_niew (Union[Unset, list[Union[None, str]]]):
        auth_cipher_nisw (Union[Unset, list[Union[None, str]]]):
        auth_psk (Union[Unset, list[str]]):
        auth_psk_empty (Union[Unset, bool]):
        auth_psk_ic (Union[Unset, list[str]]):
        auth_psk_ie (Union[Unset, list[str]]):
        auth_psk_iew (Union[Unset, list[str]]):
        auth_psk_isw (Union[Unset, list[str]]):
        auth_psk_n (Union[Unset, list[str]]):
        auth_psk_nic (Union[Unset, list[str]]):
        auth_psk_nie (Union[Unset, list[str]]):
        auth_psk_niew (Union[Unset, list[str]]):
        auth_psk_nisw (Union[Unset, list[str]]):
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
        distance (Union[Unset, list[float]]):
        distance_empty (Union[Unset, bool]):
        distance_gt (Union[Unset, list[float]]):
        distance_gte (Union[Unset, list[float]]):
        distance_lt (Union[Unset, list[float]]):
        distance_lte (Union[Unset, list[float]]):
        distance_n (Union[Unset, list[float]]):
        distance_unit (Union[Unset, WirelessWirelessLinksListDistanceUnit]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_a_id (Union[Unset, list[int]]):
        interface_a_id_n (Union[Unset, list[int]]):
        interface_b_id (Union[Unset, list[int]]):
        interface_b_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        ssid (Union[Unset, list[str]]):
        ssid_empty (Union[Unset, bool]):
        ssid_ic (Union[Unset, list[str]]):
        ssid_ie (Union[Unset, list[str]]):
        ssid_iew (Union[Unset, list[str]]):
        ssid_isw (Union[Unset, list[str]]):
        ssid_n (Union[Unset, list[str]]):
        ssid_nic (Union[Unset, list[str]]):
        ssid_nie (Union[Unset, list[str]]):
        ssid_niew (Union[Unset, list[str]]):
        ssid_nisw (Union[Unset, list[str]]):
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
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWirelessLinkList
    """

    return sync_detailed(
        client=client,
        auth_cipher=auth_cipher,
        auth_cipher_empty=auth_cipher_empty,
        auth_cipher_ic=auth_cipher_ic,
        auth_cipher_ie=auth_cipher_ie,
        auth_cipher_iew=auth_cipher_iew,
        auth_cipher_isw=auth_cipher_isw,
        auth_cipher_n=auth_cipher_n,
        auth_cipher_nic=auth_cipher_nic,
        auth_cipher_nie=auth_cipher_nie,
        auth_cipher_niew=auth_cipher_niew,
        auth_cipher_nisw=auth_cipher_nisw,
        auth_psk=auth_psk,
        auth_psk_empty=auth_psk_empty,
        auth_psk_ic=auth_psk_ic,
        auth_psk_ie=auth_psk_ie,
        auth_psk_iew=auth_psk_iew,
        auth_psk_isw=auth_psk_isw,
        auth_psk_n=auth_psk_n,
        auth_psk_nic=auth_psk_nic,
        auth_psk_nie=auth_psk_nie,
        auth_psk_niew=auth_psk_niew,
        auth_psk_nisw=auth_psk_nisw,
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
        interface_a_id=interface_a_id,
        interface_a_id_n=interface_a_id_n,
        interface_b_id=interface_b_id,
        interface_b_id_n=interface_b_id_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        q=q,
        ssid=ssid,
        ssid_empty=ssid_empty,
        ssid_ic=ssid_ic,
        ssid_ie=ssid_ie,
        ssid_iew=ssid_iew,
        ssid_isw=ssid_isw,
        ssid_n=ssid_n,
        ssid_nic=ssid_nic,
        ssid_nie=ssid_nie,
        ssid_niew=ssid_niew,
        ssid_nisw=ssid_nisw,
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
        updated_by_request=updated_by_request,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    auth_cipher: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_empty: Union[Unset, bool] = UNSET,
    auth_cipher_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_n: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_psk: Union[Unset, list[str]] = UNSET,
    auth_psk_empty: Union[Unset, bool] = UNSET,
    auth_psk_ic: Union[Unset, list[str]] = UNSET,
    auth_psk_ie: Union[Unset, list[str]] = UNSET,
    auth_psk_iew: Union[Unset, list[str]] = UNSET,
    auth_psk_isw: Union[Unset, list[str]] = UNSET,
    auth_psk_n: Union[Unset, list[str]] = UNSET,
    auth_psk_nic: Union[Unset, list[str]] = UNSET,
    auth_psk_nie: Union[Unset, list[str]] = UNSET,
    auth_psk_niew: Union[Unset, list[str]] = UNSET,
    auth_psk_nisw: Union[Unset, list[str]] = UNSET,
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
    distance: Union[Unset, list[float]] = UNSET,
    distance_empty: Union[Unset, bool] = UNSET,
    distance_gt: Union[Unset, list[float]] = UNSET,
    distance_gte: Union[Unset, list[float]] = UNSET,
    distance_lt: Union[Unset, list[float]] = UNSET,
    distance_lte: Union[Unset, list[float]] = UNSET,
    distance_n: Union[Unset, list[float]] = UNSET,
    distance_unit: Union[Unset, WirelessWirelessLinksListDistanceUnit] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_a_id: Union[Unset, list[int]] = UNSET,
    interface_a_id_n: Union[Unset, list[int]] = UNSET,
    interface_b_id: Union[Unset, list[int]] = UNSET,
    interface_b_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    ssid: Union[Unset, list[str]] = UNSET,
    ssid_empty: Union[Unset, bool] = UNSET,
    ssid_ic: Union[Unset, list[str]] = UNSET,
    ssid_ie: Union[Unset, list[str]] = UNSET,
    ssid_iew: Union[Unset, list[str]] = UNSET,
    ssid_isw: Union[Unset, list[str]] = UNSET,
    ssid_n: Union[Unset, list[str]] = UNSET,
    ssid_nic: Union[Unset, list[str]] = UNSET,
    ssid_nie: Union[Unset, list[str]] = UNSET,
    ssid_niew: Union[Unset, list[str]] = UNSET,
    ssid_nisw: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedWirelessLinkList]:
    """Get a list of wireless link objects.

    Args:
        auth_cipher (Union[Unset, list[Union[None, str]]]):
        auth_cipher_empty (Union[Unset, bool]):
        auth_cipher_ic (Union[Unset, list[Union[None, str]]]):
        auth_cipher_ie (Union[Unset, list[Union[None, str]]]):
        auth_cipher_iew (Union[Unset, list[Union[None, str]]]):
        auth_cipher_isw (Union[Unset, list[Union[None, str]]]):
        auth_cipher_n (Union[Unset, list[Union[None, str]]]):
        auth_cipher_nic (Union[Unset, list[Union[None, str]]]):
        auth_cipher_nie (Union[Unset, list[Union[None, str]]]):
        auth_cipher_niew (Union[Unset, list[Union[None, str]]]):
        auth_cipher_nisw (Union[Unset, list[Union[None, str]]]):
        auth_psk (Union[Unset, list[str]]):
        auth_psk_empty (Union[Unset, bool]):
        auth_psk_ic (Union[Unset, list[str]]):
        auth_psk_ie (Union[Unset, list[str]]):
        auth_psk_iew (Union[Unset, list[str]]):
        auth_psk_isw (Union[Unset, list[str]]):
        auth_psk_n (Union[Unset, list[str]]):
        auth_psk_nic (Union[Unset, list[str]]):
        auth_psk_nie (Union[Unset, list[str]]):
        auth_psk_niew (Union[Unset, list[str]]):
        auth_psk_nisw (Union[Unset, list[str]]):
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
        distance (Union[Unset, list[float]]):
        distance_empty (Union[Unset, bool]):
        distance_gt (Union[Unset, list[float]]):
        distance_gte (Union[Unset, list[float]]):
        distance_lt (Union[Unset, list[float]]):
        distance_lte (Union[Unset, list[float]]):
        distance_n (Union[Unset, list[float]]):
        distance_unit (Union[Unset, WirelessWirelessLinksListDistanceUnit]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_a_id (Union[Unset, list[int]]):
        interface_a_id_n (Union[Unset, list[int]]):
        interface_b_id (Union[Unset, list[int]]):
        interface_b_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        ssid (Union[Unset, list[str]]):
        ssid_empty (Union[Unset, bool]):
        ssid_ic (Union[Unset, list[str]]):
        ssid_ie (Union[Unset, list[str]]):
        ssid_iew (Union[Unset, list[str]]):
        ssid_isw (Union[Unset, list[str]]):
        ssid_n (Union[Unset, list[str]]):
        ssid_nic (Union[Unset, list[str]]):
        ssid_nie (Union[Unset, list[str]]):
        ssid_niew (Union[Unset, list[str]]):
        ssid_nisw (Union[Unset, list[str]]):
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
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedWirelessLinkList]
    """

    kwargs = _get_kwargs(
        auth_cipher=auth_cipher,
        auth_cipher_empty=auth_cipher_empty,
        auth_cipher_ic=auth_cipher_ic,
        auth_cipher_ie=auth_cipher_ie,
        auth_cipher_iew=auth_cipher_iew,
        auth_cipher_isw=auth_cipher_isw,
        auth_cipher_n=auth_cipher_n,
        auth_cipher_nic=auth_cipher_nic,
        auth_cipher_nie=auth_cipher_nie,
        auth_cipher_niew=auth_cipher_niew,
        auth_cipher_nisw=auth_cipher_nisw,
        auth_psk=auth_psk,
        auth_psk_empty=auth_psk_empty,
        auth_psk_ic=auth_psk_ic,
        auth_psk_ie=auth_psk_ie,
        auth_psk_iew=auth_psk_iew,
        auth_psk_isw=auth_psk_isw,
        auth_psk_n=auth_psk_n,
        auth_psk_nic=auth_psk_nic,
        auth_psk_nie=auth_psk_nie,
        auth_psk_niew=auth_psk_niew,
        auth_psk_nisw=auth_psk_nisw,
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
        interface_a_id=interface_a_id,
        interface_a_id_n=interface_a_id_n,
        interface_b_id=interface_b_id,
        interface_b_id_n=interface_b_id_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        q=q,
        ssid=ssid,
        ssid_empty=ssid_empty,
        ssid_ic=ssid_ic,
        ssid_ie=ssid_ie,
        ssid_iew=ssid_iew,
        ssid_isw=ssid_isw,
        ssid_n=ssid_n,
        ssid_nic=ssid_nic,
        ssid_nie=ssid_nie,
        ssid_niew=ssid_niew,
        ssid_nisw=ssid_nisw,
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
        updated_by_request=updated_by_request,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    auth_cipher: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_empty: Union[Unset, bool] = UNSET,
    auth_cipher_ic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_ie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_iew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_isw: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_n: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_nic: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_nie: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_niew: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_cipher_nisw: Union[Unset, list[Union[None, str]]] = UNSET,
    auth_psk: Union[Unset, list[str]] = UNSET,
    auth_psk_empty: Union[Unset, bool] = UNSET,
    auth_psk_ic: Union[Unset, list[str]] = UNSET,
    auth_psk_ie: Union[Unset, list[str]] = UNSET,
    auth_psk_iew: Union[Unset, list[str]] = UNSET,
    auth_psk_isw: Union[Unset, list[str]] = UNSET,
    auth_psk_n: Union[Unset, list[str]] = UNSET,
    auth_psk_nic: Union[Unset, list[str]] = UNSET,
    auth_psk_nie: Union[Unset, list[str]] = UNSET,
    auth_psk_niew: Union[Unset, list[str]] = UNSET,
    auth_psk_nisw: Union[Unset, list[str]] = UNSET,
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
    distance: Union[Unset, list[float]] = UNSET,
    distance_empty: Union[Unset, bool] = UNSET,
    distance_gt: Union[Unset, list[float]] = UNSET,
    distance_gte: Union[Unset, list[float]] = UNSET,
    distance_lt: Union[Unset, list[float]] = UNSET,
    distance_lte: Union[Unset, list[float]] = UNSET,
    distance_n: Union[Unset, list[float]] = UNSET,
    distance_unit: Union[Unset, WirelessWirelessLinksListDistanceUnit] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_a_id: Union[Unset, list[int]] = UNSET,
    interface_a_id_n: Union[Unset, list[int]] = UNSET,
    interface_b_id: Union[Unset, list[int]] = UNSET,
    interface_b_id_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    q: Union[Unset, str] = UNSET,
    ssid: Union[Unset, list[str]] = UNSET,
    ssid_empty: Union[Unset, bool] = UNSET,
    ssid_ic: Union[Unset, list[str]] = UNSET,
    ssid_ie: Union[Unset, list[str]] = UNSET,
    ssid_iew: Union[Unset, list[str]] = UNSET,
    ssid_isw: Union[Unset, list[str]] = UNSET,
    ssid_n: Union[Unset, list[str]] = UNSET,
    ssid_nic: Union[Unset, list[str]] = UNSET,
    ssid_nie: Union[Unset, list[str]] = UNSET,
    ssid_niew: Union[Unset, list[str]] = UNSET,
    ssid_nisw: Union[Unset, list[str]] = UNSET,
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
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedWirelessLinkList]:
    """Get a list of wireless link objects.

    Args:
        auth_cipher (Union[Unset, list[Union[None, str]]]):
        auth_cipher_empty (Union[Unset, bool]):
        auth_cipher_ic (Union[Unset, list[Union[None, str]]]):
        auth_cipher_ie (Union[Unset, list[Union[None, str]]]):
        auth_cipher_iew (Union[Unset, list[Union[None, str]]]):
        auth_cipher_isw (Union[Unset, list[Union[None, str]]]):
        auth_cipher_n (Union[Unset, list[Union[None, str]]]):
        auth_cipher_nic (Union[Unset, list[Union[None, str]]]):
        auth_cipher_nie (Union[Unset, list[Union[None, str]]]):
        auth_cipher_niew (Union[Unset, list[Union[None, str]]]):
        auth_cipher_nisw (Union[Unset, list[Union[None, str]]]):
        auth_psk (Union[Unset, list[str]]):
        auth_psk_empty (Union[Unset, bool]):
        auth_psk_ic (Union[Unset, list[str]]):
        auth_psk_ie (Union[Unset, list[str]]):
        auth_psk_iew (Union[Unset, list[str]]):
        auth_psk_isw (Union[Unset, list[str]]):
        auth_psk_n (Union[Unset, list[str]]):
        auth_psk_nic (Union[Unset, list[str]]):
        auth_psk_nie (Union[Unset, list[str]]):
        auth_psk_niew (Union[Unset, list[str]]):
        auth_psk_nisw (Union[Unset, list[str]]):
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
        distance (Union[Unset, list[float]]):
        distance_empty (Union[Unset, bool]):
        distance_gt (Union[Unset, list[float]]):
        distance_gte (Union[Unset, list[float]]):
        distance_lt (Union[Unset, list[float]]):
        distance_lte (Union[Unset, list[float]]):
        distance_n (Union[Unset, list[float]]):
        distance_unit (Union[Unset, WirelessWirelessLinksListDistanceUnit]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_a_id (Union[Unset, list[int]]):
        interface_a_id_n (Union[Unset, list[int]]):
        interface_b_id (Union[Unset, list[int]]):
        interface_b_id_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        q (Union[Unset, str]):
        ssid (Union[Unset, list[str]]):
        ssid_empty (Union[Unset, bool]):
        ssid_ic (Union[Unset, list[str]]):
        ssid_ie (Union[Unset, list[str]]):
        ssid_iew (Union[Unset, list[str]]):
        ssid_isw (Union[Unset, list[str]]):
        ssid_n (Union[Unset, list[str]]):
        ssid_nic (Union[Unset, list[str]]):
        ssid_nie (Union[Unset, list[str]]):
        ssid_niew (Union[Unset, list[str]]):
        ssid_nisw (Union[Unset, list[str]]):
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
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedWirelessLinkList
    """

    return (
        await asyncio_detailed(
            client=client,
            auth_cipher=auth_cipher,
            auth_cipher_empty=auth_cipher_empty,
            auth_cipher_ic=auth_cipher_ic,
            auth_cipher_ie=auth_cipher_ie,
            auth_cipher_iew=auth_cipher_iew,
            auth_cipher_isw=auth_cipher_isw,
            auth_cipher_n=auth_cipher_n,
            auth_cipher_nic=auth_cipher_nic,
            auth_cipher_nie=auth_cipher_nie,
            auth_cipher_niew=auth_cipher_niew,
            auth_cipher_nisw=auth_cipher_nisw,
            auth_psk=auth_psk,
            auth_psk_empty=auth_psk_empty,
            auth_psk_ic=auth_psk_ic,
            auth_psk_ie=auth_psk_ie,
            auth_psk_iew=auth_psk_iew,
            auth_psk_isw=auth_psk_isw,
            auth_psk_n=auth_psk_n,
            auth_psk_nic=auth_psk_nic,
            auth_psk_nie=auth_psk_nie,
            auth_psk_niew=auth_psk_niew,
            auth_psk_nisw=auth_psk_nisw,
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
            interface_a_id=interface_a_id,
            interface_a_id_n=interface_a_id_n,
            interface_b_id=interface_b_id,
            interface_b_id_n=interface_b_id_n,
            last_updated=last_updated,
            last_updated_empty=last_updated_empty,
            last_updated_gt=last_updated_gt,
            last_updated_gte=last_updated_gte,
            last_updated_lt=last_updated_lt,
            last_updated_lte=last_updated_lte,
            last_updated_n=last_updated_n,
            limit=limit,
            modified_by_request=modified_by_request,
            offset=offset,
            ordering=ordering,
            q=q,
            ssid=ssid,
            ssid_empty=ssid_empty,
            ssid_ic=ssid_ic,
            ssid_ie=ssid_ie,
            ssid_iew=ssid_iew,
            ssid_isw=ssid_isw,
            ssid_n=ssid_n,
            ssid_nic=ssid_nic,
            ssid_nie=ssid_nie,
            ssid_niew=ssid_niew,
            ssid_nisw=ssid_nisw,
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
            updated_by_request=updated_by_request,
        )
    ).parsed
