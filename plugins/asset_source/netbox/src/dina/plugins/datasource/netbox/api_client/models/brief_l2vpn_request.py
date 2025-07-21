from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.brief_l2vpn_request_type import BriefL2VPNRequestType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BriefL2VPNRequest")


@_attrs_define
class BriefL2VPNRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str):
        slug (str):
        identifier (Union[None, Unset, int]):
        type_ (Union[Unset, BriefL2VPNRequestType]): * `vpws` - VPWS
            * `vpls` - VPLS
            * `vxlan` - VXLAN
            * `vxlan-evpn` - VXLAN-EVPN
            * `mpls-evpn` - MPLS EVPN
            * `pbb-evpn` - PBB EVPN
            * `evpn-vpws` - EVPN VPWS
            * `epl` - EPL
            * `evpl` - EVPL
            * `ep-lan` - Ethernet Private LAN
            * `evp-lan` - Ethernet Virtual Private LAN
            * `ep-tree` - Ethernet Private Tree
            * `evp-tree` - Ethernet Virtual Private Tree
            * `spb` - SPB
        description (Union[Unset, str]):
    """

    name: str
    slug: str
    identifier: Union[None, Unset, int] = UNSET
    type_: Union[Unset, BriefL2VPNRequestType] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        identifier: Union[None, Unset, int]
        if isinstance(self.identifier, Unset):
            identifier = UNSET
        else:
            identifier = self.identifier

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
            }
        )
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if type_ is not UNSET:
            field_dict["type"] = type_
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        def _parse_identifier(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        identifier = _parse_identifier(d.pop("identifier", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BriefL2VPNRequestType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BriefL2VPNRequestType(_type_)

        description = d.pop("description", UNSET)

        brief_l2vpn_request = cls(
            name=name,
            slug=slug,
            identifier=identifier,
            type_=type_,
            description=description,
        )

        brief_l2vpn_request.additional_properties = d
        return brief_l2vpn_request

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
