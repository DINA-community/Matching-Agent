import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_site_request_status import WritableSiteRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_region_request import BriefRegionRequest
    from ..models.brief_site_group_request import BriefSiteGroupRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.writable_site_request_custom_fields import (
        WritableSiteRequestCustomFields,
    )


T = TypeVar("T", bound="WritableSiteRequest")


@_attrs_define
class WritableSiteRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str): Full name of the site
        slug (str):
        status (Union[Unset, WritableSiteRequestStatus]): * `planned` - Planned
            * `staging` - Staging
            * `active` - Active
            * `decommissioning` - Decommissioning
            * `retired` - Retired
        region (Union['BriefRegionRequest', None, Unset, int]):
        group (Union['BriefSiteGroupRequest', None, Unset, int]):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        facility (Union[Unset, str]): Local facility ID or description
        time_zone (Union[None, Unset, str]):
        description (Union[Unset, str]):
        physical_address (Union[Unset, str]): Physical location of the building
        shipping_address (Union[Unset, str]): If different from the physical address
        latitude (Union[None, Unset, float]): GPS coordinate in decimal format (xx.yyyyyy)
        longitude (Union[None, Unset, float]): GPS coordinate in decimal format (xx.yyyyyy)
        comments (Union[Unset, str]):
        asns (Union[Unset, list[int]]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WritableSiteRequestCustomFields]):
    """

    name: str
    slug: str
    status: Union[Unset, WritableSiteRequestStatus] = UNSET
    region: Union["BriefRegionRequest", None, Unset, int] = UNSET
    group: Union["BriefSiteGroupRequest", None, Unset, int] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    facility: Union[Unset, str] = UNSET
    time_zone: Union[None, Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    physical_address: Union[Unset, str] = UNSET
    shipping_address: Union[Unset, str] = UNSET
    latitude: Union[None, Unset, float] = UNSET
    longitude: Union[None, Unset, float] = UNSET
    comments: Union[Unset, str] = UNSET
    asns: Union[Unset, list[int]] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WritableSiteRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_region_request import BriefRegionRequest
        from ..models.brief_site_group_request import BriefSiteGroupRequest
        from ..models.brief_tenant_request import BriefTenantRequest

        name = self.name

        slug = self.slug

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        region: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.region, Unset):
            region = UNSET
        elif isinstance(self.region, BriefRegionRequest):
            region = self.region.to_dict()
        else:
            region = self.region

        group: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.group, Unset):
            group = UNSET
        elif isinstance(self.group, BriefSiteGroupRequest):
            group = self.group.to_dict()
        else:
            group = self.group

        tenant: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenantRequest):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        facility = self.facility

        time_zone: Union[None, Unset, str]
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        description = self.description

        physical_address = self.physical_address

        shipping_address = self.shipping_address

        latitude: Union[None, Unset, float]
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: Union[None, Unset, float]
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        comments = self.comments

        asns: Union[Unset, list[int]] = UNSET
        if not isinstance(self.asns, Unset):
            asns = self.asns

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
                "slug": slug,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if region is not UNSET:
            field_dict["region"] = region
        if group is not UNSET:
            field_dict["group"] = group
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if facility is not UNSET:
            field_dict["facility"] = facility
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if description is not UNSET:
            field_dict["description"] = description
        if physical_address is not UNSET:
            field_dict["physical_address"] = physical_address
        if shipping_address is not UNSET:
            field_dict["shipping_address"] = shipping_address
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if comments is not UNSET:
            field_dict["comments"] = comments
        if asns is not UNSET:
            field_dict["asns"] = asns
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        slug = (None, str(self.slug).encode(), "text/plain")

        status: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

        region: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.region, Unset):
            region = UNSET
        elif isinstance(self.region, int):
            region = (None, str(self.region).encode(), "text/plain")
        elif isinstance(self.region, None):
            region = (None, str(self.region).encode(), "text/plain")
        elif isinstance(self.region, BriefRegionRequest):
            region = (
                None,
                json.dumps(self.region.to_dict()).encode(),
                "application/json",
            )
        else:
            region = (None, str(self.region).encode(), "text/plain")

        group: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.group, Unset):
            group = UNSET
        elif isinstance(self.group, int):
            group = (None, str(self.group).encode(), "text/plain")
        elif isinstance(self.group, None):
            group = (None, str(self.group).encode(), "text/plain")
        elif isinstance(self.group, BriefSiteGroupRequest):
            group = (
                None,
                json.dumps(self.group.to_dict()).encode(),
                "application/json",
            )
        else:
            group = (None, str(self.group).encode(), "text/plain")

        tenant: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, int):
            tenant = (None, str(self.tenant).encode(), "text/plain")
        elif isinstance(self.tenant, None):
            tenant = (None, str(self.tenant).encode(), "text/plain")
        elif isinstance(self.tenant, BriefTenantRequest):
            tenant = (
                None,
                json.dumps(self.tenant.to_dict()).encode(),
                "application/json",
            )
        else:
            tenant = (None, str(self.tenant).encode(), "text/plain")

        facility = (
            self.facility
            if isinstance(self.facility, Unset)
            else (None, str(self.facility).encode(), "text/plain")
        )

        time_zone: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        elif isinstance(self.time_zone, str):
            time_zone = (None, str(self.time_zone).encode(), "text/plain")
        else:
            time_zone = (None, str(self.time_zone).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        physical_address = (
            self.physical_address
            if isinstance(self.physical_address, Unset)
            else (None, str(self.physical_address).encode(), "text/plain")
        )

        shipping_address = (
            self.shipping_address
            if isinstance(self.shipping_address, Unset)
            else (None, str(self.shipping_address).encode(), "text/plain")
        )

        latitude: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.latitude, Unset):
            latitude = UNSET
        elif isinstance(self.latitude, float):
            latitude = (None, str(self.latitude).encode(), "text/plain")
        else:
            latitude = (None, str(self.latitude).encode(), "text/plain")

        longitude: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.longitude, Unset):
            longitude = UNSET
        elif isinstance(self.longitude, float):
            longitude = (None, str(self.longitude).encode(), "text/plain")
        else:
            longitude = (None, str(self.longitude).encode(), "text/plain")

        comments = (
            self.comments
            if isinstance(self.comments, Unset)
            else (None, str(self.comments).encode(), "text/plain")
        )

        asns: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.asns, Unset):
            _temp_asns = self.asns
            asns = (None, json.dumps(_temp_asns).encode(), "application/json")

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
                "name": name,
                "slug": slug,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if region is not UNSET:
            field_dict["region"] = region
        if group is not UNSET:
            field_dict["group"] = group
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if facility is not UNSET:
            field_dict["facility"] = facility
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if description is not UNSET:
            field_dict["description"] = description
        if physical_address is not UNSET:
            field_dict["physical_address"] = physical_address
        if shipping_address is not UNSET:
            field_dict["shipping_address"] = shipping_address
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if comments is not UNSET:
            field_dict["comments"] = comments
        if asns is not UNSET:
            field_dict["asns"] = asns
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_region_request import BriefRegionRequest
        from ..models.brief_site_group_request import BriefSiteGroupRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.writable_site_request_custom_fields import (
            WritableSiteRequestCustomFields,
        )

        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        _status = d.pop("status", UNSET)
        status: Union[Unset, WritableSiteRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WritableSiteRequestStatus(_status)

        def _parse_region(
            data: object,
        ) -> Union["BriefRegionRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                region_type_1_type_1 = BriefRegionRequest.from_dict(data)

                return region_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefRegionRequest", None, Unset, int], data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_group(
            data: object,
        ) -> Union["BriefSiteGroupRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_1_type_1 = BriefSiteGroupRequest.from_dict(data)

                return group_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefSiteGroupRequest", None, Unset, int], data)

        group = _parse_group(d.pop("group", UNSET))

        def _parse_tenant(
            data: object,
        ) -> Union["BriefTenantRequest", None, Unset, int]:
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

        facility = d.pop("facility", UNSET)

        def _parse_time_zone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        time_zone = _parse_time_zone(d.pop("time_zone", UNSET))

        description = d.pop("description", UNSET)

        physical_address = d.pop("physical_address", UNSET)

        shipping_address = d.pop("shipping_address", UNSET)

        def _parse_latitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        comments = d.pop("comments", UNSET)

        asns = cast(list[int], d.pop("asns", UNSET))

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WritableSiteRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WritableSiteRequestCustomFields.from_dict(_custom_fields)

        writable_site_request = cls(
            name=name,
            slug=slug,
            status=status,
            region=region,
            group=group,
            tenant=tenant,
            facility=facility,
            time_zone=time_zone,
            description=description,
            physical_address=physical_address,
            shipping_address=shipping_address,
            latitude=latitude,
            longitude=longitude,
            comments=comments,
            asns=asns,
            tags=tags,
            custom_fields=custom_fields,
        )

        writable_site_request.additional_properties = d
        return writable_site_request

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
