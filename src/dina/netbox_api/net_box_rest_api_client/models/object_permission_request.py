import json
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectPermissionRequest")


@_attrs_define
class ObjectPermissionRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            name (str):
            object_types (list[str]):
            actions (list[str]): The list of actions granted by this permission
            description (Union[Unset, str]):
            enabled (Union[Unset, bool]):
            constraints (Union[Unset, Any]): Queryset filter matching the applicable objects of the selected type(s)
            groups (Union[Unset, list[int]]):
            users (Union[Unset, list[int]]):
    """

    name: str
    object_types: list[str]
    actions: list[str]
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    constraints: Union[Unset, Any] = UNSET
    groups: Union[Unset, list[int]] = UNSET
    users: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        object_types = self.object_types

        actions = self.actions

        description = self.description

        enabled = self.enabled

        constraints = self.constraints

        groups: Union[Unset, list[int]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        users: Union[Unset, list[int]] = UNSET
        if not isinstance(self.users, Unset):
            users = self.users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "object_types": object_types,
                "actions": actions,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if constraints is not UNSET:
            field_dict["constraints"] = constraints
        if groups is not UNSET:
            field_dict["groups"] = groups
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        _temp_object_types = self.object_types
        object_types = (None, json.dumps(_temp_object_types).encode(), "application/json")

        _temp_actions = self.actions
        actions = (None, json.dumps(_temp_actions).encode(), "application/json")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        enabled = self.enabled if isinstance(self.enabled, Unset) else (None, str(self.enabled).encode(), "text/plain")

        constraints = (
            self.constraints
            if isinstance(self.constraints, Unset)
            else (None, str(self.constraints).encode(), "text/plain")
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

        field_dict.update(
            {
                "name": name,
                "object_types": object_types,
                "actions": actions,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if constraints is not UNSET:
            field_dict["constraints"] = constraints
        if groups is not UNSET:
            field_dict["groups"] = groups
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        object_types = cast(list[str], d.pop("object_types"))

        actions = cast(list[str], d.pop("actions"))

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        constraints = d.pop("constraints", UNSET)

        groups = cast(list[int], d.pop("groups", UNSET))

        users = cast(list[int], d.pop("users", UNSET))

        object_permission_request = cls(
            name=name,
            object_types=object_types,
            actions=actions,
            description=description,
            enabled=enabled,
            constraints=constraints,
            groups=groups,
            users=users,
        )

        object_permission_request.additional_properties = d
        return object_permission_request

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
