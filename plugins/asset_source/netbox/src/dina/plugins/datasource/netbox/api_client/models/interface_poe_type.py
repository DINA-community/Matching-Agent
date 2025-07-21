from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.interface_poe_type_label import InterfacePoeTypeLabel
from ..models.interface_poe_type_value import InterfacePoeTypeValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="InterfacePoeType")


@_attrs_define
class InterfacePoeType:
    """
    Attributes:
        value (Union[Unset, InterfacePoeTypeValue]): * `type1-ieee802.3af` - 802.3af (Type 1)
            * `type2-ieee802.3at` - 802.3at (Type 2)
            * `type3-ieee802.3bt` - 802.3bt (Type 3)
            * `type4-ieee802.3bt` - 802.3bt (Type 4)
            * `passive-24v-2pair` - Passive 24V (2-pair)
            * `passive-24v-4pair` - Passive 24V (4-pair)
            * `passive-48v-2pair` - Passive 48V (2-pair)
            * `passive-48v-4pair` - Passive 48V (4-pair)
        label (Union[Unset, InterfacePoeTypeLabel]):
    """

    value: Union[Unset, InterfacePoeTypeValue] = UNSET
    label: Union[Unset, InterfacePoeTypeLabel] = UNSET
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
        value: Union[Unset, InterfacePoeTypeValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = InterfacePoeTypeValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, InterfacePoeTypeLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = InterfacePoeTypeLabel(_label)

        interface_poe_type = cls(
            value=value,
            label=label,
        )

        interface_poe_type.additional_properties = d
        return interface_poe_type

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
