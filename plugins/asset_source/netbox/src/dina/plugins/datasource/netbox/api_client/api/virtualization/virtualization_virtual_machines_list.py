import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_virtual_machine_with_config_context_list import (
    PaginatedVirtualMachineWithConfigContextList,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cluster: Union[Unset, list[str]] = UNSET,
    cluster_n: Union[Unset, list[str]] = UNSET,
    cluster_group: Union[Unset, list[str]] = UNSET,
    cluster_group_n: Union[Unset, list[str]] = UNSET,
    cluster_group_id: Union[Unset, list[int]] = UNSET,
    cluster_group_id_n: Union[Unset, list[int]] = UNSET,
    cluster_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cluster_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cluster_type: Union[Unset, list[str]] = UNSET,
    cluster_type_n: Union[Unset, list[str]] = UNSET,
    cluster_type_id: Union[Unset, list[int]] = UNSET,
    cluster_type_id_n: Union[Unset, list[int]] = UNSET,
    config_template_id: Union[Unset, list[Union[None, int]]] = UNSET,
    config_template_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[Union[None, int]]] = UNSET,
    device_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    disk: Union[Unset, list[int]] = UNSET,
    disk_empty: Union[Unset, bool] = UNSET,
    disk_gt: Union[Unset, list[int]] = UNSET,
    disk_gte: Union[Unset, list[int]] = UNSET,
    disk_lt: Union[Unset, list[int]] = UNSET,
    disk_lte: Union[Unset, list[int]] = UNSET,
    disk_n: Union[Unset, list[int]] = UNSET,
    has_primary_ip: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_count: Union[Unset, list[int]] = UNSET,
    interface_count_empty: Union[Unset, bool] = UNSET,
    interface_count_gt: Union[Unset, list[int]] = UNSET,
    interface_count_gte: Union[Unset, list[int]] = UNSET,
    interface_count_lt: Union[Unset, list[int]] = UNSET,
    interface_count_lte: Union[Unset, list[int]] = UNSET,
    interface_count_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    local_context_data: Union[Unset, bool] = UNSET,
    mac_address: Union[Unset, list[str]] = UNSET,
    mac_address_ic: Union[Unset, list[str]] = UNSET,
    mac_address_ie: Union[Unset, list[str]] = UNSET,
    mac_address_iew: Union[Unset, list[str]] = UNSET,
    mac_address_isw: Union[Unset, list[str]] = UNSET,
    mac_address_n: Union[Unset, list[str]] = UNSET,
    mac_address_nic: Union[Unset, list[str]] = UNSET,
    mac_address_nie: Union[Unset, list[str]] = UNSET,
    mac_address_niew: Union[Unset, list[str]] = UNSET,
    mac_address_nisw: Union[Unset, list[str]] = UNSET,
    memory: Union[Unset, list[int]] = UNSET,
    memory_empty: Union[Unset, bool] = UNSET,
    memory_gt: Union[Unset, list[int]] = UNSET,
    memory_gte: Union[Unset, list[int]] = UNSET,
    memory_lt: Union[Unset, list[int]] = UNSET,
    memory_lte: Union[Unset, list[int]] = UNSET,
    memory_n: Union[Unset, list[int]] = UNSET,
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
    platform: Union[Unset, list[str]] = UNSET,
    platform_n: Union[Unset, list[str]] = UNSET,
    platform_id: Union[Unset, list[Union[None, int]]] = UNSET,
    platform_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    primary_ip4: Union[Unset, list[str]] = UNSET,
    primary_ip4_n: Union[Unset, list[str]] = UNSET,
    primary_ip4_id: Union[Unset, list[int]] = UNSET,
    primary_ip4_id_n: Union[Unset, list[int]] = UNSET,
    primary_ip6: Union[Unset, list[str]] = UNSET,
    primary_ip6_n: Union[Unset, list[str]] = UNSET,
    primary_ip6_id: Union[Unset, list[int]] = UNSET,
    primary_ip6_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[str]] = UNSET,
    role_id_n: Union[Unset, list[str]] = UNSET,
    serial: Union[Unset, list[str]] = UNSET,
    serial_empty: Union[Unset, bool] = UNSET,
    serial_ic: Union[Unset, list[str]] = UNSET,
    serial_ie: Union[Unset, list[str]] = UNSET,
    serial_iew: Union[Unset, list[str]] = UNSET,
    serial_isw: Union[Unset, list[str]] = UNSET,
    serial_n: Union[Unset, list[str]] = UNSET,
    serial_nic: Union[Unset, list[str]] = UNSET,
    serial_nie: Union[Unset, list[str]] = UNSET,
    serial_niew: Union[Unset, list[str]] = UNSET,
    serial_nisw: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[Union[None, int]]] = UNSET,
    site_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    vcpus: Union[Unset, list[float]] = UNSET,
    vcpus_empty: Union[Unset, bool] = UNSET,
    vcpus_gt: Union[Unset, list[float]] = UNSET,
    vcpus_gte: Union[Unset, list[float]] = UNSET,
    vcpus_lt: Union[Unset, list[float]] = UNSET,
    vcpus_lte: Union[Unset, list[float]] = UNSET,
    vcpus_n: Union[Unset, list[float]] = UNSET,
    virtual_disk_count: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_empty: Union[Unset, bool] = UNSET,
    virtual_disk_count_gt: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_gte: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_lt: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_lte: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_n: Union[Unset, list[int]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_cluster: Union[Unset, list[str]] = UNSET
    if not isinstance(cluster, Unset):
        json_cluster = cluster

    params["cluster"] = json_cluster

    json_cluster_n: Union[Unset, list[str]] = UNSET
    if not isinstance(cluster_n, Unset):
        json_cluster_n = cluster_n

    params["cluster__n"] = json_cluster_n

    json_cluster_group: Union[Unset, list[str]] = UNSET
    if not isinstance(cluster_group, Unset):
        json_cluster_group = cluster_group

    params["cluster_group"] = json_cluster_group

    json_cluster_group_n: Union[Unset, list[str]] = UNSET
    if not isinstance(cluster_group_n, Unset):
        json_cluster_group_n = cluster_group_n

    params["cluster_group__n"] = json_cluster_group_n

    json_cluster_group_id: Union[Unset, list[int]] = UNSET
    if not isinstance(cluster_group_id, Unset):
        json_cluster_group_id = cluster_group_id

    params["cluster_group_id"] = json_cluster_group_id

    json_cluster_group_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(cluster_group_id_n, Unset):
        json_cluster_group_id_n = cluster_group_id_n

    params["cluster_group_id__n"] = json_cluster_group_id_n

    json_cluster_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(cluster_id, Unset):
        json_cluster_id = []
        for cluster_id_item_data in cluster_id:
            cluster_id_item: Union[None, int]
            cluster_id_item = cluster_id_item_data
            json_cluster_id.append(cluster_id_item)

    params["cluster_id"] = json_cluster_id

    json_cluster_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(cluster_id_n, Unset):
        json_cluster_id_n = []
        for cluster_id_n_item_data in cluster_id_n:
            cluster_id_n_item: Union[None, int]
            cluster_id_n_item = cluster_id_n_item_data
            json_cluster_id_n.append(cluster_id_n_item)

    params["cluster_id__n"] = json_cluster_id_n

    json_cluster_type: Union[Unset, list[str]] = UNSET
    if not isinstance(cluster_type, Unset):
        json_cluster_type = cluster_type

    params["cluster_type"] = json_cluster_type

    json_cluster_type_n: Union[Unset, list[str]] = UNSET
    if not isinstance(cluster_type_n, Unset):
        json_cluster_type_n = cluster_type_n

    params["cluster_type__n"] = json_cluster_type_n

    json_cluster_type_id: Union[Unset, list[int]] = UNSET
    if not isinstance(cluster_type_id, Unset):
        json_cluster_type_id = cluster_type_id

    params["cluster_type_id"] = json_cluster_type_id

    json_cluster_type_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(cluster_type_id_n, Unset):
        json_cluster_type_id_n = cluster_type_id_n

    params["cluster_type_id__n"] = json_cluster_type_id_n

    json_config_template_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(config_template_id, Unset):
        json_config_template_id = []
        for config_template_id_item_data in config_template_id:
            config_template_id_item: Union[None, int]
            config_template_id_item = config_template_id_item_data
            json_config_template_id.append(config_template_id_item)

    params["config_template_id"] = json_config_template_id

    json_config_template_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(config_template_id_n, Unset):
        json_config_template_id_n = []
        for config_template_id_n_item_data in config_template_id_n:
            config_template_id_n_item: Union[None, int]
            config_template_id_n_item = config_template_id_n_item_data
            json_config_template_id_n.append(config_template_id_n_item)

    params["config_template_id__n"] = json_config_template_id_n

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

    json_device_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(device_id, Unset):
        json_device_id = []
        for device_id_item_data in device_id:
            device_id_item: Union[None, int]
            device_id_item = device_id_item_data
            json_device_id.append(device_id_item)

    params["device_id"] = json_device_id

    json_device_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(device_id_n, Unset):
        json_device_id_n = []
        for device_id_n_item_data in device_id_n:
            device_id_n_item: Union[None, int]
            device_id_n_item = device_id_n_item_data
            json_device_id_n.append(device_id_n_item)

    params["device_id__n"] = json_device_id_n

    json_disk: Union[Unset, list[int]] = UNSET
    if not isinstance(disk, Unset):
        json_disk = disk

    params["disk"] = json_disk

    params["disk__empty"] = disk_empty

    json_disk_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(disk_gt, Unset):
        json_disk_gt = disk_gt

    params["disk__gt"] = json_disk_gt

    json_disk_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(disk_gte, Unset):
        json_disk_gte = disk_gte

    params["disk__gte"] = json_disk_gte

    json_disk_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(disk_lt, Unset):
        json_disk_lt = disk_lt

    params["disk__lt"] = json_disk_lt

    json_disk_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(disk_lte, Unset):
        json_disk_lte = disk_lte

    params["disk__lte"] = json_disk_lte

    json_disk_n: Union[Unset, list[int]] = UNSET
    if not isinstance(disk_n, Unset):
        json_disk_n = disk_n

    params["disk__n"] = json_disk_n

    params["has_primary_ip"] = has_primary_ip

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

    json_interface_count: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_count, Unset):
        json_interface_count = interface_count

    params["interface_count"] = json_interface_count

    params["interface_count__empty"] = interface_count_empty

    json_interface_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_count_gt, Unset):
        json_interface_count_gt = interface_count_gt

    params["interface_count__gt"] = json_interface_count_gt

    json_interface_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_count_gte, Unset):
        json_interface_count_gte = interface_count_gte

    params["interface_count__gte"] = json_interface_count_gte

    json_interface_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_count_lt, Unset):
        json_interface_count_lt = interface_count_lt

    params["interface_count__lt"] = json_interface_count_lt

    json_interface_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_count_lte, Unset):
        json_interface_count_lte = interface_count_lte

    params["interface_count__lte"] = json_interface_count_lte

    json_interface_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(interface_count_n, Unset):
        json_interface_count_n = interface_count_n

    params["interface_count__n"] = json_interface_count_n

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

    params["local_context_data"] = local_context_data

    json_mac_address: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address, Unset):
        json_mac_address = mac_address

    params["mac_address"] = json_mac_address

    json_mac_address_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address_ic, Unset):
        json_mac_address_ic = mac_address_ic

    params["mac_address__ic"] = json_mac_address_ic

    json_mac_address_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address_ie, Unset):
        json_mac_address_ie = mac_address_ie

    params["mac_address__ie"] = json_mac_address_ie

    json_mac_address_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address_iew, Unset):
        json_mac_address_iew = mac_address_iew

    params["mac_address__iew"] = json_mac_address_iew

    json_mac_address_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address_isw, Unset):
        json_mac_address_isw = mac_address_isw

    params["mac_address__isw"] = json_mac_address_isw

    json_mac_address_n: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address_n, Unset):
        json_mac_address_n = mac_address_n

    params["mac_address__n"] = json_mac_address_n

    json_mac_address_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address_nic, Unset):
        json_mac_address_nic = mac_address_nic

    params["mac_address__nic"] = json_mac_address_nic

    json_mac_address_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address_nie, Unset):
        json_mac_address_nie = mac_address_nie

    params["mac_address__nie"] = json_mac_address_nie

    json_mac_address_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address_niew, Unset):
        json_mac_address_niew = mac_address_niew

    params["mac_address__niew"] = json_mac_address_niew

    json_mac_address_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address_nisw, Unset):
        json_mac_address_nisw = mac_address_nisw

    params["mac_address__nisw"] = json_mac_address_nisw

    json_memory: Union[Unset, list[int]] = UNSET
    if not isinstance(memory, Unset):
        json_memory = memory

    params["memory"] = json_memory

    params["memory__empty"] = memory_empty

    json_memory_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(memory_gt, Unset):
        json_memory_gt = memory_gt

    params["memory__gt"] = json_memory_gt

    json_memory_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(memory_gte, Unset):
        json_memory_gte = memory_gte

    params["memory__gte"] = json_memory_gte

    json_memory_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(memory_lt, Unset):
        json_memory_lt = memory_lt

    params["memory__lt"] = json_memory_lt

    json_memory_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(memory_lte, Unset):
        json_memory_lte = memory_lte

    params["memory__lte"] = json_memory_lte

    json_memory_n: Union[Unset, list[int]] = UNSET
    if not isinstance(memory_n, Unset):
        json_memory_n = memory_n

    params["memory__n"] = json_memory_n

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

    json_platform: Union[Unset, list[str]] = UNSET
    if not isinstance(platform, Unset):
        json_platform = platform

    params["platform"] = json_platform

    json_platform_n: Union[Unset, list[str]] = UNSET
    if not isinstance(platform_n, Unset):
        json_platform_n = platform_n

    params["platform__n"] = json_platform_n

    json_platform_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(platform_id, Unset):
        json_platform_id = []
        for platform_id_item_data in platform_id:
            platform_id_item: Union[None, int]
            platform_id_item = platform_id_item_data
            json_platform_id.append(platform_id_item)

    params["platform_id"] = json_platform_id

    json_platform_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(platform_id_n, Unset):
        json_platform_id_n = []
        for platform_id_n_item_data in platform_id_n:
            platform_id_n_item: Union[None, int]
            platform_id_n_item = platform_id_n_item_data
            json_platform_id_n.append(platform_id_n_item)

    params["platform_id__n"] = json_platform_id_n

    json_primary_ip4: Union[Unset, list[str]] = UNSET
    if not isinstance(primary_ip4, Unset):
        json_primary_ip4 = primary_ip4

    params["primary_ip4"] = json_primary_ip4

    json_primary_ip4_n: Union[Unset, list[str]] = UNSET
    if not isinstance(primary_ip4_n, Unset):
        json_primary_ip4_n = primary_ip4_n

    params["primary_ip4__n"] = json_primary_ip4_n

    json_primary_ip4_id: Union[Unset, list[int]] = UNSET
    if not isinstance(primary_ip4_id, Unset):
        json_primary_ip4_id = primary_ip4_id

    params["primary_ip4_id"] = json_primary_ip4_id

    json_primary_ip4_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(primary_ip4_id_n, Unset):
        json_primary_ip4_id_n = primary_ip4_id_n

    params["primary_ip4_id__n"] = json_primary_ip4_id_n

    json_primary_ip6: Union[Unset, list[str]] = UNSET
    if not isinstance(primary_ip6, Unset):
        json_primary_ip6 = primary_ip6

    params["primary_ip6"] = json_primary_ip6

    json_primary_ip6_n: Union[Unset, list[str]] = UNSET
    if not isinstance(primary_ip6_n, Unset):
        json_primary_ip6_n = primary_ip6_n

    params["primary_ip6__n"] = json_primary_ip6_n

    json_primary_ip6_id: Union[Unset, list[int]] = UNSET
    if not isinstance(primary_ip6_id, Unset):
        json_primary_ip6_id = primary_ip6_id

    params["primary_ip6_id"] = json_primary_ip6_id

    json_primary_ip6_id_n: Union[Unset, list[int]] = UNSET
    if not isinstance(primary_ip6_id_n, Unset):
        json_primary_ip6_id_n = primary_ip6_id_n

    params["primary_ip6_id__n"] = json_primary_ip6_id_n

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

    json_role: Union[Unset, list[str]] = UNSET
    if not isinstance(role, Unset):
        json_role = role

    params["role"] = json_role

    json_role_n: Union[Unset, list[str]] = UNSET
    if not isinstance(role_n, Unset):
        json_role_n = role_n

    params["role__n"] = json_role_n

    json_role_id: Union[Unset, list[str]] = UNSET
    if not isinstance(role_id, Unset):
        json_role_id = role_id

    params["role_id"] = json_role_id

    json_role_id_n: Union[Unset, list[str]] = UNSET
    if not isinstance(role_id_n, Unset):
        json_role_id_n = role_id_n

    params["role_id__n"] = json_role_id_n

    json_serial: Union[Unset, list[str]] = UNSET
    if not isinstance(serial, Unset):
        json_serial = serial

    params["serial"] = json_serial

    params["serial__empty"] = serial_empty

    json_serial_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_ic, Unset):
        json_serial_ic = serial_ic

    params["serial__ic"] = json_serial_ic

    json_serial_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_ie, Unset):
        json_serial_ie = serial_ie

    params["serial__ie"] = json_serial_ie

    json_serial_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_iew, Unset):
        json_serial_iew = serial_iew

    params["serial__iew"] = json_serial_iew

    json_serial_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_isw, Unset):
        json_serial_isw = serial_isw

    params["serial__isw"] = json_serial_isw

    json_serial_n: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_n, Unset):
        json_serial_n = serial_n

    params["serial__n"] = json_serial_n

    json_serial_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_nic, Unset):
        json_serial_nic = serial_nic

    params["serial__nic"] = json_serial_nic

    json_serial_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_nie, Unset):
        json_serial_nie = serial_nie

    params["serial__nie"] = json_serial_nie

    json_serial_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_niew, Unset):
        json_serial_niew = serial_niew

    params["serial__niew"] = json_serial_niew

    json_serial_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_nisw, Unset):
        json_serial_nisw = serial_nisw

    params["serial__nisw"] = json_serial_nisw

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

    json_site_id: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(site_id, Unset):
        json_site_id = []
        for site_id_item_data in site_id:
            site_id_item: Union[None, int]
            site_id_item = site_id_item_data
            json_site_id.append(site_id_item)

    params["site_id"] = json_site_id

    json_site_id_n: Union[Unset, list[Union[None, int]]] = UNSET
    if not isinstance(site_id_n, Unset):
        json_site_id_n = []
        for site_id_n_item_data in site_id_n:
            site_id_n_item: Union[None, int]
            site_id_n_item = site_id_n_item_data
            json_site_id_n.append(site_id_n_item)

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

    json_updated_by_request: Union[Unset, str] = UNSET
    if not isinstance(updated_by_request, Unset):
        json_updated_by_request = str(updated_by_request)
    params["updated_by_request"] = json_updated_by_request

    json_vcpus: Union[Unset, list[float]] = UNSET
    if not isinstance(vcpus, Unset):
        json_vcpus = vcpus

    params["vcpus"] = json_vcpus

    params["vcpus__empty"] = vcpus_empty

    json_vcpus_gt: Union[Unset, list[float]] = UNSET
    if not isinstance(vcpus_gt, Unset):
        json_vcpus_gt = vcpus_gt

    params["vcpus__gt"] = json_vcpus_gt

    json_vcpus_gte: Union[Unset, list[float]] = UNSET
    if not isinstance(vcpus_gte, Unset):
        json_vcpus_gte = vcpus_gte

    params["vcpus__gte"] = json_vcpus_gte

    json_vcpus_lt: Union[Unset, list[float]] = UNSET
    if not isinstance(vcpus_lt, Unset):
        json_vcpus_lt = vcpus_lt

    params["vcpus__lt"] = json_vcpus_lt

    json_vcpus_lte: Union[Unset, list[float]] = UNSET
    if not isinstance(vcpus_lte, Unset):
        json_vcpus_lte = vcpus_lte

    params["vcpus__lte"] = json_vcpus_lte

    json_vcpus_n: Union[Unset, list[float]] = UNSET
    if not isinstance(vcpus_n, Unset):
        json_vcpus_n = vcpus_n

    params["vcpus__n"] = json_vcpus_n

    json_virtual_disk_count: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_disk_count, Unset):
        json_virtual_disk_count = virtual_disk_count

    params["virtual_disk_count"] = json_virtual_disk_count

    params["virtual_disk_count__empty"] = virtual_disk_count_empty

    json_virtual_disk_count_gt: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_disk_count_gt, Unset):
        json_virtual_disk_count_gt = virtual_disk_count_gt

    params["virtual_disk_count__gt"] = json_virtual_disk_count_gt

    json_virtual_disk_count_gte: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_disk_count_gte, Unset):
        json_virtual_disk_count_gte = virtual_disk_count_gte

    params["virtual_disk_count__gte"] = json_virtual_disk_count_gte

    json_virtual_disk_count_lt: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_disk_count_lt, Unset):
        json_virtual_disk_count_lt = virtual_disk_count_lt

    params["virtual_disk_count__lt"] = json_virtual_disk_count_lt

    json_virtual_disk_count_lte: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_disk_count_lte, Unset):
        json_virtual_disk_count_lte = virtual_disk_count_lte

    params["virtual_disk_count__lte"] = json_virtual_disk_count_lte

    json_virtual_disk_count_n: Union[Unset, list[int]] = UNSET
    if not isinstance(virtual_disk_count_n, Unset):
        json_virtual_disk_count_n = virtual_disk_count_n

    params["virtual_disk_count__n"] = json_virtual_disk_count_n

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/virtualization/virtual-machines/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedVirtualMachineWithConfigContextList]:
    if response.status_code == 200:
        response_200 = PaginatedVirtualMachineWithConfigContextList.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedVirtualMachineWithConfigContextList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cluster: Union[Unset, list[str]] = UNSET,
    cluster_n: Union[Unset, list[str]] = UNSET,
    cluster_group: Union[Unset, list[str]] = UNSET,
    cluster_group_n: Union[Unset, list[str]] = UNSET,
    cluster_group_id: Union[Unset, list[int]] = UNSET,
    cluster_group_id_n: Union[Unset, list[int]] = UNSET,
    cluster_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cluster_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cluster_type: Union[Unset, list[str]] = UNSET,
    cluster_type_n: Union[Unset, list[str]] = UNSET,
    cluster_type_id: Union[Unset, list[int]] = UNSET,
    cluster_type_id_n: Union[Unset, list[int]] = UNSET,
    config_template_id: Union[Unset, list[Union[None, int]]] = UNSET,
    config_template_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[Union[None, int]]] = UNSET,
    device_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    disk: Union[Unset, list[int]] = UNSET,
    disk_empty: Union[Unset, bool] = UNSET,
    disk_gt: Union[Unset, list[int]] = UNSET,
    disk_gte: Union[Unset, list[int]] = UNSET,
    disk_lt: Union[Unset, list[int]] = UNSET,
    disk_lte: Union[Unset, list[int]] = UNSET,
    disk_n: Union[Unset, list[int]] = UNSET,
    has_primary_ip: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_count: Union[Unset, list[int]] = UNSET,
    interface_count_empty: Union[Unset, bool] = UNSET,
    interface_count_gt: Union[Unset, list[int]] = UNSET,
    interface_count_gte: Union[Unset, list[int]] = UNSET,
    interface_count_lt: Union[Unset, list[int]] = UNSET,
    interface_count_lte: Union[Unset, list[int]] = UNSET,
    interface_count_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    local_context_data: Union[Unset, bool] = UNSET,
    mac_address: Union[Unset, list[str]] = UNSET,
    mac_address_ic: Union[Unset, list[str]] = UNSET,
    mac_address_ie: Union[Unset, list[str]] = UNSET,
    mac_address_iew: Union[Unset, list[str]] = UNSET,
    mac_address_isw: Union[Unset, list[str]] = UNSET,
    mac_address_n: Union[Unset, list[str]] = UNSET,
    mac_address_nic: Union[Unset, list[str]] = UNSET,
    mac_address_nie: Union[Unset, list[str]] = UNSET,
    mac_address_niew: Union[Unset, list[str]] = UNSET,
    mac_address_nisw: Union[Unset, list[str]] = UNSET,
    memory: Union[Unset, list[int]] = UNSET,
    memory_empty: Union[Unset, bool] = UNSET,
    memory_gt: Union[Unset, list[int]] = UNSET,
    memory_gte: Union[Unset, list[int]] = UNSET,
    memory_lt: Union[Unset, list[int]] = UNSET,
    memory_lte: Union[Unset, list[int]] = UNSET,
    memory_n: Union[Unset, list[int]] = UNSET,
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
    platform: Union[Unset, list[str]] = UNSET,
    platform_n: Union[Unset, list[str]] = UNSET,
    platform_id: Union[Unset, list[Union[None, int]]] = UNSET,
    platform_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    primary_ip4: Union[Unset, list[str]] = UNSET,
    primary_ip4_n: Union[Unset, list[str]] = UNSET,
    primary_ip4_id: Union[Unset, list[int]] = UNSET,
    primary_ip4_id_n: Union[Unset, list[int]] = UNSET,
    primary_ip6: Union[Unset, list[str]] = UNSET,
    primary_ip6_n: Union[Unset, list[str]] = UNSET,
    primary_ip6_id: Union[Unset, list[int]] = UNSET,
    primary_ip6_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[str]] = UNSET,
    role_id_n: Union[Unset, list[str]] = UNSET,
    serial: Union[Unset, list[str]] = UNSET,
    serial_empty: Union[Unset, bool] = UNSET,
    serial_ic: Union[Unset, list[str]] = UNSET,
    serial_ie: Union[Unset, list[str]] = UNSET,
    serial_iew: Union[Unset, list[str]] = UNSET,
    serial_isw: Union[Unset, list[str]] = UNSET,
    serial_n: Union[Unset, list[str]] = UNSET,
    serial_nic: Union[Unset, list[str]] = UNSET,
    serial_nie: Union[Unset, list[str]] = UNSET,
    serial_niew: Union[Unset, list[str]] = UNSET,
    serial_nisw: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[Union[None, int]]] = UNSET,
    site_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    vcpus: Union[Unset, list[float]] = UNSET,
    vcpus_empty: Union[Unset, bool] = UNSET,
    vcpus_gt: Union[Unset, list[float]] = UNSET,
    vcpus_gte: Union[Unset, list[float]] = UNSET,
    vcpus_lt: Union[Unset, list[float]] = UNSET,
    vcpus_lte: Union[Unset, list[float]] = UNSET,
    vcpus_n: Union[Unset, list[float]] = UNSET,
    virtual_disk_count: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_empty: Union[Unset, bool] = UNSET,
    virtual_disk_count_gt: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_gte: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_lt: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_lte: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedVirtualMachineWithConfigContextList]:
    """Get a list of virtual machine objects.

    Args:
        cluster (Union[Unset, list[str]]):
        cluster_n (Union[Unset, list[str]]):
        cluster_group (Union[Unset, list[str]]):
        cluster_group_n (Union[Unset, list[str]]):
        cluster_group_id (Union[Unset, list[int]]):
        cluster_group_id_n (Union[Unset, list[int]]):
        cluster_id (Union[Unset, list[Union[None, int]]]):
        cluster_id_n (Union[Unset, list[Union[None, int]]]):
        cluster_type (Union[Unset, list[str]]):
        cluster_type_n (Union[Unset, list[str]]):
        cluster_type_id (Union[Unset, list[int]]):
        cluster_type_id_n (Union[Unset, list[int]]):
        config_template_id (Union[Unset, list[Union[None, int]]]):
        config_template_id_n (Union[Unset, list[Union[None, int]]]):
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
        device (Union[Unset, list[Union[None, str]]]):
        device_n (Union[Unset, list[Union[None, str]]]):
        device_id (Union[Unset, list[Union[None, int]]]):
        device_id_n (Union[Unset, list[Union[None, int]]]):
        disk (Union[Unset, list[int]]):
        disk_empty (Union[Unset, bool]):
        disk_gt (Union[Unset, list[int]]):
        disk_gte (Union[Unset, list[int]]):
        disk_lt (Union[Unset, list[int]]):
        disk_lte (Union[Unset, list[int]]):
        disk_n (Union[Unset, list[int]]):
        has_primary_ip (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_count (Union[Unset, list[int]]):
        interface_count_empty (Union[Unset, bool]):
        interface_count_gt (Union[Unset, list[int]]):
        interface_count_gte (Union[Unset, list[int]]):
        interface_count_lt (Union[Unset, list[int]]):
        interface_count_lte (Union[Unset, list[int]]):
        interface_count_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        local_context_data (Union[Unset, bool]):
        mac_address (Union[Unset, list[str]]):
        mac_address_ic (Union[Unset, list[str]]):
        mac_address_ie (Union[Unset, list[str]]):
        mac_address_iew (Union[Unset, list[str]]):
        mac_address_isw (Union[Unset, list[str]]):
        mac_address_n (Union[Unset, list[str]]):
        mac_address_nic (Union[Unset, list[str]]):
        mac_address_nie (Union[Unset, list[str]]):
        mac_address_niew (Union[Unset, list[str]]):
        mac_address_nisw (Union[Unset, list[str]]):
        memory (Union[Unset, list[int]]):
        memory_empty (Union[Unset, bool]):
        memory_gt (Union[Unset, list[int]]):
        memory_gte (Union[Unset, list[int]]):
        memory_lt (Union[Unset, list[int]]):
        memory_lte (Union[Unset, list[int]]):
        memory_n (Union[Unset, list[int]]):
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
        platform (Union[Unset, list[str]]):
        platform_n (Union[Unset, list[str]]):
        platform_id (Union[Unset, list[Union[None, int]]]):
        platform_id_n (Union[Unset, list[Union[None, int]]]):
        primary_ip4 (Union[Unset, list[str]]):
        primary_ip4_n (Union[Unset, list[str]]):
        primary_ip4_id (Union[Unset, list[int]]):
        primary_ip4_id_n (Union[Unset, list[int]]):
        primary_ip6 (Union[Unset, list[str]]):
        primary_ip6_n (Union[Unset, list[str]]):
        primary_ip6_id (Union[Unset, list[int]]):
        primary_ip6_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[str]]):
        role_id_n (Union[Unset, list[str]]):
        serial (Union[Unset, list[str]]):
        serial_empty (Union[Unset, bool]):
        serial_ic (Union[Unset, list[str]]):
        serial_ie (Union[Unset, list[str]]):
        serial_iew (Union[Unset, list[str]]):
        serial_isw (Union[Unset, list[str]]):
        serial_n (Union[Unset, list[str]]):
        serial_nic (Union[Unset, list[str]]):
        serial_nie (Union[Unset, list[str]]):
        serial_niew (Union[Unset, list[str]]):
        serial_nisw (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[Union[None, int]]]):
        site_id_n (Union[Unset, list[Union[None, int]]]):
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
        vcpus (Union[Unset, list[float]]):
        vcpus_empty (Union[Unset, bool]):
        vcpus_gt (Union[Unset, list[float]]):
        vcpus_gte (Union[Unset, list[float]]):
        vcpus_lt (Union[Unset, list[float]]):
        vcpus_lte (Union[Unset, list[float]]):
        vcpus_n (Union[Unset, list[float]]):
        virtual_disk_count (Union[Unset, list[int]]):
        virtual_disk_count_empty (Union[Unset, bool]):
        virtual_disk_count_gt (Union[Unset, list[int]]):
        virtual_disk_count_gte (Union[Unset, list[int]]):
        virtual_disk_count_lt (Union[Unset, list[int]]):
        virtual_disk_count_lte (Union[Unset, list[int]]):
        virtual_disk_count_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedVirtualMachineWithConfigContextList]
    """

    kwargs = _get_kwargs(
        cluster=cluster,
        cluster_n=cluster_n,
        cluster_group=cluster_group,
        cluster_group_n=cluster_group_n,
        cluster_group_id=cluster_group_id,
        cluster_group_id_n=cluster_group_id_n,
        cluster_id=cluster_id,
        cluster_id_n=cluster_id_n,
        cluster_type=cluster_type,
        cluster_type_n=cluster_type_n,
        cluster_type_id=cluster_type_id,
        cluster_type_id_n=cluster_type_id_n,
        config_template_id=config_template_id,
        config_template_id_n=config_template_id_n,
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
        device=device,
        device_n=device_n,
        device_id=device_id,
        device_id_n=device_id_n,
        disk=disk,
        disk_empty=disk_empty,
        disk_gt=disk_gt,
        disk_gte=disk_gte,
        disk_lt=disk_lt,
        disk_lte=disk_lte,
        disk_n=disk_n,
        has_primary_ip=has_primary_ip,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface_count=interface_count,
        interface_count_empty=interface_count_empty,
        interface_count_gt=interface_count_gt,
        interface_count_gte=interface_count_gte,
        interface_count_lt=interface_count_lt,
        interface_count_lte=interface_count_lte,
        interface_count_n=interface_count_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        local_context_data=local_context_data,
        mac_address=mac_address,
        mac_address_ic=mac_address_ic,
        mac_address_ie=mac_address_ie,
        mac_address_iew=mac_address_iew,
        mac_address_isw=mac_address_isw,
        mac_address_n=mac_address_n,
        mac_address_nic=mac_address_nic,
        mac_address_nie=mac_address_nie,
        mac_address_niew=mac_address_niew,
        mac_address_nisw=mac_address_nisw,
        memory=memory,
        memory_empty=memory_empty,
        memory_gt=memory_gt,
        memory_gte=memory_gte,
        memory_lt=memory_lt,
        memory_lte=memory_lte,
        memory_n=memory_n,
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
        platform=platform,
        platform_n=platform_n,
        platform_id=platform_id,
        platform_id_n=platform_id_n,
        primary_ip4=primary_ip4,
        primary_ip4_n=primary_ip4_n,
        primary_ip4_id=primary_ip4_id,
        primary_ip4_id_n=primary_ip4_id_n,
        primary_ip6=primary_ip6,
        primary_ip6_n=primary_ip6_n,
        primary_ip6_id=primary_ip6_id,
        primary_ip6_id_n=primary_ip6_id_n,
        q=q,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
        serial=serial,
        serial_empty=serial_empty,
        serial_ic=serial_ic,
        serial_ie=serial_ie,
        serial_iew=serial_iew,
        serial_isw=serial_isw,
        serial_n=serial_n,
        serial_nic=serial_nic,
        serial_nie=serial_nie,
        serial_niew=serial_niew,
        serial_nisw=serial_nisw,
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
        updated_by_request=updated_by_request,
        vcpus=vcpus,
        vcpus_empty=vcpus_empty,
        vcpus_gt=vcpus_gt,
        vcpus_gte=vcpus_gte,
        vcpus_lt=vcpus_lt,
        vcpus_lte=vcpus_lte,
        vcpus_n=vcpus_n,
        virtual_disk_count=virtual_disk_count,
        virtual_disk_count_empty=virtual_disk_count_empty,
        virtual_disk_count_gt=virtual_disk_count_gt,
        virtual_disk_count_gte=virtual_disk_count_gte,
        virtual_disk_count_lt=virtual_disk_count_lt,
        virtual_disk_count_lte=virtual_disk_count_lte,
        virtual_disk_count_n=virtual_disk_count_n,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cluster: Union[Unset, list[str]] = UNSET,
    cluster_n: Union[Unset, list[str]] = UNSET,
    cluster_group: Union[Unset, list[str]] = UNSET,
    cluster_group_n: Union[Unset, list[str]] = UNSET,
    cluster_group_id: Union[Unset, list[int]] = UNSET,
    cluster_group_id_n: Union[Unset, list[int]] = UNSET,
    cluster_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cluster_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cluster_type: Union[Unset, list[str]] = UNSET,
    cluster_type_n: Union[Unset, list[str]] = UNSET,
    cluster_type_id: Union[Unset, list[int]] = UNSET,
    cluster_type_id_n: Union[Unset, list[int]] = UNSET,
    config_template_id: Union[Unset, list[Union[None, int]]] = UNSET,
    config_template_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[Union[None, int]]] = UNSET,
    device_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    disk: Union[Unset, list[int]] = UNSET,
    disk_empty: Union[Unset, bool] = UNSET,
    disk_gt: Union[Unset, list[int]] = UNSET,
    disk_gte: Union[Unset, list[int]] = UNSET,
    disk_lt: Union[Unset, list[int]] = UNSET,
    disk_lte: Union[Unset, list[int]] = UNSET,
    disk_n: Union[Unset, list[int]] = UNSET,
    has_primary_ip: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_count: Union[Unset, list[int]] = UNSET,
    interface_count_empty: Union[Unset, bool] = UNSET,
    interface_count_gt: Union[Unset, list[int]] = UNSET,
    interface_count_gte: Union[Unset, list[int]] = UNSET,
    interface_count_lt: Union[Unset, list[int]] = UNSET,
    interface_count_lte: Union[Unset, list[int]] = UNSET,
    interface_count_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    local_context_data: Union[Unset, bool] = UNSET,
    mac_address: Union[Unset, list[str]] = UNSET,
    mac_address_ic: Union[Unset, list[str]] = UNSET,
    mac_address_ie: Union[Unset, list[str]] = UNSET,
    mac_address_iew: Union[Unset, list[str]] = UNSET,
    mac_address_isw: Union[Unset, list[str]] = UNSET,
    mac_address_n: Union[Unset, list[str]] = UNSET,
    mac_address_nic: Union[Unset, list[str]] = UNSET,
    mac_address_nie: Union[Unset, list[str]] = UNSET,
    mac_address_niew: Union[Unset, list[str]] = UNSET,
    mac_address_nisw: Union[Unset, list[str]] = UNSET,
    memory: Union[Unset, list[int]] = UNSET,
    memory_empty: Union[Unset, bool] = UNSET,
    memory_gt: Union[Unset, list[int]] = UNSET,
    memory_gte: Union[Unset, list[int]] = UNSET,
    memory_lt: Union[Unset, list[int]] = UNSET,
    memory_lte: Union[Unset, list[int]] = UNSET,
    memory_n: Union[Unset, list[int]] = UNSET,
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
    platform: Union[Unset, list[str]] = UNSET,
    platform_n: Union[Unset, list[str]] = UNSET,
    platform_id: Union[Unset, list[Union[None, int]]] = UNSET,
    platform_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    primary_ip4: Union[Unset, list[str]] = UNSET,
    primary_ip4_n: Union[Unset, list[str]] = UNSET,
    primary_ip4_id: Union[Unset, list[int]] = UNSET,
    primary_ip4_id_n: Union[Unset, list[int]] = UNSET,
    primary_ip6: Union[Unset, list[str]] = UNSET,
    primary_ip6_n: Union[Unset, list[str]] = UNSET,
    primary_ip6_id: Union[Unset, list[int]] = UNSET,
    primary_ip6_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[str]] = UNSET,
    role_id_n: Union[Unset, list[str]] = UNSET,
    serial: Union[Unset, list[str]] = UNSET,
    serial_empty: Union[Unset, bool] = UNSET,
    serial_ic: Union[Unset, list[str]] = UNSET,
    serial_ie: Union[Unset, list[str]] = UNSET,
    serial_iew: Union[Unset, list[str]] = UNSET,
    serial_isw: Union[Unset, list[str]] = UNSET,
    serial_n: Union[Unset, list[str]] = UNSET,
    serial_nic: Union[Unset, list[str]] = UNSET,
    serial_nie: Union[Unset, list[str]] = UNSET,
    serial_niew: Union[Unset, list[str]] = UNSET,
    serial_nisw: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[Union[None, int]]] = UNSET,
    site_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    vcpus: Union[Unset, list[float]] = UNSET,
    vcpus_empty: Union[Unset, bool] = UNSET,
    vcpus_gt: Union[Unset, list[float]] = UNSET,
    vcpus_gte: Union[Unset, list[float]] = UNSET,
    vcpus_lt: Union[Unset, list[float]] = UNSET,
    vcpus_lte: Union[Unset, list[float]] = UNSET,
    vcpus_n: Union[Unset, list[float]] = UNSET,
    virtual_disk_count: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_empty: Union[Unset, bool] = UNSET,
    virtual_disk_count_gt: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_gte: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_lt: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_lte: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedVirtualMachineWithConfigContextList]:
    """Get a list of virtual machine objects.

    Args:
        cluster (Union[Unset, list[str]]):
        cluster_n (Union[Unset, list[str]]):
        cluster_group (Union[Unset, list[str]]):
        cluster_group_n (Union[Unset, list[str]]):
        cluster_group_id (Union[Unset, list[int]]):
        cluster_group_id_n (Union[Unset, list[int]]):
        cluster_id (Union[Unset, list[Union[None, int]]]):
        cluster_id_n (Union[Unset, list[Union[None, int]]]):
        cluster_type (Union[Unset, list[str]]):
        cluster_type_n (Union[Unset, list[str]]):
        cluster_type_id (Union[Unset, list[int]]):
        cluster_type_id_n (Union[Unset, list[int]]):
        config_template_id (Union[Unset, list[Union[None, int]]]):
        config_template_id_n (Union[Unset, list[Union[None, int]]]):
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
        device (Union[Unset, list[Union[None, str]]]):
        device_n (Union[Unset, list[Union[None, str]]]):
        device_id (Union[Unset, list[Union[None, int]]]):
        device_id_n (Union[Unset, list[Union[None, int]]]):
        disk (Union[Unset, list[int]]):
        disk_empty (Union[Unset, bool]):
        disk_gt (Union[Unset, list[int]]):
        disk_gte (Union[Unset, list[int]]):
        disk_lt (Union[Unset, list[int]]):
        disk_lte (Union[Unset, list[int]]):
        disk_n (Union[Unset, list[int]]):
        has_primary_ip (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_count (Union[Unset, list[int]]):
        interface_count_empty (Union[Unset, bool]):
        interface_count_gt (Union[Unset, list[int]]):
        interface_count_gte (Union[Unset, list[int]]):
        interface_count_lt (Union[Unset, list[int]]):
        interface_count_lte (Union[Unset, list[int]]):
        interface_count_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        local_context_data (Union[Unset, bool]):
        mac_address (Union[Unset, list[str]]):
        mac_address_ic (Union[Unset, list[str]]):
        mac_address_ie (Union[Unset, list[str]]):
        mac_address_iew (Union[Unset, list[str]]):
        mac_address_isw (Union[Unset, list[str]]):
        mac_address_n (Union[Unset, list[str]]):
        mac_address_nic (Union[Unset, list[str]]):
        mac_address_nie (Union[Unset, list[str]]):
        mac_address_niew (Union[Unset, list[str]]):
        mac_address_nisw (Union[Unset, list[str]]):
        memory (Union[Unset, list[int]]):
        memory_empty (Union[Unset, bool]):
        memory_gt (Union[Unset, list[int]]):
        memory_gte (Union[Unset, list[int]]):
        memory_lt (Union[Unset, list[int]]):
        memory_lte (Union[Unset, list[int]]):
        memory_n (Union[Unset, list[int]]):
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
        platform (Union[Unset, list[str]]):
        platform_n (Union[Unset, list[str]]):
        platform_id (Union[Unset, list[Union[None, int]]]):
        platform_id_n (Union[Unset, list[Union[None, int]]]):
        primary_ip4 (Union[Unset, list[str]]):
        primary_ip4_n (Union[Unset, list[str]]):
        primary_ip4_id (Union[Unset, list[int]]):
        primary_ip4_id_n (Union[Unset, list[int]]):
        primary_ip6 (Union[Unset, list[str]]):
        primary_ip6_n (Union[Unset, list[str]]):
        primary_ip6_id (Union[Unset, list[int]]):
        primary_ip6_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[str]]):
        role_id_n (Union[Unset, list[str]]):
        serial (Union[Unset, list[str]]):
        serial_empty (Union[Unset, bool]):
        serial_ic (Union[Unset, list[str]]):
        serial_ie (Union[Unset, list[str]]):
        serial_iew (Union[Unset, list[str]]):
        serial_isw (Union[Unset, list[str]]):
        serial_n (Union[Unset, list[str]]):
        serial_nic (Union[Unset, list[str]]):
        serial_nie (Union[Unset, list[str]]):
        serial_niew (Union[Unset, list[str]]):
        serial_nisw (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[Union[None, int]]]):
        site_id_n (Union[Unset, list[Union[None, int]]]):
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
        vcpus (Union[Unset, list[float]]):
        vcpus_empty (Union[Unset, bool]):
        vcpus_gt (Union[Unset, list[float]]):
        vcpus_gte (Union[Unset, list[float]]):
        vcpus_lt (Union[Unset, list[float]]):
        vcpus_lte (Union[Unset, list[float]]):
        vcpus_n (Union[Unset, list[float]]):
        virtual_disk_count (Union[Unset, list[int]]):
        virtual_disk_count_empty (Union[Unset, bool]):
        virtual_disk_count_gt (Union[Unset, list[int]]):
        virtual_disk_count_gte (Union[Unset, list[int]]):
        virtual_disk_count_lt (Union[Unset, list[int]]):
        virtual_disk_count_lte (Union[Unset, list[int]]):
        virtual_disk_count_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedVirtualMachineWithConfigContextList
    """

    return sync_detailed(
        client=client,
        cluster=cluster,
        cluster_n=cluster_n,
        cluster_group=cluster_group,
        cluster_group_n=cluster_group_n,
        cluster_group_id=cluster_group_id,
        cluster_group_id_n=cluster_group_id_n,
        cluster_id=cluster_id,
        cluster_id_n=cluster_id_n,
        cluster_type=cluster_type,
        cluster_type_n=cluster_type_n,
        cluster_type_id=cluster_type_id,
        cluster_type_id_n=cluster_type_id_n,
        config_template_id=config_template_id,
        config_template_id_n=config_template_id_n,
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
        device=device,
        device_n=device_n,
        device_id=device_id,
        device_id_n=device_id_n,
        disk=disk,
        disk_empty=disk_empty,
        disk_gt=disk_gt,
        disk_gte=disk_gte,
        disk_lt=disk_lt,
        disk_lte=disk_lte,
        disk_n=disk_n,
        has_primary_ip=has_primary_ip,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface_count=interface_count,
        interface_count_empty=interface_count_empty,
        interface_count_gt=interface_count_gt,
        interface_count_gte=interface_count_gte,
        interface_count_lt=interface_count_lt,
        interface_count_lte=interface_count_lte,
        interface_count_n=interface_count_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        local_context_data=local_context_data,
        mac_address=mac_address,
        mac_address_ic=mac_address_ic,
        mac_address_ie=mac_address_ie,
        mac_address_iew=mac_address_iew,
        mac_address_isw=mac_address_isw,
        mac_address_n=mac_address_n,
        mac_address_nic=mac_address_nic,
        mac_address_nie=mac_address_nie,
        mac_address_niew=mac_address_niew,
        mac_address_nisw=mac_address_nisw,
        memory=memory,
        memory_empty=memory_empty,
        memory_gt=memory_gt,
        memory_gte=memory_gte,
        memory_lt=memory_lt,
        memory_lte=memory_lte,
        memory_n=memory_n,
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
        platform=platform,
        platform_n=platform_n,
        platform_id=platform_id,
        platform_id_n=platform_id_n,
        primary_ip4=primary_ip4,
        primary_ip4_n=primary_ip4_n,
        primary_ip4_id=primary_ip4_id,
        primary_ip4_id_n=primary_ip4_id_n,
        primary_ip6=primary_ip6,
        primary_ip6_n=primary_ip6_n,
        primary_ip6_id=primary_ip6_id,
        primary_ip6_id_n=primary_ip6_id_n,
        q=q,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
        serial=serial,
        serial_empty=serial_empty,
        serial_ic=serial_ic,
        serial_ie=serial_ie,
        serial_iew=serial_iew,
        serial_isw=serial_isw,
        serial_n=serial_n,
        serial_nic=serial_nic,
        serial_nie=serial_nie,
        serial_niew=serial_niew,
        serial_nisw=serial_nisw,
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
        updated_by_request=updated_by_request,
        vcpus=vcpus,
        vcpus_empty=vcpus_empty,
        vcpus_gt=vcpus_gt,
        vcpus_gte=vcpus_gte,
        vcpus_lt=vcpus_lt,
        vcpus_lte=vcpus_lte,
        vcpus_n=vcpus_n,
        virtual_disk_count=virtual_disk_count,
        virtual_disk_count_empty=virtual_disk_count_empty,
        virtual_disk_count_gt=virtual_disk_count_gt,
        virtual_disk_count_gte=virtual_disk_count_gte,
        virtual_disk_count_lt=virtual_disk_count_lt,
        virtual_disk_count_lte=virtual_disk_count_lte,
        virtual_disk_count_n=virtual_disk_count_n,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cluster: Union[Unset, list[str]] = UNSET,
    cluster_n: Union[Unset, list[str]] = UNSET,
    cluster_group: Union[Unset, list[str]] = UNSET,
    cluster_group_n: Union[Unset, list[str]] = UNSET,
    cluster_group_id: Union[Unset, list[int]] = UNSET,
    cluster_group_id_n: Union[Unset, list[int]] = UNSET,
    cluster_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cluster_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cluster_type: Union[Unset, list[str]] = UNSET,
    cluster_type_n: Union[Unset, list[str]] = UNSET,
    cluster_type_id: Union[Unset, list[int]] = UNSET,
    cluster_type_id_n: Union[Unset, list[int]] = UNSET,
    config_template_id: Union[Unset, list[Union[None, int]]] = UNSET,
    config_template_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[Union[None, int]]] = UNSET,
    device_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    disk: Union[Unset, list[int]] = UNSET,
    disk_empty: Union[Unset, bool] = UNSET,
    disk_gt: Union[Unset, list[int]] = UNSET,
    disk_gte: Union[Unset, list[int]] = UNSET,
    disk_lt: Union[Unset, list[int]] = UNSET,
    disk_lte: Union[Unset, list[int]] = UNSET,
    disk_n: Union[Unset, list[int]] = UNSET,
    has_primary_ip: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_count: Union[Unset, list[int]] = UNSET,
    interface_count_empty: Union[Unset, bool] = UNSET,
    interface_count_gt: Union[Unset, list[int]] = UNSET,
    interface_count_gte: Union[Unset, list[int]] = UNSET,
    interface_count_lt: Union[Unset, list[int]] = UNSET,
    interface_count_lte: Union[Unset, list[int]] = UNSET,
    interface_count_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    local_context_data: Union[Unset, bool] = UNSET,
    mac_address: Union[Unset, list[str]] = UNSET,
    mac_address_ic: Union[Unset, list[str]] = UNSET,
    mac_address_ie: Union[Unset, list[str]] = UNSET,
    mac_address_iew: Union[Unset, list[str]] = UNSET,
    mac_address_isw: Union[Unset, list[str]] = UNSET,
    mac_address_n: Union[Unset, list[str]] = UNSET,
    mac_address_nic: Union[Unset, list[str]] = UNSET,
    mac_address_nie: Union[Unset, list[str]] = UNSET,
    mac_address_niew: Union[Unset, list[str]] = UNSET,
    mac_address_nisw: Union[Unset, list[str]] = UNSET,
    memory: Union[Unset, list[int]] = UNSET,
    memory_empty: Union[Unset, bool] = UNSET,
    memory_gt: Union[Unset, list[int]] = UNSET,
    memory_gte: Union[Unset, list[int]] = UNSET,
    memory_lt: Union[Unset, list[int]] = UNSET,
    memory_lte: Union[Unset, list[int]] = UNSET,
    memory_n: Union[Unset, list[int]] = UNSET,
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
    platform: Union[Unset, list[str]] = UNSET,
    platform_n: Union[Unset, list[str]] = UNSET,
    platform_id: Union[Unset, list[Union[None, int]]] = UNSET,
    platform_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    primary_ip4: Union[Unset, list[str]] = UNSET,
    primary_ip4_n: Union[Unset, list[str]] = UNSET,
    primary_ip4_id: Union[Unset, list[int]] = UNSET,
    primary_ip4_id_n: Union[Unset, list[int]] = UNSET,
    primary_ip6: Union[Unset, list[str]] = UNSET,
    primary_ip6_n: Union[Unset, list[str]] = UNSET,
    primary_ip6_id: Union[Unset, list[int]] = UNSET,
    primary_ip6_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[str]] = UNSET,
    role_id_n: Union[Unset, list[str]] = UNSET,
    serial: Union[Unset, list[str]] = UNSET,
    serial_empty: Union[Unset, bool] = UNSET,
    serial_ic: Union[Unset, list[str]] = UNSET,
    serial_ie: Union[Unset, list[str]] = UNSET,
    serial_iew: Union[Unset, list[str]] = UNSET,
    serial_isw: Union[Unset, list[str]] = UNSET,
    serial_n: Union[Unset, list[str]] = UNSET,
    serial_nic: Union[Unset, list[str]] = UNSET,
    serial_nie: Union[Unset, list[str]] = UNSET,
    serial_niew: Union[Unset, list[str]] = UNSET,
    serial_nisw: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[Union[None, int]]] = UNSET,
    site_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    vcpus: Union[Unset, list[float]] = UNSET,
    vcpus_empty: Union[Unset, bool] = UNSET,
    vcpus_gt: Union[Unset, list[float]] = UNSET,
    vcpus_gte: Union[Unset, list[float]] = UNSET,
    vcpus_lt: Union[Unset, list[float]] = UNSET,
    vcpus_lte: Union[Unset, list[float]] = UNSET,
    vcpus_n: Union[Unset, list[float]] = UNSET,
    virtual_disk_count: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_empty: Union[Unset, bool] = UNSET,
    virtual_disk_count_gt: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_gte: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_lt: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_lte: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_n: Union[Unset, list[int]] = UNSET,
) -> Response[PaginatedVirtualMachineWithConfigContextList]:
    """Get a list of virtual machine objects.

    Args:
        cluster (Union[Unset, list[str]]):
        cluster_n (Union[Unset, list[str]]):
        cluster_group (Union[Unset, list[str]]):
        cluster_group_n (Union[Unset, list[str]]):
        cluster_group_id (Union[Unset, list[int]]):
        cluster_group_id_n (Union[Unset, list[int]]):
        cluster_id (Union[Unset, list[Union[None, int]]]):
        cluster_id_n (Union[Unset, list[Union[None, int]]]):
        cluster_type (Union[Unset, list[str]]):
        cluster_type_n (Union[Unset, list[str]]):
        cluster_type_id (Union[Unset, list[int]]):
        cluster_type_id_n (Union[Unset, list[int]]):
        config_template_id (Union[Unset, list[Union[None, int]]]):
        config_template_id_n (Union[Unset, list[Union[None, int]]]):
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
        device (Union[Unset, list[Union[None, str]]]):
        device_n (Union[Unset, list[Union[None, str]]]):
        device_id (Union[Unset, list[Union[None, int]]]):
        device_id_n (Union[Unset, list[Union[None, int]]]):
        disk (Union[Unset, list[int]]):
        disk_empty (Union[Unset, bool]):
        disk_gt (Union[Unset, list[int]]):
        disk_gte (Union[Unset, list[int]]):
        disk_lt (Union[Unset, list[int]]):
        disk_lte (Union[Unset, list[int]]):
        disk_n (Union[Unset, list[int]]):
        has_primary_ip (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_count (Union[Unset, list[int]]):
        interface_count_empty (Union[Unset, bool]):
        interface_count_gt (Union[Unset, list[int]]):
        interface_count_gte (Union[Unset, list[int]]):
        interface_count_lt (Union[Unset, list[int]]):
        interface_count_lte (Union[Unset, list[int]]):
        interface_count_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        local_context_data (Union[Unset, bool]):
        mac_address (Union[Unset, list[str]]):
        mac_address_ic (Union[Unset, list[str]]):
        mac_address_ie (Union[Unset, list[str]]):
        mac_address_iew (Union[Unset, list[str]]):
        mac_address_isw (Union[Unset, list[str]]):
        mac_address_n (Union[Unset, list[str]]):
        mac_address_nic (Union[Unset, list[str]]):
        mac_address_nie (Union[Unset, list[str]]):
        mac_address_niew (Union[Unset, list[str]]):
        mac_address_nisw (Union[Unset, list[str]]):
        memory (Union[Unset, list[int]]):
        memory_empty (Union[Unset, bool]):
        memory_gt (Union[Unset, list[int]]):
        memory_gte (Union[Unset, list[int]]):
        memory_lt (Union[Unset, list[int]]):
        memory_lte (Union[Unset, list[int]]):
        memory_n (Union[Unset, list[int]]):
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
        platform (Union[Unset, list[str]]):
        platform_n (Union[Unset, list[str]]):
        platform_id (Union[Unset, list[Union[None, int]]]):
        platform_id_n (Union[Unset, list[Union[None, int]]]):
        primary_ip4 (Union[Unset, list[str]]):
        primary_ip4_n (Union[Unset, list[str]]):
        primary_ip4_id (Union[Unset, list[int]]):
        primary_ip4_id_n (Union[Unset, list[int]]):
        primary_ip6 (Union[Unset, list[str]]):
        primary_ip6_n (Union[Unset, list[str]]):
        primary_ip6_id (Union[Unset, list[int]]):
        primary_ip6_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[str]]):
        role_id_n (Union[Unset, list[str]]):
        serial (Union[Unset, list[str]]):
        serial_empty (Union[Unset, bool]):
        serial_ic (Union[Unset, list[str]]):
        serial_ie (Union[Unset, list[str]]):
        serial_iew (Union[Unset, list[str]]):
        serial_isw (Union[Unset, list[str]]):
        serial_n (Union[Unset, list[str]]):
        serial_nic (Union[Unset, list[str]]):
        serial_nie (Union[Unset, list[str]]):
        serial_niew (Union[Unset, list[str]]):
        serial_nisw (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[Union[None, int]]]):
        site_id_n (Union[Unset, list[Union[None, int]]]):
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
        vcpus (Union[Unset, list[float]]):
        vcpus_empty (Union[Unset, bool]):
        vcpus_gt (Union[Unset, list[float]]):
        vcpus_gte (Union[Unset, list[float]]):
        vcpus_lt (Union[Unset, list[float]]):
        vcpus_lte (Union[Unset, list[float]]):
        vcpus_n (Union[Unset, list[float]]):
        virtual_disk_count (Union[Unset, list[int]]):
        virtual_disk_count_empty (Union[Unset, bool]):
        virtual_disk_count_gt (Union[Unset, list[int]]):
        virtual_disk_count_gte (Union[Unset, list[int]]):
        virtual_disk_count_lt (Union[Unset, list[int]]):
        virtual_disk_count_lte (Union[Unset, list[int]]):
        virtual_disk_count_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedVirtualMachineWithConfigContextList]
    """

    kwargs = _get_kwargs(
        cluster=cluster,
        cluster_n=cluster_n,
        cluster_group=cluster_group,
        cluster_group_n=cluster_group_n,
        cluster_group_id=cluster_group_id,
        cluster_group_id_n=cluster_group_id_n,
        cluster_id=cluster_id,
        cluster_id_n=cluster_id_n,
        cluster_type=cluster_type,
        cluster_type_n=cluster_type_n,
        cluster_type_id=cluster_type_id,
        cluster_type_id_n=cluster_type_id_n,
        config_template_id=config_template_id,
        config_template_id_n=config_template_id_n,
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
        device=device,
        device_n=device_n,
        device_id=device_id,
        device_id_n=device_id_n,
        disk=disk,
        disk_empty=disk_empty,
        disk_gt=disk_gt,
        disk_gte=disk_gte,
        disk_lt=disk_lt,
        disk_lte=disk_lte,
        disk_n=disk_n,
        has_primary_ip=has_primary_ip,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        interface_count=interface_count,
        interface_count_empty=interface_count_empty,
        interface_count_gt=interface_count_gt,
        interface_count_gte=interface_count_gte,
        interface_count_lt=interface_count_lt,
        interface_count_lte=interface_count_lte,
        interface_count_n=interface_count_n,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        local_context_data=local_context_data,
        mac_address=mac_address,
        mac_address_ic=mac_address_ic,
        mac_address_ie=mac_address_ie,
        mac_address_iew=mac_address_iew,
        mac_address_isw=mac_address_isw,
        mac_address_n=mac_address_n,
        mac_address_nic=mac_address_nic,
        mac_address_nie=mac_address_nie,
        mac_address_niew=mac_address_niew,
        mac_address_nisw=mac_address_nisw,
        memory=memory,
        memory_empty=memory_empty,
        memory_gt=memory_gt,
        memory_gte=memory_gte,
        memory_lt=memory_lt,
        memory_lte=memory_lte,
        memory_n=memory_n,
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
        platform=platform,
        platform_n=platform_n,
        platform_id=platform_id,
        platform_id_n=platform_id_n,
        primary_ip4=primary_ip4,
        primary_ip4_n=primary_ip4_n,
        primary_ip4_id=primary_ip4_id,
        primary_ip4_id_n=primary_ip4_id_n,
        primary_ip6=primary_ip6,
        primary_ip6_n=primary_ip6_n,
        primary_ip6_id=primary_ip6_id,
        primary_ip6_id_n=primary_ip6_id_n,
        q=q,
        region=region,
        region_n=region_n,
        region_id=region_id,
        region_id_n=region_id_n,
        role=role,
        role_n=role_n,
        role_id=role_id,
        role_id_n=role_id_n,
        serial=serial,
        serial_empty=serial_empty,
        serial_ic=serial_ic,
        serial_ie=serial_ie,
        serial_iew=serial_iew,
        serial_isw=serial_isw,
        serial_n=serial_n,
        serial_nic=serial_nic,
        serial_nie=serial_nie,
        serial_niew=serial_niew,
        serial_nisw=serial_nisw,
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
        updated_by_request=updated_by_request,
        vcpus=vcpus,
        vcpus_empty=vcpus_empty,
        vcpus_gt=vcpus_gt,
        vcpus_gte=vcpus_gte,
        vcpus_lt=vcpus_lt,
        vcpus_lte=vcpus_lte,
        vcpus_n=vcpus_n,
        virtual_disk_count=virtual_disk_count,
        virtual_disk_count_empty=virtual_disk_count_empty,
        virtual_disk_count_gt=virtual_disk_count_gt,
        virtual_disk_count_gte=virtual_disk_count_gte,
        virtual_disk_count_lt=virtual_disk_count_lt,
        virtual_disk_count_lte=virtual_disk_count_lte,
        virtual_disk_count_n=virtual_disk_count_n,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cluster: Union[Unset, list[str]] = UNSET,
    cluster_n: Union[Unset, list[str]] = UNSET,
    cluster_group: Union[Unset, list[str]] = UNSET,
    cluster_group_n: Union[Unset, list[str]] = UNSET,
    cluster_group_id: Union[Unset, list[int]] = UNSET,
    cluster_group_id_n: Union[Unset, list[int]] = UNSET,
    cluster_id: Union[Unset, list[Union[None, int]]] = UNSET,
    cluster_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    cluster_type: Union[Unset, list[str]] = UNSET,
    cluster_type_n: Union[Unset, list[str]] = UNSET,
    cluster_type_id: Union[Unset, list[int]] = UNSET,
    cluster_type_id_n: Union[Unset, list[int]] = UNSET,
    config_template_id: Union[Unset, list[Union[None, int]]] = UNSET,
    config_template_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    device: Union[Unset, list[Union[None, str]]] = UNSET,
    device_n: Union[Unset, list[Union[None, str]]] = UNSET,
    device_id: Union[Unset, list[Union[None, int]]] = UNSET,
    device_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    disk: Union[Unset, list[int]] = UNSET,
    disk_empty: Union[Unset, bool] = UNSET,
    disk_gt: Union[Unset, list[int]] = UNSET,
    disk_gte: Union[Unset, list[int]] = UNSET,
    disk_lt: Union[Unset, list[int]] = UNSET,
    disk_lte: Union[Unset, list[int]] = UNSET,
    disk_n: Union[Unset, list[int]] = UNSET,
    has_primary_ip: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    interface_count: Union[Unset, list[int]] = UNSET,
    interface_count_empty: Union[Unset, bool] = UNSET,
    interface_count_gt: Union[Unset, list[int]] = UNSET,
    interface_count_gte: Union[Unset, list[int]] = UNSET,
    interface_count_lt: Union[Unset, list[int]] = UNSET,
    interface_count_lte: Union[Unset, list[int]] = UNSET,
    interface_count_n: Union[Unset, list[int]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    local_context_data: Union[Unset, bool] = UNSET,
    mac_address: Union[Unset, list[str]] = UNSET,
    mac_address_ic: Union[Unset, list[str]] = UNSET,
    mac_address_ie: Union[Unset, list[str]] = UNSET,
    mac_address_iew: Union[Unset, list[str]] = UNSET,
    mac_address_isw: Union[Unset, list[str]] = UNSET,
    mac_address_n: Union[Unset, list[str]] = UNSET,
    mac_address_nic: Union[Unset, list[str]] = UNSET,
    mac_address_nie: Union[Unset, list[str]] = UNSET,
    mac_address_niew: Union[Unset, list[str]] = UNSET,
    mac_address_nisw: Union[Unset, list[str]] = UNSET,
    memory: Union[Unset, list[int]] = UNSET,
    memory_empty: Union[Unset, bool] = UNSET,
    memory_gt: Union[Unset, list[int]] = UNSET,
    memory_gte: Union[Unset, list[int]] = UNSET,
    memory_lt: Union[Unset, list[int]] = UNSET,
    memory_lte: Union[Unset, list[int]] = UNSET,
    memory_n: Union[Unset, list[int]] = UNSET,
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
    platform: Union[Unset, list[str]] = UNSET,
    platform_n: Union[Unset, list[str]] = UNSET,
    platform_id: Union[Unset, list[Union[None, int]]] = UNSET,
    platform_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
    primary_ip4: Union[Unset, list[str]] = UNSET,
    primary_ip4_n: Union[Unset, list[str]] = UNSET,
    primary_ip4_id: Union[Unset, list[int]] = UNSET,
    primary_ip4_id_n: Union[Unset, list[int]] = UNSET,
    primary_ip6: Union[Unset, list[str]] = UNSET,
    primary_ip6_n: Union[Unset, list[str]] = UNSET,
    primary_ip6_id: Union[Unset, list[int]] = UNSET,
    primary_ip6_id_n: Union[Unset, list[int]] = UNSET,
    q: Union[Unset, str] = UNSET,
    region: Union[Unset, list[str]] = UNSET,
    region_n: Union[Unset, list[str]] = UNSET,
    region_id: Union[Unset, list[str]] = UNSET,
    region_id_n: Union[Unset, list[str]] = UNSET,
    role: Union[Unset, list[str]] = UNSET,
    role_n: Union[Unset, list[str]] = UNSET,
    role_id: Union[Unset, list[str]] = UNSET,
    role_id_n: Union[Unset, list[str]] = UNSET,
    serial: Union[Unset, list[str]] = UNSET,
    serial_empty: Union[Unset, bool] = UNSET,
    serial_ic: Union[Unset, list[str]] = UNSET,
    serial_ie: Union[Unset, list[str]] = UNSET,
    serial_iew: Union[Unset, list[str]] = UNSET,
    serial_isw: Union[Unset, list[str]] = UNSET,
    serial_n: Union[Unset, list[str]] = UNSET,
    serial_nic: Union[Unset, list[str]] = UNSET,
    serial_nie: Union[Unset, list[str]] = UNSET,
    serial_niew: Union[Unset, list[str]] = UNSET,
    serial_nisw: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_group: Union[Unset, list[str]] = UNSET,
    site_group_n: Union[Unset, list[str]] = UNSET,
    site_group_id: Union[Unset, list[str]] = UNSET,
    site_group_id_n: Union[Unset, list[str]] = UNSET,
    site_id: Union[Unset, list[Union[None, int]]] = UNSET,
    site_id_n: Union[Unset, list[Union[None, int]]] = UNSET,
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
    vcpus: Union[Unset, list[float]] = UNSET,
    vcpus_empty: Union[Unset, bool] = UNSET,
    vcpus_gt: Union[Unset, list[float]] = UNSET,
    vcpus_gte: Union[Unset, list[float]] = UNSET,
    vcpus_lt: Union[Unset, list[float]] = UNSET,
    vcpus_lte: Union[Unset, list[float]] = UNSET,
    vcpus_n: Union[Unset, list[float]] = UNSET,
    virtual_disk_count: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_empty: Union[Unset, bool] = UNSET,
    virtual_disk_count_gt: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_gte: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_lt: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_lte: Union[Unset, list[int]] = UNSET,
    virtual_disk_count_n: Union[Unset, list[int]] = UNSET,
) -> Optional[PaginatedVirtualMachineWithConfigContextList]:
    """Get a list of virtual machine objects.

    Args:
        cluster (Union[Unset, list[str]]):
        cluster_n (Union[Unset, list[str]]):
        cluster_group (Union[Unset, list[str]]):
        cluster_group_n (Union[Unset, list[str]]):
        cluster_group_id (Union[Unset, list[int]]):
        cluster_group_id_n (Union[Unset, list[int]]):
        cluster_id (Union[Unset, list[Union[None, int]]]):
        cluster_id_n (Union[Unset, list[Union[None, int]]]):
        cluster_type (Union[Unset, list[str]]):
        cluster_type_n (Union[Unset, list[str]]):
        cluster_type_id (Union[Unset, list[int]]):
        cluster_type_id_n (Union[Unset, list[int]]):
        config_template_id (Union[Unset, list[Union[None, int]]]):
        config_template_id_n (Union[Unset, list[Union[None, int]]]):
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
        device (Union[Unset, list[Union[None, str]]]):
        device_n (Union[Unset, list[Union[None, str]]]):
        device_id (Union[Unset, list[Union[None, int]]]):
        device_id_n (Union[Unset, list[Union[None, int]]]):
        disk (Union[Unset, list[int]]):
        disk_empty (Union[Unset, bool]):
        disk_gt (Union[Unset, list[int]]):
        disk_gte (Union[Unset, list[int]]):
        disk_lt (Union[Unset, list[int]]):
        disk_lte (Union[Unset, list[int]]):
        disk_n (Union[Unset, list[int]]):
        has_primary_ip (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        interface_count (Union[Unset, list[int]]):
        interface_count_empty (Union[Unset, bool]):
        interface_count_gt (Union[Unset, list[int]]):
        interface_count_gte (Union[Unset, list[int]]):
        interface_count_lt (Union[Unset, list[int]]):
        interface_count_lte (Union[Unset, list[int]]):
        interface_count_n (Union[Unset, list[int]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        local_context_data (Union[Unset, bool]):
        mac_address (Union[Unset, list[str]]):
        mac_address_ic (Union[Unset, list[str]]):
        mac_address_ie (Union[Unset, list[str]]):
        mac_address_iew (Union[Unset, list[str]]):
        mac_address_isw (Union[Unset, list[str]]):
        mac_address_n (Union[Unset, list[str]]):
        mac_address_nic (Union[Unset, list[str]]):
        mac_address_nie (Union[Unset, list[str]]):
        mac_address_niew (Union[Unset, list[str]]):
        mac_address_nisw (Union[Unset, list[str]]):
        memory (Union[Unset, list[int]]):
        memory_empty (Union[Unset, bool]):
        memory_gt (Union[Unset, list[int]]):
        memory_gte (Union[Unset, list[int]]):
        memory_lt (Union[Unset, list[int]]):
        memory_lte (Union[Unset, list[int]]):
        memory_n (Union[Unset, list[int]]):
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
        platform (Union[Unset, list[str]]):
        platform_n (Union[Unset, list[str]]):
        platform_id (Union[Unset, list[Union[None, int]]]):
        platform_id_n (Union[Unset, list[Union[None, int]]]):
        primary_ip4 (Union[Unset, list[str]]):
        primary_ip4_n (Union[Unset, list[str]]):
        primary_ip4_id (Union[Unset, list[int]]):
        primary_ip4_id_n (Union[Unset, list[int]]):
        primary_ip6 (Union[Unset, list[str]]):
        primary_ip6_n (Union[Unset, list[str]]):
        primary_ip6_id (Union[Unset, list[int]]):
        primary_ip6_id_n (Union[Unset, list[int]]):
        q (Union[Unset, str]):
        region (Union[Unset, list[str]]):
        region_n (Union[Unset, list[str]]):
        region_id (Union[Unset, list[str]]):
        region_id_n (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        role_n (Union[Unset, list[str]]):
        role_id (Union[Unset, list[str]]):
        role_id_n (Union[Unset, list[str]]):
        serial (Union[Unset, list[str]]):
        serial_empty (Union[Unset, bool]):
        serial_ic (Union[Unset, list[str]]):
        serial_ie (Union[Unset, list[str]]):
        serial_iew (Union[Unset, list[str]]):
        serial_isw (Union[Unset, list[str]]):
        serial_n (Union[Unset, list[str]]):
        serial_nic (Union[Unset, list[str]]):
        serial_nie (Union[Unset, list[str]]):
        serial_niew (Union[Unset, list[str]]):
        serial_nisw (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_group (Union[Unset, list[str]]):
        site_group_n (Union[Unset, list[str]]):
        site_group_id (Union[Unset, list[str]]):
        site_group_id_n (Union[Unset, list[str]]):
        site_id (Union[Unset, list[Union[None, int]]]):
        site_id_n (Union[Unset, list[Union[None, int]]]):
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
        vcpus (Union[Unset, list[float]]):
        vcpus_empty (Union[Unset, bool]):
        vcpus_gt (Union[Unset, list[float]]):
        vcpus_gte (Union[Unset, list[float]]):
        vcpus_lt (Union[Unset, list[float]]):
        vcpus_lte (Union[Unset, list[float]]):
        vcpus_n (Union[Unset, list[float]]):
        virtual_disk_count (Union[Unset, list[int]]):
        virtual_disk_count_empty (Union[Unset, bool]):
        virtual_disk_count_gt (Union[Unset, list[int]]):
        virtual_disk_count_gte (Union[Unset, list[int]]):
        virtual_disk_count_lt (Union[Unset, list[int]]):
        virtual_disk_count_lte (Union[Unset, list[int]]):
        virtual_disk_count_n (Union[Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedVirtualMachineWithConfigContextList
    """

    return (
        await asyncio_detailed(
            client=client,
            cluster=cluster,
            cluster_n=cluster_n,
            cluster_group=cluster_group,
            cluster_group_n=cluster_group_n,
            cluster_group_id=cluster_group_id,
            cluster_group_id_n=cluster_group_id_n,
            cluster_id=cluster_id,
            cluster_id_n=cluster_id_n,
            cluster_type=cluster_type,
            cluster_type_n=cluster_type_n,
            cluster_type_id=cluster_type_id,
            cluster_type_id_n=cluster_type_id_n,
            config_template_id=config_template_id,
            config_template_id_n=config_template_id_n,
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
            device=device,
            device_n=device_n,
            device_id=device_id,
            device_id_n=device_id_n,
            disk=disk,
            disk_empty=disk_empty,
            disk_gt=disk_gt,
            disk_gte=disk_gte,
            disk_lt=disk_lt,
            disk_lte=disk_lte,
            disk_n=disk_n,
            has_primary_ip=has_primary_ip,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            interface_count=interface_count,
            interface_count_empty=interface_count_empty,
            interface_count_gt=interface_count_gt,
            interface_count_gte=interface_count_gte,
            interface_count_lt=interface_count_lt,
            interface_count_lte=interface_count_lte,
            interface_count_n=interface_count_n,
            last_updated=last_updated,
            last_updated_empty=last_updated_empty,
            last_updated_gt=last_updated_gt,
            last_updated_gte=last_updated_gte,
            last_updated_lt=last_updated_lt,
            last_updated_lte=last_updated_lte,
            last_updated_n=last_updated_n,
            limit=limit,
            local_context_data=local_context_data,
            mac_address=mac_address,
            mac_address_ic=mac_address_ic,
            mac_address_ie=mac_address_ie,
            mac_address_iew=mac_address_iew,
            mac_address_isw=mac_address_isw,
            mac_address_n=mac_address_n,
            mac_address_nic=mac_address_nic,
            mac_address_nie=mac_address_nie,
            mac_address_niew=mac_address_niew,
            mac_address_nisw=mac_address_nisw,
            memory=memory,
            memory_empty=memory_empty,
            memory_gt=memory_gt,
            memory_gte=memory_gte,
            memory_lt=memory_lt,
            memory_lte=memory_lte,
            memory_n=memory_n,
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
            platform=platform,
            platform_n=platform_n,
            platform_id=platform_id,
            platform_id_n=platform_id_n,
            primary_ip4=primary_ip4,
            primary_ip4_n=primary_ip4_n,
            primary_ip4_id=primary_ip4_id,
            primary_ip4_id_n=primary_ip4_id_n,
            primary_ip6=primary_ip6,
            primary_ip6_n=primary_ip6_n,
            primary_ip6_id=primary_ip6_id,
            primary_ip6_id_n=primary_ip6_id_n,
            q=q,
            region=region,
            region_n=region_n,
            region_id=region_id,
            region_id_n=region_id_n,
            role=role,
            role_n=role_n,
            role_id=role_id,
            role_id_n=role_id_n,
            serial=serial,
            serial_empty=serial_empty,
            serial_ic=serial_ic,
            serial_ie=serial_ie,
            serial_iew=serial_iew,
            serial_isw=serial_isw,
            serial_n=serial_n,
            serial_nic=serial_nic,
            serial_nie=serial_nie,
            serial_niew=serial_niew,
            serial_nisw=serial_nisw,
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
            updated_by_request=updated_by_request,
            vcpus=vcpus,
            vcpus_empty=vcpus_empty,
            vcpus_gt=vcpus_gt,
            vcpus_gte=vcpus_gte,
            vcpus_lt=vcpus_lt,
            vcpus_lte=vcpus_lte,
            vcpus_n=vcpus_n,
            virtual_disk_count=virtual_disk_count,
            virtual_disk_count_empty=virtual_disk_count_empty,
            virtual_disk_count_gt=virtual_disk_count_gt,
            virtual_disk_count_gte=virtual_disk_count_gte,
            virtual_disk_count_lt=virtual_disk_count_lt,
            virtual_disk_count_lte=virtual_disk_count_lte,
            virtual_disk_count_n=virtual_disk_count_n,
        )
    ).parsed
