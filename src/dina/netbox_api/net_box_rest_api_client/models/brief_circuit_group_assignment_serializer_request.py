from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.brief_circuit_group_assignment_serializer_request_priority import (
    BriefCircuitGroupAssignmentSerializerRequestPriority,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_circuit_group_request import BriefCircuitGroupRequest


T = TypeVar("T", bound="BriefCircuitGroupAssignmentSerializerRequest")


@_attrs_define
class BriefCircuitGroupAssignmentSerializerRequest:
    """Base serializer for group assignments under CircuitSerializer.

    Attributes:
        group (Union['BriefCircuitGroupRequest', int]):
        priority (Union[Unset, BriefCircuitGroupAssignmentSerializerRequestPriority]): * `primary` - Primary
            * `secondary` - Secondary
            * `tertiary` - Tertiary
            * `inactive` - Inactive
    """

    group: Union["BriefCircuitGroupRequest", int]
    priority: Union[Unset, BriefCircuitGroupAssignmentSerializerRequestPriority] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_circuit_group_request import BriefCircuitGroupRequest

        group: Union[dict[str, Any], int]
        if isinstance(self.group, BriefCircuitGroupRequest):
            group = self.group.to_dict()
        else:
            group = self.group

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group": group,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_circuit_group_request import BriefCircuitGroupRequest

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

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, BriefCircuitGroupAssignmentSerializerRequestPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = BriefCircuitGroupAssignmentSerializerRequestPriority(_priority)

        brief_circuit_group_assignment_serializer_request = cls(
            group=group,
            priority=priority,
        )

        brief_circuit_group_assignment_serializer_request.additional_properties = d
        return brief_circuit_group_assignment_serializer_request

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
