from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BriefRIR")


@_attrs_define
class BriefRIR:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display (str):
        name (str):
        slug (str):
        aggregate_count (int):
        description (Union[Unset, str]):
    """

    id: int
    url: str
    display: str
    name: str
    slug: str
    aggregate_count: int
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        name = self.name

        slug = self.slug

        aggregate_count = self.aggregate_count

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
                "aggregate_count": aggregate_count,
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

        aggregate_count = d.pop("aggregate_count")

        description = d.pop("description", UNSET)

        brief_rir = cls(
            id=id,
            url=url,
            display=display,
            name=name,
            slug=slug,
            aggregate_count=aggregate_count,
            description=description,
        )

        brief_rir.additional_properties = d
        return brief_rir

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
