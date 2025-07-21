import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_writable_circuit_group_assignment_request_priority_type_1 import (
    PatchedWritableCircuitGroupAssignmentRequestPriorityType1,
)
from ..models.patched_writable_circuit_group_assignment_request_priority_type_2_type_1 import (
    PatchedWritableCircuitGroupAssignmentRequestPriorityType2Type1,
)
from ..models.patched_writable_circuit_group_assignment_request_priority_type_3_type_1 import (
    PatchedWritableCircuitGroupAssignmentRequestPriorityType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_circuit_group_request import BriefCircuitGroupRequest
    from ..models.nested_tag_request import NestedTagRequest


T = TypeVar("T", bound="PatchedWritableCircuitGroupAssignmentRequest")


@_attrs_define
class PatchedWritableCircuitGroupAssignmentRequest:
    """Base serializer for group assignments under CircuitSerializer.

    Attributes:
        group (Union['BriefCircuitGroupRequest', Unset, int]):
        member_type (Union[Unset, str]):
        member_id (Union[Unset, int]):
        priority (Union[None, PatchedWritableCircuitGroupAssignmentRequestPriorityType1,
            PatchedWritableCircuitGroupAssignmentRequestPriorityType2Type1,
            PatchedWritableCircuitGroupAssignmentRequestPriorityType3Type1, Unset]): * `primary` - Primary
            * `secondary` - Secondary
            * `tertiary` - Tertiary
            * `inactive` - Inactive
        tags (Union[Unset, list['NestedTagRequest']]):
    """

    group: Union["BriefCircuitGroupRequest", Unset, int] = UNSET
    member_type: Union[Unset, str] = UNSET
    member_id: Union[Unset, int] = UNSET
    priority: Union[
        None,
        PatchedWritableCircuitGroupAssignmentRequestPriorityType1,
        PatchedWritableCircuitGroupAssignmentRequestPriorityType2Type1,
        PatchedWritableCircuitGroupAssignmentRequestPriorityType3Type1,
        Unset,
    ] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_circuit_group_request import BriefCircuitGroupRequest

        group: Union[Unset, dict[str, Any], int]
        if isinstance(self.group, Unset):
            group = UNSET
        elif isinstance(self.group, BriefCircuitGroupRequest):
            group = self.group.to_dict()
        else:
            group = self.group

        member_type = self.member_type

        member_id = self.member_id

        priority: Union[None, Unset, str]
        if isinstance(self.priority, Unset):
            priority = UNSET
        elif isinstance(
            self.priority, PatchedWritableCircuitGroupAssignmentRequestPriorityType1
        ):
            priority = self.priority.value
        elif isinstance(
            self.priority,
            PatchedWritableCircuitGroupAssignmentRequestPriorityType2Type1,
        ):
            priority = self.priority.value
        elif isinstance(
            self.priority,
            PatchedWritableCircuitGroupAssignmentRequestPriorityType3Type1,
        ):
            priority = self.priority.value
        else:
            priority = self.priority

        tags: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group
        if member_type is not UNSET:
            field_dict["member_type"] = member_type
        if member_id is not UNSET:
            field_dict["member_id"] = member_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        group: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.group, Unset):
            group = UNSET
        elif isinstance(self.group, int):
            group = (None, str(self.group).encode(), "text/plain")
        else:
            group = (
                None,
                json.dumps(self.group.to_dict()).encode(),
                "application/json",
            )

        member_type = (
            self.member_type
            if isinstance(self.member_type, Unset)
            else (None, str(self.member_type).encode(), "text/plain")
        )

        member_id = (
            self.member_id
            if isinstance(self.member_id, Unset)
            else (None, str(self.member_id).encode(), "text/plain")
        )

        priority: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.priority, Unset):
            priority = UNSET
        elif isinstance(self.priority, None):
            priority = (None, str(self.priority).encode(), "text/plain")
        elif isinstance(
            self.priority, PatchedWritableCircuitGroupAssignmentRequestPriorityType1
        ):
            priority = (None, str(self.priority.value).encode(), "text/plain")
        elif isinstance(self.priority, None):
            priority = (None, str(self.priority).encode(), "text/plain")
        elif isinstance(
            self.priority,
            PatchedWritableCircuitGroupAssignmentRequestPriorityType2Type1,
        ):
            priority = (None, str(self.priority.value).encode(), "text/plain")
        elif isinstance(self.priority, None):
            priority = (None, str(self.priority).encode(), "text/plain")
        else:
            priority = (None, str(self.priority.value).encode(), "text/plain")

        tags: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tags, Unset):
            _temp_tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                _temp_tags.append(tags_item)
            tags = (None, json.dumps(_temp_tags).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group
        if member_type is not UNSET:
            field_dict["member_type"] = member_type
        if member_id is not UNSET:
            field_dict["member_id"] = member_id
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

        def _parse_group(data: object) -> Union["BriefCircuitGroupRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_1 = BriefCircuitGroupRequest.from_dict(data)

                return group_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefCircuitGroupRequest", Unset, int], data)

        group = _parse_group(d.pop("group", UNSET))

        member_type = d.pop("member_type", UNSET)

        member_id = d.pop("member_id", UNSET)

        def _parse_priority(
            data: object,
        ) -> Union[
            None,
            PatchedWritableCircuitGroupAssignmentRequestPriorityType1,
            PatchedWritableCircuitGroupAssignmentRequestPriorityType2Type1,
            PatchedWritableCircuitGroupAssignmentRequestPriorityType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_1 = (
                    PatchedWritableCircuitGroupAssignmentRequestPriorityType1(data)
                )

                return priority_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_2_type_1 = (
                    PatchedWritableCircuitGroupAssignmentRequestPriorityType2Type1(data)
                )

                return priority_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_3_type_1 = (
                    PatchedWritableCircuitGroupAssignmentRequestPriorityType3Type1(data)
                )

                return priority_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PatchedWritableCircuitGroupAssignmentRequestPriorityType1,
                    PatchedWritableCircuitGroupAssignmentRequestPriorityType2Type1,
                    PatchedWritableCircuitGroupAssignmentRequestPriorityType3Type1,
                    Unset,
                ],
                data,
            )

        priority = _parse_priority(d.pop("priority", UNSET))

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        patched_writable_circuit_group_assignment_request = cls(
            group=group,
            member_type=member_type,
            member_id=member_id,
            priority=priority,
            tags=tags,
        )

        patched_writable_circuit_group_assignment_request.additional_properties = d
        return patched_writable_circuit_group_assignment_request

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
