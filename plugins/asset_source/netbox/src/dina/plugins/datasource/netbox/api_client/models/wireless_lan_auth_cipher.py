from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.wireless_lan_auth_cipher_label import WirelessLANAuthCipherLabel
from ..models.wireless_lan_auth_cipher_value import WirelessLANAuthCipherValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="WirelessLANAuthCipher")


@_attrs_define
class WirelessLANAuthCipher:
    """
    Attributes:
        value (Union[Unset, WirelessLANAuthCipherValue]): * `auto` - Auto
            * `tkip` - TKIP
            * `aes` - AES
        label (Union[Unset, WirelessLANAuthCipherLabel]):
    """

    value: Union[Unset, WirelessLANAuthCipherValue] = UNSET
    label: Union[Unset, WirelessLANAuthCipherLabel] = UNSET
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
        value: Union[Unset, WirelessLANAuthCipherValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = WirelessLANAuthCipherValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, WirelessLANAuthCipherLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = WirelessLANAuthCipherLabel(_label)

        wireless_lan_auth_cipher = cls(
            value=value,
            label=label,
        )

        wireless_lan_auth_cipher.additional_properties = d
        return wireless_lan_auth_cipher

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
