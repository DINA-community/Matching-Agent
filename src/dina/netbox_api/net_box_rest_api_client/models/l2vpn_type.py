from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.l2vpn_type_label import L2VPNTypeLabel
from ..models.l2vpn_type_value import L2VPNTypeValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="L2VPNType")


@_attrs_define
class L2VPNType:
    """
    Attributes:
        value (Union[Unset, L2VPNTypeValue]): * `vpws` - VPWS
            * `vpls` - VPLS
            * `vxlan` - VXLAN
            * `vxlan-evpn` - VXLAN-EVPN
            * `mpls-evpn` - MPLS EVPN
            * `pbb-evpn` - PBB EVPN
            * `evpn-vpws` - EVPN VPWS
            * `epl` - EPL
            * `evpl` - EVPL
            * `ep-lan` - Ethernet Private LAN
            * `evp-lan` - Ethernet Virtual Private LAN
            * `ep-tree` - Ethernet Private Tree
            * `evp-tree` - Ethernet Virtual Private Tree
            * `spb` - SPB
        label (Union[Unset, L2VPNTypeLabel]):
    """

    value: Union[Unset, L2VPNTypeValue] = UNSET
    label: Union[Unset, L2VPNTypeLabel] = UNSET
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
        value: Union[Unset, L2VPNTypeValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = L2VPNTypeValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, L2VPNTypeLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = L2VPNTypeLabel(_label)

        l2vpn_type = cls(
            value=value,
            label=label,
        )

        l2vpn_type.additional_properties = d
        return l2vpn_type

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
