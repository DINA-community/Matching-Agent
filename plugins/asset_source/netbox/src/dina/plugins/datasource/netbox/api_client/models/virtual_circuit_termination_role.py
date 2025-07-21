from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.virtual_circuit_termination_role_label import (
    VirtualCircuitTerminationRoleLabel,
)
from ..models.virtual_circuit_termination_role_value import (
    VirtualCircuitTerminationRoleValue,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualCircuitTerminationRole")


@_attrs_define
class VirtualCircuitTerminationRole:
    """
    Attributes:
        value (Union[Unset, VirtualCircuitTerminationRoleValue]): * `peer` - Peer
            * `hub` - Hub
            * `spoke` - Spoke
        label (Union[Unset, VirtualCircuitTerminationRoleLabel]):
    """

    value: Union[Unset, VirtualCircuitTerminationRoleValue] = UNSET
    label: Union[Unset, VirtualCircuitTerminationRoleLabel] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value: Union[Unset, str] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.value

        label: Union[Unset, str] = UNSET
        if not isinstance(self.label, Unset):
            label = self.label.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _value = d.pop("value", UNSET)
        value: Union[Unset, VirtualCircuitTerminationRoleValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = VirtualCircuitTerminationRoleValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, VirtualCircuitTerminationRoleLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = VirtualCircuitTerminationRoleLabel(_label)

        virtual_circuit_termination_role = cls(
            value=value,
            label=label,
        )

        virtual_circuit_termination_role.additional_properties = d
        return virtual_circuit_termination_role

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
