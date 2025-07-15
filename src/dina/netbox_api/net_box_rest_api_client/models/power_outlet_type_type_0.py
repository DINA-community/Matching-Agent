from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.power_outlet_type_type_0_label import PowerOutletTypeType0Label
from ..models.power_outlet_type_type_0_value_type_1 import PowerOutletTypeType0ValueType1
from ..types import UNSET, Unset

T = TypeVar("T", bound="PowerOutletTypeType0")


@_attrs_define
class PowerOutletTypeType0:
    """
    Attributes:
        value (Union[None, PowerOutletTypeType0ValueType1, Unset]): * `iec-60320-c5` - C5
            * `iec-60320-c7` - C7
            * `iec-60320-c13` - C13
            * `iec-60320-c15` - C15
            * `iec-60320-c19` - C19
            * `iec-60320-c21` - C21
            * `iec-60309-p-n-e-4h` - P+N+E 4H
            * `iec-60309-p-n-e-6h` - P+N+E 6H
            * `iec-60309-p-n-e-9h` - P+N+E 9H
            * `iec-60309-2p-e-4h` - 2P+E 4H
            * `iec-60309-2p-e-6h` - 2P+E 6H
            * `iec-60309-2p-e-9h` - 2P+E 9H
            * `iec-60309-3p-e-4h` - 3P+E 4H
            * `iec-60309-3p-e-6h` - 3P+E 6H
            * `iec-60309-3p-e-9h` - 3P+E 9H
            * `iec-60309-3p-n-e-4h` - 3P+N+E 4H
            * `iec-60309-3p-n-e-6h` - 3P+N+E 6H
            * `iec-60309-3p-n-e-9h` - 3P+N+E 9H
            * `iec-60906-1` - IEC 60906-1
            * `nbr-14136-10a` - 2P+T 10A (NBR 14136)
            * `nbr-14136-20a` - 2P+T 20A (NBR 14136)
            * `nema-1-15r` - NEMA 1-15R
            * `nema-5-15r` - NEMA 5-15R
            * `nema-5-20r` - NEMA 5-20R
            * `nema-5-30r` - NEMA 5-30R
            * `nema-5-50r` - NEMA 5-50R
            * `nema-6-15r` - NEMA 6-15R
            * `nema-6-20r` - NEMA 6-20R
            * `nema-6-30r` - NEMA 6-30R
            * `nema-6-50r` - NEMA 6-50R
            * `nema-10-30r` - NEMA 10-30R
            * `nema-10-50r` - NEMA 10-50R
            * `nema-14-20r` - NEMA 14-20R
            * `nema-14-30r` - NEMA 14-30R
            * `nema-14-50r` - NEMA 14-50R
            * `nema-14-60r` - NEMA 14-60R
            * `nema-15-15r` - NEMA 15-15R
            * `nema-15-20r` - NEMA 15-20R
            * `nema-15-30r` - NEMA 15-30R
            * `nema-15-50r` - NEMA 15-50R
            * `nema-15-60r` - NEMA 15-60R
            * `nema-l1-15r` - NEMA L1-15R
            * `nema-l5-15r` - NEMA L5-15R
            * `nema-l5-20r` - NEMA L5-20R
            * `nema-l5-30r` - NEMA L5-30R
            * `nema-l5-50r` - NEMA L5-50R
            * `nema-l6-15r` - NEMA L6-15R
            * `nema-l6-20r` - NEMA L6-20R
            * `nema-l6-30r` - NEMA L6-30R
            * `nema-l6-50r` - NEMA L6-50R
            * `nema-l10-30r` - NEMA L10-30R
            * `nema-l14-20r` - NEMA L14-20R
            * `nema-l14-30r` - NEMA L14-30R
            * `nema-l14-50r` - NEMA L14-50R
            * `nema-l14-60r` - NEMA L14-60R
            * `nema-l15-20r` - NEMA L15-20R
            * `nema-l15-30r` - NEMA L15-30R
            * `nema-l15-50r` - NEMA L15-50R
            * `nema-l15-60r` - NEMA L15-60R
            * `nema-l21-20r` - NEMA L21-20R
            * `nema-l21-30r` - NEMA L21-30R
            * `nema-l22-20r` - NEMA L22-20R
            * `nema-l22-30r` - NEMA L22-30R
            * `CS6360C` - CS6360C
            * `CS6364C` - CS6364C
            * `CS8164C` - CS8164C
            * `CS8264C` - CS8264C
            * `CS8364C` - CS8364C
            * `CS8464C` - CS8464C
            * `ita-e` - ITA Type E (CEE 7/5)
            * `ita-f` - ITA Type F (CEE 7/3)
            * `ita-g` - ITA Type G (BS 1363)
            * `ita-h` - ITA Type H
            * `ita-i` - ITA Type I
            * `ita-j` - ITA Type J
            * `ita-k` - ITA Type K
            * `ita-l` - ITA Type L (CEI 23-50)
            * `ita-m` - ITA Type M (BS 546)
            * `ita-n` - ITA Type N
            * `ita-o` - ITA Type O
            * `ita-multistandard` - ITA Multistandard
            * `usb-a` - USB Type A
            * `usb-micro-b` - USB Micro B
            * `usb-c` - USB Type C
            * `molex-micro-fit-1x2` - Molex Micro-Fit 1x2
            * `molex-micro-fit-2x2` - Molex Micro-Fit 2x2
            * `molex-micro-fit-2x4` - Molex Micro-Fit 2x4
            * `dc-terminal` - DC Terminal
            * `eaton-c39` - Eaton C39
            * `hdot-cx` - HDOT Cx
            * `saf-d-grid` - Saf-D-Grid
            * `neutrik-powercon-20a` - Neutrik powerCON (20A)
            * `neutrik-powercon-32a` - Neutrik powerCON (32A)
            * `neutrik-powercon-true1` - Neutrik powerCON TRUE1
            * `neutrik-powercon-true1-top` - Neutrik powerCON TRUE1 TOP
            * `ubiquiti-smartpower` - Ubiquiti SmartPower
            * `hardwired` - Hardwired
            * `other` - Other
        label (Union[Unset, PowerOutletTypeType0Label]):
    """

    value: Union[None, PowerOutletTypeType0ValueType1, Unset] = UNSET
    label: Union[Unset, PowerOutletTypeType0Label] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value: Union[None, Unset, str]
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, PowerOutletTypeType0ValueType1):
            value = self.value.value
        else:
            value = self.value

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

        def _parse_value(data: object) -> Union[None, PowerOutletTypeType0ValueType1, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                value_type_1 = PowerOutletTypeType0ValueType1(data)

                return value_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, PowerOutletTypeType0ValueType1, Unset], data)

        value = _parse_value(d.pop("value", UNSET))

        _label = d.pop("label", UNSET)
        label: Union[Unset, PowerOutletTypeType0Label]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = PowerOutletTypeType0Label(_label)

        power_outlet_type_type_0 = cls(
            value=value,
            label=label,
        )

        power_outlet_type_type_0.additional_properties = d
        return power_outlet_type_type_0

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
