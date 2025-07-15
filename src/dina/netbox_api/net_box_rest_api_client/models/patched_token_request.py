import datetime
import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_user_request import BriefUserRequest


T = TypeVar("T", bound="PatchedTokenRequest")


@_attrs_define
class PatchedTokenRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            user (Union['BriefUserRequest', Unset, int]):
            expires (Union[None, Unset, datetime.datetime]):
            last_used (Union[None, Unset, datetime.datetime]):
            key (Union[Unset, str]):
            write_enabled (Union[Unset, bool]): Permit create/update/delete operations using this key
            description (Union[Unset, str]):
    """

    user: Union["BriefUserRequest", Unset, int] = UNSET
    expires: Union[None, Unset, datetime.datetime] = UNSET
    last_used: Union[None, Unset, datetime.datetime] = UNSET
    key: Union[Unset, str] = UNSET
    write_enabled: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_user_request import BriefUserRequest

        user: Union[Unset, dict[str, Any], int]
        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, BriefUserRequest):
            user = self.user.to_dict()
        else:
            user = self.user

        expires: Union[None, Unset, str]
        if isinstance(self.expires, Unset):
            expires = UNSET
        elif isinstance(self.expires, datetime.datetime):
            expires = self.expires.isoformat()
        else:
            expires = self.expires

        last_used: Union[None, Unset, str]
        if isinstance(self.last_used, Unset):
            last_used = UNSET
        elif isinstance(self.last_used, datetime.datetime):
            last_used = self.last_used.isoformat()
        else:
            last_used = self.last_used

        key = self.key

        write_enabled = self.write_enabled

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if expires is not UNSET:
            field_dict["expires"] = expires
        if last_used is not UNSET:
            field_dict["last_used"] = last_used
        if key is not UNSET:
            field_dict["key"] = key
        if write_enabled is not UNSET:
            field_dict["write_enabled"] = write_enabled
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        user: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, int):
            user = (None, str(self.user).encode(), "text/plain")
        else:
            user = (None, json.dumps(self.user.to_dict()).encode(), "application/json")

        expires: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.expires, Unset):
            expires = UNSET
        elif isinstance(self.expires, datetime.datetime):
            expires = self.expires.isoformat().encode()
        else:
            expires = (None, str(self.expires).encode(), "text/plain")

        last_used: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.last_used, Unset):
            last_used = UNSET
        elif isinstance(self.last_used, datetime.datetime):
            last_used = self.last_used.isoformat().encode()
        else:
            last_used = (None, str(self.last_used).encode(), "text/plain")

        key = self.key if isinstance(self.key, Unset) else (None, str(self.key).encode(), "text/plain")

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

        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if expires is not UNSET:
            field_dict["expires"] = expires
        if last_used is not UNSET:
            field_dict["last_used"] = last_used
        if key is not UNSET:
            field_dict["key"] = key
        if write_enabled is not UNSET:
            field_dict["write_enabled"] = write_enabled
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_user_request import BriefUserRequest

        d = dict(src_dict)

        def _parse_user(data: object) -> Union["BriefUserRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_1 = BriefUserRequest.from_dict(data)

                return user_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefUserRequest", Unset, int], data)

        user = _parse_user(d.pop("user", UNSET))

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

        def _parse_last_used(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_type_0 = isoparse(data)

                return last_used_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_used = _parse_last_used(d.pop("last_used", UNSET))

        key = d.pop("key", UNSET)

        write_enabled = d.pop("write_enabled", UNSET)

        description = d.pop("description", UNSET)

        patched_token_request = cls(
            user=user,
            expires=expires,
            last_used=last_used,
            key=key,
            write_enabled=write_enabled,
            description=description,
        )

        patched_token_request.additional_properties = d
        return patched_token_request

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
