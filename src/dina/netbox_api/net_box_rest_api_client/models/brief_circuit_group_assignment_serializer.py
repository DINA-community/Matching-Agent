from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_circuit_group import BriefCircuitGroup
    from ..models.brief_circuit_group_assignment_serializer_priority import (
        BriefCircuitGroupAssignmentSerializerPriority,
    )


T = TypeVar("T", bound="BriefCircuitGroupAssignmentSerializer")


@_attrs_define
class BriefCircuitGroupAssignmentSerializer:
    """Base serializer for group assignments under CircuitSerializer.

    Attributes:
        id (int):
        url (str):
        display (str):
        group (BriefCircuitGroup): Adds support for custom fields and tags.
        priority (Union[Unset, BriefCircuitGroupAssignmentSerializerPriority]):
    """

    id: int
    url: str
    display: str
    group: "BriefCircuitGroup"
    priority: Union[Unset, "BriefCircuitGroupAssignmentSerializerPriority"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        group = self.group.to_dict()

        priority: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "group": group,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_circuit_group import BriefCircuitGroup
        from ..models.brief_circuit_group_assignment_serializer_priority import (
            BriefCircuitGroupAssignmentSerializerPriority,
        )

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        group = BriefCircuitGroup.from_dict(d.pop("group"))

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, BriefCircuitGroupAssignmentSerializerPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = BriefCircuitGroupAssignmentSerializerPriority.from_dict(_priority)

        brief_circuit_group_assignment_serializer = cls(
            id=id,
            url=url,
            display=display,
            group=group,
            priority=priority,
        )

        brief_circuit_group_assignment_serializer.additional_properties = d
        return brief_circuit_group_assignment_serializer

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
