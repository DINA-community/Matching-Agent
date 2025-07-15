from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.brief_fhrp_group_protocol import BriefFHRPGroupProtocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="BriefFHRPGroup")


@_attrs_define
class BriefFHRPGroup:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display (str):
        protocol (BriefFHRPGroupProtocol): * `vrrp2` - VRRPv2
            * `vrrp3` - VRRPv3
            * `carp` - CARP
            * `clusterxl` - ClusterXL
            * `hsrp` - HSRP
            * `glbp` - GLBP
            * `other` - Other
        group_id (int):
        description (Union[Unset, str]):
    """

    id: int
    url: str
    display: str
    protocol: BriefFHRPGroupProtocol
    group_id: int
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        protocol = self.protocol.value

        group_id = self.group_id

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "protocol": protocol,
                "group_id": group_id,
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

        protocol = BriefFHRPGroupProtocol(d.pop("protocol"))

        group_id = d.pop("group_id")

        description = d.pop("description", UNSET)

        brief_fhrp_group = cls(
            id=id,
            url=url,
            display=display,
            protocol=protocol,
            group_id=group_id,
            description=description,
        )

        brief_fhrp_group.additional_properties = d
        return brief_fhrp_group

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
