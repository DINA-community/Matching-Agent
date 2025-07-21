from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tunnel_encapsulation_label import TunnelEncapsulationLabel
from ..models.tunnel_encapsulation_value import TunnelEncapsulationValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="TunnelEncapsulation")


@_attrs_define
class TunnelEncapsulation:
    """
    Attributes:
        value (Union[Unset, TunnelEncapsulationValue]): * `ipsec-transport` - IPsec - Transport
            * `ipsec-tunnel` - IPsec - Tunnel
            * `ip-ip` - IP-in-IP
            * `gre` - GRE
            * `wireguard` - WireGuard
            * `openvpn` - OpenVPN
            * `l2tp` - L2TP
            * `pptp` - PPTP
        label (Union[Unset, TunnelEncapsulationLabel]):
    """

    value: Union[Unset, TunnelEncapsulationValue] = UNSET
    label: Union[Unset, TunnelEncapsulationLabel] = UNSET
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
        value: Union[Unset, TunnelEncapsulationValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = TunnelEncapsulationValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, TunnelEncapsulationLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = TunnelEncapsulationLabel(_label)

        tunnel_encapsulation = cls(
            value=value,
            label=label,
        )

        tunnel_encapsulation.additional_properties = d
        return tunnel_encapsulation

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
