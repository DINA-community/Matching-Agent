import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_manufacturer import BriefManufacturer
    from ..models.brief_platform import BriefPlatform
    from ..models.device_type_airflow_type_0 import DeviceTypeAirflowType0
    from ..models.device_type_custom_fields import DeviceTypeCustomFields
    from ..models.device_type_subdevice_role_type_0 import DeviceTypeSubdeviceRoleType0
    from ..models.device_type_weight_unit_type_0 import DeviceTypeWeightUnitType0
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="DeviceType")


@_attrs_define
class DeviceType:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        manufacturer (BriefManufacturer): Adds support for custom fields and tags.
        model (str):
        slug (str):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        console_port_template_count (int):
        console_server_port_template_count (int):
        power_port_template_count (int):
        power_outlet_template_count (int):
        interface_template_count (int):
        front_port_template_count (int):
        rear_port_template_count (int):
        device_bay_template_count (int):
        module_bay_template_count (int):
        inventory_item_template_count (int):
        default_platform (Union['BriefPlatform', None, Unset]):
        part_number (Union[Unset, str]): Discrete part number (optional)
        u_height (Union[Unset, float]):  Default: 1.0.
        exclude_from_utilization (Union[Unset, bool]): Devices of this type are excluded when calculating rack
            utilization.
        is_full_depth (Union[Unset, bool]): Device consumes both front and rear rack faces.
        subdevice_role (Union['DeviceTypeSubdeviceRoleType0', None, Unset]):
        airflow (Union['DeviceTypeAirflowType0', None, Unset]):
        weight (Union[None, Unset, float]):
        weight_unit (Union['DeviceTypeWeightUnitType0', None, Unset]):
        front_image (Union[None, Unset, str]):
        rear_image (Union[None, Unset, str]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, DeviceTypeCustomFields]):
        device_count (Union[Unset, int]):
    """

    id: int
    url: str
    display_url: str
    display: str
    manufacturer: "BriefManufacturer"
    model: str
    slug: str
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    console_port_template_count: int
    console_server_port_template_count: int
    power_port_template_count: int
    power_outlet_template_count: int
    interface_template_count: int
    front_port_template_count: int
    rear_port_template_count: int
    device_bay_template_count: int
    module_bay_template_count: int
    inventory_item_template_count: int
    default_platform: Union["BriefPlatform", None, Unset] = UNSET
    part_number: Union[Unset, str] = UNSET
    u_height: Union[Unset, float] = 1.0
    exclude_from_utilization: Union[Unset, bool] = UNSET
    is_full_depth: Union[Unset, bool] = UNSET
    subdevice_role: Union["DeviceTypeSubdeviceRoleType0", None, Unset] = UNSET
    airflow: Union["DeviceTypeAirflowType0", None, Unset] = UNSET
    weight: Union[None, Unset, float] = UNSET
    weight_unit: Union["DeviceTypeWeightUnitType0", None, Unset] = UNSET
    front_image: Union[None, Unset, str] = UNSET
    rear_image: Union[None, Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "DeviceTypeCustomFields"] = UNSET
    device_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_platform import BriefPlatform
        from ..models.device_type_airflow_type_0 import DeviceTypeAirflowType0
        from ..models.device_type_subdevice_role_type_0 import (
            DeviceTypeSubdeviceRoleType0,
        )
        from ..models.device_type_weight_unit_type_0 import DeviceTypeWeightUnitType0

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        manufacturer = self.manufacturer.to_dict()

        model = self.model

        slug = self.slug

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

        console_port_template_count = self.console_port_template_count

        console_server_port_template_count = self.console_server_port_template_count

        power_port_template_count = self.power_port_template_count

        power_outlet_template_count = self.power_outlet_template_count

        interface_template_count = self.interface_template_count

        front_port_template_count = self.front_port_template_count

        rear_port_template_count = self.rear_port_template_count

        device_bay_template_count = self.device_bay_template_count

        module_bay_template_count = self.module_bay_template_count

        inventory_item_template_count = self.inventory_item_template_count

        default_platform: Union[None, Unset, dict[str, Any]]
        if isinstance(self.default_platform, Unset):
            default_platform = UNSET
        elif isinstance(self.default_platform, BriefPlatform):
            default_platform = self.default_platform.to_dict()
        else:
            default_platform = self.default_platform

        part_number = self.part_number

        u_height = self.u_height

        exclude_from_utilization = self.exclude_from_utilization

        is_full_depth = self.is_full_depth

        subdevice_role: Union[None, Unset, dict[str, Any]]
        if isinstance(self.subdevice_role, Unset):
            subdevice_role = UNSET
        elif isinstance(self.subdevice_role, DeviceTypeSubdeviceRoleType0):
            subdevice_role = self.subdevice_role.to_dict()
        else:
            subdevice_role = self.subdevice_role

        airflow: Union[None, Unset, dict[str, Any]]
        if isinstance(self.airflow, Unset):
            airflow = UNSET
        elif isinstance(self.airflow, DeviceTypeAirflowType0):
            airflow = self.airflow.to_dict()
        else:
            airflow = self.airflow

        weight: Union[None, Unset, float]
        if isinstance(self.weight, Unset):
            weight = UNSET
        else:
            weight = self.weight

        weight_unit: Union[None, Unset, dict[str, Any]]
        if isinstance(self.weight_unit, Unset):
            weight_unit = UNSET
        elif isinstance(self.weight_unit, DeviceTypeWeightUnitType0):
            weight_unit = self.weight_unit.to_dict()
        else:
            weight_unit = self.weight_unit

        front_image: Union[None, Unset, str]
        if isinstance(self.front_image, Unset):
            front_image = UNSET
        else:
            front_image = self.front_image

        rear_image: Union[None, Unset, str]
        if isinstance(self.rear_image, Unset):
            rear_image = UNSET
        else:
            rear_image = self.rear_image

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

        device_count = self.device_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "manufacturer": manufacturer,
                "model": model,
                "slug": slug,
                "created": created,
                "last_updated": last_updated,
                "console_port_template_count": console_port_template_count,
                "console_server_port_template_count": console_server_port_template_count,
                "power_port_template_count": power_port_template_count,
                "power_outlet_template_count": power_outlet_template_count,
                "interface_template_count": interface_template_count,
                "front_port_template_count": front_port_template_count,
                "rear_port_template_count": rear_port_template_count,
                "device_bay_template_count": device_bay_template_count,
                "module_bay_template_count": module_bay_template_count,
                "inventory_item_template_count": inventory_item_template_count,
            }
        )
        if default_platform is not UNSET:
            field_dict["default_platform"] = default_platform
        if part_number is not UNSET:
            field_dict["part_number"] = part_number
        if u_height is not UNSET:
            field_dict["u_height"] = u_height
        if exclude_from_utilization is not UNSET:
            field_dict["exclude_from_utilization"] = exclude_from_utilization
        if is_full_depth is not UNSET:
            field_dict["is_full_depth"] = is_full_depth
        if subdevice_role is not UNSET:
            field_dict["subdevice_role"] = subdevice_role
        if airflow is not UNSET:
            field_dict["airflow"] = airflow
        if weight is not UNSET:
            field_dict["weight"] = weight
        if weight_unit is not UNSET:
            field_dict["weight_unit"] = weight_unit
        if front_image is not UNSET:
            field_dict["front_image"] = front_image
        if rear_image is not UNSET:
            field_dict["rear_image"] = rear_image
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if device_count is not UNSET:
            field_dict["device_count"] = device_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_manufacturer import BriefManufacturer
        from ..models.brief_platform import BriefPlatform
        from ..models.device_type_airflow_type_0 import DeviceTypeAirflowType0
        from ..models.device_type_custom_fields import DeviceTypeCustomFields
        from ..models.device_type_subdevice_role_type_0 import (
            DeviceTypeSubdeviceRoleType0,
        )
        from ..models.device_type_weight_unit_type_0 import DeviceTypeWeightUnitType0
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        manufacturer = BriefManufacturer.from_dict(d.pop("manufacturer"))

        model = d.pop("model")

        slug = d.pop("slug")

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

        console_port_template_count = d.pop("console_port_template_count")

        console_server_port_template_count = d.pop("console_server_port_template_count")

        power_port_template_count = d.pop("power_port_template_count")

        power_outlet_template_count = d.pop("power_outlet_template_count")

        interface_template_count = d.pop("interface_template_count")

        front_port_template_count = d.pop("front_port_template_count")

        rear_port_template_count = d.pop("rear_port_template_count")

        device_bay_template_count = d.pop("device_bay_template_count")

        module_bay_template_count = d.pop("module_bay_template_count")

        inventory_item_template_count = d.pop("inventory_item_template_count")

        def _parse_default_platform(
            data: object,
        ) -> Union["BriefPlatform", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_platform_type_1 = BriefPlatform.from_dict(data)

                return default_platform_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefPlatform", None, Unset], data)

        default_platform = _parse_default_platform(d.pop("default_platform", UNSET))

        part_number = d.pop("part_number", UNSET)

        u_height = d.pop("u_height", UNSET)

        exclude_from_utilization = d.pop("exclude_from_utilization", UNSET)

        is_full_depth = d.pop("is_full_depth", UNSET)

        def _parse_subdevice_role(
            data: object,
        ) -> Union["DeviceTypeSubdeviceRoleType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subdevice_role_type_0 = DeviceTypeSubdeviceRoleType0.from_dict(data)

                return subdevice_role_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DeviceTypeSubdeviceRoleType0", None, Unset], data)

        subdevice_role = _parse_subdevice_role(d.pop("subdevice_role", UNSET))

        def _parse_airflow(
            data: object,
        ) -> Union["DeviceTypeAirflowType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                airflow_type_0 = DeviceTypeAirflowType0.from_dict(data)

                return airflow_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DeviceTypeAirflowType0", None, Unset], data)

        airflow = _parse_airflow(d.pop("airflow", UNSET))

        def _parse_weight(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        weight = _parse_weight(d.pop("weight", UNSET))

        def _parse_weight_unit(
            data: object,
        ) -> Union["DeviceTypeWeightUnitType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                weight_unit_type_0 = DeviceTypeWeightUnitType0.from_dict(data)

                return weight_unit_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DeviceTypeWeightUnitType0", None, Unset], data)

        weight_unit = _parse_weight_unit(d.pop("weight_unit", UNSET))

        def _parse_front_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        front_image = _parse_front_image(d.pop("front_image", UNSET))

        def _parse_rear_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rear_image = _parse_rear_image(d.pop("rear_image", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, DeviceTypeCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = DeviceTypeCustomFields.from_dict(_custom_fields)

        device_count = d.pop("device_count", UNSET)

        device_type = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            manufacturer=manufacturer,
            model=model,
            slug=slug,
            created=created,
            last_updated=last_updated,
            console_port_template_count=console_port_template_count,
            console_server_port_template_count=console_server_port_template_count,
            power_port_template_count=power_port_template_count,
            power_outlet_template_count=power_outlet_template_count,
            interface_template_count=interface_template_count,
            front_port_template_count=front_port_template_count,
            rear_port_template_count=rear_port_template_count,
            device_bay_template_count=device_bay_template_count,
            module_bay_template_count=module_bay_template_count,
            inventory_item_template_count=inventory_item_template_count,
            default_platform=default_platform,
            part_number=part_number,
            u_height=u_height,
            exclude_from_utilization=exclude_from_utilization,
            is_full_depth=is_full_depth,
            subdevice_role=subdevice_role,
            airflow=airflow,
            weight=weight,
            weight_unit=weight_unit,
            front_image=front_image,
            rear_image=rear_image,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
            device_count=device_count,
        )

        device_type.additional_properties = d
        return device_type

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
