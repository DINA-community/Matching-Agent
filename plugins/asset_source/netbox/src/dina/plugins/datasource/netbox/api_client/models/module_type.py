import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_manufacturer import BriefManufacturer
    from ..models.brief_module_type_profile import BriefModuleTypeProfile
    from ..models.module_type_airflow_type_0 import ModuleTypeAirflowType0
    from ..models.module_type_custom_fields import ModuleTypeCustomFields
    from ..models.module_type_weight_unit_type_0 import ModuleTypeWeightUnitType0
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="ModuleType")


@_attrs_define
class ModuleType:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        manufacturer (BriefManufacturer): Adds support for custom fields and tags.
        model (str):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        profile (Union['BriefModuleTypeProfile', None, Unset]):
        part_number (Union[Unset, str]): Discrete part number (optional)
        airflow (Union['ModuleTypeAirflowType0', None, Unset]):
        weight (Union[None, Unset, float]):
        weight_unit (Union['ModuleTypeWeightUnitType0', None, Unset]):
        description (Union[Unset, str]):
        attributes (Union[Unset, Any]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, ModuleTypeCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    manufacturer: "BriefManufacturer"
    model: str
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    profile: Union["BriefModuleTypeProfile", None, Unset] = UNSET
    part_number: Union[Unset, str] = UNSET
    airflow: Union["ModuleTypeAirflowType0", None, Unset] = UNSET
    weight: Union[None, Unset, float] = UNSET
    weight_unit: Union["ModuleTypeWeightUnitType0", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    attributes: Union[Unset, Any] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "ModuleTypeCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_module_type_profile import BriefModuleTypeProfile
        from ..models.module_type_airflow_type_0 import ModuleTypeAirflowType0
        from ..models.module_type_weight_unit_type_0 import ModuleTypeWeightUnitType0

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        manufacturer = self.manufacturer.to_dict()

        model = self.model

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

        profile: Union[None, Unset, dict[str, Any]]
        if isinstance(self.profile, Unset):
            profile = UNSET
        elif isinstance(self.profile, BriefModuleTypeProfile):
            profile = self.profile.to_dict()
        else:
            profile = self.profile

        part_number = self.part_number

        airflow: Union[None, Unset, dict[str, Any]]
        if isinstance(self.airflow, Unset):
            airflow = UNSET
        elif isinstance(self.airflow, ModuleTypeAirflowType0):
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
        elif isinstance(self.weight_unit, ModuleTypeWeightUnitType0):
            weight_unit = self.weight_unit.to_dict()
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
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "manufacturer": manufacturer,
                "model": model,
                "created": created,
                "last_updated": last_updated,
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
        from ..models.brief_manufacturer import BriefManufacturer
        from ..models.brief_module_type_profile import BriefModuleTypeProfile
        from ..models.module_type_airflow_type_0 import ModuleTypeAirflowType0
        from ..models.module_type_custom_fields import ModuleTypeCustomFields
        from ..models.module_type_weight_unit_type_0 import ModuleTypeWeightUnitType0
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        manufacturer = BriefManufacturer.from_dict(d.pop("manufacturer"))

        model = d.pop("model")

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

        def _parse_profile(
            data: object,
        ) -> Union["BriefModuleTypeProfile", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                profile_type_1 = BriefModuleTypeProfile.from_dict(data)

                return profile_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefModuleTypeProfile", None, Unset], data)

        profile = _parse_profile(d.pop("profile", UNSET))

        part_number = d.pop("part_number", UNSET)

        def _parse_airflow(
            data: object,
        ) -> Union["ModuleTypeAirflowType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                airflow_type_0 = ModuleTypeAirflowType0.from_dict(data)

                return airflow_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModuleTypeAirflowType0", None, Unset], data)

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
        ) -> Union["ModuleTypeWeightUnitType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                weight_unit_type_0 = ModuleTypeWeightUnitType0.from_dict(data)

                return weight_unit_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModuleTypeWeightUnitType0", None, Unset], data)

        weight_unit = _parse_weight_unit(d.pop("weight_unit", UNSET))

        description = d.pop("description", UNSET)

        attributes = d.pop("attributes", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, ModuleTypeCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ModuleTypeCustomFields.from_dict(_custom_fields)

        module_type = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            manufacturer=manufacturer,
            model=model,
            created=created,
            last_updated=last_updated,
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

        module_type.additional_properties = d
        return module_type

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
