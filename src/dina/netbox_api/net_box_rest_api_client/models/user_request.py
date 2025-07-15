import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserRequest")


@_attrs_define
class UserRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
            password (str):
            first_name (Union[Unset, str]):
            last_name (Union[Unset, str]):
            email (Union[Unset, str]):
            is_staff (Union[Unset, bool]): Designates whether the user can log into this admin site.
            is_active (Union[Unset, bool]): Designates whether this user should be treated as active. Unselect this instead
                of deleting accounts.
            date_joined (Union[Unset, datetime.datetime]):
            last_login (Union[None, Unset, datetime.datetime]):
            groups (Union[Unset, list[int]]):
            permissions (Union[Unset, list[int]]):
    """

    username: str
    password: str
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    is_staff: Union[Unset, bool] = UNSET
    is_active: Union[Unset, bool] = UNSET
    date_joined: Union[Unset, datetime.datetime] = UNSET
    last_login: Union[None, Unset, datetime.datetime] = UNSET
    groups: Union[Unset, list[int]] = UNSET
    permissions: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

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

        groups: Union[Unset, list[int]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        permissions: Union[Unset, list[int]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "password": password,
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

    def to_multipart(self) -> dict[str, Any]:
        username = (None, str(self.username).encode(), "text/plain")

        password = (None, str(self.password).encode(), "text/plain")

        first_name = (
            self.first_name
            if isinstance(self.first_name, Unset)
            else (None, str(self.first_name).encode(), "text/plain")
        )

        last_name = (
            self.last_name if isinstance(self.last_name, Unset) else (None, str(self.last_name).encode(), "text/plain")
        )

        email = self.email if isinstance(self.email, Unset) else (None, str(self.email).encode(), "text/plain")

        is_staff = (
            self.is_staff if isinstance(self.is_staff, Unset) else (None, str(self.is_staff).encode(), "text/plain")
        )

        is_active = (
            self.is_active if isinstance(self.is_active, Unset) else (None, str(self.is_active).encode(), "text/plain")
        )

        date_joined: Union[Unset, bytes] = UNSET
        if not isinstance(self.date_joined, Unset):
            date_joined = self.date_joined.isoformat().encode()

        last_login: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.last_login, Unset):
            last_login = UNSET
        elif isinstance(self.last_login, datetime.datetime):
            last_login = self.last_login.isoformat().encode()
        else:
            last_login = (None, str(self.last_login).encode(), "text/plain")

        groups: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.groups, Unset):
            _temp_groups = self.groups
            groups = (None, json.dumps(_temp_groups).encode(), "application/json")

        permissions: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.permissions, Unset):
            _temp_permissions = self.permissions
            permissions = (None, json.dumps(_temp_permissions).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "username": username,
                "password": password,
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
        d = dict(src_dict)
        username = d.pop("username")

        password = d.pop("password")

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

        groups = cast(list[int], d.pop("groups", UNSET))

        permissions = cast(list[int], d.pop("permissions", UNSET))

        user_request = cls(
            username=username,
            password=password,
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

        user_request.additional_properties = d
        return user_request

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
