import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_device_type_request_airflow_type_1 import (
    WritableDeviceTypeRequestAirflowType1,
)
from ..models.writable_device_type_request_airflow_type_2_type_1 import (
    WritableDeviceTypeRequestAirflowType2Type1,
)
from ..models.writable_device_type_request_airflow_type_3_type_1 import (
    WritableDeviceTypeRequestAirflowType3Type1,
)
from ..models.writable_device_type_request_parentchild_status import (
    WritableDeviceTypeRequestParentchildStatus,
)
from ..models.writable_device_type_request_weight_unit_type_1 import (
    WritableDeviceTypeRequestWeightUnitType1,
)
from ..models.writable_device_type_request_weight_unit_type_2_type_1 import (
    WritableDeviceTypeRequestWeightUnitType2Type1,
)
from ..models.writable_device_type_request_weight_unit_type_3_type_1 import (
    WritableDeviceTypeRequestWeightUnitType3Type1,
)
from ..types import UNSET, File, FileJsonType, Unset

if TYPE_CHECKING:
    from ..models.brief_manufacturer_request import BriefManufacturerRequest
    from ..models.brief_platform_request import BriefPlatformRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.writable_device_type_request_custom_fields import (
        WritableDeviceTypeRequestCustomFields,
    )


T = TypeVar("T", bound="WritableDeviceTypeRequest")


