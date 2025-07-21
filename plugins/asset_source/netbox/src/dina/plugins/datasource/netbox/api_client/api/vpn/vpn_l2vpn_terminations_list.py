import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_l2vpn_termination_list import PaginatedL2VPNTerminationList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    assigned_object_id: Union[Unset, list[int]] = UNSET,
    assigned_object_id_empty: Union[Unset, bool] = UNSET,
    assigned_object_id_gt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_gte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_n: Union[Unset, list[int]] = UNSET,
    assigned_object_type: Union[Unset, str] = UNSET,
    assigned_object_type_n: Union[Unset, str] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    device_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface: Union[Unset, list[str]] = UNSET,
    interface_n: Union[Unset, list[str]] = UNSET,
    interface_id: Union[Unset, list[int]] = UNSET,
    interface_id_n: Union[Unset, list[int]] = UNSET,
    l2vpn: Union[Unset, list[str]] = UNSET,
    l2vpn_n: Union[Unset, list[str]] = UNSET,
    l2vpn_id: Union[Unset, list[int]] = UNSET,
    l2vpn_id_n: Union[Unset, list[int]] = UNSET,
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
    region: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[int]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_machine: Union[Unset, list[str]] = UNSET,
    virtual_machine_n: Union[Unset, list[str]] = UNSET,
    virtual_machine_id: Union[Unset, list[int]] = UNSET,
    virtual_machine_id_n: Union[Unset, list[int]] = UNSET,
    vlan: Union[Unset, list[str]] = UNSET,
    vlan_n: Union[Unset, list[str]] = UNSET,
    vlan_id: Union[Unset, list[int]] = UNSET,
    vlan_id_n: Union[Unset, list[int]] = UNSET,
    vlan_vid: Union[Unset, int] = UNSET,
    vlan_vid_empty: Union[Unset, int] = UNSET,
    vlan_vid_gt: Union[Unset, int] = UNSET,
    vlan_vid_gte: Union[Unset, int] = UNSET,
    vlan_vid_lt: Union[Unset, int] = UNSET,
    vlan_vid_lte: Union[Unset, int] = UNSET,
    vlan_vid_n: Union[Unset, int] = UNSET,
    vminterface: Union[Unset, list[str]] = UNSET,
    vminterface_n: Union[Unset, list[str]] = UNSET,
    vminterface_id: Union[Unset, list[int]] = UNSET,
    vminterface_id_n: Union[Unset, list[int]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_assigned_object_id: Union[Unset, list[int]] = UNSET
    if not isinstance(assigned_object_id, Unset):
        json_assigned_object_id = assigned_object_id

    params["assigned_object_id"] = json_assigned_object_id

    params["assigned_object_id__empty"] = assigned_object_id_empty

    json_assigned_object_id_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(assigned_object_id_gt, Unset):
        json_assigned_object_id_gt = assigned_object_id_gt

    params["assigned_object_id__gt"] = json_assigned_object_id_gt

    json_assigned_object_id_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(assigned_object_id_gte, Unset):
        json_assigned_object_id_gte = assigned_object_id_gte

    params["assigned_object_id__gte"] = json_assigned_object_id_gte

    json_assigned_object_id_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(assigned_object_id_lt, Unset):
        json_assigned_object_id_lt = assigned_object_id_lt

    params["assigned_object_id__lt"] = json_assigned_object_id_lt

    json_assigned_object_id_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(assigned_object_id_lte, Unset):
        json_assigned_object_id_lte = assigned_object_id_lte

    params["assigned_object_id__lte"] = json_assigned_object_id_lte

    json_assigned_object_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(assigned_object_id_n, Unset):
        json_assigned_object_id_n = assigned_object_id_n

    params["assigned_object_id__n"] = json_assigned_object_id_n

    params["assigned_object_type"] = assigned_object_type

    params["assigned_object_type__n"] = assigned_object_type_n

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

    json_device: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(device, Unset):
        json_device = []
        for device_item_data in device:
            device_item: Union[None, str]
            device_item = device_item_data
            json_device.append(device_item)

    params["device"] = json_device

    json_device_n: Union[Unset, list[Union[None, str]]] = UNSET
    if not isinstance(device_n, Unset):
        json_device_n = []
        for device_n_item_data in device_n:
            device_n_item: Union[None, str]
            device_n_item = device_n_item_data
            json_device_n.append(device_n_item)

    params["device__n"] = json_device_n

    json_device_id: Union[Unset, list[int]] = UNSET
    if not isinstance(device_id, Unset):
        json_device_id = device_id

    params["device_id"] = json_device_id

    json_device_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(device_id_n, Unset):
        json_device_id_n = device_id_n

    params["device_id__n"] = json_device_id_n

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

    json_interface: Union[Unset, list[str]] = UNSET
    if not isinstance(interface, Unset):
        json_interface = interface

    params["interface"] = json_interface

    json_interface_n: Union[Unset, list[str]] = UNSET
    if not isinstance(interface_n, Unset):
        json_interface_n = interface_n

    params["interface__n"] = json_interface_n

    json_interface_id: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_id, Unset):
        json_interface_id = interface_id

    params["interface_id"] = json_interface_id

    json_interface_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_id_n, Unset):
        json_interface_id_n = interface_id_n

    params["interface_id__n"] = json_interface_id_n

    json_l2vpn: Union[Unset, list[str]] = UNSET
    if not isinstance(l2vpn, Unset):
        json_l2vpn = l2vpn

    params["l2vpn"] = json_l2vpn

    json_l2vpn_n: Union[Unset, list[str]] = UNSET
    if not isinstance(l2vpn_n, Unset):
        json_l2vpn_n = l2vpn_n

    params["l2vpn__n"] = json_l2vpn_n

    json_l2vpn_id: Union[Unset, list[int]] = UNSET
    if not isinstance(l2vpn_id, Unset):
        json_l2vpn_id = l2vpn_id

    params["l2vpn_id"] = json_l2vpn_id

    json_l2vpn_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(l2vpn_id_n, Unset):
        json_l2vpn_id_n = l2vpn_id_n

    params["l2vpn_id__n"] = json_l2vpn_id_n

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

    json_region: Union[Unset, list[str]] = UNSET
    if not isinstance(region, Unset):
        json_region = region

    params["region"] = json_region

    json_region_id: Union[Unset, list[int]] = UNSET
    if not isinstance(region_id, Unset):
        json_region_id = region_id

    params["region_id"] = json_region_id

    json_site: Union[Unset, list[str]] = UNSET
    if not isinstance(site, Unset):
        json_site = site

    params["site"] = json_site

    json_site_id: Union[Unset, list[int]] = UNSET
    if not isinstance(site_id, Unset):
        json_site_id = site_id

    params["site_id"] = json_site_id

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

    json_virtual_machine: Union[Unset, list[str]] = UNSET
    if not isinstance(virtual_machine, Unset):
        json_virtual_machine = virtual_machine

    params["virtual_machine"] = json_virtual_machine

    json_virtual_machine_n: Union[Unset, list[str]] = UNSET
    if not isinstance(virtual_machine_n, Unset):
        json_virtual_machine_n = virtual_machine_n

    params["virtual_machine__n"] = json_virtual_machine_n

    json_virtual_machine_id: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_machine_id, Unset):
        json_virtual_machine_id = virtual_machine_id

    params["virtual_machine_id"] = json_virtual_machine_id

    json_virtual_machine_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_machine_id_n, Unset):
        json_virtual_machine_id_n = virtual_machine_id_n

    params["virtual_machine_id__n"] = json_virtual_machine_id_n

    json_vlan: Union[Unset, list[str]] = UNSET
    if not isinstance(vlan, Unset):
        json_vlan = vlan

    params["vlan"] = json_vlan

    json_vlan_n: Union[Unset, list[str]] = UNSET
    if not isinstance(vlan_n, Unset):
        json_vlan_n = vlan_n

    params["vlan__n"] = json_vlan_n

    json_vlan_id: Union[Unset, list[int]] = UNSET
    if not isinstance(vlan_id, Unset):
        json_vlan_id = vlan_id

    params["vlan_id"] = json_vlan_id

    json_vlan_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(vlan_id_n, Unset):
        json_vlan_id_n = vlan_id_n

    params["vlan_id__n"] = json_vlan_id_n

    params["vlan_vid"] = vlan_vid

    params["vlan_vid__empty"] = vlan_vid_empty

    params["vlan_vid__gt"] = vlan_vid_gt

    params["vlan_vid__gte"] = vlan_vid_gte

    params["vlan_vid__lt"] = vlan_vid_lt

    params["vlan_vid__lte"] = vlan_vid_lte

    params["vlan_vid__n"] = vlan_vid_n

    json_vminterface: Union[Unset, list[str]] = UNSET
    if not isinstance(vminterface, Unset):
        json_vminterface = vminterface

    params["vminterface"] = json_vminterface

    json_vminterface_n: Union[Unset, list[str]] = UNSET
    if not isinstance(vminterface_n, Unset):
        json_vminterface_n = vminterface_n

    params["vminterface__n"] = json_vminterface_n

    json_vminterface_id: Union[Unset, list[int]] = UNSET
    if not isinstance(vminterface_id, Unset):
        json_vminterface_id = vminterface_id

    params["vminterface_id"] = json_vminterface_id

    json_vminterface_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(vminterface_id_n, Unset):
        json_vminterface_id_n = vminterface_id_n

    params["vminterface_id__n"] = json_vminterface_id_n

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/vpn/l2vpn-terminations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedL2VPNTerminationList]:
    if response.status_code == 200:
        response_200 = PaginatedL2VPNTerminationList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedL2VPNTerminationList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    assigned_object_id: Union[Unset, list[int]] = UNSET,
    assigned_object_id_empty: Union[Unset, bool] = UNSET,
    assigned_object_id_gt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_gte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_n: Union[Unset, list[int]] = UNSET,
    assigned_object_type: Union[Unset, str] = UNSET,
    assigned_object_type_n: Union[Unset, str] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    device_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface: Union[Unset, list[str]] = UNSET,
    interface_n: Union[Unset, list[str]] = UNSET,
    interface_id: Union[Unset, list[int]] = UNSET,
    interface_id_n: Union[Unset, list[int]] = UNSET,
    l2vpn: Union[Unset, list[str]] = UNSET,
    l2vpn_n: Union[Unset, list[str]] = UNSET,
    l2vpn_id: Union[Unset, list[int]] = UNSET,
    l2vpn_id_n: Union[Unset, list[int]] = UNSET,
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
    region: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[int]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_machine: Union[Unset, list[str]] = UNSET,
    virtual_machine_n: Union[Unset, list[str]] = UNSET,
    virtual_machine_id: Union[Unset, list[int]] = UNSET,
    virtual_machine_id_n: Union[Unset, list[int]] = UNSET,
    vlan: Union[Unset, list[str]] = UNSET,
    vlan_n: Union[Unset, list[str]] = UNSET,
    vlan_id: Union[Unset, list[int]] = UNSET,
    vlan_id_n: Union[Unset, list[int]] = UNSET,
    vlan_vid: Union[Unset, int] = UNSET,
    vlan_vid_empty: Union[Unset, int] = UNSET,
    vlan_vid_gt: Union[Unset, int] = UNSET,
    vlan_vid_gte: Union[Unset, int] = UNSET,
    vlan_vid_lt: Union[Unset, int] = UNSET,
    vlan_vid_lte: Union[Unset, int] = UNSET,
    vlan_vid_n: Union[Unset, int] = UNSET,
    vminterface: Union[Unset, list[str]] = UNSET,
    vminterface_n: Union[Unset, list[str]] = UNSET,
    vminterface_id: Union[Unset, list[int]] = UNSET,
    vminterface_id_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedL2VPNTerminationList]:
    """Get a list of L2VPN termination objects.

    Args:
        assigned_object_id (Union[Unset, list[int]]):
        assigned_object_id_empty (Union[Unset, bool]):
        assigned_object_id_gt (Union[Unset, list[int]]):
        assigned_object_id_gte (Union[Unset, list[int]]):
        assigned_object_id_lt (Union[Unset, list[int]]):
        assigned_object_id_lte (Union[Unset, list[int]]):
        assigned_object_id_n (Union[Unset, list[int]]):
        assigned_object_type (Union[Unset, str]):
        assigned_object_type_n (Union[Unset, str]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        device (Union[Unset, list[Union[None, str]]]):
        device_n (Union[Unset, list[Union[None, str]]]):
        device_id (Union[Unset, list[int]]):
        device_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface (Union[Unset, list[str]]):
        interface_n (Union[Unset, list[str]]):
        interface_id (Union[Unset, list[int]]):
        interface_id_n (Union[Unset, list[int]]):
        l2vpn (Union[Unset, list[str]]):
        l2vpn_n (Union[Unset, list[str]]):
        l2vpn_id (Union[Unset, list[int]]):
        l2vpn_id_n (Union[Unset, list[int]]):
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
        region (Union[Unset, list[str]]):
        region_id (Union[Unset, list[int]]):
        site (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        virtual_machine (Union[Unset, list[str]]):
        virtual_machine_n (Union[Unset, list[str]]):
        virtual_machine_id (Union[Unset, list[int]]):
        virtual_machine_id_n (Union[Unset, list[int]]):
        vlan (Union[Unset, list[str]]):
        vlan_n (Union[Unset, list[str]]):
        vlan_id (Union[Unset, list[int]]):
        vlan_id_n (Union[Unset, list[int]]):
        vlan_vid (Union[Unset, int]):
        vlan_vid_empty (Union[Unset, int]):
        vlan_vid_gt (Union[Unset, int]):
        vlan_vid_gte (Union[Unset, int]):
        vlan_vid_lt (Union[Unset, int]):
        vlan_vid_lte (Union[Unset, int]):
        vlan_vid_n (Union[Unset, int]):
        vminterface (Union[Unset, list[str]]):
        vminterface_n (Union[Unset, list[str]]):
        vminterface_id (Union[Unset, list[int]]):
        vminterface_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedL2VPNTerminationList]
    """

    kwargs = _get_kwargs(
        assigned_object_id=assigned_object_id,
        assigned_object_id_empty=assigned_object_id_empty,
        assigned_object_id_gt=assigned_object_id_gt,
        assigned_object_id_gte=assigned_object_id_gte,
        assigned_object_id_lt=assigned_object_id_lt,
        assigned_object_id_lte=assigned_object_id_lte,
        assigned_object_id_n=assigned_object_id_n,
        assigned_object_type=assigned_object_type,
        assigned_object_type_n=assigned_object_type_n,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        device=device,
        device_n=device_n,
        device_id=device_id,
        device_id_n=device_id_n,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface=interface,
        interface_n=interface_n,
        interface_id=interface_id,
        interface_id_n=interface_id_n,
        l2vpn=l2vpn,
        l2vpn_n=l2vpn_n,
        l2vpn_id=l2vpn_id,
        l2vpn_id_n=l2vpn_id_n,
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
        region=region,
        region_id=region_id,
        site=site,
        site_id=site_id,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
        virtual_machine=virtual_machine,
        virtual_machine_n=virtual_machine_n,
        virtual_machine_id=virtual_machine_id,
        virtual_machine_id_n=virtual_machine_id_n,
        vlan=vlan,
        vlan_n=vlan_n,
        vlan_id=vlan_id,
        vlan_id_n=vlan_id_n,
        vlan_vid=vlan_vid,
        vlan_vid_empty=vlan_vid_empty,
        vlan_vid_gt=vlan_vid_gt,
        vlan_vid_gte=vlan_vid_gte,
        vlan_vid_lt=vlan_vid_lt,
        vlan_vid_lte=vlan_vid_lte,
        vlan_vid_n=vlan_vid_n,
        vminterface=vminterface,
        vminterface_n=vminterface_n,
        vminterface_id=vminterface_id,
        vminterface_id_n=vminterface_id_n,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    assigned_object_id: Union[Unset, list[int]] = UNSET,
    assigned_object_id_empty: Union[Unset, bool] = UNSET,
    assigned_object_id_gt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_gte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_n: Union[Unset, list[int]] = UNSET,
    assigned_object_type: Union[Unset, str] = UNSET,
    assigned_object_type_n: Union[Unset, str] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    device_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface: Union[Unset, list[str]] = UNSET,
    interface_n: Union[Unset, list[str]] = UNSET,
    interface_id: Union[Unset, list[int]] = UNSET,
    interface_id_n: Union[Unset, list[int]] = UNSET,
    l2vpn: Union[Unset, list[str]] = UNSET,
    l2vpn_n: Union[Unset, list[str]] = UNSET,
    l2vpn_id: Union[Unset, list[int]] = UNSET,
    l2vpn_id_n: Union[Unset, list[int]] = UNSET,
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
    region: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[int]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_machine: Union[Unset, list[str]] = UNSET,
    virtual_machine_n: Union[Unset, list[str]] = UNSET,
    virtual_machine_id: Union[Unset, list[int]] = UNSET,
    virtual_machine_id_n: Union[Unset, list[int]] = UNSET,
    vlan: Union[Unset, list[str]] = UNSET,
    vlan_n: Union[Unset, list[str]] = UNSET,
    vlan_id: Union[Unset, list[int]] = UNSET,
    vlan_id_n: Union[Unset, list[int]] = UNSET,
    vlan_vid: Union[Unset, int] = UNSET,
    vlan_vid_empty: Union[Unset, int] = UNSET,
    vlan_vid_gt: Union[Unset, int] = UNSET,
    vlan_vid_gte: Union[Unset, int] = UNSET,
    vlan_vid_lt: Union[Unset, int] = UNSET,
    vlan_vid_lte: Union[Unset, int] = UNSET,
    vlan_vid_n: Union[Unset, int] = UNSET,
    vminterface: Union[Unset, list[str]] = UNSET,
    vminterface_n: Union[Unset, list[str]] = UNSET,
    vminterface_id: Union[Unset, list[int]] = UNSET,
    vminterface_id_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedL2VPNTerminationList]:
    """Get a list of L2VPN termination objects.

    Args:
        assigned_object_id (Union[Unset, list[int]]):
        assigned_object_id_empty (Union[Unset, bool]):
        assigned_object_id_gt (Union[Unset, list[int]]):
        assigned_object_id_gte (Union[Unset, list[int]]):
        assigned_object_id_lt (Union[Unset, list[int]]):
        assigned_object_id_lte (Union[Unset, list[int]]):
        assigned_object_id_n (Union[Unset, list[int]]):
        assigned_object_type (Union[Unset, str]):
        assigned_object_type_n (Union[Unset, str]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        device (Union[Unset, list[Union[None, str]]]):
        device_n (Union[Unset, list[Union[None, str]]]):
        device_id (Union[Unset, list[int]]):
        device_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface (Union[Unset, list[str]]):
        interface_n (Union[Unset, list[str]]):
        interface_id (Union[Unset, list[int]]):
        interface_id_n (Union[Unset, list[int]]):
        l2vpn (Union[Unset, list[str]]):
        l2vpn_n (Union[Unset, list[str]]):
        l2vpn_id (Union[Unset, list[int]]):
        l2vpn_id_n (Union[Unset, list[int]]):
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
        region (Union[Unset, list[str]]):
        region_id (Union[Unset, list[int]]):
        site (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        virtual_machine (Union[Unset, list[str]]):
        virtual_machine_n (Union[Unset, list[str]]):
        virtual_machine_id (Union[Unset, list[int]]):
        virtual_machine_id_n (Union[Unset, list[int]]):
        vlan (Union[Unset, list[str]]):
        vlan_n (Union[Unset, list[str]]):
        vlan_id (Union[Unset, list[int]]):
        vlan_id_n (Union[Unset, list[int]]):
        vlan_vid (Union[Unset, int]):
        vlan_vid_empty (Union[Unset, int]):
        vlan_vid_gt (Union[Unset, int]):
        vlan_vid_gte (Union[Unset, int]):
        vlan_vid_lt (Union[Unset, int]):
        vlan_vid_lte (Union[Unset, int]):
        vlan_vid_n (Union[Unset, int]):
        vminterface (Union[Unset, list[str]]):
        vminterface_n (Union[Unset, list[str]]):
        vminterface_id (Union[Unset, list[int]]):
        vminterface_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedL2VPNTerminationList
    """

    return sync_detailed(
        client=client,
        assigned_object_id=assigned_object_id,
        assigned_object_id_empty=assigned_object_id_empty,
        assigned_object_id_gt=assigned_object_id_gt,
        assigned_object_id_gte=assigned_object_id_gte,
        assigned_object_id_lt=assigned_object_id_lt,
        assigned_object_id_lte=assigned_object_id_lte,
        assigned_object_id_n=assigned_object_id_n,
        assigned_object_type=assigned_object_type,
        assigned_object_type_n=assigned_object_type_n,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        device=device,
        device_n=device_n,
        device_id=device_id,
        device_id_n=device_id_n,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface=interface,
        interface_n=interface_n,
        interface_id=interface_id,
        interface_id_n=interface_id_n,
        l2vpn=l2vpn,
        l2vpn_n=l2vpn_n,
        l2vpn_id=l2vpn_id,
        l2vpn_id_n=l2vpn_id_n,
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
        region=region,
        region_id=region_id,
        site=site,
        site_id=site_id,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
        virtual_machine=virtual_machine,
        virtual_machine_n=virtual_machine_n,
        virtual_machine_id=virtual_machine_id,
        virtual_machine_id_n=virtual_machine_id_n,
        vlan=vlan,
        vlan_n=vlan_n,
        vlan_id=vlan_id,
        vlan_id_n=vlan_id_n,
        vlan_vid=vlan_vid,
        vlan_vid_empty=vlan_vid_empty,
        vlan_vid_gt=vlan_vid_gt,
        vlan_vid_gte=vlan_vid_gte,
        vlan_vid_lt=vlan_vid_lt,
        vlan_vid_lte=vlan_vid_lte,
        vlan_vid_n=vlan_vid_n,
        vminterface=vminterface,
        vminterface_n=vminterface_n,
        vminterface_id=vminterface_id,
        vminterface_id_n=vminterface_id_n,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    assigned_object_id: Union[Unset, list[int]] = UNSET,
    assigned_object_id_empty: Union[Unset, bool] = UNSET,
    assigned_object_id_gt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_gte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_n: Union[Unset, list[int]] = UNSET,
    assigned_object_type: Union[Unset, str] = UNSET,
    assigned_object_type_n: Union[Unset, str] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    device_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface: Union[Unset, list[str]] = UNSET,
    interface_n: Union[Unset, list[str]] = UNSET,
    interface_id: Union[Unset, list[int]] = UNSET,
    interface_id_n: Union[Unset, list[int]] = UNSET,
    l2vpn: Union[Unset, list[str]] = UNSET,
    l2vpn_n: Union[Unset, list[str]] = UNSET,
    l2vpn_id: Union[Unset, list[int]] = UNSET,
    l2vpn_id_n: Union[Unset, list[int]] = UNSET,
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
    region: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[int]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_machine: Union[Unset, list[str]] = UNSET,
    virtual_machine_n: Union[Unset, list[str]] = UNSET,
    virtual_machine_id: Union[Unset, list[int]] = UNSET,
    virtual_machine_id_n: Union[Unset, list[int]] = UNSET,
    vlan: Union[Unset, list[str]] = UNSET,
    vlan_n: Union[Unset, list[str]] = UNSET,
    vlan_id: Union[Unset, list[int]] = UNSET,
    vlan_id_n: Union[Unset, list[int]] = UNSET,
    vlan_vid: Union[Unset, int] = UNSET,
    vlan_vid_empty: Union[Unset, int] = UNSET,
    vlan_vid_gt: Union[Unset, int] = UNSET,
    vlan_vid_gte: Union[Unset, int] = UNSET,
    vlan_vid_lt: Union[Unset, int] = UNSET,
    vlan_vid_lte: Union[Unset, int] = UNSET,
    vlan_vid_n: Union[Unset, int] = UNSET,
    vminterface: Union[Unset, list[str]] = UNSET,
    vminterface_n: Union[Unset, list[str]] = UNSET,
    vminterface_id: Union[Unset, list[int]] = UNSET,
    vminterface_id_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedL2VPNTerminationList]:
    """Get a list of L2VPN termination objects.

    Args:
        assigned_object_id (Union[Unset, list[int]]):
        assigned_object_id_empty (Union[Unset, bool]):
        assigned_object_id_gt (Union[Unset, list[int]]):
        assigned_object_id_gte (Union[Unset, list[int]]):
        assigned_object_id_lt (Union[Unset, list[int]]):
        assigned_object_id_lte (Union[Unset, list[int]]):
        assigned_object_id_n (Union[Unset, list[int]]):
        assigned_object_type (Union[Unset, str]):
        assigned_object_type_n (Union[Unset, str]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        device (Union[Unset, list[Union[None, str]]]):
        device_n (Union[Unset, list[Union[None, str]]]):
        device_id (Union[Unset, list[int]]):
        device_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface (Union[Unset, list[str]]):
        interface_n (Union[Unset, list[str]]):
        interface_id (Union[Unset, list[int]]):
        interface_id_n (Union[Unset, list[int]]):
        l2vpn (Union[Unset, list[str]]):
        l2vpn_n (Union[Unset, list[str]]):
        l2vpn_id (Union[Unset, list[int]]):
        l2vpn_id_n (Union[Unset, list[int]]):
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
        region (Union[Unset, list[str]]):
        region_id (Union[Unset, list[int]]):
        site (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        virtual_machine (Union[Unset, list[str]]):
        virtual_machine_n (Union[Unset, list[str]]):
        virtual_machine_id (Union[Unset, list[int]]):
        virtual_machine_id_n (Union[Unset, list[int]]):
        vlan (Union[Unset, list[str]]):
        vlan_n (Union[Unset, list[str]]):
        vlan_id (Union[Unset, list[int]]):
        vlan_id_n (Union[Unset, list[int]]):
        vlan_vid (Union[Unset, int]):
        vlan_vid_empty (Union[Unset, int]):
        vlan_vid_gt (Union[Unset, int]):
        vlan_vid_gte (Union[Unset, int]):
        vlan_vid_lt (Union[Unset, int]):
        vlan_vid_lte (Union[Unset, int]):
        vlan_vid_n (Union[Unset, int]):
        vminterface (Union[Unset, list[str]]):
        vminterface_n (Union[Unset, list[str]]):
        vminterface_id (Union[Unset, list[int]]):
        vminterface_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedL2VPNTerminationList]
    """

    kwargs = _get_kwargs(
        assigned_object_id=assigned_object_id,
        assigned_object_id_empty=assigned_object_id_empty,
        assigned_object_id_gt=assigned_object_id_gt,
        assigned_object_id_gte=assigned_object_id_gte,
        assigned_object_id_lt=assigned_object_id_lt,
        assigned_object_id_lte=assigned_object_id_lte,
        assigned_object_id_n=assigned_object_id_n,
        assigned_object_type=assigned_object_type,
        assigned_object_type_n=assigned_object_type_n,
        created=created,
        created_empty=created_empty,
        created_gt=created_gt,
        created_gte=created_gte,
        created_lt=created_lt,
        created_lte=created_lte,
        created_n=created_n,
        created_by_request=created_by_request,
        device=device,
        device_n=device_n,
        device_id=device_id,
        device_id_n=device_id_n,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface=interface,
        interface_n=interface_n,
        interface_id=interface_id,
        interface_id_n=interface_id_n,
        l2vpn=l2vpn,
        l2vpn_n=l2vpn_n,
        l2vpn_id=l2vpn_id,
        l2vpn_id_n=l2vpn_id_n,
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
        region=region,
        region_id=region_id,
        site=site,
        site_id=site_id,
        tag=tag,
        tag_n=tag_n,
        tag_id=tag_id,
        tag_id_n=tag_id_n,
        updated_by_request=updated_by_request,
        virtual_machine=virtual_machine,
        virtual_machine_n=virtual_machine_n,
        virtual_machine_id=virtual_machine_id,
        virtual_machine_id_n=virtual_machine_id_n,
        vlan=vlan,
        vlan_n=vlan_n,
        vlan_id=vlan_id,
        vlan_id_n=vlan_id_n,
        vlan_vid=vlan_vid,
        vlan_vid_empty=vlan_vid_empty,
        vlan_vid_gt=vlan_vid_gt,
        vlan_vid_gte=vlan_vid_gte,
        vlan_vid_lt=vlan_vid_lt,
        vlan_vid_lte=vlan_vid_lte,
        vlan_vid_n=vlan_vid_n,
        vminterface=vminterface,
        vminterface_n=vminterface_n,
        vminterface_id=vminterface_id,
        vminterface_id_n=vminterface_id_n,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    assigned_object_id: Union[Unset, list[int]] = UNSET,
    assigned_object_id_empty: Union[Unset, bool] = UNSET,
    assigned_object_id_gt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_gte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lt: Union[Unset, list[int]] = UNSET,
    assigned_object_id_lte: Union[Unset, list[int]] = UNSET,
    assigned_object_id_n: Union[Unset, list[int]] = UNSET,
    assigned_object_type: Union[Unset, str] = UNSET,
    assigned_object_type_n: Union[Unset, str] = UNSET,
    created: Union[Unset, list[datetime.datetime]] = UNSET,
    created_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    created_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    created_n: Union[Unset, list[datetime.datetime]] = UNSET,
    created_by_request: Union[Unset, UUID] = UNSET,
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[int]] = UNSET,
    device_id_n: Union[Unset, list[int]] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface: Union[Unset, list[str]] = UNSET,
    interface_n: Union[Unset, list[str]] = UNSET,
    interface_id: Union[Unset, list[int]] = UNSET,
    interface_id_n: Union[Unset, list[int]] = UNSET,
    l2vpn: Union[Unset, list[str]] = UNSET,
    l2vpn_n: Union[Unset, list[str]] = UNSET,
    l2vpn_id: Union[Unset, list[int]] = UNSET,
    l2vpn_id_n: Union[Unset, list[int]] = UNSET,
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
    region: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[int]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[int]] = UNSET,
    tag: Union[Unset, list[str]] = UNSET,
    tag_n: Union[Unset, list[str]] = UNSET,
    tag_id: Union[Unset, list[int]] = UNSET,
    tag_id_n: Union[Unset, list[int]] = UNSET,
    updated_by_request: Union[Unset, UUID] = UNSET,
    virtual_machine: Union[Unset, list[str]] = UNSET,
    virtual_machine_n: Union[Unset, list[str]] = UNSET,
    virtual_machine_id: Union[Unset, list[int]] = UNSET,
    virtual_machine_id_n: Union[Unset, list[int]] = UNSET,
    vlan: Union[Unset, list[str]] = UNSET,
    vlan_n: Union[Unset, list[str]] = UNSET,
    vlan_id: Union[Unset, list[int]] = UNSET,
    vlan_id_n: Union[Unset, list[int]] = UNSET,
    vlan_vid: Union[Unset, int] = UNSET,
    vlan_vid_empty: Union[Unset, int] = UNSET,
    vlan_vid_gt: Union[Unset, int] = UNSET,
    vlan_vid_gte: Union[Unset, int] = UNSET,
    vlan_vid_lt: Union[Unset, int] = UNSET,
    vlan_vid_lte: Union[Unset, int] = UNSET,
    vlan_vid_n: Union[Unset, int] = UNSET,
    vminterface: Union[Unset, list[str]] = UNSET,
    vminterface_n: Union[Unset, list[str]] = UNSET,
    vminterface_id: Union[Unset, list[int]] = UNSET,
    vminterface_id_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedL2VPNTerminationList]:
    """Get a list of L2VPN termination objects.

    Args:
        assigned_object_id (Union[Unset, list[int]]):
        assigned_object_id_empty (Union[Unset, bool]):
        assigned_object_id_gt (Union[Unset, list[int]]):
        assigned_object_id_gte (Union[Unset, list[int]]):
        assigned_object_id_lt (Union[Unset, list[int]]):
        assigned_object_id_lte (Union[Unset, list[int]]):
        assigned_object_id_n (Union[Unset, list[int]]):
        assigned_object_type (Union[Unset, str]):
        assigned_object_type_n (Union[Unset, str]):
        created (Union[Unset, list[datetime.datetime]]):
        created_empty (Union[Unset, list[datetime.datetime]]):
        created_gt (Union[Unset, list[datetime.datetime]]):
        created_gte (Union[Unset, list[datetime.datetime]]):
        created_lt (Union[Unset, list[datetime.datetime]]):
        created_lte (Union[Unset, list[datetime.datetime]]):
        created_n (Union[Unset, list[datetime.datetime]]):
        created_by_request (Union[Unset, UUID]):
        device (Union[Unset, list[Union[None, str]]]):
        device_n (Union[Unset, list[Union[None, str]]]):
        device_id (Union[Unset, list[int]]):
        device_id_n (Union[Unset, list[int]]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface (Union[Unset, list[str]]):
        interface_n (Union[Unset, list[str]]):
        interface_id (Union[Unset, list[int]]):
        interface_id_n (Union[Unset, list[int]]):
        l2vpn (Union[Unset, list[str]]):
        l2vpn_n (Union[Unset, list[str]]):
        l2vpn_id (Union[Unset, list[int]]):
        l2vpn_id_n (Union[Unset, list[int]]):
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
        region (Union[Unset, list[str]]):
        region_id (Union[Unset, list[int]]):
        site (Union[Unset, list[str]]):
        site_id (Union[Unset, list[int]]):
        tag (Union[Unset, list[str]]):
        tag_n (Union[Unset, list[str]]):
        tag_id (Union[Unset, list[int]]):
        tag_id_n (Union[Unset, list[int]]):
        updated_by_request (Union[Unset, UUID]):
        virtual_machine (Union[Unset, list[str]]):
        virtual_machine_n (Union[Unset, list[str]]):
        virtual_machine_id (Union[Unset, list[int]]):
        virtual_machine_id_n (Union[Unset, list[int]]):
        vlan (Union[Unset, list[str]]):
        vlan_n (Union[Unset, list[str]]):
        vlan_id (Union[Unset, list[int]]):
        vlan_id_n (Union[Unset, list[int]]):
        vlan_vid (Union[Unset, int]):
        vlan_vid_empty (Union[Unset, int]):
        vlan_vid_gt (Union[Unset, int]):
        vlan_vid_gte (Union[Unset, int]):
        vlan_vid_lt (Union[Unset, int]):
        vlan_vid_lte (Union[Unset, int]):
        vlan_vid_n (Union[Unset, int]):
        vminterface (Union[Unset, list[str]]):
        vminterface_n (Union[Unset, list[str]]):
        vminterface_id (Union[Unset, list[int]]):
        vminterface_id_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedL2VPNTerminationList
    """

    return (
        await asyncio_detailed(
            client=client,
            assigned_object_id=assigned_object_id,
            assigned_object_id_empty=assigned_object_id_empty,
            assigned_object_id_gt=assigned_object_id_gt,
            assigned_object_id_gte=assigned_object_id_gte,
            assigned_object_id_lt=assigned_object_id_lt,
            assigned_object_id_lte=assigned_object_id_lte,
            assigned_object_id_n=assigned_object_id_n,
            assigned_object_type=assigned_object_type,
            assigned_object_type_n=assigned_object_type_n,
            created=created,
            created_empty=created_empty,
            created_gt=created_gt,
            created_gte=created_gte,
            created_lt=created_lt,
            created_lte=created_lte,
            created_n=created_n,
            created_by_request=created_by_request,
            device=device,
            device_n=device_n,
            device_id=device_id,
            device_id_n=device_id_n,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            interface=interface,
            interface_n=interface_n,
            interface_id=interface_id,
            interface_id_n=interface_id_n,
            l2vpn=l2vpn,
            l2vpn_n=l2vpn_n,
            l2vpn_id=l2vpn_id,
            l2vpn_id_n=l2vpn_id_n,
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
            region=region,
            region_id=region_id,
            site=site,
            site_id=site_id,
            tag=tag,
            tag_n=tag_n,
            tag_id=tag_id,
            tag_id_n=tag_id_n,
            updated_by_request=updated_by_request,
            virtual_machine=virtual_machine,
            virtual_machine_n=virtual_machine_n,
            virtual_machine_id=virtual_machine_id,
            virtual_machine_id_n=virtual_machine_id_n,
            vlan=vlan,
            vlan_n=vlan_n,
            vlan_id=vlan_id,
            vlan_id_n=vlan_id_n,
            vlan_vid=vlan_vid,
            vlan_vid_empty=vlan_vid_empty,
            vlan_vid_gt=vlan_vid_gt,
            vlan_vid_gte=vlan_vid_gte,
            vlan_vid_lt=vlan_vid_lt,
            vlan_vid_lte=vlan_vid_lte,
            vlan_vid_n=vlan_vid_n,
            vminterface=vminterface,
            vminterface_n=vminterface_n,
            vminterface_id=vminterface_id,
            vminterface_id_n=vminterface_id_n,
        )
    ).parsed
