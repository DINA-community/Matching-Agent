import json
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SavedFilterRequest")


@_attrs_define
class SavedFilterRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            object_types (list[str]):
            name (str):
            slug (str):
            parameters (Any):
            description (Union[Unset, str]):
            user (Union[None, Unset, int]):
            weight (Union[Unset, int]):
            enabled (Union[Unset, bool]):
            shared (Union[Unset, bool]):
    """

    object_types: list[str]
    name: str
    slug: str
    parameters: Any
    description: Union[Unset, str] = UNSET
    user: Union[None, Unset, int] = UNSET
    weight: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    shared: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_types = self.object_types

        name = self.name

        slug = self.slug

        parameters = self.parameters

        description = self.description

        user: Union[None, Unset, int]
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        weight = self.weight

        enabled = self.enabled

        shared = self.shared

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_types": object_types,
                "name": name,
                "slug": slug,
                "parameters": parameters,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if user is not UNSET:
            field_dict["user"] = user
        if weight is not UNSET:
            field_dict["weight"] = weight
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if shared is not UNSET:
            field_dict["shared"] = shared

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        _temp_object_types = self.object_types
        object_types = (
            None,
            json.dumps(_temp_object_types).encode(),
            "application/json",
        )

        name = (None, str(self.name).encode(), "text/plain")

        slug = (None, str(self.slug).encode(), "text/plain")

        parameters = (None, str(self.parameters).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        user: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.user, Unset):
            user = UNSET
        elif isinstance(self.user, int):
            user = (None, str(self.user).encode(), "text/plain")
        else:
            user = (None, str(self.user).encode(), "text/plain")

        weight = (
            self.weight
            if isinstance(self.weight, Unset)
            else (None, str(self.weight).encode(), "text/plain")
        )

        enabled = (
            self.enabled
            if isinstance(self.enabled, Unset)
            else (None, str(self.enabled).encode(), "text/plain")
        )

        shared = (
            self.shared
            if isinstance(self.shared, Unset)
            else (None, str(self.shared).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "object_types": object_types,
                "name": name,
                "slug": slug,
                "parameters": parameters,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if user is not UNSET:
            field_dict["user"] = user
        if weight is not UNSET:
            field_dict["weight"] = weight
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if shared is not UNSET:
            field_dict["shared"] = shared

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_types = cast(list[str], d.pop("object_types"))

        name = d.pop("name")

        slug = d.pop("slug")

        parameters = d.pop("parameters")

        description = d.pop("description", UNSET)

        def _parse_user(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        user = _parse_user(d.pop("user", UNSET))

        weight = d.pop("weight", UNSET)

        enabled = d.pop("enabled", UNSET)

        shared = d.pop("shared", UNSET)

        saved_filter_request = cls(
            object_types=object_types,
            name=name,
            slug=slug,
            parameters=parameters,
            description=description,
            user=user,
            weight=weight,
            enabled=enabled,
            shared=shared,
        )

        saved_filter_request.additional_properties = d
        return saved_filter_request

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
