from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ip_sec_profile_mode_label import IPSecProfileModeLabel
from ..models.ip_sec_profile_mode_value import IPSecProfileModeValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecProfileMode")


@_attrs_define
class IPSecProfileMode:
    """
    Attributes:
        value (Union[Unset, IPSecProfileModeValue]): * `esp` - ESP
            * `ah` - AH
        label (Union[Unset, IPSecProfileModeLabel]):
    """

    value: Union[Unset, IPSecProfileModeValue] = UNSET
    label: Union[Unset, IPSecProfileModeLabel] = UNSET
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
        value: Union[Unset, IPSecProfileModeValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = IPSecProfileModeValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, IPSecProfileModeLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = IPSecProfileModeLabel(_label)

        ip_sec_profile_mode = cls(
            value=value,
            label=label,
        )

        ip_sec_profile_mode.additional_properties = d
        return ip_sec_profile_mode

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
