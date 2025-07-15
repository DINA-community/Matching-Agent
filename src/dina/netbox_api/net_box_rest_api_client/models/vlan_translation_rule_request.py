from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VLANTranslationRuleRequest")


@_attrs_define
class VLANTranslationRuleRequest:
    """Adds support for custom fields and tags.

    Attributes:
        policy (int):
        local_vid (int): Numeric VLAN ID (1-4094)
        remote_vid (int): Numeric VLAN ID (1-4094)
        description (Union[Unset, str]):
    """

    policy: int
    local_vid: int
    remote_vid: int
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        policy = self.policy

        local_vid = self.local_vid

        remote_vid = self.remote_vid

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "policy": policy,
                "local_vid": local_vid,
                "remote_vid": remote_vid,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        policy = (None, str(self.policy).encode(), "text/plain")

        local_vid = (None, str(self.local_vid).encode(), "text/plain")

        remote_vid = (None, str(self.remote_vid).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "policy": policy,
                "local_vid": local_vid,
                "remote_vid": remote_vid,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        policy = d.pop("policy")

        local_vid = d.pop("local_vid")

        remote_vid = d.pop("remote_vid")

        description = d.pop("description", UNSET)

        vlan_translation_rule_request = cls(
            policy=policy,
            local_vid=local_vid,
            remote_vid=remote_vid,
            description=description,
        )

        vlan_translation_rule_request.additional_properties = d
        return vlan_translation_rule_request

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
