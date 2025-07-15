import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.journal_entry_custom_fields import JournalEntryCustomFields
    from ..models.journal_entry_kind import JournalEntryKind
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="JournalEntry")


@_attrs_define
class JournalEntry:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        assigned_object_type (str):
        assigned_object_id (int):
        assigned_object (Any):
        created (Union[None, datetime.datetime]):
        comments (str):
        last_updated (Union[None, datetime.datetime]):
        created_by (Union[None, Unset, int]):
        kind (Union[Unset, JournalEntryKind]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, JournalEntryCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    assigned_object_type: str
    assigned_object_id: int
    assigned_object: Any
    created: Union[None, datetime.datetime]
    comments: str
    last_updated: Union[None, datetime.datetime]
    created_by: Union[None, Unset, int] = UNSET
    kind: Union[Unset, "JournalEntryKind"] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "JournalEntryCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        assigned_object_type = self.assigned_object_type

        assigned_object_id = self.assigned_object_id

        assigned_object = self.assigned_object

        created: Union[None, str]
        if isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        comments = self.comments

        last_updated: Union[None, str]
        if isinstance(self.last_updated, datetime.datetime):
            last_updated = self.last_updated.isoformat()
        else:
            last_updated = self.last_updated

        created_by: Union[None, Unset, int]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        kind: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.to_dict()

        tags: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "assigned_object_type": assigned_object_type,
                "assigned_object_id": assigned_object_id,
                "assigned_object": assigned_object,
                "created": created,
                "comments": comments,
                "last_updated": last_updated,
            }
        )
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if kind is not UNSET:
            field_dict["kind"] = kind
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.journal_entry_custom_fields import JournalEntryCustomFields
        from ..models.journal_entry_kind import JournalEntryKind
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        assigned_object_type = d.pop("assigned_object_type")

        assigned_object_id = d.pop("assigned_object_id")

        assigned_object = d.pop("assigned_object")

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

        comments = d.pop("comments")

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

        def _parse_created_by(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, JournalEntryKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = JournalEntryKind.from_dict(_kind)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, JournalEntryCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = JournalEntryCustomFields.from_dict(_custom_fields)

        journal_entry = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            assigned_object_type=assigned_object_type,
            assigned_object_id=assigned_object_id,
            assigned_object=assigned_object,
            created=created,
            comments=comments,
            last_updated=last_updated,
            created_by=created_by,
            kind=kind,
            tags=tags,
            custom_fields=custom_fields,
        )

        journal_entry.additional_properties = d
        return journal_entry

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
