import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_module_type_request_airflow_type_1 import (
    WritableModuleTypeRequestAirflowType1,
)
from ..models.writable_module_type_request_airflow_type_2_type_1 import (
    WritableModuleTypeRequestAirflowType2Type1,
)
from ..models.writable_module_type_request_airflow_type_3_type_1 import (
    WritableModuleTypeRequestAirflowType3Type1,
)
from ..models.writable_module_type_request_weight_unit_type_1 import (
    WritableModuleTypeRequestWeightUnitType1,
)
from ..models.writable_module_type_request_weight_unit_type_2_type_1 import (
    WritableModuleTypeRequestWeightUnitType2Type1,
)
from ..models.writable_module_type_request_weight_unit_type_3_type_1 import (
    WritableModuleTypeRequestWeightUnitType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_manufacturer_request import BriefManufacturerRequest
    from ..models.brief_module_type_profile_request import BriefModuleTypeProfileRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.writable_module_type_request_custom_fields import (
        WritableModuleTypeRequestCustomFields,
    )


T = TypeVar("T", bound="WritableModuleTypeRequest")


@_attrs_define
class WritableModuleTypeRequest:
    """Adds support for custom fields and tags.

    Attributes:
        manufacturer (Union['BriefManufacturerRequest', int]):
        model (str):
        profile (Union['BriefModuleTypeProfileRequest', None, Unset, int]):
        part_number (Union[Unset, str]): Discrete part number (optional)
        airflow (Union[None, Unset, WritableModuleTypeRequestAirflowType1, WritableModuleTypeRequestAirflowType2Type1,
            WritableModuleTypeRequestAirflowType3Type1]): * `front-to-rear` - Front to rear
            * `rear-to-front` - Rear to front
            * `left-to-right` - Left to right
            * `right-to-left` - Right to left
            * `side-to-rear` - Side to rear
            * `passive` - Passive
        weight (Union[None, Unset, float]):
        weight_unit (Union[None, Unset, WritableModuleTypeRequestWeightUnitType1,
            WritableModuleTypeRequestWeightUnitType2Type1, WritableModuleTypeRequestWeightUnitType3Type1]): * `kg` -
            Kilograms
            * `g` - Grams
            * `lb` - Pounds
            * `oz` - Ounces
        description (Union[Unset, str]):
        attributes (Union[Unset, Any]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WritableModuleTypeRequestCustomFields]):
    """

    manufacturer: Union["BriefManufacturerRequest", int]
    model: str
    profile: Union["BriefModuleTypeProfileRequest", None, Unset, int] = UNSET
    part_number: Union[Unset, str] = UNSET
    airflow: Union[
        None,
        Unset,
        WritableModuleTypeRequestAirflowType1,
        WritableModuleTypeRequestAirflowType2Type1,
        WritableModuleTypeRequestAirflowType3Type1,
    ] = UNSET
    weight: Union[None, Unset, float] = UNSET
    weight_unit: Union[
        None,
        Unset,
        WritableModuleTypeRequestWeightUnitType1,
        WritableModuleTypeRequestWeightUnitType2Type1,
        WritableModuleTypeRequestWeightUnitType3Type1,
    ] = UNSET
    description: Union[Unset, str] = UNSET
    attributes: Union[Unset, Any] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WritableModuleTypeRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_manufacturer_request import BriefManufacturerRequest
        from ..models.brief_module_type_profile_request import (
            BriefModuleTypeProfileRequest,
        )

        manufacturer: Union[dict[str, Any], int]
        if isinstance(self.manufacturer, BriefManufacturerRequest):
            manufacturer = self.manufacturer.to_dict()
        else:
            manufacturer = self.manufacturer

        model = self.model

        profile: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.profile, Unset):
            profile = UNSET
        elif isinstance(self.profile, BriefModuleTypeProfileRequest):
            profile = self.profile.to_dict()
        else:
            profile = self.profile

        part_number = self.part_number

        airflow: Union[None, Unset, str]
        if isinstance(self.airflow, Unset):
            airflow = UNSET
        elif isinstance(self.airflow, WritableModuleTypeRequestAirflowType1):
            airflow = self.airflow.value
        elif isinstance(self.airflow, WritableModuleTypeRequestAirflowType2Type1):
            airflow = self.airflow.value
        elif isinstance(self.airflow, WritableModuleTypeRequestAirflowType3Type1):
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
        elif isinstance(self.weight_unit, WritableModuleTypeRequestWeightUnitType1):
            weight_unit = self.weight_unit.value
        elif isinstance(
            self.weight_unit, WritableModuleTypeRequestWeightUnitType2Type1
        ):
            weight_unit = self.weight_unit.value
        elif isinstance(
            self.weight_unit, WritableModuleTypeRequestWeightUnitType3Type1
        ):
            weight_unit = self.weight_unit.value
        else:
            weight_unit = self.weight_unit

        description = self.description

        attributes = self.attributes

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
            }
        )
        if profile is not UNSET:
            field_dict["profile"] = profile
        if part_number is not UNSET:
            field_dict["part_number"] = part_number
        if airflow is not UNSET:
            field_dict["airflow"] = airflow
        if weight is not UNSET:
            field_dict["weight"] = weight
        if weight_unit is not UNSET:
            field_dict["weight_unit"] = weight_unit
        if description is not UNSET:
            field_dict["description"] = description
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
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

        profile: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.profile, Unset):
            profile = UNSET
        elif isinstance(self.profile, int):
            profile = (None, str(self.profile).encode(), "text/plain")
        elif isinstance(self.profile, None):
            profile = (None, str(self.profile).encode(), "text/plain")
        elif isinstance(self.profile, BriefModuleTypeProfileRequest):
            profile = (
                None,
                json.dumps(self.profile.to_dict()).encode(),
                "application/json",
            )
        else:
            profile = (None, str(self.profile).encode(), "text/plain")

        part_number = (
            self.part_number
            if isinstance(self.part_number, Unset)
            else (None, str(self.part_number).encode(), "text/plain")
        )

        airflow: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.airflow, Unset):
            airflow = UNSET
        elif isinstance(self.airflow, None):
            airflow = (None, str(self.airflow).encode(), "text/plain")
        elif isinstance(self.airflow, WritableModuleTypeRequestAirflowType1):
            airflow = (None, str(self.airflow.value).encode(), "text/plain")
        elif isinstance(self.airflow, None):
            airflow = (None, str(self.airflow).encode(), "text/plain")
        elif isinstance(self.airflow, WritableModuleTypeRequestAirflowType2Type1):
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
        elif isinstance(self.weight_unit, WritableModuleTypeRequestWeightUnitType1):
            weight_unit = (None, str(self.weight_unit.value).encode(), "text/plain")
        elif isinstance(self.weight_unit, None):
            weight_unit = (None, str(self.weight_unit).encode(), "text/plain")
        elif isinstance(
            self.weight_unit, WritableModuleTypeRequestWeightUnitType2Type1
        ):
            weight_unit = (None, str(self.weight_unit.value).encode(), "text/plain")
        elif isinstance(self.weight_unit, None):
            weight_unit = (None, str(self.weight_unit).encode(), "text/plain")
        else:
            weight_unit = (None, str(self.weight_unit.value).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        attributes = (
            self.attributes
            if isinstance(self.attributes, Unset)
            else (None, str(self.attributes).encode(), "text/plain")
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
            }
        )
        if profile is not UNSET:
            field_dict["profile"] = profile
        if part_number is not UNSET:
            field_dict["part_number"] = part_number
        if airflow is not UNSET:
            field_dict["airflow"] = airflow
        if weight is not UNSET:
            field_dict["weight"] = weight
        if weight_unit is not UNSET:
            field_dict["weight_unit"] = weight_unit
        if description is not UNSET:
            field_dict["description"] = description
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
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
        from ..models.brief_module_type_profile_request import (
            BriefModuleTypeProfileRequest,
        )
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.writable_module_type_request_custom_fields import (
            WritableModuleTypeRequestCustomFields,
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

        def _parse_profile(
            data: object,
        ) -> Union["BriefModuleTypeProfileRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                profile_type_1_type_1 = BriefModuleTypeProfileRequest.from_dict(data)

                return profile_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefModuleTypeProfileRequest", None, Unset, int], data)

        profile = _parse_profile(d.pop("profile", UNSET))

        part_number = d.pop("part_number", UNSET)

        def _parse_airflow(
            data: object,
        ) -> Union[
            None,
            Unset,
            WritableModuleTypeRequestAirflowType1,
            WritableModuleTypeRequestAirflowType2Type1,
            WritableModuleTypeRequestAirflowType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                airflow_type_1 = WritableModuleTypeRequestAirflowType1(data)

                return airflow_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                airflow_type_2_type_1 = WritableModuleTypeRequestAirflowType2Type1(data)

                return airflow_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                airflow_type_3_type_1 = WritableModuleTypeRequestAirflowType3Type1(data)

                return airflow_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    WritableModuleTypeRequestAirflowType1,
                    WritableModuleTypeRequestAirflowType2Type1,
                    WritableModuleTypeRequestAirflowType3Type1,
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
            WritableModuleTypeRequestWeightUnitType1,
            WritableModuleTypeRequestWeightUnitType2Type1,
            WritableModuleTypeRequestWeightUnitType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                weight_unit_type_1 = WritableModuleTypeRequestWeightUnitType1(data)

                return weight_unit_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                weight_unit_type_2_type_1 = (
                    WritableModuleTypeRequestWeightUnitType2Type1(data)
                )

                return weight_unit_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                weight_unit_type_3_type_1 = (
                    WritableModuleTypeRequestWeightUnitType3Type1(data)
                )

                return weight_unit_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    WritableModuleTypeRequestWeightUnitType1,
                    WritableModuleTypeRequestWeightUnitType2Type1,
                    WritableModuleTypeRequestWeightUnitType3Type1,
                ],
                data,
            )

        weight_unit = _parse_weight_unit(d.pop("weight_unit", UNSET))

        description = d.pop("description", UNSET)

        attributes = d.pop("attributes", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WritableModuleTypeRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WritableModuleTypeRequestCustomFields.from_dict(
                _custom_fields
            )

        writable_module_type_request = cls(
            manufacturer=manufacturer,
            model=model,
            profile=profile,
            part_number=part_number,
            airflow=airflow,
            weight=weight,
            weight_unit=weight_unit,
            description=description,
            attributes=attributes,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        writable_module_type_request.additional_properties = d
        return writable_module_type_request

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
