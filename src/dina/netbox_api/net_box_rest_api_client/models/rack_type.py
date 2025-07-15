import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_manufacturer import BriefManufacturer
    from ..models.nested_tag import NestedTag
    from ..models.rack_type_custom_fields import RackTypeCustomFields
    from ..models.rack_type_form_factor_type_0 import RackTypeFormFactorType0
    from ..models.rack_type_outer_unit_type_0 import RackTypeOuterUnitType0
    from ..models.rack_type_weight_unit_type_0 import RackTypeWeightUnitType0
    from ..models.rack_type_width import RackTypeWidth


T = TypeVar("T", bound="RackType")


@_attrs_define
class RackType:
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
        description (Union[Unset, str]):
        form_factor (Union['RackTypeFormFactorType0', None, Unset]):
        width (Union[Unset, RackTypeWidth]):
        u_height (Union[Unset, int]): Height in rack units
        starting_unit (Union[Unset, int]): Starting unit for rack
        desc_units (Union[Unset, bool]): Units are numbered top-to-bottom
        outer_width (Union[None, Unset, int]): Outer dimension of rack (width)
        outer_height (Union[None, Unset, int]): Outer dimension of rack (height)
        outer_depth (Union[None, Unset, int]): Outer dimension of rack (depth)
        outer_unit (Union['RackTypeOuterUnitType0', None, Unset]):
        weight (Union[None, Unset, float]):
        max_weight (Union[None, Unset, int]): Maximum load capacity for the rack
        weight_unit (Union['RackTypeWeightUnitType0', None, Unset]):
        mounting_depth (Union[None, Unset, int]): Maximum depth of a mounted device, in millimeters. For four-post
            racks, this is the distance between the front and rear rails.
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, RackTypeCustomFields]):
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
    description: Union[Unset, str] = UNSET
    form_factor: Union["RackTypeFormFactorType0", None, Unset] = UNSET
    width: Union[Unset, "RackTypeWidth"] = UNSET
    u_height: Union[Unset, int] = UNSET
    starting_unit: Union[Unset, int] = UNSET
    desc_units: Union[Unset, bool] = UNSET
    outer_width: Union[None, Unset, int] = UNSET
    outer_height: Union[None, Unset, int] = UNSET
    outer_depth: Union[None, Unset, int] = UNSET
    outer_unit: Union["RackTypeOuterUnitType0", None, Unset] = UNSET
    weight: Union[None, Unset, float] = UNSET
    max_weight: Union[None, Unset, int] = UNSET
    weight_unit: Union["RackTypeWeightUnitType0", None, Unset] = UNSET
    mounting_depth: Union[None, Unset, int] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "RackTypeCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rack_type_form_factor_type_0 import RackTypeFormFactorType0
        from ..models.rack_type_outer_unit_type_0 import RackTypeOuterUnitType0
        from ..models.rack_type_weight_unit_type_0 import RackTypeWeightUnitType0

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

        description = self.description

        form_factor: Union[None, Unset, dict[str, Any]]
        if isinstance(self.form_factor, Unset):
            form_factor = UNSET
        elif isinstance(self.form_factor, RackTypeFormFactorType0):
            form_factor = self.form_factor.to_dict()
        else:
            form_factor = self.form_factor

        width: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.width, Unset):
            width = self.width.to_dict()

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

        outer_unit: Union[None, Unset, dict[str, Any]]
        if isinstance(self.outer_unit, Unset):
            outer_unit = UNSET
        elif isinstance(self.outer_unit, RackTypeOuterUnitType0):
            outer_unit = self.outer_unit.to_dict()
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

        weight_unit: Union[None, Unset, dict[str, Any]]
        if isinstance(self.weight_unit, Unset):
            weight_unit = UNSET
        elif isinstance(self.weight_unit, RackTypeWeightUnitType0):
            weight_unit = self.weight_unit.to_dict()
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
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "manufacturer": manufacturer,
                "model": model,
                "slug": slug,
                "created": created,
                "last_updated": last_updated,
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
        from ..models.brief_manufacturer import BriefManufacturer
        from ..models.nested_tag import NestedTag
        from ..models.rack_type_custom_fields import RackTypeCustomFields
        from ..models.rack_type_form_factor_type_0 import RackTypeFormFactorType0
        from ..models.rack_type_outer_unit_type_0 import RackTypeOuterUnitType0
        from ..models.rack_type_weight_unit_type_0 import RackTypeWeightUnitType0
        from ..models.rack_type_width import RackTypeWidth

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

        description = d.pop("description", UNSET)

        def _parse_form_factor(data: object) -> Union["RackTypeFormFactorType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                form_factor_type_0 = RackTypeFormFactorType0.from_dict(data)

                return form_factor_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RackTypeFormFactorType0", None, Unset], data)

        form_factor = _parse_form_factor(d.pop("form_factor", UNSET))

        _width = d.pop("width", UNSET)
        width: Union[Unset, RackTypeWidth]
        if isinstance(_width, Unset):
            width = UNSET
        else:
            width = RackTypeWidth.from_dict(_width)

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

        def _parse_outer_unit(data: object) -> Union["RackTypeOuterUnitType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                outer_unit_type_0 = RackTypeOuterUnitType0.from_dict(data)

                return outer_unit_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RackTypeOuterUnitType0", None, Unset], data)

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

        def _parse_weight_unit(data: object) -> Union["RackTypeWeightUnitType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                weight_unit_type_0 = RackTypeWeightUnitType0.from_dict(data)

                return weight_unit_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RackTypeWeightUnitType0", None, Unset], data)

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
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, RackTypeCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = RackTypeCustomFields.from_dict(_custom_fields)

        rack_type = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            manufacturer=manufacturer,
            model=model,
            slug=slug,
            created=created,
            last_updated=last_updated,
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

        rack_type.additional_properties = d
        return rack_type

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
