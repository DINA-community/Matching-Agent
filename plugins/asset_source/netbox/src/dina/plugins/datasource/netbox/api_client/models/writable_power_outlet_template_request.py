import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_power_outlet_template_request_feed_leg_type_1 import (
    WritablePowerOutletTemplateRequestFeedLegType1,
)
from ..models.writable_power_outlet_template_request_feed_leg_type_2_type_1 import (
    WritablePowerOutletTemplateRequestFeedLegType2Type1,
)
from ..models.writable_power_outlet_template_request_feed_leg_type_3_type_1 import (
    WritablePowerOutletTemplateRequestFeedLegType3Type1,
)
from ..models.writable_power_outlet_template_request_type_type_1 import (
    WritablePowerOutletTemplateRequestTypeType1,
)
from ..models.writable_power_outlet_template_request_type_type_2_type_1 import (
    WritablePowerOutletTemplateRequestTypeType2Type1,
)
from ..models.writable_power_outlet_template_request_type_type_3_type_1 import (
    WritablePowerOutletTemplateRequestTypeType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_type_request import BriefDeviceTypeRequest
    from ..models.brief_module_type_request import BriefModuleTypeRequest
    from ..models.brief_power_port_template_request import BriefPowerPortTemplateRequest


T = TypeVar("T", bound="WritablePowerOutletTemplateRequest")


@_attrs_define
class WritablePowerOutletTemplateRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            name (str): {module} is accepted as a substitution for the module bay position when attached to a module type.
            device_type (Union['BriefDeviceTypeRequest', None, Unset, int]):
            module_type (Union['BriefModuleTypeRequest', None, Unset, int]):
            label (Union[Unset, str]): Physical label
            type_ (Union[None, Unset, WritablePowerOutletTemplateRequestTypeType1,
                WritablePowerOutletTemplateRequestTypeType2Type1, WritablePowerOutletTemplateRequestTypeType3Type1]): *
                `iec-60320-c5` - C5
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
            power_port (Union['BriefPowerPortTemplateRequest', None, Unset, int]):
            feed_leg (Union[None, Unset, WritablePowerOutletTemplateRequestFeedLegType1,
                WritablePowerOutletTemplateRequestFeedLegType2Type1, WritablePowerOutletTemplateRequestFeedLegType3Type1]):
                Phase (for three-phase feeds)

                * `A` - A
                * `B` - B
                * `C` - C
            description (Union[Unset, str]):
    """

    name: str
    device_type: Union["BriefDeviceTypeRequest", None, Unset, int] = UNSET
    module_type: Union["BriefModuleTypeRequest", None, Unset, int] = UNSET
    label: Union[Unset, str] = UNSET
    type_: Union[
        None,
        Unset,
        WritablePowerOutletTemplateRequestTypeType1,
        WritablePowerOutletTemplateRequestTypeType2Type1,
        WritablePowerOutletTemplateRequestTypeType3Type1,
    ] = UNSET
    power_port: Union["BriefPowerPortTemplateRequest", None, Unset, int] = UNSET
    feed_leg: Union[
        None,
        Unset,
        WritablePowerOutletTemplateRequestFeedLegType1,
        WritablePowerOutletTemplateRequestFeedLegType2Type1,
        WritablePowerOutletTemplateRequestFeedLegType3Type1,
    ] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device_type_request import BriefDeviceTypeRequest
        from ..models.brief_module_type_request import BriefModuleTypeRequest
        from ..models.brief_power_port_template_request import (
            BriefPowerPortTemplateRequest,
        )

        name = self.name

        device_type: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.device_type, Unset):
            device_type = UNSET
        elif isinstance(self.device_type, BriefDeviceTypeRequest):
            device_type = self.device_type.to_dict()
        else:
            device_type = self.device_type

        module_type: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.module_type, Unset):
            module_type = UNSET
        elif isinstance(self.module_type, BriefModuleTypeRequest):
            module_type = self.module_type.to_dict()
        else:
            module_type = self.module_type

        label = self.label

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, WritablePowerOutletTemplateRequestTypeType1):
            type_ = self.type_.value
        elif isinstance(self.type_, WritablePowerOutletTemplateRequestTypeType2Type1):
            type_ = self.type_.value
        elif isinstance(self.type_, WritablePowerOutletTemplateRequestTypeType3Type1):
            type_ = self.type_.value
        else:
            type_ = self.type_

        power_port: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.power_port, Unset):
            power_port = UNSET
        elif isinstance(self.power_port, BriefPowerPortTemplateRequest):
            power_port = self.power_port.to_dict()
        else:
            power_port = self.power_port

        feed_leg: Union[None, Unset, str]
        if isinstance(self.feed_leg, Unset):
            feed_leg = UNSET
        elif isinstance(self.feed_leg, WritablePowerOutletTemplateRequestFeedLegType1):
            feed_leg = self.feed_leg.value
        elif isinstance(
            self.feed_leg, WritablePowerOutletTemplateRequestFeedLegType2Type1
        ):
            feed_leg = self.feed_leg.value
        elif isinstance(
            self.feed_leg, WritablePowerOutletTemplateRequestFeedLegType3Type1
        ):
            feed_leg = self.feed_leg.value
        else:
            feed_leg = self.feed_leg

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if module_type is not UNSET:
            field_dict["module_type"] = module_type
        if label is not UNSET:
            field_dict["label"] = label
        if type_ is not UNSET:
            field_dict["type"] = type_
        if power_port is not UNSET:
            field_dict["power_port"] = power_port
        if feed_leg is not UNSET:
            field_dict["feed_leg"] = feed_leg
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        device_type: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.device_type, Unset):
            device_type = UNSET
        elif isinstance(self.device_type, int):
            device_type = (None, str(self.device_type).encode(), "text/plain")
        elif isinstance(self.device_type, None):
            device_type = (None, str(self.device_type).encode(), "text/plain")
        elif isinstance(self.device_type, BriefDeviceTypeRequest):
            device_type = (
                None,
                json.dumps(self.device_type.to_dict()).encode(),
                "application/json",
            )
        else:
            device_type = (None, str(self.device_type).encode(), "text/plain")

        module_type: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.module_type, Unset):
            module_type = UNSET
        elif isinstance(self.module_type, int):
            module_type = (None, str(self.module_type).encode(), "text/plain")
        elif isinstance(self.module_type, None):
            module_type = (None, str(self.module_type).encode(), "text/plain")
        elif isinstance(self.module_type, BriefModuleTypeRequest):
            module_type = (
                None,
                json.dumps(self.module_type.to_dict()).encode(),
                "application/json",
            )
        else:
            module_type = (None, str(self.module_type).encode(), "text/plain")

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
        elif isinstance(self.type_, WritablePowerOutletTemplateRequestTypeType1):
            type_ = (None, str(self.type_.value).encode(), "text/plain")
        elif isinstance(self.type_, None):
            type_ = (None, str(self.type_).encode(), "text/plain")
        elif isinstance(self.type_, WritablePowerOutletTemplateRequestTypeType2Type1):
            type_ = (None, str(self.type_.value).encode(), "text/plain")
        elif isinstance(self.type_, None):
            type_ = (None, str(self.type_).encode(), "text/plain")
        else:
            type_ = (None, str(self.type_.value).encode(), "text/plain")

        power_port: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.power_port, Unset):
            power_port = UNSET
        elif isinstance(self.power_port, int):
            power_port = (None, str(self.power_port).encode(), "text/plain")
        elif isinstance(self.power_port, None):
            power_port = (None, str(self.power_port).encode(), "text/plain")
        elif isinstance(self.power_port, BriefPowerPortTemplateRequest):
            power_port = (
                None,
                json.dumps(self.power_port.to_dict()).encode(),
                "application/json",
            )
        else:
            power_port = (None, str(self.power_port).encode(), "text/plain")

        feed_leg: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.feed_leg, Unset):
            feed_leg = UNSET
        elif isinstance(self.feed_leg, None):
            feed_leg = (None, str(self.feed_leg).encode(), "text/plain")
        elif isinstance(self.feed_leg, WritablePowerOutletTemplateRequestFeedLegType1):
            feed_leg = (None, str(self.feed_leg.value).encode(), "text/plain")
        elif isinstance(self.feed_leg, None):
            feed_leg = (None, str(self.feed_leg).encode(), "text/plain")
        elif isinstance(
            self.feed_leg, WritablePowerOutletTemplateRequestFeedLegType2Type1
        ):
            feed_leg = (None, str(self.feed_leg.value).encode(), "text/plain")
        elif isinstance(self.feed_leg, None):
            feed_leg = (None, str(self.feed_leg).encode(), "text/plain")
        else:
            feed_leg = (None, str(self.feed_leg.value).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "name": name,
            }
        )
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if module_type is not UNSET:
            field_dict["module_type"] = module_type
        if label is not UNSET:
            field_dict["label"] = label
        if type_ is not UNSET:
            field_dict["type"] = type_
        if power_port is not UNSET:
            field_dict["power_port"] = power_port
        if feed_leg is not UNSET:
            field_dict["feed_leg"] = feed_leg
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_device_type_request import BriefDeviceTypeRequest
        from ..models.brief_module_type_request import BriefModuleTypeRequest
        from ..models.brief_power_port_template_request import (
            BriefPowerPortTemplateRequest,
        )

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_device_type(
            data: object,
        ) -> Union["BriefDeviceTypeRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_type_type_1_type_1 = BriefDeviceTypeRequest.from_dict(data)

                return device_type_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDeviceTypeRequest", None, Unset, int], data)

        device_type = _parse_device_type(d.pop("device_type", UNSET))

        def _parse_module_type(
            data: object,
        ) -> Union["BriefModuleTypeRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                module_type_type_1_type_1 = BriefModuleTypeRequest.from_dict(data)

                return module_type_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefModuleTypeRequest", None, Unset, int], data)

        module_type = _parse_module_type(d.pop("module_type", UNSET))

        label = d.pop("label", UNSET)

        def _parse_type_(
            data: object,
        ) -> Union[
            None,
            Unset,
            WritablePowerOutletTemplateRequestTypeType1,
            WritablePowerOutletTemplateRequestTypeType2Type1,
            WritablePowerOutletTemplateRequestTypeType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = WritablePowerOutletTemplateRequestTypeType1(data)

                return type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_2_type_1 = WritablePowerOutletTemplateRequestTypeType2Type1(
                    data
                )

                return type_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_3_type_1 = WritablePowerOutletTemplateRequestTypeType3Type1(
                    data
                )

                return type_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    WritablePowerOutletTemplateRequestTypeType1,
                    WritablePowerOutletTemplateRequestTypeType2Type1,
                    WritablePowerOutletTemplateRequestTypeType3Type1,
                ],
                data,
            )

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_power_port(
            data: object,
        ) -> Union["BriefPowerPortTemplateRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                power_port_type_1_type_1 = BriefPowerPortTemplateRequest.from_dict(data)

                return power_port_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefPowerPortTemplateRequest", None, Unset, int], data)

        power_port = _parse_power_port(d.pop("power_port", UNSET))

        def _parse_feed_leg(
            data: object,
        ) -> Union[
            None,
            Unset,
            WritablePowerOutletTemplateRequestFeedLegType1,
            WritablePowerOutletTemplateRequestFeedLegType2Type1,
            WritablePowerOutletTemplateRequestFeedLegType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                feed_leg_type_1 = WritablePowerOutletTemplateRequestFeedLegType1(data)

                return feed_leg_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                feed_leg_type_2_type_1 = (
                    WritablePowerOutletTemplateRequestFeedLegType2Type1(data)
                )

                return feed_leg_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                feed_leg_type_3_type_1 = (
                    WritablePowerOutletTemplateRequestFeedLegType3Type1(data)
                )

                return feed_leg_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    WritablePowerOutletTemplateRequestFeedLegType1,
                    WritablePowerOutletTemplateRequestFeedLegType2Type1,
                    WritablePowerOutletTemplateRequestFeedLegType3Type1,
                ],
                data,
            )

        feed_leg = _parse_feed_leg(d.pop("feed_leg", UNSET))

        description = d.pop("description", UNSET)

        writable_power_outlet_template_request = cls(
            name=name,
            device_type=device_type,
            module_type=module_type,
            label=label,
            type_=type_,
            power_port=power_port,
            feed_leg=feed_leg,
            description=description,
        )

        writable_power_outlet_template_request.additional_properties = d
        return writable_power_outlet_template_request

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
