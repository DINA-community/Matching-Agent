from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.brief_vlan_group import BriefVLANGroup


T = TypeVar("T", bound="AvailableVLAN")


@_attrs_define
class AvailableVLAN:
    """Representation of a VLAN which does not exist in the database.

    Attributes:
        vid (int):
        group (Union['BriefVLANGroup', None]):
    """

    vid: int
    group: Union["BriefVLANGroup", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_vlan_group import BriefVLANGroup

        vid = self.vid

        group: Union[None, dict[str, Any]]
        if isinstance(self.group, BriefVLANGroup):
            group = self.group.to_dict()
        else:
            group = self.group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vid": vid,
                "group": group,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_vlan_group import BriefVLANGroup

        d = dict(src_dict)
        vid = d.pop("vid")

        def _parse_group(data: object) -> Union["BriefVLANGroup", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_1 = BriefVLANGroup.from_dict(data)

                return group_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVLANGroup", None], data)

        group = _parse_group(d.pop("group"))

        available_vlan = cls(
            vid=vid,
            group=group,
        )

        available_vlan.additional_properties = d
        return available_vlan

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
