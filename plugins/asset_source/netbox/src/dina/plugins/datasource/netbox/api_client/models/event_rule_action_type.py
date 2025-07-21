from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_rule_action_type_label import EventRuleActionTypeLabel
from ..models.event_rule_action_type_value import EventRuleActionTypeValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventRuleActionType")


@_attrs_define
class EventRuleActionType:
    """
    Attributes:
        value (Union[Unset, EventRuleActionTypeValue]): * `webhook` - Webhook
            * `script` - Script
            * `notification` - Notification
        label (Union[Unset, EventRuleActionTypeLabel]):
    """

    value: Union[Unset, EventRuleActionTypeValue] = UNSET
    label: Union[Unset, EventRuleActionTypeLabel] = UNSET
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
        value: Union[Unset, EventRuleActionTypeValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = EventRuleActionTypeValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, EventRuleActionTypeLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = EventRuleActionTypeLabel(_label)

        event_rule_action_type = cls(
            value=value,
            label=label,
        )

        event_rule_action_type.additional_properties = d
        return event_rule_action_type

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
