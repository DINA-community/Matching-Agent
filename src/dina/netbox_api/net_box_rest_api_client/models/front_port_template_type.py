from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.front_port_template_type_label import FrontPortTemplateTypeLabel
from ..models.front_port_template_type_value import FrontPortTemplateTypeValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="FrontPortTemplateType")


@_attrs_define
class FrontPortTemplateType:
    """
    Attributes:
        value (Union[Unset, FrontPortTemplateTypeValue]): * `8p8c` - 8P8C
            * `8p6c` - 8P6C
            * `8p4c` - 8P4C
            * `8p2c` - 8P2C
            * `6p6c` - 6P6C
            * `6p4c` - 6P4C
            * `6p2c` - 6P2C
            * `4p4c` - 4P4C
            * `4p2c` - 4P2C
            * `gg45` - GG45
            * `tera-4p` - TERA 4P
            * `tera-2p` - TERA 2P
            * `tera-1p` - TERA 1P
            * `110-punch` - 110 Punch
            * `bnc` - BNC
            * `f` - F Connector
            * `n` - N Connector
            * `mrj21` - MRJ21
            * `fc` - FC
            * `fc-pc` - FC/PC
            * `fc-upc` - FC/UPC
            * `fc-apc` - FC/APC
            * `lc` - LC
            * `lc-pc` - LC/PC
            * `lc-upc` - LC/UPC
            * `lc-apc` - LC/APC
            * `lsh` - LSH
            * `lsh-pc` - LSH/PC
            * `lsh-upc` - LSH/UPC
            * `lsh-apc` - LSH/APC
            * `lx5` - LX.5
            * `lx5-pc` - LX.5/PC
            * `lx5-upc` - LX.5/UPC
            * `lx5-apc` - LX.5/APC
            * `mpo` - MPO
            * `mtrj` - MTRJ
            * `sc` - SC
            * `sc-pc` - SC/PC
            * `sc-upc` - SC/UPC
            * `sc-apc` - SC/APC
            * `st` - ST
            * `cs` - CS
            * `sn` - SN
            * `sma-905` - SMA 905
            * `sma-906` - SMA 906
            * `urm-p2` - URM-P2
            * `urm-p4` - URM-P4
            * `urm-p8` - URM-P8
            * `splice` - Splice
            * `usb-a` - USB Type A
            * `usb-b` - USB Type B
            * `usb-c` - USB Type C
            * `usb-mini-a` - USB Mini A
            * `usb-mini-b` - USB Mini B
            * `usb-micro-a` - USB Micro A
            * `usb-micro-b` - USB Micro B
            * `usb-micro-ab` - USB Micro AB
            * `other` - Other
        label (Union[Unset, FrontPortTemplateTypeLabel]):
    """

    value: Union[Unset, FrontPortTemplateTypeValue] = UNSET
    label: Union[Unset, FrontPortTemplateTypeLabel] = UNSET
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
        value: Union[Unset, FrontPortTemplateTypeValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = FrontPortTemplateTypeValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, FrontPortTemplateTypeLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = FrontPortTemplateTypeLabel(_label)

        front_port_template_type = cls(
            value=value,
            label=label,
        )

        front_port_template_type.additional_properties = d
        return front_port_template_type

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
