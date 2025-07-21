import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_writable_event_rule_request_action_type import (
    PatchedWritableEventRuleRequestActionType,
)
from ..models.patched_writable_event_rule_request_event_types_item import (
    PatchedWritableEventRuleRequestEventTypesItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_writable_event_rule_request_custom_fields import (
        PatchedWritableEventRuleRequestCustomFields,
    )


T = TypeVar("T", bound="PatchedWritableEventRuleRequest")


@_attrs_define
class PatchedWritableEventRuleRequest:
    """Adds support for custom fields and tags.

    Attributes:
        object_types (Union[Unset, list[str]]):
        name (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        event_types (Union[Unset, list[PatchedWritableEventRuleRequestEventTypesItem]]): The types of event which will
            trigger this rule.
        conditions (Union[Unset, Any]): A set of conditions which determine whether the event will be generated.
        action_type (Union[Unset, PatchedWritableEventRuleRequestActionType]): * `webhook` - Webhook
            * `script` - Script
            * `notification` - Notification
        action_object_type (Union[Unset, str]):
        action_object_id (Union[None, Unset, int]):
        description (Union[Unset, str]):
        custom_fields (Union[Unset, PatchedWritableEventRuleRequestCustomFields]):
        tags (Union[Unset, list['NestedTagRequest']]):
    """

    object_types: Union[Unset, list[str]] = UNSET
    name: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    event_types: Union[Unset, list[PatchedWritableEventRuleRequestEventTypesItem]] = (
        UNSET
    )
    conditions: Union[Unset, Any] = UNSET
    action_type: Union[Unset, PatchedWritableEventRuleRequestActionType] = UNSET
    action_object_type: Union[Unset, str] = UNSET
    action_object_id: Union[None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, "PatchedWritableEventRuleRequestCustomFields"] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.object_types, Unset):
            object_types = self.object_types

        name = self.name

        enabled = self.enabled

        event_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = []
            for event_types_item_data in self.event_types:
                event_types_item = event_types_item_data.value
                event_types.append(event_types_item)

        conditions = self.conditions

        action_type: Union[Unset, str] = UNSET
        if not isinstance(self.action_type, Unset):
            action_type = self.action_type.value

        action_object_type = self.action_object_type

        action_object_id: Union[None, Unset, int]
        if isinstance(self.action_object_id, Unset):
            action_object_id = UNSET
        else:
            action_object_id = self.action_object_id

        description = self.description

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        tags: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_types is not UNSET:
            field_dict["object_types"] = object_types
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if action_type is not UNSET:
            field_dict["action_type"] = action_type
        if action_object_type is not UNSET:
            field_dict["action_object_type"] = action_object_type
        if action_object_id is not UNSET:
            field_dict["action_object_id"] = action_object_id
        if description is not UNSET:
            field_dict["description"] = description
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        object_types: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.object_types, Unset):
            _temp_object_types = self.object_types
            object_types = (
                None,
                json.dumps(_temp_object_types).encode(),
                "application/json",
            )

        name = (
            self.name
            if isinstance(self.name, Unset)
            else (None, str(self.name).encode(), "text/plain")
        )

        enabled = (
            self.enabled
            if isinstance(self.enabled, Unset)
            else (None, str(self.enabled).encode(), "text/plain")
        )

        event_types: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.event_types, Unset):
            _temp_event_types = []
            for event_types_item_data in self.event_types:
                event_types_item = event_types_item_data.value
                _temp_event_types.append(event_types_item)
            event_types = (
                None,
                json.dumps(_temp_event_types).encode(),
                "application/json",
            )

        conditions = (
            self.conditions
            if isinstance(self.conditions, Unset)
            else (None, str(self.conditions).encode(), "text/plain")
        )

        action_type: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.action_type, Unset):
            action_type = (None, str(self.action_type.value).encode(), "text/plain")

        action_object_type = (
            self.action_object_type
            if isinstance(self.action_object_type, Unset)
            else (None, str(self.action_object_type).encode(), "text/plain")
        )

        action_object_id: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.action_object_id, Unset):
            action_object_id = UNSET
        elif isinstance(self.action_object_id, int):
            action_object_id = (None, str(self.action_object_id).encode(), "text/plain")
        else:
            action_object_id = (None, str(self.action_object_id).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        custom_fields: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = (
                None,
                json.dumps(self.custom_fields.to_dict()).encode(),
                "application/json",
            )

        tags: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tags, Unset):
            _temp_tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                _temp_tags.append(tags_item)
            tags = (None, json.dumps(_temp_tags).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if object_types is not UNSET:
            field_dict["object_types"] = object_types
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if action_type is not UNSET:
            field_dict["action_type"] = action_type
        if action_object_type is not UNSET:
            field_dict["action_object_type"] = action_object_type
        if action_object_id is not UNSET:
            field_dict["action_object_id"] = action_object_id
        if description is not UNSET:
            field_dict["description"] = description
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_writable_event_rule_request_custom_fields import (
            PatchedWritableEventRuleRequestCustomFields,
        )

        d = dict(src_dict)
        object_types = cast(list[str], d.pop("object_types", UNSET))

        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        event_types = []
        _event_types = d.pop("event_types", UNSET)
        for event_types_item_data in _event_types or []:
            event_types_item = PatchedWritableEventRuleRequestEventTypesItem(
                event_types_item_data
            )

            event_types.append(event_types_item)

        conditions = d.pop("conditions", UNSET)

        _action_type = d.pop("action_type", UNSET)
        action_type: Union[Unset, PatchedWritableEventRuleRequestActionType]
        if isinstance(_action_type, Unset):
            action_type = UNSET
        else:
            action_type = PatchedWritableEventRuleRequestActionType(_action_type)

        action_object_type = d.pop("action_object_type", UNSET)

        def _parse_action_object_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        action_object_id = _parse_action_object_id(d.pop("action_object_id", UNSET))

        description = d.pop("description", UNSET)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedWritableEventRuleRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedWritableEventRuleRequestCustomFields.from_dict(
                _custom_fields
            )

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        patched_writable_event_rule_request = cls(
            object_types=object_types,
            name=name,
            enabled=enabled,
            event_types=event_types,
            conditions=conditions,
            action_type=action_type,
            action_object_type=action_object_type,
            action_object_id=action_object_id,
            description=description,
            custom_fields=custom_fields,
            tags=tags,
        )

        patched_writable_event_rule_request.additional_properties = d
        return patched_writable_event_rule_request

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
