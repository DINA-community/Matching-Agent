from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vlan_translation_rule import VLANTranslationRule


T = TypeVar("T", bound="VLANTranslationPolicy")


@_attrs_define
class VLANTranslationPolicy:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display (str):
        name (str):
        rules (list['VLANTranslationRule']):
        description (Union[Unset, str]):
    """

    id: int
    url: str
    display: str
    name: str
    rules: list["VLANTranslationRule"]
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        name = self.name

        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "name": name,
                "rules": rules,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vlan_translation_rule import VLANTranslationRule

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        name = d.pop("name")

        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = VLANTranslationRule.from_dict(rules_item_data)

            rules.append(rules_item)

        description = d.pop("description", UNSET)

        vlan_translation_policy = cls(
            id=id,
            url=url,
            display=display,
            name=name,
            rules=rules,
            description=description,
        )

        vlan_translation_policy.additional_properties = d
        return vlan_translation_policy

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
