import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device import BriefDevice
    from ..models.device_bay_custom_fields import DeviceBayCustomFields
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="DeviceBay")


@_attrs_define
class DeviceBay:
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
        label (Union[Unset, str]): Physical label
        description (Union[Unset, str]):
        installed_device (Union['BriefDevice', None, Unset]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, DeviceBayCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    device: "BriefDevice"
    name: str
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    label: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    installed_device: Union["BriefDevice", None, Unset] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "DeviceBayCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device import BriefDevice

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

        label = self.label

        description = self.description

        installed_device: Union[None, Unset, dict[str, Any]]
        if isinstance(self.installed_device, Unset):
            installed_device = UNSET
        elif isinstance(self.installed_device, BriefDevice):
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
        from ..models.brief_device import BriefDevice
        from ..models.device_bay_custom_fields import DeviceBayCustomFields
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

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        def _parse_installed_device(data: object) -> Union["BriefDevice", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                installed_device_type_1 = BriefDevice.from_dict(data)

                return installed_device_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDevice", None, Unset], data)

        installed_device = _parse_installed_device(d.pop("installed_device", UNSET))

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, DeviceBayCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = DeviceBayCustomFields.from_dict(_custom_fields)

        device_bay = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            device=device,
            name=name,
            created=created,
            last_updated=last_updated,
            label=label,
            description=description,
            installed_device=installed_device,
            tags=tags,
            custom_fields=custom_fields,
        )

        device_bay.additional_properties = d
        return device_bay

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
