import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_writable_console_server_port_template_request_type_type_1 import (
    PatchedWritableConsoleServerPortTemplateRequestTypeType1,
)
from ..models.patched_writable_console_server_port_template_request_type_type_2_type_1 import (
    PatchedWritableConsoleServerPortTemplateRequestTypeType2Type1,
)
from ..models.patched_writable_console_server_port_template_request_type_type_3_type_1 import (
    PatchedWritableConsoleServerPortTemplateRequestTypeType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_type_request import BriefDeviceTypeRequest
    from ..models.brief_module_type_request import BriefModuleTypeRequest


T = TypeVar("T", bound="PatchedWritableConsoleServerPortTemplateRequest")


@_attrs_define
class PatchedWritableConsoleServerPortTemplateRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            device_type (Union['BriefDeviceTypeRequest', None, Unset, int]):
            module_type (Union['BriefModuleTypeRequest', None, Unset, int]):
            name (Union[Unset, str]): {module} is accepted as a substitution for the module bay position when attached to a
                module type.
            label (Union[Unset, str]): Physical label
            type_ (Union[None, PatchedWritableConsoleServerPortTemplateRequestTypeType1,
                PatchedWritableConsoleServerPortTemplateRequestTypeType2Type1,
                PatchedWritableConsoleServerPortTemplateRequestTypeType3Type1, Unset]): * `de-9` - DE-9
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
            description (Union[Unset, str]):
    """

    device_type: Union["BriefDeviceTypeRequest", None, Unset, int] = UNSET
    module_type: Union["BriefModuleTypeRequest", None, Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    type_: Union[
        None,
        PatchedWritableConsoleServerPortTemplateRequestTypeType1,
        PatchedWritableConsoleServerPortTemplateRequestTypeType2Type1,
        PatchedWritableConsoleServerPortTemplateRequestTypeType3Type1,
        Unset,
    ] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device_type_request import BriefDeviceTypeRequest
        from ..models.brief_module_type_request import BriefModuleTypeRequest

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

        name = self.name

        label = self.label

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, PatchedWritableConsoleServerPortTemplateRequestTypeType1):
            type_ = self.type_.value
        elif isinstance(self.type_, PatchedWritableConsoleServerPortTemplateRequestTypeType2Type1):
            type_ = self.type_.value
        elif isinstance(self.type_, PatchedWritableConsoleServerPortTemplateRequestTypeType3Type1):
            type_ = self.type_.value
        else:
            type_ = self.type_

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if module_type is not UNSET:
            field_dict["module_type"] = module_type
        if name is not UNSET:
            field_dict["name"] = name
        if label is not UNSET:
            field_dict["label"] = label
        if type_ is not UNSET:
            field_dict["type"] = type_
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        device_type: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.device_type, Unset):
            device_type = UNSET
        elif isinstance(self.device_type, int):
            device_type = (None, str(self.device_type).encode(), "text/plain")
        elif isinstance(self.device_type, None):
            device_type = (None, str(self.device_type).encode(), "text/plain")
        elif isinstance(self.device_type, BriefDeviceTypeRequest):
            device_type = (None, json.dumps(self.device_type.to_dict()).encode(), "application/json")
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
            module_type = (None, json.dumps(self.module_type.to_dict()).encode(), "application/json")
        else:
            module_type = (None, str(self.module_type).encode(), "text/plain")

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        label = self.label if isinstance(self.label, Unset) else (None, str(self.label).encode(), "text/plain")

        type_: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, None):
            type_ = (None, str(self.type_).encode(), "text/plain")
        elif isinstance(self.type_, PatchedWritableConsoleServerPortTemplateRequestTypeType1):
            type_ = (None, str(self.type_.value).encode(), "text/plain")
        elif isinstance(self.type_, None):
            type_ = (None, str(self.type_).encode(), "text/plain")
        elif isinstance(self.type_, PatchedWritableConsoleServerPortTemplateRequestTypeType2Type1):
            type_ = (None, str(self.type_.value).encode(), "text/plain")
        elif isinstance(self.type_, None):
            type_ = (None, str(self.type_).encode(), "text/plain")
        else:
            type_ = (None, str(self.type_.value).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if module_type is not UNSET:
            field_dict["module_type"] = module_type
        if name is not UNSET:
            field_dict["name"] = name
        if label is not UNSET:
            field_dict["label"] = label
        if type_ is not UNSET:
            field_dict["type"] = type_
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_device_type_request import BriefDeviceTypeRequest
        from ..models.brief_module_type_request import BriefModuleTypeRequest

        d = dict(src_dict)

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

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        def _parse_type_(
            data: object,
        ) -> Union[
            None,
            PatchedWritableConsoleServerPortTemplateRequestTypeType1,
            PatchedWritableConsoleServerPortTemplateRequestTypeType2Type1,
            PatchedWritableConsoleServerPortTemplateRequestTypeType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = PatchedWritableConsoleServerPortTemplateRequestTypeType1(data)

                return type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_2_type_1 = PatchedWritableConsoleServerPortTemplateRequestTypeType2Type1(data)

                return type_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_3_type_1 = PatchedWritableConsoleServerPortTemplateRequestTypeType3Type1(data)

                return type_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PatchedWritableConsoleServerPortTemplateRequestTypeType1,
                    PatchedWritableConsoleServerPortTemplateRequestTypeType2Type1,
                    PatchedWritableConsoleServerPortTemplateRequestTypeType3Type1,
                    Unset,
                ],
                data,
            )

        type_ = _parse_type_(d.pop("type", UNSET))

        description = d.pop("description", UNSET)

        patched_writable_console_server_port_template_request = cls(
            device_type=device_type,
            module_type=module_type,
            name=name,
            label=label,
            type_=type_,
            description=description,
        )

        patched_writable_console_server_port_template_request.additional_properties = d
        return patched_writable_console_server_port_template_request

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
