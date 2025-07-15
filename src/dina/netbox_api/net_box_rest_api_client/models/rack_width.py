from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rack_width_label import RackWidthLabel
from ..models.rack_width_value import RackWidthValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="RackWidth")


@_attrs_define
class RackWidth:
    """
    Attributes:
        value (Union[Unset, RackWidthValue]): * `10` - 10 inches
            * `19` - 19 inches
            * `21` - 21 inches
            * `23` - 23 inches
        label (Union[Unset, RackWidthLabel]):
    """

    value: Union[Unset, RackWidthValue] = UNSET
    label: Union[Unset, RackWidthLabel] = UNSET
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
        value: Union[Unset, RackWidthValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = RackWidthValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, RackWidthLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = RackWidthLabel(_label)

        rack_width = cls(
            value=value,
            label=label,
        )

        rack_width.additional_properties = d
        return rack_width

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
