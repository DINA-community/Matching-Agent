from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.module_request_status import ModuleRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_request import BriefDeviceRequest
    from ..models.brief_module_type_request import BriefModuleTypeRequest
    from ..models.module_request_custom_fields import ModuleRequestCustomFields
    from ..models.nested_module_bay_request import NestedModuleBayRequest
    from ..models.nested_tag_request import NestedTagRequest


T = TypeVar("T", bound="ModuleRequest")


@_attrs_define
class ModuleRequest:
    """Adds support for custom fields and tags.

    Attributes:
        device (Union['BriefDeviceRequest', int]):
        module_bay (NestedModuleBayRequest): Represents an object related through a ForeignKey field. On write, it
            accepts a primary key (PK) value or a
            dictionary of attributes which can be used to uniquely identify the related object. This class should be
            subclassed to return a full representation of the related object on read.
        module_type (Union['BriefModuleTypeRequest', int]):
        status (Union[Unset, ModuleRequestStatus]): * `offline` - Offline
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
        custom_fields (Union[Unset, ModuleRequestCustomFields]):
    """

    device: Union["BriefDeviceRequest", int]
    module_bay: "NestedModuleBayRequest"
    module_type: Union["BriefModuleTypeRequest", int]
    status: Union[Unset, ModuleRequestStatus] = UNSET
    serial: Union[Unset, str] = UNSET
    asset_tag: Union[None, Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "ModuleRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device_request import BriefDeviceRequest
        from ..models.brief_module_type_request import BriefModuleTypeRequest

        device: Union[dict[str, Any], int]
        if isinstance(self.device, BriefDeviceRequest):
            device = self.device.to_dict()
        else:
            device = self.device

        module_bay = self.module_bay.to_dict()

        module_type: Union[dict[str, Any], int]
        if isinstance(self.module_type, BriefModuleTypeRequest):
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
        field_dict.update(
            {
                "device": device,
                "module_bay": module_bay,
                "module_type": module_type,
            }
        )
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
        from ..models.module_request_custom_fields import ModuleRequestCustomFields
        from ..models.nested_module_bay_request import NestedModuleBayRequest
        from ..models.nested_tag_request import NestedTagRequest

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

        module_bay = NestedModuleBayRequest.from_dict(d.pop("module_bay"))

        def _parse_module_type(data: object) -> Union["BriefModuleTypeRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                module_type_type_1 = BriefModuleTypeRequest.from_dict(data)

                return module_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefModuleTypeRequest", int], data)

        module_type = _parse_module_type(d.pop("module_type"))

        _status = d.pop("status", UNSET)
        status: Union[Unset, ModuleRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ModuleRequestStatus(_status)

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
        custom_fields: Union[Unset, ModuleRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ModuleRequestCustomFields.from_dict(_custom_fields)

        module_request = cls(
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

        module_request.additional_properties = d
        return module_request

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
