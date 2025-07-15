from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CircuitCircuitTerminationRequest")


@_attrs_define
class CircuitCircuitTerminationRequest:
    """Represents an object related through a ForeignKey field. On write, it accepts a primary key (PK) value or a
    dictionary of attributes which can be used to uniquely identify the related object. This class should be
    subclassed to return a full representation of the related object on read.

        Attributes:
            termination_type (Union[None, Unset, str]):
            termination_id (Union[None, Unset, int]):
            port_speed (Union[None, Unset, int]): Physical circuit speed
            upstream_speed (Union[None, Unset, int]): Upstream speed, if different from port speed
            xconnect_id (Union[Unset, str]): ID of the local cross-connect
            description (Union[Unset, str]):
    """

    termination_type: Union[None, Unset, str] = UNSET
    termination_id: Union[None, Unset, int] = UNSET
    port_speed: Union[None, Unset, int] = UNSET
    upstream_speed: Union[None, Unset, int] = UNSET
    xconnect_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        termination_type: Union[None, Unset, str]
        if isinstance(self.termination_type, Unset):
            termination_type = UNSET
        else:
            termination_type = self.termination_type

        termination_id: Union[None, Unset, int]
        if isinstance(self.termination_id, Unset):
            termination_id = UNSET
        else:
            termination_id = self.termination_id

        port_speed: Union[None, Unset, int]
        if isinstance(self.port_speed, Unset):
            port_speed = UNSET
        else:
            port_speed = self.port_speed

        upstream_speed: Union[None, Unset, int]
        if isinstance(self.upstream_speed, Unset):
            upstream_speed = UNSET
        else:
            upstream_speed = self.upstream_speed

        xconnect_id = self.xconnect_id

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if termination_type is not UNSET:
            field_dict["termination_type"] = termination_type
        if termination_id is not UNSET:
            field_dict["termination_id"] = termination_id
        if port_speed is not UNSET:
            field_dict["port_speed"] = port_speed
        if upstream_speed is not UNSET:
            field_dict["upstream_speed"] = upstream_speed
        if xconnect_id is not UNSET:
            field_dict["xconnect_id"] = xconnect_id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_termination_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        termination_type = _parse_termination_type(d.pop("termination_type", UNSET))

        def _parse_termination_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        termination_id = _parse_termination_id(d.pop("termination_id", UNSET))

        def _parse_port_speed(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        port_speed = _parse_port_speed(d.pop("port_speed", UNSET))

        def _parse_upstream_speed(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        upstream_speed = _parse_upstream_speed(d.pop("upstream_speed", UNSET))

        xconnect_id = d.pop("xconnect_id", UNSET)

        description = d.pop("description", UNSET)

        circuit_circuit_termination_request = cls(
            termination_type=termination_type,
            termination_id=termination_id,
            port_speed=port_speed,
            upstream_speed=upstream_speed,
            xconnect_id=xconnect_id,
            description=description,
        )

        circuit_circuit_termination_request.additional_properties = d
        return circuit_circuit_termination_request

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
