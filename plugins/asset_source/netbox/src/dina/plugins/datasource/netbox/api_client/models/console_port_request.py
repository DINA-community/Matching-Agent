from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.console_port_request_speed_type_1 import ConsolePortRequestSpeedType1
from ..models.console_port_request_speed_type_2_type_1 import (
    ConsolePortRequestSpeedType2Type1,
)
from ..models.console_port_request_speed_type_3_type_1 import (
    ConsolePortRequestSpeedType3Type1,
)
from ..models.console_port_request_type import ConsolePortRequestType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_request import BriefDeviceRequest
    from ..models.brief_module_request import BriefModuleRequest
    from ..models.console_port_request_custom_fields import (
        ConsolePortRequestCustomFields,
    )
    from ..models.nested_tag_request import NestedTagRequest


T = TypeVar("T", bound="ConsolePortRequest")


@_attrs_define
class ConsolePortRequest:
    """Adds support for custom fields and tags.

    Attributes:
        device (Union['BriefDeviceRequest', int]):
        name (str):
        module (Union['BriefModuleRequest', None, Unset, int]):
        label (Union[Unset, str]): Physical label
        type_ (Union[Unset, ConsolePortRequestType]): * `de-9` - DE-9
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
        speed (Union[ConsolePortRequestSpeedType1, ConsolePortRequestSpeedType2Type1, ConsolePortRequestSpeedType3Type1,
            None, Unset]): * `1200` - 1200 bps
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
        custom_fields (Union[Unset, ConsolePortRequestCustomFields]):
    """

    device: Union["BriefDeviceRequest", int]
    name: str
    module: Union["BriefModuleRequest", None, Unset, int] = UNSET
    label: Union[Unset, str] = UNSET
    type_: Union[Unset, ConsolePortRequestType] = UNSET
    speed: Union[
        ConsolePortRequestSpeedType1,
        ConsolePortRequestSpeedType2Type1,
        ConsolePortRequestSpeedType3Type1,
        None,
        Unset,
    ] = UNSET
    description: Union[Unset, str] = UNSET
    mark_connected: Union[Unset, bool] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "ConsolePortRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device_request import BriefDeviceRequest
        from ..models.brief_module_request import BriefModuleRequest

        device: Union[dict[str, Any], int]
        if isinstance(self.device, BriefDeviceRequest):
            device = self.device.to_dict()
        else:
            device = self.device

        name = self.name

        module: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.module, Unset):
            module = UNSET
        elif isinstance(self.module, BriefModuleRequest):
            module = self.module.to_dict()
        else:
            module = self.module

        label = self.label

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        speed: Union[None, Unset, int]
        if isinstance(self.speed, Unset):
            speed = UNSET
        elif isinstance(self.speed, ConsolePortRequestSpeedType1):
            speed = self.speed.value
        elif isinstance(self.speed, ConsolePortRequestSpeedType2Type1):
            speed = self.speed.value
        elif isinstance(self.speed, ConsolePortRequestSpeedType3Type1):
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
        field_dict.update(
            {
                "device": device,
                "name": name,
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
        from ..models.brief_device_request import BriefDeviceRequest
        from ..models.brief_module_request import BriefModuleRequest
        from ..models.console_port_request_custom_fields import (
            ConsolePortRequestCustomFields,
        )
        from ..models.nested_tag_request import NestedTagRequest

        d = dict(src_dict)

        def _parse_device(data: object) -> Union["BriefDeviceRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_type_1 = BriefDeviceRequest.from_dict(data)

                return device_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDeviceRequest", int], data)

        device = _parse_device(d.pop("device"))

        name = d.pop("name")

        def _parse_module(
            data: object,
        ) -> Union["BriefModuleRequest", None, Unset, int]:
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

        label = d.pop("label", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ConsolePortRequestType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ConsolePortRequestType(_type_)

        def _parse_speed(
            data: object,
        ) -> Union[
            ConsolePortRequestSpeedType1,
            ConsolePortRequestSpeedType2Type1,
            ConsolePortRequestSpeedType3Type1,
            None,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                speed_type_1 = ConsolePortRequestSpeedType1(data)

                return speed_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                speed_type_2_type_1 = ConsolePortRequestSpeedType2Type1(data)

                return speed_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, int):
                    raise TypeError()
                speed_type_3_type_1 = ConsolePortRequestSpeedType3Type1(data)

                return speed_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    ConsolePortRequestSpeedType1,
                    ConsolePortRequestSpeedType2Type1,
                    ConsolePortRequestSpeedType3Type1,
                    None,
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
        custom_fields: Union[Unset, ConsolePortRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ConsolePortRequestCustomFields.from_dict(_custom_fields)

        console_port_request = cls(
            device=device,
            name=name,
            module=module,
            label=label,
            type_=type_,
            speed=speed,
            description=description,
            mark_connected=mark_connected,
            tags=tags,
            custom_fields=custom_fields,
        )

        console_port_request.additional_properties = d
        return console_port_request

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
