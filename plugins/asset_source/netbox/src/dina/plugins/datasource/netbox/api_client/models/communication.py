from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device import BriefDevice


T = TypeVar("T", bound="Communication")


@_attrs_define
class Communication:
    """REST API Model Serializer for Communication.

    Attributes:
        id (int):
        url (str):
        source_device (BriefDevice): Adds support for custom fields and tags.
        destination_device (Union[None, Unset, int]):
        source_ip_addr (Union[None, Unset, int]):
        destination_ip_addr (Union[None, Unset, int]):
        destination_port (Union[None, Unset, int]):
        network_protocol (Union[None, Unset, str]):
        transport_protocol (Union[None, Unset, str]):
        application_protocol (Union[None, Unset, str]):
    """

    id: int
    url: str
    source_device: "BriefDevice"
    destination_device: Union[None, Unset, int] = UNSET
    source_ip_addr: Union[None, Unset, int] = UNSET
    destination_ip_addr: Union[None, Unset, int] = UNSET
    destination_port: Union[None, Unset, int] = UNSET
    network_protocol: Union[None, Unset, str] = UNSET
    transport_protocol: Union[None, Unset, str] = UNSET
    application_protocol: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        source_device = self.source_device.to_dict()

        destination_device: Union[None, Unset, int]
        if isinstance(self.destination_device, Unset):
            destination_device = UNSET
        else:
            destination_device = self.destination_device

        source_ip_addr: Union[None, Unset, int]
        if isinstance(self.source_ip_addr, Unset):
            source_ip_addr = UNSET
        else:
            source_ip_addr = self.source_ip_addr

        destination_ip_addr: Union[None, Unset, int]
        if isinstance(self.destination_ip_addr, Unset):
            destination_ip_addr = UNSET
        else:
            destination_ip_addr = self.destination_ip_addr

        destination_port: Union[None, Unset, int]
        if isinstance(self.destination_port, Unset):
            destination_port = UNSET
        else:
            destination_port = self.destination_port

        network_protocol: Union[None, Unset, str]
        if isinstance(self.network_protocol, Unset):
            network_protocol = UNSET
        else:
            network_protocol = self.network_protocol

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "source_device": source_device,
            }
        )
        if destination_device is not UNSET:
            field_dict["destination_device"] = destination_device
        if source_ip_addr is not UNSET:
            field_dict["source_ip_addr"] = source_ip_addr
        if destination_ip_addr is not UNSET:
            field_dict["destination_ip_addr"] = destination_ip_addr
        if destination_port is not UNSET:
            field_dict["destination_port"] = destination_port
        if network_protocol is not UNSET:
            field_dict["network_protocol"] = network_protocol
        if transport_protocol is not UNSET:
            field_dict["transport_protocol"] = transport_protocol
        if application_protocol is not UNSET:
            field_dict["application_protocol"] = application_protocol

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_device import BriefDevice

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        source_device = BriefDevice.from_dict(d.pop("source_device"))

        def _parse_destination_device(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        destination_device = _parse_destination_device(
            d.pop("destination_device", UNSET)
        )

        def _parse_source_ip_addr(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        source_ip_addr = _parse_source_ip_addr(d.pop("source_ip_addr", UNSET))

        def _parse_destination_ip_addr(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        destination_ip_addr = _parse_destination_ip_addr(
            d.pop("destination_ip_addr", UNSET)
        )

        def _parse_destination_port(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        destination_port = _parse_destination_port(d.pop("destination_port", UNSET))

        def _parse_network_protocol(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        network_protocol = _parse_network_protocol(d.pop("network_protocol", UNSET))

        def _parse_transport_protocol(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        transport_protocol = _parse_transport_protocol(
            d.pop("transport_protocol", UNSET)
        )

        def _parse_application_protocol(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        application_protocol = _parse_application_protocol(
            d.pop("application_protocol", UNSET)
        )

        communication = cls(
            id=id,
            url=url,
            source_device=source_device,
            destination_device=destination_device,
            source_ip_addr=source_ip_addr,
            destination_ip_addr=destination_ip_addr,
            destination_port=destination_port,
            network_protocol=network_protocol,
            transport_protocol=transport_protocol,
            application_protocol=application_protocol,
        )

        communication.additional_properties = d
        return communication

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
