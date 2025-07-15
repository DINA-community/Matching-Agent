import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_device_finding_list import PaginatedDeviceFindingList
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
    confidence: Union[Unset, list[float]] = UNSET,
    confidence_empty: Union[Unset, bool] = UNSET,
    confidence_gt: Union[Unset, list[float]] = UNSET,
    confidence_gte: Union[Unset, list[float]] = UNSET,
    confidence_lt: Union[Unset, list[float]] = UNSET,
    confidence_lte: Union[Unset, list[float]] = UNSET,
    confidence_n: Union[Unset, list[float]] = UNSET,
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
    device: Union[Unset, int] = UNSET,
    device_n: Union[Unset, int] = UNSET,
    device_family: Union[Unset, list[str]] = UNSET,
    device_family_empty: Union[Unset, bool] = UNSET,
    device_family_ic: Union[Unset, list[str]] = UNSET,
    device_family_ie: Union[Unset, list[str]] = UNSET,
    device_family_iew: Union[Unset, list[str]] = UNSET,
    device_family_isw: Union[Unset, list[str]] = UNSET,
    device_family_n: Union[Unset, list[str]] = UNSET,
    device_family_nic: Union[Unset, list[str]] = UNSET,
    device_family_nie: Union[Unset, list[str]] = UNSET,
    device_family_niew: Union[Unset, list[str]] = UNSET,
    device_family_nisw: Union[Unset, list[str]] = UNSET,
    device_name: Union[Unset, list[str]] = UNSET,
    device_name_empty: Union[Unset, bool] = UNSET,
    device_name_ic: Union[Unset, list[str]] = UNSET,
    device_name_ie: Union[Unset, list[str]] = UNSET,
    device_name_iew: Union[Unset, list[str]] = UNSET,
    device_name_isw: Union[Unset, list[str]] = UNSET,
    device_name_n: Union[Unset, list[str]] = UNSET,
    device_name_nic: Union[Unset, list[str]] = UNSET,
    device_name_nie: Union[Unset, list[str]] = UNSET,
    device_name_niew: Union[Unset, list[str]] = UNSET,
    device_name_nisw: Union[Unset, list[str]] = UNSET,
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_empty: Union[Unset, bool] = UNSET,
    device_role_ic: Union[Unset, list[str]] = UNSET,
    device_role_ie: Union[Unset, list[str]] = UNSET,
    device_role_iew: Union[Unset, list[str]] = UNSET,
    device_role_isw: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_nic: Union[Unset, list[str]] = UNSET,
    device_role_nie: Union[Unset, list[str]] = UNSET,
    device_role_niew: Union[Unset, list[str]] = UNSET,
    device_role_nisw: Union[Unset, list[str]] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_empty: Union[Unset, bool] = UNSET,
    device_type_ic: Union[Unset, list[str]] = UNSET,
    device_type_ie: Union[Unset, list[str]] = UNSET,
    device_type_iew: Union[Unset, list[str]] = UNSET,
    device_type_isw: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_nic: Union[Unset, list[str]] = UNSET,
    device_type_nie: Union[Unset, list[str]] = UNSET,
    device_type_niew: Union[Unset, list[str]] = UNSET,
    device_type_nisw: Union[Unset, list[str]] = UNSET,
    exposure: Union[Unset, list[str]] = UNSET,
    exposure_empty: Union[Unset, bool] = UNSET,
    exposure_ic: Union[Unset, list[str]] = UNSET,
    exposure_ie: Union[Unset, list[str]] = UNSET,
    exposure_iew: Union[Unset, list[str]] = UNSET,
    exposure_isw: Union[Unset, list[str]] = UNSET,
    exposure_n: Union[Unset, list[str]] = UNSET,
    exposure_nic: Union[Unset, list[str]] = UNSET,
    exposure_nie: Union[Unset, list[str]] = UNSET,
    exposure_niew: Union[Unset, list[str]] = UNSET,
    exposure_nisw: Union[Unset, list[str]] = UNSET,
    hardware_cpe: Union[Unset, list[str]] = UNSET,
    hardware_cpe_empty: Union[Unset, bool] = UNSET,
    hardware_cpe_ic: Union[Unset, list[str]] = UNSET,
    hardware_cpe_ie: Union[Unset, list[str]] = UNSET,
    hardware_cpe_iew: Union[Unset, list[str]] = UNSET,
    hardware_cpe_isw: Union[Unset, list[str]] = UNSET,
    hardware_cpe_n: Union[Unset, list[str]] = UNSET,
    hardware_cpe_nic: Union[Unset, list[str]] = UNSET,
    hardware_cpe_nie: Union[Unset, list[str]] = UNSET,
    hardware_cpe_niew: Union[Unset, list[str]] = UNSET,
    hardware_cpe_nisw: Union[Unset, list[str]] = UNSET,
    hardware_version: Union[Unset, list[str]] = UNSET,
    hardware_version_empty: Union[Unset, bool] = UNSET,
    hardware_version_ic: Union[Unset, list[str]] = UNSET,
    hardware_version_ie: Union[Unset, list[str]] = UNSET,
    hardware_version_iew: Union[Unset, list[str]] = UNSET,
    hardware_version_isw: Union[Unset, list[str]] = UNSET,
    hardware_version_n: Union[Unset, list[str]] = UNSET,
    hardware_version_nic: Union[Unset, list[str]] = UNSET,
    hardware_version_nie: Union[Unset, list[str]] = UNSET,
    hardware_version_niew: Union[Unset, list[str]] = UNSET,
    hardware_version_nisw: Union[Unset, list[str]] = UNSET,
    has_predicted_device: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    ip_address: Union[Unset, list[str]] = UNSET,
    ip_address_empty: Union[Unset, bool] = UNSET,
    ip_address_ic: Union[Unset, list[str]] = UNSET,
    ip_address_ie: Union[Unset, list[str]] = UNSET,
    ip_address_iew: Union[Unset, list[str]] = UNSET,
    ip_address_isw: Union[Unset, list[str]] = UNSET,
    ip_address_n: Union[Unset, list[str]] = UNSET,
    ip_address_nic: Union[Unset, list[str]] = UNSET,
    ip_address_nie: Union[Unset, list[str]] = UNSET,
    ip_address_niew: Union[Unset, list[str]] = UNSET,
    ip_address_nisw: Union[Unset, list[str]] = UNSET,
    is_firmware: Union[Unset, list[str]] = UNSET,
    is_firmware_empty: Union[Unset, bool] = UNSET,
    is_firmware_ic: Union[Unset, list[str]] = UNSET,
    is_firmware_ie: Union[Unset, list[str]] = UNSET,
    is_firmware_iew: Union[Unset, list[str]] = UNSET,
    is_firmware_isw: Union[Unset, list[str]] = UNSET,
    is_firmware_n: Union[Unset, list[str]] = UNSET,
    is_firmware_nic: Union[Unset, list[str]] = UNSET,
    is_firmware_nie: Union[Unset, list[str]] = UNSET,
    is_firmware_niew: Union[Unset, list[str]] = UNSET,
    is_firmware_nisw: Union[Unset, list[str]] = UNSET,
    is_router: Union[Unset, list[str]] = UNSET,
    is_router_empty: Union[Unset, bool] = UNSET,
    is_router_ic: Union[Unset, list[str]] = UNSET,
    is_router_ie: Union[Unset, list[str]] = UNSET,
    is_router_iew: Union[Unset, list[str]] = UNSET,
    is_router_isw: Union[Unset, list[str]] = UNSET,
    is_router_n: Union[Unset, list[str]] = UNSET,
    is_router_nic: Union[Unset, list[str]] = UNSET,
    is_router_nie: Union[Unset, list[str]] = UNSET,
    is_router_niew: Union[Unset, list[str]] = UNSET,
    is_router_nisw: Union[Unset, list[str]] = UNSET,
    is_safety_critical: Union[Unset, list[str]] = UNSET,
    is_safety_critical_empty: Union[Unset, bool] = UNSET,
    is_safety_critical_ic: Union[Unset, list[str]] = UNSET,
    is_safety_critical_ie: Union[Unset, list[str]] = UNSET,
    is_safety_critical_iew: Union[Unset, list[str]] = UNSET,
    is_safety_critical_isw: Union[Unset, list[str]] = UNSET,
    is_safety_critical_n: Union[Unset, list[str]] = UNSET,
    is_safety_critical_nic: Union[Unset, list[str]] = UNSET,
    is_safety_critical_nie: Union[Unset, list[str]] = UNSET,
    is_safety_critical_niew: Union[Unset, list[str]] = UNSET,
    is_safety_critical_nisw: Union[Unset, list[str]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_empty: Union[Unset, bool] = UNSET,
    location_ic: Union[Unset, list[str]] = UNSET,
    location_ie: Union[Unset, list[str]] = UNSET,
    location_iew: Union[Unset, list[str]] = UNSET,
    location_isw: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_nic: Union[Unset, list[str]] = UNSET,
    location_nie: Union[Unset, list[str]] = UNSET,
    location_niew: Union[Unset, list[str]] = UNSET,
    location_nisw: Union[Unset, list[str]] = UNSET,
    mac_address: Union[Unset, list[str]] = UNSET,
    mac_address_empty: Union[Unset, bool] = UNSET,
    mac_address_ic: Union[Unset, list[str]] = UNSET,
    mac_address_ie: Union[Unset, list[str]] = UNSET,
    mac_address_iew: Union[Unset, list[str]] = UNSET,
    mac_address_isw: Union[Unset, list[str]] = UNSET,
    mac_address_n: Union[Unset, list[str]] = UNSET,
    mac_address_nic: Union[Unset, list[str]] = UNSET,
    mac_address_nie: Union[Unset, list[str]] = UNSET,
    mac_address_niew: Union[Unset, list[str]] = UNSET,
    mac_address_nisw: Union[Unset, list[str]] = UNSET,
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_empty: Union[Unset, bool] = UNSET,
    manufacturer_ic: Union[Unset, list[str]] = UNSET,
    manufacturer_ie: Union[Unset, list[str]] = UNSET,
    manufacturer_iew: Union[Unset, list[str]] = UNSET,
    manufacturer_isw: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_nic: Union[Unset, list[str]] = UNSET,
    manufacturer_nie: Union[Unset, list[str]] = UNSET,
    manufacturer_niew: Union[Unset, list[str]] = UNSET,
    manufacturer_nisw: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    oui: Union[Unset, list[str]] = UNSET,
    oui_empty: Union[Unset, bool] = UNSET,
    oui_ic: Union[Unset, list[str]] = UNSET,
    oui_ie: Union[Unset, list[str]] = UNSET,
    oui_iew: Union[Unset, list[str]] = UNSET,
    oui_isw: Union[Unset, list[str]] = UNSET,
    oui_n: Union[Unset, list[str]] = UNSET,
    oui_nic: Union[Unset, list[str]] = UNSET,
    oui_nie: Union[Unset, list[str]] = UNSET,
    oui_niew: Union[Unset, list[str]] = UNSET,
    oui_nisw: Union[Unset, list[str]] = UNSET,
    part_number: Union[Unset, list[str]] = UNSET,
    part_number_empty: Union[Unset, bool] = UNSET,
    part_number_ic: Union[Unset, list[str]] = UNSET,
    part_number_ie: Union[Unset, list[str]] = UNSET,
    part_number_iew: Union[Unset, list[str]] = UNSET,
    part_number_isw: Union[Unset, list[str]] = UNSET,
    part_number_n: Union[Unset, list[str]] = UNSET,
    part_number_nic: Union[Unset, list[str]] = UNSET,
    part_number_nie: Union[Unset, list[str]] = UNSET,
    part_number_niew: Union[Unset, list[str]] = UNSET,
    part_number_nisw: Union[Unset, list[str]] = UNSET,
    port: Union[Unset, list[str]] = UNSET,
    port_empty: Union[Unset, bool] = UNSET,
    port_ic: Union[Unset, list[str]] = UNSET,
    port_ie: Union[Unset, list[str]] = UNSET,
    port_iew: Union[Unset, list[str]] = UNSET,
    port_isw: Union[Unset, list[str]] = UNSET,
    port_n: Union[Unset, list[str]] = UNSET,
    port_nic: Union[Unset, list[str]] = UNSET,
    port_nie: Union[Unset, list[str]] = UNSET,
    port_niew: Union[Unset, list[str]] = UNSET,
    port_nisw: Union[Unset, list[str]] = UNSET,
    predicted_device: Union[Unset, int] = UNSET,
    predicted_device_n: Union[Unset, int] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_empty: Union[Unset, bool] = UNSET,
    rack_ic: Union[Unset, list[str]] = UNSET,
    rack_ie: Union[Unset, list[str]] = UNSET,
    rack_iew: Union[Unset, list[str]] = UNSET,
    rack_isw: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
    rack_nic: Union[Unset, list[str]] = UNSET,
    rack_nie: Union[Unset, list[str]] = UNSET,
    rack_niew: Union[Unset, list[str]] = UNSET,
    rack_nisw: Union[Unset, list[str]] = UNSET,
    serial_number: Union[Unset, list[str]] = UNSET,
    serial_number_empty: Union[Unset, bool] = UNSET,
    serial_number_ic: Union[Unset, list[str]] = UNSET,
    serial_number_ie: Union[Unset, list[str]] = UNSET,
    serial_number_iew: Union[Unset, list[str]] = UNSET,
    serial_number_isw: Union[Unset, list[str]] = UNSET,
    serial_number_n: Union[Unset, list[str]] = UNSET,
    serial_number_nic: Union[Unset, list[str]] = UNSET,
    serial_number_nie: Union[Unset, list[str]] = UNSET,
    serial_number_niew: Union[Unset, list[str]] = UNSET,
    serial_number_nisw: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_empty: Union[Unset, bool] = UNSET,
    site_ic: Union[Unset, list[str]] = UNSET,
    site_ie: Union[Unset, list[str]] = UNSET,
    site_iew: Union[Unset, list[str]] = UNSET,
    site_isw: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_nic: Union[Unset, list[str]] = UNSET,
    site_nie: Union[Unset, list[str]] = UNSET,
    site_niew: Union[Unset, list[str]] = UNSET,
    site_nisw: Union[Unset, list[str]] = UNSET,
    software_name: Union[Unset, list[str]] = UNSET,
    software_name_empty: Union[Unset, bool] = UNSET,
    software_name_ic: Union[Unset, list[str]] = UNSET,
    software_name_ie: Union[Unset, list[str]] = UNSET,
    software_name_iew: Union[Unset, list[str]] = UNSET,
    software_name_isw: Union[Unset, list[str]] = UNSET,
    software_name_n: Union[Unset, list[str]] = UNSET,
    software_name_nic: Union[Unset, list[str]] = UNSET,
    software_name_nie: Union[Unset, list[str]] = UNSET,
    software_name_niew: Union[Unset, list[str]] = UNSET,
    software_name_nisw: Union[Unset, list[str]] = UNSET,
    source: Union[Unset, list[str]] = UNSET,
    source_empty: Union[Unset, bool] = UNSET,
    source_ic: Union[Unset, list[str]] = UNSET,
    source_ie: Union[Unset, list[str]] = UNSET,
    source_iew: Union[Unset, list[str]] = UNSET,
    source_isw: Union[Unset, list[str]] = UNSET,
    source_n: Union[Unset, list[str]] = UNSET,
    source_nic: Union[Unset, list[str]] = UNSET,
    source_nie: Union[Unset, list[str]] = UNSET,
    source_niew: Union[Unset, list[str]] = UNSET,
    source_nisw: Union[Unset, list[str]] = UNSET,
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

    json_confidence: Union[Unset, list[float]] = UNSET
    if not isinstance(confidence, Unset):
        json_confidence = confidence

    params["confidence"] = json_confidence

    params["confidence__empty"] = confidence_empty

    json_confidence_gt: Union[Unset, list[float]] = UNSET
    if not isinstance(confidence_gt, Unset):
        json_confidence_gt = confidence_gt

    params["confidence__gt"] = json_confidence_gt

    json_confidence_gte: Union[Unset, list[float]] = UNSET
    if not isinstance(confidence_gte, Unset):
        json_confidence_gte = confidence_gte

    params["confidence__gte"] = json_confidence_gte

    json_confidence_lt: Union[Unset, list[float]] = UNSET
    if not isinstance(confidence_lt, Unset):
        json_confidence_lt = confidence_lt

    params["confidence__lt"] = json_confidence_lt

    json_confidence_lte: Union[Unset, list[float]] = UNSET
    if not isinstance(confidence_lte, Unset):
        json_confidence_lte = confidence_lte

    params["confidence__lte"] = json_confidence_lte

    json_confidence_n: Union[Unset, list[float]] = UNSET
    if not isinstance(confidence_n, Unset):
        json_confidence_n = confidence_n

    params["confidence__n"] = json_confidence_n

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

    params["device"] = device

    params["device__n"] = device_n

    json_device_family: Union[Unset, list[str]] = UNSET
    if not isinstance(device_family, Unset):
        json_device_family = device_family

    params["device_family"] = json_device_family

    params["device_family__empty"] = device_family_empty

    json_device_family_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(device_family_ic, Unset):
        json_device_family_ic = device_family_ic

    params["device_family__ic"] = json_device_family_ic

    json_device_family_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(device_family_ie, Unset):
        json_device_family_ie = device_family_ie

    params["device_family__ie"] = json_device_family_ie

    json_device_family_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(device_family_iew, Unset):
        json_device_family_iew = device_family_iew

    params["device_family__iew"] = json_device_family_iew

    json_device_family_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(device_family_isw, Unset):
        json_device_family_isw = device_family_isw

    params["device_family__isw"] = json_device_family_isw

    json_device_family_n: Union[Unset, list[str]] = UNSET
    if not isinstance(device_family_n, Unset):
        json_device_family_n = device_family_n

    params["device_family__n"] = json_device_family_n

    json_device_family_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(device_family_nic, Unset):
        json_device_family_nic = device_family_nic

    params["device_family__nic"] = json_device_family_nic

    json_device_family_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(device_family_nie, Unset):
        json_device_family_nie = device_family_nie

    params["device_family__nie"] = json_device_family_nie

    json_device_family_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(device_family_niew, Unset):
        json_device_family_niew = device_family_niew

    params["device_family__niew"] = json_device_family_niew

    json_device_family_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(device_family_nisw, Unset):
        json_device_family_nisw = device_family_nisw

    params["device_family__nisw"] = json_device_family_nisw

    json_device_name: Union[Unset, list[str]] = UNSET
    if not isinstance(device_name, Unset):
        json_device_name = device_name

    params["device_name"] = json_device_name

    params["device_name__empty"] = device_name_empty

    json_device_name_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(device_name_ic, Unset):
        json_device_name_ic = device_name_ic

    params["device_name__ic"] = json_device_name_ic

    json_device_name_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(device_name_ie, Unset):
        json_device_name_ie = device_name_ie

    params["device_name__ie"] = json_device_name_ie

    json_device_name_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(device_name_iew, Unset):
        json_device_name_iew = device_name_iew

    params["device_name__iew"] = json_device_name_iew

    json_device_name_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(device_name_isw, Unset):
        json_device_name_isw = device_name_isw

    params["device_name__isw"] = json_device_name_isw

    json_device_name_n: Union[Unset, list[str]] = UNSET
    if not isinstance(device_name_n, Unset):
        json_device_name_n = device_name_n

    params["device_name__n"] = json_device_name_n

    json_device_name_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(device_name_nic, Unset):
        json_device_name_nic = device_name_nic

    params["device_name__nic"] = json_device_name_nic

    json_device_name_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(device_name_nie, Unset):
        json_device_name_nie = device_name_nie

    params["device_name__nie"] = json_device_name_nie

    json_device_name_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(device_name_niew, Unset):
        json_device_name_niew = device_name_niew

    params["device_name__niew"] = json_device_name_niew

    json_device_name_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(device_name_nisw, Unset):
        json_device_name_nisw = device_name_nisw

    params["device_name__nisw"] = json_device_name_nisw

    json_device_role: Union[Unset, list[str]] = UNSET
    if not isinstance(device_role, Unset):
        json_device_role = device_role

    params["device_role"] = json_device_role

    params["device_role__empty"] = device_role_empty

    json_device_role_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(device_role_ic, Unset):
        json_device_role_ic = device_role_ic

    params["device_role__ic"] = json_device_role_ic

    json_device_role_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(device_role_ie, Unset):
        json_device_role_ie = device_role_ie

    params["device_role__ie"] = json_device_role_ie

    json_device_role_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(device_role_iew, Unset):
        json_device_role_iew = device_role_iew

    params["device_role__iew"] = json_device_role_iew

    json_device_role_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(device_role_isw, Unset):
        json_device_role_isw = device_role_isw

    params["device_role__isw"] = json_device_role_isw

    json_device_role_n: Union[Unset, list[str]] = UNSET
    if not isinstance(device_role_n, Unset):
        json_device_role_n = device_role_n

    params["device_role__n"] = json_device_role_n

    json_device_role_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(device_role_nic, Unset):
        json_device_role_nic = device_role_nic

    params["device_role__nic"] = json_device_role_nic

    json_device_role_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(device_role_nie, Unset):
        json_device_role_nie = device_role_nie

    params["device_role__nie"] = json_device_role_nie

    json_device_role_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(device_role_niew, Unset):
        json_device_role_niew = device_role_niew

    params["device_role__niew"] = json_device_role_niew

    json_device_role_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(device_role_nisw, Unset):
        json_device_role_nisw = device_role_nisw

    params["device_role__nisw"] = json_device_role_nisw

    json_device_type: Union[Unset, list[str]] = UNSET
    if not isinstance(device_type, Unset):
        json_device_type = device_type

    params["device_type"] = json_device_type

    params["device_type__empty"] = device_type_empty

    json_device_type_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(device_type_ic, Unset):
        json_device_type_ic = device_type_ic

    params["device_type__ic"] = json_device_type_ic

    json_device_type_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(device_type_ie, Unset):
        json_device_type_ie = device_type_ie

    params["device_type__ie"] = json_device_type_ie

    json_device_type_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(device_type_iew, Unset):
        json_device_type_iew = device_type_iew

    params["device_type__iew"] = json_device_type_iew

    json_device_type_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(device_type_isw, Unset):
        json_device_type_isw = device_type_isw

    params["device_type__isw"] = json_device_type_isw

    json_device_type_n: Union[Unset, list[str]] = UNSET
    if not isinstance(device_type_n, Unset):
        json_device_type_n = device_type_n

    params["device_type__n"] = json_device_type_n

    json_device_type_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(device_type_nic, Unset):
        json_device_type_nic = device_type_nic

    params["device_type__nic"] = json_device_type_nic

    json_device_type_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(device_type_nie, Unset):
        json_device_type_nie = device_type_nie

    params["device_type__nie"] = json_device_type_nie

    json_device_type_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(device_type_niew, Unset):
        json_device_type_niew = device_type_niew

    params["device_type__niew"] = json_device_type_niew

    json_device_type_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(device_type_nisw, Unset):
        json_device_type_nisw = device_type_nisw

    params["device_type__nisw"] = json_device_type_nisw

    json_exposure: Union[Unset, list[str]] = UNSET
    if not isinstance(exposure, Unset):
        json_exposure = exposure

    params["exposure"] = json_exposure

    params["exposure__empty"] = exposure_empty

    json_exposure_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(exposure_ic, Unset):
        json_exposure_ic = exposure_ic

    params["exposure__ic"] = json_exposure_ic

    json_exposure_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(exposure_ie, Unset):
        json_exposure_ie = exposure_ie

    params["exposure__ie"] = json_exposure_ie

    json_exposure_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(exposure_iew, Unset):
        json_exposure_iew = exposure_iew

    params["exposure__iew"] = json_exposure_iew

    json_exposure_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(exposure_isw, Unset):
        json_exposure_isw = exposure_isw

    params["exposure__isw"] = json_exposure_isw

    json_exposure_n: Union[Unset, list[str]] = UNSET
    if not isinstance(exposure_n, Unset):
        json_exposure_n = exposure_n

    params["exposure__n"] = json_exposure_n

    json_exposure_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(exposure_nic, Unset):
        json_exposure_nic = exposure_nic

    params["exposure__nic"] = json_exposure_nic

    json_exposure_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(exposure_nie, Unset):
        json_exposure_nie = exposure_nie

    params["exposure__nie"] = json_exposure_nie

    json_exposure_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(exposure_niew, Unset):
        json_exposure_niew = exposure_niew

    params["exposure__niew"] = json_exposure_niew

    json_exposure_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(exposure_nisw, Unset):
        json_exposure_nisw = exposure_nisw

    params["exposure__nisw"] = json_exposure_nisw

    json_hardware_cpe: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_cpe, Unset):
        json_hardware_cpe = hardware_cpe

    params["hardware_cpe"] = json_hardware_cpe

    params["hardware_cpe__empty"] = hardware_cpe_empty

    json_hardware_cpe_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_cpe_ic, Unset):
        json_hardware_cpe_ic = hardware_cpe_ic

    params["hardware_cpe__ic"] = json_hardware_cpe_ic

    json_hardware_cpe_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_cpe_ie, Unset):
        json_hardware_cpe_ie = hardware_cpe_ie

    params["hardware_cpe__ie"] = json_hardware_cpe_ie

    json_hardware_cpe_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_cpe_iew, Unset):
        json_hardware_cpe_iew = hardware_cpe_iew

    params["hardware_cpe__iew"] = json_hardware_cpe_iew

    json_hardware_cpe_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_cpe_isw, Unset):
        json_hardware_cpe_isw = hardware_cpe_isw

    params["hardware_cpe__isw"] = json_hardware_cpe_isw

    json_hardware_cpe_n: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_cpe_n, Unset):
        json_hardware_cpe_n = hardware_cpe_n

    params["hardware_cpe__n"] = json_hardware_cpe_n

    json_hardware_cpe_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_cpe_nic, Unset):
        json_hardware_cpe_nic = hardware_cpe_nic

    params["hardware_cpe__nic"] = json_hardware_cpe_nic

    json_hardware_cpe_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_cpe_nie, Unset):
        json_hardware_cpe_nie = hardware_cpe_nie

    params["hardware_cpe__nie"] = json_hardware_cpe_nie

    json_hardware_cpe_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_cpe_niew, Unset):
        json_hardware_cpe_niew = hardware_cpe_niew

    params["hardware_cpe__niew"] = json_hardware_cpe_niew

    json_hardware_cpe_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_cpe_nisw, Unset):
        json_hardware_cpe_nisw = hardware_cpe_nisw

    params["hardware_cpe__nisw"] = json_hardware_cpe_nisw

    json_hardware_version: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_version, Unset):
        json_hardware_version = hardware_version

    params["hardware_version"] = json_hardware_version

    params["hardware_version__empty"] = hardware_version_empty

    json_hardware_version_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_version_ic, Unset):
        json_hardware_version_ic = hardware_version_ic

    params["hardware_version__ic"] = json_hardware_version_ic

    json_hardware_version_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_version_ie, Unset):
        json_hardware_version_ie = hardware_version_ie

    params["hardware_version__ie"] = json_hardware_version_ie

    json_hardware_version_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_version_iew, Unset):
        json_hardware_version_iew = hardware_version_iew

    params["hardware_version__iew"] = json_hardware_version_iew

    json_hardware_version_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_version_isw, Unset):
        json_hardware_version_isw = hardware_version_isw

    params["hardware_version__isw"] = json_hardware_version_isw

    json_hardware_version_n: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_version_n, Unset):
        json_hardware_version_n = hardware_version_n

    params["hardware_version__n"] = json_hardware_version_n

    json_hardware_version_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_version_nic, Unset):
        json_hardware_version_nic = hardware_version_nic

    params["hardware_version__nic"] = json_hardware_version_nic

    json_hardware_version_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_version_nie, Unset):
        json_hardware_version_nie = hardware_version_nie

    params["hardware_version__nie"] = json_hardware_version_nie

    json_hardware_version_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_version_niew, Unset):
        json_hardware_version_niew = hardware_version_niew

    params["hardware_version__niew"] = json_hardware_version_niew

    json_hardware_version_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(hardware_version_nisw, Unset):
        json_hardware_version_nisw = hardware_version_nisw

    params["hardware_version__nisw"] = json_hardware_version_nisw

    params["has_predicted_device"] = has_predicted_device

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

    json_ip_address: Union[Unset, list[str]] = UNSET
    if not isinstance(ip_address, Unset):
        json_ip_address = ip_address

    params["ip_address"] = json_ip_address

    params["ip_address__empty"] = ip_address_empty

    json_ip_address_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(ip_address_ic, Unset):
        json_ip_address_ic = ip_address_ic

    params["ip_address__ic"] = json_ip_address_ic

    json_ip_address_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(ip_address_ie, Unset):
        json_ip_address_ie = ip_address_ie

    params["ip_address__ie"] = json_ip_address_ie

    json_ip_address_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(ip_address_iew, Unset):
        json_ip_address_iew = ip_address_iew

    params["ip_address__iew"] = json_ip_address_iew

    json_ip_address_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(ip_address_isw, Unset):
        json_ip_address_isw = ip_address_isw

    params["ip_address__isw"] = json_ip_address_isw

    json_ip_address_n: Union[Unset, list[str]] = UNSET
    if not isinstance(ip_address_n, Unset):
        json_ip_address_n = ip_address_n

    params["ip_address__n"] = json_ip_address_n

    json_ip_address_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(ip_address_nic, Unset):
        json_ip_address_nic = ip_address_nic

    params["ip_address__nic"] = json_ip_address_nic

    json_ip_address_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(ip_address_nie, Unset):
        json_ip_address_nie = ip_address_nie

    params["ip_address__nie"] = json_ip_address_nie

    json_ip_address_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(ip_address_niew, Unset):
        json_ip_address_niew = ip_address_niew

    params["ip_address__niew"] = json_ip_address_niew

    json_ip_address_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(ip_address_nisw, Unset):
        json_ip_address_nisw = ip_address_nisw

    params["ip_address__nisw"] = json_ip_address_nisw

    json_is_firmware: Union[Unset, list[str]] = UNSET
    if not isinstance(is_firmware, Unset):
        json_is_firmware = is_firmware

    params["is_firmware"] = json_is_firmware

    params["is_firmware__empty"] = is_firmware_empty

    json_is_firmware_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(is_firmware_ic, Unset):
        json_is_firmware_ic = is_firmware_ic

    params["is_firmware__ic"] = json_is_firmware_ic

    json_is_firmware_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(is_firmware_ie, Unset):
        json_is_firmware_ie = is_firmware_ie

    params["is_firmware__ie"] = json_is_firmware_ie

    json_is_firmware_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(is_firmware_iew, Unset):
        json_is_firmware_iew = is_firmware_iew

    params["is_firmware__iew"] = json_is_firmware_iew

    json_is_firmware_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(is_firmware_isw, Unset):
        json_is_firmware_isw = is_firmware_isw

    params["is_firmware__isw"] = json_is_firmware_isw

    json_is_firmware_n: Union[Unset, list[str]] = UNSET
    if not isinstance(is_firmware_n, Unset):
        json_is_firmware_n = is_firmware_n

    params["is_firmware__n"] = json_is_firmware_n

    json_is_firmware_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(is_firmware_nic, Unset):
        json_is_firmware_nic = is_firmware_nic

    params["is_firmware__nic"] = json_is_firmware_nic

    json_is_firmware_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(is_firmware_nie, Unset):
        json_is_firmware_nie = is_firmware_nie

    params["is_firmware__nie"] = json_is_firmware_nie

    json_is_firmware_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(is_firmware_niew, Unset):
        json_is_firmware_niew = is_firmware_niew

    params["is_firmware__niew"] = json_is_firmware_niew

    json_is_firmware_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(is_firmware_nisw, Unset):
        json_is_firmware_nisw = is_firmware_nisw

    params["is_firmware__nisw"] = json_is_firmware_nisw

    json_is_router: Union[Unset, list[str]] = UNSET
    if not isinstance(is_router, Unset):
        json_is_router = is_router

    params["is_router"] = json_is_router

    params["is_router__empty"] = is_router_empty

    json_is_router_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(is_router_ic, Unset):
        json_is_router_ic = is_router_ic

    params["is_router__ic"] = json_is_router_ic

    json_is_router_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(is_router_ie, Unset):
        json_is_router_ie = is_router_ie

    params["is_router__ie"] = json_is_router_ie

    json_is_router_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(is_router_iew, Unset):
        json_is_router_iew = is_router_iew

    params["is_router__iew"] = json_is_router_iew

    json_is_router_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(is_router_isw, Unset):
        json_is_router_isw = is_router_isw

    params["is_router__isw"] = json_is_router_isw

    json_is_router_n: Union[Unset, list[str]] = UNSET
    if not isinstance(is_router_n, Unset):
        json_is_router_n = is_router_n

    params["is_router__n"] = json_is_router_n

    json_is_router_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(is_router_nic, Unset):
        json_is_router_nic = is_router_nic

    params["is_router__nic"] = json_is_router_nic

    json_is_router_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(is_router_nie, Unset):
        json_is_router_nie = is_router_nie

    params["is_router__nie"] = json_is_router_nie

    json_is_router_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(is_router_niew, Unset):
        json_is_router_niew = is_router_niew

    params["is_router__niew"] = json_is_router_niew

    json_is_router_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(is_router_nisw, Unset):
        json_is_router_nisw = is_router_nisw

    params["is_router__nisw"] = json_is_router_nisw

    json_is_safety_critical: Union[Unset, list[str]] = UNSET
    if not isinstance(is_safety_critical, Unset):
        json_is_safety_critical = is_safety_critical

    params["is_safety_critical"] = json_is_safety_critical

    params["is_safety_critical__empty"] = is_safety_critical_empty

    json_is_safety_critical_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(is_safety_critical_ic, Unset):
        json_is_safety_critical_ic = is_safety_critical_ic

    params["is_safety_critical__ic"] = json_is_safety_critical_ic

    json_is_safety_critical_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(is_safety_critical_ie, Unset):
        json_is_safety_critical_ie = is_safety_critical_ie

    params["is_safety_critical__ie"] = json_is_safety_critical_ie

    json_is_safety_critical_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(is_safety_critical_iew, Unset):
        json_is_safety_critical_iew = is_safety_critical_iew

    params["is_safety_critical__iew"] = json_is_safety_critical_iew

    json_is_safety_critical_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(is_safety_critical_isw, Unset):
        json_is_safety_critical_isw = is_safety_critical_isw

    params["is_safety_critical__isw"] = json_is_safety_critical_isw

    json_is_safety_critical_n: Union[Unset, list[str]] = UNSET
    if not isinstance(is_safety_critical_n, Unset):
        json_is_safety_critical_n = is_safety_critical_n

    params["is_safety_critical__n"] = json_is_safety_critical_n

    json_is_safety_critical_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(is_safety_critical_nic, Unset):
        json_is_safety_critical_nic = is_safety_critical_nic

    params["is_safety_critical__nic"] = json_is_safety_critical_nic

    json_is_safety_critical_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(is_safety_critical_nie, Unset):
        json_is_safety_critical_nie = is_safety_critical_nie

    params["is_safety_critical__nie"] = json_is_safety_critical_nie

    json_is_safety_critical_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(is_safety_critical_niew, Unset):
        json_is_safety_critical_niew = is_safety_critical_niew

    params["is_safety_critical__niew"] = json_is_safety_critical_niew

    json_is_safety_critical_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(is_safety_critical_nisw, Unset):
        json_is_safety_critical_nisw = is_safety_critical_nisw

    params["is_safety_critical__nisw"] = json_is_safety_critical_nisw

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

    json_location: Union[Unset, list[str]] = UNSET
    if not isinstance(location, Unset):
        json_location = location

    params["location"] = json_location

    params["location__empty"] = location_empty

    json_location_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(location_ic, Unset):
        json_location_ic = location_ic

    params["location__ic"] = json_location_ic

    json_location_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(location_ie, Unset):
        json_location_ie = location_ie

    params["location__ie"] = json_location_ie

    json_location_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(location_iew, Unset):
        json_location_iew = location_iew

    params["location__iew"] = json_location_iew

    json_location_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(location_isw, Unset):
        json_location_isw = location_isw

    params["location__isw"] = json_location_isw

    json_location_n: Union[Unset, list[str]] = UNSET
    if not isinstance(location_n, Unset):
        json_location_n = location_n

    params["location__n"] = json_location_n

    json_location_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(location_nic, Unset):
        json_location_nic = location_nic

    params["location__nic"] = json_location_nic

    json_location_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(location_nie, Unset):
        json_location_nie = location_nie

    params["location__nie"] = json_location_nie

    json_location_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(location_niew, Unset):
        json_location_niew = location_niew

    params["location__niew"] = json_location_niew

    json_location_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(location_nisw, Unset):
        json_location_nisw = location_nisw

    params["location__nisw"] = json_location_nisw

    json_mac_address: Union[Unset, list[str]] = UNSET
    if not isinstance(mac_address, Unset):
        json_mac_address = mac_address

    params["mac_address"] = json_mac_address

    params["mac_address__empty"] = mac_address_empty

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

    json_manufacturer: Union[Unset, list[str]] = UNSET
    if not isinstance(manufacturer, Unset):
        json_manufacturer = manufacturer

    params["manufacturer"] = json_manufacturer

    params["manufacturer__empty"] = manufacturer_empty

    json_manufacturer_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(manufacturer_ic, Unset):
        json_manufacturer_ic = manufacturer_ic

    params["manufacturer__ic"] = json_manufacturer_ic

    json_manufacturer_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(manufacturer_ie, Unset):
        json_manufacturer_ie = manufacturer_ie

    params["manufacturer__ie"] = json_manufacturer_ie

    json_manufacturer_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(manufacturer_iew, Unset):
        json_manufacturer_iew = manufacturer_iew

    params["manufacturer__iew"] = json_manufacturer_iew

    json_manufacturer_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(manufacturer_isw, Unset):
        json_manufacturer_isw = manufacturer_isw

    params["manufacturer__isw"] = json_manufacturer_isw

    json_manufacturer_n: Union[Unset, list[str]] = UNSET
    if not isinstance(manufacturer_n, Unset):
        json_manufacturer_n = manufacturer_n

    params["manufacturer__n"] = json_manufacturer_n

    json_manufacturer_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(manufacturer_nic, Unset):
        json_manufacturer_nic = manufacturer_nic

    params["manufacturer__nic"] = json_manufacturer_nic

    json_manufacturer_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(manufacturer_nie, Unset):
        json_manufacturer_nie = manufacturer_nie

    params["manufacturer__nie"] = json_manufacturer_nie

    json_manufacturer_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(manufacturer_niew, Unset):
        json_manufacturer_niew = manufacturer_niew

    params["manufacturer__niew"] = json_manufacturer_niew

    json_manufacturer_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(manufacturer_nisw, Unset):
        json_manufacturer_nisw = manufacturer_nisw

    params["manufacturer__nisw"] = json_manufacturer_nisw

    json_modified_by_request: Union[Unset, str] = UNSET
    if not isinstance(modified_by_request, Unset):
        json_modified_by_request = str(modified_by_request)
    params["modified_by_request"] = json_modified_by_request

    params["offset"] = offset

    params["ordering"] = ordering

    json_oui: Union[Unset, list[str]] = UNSET
    if not isinstance(oui, Unset):
        json_oui = oui

    params["oui"] = json_oui

    params["oui__empty"] = oui_empty

    json_oui_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(oui_ic, Unset):
        json_oui_ic = oui_ic

    params["oui__ic"] = json_oui_ic

    json_oui_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(oui_ie, Unset):
        json_oui_ie = oui_ie

    params["oui__ie"] = json_oui_ie

    json_oui_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(oui_iew, Unset):
        json_oui_iew = oui_iew

    params["oui__iew"] = json_oui_iew

    json_oui_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(oui_isw, Unset):
        json_oui_isw = oui_isw

    params["oui__isw"] = json_oui_isw

    json_oui_n: Union[Unset, list[str]] = UNSET
    if not isinstance(oui_n, Unset):
        json_oui_n = oui_n

    params["oui__n"] = json_oui_n

    json_oui_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(oui_nic, Unset):
        json_oui_nic = oui_nic

    params["oui__nic"] = json_oui_nic

    json_oui_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(oui_nie, Unset):
        json_oui_nie = oui_nie

    params["oui__nie"] = json_oui_nie

    json_oui_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(oui_niew, Unset):
        json_oui_niew = oui_niew

    params["oui__niew"] = json_oui_niew

    json_oui_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(oui_nisw, Unset):
        json_oui_nisw = oui_nisw

    params["oui__nisw"] = json_oui_nisw

    json_part_number: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number, Unset):
        json_part_number = part_number

    params["part_number"] = json_part_number

    params["part_number__empty"] = part_number_empty

    json_part_number_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number_ic, Unset):
        json_part_number_ic = part_number_ic

    params["part_number__ic"] = json_part_number_ic

    json_part_number_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number_ie, Unset):
        json_part_number_ie = part_number_ie

    params["part_number__ie"] = json_part_number_ie

    json_part_number_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number_iew, Unset):
        json_part_number_iew = part_number_iew

    params["part_number__iew"] = json_part_number_iew

    json_part_number_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number_isw, Unset):
        json_part_number_isw = part_number_isw

    params["part_number__isw"] = json_part_number_isw

    json_part_number_n: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number_n, Unset):
        json_part_number_n = part_number_n

    params["part_number__n"] = json_part_number_n

    json_part_number_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number_nic, Unset):
        json_part_number_nic = part_number_nic

    params["part_number__nic"] = json_part_number_nic

    json_part_number_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number_nie, Unset):
        json_part_number_nie = part_number_nie

    params["part_number__nie"] = json_part_number_nie

    json_part_number_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number_niew, Unset):
        json_part_number_niew = part_number_niew

    params["part_number__niew"] = json_part_number_niew

    json_part_number_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(part_number_nisw, Unset):
        json_part_number_nisw = part_number_nisw

    params["part_number__nisw"] = json_part_number_nisw

    json_port: Union[Unset, list[str]] = UNSET
    if not isinstance(port, Unset):
        json_port = port

    params["port"] = json_port

    params["port__empty"] = port_empty

    json_port_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(port_ic, Unset):
        json_port_ic = port_ic

    params["port__ic"] = json_port_ic

    json_port_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(port_ie, Unset):
        json_port_ie = port_ie

    params["port__ie"] = json_port_ie

    json_port_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(port_iew, Unset):
        json_port_iew = port_iew

    params["port__iew"] = json_port_iew

    json_port_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(port_isw, Unset):
        json_port_isw = port_isw

    params["port__isw"] = json_port_isw

    json_port_n: Union[Unset, list[str]] = UNSET
    if not isinstance(port_n, Unset):
        json_port_n = port_n

    params["port__n"] = json_port_n

    json_port_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(port_nic, Unset):
        json_port_nic = port_nic

    params["port__nic"] = json_port_nic

    json_port_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(port_nie, Unset):
        json_port_nie = port_nie

    params["port__nie"] = json_port_nie

    json_port_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(port_niew, Unset):
        json_port_niew = port_niew

    params["port__niew"] = json_port_niew

    json_port_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(port_nisw, Unset):
        json_port_nisw = port_nisw

    params["port__nisw"] = json_port_nisw

    params["predicted_device"] = predicted_device

    params["predicted_device__n"] = predicted_device_n

    params["q"] = q

    json_rack: Union[Unset, list[str]] = UNSET
    if not isinstance(rack, Unset):
        json_rack = rack

    params["rack"] = json_rack

    params["rack__empty"] = rack_empty

    json_rack_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(rack_ic, Unset):
        json_rack_ic = rack_ic

    params["rack__ic"] = json_rack_ic

    json_rack_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(rack_ie, Unset):
        json_rack_ie = rack_ie

    params["rack__ie"] = json_rack_ie

    json_rack_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(rack_iew, Unset):
        json_rack_iew = rack_iew

    params["rack__iew"] = json_rack_iew

    json_rack_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(rack_isw, Unset):
        json_rack_isw = rack_isw

    params["rack__isw"] = json_rack_isw

    json_rack_n: Union[Unset, list[str]] = UNSET
    if not isinstance(rack_n, Unset):
        json_rack_n = rack_n

    params["rack__n"] = json_rack_n

    json_rack_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(rack_nic, Unset):
        json_rack_nic = rack_nic

    params["rack__nic"] = json_rack_nic

    json_rack_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(rack_nie, Unset):
        json_rack_nie = rack_nie

    params["rack__nie"] = json_rack_nie

    json_rack_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(rack_niew, Unset):
        json_rack_niew = rack_niew

    params["rack__niew"] = json_rack_niew

    json_rack_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(rack_nisw, Unset):
        json_rack_nisw = rack_nisw

    params["rack__nisw"] = json_rack_nisw

    json_serial_number: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_number, Unset):
        json_serial_number = serial_number

    params["serial_number"] = json_serial_number

    params["serial_number__empty"] = serial_number_empty

    json_serial_number_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_number_ic, Unset):
        json_serial_number_ic = serial_number_ic

    params["serial_number__ic"] = json_serial_number_ic

    json_serial_number_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_number_ie, Unset):
        json_serial_number_ie = serial_number_ie

    params["serial_number__ie"] = json_serial_number_ie

    json_serial_number_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_number_iew, Unset):
        json_serial_number_iew = serial_number_iew

    params["serial_number__iew"] = json_serial_number_iew

    json_serial_number_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_number_isw, Unset):
        json_serial_number_isw = serial_number_isw

    params["serial_number__isw"] = json_serial_number_isw

    json_serial_number_n: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_number_n, Unset):
        json_serial_number_n = serial_number_n

    params["serial_number__n"] = json_serial_number_n

    json_serial_number_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_number_nic, Unset):
        json_serial_number_nic = serial_number_nic

    params["serial_number__nic"] = json_serial_number_nic

    json_serial_number_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_number_nie, Unset):
        json_serial_number_nie = serial_number_nie

    params["serial_number__nie"] = json_serial_number_nie

    json_serial_number_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_number_niew, Unset):
        json_serial_number_niew = serial_number_niew

    params["serial_number__niew"] = json_serial_number_niew

    json_serial_number_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(serial_number_nisw, Unset):
        json_serial_number_nisw = serial_number_nisw

    params["serial_number__nisw"] = json_serial_number_nisw

    json_site: Union[Unset, list[str]] = UNSET
    if not isinstance(site, Unset):
        json_site = site

    params["site"] = json_site

    params["site__empty"] = site_empty

    json_site_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(site_ic, Unset):
        json_site_ic = site_ic

    params["site__ic"] = json_site_ic

    json_site_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(site_ie, Unset):
        json_site_ie = site_ie

    params["site__ie"] = json_site_ie

    json_site_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(site_iew, Unset):
        json_site_iew = site_iew

    params["site__iew"] = json_site_iew

    json_site_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(site_isw, Unset):
        json_site_isw = site_isw

    params["site__isw"] = json_site_isw

    json_site_n: Union[Unset, list[str]] = UNSET
    if not isinstance(site_n, Unset):
        json_site_n = site_n

    params["site__n"] = json_site_n

    json_site_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(site_nic, Unset):
        json_site_nic = site_nic

    params["site__nic"] = json_site_nic

    json_site_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(site_nie, Unset):
        json_site_nie = site_nie

    params["site__nie"] = json_site_nie

    json_site_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(site_niew, Unset):
        json_site_niew = site_niew

    params["site__niew"] = json_site_niew

    json_site_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(site_nisw, Unset):
        json_site_nisw = site_nisw

    params["site__nisw"] = json_site_nisw

    json_software_name: Union[Unset, list[str]] = UNSET
    if not isinstance(software_name, Unset):
        json_software_name = software_name

    params["software_name"] = json_software_name

    params["software_name__empty"] = software_name_empty

    json_software_name_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(software_name_ic, Unset):
        json_software_name_ic = software_name_ic

    params["software_name__ic"] = json_software_name_ic

    json_software_name_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(software_name_ie, Unset):
        json_software_name_ie = software_name_ie

    params["software_name__ie"] = json_software_name_ie

    json_software_name_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(software_name_iew, Unset):
        json_software_name_iew = software_name_iew

    params["software_name__iew"] = json_software_name_iew

    json_software_name_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(software_name_isw, Unset):
        json_software_name_isw = software_name_isw

    params["software_name__isw"] = json_software_name_isw

    json_software_name_n: Union[Unset, list[str]] = UNSET
    if not isinstance(software_name_n, Unset):
        json_software_name_n = software_name_n

    params["software_name__n"] = json_software_name_n

    json_software_name_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(software_name_nic, Unset):
        json_software_name_nic = software_name_nic

    params["software_name__nic"] = json_software_name_nic

    json_software_name_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(software_name_nie, Unset):
        json_software_name_nie = software_name_nie

    params["software_name__nie"] = json_software_name_nie

    json_software_name_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(software_name_niew, Unset):
        json_software_name_niew = software_name_niew

    params["software_name__niew"] = json_software_name_niew

    json_software_name_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(software_name_nisw, Unset):
        json_software_name_nisw = software_name_nisw

    params["software_name__nisw"] = json_software_name_nisw

    json_source: Union[Unset, list[str]] = UNSET
    if not isinstance(source, Unset):
        json_source = source

    params["source"] = json_source

    params["source__empty"] = source_empty

    json_source_ic: Union[Unset, list[str]] = UNSET
    if not isinstance(source_ic, Unset):
        json_source_ic = source_ic

    params["source__ic"] = json_source_ic

    json_source_ie: Union[Unset, list[str]] = UNSET
    if not isinstance(source_ie, Unset):
        json_source_ie = source_ie

    params["source__ie"] = json_source_ie

    json_source_iew: Union[Unset, list[str]] = UNSET
    if not isinstance(source_iew, Unset):
        json_source_iew = source_iew

    params["source__iew"] = json_source_iew

    json_source_isw: Union[Unset, list[str]] = UNSET
    if not isinstance(source_isw, Unset):
        json_source_isw = source_isw

    params["source__isw"] = json_source_isw

    json_source_n: Union[Unset, list[str]] = UNSET
    if not isinstance(source_n, Unset):
        json_source_n = source_n

    params["source__n"] = json_source_n

    json_source_nic: Union[Unset, list[str]] = UNSET
    if not isinstance(source_nic, Unset):
        json_source_nic = source_nic

    params["source__nic"] = json_source_nic

    json_source_nie: Union[Unset, list[str]] = UNSET
    if not isinstance(source_nie, Unset):
        json_source_nie = source_nie

    params["source__nie"] = json_source_nie

    json_source_niew: Union[Unset, list[str]] = UNSET
    if not isinstance(source_niew, Unset):
        json_source_niew = source_niew

    params["source__niew"] = json_source_niew

    json_source_nisw: Union[Unset, list[str]] = UNSET
    if not isinstance(source_nisw, Unset):
        json_source_nisw = source_nisw

    params["source__nisw"] = json_source_nisw

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
        "url": "/api/plugins/d3c/devicefindings-list/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedDeviceFindingList]:
    if response.status_code == 200:
        response_200 = PaginatedDeviceFindingList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedDeviceFindingList]:
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
    confidence: Union[Unset, list[float]] = UNSET,
    confidence_empty: Union[Unset, bool] = UNSET,
    confidence_gt: Union[Unset, list[float]] = UNSET,
    confidence_gte: Union[Unset, list[float]] = UNSET,
    confidence_lt: Union[Unset, list[float]] = UNSET,
    confidence_lte: Union[Unset, list[float]] = UNSET,
    confidence_n: Union[Unset, list[float]] = UNSET,
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
    device: Union[Unset, int] = UNSET,
    device_n: Union[Unset, int] = UNSET,
    device_family: Union[Unset, list[str]] = UNSET,
    device_family_empty: Union[Unset, bool] = UNSET,
    device_family_ic: Union[Unset, list[str]] = UNSET,
    device_family_ie: Union[Unset, list[str]] = UNSET,
    device_family_iew: Union[Unset, list[str]] = UNSET,
    device_family_isw: Union[Unset, list[str]] = UNSET,
    device_family_n: Union[Unset, list[str]] = UNSET,
    device_family_nic: Union[Unset, list[str]] = UNSET,
    device_family_nie: Union[Unset, list[str]] = UNSET,
    device_family_niew: Union[Unset, list[str]] = UNSET,
    device_family_nisw: Union[Unset, list[str]] = UNSET,
    device_name: Union[Unset, list[str]] = UNSET,
    device_name_empty: Union[Unset, bool] = UNSET,
    device_name_ic: Union[Unset, list[str]] = UNSET,
    device_name_ie: Union[Unset, list[str]] = UNSET,
    device_name_iew: Union[Unset, list[str]] = UNSET,
    device_name_isw: Union[Unset, list[str]] = UNSET,
    device_name_n: Union[Unset, list[str]] = UNSET,
    device_name_nic: Union[Unset, list[str]] = UNSET,
    device_name_nie: Union[Unset, list[str]] = UNSET,
    device_name_niew: Union[Unset, list[str]] = UNSET,
    device_name_nisw: Union[Unset, list[str]] = UNSET,
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_empty: Union[Unset, bool] = UNSET,
    device_role_ic: Union[Unset, list[str]] = UNSET,
    device_role_ie: Union[Unset, list[str]] = UNSET,
    device_role_iew: Union[Unset, list[str]] = UNSET,
    device_role_isw: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_nic: Union[Unset, list[str]] = UNSET,
    device_role_nie: Union[Unset, list[str]] = UNSET,
    device_role_niew: Union[Unset, list[str]] = UNSET,
    device_role_nisw: Union[Unset, list[str]] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_empty: Union[Unset, bool] = UNSET,
    device_type_ic: Union[Unset, list[str]] = UNSET,
    device_type_ie: Union[Unset, list[str]] = UNSET,
    device_type_iew: Union[Unset, list[str]] = UNSET,
    device_type_isw: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_nic: Union[Unset, list[str]] = UNSET,
    device_type_nie: Union[Unset, list[str]] = UNSET,
    device_type_niew: Union[Unset, list[str]] = UNSET,
    device_type_nisw: Union[Unset, list[str]] = UNSET,
    exposure: Union[Unset, list[str]] = UNSET,
    exposure_empty: Union[Unset, bool] = UNSET,
    exposure_ic: Union[Unset, list[str]] = UNSET,
    exposure_ie: Union[Unset, list[str]] = UNSET,
    exposure_iew: Union[Unset, list[str]] = UNSET,
    exposure_isw: Union[Unset, list[str]] = UNSET,
    exposure_n: Union[Unset, list[str]] = UNSET,
    exposure_nic: Union[Unset, list[str]] = UNSET,
    exposure_nie: Union[Unset, list[str]] = UNSET,
    exposure_niew: Union[Unset, list[str]] = UNSET,
    exposure_nisw: Union[Unset, list[str]] = UNSET,
    hardware_cpe: Union[Unset, list[str]] = UNSET,
    hardware_cpe_empty: Union[Unset, bool] = UNSET,
    hardware_cpe_ic: Union[Unset, list[str]] = UNSET,
    hardware_cpe_ie: Union[Unset, list[str]] = UNSET,
    hardware_cpe_iew: Union[Unset, list[str]] = UNSET,
    hardware_cpe_isw: Union[Unset, list[str]] = UNSET,
    hardware_cpe_n: Union[Unset, list[str]] = UNSET,
    hardware_cpe_nic: Union[Unset, list[str]] = UNSET,
    hardware_cpe_nie: Union[Unset, list[str]] = UNSET,
    hardware_cpe_niew: Union[Unset, list[str]] = UNSET,
    hardware_cpe_nisw: Union[Unset, list[str]] = UNSET,
    hardware_version: Union[Unset, list[str]] = UNSET,
    hardware_version_empty: Union[Unset, bool] = UNSET,
    hardware_version_ic: Union[Unset, list[str]] = UNSET,
    hardware_version_ie: Union[Unset, list[str]] = UNSET,
    hardware_version_iew: Union[Unset, list[str]] = UNSET,
    hardware_version_isw: Union[Unset, list[str]] = UNSET,
    hardware_version_n: Union[Unset, list[str]] = UNSET,
    hardware_version_nic: Union[Unset, list[str]] = UNSET,
    hardware_version_nie: Union[Unset, list[str]] = UNSET,
    hardware_version_niew: Union[Unset, list[str]] = UNSET,
    hardware_version_nisw: Union[Unset, list[str]] = UNSET,
    has_predicted_device: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    ip_address: Union[Unset, list[str]] = UNSET,
    ip_address_empty: Union[Unset, bool] = UNSET,
    ip_address_ic: Union[Unset, list[str]] = UNSET,
    ip_address_ie: Union[Unset, list[str]] = UNSET,
    ip_address_iew: Union[Unset, list[str]] = UNSET,
    ip_address_isw: Union[Unset, list[str]] = UNSET,
    ip_address_n: Union[Unset, list[str]] = UNSET,
    ip_address_nic: Union[Unset, list[str]] = UNSET,
    ip_address_nie: Union[Unset, list[str]] = UNSET,
    ip_address_niew: Union[Unset, list[str]] = UNSET,
    ip_address_nisw: Union[Unset, list[str]] = UNSET,
    is_firmware: Union[Unset, list[str]] = UNSET,
    is_firmware_empty: Union[Unset, bool] = UNSET,
    is_firmware_ic: Union[Unset, list[str]] = UNSET,
    is_firmware_ie: Union[Unset, list[str]] = UNSET,
    is_firmware_iew: Union[Unset, list[str]] = UNSET,
    is_firmware_isw: Union[Unset, list[str]] = UNSET,
    is_firmware_n: Union[Unset, list[str]] = UNSET,
    is_firmware_nic: Union[Unset, list[str]] = UNSET,
    is_firmware_nie: Union[Unset, list[str]] = UNSET,
    is_firmware_niew: Union[Unset, list[str]] = UNSET,
    is_firmware_nisw: Union[Unset, list[str]] = UNSET,
    is_router: Union[Unset, list[str]] = UNSET,
    is_router_empty: Union[Unset, bool] = UNSET,
    is_router_ic: Union[Unset, list[str]] = UNSET,
    is_router_ie: Union[Unset, list[str]] = UNSET,
    is_router_iew: Union[Unset, list[str]] = UNSET,
    is_router_isw: Union[Unset, list[str]] = UNSET,
    is_router_n: Union[Unset, list[str]] = UNSET,
    is_router_nic: Union[Unset, list[str]] = UNSET,
    is_router_nie: Union[Unset, list[str]] = UNSET,
    is_router_niew: Union[Unset, list[str]] = UNSET,
    is_router_nisw: Union[Unset, list[str]] = UNSET,
    is_safety_critical: Union[Unset, list[str]] = UNSET,
    is_safety_critical_empty: Union[Unset, bool] = UNSET,
    is_safety_critical_ic: Union[Unset, list[str]] = UNSET,
    is_safety_critical_ie: Union[Unset, list[str]] = UNSET,
    is_safety_critical_iew: Union[Unset, list[str]] = UNSET,
    is_safety_critical_isw: Union[Unset, list[str]] = UNSET,
    is_safety_critical_n: Union[Unset, list[str]] = UNSET,
    is_safety_critical_nic: Union[Unset, list[str]] = UNSET,
    is_safety_critical_nie: Union[Unset, list[str]] = UNSET,
    is_safety_critical_niew: Union[Unset, list[str]] = UNSET,
    is_safety_critical_nisw: Union[Unset, list[str]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_empty: Union[Unset, bool] = UNSET,
    location_ic: Union[Unset, list[str]] = UNSET,
    location_ie: Union[Unset, list[str]] = UNSET,
    location_iew: Union[Unset, list[str]] = UNSET,
    location_isw: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_nic: Union[Unset, list[str]] = UNSET,
    location_nie: Union[Unset, list[str]] = UNSET,
    location_niew: Union[Unset, list[str]] = UNSET,
    location_nisw: Union[Unset, list[str]] = UNSET,
    mac_address: Union[Unset, list[str]] = UNSET,
    mac_address_empty: Union[Unset, bool] = UNSET,
    mac_address_ic: Union[Unset, list[str]] = UNSET,
    mac_address_ie: Union[Unset, list[str]] = UNSET,
    mac_address_iew: Union[Unset, list[str]] = UNSET,
    mac_address_isw: Union[Unset, list[str]] = UNSET,
    mac_address_n: Union[Unset, list[str]] = UNSET,
    mac_address_nic: Union[Unset, list[str]] = UNSET,
    mac_address_nie: Union[Unset, list[str]] = UNSET,
    mac_address_niew: Union[Unset, list[str]] = UNSET,
    mac_address_nisw: Union[Unset, list[str]] = UNSET,
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_empty: Union[Unset, bool] = UNSET,
    manufacturer_ic: Union[Unset, list[str]] = UNSET,
    manufacturer_ie: Union[Unset, list[str]] = UNSET,
    manufacturer_iew: Union[Unset, list[str]] = UNSET,
    manufacturer_isw: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_nic: Union[Unset, list[str]] = UNSET,
    manufacturer_nie: Union[Unset, list[str]] = UNSET,
    manufacturer_niew: Union[Unset, list[str]] = UNSET,
    manufacturer_nisw: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    oui: Union[Unset, list[str]] = UNSET,
    oui_empty: Union[Unset, bool] = UNSET,
    oui_ic: Union[Unset, list[str]] = UNSET,
    oui_ie: Union[Unset, list[str]] = UNSET,
    oui_iew: Union[Unset, list[str]] = UNSET,
    oui_isw: Union[Unset, list[str]] = UNSET,
    oui_n: Union[Unset, list[str]] = UNSET,
    oui_nic: Union[Unset, list[str]] = UNSET,
    oui_nie: Union[Unset, list[str]] = UNSET,
    oui_niew: Union[Unset, list[str]] = UNSET,
    oui_nisw: Union[Unset, list[str]] = UNSET,
    part_number: Union[Unset, list[str]] = UNSET,
    part_number_empty: Union[Unset, bool] = UNSET,
    part_number_ic: Union[Unset, list[str]] = UNSET,
    part_number_ie: Union[Unset, list[str]] = UNSET,
    part_number_iew: Union[Unset, list[str]] = UNSET,
    part_number_isw: Union[Unset, list[str]] = UNSET,
    part_number_n: Union[Unset, list[str]] = UNSET,
    part_number_nic: Union[Unset, list[str]] = UNSET,
    part_number_nie: Union[Unset, list[str]] = UNSET,
    part_number_niew: Union[Unset, list[str]] = UNSET,
    part_number_nisw: Union[Unset, list[str]] = UNSET,
    port: Union[Unset, list[str]] = UNSET,
    port_empty: Union[Unset, bool] = UNSET,
    port_ic: Union[Unset, list[str]] = UNSET,
    port_ie: Union[Unset, list[str]] = UNSET,
    port_iew: Union[Unset, list[str]] = UNSET,
    port_isw: Union[Unset, list[str]] = UNSET,
    port_n: Union[Unset, list[str]] = UNSET,
    port_nic: Union[Unset, list[str]] = UNSET,
    port_nie: Union[Unset, list[str]] = UNSET,
    port_niew: Union[Unset, list[str]] = UNSET,
    port_nisw: Union[Unset, list[str]] = UNSET,
    predicted_device: Union[Unset, int] = UNSET,
    predicted_device_n: Union[Unset, int] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_empty: Union[Unset, bool] = UNSET,
    rack_ic: Union[Unset, list[str]] = UNSET,
    rack_ie: Union[Unset, list[str]] = UNSET,
    rack_iew: Union[Unset, list[str]] = UNSET,
    rack_isw: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
    rack_nic: Union[Unset, list[str]] = UNSET,
    rack_nie: Union[Unset, list[str]] = UNSET,
    rack_niew: Union[Unset, list[str]] = UNSET,
    rack_nisw: Union[Unset, list[str]] = UNSET,
    serial_number: Union[Unset, list[str]] = UNSET,
    serial_number_empty: Union[Unset, bool] = UNSET,
    serial_number_ic: Union[Unset, list[str]] = UNSET,
    serial_number_ie: Union[Unset, list[str]] = UNSET,
    serial_number_iew: Union[Unset, list[str]] = UNSET,
    serial_number_isw: Union[Unset, list[str]] = UNSET,
    serial_number_n: Union[Unset, list[str]] = UNSET,
    serial_number_nic: Union[Unset, list[str]] = UNSET,
    serial_number_nie: Union[Unset, list[str]] = UNSET,
    serial_number_niew: Union[Unset, list[str]] = UNSET,
    serial_number_nisw: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_empty: Union[Unset, bool] = UNSET,
    site_ic: Union[Unset, list[str]] = UNSET,
    site_ie: Union[Unset, list[str]] = UNSET,
    site_iew: Union[Unset, list[str]] = UNSET,
    site_isw: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_nic: Union[Unset, list[str]] = UNSET,
    site_nie: Union[Unset, list[str]] = UNSET,
    site_niew: Union[Unset, list[str]] = UNSET,
    site_nisw: Union[Unset, list[str]] = UNSET,
    software_name: Union[Unset, list[str]] = UNSET,
    software_name_empty: Union[Unset, bool] = UNSET,
    software_name_ic: Union[Unset, list[str]] = UNSET,
    software_name_ie: Union[Unset, list[str]] = UNSET,
    software_name_iew: Union[Unset, list[str]] = UNSET,
    software_name_isw: Union[Unset, list[str]] = UNSET,
    software_name_n: Union[Unset, list[str]] = UNSET,
    software_name_nic: Union[Unset, list[str]] = UNSET,
    software_name_nie: Union[Unset, list[str]] = UNSET,
    software_name_niew: Union[Unset, list[str]] = UNSET,
    software_name_nisw: Union[Unset, list[str]] = UNSET,
    source: Union[Unset, list[str]] = UNSET,
    source_empty: Union[Unset, bool] = UNSET,
    source_ic: Union[Unset, list[str]] = UNSET,
    source_ie: Union[Unset, list[str]] = UNSET,
    source_iew: Union[Unset, list[str]] = UNSET,
    source_isw: Union[Unset, list[str]] = UNSET,
    source_n: Union[Unset, list[str]] = UNSET,
    source_nic: Union[Unset, list[str]] = UNSET,
    source_nie: Union[Unset, list[str]] = UNSET,
    source_niew: Union[Unset, list[str]] = UNSET,
    source_nisw: Union[Unset, list[str]] = UNSET,
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
) -> Response[PaginatedDeviceFindingList]:
    """ViewSet for DeviceFinding.

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
        confidence (Union[Unset, list[float]]):
        confidence_empty (Union[Unset, bool]):
        confidence_gt (Union[Unset, list[float]]):
        confidence_gte (Union[Unset, list[float]]):
        confidence_lt (Union[Unset, list[float]]):
        confidence_lte (Union[Unset, list[float]]):
        confidence_n (Union[Unset, list[float]]):
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
        device (Union[Unset, int]):
        device_n (Union[Unset, int]):
        device_family (Union[Unset, list[str]]):
        device_family_empty (Union[Unset, bool]):
        device_family_ic (Union[Unset, list[str]]):
        device_family_ie (Union[Unset, list[str]]):
        device_family_iew (Union[Unset, list[str]]):
        device_family_isw (Union[Unset, list[str]]):
        device_family_n (Union[Unset, list[str]]):
        device_family_nic (Union[Unset, list[str]]):
        device_family_nie (Union[Unset, list[str]]):
        device_family_niew (Union[Unset, list[str]]):
        device_family_nisw (Union[Unset, list[str]]):
        device_name (Union[Unset, list[str]]):
        device_name_empty (Union[Unset, bool]):
        device_name_ic (Union[Unset, list[str]]):
        device_name_ie (Union[Unset, list[str]]):
        device_name_iew (Union[Unset, list[str]]):
        device_name_isw (Union[Unset, list[str]]):
        device_name_n (Union[Unset, list[str]]):
        device_name_nic (Union[Unset, list[str]]):
        device_name_nie (Union[Unset, list[str]]):
        device_name_niew (Union[Unset, list[str]]):
        device_name_nisw (Union[Unset, list[str]]):
        device_role (Union[Unset, list[str]]):
        device_role_empty (Union[Unset, bool]):
        device_role_ic (Union[Unset, list[str]]):
        device_role_ie (Union[Unset, list[str]]):
        device_role_iew (Union[Unset, list[str]]):
        device_role_isw (Union[Unset, list[str]]):
        device_role_n (Union[Unset, list[str]]):
        device_role_nic (Union[Unset, list[str]]):
        device_role_nie (Union[Unset, list[str]]):
        device_role_niew (Union[Unset, list[str]]):
        device_role_nisw (Union[Unset, list[str]]):
        device_type (Union[Unset, list[str]]):
        device_type_empty (Union[Unset, bool]):
        device_type_ic (Union[Unset, list[str]]):
        device_type_ie (Union[Unset, list[str]]):
        device_type_iew (Union[Unset, list[str]]):
        device_type_isw (Union[Unset, list[str]]):
        device_type_n (Union[Unset, list[str]]):
        device_type_nic (Union[Unset, list[str]]):
        device_type_nie (Union[Unset, list[str]]):
        device_type_niew (Union[Unset, list[str]]):
        device_type_nisw (Union[Unset, list[str]]):
        exposure (Union[Unset, list[str]]):
        exposure_empty (Union[Unset, bool]):
        exposure_ic (Union[Unset, list[str]]):
        exposure_ie (Union[Unset, list[str]]):
        exposure_iew (Union[Unset, list[str]]):
        exposure_isw (Union[Unset, list[str]]):
        exposure_n (Union[Unset, list[str]]):
        exposure_nic (Union[Unset, list[str]]):
        exposure_nie (Union[Unset, list[str]]):
        exposure_niew (Union[Unset, list[str]]):
        exposure_nisw (Union[Unset, list[str]]):
        hardware_cpe (Union[Unset, list[str]]):
        hardware_cpe_empty (Union[Unset, bool]):
        hardware_cpe_ic (Union[Unset, list[str]]):
        hardware_cpe_ie (Union[Unset, list[str]]):
        hardware_cpe_iew (Union[Unset, list[str]]):
        hardware_cpe_isw (Union[Unset, list[str]]):
        hardware_cpe_n (Union[Unset, list[str]]):
        hardware_cpe_nic (Union[Unset, list[str]]):
        hardware_cpe_nie (Union[Unset, list[str]]):
        hardware_cpe_niew (Union[Unset, list[str]]):
        hardware_cpe_nisw (Union[Unset, list[str]]):
        hardware_version (Union[Unset, list[str]]):
        hardware_version_empty (Union[Unset, bool]):
        hardware_version_ic (Union[Unset, list[str]]):
        hardware_version_ie (Union[Unset, list[str]]):
        hardware_version_iew (Union[Unset, list[str]]):
        hardware_version_isw (Union[Unset, list[str]]):
        hardware_version_n (Union[Unset, list[str]]):
        hardware_version_nic (Union[Unset, list[str]]):
        hardware_version_nie (Union[Unset, list[str]]):
        hardware_version_niew (Union[Unset, list[str]]):
        hardware_version_nisw (Union[Unset, list[str]]):
        has_predicted_device (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        ip_address (Union[Unset, list[str]]):
        ip_address_empty (Union[Unset, bool]):
        ip_address_ic (Union[Unset, list[str]]):
        ip_address_ie (Union[Unset, list[str]]):
        ip_address_iew (Union[Unset, list[str]]):
        ip_address_isw (Union[Unset, list[str]]):
        ip_address_n (Union[Unset, list[str]]):
        ip_address_nic (Union[Unset, list[str]]):
        ip_address_nie (Union[Unset, list[str]]):
        ip_address_niew (Union[Unset, list[str]]):
        ip_address_nisw (Union[Unset, list[str]]):
        is_firmware (Union[Unset, list[str]]):
        is_firmware_empty (Union[Unset, bool]):
        is_firmware_ic (Union[Unset, list[str]]):
        is_firmware_ie (Union[Unset, list[str]]):
        is_firmware_iew (Union[Unset, list[str]]):
        is_firmware_isw (Union[Unset, list[str]]):
        is_firmware_n (Union[Unset, list[str]]):
        is_firmware_nic (Union[Unset, list[str]]):
        is_firmware_nie (Union[Unset, list[str]]):
        is_firmware_niew (Union[Unset, list[str]]):
        is_firmware_nisw (Union[Unset, list[str]]):
        is_router (Union[Unset, list[str]]):
        is_router_empty (Union[Unset, bool]):
        is_router_ic (Union[Unset, list[str]]):
        is_router_ie (Union[Unset, list[str]]):
        is_router_iew (Union[Unset, list[str]]):
        is_router_isw (Union[Unset, list[str]]):
        is_router_n (Union[Unset, list[str]]):
        is_router_nic (Union[Unset, list[str]]):
        is_router_nie (Union[Unset, list[str]]):
        is_router_niew (Union[Unset, list[str]]):
        is_router_nisw (Union[Unset, list[str]]):
        is_safety_critical (Union[Unset, list[str]]):
        is_safety_critical_empty (Union[Unset, bool]):
        is_safety_critical_ic (Union[Unset, list[str]]):
        is_safety_critical_ie (Union[Unset, list[str]]):
        is_safety_critical_iew (Union[Unset, list[str]]):
        is_safety_critical_isw (Union[Unset, list[str]]):
        is_safety_critical_n (Union[Unset, list[str]]):
        is_safety_critical_nic (Union[Unset, list[str]]):
        is_safety_critical_nie (Union[Unset, list[str]]):
        is_safety_critical_niew (Union[Unset, list[str]]):
        is_safety_critical_nisw (Union[Unset, list[str]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_empty (Union[Unset, bool]):
        location_ic (Union[Unset, list[str]]):
        location_ie (Union[Unset, list[str]]):
        location_iew (Union[Unset, list[str]]):
        location_isw (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_nic (Union[Unset, list[str]]):
        location_nie (Union[Unset, list[str]]):
        location_niew (Union[Unset, list[str]]):
        location_nisw (Union[Unset, list[str]]):
        mac_address (Union[Unset, list[str]]):
        mac_address_empty (Union[Unset, bool]):
        mac_address_ic (Union[Unset, list[str]]):
        mac_address_ie (Union[Unset, list[str]]):
        mac_address_iew (Union[Unset, list[str]]):
        mac_address_isw (Union[Unset, list[str]]):
        mac_address_n (Union[Unset, list[str]]):
        mac_address_nic (Union[Unset, list[str]]):
        mac_address_nie (Union[Unset, list[str]]):
        mac_address_niew (Union[Unset, list[str]]):
        mac_address_nisw (Union[Unset, list[str]]):
        manufacturer (Union[Unset, list[str]]):
        manufacturer_empty (Union[Unset, bool]):
        manufacturer_ic (Union[Unset, list[str]]):
        manufacturer_ie (Union[Unset, list[str]]):
        manufacturer_iew (Union[Unset, list[str]]):
        manufacturer_isw (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_nic (Union[Unset, list[str]]):
        manufacturer_nie (Union[Unset, list[str]]):
        manufacturer_niew (Union[Unset, list[str]]):
        manufacturer_nisw (Union[Unset, list[str]]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        oui (Union[Unset, list[str]]):
        oui_empty (Union[Unset, bool]):
        oui_ic (Union[Unset, list[str]]):
        oui_ie (Union[Unset, list[str]]):
        oui_iew (Union[Unset, list[str]]):
        oui_isw (Union[Unset, list[str]]):
        oui_n (Union[Unset, list[str]]):
        oui_nic (Union[Unset, list[str]]):
        oui_nie (Union[Unset, list[str]]):
        oui_niew (Union[Unset, list[str]]):
        oui_nisw (Union[Unset, list[str]]):
        part_number (Union[Unset, list[str]]):
        part_number_empty (Union[Unset, bool]):
        part_number_ic (Union[Unset, list[str]]):
        part_number_ie (Union[Unset, list[str]]):
        part_number_iew (Union[Unset, list[str]]):
        part_number_isw (Union[Unset, list[str]]):
        part_number_n (Union[Unset, list[str]]):
        part_number_nic (Union[Unset, list[str]]):
        part_number_nie (Union[Unset, list[str]]):
        part_number_niew (Union[Unset, list[str]]):
        part_number_nisw (Union[Unset, list[str]]):
        port (Union[Unset, list[str]]):
        port_empty (Union[Unset, bool]):
        port_ic (Union[Unset, list[str]]):
        port_ie (Union[Unset, list[str]]):
        port_iew (Union[Unset, list[str]]):
        port_isw (Union[Unset, list[str]]):
        port_n (Union[Unset, list[str]]):
        port_nic (Union[Unset, list[str]]):
        port_nie (Union[Unset, list[str]]):
        port_niew (Union[Unset, list[str]]):
        port_nisw (Union[Unset, list[str]]):
        predicted_device (Union[Unset, int]):
        predicted_device_n (Union[Unset, int]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_empty (Union[Unset, bool]):
        rack_ic (Union[Unset, list[str]]):
        rack_ie (Union[Unset, list[str]]):
        rack_iew (Union[Unset, list[str]]):
        rack_isw (Union[Unset, list[str]]):
        rack_n (Union[Unset, list[str]]):
        rack_nic (Union[Unset, list[str]]):
        rack_nie (Union[Unset, list[str]]):
        rack_niew (Union[Unset, list[str]]):
        rack_nisw (Union[Unset, list[str]]):
        serial_number (Union[Unset, list[str]]):
        serial_number_empty (Union[Unset, bool]):
        serial_number_ic (Union[Unset, list[str]]):
        serial_number_ie (Union[Unset, list[str]]):
        serial_number_iew (Union[Unset, list[str]]):
        serial_number_isw (Union[Unset, list[str]]):
        serial_number_n (Union[Unset, list[str]]):
        serial_number_nic (Union[Unset, list[str]]):
        serial_number_nie (Union[Unset, list[str]]):
        serial_number_niew (Union[Unset, list[str]]):
        serial_number_nisw (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_empty (Union[Unset, bool]):
        site_ic (Union[Unset, list[str]]):
        site_ie (Union[Unset, list[str]]):
        site_iew (Union[Unset, list[str]]):
        site_isw (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_nic (Union[Unset, list[str]]):
        site_nie (Union[Unset, list[str]]):
        site_niew (Union[Unset, list[str]]):
        site_nisw (Union[Unset, list[str]]):
        software_name (Union[Unset, list[str]]):
        software_name_empty (Union[Unset, bool]):
        software_name_ic (Union[Unset, list[str]]):
        software_name_ie (Union[Unset, list[str]]):
        software_name_iew (Union[Unset, list[str]]):
        software_name_isw (Union[Unset, list[str]]):
        software_name_n (Union[Unset, list[str]]):
        software_name_nic (Union[Unset, list[str]]):
        software_name_nie (Union[Unset, list[str]]):
        software_name_niew (Union[Unset, list[str]]):
        software_name_nisw (Union[Unset, list[str]]):
        source (Union[Unset, list[str]]):
        source_empty (Union[Unset, bool]):
        source_ic (Union[Unset, list[str]]):
        source_ie (Union[Unset, list[str]]):
        source_iew (Union[Unset, list[str]]):
        source_isw (Union[Unset, list[str]]):
        source_n (Union[Unset, list[str]]):
        source_nic (Union[Unset, list[str]]):
        source_nie (Union[Unset, list[str]]):
        source_niew (Union[Unset, list[str]]):
        source_nisw (Union[Unset, list[str]]):
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
        Response[PaginatedDeviceFindingList]
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
        confidence=confidence,
        confidence_empty=confidence_empty,
        confidence_gt=confidence_gt,
        confidence_gte=confidence_gte,
        confidence_lt=confidence_lt,
        confidence_lte=confidence_lte,
        confidence_n=confidence_n,
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
        device_family=device_family,
        device_family_empty=device_family_empty,
        device_family_ic=device_family_ic,
        device_family_ie=device_family_ie,
        device_family_iew=device_family_iew,
        device_family_isw=device_family_isw,
        device_family_n=device_family_n,
        device_family_nic=device_family_nic,
        device_family_nie=device_family_nie,
        device_family_niew=device_family_niew,
        device_family_nisw=device_family_nisw,
        device_name=device_name,
        device_name_empty=device_name_empty,
        device_name_ic=device_name_ic,
        device_name_ie=device_name_ie,
        device_name_iew=device_name_iew,
        device_name_isw=device_name_isw,
        device_name_n=device_name_n,
        device_name_nic=device_name_nic,
        device_name_nie=device_name_nie,
        device_name_niew=device_name_niew,
        device_name_nisw=device_name_nisw,
        device_role=device_role,
        device_role_empty=device_role_empty,
        device_role_ic=device_role_ic,
        device_role_ie=device_role_ie,
        device_role_iew=device_role_iew,
        device_role_isw=device_role_isw,
        device_role_n=device_role_n,
        device_role_nic=device_role_nic,
        device_role_nie=device_role_nie,
        device_role_niew=device_role_niew,
        device_role_nisw=device_role_nisw,
        device_type=device_type,
        device_type_empty=device_type_empty,
        device_type_ic=device_type_ic,
        device_type_ie=device_type_ie,
        device_type_iew=device_type_iew,
        device_type_isw=device_type_isw,
        device_type_n=device_type_n,
        device_type_nic=device_type_nic,
        device_type_nie=device_type_nie,
        device_type_niew=device_type_niew,
        device_type_nisw=device_type_nisw,
        exposure=exposure,
        exposure_empty=exposure_empty,
        exposure_ic=exposure_ic,
        exposure_ie=exposure_ie,
        exposure_iew=exposure_iew,
        exposure_isw=exposure_isw,
        exposure_n=exposure_n,
        exposure_nic=exposure_nic,
        exposure_nie=exposure_nie,
        exposure_niew=exposure_niew,
        exposure_nisw=exposure_nisw,
        hardware_cpe=hardware_cpe,
        hardware_cpe_empty=hardware_cpe_empty,
        hardware_cpe_ic=hardware_cpe_ic,
        hardware_cpe_ie=hardware_cpe_ie,
        hardware_cpe_iew=hardware_cpe_iew,
        hardware_cpe_isw=hardware_cpe_isw,
        hardware_cpe_n=hardware_cpe_n,
        hardware_cpe_nic=hardware_cpe_nic,
        hardware_cpe_nie=hardware_cpe_nie,
        hardware_cpe_niew=hardware_cpe_niew,
        hardware_cpe_nisw=hardware_cpe_nisw,
        hardware_version=hardware_version,
        hardware_version_empty=hardware_version_empty,
        hardware_version_ic=hardware_version_ic,
        hardware_version_ie=hardware_version_ie,
        hardware_version_iew=hardware_version_iew,
        hardware_version_isw=hardware_version_isw,
        hardware_version_n=hardware_version_n,
        hardware_version_nic=hardware_version_nic,
        hardware_version_nie=hardware_version_nie,
        hardware_version_niew=hardware_version_niew,
        hardware_version_nisw=hardware_version_nisw,
        has_predicted_device=has_predicted_device,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        ip_address=ip_address,
        ip_address_empty=ip_address_empty,
        ip_address_ic=ip_address_ic,
        ip_address_ie=ip_address_ie,
        ip_address_iew=ip_address_iew,
        ip_address_isw=ip_address_isw,
        ip_address_n=ip_address_n,
        ip_address_nic=ip_address_nic,
        ip_address_nie=ip_address_nie,
        ip_address_niew=ip_address_niew,
        ip_address_nisw=ip_address_nisw,
        is_firmware=is_firmware,
        is_firmware_empty=is_firmware_empty,
        is_firmware_ic=is_firmware_ic,
        is_firmware_ie=is_firmware_ie,
        is_firmware_iew=is_firmware_iew,
        is_firmware_isw=is_firmware_isw,
        is_firmware_n=is_firmware_n,
        is_firmware_nic=is_firmware_nic,
        is_firmware_nie=is_firmware_nie,
        is_firmware_niew=is_firmware_niew,
        is_firmware_nisw=is_firmware_nisw,
        is_router=is_router,
        is_router_empty=is_router_empty,
        is_router_ic=is_router_ic,
        is_router_ie=is_router_ie,
        is_router_iew=is_router_iew,
        is_router_isw=is_router_isw,
        is_router_n=is_router_n,
        is_router_nic=is_router_nic,
        is_router_nie=is_router_nie,
        is_router_niew=is_router_niew,
        is_router_nisw=is_router_nisw,
        is_safety_critical=is_safety_critical,
        is_safety_critical_empty=is_safety_critical_empty,
        is_safety_critical_ic=is_safety_critical_ic,
        is_safety_critical_ie=is_safety_critical_ie,
        is_safety_critical_iew=is_safety_critical_iew,
        is_safety_critical_isw=is_safety_critical_isw,
        is_safety_critical_n=is_safety_critical_n,
        is_safety_critical_nic=is_safety_critical_nic,
        is_safety_critical_nie=is_safety_critical_nie,
        is_safety_critical_niew=is_safety_critical_niew,
        is_safety_critical_nisw=is_safety_critical_nisw,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        location=location,
        location_empty=location_empty,
        location_ic=location_ic,
        location_ie=location_ie,
        location_iew=location_iew,
        location_isw=location_isw,
        location_n=location_n,
        location_nic=location_nic,
        location_nie=location_nie,
        location_niew=location_niew,
        location_nisw=location_nisw,
        mac_address=mac_address,
        mac_address_empty=mac_address_empty,
        mac_address_ic=mac_address_ic,
        mac_address_ie=mac_address_ie,
        mac_address_iew=mac_address_iew,
        mac_address_isw=mac_address_isw,
        mac_address_n=mac_address_n,
        mac_address_nic=mac_address_nic,
        mac_address_nie=mac_address_nie,
        mac_address_niew=mac_address_niew,
        mac_address_nisw=mac_address_nisw,
        manufacturer=manufacturer,
        manufacturer_empty=manufacturer_empty,
        manufacturer_ic=manufacturer_ic,
        manufacturer_ie=manufacturer_ie,
        manufacturer_iew=manufacturer_iew,
        manufacturer_isw=manufacturer_isw,
        manufacturer_n=manufacturer_n,
        manufacturer_nic=manufacturer_nic,
        manufacturer_nie=manufacturer_nie,
        manufacturer_niew=manufacturer_niew,
        manufacturer_nisw=manufacturer_nisw,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        oui=oui,
        oui_empty=oui_empty,
        oui_ic=oui_ic,
        oui_ie=oui_ie,
        oui_iew=oui_iew,
        oui_isw=oui_isw,
        oui_n=oui_n,
        oui_nic=oui_nic,
        oui_nie=oui_nie,
        oui_niew=oui_niew,
        oui_nisw=oui_nisw,
        part_number=part_number,
        part_number_empty=part_number_empty,
        part_number_ic=part_number_ic,
        part_number_ie=part_number_ie,
        part_number_iew=part_number_iew,
        part_number_isw=part_number_isw,
        part_number_n=part_number_n,
        part_number_nic=part_number_nic,
        part_number_nie=part_number_nie,
        part_number_niew=part_number_niew,
        part_number_nisw=part_number_nisw,
        port=port,
        port_empty=port_empty,
        port_ic=port_ic,
        port_ie=port_ie,
        port_iew=port_iew,
        port_isw=port_isw,
        port_n=port_n,
        port_nic=port_nic,
        port_nie=port_nie,
        port_niew=port_niew,
        port_nisw=port_nisw,
        predicted_device=predicted_device,
        predicted_device_n=predicted_device_n,
        q=q,
        rack=rack,
        rack_empty=rack_empty,
        rack_ic=rack_ic,
        rack_ie=rack_ie,
        rack_iew=rack_iew,
        rack_isw=rack_isw,
        rack_n=rack_n,
        rack_nic=rack_nic,
        rack_nie=rack_nie,
        rack_niew=rack_niew,
        rack_nisw=rack_nisw,
        serial_number=serial_number,
        serial_number_empty=serial_number_empty,
        serial_number_ic=serial_number_ic,
        serial_number_ie=serial_number_ie,
        serial_number_iew=serial_number_iew,
        serial_number_isw=serial_number_isw,
        serial_number_n=serial_number_n,
        serial_number_nic=serial_number_nic,
        serial_number_nie=serial_number_nie,
        serial_number_niew=serial_number_niew,
        serial_number_nisw=serial_number_nisw,
        site=site,
        site_empty=site_empty,
        site_ic=site_ic,
        site_ie=site_ie,
        site_iew=site_iew,
        site_isw=site_isw,
        site_n=site_n,
        site_nic=site_nic,
        site_nie=site_nie,
        site_niew=site_niew,
        site_nisw=site_nisw,
        software_name=software_name,
        software_name_empty=software_name_empty,
        software_name_ic=software_name_ic,
        software_name_ie=software_name_ie,
        software_name_iew=software_name_iew,
        software_name_isw=software_name_isw,
        software_name_n=software_name_n,
        software_name_nic=software_name_nic,
        software_name_nie=software_name_nie,
        software_name_niew=software_name_niew,
        software_name_nisw=software_name_nisw,
        source=source,
        source_empty=source_empty,
        source_ic=source_ic,
        source_ie=source_ie,
        source_iew=source_iew,
        source_isw=source_isw,
        source_n=source_n,
        source_nic=source_nic,
        source_nie=source_nie,
        source_niew=source_niew,
        source_nisw=source_nisw,
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
    confidence: Union[Unset, list[float]] = UNSET,
    confidence_empty: Union[Unset, bool] = UNSET,
    confidence_gt: Union[Unset, list[float]] = UNSET,
    confidence_gte: Union[Unset, list[float]] = UNSET,
    confidence_lt: Union[Unset, list[float]] = UNSET,
    confidence_lte: Union[Unset, list[float]] = UNSET,
    confidence_n: Union[Unset, list[float]] = UNSET,
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
    device: Union[Unset, int] = UNSET,
    device_n: Union[Unset, int] = UNSET,
    device_family: Union[Unset, list[str]] = UNSET,
    device_family_empty: Union[Unset, bool] = UNSET,
    device_family_ic: Union[Unset, list[str]] = UNSET,
    device_family_ie: Union[Unset, list[str]] = UNSET,
    device_family_iew: Union[Unset, list[str]] = UNSET,
    device_family_isw: Union[Unset, list[str]] = UNSET,
    device_family_n: Union[Unset, list[str]] = UNSET,
    device_family_nic: Union[Unset, list[str]] = UNSET,
    device_family_nie: Union[Unset, list[str]] = UNSET,
    device_family_niew: Union[Unset, list[str]] = UNSET,
    device_family_nisw: Union[Unset, list[str]] = UNSET,
    device_name: Union[Unset, list[str]] = UNSET,
    device_name_empty: Union[Unset, bool] = UNSET,
    device_name_ic: Union[Unset, list[str]] = UNSET,
    device_name_ie: Union[Unset, list[str]] = UNSET,
    device_name_iew: Union[Unset, list[str]] = UNSET,
    device_name_isw: Union[Unset, list[str]] = UNSET,
    device_name_n: Union[Unset, list[str]] = UNSET,
    device_name_nic: Union[Unset, list[str]] = UNSET,
    device_name_nie: Union[Unset, list[str]] = UNSET,
    device_name_niew: Union[Unset, list[str]] = UNSET,
    device_name_nisw: Union[Unset, list[str]] = UNSET,
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_empty: Union[Unset, bool] = UNSET,
    device_role_ic: Union[Unset, list[str]] = UNSET,
    device_role_ie: Union[Unset, list[str]] = UNSET,
    device_role_iew: Union[Unset, list[str]] = UNSET,
    device_role_isw: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_nic: Union[Unset, list[str]] = UNSET,
    device_role_nie: Union[Unset, list[str]] = UNSET,
    device_role_niew: Union[Unset, list[str]] = UNSET,
    device_role_nisw: Union[Unset, list[str]] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_empty: Union[Unset, bool] = UNSET,
    device_type_ic: Union[Unset, list[str]] = UNSET,
    device_type_ie: Union[Unset, list[str]] = UNSET,
    device_type_iew: Union[Unset, list[str]] = UNSET,
    device_type_isw: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_nic: Union[Unset, list[str]] = UNSET,
    device_type_nie: Union[Unset, list[str]] = UNSET,
    device_type_niew: Union[Unset, list[str]] = UNSET,
    device_type_nisw: Union[Unset, list[str]] = UNSET,
    exposure: Union[Unset, list[str]] = UNSET,
    exposure_empty: Union[Unset, bool] = UNSET,
    exposure_ic: Union[Unset, list[str]] = UNSET,
    exposure_ie: Union[Unset, list[str]] = UNSET,
    exposure_iew: Union[Unset, list[str]] = UNSET,
    exposure_isw: Union[Unset, list[str]] = UNSET,
    exposure_n: Union[Unset, list[str]] = UNSET,
    exposure_nic: Union[Unset, list[str]] = UNSET,
    exposure_nie: Union[Unset, list[str]] = UNSET,
    exposure_niew: Union[Unset, list[str]] = UNSET,
    exposure_nisw: Union[Unset, list[str]] = UNSET,
    hardware_cpe: Union[Unset, list[str]] = UNSET,
    hardware_cpe_empty: Union[Unset, bool] = UNSET,
    hardware_cpe_ic: Union[Unset, list[str]] = UNSET,
    hardware_cpe_ie: Union[Unset, list[str]] = UNSET,
    hardware_cpe_iew: Union[Unset, list[str]] = UNSET,
    hardware_cpe_isw: Union[Unset, list[str]] = UNSET,
    hardware_cpe_n: Union[Unset, list[str]] = UNSET,
    hardware_cpe_nic: Union[Unset, list[str]] = UNSET,
    hardware_cpe_nie: Union[Unset, list[str]] = UNSET,
    hardware_cpe_niew: Union[Unset, list[str]] = UNSET,
    hardware_cpe_nisw: Union[Unset, list[str]] = UNSET,
    hardware_version: Union[Unset, list[str]] = UNSET,
    hardware_version_empty: Union[Unset, bool] = UNSET,
    hardware_version_ic: Union[Unset, list[str]] = UNSET,
    hardware_version_ie: Union[Unset, list[str]] = UNSET,
    hardware_version_iew: Union[Unset, list[str]] = UNSET,
    hardware_version_isw: Union[Unset, list[str]] = UNSET,
    hardware_version_n: Union[Unset, list[str]] = UNSET,
    hardware_version_nic: Union[Unset, list[str]] = UNSET,
    hardware_version_nie: Union[Unset, list[str]] = UNSET,
    hardware_version_niew: Union[Unset, list[str]] = UNSET,
    hardware_version_nisw: Union[Unset, list[str]] = UNSET,
    has_predicted_device: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    ip_address: Union[Unset, list[str]] = UNSET,
    ip_address_empty: Union[Unset, bool] = UNSET,
    ip_address_ic: Union[Unset, list[str]] = UNSET,
    ip_address_ie: Union[Unset, list[str]] = UNSET,
    ip_address_iew: Union[Unset, list[str]] = UNSET,
    ip_address_isw: Union[Unset, list[str]] = UNSET,
    ip_address_n: Union[Unset, list[str]] = UNSET,
    ip_address_nic: Union[Unset, list[str]] = UNSET,
    ip_address_nie: Union[Unset, list[str]] = UNSET,
    ip_address_niew: Union[Unset, list[str]] = UNSET,
    ip_address_nisw: Union[Unset, list[str]] = UNSET,
    is_firmware: Union[Unset, list[str]] = UNSET,
    is_firmware_empty: Union[Unset, bool] = UNSET,
    is_firmware_ic: Union[Unset, list[str]] = UNSET,
    is_firmware_ie: Union[Unset, list[str]] = UNSET,
    is_firmware_iew: Union[Unset, list[str]] = UNSET,
    is_firmware_isw: Union[Unset, list[str]] = UNSET,
    is_firmware_n: Union[Unset, list[str]] = UNSET,
    is_firmware_nic: Union[Unset, list[str]] = UNSET,
    is_firmware_nie: Union[Unset, list[str]] = UNSET,
    is_firmware_niew: Union[Unset, list[str]] = UNSET,
    is_firmware_nisw: Union[Unset, list[str]] = UNSET,
    is_router: Union[Unset, list[str]] = UNSET,
    is_router_empty: Union[Unset, bool] = UNSET,
    is_router_ic: Union[Unset, list[str]] = UNSET,
    is_router_ie: Union[Unset, list[str]] = UNSET,
    is_router_iew: Union[Unset, list[str]] = UNSET,
    is_router_isw: Union[Unset, list[str]] = UNSET,
    is_router_n: Union[Unset, list[str]] = UNSET,
    is_router_nic: Union[Unset, list[str]] = UNSET,
    is_router_nie: Union[Unset, list[str]] = UNSET,
    is_router_niew: Union[Unset, list[str]] = UNSET,
    is_router_nisw: Union[Unset, list[str]] = UNSET,
    is_safety_critical: Union[Unset, list[str]] = UNSET,
    is_safety_critical_empty: Union[Unset, bool] = UNSET,
    is_safety_critical_ic: Union[Unset, list[str]] = UNSET,
    is_safety_critical_ie: Union[Unset, list[str]] = UNSET,
    is_safety_critical_iew: Union[Unset, list[str]] = UNSET,
    is_safety_critical_isw: Union[Unset, list[str]] = UNSET,
    is_safety_critical_n: Union[Unset, list[str]] = UNSET,
    is_safety_critical_nic: Union[Unset, list[str]] = UNSET,
    is_safety_critical_nie: Union[Unset, list[str]] = UNSET,
    is_safety_critical_niew: Union[Unset, list[str]] = UNSET,
    is_safety_critical_nisw: Union[Unset, list[str]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_empty: Union[Unset, bool] = UNSET,
    location_ic: Union[Unset, list[str]] = UNSET,
    location_ie: Union[Unset, list[str]] = UNSET,
    location_iew: Union[Unset, list[str]] = UNSET,
    location_isw: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_nic: Union[Unset, list[str]] = UNSET,
    location_nie: Union[Unset, list[str]] = UNSET,
    location_niew: Union[Unset, list[str]] = UNSET,
    location_nisw: Union[Unset, list[str]] = UNSET,
    mac_address: Union[Unset, list[str]] = UNSET,
    mac_address_empty: Union[Unset, bool] = UNSET,
    mac_address_ic: Union[Unset, list[str]] = UNSET,
    mac_address_ie: Union[Unset, list[str]] = UNSET,
    mac_address_iew: Union[Unset, list[str]] = UNSET,
    mac_address_isw: Union[Unset, list[str]] = UNSET,
    mac_address_n: Union[Unset, list[str]] = UNSET,
    mac_address_nic: Union[Unset, list[str]] = UNSET,
    mac_address_nie: Union[Unset, list[str]] = UNSET,
    mac_address_niew: Union[Unset, list[str]] = UNSET,
    mac_address_nisw: Union[Unset, list[str]] = UNSET,
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_empty: Union[Unset, bool] = UNSET,
    manufacturer_ic: Union[Unset, list[str]] = UNSET,
    manufacturer_ie: Union[Unset, list[str]] = UNSET,
    manufacturer_iew: Union[Unset, list[str]] = UNSET,
    manufacturer_isw: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_nic: Union[Unset, list[str]] = UNSET,
    manufacturer_nie: Union[Unset, list[str]] = UNSET,
    manufacturer_niew: Union[Unset, list[str]] = UNSET,
    manufacturer_nisw: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    oui: Union[Unset, list[str]] = UNSET,
    oui_empty: Union[Unset, bool] = UNSET,
    oui_ic: Union[Unset, list[str]] = UNSET,
    oui_ie: Union[Unset, list[str]] = UNSET,
    oui_iew: Union[Unset, list[str]] = UNSET,
    oui_isw: Union[Unset, list[str]] = UNSET,
    oui_n: Union[Unset, list[str]] = UNSET,
    oui_nic: Union[Unset, list[str]] = UNSET,
    oui_nie: Union[Unset, list[str]] = UNSET,
    oui_niew: Union[Unset, list[str]] = UNSET,
    oui_nisw: Union[Unset, list[str]] = UNSET,
    part_number: Union[Unset, list[str]] = UNSET,
    part_number_empty: Union[Unset, bool] = UNSET,
    part_number_ic: Union[Unset, list[str]] = UNSET,
    part_number_ie: Union[Unset, list[str]] = UNSET,
    part_number_iew: Union[Unset, list[str]] = UNSET,
    part_number_isw: Union[Unset, list[str]] = UNSET,
    part_number_n: Union[Unset, list[str]] = UNSET,
    part_number_nic: Union[Unset, list[str]] = UNSET,
    part_number_nie: Union[Unset, list[str]] = UNSET,
    part_number_niew: Union[Unset, list[str]] = UNSET,
    part_number_nisw: Union[Unset, list[str]] = UNSET,
    port: Union[Unset, list[str]] = UNSET,
    port_empty: Union[Unset, bool] = UNSET,
    port_ic: Union[Unset, list[str]] = UNSET,
    port_ie: Union[Unset, list[str]] = UNSET,
    port_iew: Union[Unset, list[str]] = UNSET,
    port_isw: Union[Unset, list[str]] = UNSET,
    port_n: Union[Unset, list[str]] = UNSET,
    port_nic: Union[Unset, list[str]] = UNSET,
    port_nie: Union[Unset, list[str]] = UNSET,
    port_niew: Union[Unset, list[str]] = UNSET,
    port_nisw: Union[Unset, list[str]] = UNSET,
    predicted_device: Union[Unset, int] = UNSET,
    predicted_device_n: Union[Unset, int] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_empty: Union[Unset, bool] = UNSET,
    rack_ic: Union[Unset, list[str]] = UNSET,
    rack_ie: Union[Unset, list[str]] = UNSET,
    rack_iew: Union[Unset, list[str]] = UNSET,
    rack_isw: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
    rack_nic: Union[Unset, list[str]] = UNSET,
    rack_nie: Union[Unset, list[str]] = UNSET,
    rack_niew: Union[Unset, list[str]] = UNSET,
    rack_nisw: Union[Unset, list[str]] = UNSET,
    serial_number: Union[Unset, list[str]] = UNSET,
    serial_number_empty: Union[Unset, bool] = UNSET,
    serial_number_ic: Union[Unset, list[str]] = UNSET,
    serial_number_ie: Union[Unset, list[str]] = UNSET,
    serial_number_iew: Union[Unset, list[str]] = UNSET,
    serial_number_isw: Union[Unset, list[str]] = UNSET,
    serial_number_n: Union[Unset, list[str]] = UNSET,
    serial_number_nic: Union[Unset, list[str]] = UNSET,
    serial_number_nie: Union[Unset, list[str]] = UNSET,
    serial_number_niew: Union[Unset, list[str]] = UNSET,
    serial_number_nisw: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_empty: Union[Unset, bool] = UNSET,
    site_ic: Union[Unset, list[str]] = UNSET,
    site_ie: Union[Unset, list[str]] = UNSET,
    site_iew: Union[Unset, list[str]] = UNSET,
    site_isw: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_nic: Union[Unset, list[str]] = UNSET,
    site_nie: Union[Unset, list[str]] = UNSET,
    site_niew: Union[Unset, list[str]] = UNSET,
    site_nisw: Union[Unset, list[str]] = UNSET,
    software_name: Union[Unset, list[str]] = UNSET,
    software_name_empty: Union[Unset, bool] = UNSET,
    software_name_ic: Union[Unset, list[str]] = UNSET,
    software_name_ie: Union[Unset, list[str]] = UNSET,
    software_name_iew: Union[Unset, list[str]] = UNSET,
    software_name_isw: Union[Unset, list[str]] = UNSET,
    software_name_n: Union[Unset, list[str]] = UNSET,
    software_name_nic: Union[Unset, list[str]] = UNSET,
    software_name_nie: Union[Unset, list[str]] = UNSET,
    software_name_niew: Union[Unset, list[str]] = UNSET,
    software_name_nisw: Union[Unset, list[str]] = UNSET,
    source: Union[Unset, list[str]] = UNSET,
    source_empty: Union[Unset, bool] = UNSET,
    source_ic: Union[Unset, list[str]] = UNSET,
    source_ie: Union[Unset, list[str]] = UNSET,
    source_iew: Union[Unset, list[str]] = UNSET,
    source_isw: Union[Unset, list[str]] = UNSET,
    source_n: Union[Unset, list[str]] = UNSET,
    source_nic: Union[Unset, list[str]] = UNSET,
    source_nie: Union[Unset, list[str]] = UNSET,
    source_niew: Union[Unset, list[str]] = UNSET,
    source_nisw: Union[Unset, list[str]] = UNSET,
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
) -> Optional[PaginatedDeviceFindingList]:
    """ViewSet for DeviceFinding.

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
        confidence (Union[Unset, list[float]]):
        confidence_empty (Union[Unset, bool]):
        confidence_gt (Union[Unset, list[float]]):
        confidence_gte (Union[Unset, list[float]]):
        confidence_lt (Union[Unset, list[float]]):
        confidence_lte (Union[Unset, list[float]]):
        confidence_n (Union[Unset, list[float]]):
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
        device (Union[Unset, int]):
        device_n (Union[Unset, int]):
        device_family (Union[Unset, list[str]]):
        device_family_empty (Union[Unset, bool]):
        device_family_ic (Union[Unset, list[str]]):
        device_family_ie (Union[Unset, list[str]]):
        device_family_iew (Union[Unset, list[str]]):
        device_family_isw (Union[Unset, list[str]]):
        device_family_n (Union[Unset, list[str]]):
        device_family_nic (Union[Unset, list[str]]):
        device_family_nie (Union[Unset, list[str]]):
        device_family_niew (Union[Unset, list[str]]):
        device_family_nisw (Union[Unset, list[str]]):
        device_name (Union[Unset, list[str]]):
        device_name_empty (Union[Unset, bool]):
        device_name_ic (Union[Unset, list[str]]):
        device_name_ie (Union[Unset, list[str]]):
        device_name_iew (Union[Unset, list[str]]):
        device_name_isw (Union[Unset, list[str]]):
        device_name_n (Union[Unset, list[str]]):
        device_name_nic (Union[Unset, list[str]]):
        device_name_nie (Union[Unset, list[str]]):
        device_name_niew (Union[Unset, list[str]]):
        device_name_nisw (Union[Unset, list[str]]):
        device_role (Union[Unset, list[str]]):
        device_role_empty (Union[Unset, bool]):
        device_role_ic (Union[Unset, list[str]]):
        device_role_ie (Union[Unset, list[str]]):
        device_role_iew (Union[Unset, list[str]]):
        device_role_isw (Union[Unset, list[str]]):
        device_role_n (Union[Unset, list[str]]):
        device_role_nic (Union[Unset, list[str]]):
        device_role_nie (Union[Unset, list[str]]):
        device_role_niew (Union[Unset, list[str]]):
        device_role_nisw (Union[Unset, list[str]]):
        device_type (Union[Unset, list[str]]):
        device_type_empty (Union[Unset, bool]):
        device_type_ic (Union[Unset, list[str]]):
        device_type_ie (Union[Unset, list[str]]):
        device_type_iew (Union[Unset, list[str]]):
        device_type_isw (Union[Unset, list[str]]):
        device_type_n (Union[Unset, list[str]]):
        device_type_nic (Union[Unset, list[str]]):
        device_type_nie (Union[Unset, list[str]]):
        device_type_niew (Union[Unset, list[str]]):
        device_type_nisw (Union[Unset, list[str]]):
        exposure (Union[Unset, list[str]]):
        exposure_empty (Union[Unset, bool]):
        exposure_ic (Union[Unset, list[str]]):
        exposure_ie (Union[Unset, list[str]]):
        exposure_iew (Union[Unset, list[str]]):
        exposure_isw (Union[Unset, list[str]]):
        exposure_n (Union[Unset, list[str]]):
        exposure_nic (Union[Unset, list[str]]):
        exposure_nie (Union[Unset, list[str]]):
        exposure_niew (Union[Unset, list[str]]):
        exposure_nisw (Union[Unset, list[str]]):
        hardware_cpe (Union[Unset, list[str]]):
        hardware_cpe_empty (Union[Unset, bool]):
        hardware_cpe_ic (Union[Unset, list[str]]):
        hardware_cpe_ie (Union[Unset, list[str]]):
        hardware_cpe_iew (Union[Unset, list[str]]):
        hardware_cpe_isw (Union[Unset, list[str]]):
        hardware_cpe_n (Union[Unset, list[str]]):
        hardware_cpe_nic (Union[Unset, list[str]]):
        hardware_cpe_nie (Union[Unset, list[str]]):
        hardware_cpe_niew (Union[Unset, list[str]]):
        hardware_cpe_nisw (Union[Unset, list[str]]):
        hardware_version (Union[Unset, list[str]]):
        hardware_version_empty (Union[Unset, bool]):
        hardware_version_ic (Union[Unset, list[str]]):
        hardware_version_ie (Union[Unset, list[str]]):
        hardware_version_iew (Union[Unset, list[str]]):
        hardware_version_isw (Union[Unset, list[str]]):
        hardware_version_n (Union[Unset, list[str]]):
        hardware_version_nic (Union[Unset, list[str]]):
        hardware_version_nie (Union[Unset, list[str]]):
        hardware_version_niew (Union[Unset, list[str]]):
        hardware_version_nisw (Union[Unset, list[str]]):
        has_predicted_device (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        ip_address (Union[Unset, list[str]]):
        ip_address_empty (Union[Unset, bool]):
        ip_address_ic (Union[Unset, list[str]]):
        ip_address_ie (Union[Unset, list[str]]):
        ip_address_iew (Union[Unset, list[str]]):
        ip_address_isw (Union[Unset, list[str]]):
        ip_address_n (Union[Unset, list[str]]):
        ip_address_nic (Union[Unset, list[str]]):
        ip_address_nie (Union[Unset, list[str]]):
        ip_address_niew (Union[Unset, list[str]]):
        ip_address_nisw (Union[Unset, list[str]]):
        is_firmware (Union[Unset, list[str]]):
        is_firmware_empty (Union[Unset, bool]):
        is_firmware_ic (Union[Unset, list[str]]):
        is_firmware_ie (Union[Unset, list[str]]):
        is_firmware_iew (Union[Unset, list[str]]):
        is_firmware_isw (Union[Unset, list[str]]):
        is_firmware_n (Union[Unset, list[str]]):
        is_firmware_nic (Union[Unset, list[str]]):
        is_firmware_nie (Union[Unset, list[str]]):
        is_firmware_niew (Union[Unset, list[str]]):
        is_firmware_nisw (Union[Unset, list[str]]):
        is_router (Union[Unset, list[str]]):
        is_router_empty (Union[Unset, bool]):
        is_router_ic (Union[Unset, list[str]]):
        is_router_ie (Union[Unset, list[str]]):
        is_router_iew (Union[Unset, list[str]]):
        is_router_isw (Union[Unset, list[str]]):
        is_router_n (Union[Unset, list[str]]):
        is_router_nic (Union[Unset, list[str]]):
        is_router_nie (Union[Unset, list[str]]):
        is_router_niew (Union[Unset, list[str]]):
        is_router_nisw (Union[Unset, list[str]]):
        is_safety_critical (Union[Unset, list[str]]):
        is_safety_critical_empty (Union[Unset, bool]):
        is_safety_critical_ic (Union[Unset, list[str]]):
        is_safety_critical_ie (Union[Unset, list[str]]):
        is_safety_critical_iew (Union[Unset, list[str]]):
        is_safety_critical_isw (Union[Unset, list[str]]):
        is_safety_critical_n (Union[Unset, list[str]]):
        is_safety_critical_nic (Union[Unset, list[str]]):
        is_safety_critical_nie (Union[Unset, list[str]]):
        is_safety_critical_niew (Union[Unset, list[str]]):
        is_safety_critical_nisw (Union[Unset, list[str]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_empty (Union[Unset, bool]):
        location_ic (Union[Unset, list[str]]):
        location_ie (Union[Unset, list[str]]):
        location_iew (Union[Unset, list[str]]):
        location_isw (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_nic (Union[Unset, list[str]]):
        location_nie (Union[Unset, list[str]]):
        location_niew (Union[Unset, list[str]]):
        location_nisw (Union[Unset, list[str]]):
        mac_address (Union[Unset, list[str]]):
        mac_address_empty (Union[Unset, bool]):
        mac_address_ic (Union[Unset, list[str]]):
        mac_address_ie (Union[Unset, list[str]]):
        mac_address_iew (Union[Unset, list[str]]):
        mac_address_isw (Union[Unset, list[str]]):
        mac_address_n (Union[Unset, list[str]]):
        mac_address_nic (Union[Unset, list[str]]):
        mac_address_nie (Union[Unset, list[str]]):
        mac_address_niew (Union[Unset, list[str]]):
        mac_address_nisw (Union[Unset, list[str]]):
        manufacturer (Union[Unset, list[str]]):
        manufacturer_empty (Union[Unset, bool]):
        manufacturer_ic (Union[Unset, list[str]]):
        manufacturer_ie (Union[Unset, list[str]]):
        manufacturer_iew (Union[Unset, list[str]]):
        manufacturer_isw (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_nic (Union[Unset, list[str]]):
        manufacturer_nie (Union[Unset, list[str]]):
        manufacturer_niew (Union[Unset, list[str]]):
        manufacturer_nisw (Union[Unset, list[str]]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        oui (Union[Unset, list[str]]):
        oui_empty (Union[Unset, bool]):
        oui_ic (Union[Unset, list[str]]):
        oui_ie (Union[Unset, list[str]]):
        oui_iew (Union[Unset, list[str]]):
        oui_isw (Union[Unset, list[str]]):
        oui_n (Union[Unset, list[str]]):
        oui_nic (Union[Unset, list[str]]):
        oui_nie (Union[Unset, list[str]]):
        oui_niew (Union[Unset, list[str]]):
        oui_nisw (Union[Unset, list[str]]):
        part_number (Union[Unset, list[str]]):
        part_number_empty (Union[Unset, bool]):
        part_number_ic (Union[Unset, list[str]]):
        part_number_ie (Union[Unset, list[str]]):
        part_number_iew (Union[Unset, list[str]]):
        part_number_isw (Union[Unset, list[str]]):
        part_number_n (Union[Unset, list[str]]):
        part_number_nic (Union[Unset, list[str]]):
        part_number_nie (Union[Unset, list[str]]):
        part_number_niew (Union[Unset, list[str]]):
        part_number_nisw (Union[Unset, list[str]]):
        port (Union[Unset, list[str]]):
        port_empty (Union[Unset, bool]):
        port_ic (Union[Unset, list[str]]):
        port_ie (Union[Unset, list[str]]):
        port_iew (Union[Unset, list[str]]):
        port_isw (Union[Unset, list[str]]):
        port_n (Union[Unset, list[str]]):
        port_nic (Union[Unset, list[str]]):
        port_nie (Union[Unset, list[str]]):
        port_niew (Union[Unset, list[str]]):
        port_nisw (Union[Unset, list[str]]):
        predicted_device (Union[Unset, int]):
        predicted_device_n (Union[Unset, int]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_empty (Union[Unset, bool]):
        rack_ic (Union[Unset, list[str]]):
        rack_ie (Union[Unset, list[str]]):
        rack_iew (Union[Unset, list[str]]):
        rack_isw (Union[Unset, list[str]]):
        rack_n (Union[Unset, list[str]]):
        rack_nic (Union[Unset, list[str]]):
        rack_nie (Union[Unset, list[str]]):
        rack_niew (Union[Unset, list[str]]):
        rack_nisw (Union[Unset, list[str]]):
        serial_number (Union[Unset, list[str]]):
        serial_number_empty (Union[Unset, bool]):
        serial_number_ic (Union[Unset, list[str]]):
        serial_number_ie (Union[Unset, list[str]]):
        serial_number_iew (Union[Unset, list[str]]):
        serial_number_isw (Union[Unset, list[str]]):
        serial_number_n (Union[Unset, list[str]]):
        serial_number_nic (Union[Unset, list[str]]):
        serial_number_nie (Union[Unset, list[str]]):
        serial_number_niew (Union[Unset, list[str]]):
        serial_number_nisw (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_empty (Union[Unset, bool]):
        site_ic (Union[Unset, list[str]]):
        site_ie (Union[Unset, list[str]]):
        site_iew (Union[Unset, list[str]]):
        site_isw (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_nic (Union[Unset, list[str]]):
        site_nie (Union[Unset, list[str]]):
        site_niew (Union[Unset, list[str]]):
        site_nisw (Union[Unset, list[str]]):
        software_name (Union[Unset, list[str]]):
        software_name_empty (Union[Unset, bool]):
        software_name_ic (Union[Unset, list[str]]):
        software_name_ie (Union[Unset, list[str]]):
        software_name_iew (Union[Unset, list[str]]):
        software_name_isw (Union[Unset, list[str]]):
        software_name_n (Union[Unset, list[str]]):
        software_name_nic (Union[Unset, list[str]]):
        software_name_nie (Union[Unset, list[str]]):
        software_name_niew (Union[Unset, list[str]]):
        software_name_nisw (Union[Unset, list[str]]):
        source (Union[Unset, list[str]]):
        source_empty (Union[Unset, bool]):
        source_ic (Union[Unset, list[str]]):
        source_ie (Union[Unset, list[str]]):
        source_iew (Union[Unset, list[str]]):
        source_isw (Union[Unset, list[str]]):
        source_n (Union[Unset, list[str]]):
        source_nic (Union[Unset, list[str]]):
        source_nie (Union[Unset, list[str]]):
        source_niew (Union[Unset, list[str]]):
        source_nisw (Union[Unset, list[str]]):
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
        PaginatedDeviceFindingList
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
        confidence=confidence,
        confidence_empty=confidence_empty,
        confidence_gt=confidence_gt,
        confidence_gte=confidence_gte,
        confidence_lt=confidence_lt,
        confidence_lte=confidence_lte,
        confidence_n=confidence_n,
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
        device_family=device_family,
        device_family_empty=device_family_empty,
        device_family_ic=device_family_ic,
        device_family_ie=device_family_ie,
        device_family_iew=device_family_iew,
        device_family_isw=device_family_isw,
        device_family_n=device_family_n,
        device_family_nic=device_family_nic,
        device_family_nie=device_family_nie,
        device_family_niew=device_family_niew,
        device_family_nisw=device_family_nisw,
        device_name=device_name,
        device_name_empty=device_name_empty,
        device_name_ic=device_name_ic,
        device_name_ie=device_name_ie,
        device_name_iew=device_name_iew,
        device_name_isw=device_name_isw,
        device_name_n=device_name_n,
        device_name_nic=device_name_nic,
        device_name_nie=device_name_nie,
        device_name_niew=device_name_niew,
        device_name_nisw=device_name_nisw,
        device_role=device_role,
        device_role_empty=device_role_empty,
        device_role_ic=device_role_ic,
        device_role_ie=device_role_ie,
        device_role_iew=device_role_iew,
        device_role_isw=device_role_isw,
        device_role_n=device_role_n,
        device_role_nic=device_role_nic,
        device_role_nie=device_role_nie,
        device_role_niew=device_role_niew,
        device_role_nisw=device_role_nisw,
        device_type=device_type,
        device_type_empty=device_type_empty,
        device_type_ic=device_type_ic,
        device_type_ie=device_type_ie,
        device_type_iew=device_type_iew,
        device_type_isw=device_type_isw,
        device_type_n=device_type_n,
        device_type_nic=device_type_nic,
        device_type_nie=device_type_nie,
        device_type_niew=device_type_niew,
        device_type_nisw=device_type_nisw,
        exposure=exposure,
        exposure_empty=exposure_empty,
        exposure_ic=exposure_ic,
        exposure_ie=exposure_ie,
        exposure_iew=exposure_iew,
        exposure_isw=exposure_isw,
        exposure_n=exposure_n,
        exposure_nic=exposure_nic,
        exposure_nie=exposure_nie,
        exposure_niew=exposure_niew,
        exposure_nisw=exposure_nisw,
        hardware_cpe=hardware_cpe,
        hardware_cpe_empty=hardware_cpe_empty,
        hardware_cpe_ic=hardware_cpe_ic,
        hardware_cpe_ie=hardware_cpe_ie,
        hardware_cpe_iew=hardware_cpe_iew,
        hardware_cpe_isw=hardware_cpe_isw,
        hardware_cpe_n=hardware_cpe_n,
        hardware_cpe_nic=hardware_cpe_nic,
        hardware_cpe_nie=hardware_cpe_nie,
        hardware_cpe_niew=hardware_cpe_niew,
        hardware_cpe_nisw=hardware_cpe_nisw,
        hardware_version=hardware_version,
        hardware_version_empty=hardware_version_empty,
        hardware_version_ic=hardware_version_ic,
        hardware_version_ie=hardware_version_ie,
        hardware_version_iew=hardware_version_iew,
        hardware_version_isw=hardware_version_isw,
        hardware_version_n=hardware_version_n,
        hardware_version_nic=hardware_version_nic,
        hardware_version_nie=hardware_version_nie,
        hardware_version_niew=hardware_version_niew,
        hardware_version_nisw=hardware_version_nisw,
        has_predicted_device=has_predicted_device,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        ip_address=ip_address,
        ip_address_empty=ip_address_empty,
        ip_address_ic=ip_address_ic,
        ip_address_ie=ip_address_ie,
        ip_address_iew=ip_address_iew,
        ip_address_isw=ip_address_isw,
        ip_address_n=ip_address_n,
        ip_address_nic=ip_address_nic,
        ip_address_nie=ip_address_nie,
        ip_address_niew=ip_address_niew,
        ip_address_nisw=ip_address_nisw,
        is_firmware=is_firmware,
        is_firmware_empty=is_firmware_empty,
        is_firmware_ic=is_firmware_ic,
        is_firmware_ie=is_firmware_ie,
        is_firmware_iew=is_firmware_iew,
        is_firmware_isw=is_firmware_isw,
        is_firmware_n=is_firmware_n,
        is_firmware_nic=is_firmware_nic,
        is_firmware_nie=is_firmware_nie,
        is_firmware_niew=is_firmware_niew,
        is_firmware_nisw=is_firmware_nisw,
        is_router=is_router,
        is_router_empty=is_router_empty,
        is_router_ic=is_router_ic,
        is_router_ie=is_router_ie,
        is_router_iew=is_router_iew,
        is_router_isw=is_router_isw,
        is_router_n=is_router_n,
        is_router_nic=is_router_nic,
        is_router_nie=is_router_nie,
        is_router_niew=is_router_niew,
        is_router_nisw=is_router_nisw,
        is_safety_critical=is_safety_critical,
        is_safety_critical_empty=is_safety_critical_empty,
        is_safety_critical_ic=is_safety_critical_ic,
        is_safety_critical_ie=is_safety_critical_ie,
        is_safety_critical_iew=is_safety_critical_iew,
        is_safety_critical_isw=is_safety_critical_isw,
        is_safety_critical_n=is_safety_critical_n,
        is_safety_critical_nic=is_safety_critical_nic,
        is_safety_critical_nie=is_safety_critical_nie,
        is_safety_critical_niew=is_safety_critical_niew,
        is_safety_critical_nisw=is_safety_critical_nisw,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        location=location,
        location_empty=location_empty,
        location_ic=location_ic,
        location_ie=location_ie,
        location_iew=location_iew,
        location_isw=location_isw,
        location_n=location_n,
        location_nic=location_nic,
        location_nie=location_nie,
        location_niew=location_niew,
        location_nisw=location_nisw,
        mac_address=mac_address,
        mac_address_empty=mac_address_empty,
        mac_address_ic=mac_address_ic,
        mac_address_ie=mac_address_ie,
        mac_address_iew=mac_address_iew,
        mac_address_isw=mac_address_isw,
        mac_address_n=mac_address_n,
        mac_address_nic=mac_address_nic,
        mac_address_nie=mac_address_nie,
        mac_address_niew=mac_address_niew,
        mac_address_nisw=mac_address_nisw,
        manufacturer=manufacturer,
        manufacturer_empty=manufacturer_empty,
        manufacturer_ic=manufacturer_ic,
        manufacturer_ie=manufacturer_ie,
        manufacturer_iew=manufacturer_iew,
        manufacturer_isw=manufacturer_isw,
        manufacturer_n=manufacturer_n,
        manufacturer_nic=manufacturer_nic,
        manufacturer_nie=manufacturer_nie,
        manufacturer_niew=manufacturer_niew,
        manufacturer_nisw=manufacturer_nisw,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        oui=oui,
        oui_empty=oui_empty,
        oui_ic=oui_ic,
        oui_ie=oui_ie,
        oui_iew=oui_iew,
        oui_isw=oui_isw,
        oui_n=oui_n,
        oui_nic=oui_nic,
        oui_nie=oui_nie,
        oui_niew=oui_niew,
        oui_nisw=oui_nisw,
        part_number=part_number,
        part_number_empty=part_number_empty,
        part_number_ic=part_number_ic,
        part_number_ie=part_number_ie,
        part_number_iew=part_number_iew,
        part_number_isw=part_number_isw,
        part_number_n=part_number_n,
        part_number_nic=part_number_nic,
        part_number_nie=part_number_nie,
        part_number_niew=part_number_niew,
        part_number_nisw=part_number_nisw,
        port=port,
        port_empty=port_empty,
        port_ic=port_ic,
        port_ie=port_ie,
        port_iew=port_iew,
        port_isw=port_isw,
        port_n=port_n,
        port_nic=port_nic,
        port_nie=port_nie,
        port_niew=port_niew,
        port_nisw=port_nisw,
        predicted_device=predicted_device,
        predicted_device_n=predicted_device_n,
        q=q,
        rack=rack,
        rack_empty=rack_empty,
        rack_ic=rack_ic,
        rack_ie=rack_ie,
        rack_iew=rack_iew,
        rack_isw=rack_isw,
        rack_n=rack_n,
        rack_nic=rack_nic,
        rack_nie=rack_nie,
        rack_niew=rack_niew,
        rack_nisw=rack_nisw,
        serial_number=serial_number,
        serial_number_empty=serial_number_empty,
        serial_number_ic=serial_number_ic,
        serial_number_ie=serial_number_ie,
        serial_number_iew=serial_number_iew,
        serial_number_isw=serial_number_isw,
        serial_number_n=serial_number_n,
        serial_number_nic=serial_number_nic,
        serial_number_nie=serial_number_nie,
        serial_number_niew=serial_number_niew,
        serial_number_nisw=serial_number_nisw,
        site=site,
        site_empty=site_empty,
        site_ic=site_ic,
        site_ie=site_ie,
        site_iew=site_iew,
        site_isw=site_isw,
        site_n=site_n,
        site_nic=site_nic,
        site_nie=site_nie,
        site_niew=site_niew,
        site_nisw=site_nisw,
        software_name=software_name,
        software_name_empty=software_name_empty,
        software_name_ic=software_name_ic,
        software_name_ie=software_name_ie,
        software_name_iew=software_name_iew,
        software_name_isw=software_name_isw,
        software_name_n=software_name_n,
        software_name_nic=software_name_nic,
        software_name_nie=software_name_nie,
        software_name_niew=software_name_niew,
        software_name_nisw=software_name_nisw,
        source=source,
        source_empty=source_empty,
        source_ic=source_ic,
        source_ie=source_ie,
        source_iew=source_iew,
        source_isw=source_isw,
        source_n=source_n,
        source_nic=source_nic,
        source_nie=source_nie,
        source_niew=source_niew,
        source_nisw=source_nisw,
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
    confidence: Union[Unset, list[float]] = UNSET,
    confidence_empty: Union[Unset, bool] = UNSET,
    confidence_gt: Union[Unset, list[float]] = UNSET,
    confidence_gte: Union[Unset, list[float]] = UNSET,
    confidence_lt: Union[Unset, list[float]] = UNSET,
    confidence_lte: Union[Unset, list[float]] = UNSET,
    confidence_n: Union[Unset, list[float]] = UNSET,
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
    device: Union[Unset, int] = UNSET,
    device_n: Union[Unset, int] = UNSET,
    device_family: Union[Unset, list[str]] = UNSET,
    device_family_empty: Union[Unset, bool] = UNSET,
    device_family_ic: Union[Unset, list[str]] = UNSET,
    device_family_ie: Union[Unset, list[str]] = UNSET,
    device_family_iew: Union[Unset, list[str]] = UNSET,
    device_family_isw: Union[Unset, list[str]] = UNSET,
    device_family_n: Union[Unset, list[str]] = UNSET,
    device_family_nic: Union[Unset, list[str]] = UNSET,
    device_family_nie: Union[Unset, list[str]] = UNSET,
    device_family_niew: Union[Unset, list[str]] = UNSET,
    device_family_nisw: Union[Unset, list[str]] = UNSET,
    device_name: Union[Unset, list[str]] = UNSET,
    device_name_empty: Union[Unset, bool] = UNSET,
    device_name_ic: Union[Unset, list[str]] = UNSET,
    device_name_ie: Union[Unset, list[str]] = UNSET,
    device_name_iew: Union[Unset, list[str]] = UNSET,
    device_name_isw: Union[Unset, list[str]] = UNSET,
    device_name_n: Union[Unset, list[str]] = UNSET,
    device_name_nic: Union[Unset, list[str]] = UNSET,
    device_name_nie: Union[Unset, list[str]] = UNSET,
    device_name_niew: Union[Unset, list[str]] = UNSET,
    device_name_nisw: Union[Unset, list[str]] = UNSET,
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_empty: Union[Unset, bool] = UNSET,
    device_role_ic: Union[Unset, list[str]] = UNSET,
    device_role_ie: Union[Unset, list[str]] = UNSET,
    device_role_iew: Union[Unset, list[str]] = UNSET,
    device_role_isw: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_nic: Union[Unset, list[str]] = UNSET,
    device_role_nie: Union[Unset, list[str]] = UNSET,
    device_role_niew: Union[Unset, list[str]] = UNSET,
    device_role_nisw: Union[Unset, list[str]] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_empty: Union[Unset, bool] = UNSET,
    device_type_ic: Union[Unset, list[str]] = UNSET,
    device_type_ie: Union[Unset, list[str]] = UNSET,
    device_type_iew: Union[Unset, list[str]] = UNSET,
    device_type_isw: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_nic: Union[Unset, list[str]] = UNSET,
    device_type_nie: Union[Unset, list[str]] = UNSET,
    device_type_niew: Union[Unset, list[str]] = UNSET,
    device_type_nisw: Union[Unset, list[str]] = UNSET,
    exposure: Union[Unset, list[str]] = UNSET,
    exposure_empty: Union[Unset, bool] = UNSET,
    exposure_ic: Union[Unset, list[str]] = UNSET,
    exposure_ie: Union[Unset, list[str]] = UNSET,
    exposure_iew: Union[Unset, list[str]] = UNSET,
    exposure_isw: Union[Unset, list[str]] = UNSET,
    exposure_n: Union[Unset, list[str]] = UNSET,
    exposure_nic: Union[Unset, list[str]] = UNSET,
    exposure_nie: Union[Unset, list[str]] = UNSET,
    exposure_niew: Union[Unset, list[str]] = UNSET,
    exposure_nisw: Union[Unset, list[str]] = UNSET,
    hardware_cpe: Union[Unset, list[str]] = UNSET,
    hardware_cpe_empty: Union[Unset, bool] = UNSET,
    hardware_cpe_ic: Union[Unset, list[str]] = UNSET,
    hardware_cpe_ie: Union[Unset, list[str]] = UNSET,
    hardware_cpe_iew: Union[Unset, list[str]] = UNSET,
    hardware_cpe_isw: Union[Unset, list[str]] = UNSET,
    hardware_cpe_n: Union[Unset, list[str]] = UNSET,
    hardware_cpe_nic: Union[Unset, list[str]] = UNSET,
    hardware_cpe_nie: Union[Unset, list[str]] = UNSET,
    hardware_cpe_niew: Union[Unset, list[str]] = UNSET,
    hardware_cpe_nisw: Union[Unset, list[str]] = UNSET,
    hardware_version: Union[Unset, list[str]] = UNSET,
    hardware_version_empty: Union[Unset, bool] = UNSET,
    hardware_version_ic: Union[Unset, list[str]] = UNSET,
    hardware_version_ie: Union[Unset, list[str]] = UNSET,
    hardware_version_iew: Union[Unset, list[str]] = UNSET,
    hardware_version_isw: Union[Unset, list[str]] = UNSET,
    hardware_version_n: Union[Unset, list[str]] = UNSET,
    hardware_version_nic: Union[Unset, list[str]] = UNSET,
    hardware_version_nie: Union[Unset, list[str]] = UNSET,
    hardware_version_niew: Union[Unset, list[str]] = UNSET,
    hardware_version_nisw: Union[Unset, list[str]] = UNSET,
    has_predicted_device: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    ip_address: Union[Unset, list[str]] = UNSET,
    ip_address_empty: Union[Unset, bool] = UNSET,
    ip_address_ic: Union[Unset, list[str]] = UNSET,
    ip_address_ie: Union[Unset, list[str]] = UNSET,
    ip_address_iew: Union[Unset, list[str]] = UNSET,
    ip_address_isw: Union[Unset, list[str]] = UNSET,
    ip_address_n: Union[Unset, list[str]] = UNSET,
    ip_address_nic: Union[Unset, list[str]] = UNSET,
    ip_address_nie: Union[Unset, list[str]] = UNSET,
    ip_address_niew: Union[Unset, list[str]] = UNSET,
    ip_address_nisw: Union[Unset, list[str]] = UNSET,
    is_firmware: Union[Unset, list[str]] = UNSET,
    is_firmware_empty: Union[Unset, bool] = UNSET,
    is_firmware_ic: Union[Unset, list[str]] = UNSET,
    is_firmware_ie: Union[Unset, list[str]] = UNSET,
    is_firmware_iew: Union[Unset, list[str]] = UNSET,
    is_firmware_isw: Union[Unset, list[str]] = UNSET,
    is_firmware_n: Union[Unset, list[str]] = UNSET,
    is_firmware_nic: Union[Unset, list[str]] = UNSET,
    is_firmware_nie: Union[Unset, list[str]] = UNSET,
    is_firmware_niew: Union[Unset, list[str]] = UNSET,
    is_firmware_nisw: Union[Unset, list[str]] = UNSET,
    is_router: Union[Unset, list[str]] = UNSET,
    is_router_empty: Union[Unset, bool] = UNSET,
    is_router_ic: Union[Unset, list[str]] = UNSET,
    is_router_ie: Union[Unset, list[str]] = UNSET,
    is_router_iew: Union[Unset, list[str]] = UNSET,
    is_router_isw: Union[Unset, list[str]] = UNSET,
    is_router_n: Union[Unset, list[str]] = UNSET,
    is_router_nic: Union[Unset, list[str]] = UNSET,
    is_router_nie: Union[Unset, list[str]] = UNSET,
    is_router_niew: Union[Unset, list[str]] = UNSET,
    is_router_nisw: Union[Unset, list[str]] = UNSET,
    is_safety_critical: Union[Unset, list[str]] = UNSET,
    is_safety_critical_empty: Union[Unset, bool] = UNSET,
    is_safety_critical_ic: Union[Unset, list[str]] = UNSET,
    is_safety_critical_ie: Union[Unset, list[str]] = UNSET,
    is_safety_critical_iew: Union[Unset, list[str]] = UNSET,
    is_safety_critical_isw: Union[Unset, list[str]] = UNSET,
    is_safety_critical_n: Union[Unset, list[str]] = UNSET,
    is_safety_critical_nic: Union[Unset, list[str]] = UNSET,
    is_safety_critical_nie: Union[Unset, list[str]] = UNSET,
    is_safety_critical_niew: Union[Unset, list[str]] = UNSET,
    is_safety_critical_nisw: Union[Unset, list[str]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_empty: Union[Unset, bool] = UNSET,
    location_ic: Union[Unset, list[str]] = UNSET,
    location_ie: Union[Unset, list[str]] = UNSET,
    location_iew: Union[Unset, list[str]] = UNSET,
    location_isw: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_nic: Union[Unset, list[str]] = UNSET,
    location_nie: Union[Unset, list[str]] = UNSET,
    location_niew: Union[Unset, list[str]] = UNSET,
    location_nisw: Union[Unset, list[str]] = UNSET,
    mac_address: Union[Unset, list[str]] = UNSET,
    mac_address_empty: Union[Unset, bool] = UNSET,
    mac_address_ic: Union[Unset, list[str]] = UNSET,
    mac_address_ie: Union[Unset, list[str]] = UNSET,
    mac_address_iew: Union[Unset, list[str]] = UNSET,
    mac_address_isw: Union[Unset, list[str]] = UNSET,
    mac_address_n: Union[Unset, list[str]] = UNSET,
    mac_address_nic: Union[Unset, list[str]] = UNSET,
    mac_address_nie: Union[Unset, list[str]] = UNSET,
    mac_address_niew: Union[Unset, list[str]] = UNSET,
    mac_address_nisw: Union[Unset, list[str]] = UNSET,
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_empty: Union[Unset, bool] = UNSET,
    manufacturer_ic: Union[Unset, list[str]] = UNSET,
    manufacturer_ie: Union[Unset, list[str]] = UNSET,
    manufacturer_iew: Union[Unset, list[str]] = UNSET,
    manufacturer_isw: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_nic: Union[Unset, list[str]] = UNSET,
    manufacturer_nie: Union[Unset, list[str]] = UNSET,
    manufacturer_niew: Union[Unset, list[str]] = UNSET,
    manufacturer_nisw: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    oui: Union[Unset, list[str]] = UNSET,
    oui_empty: Union[Unset, bool] = UNSET,
    oui_ic: Union[Unset, list[str]] = UNSET,
    oui_ie: Union[Unset, list[str]] = UNSET,
    oui_iew: Union[Unset, list[str]] = UNSET,
    oui_isw: Union[Unset, list[str]] = UNSET,
    oui_n: Union[Unset, list[str]] = UNSET,
    oui_nic: Union[Unset, list[str]] = UNSET,
    oui_nie: Union[Unset, list[str]] = UNSET,
    oui_niew: Union[Unset, list[str]] = UNSET,
    oui_nisw: Union[Unset, list[str]] = UNSET,
    part_number: Union[Unset, list[str]] = UNSET,
    part_number_empty: Union[Unset, bool] = UNSET,
    part_number_ic: Union[Unset, list[str]] = UNSET,
    part_number_ie: Union[Unset, list[str]] = UNSET,
    part_number_iew: Union[Unset, list[str]] = UNSET,
    part_number_isw: Union[Unset, list[str]] = UNSET,
    part_number_n: Union[Unset, list[str]] = UNSET,
    part_number_nic: Union[Unset, list[str]] = UNSET,
    part_number_nie: Union[Unset, list[str]] = UNSET,
    part_number_niew: Union[Unset, list[str]] = UNSET,
    part_number_nisw: Union[Unset, list[str]] = UNSET,
    port: Union[Unset, list[str]] = UNSET,
    port_empty: Union[Unset, bool] = UNSET,
    port_ic: Union[Unset, list[str]] = UNSET,
    port_ie: Union[Unset, list[str]] = UNSET,
    port_iew: Union[Unset, list[str]] = UNSET,
    port_isw: Union[Unset, list[str]] = UNSET,
    port_n: Union[Unset, list[str]] = UNSET,
    port_nic: Union[Unset, list[str]] = UNSET,
    port_nie: Union[Unset, list[str]] = UNSET,
    port_niew: Union[Unset, list[str]] = UNSET,
    port_nisw: Union[Unset, list[str]] = UNSET,
    predicted_device: Union[Unset, int] = UNSET,
    predicted_device_n: Union[Unset, int] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_empty: Union[Unset, bool] = UNSET,
    rack_ic: Union[Unset, list[str]] = UNSET,
    rack_ie: Union[Unset, list[str]] = UNSET,
    rack_iew: Union[Unset, list[str]] = UNSET,
    rack_isw: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
    rack_nic: Union[Unset, list[str]] = UNSET,
    rack_nie: Union[Unset, list[str]] = UNSET,
    rack_niew: Union[Unset, list[str]] = UNSET,
    rack_nisw: Union[Unset, list[str]] = UNSET,
    serial_number: Union[Unset, list[str]] = UNSET,
    serial_number_empty: Union[Unset, bool] = UNSET,
    serial_number_ic: Union[Unset, list[str]] = UNSET,
    serial_number_ie: Union[Unset, list[str]] = UNSET,
    serial_number_iew: Union[Unset, list[str]] = UNSET,
    serial_number_isw: Union[Unset, list[str]] = UNSET,
    serial_number_n: Union[Unset, list[str]] = UNSET,
    serial_number_nic: Union[Unset, list[str]] = UNSET,
    serial_number_nie: Union[Unset, list[str]] = UNSET,
    serial_number_niew: Union[Unset, list[str]] = UNSET,
    serial_number_nisw: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_empty: Union[Unset, bool] = UNSET,
    site_ic: Union[Unset, list[str]] = UNSET,
    site_ie: Union[Unset, list[str]] = UNSET,
    site_iew: Union[Unset, list[str]] = UNSET,
    site_isw: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_nic: Union[Unset, list[str]] = UNSET,
    site_nie: Union[Unset, list[str]] = UNSET,
    site_niew: Union[Unset, list[str]] = UNSET,
    site_nisw: Union[Unset, list[str]] = UNSET,
    software_name: Union[Unset, list[str]] = UNSET,
    software_name_empty: Union[Unset, bool] = UNSET,
    software_name_ic: Union[Unset, list[str]] = UNSET,
    software_name_ie: Union[Unset, list[str]] = UNSET,
    software_name_iew: Union[Unset, list[str]] = UNSET,
    software_name_isw: Union[Unset, list[str]] = UNSET,
    software_name_n: Union[Unset, list[str]] = UNSET,
    software_name_nic: Union[Unset, list[str]] = UNSET,
    software_name_nie: Union[Unset, list[str]] = UNSET,
    software_name_niew: Union[Unset, list[str]] = UNSET,
    software_name_nisw: Union[Unset, list[str]] = UNSET,
    source: Union[Unset, list[str]] = UNSET,
    source_empty: Union[Unset, bool] = UNSET,
    source_ic: Union[Unset, list[str]] = UNSET,
    source_ie: Union[Unset, list[str]] = UNSET,
    source_iew: Union[Unset, list[str]] = UNSET,
    source_isw: Union[Unset, list[str]] = UNSET,
    source_n: Union[Unset, list[str]] = UNSET,
    source_nic: Union[Unset, list[str]] = UNSET,
    source_nie: Union[Unset, list[str]] = UNSET,
    source_niew: Union[Unset, list[str]] = UNSET,
    source_nisw: Union[Unset, list[str]] = UNSET,
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
) -> Response[PaginatedDeviceFindingList]:
    """ViewSet for DeviceFinding.

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
        confidence (Union[Unset, list[float]]):
        confidence_empty (Union[Unset, bool]):
        confidence_gt (Union[Unset, list[float]]):
        confidence_gte (Union[Unset, list[float]]):
        confidence_lt (Union[Unset, list[float]]):
        confidence_lte (Union[Unset, list[float]]):
        confidence_n (Union[Unset, list[float]]):
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
        device (Union[Unset, int]):
        device_n (Union[Unset, int]):
        device_family (Union[Unset, list[str]]):
        device_family_empty (Union[Unset, bool]):
        device_family_ic (Union[Unset, list[str]]):
        device_family_ie (Union[Unset, list[str]]):
        device_family_iew (Union[Unset, list[str]]):
        device_family_isw (Union[Unset, list[str]]):
        device_family_n (Union[Unset, list[str]]):
        device_family_nic (Union[Unset, list[str]]):
        device_family_nie (Union[Unset, list[str]]):
        device_family_niew (Union[Unset, list[str]]):
        device_family_nisw (Union[Unset, list[str]]):
        device_name (Union[Unset, list[str]]):
        device_name_empty (Union[Unset, bool]):
        device_name_ic (Union[Unset, list[str]]):
        device_name_ie (Union[Unset, list[str]]):
        device_name_iew (Union[Unset, list[str]]):
        device_name_isw (Union[Unset, list[str]]):
        device_name_n (Union[Unset, list[str]]):
        device_name_nic (Union[Unset, list[str]]):
        device_name_nie (Union[Unset, list[str]]):
        device_name_niew (Union[Unset, list[str]]):
        device_name_nisw (Union[Unset, list[str]]):
        device_role (Union[Unset, list[str]]):
        device_role_empty (Union[Unset, bool]):
        device_role_ic (Union[Unset, list[str]]):
        device_role_ie (Union[Unset, list[str]]):
        device_role_iew (Union[Unset, list[str]]):
        device_role_isw (Union[Unset, list[str]]):
        device_role_n (Union[Unset, list[str]]):
        device_role_nic (Union[Unset, list[str]]):
        device_role_nie (Union[Unset, list[str]]):
        device_role_niew (Union[Unset, list[str]]):
        device_role_nisw (Union[Unset, list[str]]):
        device_type (Union[Unset, list[str]]):
        device_type_empty (Union[Unset, bool]):
        device_type_ic (Union[Unset, list[str]]):
        device_type_ie (Union[Unset, list[str]]):
        device_type_iew (Union[Unset, list[str]]):
        device_type_isw (Union[Unset, list[str]]):
        device_type_n (Union[Unset, list[str]]):
        device_type_nic (Union[Unset, list[str]]):
        device_type_nie (Union[Unset, list[str]]):
        device_type_niew (Union[Unset, list[str]]):
        device_type_nisw (Union[Unset, list[str]]):
        exposure (Union[Unset, list[str]]):
        exposure_empty (Union[Unset, bool]):
        exposure_ic (Union[Unset, list[str]]):
        exposure_ie (Union[Unset, list[str]]):
        exposure_iew (Union[Unset, list[str]]):
        exposure_isw (Union[Unset, list[str]]):
        exposure_n (Union[Unset, list[str]]):
        exposure_nic (Union[Unset, list[str]]):
        exposure_nie (Union[Unset, list[str]]):
        exposure_niew (Union[Unset, list[str]]):
        exposure_nisw (Union[Unset, list[str]]):
        hardware_cpe (Union[Unset, list[str]]):
        hardware_cpe_empty (Union[Unset, bool]):
        hardware_cpe_ic (Union[Unset, list[str]]):
        hardware_cpe_ie (Union[Unset, list[str]]):
        hardware_cpe_iew (Union[Unset, list[str]]):
        hardware_cpe_isw (Union[Unset, list[str]]):
        hardware_cpe_n (Union[Unset, list[str]]):
        hardware_cpe_nic (Union[Unset, list[str]]):
        hardware_cpe_nie (Union[Unset, list[str]]):
        hardware_cpe_niew (Union[Unset, list[str]]):
        hardware_cpe_nisw (Union[Unset, list[str]]):
        hardware_version (Union[Unset, list[str]]):
        hardware_version_empty (Union[Unset, bool]):
        hardware_version_ic (Union[Unset, list[str]]):
        hardware_version_ie (Union[Unset, list[str]]):
        hardware_version_iew (Union[Unset, list[str]]):
        hardware_version_isw (Union[Unset, list[str]]):
        hardware_version_n (Union[Unset, list[str]]):
        hardware_version_nic (Union[Unset, list[str]]):
        hardware_version_nie (Union[Unset, list[str]]):
        hardware_version_niew (Union[Unset, list[str]]):
        hardware_version_nisw (Union[Unset, list[str]]):
        has_predicted_device (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        ip_address (Union[Unset, list[str]]):
        ip_address_empty (Union[Unset, bool]):
        ip_address_ic (Union[Unset, list[str]]):
        ip_address_ie (Union[Unset, list[str]]):
        ip_address_iew (Union[Unset, list[str]]):
        ip_address_isw (Union[Unset, list[str]]):
        ip_address_n (Union[Unset, list[str]]):
        ip_address_nic (Union[Unset, list[str]]):
        ip_address_nie (Union[Unset, list[str]]):
        ip_address_niew (Union[Unset, list[str]]):
        ip_address_nisw (Union[Unset, list[str]]):
        is_firmware (Union[Unset, list[str]]):
        is_firmware_empty (Union[Unset, bool]):
        is_firmware_ic (Union[Unset, list[str]]):
        is_firmware_ie (Union[Unset, list[str]]):
        is_firmware_iew (Union[Unset, list[str]]):
        is_firmware_isw (Union[Unset, list[str]]):
        is_firmware_n (Union[Unset, list[str]]):
        is_firmware_nic (Union[Unset, list[str]]):
        is_firmware_nie (Union[Unset, list[str]]):
        is_firmware_niew (Union[Unset, list[str]]):
        is_firmware_nisw (Union[Unset, list[str]]):
        is_router (Union[Unset, list[str]]):
        is_router_empty (Union[Unset, bool]):
        is_router_ic (Union[Unset, list[str]]):
        is_router_ie (Union[Unset, list[str]]):
        is_router_iew (Union[Unset, list[str]]):
        is_router_isw (Union[Unset, list[str]]):
        is_router_n (Union[Unset, list[str]]):
        is_router_nic (Union[Unset, list[str]]):
        is_router_nie (Union[Unset, list[str]]):
        is_router_niew (Union[Unset, list[str]]):
        is_router_nisw (Union[Unset, list[str]]):
        is_safety_critical (Union[Unset, list[str]]):
        is_safety_critical_empty (Union[Unset, bool]):
        is_safety_critical_ic (Union[Unset, list[str]]):
        is_safety_critical_ie (Union[Unset, list[str]]):
        is_safety_critical_iew (Union[Unset, list[str]]):
        is_safety_critical_isw (Union[Unset, list[str]]):
        is_safety_critical_n (Union[Unset, list[str]]):
        is_safety_critical_nic (Union[Unset, list[str]]):
        is_safety_critical_nie (Union[Unset, list[str]]):
        is_safety_critical_niew (Union[Unset, list[str]]):
        is_safety_critical_nisw (Union[Unset, list[str]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_empty (Union[Unset, bool]):
        location_ic (Union[Unset, list[str]]):
        location_ie (Union[Unset, list[str]]):
        location_iew (Union[Unset, list[str]]):
        location_isw (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_nic (Union[Unset, list[str]]):
        location_nie (Union[Unset, list[str]]):
        location_niew (Union[Unset, list[str]]):
        location_nisw (Union[Unset, list[str]]):
        mac_address (Union[Unset, list[str]]):
        mac_address_empty (Union[Unset, bool]):
        mac_address_ic (Union[Unset, list[str]]):
        mac_address_ie (Union[Unset, list[str]]):
        mac_address_iew (Union[Unset, list[str]]):
        mac_address_isw (Union[Unset, list[str]]):
        mac_address_n (Union[Unset, list[str]]):
        mac_address_nic (Union[Unset, list[str]]):
        mac_address_nie (Union[Unset, list[str]]):
        mac_address_niew (Union[Unset, list[str]]):
        mac_address_nisw (Union[Unset, list[str]]):
        manufacturer (Union[Unset, list[str]]):
        manufacturer_empty (Union[Unset, bool]):
        manufacturer_ic (Union[Unset, list[str]]):
        manufacturer_ie (Union[Unset, list[str]]):
        manufacturer_iew (Union[Unset, list[str]]):
        manufacturer_isw (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_nic (Union[Unset, list[str]]):
        manufacturer_nie (Union[Unset, list[str]]):
        manufacturer_niew (Union[Unset, list[str]]):
        manufacturer_nisw (Union[Unset, list[str]]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        oui (Union[Unset, list[str]]):
        oui_empty (Union[Unset, bool]):
        oui_ic (Union[Unset, list[str]]):
        oui_ie (Union[Unset, list[str]]):
        oui_iew (Union[Unset, list[str]]):
        oui_isw (Union[Unset, list[str]]):
        oui_n (Union[Unset, list[str]]):
        oui_nic (Union[Unset, list[str]]):
        oui_nie (Union[Unset, list[str]]):
        oui_niew (Union[Unset, list[str]]):
        oui_nisw (Union[Unset, list[str]]):
        part_number (Union[Unset, list[str]]):
        part_number_empty (Union[Unset, bool]):
        part_number_ic (Union[Unset, list[str]]):
        part_number_ie (Union[Unset, list[str]]):
        part_number_iew (Union[Unset, list[str]]):
        part_number_isw (Union[Unset, list[str]]):
        part_number_n (Union[Unset, list[str]]):
        part_number_nic (Union[Unset, list[str]]):
        part_number_nie (Union[Unset, list[str]]):
        part_number_niew (Union[Unset, list[str]]):
        part_number_nisw (Union[Unset, list[str]]):
        port (Union[Unset, list[str]]):
        port_empty (Union[Unset, bool]):
        port_ic (Union[Unset, list[str]]):
        port_ie (Union[Unset, list[str]]):
        port_iew (Union[Unset, list[str]]):
        port_isw (Union[Unset, list[str]]):
        port_n (Union[Unset, list[str]]):
        port_nic (Union[Unset, list[str]]):
        port_nie (Union[Unset, list[str]]):
        port_niew (Union[Unset, list[str]]):
        port_nisw (Union[Unset, list[str]]):
        predicted_device (Union[Unset, int]):
        predicted_device_n (Union[Unset, int]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_empty (Union[Unset, bool]):
        rack_ic (Union[Unset, list[str]]):
        rack_ie (Union[Unset, list[str]]):
        rack_iew (Union[Unset, list[str]]):
        rack_isw (Union[Unset, list[str]]):
        rack_n (Union[Unset, list[str]]):
        rack_nic (Union[Unset, list[str]]):
        rack_nie (Union[Unset, list[str]]):
        rack_niew (Union[Unset, list[str]]):
        rack_nisw (Union[Unset, list[str]]):
        serial_number (Union[Unset, list[str]]):
        serial_number_empty (Union[Unset, bool]):
        serial_number_ic (Union[Unset, list[str]]):
        serial_number_ie (Union[Unset, list[str]]):
        serial_number_iew (Union[Unset, list[str]]):
        serial_number_isw (Union[Unset, list[str]]):
        serial_number_n (Union[Unset, list[str]]):
        serial_number_nic (Union[Unset, list[str]]):
        serial_number_nie (Union[Unset, list[str]]):
        serial_number_niew (Union[Unset, list[str]]):
        serial_number_nisw (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_empty (Union[Unset, bool]):
        site_ic (Union[Unset, list[str]]):
        site_ie (Union[Unset, list[str]]):
        site_iew (Union[Unset, list[str]]):
        site_isw (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_nic (Union[Unset, list[str]]):
        site_nie (Union[Unset, list[str]]):
        site_niew (Union[Unset, list[str]]):
        site_nisw (Union[Unset, list[str]]):
        software_name (Union[Unset, list[str]]):
        software_name_empty (Union[Unset, bool]):
        software_name_ic (Union[Unset, list[str]]):
        software_name_ie (Union[Unset, list[str]]):
        software_name_iew (Union[Unset, list[str]]):
        software_name_isw (Union[Unset, list[str]]):
        software_name_n (Union[Unset, list[str]]):
        software_name_nic (Union[Unset, list[str]]):
        software_name_nie (Union[Unset, list[str]]):
        software_name_niew (Union[Unset, list[str]]):
        software_name_nisw (Union[Unset, list[str]]):
        source (Union[Unset, list[str]]):
        source_empty (Union[Unset, bool]):
        source_ic (Union[Unset, list[str]]):
        source_ie (Union[Unset, list[str]]):
        source_iew (Union[Unset, list[str]]):
        source_isw (Union[Unset, list[str]]):
        source_n (Union[Unset, list[str]]):
        source_nic (Union[Unset, list[str]]):
        source_nie (Union[Unset, list[str]]):
        source_niew (Union[Unset, list[str]]):
        source_nisw (Union[Unset, list[str]]):
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
        Response[PaginatedDeviceFindingList]
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
        confidence=confidence,
        confidence_empty=confidence_empty,
        confidence_gt=confidence_gt,
        confidence_gte=confidence_gte,
        confidence_lt=confidence_lt,
        confidence_lte=confidence_lte,
        confidence_n=confidence_n,
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
        device_family=device_family,
        device_family_empty=device_family_empty,
        device_family_ic=device_family_ic,
        device_family_ie=device_family_ie,
        device_family_iew=device_family_iew,
        device_family_isw=device_family_isw,
        device_family_n=device_family_n,
        device_family_nic=device_family_nic,
        device_family_nie=device_family_nie,
        device_family_niew=device_family_niew,
        device_family_nisw=device_family_nisw,
        device_name=device_name,
        device_name_empty=device_name_empty,
        device_name_ic=device_name_ic,
        device_name_ie=device_name_ie,
        device_name_iew=device_name_iew,
        device_name_isw=device_name_isw,
        device_name_n=device_name_n,
        device_name_nic=device_name_nic,
        device_name_nie=device_name_nie,
        device_name_niew=device_name_niew,
        device_name_nisw=device_name_nisw,
        device_role=device_role,
        device_role_empty=device_role_empty,
        device_role_ic=device_role_ic,
        device_role_ie=device_role_ie,
        device_role_iew=device_role_iew,
        device_role_isw=device_role_isw,
        device_role_n=device_role_n,
        device_role_nic=device_role_nic,
        device_role_nie=device_role_nie,
        device_role_niew=device_role_niew,
        device_role_nisw=device_role_nisw,
        device_type=device_type,
        device_type_empty=device_type_empty,
        device_type_ic=device_type_ic,
        device_type_ie=device_type_ie,
        device_type_iew=device_type_iew,
        device_type_isw=device_type_isw,
        device_type_n=device_type_n,
        device_type_nic=device_type_nic,
        device_type_nie=device_type_nie,
        device_type_niew=device_type_niew,
        device_type_nisw=device_type_nisw,
        exposure=exposure,
        exposure_empty=exposure_empty,
        exposure_ic=exposure_ic,
        exposure_ie=exposure_ie,
        exposure_iew=exposure_iew,
        exposure_isw=exposure_isw,
        exposure_n=exposure_n,
        exposure_nic=exposure_nic,
        exposure_nie=exposure_nie,
        exposure_niew=exposure_niew,
        exposure_nisw=exposure_nisw,
        hardware_cpe=hardware_cpe,
        hardware_cpe_empty=hardware_cpe_empty,
        hardware_cpe_ic=hardware_cpe_ic,
        hardware_cpe_ie=hardware_cpe_ie,
        hardware_cpe_iew=hardware_cpe_iew,
        hardware_cpe_isw=hardware_cpe_isw,
        hardware_cpe_n=hardware_cpe_n,
        hardware_cpe_nic=hardware_cpe_nic,
        hardware_cpe_nie=hardware_cpe_nie,
        hardware_cpe_niew=hardware_cpe_niew,
        hardware_cpe_nisw=hardware_cpe_nisw,
        hardware_version=hardware_version,
        hardware_version_empty=hardware_version_empty,
        hardware_version_ic=hardware_version_ic,
        hardware_version_ie=hardware_version_ie,
        hardware_version_iew=hardware_version_iew,
        hardware_version_isw=hardware_version_isw,
        hardware_version_n=hardware_version_n,
        hardware_version_nic=hardware_version_nic,
        hardware_version_nie=hardware_version_nie,
        hardware_version_niew=hardware_version_niew,
        hardware_version_nisw=hardware_version_nisw,
        has_predicted_device=has_predicted_device,
        id=id,
        id_empty=id_empty,
        id_gt=id_gt,
        id_gte=id_gte,
        id_lt=id_lt,
        id_lte=id_lte,
        id_n=id_n,
        ip_address=ip_address,
        ip_address_empty=ip_address_empty,
        ip_address_ic=ip_address_ic,
        ip_address_ie=ip_address_ie,
        ip_address_iew=ip_address_iew,
        ip_address_isw=ip_address_isw,
        ip_address_n=ip_address_n,
        ip_address_nic=ip_address_nic,
        ip_address_nie=ip_address_nie,
        ip_address_niew=ip_address_niew,
        ip_address_nisw=ip_address_nisw,
        is_firmware=is_firmware,
        is_firmware_empty=is_firmware_empty,
        is_firmware_ic=is_firmware_ic,
        is_firmware_ie=is_firmware_ie,
        is_firmware_iew=is_firmware_iew,
        is_firmware_isw=is_firmware_isw,
        is_firmware_n=is_firmware_n,
        is_firmware_nic=is_firmware_nic,
        is_firmware_nie=is_firmware_nie,
        is_firmware_niew=is_firmware_niew,
        is_firmware_nisw=is_firmware_nisw,
        is_router=is_router,
        is_router_empty=is_router_empty,
        is_router_ic=is_router_ic,
        is_router_ie=is_router_ie,
        is_router_iew=is_router_iew,
        is_router_isw=is_router_isw,
        is_router_n=is_router_n,
        is_router_nic=is_router_nic,
        is_router_nie=is_router_nie,
        is_router_niew=is_router_niew,
        is_router_nisw=is_router_nisw,
        is_safety_critical=is_safety_critical,
        is_safety_critical_empty=is_safety_critical_empty,
        is_safety_critical_ic=is_safety_critical_ic,
        is_safety_critical_ie=is_safety_critical_ie,
        is_safety_critical_iew=is_safety_critical_iew,
        is_safety_critical_isw=is_safety_critical_isw,
        is_safety_critical_n=is_safety_critical_n,
        is_safety_critical_nic=is_safety_critical_nic,
        is_safety_critical_nie=is_safety_critical_nie,
        is_safety_critical_niew=is_safety_critical_niew,
        is_safety_critical_nisw=is_safety_critical_nisw,
        last_updated=last_updated,
        last_updated_empty=last_updated_empty,
        last_updated_gt=last_updated_gt,
        last_updated_gte=last_updated_gte,
        last_updated_lt=last_updated_lt,
        last_updated_lte=last_updated_lte,
        last_updated_n=last_updated_n,
        limit=limit,
        location=location,
        location_empty=location_empty,
        location_ic=location_ic,
        location_ie=location_ie,
        location_iew=location_iew,
        location_isw=location_isw,
        location_n=location_n,
        location_nic=location_nic,
        location_nie=location_nie,
        location_niew=location_niew,
        location_nisw=location_nisw,
        mac_address=mac_address,
        mac_address_empty=mac_address_empty,
        mac_address_ic=mac_address_ic,
        mac_address_ie=mac_address_ie,
        mac_address_iew=mac_address_iew,
        mac_address_isw=mac_address_isw,
        mac_address_n=mac_address_n,
        mac_address_nic=mac_address_nic,
        mac_address_nie=mac_address_nie,
        mac_address_niew=mac_address_niew,
        mac_address_nisw=mac_address_nisw,
        manufacturer=manufacturer,
        manufacturer_empty=manufacturer_empty,
        manufacturer_ic=manufacturer_ic,
        manufacturer_ie=manufacturer_ie,
        manufacturer_iew=manufacturer_iew,
        manufacturer_isw=manufacturer_isw,
        manufacturer_n=manufacturer_n,
        manufacturer_nic=manufacturer_nic,
        manufacturer_nie=manufacturer_nie,
        manufacturer_niew=manufacturer_niew,
        manufacturer_nisw=manufacturer_nisw,
        modified_by_request=modified_by_request,
        offset=offset,
        ordering=ordering,
        oui=oui,
        oui_empty=oui_empty,
        oui_ic=oui_ic,
        oui_ie=oui_ie,
        oui_iew=oui_iew,
        oui_isw=oui_isw,
        oui_n=oui_n,
        oui_nic=oui_nic,
        oui_nie=oui_nie,
        oui_niew=oui_niew,
        oui_nisw=oui_nisw,
        part_number=part_number,
        part_number_empty=part_number_empty,
        part_number_ic=part_number_ic,
        part_number_ie=part_number_ie,
        part_number_iew=part_number_iew,
        part_number_isw=part_number_isw,
        part_number_n=part_number_n,
        part_number_nic=part_number_nic,
        part_number_nie=part_number_nie,
        part_number_niew=part_number_niew,
        part_number_nisw=part_number_nisw,
        port=port,
        port_empty=port_empty,
        port_ic=port_ic,
        port_ie=port_ie,
        port_iew=port_iew,
        port_isw=port_isw,
        port_n=port_n,
        port_nic=port_nic,
        port_nie=port_nie,
        port_niew=port_niew,
        port_nisw=port_nisw,
        predicted_device=predicted_device,
        predicted_device_n=predicted_device_n,
        q=q,
        rack=rack,
        rack_empty=rack_empty,
        rack_ic=rack_ic,
        rack_ie=rack_ie,
        rack_iew=rack_iew,
        rack_isw=rack_isw,
        rack_n=rack_n,
        rack_nic=rack_nic,
        rack_nie=rack_nie,
        rack_niew=rack_niew,
        rack_nisw=rack_nisw,
        serial_number=serial_number,
        serial_number_empty=serial_number_empty,
        serial_number_ic=serial_number_ic,
        serial_number_ie=serial_number_ie,
        serial_number_iew=serial_number_iew,
        serial_number_isw=serial_number_isw,
        serial_number_n=serial_number_n,
        serial_number_nic=serial_number_nic,
        serial_number_nie=serial_number_nie,
        serial_number_niew=serial_number_niew,
        serial_number_nisw=serial_number_nisw,
        site=site,
        site_empty=site_empty,
        site_ic=site_ic,
        site_ie=site_ie,
        site_iew=site_iew,
        site_isw=site_isw,
        site_n=site_n,
        site_nic=site_nic,
        site_nie=site_nie,
        site_niew=site_niew,
        site_nisw=site_nisw,
        software_name=software_name,
        software_name_empty=software_name_empty,
        software_name_ic=software_name_ic,
        software_name_ie=software_name_ie,
        software_name_iew=software_name_iew,
        software_name_isw=software_name_isw,
        software_name_n=software_name_n,
        software_name_nic=software_name_nic,
        software_name_nie=software_name_nie,
        software_name_niew=software_name_niew,
        software_name_nisw=software_name_nisw,
        source=source,
        source_empty=source_empty,
        source_ic=source_ic,
        source_ie=source_ie,
        source_iew=source_iew,
        source_isw=source_isw,
        source_n=source_n,
        source_nic=source_nic,
        source_nie=source_nie,
        source_niew=source_niew,
        source_nisw=source_nisw,
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
    confidence: Union[Unset, list[float]] = UNSET,
    confidence_empty: Union[Unset, bool] = UNSET,
    confidence_gt: Union[Unset, list[float]] = UNSET,
    confidence_gte: Union[Unset, list[float]] = UNSET,
    confidence_lt: Union[Unset, list[float]] = UNSET,
    confidence_lte: Union[Unset, list[float]] = UNSET,
    confidence_n: Union[Unset, list[float]] = UNSET,
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
    device: Union[Unset, int] = UNSET,
    device_n: Union[Unset, int] = UNSET,
    device_family: Union[Unset, list[str]] = UNSET,
    device_family_empty: Union[Unset, bool] = UNSET,
    device_family_ic: Union[Unset, list[str]] = UNSET,
    device_family_ie: Union[Unset, list[str]] = UNSET,
    device_family_iew: Union[Unset, list[str]] = UNSET,
    device_family_isw: Union[Unset, list[str]] = UNSET,
    device_family_n: Union[Unset, list[str]] = UNSET,
    device_family_nic: Union[Unset, list[str]] = UNSET,
    device_family_nie: Union[Unset, list[str]] = UNSET,
    device_family_niew: Union[Unset, list[str]] = UNSET,
    device_family_nisw: Union[Unset, list[str]] = UNSET,
    device_name: Union[Unset, list[str]] = UNSET,
    device_name_empty: Union[Unset, bool] = UNSET,
    device_name_ic: Union[Unset, list[str]] = UNSET,
    device_name_ie: Union[Unset, list[str]] = UNSET,
    device_name_iew: Union[Unset, list[str]] = UNSET,
    device_name_isw: Union[Unset, list[str]] = UNSET,
    device_name_n: Union[Unset, list[str]] = UNSET,
    device_name_nic: Union[Unset, list[str]] = UNSET,
    device_name_nie: Union[Unset, list[str]] = UNSET,
    device_name_niew: Union[Unset, list[str]] = UNSET,
    device_name_nisw: Union[Unset, list[str]] = UNSET,
    device_role: Union[Unset, list[str]] = UNSET,
    device_role_empty: Union[Unset, bool] = UNSET,
    device_role_ic: Union[Unset, list[str]] = UNSET,
    device_role_ie: Union[Unset, list[str]] = UNSET,
    device_role_iew: Union[Unset, list[str]] = UNSET,
    device_role_isw: Union[Unset, list[str]] = UNSET,
    device_role_n: Union[Unset, list[str]] = UNSET,
    device_role_nic: Union[Unset, list[str]] = UNSET,
    device_role_nie: Union[Unset, list[str]] = UNSET,
    device_role_niew: Union[Unset, list[str]] = UNSET,
    device_role_nisw: Union[Unset, list[str]] = UNSET,
    device_type: Union[Unset, list[str]] = UNSET,
    device_type_empty: Union[Unset, bool] = UNSET,
    device_type_ic: Union[Unset, list[str]] = UNSET,
    device_type_ie: Union[Unset, list[str]] = UNSET,
    device_type_iew: Union[Unset, list[str]] = UNSET,
    device_type_isw: Union[Unset, list[str]] = UNSET,
    device_type_n: Union[Unset, list[str]] = UNSET,
    device_type_nic: Union[Unset, list[str]] = UNSET,
    device_type_nie: Union[Unset, list[str]] = UNSET,
    device_type_niew: Union[Unset, list[str]] = UNSET,
    device_type_nisw: Union[Unset, list[str]] = UNSET,
    exposure: Union[Unset, list[str]] = UNSET,
    exposure_empty: Union[Unset, bool] = UNSET,
    exposure_ic: Union[Unset, list[str]] = UNSET,
    exposure_ie: Union[Unset, list[str]] = UNSET,
    exposure_iew: Union[Unset, list[str]] = UNSET,
    exposure_isw: Union[Unset, list[str]] = UNSET,
    exposure_n: Union[Unset, list[str]] = UNSET,
    exposure_nic: Union[Unset, list[str]] = UNSET,
    exposure_nie: Union[Unset, list[str]] = UNSET,
    exposure_niew: Union[Unset, list[str]] = UNSET,
    exposure_nisw: Union[Unset, list[str]] = UNSET,
    hardware_cpe: Union[Unset, list[str]] = UNSET,
    hardware_cpe_empty: Union[Unset, bool] = UNSET,
    hardware_cpe_ic: Union[Unset, list[str]] = UNSET,
    hardware_cpe_ie: Union[Unset, list[str]] = UNSET,
    hardware_cpe_iew: Union[Unset, list[str]] = UNSET,
    hardware_cpe_isw: Union[Unset, list[str]] = UNSET,
    hardware_cpe_n: Union[Unset, list[str]] = UNSET,
    hardware_cpe_nic: Union[Unset, list[str]] = UNSET,
    hardware_cpe_nie: Union[Unset, list[str]] = UNSET,
    hardware_cpe_niew: Union[Unset, list[str]] = UNSET,
    hardware_cpe_nisw: Union[Unset, list[str]] = UNSET,
    hardware_version: Union[Unset, list[str]] = UNSET,
    hardware_version_empty: Union[Unset, bool] = UNSET,
    hardware_version_ic: Union[Unset, list[str]] = UNSET,
    hardware_version_ie: Union[Unset, list[str]] = UNSET,
    hardware_version_iew: Union[Unset, list[str]] = UNSET,
    hardware_version_isw: Union[Unset, list[str]] = UNSET,
    hardware_version_n: Union[Unset, list[str]] = UNSET,
    hardware_version_nic: Union[Unset, list[str]] = UNSET,
    hardware_version_nie: Union[Unset, list[str]] = UNSET,
    hardware_version_niew: Union[Unset, list[str]] = UNSET,
    hardware_version_nisw: Union[Unset, list[str]] = UNSET,
    has_predicted_device: Union[Unset, bool] = UNSET,
    id: Union[Unset, list[int]] = UNSET,
    id_empty: Union[Unset, bool] = UNSET,
    id_gt: Union[Unset, list[int]] = UNSET,
    id_gte: Union[Unset, list[int]] = UNSET,
    id_lt: Union[Unset, list[int]] = UNSET,
    id_lte: Union[Unset, list[int]] = UNSET,
    id_n: Union[Unset, list[int]] = UNSET,
    ip_address: Union[Unset, list[str]] = UNSET,
    ip_address_empty: Union[Unset, bool] = UNSET,
    ip_address_ic: Union[Unset, list[str]] = UNSET,
    ip_address_ie: Union[Unset, list[str]] = UNSET,
    ip_address_iew: Union[Unset, list[str]] = UNSET,
    ip_address_isw: Union[Unset, list[str]] = UNSET,
    ip_address_n: Union[Unset, list[str]] = UNSET,
    ip_address_nic: Union[Unset, list[str]] = UNSET,
    ip_address_nie: Union[Unset, list[str]] = UNSET,
    ip_address_niew: Union[Unset, list[str]] = UNSET,
    ip_address_nisw: Union[Unset, list[str]] = UNSET,
    is_firmware: Union[Unset, list[str]] = UNSET,
    is_firmware_empty: Union[Unset, bool] = UNSET,
    is_firmware_ic: Union[Unset, list[str]] = UNSET,
    is_firmware_ie: Union[Unset, list[str]] = UNSET,
    is_firmware_iew: Union[Unset, list[str]] = UNSET,
    is_firmware_isw: Union[Unset, list[str]] = UNSET,
    is_firmware_n: Union[Unset, list[str]] = UNSET,
    is_firmware_nic: Union[Unset, list[str]] = UNSET,
    is_firmware_nie: Union[Unset, list[str]] = UNSET,
    is_firmware_niew: Union[Unset, list[str]] = UNSET,
    is_firmware_nisw: Union[Unset, list[str]] = UNSET,
    is_router: Union[Unset, list[str]] = UNSET,
    is_router_empty: Union[Unset, bool] = UNSET,
    is_router_ic: Union[Unset, list[str]] = UNSET,
    is_router_ie: Union[Unset, list[str]] = UNSET,
    is_router_iew: Union[Unset, list[str]] = UNSET,
    is_router_isw: Union[Unset, list[str]] = UNSET,
    is_router_n: Union[Unset, list[str]] = UNSET,
    is_router_nic: Union[Unset, list[str]] = UNSET,
    is_router_nie: Union[Unset, list[str]] = UNSET,
    is_router_niew: Union[Unset, list[str]] = UNSET,
    is_router_nisw: Union[Unset, list[str]] = UNSET,
    is_safety_critical: Union[Unset, list[str]] = UNSET,
    is_safety_critical_empty: Union[Unset, bool] = UNSET,
    is_safety_critical_ic: Union[Unset, list[str]] = UNSET,
    is_safety_critical_ie: Union[Unset, list[str]] = UNSET,
    is_safety_critical_iew: Union[Unset, list[str]] = UNSET,
    is_safety_critical_isw: Union[Unset, list[str]] = UNSET,
    is_safety_critical_n: Union[Unset, list[str]] = UNSET,
    is_safety_critical_nic: Union[Unset, list[str]] = UNSET,
    is_safety_critical_nie: Union[Unset, list[str]] = UNSET,
    is_safety_critical_niew: Union[Unset, list[str]] = UNSET,
    is_safety_critical_nisw: Union[Unset, list[str]] = UNSET,
    last_updated: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_empty: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_gte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lt: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_lte: Union[Unset, list[datetime.datetime]] = UNSET,
    last_updated_n: Union[Unset, list[datetime.datetime]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, list[str]] = UNSET,
    location_empty: Union[Unset, bool] = UNSET,
    location_ic: Union[Unset, list[str]] = UNSET,
    location_ie: Union[Unset, list[str]] = UNSET,
    location_iew: Union[Unset, list[str]] = UNSET,
    location_isw: Union[Unset, list[str]] = UNSET,
    location_n: Union[Unset, list[str]] = UNSET,
    location_nic: Union[Unset, list[str]] = UNSET,
    location_nie: Union[Unset, list[str]] = UNSET,
    location_niew: Union[Unset, list[str]] = UNSET,
    location_nisw: Union[Unset, list[str]] = UNSET,
    mac_address: Union[Unset, list[str]] = UNSET,
    mac_address_empty: Union[Unset, bool] = UNSET,
    mac_address_ic: Union[Unset, list[str]] = UNSET,
    mac_address_ie: Union[Unset, list[str]] = UNSET,
    mac_address_iew: Union[Unset, list[str]] = UNSET,
    mac_address_isw: Union[Unset, list[str]] = UNSET,
    mac_address_n: Union[Unset, list[str]] = UNSET,
    mac_address_nic: Union[Unset, list[str]] = UNSET,
    mac_address_nie: Union[Unset, list[str]] = UNSET,
    mac_address_niew: Union[Unset, list[str]] = UNSET,
    mac_address_nisw: Union[Unset, list[str]] = UNSET,
    manufacturer: Union[Unset, list[str]] = UNSET,
    manufacturer_empty: Union[Unset, bool] = UNSET,
    manufacturer_ic: Union[Unset, list[str]] = UNSET,
    manufacturer_ie: Union[Unset, list[str]] = UNSET,
    manufacturer_iew: Union[Unset, list[str]] = UNSET,
    manufacturer_isw: Union[Unset, list[str]] = UNSET,
    manufacturer_n: Union[Unset, list[str]] = UNSET,
    manufacturer_nic: Union[Unset, list[str]] = UNSET,
    manufacturer_nie: Union[Unset, list[str]] = UNSET,
    manufacturer_niew: Union[Unset, list[str]] = UNSET,
    manufacturer_nisw: Union[Unset, list[str]] = UNSET,
    modified_by_request: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    oui: Union[Unset, list[str]] = UNSET,
    oui_empty: Union[Unset, bool] = UNSET,
    oui_ic: Union[Unset, list[str]] = UNSET,
    oui_ie: Union[Unset, list[str]] = UNSET,
    oui_iew: Union[Unset, list[str]] = UNSET,
    oui_isw: Union[Unset, list[str]] = UNSET,
    oui_n: Union[Unset, list[str]] = UNSET,
    oui_nic: Union[Unset, list[str]] = UNSET,
    oui_nie: Union[Unset, list[str]] = UNSET,
    oui_niew: Union[Unset, list[str]] = UNSET,
    oui_nisw: Union[Unset, list[str]] = UNSET,
    part_number: Union[Unset, list[str]] = UNSET,
    part_number_empty: Union[Unset, bool] = UNSET,
    part_number_ic: Union[Unset, list[str]] = UNSET,
    part_number_ie: Union[Unset, list[str]] = UNSET,
    part_number_iew: Union[Unset, list[str]] = UNSET,
    part_number_isw: Union[Unset, list[str]] = UNSET,
    part_number_n: Union[Unset, list[str]] = UNSET,
    part_number_nic: Union[Unset, list[str]] = UNSET,
    part_number_nie: Union[Unset, list[str]] = UNSET,
    part_number_niew: Union[Unset, list[str]] = UNSET,
    part_number_nisw: Union[Unset, list[str]] = UNSET,
    port: Union[Unset, list[str]] = UNSET,
    port_empty: Union[Unset, bool] = UNSET,
    port_ic: Union[Unset, list[str]] = UNSET,
    port_ie: Union[Unset, list[str]] = UNSET,
    port_iew: Union[Unset, list[str]] = UNSET,
    port_isw: Union[Unset, list[str]] = UNSET,
    port_n: Union[Unset, list[str]] = UNSET,
    port_nic: Union[Unset, list[str]] = UNSET,
    port_nie: Union[Unset, list[str]] = UNSET,
    port_niew: Union[Unset, list[str]] = UNSET,
    port_nisw: Union[Unset, list[str]] = UNSET,
    predicted_device: Union[Unset, int] = UNSET,
    predicted_device_n: Union[Unset, int] = UNSET,
    q: Union[Unset, str] = UNSET,
    rack: Union[Unset, list[str]] = UNSET,
    rack_empty: Union[Unset, bool] = UNSET,
    rack_ic: Union[Unset, list[str]] = UNSET,
    rack_ie: Union[Unset, list[str]] = UNSET,
    rack_iew: Union[Unset, list[str]] = UNSET,
    rack_isw: Union[Unset, list[str]] = UNSET,
    rack_n: Union[Unset, list[str]] = UNSET,
    rack_nic: Union[Unset, list[str]] = UNSET,
    rack_nie: Union[Unset, list[str]] = UNSET,
    rack_niew: Union[Unset, list[str]] = UNSET,
    rack_nisw: Union[Unset, list[str]] = UNSET,
    serial_number: Union[Unset, list[str]] = UNSET,
    serial_number_empty: Union[Unset, bool] = UNSET,
    serial_number_ic: Union[Unset, list[str]] = UNSET,
    serial_number_ie: Union[Unset, list[str]] = UNSET,
    serial_number_iew: Union[Unset, list[str]] = UNSET,
    serial_number_isw: Union[Unset, list[str]] = UNSET,
    serial_number_n: Union[Unset, list[str]] = UNSET,
    serial_number_nic: Union[Unset, list[str]] = UNSET,
    serial_number_nie: Union[Unset, list[str]] = UNSET,
    serial_number_niew: Union[Unset, list[str]] = UNSET,
    serial_number_nisw: Union[Unset, list[str]] = UNSET,
    site: Union[Unset, list[str]] = UNSET,
    site_empty: Union[Unset, bool] = UNSET,
    site_ic: Union[Unset, list[str]] = UNSET,
    site_ie: Union[Unset, list[str]] = UNSET,
    site_iew: Union[Unset, list[str]] = UNSET,
    site_isw: Union[Unset, list[str]] = UNSET,
    site_n: Union[Unset, list[str]] = UNSET,
    site_nic: Union[Unset, list[str]] = UNSET,
    site_nie: Union[Unset, list[str]] = UNSET,
    site_niew: Union[Unset, list[str]] = UNSET,
    site_nisw: Union[Unset, list[str]] = UNSET,
    software_name: Union[Unset, list[str]] = UNSET,
    software_name_empty: Union[Unset, bool] = UNSET,
    software_name_ic: Union[Unset, list[str]] = UNSET,
    software_name_ie: Union[Unset, list[str]] = UNSET,
    software_name_iew: Union[Unset, list[str]] = UNSET,
    software_name_isw: Union[Unset, list[str]] = UNSET,
    software_name_n: Union[Unset, list[str]] = UNSET,
    software_name_nic: Union[Unset, list[str]] = UNSET,
    software_name_nie: Union[Unset, list[str]] = UNSET,
    software_name_niew: Union[Unset, list[str]] = UNSET,
    software_name_nisw: Union[Unset, list[str]] = UNSET,
    source: Union[Unset, list[str]] = UNSET,
    source_empty: Union[Unset, bool] = UNSET,
    source_ic: Union[Unset, list[str]] = UNSET,
    source_ie: Union[Unset, list[str]] = UNSET,
    source_iew: Union[Unset, list[str]] = UNSET,
    source_isw: Union[Unset, list[str]] = UNSET,
    source_n: Union[Unset, list[str]] = UNSET,
    source_nic: Union[Unset, list[str]] = UNSET,
    source_nie: Union[Unset, list[str]] = UNSET,
    source_niew: Union[Unset, list[str]] = UNSET,
    source_nisw: Union[Unset, list[str]] = UNSET,
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
) -> Optional[PaginatedDeviceFindingList]:
    """ViewSet for DeviceFinding.

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
        confidence (Union[Unset, list[float]]):
        confidence_empty (Union[Unset, bool]):
        confidence_gt (Union[Unset, list[float]]):
        confidence_gte (Union[Unset, list[float]]):
        confidence_lt (Union[Unset, list[float]]):
        confidence_lte (Union[Unset, list[float]]):
        confidence_n (Union[Unset, list[float]]):
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
        device (Union[Unset, int]):
        device_n (Union[Unset, int]):
        device_family (Union[Unset, list[str]]):
        device_family_empty (Union[Unset, bool]):
        device_family_ic (Union[Unset, list[str]]):
        device_family_ie (Union[Unset, list[str]]):
        device_family_iew (Union[Unset, list[str]]):
        device_family_isw (Union[Unset, list[str]]):
        device_family_n (Union[Unset, list[str]]):
        device_family_nic (Union[Unset, list[str]]):
        device_family_nie (Union[Unset, list[str]]):
        device_family_niew (Union[Unset, list[str]]):
        device_family_nisw (Union[Unset, list[str]]):
        device_name (Union[Unset, list[str]]):
        device_name_empty (Union[Unset, bool]):
        device_name_ic (Union[Unset, list[str]]):
        device_name_ie (Union[Unset, list[str]]):
        device_name_iew (Union[Unset, list[str]]):
        device_name_isw (Union[Unset, list[str]]):
        device_name_n (Union[Unset, list[str]]):
        device_name_nic (Union[Unset, list[str]]):
        device_name_nie (Union[Unset, list[str]]):
        device_name_niew (Union[Unset, list[str]]):
        device_name_nisw (Union[Unset, list[str]]):
        device_role (Union[Unset, list[str]]):
        device_role_empty (Union[Unset, bool]):
        device_role_ic (Union[Unset, list[str]]):
        device_role_ie (Union[Unset, list[str]]):
        device_role_iew (Union[Unset, list[str]]):
        device_role_isw (Union[Unset, list[str]]):
        device_role_n (Union[Unset, list[str]]):
        device_role_nic (Union[Unset, list[str]]):
        device_role_nie (Union[Unset, list[str]]):
        device_role_niew (Union[Unset, list[str]]):
        device_role_nisw (Union[Unset, list[str]]):
        device_type (Union[Unset, list[str]]):
        device_type_empty (Union[Unset, bool]):
        device_type_ic (Union[Unset, list[str]]):
        device_type_ie (Union[Unset, list[str]]):
        device_type_iew (Union[Unset, list[str]]):
        device_type_isw (Union[Unset, list[str]]):
        device_type_n (Union[Unset, list[str]]):
        device_type_nic (Union[Unset, list[str]]):
        device_type_nie (Union[Unset, list[str]]):
        device_type_niew (Union[Unset, list[str]]):
        device_type_nisw (Union[Unset, list[str]]):
        exposure (Union[Unset, list[str]]):
        exposure_empty (Union[Unset, bool]):
        exposure_ic (Union[Unset, list[str]]):
        exposure_ie (Union[Unset, list[str]]):
        exposure_iew (Union[Unset, list[str]]):
        exposure_isw (Union[Unset, list[str]]):
        exposure_n (Union[Unset, list[str]]):
        exposure_nic (Union[Unset, list[str]]):
        exposure_nie (Union[Unset, list[str]]):
        exposure_niew (Union[Unset, list[str]]):
        exposure_nisw (Union[Unset, list[str]]):
        hardware_cpe (Union[Unset, list[str]]):
        hardware_cpe_empty (Union[Unset, bool]):
        hardware_cpe_ic (Union[Unset, list[str]]):
        hardware_cpe_ie (Union[Unset, list[str]]):
        hardware_cpe_iew (Union[Unset, list[str]]):
        hardware_cpe_isw (Union[Unset, list[str]]):
        hardware_cpe_n (Union[Unset, list[str]]):
        hardware_cpe_nic (Union[Unset, list[str]]):
        hardware_cpe_nie (Union[Unset, list[str]]):
        hardware_cpe_niew (Union[Unset, list[str]]):
        hardware_cpe_nisw (Union[Unset, list[str]]):
        hardware_version (Union[Unset, list[str]]):
        hardware_version_empty (Union[Unset, bool]):
        hardware_version_ic (Union[Unset, list[str]]):
        hardware_version_ie (Union[Unset, list[str]]):
        hardware_version_iew (Union[Unset, list[str]]):
        hardware_version_isw (Union[Unset, list[str]]):
        hardware_version_n (Union[Unset, list[str]]):
        hardware_version_nic (Union[Unset, list[str]]):
        hardware_version_nie (Union[Unset, list[str]]):
        hardware_version_niew (Union[Unset, list[str]]):
        hardware_version_nisw (Union[Unset, list[str]]):
        has_predicted_device (Union[Unset, bool]):
        id (Union[Unset, list[int]]):
        id_empty (Union[Unset, bool]):
        id_gt (Union[Unset, list[int]]):
        id_gte (Union[Unset, list[int]]):
        id_lt (Union[Unset, list[int]]):
        id_lte (Union[Unset, list[int]]):
        id_n (Union[Unset, list[int]]):
        ip_address (Union[Unset, list[str]]):
        ip_address_empty (Union[Unset, bool]):
        ip_address_ic (Union[Unset, list[str]]):
        ip_address_ie (Union[Unset, list[str]]):
        ip_address_iew (Union[Unset, list[str]]):
        ip_address_isw (Union[Unset, list[str]]):
        ip_address_n (Union[Unset, list[str]]):
        ip_address_nic (Union[Unset, list[str]]):
        ip_address_nie (Union[Unset, list[str]]):
        ip_address_niew (Union[Unset, list[str]]):
        ip_address_nisw (Union[Unset, list[str]]):
        is_firmware (Union[Unset, list[str]]):
        is_firmware_empty (Union[Unset, bool]):
        is_firmware_ic (Union[Unset, list[str]]):
        is_firmware_ie (Union[Unset, list[str]]):
        is_firmware_iew (Union[Unset, list[str]]):
        is_firmware_isw (Union[Unset, list[str]]):
        is_firmware_n (Union[Unset, list[str]]):
        is_firmware_nic (Union[Unset, list[str]]):
        is_firmware_nie (Union[Unset, list[str]]):
        is_firmware_niew (Union[Unset, list[str]]):
        is_firmware_nisw (Union[Unset, list[str]]):
        is_router (Union[Unset, list[str]]):
        is_router_empty (Union[Unset, bool]):
        is_router_ic (Union[Unset, list[str]]):
        is_router_ie (Union[Unset, list[str]]):
        is_router_iew (Union[Unset, list[str]]):
        is_router_isw (Union[Unset, list[str]]):
        is_router_n (Union[Unset, list[str]]):
        is_router_nic (Union[Unset, list[str]]):
        is_router_nie (Union[Unset, list[str]]):
        is_router_niew (Union[Unset, list[str]]):
        is_router_nisw (Union[Unset, list[str]]):
        is_safety_critical (Union[Unset, list[str]]):
        is_safety_critical_empty (Union[Unset, bool]):
        is_safety_critical_ic (Union[Unset, list[str]]):
        is_safety_critical_ie (Union[Unset, list[str]]):
        is_safety_critical_iew (Union[Unset, list[str]]):
        is_safety_critical_isw (Union[Unset, list[str]]):
        is_safety_critical_n (Union[Unset, list[str]]):
        is_safety_critical_nic (Union[Unset, list[str]]):
        is_safety_critical_nie (Union[Unset, list[str]]):
        is_safety_critical_niew (Union[Unset, list[str]]):
        is_safety_critical_nisw (Union[Unset, list[str]]):
        last_updated (Union[Unset, list[datetime.datetime]]):
        last_updated_empty (Union[Unset, list[datetime.datetime]]):
        last_updated_gt (Union[Unset, list[datetime.datetime]]):
        last_updated_gte (Union[Unset, list[datetime.datetime]]):
        last_updated_lt (Union[Unset, list[datetime.datetime]]):
        last_updated_lte (Union[Unset, list[datetime.datetime]]):
        last_updated_n (Union[Unset, list[datetime.datetime]]):
        limit (Union[Unset, int]):
        location (Union[Unset, list[str]]):
        location_empty (Union[Unset, bool]):
        location_ic (Union[Unset, list[str]]):
        location_ie (Union[Unset, list[str]]):
        location_iew (Union[Unset, list[str]]):
        location_isw (Union[Unset, list[str]]):
        location_n (Union[Unset, list[str]]):
        location_nic (Union[Unset, list[str]]):
        location_nie (Union[Unset, list[str]]):
        location_niew (Union[Unset, list[str]]):
        location_nisw (Union[Unset, list[str]]):
        mac_address (Union[Unset, list[str]]):
        mac_address_empty (Union[Unset, bool]):
        mac_address_ic (Union[Unset, list[str]]):
        mac_address_ie (Union[Unset, list[str]]):
        mac_address_iew (Union[Unset, list[str]]):
        mac_address_isw (Union[Unset, list[str]]):
        mac_address_n (Union[Unset, list[str]]):
        mac_address_nic (Union[Unset, list[str]]):
        mac_address_nie (Union[Unset, list[str]]):
        mac_address_niew (Union[Unset, list[str]]):
        mac_address_nisw (Union[Unset, list[str]]):
        manufacturer (Union[Unset, list[str]]):
        manufacturer_empty (Union[Unset, bool]):
        manufacturer_ic (Union[Unset, list[str]]):
        manufacturer_ie (Union[Unset, list[str]]):
        manufacturer_iew (Union[Unset, list[str]]):
        manufacturer_isw (Union[Unset, list[str]]):
        manufacturer_n (Union[Unset, list[str]]):
        manufacturer_nic (Union[Unset, list[str]]):
        manufacturer_nie (Union[Unset, list[str]]):
        manufacturer_niew (Union[Unset, list[str]]):
        manufacturer_nisw (Union[Unset, list[str]]):
        modified_by_request (Union[Unset, UUID]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        oui (Union[Unset, list[str]]):
        oui_empty (Union[Unset, bool]):
        oui_ic (Union[Unset, list[str]]):
        oui_ie (Union[Unset, list[str]]):
        oui_iew (Union[Unset, list[str]]):
        oui_isw (Union[Unset, list[str]]):
        oui_n (Union[Unset, list[str]]):
        oui_nic (Union[Unset, list[str]]):
        oui_nie (Union[Unset, list[str]]):
        oui_niew (Union[Unset, list[str]]):
        oui_nisw (Union[Unset, list[str]]):
        part_number (Union[Unset, list[str]]):
        part_number_empty (Union[Unset, bool]):
        part_number_ic (Union[Unset, list[str]]):
        part_number_ie (Union[Unset, list[str]]):
        part_number_iew (Union[Unset, list[str]]):
        part_number_isw (Union[Unset, list[str]]):
        part_number_n (Union[Unset, list[str]]):
        part_number_nic (Union[Unset, list[str]]):
        part_number_nie (Union[Unset, list[str]]):
        part_number_niew (Union[Unset, list[str]]):
        part_number_nisw (Union[Unset, list[str]]):
        port (Union[Unset, list[str]]):
        port_empty (Union[Unset, bool]):
        port_ic (Union[Unset, list[str]]):
        port_ie (Union[Unset, list[str]]):
        port_iew (Union[Unset, list[str]]):
        port_isw (Union[Unset, list[str]]):
        port_n (Union[Unset, list[str]]):
        port_nic (Union[Unset, list[str]]):
        port_nie (Union[Unset, list[str]]):
        port_niew (Union[Unset, list[str]]):
        port_nisw (Union[Unset, list[str]]):
        predicted_device (Union[Unset, int]):
        predicted_device_n (Union[Unset, int]):
        q (Union[Unset, str]):
        rack (Union[Unset, list[str]]):
        rack_empty (Union[Unset, bool]):
        rack_ic (Union[Unset, list[str]]):
        rack_ie (Union[Unset, list[str]]):
        rack_iew (Union[Unset, list[str]]):
        rack_isw (Union[Unset, list[str]]):
        rack_n (Union[Unset, list[str]]):
        rack_nic (Union[Unset, list[str]]):
        rack_nie (Union[Unset, list[str]]):
        rack_niew (Union[Unset, list[str]]):
        rack_nisw (Union[Unset, list[str]]):
        serial_number (Union[Unset, list[str]]):
        serial_number_empty (Union[Unset, bool]):
        serial_number_ic (Union[Unset, list[str]]):
        serial_number_ie (Union[Unset, list[str]]):
        serial_number_iew (Union[Unset, list[str]]):
        serial_number_isw (Union[Unset, list[str]]):
        serial_number_n (Union[Unset, list[str]]):
        serial_number_nic (Union[Unset, list[str]]):
        serial_number_nie (Union[Unset, list[str]]):
        serial_number_niew (Union[Unset, list[str]]):
        serial_number_nisw (Union[Unset, list[str]]):
        site (Union[Unset, list[str]]):
        site_empty (Union[Unset, bool]):
        site_ic (Union[Unset, list[str]]):
        site_ie (Union[Unset, list[str]]):
        site_iew (Union[Unset, list[str]]):
        site_isw (Union[Unset, list[str]]):
        site_n (Union[Unset, list[str]]):
        site_nic (Union[Unset, list[str]]):
        site_nie (Union[Unset, list[str]]):
        site_niew (Union[Unset, list[str]]):
        site_nisw (Union[Unset, list[str]]):
        software_name (Union[Unset, list[str]]):
        software_name_empty (Union[Unset, bool]):
        software_name_ic (Union[Unset, list[str]]):
        software_name_ie (Union[Unset, list[str]]):
        software_name_iew (Union[Unset, list[str]]):
        software_name_isw (Union[Unset, list[str]]):
        software_name_n (Union[Unset, list[str]]):
        software_name_nic (Union[Unset, list[str]]):
        software_name_nie (Union[Unset, list[str]]):
        software_name_niew (Union[Unset, list[str]]):
        software_name_nisw (Union[Unset, list[str]]):
        source (Union[Unset, list[str]]):
        source_empty (Union[Unset, bool]):
        source_ic (Union[Unset, list[str]]):
        source_ie (Union[Unset, list[str]]):
        source_iew (Union[Unset, list[str]]):
        source_isw (Union[Unset, list[str]]):
        source_n (Union[Unset, list[str]]):
        source_nic (Union[Unset, list[str]]):
        source_nie (Union[Unset, list[str]]):
        source_niew (Union[Unset, list[str]]):
        source_nisw (Union[Unset, list[str]]):
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
        PaginatedDeviceFindingList
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
            confidence=confidence,
            confidence_empty=confidence_empty,
            confidence_gt=confidence_gt,
            confidence_gte=confidence_gte,
            confidence_lt=confidence_lt,
            confidence_lte=confidence_lte,
            confidence_n=confidence_n,
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
            device_family=device_family,
            device_family_empty=device_family_empty,
            device_family_ic=device_family_ic,
            device_family_ie=device_family_ie,
            device_family_iew=device_family_iew,
            device_family_isw=device_family_isw,
            device_family_n=device_family_n,
            device_family_nic=device_family_nic,
            device_family_nie=device_family_nie,
            device_family_niew=device_family_niew,
            device_family_nisw=device_family_nisw,
            device_name=device_name,
            device_name_empty=device_name_empty,
            device_name_ic=device_name_ic,
            device_name_ie=device_name_ie,
            device_name_iew=device_name_iew,
            device_name_isw=device_name_isw,
            device_name_n=device_name_n,
            device_name_nic=device_name_nic,
            device_name_nie=device_name_nie,
            device_name_niew=device_name_niew,
            device_name_nisw=device_name_nisw,
            device_role=device_role,
            device_role_empty=device_role_empty,
            device_role_ic=device_role_ic,
            device_role_ie=device_role_ie,
            device_role_iew=device_role_iew,
            device_role_isw=device_role_isw,
            device_role_n=device_role_n,
            device_role_nic=device_role_nic,
            device_role_nie=device_role_nie,
            device_role_niew=device_role_niew,
            device_role_nisw=device_role_nisw,
            device_type=device_type,
            device_type_empty=device_type_empty,
            device_type_ic=device_type_ic,
            device_type_ie=device_type_ie,
            device_type_iew=device_type_iew,
            device_type_isw=device_type_isw,
            device_type_n=device_type_n,
            device_type_nic=device_type_nic,
            device_type_nie=device_type_nie,
            device_type_niew=device_type_niew,
            device_type_nisw=device_type_nisw,
            exposure=exposure,
            exposure_empty=exposure_empty,
            exposure_ic=exposure_ic,
            exposure_ie=exposure_ie,
            exposure_iew=exposure_iew,
            exposure_isw=exposure_isw,
            exposure_n=exposure_n,
            exposure_nic=exposure_nic,
            exposure_nie=exposure_nie,
            exposure_niew=exposure_niew,
            exposure_nisw=exposure_nisw,
            hardware_cpe=hardware_cpe,
            hardware_cpe_empty=hardware_cpe_empty,
            hardware_cpe_ic=hardware_cpe_ic,
            hardware_cpe_ie=hardware_cpe_ie,
            hardware_cpe_iew=hardware_cpe_iew,
            hardware_cpe_isw=hardware_cpe_isw,
            hardware_cpe_n=hardware_cpe_n,
            hardware_cpe_nic=hardware_cpe_nic,
            hardware_cpe_nie=hardware_cpe_nie,
            hardware_cpe_niew=hardware_cpe_niew,
            hardware_cpe_nisw=hardware_cpe_nisw,
            hardware_version=hardware_version,
            hardware_version_empty=hardware_version_empty,
            hardware_version_ic=hardware_version_ic,
            hardware_version_ie=hardware_version_ie,
            hardware_version_iew=hardware_version_iew,
            hardware_version_isw=hardware_version_isw,
            hardware_version_n=hardware_version_n,
            hardware_version_nic=hardware_version_nic,
            hardware_version_nie=hardware_version_nie,
            hardware_version_niew=hardware_version_niew,
            hardware_version_nisw=hardware_version_nisw,
            has_predicted_device=has_predicted_device,
            id=id,
            id_empty=id_empty,
            id_gt=id_gt,
            id_gte=id_gte,
            id_lt=id_lt,
            id_lte=id_lte,
            id_n=id_n,
            ip_address=ip_address,
            ip_address_empty=ip_address_empty,
            ip_address_ic=ip_address_ic,
            ip_address_ie=ip_address_ie,
            ip_address_iew=ip_address_iew,
            ip_address_isw=ip_address_isw,
            ip_address_n=ip_address_n,
            ip_address_nic=ip_address_nic,
            ip_address_nie=ip_address_nie,
            ip_address_niew=ip_address_niew,
            ip_address_nisw=ip_address_nisw,
            is_firmware=is_firmware,
            is_firmware_empty=is_firmware_empty,
            is_firmware_ic=is_firmware_ic,
            is_firmware_ie=is_firmware_ie,
            is_firmware_iew=is_firmware_iew,
            is_firmware_isw=is_firmware_isw,
            is_firmware_n=is_firmware_n,
            is_firmware_nic=is_firmware_nic,
            is_firmware_nie=is_firmware_nie,
            is_firmware_niew=is_firmware_niew,
            is_firmware_nisw=is_firmware_nisw,
            is_router=is_router,
            is_router_empty=is_router_empty,
            is_router_ic=is_router_ic,
            is_router_ie=is_router_ie,
            is_router_iew=is_router_iew,
            is_router_isw=is_router_isw,
            is_router_n=is_router_n,
            is_router_nic=is_router_nic,
            is_router_nie=is_router_nie,
            is_router_niew=is_router_niew,
            is_router_nisw=is_router_nisw,
            is_safety_critical=is_safety_critical,
            is_safety_critical_empty=is_safety_critical_empty,
            is_safety_critical_ic=is_safety_critical_ic,
            is_safety_critical_ie=is_safety_critical_ie,
            is_safety_critical_iew=is_safety_critical_iew,
            is_safety_critical_isw=is_safety_critical_isw,
            is_safety_critical_n=is_safety_critical_n,
            is_safety_critical_nic=is_safety_critical_nic,
            is_safety_critical_nie=is_safety_critical_nie,
            is_safety_critical_niew=is_safety_critical_niew,
            is_safety_critical_nisw=is_safety_critical_nisw,
            last_updated=last_updated,
            last_updated_empty=last_updated_empty,
            last_updated_gt=last_updated_gt,
            last_updated_gte=last_updated_gte,
            last_updated_lt=last_updated_lt,
            last_updated_lte=last_updated_lte,
            last_updated_n=last_updated_n,
            limit=limit,
            location=location,
            location_empty=location_empty,
            location_ic=location_ic,
            location_ie=location_ie,
            location_iew=location_iew,
            location_isw=location_isw,
            location_n=location_n,
            location_nic=location_nic,
            location_nie=location_nie,
            location_niew=location_niew,
            location_nisw=location_nisw,
            mac_address=mac_address,
            mac_address_empty=mac_address_empty,
            mac_address_ic=mac_address_ic,
            mac_address_ie=mac_address_ie,
            mac_address_iew=mac_address_iew,
            mac_address_isw=mac_address_isw,
            mac_address_n=mac_address_n,
            mac_address_nic=mac_address_nic,
            mac_address_nie=mac_address_nie,
            mac_address_niew=mac_address_niew,
            mac_address_nisw=mac_address_nisw,
            manufacturer=manufacturer,
            manufacturer_empty=manufacturer_empty,
            manufacturer_ic=manufacturer_ic,
            manufacturer_ie=manufacturer_ie,
            manufacturer_iew=manufacturer_iew,
            manufacturer_isw=manufacturer_isw,
            manufacturer_n=manufacturer_n,
            manufacturer_nic=manufacturer_nic,
            manufacturer_nie=manufacturer_nie,
            manufacturer_niew=manufacturer_niew,
            manufacturer_nisw=manufacturer_nisw,
            modified_by_request=modified_by_request,
            offset=offset,
            ordering=ordering,
            oui=oui,
            oui_empty=oui_empty,
            oui_ic=oui_ic,
            oui_ie=oui_ie,
            oui_iew=oui_iew,
            oui_isw=oui_isw,
            oui_n=oui_n,
            oui_nic=oui_nic,
            oui_nie=oui_nie,
            oui_niew=oui_niew,
            oui_nisw=oui_nisw,
            part_number=part_number,
            part_number_empty=part_number_empty,
            part_number_ic=part_number_ic,
            part_number_ie=part_number_ie,
            part_number_iew=part_number_iew,
            part_number_isw=part_number_isw,
            part_number_n=part_number_n,
            part_number_nic=part_number_nic,
            part_number_nie=part_number_nie,
            part_number_niew=part_number_niew,
            part_number_nisw=part_number_nisw,
            port=port,
            port_empty=port_empty,
            port_ic=port_ic,
            port_ie=port_ie,
            port_iew=port_iew,
            port_isw=port_isw,
            port_n=port_n,
            port_nic=port_nic,
            port_nie=port_nie,
            port_niew=port_niew,
            port_nisw=port_nisw,
            predicted_device=predicted_device,
            predicted_device_n=predicted_device_n,
            q=q,
            rack=rack,
            rack_empty=rack_empty,
            rack_ic=rack_ic,
            rack_ie=rack_ie,
            rack_iew=rack_iew,
            rack_isw=rack_isw,
            rack_n=rack_n,
            rack_nic=rack_nic,
            rack_nie=rack_nie,
            rack_niew=rack_niew,
            rack_nisw=rack_nisw,
            serial_number=serial_number,
            serial_number_empty=serial_number_empty,
            serial_number_ic=serial_number_ic,
            serial_number_ie=serial_number_ie,
            serial_number_iew=serial_number_iew,
            serial_number_isw=serial_number_isw,
            serial_number_n=serial_number_n,
            serial_number_nic=serial_number_nic,
            serial_number_nie=serial_number_nie,
            serial_number_niew=serial_number_niew,
            serial_number_nisw=serial_number_nisw,
            site=site,
            site_empty=site_empty,
            site_ic=site_ic,
            site_ie=site_ie,
            site_iew=site_iew,
            site_isw=site_isw,
            site_n=site_n,
            site_nic=site_nic,
            site_nie=site_nie,
            site_niew=site_niew,
            site_nisw=site_nisw,
            software_name=software_name,
            software_name_empty=software_name_empty,
            software_name_ic=software_name_ic,
            software_name_ie=software_name_ie,
            software_name_iew=software_name_iew,
            software_name_isw=software_name_isw,
            software_name_n=software_name_n,
            software_name_nic=software_name_nic,
            software_name_nie=software_name_nie,
            software_name_niew=software_name_niew,
            software_name_nisw=software_name_nisw,
            source=source,
            source_empty=source_empty,
            source_ic=source_ic,
            source_ie=source_ie,
            source_iew=source_iew,
            source_isw=source_isw,
            source_n=source_n,
            source_nic=source_nic,
            source_nie=source_nie,
            source_niew=source_niew,
            source_nisw=source_nisw,
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
