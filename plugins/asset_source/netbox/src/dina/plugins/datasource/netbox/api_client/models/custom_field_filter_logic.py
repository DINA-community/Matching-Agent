from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_field_filter_logic_label import CustomFieldFilterLogicLabel
from ..models.custom_field_filter_logic_value import CustomFieldFilterLogicValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldFilterLogic")


@_attrs_define
class CustomFieldFilterLogic:
    """
    Attributes:
        value (Union[Unset, CustomFieldFilterLogicValue]): * `disabled` - Disabled
            * `loose` - Loose
            * `exact` - Exact
        label (Union[Unset, CustomFieldFilterLogicLabel]):
    """

    value: Union[Unset, CustomFieldFilterLogicValue] = UNSET
    label: Union[Unset, CustomFieldFilterLogicLabel] = UNSET
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
        value: Union[Unset, CustomFieldFilterLogicValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = CustomFieldFilterLogicValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, CustomFieldFilterLogicLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = CustomFieldFilterLogicLabel(_label)

        custom_field_filter_logic = cls(
            value=value,
            label=label,
        )

        custom_field_filter_logic.additional_properties = d
        return custom_field_filter_logic

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
