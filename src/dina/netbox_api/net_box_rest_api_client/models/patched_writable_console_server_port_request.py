import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_writable_console_server_port_request_speed_type_1 import (
    PatchedWritableConsoleServerPortRequestSpeedType1,
)
from ..models.patched_writable_console_server_port_request_speed_type_2_type_1 import (
    PatchedWritableConsoleServerPortRequestSpeedType2Type1,
)
from ..models.patched_writable_console_server_port_request_speed_type_3_type_1 import (
    PatchedWritableConsoleServerPortRequestSpeedType3Type1,
)
from ..models.patched_writable_console_server_port_request_type_type_1 import (
    PatchedWritableConsoleServerPortRequestTypeType1,
)
from ..models.patched_writable_console_server_port_request_type_type_2_type_1 import (
    PatchedWritableConsoleServerPortRequestTypeType2Type1,
)
from ..models.patched_writable_console_server_port_request_type_type_3_type_1 import (
    PatchedWritableConsoleServerPortRequestTypeType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_request import BriefDeviceRequest
    from ..models.brief_module_request import BriefModuleRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_writable_console_server_port_request_custom_fields import (
        PatchedWritableConsoleServerPortRequestCustomFields,
    )


T = TypeVar("T", bound="PatchedWritableConsoleServerPortRequest")


@_attrs_define
class PatchedWritableConsoleServerPortRequest:
    """Adds support for custom fields and tags.

    Attributes:
        device (Union['BriefDeviceRequest', Unset, int]):
        module (Union['BriefModuleRequest', None, Unset, int]):
        name (Union[Unset, str]):
        label (Union[Unset, str]): Physical label
        type_ (Union[None, PatchedWritableConsoleServerPortRequestTypeType1,
            PatchedWritableConsoleServerPortRequestTypeType2Type1, PatchedWritableConsoleServerPortRequestTypeType3Type1,
            Unset]): Physical port type

            * `de-9` - DE-9
            * `db-25` - DB-25
            * `rj-11` - RJ-11
            * `rj-12` - RJ-12
            * `rj-45` - RJ-45
            * `mini-din-8` - Mini-DIN 8
            * `usb-a` - USB Type A
            * `usb-b` - USB Type B
            * `usb-c` - USB Type C
            * `usb-mini-a` - USB Mini A
            * `usb-mini-b` - USB Mini B
            * `usb-micro-a` - USB Micro A
            * `usb-micro-b` - USB Micro B
            * `usb-micro-ab` - USB Micro AB
            * `other` - Other
        speed (Union[None, PatchedWritableConsoleServerPortRequestSpeedType1,
            PatchedWritableConsoleServerPortRequestSpeedType2Type1, PatchedWritableConsoleServerPortRequestSpeedType3Type1,
            Unset]): Port speed in bits per second

            * `1200` - 1200 bps
            * `2400` - 2400 bps
            * `4800` - 4800 bps
            * `9600` - 9600 bps
            * `19200` - 19.2 kbps
            * `38400` - 38.4 kbps
            * `57600` - 57.6 kbps
            * `115200` - 115.2 kbps
        description (Union[Unset, str]):
        mark_connected (Union[Unset, bool]): Treat as if a cable is connected
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedWritableConsoleServerPortRequestCustomFields]):
    """

    device: Union["BriefDeviceRequest", Unset, int] = UNSET
    module: Union["BriefModuleRequest", None, Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    type_: Union[
        None,
        PatchedWritableConsoleServerPortRequestTypeType1,
        PatchedWritableConsoleServerPortRequestTypeType2Type1,
        PatchedWritableConsoleServerPortRequestTypeType3Type1,
        Unset,
    ] = UNSET
    speed: Union[
        None,
        PatchedWritableConsoleServerPortRequestSpeedType1,
        PatchedWritableConsoleServerPortRequestSpeedType2Type1,
        PatchedWritableConsoleServerPortRequestSpeedType3Type1,
        Unset,
    ] = UNSET
    description: Union[Unset, str] = UNSET
    mark_connected: Union[Unset, bool] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedWritableConsoleServerPortRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device_request import BriefDeviceRequest
        from ..models.brief_module_request import BriefModuleRequest

        device: Union[Unset, dict[str, Any], int]
        if isinstance(self.device, Unset):
            device = UNSET
        elif isinstance(self.device, BriefDeviceRequest):
            device = self.device.to_dict()
        else:
            device = self.device

        module: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.module, Unset):
            module = UNSET
        elif isinstance(self.module, BriefModuleRequest):
            module = self.module.to_dict()
        else:
            module = self.module

        name = self.name

        label = self.label

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, PatchedWritableConsoleServerPortRequestTypeType1):
            type_ = self.type_.value
        elif isinstance(self.type_, PatchedWritableConsoleServerPortRequestTypeType2Type1):
            type_ = self.type_.value
        elif isinstance(self.type_, PatchedWritableConsoleServerPortRequestTypeType3Type1):
            type_ = self.type_.value
        else:
            type_ = self.type_

        speed: Union[None, Unset, int]
        if isinstance(self.speed, Unset):
            speed = UNSET
        elif isinstance(self.speed, PatchedWritableConsoleServerPortRequestSpeedType1):
            speed = self.speed.value
        elif isinstance(self.speed, PatchedWritableConsoleServerPortRequestSpeedType2Type1):
            speed = self.speed.value
        elif isinstance(self.speed, PatchedWritableConsoleServerPortRequestSpeedType3Type1):
            speed = self.speed.value
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
        field_dict.update({})
        if device is not UNSET:
            field_dict["device"] = device
        if module is not UNSET:
            field_dict["module"] = module
        if name is not UNSET:
            field_dict["name"] = name
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

    def to_multipart(self) -> dict[str, Any]:
        device: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.device, Unset):
            device = UNSET
        elif isinstance(self.device, int):
            device = (None, str(self.device).encode(), "text/plain")
        else:
            device = (None, json.dumps(self.device.to_dict()).encode(), "application/json")

        module: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.module, Unset):
            module = UNSET
        elif isinstance(self.module, int):
            module = (None, str(self.module).encode(), "text/plain")
        elif isinstance(self.module, None):
            module = (None, str(self.module).encode(), "text/plain")
        elif isinstance(self.module, BriefModuleRequest):
            module = (None, json.dumps(self.module.to_dict()).encode(), "application/json")
        else:
            module = (None, str(self.module).encode(), "text/plain")

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        label = self.label if isinstance(self.label, Unset) else (None, str(self.label).encode(), "text/plain")

        type_: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, None):
            type_ = (None, str(self.type_).encode(), "text/plain")
        elif isinstance(self.type_, PatchedWritableConsoleServerPortRequestTypeType1):
            type_ = (None, str(self.type_.value).encode(), "text/plain")
        elif isinstance(self.type_, None):
            type_ = (None, str(self.type_).encode(), "text/plain")
        elif isinstance(self.type_, PatchedWritableConsoleServerPortRequestTypeType2Type1):
            type_ = (None, str(self.type_.value).encode(), "text/plain")
        elif isinstance(self.type_, None):
            type_ = (None, str(self.type_).encode(), "text/plain")
        else:
            type_ = (None, str(self.type_.value).encode(), "text/plain")

        speed: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.speed, Unset):
            speed = UNSET
        elif isinstance(self.speed, None):
            speed = (None, str(self.speed).encode(), "text/plain")
        elif isinstance(self.speed, PatchedWritableConsoleServerPortRequestSpeedType1):
            speed = (None, str(self.speed.value).encode(), "text/plain")
        elif isinstance(self.speed, None):
            speed = (None, str(self.speed).encode(), "text/plain")
        elif isinstance(self.speed, PatchedWritableConsoleServerPortRequestSpeedType2Type1):
            speed = (None, str(self.speed.value).encode(), "text/plain")
        elif isinstance(self.speed, None):
            speed = (None, str(self.speed).encode(), "text/plain")
        else:
            speed = (None, str(self.speed.value).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        mark_connected = (
            self.mark_connected
            if isinstance(self.mark_connected, Unset)
            else (None, str(self.mark_connected).encode(), "text/plain")
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
            custom_fields = (None, json.dumps(self.custom_fields.to_dict()).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if device is not UNSET:
            field_dict["device"] = device
        if module is not UNSET:
            field_dict["module"] = module
        if name is not UNSET:
            field_dict["name"] = name
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
        from ..models.brief_device_request import BriefDeviceRequest
        from ..models.brief_module_request import BriefModuleRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_writable_console_server_port_request_custom_fields import (
            PatchedWritableConsoleServerPortRequestCustomFields,
        )

        d = dict(src_dict)

        def _parse_device(data: object) -> Union["BriefDeviceRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_type_1 = BriefDeviceRequest.from_dict(data)

                return device_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDeviceRequest", Unset, int], data)

        device = _parse_device(d.pop("device", UNSET))

        def _parse_module(data: object) -> Union["BriefModuleRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                module_type_1_type_1 = BriefModuleRequest.from_dict(data)

                return module_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefModuleRequest", None, Unset, int], data)

        module = _parse_module(d.pop("module", UNSET))

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        def _parse_type_(
            data: object,
        ) -> Union[
            None,
            PatchedWritableConsoleServerPortRequestTypeType1,
            PatchedWritableConsoleServerPortRequestTypeType2Type1,
            PatchedWritableConsoleServerPortRequestTypeType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = PatchedWritableConsoleServerPortRequestTypeType1(data)

                return type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_2_type_1 = PatchedWritableConsoleServerPortRequestTypeType2Type1(data)

                return type_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_3_type_1 = PatchedWritableConsoleServerPortRequestTypeType3Type1(data)

                return type_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PatchedWritableConsoleServerPortRequestTypeType1,
                    PatchedWritableConsoleServerPortRequestTypeType2Type1,
                    PatchedWritableConsoleServerPortRequestTypeType3Type1,
                    Unset,
                ],
                data,
            )

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_speed(
            data: object,
        ) -> Union[
            None,
            PatchedWritableConsoleServerPortRequestSpeedType1,
            PatchedWritableConsoleServerPortRequestSpeedType2Type1,
            PatchedWritableConsoleServerPortRequestSpeedType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                speed_type_1 = PatchedWritableConsoleServerPortRequestSpeedType1(data)

                return speed_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                speed_type_2_type_1 = PatchedWritableConsoleServerPortRequestSpeedType2Type1(data)

                return speed_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                speed_type_3_type_1 = PatchedWritableConsoleServerPortRequestSpeedType3Type1(data)

                return speed_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PatchedWritableConsoleServerPortRequestSpeedType1,
                    PatchedWritableConsoleServerPortRequestSpeedType2Type1,
                    PatchedWritableConsoleServerPortRequestSpeedType3Type1,
                    Unset,
                ],
                data,
            )

        speed = _parse_speed(d.pop("speed", UNSET))

        description = d.pop("description", UNSET)

        mark_connected = d.pop("mark_connected", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedWritableConsoleServerPortRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedWritableConsoleServerPortRequestCustomFields.from_dict(_custom_fields)

        patched_writable_console_server_port_request = cls(
            device=device,
            module=module,
            name=name,
            label=label,
            type_=type_,
            speed=speed,
            description=description,
            mark_connected=mark_connected,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_writable_console_server_port_request.additional_properties = d
        return patched_writable_console_server_port_request

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
