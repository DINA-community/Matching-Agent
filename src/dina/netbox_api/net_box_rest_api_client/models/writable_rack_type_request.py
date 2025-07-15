import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_rack_type_request_form_factor import WritableRackTypeRequestFormFactor
from ..models.writable_rack_type_request_outer_unit_type_1 import WritableRackTypeRequestOuterUnitType1
from ..models.writable_rack_type_request_outer_unit_type_2_type_1 import WritableRackTypeRequestOuterUnitType2Type1
from ..models.writable_rack_type_request_outer_unit_type_3_type_1 import WritableRackTypeRequestOuterUnitType3Type1
from ..models.writable_rack_type_request_weight_unit_type_1 import WritableRackTypeRequestWeightUnitType1
from ..models.writable_rack_type_request_weight_unit_type_2_type_1 import WritableRackTypeRequestWeightUnitType2Type1
from ..models.writable_rack_type_request_weight_unit_type_3_type_1 import WritableRackTypeRequestWeightUnitType3Type1
from ..models.writable_rack_type_request_width import WritableRackTypeRequestWidth
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_manufacturer_request import BriefManufacturerRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.writable_rack_type_request_custom_fields import WritableRackTypeRequestCustomFields


T = TypeVar("T", bound="WritableRackTypeRequest")


