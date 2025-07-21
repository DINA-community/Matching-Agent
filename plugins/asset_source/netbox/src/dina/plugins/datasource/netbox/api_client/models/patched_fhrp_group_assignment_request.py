import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_fhrp_group_request import BriefFHRPGroupRequest


T = TypeVar("T", bound="PatchedFHRPGroupAssignmentRequest")


@_attrs_define
class PatchedFHRPGroupAssignmentRequest:
    """Adds support for custom fields and tags.

    Attributes:
        group (Union['BriefFHRPGroupRequest', Unset, int]):
        interface_type (Union[Unset, str]):
        interface_id (Union[Unset, int]):
        priority (Union[Unset, int]):
    """

    group: Union["BriefFHRPGroupRequest", Unset, int] = UNSET
    interface_type: Union[Unset, str] = UNSET
    interface_id: Union[Unset, int] = UNSET
    priority: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_fhrp_group_request import BriefFHRPGroupRequest

        group: Union[Unset, dict[str, Any], int]
        if isinstance(self.group, Unset):
            group = UNSET
        elif isinstance(self.group, BriefFHRPGroupRequest):
            group = self.group.to_dict()
        else:
            group = self.group

        interface_type = self.interface_type

        interface_id = self.interface_id

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group
        if interface_type is not UNSET:
            field_dict["interface_type"] = interface_type
        if interface_id is not UNSET:
            field_dict["interface_id"] = interface_id
        if priority is not UNSET:
            field_dict["priority"] = priority

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

        interface_type = (
            self.interface_type
            if isinstance(self.interface_type, Unset)
            else (None, str(self.interface_type).encode(), "text/plain")
        )

        interface_id = (
            self.interface_id
            if isinstance(self.interface_id, Unset)
            else (None, str(self.interface_id).encode(), "text/plain")
        )

        priority = (
            self.priority
            if isinstance(self.priority, Unset)
            else (None, str(self.priority).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group
        if interface_type is not UNSET:
            field_dict["interface_type"] = interface_type
        if interface_id is not UNSET:
            field_dict["interface_id"] = interface_id
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_fhrp_group_request import BriefFHRPGroupRequest

        d = dict(src_dict)

        def _parse_group(data: object) -> Union["BriefFHRPGroupRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_1 = BriefFHRPGroupRequest.from_dict(data)

                return group_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefFHRPGroupRequest", Unset, int], data)

        group = _parse_group(d.pop("group", UNSET))

        interface_type = d.pop("interface_type", UNSET)

        interface_id = d.pop("interface_id", UNSET)

        priority = d.pop("priority", UNSET)

        patched_fhrp_group_assignment_request = cls(
            group=group,
            interface_type=interface_type,
            interface_id=interface_id,
            priority=priority,
        )

        patched_fhrp_group_assignment_request.additional_properties = d
        return patched_fhrp_group_assignment_request

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
