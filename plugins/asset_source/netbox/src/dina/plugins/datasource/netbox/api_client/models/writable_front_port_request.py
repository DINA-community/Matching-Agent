import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_front_port_request_type import WritableFrontPortRequestType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_request import BriefDeviceRequest
    from ..models.brief_module_request import BriefModuleRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.writable_front_port_request_custom_fields import (
        WritableFrontPortRequestCustomFields,
    )


T = TypeVar("T", bound="WritableFrontPortRequest")


@_attrs_define
class WritableFrontPortRequest:
    """Adds support for custom fields and tags.

    Attributes:
        device (Union['BriefDeviceRequest', int]):
        name (str):
        type_ (WritableFrontPortRequestType): * `8p8c` - 8P8C
            * `8p6c` - 8P6C
            * `8p4c` - 8P4C
            * `8p2c` - 8P2C
            * `6p6c` - 6P6C
            * `6p4c` - 6P4C
            * `6p2c` - 6P2C
            * `4p4c` - 4P4C
            * `4p2c` - 4P2C
            * `gg45` - GG45
            * `tera-4p` - TERA 4P
            * `tera-2p` - TERA 2P
            * `tera-1p` - TERA 1P
            * `110-punch` - 110 Punch
            * `bnc` - BNC
            * `f` - F Connector
            * `n` - N Connector
            * `mrj21` - MRJ21
            * `fc` - FC
            * `fc-pc` - FC/PC
            * `fc-upc` - FC/UPC
            * `fc-apc` - FC/APC
            * `lc` - LC
            * `lc-pc` - LC/PC
            * `lc-upc` - LC/UPC
            * `lc-apc` - LC/APC
            * `lsh` - LSH
            * `lsh-pc` - LSH/PC
            * `lsh-upc` - LSH/UPC
            * `lsh-apc` - LSH/APC
            * `lx5` - LX.5
            * `lx5-pc` - LX.5/PC
            * `lx5-upc` - LX.5/UPC
            * `lx5-apc` - LX.5/APC
            * `mpo` - MPO
            * `mtrj` - MTRJ
            * `sc` - SC
            * `sc-pc` - SC/PC
            * `sc-upc` - SC/UPC
            * `sc-apc` - SC/APC
            * `st` - ST
            * `cs` - CS
            * `sn` - SN
            * `sma-905` - SMA 905
            * `sma-906` - SMA 906
            * `urm-p2` - URM-P2
            * `urm-p4` - URM-P4
            * `urm-p8` - URM-P8
            * `splice` - Splice
            * `usb-a` - USB Type A
            * `usb-b` - USB Type B
            * `usb-c` - USB Type C
            * `usb-mini-a` - USB Mini A
            * `usb-mini-b` - USB Mini B
            * `usb-micro-a` - USB Micro A
            * `usb-micro-b` - USB Micro B
            * `usb-micro-ab` - USB Micro AB
            * `other` - Other
        rear_port (int):
        module (Union['BriefModuleRequest', None, Unset, int]):
        label (Union[Unset, str]): Physical label
        color (Union[Unset, str]):
        rear_port_position (Union[Unset, int]): Mapped position on corresponding rear port
        description (Union[Unset, str]):
        mark_connected (Union[Unset, bool]): Treat as if a cable is connected
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WritableFrontPortRequestCustomFields]):
    """

    device: Union["BriefDeviceRequest", int]
    name: str
    type_: WritableFrontPortRequestType
    rear_port: int
    module: Union["BriefModuleRequest", None, Unset, int] = UNSET
    label: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    rear_port_position: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    mark_connected: Union[Unset, bool] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WritableFrontPortRequestCustomFields"] = UNSET
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

        type_ = self.type_.value

        rear_port = self.rear_port

        module: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.module, Unset):
            module = UNSET
        elif isinstance(self.module, BriefModuleRequest):
            module = self.module.to_dict()
        else:
            module = self.module

        label = self.label

        color = self.color

        rear_port_position = self.rear_port_position

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
                "type": type_,
                "rear_port": rear_port,
            }
        )
        if module is not UNSET:
            field_dict["module"] = module
        if label is not UNSET:
            field_dict["label"] = label
        if color is not UNSET:
            field_dict["color"] = color
        if rear_port_position is not UNSET:
            field_dict["rear_port_position"] = rear_port_position
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
        device: tuple[None, bytes, str]

        if isinstance(self.device, int):
            device = (None, str(self.device).encode(), "text/plain")
        else:
            device = (
                None,
                json.dumps(self.device.to_dict()).encode(),
                "application/json",
            )

        name = (None, str(self.name).encode(), "text/plain")

        type_ = (None, str(self.type_.value).encode(), "text/plain")

        rear_port = (None, str(self.rear_port).encode(), "text/plain")

        module: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.module, Unset):
            module = UNSET
        elif isinstance(self.module, int):
            module = (None, str(self.module).encode(), "text/plain")
        elif isinstance(self.module, None):
            module = (None, str(self.module).encode(), "text/plain")
        elif isinstance(self.module, BriefModuleRequest):
            module = (
                None,
                json.dumps(self.module.to_dict()).encode(),
                "application/json",
            )
        else:
            module = (None, str(self.module).encode(), "text/plain")

        label = (
            self.label
            if isinstance(self.label, Unset)
            else (None, str(self.label).encode(), "text/plain")
        )

        color = (
            self.color
            if isinstance(self.color, Unset)
            else (None, str(self.color).encode(), "text/plain")
        )

        rear_port_position = (
            self.rear_port_position
            if isinstance(self.rear_port_position, Unset)
            else (None, str(self.rear_port_position).encode(), "text/plain")
        )

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
                "device": device,
                "name": name,
                "type": type_,
                "rear_port": rear_port,
            }
        )
        if module is not UNSET:
            field_dict["module"] = module
        if label is not UNSET:
            field_dict["label"] = label
        if color is not UNSET:
            field_dict["color"] = color
        if rear_port_position is not UNSET:
            field_dict["rear_port_position"] = rear_port_position
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
        from ..models.writable_front_port_request_custom_fields import (
            WritableFrontPortRequestCustomFields,
        )

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

        type_ = WritableFrontPortRequestType(d.pop("type"))

        rear_port = d.pop("rear_port")

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

        color = d.pop("color", UNSET)

        rear_port_position = d.pop("rear_port_position", UNSET)

        description = d.pop("description", UNSET)

        mark_connected = d.pop("mark_connected", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WritableFrontPortRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WritableFrontPortRequestCustomFields.from_dict(
                _custom_fields
            )

        writable_front_port_request = cls(
            device=device,
            name=name,
            type_=type_,
            rear_port=rear_port,
            module=module,
            label=label,
            color=color,
            rear_port_position=rear_port_position,
            description=description,
            mark_connected=mark_connected,
            tags=tags,
            custom_fields=custom_fields,
        )

        writable_front_port_request.additional_properties = d
        return writable_front_port_request

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
