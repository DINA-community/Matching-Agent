from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BriefCluster")


@_attrs_define
class BriefCluster:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display (str):
        name (str):
        description (Union[Unset, str]):
        virtualmachine_count (Union[Unset, int]):
    """

    id: int
    url: str
    display: str
    name: str
    description: Union[Unset, str] = UNSET
    virtualmachine_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        name = self.name

        description = self.description

        virtualmachine_count = self.virtualmachine_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if virtualmachine_count is not UNSET:
            field_dict["virtualmachine_count"] = virtualmachine_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        virtualmachine_count = d.pop("virtualmachine_count", UNSET)

        brief_cluster = cls(
            id=id,
            url=url,
            display=display,
            name=name,
            description=description,
            virtualmachine_count=virtualmachine_count,
        )

        brief_cluster.additional_properties = d
        return brief_cluster

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
