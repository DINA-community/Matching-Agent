from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_field_ui_visible_label import CustomFieldUiVisibleLabel
from ..models.custom_field_ui_visible_value import CustomFieldUiVisibleValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldUiVisible")


@_attrs_define
class CustomFieldUiVisible:
    """
    Attributes:
        value (Union[Unset, CustomFieldUiVisibleValue]): * `always` - Always
            * `if-set` - If set
            * `hidden` - Hidden
        label (Union[Unset, CustomFieldUiVisibleLabel]):
    """

    value: Union[Unset, CustomFieldUiVisibleValue] = UNSET
    label: Union[Unset, CustomFieldUiVisibleLabel] = UNSET
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
        value: Union[Unset, CustomFieldUiVisibleValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = CustomFieldUiVisibleValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, CustomFieldUiVisibleLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = CustomFieldUiVisibleLabel(_label)

        custom_field_ui_visible = cls(
            value=value,
            label=label,
        )

        custom_field_ui_visible.additional_properties = d
        return custom_field_ui_visible

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
