import json
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedTableConfigRequest")


@_attrs_define
class PatchedTableConfigRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            object_type (Union[Unset, str]):
            table (Union[Unset, str]):
            name (Union[Unset, str]):
            description (Union[Unset, str]):
            user (Union[None, Unset, int]):
            weight (Union[Unset, int]):
            enabled (Union[Unset, bool]):
            shared (Union[Unset, bool]):
            columns (Union[Unset, list[str]]):
            ordering (Union[None, Unset, list[str]]):
    """

    object_type: Union[Unset, str] = UNSET
    table: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    user: Union[None, Unset, int] = UNSET
    weight: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    shared: Union[Unset, bool] = UNSET
    columns: Union[Unset, list[str]] = UNSET
    ordering: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_type = self.object_type

        table = self.table

        name = self.name

        description = self.description

        user: Union[None, Unset, int]
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        weight = self.weight

        enabled = self.enabled

        shared = self.shared

        columns: Union[Unset, list[str]] = UNSET
        if not isinstance(self.columns, Unset):
            columns = self.columns

        ordering: Union[None, Unset, list[str]]
        if isinstance(self.ordering, Unset):
            ordering = UNSET
        elif isinstance(self.ordering, list):
            ordering = self.ordering

        else:
            ordering = self.ordering

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if table is not UNSET:
            field_dict["table"] = table
        if name is not UNSET:
            field_dict["name"] = name
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
        if columns is not UNSET:
            field_dict["columns"] = columns
        if ordering is not UNSET:
            field_dict["ordering"] = ordering

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        object_type = (
            self.object_type
            if isinstance(self.object_type, Unset)
            else (None, str(self.object_type).encode(), "text/plain")
        )

        table = (
            self.table
            if isinstance(self.table, Unset)
            else (None, str(self.table).encode(), "text/plain")
        )

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

        columns: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.columns, Unset):
            _temp_columns = self.columns
            columns = (None, json.dumps(_temp_columns).encode(), "application/json")

        ordering: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.ordering, Unset):
            ordering = UNSET
        elif isinstance(self.ordering, list):
            _temp_ordering = self.ordering
            ordering = (None, json.dumps(_temp_ordering).encode(), "application/json")
        else:
            ordering = (None, str(self.ordering).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if table is not UNSET:
            field_dict["table"] = table
        if name is not UNSET:
            field_dict["name"] = name
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
        if columns is not UNSET:
            field_dict["columns"] = columns
        if ordering is not UNSET:
            field_dict["ordering"] = ordering

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_type = d.pop("object_type", UNSET)

        table = d.pop("table", UNSET)

        name = d.pop("name", UNSET)

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

        columns = cast(list[str], d.pop("columns", UNSET))

        def _parse_ordering(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ordering_type_0 = cast(list[str], data)

                return ordering_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        ordering = _parse_ordering(d.pop("ordering", UNSET))

        patched_table_config_request = cls(
            object_type=object_type,
            table=table,
            name=name,
            description=description,
            user=user,
            weight=weight,
            enabled=enabled,
            shared=shared,
            columns=columns,
            ordering=ordering,
        )

        patched_table_config_request.additional_properties = d
        return patched_table_config_request

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
