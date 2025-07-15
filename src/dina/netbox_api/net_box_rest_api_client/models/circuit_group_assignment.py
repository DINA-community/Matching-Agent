import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_circuit_group import BriefCircuitGroup
    from ..models.circuit_group_assignment_priority import CircuitGroupAssignmentPriority
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="CircuitGroupAssignment")


@_attrs_define
class CircuitGroupAssignment:
    """Base serializer for group assignments under CircuitSerializer.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        group (BriefCircuitGroup): Adds support for custom fields and tags.
        member_type (str):
        member_id (int):
        member (Any):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        priority (Union[Unset, CircuitGroupAssignmentPriority]):
        tags (Union[Unset, list['NestedTag']]):
    """

    id: int
    url: str
    display_url: str
    display: str
    group: "BriefCircuitGroup"
    member_type: str
    member_id: int
    member: Any
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    priority: Union[Unset, "CircuitGroupAssignmentPriority"] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        group = self.group.to_dict()

        member_type = self.member_type

        member_id = self.member_id

        member = self.member

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

        priority: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        tags: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "group": group,
                "member_type": member_type,
                "member_id": member_id,
                "member": member,
                "created": created,
                "last_updated": last_updated,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_circuit_group import BriefCircuitGroup
        from ..models.circuit_group_assignment_priority import CircuitGroupAssignmentPriority
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        group = BriefCircuitGroup.from_dict(d.pop("group"))

        member_type = d.pop("member_type")

        member_id = d.pop("member_id")

        member = d.pop("member")

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

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, CircuitGroupAssignmentPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = CircuitGroupAssignmentPriority.from_dict(_priority)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        circuit_group_assignment = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            group=group,
            member_type=member_type,
            member_id=member_id,
            member=member,
            created=created,
            last_updated=last_updated,
            priority=priority,
            tags=tags,
        )

        circuit_group_assignment.additional_properties = d
        return circuit_group_assignment

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
