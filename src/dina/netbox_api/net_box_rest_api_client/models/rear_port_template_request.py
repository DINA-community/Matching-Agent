from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rear_port_template_request_type import RearPortTemplateRequestType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_type_request import BriefDeviceTypeRequest
    from ..models.brief_module_type_request import BriefModuleTypeRequest


T = TypeVar("T", bound="RearPortTemplateRequest")


@_attrs_define
class RearPortTemplateRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            name (str): {module} is accepted as a substitution for the module bay position when attached to a module type.
            type_ (RearPortTemplateRequestType): * `8p8c` - 8P8C
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
            device_type (Union['BriefDeviceTypeRequest', None, Unset, int]):
            module_type (Union['BriefModuleTypeRequest', None, Unset, int]):
            label (Union[Unset, str]): Physical label
            color (Union[Unset, str]):
            positions (Union[Unset, int]):
            description (Union[Unset, str]):
    """

    name: str
    type_: RearPortTemplateRequestType
    device_type: Union["BriefDeviceTypeRequest", None, Unset, int] = UNSET
    module_type: Union["BriefModuleTypeRequest", None, Unset, int] = UNSET
    label: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    positions: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device_type_request import BriefDeviceTypeRequest
        from ..models.brief_module_type_request import BriefModuleTypeRequest

        name = self.name

        type_ = self.type_.value

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

        color = self.color

        positions = self.positions

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if module_type is not UNSET:
            field_dict["module_type"] = module_type
        if label is not UNSET:
            field_dict["label"] = label
        if color is not UNSET:
            field_dict["color"] = color
        if positions is not UNSET:
            field_dict["positions"] = positions
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_device_type_request import BriefDeviceTypeRequest
        from ..models.brief_module_type_request import BriefModuleTypeRequest

        d = dict(src_dict)
        name = d.pop("name")

        type_ = RearPortTemplateRequestType(d.pop("type"))

        def _parse_device_type(data: object) -> Union["BriefDeviceTypeRequest", None, Unset, int]:
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

        def _parse_module_type(data: object) -> Union["BriefModuleTypeRequest", None, Unset, int]:
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

        color = d.pop("color", UNSET)

        positions = d.pop("positions", UNSET)

        description = d.pop("description", UNSET)

        rear_port_template_request = cls(
            name=name,
            type_=type_,
            device_type=device_type,
            module_type=module_type,
            label=label,
            color=color,
            positions=positions,
            description=description,
        )

        rear_port_template_request.additional_properties = d
        return rear_port_template_request

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