@_attrs_define
class WritableDeviceTypeRequest:
    """Adds support for custom fields and tags.

    Attributes:
        manufacturer (Union['BriefManufacturerRequest', int]):
        model (str):
        slug (str):
        default_platform (Union['BriefPlatformRequest', None, Unset, int]):
        part_number (Union[Unset, str]): Discrete part number (optional)
        u_height (Union[Unset, float]):  Default: 1.0.
        exclude_from_utilization (Union[Unset, bool]): Devices of this type are excluded when calculating rack
            utilization.
        is_full_depth (Union[Unset, bool]): Device consumes both front and rear rack faces.
        subdevice_role (Union[None, Unset, WritableDeviceTypeRequestParentchildStatus]): Parent devices house child
            devices in device bays. Leave blank if this device type is neither a parent nor a child.

            * `parent` - Parent
            * `child` - Child
        airflow (Union[None, Unset, WritableDeviceTypeRequestAirflowType1, WritableDeviceTypeRequestAirflowType2Type1,
            WritableDeviceTypeRequestAirflowType3Type1]): * `front-to-rear` - Front to rear
            * `rear-to-front` - Rear to front
            * `left-to-right` - Left to right
            * `right-to-left` - Right to left
            * `side-to-rear` - Side to rear
            * `rear-to-side` - Rear to side
            * `bottom-to-top` - Bottom to top
            * `top-to-bottom` - Top to bottom
            * `passive` - Passive
            * `mixed` - Mixed
        weight (Union[None, Unset, float]):
        weight_unit (Union[None, Unset, WritableDeviceTypeRequestWeightUnitType1,
            WritableDeviceTypeRequestWeightUnitType2Type1, WritableDeviceTypeRequestWeightUnitType3Type1]): * `kg` -
            Kilograms
            * `g` - Grams
            * `lb` - Pounds
            * `oz` - Ounces
        front_image (Union[File, None, Unset]):
        rear_image (Union[File, None, Unset]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WritableDeviceTypeRequestCustomFields]):
    """

    manufacturer: Union["BriefManufacturerRequest", int]
    model: str
    slug: str
    default_platform: Union["BriefPlatformRequest", None, Unset, int] = UNSET
    part_number: Union[Unset, str] = UNSET
    u_height: Union[Unset, float] = 1.0
    exclude_from_utilization: Union[Unset, bool] = UNSET
    is_full_depth: Union[Unset, bool] = UNSET
    subdevice_role: Union[None, Unset, WritableDeviceTypeRequestParentchildStatus] = (
        UNSET
    )
    airflow: Union[
        None,
        Unset,
        WritableDeviceTypeRequestAirflowType1,
        WritableDeviceTypeRequestAirflowType2Type1,
        WritableDeviceTypeRequestAirflowType3Type1,
    ] = UNSET
    weight: Union[None, Unset, float] = UNSET
    weight_unit: Union[
        None,
        Unset,
        WritableDeviceTypeRequestWeightUnitType1,
        WritableDeviceTypeRequestWeightUnitType2Type1,
        WritableDeviceTypeRequestWeightUnitType3Type1,
    ] = UNSET
    front_image: Union[File, None, Unset] = UNSET
    rear_image: Union[File, None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WritableDeviceTypeRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_manufacturer_request import BriefManufacturerRequest
        from ..models.brief_platform_request import BriefPlatformRequest

        manufacturer: Union[dict[str, Any], int]
        if isinstance(self.manufacturer, BriefManufacturerRequest):
            manufacturer = self.manufacturer.to_dict()
        else:
            manufacturer = self.manufacturer

        model = self.model

        slug = self.slug

        default_platform: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.default_platform, Unset):
            default_platform = UNSET
        elif isinstance(self.default_platform, BriefPlatformRequest):
            default_platform = self.default_platform.to_dict()
        else:
            default_platform = self.default_platform

        part_number = self.part_number

        u_height = self.u_height

        exclude_from_utilization = self.exclude_from_utilization

        is_full_depth = self.is_full_depth

        subdevice_role: Union[None, Unset, str]
        if isinstance(self.subdevice_role, Unset):
            subdevice_role = UNSET
        elif isinstance(
            self.subdevice_role, WritableDeviceTypeRequestParentchildStatus
        ):
            subdevice_role = self.subdevice_role.value
        elif isinstance(
            self.subdevice_role, WritableDeviceTypeRequestParentchildStatus
        ):
            subdevice_role = self.subdevice_role.value
        elif isinstance(
            self.subdevice_role, WritableDeviceTypeRequestParentchildStatus
        ):
            subdevice_role = self.subdevice_role.value
        else:
            subdevice_role = self.subdevice_role

        airflow: Union[None, Unset, str]
        if isinstance(self.airflow, Unset):
            airflow = UNSET
        elif isinstance(self.airflow, WritableDeviceTypeRequestAirflowType1):
            airflow = self.airflow.value
        elif isinstance(self.airflow, WritableDeviceTypeRequestAirflowType2Type1):
            airflow = self.airflow.value
        elif isinstance(self.airflow, WritableDeviceTypeRequestAirflowType3Type1):
            airflow = self.airflow.value
        else:
            airflow = self.airflow

        weight: Union[None, Unset, float]
        if isinstance(self.weight, Unset):
            weight = UNSET
        else:
            weight = self.weight

        weight_unit: Union[None, Unset, str]
        if isinstance(self.weight_unit, Unset):
            weight_unit = UNSET
        elif isinstance(self.weight_unit, WritableDeviceTypeRequestWeightUnitType1):
            weight_unit = self.weight_unit.value
        elif isinstance(
            self.weight_unit, WritableDeviceTypeRequestWeightUnitType2Type1
        ):
            weight_unit = self.weight_unit.value
        elif isinstance(
            self.weight_unit, WritableDeviceTypeRequestWeightUnitType3Type1
        ):
            weight_unit = self.weight_unit.value
        else:
            weight_unit = self.weight_unit

        front_image: Union[FileJsonType, None, Unset]
        if isinstance(self.front_image, Unset):
            front_image = UNSET
        elif isinstance(self.front_image, File):
            front_image = self.front_image.to_tuple()

        else:
            front_image = self.front_image

        rear_image: Union[FileJsonType, None, Unset]
        if isinstance(self.rear_image, Unset):
            rear_image = UNSET
        elif isinstance(self.rear_image, File):
            rear_image = self.rear_image.to_tuple()

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "manufacturer": manufacturer,
                "model": model,
                "slug": slug,
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

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        manufacturer: tuple[None, bytes, str]

        if isinstance(self.manufacturer, int):
            manufacturer = (None, str(self.manufacturer).encode(), "text/plain")
        else:
            manufacturer = (
                None,
                json.dumps(self.manufacturer.to_dict()).encode(),
                "application/json",
            )

        model = (None, str(self.model).encode(), "text/plain")

        slug = (None, str(self.slug).encode(), "text/plain")

        default_platform: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.default_platform, Unset):
            default_platform = UNSET
        elif isinstance(self.default_platform, int):
            default_platform = (None, str(self.default_platform).encode(), "text/plain")
        elif isinstance(self.default_platform, None):
            default_platform = (None, str(self.default_platform).encode(), "text/plain")
        elif isinstance(self.default_platform, BriefPlatformRequest):
            default_platform = (
                None,
                json.dumps(self.default_platform.to_dict()).encode(),
                "application/json",
            )
        else:
            default_platform = (None, str(self.default_platform).encode(), "text/plain")

        part_number = (
            self.part_number
            if isinstance(self.part_number, Unset)
            else (None, str(self.part_number).encode(), "text/plain")
        )

        u_height = (
            self.u_height
            if isinstance(self.u_height, Unset)
            else (None, str(self.u_height).encode(), "text/plain")
        )

        exclude_from_utilization = (
            self.exclude_from_utilization
            if isinstance(self.exclude_from_utilization, Unset)
            else (None, str(self.exclude_from_utilization).encode(), "text/plain")
        )

        is_full_depth = (
            self.is_full_depth
            if isinstance(self.is_full_depth, Unset)
            else (None, str(self.is_full_depth).encode(), "text/plain")
        )

        subdevice_role: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.subdevice_role, Unset):
            subdevice_role = UNSET
        elif isinstance(self.subdevice_role, None):
            subdevice_role = (None, str(self.subdevice_role).encode(), "text/plain")
        elif isinstance(
            self.subdevice_role, WritableDeviceTypeRequestParentchildStatus
        ):
            subdevice_role = (
                None,
                str(self.subdevice_role.value).encode(),
                "text/plain",
            )
        elif isinstance(self.subdevice_role, None):
            subdevice_role = (None, str(self.subdevice_role).encode(), "text/plain")
        elif isinstance(
            self.subdevice_role, WritableDeviceTypeRequestParentchildStatus
        ):
            subdevice_role = (
                None,
                str(self.subdevice_role.value).encode(),
                "text/plain",
            )
        elif isinstance(self.subdevice_role, None):
            subdevice_role = (None, str(self.subdevice_role).encode(), "text/plain")
        else:
            subdevice_role = (
                None,
                str(self.subdevice_role.value).encode(),
                "text/plain",
            )

        airflow: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.airflow, Unset):
            airflow = UNSET
        elif isinstance(self.airflow, None):
            airflow = (None, str(self.airflow).encode(), "text/plain")
        elif isinstance(self.airflow, WritableDeviceTypeRequestAirflowType1):
            airflow = (None, str(self.airflow.value).encode(), "text/plain")
        elif isinstance(self.airflow, None):
            airflow = (None, str(self.airflow).encode(), "text/plain")
        elif isinstance(self.airflow, WritableDeviceTypeRequestAirflowType2Type1):
            airflow = (None, str(self.airflow.value).encode(), "text/plain")
        elif isinstance(self.airflow, None):
            airflow = (None, str(self.airflow).encode(), "text/plain")
        else:
            airflow = (None, str(self.airflow.value).encode(), "text/plain")

        weight: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.weight, Unset):
            weight = UNSET
        elif isinstance(self.weight, float):
            weight = (None, str(self.weight).encode(), "text/plain")
        else:
            weight = (None, str(self.weight).encode(), "text/plain")

        weight_unit: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.weight_unit, Unset):
            weight_unit = UNSET
        elif isinstance(self.weight_unit, None):
            weight_unit = (None, str(self.weight_unit).encode(), "text/plain")
        elif isinstance(self.weight_unit, WritableDeviceTypeRequestWeightUnitType1):
            weight_unit = (None, str(self.weight_unit.value).encode(), "text/plain")
        elif isinstance(self.weight_unit, None):
            weight_unit = (None, str(self.weight_unit).encode(), "text/plain")
        elif isinstance(
            self.weight_unit, WritableDeviceTypeRequestWeightUnitType2Type1
        ):
            weight_unit = (None, str(self.weight_unit.value).encode(), "text/plain")
        elif isinstance(self.weight_unit, None):
            weight_unit = (None, str(self.weight_unit).encode(), "text/plain")
        else:
            weight_unit = (None, str(self.weight_unit.value).encode(), "text/plain")

        front_image: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.front_image, Unset):
            front_image = UNSET
        elif isinstance(self.front_image, File):
            front_image = self.front_image.to_tuple()
        else:
            front_image = (None, str(self.front_image).encode(), "text/plain")

        rear_image: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.rear_image, Unset):
            rear_image = UNSET
        elif isinstance(self.rear_image, File):
            rear_image = self.rear_image.to_tuple()
        else:
            rear_image = (None, str(self.rear_image).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        comments = (
            self.comments
            if isinstance(self.comments, Unset)
            else (None, str(self.comments).encode(), "text/plain")
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
            custom_fields = (
                None,
                json.dumps(self.custom_fields.to_dict()).encode(),
                "application/json",
            )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "manufacturer": manufacturer,
                "model": model,
                "slug": slug,
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_manufacturer_request import BriefManufacturerRequest
        from ..models.brief_platform_request import BriefPlatformRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.writable_device_type_request_custom_fields import (
            WritableDeviceTypeRequestCustomFields,
        )

        d = dict(src_dict)

        def _parse_manufacturer(data: object) -> Union["BriefManufacturerRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                manufacturer_type_1 = BriefManufacturerRequest.from_dict(data)

                return manufacturer_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefManufacturerRequest", int], data)

        manufacturer = _parse_manufacturer(d.pop("manufacturer"))

        model = d.pop("model")

        slug = d.pop("slug")

        def _parse_default_platform(
            data: object,
        ) -> Union["BriefPlatformRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                default_platform_type_1_type_1 = BriefPlatformRequest.from_dict(data)

                return default_platform_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefPlatformRequest", None, Unset, int], data)

        default_platform = _parse_default_platform(d.pop("default_platform", UNSET))

        part_number = d.pop("part_number", UNSET)

        u_height = d.pop("u_height", UNSET)

        exclude_from_utilization = d.pop("exclude_from_utilization", UNSET)

        is_full_depth = d.pop("is_full_depth", UNSET)

        def _parse_subdevice_role(
            data: object,
        ) -> Union[None, Unset, WritableDeviceTypeRequestParentchildStatus]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subdevice_role_type_1 = WritableDeviceTypeRequestParentchildStatus(data)

                return subdevice_role_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subdevice_role_type_2_type_1 = (
                    WritableDeviceTypeRequestParentchildStatus(data)
                )

                return subdevice_role_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subdevice_role_type_3_type_1 = (
                    WritableDeviceTypeRequestParentchildStatus(data)
                )

                return subdevice_role_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, WritableDeviceTypeRequestParentchildStatus], data
            )

        subdevice_role = _parse_subdevice_role(d.pop("subdevice_role", UNSET))

        def _parse_airflow(
            data: object,
        ) -> Union[
            None,
            Unset,
            WritableDeviceTypeRequestAirflowType1,
            WritableDeviceTypeRequestAirflowType2Type1,
            WritableDeviceTypeRequestAirflowType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                airflow_type_1 = WritableDeviceTypeRequestAirflowType1(data)

                return airflow_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                airflow_type_2_type_1 = WritableDeviceTypeRequestAirflowType2Type1(data)

                return airflow_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                airflow_type_3_type_1 = WritableDeviceTypeRequestAirflowType3Type1(data)

                return airflow_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    WritableDeviceTypeRequestAirflowType1,
                    WritableDeviceTypeRequestAirflowType2Type1,
                    WritableDeviceTypeRequestAirflowType3Type1,
                ],
                data,
            )

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
        ) -> Union[
            None,
            Unset,
            WritableDeviceTypeRequestWeightUnitType1,
            WritableDeviceTypeRequestWeightUnitType2Type1,
            WritableDeviceTypeRequestWeightUnitType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                weight_unit_type_1 = WritableDeviceTypeRequestWeightUnitType1(data)

                return weight_unit_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                weight_unit_type_2_type_1 = (
                    WritableDeviceTypeRequestWeightUnitType2Type1(data)
                )

                return weight_unit_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                weight_unit_type_3_type_1 = (
                    WritableDeviceTypeRequestWeightUnitType3Type1(data)
                )

                return weight_unit_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    WritableDeviceTypeRequestWeightUnitType1,
                    WritableDeviceTypeRequestWeightUnitType2Type1,
                    WritableDeviceTypeRequestWeightUnitType3Type1,
                ],
                data,
            )

        weight_unit = _parse_weight_unit(d.pop("weight_unit", UNSET))

        def _parse_front_image(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                front_image_type_0 = File(payload=BytesIO(data))

                return front_image_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        front_image = _parse_front_image(d.pop("front_image", UNSET))

        def _parse_rear_image(data: object) -> Union[File, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                rear_image_type_0 = File(payload=BytesIO(data))

                return rear_image_type_0
            except:  # noqa: E722
                pass
            return cast(Union[File, None, Unset], data)

        rear_image = _parse_rear_image(d.pop("rear_image", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WritableDeviceTypeRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WritableDeviceTypeRequestCustomFields.from_dict(
                _custom_fields
            )

        writable_device_type_request = cls(
            manufacturer=manufacturer,
            model=model,
            slug=slug,
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
        )

        writable_device_type_request.additional_properties = d
        return writable_device_type_request

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
