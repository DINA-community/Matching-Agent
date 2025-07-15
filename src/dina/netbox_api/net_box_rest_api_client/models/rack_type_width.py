from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rack_type_width_label import RackTypeWidthLabel
from ..models.rack_type_width_value import RackTypeWidthValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="RackTypeWidth")


@_attrs_define
class RackTypeWidth:
    """
    Attributes:
        value (Union[Unset, RackTypeWidthValue]): * `10` - 10 inches
            * `19` - 19 inches
            * `21` - 21 inches
            * `23` - 23 inches
        label (Union[Unset, RackTypeWidthLabel]):
    """

    value: Union[Unset, RackTypeWidthValue] = UNSET
    label: Union[Unset, RackTypeWidthLabel] = UNSET
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
        value: Union[Unset, RackTypeWidthValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = RackTypeWidthValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, RackTypeWidthLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = RackTypeWidthLabel(_label)

        rack_type_width = cls(
            value=value,
            label=label,
        )

        rack_type_width.additional_properties = d
        return rack_type_width

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
