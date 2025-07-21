import json
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedNotificationGroupRequest")


@_attrs_define
class PatchedNotificationGroupRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            name (Union[Unset, str]):
            description (Union[Unset, str]):
            groups (Union[Unset, list[int]]):
            users (Union[Unset, list[int]]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    groups: Union[Unset, list[int]] = UNSET
    users: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        groups: Union[Unset, list[int]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        users: Union[Unset, list[int]] = UNSET
        if not isinstance(self.users, Unset):
            users = self.users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if groups is not UNSET:
            field_dict["groups"] = groups
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (
            self.name
            if isinstance(self.name, Unset)
            else (None, str(self.name).encode(), "text/plain")
        )

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        groups: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.groups, Unset):
            _temp_groups = self.groups
            groups = (None, json.dumps(_temp_groups).encode(), "application/json")

        users: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.users, Unset):
            _temp_users = self.users
            users = (None, json.dumps(_temp_users).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if groups is not UNSET:
            field_dict["groups"] = groups
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        groups = cast(list[int], d.pop("groups", UNSET))

        users = cast(list[int], d.pop("users", UNSET))

        patched_notification_group_request = cls(
            name=name,
            description=description,
            groups=groups,
            users=users,
        )

        patched_notification_group_request.additional_properties = d
        return patched_notification_group_request

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
