import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_address import IPAddress
    from ..models.nested_tag import NestedTag
    from ..models.service_custom_fields import ServiceCustomFields
    from ..models.service_protocol import ServiceProtocol


T = TypeVar("T", bound="Service")


@_attrs_define
class Service:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        parent_object_type (str):
        parent_object_id (int):
        parent (Any):
        name (str):
        ports (list[int]):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        protocol (Union[Unset, ServiceProtocol]):
        ipaddresses (Union[Unset, list['IPAddress']]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, ServiceCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    parent_object_type: str
    parent_object_id: int
    parent: Any
    name: str
    ports: list[int]
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    protocol: Union[Unset, "ServiceProtocol"] = UNSET
    ipaddresses: Union[Unset, list["IPAddress"]] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "ServiceCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        parent_object_type = self.parent_object_type

        parent_object_id = self.parent_object_id

        parent = self.parent

        name = self.name

        ports = self.ports

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

        protocol: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.to_dict()

        ipaddresses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ipaddresses, Unset):
            ipaddresses = []
            for ipaddresses_item_data in self.ipaddresses:
                ipaddresses_item = ipaddresses_item_data.to_dict()
                ipaddresses.append(ipaddresses_item)

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
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "parent_object_type": parent_object_type,
                "parent_object_id": parent_object_id,
                "parent": parent,
                "name": name,
                "ports": ports,
                "created": created,
                "last_updated": last_updated,
            }
        )
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
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
        from ..models.ip_address import IPAddress
        from ..models.nested_tag import NestedTag
        from ..models.service_custom_fields import ServiceCustomFields
        from ..models.service_protocol import ServiceProtocol

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        parent_object_type = d.pop("parent_object_type")

        parent_object_id = d.pop("parent_object_id")

        parent = d.pop("parent")

        name = d.pop("name")

        ports = cast(list[int], d.pop("ports"))

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

        _protocol = d.pop("protocol", UNSET)
        protocol: Union[Unset, ServiceProtocol]
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = ServiceProtocol.from_dict(_protocol)

        ipaddresses = []
        _ipaddresses = d.pop("ipaddresses", UNSET)
        for ipaddresses_item_data in _ipaddresses or []:
            ipaddresses_item = IPAddress.from_dict(ipaddresses_item_data)

            ipaddresses.append(ipaddresses_item)

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, ServiceCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ServiceCustomFields.from_dict(_custom_fields)

        service = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            parent_object_type=parent_object_type,
            parent_object_id=parent_object_id,
            parent=parent,
            name=name,
            ports=ports,
            created=created,
            last_updated=last_updated,
            protocol=protocol,
            ipaddresses=ipaddresses,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        service.additional_properties = d
        return service

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
