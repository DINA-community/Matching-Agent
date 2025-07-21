from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.power_port_template_request_type_type_1 import (
    PowerPortTemplateRequestTypeType1,
)
from ..models.power_port_template_request_type_type_2_type_1 import (
    PowerPortTemplateRequestTypeType2Type1,
)
from ..models.power_port_template_request_type_type_3_type_1 import (
    PowerPortTemplateRequestTypeType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_type_request import BriefDeviceTypeRequest
    from ..models.brief_module_type_request import BriefModuleTypeRequest


T = TypeVar("T", bound="PowerPortTemplateRequest")


@_attrs_define
class PowerPortTemplateRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            name (str): {module} is accepted as a substitution for the module bay position when attached to a module type.
            device_type (Union['BriefDeviceTypeRequest', None, Unset, int]):
            module_type (Union['BriefModuleTypeRequest', None, Unset, int]):
            label (Union[Unset, str]): Physical label
            type_ (Union[None, PowerPortTemplateRequestTypeType1, PowerPortTemplateRequestTypeType2Type1,
                PowerPortTemplateRequestTypeType3Type1, Unset]): * `iec-60320-c6` - C6
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
    """

    name: str
    device_type: Union["BriefDeviceTypeRequest", None, Unset, int] = UNSET
    module_type: Union["BriefModuleTypeRequest", None, Unset, int] = UNSET
    label: Union[Unset, str] = UNSET
    type_: Union[
        None,
        PowerPortTemplateRequestTypeType1,
        PowerPortTemplateRequestTypeType2Type1,
        PowerPortTemplateRequestTypeType3Type1,
        Unset,
    ] = UNSET
    maximum_draw: Union[None, Unset, int] = UNSET
    allocated_draw: Union[None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device_type_request import BriefDeviceTypeRequest
        from ..models.brief_module_type_request import BriefModuleTypeRequest

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
        elif isinstance(self.type_, PowerPortTemplateRequestTypeType1):
            type_ = self.type_.value
        elif isinstance(self.type_, PowerPortTemplateRequestTypeType2Type1):
            type_ = self.type_.value
        elif isinstance(self.type_, PowerPortTemplateRequestTypeType3Type1):
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
        if maximum_draw is not UNSET:
            field_dict["maximum_draw"] = maximum_draw
        if allocated_draw is not UNSET:
            field_dict["allocated_draw"] = allocated_draw
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_device_type_request import BriefDeviceTypeRequest
        from ..models.brief_module_type_request import BriefModuleTypeRequest

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
            PowerPortTemplateRequestTypeType1,
            PowerPortTemplateRequestTypeType2Type1,
            PowerPortTemplateRequestTypeType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = PowerPortTemplateRequestTypeType1(data)

                return type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_2_type_1 = PowerPortTemplateRequestTypeType2Type1(data)

                return type_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_3_type_1 = PowerPortTemplateRequestTypeType3Type1(data)

                return type_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PowerPortTemplateRequestTypeType1,
                    PowerPortTemplateRequestTypeType2Type1,
                    PowerPortTemplateRequestTypeType3Type1,
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

        power_port_template_request = cls(
            name=name,
            device_type=device_type,
            module_type=module_type,
            label=label,
            type_=type_,
            maximum_draw=maximum_draw,
            allocated_draw=allocated_draw,
            description=description,
        )

        power_port_template_request.additional_properties = d
        return power_port_template_request

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
