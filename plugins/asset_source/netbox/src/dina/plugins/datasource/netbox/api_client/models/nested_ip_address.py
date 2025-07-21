from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NestedIPAddress")


@_attrs_define
class NestedIPAddress:
    """Represents an object related through a ForeignKey field. On write, it accepts a primary key (PK) value or a
    dictionary of attributes which can be used to uniquely identify the related object. This class should be
    subclassed to return a full representation of the related object on read.

        Attributes:
            id (int):
            url (str):
            display_url (str):
            display (str):
            family (int):
            address (str):
    """

    id: int
    url: str
    display_url: str
    display: str
    family: int
    address: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        family = self.family

        address = self.address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "family": family,
                "address": address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        family = d.pop("family")

        address = d.pop("address")

        nested_ip_address = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            family=family,
            address=address,
        )

        nested_ip_address.additional_properties = d
        return nested_ip_address

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
