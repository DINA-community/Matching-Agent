import json
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TagRequest")


@_attrs_define
class TagRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            name (str):
            slug (str):
            color (Union[Unset, str]):
            description (Union[Unset, str]):
            weight (Union[Unset, int]):
            object_types (Union[Unset, list[str]]):
    """

    name: str
    slug: str
    color: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    weight: Union[Unset, int] = UNSET
    object_types: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        color = self.color

        description = self.description

        weight = self.weight

        object_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.object_types, Unset):
            object_types = self.object_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description
        if weight is not UNSET:
            field_dict["weight"] = weight
        if object_types is not UNSET:
            field_dict["object_types"] = object_types

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        slug = (None, str(self.slug).encode(), "text/plain")

        color = self.color if isinstance(self.color, Unset) else (None, str(self.color).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        weight = self.weight if isinstance(self.weight, Unset) else (None, str(self.weight).encode(), "text/plain")

        object_types: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.object_types, Unset):
            _temp_object_types = self.object_types
            object_types = (None, json.dumps(_temp_object_types).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "name": name,
                "slug": slug,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description
        if weight is not UNSET:
            field_dict["weight"] = weight
        if object_types is not UNSET:
            field_dict["object_types"] = object_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        color = d.pop("color", UNSET)

        description = d.pop("description", UNSET)

        weight = d.pop("weight", UNSET)

        object_types = cast(list[str], d.pop("object_types", UNSET))

        tag_request = cls(
            name=name,
            slug=slug,
            color=color,
            description=description,
            weight=weight,
            object_types=object_types,
        )

        tag_request.additional_properties = d
        return tag_request

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
