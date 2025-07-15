import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_contact_assignment_request_priority_type_1 import WritableContactAssignmentRequestPriorityType1
from ..models.writable_contact_assignment_request_priority_type_2_type_1 import (
    WritableContactAssignmentRequestPriorityType2Type1,
)
from ..models.writable_contact_assignment_request_priority_type_3_type_1 import (
    WritableContactAssignmentRequestPriorityType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_contact_request import BriefContactRequest
    from ..models.brief_contact_role_request import BriefContactRoleRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.writable_contact_assignment_request_custom_fields import WritableContactAssignmentRequestCustomFields


T = TypeVar("T", bound="WritableContactAssignmentRequest")


@_attrs_define
class WritableContactAssignmentRequest:
    """Adds support for custom fields and tags.

    Attributes:
        object_type (str):
        object_id (int):
        contact (Union['BriefContactRequest', int]):
        role (Union['BriefContactRoleRequest', None, Unset, int]):
        priority (Union[None, Unset, WritableContactAssignmentRequestPriorityType1,
            WritableContactAssignmentRequestPriorityType2Type1, WritableContactAssignmentRequestPriorityType3Type1]): *
            `primary` - Primary
            * `secondary` - Secondary
            * `tertiary` - Tertiary
            * `inactive` - Inactive
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WritableContactAssignmentRequestCustomFields]):
    """

    object_type: str
    object_id: int
    contact: Union["BriefContactRequest", int]
    role: Union["BriefContactRoleRequest", None, Unset, int] = UNSET
    priority: Union[
        None,
        Unset,
        WritableContactAssignmentRequestPriorityType1,
        WritableContactAssignmentRequestPriorityType2Type1,
        WritableContactAssignmentRequestPriorityType3Type1,
    ] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WritableContactAssignmentRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_contact_request import BriefContactRequest
        from ..models.brief_contact_role_request import BriefContactRoleRequest

        object_type = self.object_type

        object_id = self.object_id

        contact: Union[dict[str, Any], int]
        if isinstance(self.contact, BriefContactRequest):
            contact = self.contact.to_dict()
        else:
            contact = self.contact

        role: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, BriefContactRoleRequest):
            role = self.role.to_dict()
        else:
            role = self.role

        priority: Union[None, Unset, str]
        if isinstance(self.priority, Unset):
            priority = UNSET
        elif isinstance(self.priority, WritableContactAssignmentRequestPriorityType1):
            priority = self.priority.value
        elif isinstance(self.priority, WritableContactAssignmentRequestPriorityType2Type1):
            priority = self.priority.value
        elif isinstance(self.priority, WritableContactAssignmentRequestPriorityType3Type1):
            priority = self.priority.value
        else:
            priority = self.priority

        tags: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_type": object_type,
                "object_id": object_id,
                "contact": contact,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role
        if priority is not UNSET:
            field_dict["priority"] = priority
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        object_type = (None, str(self.object_type).encode(), "text/plain")

        object_id = (None, str(self.object_id).encode(), "text/plain")

        contact: tuple[None, bytes, str]

        if isinstance(self.contact, int):
            contact = (None, str(self.contact).encode(), "text/plain")
        else:
            contact = (None, json.dumps(self.contact.to_dict()).encode(), "application/json")

        role: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, int):
            role = (None, str(self.role).encode(), "text/plain")
        elif isinstance(self.role, None):
            role = (None, str(self.role).encode(), "text/plain")
        elif isinstance(self.role, BriefContactRoleRequest):
            role = (None, json.dumps(self.role.to_dict()).encode(), "application/json")
        else:
            role = (None, str(self.role).encode(), "text/plain")

        priority: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.priority, Unset):
            priority = UNSET
        elif isinstance(self.priority, None):
            priority = (None, str(self.priority).encode(), "text/plain")
        elif isinstance(self.priority, WritableContactAssignmentRequestPriorityType1):
            priority = (None, str(self.priority.value).encode(), "text/plain")
        elif isinstance(self.priority, None):
            priority = (None, str(self.priority).encode(), "text/plain")
        elif isinstance(self.priority, WritableContactAssignmentRequestPriorityType2Type1):
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

        custom_fields: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = (None, json.dumps(self.custom_fields.to_dict()).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "object_type": object_type,
                "object_id": object_id,
                "contact": contact,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role
        if priority is not UNSET:
            field_dict["priority"] = priority
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_contact_request import BriefContactRequest
        from ..models.brief_contact_role_request import BriefContactRoleRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.writable_contact_assignment_request_custom_fields import (
            WritableContactAssignmentRequestCustomFields,
        )

        d = dict(src_dict)
        object_type = d.pop("object_type")

        object_id = d.pop("object_id")

        def _parse_contact(data: object) -> Union["BriefContactRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                contact_type_1 = BriefContactRequest.from_dict(data)

                return contact_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefContactRequest", int], data)

        contact = _parse_contact(d.pop("contact"))

        def _parse_role(data: object) -> Union["BriefContactRoleRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                role_type_1_type_1 = BriefContactRoleRequest.from_dict(data)

                return role_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefContactRoleRequest", None, Unset, int], data)

        role = _parse_role(d.pop("role", UNSET))

        def _parse_priority(
            data: object,
        ) -> Union[
            None,
            Unset,
            WritableContactAssignmentRequestPriorityType1,
            WritableContactAssignmentRequestPriorityType2Type1,
            WritableContactAssignmentRequestPriorityType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_1 = WritableContactAssignmentRequestPriorityType1(data)

                return priority_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_2_type_1 = WritableContactAssignmentRequestPriorityType2Type1(data)

                return priority_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                priority_type_3_type_1 = WritableContactAssignmentRequestPriorityType3Type1(data)

                return priority_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    WritableContactAssignmentRequestPriorityType1,
                    WritableContactAssignmentRequestPriorityType2Type1,
                    WritableContactAssignmentRequestPriorityType3Type1,
                ],
                data,
            )

        priority = _parse_priority(d.pop("priority", UNSET))

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WritableContactAssignmentRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WritableContactAssignmentRequestCustomFields.from_dict(_custom_fields)

        writable_contact_assignment_request = cls(
            object_type=object_type,
            object_id=object_id,
            contact=contact,
            role=role,
            priority=priority,
            tags=tags,
            custom_fields=custom_fields,
        )

        writable_contact_assignment_request.additional_properties = d
        return writable_contact_assignment_request

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
