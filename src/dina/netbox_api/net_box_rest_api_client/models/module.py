import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device import BriefDevice
    from ..models.brief_module_type import BriefModuleType
    from ..models.module_custom_fields import ModuleCustomFields
    from ..models.module_status import ModuleStatus
    from ..models.nested_module_bay import NestedModuleBay
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="Module")


@_attrs_define
class Module:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        device (BriefDevice): Adds support for custom fields and tags.
        module_bay (NestedModuleBay): Represents an object related through a ForeignKey field. On write, it accepts a
            primary key (PK) value or a
            dictionary of attributes which can be used to uniquely identify the related object. This class should be
            subclassed to return a full representation of the related object on read.
        module_type (BriefModuleType): Adds support for custom fields and tags.
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        status (Union[Unset, ModuleStatus]):
        serial (Union[Unset, str]):
        asset_tag (Union[None, Unset, str]): A unique tag used to identify this device
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, ModuleCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    device: "BriefDevice"
    module_bay: "NestedModuleBay"
    module_type: "BriefModuleType"
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    status: Union[Unset, "ModuleStatus"] = UNSET
    serial: Union[Unset, str] = UNSET
    asset_tag: Union[None, Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "ModuleCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        device = self.device.to_dict()

        module_bay = self.module_bay.to_dict()

        module_type = self.module_type.to_dict()

        created: Union[None, str]
        if isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        last_updated: Union[None, str]
        if isinstance(self.last_updated, datetime.datetime):
            last_updated = self.last_updated.isoformat()
        else:
            last_updated = self.last_updated

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

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
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "device": device,
                "module_bay": module_bay,
                "module_type": module_type,
                "created": created,
                "last_updated": last_updated,
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
        from ..models.brief_device import BriefDevice
        from ..models.brief_module_type import BriefModuleType
        from ..models.module_custom_fields import ModuleCustomFields
        from ..models.module_status import ModuleStatus
        from ..models.nested_module_bay import NestedModuleBay
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        device = BriefDevice.from_dict(d.pop("device"))

        module_bay = NestedModuleBay.from_dict(d.pop("module_bay"))

        module_type = BriefModuleType.from_dict(d.pop("module_type"))

        def _parse_created(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = isoparse(data)

                return created_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        created = _parse_created(d.pop("created"))

        def _parse_last_updated(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_type_0 = isoparse(data)

                return last_updated_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_updated = _parse_last_updated(d.pop("last_updated"))

        _status = d.pop("status", UNSET)
        status: Union[Unset, ModuleStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ModuleStatus.from_dict(_status)

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
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, ModuleCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ModuleCustomFields.from_dict(_custom_fields)

        module = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            device=device,
            module_bay=module_bay,
            module_type=module_type,
            created=created,
            last_updated=last_updated,
            status=status,
            serial=serial,
            asset_tag=asset_tag,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        module.additional_properties = d
        return module

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
