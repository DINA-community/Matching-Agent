from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.circuit_group_assignment_priority_label import (
    CircuitGroupAssignmentPriorityLabel,
)
from ..models.circuit_group_assignment_priority_value import (
    CircuitGroupAssignmentPriorityValue,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CircuitGroupAssignmentPriority")


@_attrs_define
class CircuitGroupAssignmentPriority:
    """
    Attributes:
        value (Union[Unset, CircuitGroupAssignmentPriorityValue]): * `primary` - Primary
            * `secondary` - Secondary
            * `tertiary` - Tertiary
            * `inactive` - Inactive
        label (Union[Unset, CircuitGroupAssignmentPriorityLabel]):
    """

    value: Union[Unset, CircuitGroupAssignmentPriorityValue] = UNSET
    label: Union[Unset, CircuitGroupAssignmentPriorityLabel] = UNSET
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
        value: Union[Unset, CircuitGroupAssignmentPriorityValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = CircuitGroupAssignmentPriorityValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, CircuitGroupAssignmentPriorityLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = CircuitGroupAssignmentPriorityLabel(_label)

        circuit_group_assignment_priority = cls(
            value=value,
            label=label,
        )

        circuit_group_assignment_priority.additional_properties = d
        return circuit_group_assignment_priority

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
