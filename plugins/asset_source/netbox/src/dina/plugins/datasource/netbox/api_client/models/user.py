import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group import Group
    from ..models.object_permission import ObjectPermission


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            id (int):
            url (str):
            display_url (str):
            display (str):
            username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
            first_name (Union[Unset, str]):
            last_name (Union[Unset, str]):
            email (Union[Unset, str]):
            is_staff (Union[Unset, bool]): Designates whether the user can log into this admin site.
            is_active (Union[Unset, bool]): Designates whether this user should be treated as active. Unselect this instead
                of deleting accounts.
            date_joined (Union[Unset, datetime.datetime]):
            last_login (Union[None, Unset, datetime.datetime]):
            groups (Union[Unset, list['Group']]):
            permissions (Union[Unset, list['ObjectPermission']]):
    """

    id: int
    url: str
    display_url: str
    display: str
    username: str
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    is_staff: Union[Unset, bool] = UNSET
    is_active: Union[Unset, bool] = UNSET
    date_joined: Union[Unset, datetime.datetime] = UNSET
    last_login: Union[None, Unset, datetime.datetime] = UNSET
    groups: Union[Unset, list["Group"]] = UNSET
    permissions: Union[Unset, list["ObjectPermission"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        username = self.username

        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        is_staff = self.is_staff

        is_active = self.is_active

        date_joined: Union[Unset, str] = UNSET
        if not isinstance(self.date_joined, Unset):
            date_joined = self.date_joined.isoformat()

        last_login: Union[None, Unset, str]
        if isinstance(self.last_login, Unset):
            last_login = UNSET
        elif isinstance(self.last_login, datetime.datetime):
            last_login = self.last_login.isoformat()
        else:
            last_login = self.last_login

        groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

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
                "username": username,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if is_staff is not UNSET:
            field_dict["is_staff"] = is_staff
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if date_joined is not UNSET:
            field_dict["date_joined"] = date_joined
        if last_login is not UNSET:
            field_dict["last_login"] = last_login
        if groups is not UNSET:
            field_dict["groups"] = groups
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group import Group
        from ..models.object_permission import ObjectPermission

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        username = d.pop("username")

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        email = d.pop("email", UNSET)

        is_staff = d.pop("is_staff", UNSET)

        is_active = d.pop("is_active", UNSET)

        _date_joined = d.pop("date_joined", UNSET)
        date_joined: Union[Unset, datetime.datetime]
        if isinstance(_date_joined, Unset):
            date_joined = UNSET
        else:
            date_joined = isoparse(_date_joined)

        def _parse_last_login(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_login_type_0 = isoparse(data)

                return last_login_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_login = _parse_last_login(d.pop("last_login", UNSET))

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = Group.from_dict(groups_item_data)

            groups.append(groups_item)

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = ObjectPermission.from_dict(permissions_item_data)

            permissions.append(permissions_item)

        user = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            date_joined=date_joined,
            last_login=last_login,
            groups=groups,
            permissions=permissions,
        )

        user.additional_properties = d
        return user

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
