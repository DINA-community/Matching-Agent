from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.console_server_port_template_type_label import ConsoleServerPortTemplateTypeLabel
from ..models.console_server_port_template_type_value import ConsoleServerPortTemplateTypeValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsoleServerPortTemplateType")


@_attrs_define
class ConsoleServerPortTemplateType:
    """
    Attributes:
        value (Union[Unset, ConsoleServerPortTemplateTypeValue]): * `de-9` - DE-9
            * `db-25` - DB-25
            * `rj-11` - RJ-11
            * `rj-12` - RJ-12
            * `rj-45` - RJ-45
            * `mini-din-8` - Mini-DIN 8
            * `usb-a` - USB Type A
            * `usb-b` - USB Type B
            * `usb-c` - USB Type C
            * `usb-mini-a` - USB Mini A
            * `usb-mini-b` - USB Mini B
            * `usb-micro-a` - USB Micro A
            * `usb-micro-b` - USB Micro B
            * `usb-micro-ab` - USB Micro AB
            * `other` - Other
        label (Union[Unset, ConsoleServerPortTemplateTypeLabel]):
    """

    value: Union[Unset, ConsoleServerPortTemplateTypeValue] = UNSET
    label: Union[Unset, ConsoleServerPortTemplateTypeLabel] = UNSET
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
        value: Union[Unset, ConsoleServerPortTemplateTypeValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = ConsoleServerPortTemplateTypeValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, ConsoleServerPortTemplateTypeLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = ConsoleServerPortTemplateTypeLabel(_label)

        console_server_port_template_type = cls(
            value=value,
            label=label,
        )

        console_server_port_template_type.additional_properties = d
        return console_server_port_template_type

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
