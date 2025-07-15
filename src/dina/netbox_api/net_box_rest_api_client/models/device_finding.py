from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceFinding")


@_attrs_define
class DeviceFinding:
    """REST API Model Serializer for DeviceFindings.

    Attributes:
        id (int):
        url (str):
        source (str):
        device (Union[None, Unset, int]):
        confidence (Union[None, Unset, float]):
        description (Union[None, Unset, str]):
        device_role (Union[None, Unset, str]):
        serial_number (Union[None, Unset, str]):
        device_name (Union[None, Unset, str]):
        status (Union[None, Unset, str]):
        site (Union[None, Unset, str]):
        rack (Union[None, Unset, str]):
        location (Union[None, Unset, str]):
        device_type (Union[None, Unset, str]):
        is_safety_critical (Union[None, Unset, str]):
        ip_address (Union[None, Unset, str]):
        mac_address (Union[None, Unset, str]):
        transport_protocol (Union[None, Unset, str]):
        application_protocol (Union[None, Unset, str]):
        port (Union[None, Unset, str]):
        is_router (Union[None, Unset, str]):
        manufacturer (Union[None, Unset, str]):
        oui (Union[None, Unset, str]):
        device_family (Union[None, Unset, str]):
        part_number (Union[None, Unset, str]):
        hardware_version (Union[None, Unset, str]):
        hardware_cpe (Union[None, Unset, str]):
        software_name (Union[None, Unset, str]):
        is_firmware (Union[None, Unset, str]):
        version (Union[None, Unset, str]):
        exposure (Union[None, Unset, str]):
        has_predicted_device (Union[Unset, bool]):
        predicted_device (Union[None, Unset, int]):
    """

    id: int
    url: str
    source: str
    device: Union[None, Unset, int] = UNSET
    confidence: Union[None, Unset, float] = UNSET
    description: Union[None, Unset, str] = UNSET
    device_role: Union[None, Unset, str] = UNSET
    serial_number: Union[None, Unset, str] = UNSET
    device_name: Union[None, Unset, str] = UNSET
    status: Union[None, Unset, str] = UNSET
    site: Union[None, Unset, str] = UNSET
    rack: Union[None, Unset, str] = UNSET
    location: Union[None, Unset, str] = UNSET
    device_type: Union[None, Unset, str] = UNSET
    is_safety_critical: Union[None, Unset, str] = UNSET
    ip_address: Union[None, Unset, str] = UNSET
    mac_address: Union[None, Unset, str] = UNSET
    transport_protocol: Union[None, Unset, str] = UNSET
    application_protocol: Union[None, Unset, str] = UNSET
    port: Union[None, Unset, str] = UNSET
    is_router: Union[None, Unset, str] = UNSET
    manufacturer: Union[None, Unset, str] = UNSET
    oui: Union[None, Unset, str] = UNSET
    device_family: Union[None, Unset, str] = UNSET
    part_number: Union[None, Unset, str] = UNSET
    hardware_version: Union[None, Unset, str] = UNSET
    hardware_cpe: Union[None, Unset, str] = UNSET
    software_name: Union[None, Unset, str] = UNSET
    is_firmware: Union[None, Unset, str] = UNSET
    version: Union[None, Unset, str] = UNSET
    exposure: Union[None, Unset, str] = UNSET
    has_predicted_device: Union[Unset, bool] = UNSET
    predicted_device: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        source = self.source

        device: Union[None, Unset, int]
        if isinstance(self.device, Unset):
            device = UNSET
        else:
            device = self.device

        confidence: Union[None, Unset, float]
        if isinstance(self.confidence, Unset):
            confidence = UNSET
        else:
            confidence = self.confidence

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        device_role: Union[None, Unset, str]
        if isinstance(self.device_role, Unset):
            device_role = UNSET
        else:
            device_role = self.device_role

        serial_number: Union[None, Unset, str]
        if isinstance(self.serial_number, Unset):
            serial_number = UNSET
        else:
            serial_number = self.serial_number

        device_name: Union[None, Unset, str]
        if isinstance(self.device_name, Unset):
            device_name = UNSET
        else:
            device_name = self.device_name

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        site: Union[None, Unset, str]
        if isinstance(self.site, Unset):
            site = UNSET
        else:
            site = self.site

        rack: Union[None, Unset, str]
        if isinstance(self.rack, Unset):
            rack = UNSET
        else:
            rack = self.rack

        location: Union[None, Unset, str]
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        device_type: Union[None, Unset, str]
        if isinstance(self.device_type, Unset):
            device_type = UNSET
        else:
            device_type = self.device_type

        is_safety_critical: Union[None, Unset, str]
        if isinstance(self.is_safety_critical, Unset):
            is_safety_critical = UNSET
        else:
            is_safety_critical = self.is_safety_critical

        ip_address: Union[None, Unset, str]
        if isinstance(self.ip_address, Unset):
            ip_address = UNSET
        else:
            ip_address = self.ip_address

        mac_address: Union[None, Unset, str]
        if isinstance(self.mac_address, Unset):
            mac_address = UNSET
        else:
            mac_address = self.mac_address

        transport_protocol: Union[None, Unset, str]
        if isinstance(self.transport_protocol, Unset):
            transport_protocol = UNSET
        else:
            transport_protocol = self.transport_protocol

        application_protocol: Union[None, Unset, str]
        if isinstance(self.application_protocol, Unset):
            application_protocol = UNSET
        else:
            application_protocol = self.application_protocol

        port: Union[None, Unset, str]
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        is_router: Union[None, Unset, str]
        if isinstance(self.is_router, Unset):
            is_router = UNSET
        else:
            is_router = self.is_router

        manufacturer: Union[None, Unset, str]
        if isinstance(self.manufacturer, Unset):
            manufacturer = UNSET
        else:
            manufacturer = self.manufacturer

        oui: Union[None, Unset, str]
        if isinstance(self.oui, Unset):
            oui = UNSET
        else:
            oui = self.oui

        device_family: Union[None, Unset, str]
        if isinstance(self.device_family, Unset):
            device_family = UNSET
        else:
            device_family = self.device_family

        part_number: Union[None, Unset, str]
        if isinstance(self.part_number, Unset):
            part_number = UNSET
        else:
            part_number = self.part_number

        hardware_version: Union[None, Unset, str]
        if isinstance(self.hardware_version, Unset):
            hardware_version = UNSET
        else:
            hardware_version = self.hardware_version

        hardware_cpe: Union[None, Unset, str]
        if isinstance(self.hardware_cpe, Unset):
            hardware_cpe = UNSET
        else:
            hardware_cpe = self.hardware_cpe

        software_name: Union[None, Unset, str]
        if isinstance(self.software_name, Unset):
            software_name = UNSET
        else:
            software_name = self.software_name

        is_firmware: Union[None, Unset, str]
        if isinstance(self.is_firmware, Unset):
            is_firmware = UNSET
        else:
            is_firmware = self.is_firmware

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        exposure: Union[None, Unset, str]
        if isinstance(self.exposure, Unset):
            exposure = UNSET
        else:
            exposure = self.exposure

        has_predicted_device = self.has_predicted_device

        predicted_device: Union[None, Unset, int]
        if isinstance(self.predicted_device, Unset):
            predicted_device = UNSET
        else:
            predicted_device = self.predicted_device

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "source": source,
            }
        )
        if device is not UNSET:
            field_dict["device"] = device
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if description is not UNSET:
            field_dict["description"] = description
        if device_role is not UNSET:
            field_dict["device_role"] = device_role
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number
        if device_name is not UNSET:
            field_dict["device_name"] = device_name
        if status is not UNSET:
            field_dict["status"] = status
        if site is not UNSET:
            field_dict["site"] = site
        if rack is not UNSET:
            field_dict["rack"] = rack
        if location is not UNSET:
            field_dict["location"] = location
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if is_safety_critical is not UNSET:
            field_dict["is_safety_critical"] = is_safety_critical
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if mac_address is not UNSET:
            field_dict["mac_address"] = mac_address
        if transport_protocol is not UNSET:
            field_dict["transport_protocol"] = transport_protocol
        if application_protocol is not UNSET:
            field_dict["application_protocol"] = application_protocol
        if port is not UNSET:
            field_dict["port"] = port
        if is_router is not UNSET:
            field_dict["is_router"] = is_router
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if oui is not UNSET:
            field_dict["oui"] = oui
        if device_family is not UNSET:
            field_dict["device_family"] = device_family
        if part_number is not UNSET:
            field_dict["part_number"] = part_number
        if hardware_version is not UNSET:
            field_dict["hardware_version"] = hardware_version
        if hardware_cpe is not UNSET:
            field_dict["hardware_cpe"] = hardware_cpe
        if software_name is not UNSET:
            field_dict["software_name"] = software_name
        if is_firmware is not UNSET:
            field_dict["is_firmware"] = is_firmware
        if version is not UNSET:
            field_dict["version"] = version
        if exposure is not UNSET:
            field_dict["exposure"] = exposure
        if has_predicted_device is not UNSET:
            field_dict["has_predicted_device"] = has_predicted_device
        if predicted_device is not UNSET:
            field_dict["predicted_device"] = predicted_device

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        source = d.pop("source")

        def _parse_device(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        device = _parse_device(d.pop("device", UNSET))

        def _parse_confidence(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        confidence = _parse_confidence(d.pop("confidence", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_device_role(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_role = _parse_device_role(d.pop("device_role", UNSET))

        def _parse_serial_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        serial_number = _parse_serial_number(d.pop("serial_number", UNSET))

        def _parse_device_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_name = _parse_device_name(d.pop("device_name", UNSET))

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_site(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        site = _parse_site(d.pop("site", UNSET))

        def _parse_rack(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rack = _parse_rack(d.pop("rack", UNSET))

        def _parse_location(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_device_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_type = _parse_device_type(d.pop("device_type", UNSET))

        def _parse_is_safety_critical(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        is_safety_critical = _parse_is_safety_critical(d.pop("is_safety_critical", UNSET))

        def _parse_ip_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ip_address = _parse_ip_address(d.pop("ip_address", UNSET))

        def _parse_mac_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mac_address = _parse_mac_address(d.pop("mac_address", UNSET))

        def _parse_transport_protocol(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        transport_protocol = _parse_transport_protocol(d.pop("transport_protocol", UNSET))

        def _parse_application_protocol(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        application_protocol = _parse_application_protocol(d.pop("application_protocol", UNSET))

        def _parse_port(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_is_router(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        is_router = _parse_is_router(d.pop("is_router", UNSET))

        def _parse_manufacturer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        manufacturer = _parse_manufacturer(d.pop("manufacturer", UNSET))

        def _parse_oui(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        oui = _parse_oui(d.pop("oui", UNSET))

        def _parse_device_family(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        device_family = _parse_device_family(d.pop("device_family", UNSET))

        def _parse_part_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        part_number = _parse_part_number(d.pop("part_number", UNSET))

        def _parse_hardware_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hardware_version = _parse_hardware_version(d.pop("hardware_version", UNSET))

        def _parse_hardware_cpe(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hardware_cpe = _parse_hardware_cpe(d.pop("hardware_cpe", UNSET))

        def _parse_software_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        software_name = _parse_software_name(d.pop("software_name", UNSET))

        def _parse_is_firmware(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        is_firmware = _parse_is_firmware(d.pop("is_firmware", UNSET))

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_exposure(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        exposure = _parse_exposure(d.pop("exposure", UNSET))

        has_predicted_device = d.pop("has_predicted_device", UNSET)

        def _parse_predicted_device(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        predicted_device = _parse_predicted_device(d.pop("predicted_device", UNSET))

        device_finding = cls(
            id=id,
            url=url,
            source=source,
            device=device,
            confidence=confidence,
            description=description,
            device_role=device_role,
            serial_number=serial_number,
            device_name=device_name,
            status=status,
            site=site,
            rack=rack,
            location=location,
            device_type=device_type,
            is_safety_critical=is_safety_critical,
            ip_address=ip_address,
            mac_address=mac_address,
            transport_protocol=transport_protocol,
            application_protocol=application_protocol,
            port=port,
            is_router=is_router,
            manufacturer=manufacturer,
            oui=oui,
            device_family=device_family,
            part_number=part_number,
            hardware_version=hardware_version,
            hardware_cpe=hardware_cpe,
            software_name=software_name,
            is_firmware=is_firmware,
            version=version,
            exposure=exposure,
            has_predicted_device=has_predicted_device,
            predicted_device=predicted_device,
        )

        device_finding.additional_properties = d
        return device_finding

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
