import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_rack_request_airflow_type_1 import WritableRackRequestAirflowType1
from ..models.writable_rack_request_airflow_type_2_type_1 import WritableRackRequestAirflowType2Type1
from ..models.writable_rack_request_airflow_type_3_type_1 import WritableRackRequestAirflowType3Type1
from ..models.writable_rack_request_form_factor_type_1 import WritableRackRequestFormFactorType1
from ..models.writable_rack_request_form_factor_type_2_type_1 import WritableRackRequestFormFactorType2Type1
from ..models.writable_rack_request_form_factor_type_3_type_1 import WritableRackRequestFormFactorType3Type1
from ..models.writable_rack_request_outer_unit_type_1 import WritableRackRequestOuterUnitType1
from ..models.writable_rack_request_outer_unit_type_2_type_1 import WritableRackRequestOuterUnitType2Type1
from ..models.writable_rack_request_outer_unit_type_3_type_1 import WritableRackRequestOuterUnitType3Type1
from ..models.writable_rack_request_status import WritableRackRequestStatus
from ..models.writable_rack_request_weight_unit_type_1 import WritableRackRequestWeightUnitType1
from ..models.writable_rack_request_weight_unit_type_2_type_1 import WritableRackRequestWeightUnitType2Type1
from ..models.writable_rack_request_weight_unit_type_3_type_1 import WritableRackRequestWeightUnitType3Type1
from ..models.writable_rack_request_width import WritableRackRequestWidth
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_location_request import BriefLocationRequest
    from ..models.brief_rack_role_request import BriefRackRoleRequest
    from ..models.brief_rack_type_request import BriefRackTypeRequest
    from ..models.brief_site_request import BriefSiteRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.writable_rack_request_custom_fields import WritableRackRequestCustomFields


T = TypeVar("T", bound="WritableRackRequest")


