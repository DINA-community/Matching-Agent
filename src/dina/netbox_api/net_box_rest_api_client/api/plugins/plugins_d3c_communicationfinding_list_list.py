import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_communication_finding_list import PaginatedCommunicationFindingList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    application_protocol: Union[Unset, list[str]] = UNSET,
    application_protocol_empty: Union[Unset, bool] = UNSET,
    application_protocol_ic: Union[Unset, list[str]] = UNSET,
    application_protocol_ie: Union[Unset, list[str]] = UNSET,
    application_protocol_iew: Union[Unset, list[str]] = UNSET,
    application_protocol_isw: Union[Unset, list[str]] = UNSET,
    application_protocol_n: Union[Unset, list[str]] = UNSET,
    application_protocol_nic: Union[Unset, list[str]] = UNSET,
    application_protocol_nie: Union[Unset, list[str]] = UNSET,
    application_protocol_niew: Union[Unset, list[str]] = UNSET,
    application_protocol_nisw: Union[Unset, list[str]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    destination_ip: Union[Unset, list[str]] = UNSET,
    destination_ip_empty: Union[Unset, bool] = UNSET,
    destination_ip_ic: Union[Unset, list[str]] = UNSET,
    destination_ip_ie: Union[Unset, list[str]] = UNSET,
    destination_ip_iew: Union[Unset, list[str]] = UNSET,
    destination_ip_isw: Union[Unset, list[str]] = UNSET,
    destination_ip_n: Union[Unset, list[str]] = UNSET,
    destination_ip_nic: Union[Unset, list[str]] = UNSET,
    destination_ip_nie: Union[Unset, list[str]] = UNSET,
    destination_ip_niew: Union[Unset, list[str]] = UNSET,
    destination_ip_nisw: Union[Unset, list[str]] = UNSET,
    destination_port: Union[Unset, list[str]] = UNSET,
    destination_port_empty: Union[Unset, bool] = UNSET,
    destination_port_ic: Union[Unset, list[str]] = UNSET,
    destination_port_ie: Union[Unset, list[str]] = UNSET,
    destination_port_iew: Union[Unset, list[str]] = UNSET,
    destination_port_isw: Union[Unset, list[str]] = UNSET,
    destination_port_n: Union[Unset, list[str]] = UNSET,
    destination_port_nic: Union[Unset, list[str]] = UNSET,
    destination_port_nie: Union[Unset, list[str]] = UNSET,
    destination_port_niew: Union[Unset, list[str]] = UNSET,
    destination_port_nisw: Union[Unset, list[str]] = UNSET,
    has_2_predicted_devices: Union[Unset, bool] = UNSET,
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
    network_protocol: Union[Unset, list[str]] = UNSET,
    network_protocol_empty: Union[Unset, bool] = UNSET,
    network_protocol_ic: Union[Unset, list[str]] = UNSET,
    network_protocol_ie: Union[Unset, list[str]] = UNSET,
    network_protocol_iew: Union[Unset, list[str]] = UNSET,
    network_protocol_isw: Union[Unset, list[str]] = UNSET,
    network_protocol_n: Union[Unset, list[str]] = UNSET,
    network_protocol_nic: Union[Unset, list[str]] = UNSET,
    network_protocol_nie: Union[Unset, list[str]] = UNSET,
    network_protocol_niew: Union[Unset, list[str]] = UNSET,
    network_protocol_nisw: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    predicted_dst_device: Union[Unset, int] = UNSET,
    predicted_dst_device_n: Union[Unset, int] = UNSET,
    predicted_src_device: Union[Unset, int] = UNSET,
    predicted_src_device_n: Union[Unset, int] = UNSET,
    q: Union[Unset, str] = UNSET,
    source_ip: Union[Unset, list[str]] = UNSET,
    source_ip_empty: Union[Unset, bool] = UNSET,
    source_ip_ic: Union[Unset, list[str]] = UNSET,
    source_ip_ie: Union[Unset, list[str]] = UNSET,
    source_ip_iew: Union[Unset, list[str]] = UNSET,
    source_ip_isw: Union[Unset, list[str]] = UNSET,
    source_ip_n: Union[Unset, list[str]] = UNSET,
    source_ip_nic: Union[Unset, list[str]] = UNSET,
    source_ip_nie: Union[Unset, list[str]] = UNSET,
    source_ip_niew: Union[Unset, list[str]] = UNSET,
    source_ip_nisw: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    transport_protocol: Union[Unset, list[str]] = UNSET,
    transport_protocol_empty: Union[Unset, bool] = UNSET,
    transport_protocol_ic: Union[Unset, list[str]] = UNSET,
    transport_protocol_ie: Union[Unset, list[str]] = UNSET,
    transport_protocol_iew: Union[Unset, list[str]] = UNSET,
    transport_protocol_isw: Union[Unset, list[str]] = UNSET,
    transport_protocol_n: Union[Unset, list[str]] = UNSET,
    transport_protocol_nic: Union[Unset, list[str]] = UNSET,
    transport_protocol_nie: Union[Unset, list[str]] = UNSET,
    transport_protocol_niew: Union[Unset, list[str]] = UNSET,
    transport_protocol_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_application_protocol: Union[Unset, list[str]] = UNSET
    if not isinstance(application_protocol, Unset):
        json_application_protocol = application_protocol

    params["application_protocol"] = json_application_protocol

    params["application_protocol__empty"] = application_protocol_empty

    json_application_protocol_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(application_protocol_ic, Unset):
        json_application_protocol_ic = application_protocol_ic

    params["application_protocol__ic"] = json_application_protocol_ic

    json_application_protocol_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(application_protocol_ie, Unset):
        json_application_protocol_ie = application_protocol_ie

    params["application_protocol__ie"] = json_application_protocol_ie

    json_application_protocol_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(application_protocol_iew, Unset):
        json_application_protocol_iew = application_protocol_iew

    params["application_protocol__iew"] = json_application_protocol_iew

    json_application_protocol_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(application_protocol_isw, Unset):
        json_application_protocol_isw = application_protocol_isw

    params["application_protocol__isw"] = json_application_protocol_isw

    json_application_protocol_n: Union[Unset, list[str]] = UNSET
    if not isinstance(application_protocol_n, Unset):
        json_application_protocol_n = application_protocol_n

    params["application_protocol__n"] = json_application_protocol_n

    json_application_protocol_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(application_protocol_nic, Unset):
        json_application_protocol_nic = application_protocol_nic

    params["application_protocol__nic"] = json_application_protocol_nic

    json_application_protocol_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(application_protocol_nie, Unset):
        json_application_protocol_nie = application_protocol_nie

    params["application_protocol__nie"] = json_application_protocol_nie

    json_application_protocol_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(application_protocol_niew, Unset):
        json_application_protocol_niew = application_protocol_niew

    params["application_protocol__niew"] = json_application_protocol_niew

    json_application_protocol_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(application_protocol_nisw, Unset):
        json_application_protocol_nisw = application_protocol_nisw

    params["application_protocol__nisw"] = json_application_protocol_nisw

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

    json_destination_ip: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_ip, Unset):
        json_destination_ip = destination_ip

    params["destination_ip"] = json_destination_ip

    params["destination_ip__empty"] = destination_ip_empty

    json_destination_ip_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_ip_ic, Unset):
        json_destination_ip_ic = destination_ip_ic

    params["destination_ip__ic"] = json_destination_ip_ic

    json_destination_ip_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_ip_ie, Unset):
        json_destination_ip_ie = destination_ip_ie

    params["destination_ip__ie"] = json_destination_ip_ie

    json_destination_ip_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_ip_iew, Unset):
        json_destination_ip_iew = destination_ip_iew

    params["destination_ip__iew"] = json_destination_ip_iew

    json_destination_ip_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_ip_isw, Unset):
        json_destination_ip_isw = destination_ip_isw

    params["destination_ip__isw"] = json_destination_ip_isw

    json_destination_ip_n: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_ip_n, Unset):
        json_destination_ip_n = destination_ip_n

    params["destination_ip__n"] = json_destination_ip_n

    json_destination_ip_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_ip_nic, Unset):
        json_destination_ip_nic = destination_ip_nic

    params["destination_ip__nic"] = json_destination_ip_nic

    json_destination_ip_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_ip_nie, Unset):
        json_destination_ip_nie = destination_ip_nie

    params["destination_ip__nie"] = json_destination_ip_nie

    json_destination_ip_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_ip_niew, Unset):
        json_destination_ip_niew = destination_ip_niew

    params["destination_ip__niew"] = json_destination_ip_niew

    json_destination_ip_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_ip_nisw, Unset):
        json_destination_ip_nisw = destination_ip_nisw

    params["destination_ip__nisw"] = json_destination_ip_nisw

    json_destination_port: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_port, Unset):
        json_destination_port = destination_port

    params["destination_port"] = json_destination_port

    params["destination_port__empty"] = destination_port_empty

    json_destination_port_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_port_ic, Unset):
        json_destination_port_ic = destination_port_ic

    params["destination_port__ic"] = json_destination_port_ic

    json_destination_port_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_port_ie, Unset):
        json_destination_port_ie = destination_port_ie

    params["destination_port__ie"] = json_destination_port_ie

    json_destination_port_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_port_iew, Unset):
        json_destination_port_iew = destination_port_iew

    params["destination_port__iew"] = json_destination_port_iew

    json_destination_port_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_port_isw, Unset):
        json_destination_port_isw = destination_port_isw

    params["destination_port__isw"] = json_destination_port_isw

    json_destination_port_n: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_port_n, Unset):
        json_destination_port_n = destination_port_n

    params["destination_port__n"] = json_destination_port_n

    json_destination_port_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_port_nic, Unset):
        json_destination_port_nic = destination_port_nic

    params["destination_port__nic"] = json_destination_port_nic

    json_destination_port_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_port_nie, Unset):
        json_destination_port_nie = destination_port_nie

    params["destination_port__nie"] = json_destination_port_nie

    json_destination_port_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_port_niew, Unset):
        json_destination_port_niew = destination_port_niew

    params["destination_port__niew"] = json_destination_port_niew

    json_destination_port_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(destination_port_nisw, Unset):
        json_destination_port_nisw = destination_port_nisw

    params["destination_port__nisw"] = json_destination_port_nisw

    params["has_2_predicted_devices"] = has_2_predicted_devices

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

    json_network_protocol: Union[Unset, list[str]] = UNSET
    if not isinstance(network_protocol, Unset):
        json_network_protocol = network_protocol

    params["network_protocol"] = json_network_protocol

    params["network_protocol__empty"] = network_protocol_empty

    json_network_protocol_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(network_protocol_ic, Unset):
        json_network_protocol_ic = network_protocol_ic

    params["network_protocol__ic"] = json_network_protocol_ic

    json_network_protocol_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(network_protocol_ie, Unset):
        json_network_protocol_ie = network_protocol_ie

    params["network_protocol__ie"] = json_network_protocol_ie

    json_network_protocol_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(network_protocol_iew, Unset):
        json_network_protocol_iew = network_protocol_iew

    params["network_protocol__iew"] = json_network_protocol_iew

    json_network_protocol_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(network_protocol_isw, Unset):
        json_network_protocol_isw = network_protocol_isw

    params["network_protocol__isw"] = json_network_protocol_isw

    json_network_protocol_n: Union[Unset, list[str]] = UNSET
    if not isinstance(network_protocol_n, Unset):
        json_network_protocol_n = network_protocol_n

    params["network_protocol__n"] = json_network_protocol_n

    json_network_protocol_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(network_protocol_nic, Unset):
        json_network_protocol_nic = network_protocol_nic

    params["network_protocol__nic"] = json_network_protocol_nic

    json_network_protocol_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(network_protocol_nie, Unset):
        json_network_protocol_nie = network_protocol_nie

    params["network_protocol__nie"] = json_network_protocol_nie

    json_network_protocol_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(network_protocol_niew, Unset):
        json_network_protocol_niew = network_protocol_niew

    params["network_protocol__niew"] = json_network_protocol_niew

    json_network_protocol_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(network_protocol_nisw, Unset):
        json_network_protocol_nisw = network_protocol_nisw

    params["network_protocol__nisw"] = json_network_protocol_nisw

    params["offset"] = offset

    params["ordering"] = ordering

    params["predicted_dst_device"] = predicted_dst_device

    params["predicted_dst_device__n"] = predicted_dst_device_n

    params["predicted_src_device"] = predicted_src_device

    params["predicted_src_device__n"] = predicted_src_device_n

    params["q"] = q

    json_source_ip: Union[Unset, list[str]] = UNSET
    if not isinstance(source_ip, Unset):
        json_source_ip = source_ip

    params["source_ip"] = json_source_ip

    params["source_ip__empty"] = source_ip_empty

    json_source_ip_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(source_ip_ic, Unset):
        json_source_ip_ic = source_ip_ic

    params["source_ip__ic"] = json_source_ip_ic

    json_source_ip_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(source_ip_ie, Unset):
        json_source_ip_ie = source_ip_ie

    params["source_ip__ie"] = json_source_ip_ie

    json_source_ip_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(source_ip_iew, Unset):
        json_source_ip_iew = source_ip_iew

    params["source_ip__iew"] = json_source_ip_iew

    json_source_ip_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(source_ip_isw, Unset):
        json_source_ip_isw = source_ip_isw

    params["source_ip__isw"] = json_source_ip_isw

    json_source_ip_n: Union[Unset, list[str]] = UNSET
    if not isinstance(source_ip_n, Unset):
        json_source_ip_n = source_ip_n

    params["source_ip__n"] = json_source_ip_n

    json_source_ip_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(source_ip_nic, Unset):
        json_source_ip_nic = source_ip_nic

    params["source_ip__nic"] = json_source_ip_nic

    json_source_ip_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(source_ip_nie, Unset):
        json_source_ip_nie = source_ip_nie

    params["source_ip__nie"] = json_source_ip_nie

    json_source_ip_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(source_ip_niew, Unset):
        json_source_ip_niew = source_ip_niew

    params["source_ip__niew"] = json_source_ip_niew

    json_source_ip_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(source_ip_nisw, Unset):
        json_source_ip_nisw = source_ip_nisw

    params["source_ip__nisw"] = json_source_ip_nisw

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

    json_transport_protocol: Union[Unset, list[str]] = UNSET
    if not isinstance(transport_protocol, Unset):
        json_transport_protocol = transport_protocol

    params["transport_protocol"] = json_transport_protocol

    params["transport_protocol__empty"] = transport_protocol_empty

    json_transport_protocol_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(transport_protocol_ic, Unset):
        json_transport_protocol_ic = transport_protocol_ic

    params["transport_protocol__ic"] = json_transport_protocol_ic

    json_transport_protocol_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(transport_protocol_ie, Unset):
        json_transport_protocol_ie = transport_protocol_ie

    params["transport_protocol__ie"] = json_transport_protocol_ie

    json_transport_protocol_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(transport_protocol_iew, Unset):
        json_transport_protocol_iew = transport_protocol_iew

    params["transport_protocol__iew"] = json_transport_protocol_iew

    json_transport_protocol_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(transport_protocol_isw, Unset):
        json_transport_protocol_isw = transport_protocol_isw

    params["transport_protocol__isw"] = json_transport_protocol_isw

    json_transport_protocol_n: Union[Unset, list[str]] = UNSET
    if not isinstance(transport_protocol_n, Unset):
        json_transport_protocol_n = transport_protocol_n

    params["transport_protocol__n"] = json_transport_protocol_n

    json_transport_protocol_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(transport_protocol_nic, Unset):
        json_transport_protocol_nic = transport_protocol_nic

    params["transport_protocol__nic"] = json_transport_protocol_nic

    json_transport_protocol_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(transport_protocol_nie, Unset):
        json_transport_protocol_nie = transport_protocol_nie

    params["transport_protocol__nie"] = json_transport_protocol_nie

    json_transport_protocol_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(transport_protocol_niew, Unset):
        json_transport_protocol_niew = transport_protocol_niew

    params["transport_protocol__niew"] = json_transport_protocol_niew

    json_transport_protocol_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(transport_protocol_nisw, Unset):
        json_transport_protocol_nisw = transport_protocol_nisw

    params["transport_protocol__nisw"] = json_transport_protocol_nisw

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/plugins/d3c/communicationfinding-list/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedCommunicationFindingList]:
    if response.status_code == 200:
        response_200 = PaginatedCommunicationFindingList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedCommunicationFindingList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    application_protocol: Union[Unset, list[str]] = UNSET,
    application_protocol_empty: Union[Unset, bool] = UNSET,
    application_protocol_ic: Union[Unset, list[str]] = UNSET,
    application_protocol_ie: Union[Unset, list[str]] = UNSET,
    application_protocol_iew: Union[Unset, list[str]] = UNSET,
    application_protocol_isw: Union[Unset, list[str]] = UNSET,
    application_protocol_n: Union[Unset, list[str]] = UNSET,
    application_protocol_nic: Union[Unset, list[str]] = UNSET,
    application_protocol_nie: Union[Unset, list[str]] = UNSET,
    application_protocol_niew: Union[Unset, list[str]] = UNSET,
    application_protocol_nisw: Union[Unset, list[str]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    destination_ip: Union[Unset, list[str]] = UNSET,
    destination_ip_empty: Union[Unset, bool] = UNSET,
    destination_ip_ic: Union[Unset, list[str]] = UNSET,
    destination_ip_ie: Union[Unset, list[str]] = UNSET,
    destination_ip_iew: Union[Unset, list[str]] = UNSET,
    destination_ip_isw: Union[Unset, list[str]] = UNSET,
    destination_ip_n: Union[Unset, list[str]] = UNSET,
    destination_ip_nic: Union[Unset, list[str]] = UNSET,
    destination_ip_nie: Union[Unset, list[str]] = UNSET,
    destination_ip_niew: Union[Unset, list[str]] = UNSET,
    destination_ip_nisw: Union[Unset, list[str]] = UNSET,
    destination_port: Union[Unset, list[str]] = UNSET,
    destination_port_empty: Union[Unset, bool] = UNSET,
    destination_port_ic: Union[Unset, list[str]] = UNSET,
    destination_port_ie: Union[Unset, list[str]] = UNSET,
    destination_port_iew: Union[Unset, list[str]] = UNSET,
    destination_port_isw: Union[Unset, list[str]] = UNSET,
    destination_port_n: Union[Unset, list[str]] = UNSET,
    destination_port_nic: Union[Unset, list[str]] = UNSET,
    destination_port_nie: Union[Unset, list[str]] = UNSET,
    destination_port_niew: Union[Unset, list[str]] = UNSET,
    destination_port_nisw: Union[Unset, list[str]] = UNSET,
    has_2_predicted_devices: Union[Unset, bool] = UNSET,
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
    network_protocol: Union[Unset, list[str]] = UNSET,
    network_protocol_empty: Union[Unset, bool] = UNSET,
    network_protocol_ic: Union[Unset, list[str]] = UNSET,
    network_protocol_ie: Union[Unset, list[str]] = UNSET,
    network_protocol_iew: Union[Unset, list[str]] = UNSET,
    network_protocol_isw: Union[Unset, list[str]] = UNSET,
    network_protocol_n: Union[Unset, list[str]] = UNSET,
    network_protocol_nic: Union[Unset, list[str]] = UNSET,
    network_protocol_nie: Union[Unset, list[str]] = UNSET,
    network_protocol_niew: Union[Unset, list[str]] = UNSET,
    network_protocol_nisw: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    predicted_dst_device: Union[Unset, int] = UNSET,
    predicted_dst_device_n: Union[Unset, int] = UNSET,
    predicted_src_device: Union[Unset, int] = UNSET,
    predicted_src_device_n: Union[Unset, int] = UNSET,
    q: Union[Unset, str] = UNSET,
    source_ip: Union[Unset, list[str]] = UNSET,
    source_ip_empty: Union[Unset, bool] = UNSET,
    source_ip_ic: Union[Unset, list[str]] = UNSET,
    source_ip_ie: Union[Unset, list[str]] = UNSET,
    source_ip_iew: Union[Unset, list[str]] = UNSET,
    source_ip_isw: Union[Unset, list[str]] = UNSET,
    source_ip_n: Union[Unset, list[str]] = UNSET,
    source_ip_nic: Union[Unset, list[str]] = UNSET,
    source_ip_nie: Union[Unset, list[str]] = UNSET,
    source_ip_niew: Union[Unset, list[str]] = UNSET,
    source_ip_nisw: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    transport_protocol: Union[Unset, list[str]] = UNSET,
    transport_protocol_empty: Union[Unset, bool] = UNSET,
    transport_protocol_ic: Union[Unset, list[str]] = UNSET,
    transport_protocol_ie: Union[Unset, list[str]] = UNSET,
    transport_protocol_iew: Union[Unset, list[str]] = UNSET,
    transport_protocol_isw: Union[Unset, list[str]] = UNSET,
    transport_protocol_n: Union[Unset, list[str]] = UNSET,
    transport_protocol_nic: Union[Unset, list[str]] = UNSET,
    transport_protocol_nie: Union[Unset, list[str]] = UNSET,
    transport_protocol_niew: Union[Unset, list[str]] = UNSET,
    transport_protocol_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedCommunicationFindingList]:
    """ViewSet for CommunicationFinding.

    Args:
        application_protocol (Union[Unset, list[str]]):
        application_protocol_empty (Union[Unset, bool]):
        application_protocol_ic (Union[Unset, list[str]]):
        application_protocol_ie (Union[Unset, list[str]]):
        application_protocol_iew (Union[Unset, list[str]]):
        application_protocol_isw (Union[Unset, list[str]]):
        application_protocol_n (Union[Unset, list[str]]):
        application_protocol_nic (Union[Unset, list[str]]):
        application_protocol_nie (Union[Unset, list[str]]):
        application_protocol_niew (Union[Unset, list[str]]):
        application_protocol_nisw (Union[Unset, list[str]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        destination_ip (Union[Unset, list[str]]):
        destination_ip_empty (Union[Unset, bool]):
        destination_ip_ic (Union[Unset, list[str]]):
        destination_ip_ie (Union[Unset, list[str]]):
        destination_ip_iew (Union[Unset, list[str]]):
        destination_ip_isw (Union[Unset, list[str]]):
        destination_ip_n (Union[Unset, list[str]]):
        destination_ip_nic (Union[Unset, list[str]]):
        destination_ip_nie (Union[Unset, list[str]]):
        destination_ip_niew (Union[Unset, list[str]]):
        destination_ip_nisw (Union[Unset, list[str]]):
        destination_port (Union[Unset, list[str]]):
        destination_port_empty (Union[Unset, bool]):
        destination_port_ic (Union[Unset, list[str]]):
        destination_port_ie (Union[Unset, list[str]]):
        destination_port_iew (Union[Unset, list[str]]):
        destination_port_isw (Union[Unset, list[str]]):
        destination_port_n (Union[Unset, list[str]]):
        destination_port_nic (Union[Unset, list[str]]):
        destination_port_nie (Union[Unset, list[str]]):
        destination_port_niew (Union[Unset, list[str]]):
        destination_port_nisw (Union[Unset, list[str]]):
        has_2_predicted_devices (Union[Unset, bool]):
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
        network_protocol (Union[Unset, list[str]]):
        network_protocol_empty (Union[Unset, bool]):
        network_protocol_ic (Union[Unset, list[str]]):
        network_protocol_ie (Union[Unset, list[str]]):
        network_protocol_iew (Union[Unset, list[str]]):
        network_protocol_isw (Union[Unset, list[str]]):
        network_protocol_n (Union[Unset, list[str]]):
        network_protocol_nic (Union[Unset, list[str]]):
        network_protocol_nie (Union[Unset, list[str]]):
        network_protocol_niew (Union[Unset, list[str]]):
        network_protocol_nisw (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        predicted_dst_device (Union[Unset, int]):
        predicted_dst_device_n (Union[Unset, int]):
        predicted_src_device (Union[Unset, int]):
        predicted_src_device_n (Union[Unset, int]):
        q (Union[Unset, str]):
        source_ip (Union[Unset, list[str]]):
        source_ip_empty (Union[Unset, bool]):
        source_ip_ic (Union[Unset, list[str]]):
        source_ip_ie (Union[Unset, list[str]]):
        source_ip_iew (Union[Unset, list[str]]):
        source_ip_isw (Union[Unset, list[str]]):
        source_ip_n (Union[Unset, list[str]]):
        source_ip_nic (Union[Unset, list[str]]):
        source_ip_nie (Union[Unset, list[str]]):
        source_ip_niew (Union[Unset, list[str]]):
        source_ip_nisw (Union[Unset, list[str]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        transport_protocol (Union[Unset, list[str]]):
        transport_protocol_empty (Union[Unset, bool]):
        transport_protocol_ic (Union[Unset, list[str]]):
        transport_protocol_ie (Union[Unset, list[str]]):
        transport_protocol_iew (Union[Unset, list[str]]):
        transport_protocol_isw (Union[Unset, list[str]]):
        transport_protocol_n (Union[Unset, list[str]]):
        transport_protocol_nic (Union[Unset, list[str]]):
        transport_protocol_nie (Union[Unset, list[str]]):
        transport_protocol_niew (Union[Unset, list[str]]):
        transport_protocol_nisw (Union[Unset, list[str]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCommunicationFindingList]
    """

    kwargs = _get_kwargs(
        application_protocol=application_protocol,
        application_protocol_empty=application_protocol_empty,
        application_protocol_ic=application_protocol_ic,
        application_protocol_ie=application_protocol_ie,
        application_protocol_iew=application_protocol_iew,
        application_protocol_isw=application_protocol_isw,
        application_protocol_n=application_protocol_n,
        application_protocol_nic=application_protocol_nic,
        application_protocol_nie=application_protocol_nie,
        application_protocol_niew=application_protocol_niew,
        application_protocol_nisw=application_protocol_nisw,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        destination_ip=destination_ip,
        destination_ip_empty=destination_ip_empty,
        destination_ip_ic=destination_ip_ic,
        destination_ip_ie=destination_ip_ie,
        destination_ip_iew=destination_ip_iew,
        destination_ip_isw=destination_ip_isw,
        destination_ip_n=destination_ip_n,
        destination_ip_nic=destination_ip_nic,
        destination_ip_nie=destination_ip_nie,
        destination_ip_niew=destination_ip_niew,
        destination_ip_nisw=destination_ip_nisw,
        destination_port=destination_port,
        destination_port_empty=destination_port_empty,
        destination_port_ic=destination_port_ic,
        destination_port_ie=destination_port_ie,
        destination_port_iew=destination_port_iew,
        destination_port_isw=destination_port_isw,
        destination_port_n=destination_port_n,
        destination_port_nic=destination_port_nic,
        destination_port_nie=destination_port_nie,
        destination_port_niew=destination_port_niew,
        destination_port_nisw=destination_port_nisw,
        has_2_predicted_devices=has_2_predicted_devices,
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
        network_protocol=network_protocol,
        network_protocol_empty=network_protocol_empty,
        network_protocol_ic=network_protocol_ic,
        network_protocol_ie=network_protocol_ie,
        network_protocol_iew=network_protocol_iew,
        network_protocol_isw=network_protocol_isw,
        network_protocol_n=network_protocol_n,
        network_protocol_nic=network_protocol_nic,
        network_protocol_nie=network_protocol_nie,
        network_protocol_niew=network_protocol_niew,
        network_protocol_nisw=network_protocol_nisw,
        offset=offset,
        ordering=ordering,
        predicted_dst_device=predicted_dst_device,
        predicted_dst_device_n=predicted_dst_device_n,
        predicted_src_device=predicted_src_device,
        predicted_src_device_n=predicted_src_device_n,
        q=q,
        source_ip=source_ip,
        source_ip_empty=source_ip_empty,
        source_ip_ic=source_ip_ic,
        source_ip_ie=source_ip_ie,
        source_ip_iew=source_ip_iew,
        source_ip_isw=source_ip_isw,
        source_ip_n=source_ip_n,
        source_ip_nic=source_ip_nic,
        source_ip_nie=source_ip_nie,
        source_ip_niew=source_ip_niew,
        source_ip_nisw=source_ip_nisw,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        transport_protocol=transport_protocol,
        transport_protocol_empty=transport_protocol_empty,
        transport_protocol_ic=transport_protocol_ic,
        transport_protocol_ie=transport_protocol_ie,
        transport_protocol_iew=transport_protocol_iew,
        transport_protocol_isw=transport_protocol_isw,
        transport_protocol_n=transport_protocol_n,
        transport_protocol_nic=transport_protocol_nic,
        transport_protocol_nie=transport_protocol_nie,
        transport_protocol_niew=transport_protocol_niew,
        transport_protocol_nisw=transport_protocol_nisw,
        updated_by_request=updated_by_request,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    application_protocol: Union[Unset, list[str]] = UNSET,
    application_protocol_empty: Union[Unset, bool] = UNSET,
    application_protocol_ic: Union[Unset, list[str]] = UNSET,
    application_protocol_ie: Union[Unset, list[str]] = UNSET,
    application_protocol_iew: Union[Unset, list[str]] = UNSET,
    application_protocol_isw: Union[Unset, list[str]] = UNSET,
    application_protocol_n: Union[Unset, list[str]] = UNSET,
    application_protocol_nic: Union[Unset, list[str]] = UNSET,
    application_protocol_nie: Union[Unset, list[str]] = UNSET,
    application_protocol_niew: Union[Unset, list[str]] = UNSET,
    application_protocol_nisw: Union[Unset, list[str]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    destination_ip: Union[Unset, list[str]] = UNSET,
    destination_ip_empty: Union[Unset, bool] = UNSET,
    destination_ip_ic: Union[Unset, list[str]] = UNSET,
    destination_ip_ie: Union[Unset, list[str]] = UNSET,
    destination_ip_iew: Union[Unset, list[str]] = UNSET,
    destination_ip_isw: Union[Unset, list[str]] = UNSET,
    destination_ip_n: Union[Unset, list[str]] = UNSET,
    destination_ip_nic: Union[Unset, list[str]] = UNSET,
    destination_ip_nie: Union[Unset, list[str]] = UNSET,
    destination_ip_niew: Union[Unset, list[str]] = UNSET,
    destination_ip_nisw: Union[Unset, list[str]] = UNSET,
    destination_port: Union[Unset, list[str]] = UNSET,
    destination_port_empty: Union[Unset, bool] = UNSET,
    destination_port_ic: Union[Unset, list[str]] = UNSET,
    destination_port_ie: Union[Unset, list[str]] = UNSET,
    destination_port_iew: Union[Unset, list[str]] = UNSET,
    destination_port_isw: Union[Unset, list[str]] = UNSET,
    destination_port_n: Union[Unset, list[str]] = UNSET,
    destination_port_nic: Union[Unset, list[str]] = UNSET,
    destination_port_nie: Union[Unset, list[str]] = UNSET,
    destination_port_niew: Union[Unset, list[str]] = UNSET,
    destination_port_nisw: Union[Unset, list[str]] = UNSET,
    has_2_predicted_devices: Union[Unset, bool] = UNSET,
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
    network_protocol: Union[Unset, list[str]] = UNSET,
    network_protocol_empty: Union[Unset, bool] = UNSET,
    network_protocol_ic: Union[Unset, list[str]] = UNSET,
    network_protocol_ie: Union[Unset, list[str]] = UNSET,
    network_protocol_iew: Union[Unset, list[str]] = UNSET,
    network_protocol_isw: Union[Unset, list[str]] = UNSET,
    network_protocol_n: Union[Unset, list[str]] = UNSET,
    network_protocol_nic: Union[Unset, list[str]] = UNSET,
    network_protocol_nie: Union[Unset, list[str]] = UNSET,
    network_protocol_niew: Union[Unset, list[str]] = UNSET,
    network_protocol_nisw: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    predicted_dst_device: Union[Unset, int] = UNSET,
    predicted_dst_device_n: Union[Unset, int] = UNSET,
    predicted_src_device: Union[Unset, int] = UNSET,
    predicted_src_device_n: Union[Unset, int] = UNSET,
    q: Union[Unset, str] = UNSET,
    source_ip: Union[Unset, list[str]] = UNSET,
    source_ip_empty: Union[Unset, bool] = UNSET,
    source_ip_ic: Union[Unset, list[str]] = UNSET,
    source_ip_ie: Union[Unset, list[str]] = UNSET,
    source_ip_iew: Union[Unset, list[str]] = UNSET,
    source_ip_isw: Union[Unset, list[str]] = UNSET,
    source_ip_n: Union[Unset, list[str]] = UNSET,
    source_ip_nic: Union[Unset, list[str]] = UNSET,
    source_ip_nie: Union[Unset, list[str]] = UNSET,
    source_ip_niew: Union[Unset, list[str]] = UNSET,
    source_ip_nisw: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    transport_protocol: Union[Unset, list[str]] = UNSET,
    transport_protocol_empty: Union[Unset, bool] = UNSET,
    transport_protocol_ic: Union[Unset, list[str]] = UNSET,
    transport_protocol_ie: Union[Unset, list[str]] = UNSET,
    transport_protocol_iew: Union[Unset, list[str]] = UNSET,
    transport_protocol_isw: Union[Unset, list[str]] = UNSET,
    transport_protocol_n: Union[Unset, list[str]] = UNSET,
    transport_protocol_nic: Union[Unset, list[str]] = UNSET,
    transport_protocol_nie: Union[Unset, list[str]] = UNSET,
    transport_protocol_niew: Union[Unset, list[str]] = UNSET,
    transport_protocol_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedCommunicationFindingList]:
    """ViewSet for CommunicationFinding.

    Args:
        application_protocol (Union[Unset, list[str]]):
        application_protocol_empty (Union[Unset, bool]):
        application_protocol_ic (Union[Unset, list[str]]):
        application_protocol_ie (Union[Unset, list[str]]):
        application_protocol_iew (Union[Unset, list[str]]):
        application_protocol_isw (Union[Unset, list[str]]):
        application_protocol_n (Union[Unset, list[str]]):
        application_protocol_nic (Union[Unset, list[str]]):
        application_protocol_nie (Union[Unset, list[str]]):
        application_protocol_niew (Union[Unset, list[str]]):
        application_protocol_nisw (Union[Unset, list[str]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        destination_ip (Union[Unset, list[str]]):
        destination_ip_empty (Union[Unset, bool]):
        destination_ip_ic (Union[Unset, list[str]]):
        destination_ip_ie (Union[Unset, list[str]]):
        destination_ip_iew (Union[Unset, list[str]]):
        destination_ip_isw (Union[Unset, list[str]]):
        destination_ip_n (Union[Unset, list[str]]):
        destination_ip_nic (Union[Unset, list[str]]):
        destination_ip_nie (Union[Unset, list[str]]):
        destination_ip_niew (Union[Unset, list[str]]):
        destination_ip_nisw (Union[Unset, list[str]]):
        destination_port (Union[Unset, list[str]]):
        destination_port_empty (Union[Unset, bool]):
        destination_port_ic (Union[Unset, list[str]]):
        destination_port_ie (Union[Unset, list[str]]):
        destination_port_iew (Union[Unset, list[str]]):
        destination_port_isw (Union[Unset, list[str]]):
        destination_port_n (Union[Unset, list[str]]):
        destination_port_nic (Union[Unset, list[str]]):
        destination_port_nie (Union[Unset, list[str]]):
        destination_port_niew (Union[Unset, list[str]]):
        destination_port_nisw (Union[Unset, list[str]]):
        has_2_predicted_devices (Union[Unset, bool]):
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
        network_protocol (Union[Unset, list[str]]):
        network_protocol_empty (Union[Unset, bool]):
        network_protocol_ic (Union[Unset, list[str]]):
        network_protocol_ie (Union[Unset, list[str]]):
        network_protocol_iew (Union[Unset, list[str]]):
        network_protocol_isw (Union[Unset, list[str]]):
        network_protocol_n (Union[Unset, list[str]]):
        network_protocol_nic (Union[Unset, list[str]]):
        network_protocol_nie (Union[Unset, list[str]]):
        network_protocol_niew (Union[Unset, list[str]]):
        network_protocol_nisw (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        predicted_dst_device (Union[Unset, int]):
        predicted_dst_device_n (Union[Unset, int]):
        predicted_src_device (Union[Unset, int]):
        predicted_src_device_n (Union[Unset, int]):
        q (Union[Unset, str]):
        source_ip (Union[Unset, list[str]]):
        source_ip_empty (Union[Unset, bool]):
        source_ip_ic (Union[Unset, list[str]]):
        source_ip_ie (Union[Unset, list[str]]):
        source_ip_iew (Union[Unset, list[str]]):
        source_ip_isw (Union[Unset, list[str]]):
        source_ip_n (Union[Unset, list[str]]):
        source_ip_nic (Union[Unset, list[str]]):
        source_ip_nie (Union[Unset, list[str]]):
        source_ip_niew (Union[Unset, list[str]]):
        source_ip_nisw (Union[Unset, list[str]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        transport_protocol (Union[Unset, list[str]]):
        transport_protocol_empty (Union[Unset, bool]):
        transport_protocol_ic (Union[Unset, list[str]]):
        transport_protocol_ie (Union[Unset, list[str]]):
        transport_protocol_iew (Union[Unset, list[str]]):
        transport_protocol_isw (Union[Unset, list[str]]):
        transport_protocol_n (Union[Unset, list[str]]):
        transport_protocol_nic (Union[Unset, list[str]]):
        transport_protocol_nie (Union[Unset, list[str]]):
        transport_protocol_niew (Union[Unset, list[str]]):
        transport_protocol_nisw (Union[Unset, list[str]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCommunicationFindingList
    """

    return sync_detailed(
        client=client,
        application_protocol=application_protocol,
        application_protocol_empty=application_protocol_empty,
        application_protocol_ic=application_protocol_ic,
        application_protocol_ie=application_protocol_ie,
        application_protocol_iew=application_protocol_iew,
        application_protocol_isw=application_protocol_isw,
        application_protocol_n=application_protocol_n,
        application_protocol_nic=application_protocol_nic,
        application_protocol_nie=application_protocol_nie,
        application_protocol_niew=application_protocol_niew,
        application_protocol_nisw=application_protocol_nisw,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        destination_ip=destination_ip,
        destination_ip_empty=destination_ip_empty,
        destination_ip_ic=destination_ip_ic,
        destination_ip_ie=destination_ip_ie,
        destination_ip_iew=destination_ip_iew,
        destination_ip_isw=destination_ip_isw,
        destination_ip_n=destination_ip_n,
        destination_ip_nic=destination_ip_nic,
        destination_ip_nie=destination_ip_nie,
        destination_ip_niew=destination_ip_niew,
        destination_ip_nisw=destination_ip_nisw,
        destination_port=destination_port,
        destination_port_empty=destination_port_empty,
        destination_port_ic=destination_port_ic,
        destination_port_ie=destination_port_ie,
        destination_port_iew=destination_port_iew,
        destination_port_isw=destination_port_isw,
        destination_port_n=destination_port_n,
        destination_port_nic=destination_port_nic,
        destination_port_nie=destination_port_nie,
        destination_port_niew=destination_port_niew,
        destination_port_nisw=destination_port_nisw,
        has_2_predicted_devices=has_2_predicted_devices,
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
        network_protocol=network_protocol,
        network_protocol_empty=network_protocol_empty,
        network_protocol_ic=network_protocol_ic,
        network_protocol_ie=network_protocol_ie,
        network_protocol_iew=network_protocol_iew,
        network_protocol_isw=network_protocol_isw,
        network_protocol_n=network_protocol_n,
        network_protocol_nic=network_protocol_nic,
        network_protocol_nie=network_protocol_nie,
        network_protocol_niew=network_protocol_niew,
        network_protocol_nisw=network_protocol_nisw,
        offset=offset,
        ordering=ordering,
        predicted_dst_device=predicted_dst_device,
        predicted_dst_device_n=predicted_dst_device_n,
        predicted_src_device=predicted_src_device,
        predicted_src_device_n=predicted_src_device_n,
        q=q,
        source_ip=source_ip,
        source_ip_empty=source_ip_empty,
        source_ip_ic=source_ip_ic,
        source_ip_ie=source_ip_ie,
        source_ip_iew=source_ip_iew,
        source_ip_isw=source_ip_isw,
        source_ip_n=source_ip_n,
        source_ip_nic=source_ip_nic,
        source_ip_nie=source_ip_nie,
        source_ip_niew=source_ip_niew,
        source_ip_nisw=source_ip_nisw,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        transport_protocol=transport_protocol,
        transport_protocol_empty=transport_protocol_empty,
        transport_protocol_ic=transport_protocol_ic,
        transport_protocol_ie=transport_protocol_ie,
        transport_protocol_iew=transport_protocol_iew,
        transport_protocol_isw=transport_protocol_isw,
        transport_protocol_n=transport_protocol_n,
        transport_protocol_nic=transport_protocol_nic,
        transport_protocol_nie=transport_protocol_nie,
        transport_protocol_niew=transport_protocol_niew,
        transport_protocol_nisw=transport_protocol_nisw,
        updated_by_request=updated_by_request,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    application_protocol: Union[Unset, list[str]] = UNSET,
    application_protocol_empty: Union[Unset, bool] = UNSET,
    application_protocol_ic: Union[Unset, list[str]] = UNSET,
    application_protocol_ie: Union[Unset, list[str]] = UNSET,
    application_protocol_iew: Union[Unset, list[str]] = UNSET,
    application_protocol_isw: Union[Unset, list[str]] = UNSET,
    application_protocol_n: Union[Unset, list[str]] = UNSET,
    application_protocol_nic: Union[Unset, list[str]] = UNSET,
    application_protocol_nie: Union[Unset, list[str]] = UNSET,
    application_protocol_niew: Union[Unset, list[str]] = UNSET,
    application_protocol_nisw: Union[Unset, list[str]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    destination_ip: Union[Unset, list[str]] = UNSET,
    destination_ip_empty: Union[Unset, bool] = UNSET,
    destination_ip_ic: Union[Unset, list[str]] = UNSET,
    destination_ip_ie: Union[Unset, list[str]] = UNSET,
    destination_ip_iew: Union[Unset, list[str]] = UNSET,
    destination_ip_isw: Union[Unset, list[str]] = UNSET,
    destination_ip_n: Union[Unset, list[str]] = UNSET,
    destination_ip_nic: Union[Unset, list[str]] = UNSET,
    destination_ip_nie: Union[Unset, list[str]] = UNSET,
    destination_ip_niew: Union[Unset, list[str]] = UNSET,
    destination_ip_nisw: Union[Unset, list[str]] = UNSET,
    destination_port: Union[Unset, list[str]] = UNSET,
    destination_port_empty: Union[Unset, bool] = UNSET,
    destination_port_ic: Union[Unset, list[str]] = UNSET,
    destination_port_ie: Union[Unset, list[str]] = UNSET,
    destination_port_iew: Union[Unset, list[str]] = UNSET,
    destination_port_isw: Union[Unset, list[str]] = UNSET,
    destination_port_n: Union[Unset, list[str]] = UNSET,
    destination_port_nic: Union[Unset, list[str]] = UNSET,
    destination_port_nie: Union[Unset, list[str]] = UNSET,
    destination_port_niew: Union[Unset, list[str]] = UNSET,
    destination_port_nisw: Union[Unset, list[str]] = UNSET,
    has_2_predicted_devices: Union[Unset, bool] = UNSET,
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
    network_protocol: Union[Unset, list[str]] = UNSET,
    network_protocol_empty: Union[Unset, bool] = UNSET,
    network_protocol_ic: Union[Unset, list[str]] = UNSET,
    network_protocol_ie: Union[Unset, list[str]] = UNSET,
    network_protocol_iew: Union[Unset, list[str]] = UNSET,
    network_protocol_isw: Union[Unset, list[str]] = UNSET,
    network_protocol_n: Union[Unset, list[str]] = UNSET,
    network_protocol_nic: Union[Unset, list[str]] = UNSET,
    network_protocol_nie: Union[Unset, list[str]] = UNSET,
    network_protocol_niew: Union[Unset, list[str]] = UNSET,
    network_protocol_nisw: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    predicted_dst_device: Union[Unset, int] = UNSET,
    predicted_dst_device_n: Union[Unset, int] = UNSET,
    predicted_src_device: Union[Unset, int] = UNSET,
    predicted_src_device_n: Union[Unset, int] = UNSET,
    q: Union[Unset, str] = UNSET,
    source_ip: Union[Unset, list[str]] = UNSET,
    source_ip_empty: Union[Unset, bool] = UNSET,
    source_ip_ic: Union[Unset, list[str]] = UNSET,
    source_ip_ie: Union[Unset, list[str]] = UNSET,
    source_ip_iew: Union[Unset, list[str]] = UNSET,
    source_ip_isw: Union[Unset, list[str]] = UNSET,
    source_ip_n: Union[Unset, list[str]] = UNSET,
    source_ip_nic: Union[Unset, list[str]] = UNSET,
    source_ip_nie: Union[Unset, list[str]] = UNSET,
    source_ip_niew: Union[Unset, list[str]] = UNSET,
    source_ip_nisw: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    transport_protocol: Union[Unset, list[str]] = UNSET,
    transport_protocol_empty: Union[Unset, bool] = UNSET,
    transport_protocol_ic: Union[Unset, list[str]] = UNSET,
    transport_protocol_ie: Union[Unset, list[str]] = UNSET,
    transport_protocol_iew: Union[Unset, list[str]] = UNSET,
    transport_protocol_isw: Union[Unset, list[str]] = UNSET,
    transport_protocol_n: Union[Unset, list[str]] = UNSET,
    transport_protocol_nic: Union[Unset, list[str]] = UNSET,
    transport_protocol_nie: Union[Unset, list[str]] = UNSET,
    transport_protocol_niew: Union[Unset, list[str]] = UNSET,
    transport_protocol_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Response[PaginatedCommunicationFindingList]:
    """ViewSet for CommunicationFinding.

    Args:
        application_protocol (Union[Unset, list[str]]):
        application_protocol_empty (Union[Unset, bool]):
        application_protocol_ic (Union[Unset, list[str]]):
        application_protocol_ie (Union[Unset, list[str]]):
        application_protocol_iew (Union[Unset, list[str]]):
        application_protocol_isw (Union[Unset, list[str]]):
        application_protocol_n (Union[Unset, list[str]]):
        application_protocol_nic (Union[Unset, list[str]]):
        application_protocol_nie (Union[Unset, list[str]]):
        application_protocol_niew (Union[Unset, list[str]]):
        application_protocol_nisw (Union[Unset, list[str]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        destination_ip (Union[Unset, list[str]]):
        destination_ip_empty (Union[Unset, bool]):
        destination_ip_ic (Union[Unset, list[str]]):
        destination_ip_ie (Union[Unset, list[str]]):
        destination_ip_iew (Union[Unset, list[str]]):
        destination_ip_isw (Union[Unset, list[str]]):
        destination_ip_n (Union[Unset, list[str]]):
        destination_ip_nic (Union[Unset, list[str]]):
        destination_ip_nie (Union[Unset, list[str]]):
        destination_ip_niew (Union[Unset, list[str]]):
        destination_ip_nisw (Union[Unset, list[str]]):
        destination_port (Union[Unset, list[str]]):
        destination_port_empty (Union[Unset, bool]):
        destination_port_ic (Union[Unset, list[str]]):
        destination_port_ie (Union[Unset, list[str]]):
        destination_port_iew (Union[Unset, list[str]]):
        destination_port_isw (Union[Unset, list[str]]):
        destination_port_n (Union[Unset, list[str]]):
        destination_port_nic (Union[Unset, list[str]]):
        destination_port_nie (Union[Unset, list[str]]):
        destination_port_niew (Union[Unset, list[str]]):
        destination_port_nisw (Union[Unset, list[str]]):
        has_2_predicted_devices (Union[Unset, bool]):
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
        network_protocol (Union[Unset, list[str]]):
        network_protocol_empty (Union[Unset, bool]):
        network_protocol_ic (Union[Unset, list[str]]):
        network_protocol_ie (Union[Unset, list[str]]):
        network_protocol_iew (Union[Unset, list[str]]):
        network_protocol_isw (Union[Unset, list[str]]):
        network_protocol_n (Union[Unset, list[str]]):
        network_protocol_nic (Union[Unset, list[str]]):
        network_protocol_nie (Union[Unset, list[str]]):
        network_protocol_niew (Union[Unset, list[str]]):
        network_protocol_nisw (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        predicted_dst_device (Union[Unset, int]):
        predicted_dst_device_n (Union[Unset, int]):
        predicted_src_device (Union[Unset, int]):
        predicted_src_device_n (Union[Unset, int]):
        q (Union[Unset, str]):
        source_ip (Union[Unset, list[str]]):
        source_ip_empty (Union[Unset, bool]):
        source_ip_ic (Union[Unset, list[str]]):
        source_ip_ie (Union[Unset, list[str]]):
        source_ip_iew (Union[Unset, list[str]]):
        source_ip_isw (Union[Unset, list[str]]):
        source_ip_n (Union[Unset, list[str]]):
        source_ip_nic (Union[Unset, list[str]]):
        source_ip_nie (Union[Unset, list[str]]):
        source_ip_niew (Union[Unset, list[str]]):
        source_ip_nisw (Union[Unset, list[str]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        transport_protocol (Union[Unset, list[str]]):
        transport_protocol_empty (Union[Unset, bool]):
        transport_protocol_ic (Union[Unset, list[str]]):
        transport_protocol_ie (Union[Unset, list[str]]):
        transport_protocol_iew (Union[Unset, list[str]]):
        transport_protocol_isw (Union[Unset, list[str]]):
        transport_protocol_n (Union[Unset, list[str]]):
        transport_protocol_nic (Union[Unset, list[str]]):
        transport_protocol_nie (Union[Unset, list[str]]):
        transport_protocol_niew (Union[Unset, list[str]]):
        transport_protocol_nisw (Union[Unset, list[str]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedCommunicationFindingList]
    """

    kwargs = _get_kwargs(
        application_protocol=application_protocol,
        application_protocol_empty=application_protocol_empty,
        application_protocol_ic=application_protocol_ic,
        application_protocol_ie=application_protocol_ie,
        application_protocol_iew=application_protocol_iew,
        application_protocol_isw=application_protocol_isw,
        application_protocol_n=application_protocol_n,
        application_protocol_nic=application_protocol_nic,
        application_protocol_nie=application_protocol_nie,
        application_protocol_niew=application_protocol_niew,
        application_protocol_nisw=application_protocol_nisw,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        destination_ip=destination_ip,
        destination_ip_empty=destination_ip_empty,
        destination_ip_ic=destination_ip_ic,
        destination_ip_ie=destination_ip_ie,
        destination_ip_iew=destination_ip_iew,
        destination_ip_isw=destination_ip_isw,
        destination_ip_n=destination_ip_n,
        destination_ip_nic=destination_ip_nic,
        destination_ip_nie=destination_ip_nie,
        destination_ip_niew=destination_ip_niew,
        destination_ip_nisw=destination_ip_nisw,
        destination_port=destination_port,
        destination_port_empty=destination_port_empty,
        destination_port_ic=destination_port_ic,
        destination_port_ie=destination_port_ie,
        destination_port_iew=destination_port_iew,
        destination_port_isw=destination_port_isw,
        destination_port_n=destination_port_n,
        destination_port_nic=destination_port_nic,
        destination_port_nie=destination_port_nie,
        destination_port_niew=destination_port_niew,
        destination_port_nisw=destination_port_nisw,
        has_2_predicted_devices=has_2_predicted_devices,
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
        network_protocol=network_protocol,
        network_protocol_empty=network_protocol_empty,
        network_protocol_ic=network_protocol_ic,
        network_protocol_ie=network_protocol_ie,
        network_protocol_iew=network_protocol_iew,
        network_protocol_isw=network_protocol_isw,
        network_protocol_n=network_protocol_n,
        network_protocol_nic=network_protocol_nic,
        network_protocol_nie=network_protocol_nie,
        network_protocol_niew=network_protocol_niew,
        network_protocol_nisw=network_protocol_nisw,
        offset=offset,
        ordering=ordering,
        predicted_dst_device=predicted_dst_device,
        predicted_dst_device_n=predicted_dst_device_n,
        predicted_src_device=predicted_src_device,
        predicted_src_device_n=predicted_src_device_n,
        q=q,
        source_ip=source_ip,
        source_ip_empty=source_ip_empty,
        source_ip_ic=source_ip_ic,
        source_ip_ie=source_ip_ie,
        source_ip_iew=source_ip_iew,
        source_ip_isw=source_ip_isw,
        source_ip_n=source_ip_n,
        source_ip_nic=source_ip_nic,
        source_ip_nie=source_ip_nie,
        source_ip_niew=source_ip_niew,
        source_ip_nisw=source_ip_nisw,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        transport_protocol=transport_protocol,
        transport_protocol_empty=transport_protocol_empty,
        transport_protocol_ic=transport_protocol_ic,
        transport_protocol_ie=transport_protocol_ie,
        transport_protocol_iew=transport_protocol_iew,
        transport_protocol_isw=transport_protocol_isw,
        transport_protocol_n=transport_protocol_n,
        transport_protocol_nic=transport_protocol_nic,
        transport_protocol_nie=transport_protocol_nie,
        transport_protocol_niew=transport_protocol_niew,
        transport_protocol_nisw=transport_protocol_nisw,
        updated_by_request=updated_by_request,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    application_protocol: Union[Unset, list[str]] = UNSET,
    application_protocol_empty: Union[Unset, bool] = UNSET,
    application_protocol_ic: Union[Unset, list[str]] = UNSET,
    application_protocol_ie: Union[Unset, list[str]] = UNSET,
    application_protocol_iew: Union[Unset, list[str]] = UNSET,
    application_protocol_isw: Union[Unset, list[str]] = UNSET,
    application_protocol_n: Union[Unset, list[str]] = UNSET,
    application_protocol_nic: Union[Unset, list[str]] = UNSET,
    application_protocol_nie: Union[Unset, list[str]] = UNSET,
    application_protocol_niew: Union[Unset, list[str]] = UNSET,
    application_protocol_nisw: Union[Unset, list[str]] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    destination_ip: Union[Unset, list[str]] = UNSET,
    destination_ip_empty: Union[Unset, bool] = UNSET,
    destination_ip_ic: Union[Unset, list[str]] = UNSET,
    destination_ip_ie: Union[Unset, list[str]] = UNSET,
    destination_ip_iew: Union[Unset, list[str]] = UNSET,
    destination_ip_isw: Union[Unset, list[str]] = UNSET,
    destination_ip_n: Union[Unset, list[str]] = UNSET,
    destination_ip_nic: Union[Unset, list[str]] = UNSET,
    destination_ip_nie: Union[Unset, list[str]] = UNSET,
    destination_ip_niew: Union[Unset, list[str]] = UNSET,
    destination_ip_nisw: Union[Unset, list[str]] = UNSET,
    destination_port: Union[Unset, list[str]] = UNSET,
    destination_port_empty: Union[Unset, bool] = UNSET,
    destination_port_ic: Union[Unset, list[str]] = UNSET,
    destination_port_ie: Union[Unset, list[str]] = UNSET,
    destination_port_iew: Union[Unset, list[str]] = UNSET,
    destination_port_isw: Union[Unset, list[str]] = UNSET,
    destination_port_n: Union[Unset, list[str]] = UNSET,
    destination_port_nic: Union[Unset, list[str]] = UNSET,
    destination_port_nie: Union[Unset, list[str]] = UNSET,
    destination_port_niew: Union[Unset, list[str]] = UNSET,
    destination_port_nisw: Union[Unset, list[str]] = UNSET,
    has_2_predicted_devices: Union[Unset, bool] = UNSET,
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
    network_protocol: Union[Unset, list[str]] = UNSET,
    network_protocol_empty: Union[Unset, bool] = UNSET,
    network_protocol_ic: Union[Unset, list[str]] = UNSET,
    network_protocol_ie: Union[Unset, list[str]] = UNSET,
    network_protocol_iew: Union[Unset, list[str]] = UNSET,
    network_protocol_isw: Union[Unset, list[str]] = UNSET,
    network_protocol_n: Union[Unset, list[str]] = UNSET,
    network_protocol_nic: Union[Unset, list[str]] = UNSET,
    network_protocol_nie: Union[Unset, list[str]] = UNSET,
    network_protocol_niew: Union[Unset, list[str]] = UNSET,
    network_protocol_nisw: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    predicted_dst_device: Union[Unset, int] = UNSET,
    predicted_dst_device_n: Union[Unset, int] = UNSET,
    predicted_src_device: Union[Unset, int] = UNSET,
    predicted_src_device_n: Union[Unset, int] = UNSET,
    q: Union[Unset, str] = UNSET,
    source_ip: Union[Unset, list[str]] = UNSET,
    source_ip_empty: Union[Unset, bool] = UNSET,
    source_ip_ic: Union[Unset, list[str]] = UNSET,
    source_ip_ie: Union[Unset, list[str]] = UNSET,
    source_ip_iew: Union[Unset, list[str]] = UNSET,
    source_ip_isw: Union[Unset, list[str]] = UNSET,
    source_ip_n: Union[Unset, list[str]] = UNSET,
    source_ip_nic: Union[Unset, list[str]] = UNSET,
    source_ip_nie: Union[Unset, list[str]] = UNSET,
    source_ip_niew: Union[Unset, list[str]] = UNSET,
    source_ip_nisw: Union[Unset, list[str]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    transport_protocol: Union[Unset, list[str]] = UNSET,
    transport_protocol_empty: Union[Unset, bool] = UNSET,
    transport_protocol_ic: Union[Unset, list[str]] = UNSET,
    transport_protocol_ie: Union[Unset, list[str]] = UNSET,
    transport_protocol_iew: Union[Unset, list[str]] = UNSET,
    transport_protocol_isw: Union[Unset, list[str]] = UNSET,
    transport_protocol_n: Union[Unset, list[str]] = UNSET,
    transport_protocol_nic: Union[Unset, list[str]] = UNSET,
    transport_protocol_nie: Union[Unset, list[str]] = UNSET,
    transport_protocol_niew: Union[Unset, list[str]] = UNSET,
    transport_protocol_nisw: Union[Unset, list[str]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
) -> Optional[PaginatedCommunicationFindingList]:
    """ViewSet for CommunicationFinding.

    Args:
        application_protocol (Union[Unset, list[str]]):
        application_protocol_empty (Union[Unset, bool]):
        application_protocol_ic (Union[Unset, list[str]]):
        application_protocol_ie (Union[Unset, list[str]]):
        application_protocol_iew (Union[Unset, list[str]]):
        application_protocol_isw (Union[Unset, list[str]]):
        application_protocol_n (Union[Unset, list[str]]):
        application_protocol_nic (Union[Unset, list[str]]):
        application_protocol_nie (Union[Unset, list[str]]):
        application_protocol_niew (Union[Unset, list[str]]):
        application_protocol_nisw (Union[Unset, list[str]]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        destination_ip (Union[Unset, list[str]]):
        destination_ip_empty (Union[Unset, bool]):
        destination_ip_ic (Union[Unset, list[str]]):
        destination_ip_ie (Union[Unset, list[str]]):
        destination_ip_iew (Union[Unset, list[str]]):
        destination_ip_isw (Union[Unset, list[str]]):
        destination_ip_n (Union[Unset, list[str]]):
        destination_ip_nic (Union[Unset, list[str]]):
        destination_ip_nie (Union[Unset, list[str]]):
        destination_ip_niew (Union[Unset, list[str]]):
        destination_ip_nisw (Union[Unset, list[str]]):
        destination_port (Union[Unset, list[str]]):
        destination_port_empty (Union[Unset, bool]):
        destination_port_ic (Union[Unset, list[str]]):
        destination_port_ie (Union[Unset, list[str]]):
        destination_port_iew (Union[Unset, list[str]]):
        destination_port_isw (Union[Unset, list[str]]):
        destination_port_n (Union[Unset, list[str]]):
        destination_port_nic (Union[Unset, list[str]]):
        destination_port_nie (Union[Unset, list[str]]):
        destination_port_niew (Union[Unset, list[str]]):
        destination_port_nisw (Union[Unset, list[str]]):
        has_2_predicted_devices (Union[Unset, bool]):
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
        network_protocol (Union[Unset, list[str]]):
        network_protocol_empty (Union[Unset, bool]):
        network_protocol_ic (Union[Unset, list[str]]):
        network_protocol_ie (Union[Unset, list[str]]):
        network_protocol_iew (Union[Unset, list[str]]):
        network_protocol_isw (Union[Unset, list[str]]):
        network_protocol_n (Union[Unset, list[str]]):
        network_protocol_nic (Union[Unset, list[str]]):
        network_protocol_nie (Union[Unset, list[str]]):
        network_protocol_niew (Union[Unset, list[str]]):
        network_protocol_nisw (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        predicted_dst_device (Union[Unset, int]):
        predicted_dst_device_n (Union[Unset, int]):
        predicted_src_device (Union[Unset, int]):
        predicted_src_device_n (Union[Unset, int]):
        q (Union[Unset, str]):
        source_ip (Union[Unset, list[str]]):
        source_ip_empty (Union[Unset, bool]):
        source_ip_ic (Union[Unset, list[str]]):
        source_ip_ie (Union[Unset, list[str]]):
        source_ip_iew (Union[Unset, list[str]]):
        source_ip_isw (Union[Unset, list[str]]):
        source_ip_n (Union[Unset, list[str]]):
        source_ip_nic (Union[Unset, list[str]]):
        source_ip_nie (Union[Unset, list[str]]):
        source_ip_niew (Union[Unset, list[str]]):
        source_ip_nisw (Union[Unset, list[str]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        transport_protocol (Union[Unset, list[str]]):
        transport_protocol_empty (Union[Unset, bool]):
        transport_protocol_ic (Union[Unset, list[str]]):
        transport_protocol_ie (Union[Unset, list[str]]):
        transport_protocol_iew (Union[Unset, list[str]]):
        transport_protocol_isw (Union[Unset, list[str]]):
        transport_protocol_n (Union[Unset, list[str]]):
        transport_protocol_nic (Union[Unset, list[str]]):
        transport_protocol_nie (Union[Unset, list[str]]):
        transport_protocol_niew (Union[Unset, list[str]]):
        transport_protocol_nisw (Union[Unset, list[str]]):
        updated_by_request (Union[Unset, UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedCommunicationFindingList
    """

    return (
        await asyncio_detailed(
            client=client,
            application_protocol=application_protocol,
            application_protocol_empty=application_protocol_empty,
            application_protocol_ic=application_protocol_ic,
            application_protocol_ie=application_protocol_ie,
            application_protocol_iew=application_protocol_iew,
            application_protocol_isw=application_protocol_isw,
            application_protocol_n=application_protocol_n,
            application_protocol_nic=application_protocol_nic,
            application_protocol_nie=application_protocol_nie,
            application_protocol_niew=application_protocol_niew,
            application_protocol_nisw=application_protocol_nisw,
            created=created,
            created_empty=created_empty,
            created_gt=created_gt,
            created_gte=created_gte,
            created_lt=created_lt,
            created_lte=created_lte,
            created_n=created_n,
            created_by_request=created_by_request,
            destination_ip=destination_ip,
            destination_ip_empty=destination_ip_empty,
            destination_ip_ic=destination_ip_ic,
            destination_ip_ie=destination_ip_ie,
            destination_ip_iew=destination_ip_iew,
            destination_ip_isw=destination_ip_isw,
            destination_ip_n=destination_ip_n,
            destination_ip_nic=destination_ip_nic,
            destination_ip_nie=destination_ip_nie,
            destination_ip_niew=destination_ip_niew,
            destination_ip_nisw=destination_ip_nisw,
            destination_port=destination_port,
            destination_port_empty=destination_port_empty,
            destination_port_ic=destination_port_ic,
            destination_port_ie=destination_port_ie,
            destination_port_iew=destination_port_iew,
            destination_port_isw=destination_port_isw,
            destination_port_n=destination_port_n,
            destination_port_nic=destination_port_nic,
            destination_port_nie=destination_port_nie,
            destination_port_niew=destination_port_niew,
            destination_port_nisw=destination_port_nisw,
            has_2_predicted_devices=has_2_predicted_devices,
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
            network_protocol=network_protocol,
            network_protocol_empty=network_protocol_empty,
            network_protocol_ic=network_protocol_ic,
            network_protocol_ie=network_protocol_ie,
            network_protocol_iew=network_protocol_iew,
            network_protocol_isw=network_protocol_isw,
            network_protocol_n=network_protocol_n,
            network_protocol_nic=network_protocol_nic,
            network_protocol_nie=network_protocol_nie,
            network_protocol_niew=network_protocol_niew,
            network_protocol_nisw=network_protocol_nisw,
            offset=offset,
            ordering=ordering,
            predicted_dst_device=predicted_dst_device,
            predicted_dst_device_n=predicted_dst_device_n,
            predicted_src_device=predicted_src_device,
            predicted_src_device_n=predicted_src_device_n,
            q=q,
            source_ip=source_ip,
            source_ip_empty=source_ip_empty,
            source_ip_ic=source_ip_ic,
            source_ip_ie=source_ip_ie,
            source_ip_iew=source_ip_iew,
            source_ip_isw=source_ip_isw,
            source_ip_n=source_ip_n,
            source_ip_nic=source_ip_nic,
            source_ip_nie=source_ip_nie,
            source_ip_niew=source_ip_niew,
            source_ip_nisw=source_ip_nisw,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
            transport_protocol=transport_protocol,
            transport_protocol_empty=transport_protocol_empty,
            transport_protocol_ic=transport_protocol_ic,
            transport_protocol_ie=transport_protocol_ie,
            transport_protocol_iew=transport_protocol_iew,
            transport_protocol_isw=transport_protocol_isw,
            transport_protocol_n=transport_protocol_n,
            transport_protocol_nic=transport_protocol_nic,
            transport_protocol_nie=transport_protocol_nie,
            transport_protocol_niew=transport_protocol_niew,
            transport_protocol_nisw=transport_protocol_nisw,
            updated_by_request=updated_by_request,
        )
    ).parsed
