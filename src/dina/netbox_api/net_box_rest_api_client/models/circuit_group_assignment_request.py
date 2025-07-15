from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.circuit_group_assignment_request_priority import CircuitGroupAssignmentRequestPriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_circuit_group_request import BriefCircuitGroupRequest
    from ..models.nested_tag_request import NestedTagRequest


T = TypeVar("T", bound="CircuitGroupAssignmentRequest")


@_attrs_define
class CircuitGroupAssignmentRequest:
    """Base serializer for group assignments under CircuitSerializer.

    Attributes:
        group (Union['BriefCircuitGroupRequest', int]):
        member_type (str):
        member_id (int):
        priority (Union[Unset, CircuitGroupAssignmentRequestPriority]): * `primary` - Primary
            * `secondary` - Secondary
            * `tertiary` - Tertiary
            * `inactive` - Inactive
        tags (Union[Unset, list['NestedTagRequest']]):
    """

    group: Union["BriefCircuitGroupRequest", int]
    member_type: str
    member_id: int
    priority: Union[Unset, CircuitGroupAssignmentRequestPriority] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_circuit_group_request import BriefCircuitGroupRequest

        group: Union[dict[str, Any], int]
        if isinstance(self.group, BriefCircuitGroupRequest):
            group = self.group.to_dict()
        else:
            group = self.group

        member_type = self.member_type

        member_id = self.member_id

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

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
                "group": group,
                "member_type": member_type,
                "member_id": member_id,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_circuit_group_request import BriefCircuitGroupRequest
        from ..models.nested_tag_request import NestedTagRequest

        d = dict(src_dict)

        def _parse_group(data: object) -> Union["BriefCircuitGroupRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_1 = BriefCircuitGroupRequest.from_dict(data)

                return group_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefCircuitGroupRequest", int], data)

        group = _parse_group(d.pop("group"))

        member_type = d.pop("member_type")

        member_id = d.pop("member_id")

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, CircuitGroupAssignmentRequestPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = CircuitGroupAssignmentRequestPriority(_priority)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        circuit_group_assignment_request = cls(
            group=group,
            member_type=member_type,
            member_id=member_id,
            priority=priority,
            tags=tags,
        )

        circuit_group_assignment_request.additional_properties = d
        return circuit_group_assignment_request

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
