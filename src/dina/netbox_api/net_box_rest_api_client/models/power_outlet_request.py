from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.power_outlet_request_feed_leg_type_1 import PowerOutletRequestFeedLegType1
from ..models.power_outlet_request_feed_leg_type_2_type_1 import PowerOutletRequestFeedLegType2Type1
from ..models.power_outlet_request_feed_leg_type_3_type_1 import PowerOutletRequestFeedLegType3Type1
from ..models.power_outlet_request_status import PowerOutletRequestStatus
from ..models.power_outlet_request_type_type_1 import PowerOutletRequestTypeType1
from ..models.power_outlet_request_type_type_2_type_1 import PowerOutletRequestTypeType2Type1
from ..models.power_outlet_request_type_type_3_type_1 import PowerOutletRequestTypeType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_request import BriefDeviceRequest
    from ..models.brief_module_request import BriefModuleRequest
    from ..models.brief_power_port_request import BriefPowerPortRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.power_outlet_request_custom_fields import PowerOutletRequestCustomFields


T = TypeVar("T", bound="PowerOutletRequest")


@_attrs_define
class PowerOutletRequest:
    """Adds support for custom fields and tags.

    Attributes:
        device (Union['BriefDeviceRequest', int]):
        name (str):
        module (Union['BriefModuleRequest', None, Unset, int]):
        label (Union[Unset, str]): Physical label
        type_ (Union[None, PowerOutletRequestTypeType1, PowerOutletRequestTypeType2Type1,
            PowerOutletRequestTypeType3Type1, Unset]): * `iec-60320-c5` - C5
            * `iec-60320-c7` - C7
            * `iec-60320-c13` - C13
            * `iec-60320-c15` - C15
            * `iec-60320-c19` - C19
            * `iec-60320-c21` - C21
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
            * `nema-1-15r` - NEMA 1-15R
            * `nema-5-15r` - NEMA 5-15R
            * `nema-5-20r` - NEMA 5-20R
            * `nema-5-30r` - NEMA 5-30R
            * `nema-5-50r` - NEMA 5-50R
            * `nema-6-15r` - NEMA 6-15R
            * `nema-6-20r` - NEMA 6-20R
            * `nema-6-30r` - NEMA 6-30R
            * `nema-6-50r` - NEMA 6-50R
            * `nema-10-30r` - NEMA 10-30R
            * `nema-10-50r` - NEMA 10-50R
            * `nema-14-20r` - NEMA 14-20R
            * `nema-14-30r` - NEMA 14-30R
            * `nema-14-50r` - NEMA 14-50R
            * `nema-14-60r` - NEMA 14-60R
            * `nema-15-15r` - NEMA 15-15R
            * `nema-15-20r` - NEMA 15-20R
            * `nema-15-30r` - NEMA 15-30R
            * `nema-15-50r` - NEMA 15-50R
            * `nema-15-60r` - NEMA 15-60R
            * `nema-l1-15r` - NEMA L1-15R
            * `nema-l5-15r` - NEMA L5-15R
            * `nema-l5-20r` - NEMA L5-20R
            * `nema-l5-30r` - NEMA L5-30R
            * `nema-l5-50r` - NEMA L5-50R
            * `nema-l6-15r` - NEMA L6-15R
            * `nema-l6-20r` - NEMA L6-20R
            * `nema-l6-30r` - NEMA L6-30R
            * `nema-l6-50r` - NEMA L6-50R
            * `nema-l10-30r` - NEMA L10-30R
            * `nema-l14-20r` - NEMA L14-20R
            * `nema-l14-30r` - NEMA L14-30R
            * `nema-l14-50r` - NEMA L14-50R
            * `nema-l14-60r` - NEMA L14-60R
            * `nema-l15-20r` - NEMA L15-20R
            * `nema-l15-30r` - NEMA L15-30R
            * `nema-l15-50r` - NEMA L15-50R
            * `nema-l15-60r` - NEMA L15-60R
            * `nema-l21-20r` - NEMA L21-20R
            * `nema-l21-30r` - NEMA L21-30R
            * `nema-l22-20r` - NEMA L22-20R
            * `nema-l22-30r` - NEMA L22-30R
            * `CS6360C` - CS6360C
            * `CS6364C` - CS6364C
            * `CS8164C` - CS8164C
            * `CS8264C` - CS8264C
            * `CS8364C` - CS8364C
            * `CS8464C` - CS8464C
            * `ita-e` - ITA Type E (CEE 7/5)
            * `ita-f` - ITA Type F (CEE 7/3)
            * `ita-g` - ITA Type G (BS 1363)
            * `ita-h` - ITA Type H
            * `ita-i` - ITA Type I
            * `ita-j` - ITA Type J
            * `ita-k` - ITA Type K
            * `ita-l` - ITA Type L (CEI 23-50)
            * `ita-m` - ITA Type M (BS 546)
            * `ita-n` - ITA Type N
            * `ita-o` - ITA Type O
            * `ita-multistandard` - ITA Multistandard
            * `usb-a` - USB Type A
            * `usb-micro-b` - USB Micro B
            * `usb-c` - USB Type C
            * `molex-micro-fit-1x2` - Molex Micro-Fit 1x2
            * `molex-micro-fit-2x2` - Molex Micro-Fit 2x2
            * `molex-micro-fit-2x4` - Molex Micro-Fit 2x4
            * `dc-terminal` - DC Terminal
            * `eaton-c39` - Eaton C39
            * `hdot-cx` - HDOT Cx
            * `saf-d-grid` - Saf-D-Grid
            * `neutrik-powercon-20a` - Neutrik powerCON (20A)
            * `neutrik-powercon-32a` - Neutrik powerCON (32A)
            * `neutrik-powercon-true1` - Neutrik powerCON TRUE1
            * `neutrik-powercon-true1-top` - Neutrik powerCON TRUE1 TOP
            * `ubiquiti-smartpower` - Ubiquiti SmartPower
            * `hardwired` - Hardwired
            * `other` - Other
        status (Union[Unset, PowerOutletRequestStatus]): * `enabled` - Enabled
            * `disabled` - Disabled
            * `faulty` - Faulty
        color (Union[Unset, str]):
        power_port (Union['BriefPowerPortRequest', None, Unset, int]):
        feed_leg (Union[None, PowerOutletRequestFeedLegType1, PowerOutletRequestFeedLegType2Type1,
            PowerOutletRequestFeedLegType3Type1, Unset]): * `A` - A
            * `B` - B
            * `C` - C
        description (Union[Unset, str]):
        mark_connected (Union[Unset, bool]): Treat as if a cable is connected
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PowerOutletRequestCustomFields]):
    """

    device: Union["BriefDeviceRequest", int]
    name: str
    module: Union["BriefModuleRequest", None, Unset, int] = UNSET
    label: Union[Unset, str] = UNSET
    type_: Union[
        None, PowerOutletRequestTypeType1, PowerOutletRequestTypeType2Type1, PowerOutletRequestTypeType3Type1, Unset
    ] = UNSET
    status: Union[Unset, PowerOutletRequestStatus] = UNSET
    color: Union[Unset, str] = UNSET
    power_port: Union["BriefPowerPortRequest", None, Unset, int] = UNSET
    feed_leg: Union[
        None,
        PowerOutletRequestFeedLegType1,
        PowerOutletRequestFeedLegType2Type1,
        PowerOutletRequestFeedLegType3Type1,
        Unset,
    ] = UNSET
    description: Union[Unset, str] = UNSET
    mark_connected: Union[Unset, bool] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PowerOutletRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device_request import BriefDeviceRequest
        from ..models.brief_module_request import BriefModuleRequest
        from ..models.brief_power_port_request import BriefPowerPortRequest

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

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, PowerOutletRequestTypeType1):
            type_ = self.type_.value
        elif isinstance(self.type_, PowerOutletRequestTypeType2Type1):
            type_ = self.type_.value
        elif isinstance(self.type_, PowerOutletRequestTypeType3Type1):
            type_ = self.type_.value
        else:
            type_ = self.type_

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        color = self.color

        power_port: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.power_port, Unset):
            power_port = UNSET
        elif isinstance(self.power_port, BriefPowerPortRequest):
            power_port = self.power_port.to_dict()
        else:
            power_port = self.power_port

        feed_leg: Union[None, Unset, str]
        if isinstance(self.feed_leg, Unset):
            feed_leg = UNSET
        elif isinstance(self.feed_leg, PowerOutletRequestFeedLegType1):
            feed_leg = self.feed_leg.value
        elif isinstance(self.feed_leg, PowerOutletRequestFeedLegType2Type1):
            feed_leg = self.feed_leg.value
        elif isinstance(self.feed_leg, PowerOutletRequestFeedLegType3Type1):
            feed_leg = self.feed_leg.value
        else:
            feed_leg = self.feed_leg

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
        if status is not UNSET:
            field_dict["status"] = status
        if color is not UNSET:
            field_dict["color"] = color
        if power_port is not UNSET:
            field_dict["power_port"] = power_port
        if feed_leg is not UNSET:
            field_dict["feed_leg"] = feed_leg
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
        from ..models.brief_power_port_request import BriefPowerPortRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.power_outlet_request_custom_fields import PowerOutletRequestCustomFields

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

        label = d.pop("label", UNSET)

        def _parse_type_(
            data: object,
        ) -> Union[
            None, PowerOutletRequestTypeType1, PowerOutletRequestTypeType2Type1, PowerOutletRequestTypeType3Type1, Unset
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = PowerOutletRequestTypeType1(data)

                return type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_2_type_1 = PowerOutletRequestTypeType2Type1(data)

                return type_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_3_type_1 = PowerOutletRequestTypeType3Type1(data)

                return type_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PowerOutletRequestTypeType1,
                    PowerOutletRequestTypeType2Type1,
                    PowerOutletRequestTypeType3Type1,
                    Unset,
                ],
                data,
            )

        type_ = _parse_type_(d.pop("type", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, PowerOutletRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PowerOutletRequestStatus(_status)

        color = d.pop("color", UNSET)

        def _parse_power_port(data: object) -> Union["BriefPowerPortRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                power_port_type_1_type_1 = BriefPowerPortRequest.from_dict(data)

                return power_port_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefPowerPortRequest", None, Unset, int], data)

        power_port = _parse_power_port(d.pop("power_port", UNSET))

        def _parse_feed_leg(
            data: object,
        ) -> Union[
            None,
            PowerOutletRequestFeedLegType1,
            PowerOutletRequestFeedLegType2Type1,
            PowerOutletRequestFeedLegType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                feed_leg_type_1 = PowerOutletRequestFeedLegType1(data)

                return feed_leg_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                feed_leg_type_2_type_1 = PowerOutletRequestFeedLegType2Type1(data)

                return feed_leg_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                feed_leg_type_3_type_1 = PowerOutletRequestFeedLegType3Type1(data)

                return feed_leg_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PowerOutletRequestFeedLegType1,
                    PowerOutletRequestFeedLegType2Type1,
                    PowerOutletRequestFeedLegType3Type1,
                    Unset,
                ],
                data,
            )

        feed_leg = _parse_feed_leg(d.pop("feed_leg", UNSET))

        description = d.pop("description", UNSET)

        mark_connected = d.pop("mark_connected", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PowerOutletRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PowerOutletRequestCustomFields.from_dict(_custom_fields)

        power_outlet_request = cls(
            device=device,
            name=name,
            module=module,
            label=label,
            type_=type_,
            status=status,
            color=color,
            power_port=power_port,
            feed_leg=feed_leg,
            description=description,
            mark_connected=mark_connected,
            tags=tags,
            custom_fields=custom_fields,
        )

        power_outlet_request.additional_properties = d
        return power_outlet_request

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