@_attrs_define
class WritableRackTypeRequest:
    """Adds support for custom fields and tags.

    Attributes:
        manufacturer (Union['BriefManufacturerRequest', int]):
        model (str):
        slug (str):
        form_factor (WritableRackTypeRequestFormFactor): * `2-post-frame` - 2-post frame
            * `4-post-frame` - 4-post frame
            * `4-post-cabinet` - 4-post cabinet
            * `wall-frame` - Wall-mounted frame
            * `wall-frame-vertical` - Wall-mounted frame (vertical)
            * `wall-cabinet` - Wall-mounted cabinet
            * `wall-cabinet-vertical` - Wall-mounted cabinet (vertical)
        description (Union[Unset, str]):
        width (Union[Unset, WritableRackTypeRequestWidth]): Rail-to-rail width

            * `10` - 10 inches
            * `19` - 19 inches
            * `21` - 21 inches
            * `23` - 23 inches
        u_height (Union[Unset, int]): Height in rack units
        starting_unit (Union[Unset, int]): Starting unit for rack
        desc_units (Union[Unset, bool]): Units are numbered top-to-bottom
        outer_width (Union[None, Unset, int]): Outer dimension of rack (width)
        outer_height (Union[None, Unset, int]): Outer dimension of rack (height)
        outer_depth (Union[None, Unset, int]): Outer dimension of rack (depth)
        outer_unit (Union[None, Unset, WritableRackTypeRequestOuterUnitType1,
            WritableRackTypeRequestOuterUnitType2Type1, WritableRackTypeRequestOuterUnitType3Type1]): * `mm` - Millimeters
            * `in` - Inches
        weight (Union[None, Unset, float]):
        max_weight (Union[None, Unset, int]): Maximum load capacity for the rack
        weight_unit (Union[None, Unset, WritableRackTypeRequestWeightUnitType1,
            WritableRackTypeRequestWeightUnitType2Type1, WritableRackTypeRequestWeightUnitType3Type1]): * `kg` - Kilograms
            * `g` - Grams
            * `lb` - Pounds
            * `oz` - Ounces
        mounting_depth (Union[None, Unset, int]): Maximum depth of a mounted device, in millimeters. For four-post
            racks, this is the distance between the front and rear rails.
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WritableRackTypeRequestCustomFields]):
    """

    manufacturer: Union["BriefManufacturerRequest", int]
    model: str
    slug: str
    form_factor: WritableRackTypeRequestFormFactor
    description: Union[Unset, str] = UNSET
    width: Union[Unset, WritableRackTypeRequestWidth] = UNSET
    u_height: Union[Unset, int] = UNSET
    starting_unit: Union[Unset, int] = UNSET
    desc_units: Union[Unset, bool] = UNSET
    outer_width: Union[None, Unset, int] = UNSET
    outer_height: Union[None, Unset, int] = UNSET
    outer_depth: Union[None, Unset, int] = UNSET
    outer_unit: Union[
        None,
        Unset,
        WritableRackTypeRequestOuterUnitType1,
        WritableRackTypeRequestOuterUnitType2Type1,
        WritableRackTypeRequestOuterUnitType3Type1,
    ] = UNSET
    weight: Union[None, Unset, float] = UNSET
    max_weight: Union[None, Unset, int] = UNSET
    weight_unit: Union[
        None,
        Unset,
        WritableRackTypeRequestWeightUnitType1,
        WritableRackTypeRequestWeightUnitType2Type1,
        WritableRackTypeRequestWeightUnitType3Type1,
    ] = UNSET
    mounting_depth: Union[None, Unset, int] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WritableRackTypeRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_manufacturer_request import BriefManufacturerRequest

        manufacturer: Union[dict[str, Any], int]
        if isinstance(self.manufacturer, BriefManufacturerRequest):
            manufacturer = self.manufacturer.to_dict()
        else:
            manufacturer = self.manufacturer

        model = self.model

        slug = self.slug

        form_factor = self.form_factor.value

        description = self.description

        width: Union[Unset, int] = UNSET
        if not isinstance(self.width, Unset):
            width = self.width.value

        u_height = self.u_height

        starting_unit = self.starting_unit

        desc_units = self.desc_units

        outer_width: Union[None, Unset, int]
        if isinstance(self.outer_width, Unset):
            outer_width = UNSET
        else:
            outer_width = self.outer_width

        outer_height: Union[None, Unset, int]
        if isinstance(self.outer_height, Unset):
            outer_height = UNSET
        else:
            outer_height = self.outer_height

        outer_depth: Union[None, Unset, int]
        if isinstance(self.outer_depth, Unset):
            outer_depth = UNSET
        else:
            outer_depth = self.outer_depth

        outer_unit: Union[None, Unset, str]
        if isinstance(self.outer_unit, Unset):
            outer_unit = UNSET
        elif isinstance(self.outer_unit, WritableRackTypeRequestOuterUnitType1):
            outer_unit = self.outer_unit.value
        elif isinstance(self.outer_unit, WritableRackTypeRequestOuterUnitType2Type1):
            outer_unit = self.outer_unit.value
        elif isinstance(self.outer_unit, WritableRackTypeRequestOuterUnitType3Type1):
            outer_unit = self.outer_unit.value
        else:
            outer_unit = self.outer_unit

        weight: Union[None, Unset, float]
        if isinstance(self.weight, Unset):
            weight = UNSET
        else:
            weight = self.weight

        max_weight: Union[None, Unset, int]
        if isinstance(self.max_weight, Unset):
            max_weight = UNSET
        else:
            max_weight = self.max_weight

        weight_unit: Union[None, Unset, str]
        if isinstance(self.weight_unit, Unset):
            weight_unit = UNSET
        elif isinstance(self.weight_unit, WritableRackTypeRequestWeightUnitType1):
            weight_unit = self.weight_unit.value
        elif isinstance(self.weight_unit, WritableRackTypeRequestWeightUnitType2Type1):
            weight_unit = self.weight_unit.value
        elif isinstance(self.weight_unit, WritableRackTypeRequestWeightUnitType3Type1):
            weight_unit = self.weight_unit.value
        else:
            weight_unit = self.weight_unit

        mounting_depth: Union[None, Unset, int]
        if isinstance(self.mounting_depth, Unset):
            mounting_depth = UNSET
        else:
            mounting_depth = self.mounting_depth

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
                "form_factor": form_factor,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if width is not UNSET:
            field_dict["width"] = width
        if u_height is not UNSET:
            field_dict["u_height"] = u_height
        if starting_unit is not UNSET:
            field_dict["starting_unit"] = starting_unit
        if desc_units is not UNSET:
            field_dict["desc_units"] = desc_units
        if outer_width is not UNSET:
            field_dict["outer_width"] = outer_width
        if outer_height is not UNSET:
            field_dict["outer_height"] = outer_height
        if outer_depth is not UNSET:
            field_dict["outer_depth"] = outer_depth
        if outer_unit is not UNSET:
            field_dict["outer_unit"] = outer_unit
        if weight is not UNSET:
            field_dict["weight"] = weight
        if max_weight is not UNSET:
            field_dict["max_weight"] = max_weight
        if weight_unit is not UNSET:
            field_dict["weight_unit"] = weight_unit
        if mounting_depth is not UNSET:
            field_dict["mounting_depth"] = mounting_depth
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
            manufacturer = (None, json.dumps(self.manufacturer.to_dict()).encode(), "application/json")

        model = (None, str(self.model).encode(), "text/plain")

        slug = (None, str(self.slug).encode(), "text/plain")

        form_factor = (None, str(self.form_factor.value).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        width: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.width, Unset):
            width = (None, str(self.width.value).encode(), "text/plain")

        u_height = (
            self.u_height if isinstance(self.u_height, Unset) else (None, str(self.u_height).encode(), "text/plain")
        )

        starting_unit = (
            self.starting_unit
            if isinstance(self.starting_unit, Unset)
            else (None, str(self.starting_unit).encode(), "text/plain")
        )

        desc_units = (
            self.desc_units
            if isinstance(self.desc_units, Unset)
            else (None, str(self.desc_units).encode(), "text/plain")
        )

        outer_width: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.outer_width, Unset):
            outer_width = UNSET
        elif isinstance(self.outer_width, int):
            outer_width = (None, str(self.outer_width).encode(), "text/plain")
        else:
            outer_width = (None, str(self.outer_width).encode(), "text/plain")

        outer_height: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.outer_height, Unset):
            outer_height = UNSET
        elif isinstance(self.outer_height, int):
            outer_height = (None, str(self.outer_height).encode(), "text/plain")
        else:
            outer_height = (None, str(self.outer_height).encode(), "text/plain")

        outer_depth: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.outer_depth, Unset):
            outer_depth = UNSET
        elif isinstance(self.outer_depth, int):
            outer_depth = (None, str(self.outer_depth).encode(), "text/plain")
        else:
            outer_depth = (None, str(self.outer_depth).encode(), "text/plain")

        outer_unit: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.outer_unit, Unset):
            outer_unit = UNSET
        elif isinstance(self.outer_unit, None):
            outer_unit = (None, str(self.outer_unit).encode(), "text/plain")
        elif isinstance(self.outer_unit, WritableRackTypeRequestOuterUnitType1):
            outer_unit = (None, str(self.outer_unit.value).encode(), "text/plain")
        elif isinstance(self.outer_unit, None):
            outer_unit = (None, str(self.outer_unit).encode(), "text/plain")
        elif isinstance(self.outer_unit, WritableRackTypeRequestOuterUnitType2Type1):
            outer_unit = (None, str(self.outer_unit.value).encode(), "text/plain")
        elif isinstance(self.outer_unit, None):
            outer_unit = (None, str(self.outer_unit).encode(), "text/plain")
        else:
            outer_unit = (None, str(self.outer_unit.value).encode(), "text/plain")

        weight: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.weight, Unset):
            weight = UNSET
        elif isinstance(self.weight, float):
            weight = (None, str(self.weight).encode(), "text/plain")
        else:
            weight = (None, str(self.weight).encode(), "text/plain")

        max_weight: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.max_weight, Unset):
            max_weight = UNSET
        elif isinstance(self.max_weight, int):
            max_weight = (None, str(self.max_weight).encode(), "text/plain")
        else:
            max_weight = (None, str(self.max_weight).encode(), "text/plain")

        weight_unit: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.weight_unit, Unset):
            weight_unit = UNSET
        elif isinstance(self.weight_unit, None):
            weight_unit = (None, str(self.weight_unit).encode(), "text/plain")
        elif isinstance(self.weight_unit, WritableRackTypeRequestWeightUnitType1):
            weight_unit = (None, str(self.weight_unit.value).encode(), "text/plain")
        elif isinstance(self.weight_unit, None):
            weight_unit = (None, str(self.weight_unit).encode(), "text/plain")
        elif isinstance(self.weight_unit, WritableRackTypeRequestWeightUnitType2Type1):
            weight_unit = (None, str(self.weight_unit.value).encode(), "text/plain")
        elif isinstance(self.weight_unit, None):
            weight_unit = (None, str(self.weight_unit).encode(), "text/plain")
        else:
            weight_unit = (None, str(self.weight_unit.value).encode(), "text/plain")

        mounting_depth: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.mounting_depth, Unset):
            mounting_depth = UNSET
        elif isinstance(self.mounting_depth, int):
            mounting_depth = (None, str(self.mounting_depth).encode(), "text/plain")
        else:
            mounting_depth = (None, str(self.mounting_depth).encode(), "text/plain")

        comments = (
            self.comments if isinstance(self.comments, Unset) else (None, str(self.comments).encode(), "text/plain")
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
            custom_fields = (None, json.dumps(self.custom_fields.to_dict()).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "manufacturer": manufacturer,
                "model": model,
                "slug": slug,
                "form_factor": form_factor,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if width is not UNSET:
            field_dict["width"] = width
        if u_height is not UNSET:
            field_dict["u_height"] = u_height
        if starting_unit is not UNSET:
            field_dict["starting_unit"] = starting_unit
        if desc_units is not UNSET:
            field_dict["desc_units"] = desc_units
        if outer_width is not UNSET:
            field_dict["outer_width"] = outer_width
        if outer_height is not UNSET:
            field_dict["outer_height"] = outer_height
        if outer_depth is not UNSET:
            field_dict["outer_depth"] = outer_depth
        if outer_unit is not UNSET:
            field_dict["outer_unit"] = outer_unit
        if weight is not UNSET:
            field_dict["weight"] = weight
        if max_weight is not UNSET:
            field_dict["max_weight"] = max_weight
        if weight_unit is not UNSET:
            field_dict["weight_unit"] = weight_unit
        if mounting_depth is not UNSET:
            field_dict["mounting_depth"] = mounting_depth
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
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.writable_rack_type_request_custom_fields import WritableRackTypeRequestCustomFields

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

        form_factor = WritableRackTypeRequestFormFactor(d.pop("form_factor"))

        description = d.pop("description", UNSET)

        _width = d.pop("width", UNSET)
        width: Union[Unset, WritableRackTypeRequestWidth]
        if isinstance(_width, Unset):
            width = UNSET
        else:
            width = WritableRackTypeRequestWidth(_width)

        u_height = d.pop("u_height", UNSET)

        starting_unit = d.pop("starting_unit", UNSET)

        desc_units = d.pop("desc_units", UNSET)

        def _parse_outer_width(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        outer_width = _parse_outer_width(d.pop("outer_width", UNSET))

        def _parse_outer_height(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        outer_height = _parse_outer_height(d.pop("outer_height", UNSET))

        def _parse_outer_depth(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        outer_depth = _parse_outer_depth(d.pop("outer_depth", UNSET))

        def _parse_outer_unit(
            data: object,
        ) -> Union[
            None,
            Unset,
            WritableRackTypeRequestOuterUnitType1,
            WritableRackTypeRequestOuterUnitType2Type1,
            WritableRackTypeRequestOuterUnitType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outer_unit_type_1 = WritableRackTypeRequestOuterUnitType1(data)

                return outer_unit_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outer_unit_type_2_type_1 = WritableRackTypeRequestOuterUnitType2Type1(data)

                return outer_unit_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outer_unit_type_3_type_1 = WritableRackTypeRequestOuterUnitType3Type1(data)

                return outer_unit_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    WritableRackTypeRequestOuterUnitType1,
                    WritableRackTypeRequestOuterUnitType2Type1,
                    WritableRackTypeRequestOuterUnitType3Type1,
                ],
                data,
            )

        outer_unit = _parse_outer_unit(d.pop("outer_unit", UNSET))

        def _parse_weight(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        weight = _parse_weight(d.pop("weight", UNSET))

        def _parse_max_weight(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_weight = _parse_max_weight(d.pop("max_weight", UNSET))

        def _parse_weight_unit(
            data: object,
        ) -> Union[
            None,
            Unset,
            WritableRackTypeRequestWeightUnitType1,
            WritableRackTypeRequestWeightUnitType2Type1,
            WritableRackTypeRequestWeightUnitType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                weight_unit_type_1 = WritableRackTypeRequestWeightUnitType1(data)

                return weight_unit_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                weight_unit_type_2_type_1 = WritableRackTypeRequestWeightUnitType2Type1(data)

                return weight_unit_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                weight_unit_type_3_type_1 = WritableRackTypeRequestWeightUnitType3Type1(data)

                return weight_unit_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    WritableRackTypeRequestWeightUnitType1,
                    WritableRackTypeRequestWeightUnitType2Type1,
                    WritableRackTypeRequestWeightUnitType3Type1,
                ],
                data,
            )

        weight_unit = _parse_weight_unit(d.pop("weight_unit", UNSET))

        def _parse_mounting_depth(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        mounting_depth = _parse_mounting_depth(d.pop("mounting_depth", UNSET))

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WritableRackTypeRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WritableRackTypeRequestCustomFields.from_dict(_custom_fields)

        writable_rack_type_request = cls(
            manufacturer=manufacturer,
            model=model,
            slug=slug,
            form_factor=form_factor,
            description=description,
            width=width,
            u_height=u_height,
            starting_unit=starting_unit,
            desc_units=desc_units,
            outer_width=outer_width,
            outer_height=outer_height,
            outer_depth=outer_depth,
            outer_unit=outer_unit,
            weight=weight,
            max_weight=max_weight,
            weight_unit=weight_unit,
            mounting_depth=mounting_depth,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        writable_rack_type_request.additional_properties = d
        return writable_rack_type_request

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