@_attrs_define
class WritableRackRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str):
        site (Union['BriefSiteRequest', int]):
        facility_id (Union[None, Unset, str]):
        location (Union['BriefLocationRequest', None, Unset, int]):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        status (Union[Unset, WritableRackRequestStatus]): * `reserved` - Reserved
            * `available` - Available
            * `planned` - Planned
            * `active` - Active
            * `deprecated` - Deprecated
        role (Union['BriefRackRoleRequest', None, Unset, int]):
        serial (Union[Unset, str]):
        asset_tag (Union[None, Unset, str]): A unique tag used to identify this rack
        rack_type (Union['BriefRackTypeRequest', None, Unset, int]):
        form_factor (Union[None, Unset, WritableRackRequestFormFactorType1, WritableRackRequestFormFactorType2Type1,
            WritableRackRequestFormFactorType3Type1]): * `2-post-frame` - 2-post frame
            * `4-post-frame` - 4-post frame
            * `4-post-cabinet` - 4-post cabinet
            * `wall-frame` - Wall-mounted frame
            * `wall-frame-vertical` - Wall-mounted frame (vertical)
            * `wall-cabinet` - Wall-mounted cabinet
            * `wall-cabinet-vertical` - Wall-mounted cabinet (vertical)
        width (Union[Unset, WritableRackRequestWidth]): Rail-to-rail width

            * `10` - 10 inches
            * `19` - 19 inches
            * `21` - 21 inches
            * `23` - 23 inches
        u_height (Union[Unset, int]): Height in rack units
        starting_unit (Union[Unset, int]): Starting unit for rack
        weight (Union[None, Unset, float]):
        max_weight (Union[None, Unset, int]): Maximum load capacity for the rack
        weight_unit (Union[None, Unset, WritableRackRequestWeightUnitType1, WritableRackRequestWeightUnitType2Type1,
            WritableRackRequestWeightUnitType3Type1]): * `kg` - Kilograms
            * `g` - Grams
            * `lb` - Pounds
            * `oz` - Ounces
        desc_units (Union[Unset, bool]): Units are numbered top-to-bottom
        outer_width (Union[None, Unset, int]): Outer dimension of rack (width)
        outer_height (Union[None, Unset, int]): Outer dimension of rack (height)
        outer_depth (Union[None, Unset, int]): Outer dimension of rack (depth)
        outer_unit (Union[None, Unset, WritableRackRequestOuterUnitType1, WritableRackRequestOuterUnitType2Type1,
            WritableRackRequestOuterUnitType3Type1]): * `mm` - Millimeters
            * `in` - Inches
        mounting_depth (Union[None, Unset, int]): Maximum depth of a mounted device, in millimeters. For four-post
            racks, this is the distance between the front and rear rails.
        airflow (Union[None, Unset, WritableRackRequestAirflowType1, WritableRackRequestAirflowType2Type1,
            WritableRackRequestAirflowType3Type1]): * `front-to-rear` - Front to rear
            * `rear-to-front` - Rear to front
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WritableRackRequestCustomFields]):
    """

    name: str
    site: Union["BriefSiteRequest", int]
    facility_id: Union[None, Unset, str] = UNSET
    location: Union["BriefLocationRequest", None, Unset, int] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    status: Union[Unset, WritableRackRequestStatus] = UNSET
    role: Union["BriefRackRoleRequest", None, Unset, int] = UNSET
    serial: Union[Unset, str] = UNSET
    asset_tag: Union[None, Unset, str] = UNSET
    rack_type: Union["BriefRackTypeRequest", None, Unset, int] = UNSET
    form_factor: Union[
        None,
        Unset,
        WritableRackRequestFormFactorType1,
        WritableRackRequestFormFactorType2Type1,
        WritableRackRequestFormFactorType3Type1,
    ] = UNSET
    width: Union[Unset, WritableRackRequestWidth] = UNSET
    u_height: Union[Unset, int] = UNSET
    starting_unit: Union[Unset, int] = UNSET
    weight: Union[None, Unset, float] = UNSET
    max_weight: Union[None, Unset, int] = UNSET
    weight_unit: Union[
        None,
        Unset,
        WritableRackRequestWeightUnitType1,
        WritableRackRequestWeightUnitType2Type1,
        WritableRackRequestWeightUnitType3Type1,
    ] = UNSET
    desc_units: Union[Unset, bool] = UNSET
    outer_width: Union[None, Unset, int] = UNSET
    outer_height: Union[None, Unset, int] = UNSET
    outer_depth: Union[None, Unset, int] = UNSET
    outer_unit: Union[
        None,
        Unset,
        WritableRackRequestOuterUnitType1,
        WritableRackRequestOuterUnitType2Type1,
        WritableRackRequestOuterUnitType3Type1,
    ] = UNSET
    mounting_depth: Union[None, Unset, int] = UNSET
    airflow: Union[
        None,
        Unset,
        WritableRackRequestAirflowType1,
        WritableRackRequestAirflowType2Type1,
        WritableRackRequestAirflowType3Type1,
    ] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WritableRackRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_location_request import BriefLocationRequest
        from ..models.brief_rack_role_request import BriefRackRoleRequest
        from ..models.brief_rack_type_request import BriefRackTypeRequest
        from ..models.brief_site_request import BriefSiteRequest
        from ..models.brief_tenant_request import BriefTenantRequest

        name = self.name

        site: Union[dict[str, Any], int]
        if isinstance(self.site, BriefSiteRequest):
            site = self.site.to_dict()
        else:
            site = self.site

        facility_id: Union[None, Unset, str]
        if isinstance(self.facility_id, Unset):
            facility_id = UNSET
        else:
            facility_id = self.facility_id

        location: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, BriefLocationRequest):
            location = self.location.to_dict()
        else:
            location = self.location

        tenant: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenantRequest):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        role: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, BriefRackRoleRequest):
            role = self.role.to_dict()
        else:
            role = self.role

        serial = self.serial

        asset_tag: Union[None, Unset, str]
        if isinstance(self.asset_tag, Unset):
            asset_tag = UNSET
        else:
            asset_tag = self.asset_tag

        rack_type: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.rack_type, Unset):
            rack_type = UNSET
        elif isinstance(self.rack_type, BriefRackTypeRequest):
            rack_type = self.rack_type.to_dict()
        else:
            rack_type = self.rack_type

        form_factor: Union[None, Unset, str]
        if isinstance(self.form_factor, Unset):
            form_factor = UNSET
        elif isinstance(self.form_factor, WritableRackRequestFormFactorType1):
            form_factor = self.form_factor.value
        elif isinstance(self.form_factor, WritableRackRequestFormFactorType2Type1):
            form_factor = self.form_factor.value
        elif isinstance(self.form_factor, WritableRackRequestFormFactorType3Type1):
            form_factor = self.form_factor.value
        else:
            form_factor = self.form_factor

        width: Union[Unset, int] = UNSET
        if not isinstance(self.width, Unset):
            width = self.width.value

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

        weight_unit: Union[None, Unset, str]
        if isinstance(self.weight_unit, Unset):
            weight_unit = UNSET
        elif isinstance(self.weight_unit, WritableRackRequestWeightUnitType1):
            weight_unit = self.weight_unit.value
        elif isinstance(self.weight_unit, WritableRackRequestWeightUnitType2Type1):
            weight_unit = self.weight_unit.value
        elif isinstance(self.weight_unit, WritableRackRequestWeightUnitType3Type1):
            weight_unit = self.weight_unit.value
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

        outer_unit: Union[None, Unset, str]
        if isinstance(self.outer_unit, Unset):
            outer_unit = UNSET
        elif isinstance(self.outer_unit, WritableRackRequestOuterUnitType1):
            outer_unit = self.outer_unit.value
        elif isinstance(self.outer_unit, WritableRackRequestOuterUnitType2Type1):
            outer_unit = self.outer_unit.value
        elif isinstance(self.outer_unit, WritableRackRequestOuterUnitType3Type1):
            outer_unit = self.outer_unit.value
        else:
            outer_unit = self.outer_unit

        mounting_depth: Union[None, Unset, int]
        if isinstance(self.mounting_depth, Unset):
            mounting_depth = UNSET
        else:
            mounting_depth = self.mounting_depth

        airflow: Union[None, Unset, str]
        if isinstance(self.airflow, Unset):
            airflow = UNSET
        elif isinstance(self.airflow, WritableRackRequestAirflowType1):
            airflow = self.airflow.value
        elif isinstance(self.airflow, WritableRackRequestAirflowType2Type1):
            airflow = self.airflow.value
        elif isinstance(self.airflow, WritableRackRequestAirflowType3Type1):
            airflow = self.airflow.value
        else:
            airflow = self.airflow

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
                "name": name,
                "site": site,
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

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        site: tuple[None, bytes, str]

        if isinstance(self.site, int):
            site = (None, str(self.site).encode(), "text/plain")
        else:
            site = (None, json.dumps(self.site.to_dict()).encode(), "application/json")

        facility_id: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.facility_id, Unset):
            facility_id = UNSET
        elif isinstance(self.facility_id, str):
            facility_id = (None, str(self.facility_id).encode(), "text/plain")
        else:
            facility_id = (None, str(self.facility_id).encode(), "text/plain")

        location: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, int):
            location = (None, str(self.location).encode(), "text/plain")
        elif isinstance(self.location, None):
            location = (None, str(self.location).encode(), "text/plain")
        elif isinstance(self.location, BriefLocationRequest):
            location = (None, json.dumps(self.location.to_dict()).encode(), "application/json")
        else:
            location = (None, str(self.location).encode(), "text/plain")

        tenant: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, int):
            tenant = (None, str(self.tenant).encode(), "text/plain")
        elif isinstance(self.tenant, None):
            tenant = (None, str(self.tenant).encode(), "text/plain")
        elif isinstance(self.tenant, BriefTenantRequest):
            tenant = (None, json.dumps(self.tenant.to_dict()).encode(), "application/json")
        else:
            tenant = (None, str(self.tenant).encode(), "text/plain")

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
        elif isinstance(self.role, BriefRackRoleRequest):
            role = (None, json.dumps(self.role.to_dict()).encode(), "application/json")
        else:
            role = (None, str(self.role).encode(), "text/plain")

        serial = self.serial if isinstance(self.serial, Unset) else (None, str(self.serial).encode(), "text/plain")

        asset_tag: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.asset_tag, Unset):
            asset_tag = UNSET
        elif isinstance(self.asset_tag, str):
            asset_tag = (None, str(self.asset_tag).encode(), "text/plain")
        else:
            asset_tag = (None, str(self.asset_tag).encode(), "text/plain")

        rack_type: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.rack_type, Unset):
            rack_type = UNSET
        elif isinstance(self.rack_type, int):
            rack_type = (None, str(self.rack_type).encode(), "text/plain")
        elif isinstance(self.rack_type, None):
            rack_type = (None, str(self.rack_type).encode(), "text/plain")
        elif isinstance(self.rack_type, BriefRackTypeRequest):
            rack_type = (None, json.dumps(self.rack_type.to_dict()).encode(), "application/json")
        else:
            rack_type = (None, str(self.rack_type).encode(), "text/plain")

        form_factor: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.form_factor, Unset):
            form_factor = UNSET
        elif isinstance(self.form_factor, None):
            form_factor = (None, str(self.form_factor).encode(), "text/plain")
        elif isinstance(self.form_factor, WritableRackRequestFormFactorType1):
            form_factor = (None, str(self.form_factor.value).encode(), "text/plain")
        elif isinstance(self.form_factor, None):
            form_factor = (None, str(self.form_factor).encode(), "text/plain")
        elif isinstance(self.form_factor, WritableRackRequestFormFactorType2Type1):
            form_factor = (None, str(self.form_factor.value).encode(), "text/plain")
        elif isinstance(self.form_factor, None):
            form_factor = (None, str(self.form_factor).encode(), "text/plain")
        else:
            form_factor = (None, str(self.form_factor.value).encode(), "text/plain")

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
        elif isinstance(self.weight_unit, WritableRackRequestWeightUnitType1):
            weight_unit = (None, str(self.weight_unit.value).encode(), "text/plain")
        elif isinstance(self.weight_unit, None):
            weight_unit = (None, str(self.weight_unit).encode(), "text/plain")
        elif isinstance(self.weight_unit, WritableRackRequestWeightUnitType2Type1):
            weight_unit = (None, str(self.weight_unit.value).encode(), "text/plain")
        elif isinstance(self.weight_unit, None):
            weight_unit = (None, str(self.weight_unit).encode(), "text/plain")
        else:
            weight_unit = (None, str(self.weight_unit.value).encode(), "text/plain")

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
        elif isinstance(self.outer_unit, WritableRackRequestOuterUnitType1):
            outer_unit = (None, str(self.outer_unit.value).encode(), "text/plain")
        elif isinstance(self.outer_unit, None):
            outer_unit = (None, str(self.outer_unit).encode(), "text/plain")
        elif isinstance(self.outer_unit, WritableRackRequestOuterUnitType2Type1):
            outer_unit = (None, str(self.outer_unit.value).encode(), "text/plain")
        elif isinstance(self.outer_unit, None):
            outer_unit = (None, str(self.outer_unit).encode(), "text/plain")
        else:
            outer_unit = (None, str(self.outer_unit.value).encode(), "text/plain")

        mounting_depth: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.mounting_depth, Unset):
            mounting_depth = UNSET
        elif isinstance(self.mounting_depth, int):
            mounting_depth = (None, str(self.mounting_depth).encode(), "text/plain")
        else:
            mounting_depth = (None, str(self.mounting_depth).encode(), "text/plain")

        airflow: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.airflow, Unset):
            airflow = UNSET
        elif isinstance(self.airflow, None):
            airflow = (None, str(self.airflow).encode(), "text/plain")
        elif isinstance(self.airflow, WritableRackRequestAirflowType1):
            airflow = (None, str(self.airflow.value).encode(), "text/plain")
        elif isinstance(self.airflow, None):
            airflow = (None, str(self.airflow).encode(), "text/plain")
        elif isinstance(self.airflow, WritableRackRequestAirflowType2Type1):
            airflow = (None, str(self.airflow.value).encode(), "text/plain")
        elif isinstance(self.airflow, None):
            airflow = (None, str(self.airflow).encode(), "text/plain")
        else:
            airflow = (None, str(self.airflow.value).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

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
                "name": name,
                "site": site,
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_location_request import BriefLocationRequest
        from ..models.brief_rack_role_request import BriefRackRoleRequest
        from ..models.brief_rack_type_request import BriefRackTypeRequest
        from ..models.brief_site_request import BriefSiteRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.writable_rack_request_custom_fields import WritableRackRequestCustomFields

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_site(data: object) -> Union["BriefSiteRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                site_type_1 = BriefSiteRequest.from_dict(data)

                return site_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefSiteRequest", int], data)

        site = _parse_site(d.pop("site"))

        def _parse_facility_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        facility_id = _parse_facility_id(d.pop("facility_id", UNSET))

        def _parse_location(data: object) -> Union["BriefLocationRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_1_type_1 = BriefLocationRequest.from_dict(data)

                return location_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefLocationRequest", None, Unset, int], data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_tenant(data: object) -> Union["BriefTenantRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tenant_type_1_type_1 = BriefTenantRequest.from_dict(data)

                return tenant_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefTenantRequest", None, Unset, int], data)

        tenant = _parse_tenant(d.pop("tenant", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, WritableRackRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WritableRackRequestStatus(_status)

        def _parse_role(data: object) -> Union["BriefRackRoleRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                role_type_1_type_1 = BriefRackRoleRequest.from_dict(data)

                return role_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefRackRoleRequest", None, Unset, int], data)

        role = _parse_role(d.pop("role", UNSET))

        serial = d.pop("serial", UNSET)

        def _parse_asset_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_tag = _parse_asset_tag(d.pop("asset_tag", UNSET))

        def _parse_rack_type(data: object) -> Union["BriefRackTypeRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rack_type_type_1_type_1 = BriefRackTypeRequest.from_dict(data)

                return rack_type_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefRackTypeRequest", None, Unset, int], data)

        rack_type = _parse_rack_type(d.pop("rack_type", UNSET))

        def _parse_form_factor(
            data: object,
        ) -> Union[
            None,
            Unset,
            WritableRackRequestFormFactorType1,
            WritableRackRequestFormFactorType2Type1,
            WritableRackRequestFormFactorType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                form_factor_type_1 = WritableRackRequestFormFactorType1(data)

                return form_factor_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                form_factor_type_2_type_1 = WritableRackRequestFormFactorType2Type1(data)

                return form_factor_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                form_factor_type_3_type_1 = WritableRackRequestFormFactorType3Type1(data)

                return form_factor_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    WritableRackRequestFormFactorType1,
                    WritableRackRequestFormFactorType2Type1,
                    WritableRackRequestFormFactorType3Type1,
                ],
                data,
            )

        form_factor = _parse_form_factor(d.pop("form_factor", UNSET))

        _width = d.pop("width", UNSET)
        width: Union[Unset, WritableRackRequestWidth]
        if isinstance(_width, Unset):
            width = UNSET
        else:
            width = WritableRackRequestWidth(_width)

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
        ) -> Union[
            None,
            Unset,
            WritableRackRequestWeightUnitType1,
            WritableRackRequestWeightUnitType2Type1,
            WritableRackRequestWeightUnitType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                weight_unit_type_1 = WritableRackRequestWeightUnitType1(data)

                return weight_unit_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                weight_unit_type_2_type_1 = WritableRackRequestWeightUnitType2Type1(data)

                return weight_unit_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                weight_unit_type_3_type_1 = WritableRackRequestWeightUnitType3Type1(data)

                return weight_unit_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    WritableRackRequestWeightUnitType1,
                    WritableRackRequestWeightUnitType2Type1,
                    WritableRackRequestWeightUnitType3Type1,
                ],
                data,
            )

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

        def _parse_outer_unit(
            data: object,
        ) -> Union[
            None,
            Unset,
            WritableRackRequestOuterUnitType1,
            WritableRackRequestOuterUnitType2Type1,
            WritableRackRequestOuterUnitType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outer_unit_type_1 = WritableRackRequestOuterUnitType1(data)

                return outer_unit_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outer_unit_type_2_type_1 = WritableRackRequestOuterUnitType2Type1(data)

                return outer_unit_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                outer_unit_type_3_type_1 = WritableRackRequestOuterUnitType3Type1(data)

                return outer_unit_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    WritableRackRequestOuterUnitType1,
                    WritableRackRequestOuterUnitType2Type1,
                    WritableRackRequestOuterUnitType3Type1,
                ],
                data,
            )

        outer_unit = _parse_outer_unit(d.pop("outer_unit", UNSET))

        def _parse_mounting_depth(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        mounting_depth = _parse_mounting_depth(d.pop("mounting_depth", UNSET))

        def _parse_airflow(
            data: object,
        ) -> Union[
            None,
            Unset,
            WritableRackRequestAirflowType1,
            WritableRackRequestAirflowType2Type1,
            WritableRackRequestAirflowType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                airflow_type_1 = WritableRackRequestAirflowType1(data)

                return airflow_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                airflow_type_2_type_1 = WritableRackRequestAirflowType2Type1(data)

                return airflow_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                airflow_type_3_type_1 = WritableRackRequestAirflowType3Type1(data)

                return airflow_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    WritableRackRequestAirflowType1,
                    WritableRackRequestAirflowType2Type1,
                    WritableRackRequestAirflowType3Type1,
                ],
                data,
            )

        airflow = _parse_airflow(d.pop("airflow", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WritableRackRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WritableRackRequestCustomFields.from_dict(_custom_fields)

        writable_rack_request = cls(
            name=name,
            site=site,
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
        )

        writable_rack_request.additional_properties = d
        return writable_rack_request

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
