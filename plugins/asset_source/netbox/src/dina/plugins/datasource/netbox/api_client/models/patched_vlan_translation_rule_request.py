from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedVLANTranslationRuleRequest")


@_attrs_define
class PatchedVLANTranslationRuleRequest:
    """Adds support for custom fields and tags.

    Attributes:
        policy (Union[Unset, int]):
        local_vid (Union[Unset, int]): Numeric VLAN ID (1-4094)
        remote_vid (Union[Unset, int]): Numeric VLAN ID (1-4094)
        description (Union[Unset, str]):
    """

    policy: Union[Unset, int] = UNSET
    local_vid: Union[Unset, int] = UNSET
    remote_vid: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy = self.policy

        local_vid = self.local_vid

        remote_vid = self.remote_vid

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if policy is not UNSET:
            field_dict["policy"] = policy
        if local_vid is not UNSET:
            field_dict["local_vid"] = local_vid
        if remote_vid is not UNSET:
            field_dict["remote_vid"] = remote_vid
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        policy = (
            self.policy
            if isinstance(self.policy, Unset)
            else (None, str(self.policy).encode(), "text/plain")
        )

        local_vid = (
            self.local_vid
            if isinstance(self.local_vid, Unset)
            else (None, str(self.local_vid).encode(), "text/plain")
        )

        remote_vid = (
            self.remote_vid
            if isinstance(self.remote_vid, Unset)
            else (None, str(self.remote_vid).encode(), "text/plain")
        )

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if policy is not UNSET:
            field_dict["policy"] = policy
        if local_vid is not UNSET:
            field_dict["local_vid"] = local_vid
        if remote_vid is not UNSET:
            field_dict["remote_vid"] = remote_vid
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        policy = d.pop("policy", UNSET)

        local_vid = d.pop("local_vid", UNSET)

        remote_vid = d.pop("remote_vid", UNSET)

        description = d.pop("description", UNSET)

        patched_vlan_translation_rule_request = cls(
            policy=policy,
            local_vid=local_vid,
            remote_vid=remote_vid,
            description=description,
        )

        patched_vlan_translation_rule_request.additional_properties = d
        return patched_vlan_translation_rule_request

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
