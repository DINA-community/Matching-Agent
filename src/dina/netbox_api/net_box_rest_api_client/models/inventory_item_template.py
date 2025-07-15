import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_type import BriefDeviceType
    from ..models.brief_inventory_item_role import BriefInventoryItemRole
    from ..models.brief_manufacturer import BriefManufacturer


T = TypeVar("T", bound="InventoryItemTemplate")


@_attrs_define
class InventoryItemTemplate:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            id (int):
            url (str):
            display (str):
            device_type (BriefDeviceType): Adds support for custom fields and tags.
            name (str): {module} is accepted as a substitution for the module bay position when attached to a module type.
            component (Any):
            created (Union[None, datetime.datetime]):
            last_updated (Union[None, datetime.datetime]):
            field_depth (int):
            parent (Union[None, Unset, int]):
            label (Union[Unset, str]): Physical label
            role (Union['BriefInventoryItemRole', None, Unset]):
            manufacturer (Union['BriefManufacturer', None, Unset]):
            part_id (Union[Unset, str]): Manufacturer-assigned part identifier
            description (Union[Unset, str]):
            component_type (Union[None, Unset, str]):
            component_id (Union[None, Unset, int]):
    """

    id: int
    url: str
    display: str
    device_type: "BriefDeviceType"
    name: str
    component: Any
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    field_depth: int
    parent: Union[None, Unset, int] = UNSET
    label: Union[Unset, str] = UNSET
    role: Union["BriefInventoryItemRole", None, Unset] = UNSET
    manufacturer: Union["BriefManufacturer", None, Unset] = UNSET
    part_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    component_type: Union[None, Unset, str] = UNSET
    component_id: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_inventory_item_role import BriefInventoryItemRole
        from ..models.brief_manufacturer import BriefManufacturer

        id = self.id

        url = self.url

        display = self.display

        device_type = self.device_type.to_dict()

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "device_type": device_type,
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
        if role is not UNSET:
            field_dict["role"] = role
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if part_id is not UNSET:
            field_dict["part_id"] = part_id
        if description is not UNSET:
            field_dict["description"] = description
        if component_type is not UNSET:
            field_dict["component_type"] = component_type
        if component_id is not UNSET:
            field_dict["component_id"] = component_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_device_type import BriefDeviceType
        from ..models.brief_inventory_item_role import BriefInventoryItemRole
        from ..models.brief_manufacturer import BriefManufacturer

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        device_type = BriefDeviceType.from_dict(d.pop("device_type"))

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

        inventory_item_template = cls(
            id=id,
            url=url,
            display=display,
            device_type=device_type,
            name=name,
            component=component,
            created=created,
            last_updated=last_updated,
            field_depth=field_depth,
            parent=parent,
            label=label,
            role=role,
            manufacturer=manufacturer,
            part_id=part_id,
            description=description,
            component_type=component_type,
            component_id=component_id,
        )

        inventory_item_template.additional_properties = d
        return inventory_item_template

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
