from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BriefRole")


@_attrs_define
class BriefRole:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display (str):
        name (str):
        slug (str):
        prefix_count (int):
        vlan_count (int):
        description (Union[Unset, str]):
    """

    id: int
    url: str
    display: str
    name: str
    slug: str
    prefix_count: int
    vlan_count: int
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        name = self.name

        slug = self.slug

        prefix_count = self.prefix_count

        vlan_count = self.vlan_count

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "name": name,
                "slug": slug,
                "prefix_count": prefix_count,
                "vlan_count": vlan_count,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        name = d.pop("name")

        slug = d.pop("slug")

        prefix_count = d.pop("prefix_count")

        vlan_count = d.pop("vlan_count")

        description = d.pop("description", UNSET)

        brief_role = cls(
            id=id,
            url=url,
            display=display,
            name=name,
            slug=slug,
            prefix_count=prefix_count,
            vlan_count=vlan_count,
            description=description,
        )

        brief_role.additional_properties = d
        return brief_role

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
