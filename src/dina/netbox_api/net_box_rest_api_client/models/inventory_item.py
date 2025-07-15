import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device import BriefDevice
    from ..models.brief_inventory_item_role import BriefInventoryItemRole
    from ..models.brief_manufacturer import BriefManufacturer
    from ..models.inventory_item_custom_fields import InventoryItemCustomFields
    from ..models.inventory_item_status import InventoryItemStatus
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="InventoryItem")


@_attrs_define
class InventoryItem:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        device (BriefDevice): Adds support for custom fields and tags.
        name (str):
        component (Any):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        field_depth (int):
        parent (Union[None, Unset, int]):
        label (Union[Unset, str]): Physical label
        status (Union[Unset, InventoryItemStatus]):
        role (Union['BriefInventoryItemRole', None, Unset]):
        manufacturer (Union['BriefManufacturer', None, Unset]):
        part_id (Union[Unset, str]): Manufacturer-assigned part identifier
        serial (Union[Unset, str]):
        asset_tag (Union[None, Unset, str]): A unique tag used to identify this item
        discovered (Union[Unset, bool]): This item was automatically discovered
        description (Union[Unset, str]):
        component_type (Union[None, Unset, str]):
        component_id (Union[None, Unset, int]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, InventoryItemCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    device: "BriefDevice"
    name: str
    component: Any
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    field_depth: int
    parent: Union[None, Unset, int] = UNSET
    label: Union[Unset, str] = UNSET
    status: Union[Unset, "InventoryItemStatus"] = UNSET
    role: Union["BriefInventoryItemRole", None, Unset] = UNSET
    manufacturer: Union["BriefManufacturer", None, Unset] = UNSET
    part_id: Union[Unset, str] = UNSET
    serial: Union[Unset, str] = UNSET
    asset_tag: Union[None, Unset, str] = UNSET
    discovered: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    component_type: Union[None, Unset, str] = UNSET
    component_id: Union[None, Unset, int] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "InventoryItemCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_inventory_item_role import BriefInventoryItemRole
        from ..models.brief_manufacturer import BriefManufacturer

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        device = self.device.to_dict()

        name = self.name

        component = self.component

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

        field_depth = self.field_depth

        parent: Union[None, Unset, int]
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        label = self.label

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        role: Union[None, Unset, dict[str, Any]]
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, BriefInventoryItemRole):
            role = self.role.to_dict()
        else:
            role = self.role

        manufacturer: Union[None, Unset, dict[str, Any]]
        if isinstance(self.manufacturer, Unset):
            manufacturer = UNSET
        elif isinstance(self.manufacturer, BriefManufacturer):
            manufacturer = self.manufacturer.to_dict()
        else:
            manufacturer = self.manufacturer

        part_id = self.part_id

        serial = self.serial

        asset_tag: Union[None, Unset, str]
        if isinstance(self.asset_tag, Unset):
            asset_tag = UNSET
        else:
            asset_tag = self.asset_tag

        discovered = self.discovered

        description = self.description

        component_type: Union[None, Unset, str]
        if isinstance(self.component_type, Unset):
            component_type = UNSET
        else:
            component_type = self.component_type

        component_id: Union[None, Unset, int]
        if isinstance(self.component_id, Unset):
            component_id = UNSET
        else:
            component_id = self.component_id

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
                "component": component,
                "created": created,
                "last_updated": last_updated,
                "_depth": field_depth,
            }
        )
        if parent is not UNSET:
            field_dict["parent"] = parent
        if label is not UNSET:
            field_dict["label"] = label
        if status is not UNSET:
            field_dict["status"] = status
        if role is not UNSET:
            field_dict["role"] = role
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if part_id is not UNSET:
            field_dict["part_id"] = part_id
        if serial is not UNSET:
            field_dict["serial"] = serial
        if asset_tag is not UNSET:
            field_dict["asset_tag"] = asset_tag
        if discovered is not UNSET:
            field_dict["discovered"] = discovered
        if description is not UNSET:
            field_dict["description"] = description
        if component_type is not UNSET:
            field_dict["component_type"] = component_type
        if component_id is not UNSET:
            field_dict["component_id"] = component_id
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_device import BriefDevice
        from ..models.brief_inventory_item_role import BriefInventoryItemRole
        from ..models.brief_manufacturer import BriefManufacturer
        from ..models.inventory_item_custom_fields import InventoryItemCustomFields
        from ..models.inventory_item_status import InventoryItemStatus
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        device = BriefDevice.from_dict(d.pop("device"))

        name = d.pop("name")

        component = d.pop("component")

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

        field_depth = d.pop("_depth")

        def _parse_parent(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent = _parse_parent(d.pop("parent", UNSET))

        label = d.pop("label", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, InventoryItemStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = InventoryItemStatus.from_dict(_status)

        def _parse_role(data: object) -> Union["BriefInventoryItemRole", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                role_type_1 = BriefInventoryItemRole.from_dict(data)

                return role_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefInventoryItemRole", None, Unset], data)

        role = _parse_role(d.pop("role", UNSET))

        def _parse_manufacturer(data: object) -> Union["BriefManufacturer", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                manufacturer_type_1 = BriefManufacturer.from_dict(data)

                return manufacturer_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefManufacturer", None, Unset], data)

        manufacturer = _parse_manufacturer(d.pop("manufacturer", UNSET))

        part_id = d.pop("part_id", UNSET)

        serial = d.pop("serial", UNSET)

        def _parse_asset_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_tag = _parse_asset_tag(d.pop("asset_tag", UNSET))

        discovered = d.pop("discovered", UNSET)

        description = d.pop("description", UNSET)

        def _parse_component_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        component_type = _parse_component_type(d.pop("component_type", UNSET))

        def _parse_component_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        component_id = _parse_component_id(d.pop("component_id", UNSET))

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, InventoryItemCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = InventoryItemCustomFields.from_dict(_custom_fields)

        inventory_item = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            device=device,
            name=name,
            component=component,
            created=created,
            last_updated=last_updated,
            field_depth=field_depth,
            parent=parent,
            label=label,
            status=status,
            role=role,
            manufacturer=manufacturer,
            part_id=part_id,
            serial=serial,
            asset_tag=asset_tag,
            discovered=discovered,
            description=description,
            component_type=component_type,
            component_id=component_id,
            tags=tags,
            custom_fields=custom_fields,
        )

        inventory_item.additional_properties = d
        return inventory_item

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
