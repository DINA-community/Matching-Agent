from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrontPortRearPort")


@_attrs_define
class FrontPortRearPort:
    """NestedRearPortSerializer but with parent device omitted (since front and rear ports must belong to same device)

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        name (str):
        label (Union[Unset, str]): Physical label
        description (Union[Unset, str]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

        label = self.label

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "name": name,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        front_port_rear_port = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            label=label,
            description=description,
        )

        front_port_rear_port.additional_properties = d
        return front_port_rear_port

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
