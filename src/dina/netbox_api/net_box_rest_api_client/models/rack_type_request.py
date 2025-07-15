from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rack_type_request_form_factor_type_1 import RackTypeRequestFormFactorType1
from ..models.rack_type_request_form_factor_type_2_type_1 import RackTypeRequestFormFactorType2Type1
from ..models.rack_type_request_form_factor_type_3_type_1 import RackTypeRequestFormFactorType3Type1
from ..models.rack_type_request_outer_unit_type_1 import RackTypeRequestOuterUnitType1
from ..models.rack_type_request_outer_unit_type_2_type_1 import RackTypeRequestOuterUnitType2Type1
from ..models.rack_type_request_outer_unit_type_3_type_1 import RackTypeRequestOuterUnitType3Type1
from ..models.rack_type_request_weight_unit_type_1 import RackTypeRequestWeightUnitType1
from ..models.rack_type_request_weight_unit_type_2_type_1 import RackTypeRequestWeightUnitType2Type1
from ..models.rack_type_request_weight_unit_type_3_type_1 import RackTypeRequestWeightUnitType3Type1
from ..models.rack_type_request_width import RackTypeRequestWidth
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_manufacturer_request import BriefManufacturerRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.rack_type_request_custom_fields import RackTypeRequestCustomFields


T = TypeVar("T", bound="RackTypeRequest")


