import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_cable import BriefCable
    from ..models.brief_device import BriefDevice
    from ..models.brief_module import BriefModule
    from ..models.console_server_port_custom_fields import ConsoleServerPortCustomFields
    from ..models.console_server_port_speed_type_0 import ConsoleServerPortSpeedType0
    from ..models.console_server_port_type import ConsoleServerPortType
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="ConsoleServerPort")


@_attrs_define
class ConsoleServerPort:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        device (BriefDevice): Adds support for custom fields and tags.
        name (str):
        cable (Union['BriefCable', None]):
        cable_end (str):
        link_peers (list[Any]):
        link_peers_type (Union[None, str]): Return the type of the peer link terminations, or None.
        connected_endpoints (Union[None, list[Any]]):
        connected_endpoints_type (Union[None, str]):
        connected_endpoints_reachable (bool):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        field_occupied (bool):
        module (Union['BriefModule', None, Unset]):
        label (Union[Unset, str]): Physical label
        type_ (Union[Unset, ConsoleServerPortType]):
        speed (Union['ConsoleServerPortSpeedType0', None, Unset]):
        description (Union[Unset, str]):
        mark_connected (Union[Unset, bool]): Treat as if a cable is connected
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, ConsoleServerPortCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    device: "BriefDevice"
    name: str
    cable: Union["BriefCable", None]
    cable_end: str
    link_peers: list[Any]
    link_peers_type: Union[None, str]
    connected_endpoints: Union[None, list[Any]]
    connected_endpoints_type: Union[None, str]
    connected_endpoints_reachable: bool
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    field_occupied: bool
    module: Union["BriefModule", None, Unset] = UNSET
    label: Union[Unset, str] = UNSET
    type_: Union[Unset, "ConsoleServerPortType"] = UNSET
    speed: Union["ConsoleServerPortSpeedType0", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    mark_connected: Union[Unset, bool] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "ConsoleServerPortCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_cable import BriefCable
        from ..models.brief_module import BriefModule
        from ..models.console_server_port_speed_type_0 import (
            ConsoleServerPortSpeedType0,
        )

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        device = self.device.to_dict()

        name = self.name

        cable: Union[None, dict[str, Any]]
        if isinstance(self.cable, BriefCable):
            cable = self.cable.to_dict()
        else:
            cable = self.cable

        cable_end = self.cable_end

        link_peers = self.link_peers

        link_peers_type: Union[None, str]
        link_peers_type = self.link_peers_type

        connected_endpoints: Union[None, list[Any]]
        if isinstance(self.connected_endpoints, list):
            connected_endpoints = self.connected_endpoints

        else:
            connected_endpoints = self.connected_endpoints

        connected_endpoints_type: Union[None, str]
        connected_endpoints_type = self.connected_endpoints_type

        connected_endpoints_reachable = self.connected_endpoints_reachable

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

        field_occupied = self.field_occupied

        module: Union[None, Unset, dict[str, Any]]
        if isinstance(self.module, Unset):
            module = UNSET
        elif isinstance(self.module, BriefModule):
            module = self.module.to_dict()
        else:
            module = self.module

        label = self.label

        type_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        speed: Union[None, Unset, dict[str, Any]]
        if isinstance(self.speed, Unset):
            speed = UNSET
        elif isinstance(self.speed, ConsoleServerPortSpeedType0):
            speed = self.speed.to_dict()
        else:
            speed = self.speed

        description = self.description

        mark_connected = self.mark_connected

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
                "device": device,
                "name": name,
                "cable": cable,
                "cable_end": cable_end,
                "link_peers": link_peers,
                "link_peers_type": link_peers_type,
                "connected_endpoints": connected_endpoints,
                "connected_endpoints_type": connected_endpoints_type,
                "connected_endpoints_reachable": connected_endpoints_reachable,
                "created": created,
                "last_updated": last_updated,
                "_occupied": field_occupied,
            }
        )
        if module is not UNSET:
            field_dict["module"] = module
        if label is not UNSET:
            field_dict["label"] = label
        if type_ is not UNSET:
            field_dict["type"] = type_
        if speed is not UNSET:
            field_dict["speed"] = speed
        if description is not UNSET:
            field_dict["description"] = description
        if mark_connected is not UNSET:
            field_dict["mark_connected"] = mark_connected
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_cable import BriefCable
        from ..models.brief_device import BriefDevice
        from ..models.brief_module import BriefModule
        from ..models.console_server_port_custom_fields import (
            ConsoleServerPortCustomFields,
        )
        from ..models.console_server_port_speed_type_0 import (
            ConsoleServerPortSpeedType0,
        )
        from ..models.console_server_port_type import ConsoleServerPortType
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        device = BriefDevice.from_dict(d.pop("device"))

        name = d.pop("name")

        def _parse_cable(data: object) -> Union["BriefCable", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cable_type_1 = BriefCable.from_dict(data)

                return cable_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefCable", None], data)

        cable = _parse_cable(d.pop("cable"))

        cable_end = d.pop("cable_end")

        link_peers = cast(list[Any], d.pop("link_peers"))

        def _parse_link_peers_type(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        link_peers_type = _parse_link_peers_type(d.pop("link_peers_type"))

        def _parse_connected_endpoints(data: object) -> Union[None, list[Any]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                connected_endpoints_type_0 = cast(list[Any], data)

                return connected_endpoints_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[Any]], data)

        connected_endpoints = _parse_connected_endpoints(d.pop("connected_endpoints"))

        def _parse_connected_endpoints_type(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        connected_endpoints_type = _parse_connected_endpoints_type(
            d.pop("connected_endpoints_type")
        )

        connected_endpoints_reachable = d.pop("connected_endpoints_reachable")

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

        field_occupied = d.pop("_occupied")

        def _parse_module(data: object) -> Union["BriefModule", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                module_type_1 = BriefModule.from_dict(data)

                return module_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefModule", None, Unset], data)

        module = _parse_module(d.pop("module", UNSET))

        label = d.pop("label", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ConsoleServerPortType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ConsoleServerPortType.from_dict(_type_)

        def _parse_speed(
            data: object,
        ) -> Union["ConsoleServerPortSpeedType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                speed_type_0 = ConsoleServerPortSpeedType0.from_dict(data)

                return speed_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ConsoleServerPortSpeedType0", None, Unset], data)

        speed = _parse_speed(d.pop("speed", UNSET))

        description = d.pop("description", UNSET)

        mark_connected = d.pop("mark_connected", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, ConsoleServerPortCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ConsoleServerPortCustomFields.from_dict(_custom_fields)

        console_server_port = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            device=device,
            name=name,
            cable=cable,
            cable_end=cable_end,
            link_peers=link_peers,
            link_peers_type=link_peers_type,
            connected_endpoints=connected_endpoints,
            connected_endpoints_type=connected_endpoints_type,
            connected_endpoints_reachable=connected_endpoints_reachable,
            created=created,
            last_updated=last_updated,
            field_occupied=field_occupied,
            module=module,
            label=label,
            type_=type_,
            speed=speed,
            description=description,
            mark_connected=mark_connected,
            tags=tags,
            custom_fields=custom_fields,
        )

        console_server_port.additional_properties = d
        return console_server_port

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
