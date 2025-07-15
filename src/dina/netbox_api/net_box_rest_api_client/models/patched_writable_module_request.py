import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_writable_module_request_status import PatchedWritableModuleRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_request import BriefDeviceRequest
    from ..models.brief_module_type_request import BriefModuleTypeRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_writable_module_request_custom_fields import PatchedWritableModuleRequestCustomFields


T = TypeVar("T", bound="PatchedWritableModuleRequest")


@_attrs_define
class PatchedWritableModuleRequest:
    """Adds support for custom fields and tags.

    Attributes:
        device (Union['BriefDeviceRequest', Unset, int]):
        module_bay (Union[Unset, int]):
        module_type (Union['BriefModuleTypeRequest', Unset, int]):
        status (Union[Unset, PatchedWritableModuleRequestStatus]): * `offline` - Offline
            * `active` - Active
            * `planned` - Planned
            * `staged` - Staged
            * `failed` - Failed
            * `decommissioning` - Decommissioning
        serial (Union[Unset, str]):
        asset_tag (Union[None, Unset, str]): A unique tag used to identify this device
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedWritableModuleRequestCustomFields]):
    """

    device: Union["BriefDeviceRequest", Unset, int] = UNSET
    module_bay: Union[Unset, int] = UNSET
    module_type: Union["BriefModuleTypeRequest", Unset, int] = UNSET
    status: Union[Unset, PatchedWritableModuleRequestStatus] = UNSET
    serial: Union[Unset, str] = UNSET
    asset_tag: Union[None, Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedWritableModuleRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device_request import BriefDeviceRequest
        from ..models.brief_module_type_request import BriefModuleTypeRequest

        device: Union[Unset, dict[str, Any], int]
        if isinstance(self.device, Unset):
            device = UNSET
        elif isinstance(self.device, BriefDeviceRequest):
            device = self.device.to_dict()
        else:
            device = self.device

        module_bay = self.module_bay

        module_type: Union[Unset, dict[str, Any], int]
        if isinstance(self.module_type, Unset):
            module_type = UNSET
        elif isinstance(self.module_type, BriefModuleTypeRequest):
            module_type = self.module_type.to_dict()
        else:
            module_type = self.module_type

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        serial = self.serial

        asset_tag: Union[None, Unset, str]
        if isinstance(self.asset_tag, Unset):
            asset_tag = UNSET
        else:
            asset_tag = self.asset_tag

        description = self.description

        comments = self.comments

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
        if module_bay is not UNSET:
            field_dict["module_bay"] = module_bay
        if module_type is not UNSET:
            field_dict["module_type"] = module_type
        if status is not UNSET:
            field_dict["status"] = status
        if serial is not UNSET:
            field_dict["serial"] = serial
        if asset_tag is not UNSET:
            field_dict["asset_tag"] = asset_tag
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
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

        module_bay = (
            self.module_bay
            if isinstance(self.module_bay, Unset)
            else (None, str(self.module_bay).encode(), "text/plain")
        )

        module_type: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.module_type, Unset):
            module_type = UNSET
        elif isinstance(self.module_type, int):
            module_type = (None, str(self.module_type).encode(), "text/plain")
        else:
            module_type = (None, json.dumps(self.module_type.to_dict()).encode(), "application/json")

        status: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

        serial = self.serial if isinstance(self.serial, Unset) else (None, str(self.serial).encode(), "text/plain")

        asset_tag: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.asset_tag, Unset):
            asset_tag = UNSET
        elif isinstance(self.asset_tag, str):
            asset_tag = (None, str(self.asset_tag).encode(), "text/plain")
        else:
            asset_tag = (None, str(self.asset_tag).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        comments = (
            self.comments if isinstance(self.comments, Unset) else (None, str(self.comments).encode(), "text/plain")
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
        if module_bay is not UNSET:
            field_dict["module_bay"] = module_bay
        if module_type is not UNSET:
            field_dict["module_type"] = module_type
        if status is not UNSET:
            field_dict["status"] = status
        if serial is not UNSET:
            field_dict["serial"] = serial
        if asset_tag is not UNSET:
            field_dict["asset_tag"] = asset_tag
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_device_request import BriefDeviceRequest
        from ..models.brief_module_type_request import BriefModuleTypeRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_writable_module_request_custom_fields import PatchedWritableModuleRequestCustomFields

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

        module_bay = d.pop("module_bay", UNSET)

        def _parse_module_type(data: object) -> Union["BriefModuleTypeRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                module_type_type_1 = BriefModuleTypeRequest.from_dict(data)

                return module_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefModuleTypeRequest", Unset, int], data)

        module_type = _parse_module_type(d.pop("module_type", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, PatchedWritableModuleRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PatchedWritableModuleRequestStatus(_status)

        serial = d.pop("serial", UNSET)

        def _parse_asset_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_tag = _parse_asset_tag(d.pop("asset_tag", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedWritableModuleRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedWritableModuleRequestCustomFields.from_dict(_custom_fields)

        patched_writable_module_request = cls(
            device=device,
            module_bay=module_bay,
            module_type=module_type,
            status=status,
            serial=serial,
            asset_tag=asset_tag,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_writable_module_request.additional_properties = d
        return patched_writable_module_request

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
