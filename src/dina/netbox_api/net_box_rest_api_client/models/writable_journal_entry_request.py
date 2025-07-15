import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_journal_entry_request_kind import WritableJournalEntryRequestKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.writable_journal_entry_request_custom_fields import WritableJournalEntryRequestCustomFields


T = TypeVar("T", bound="WritableJournalEntryRequest")


@_attrs_define
class WritableJournalEntryRequest:
    """Adds support for custom fields and tags.

    Attributes:
        assigned_object_type (str):
        assigned_object_id (int):
        comments (str):
        created_by (Union[None, Unset, int]):
        kind (Union[Unset, WritableJournalEntryRequestKind]): * `info` - Info
            * `success` - Success
            * `warning` - Warning
            * `danger` - Danger
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WritableJournalEntryRequestCustomFields]):
    """

    assigned_object_type: str
    assigned_object_id: int
    comments: str
    created_by: Union[None, Unset, int] = UNSET
    kind: Union[Unset, WritableJournalEntryRequestKind] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WritableJournalEntryRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned_object_type = self.assigned_object_type

        assigned_object_id = self.assigned_object_id

        comments = self.comments

        created_by: Union[None, Unset, int]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

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
                "assigned_object_type": assigned_object_type,
                "assigned_object_id": assigned_object_id,
                "comments": comments,
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

    def to_multipart(self) -> dict[str, Any]:
        assigned_object_type = (None, str(self.assigned_object_type).encode(), "text/plain")

        assigned_object_id = (None, str(self.assigned_object_id).encode(), "text/plain")

        comments = (None, str(self.comments).encode(), "text/plain")

        created_by: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, int):
            created_by = (None, str(self.created_by).encode(), "text/plain")
        else:
            created_by = (None, str(self.created_by).encode(), "text/plain")

        kind: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.kind, Unset):
            kind = (None, str(self.kind.value).encode(), "text/plain")

        tags: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tags, Unset):
            _temp_tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                _temp_tags.append(tags_item)
            tags = (None, json.dumps(_temp_tags).encode(), "application/json")

        custom_fields: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = (None, json.dumps(self.custom_fields.to_dict()).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "assigned_object_type": assigned_object_type,
                "assigned_object_id": assigned_object_id,
                "comments": comments,
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
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.writable_journal_entry_request_custom_fields import WritableJournalEntryRequestCustomFields

        d = dict(src_dict)
        assigned_object_type = d.pop("assigned_object_type")

        assigned_object_id = d.pop("assigned_object_id")

        comments = d.pop("comments")

        def _parse_created_by(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, WritableJournalEntryRequestKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = WritableJournalEntryRequestKind(_kind)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WritableJournalEntryRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WritableJournalEntryRequestCustomFields.from_dict(_custom_fields)

        writable_journal_entry_request = cls(
            assigned_object_type=assigned_object_type,
            assigned_object_id=assigned_object_id,
            comments=comments,
            created_by=created_by,
            kind=kind,
            tags=tags,
            custom_fields=custom_fields,
        )

        writable_journal_entry_request.additional_properties = d
        return writable_journal_entry_request

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
