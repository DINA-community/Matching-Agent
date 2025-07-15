from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cable_length_unit_type_0_label import CableLengthUnitType0Label
from ..models.cable_length_unit_type_0_value_type_1 import CableLengthUnitType0ValueType1
from ..types import UNSET, Unset

T = TypeVar("T", bound="CableLengthUnitType0")


@_attrs_define
class CableLengthUnitType0:
    """
    Attributes:
        value (Union[CableLengthUnitType0ValueType1, None, Unset]): * `km` - Kilometers
            * `m` - Meters
            * `cm` - Centimeters
            * `mi` - Miles
            * `ft` - Feet
            * `in` - Inches
        label (Union[Unset, CableLengthUnitType0Label]):
    """

    value: Union[CableLengthUnitType0ValueType1, None, Unset] = UNSET
    label: Union[Unset, CableLengthUnitType0Label] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value: Union[None, Unset, str]
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, CableLengthUnitType0ValueType1):
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

        def _parse_value(data: object) -> Union[CableLengthUnitType0ValueType1, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                value_type_1 = CableLengthUnitType0ValueType1(data)

                return value_type_1
            except:  # noqa: E722
                pass
            return cast(Union[CableLengthUnitType0ValueType1, None, Unset], data)

        value = _parse_value(d.pop("value", UNSET))

        _label = d.pop("label", UNSET)
        label: Union[Unset, CableLengthUnitType0Label]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = CableLengthUnitType0Label(_label)

        cable_length_unit_type_0 = cls(
            value=value,
            label=label,
        )

        cable_length_unit_type_0.additional_properties = d
        return cable_length_unit_type_0

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
