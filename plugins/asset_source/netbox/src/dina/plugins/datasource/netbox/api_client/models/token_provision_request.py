import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenProvisionRequest")


@_attrs_define
class TokenProvisionRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            username (str):
            password (str):
            expires (Union[None, Unset, datetime.datetime]):
            write_enabled (Union[Unset, bool]): Permit create/update/delete operations using this key
            description (Union[Unset, str]):
    """

    username: str
    password: str
    expires: Union[None, Unset, datetime.datetime] = UNSET
    write_enabled: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        expires: Union[None, Unset, str]
        if isinstance(self.expires, Unset):
            expires = UNSET
        elif isinstance(self.expires, datetime.datetime):
            expires = self.expires.isoformat()
        else:
            expires = self.expires

        write_enabled = self.write_enabled

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "password": password,
            }
        )
        if expires is not UNSET:
            field_dict["expires"] = expires
        if write_enabled is not UNSET:
            field_dict["write_enabled"] = write_enabled
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        username = (None, str(self.username).encode(), "text/plain")

        password = (None, str(self.password).encode(), "text/plain")

        expires: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.expires, Unset):
            expires = UNSET
        elif isinstance(self.expires, datetime.datetime):
            expires = self.expires.isoformat().encode()
        else:
            expires = (None, str(self.expires).encode(), "text/plain")

        write_enabled = (
            self.write_enabled
            if isinstance(self.write_enabled, Unset)
            else (None, str(self.write_enabled).encode(), "text/plain")
        )

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "username": username,
                "password": password,
            }
        )
        if expires is not UNSET:
            field_dict["expires"] = expires
        if write_enabled is not UNSET:
            field_dict["write_enabled"] = write_enabled
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        password = d.pop("password")

        def _parse_expires(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_type_0 = isoparse(data)

                return expires_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        expires = _parse_expires(d.pop("expires", UNSET))

        write_enabled = d.pop("write_enabled", UNSET)

        description = d.pop("description", UNSET)

        token_provision_request = cls(
            username=username,
            password=password,
            expires=expires,
            write_enabled=write_enabled,
            description=description,
        )

        token_provision_request.additional_properties = d
        return token_provision_request

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
