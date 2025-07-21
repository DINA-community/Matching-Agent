from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_permission import ObjectPermission


T = TypeVar("T", bound="Group")


@_attrs_define
class Group:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            id (int):
            url (str):
            display_url (str):
            display (str):
            name (str):
            user_count (int):
            description (Union[Unset, str]):
            permissions (Union[Unset, list['ObjectPermission']]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    user_count: int
    description: Union[Unset, str] = UNSET
    permissions: Union[Unset, list["ObjectPermission"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

        user_count = self.user_count

        description = self.description

        permissions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.to_dict()
                permissions.append(permissions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "name": name,
                "user_count": user_count,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_permission import ObjectPermission

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

        user_count = d.pop("user_count")

        description = d.pop("description", UNSET)

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = ObjectPermission.from_dict(permissions_item_data)

            permissions.append(permissions_item)

        group = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            user_count=user_count,
            description=description,
            permissions=permissions,
        )

        group.additional_properties = d
        return group

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
