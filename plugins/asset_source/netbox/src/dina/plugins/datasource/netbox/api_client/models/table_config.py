import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TableConfig")


@_attrs_define
class TableConfig:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            id (int):
            url (str):
            display_url (str):
            display (str):
            object_type (str):
            table (str):
            name (str):
            columns (list[str]):
            created (Union[None, datetime.datetime]):
            last_updated (Union[None, datetime.datetime]):
            description (Union[Unset, str]):
            user (Union[None, Unset, int]):
            weight (Union[Unset, int]):
            enabled (Union[Unset, bool]):
            shared (Union[Unset, bool]):
            ordering (Union[None, Unset, list[str]]):
    """

    id: int
    url: str
    display_url: str
    display: str
    object_type: str
    table: str
    name: str
    columns: list[str]
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    description: Union[Unset, str] = UNSET
    user: Union[None, Unset, int] = UNSET
    weight: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    shared: Union[Unset, bool] = UNSET
    ordering: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        object_type = self.object_type

        table = self.table

        name = self.name

        columns = self.columns

        created: Union[None, str]
        if isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        last_updated: Union[None, str]
        if isinstance(self.last_updated, datetime.datetime):
            last_updated = self.last_updated.isoformat()
        else:
            last_updated = self.last_updated

        description = self.description

        user: Union[None, Unset, int]
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        weight = self.weight

        enabled = self.enabled

        shared = self.shared

        ordering: Union[None, Unset, list[str]]
        if isinstance(self.ordering, Unset):
            ordering = UNSET
        elif isinstance(self.ordering, list):
            ordering = self.ordering

        else:
            ordering = self.ordering

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "object_type": object_type,
                "table": table,
                "name": name,
                "columns": columns,
                "created": created,
                "last_updated": last_updated,
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
        if ordering is not UNSET:
            field_dict["ordering"] = ordering

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        object_type = d.pop("object_type")

        table = d.pop("table")

        name = d.pop("name")

        columns = cast(list[str], d.pop("columns"))

        def _parse_created(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = isoparse(data)

                return created_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        created = _parse_created(d.pop("created"))

        def _parse_last_updated(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_type_0 = isoparse(data)

                return last_updated_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_updated = _parse_last_updated(d.pop("last_updated"))

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

        table_config = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            object_type=object_type,
            table=table,
            name=name,
            columns=columns,
            created=created,
            last_updated=last_updated,
            description=description,
            user=user,
            weight=weight,
            enabled=enabled,
            shared=shared,
            ordering=ordering,
        )

        table_config.additional_properties = d
        return table_config

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
