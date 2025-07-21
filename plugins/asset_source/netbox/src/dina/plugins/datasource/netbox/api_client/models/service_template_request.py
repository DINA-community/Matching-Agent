from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_template_request_protocol import ServiceTemplateRequestProtocol
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.service_template_request_custom_fields import (
        ServiceTemplateRequestCustomFields,
    )


T = TypeVar("T", bound="ServiceTemplateRequest")


@_attrs_define
class ServiceTemplateRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str):
        ports (list[int]):
        protocol (Union[Unset, ServiceTemplateRequestProtocol]): * `tcp` - TCP
            * `udp` - UDP
            * `sctp` - SCTP
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, ServiceTemplateRequestCustomFields]):
    """

    name: str
    ports: list[int]
    protocol: Union[Unset, ServiceTemplateRequestProtocol] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "ServiceTemplateRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        ports = self.ports

        protocol: Union[Unset, str] = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

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
                "name": name,
                "ports": ports,
            }
        )
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
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
        from ..models.service_template_request_custom_fields import (
            ServiceTemplateRequestCustomFields,
        )

        d = dict(src_dict)
        name = d.pop("name")

        ports = cast(list[int], d.pop("ports"))

        _protocol = d.pop("protocol", UNSET)
        protocol: Union[Unset, ServiceTemplateRequestProtocol]
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = ServiceTemplateRequestProtocol(_protocol)

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, ServiceTemplateRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ServiceTemplateRequestCustomFields.from_dict(_custom_fields)

        service_template_request = cls(
            name=name,
            ports=ports,
            protocol=protocol,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        service_template_request.additional_properties = d
        return service_template_request

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
