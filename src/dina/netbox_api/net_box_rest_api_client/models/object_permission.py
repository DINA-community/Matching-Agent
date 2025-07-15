from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_group import NestedGroup
    from ..models.nested_user import NestedUser


T = TypeVar("T", bound="ObjectPermission")


@_attrs_define
class ObjectPermission:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            id (int):
            url (str):
            display_url (str):
            display (str):
            name (str):
            object_types (list[str]):
            actions (list[str]): The list of actions granted by this permission
            description (Union[Unset, str]):
            enabled (Union[Unset, bool]):
            constraints (Union[Unset, Any]): Queryset filter matching the applicable objects of the selected type(s)
            groups (Union[Unset, list['NestedGroup']]):
            users (Union[Unset, list['NestedUser']]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    object_types: list[str]
    actions: list[str]
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    constraints: Union[Unset, Any] = UNSET
    groups: Union[Unset, list["NestedGroup"]] = UNSET
    users: Union[Unset, list["NestedUser"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

        object_types = self.object_types

        actions = self.actions

        description = self.description

        enabled = self.enabled

        constraints = self.constraints

        groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        users: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
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
        from ..models.nested_group import NestedGroup
        from ..models.nested_user import NestedUser

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

        object_types = cast(list[str], d.pop("object_types"))

        actions = cast(list[str], d.pop("actions"))

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        constraints = d.pop("constraints", UNSET)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = NestedGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = NestedUser.from_dict(users_item_data)

            users.append(users_item)

        object_permission = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            object_types=object_types,
            actions=actions,
            description=description,
            enabled=enabled,
            constraints=constraints,
            groups=groups,
            users=users,
        )

        object_permission.additional_properties = d
        return object_permission

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
