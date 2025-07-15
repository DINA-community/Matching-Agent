from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ike_policy_version_label import IKEPolicyVersionLabel
from ..models.ike_policy_version_value import IKEPolicyVersionValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="IKEPolicyVersion")


@_attrs_define
class IKEPolicyVersion:
    """
    Attributes:
        value (Union[Unset, IKEPolicyVersionValue]): * `1` - IKEv1
            * `2` - IKEv2
        label (Union[Unset, IKEPolicyVersionLabel]):
    """

    value: Union[Unset, IKEPolicyVersionValue] = UNSET
    label: Union[Unset, IKEPolicyVersionLabel] = UNSET
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
        value: Union[Unset, IKEPolicyVersionValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = IKEPolicyVersionValue(_value)

        _label = d.pop("label", UNSET)
        label: Union[Unset, IKEPolicyVersionLabel]
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = IKEPolicyVersionLabel(_label)

        ike_policy_version = cls(
            value=value,
            label=label,
        )

        ike_policy_version.additional_properties = d
        return ike_policy_version

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
