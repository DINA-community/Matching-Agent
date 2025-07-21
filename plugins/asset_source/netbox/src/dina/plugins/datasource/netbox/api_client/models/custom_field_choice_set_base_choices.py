from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_field_choice_set_base_choices_label import (
    CustomFieldChoiceSetBaseChoicesLabel,
)
from ..models.custom_field_choice_set_base_choices_value import (
    CustomFieldChoiceSetBaseChoicesValue,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldChoiceSetBaseChoices")


@_attrs_define
class CustomFieldChoiceSetBaseChoices:
    """
    Attributes:
        value (Union[Unset, CustomFieldChoiceSetBaseChoicesValue]): * `IATA` - IATA (Airport codes)
            * `ISO_3166` - ISO 3166 (Country codes)
            * `UN_LOCODE` - UN/LOCODE (Location codes)
        label (Union[Unset, CustomFieldChoiceSetBaseChoicesLabel]):
    """

    value: Union[Unset, CustomFieldChoiceSetBaseChoicesValue] = UNSET
    label: Union[Unset, CustomFieldChoiceSetBaseChoicesLabel] = UNSET
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
        value: Union[Unset, CustomFieldChoiceSetBaseChoicesValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = CustomFieldChoiceSetBaseChoicesValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, CustomFieldChoiceSetBaseChoicesLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = CustomFieldChoiceSetBaseChoicesLabel(_label)

        custom_field_choice_set_base_choices = cls(
            value=value,
            label=label,
        )

        custom_field_choice_set_base_choices.additional_properties = d
        return custom_field_choice_set_base_choices

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
