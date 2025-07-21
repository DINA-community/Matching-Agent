import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_writable_power_port_request_type_type_1 import (
    PatchedWritablePowerPortRequestTypeType1,
)
from ..models.patched_writable_power_port_request_type_type_2_type_1 import (
    PatchedWritablePowerPortRequestTypeType2Type1,
)
from ..models.patched_writable_power_port_request_type_type_3_type_1 import (
    PatchedWritablePowerPortRequestTypeType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_request import BriefDeviceRequest
    from ..models.brief_module_request import BriefModuleRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_writable_power_port_request_custom_fields import (
        PatchedWritablePowerPortRequestCustomFields,
    )


T = TypeVar("T", bound="PatchedWritablePowerPortRequest")


@_attrs_define
class PatchedWritablePowerPortRequest:
    """Adds support for custom fields and tags.

    Attributes:
        device (Union['BriefDeviceRequest', Unset, int]):
        module (Union['BriefModuleRequest', None, Unset, int]):
        name (Union[Unset, str]):
        label (Union[Unset, str]): Physical label
        type_ (Union[None, PatchedWritablePowerPortRequestTypeType1, PatchedWritablePowerPortRequestTypeType2Type1,
            PatchedWritablePowerPortRequestTypeType3Type1, Unset]): Physical port type

            * `iec-60320-c6` - C6
            * `iec-60320-c8` - C8
            * `iec-60320-c14` - C14
            * `iec-60320-c16` - C16
            * `iec-60320-c20` - C20
            * `iec-60320-c22` - C22
            * `iec-60309-p-n-e-4h` - P+N+E 4H
            * `iec-60309-p-n-e-6h` - P+N+E 6H
            * `iec-60309-p-n-e-9h` - P+N+E 9H
            * `iec-60309-2p-e-4h` - 2P+E 4H
            * `iec-60309-2p-e-6h` - 2P+E 6H
            * `iec-60309-2p-e-9h` - 2P+E 9H
            * `iec-60309-3p-e-4h` - 3P+E 4H
            * `iec-60309-3p-e-6h` - 3P+E 6H
            * `iec-60309-3p-e-9h` - 3P+E 9H
            * `iec-60309-3p-n-e-4h` - 3P+N+E 4H
            * `iec-60309-3p-n-e-6h` - 3P+N+E 6H
            * `iec-60309-3p-n-e-9h` - 3P+N+E 9H
            * `iec-60906-1` - IEC 60906-1
            * `nbr-14136-10a` - 2P+T 10A (NBR 14136)
            * `nbr-14136-20a` - 2P+T 20A (NBR 14136)
            * `nema-1-15p` - NEMA 1-15P
            * `nema-5-15p` - NEMA 5-15P
            * `nema-5-20p` - NEMA 5-20P
            * `nema-5-30p` - NEMA 5-30P
            * `nema-5-50p` - NEMA 5-50P
            * `nema-6-15p` - NEMA 6-15P
            * `nema-6-20p` - NEMA 6-20P
            * `nema-6-30p` - NEMA 6-30P
            * `nema-6-50p` - NEMA 6-50P
            * `nema-10-30p` - NEMA 10-30P
            * `nema-10-50p` - NEMA 10-50P
            * `nema-14-20p` - NEMA 14-20P
            * `nema-14-30p` - NEMA 14-30P
            * `nema-14-50p` - NEMA 14-50P
            * `nema-14-60p` - NEMA 14-60P
            * `nema-15-15p` - NEMA 15-15P
            * `nema-15-20p` - NEMA 15-20P
            * `nema-15-30p` - NEMA 15-30P
            * `nema-15-50p` - NEMA 15-50P
            * `nema-15-60p` - NEMA 15-60P
            * `nema-l1-15p` - NEMA L1-15P
            * `nema-l5-15p` - NEMA L5-15P
            * `nema-l5-20p` - NEMA L5-20P
            * `nema-l5-30p` - NEMA L5-30P
            * `nema-l5-50p` - NEMA L5-50P
            * `nema-l6-15p` - NEMA L6-15P
            * `nema-l6-20p` - NEMA L6-20P
            * `nema-l6-30p` - NEMA L6-30P
            * `nema-l6-50p` - NEMA L6-50P
            * `nema-l10-30p` - NEMA L10-30P
            * `nema-l14-20p` - NEMA L14-20P
            * `nema-l14-30p` - NEMA L14-30P
            * `nema-l14-50p` - NEMA L14-50P
            * `nema-l14-60p` - NEMA L14-60P
            * `nema-l15-20p` - NEMA L15-20P
            * `nema-l15-30p` - NEMA L15-30P
            * `nema-l15-50p` - NEMA L15-50P
            * `nema-l15-60p` - NEMA L15-60P
            * `nema-l21-20p` - NEMA L21-20P
            * `nema-l21-30p` - NEMA L21-30P
            * `nema-l22-20p` - NEMA L22-20P
            * `nema-l22-30p` - NEMA L22-30P
            * `cs6361c` - CS6361C
            * `cs6365c` - CS6365C
            * `cs8165c` - CS8165C
            * `cs8265c` - CS8265C
            * `cs8365c` - CS8365C
            * `cs8465c` - CS8465C
            * `ita-c` - ITA Type C (CEE 7/16)
            * `ita-e` - ITA Type E (CEE 7/6)
            * `ita-f` - ITA Type F (CEE 7/4)
            * `ita-ef` - ITA Type E/F (CEE 7/7)
            * `ita-g` - ITA Type G (BS 1363)
            * `ita-h` - ITA Type H
            * `ita-i` - ITA Type I
            * `ita-j` - ITA Type J
            * `ita-k` - ITA Type K
            * `ita-l` - ITA Type L (CEI 23-50)
            * `ita-m` - ITA Type M (BS 546)
            * `ita-n` - ITA Type N
            * `ita-o` - ITA Type O
            * `usb-a` - USB Type A
            * `usb-b` - USB Type B
            * `usb-c` - USB Type C
            * `usb-mini-a` - USB Mini A
            * `usb-mini-b` - USB Mini B
            * `usb-micro-a` - USB Micro A
            * `usb-micro-b` - USB Micro B
            * `usb-micro-ab` - USB Micro AB
            * `usb-3-b` - USB 3.0 Type B
            * `usb-3-micro-b` - USB 3.0 Micro B
            * `molex-micro-fit-1x2` - Molex Micro-Fit 1x2
            * `molex-micro-fit-2x2` - Molex Micro-Fit 2x2
            * `molex-micro-fit-2x4` - Molex Micro-Fit 2x4
            * `dc-terminal` - DC Terminal
            * `saf-d-grid` - Saf-D-Grid
            * `neutrik-powercon-20` - Neutrik powerCON (20A)
            * `neutrik-powercon-32` - Neutrik powerCON (32A)
            * `neutrik-powercon-true1` - Neutrik powerCON TRUE1
            * `neutrik-powercon-true1-top` - Neutrik powerCON TRUE1 TOP
            * `ubiquiti-smartpower` - Ubiquiti SmartPower
            * `hardwired` - Hardwired
            * `other` - Other
        maximum_draw (Union[None, Unset, int]): Maximum power draw (watts)
        allocated_draw (Union[None, Unset, int]): Allocated power draw (watts)
        description (Union[Unset, str]):
        mark_connected (Union[Unset, bool]): Treat as if a cable is connected
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedWritablePowerPortRequestCustomFields]):
    """

    device: Union["BriefDeviceRequest", Unset, int] = UNSET
    module: Union["BriefModuleRequest", None, Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    type_: Union[
        None,
        PatchedWritablePowerPortRequestTypeType1,
        PatchedWritablePowerPortRequestTypeType2Type1,
        PatchedWritablePowerPortRequestTypeType3Type1,
        Unset,
    ] = UNSET
    maximum_draw: Union[None, Unset, int] = UNSET
    allocated_draw: Union[None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    mark_connected: Union[Unset, bool] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedWritablePowerPortRequestCustomFields"] = UNSET
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
        elif isinstance(self.type_, PatchedWritablePowerPortRequestTypeType1):
            type_ = self.type_.value
        elif isinstance(self.type_, PatchedWritablePowerPortRequestTypeType2Type1):
            type_ = self.type_.value
        elif isinstance(self.type_, PatchedWritablePowerPortRequestTypeType3Type1):
            type_ = self.type_.value
        else:
            type_ = self.type_

        maximum_draw: Union[None, Unset, int]
        if isinstance(self.maximum_draw, Unset):
            maximum_draw = UNSET
        else:
            maximum_draw = self.maximum_draw

        allocated_draw: Union[None, Unset, int]
        if isinstance(self.allocated_draw, Unset):
            allocated_draw = UNSET
        else:
            allocated_draw = self.allocated_draw

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
        if maximum_draw is not UNSET:
            field_dict["maximum_draw"] = maximum_draw
        if allocated_draw is not UNSET:
            field_dict["allocated_draw"] = allocated_draw
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
            device = (
                None,
                json.dumps(self.device.to_dict()).encode(),
                "application/json",
            )

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

        name = (
            self.name
            if isinstance(self.name, Unset)
            else (None, str(self.name).encode(), "text/plain")
        )

        label = (
            self.label
            if isinstance(self.label, Unset)
            else (None, str(self.label).encode(), "text/plain")
        )

        type_: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, None):
            type_ = (None, str(self.type_).encode(), "text/plain")
        elif isinstance(self.type_, PatchedWritablePowerPortRequestTypeType1):
            type_ = (None, str(self.type_.value).encode(), "text/plain")
        elif isinstance(self.type_, None):
            type_ = (None, str(self.type_).encode(), "text/plain")
        elif isinstance(self.type_, PatchedWritablePowerPortRequestTypeType2Type1):
            type_ = (None, str(self.type_.value).encode(), "text/plain")
        elif isinstance(self.type_, None):
            type_ = (None, str(self.type_).encode(), "text/plain")
        else:
            type_ = (None, str(self.type_.value).encode(), "text/plain")

        maximum_draw: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.maximum_draw, Unset):
            maximum_draw = UNSET
        elif isinstance(self.maximum_draw, int):
            maximum_draw = (None, str(self.maximum_draw).encode(), "text/plain")
        else:
            maximum_draw = (None, str(self.maximum_draw).encode(), "text/plain")

        allocated_draw: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.allocated_draw, Unset):
            allocated_draw = UNSET
        elif isinstance(self.allocated_draw, int):
            allocated_draw = (None, str(self.allocated_draw).encode(), "text/plain")
        else:
            allocated_draw = (None, str(self.allocated_draw).encode(), "text/plain")

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
        if maximum_draw is not UNSET:
            field_dict["maximum_draw"] = maximum_draw
        if allocated_draw is not UNSET:
            field_dict["allocated_draw"] = allocated_draw
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
        from ..models.patched_writable_power_port_request_custom_fields import (
            PatchedWritablePowerPortRequestCustomFields,
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

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        def _parse_type_(
            data: object,
        ) -> Union[
            None,
            PatchedWritablePowerPortRequestTypeType1,
            PatchedWritablePowerPortRequestTypeType2Type1,
            PatchedWritablePowerPortRequestTypeType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = PatchedWritablePowerPortRequestTypeType1(data)

                return type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_2_type_1 = PatchedWritablePowerPortRequestTypeType2Type1(data)

                return type_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_3_type_1 = PatchedWritablePowerPortRequestTypeType3Type1(data)

                return type_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PatchedWritablePowerPortRequestTypeType1,
                    PatchedWritablePowerPortRequestTypeType2Type1,
                    PatchedWritablePowerPortRequestTypeType3Type1,
                    Unset,
                ],
                data,
            )

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_maximum_draw(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        maximum_draw = _parse_maximum_draw(d.pop("maximum_draw", UNSET))

        def _parse_allocated_draw(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        allocated_draw = _parse_allocated_draw(d.pop("allocated_draw", UNSET))

        description = d.pop("description", UNSET)

        mark_connected = d.pop("mark_connected", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedWritablePowerPortRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedWritablePowerPortRequestCustomFields.from_dict(
                _custom_fields
            )

        patched_writable_power_port_request = cls(
            device=device,
            module=module,
            name=name,
            label=label,
            type_=type_,
            maximum_draw=maximum_draw,
            allocated_draw=allocated_draw,
            description=description,
            mark_connected=mark_connected,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_writable_power_port_request.additional_properties = d
        return patched_writable_power_port_request

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
