from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BriefManufacturer")


@_attrs_define
class BriefManufacturer:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display (str):
        name (str):
        slug (str):
        description (Union[Unset, str]):
        devicetype_count (Union[Unset, int]):
    """

    id: int
    url: str
    display: str
    name: str
    slug: str
    description: Union[Unset, str] = UNSET
    devicetype_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        name = self.name

        slug = self.slug

        description = self.description

        devicetype_count = self.devicetype_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "name": name,
                "slug": slug,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if devicetype_count is not UNSET:
            field_dict["devicetype_count"] = devicetype_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        name = d.pop("name")

        slug = d.pop("slug")

        description = d.pop("description", UNSET)

        devicetype_count = d.pop("devicetype_count", UNSET)

        brief_manufacturer = cls(
            id=id,
            url=url,
            display=display,
            name=name,
            slug=slug,
            description=description,
            devicetype_count=devicetype_count,
        )

        brief_manufacturer.additional_properties = d
        return brief_manufacturer

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
