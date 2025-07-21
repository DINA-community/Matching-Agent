from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_device import NestedDevice


T = TypeVar("T", bound="BriefVirtualChassis")


@_attrs_define
class BriefVirtualChassis:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display (str):
        name (str):
        member_count (int):
        master (Union['NestedDevice', None, Unset]):
        description (Union[Unset, str]):
    """

    id: int
    url: str
    display: str
    name: str
    member_count: int
    master: Union["NestedDevice", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.nested_device import NestedDevice

        id = self.id

        url = self.url

        display = self.display

        name = self.name

        member_count = self.member_count

        master: Union[None, Unset, dict[str, Any]]
        if isinstance(self.master, Unset):
            master = UNSET
        elif isinstance(self.master, NestedDevice):
            master = self.master.to_dict()
        else:
            master = self.master

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "name": name,
                "member_count": member_count,
            }
        )
        if master is not UNSET:
            field_dict["master"] = master
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nested_device import NestedDevice

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        name = d.pop("name")

        member_count = d.pop("member_count")

        def _parse_master(data: object) -> Union["NestedDevice", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                master_type_1 = NestedDevice.from_dict(data)

                return master_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NestedDevice", None, Unset], data)

        master = _parse_master(d.pop("master", UNSET))

        description = d.pop("description", UNSET)

        brief_virtual_chassis = cls(
            id=id,
            url=url,
            display=display,
            name=name,
            member_count=member_count,
            master=master,
            description=description,
        )

        brief_virtual_chassis.additional_properties = d
        return brief_virtual_chassis

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
