import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_writable_inventory_item_request_status import PatchedWritableInventoryItemRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_request import BriefDeviceRequest
    from ..models.brief_inventory_item_role_request import BriefInventoryItemRoleRequest
    from ..models.brief_manufacturer_request import BriefManufacturerRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_writable_inventory_item_request_custom_fields import (
        PatchedWritableInventoryItemRequestCustomFields,
    )


T = TypeVar("T", bound="PatchedWritableInventoryItemRequest")


@_attrs_define
class PatchedWritableInventoryItemRequest:
    """Adds support for custom fields and tags.

    Attributes:
        device (Union['BriefDeviceRequest', Unset, int]):
        parent (Union[None, Unset, int]):
        name (Union[Unset, str]):
        label (Union[Unset, str]): Physical label
        status (Union[Unset, PatchedWritableInventoryItemRequestStatus]): * `offline` - Offline
            * `active` - Active
            * `planned` - Planned
            * `staged` - Staged
            * `failed` - Failed
            * `decommissioning` - Decommissioning
        role (Union['BriefInventoryItemRoleRequest', None, Unset, int]):
        manufacturer (Union['BriefManufacturerRequest', None, Unset, int]):
        part_id (Union[Unset, str]): Manufacturer-assigned part identifier
        serial (Union[Unset, str]):
        asset_tag (Union[None, Unset, str]): A unique tag used to identify this item
        discovered (Union[Unset, bool]): This item was automatically discovered
        description (Union[Unset, str]):
        component_type (Union[None, Unset, str]):
        component_id (Union[None, Unset, int]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedWritableInventoryItemRequestCustomFields]):
    """

    device: Union["BriefDeviceRequest", Unset, int] = UNSET
    parent: Union[None, Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    status: Union[Unset, PatchedWritableInventoryItemRequestStatus] = UNSET
    role: Union["BriefInventoryItemRoleRequest", None, Unset, int] = UNSET
    manufacturer: Union["BriefManufacturerRequest", None, Unset, int] = UNSET
    part_id: Union[Unset, str] = UNSET
    serial: Union[Unset, str] = UNSET
    asset_tag: Union[None, Unset, str] = UNSET
    discovered: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    component_type: Union[None, Unset, str] = UNSET
    component_id: Union[None, Unset, int] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedWritableInventoryItemRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device_request import BriefDeviceRequest
        from ..models.brief_inventory_item_role_request import BriefInventoryItemRoleRequest
        from ..models.brief_manufacturer_request import BriefManufacturerRequest

        device: Union[Unset, dict[str, Any], int]
        if isinstance(self.device, Unset):
            device = UNSET
        elif isinstance(self.device, BriefDeviceRequest):
            device = self.device.to_dict()
        else:
            device = self.device

        parent: Union[None, Unset, int]
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        name = self.name

        label = self.label

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

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
        field_dict.update({})
        if device is not UNSET:
            field_dict["device"] = device
        if parent is not UNSET:
            field_dict["parent"] = parent
        if name is not UNSET:
            field_dict["name"] = name
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

    def to_multipart(self) -> dict[str, Any]:
        device: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.device, Unset):
            device = UNSET
        elif isinstance(self.device, int):
            device = (None, str(self.device).encode(), "text/plain")
        else:
            device = (None, json.dumps(self.device.to_dict()).encode(), "application/json")

        parent: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, int):
            parent = (None, str(self.parent).encode(), "text/plain")
        else:
            parent = (None, str(self.parent).encode(), "text/plain")

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        label = self.label if isinstance(self.label, Unset) else (None, str(self.label).encode(), "text/plain")

        status: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

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

        serial = self.serial if isinstance(self.serial, Unset) else (None, str(self.serial).encode(), "text/plain")

        asset_tag: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.asset_tag, Unset):
            asset_tag = UNSET
        elif isinstance(self.asset_tag, str):
            asset_tag = (None, str(self.asset_tag).encode(), "text/plain")
        else:
            asset_tag = (None, str(self.asset_tag).encode(), "text/plain")

        discovered = (
            self.discovered
            if isinstance(self.discovered, Unset)
            else (None, str(self.discovered).encode(), "text/plain")
        )

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
        if parent is not UNSET:
            field_dict["parent"] = parent
        if name is not UNSET:
            field_dict["name"] = name
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
        from ..models.brief_device_request import BriefDeviceRequest
        from ..models.brief_inventory_item_role_request import BriefInventoryItemRoleRequest
        from ..models.brief_manufacturer_request import BriefManufacturerRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_writable_inventory_item_request_custom_fields import (
            PatchedWritableInventoryItemRequestCustomFields,
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

        def _parse_parent(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent = _parse_parent(d.pop("parent", UNSET))

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, PatchedWritableInventoryItemRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PatchedWritableInventoryItemRequestStatus(_status)

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
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedWritableInventoryItemRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedWritableInventoryItemRequestCustomFields.from_dict(_custom_fields)

        patched_writable_inventory_item_request = cls(
            device=device,
            parent=parent,
            name=name,
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

        patched_writable_inventory_item_request.additional_properties = d
        return patched_writable_inventory_item_request

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
