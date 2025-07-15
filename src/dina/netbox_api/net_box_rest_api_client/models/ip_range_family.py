from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ip_range_family_label import IPRangeFamilyLabel
from ..models.ip_range_family_value import IPRangeFamilyValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="IPRangeFamily")


@_attrs_define
class IPRangeFamily:
    """
    Attributes:
        value (Union[Unset, IPRangeFamilyValue]): * `4` - IPv4
            * `6` - IPv6
        label (Union[Unset, IPRangeFamilyLabel]):
    """

    value: Union[Unset, IPRangeFamilyValue] = UNSET
    label: Union[Unset, IPRangeFamilyLabel] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value: Union[Unset, int] = UNSET
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
        value: Union[Unset, IPRangeFamilyValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = IPRangeFamilyValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, IPRangeFamilyLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = IPRangeFamilyLabel(_label)

        ip_range_family = cls(
            value=value,
            label=label,
        )

        ip_range_family.additional_properties = d
        return ip_range_family

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
