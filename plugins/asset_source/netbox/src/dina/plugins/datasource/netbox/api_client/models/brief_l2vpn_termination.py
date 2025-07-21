from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.brief_l2vpn import BriefL2VPN


T = TypeVar("T", bound="BriefL2VPNTermination")


@_attrs_define
class BriefL2VPNTermination:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display (str):
        l2vpn (BriefL2VPN): Adds support for custom fields and tags.
    """

    id: int
    url: str
    display: str
    l2vpn: "BriefL2VPN"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        l2vpn = self.l2vpn.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "l2vpn": l2vpn,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_l2vpn import BriefL2VPN

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        l2vpn = BriefL2VPN.from_dict(d.pop("l2vpn"))

        brief_l2vpn_termination = cls(
            id=id,
            url=url,
            display=display,
            l2vpn=l2vpn,
        )

        brief_l2vpn_termination.additional_properties = d
        return brief_l2vpn_termination

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
