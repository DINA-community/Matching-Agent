from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_template_protocol_label import ServiceTemplateProtocolLabel
from ..models.service_template_protocol_value import ServiceTemplateProtocolValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceTemplateProtocol")


@_attrs_define
class ServiceTemplateProtocol:
    """
    Attributes:
        value (Union[Unset, ServiceTemplateProtocolValue]): * `tcp` - TCP
            * `udp` - UDP
            * `sctp` - SCTP
        label (Union[Unset, ServiceTemplateProtocolLabel]):
    """

    value: Union[Unset, ServiceTemplateProtocolValue] = UNSET
    label: Union[Unset, ServiceTemplateProtocolLabel] = UNSET
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
        value: Union[Unset, ServiceTemplateProtocolValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = ServiceTemplateProtocolValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, ServiceTemplateProtocolLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = ServiceTemplateProtocolLabel(_label)

        service_template_protocol = cls(
            value=value,
            label=label,
        )

        service_template_protocol.additional_properties = d
        return service_template_protocol

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
