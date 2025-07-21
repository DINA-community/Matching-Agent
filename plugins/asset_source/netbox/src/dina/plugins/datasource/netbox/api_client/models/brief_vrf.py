from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BriefVRF")


@_attrs_define
class BriefVRF:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display (str):
        name (str):
        prefix_count (int):
        rd (Union[None, Unset, str]): Unique route distinguisher (as defined in RFC 4364)
        description (Union[Unset, str]):
    """

    id: int
    url: str
    display: str
    name: str
    prefix_count: int
    rd: Union[None, Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        name = self.name

        prefix_count = self.prefix_count

        rd: Union[None, Unset, str]
        if isinstance(self.rd, Unset):
            rd = UNSET
        else:
            rd = self.rd

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "name": name,
                "prefix_count": prefix_count,
            }
        )
        if rd is not UNSET:
            field_dict["rd"] = rd
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

        prefix_count = d.pop("prefix_count")

        def _parse_rd(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rd = _parse_rd(d.pop("rd", UNSET))

        description = d.pop("description", UNSET)

        brief_vrf = cls(
            id=id,
            url=url,
            display=display,
            name=name,
            prefix_count=prefix_count,
            rd=rd,
            description=description,
        )

        brief_vrf.additional_properties = d
        return brief_vrf

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
