import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_request import BriefDeviceRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_device_bay_request_custom_fields import (
        PatchedDeviceBayRequestCustomFields,
    )


T = TypeVar("T", bound="PatchedDeviceBayRequest")


@_attrs_define
class PatchedDeviceBayRequest:
    """Adds support for custom fields and tags.

    Attributes:
        device (Union['BriefDeviceRequest', Unset, int]):
        name (Union[Unset, str]):
        label (Union[Unset, str]): Physical label
        description (Union[Unset, str]):
        installed_device (Union['BriefDeviceRequest', None, Unset, int]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedDeviceBayRequestCustomFields]):
    """

    device: Union["BriefDeviceRequest", Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    installed_device: Union["BriefDeviceRequest", None, Unset, int] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedDeviceBayRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device_request import BriefDeviceRequest

        device: Union[Unset, dict[str, Any], int]
        if isinstance(self.device, Unset):
            device = UNSET
        elif isinstance(self.device, BriefDeviceRequest):
            device = self.device.to_dict()
        else:
            device = self.device

        name = self.name

        label = self.label

        description = self.description

        installed_device: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.installed_device, Unset):
            installed_device = UNSET
        elif isinstance(self.installed_device, BriefDeviceRequest):
            installed_device = self.installed_device.to_dict()
        else:
            installed_device = self.installed_device

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
        if name is not UNSET:
            field_dict["name"] = name
        if label is not UNSET:
            field_dict["label"] = label
        if description is not UNSET:
            field_dict["description"] = description
        if installed_device is not UNSET:
            field_dict["installed_device"] = installed_device
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

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        installed_device: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.installed_device, Unset):
            installed_device = UNSET
        elif isinstance(self.installed_device, int):
            installed_device = (None, str(self.installed_device).encode(), "text/plain")
        elif isinstance(self.installed_device, None):
            installed_device = (None, str(self.installed_device).encode(), "text/plain")
        elif isinstance(self.installed_device, BriefDeviceRequest):
            installed_device = (
                None,
                json.dumps(self.installed_device.to_dict()).encode(),
                "application/json",
            )
        else:
            installed_device = (None, str(self.installed_device).encode(), "text/plain")

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
        if name is not UNSET:
            field_dict["name"] = name
        if label is not UNSET:
            field_dict["label"] = label
        if description is not UNSET:
            field_dict["description"] = description
        if installed_device is not UNSET:
            field_dict["installed_device"] = installed_device
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_device_request import BriefDeviceRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_device_bay_request_custom_fields import (
            PatchedDeviceBayRequestCustomFields,
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

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        def _parse_installed_device(
            data: object,
        ) -> Union["BriefDeviceRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                installed_device_type_1_type_1 = BriefDeviceRequest.from_dict(data)

                return installed_device_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDeviceRequest", None, Unset, int], data)

        installed_device = _parse_installed_device(d.pop("installed_device", UNSET))

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedDeviceBayRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedDeviceBayRequestCustomFields.from_dict(
                _custom_fields
            )

        patched_device_bay_request = cls(
            device=device,
            name=name,
            label=label,
            description=description,
            installed_device=installed_device,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_device_bay_request.additional_properties = d
        return patched_device_bay_request

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