@_attrs_define
class RackTypeRequest:
    """Adds support for custom fields and tags.

    Attributes:
        manufacturer (Union['BriefManufacturerRequest', int]):
        model (str):
        slug (str):
        description (Union[Unset, str]):
        form_factor (Union[None, RackTypeRequestFormFactorType1, RackTypeRequestFormFactorType2Type1,
            RackTypeRequestFormFactorType3Type1, Unset]): * `2-post-frame` - 2-post frame
            * `4-post-frame` - 4-post frame
            * `4-post-cabinet` - 4-post cabinet
            * `wall-frame` - Wall-mounted frame
            * `wall-frame-vertical` - Wall-mounted frame (vertical)
            * `wall-cabinet` - Wall-mounted cabinet
            * `wall-cabinet-vertical` - Wall-mounted cabinet (vertical)
        width (Union[Unset, RackTypeRequestWidth]): * `10` - 10 inches
            * `19` - 19 inches
            * `21` - 21 inches
            * `23` - 23 inches
        u_height (Union[Unset, int]): Height in rack units
        starting_unit (Union[Unset, int]): Starting unit for rack
        desc_units (Union[Unset, bool]): Units are numbered top-to-bottom
        outer_width (Union[None, Unset, int]): Outer dimension of rack (width)
        outer_height (Union[None, Unset, int]): Outer dimension of rack (height)
        outer_depth (Union[None, Unset, int]): Outer dimension of rack (depth)
        outer_unit (Union[None, RackTypeRequestOuterUnitType1, RackTypeRequestOuterUnitType2Type1,
            RackTypeRequestOuterUnitType3Type1, Unset]): * `mm` - Millimeters
            * `in` - Inches
        weight (Union[None, Unset, float]):
        max_weight (Union[None, Unset, int]): Maximum load capacity for the rack
        weight_unit (Union[None, RackTypeRequestWeightUnitType1, RackTypeRequestWeightUnitType2Type1,
            RackTypeRequestWeightUnitType3Type1, Unset]): * `kg` - Kilograms
            * `g` - Grams
            * `lb` - Pounds
            * `oz` - Ounces
        mounting_depth (Union[None, Unset, int]): Maximum depth of a mounted device, in millimeters. For four-post
            racks, this is the distance between the front and rear rails.
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, RackTypeRequestCustomFields]):
    """

    manufacturer: Union["BriefManufacturerRequest", int]
    model: str
    slug: str
    description: Union[Unset, str] = UNSET
    form_factor: Union[
        None,
        RackTypeRequestFormFactorType1,
        RackTypeRequestFormFactorType2Type1,
        RackTypeRequestFormFactorType3Type1,
        Unset,
    ] = UNSET
    width: Union[Unset, RackTypeRequestWidth] = UNSET
    u_height: Union[Unset, int] = UNSET
    starting_unit: Union[Unset, int] = UNSET
    desc_units: Union[Unset, bool] = UNSET
    outer_width: Union[None, Unset, int] = UNSET
    outer_height: Union[None, Unset, int] = UNSET
    outer_depth: Union[None, Unset, int] = UNSET
    outer_unit: Union[
        None,
        RackTypeRequestOuterUnitType1,
        RackTypeRequestOuterUnitType2Type1,
        RackTypeRequestOuterUnitType3Type1,
        Unset,
    ] = UNSET
    weight: Union[None, Unset, float] = UNSET
    max_weight: Union[None, Unset, int] = UNSET
    weight_unit: Union[
        None,
        RackTypeRequestWeightUnitType1,
        RackTypeRequestWeightUnitType2Type1,
        RackTypeRequestWeightUnitType3Type1,
        Unset,
    ] = UNSET
    mounting_depth: Union[None, Unset, int] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "RackTypeRequestCustomFields"] = UNSET
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

        description = self.description

        form_factor: Union[None, Unset, str]
        if isinstance(self.form_factor, Unset):
            form_factor = UNSET
        elif isinstance(self.form_factor, RackTypeRequestFormFactorType1):
            form_factor = self.form_factor.value
        elif isinstance(self.form_factor, RackTypeRequestFormFactorType2Type1):
            form_factor = self.form_factor.value
        elif isinstance(self.form_factor, RackTypeRequestFormFactorType3Type1):
            form_factor = self.form_factor.value
        else:
            form_factor = self.form_factor

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
        elif isinstance(self.outer_unit, RackTypeRequestOuterUnitType1):
            outer_unit = self.outer_unit.value
        elif isinstance(self.outer_unit, RackTypeRequestOuterUnitType2Type1):
            outer_unit = self.outer_unit.value
        elif isinstance(self.outer_unit, RackTypeRequestOuterUnitType3Type1):
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
        elif isinstance(self.weight_unit, RackTypeRequestWeightUnitType1):
            weight_unit = self.weight_unit.value
        elif isinstance(self.weight_unit, RackTypeRequestWeightUnitType2Type1):
            weight_unit = self.weight_unit.value
        elif isinstance(self.weight_unit, RackTypeRequestWeightUnitType3Type1):
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
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if form_factor is not UNSET:
            field_dict["form_factor"] = form_factor
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
        from ..models.rack_type_request_custom_fields import RackTypeRequestCustomFields

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

        description = d.pop("description", UNSET)

        def _parse_form_factor(
            data: object,
        ) -> Union[
            None,
            RackTypeRequestFormFactorType1,
            RackTypeRequestFormFactorType2Type1,
            RackTypeRequestFormFactorType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                form_factor_type_1 = RackTypeRequestFormFactorType1(data)

                return form_factor_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                form_factor_type_2_type_1 = RackTypeRequestFormFactorType2Type1(data)

                return form_factor_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                form_factor_type_3_type_1 = RackTypeRequestFormFactorType3Type1(data)

                return form_factor_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    RackTypeRequestFormFactorType1,
                    RackTypeRequestFormFactorType2Type1,
                    RackTypeRequestFormFactorType3Type1,
                    Unset,
                ],
                data,
            )

        form_factor = _parse_form_factor(d.pop("form_factor", UNSET))

        _width = d.pop("width", UNSET)
        width: Union[Unset, RackTypeRequestWidth]
        if isinstance(_width, Unset):
            width = UNSET
        else:
            width = RackTypeRequestWidth(_width)

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
            RackTypeRequestOuterUnitType1,
            RackTypeRequestOuterUnitType2Type1,
            RackTypeRequestOuterUnitType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outer_unit_type_1 = RackTypeRequestOuterUnitType1(data)

                return outer_unit_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outer_unit_type_2_type_1 = RackTypeRequestOuterUnitType2Type1(data)

                return outer_unit_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outer_unit_type_3_type_1 = RackTypeRequestOuterUnitType3Type1(data)

                return outer_unit_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    RackTypeRequestOuterUnitType1,
                    RackTypeRequestOuterUnitType2Type1,
                    RackTypeRequestOuterUnitType3Type1,
                    Unset,
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
            RackTypeRequestWeightUnitType1,
            RackTypeRequestWeightUnitType2Type1,
            RackTypeRequestWeightUnitType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                weight_unit_type_1 = RackTypeRequestWeightUnitType1(data)

                return weight_unit_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                weight_unit_type_2_type_1 = RackTypeRequestWeightUnitType2Type1(data)

                return weight_unit_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                weight_unit_type_3_type_1 = RackTypeRequestWeightUnitType3Type1(data)

                return weight_unit_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    RackTypeRequestWeightUnitType1,
                    RackTypeRequestWeightUnitType2Type1,
                    RackTypeRequestWeightUnitType3Type1,
                    Unset,
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
        custom_fields: Union[Unset, RackTypeRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = RackTypeRequestCustomFields.from_dict(_custom_fields)

        rack_type_request = cls(
            manufacturer=manufacturer,
            model=model,
            slug=slug,
            description=description,
            form_factor=form_factor,
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

        rack_type_request.additional_properties = d
        return rack_type_request

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
