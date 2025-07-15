import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_type_request import BriefDeviceTypeRequest
    from ..models.brief_inventory_item_role_request import BriefInventoryItemRoleRequest
    from ..models.brief_manufacturer_request import BriefManufacturerRequest


T = TypeVar("T", bound="InventoryItemTemplateRequest")


@_attrs_define
class InventoryItemTemplateRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            device_type (Union['BriefDeviceTypeRequest', int]):
            name (str): {module} is accepted as a substitution for the module bay position when attached to a module type.
            parent (Union[None, Unset, int]):
            label (Union[Unset, str]): Physical label
            role (Union['BriefInventoryItemRoleRequest', None, Unset, int]):
            manufacturer (Union['BriefManufacturerRequest', None, Unset, int]):
            part_id (Union[Unset, str]): Manufacturer-assigned part identifier
            description (Union[Unset, str]):
            component_type (Union[None, Unset, str]):
            component_id (Union[None, Unset, int]):
    """

    device_type: Union["BriefDeviceTypeRequest", int]
    name: str
    parent: Union[None, Unset, int] = UNSET
    label: Union[Unset, str] = UNSET
    role: Union["BriefInventoryItemRoleRequest", None, Unset, int] = UNSET
    manufacturer: Union["BriefManufacturerRequest", None, Unset, int] = UNSET
    part_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    component_type: Union[None, Unset, str] = UNSET
    component_id: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device_type_request import BriefDeviceTypeRequest
        from ..models.brief_inventory_item_role_request import BriefInventoryItemRoleRequest
        from ..models.brief_manufacturer_request import BriefManufacturerRequest

        device_type: Union[dict[str, Any], int]
        if isinstance(self.device_type, BriefDeviceTypeRequest):
            device_type = self.device_type.to_dict()
        else:
            device_type = self.device_type

        name = self.name

        parent: Union[None, Unset, int]
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        label = self.label

        role: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, BriefInventoryItemRoleRequest):
            role = self.role.to_dict()
        else:
            role = self.role

        manufacturer: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.manufacturer, Unset):
            manufacturer = UNSET
        elif isinstance(self.manufacturer, BriefManufacturerRequest):
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
                "device_type": device_type,
                "name": name,
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

    def to_multipart(self) -> dict[str, Any]:
        device_type: tuple[None, bytes, str]

        if isinstance(self.device_type, int):
            device_type = (None, str(self.device_type).encode(), "text/plain")
        else:
            device_type = (None, json.dumps(self.device_type.to_dict()).encode(), "application/json")

        name = (None, str(self.name).encode(), "text/plain")

        parent: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, int):
            parent = (None, str(self.parent).encode(), "text/plain")
        else:
            parent = (None, str(self.parent).encode(), "text/plain")

        label = self.label if isinstance(self.label, Unset) else (None, str(self.label).encode(), "text/plain")

        role: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, int):
            role = (None, str(self.role).encode(), "text/plain")
        elif isinstance(self.role, None):
            role = (None, str(self.role).encode(), "text/plain")
        elif isinstance(self.role, BriefInventoryItemRoleRequest):
            role = (None, json.dumps(self.role.to_dict()).encode(), "application/json")
        else:
            role = (None, str(self.role).encode(), "text/plain")

        manufacturer: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.manufacturer, Unset):
            manufacturer = UNSET
        elif isinstance(self.manufacturer, int):
            manufacturer = (None, str(self.manufacturer).encode(), "text/plain")
        elif isinstance(self.manufacturer, None):
            manufacturer = (None, str(self.manufacturer).encode(), "text/plain")
        elif isinstance(self.manufacturer, BriefManufacturerRequest):
            manufacturer = (None, json.dumps(self.manufacturer.to_dict()).encode(), "application/json")
        else:
            manufacturer = (None, str(self.manufacturer).encode(), "text/plain")

        part_id = self.part_id if isinstance(self.part_id, Unset) else (None, str(self.part_id).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        component_type: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.component_type, Unset):
            component_type = UNSET
        elif isinstance(self.component_type, str):
            component_type = (None, str(self.component_type).encode(), "text/plain")
        else:
            component_type = (None, str(self.component_type).encode(), "text/plain")

        component_id: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.component_id, Unset):
            component_id = UNSET
        elif isinstance(self.component_id, int):
            component_id = (None, str(self.component_id).encode(), "text/plain")
        else:
            component_id = (None, str(self.component_id).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "device_type": device_type,
                "name": name,
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
        from ..models.brief_device_type_request import BriefDeviceTypeRequest
        from ..models.brief_inventory_item_role_request import BriefInventoryItemRoleRequest
        from ..models.brief_manufacturer_request import BriefManufacturerRequest

        d = dict(src_dict)

        def _parse_device_type(data: object) -> Union["BriefDeviceTypeRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_type_type_1 = BriefDeviceTypeRequest.from_dict(data)

                return device_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDeviceTypeRequest", int], data)

        device_type = _parse_device_type(d.pop("device_type"))

        name = d.pop("name")

        def _parse_parent(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent = _parse_parent(d.pop("parent", UNSET))

        label = d.pop("label", UNSET)

        def _parse_role(data: object) -> Union["BriefInventoryItemRoleRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                role_type_1_type_1 = BriefInventoryItemRoleRequest.from_dict(data)

                return role_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefInventoryItemRoleRequest", None, Unset, int], data)

        role = _parse_role(d.pop("role", UNSET))

        def _parse_manufacturer(data: object) -> Union["BriefManufacturerRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                manufacturer_type_1_type_1 = BriefManufacturerRequest.from_dict(data)

                return manufacturer_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefManufacturerRequest", None, Unset, int], data)

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

        inventory_item_template_request = cls(
            device_type=device_type,
            name=name,
            parent=parent,
            label=label,
            role=role,
            manufacturer=manufacturer,
            part_id=part_id,
            description=description,
            component_type=component_type,
            component_id=component_id,
        )

        inventory_item_template_request.additional_properties = d
        return inventory_item_template_request

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
