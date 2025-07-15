import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.brief_fhrp_group import BriefFHRPGroup


T = TypeVar("T", bound="FHRPGroupAssignment")


@_attrs_define
class FHRPGroupAssignment:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display (str):
        group (BriefFHRPGroup): Adds support for custom fields and tags.
        interface_type (str):
        interface_id (int):
        interface (Any):
        priority (int):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
    """

    id: int
    url: str
    display: str
    group: "BriefFHRPGroup"
    interface_type: str
    interface_id: int
    interface: Any
    priority: int
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        group = self.group.to_dict()

        interface_type = self.interface_type

        interface_id = self.interface_id

        interface = self.interface

        priority = self.priority

        created: Union[None, str]
        if isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        last_updated: Union[None, str]
        if isinstance(self.last_updated, datetime.datetime):
            last_updated = self.last_updated.isoformat()
        else:
            last_updated = self.last_updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "group": group,
                "interface_type": interface_type,
                "interface_id": interface_id,
                "interface": interface,
                "priority": priority,
                "created": created,
                "last_updated": last_updated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_fhrp_group import BriefFHRPGroup

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        group = BriefFHRPGroup.from_dict(d.pop("group"))

        interface_type = d.pop("interface_type")

        interface_id = d.pop("interface_id")

        interface = d.pop("interface")

        priority = d.pop("priority")

        def _parse_created(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = isoparse(data)

                return created_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        created = _parse_created(d.pop("created"))

        def _parse_last_updated(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_type_0 = isoparse(data)

                return last_updated_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_updated = _parse_last_updated(d.pop("last_updated"))

        fhrp_group_assignment = cls(
            id=id,
            url=url,
            display=display,
            group=group,
            interface_type=interface_type,
            interface_id=interface_id,
            interface=interface,
            priority=priority,
            created=created,
            last_updated=last_updated,
        )

        fhrp_group_assignment.additional_properties = d
        return fhrp_group_assignment

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
