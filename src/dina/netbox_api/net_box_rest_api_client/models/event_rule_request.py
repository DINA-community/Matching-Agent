from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_rule_request_action_type import EventRuleRequestActionType
from ..models.event_rule_request_event_types_item import EventRuleRequestEventTypesItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_rule_request_custom_fields import EventRuleRequestCustomFields
    from ..models.nested_tag_request import NestedTagRequest


T = TypeVar("T", bound="EventRuleRequest")


@_attrs_define
class EventRuleRequest:
    """Adds support for custom fields and tags.

    Attributes:
        object_types (list[str]):
        name (str):
        event_types (list[EventRuleRequestEventTypesItem]): The types of event which will trigger this rule.
        action_type (EventRuleRequestActionType): * `webhook` - Webhook
            * `script` - Script
            * `notification` - Notification
        action_object_type (str):
        enabled (Union[Unset, bool]):
        conditions (Union[Unset, Any]): A set of conditions which determine whether the event will be generated.
        action_object_id (Union[None, Unset, int]):
        description (Union[Unset, str]):
        custom_fields (Union[Unset, EventRuleRequestCustomFields]):
        tags (Union[Unset, list['NestedTagRequest']]):
    """

    object_types: list[str]
    name: str
    event_types: list[EventRuleRequestEventTypesItem]
    action_type: EventRuleRequestActionType
    action_object_type: str
    enabled: Union[Unset, bool] = UNSET
    conditions: Union[Unset, Any] = UNSET
    action_object_id: Union[None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, "EventRuleRequestCustomFields"] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_types = self.object_types

        name = self.name

        event_types = []
        for event_types_item_data in self.event_types:
            event_types_item = event_types_item_data.value
            event_types.append(event_types_item)

        action_type = self.action_type.value

        action_object_type = self.action_object_type

        enabled = self.enabled

        conditions = self.conditions

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
        field_dict.update(
            {
                "object_types": object_types,
                "name": name,
                "event_types": event_types,
                "action_type": action_type,
                "action_object_type": action_object_type,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
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
        from ..models.event_rule_request_custom_fields import EventRuleRequestCustomFields
        from ..models.nested_tag_request import NestedTagRequest

        d = dict(src_dict)
        object_types = cast(list[str], d.pop("object_types"))

        name = d.pop("name")

        event_types = []
        _event_types = d.pop("event_types")
        for event_types_item_data in _event_types:
            event_types_item = EventRuleRequestEventTypesItem(event_types_item_data)

            event_types.append(event_types_item)

        action_type = EventRuleRequestActionType(d.pop("action_type"))

        action_object_type = d.pop("action_object_type")

        enabled = d.pop("enabled", UNSET)

        conditions = d.pop("conditions", UNSET)

        def _parse_action_object_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        action_object_id = _parse_action_object_id(d.pop("action_object_id", UNSET))

        description = d.pop("description", UNSET)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, EventRuleRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = EventRuleRequestCustomFields.from_dict(_custom_fields)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        event_rule_request = cls(
            object_types=object_types,
            name=name,
            event_types=event_types,
            action_type=action_type,
            action_object_type=action_object_type,
            enabled=enabled,
            conditions=conditions,
            action_object_id=action_object_id,
            description=description,
            custom_fields=custom_fields,
            tags=tags,
        )

        event_rule_request.additional_properties = d
        return event_rule_request

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
