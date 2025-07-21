import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_contact import BriefContact
    from ..models.brief_contact_role import BriefContactRole
    from ..models.contact_assignment_custom_fields import ContactAssignmentCustomFields
    from ..models.contact_assignment_object import ContactAssignmentObject
    from ..models.contact_assignment_priority import ContactAssignmentPriority
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="ContactAssignment")


@_attrs_define
class ContactAssignment:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display (str):
        object_type (str):
        object_id (int):
        object_ (ContactAssignmentObject):
        contact (BriefContact): Adds support for custom fields and tags.
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        role (Union['BriefContactRole', None, Unset]):
        priority (Union[Unset, ContactAssignmentPriority]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, ContactAssignmentCustomFields]):
    """

    id: int
    url: str
    display: str
    object_type: str
    object_id: int
    object_: "ContactAssignmentObject"
    contact: "BriefContact"
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    role: Union["BriefContactRole", None, Unset] = UNSET
    priority: Union[Unset, "ContactAssignmentPriority"] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "ContactAssignmentCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_contact_role import BriefContactRole

        id = self.id

        url = self.url

        display = self.display

        object_type = self.object_type

        object_id = self.object_id

        object_ = self.object_.to_dict()

        contact = self.contact.to_dict()

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

        role: Union[None, Unset, dict[str, Any]]
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, BriefContactRole):
            role = self.role.to_dict()
        else:
            role = self.role

        priority: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

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
                "id": id,
                "url": url,
                "display": display,
                "object_type": object_type,
                "object_id": object_id,
                "object": object_,
                "contact": contact,
                "created": created,
                "last_updated": last_updated,
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
        from ..models.brief_contact import BriefContact
        from ..models.brief_contact_role import BriefContactRole
        from ..models.contact_assignment_custom_fields import (
            ContactAssignmentCustomFields,
        )
        from ..models.contact_assignment_object import ContactAssignmentObject
        from ..models.contact_assignment_priority import ContactAssignmentPriority
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        object_type = d.pop("object_type")

        object_id = d.pop("object_id")

        object_ = ContactAssignmentObject.from_dict(d.pop("object"))

        contact = BriefContact.from_dict(d.pop("contact"))

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

        def _parse_role(data: object) -> Union["BriefContactRole", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                role_type_1 = BriefContactRole.from_dict(data)

                return role_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefContactRole", None, Unset], data)

        role = _parse_role(d.pop("role", UNSET))

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, ContactAssignmentPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = ContactAssignmentPriority.from_dict(_priority)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, ContactAssignmentCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ContactAssignmentCustomFields.from_dict(_custom_fields)

        contact_assignment = cls(
            id=id,
            url=url,
            display=display,
            object_type=object_type,
            object_id=object_id,
            object_=object_,
            contact=contact,
            created=created,
            last_updated=last_updated,
            role=role,
            priority=priority,
            tags=tags,
            custom_fields=custom_fields,
        )

        contact_assignment.additional_properties = d
        return contact_assignment

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
