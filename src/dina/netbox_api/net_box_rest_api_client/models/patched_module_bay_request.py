import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_request import BriefDeviceRequest
    from ..models.brief_module_request import BriefModuleRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_module_bay_request_custom_fields import PatchedModuleBayRequestCustomFields


T = TypeVar("T", bound="PatchedModuleBayRequest")


@_attrs_define
class PatchedModuleBayRequest:
    """Adds support for custom fields and tags.

    Attributes:
        device (Union['BriefDeviceRequest', Unset, int]):
        module (Union['BriefModuleRequest', None, Unset, int]):
        name (Union[Unset, str]):
        installed_module (Union['BriefModuleRequest', None, Unset, int]):
        label (Union[Unset, str]): Physical label
        position (Union[Unset, str]): Identifier to reference when renaming installed components
        description (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedModuleBayRequestCustomFields]):
    """

    device: Union["BriefDeviceRequest", Unset, int] = UNSET
    module: Union["BriefModuleRequest", None, Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    installed_module: Union["BriefModuleRequest", None, Unset, int] = UNSET
    label: Union[Unset, str] = UNSET
    position: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedModuleBayRequestCustomFields"] = UNSET
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

        installed_module: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.installed_module, Unset):
            installed_module = UNSET
        elif isinstance(self.installed_module, BriefModuleRequest):
            installed_module = self.installed_module.to_dict()
        else:
            installed_module = self.installed_module

        label = self.label

        position = self.position

        description = self.description

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
        if installed_module is not UNSET:
            field_dict["installed_module"] = installed_module
        if label is not UNSET:
            field_dict["label"] = label
        if position is not UNSET:
            field_dict["position"] = position
        if description is not UNSET:
            field_dict["description"] = description
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

        installed_module: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.installed_module, Unset):
            installed_module = UNSET
        elif isinstance(self.installed_module, int):
            installed_module = (None, str(self.installed_module).encode(), "text/plain")
        elif isinstance(self.installed_module, None):
            installed_module = (None, str(self.installed_module).encode(), "text/plain")
        elif isinstance(self.installed_module, BriefModuleRequest):
            installed_module = (None, json.dumps(self.installed_module.to_dict()).encode(), "application/json")
        else:
            installed_module = (None, str(self.installed_module).encode(), "text/plain")

        label = self.label if isinstance(self.label, Unset) else (None, str(self.label).encode(), "text/plain")

        position = (
            self.position if isinstance(self.position, Unset) else (None, str(self.position).encode(), "text/plain")
        )

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
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
        if installed_module is not UNSET:
            field_dict["installed_module"] = installed_module
        if label is not UNSET:
            field_dict["label"] = label
        if position is not UNSET:
            field_dict["position"] = position
        if description is not UNSET:
            field_dict["description"] = description
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
        from ..models.patched_module_bay_request_custom_fields import PatchedModuleBayRequestCustomFields

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

        def _parse_installed_module(data: object) -> Union["BriefModuleRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                installed_module_type_1_type_1 = BriefModuleRequest.from_dict(data)

                return installed_module_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefModuleRequest", None, Unset, int], data)

        installed_module = _parse_installed_module(d.pop("installed_module", UNSET))

        label = d.pop("label", UNSET)

        position = d.pop("position", UNSET)

        description = d.pop("description", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedModuleBayRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedModuleBayRequestCustomFields.from_dict(_custom_fields)

        patched_module_bay_request = cls(
            device=device,
            module=module,
            name=name,
            installed_module=installed_module,
            label=label,
            position=position,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_module_bay_request.additional_properties = d
        return patched_module_bay_request

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
