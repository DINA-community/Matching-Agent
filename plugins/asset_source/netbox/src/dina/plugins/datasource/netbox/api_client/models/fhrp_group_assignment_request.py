import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.brief_fhrp_group_request import BriefFHRPGroupRequest


T = TypeVar("T", bound="FHRPGroupAssignmentRequest")


@_attrs_define
class FHRPGroupAssignmentRequest:
    """Adds support for custom fields and tags.

    Attributes:
        group (Union['BriefFHRPGroupRequest', int]):
        interface_type (str):
        interface_id (int):
        priority (int):
    """

    group: Union["BriefFHRPGroupRequest", int]
    interface_type: str
    interface_id: int
    priority: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_fhrp_group_request import BriefFHRPGroupRequest

        group: Union[dict[str, Any], int]
        if isinstance(self.group, BriefFHRPGroupRequest):
            group = self.group.to_dict()
        else:
            group = self.group

        interface_type = self.interface_type

        interface_id = self.interface_id

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group": group,
                "interface_type": interface_type,
                "interface_id": interface_id,
                "priority": priority,
            }
        )

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        group: tuple[None, bytes, str]

        if isinstance(self.group, int):
            group = (None, str(self.group).encode(), "text/plain")
        else:
            group = (
                None,
                json.dumps(self.group.to_dict()).encode(),
                "application/json",
            )

        interface_type = (None, str(self.interface_type).encode(), "text/plain")

        interface_id = (None, str(self.interface_id).encode(), "text/plain")

        priority = (None, str(self.priority).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "group": group,
                "interface_type": interface_type,
                "interface_id": interface_id,
                "priority": priority,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_fhrp_group_request import BriefFHRPGroupRequest

        d = dict(src_dict)

        def _parse_group(data: object) -> Union["BriefFHRPGroupRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_1 = BriefFHRPGroupRequest.from_dict(data)

                return group_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefFHRPGroupRequest", int], data)

        group = _parse_group(d.pop("group"))

        interface_type = d.pop("interface_type")

        interface_id = d.pop("interface_id")

        priority = d.pop("priority")

        fhrp_group_assignment_request = cls(
            group=group,
            interface_type=interface_type,
            interface_id=interface_id,
            priority=priority,
        )

        fhrp_group_assignment_request.additional_properties = d
        return fhrp_group_assignment_request

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
