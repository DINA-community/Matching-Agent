import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_location import BriefLocation
    from ..models.brief_rack_role import BriefRackRole
    from ..models.brief_rack_type import BriefRackType
    from ..models.brief_site import BriefSite
    from ..models.brief_tenant import BriefTenant
    from ..models.nested_tag import NestedTag
    from ..models.rack_airflow import RackAirflow
    from ..models.rack_custom_fields import RackCustomFields
    from ..models.rack_form_factor_type_0 import RackFormFactorType0
    from ..models.rack_outer_unit_type_0 import RackOuterUnitType0
    from ..models.rack_status import RackStatus
    from ..models.rack_weight_unit_type_0 import RackWeightUnitType0
    from ..models.rack_width import RackWidth


T = TypeVar("T", bound="Rack")


@_attrs_define
class Rack:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        name (str):
        site (BriefSite): Adds support for custom fields and tags.
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        powerfeed_count (int):
        facility_id (Union[None, Unset, str]):
        location (Union['BriefLocation', None, Unset]):
        tenant (Union['BriefTenant', None, Unset]):
        status (Union[Unset, RackStatus]):
        role (Union['BriefRackRole', None, Unset]):
        serial (Union[Unset, str]):
        asset_tag (Union[None, Unset, str]): A unique tag used to identify this rack
        rack_type (Union['BriefRackType', None, Unset]):
        form_factor (Union['RackFormFactorType0', None, Unset]):
        width (Union[Unset, RackWidth]):
        u_height (Union[Unset, int]): Height in rack units
        starting_unit (Union[Unset, int]): Starting unit for rack
        weight (Union[None, Unset, float]):
        max_weight (Union[None, Unset, int]): Maximum load capacity for the rack
        weight_unit (Union['RackWeightUnitType0', None, Unset]):
        desc_units (Union[Unset, bool]): Units are numbered top-to-bottom
        outer_width (Union[None, Unset, int]): Outer dimension of rack (width)
        outer_height (Union[None, Unset, int]): Outer dimension of rack (height)
        outer_depth (Union[None, Unset, int]): Outer dimension of rack (depth)
        outer_unit (Union['RackOuterUnitType0', None, Unset]):
        mounting_depth (Union[None, Unset, int]): Maximum depth of a mounted device, in millimeters. For four-post
            racks, this is the distance between the front and rear rails.
        airflow (Union[Unset, RackAirflow]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, RackCustomFields]):
        device_count (Union[Unset, int]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    site: "BriefSite"
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    powerfeed_count: int
    facility_id: Union[None, Unset, str] = UNSET
    location: Union["BriefLocation", None, Unset] = UNSET
    tenant: Union["BriefTenant", None, Unset] = UNSET
    status: Union[Unset, "RackStatus"] = UNSET
    role: Union["BriefRackRole", None, Unset] = UNSET
    serial: Union[Unset, str] = UNSET
    asset_tag: Union[None, Unset, str] = UNSET
    rack_type: Union["BriefRackType", None, Unset] = UNSET
    form_factor: Union["RackFormFactorType0", None, Unset] = UNSET
    width: Union[Unset, "RackWidth"] = UNSET
    u_height: Union[Unset, int] = UNSET
    starting_unit: Union[Unset, int] = UNSET
    weight: Union[None, Unset, float] = UNSET
    max_weight: Union[None, Unset, int] = UNSET
    weight_unit: Union["RackWeightUnitType0", None, Unset] = UNSET
    desc_units: Union[Unset, bool] = UNSET
    outer_width: Union[None, Unset, int] = UNSET
    outer_height: Union[None, Unset, int] = UNSET
    outer_depth: Union[None, Unset, int] = UNSET
    outer_unit: Union["RackOuterUnitType0", None, Unset] = UNSET
    mounting_depth: Union[None, Unset, int] = UNSET
    airflow: Union[Unset, "RackAirflow"] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "RackCustomFields"] = UNSET
    device_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_location import BriefLocation
        from ..models.brief_rack_role import BriefRackRole
        from ..models.brief_rack_type import BriefRackType
        from ..models.brief_tenant import BriefTenant
        from ..models.rack_form_factor_type_0 import RackFormFactorType0
        from ..models.rack_outer_unit_type_0 import RackOuterUnitType0
        from ..models.rack_weight_unit_type_0 import RackWeightUnitType0

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

        site = self.site.to_dict()

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

        powerfeed_count = self.powerfeed_count

        facility_id: Union[None, Unset, str]
        if isinstance(self.facility_id, Unset):
            facility_id = UNSET
        else:
            facility_id = self.facility_id

        location: Union[None, Unset, dict[str, Any]]
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, BriefLocation):
            location = self.location.to_dict()
        else:
            location = self.location

        tenant: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenant):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        role: Union[None, Unset, dict[str, Any]]
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, BriefRackRole):
            role = self.role.to_dict()
        else:
            role = self.role

        serial = self.serial

        asset_tag: Union[None, Unset, str]
        if isinstance(self.asset_tag, Unset):
            asset_tag = UNSET
        else:
            asset_tag = self.asset_tag

        rack_type: Union[None, Unset, dict[str, Any]]
        if isinstance(self.rack_type, Unset):
            rack_type = UNSET
        elif isinstance(self.rack_type, BriefRackType):
            rack_type = self.rack_type.to_dict()
        else:
            rack_type = self.rack_type

        form_factor: Union[None, Unset, dict[str, Any]]
        if isinstance(self.form_factor, Unset):
            form_factor = UNSET
        elif isinstance(self.form_factor, RackFormFactorType0):
            form_factor = self.form_factor.to_dict()
        else:
            form_factor = self.form_factor

        width: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.width, Unset):
            width = self.width.to_dict()

        u_height = self.u_height

        starting_unit = self.starting_unit

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
        elif isinstance(self.weight_unit, RackWeightUnitType0):
            weight_unit = self.weight_unit.to_dict()
        else:
            weight_unit = self.weight_unit

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
        elif isinstance(self.outer_unit, RackOuterUnitType0):
            outer_unit = self.outer_unit.to_dict()
        else:
            outer_unit = self.outer_unit

        mounting_depth: Union[None, Unset, int]
        if isinstance(self.mounting_depth, Unset):
            mounting_depth = UNSET
        else:
            mounting_depth = self.mounting_depth

        airflow: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.airflow, Unset):
            airflow = self.airflow.to_dict()

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
                "name": name,
                "site": site,
                "created": created,
                "last_updated": last_updated,
                "powerfeed_count": powerfeed_count,
            }
        )
        if facility_id is not UNSET:
            field_dict["facility_id"] = facility_id
        if location is not UNSET:
            field_dict["location"] = location
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if status is not UNSET:
            field_dict["status"] = status
        if role is not UNSET:
            field_dict["role"] = role
        if serial is not UNSET:
            field_dict["serial"] = serial
        if asset_tag is not UNSET:
            field_dict["asset_tag"] = asset_tag
        if rack_type is not UNSET:
            field_dict["rack_type"] = rack_type
        if form_factor is not UNSET:
            field_dict["form_factor"] = form_factor
        if width is not UNSET:
            field_dict["width"] = width
        if u_height is not UNSET:
            field_dict["u_height"] = u_height
        if starting_unit is not UNSET:
            field_dict["starting_unit"] = starting_unit
        if weight is not UNSET:
            field_dict["weight"] = weight
        if max_weight is not UNSET:
            field_dict["max_weight"] = max_weight
        if weight_unit is not UNSET:
            field_dict["weight_unit"] = weight_unit
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
        if mounting_depth is not UNSET:
            field_dict["mounting_depth"] = mounting_depth
        if airflow is not UNSET:
            field_dict["airflow"] = airflow
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
        from ..models.brief_location import BriefLocation
        from ..models.brief_rack_role import BriefRackRole
        from ..models.brief_rack_type import BriefRackType
        from ..models.brief_site import BriefSite
        from ..models.brief_tenant import BriefTenant
        from ..models.nested_tag import NestedTag
        from ..models.rack_airflow import RackAirflow
        from ..models.rack_custom_fields import RackCustomFields
        from ..models.rack_form_factor_type_0 import RackFormFactorType0
        from ..models.rack_outer_unit_type_0 import RackOuterUnitType0
        from ..models.rack_status import RackStatus
        from ..models.rack_weight_unit_type_0 import RackWeightUnitType0
        from ..models.rack_width import RackWidth

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

        site = BriefSite.from_dict(d.pop("site"))

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

        powerfeed_count = d.pop("powerfeed_count")

        def _parse_facility_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        facility_id = _parse_facility_id(d.pop("facility_id", UNSET))

        def _parse_location(data: object) -> Union["BriefLocation", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_1 = BriefLocation.from_dict(data)

                return location_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefLocation", None, Unset], data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_tenant(data: object) -> Union["BriefTenant", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tenant_type_1 = BriefTenant.from_dict(data)

                return tenant_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefTenant", None, Unset], data)

        tenant = _parse_tenant(d.pop("tenant", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, RackStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RackStatus.from_dict(_status)

        def _parse_role(data: object) -> Union["BriefRackRole", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                role_type_1 = BriefRackRole.from_dict(data)

                return role_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefRackRole", None, Unset], data)

        role = _parse_role(d.pop("role", UNSET))

        serial = d.pop("serial", UNSET)

        def _parse_asset_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_tag = _parse_asset_tag(d.pop("asset_tag", UNSET))

        def _parse_rack_type(data: object) -> Union["BriefRackType", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rack_type_type_1 = BriefRackType.from_dict(data)

                return rack_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefRackType", None, Unset], data)

        rack_type = _parse_rack_type(d.pop("rack_type", UNSET))

        def _parse_form_factor(
            data: object,
        ) -> Union["RackFormFactorType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                form_factor_type_0 = RackFormFactorType0.from_dict(data)

                return form_factor_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RackFormFactorType0", None, Unset], data)

        form_factor = _parse_form_factor(d.pop("form_factor", UNSET))

        _width = d.pop("width", UNSET)
        width: Union[Unset, RackWidth]
        if isinstance(_width, Unset):
            width = UNSET
        else:
            width = RackWidth.from_dict(_width)

        u_height = d.pop("u_height", UNSET)

        starting_unit = d.pop("starting_unit", UNSET)

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
        ) -> Union["RackWeightUnitType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                weight_unit_type_0 = RackWeightUnitType0.from_dict(data)

                return weight_unit_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RackWeightUnitType0", None, Unset], data)

        weight_unit = _parse_weight_unit(d.pop("weight_unit", UNSET))

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

        def _parse_outer_unit(data: object) -> Union["RackOuterUnitType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                outer_unit_type_0 = RackOuterUnitType0.from_dict(data)

                return outer_unit_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RackOuterUnitType0", None, Unset], data)

        outer_unit = _parse_outer_unit(d.pop("outer_unit", UNSET))

        def _parse_mounting_depth(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        mounting_depth = _parse_mounting_depth(d.pop("mounting_depth", UNSET))

        _airflow = d.pop("airflow", UNSET)
        airflow: Union[Unset, RackAirflow]
        if isinstance(_airflow, Unset):
            airflow = UNSET
        else:
            airflow = RackAirflow.from_dict(_airflow)

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, RackCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = RackCustomFields.from_dict(_custom_fields)

        device_count = d.pop("device_count", UNSET)

        rack = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            site=site,
            created=created,
            last_updated=last_updated,
            powerfeed_count=powerfeed_count,
            facility_id=facility_id,
            location=location,
            tenant=tenant,
            status=status,
            role=role,
            serial=serial,
            asset_tag=asset_tag,
            rack_type=rack_type,
            form_factor=form_factor,
            width=width,
            u_height=u_height,
            starting_unit=starting_unit,
            weight=weight,
            max_weight=max_weight,
            weight_unit=weight_unit,
            desc_units=desc_units,
            outer_width=outer_width,
            outer_height=outer_height,
            outer_depth=outer_depth,
            outer_unit=outer_unit,
            mounting_depth=mounting_depth,
            airflow=airflow,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
            device_count=device_count,
        )

        rack.additional_properties = d
        return rack

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
