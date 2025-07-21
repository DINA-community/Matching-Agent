import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device import BriefDevice
    from ..models.brief_module import BriefModule
    from ..models.module_bay_custom_fields import ModuleBayCustomFields
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="ModuleBay")


@_attrs_define
class ModuleBay:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        device (BriefDevice): Adds support for custom fields and tags.
        name (str):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        module (Union['BriefModule', None, Unset]):
        installed_module (Union['BriefModule', None, Unset]):
        label (Union[Unset, str]): Physical label
        position (Union[Unset, str]): Identifier to reference when renaming installed components
        description (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, ModuleBayCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    device: "BriefDevice"
    name: str
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    module: Union["BriefModule", None, Unset] = UNSET
    installed_module: Union["BriefModule", None, Unset] = UNSET
    label: Union[Unset, str] = UNSET
    position: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "ModuleBayCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_module import BriefModule

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        device = self.device.to_dict()

        name = self.name

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

        module: Union[None, Unset, dict[str, Any]]
        if isinstance(self.module, Unset):
            module = UNSET
        elif isinstance(self.module, BriefModule):
            module = self.module.to_dict()
        else:
            module = self.module

        installed_module: Union[None, Unset, dict[str, Any]]
        if isinstance(self.installed_module, Unset):
            installed_module = UNSET
        elif isinstance(self.installed_module, BriefModule):
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
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "device": device,
                "name": name,
                "created": created,
                "last_updated": last_updated,
            }
        )
        if module is not UNSET:
            field_dict["module"] = module
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
        from ..models.brief_device import BriefDevice
        from ..models.brief_module import BriefModule
        from ..models.module_bay_custom_fields import ModuleBayCustomFields
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        device = BriefDevice.from_dict(d.pop("device"))

        name = d.pop("name")

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

        def _parse_module(data: object) -> Union["BriefModule", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                module_type_1 = BriefModule.from_dict(data)

                return module_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefModule", None, Unset], data)

        module = _parse_module(d.pop("module", UNSET))

        def _parse_installed_module(data: object) -> Union["BriefModule", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                installed_module_type_1 = BriefModule.from_dict(data)

                return installed_module_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefModule", None, Unset], data)

        installed_module = _parse_installed_module(d.pop("installed_module", UNSET))

        label = d.pop("label", UNSET)

        position = d.pop("position", UNSET)

        description = d.pop("description", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, ModuleBayCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ModuleBayCustomFields.from_dict(_custom_fields)

        module_bay = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            device=device,
            name=name,
            created=created,
            last_updated=last_updated,
            module=module,
            installed_module=installed_module,
            label=label,
            position=position,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )

        module_bay.additional_properties = d
        return module_bay

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
