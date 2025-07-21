import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_request_custom_fields import ContactRequestCustomFields
    from ..models.nested_tag_request import NestedTagRequest


T = TypeVar("T", bound="ContactRequest")


@_attrs_define
class ContactRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str):
        groups (Union[Unset, list[int]]):
        title (Union[Unset, str]):
        phone (Union[Unset, str]):
        email (Union[Unset, str]):
        address (Union[Unset, str]):
        link (Union[Unset, str]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, ContactRequestCustomFields]):
    """

    name: str
    groups: Union[Unset, list[int]] = UNSET
    title: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    address: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "ContactRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        groups: Union[Unset, list[int]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        title = self.title

        phone = self.phone

        email = self.email

        address = self.address

        link = self.link

        description = self.description

        comments = self.comments

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
                "name": name,
            }
        )
        if groups is not UNSET:
            field_dict["groups"] = groups
        if title is not UNSET:
            field_dict["title"] = title
        if phone is not UNSET:
            field_dict["phone"] = phone
        if email is not UNSET:
            field_dict["email"] = email
        if address is not UNSET:
            field_dict["address"] = address
        if link is not UNSET:
            field_dict["link"] = link
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        groups: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.groups, Unset):
            _temp_groups = self.groups
            groups = (None, json.dumps(_temp_groups).encode(), "application/json")

        title = (
            self.title
            if isinstance(self.title, Unset)
            else (None, str(self.title).encode(), "text/plain")
        )

        phone = (
            self.phone
            if isinstance(self.phone, Unset)
            else (None, str(self.phone).encode(), "text/plain")
        )

        email = (
            self.email
            if isinstance(self.email, Unset)
            else (None, str(self.email).encode(), "text/plain")
        )

        address = (
            self.address
            if isinstance(self.address, Unset)
            else (None, str(self.address).encode(), "text/plain")
        )

        link = (
            self.link
            if isinstance(self.link, Unset)
            else (None, str(self.link).encode(), "text/plain")
        )

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        comments = (
            self.comments
            if isinstance(self.comments, Unset)
            else (None, str(self.comments).encode(), "text/plain")
        )

        tags: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tags, Unset):
            _temp_tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                _temp_tags.append(tags_item)
            tags = (None, json.dumps(_temp_tags).encode(), "application/json")

        custom_fields: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = (
                None,
                json.dumps(self.custom_fields.to_dict()).encode(),
                "application/json",
            )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "name": name,
            }
        )
        if groups is not UNSET:
            field_dict["groups"] = groups
        if title is not UNSET:
            field_dict["title"] = title
        if phone is not UNSET:
            field_dict["phone"] = phone
        if email is not UNSET:
            field_dict["email"] = email
        if address is not UNSET:
            field_dict["address"] = address
        if link is not UNSET:
            field_dict["link"] = link
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_request_custom_fields import ContactRequestCustomFields
        from ..models.nested_tag_request import NestedTagRequest

        d = dict(src_dict)
        name = d.pop("name")

        groups = cast(list[int], d.pop("groups", UNSET))

        title = d.pop("title", UNSET)

        phone = d.pop("phone", UNSET)

        email = d.pop("email", UNSET)

        address = d.pop("address", UNSET)

        link = d.pop("link", UNSET)

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, ContactRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ContactRequestCustomFields.from_dict(_custom_fields)

        contact_request = cls(
            name=name,
            groups=groups,
            title=title,
            phone=phone,
            email=email,
            address=address,
            link=link,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        contact_request.additional_properties = d
        return contact_request

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
