from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_assignment_request_priority import (
    ContactAssignmentRequestPriority,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_contact_request import BriefContactRequest
    from ..models.brief_contact_role_request import BriefContactRoleRequest
    from ..models.contact_assignment_request_custom_fields import (
        ContactAssignmentRequestCustomFields,
    )
    from ..models.nested_tag_request import NestedTagRequest


T = TypeVar("T", bound="ContactAssignmentRequest")


@_attrs_define
class ContactAssignmentRequest:
    """Adds support for custom fields and tags.

    Attributes:
        object_type (str):
        object_id (int):
        contact (Union['BriefContactRequest', int]):
        role (Union['BriefContactRoleRequest', None, Unset, int]):
        priority (Union[Unset, ContactAssignmentRequestPriority]): * `primary` - Primary
            * `secondary` - Secondary
            * `tertiary` - Tertiary
            * `inactive` - Inactive
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, ContactAssignmentRequestCustomFields]):
    """

    object_type: str
    object_id: int
    contact: Union["BriefContactRequest", int]
    role: Union["BriefContactRoleRequest", None, Unset, int] = UNSET
    priority: Union[Unset, ContactAssignmentRequestPriority] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "ContactAssignmentRequestCustomFields"] = UNSET
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

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

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

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_contact_request import BriefContactRequest
        from ..models.brief_contact_role_request import BriefContactRoleRequest
        from ..models.contact_assignment_request_custom_fields import (
            ContactAssignmentRequestCustomFields,
        )
        from ..models.nested_tag_request import NestedTagRequest

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

        def _parse_role(
            data: object,
        ) -> Union["BriefContactRoleRequest", None, Unset, int]:
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

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, ContactAssignmentRequestPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = ContactAssignmentRequestPriority(_priority)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, ContactAssignmentRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ContactAssignmentRequestCustomFields.from_dict(
                _custom_fields
            )

        contact_assignment_request = cls(
            object_type=object_type,
            object_id=object_id,
            contact=contact,
            role=role,
            priority=priority,
            tags=tags,
            custom_fields=custom_fields,
        )

        contact_assignment_request.additional_properties = d
        return contact_assignment_request

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
