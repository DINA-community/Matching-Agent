from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BriefWirelessLANGroup")


@_attrs_define
class BriefWirelessLANGroup:
    """Extends PrimaryModelSerializer to include MPTT support.

    Attributes:
        id (int):
        url (str):
        display (str):
        name (str):
        slug (str):
        wirelesslan_count (int):  Default: 0.
        field_depth (int):
        description (Union[Unset, str]):
    """

    id: int
    url: str
    display: str
    name: str
    slug: str
    field_depth: int
    wirelesslan_count: int = 0
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        name = self.name

        slug = self.slug

        wirelesslan_count = self.wirelesslan_count

        field_depth = self.field_depth

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
                "wirelesslan_count": wirelesslan_count,
                "_depth": field_depth,
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

        wirelesslan_count = d.pop("wirelesslan_count")

        field_depth = d.pop("_depth")

        description = d.pop("description", UNSET)

        brief_wireless_lan_group = cls(
            id=id,
            url=url,
            display=display,
            name=name,
            slug=slug,
            wirelesslan_count=wirelesslan_count,
            field_depth=field_depth,
            description=description,
        )

        brief_wireless_lan_group.additional_properties = d
        return brief_wireless_lan_group

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
