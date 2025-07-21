import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_service_request_protocol import WritableServiceRequestProtocol
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.writable_service_request_custom_fields import (
        WritableServiceRequestCustomFields,
    )


T = TypeVar("T", bound="WritableServiceRequest")


@_attrs_define
class WritableServiceRequest:
    """Adds support for custom fields and tags.

    Attributes:
        parent_object_type (str):
        parent_object_id (int):
        name (str):
        protocol (WritableServiceRequestProtocol): * `tcp` - TCP
            * `udp` - UDP
            * `sctp` - SCTP
        ports (list[int]):
        ipaddresses (Union[Unset, list[int]]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WritableServiceRequestCustomFields]):
    """

    parent_object_type: str
    parent_object_id: int
    name: str
    protocol: WritableServiceRequestProtocol
    ports: list[int]
    ipaddresses: Union[Unset, list[int]] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WritableServiceRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_object_type = self.parent_object_type

        parent_object_id = self.parent_object_id

        name = self.name

        protocol = self.protocol.value

        ports = self.ports

        ipaddresses: Union[Unset, list[int]] = UNSET
        if not isinstance(self.ipaddresses, Unset):
            ipaddresses = self.ipaddresses

        description = self.description

        comments = self.comments

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
                "parent_object_type": parent_object_type,
                "parent_object_id": parent_object_id,
                "name": name,
                "protocol": protocol,
                "ports": ports,
            }
        )
        if ipaddresses is not UNSET:
            field_dict["ipaddresses"] = ipaddresses
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        parent_object_type = (None, str(self.parent_object_type).encode(), "text/plain")

        parent_object_id = (None, str(self.parent_object_id).encode(), "text/plain")

        name = (None, str(self.name).encode(), "text/plain")

        protocol = (None, str(self.protocol.value).encode(), "text/plain")

        _temp_ports = self.ports
        ports = (None, json.dumps(_temp_ports).encode(), "application/json")

        ipaddresses: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.ipaddresses, Unset):
            _temp_ipaddresses = self.ipaddresses
            ipaddresses = (
                None,
                json.dumps(_temp_ipaddresses).encode(),
                "application/json",
            )

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        comments = (
            self.comments
            if isinstance(self.comments, Unset)
            else (None, str(self.comments).encode(), "text/plain")
        )

        tags: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tags, Unset):
            _temp_tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                _temp_tags.append(tags_item)
            tags = (None, json.dumps(_temp_tags).encode(), "application/json")

        custom_fields: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = (
                None,
                json.dumps(self.custom_fields.to_dict()).encode(),
                "application/json",
            )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "parent_object_type": parent_object_type,
                "parent_object_id": parent_object_id,
                "name": name,
                "protocol": protocol,
                "ports": ports,
            }
        )
        if ipaddresses is not UNSET:
            field_dict["ipaddresses"] = ipaddresses
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.writable_service_request_custom_fields import (
            WritableServiceRequestCustomFields,
        )

        d = dict(src_dict)
        parent_object_type = d.pop("parent_object_type")

        parent_object_id = d.pop("parent_object_id")

        name = d.pop("name")

        protocol = WritableServiceRequestProtocol(d.pop("protocol"))

        ports = cast(list[int], d.pop("ports"))

        ipaddresses = cast(list[int], d.pop("ipaddresses", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WritableServiceRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WritableServiceRequestCustomFields.from_dict(_custom_fields)

        writable_service_request = cls(
            parent_object_type=parent_object_type,
            parent_object_id=parent_object_id,
            name=name,
            protocol=protocol,
            ports=ports,
            ipaddresses=ipaddresses,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        writable_service_request.additional_properties = d
        return writable_service_request

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
