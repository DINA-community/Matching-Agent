from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.interface_template_poe_type_type_0_label import (
    InterfaceTemplatePoeTypeType0Label,
)
from ..models.interface_template_poe_type_type_0_value_type_1 import (
    InterfaceTemplatePoeTypeType0ValueType1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="InterfaceTemplatePoeTypeType0")


@_attrs_define
class InterfaceTemplatePoeTypeType0:
    """
    Attributes:
        value (Union[InterfaceTemplatePoeTypeType0ValueType1, None, Unset]): * `type1-ieee802.3af` - 802.3af (Type 1)
            * `type2-ieee802.3at` - 802.3at (Type 2)
            * `type3-ieee802.3bt` - 802.3bt (Type 3)
            * `type4-ieee802.3bt` - 802.3bt (Type 4)
            * `passive-24v-2pair` - Passive 24V (2-pair)
            * `passive-24v-4pair` - Passive 24V (4-pair)
            * `passive-48v-2pair` - Passive 48V (2-pair)
            * `passive-48v-4pair` - Passive 48V (4-pair)
        label (Union[Unset, InterfaceTemplatePoeTypeType0Label]):
    """

    value: Union[InterfaceTemplatePoeTypeType0ValueType1, None, Unset] = UNSET
    label: Union[Unset, InterfaceTemplatePoeTypeType0Label] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value: Union[None, Unset, str]
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, InterfaceTemplatePoeTypeType0ValueType1):
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

        def _parse_value(
            data: object,
        ) -> Union[InterfaceTemplatePoeTypeType0ValueType1, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                value_type_1 = InterfaceTemplatePoeTypeType0ValueType1(data)

                return value_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[InterfaceTemplatePoeTypeType0ValueType1, None, Unset], data
            )

        value = _parse_value(d.pop("value", UNSET))

        _label = d.pop("label", UNSET)
        label: Union[Unset, InterfaceTemplatePoeTypeType0Label]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = InterfaceTemplatePoeTypeType0Label(_label)

        interface_template_poe_type_type_0 = cls(
            value=value,
            label=label,
        )

        interface_template_poe_type_type_0.additional_properties = d
        return interface_template_poe_type_type_0

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
