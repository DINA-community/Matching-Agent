from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_ip_address_family import BriefIPAddressFamily


T = TypeVar("T", bound="BriefIPAddress")


@_attrs_define
class BriefIPAddress:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display (str):
        family (BriefIPAddressFamily):
        address (str):
        description (Union[Unset, str]):
    """

    id: int
    url: str
    display: str
    family: "BriefIPAddressFamily"
    address: str
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        family = self.family.to_dict()

        address = self.address

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "family": family,
                "address": address,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_ip_address_family import BriefIPAddressFamily

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        family = BriefIPAddressFamily.from_dict(d.pop("family"))

        address = d.pop("address")

        description = d.pop("description", UNSET)

        brief_ip_address = cls(
            id=id,
            url=url,
            display=display,
            family=family,
            address=address,
            description=description,
        )

        brief_ip_address.additional_properties = d
        return brief_ip_address

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
