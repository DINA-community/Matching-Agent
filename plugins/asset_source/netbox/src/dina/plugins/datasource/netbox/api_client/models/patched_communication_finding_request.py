from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedCommunicationFindingRequest")


@_attrs_define
class PatchedCommunicationFindingRequest:
    """REST API Model Serializer for CommunicationFinding.

    Attributes:
        source (Union[Unset, str]):
        source_ip (Union[None, Unset, str]):
        destination_ip (Union[None, Unset, str]):
        destination_port (Union[None, Unset, str]):
        network_protocol (Union[None, Unset, str]):
        transport_protocol (Union[None, Unset, str]):
        application_protocol (Union[None, Unset, str]):
    """

    source: Union[Unset, str] = UNSET
    source_ip: Union[None, Unset, str] = UNSET
    destination_ip: Union[None, Unset, str] = UNSET
    destination_port: Union[None, Unset, str] = UNSET
    network_protocol: Union[None, Unset, str] = UNSET
    transport_protocol: Union[None, Unset, str] = UNSET
    application_protocol: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        source_ip: Union[None, Unset, str]
        if isinstance(self.source_ip, Unset):
            source_ip = UNSET
        else:
            source_ip = self.source_ip

        destination_ip: Union[None, Unset, str]
        if isinstance(self.destination_ip, Unset):
            destination_ip = UNSET
        else:
            destination_ip = self.destination_ip

        destination_port: Union[None, Unset, str]
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
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if source_ip is not UNSET:
            field_dict["source_ip"] = source_ip
        if destination_ip is not UNSET:
            field_dict["destination_ip"] = destination_ip
        if destination_port is not UNSET:
            field_dict["destination_port"] = destination_port
        if network_protocol is not UNSET:
            field_dict["network_protocol"] = network_protocol
        if transport_protocol is not UNSET:
            field_dict["transport_protocol"] = transport_protocol
        if application_protocol is not UNSET:
            field_dict["application_protocol"] = application_protocol

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        source = (
            self.source
            if isinstance(self.source, Unset)
            else (None, str(self.source).encode(), "text/plain")
        )

        source_ip: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.source_ip, Unset):
            source_ip = UNSET
        elif isinstance(self.source_ip, str):
            source_ip = (None, str(self.source_ip).encode(), "text/plain")
        else:
            source_ip = (None, str(self.source_ip).encode(), "text/plain")

        destination_ip: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.destination_ip, Unset):
            destination_ip = UNSET
        elif isinstance(self.destination_ip, str):
            destination_ip = (None, str(self.destination_ip).encode(), "text/plain")
        else:
            destination_ip = (None, str(self.destination_ip).encode(), "text/plain")

        destination_port: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.destination_port, Unset):
            destination_port = UNSET
        elif isinstance(self.destination_port, str):
            destination_port = (None, str(self.destination_port).encode(), "text/plain")
        else:
            destination_port = (None, str(self.destination_port).encode(), "text/plain")

        network_protocol: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.network_protocol, Unset):
            network_protocol = UNSET
        elif isinstance(self.network_protocol, str):
            network_protocol = (None, str(self.network_protocol).encode(), "text/plain")
        else:
            network_protocol = (None, str(self.network_protocol).encode(), "text/plain")

        transport_protocol: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.transport_protocol, Unset):
            transport_protocol = UNSET
        elif isinstance(self.transport_protocol, str):
            transport_protocol = (
                None,
                str(self.transport_protocol).encode(),
                "text/plain",
            )
        else:
            transport_protocol = (
                None,
                str(self.transport_protocol).encode(),
                "text/plain",
            )

        application_protocol: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.application_protocol, Unset):
            application_protocol = UNSET
        elif isinstance(self.application_protocol, str):
            application_protocol = (
                None,
                str(self.application_protocol).encode(),
                "text/plain",
            )
        else:
            application_protocol = (
                None,
                str(self.application_protocol).encode(),
                "text/plain",
            )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if source_ip is not UNSET:
            field_dict["source_ip"] = source_ip
        if destination_ip is not UNSET:
            field_dict["destination_ip"] = destination_ip
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
        d = dict(src_dict)
        source = d.pop("source", UNSET)

        def _parse_source_ip(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_ip = _parse_source_ip(d.pop("source_ip", UNSET))

        def _parse_destination_ip(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        destination_ip = _parse_destination_ip(d.pop("destination_ip", UNSET))

        def _parse_destination_port(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

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

        patched_communication_finding_request = cls(
            source=source,
            source_ip=source_ip,
            destination_ip=destination_ip,
            destination_port=destination_port,
            network_protocol=network_protocol,
            transport_protocol=transport_protocol,
            application_protocol=application_protocol,
        )

        patched_communication_finding_request.additional_properties = d
        return patched_communication_finding_request

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
