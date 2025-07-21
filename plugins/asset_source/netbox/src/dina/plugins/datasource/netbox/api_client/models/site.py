import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asn import ASN
    from ..models.brief_region import BriefRegion
    from ..models.brief_site_group import BriefSiteGroup
    from ..models.brief_tenant import BriefTenant
    from ..models.nested_tag import NestedTag
    from ..models.site_custom_fields import SiteCustomFields
    from ..models.site_status import SiteStatus


T = TypeVar("T", bound="Site")


@_attrs_define
class Site:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        name (str): Full name of the site
        slug (str):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        circuit_count (int):
        prefix_count (int):
        rack_count (int):
        vlan_count (int):
        status (Union[Unset, SiteStatus]):
        region (Union['BriefRegion', None, Unset]):
        group (Union['BriefSiteGroup', None, Unset]):
        tenant (Union['BriefTenant', None, Unset]):
        facility (Union[Unset, str]): Local facility ID or description
        time_zone (Union[None, Unset, str]):
        description (Union[Unset, str]):
        physical_address (Union[Unset, str]): Physical location of the building
        shipping_address (Union[Unset, str]): If different from the physical address
        latitude (Union[None, Unset, float]): GPS coordinate in decimal format (xx.yyyyyy)
        longitude (Union[None, Unset, float]): GPS coordinate in decimal format (xx.yyyyyy)
        comments (Union[Unset, str]):
        asns (Union[Unset, list['ASN']]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, SiteCustomFields]):
        device_count (Union[Unset, int]):
        virtualmachine_count (Union[Unset, int]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    slug: str
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    circuit_count: int
    prefix_count: int
    rack_count: int
    vlan_count: int
    status: Union[Unset, "SiteStatus"] = UNSET
    region: Union["BriefRegion", None, Unset] = UNSET
    group: Union["BriefSiteGroup", None, Unset] = UNSET
    tenant: Union["BriefTenant", None, Unset] = UNSET
    facility: Union[Unset, str] = UNSET
    time_zone: Union[None, Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    physical_address: Union[Unset, str] = UNSET
    shipping_address: Union[Unset, str] = UNSET
    latitude: Union[None, Unset, float] = UNSET
    longitude: Union[None, Unset, float] = UNSET
    comments: Union[Unset, str] = UNSET
    asns: Union[Unset, list["ASN"]] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "SiteCustomFields"] = UNSET
    device_count: Union[Unset, int] = UNSET
    virtualmachine_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_region import BriefRegion
        from ..models.brief_site_group import BriefSiteGroup
        from ..models.brief_tenant import BriefTenant

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

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

        circuit_count = self.circuit_count

        prefix_count = self.prefix_count

        rack_count = self.rack_count

        vlan_count = self.vlan_count

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        region: Union[None, Unset, dict[str, Any]]
        if isinstance(self.region, Unset):
            region = UNSET
        elif isinstance(self.region, BriefRegion):
            region = self.region.to_dict()
        else:
            region = self.region

        group: Union[None, Unset, dict[str, Any]]
        if isinstance(self.group, Unset):
            group = UNSET
        elif isinstance(self.group, BriefSiteGroup):
            group = self.group.to_dict()
        else:
            group = self.group

        tenant: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenant):
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

        asns: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.asns, Unset):
            asns = []
            for asns_item_data in self.asns:
                asns_item = asns_item_data.to_dict()
                asns.append(asns_item)

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

        virtualmachine_count = self.virtualmachine_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "name": name,
                "slug": slug,
                "created": created,
                "last_updated": last_updated,
                "circuit_count": circuit_count,
                "prefix_count": prefix_count,
                "rack_count": rack_count,
                "vlan_count": vlan_count,
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
        if device_count is not UNSET:
            field_dict["device_count"] = device_count
        if virtualmachine_count is not UNSET:
            field_dict["virtualmachine_count"] = virtualmachine_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asn import ASN
        from ..models.brief_region import BriefRegion
        from ..models.brief_site_group import BriefSiteGroup
        from ..models.brief_tenant import BriefTenant
        from ..models.nested_tag import NestedTag
        from ..models.site_custom_fields import SiteCustomFields
        from ..models.site_status import SiteStatus

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

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

        circuit_count = d.pop("circuit_count")

        prefix_count = d.pop("prefix_count")

        rack_count = d.pop("rack_count")

        vlan_count = d.pop("vlan_count")

        _status = d.pop("status", UNSET)
        status: Union[Unset, SiteStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SiteStatus.from_dict(_status)

        def _parse_region(data: object) -> Union["BriefRegion", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                region_type_1 = BriefRegion.from_dict(data)

                return region_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefRegion", None, Unset], data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_group(data: object) -> Union["BriefSiteGroup", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_1 = BriefSiteGroup.from_dict(data)

                return group_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefSiteGroup", None, Unset], data)

        group = _parse_group(d.pop("group", UNSET))

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

        asns = []
        _asns = d.pop("asns", UNSET)
        for asns_item_data in _asns or []:
            asns_item = ASN.from_dict(asns_item_data)

            asns.append(asns_item)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, SiteCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = SiteCustomFields.from_dict(_custom_fields)

        device_count = d.pop("device_count", UNSET)

        virtualmachine_count = d.pop("virtualmachine_count", UNSET)

        site = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            slug=slug,
            created=created,
            last_updated=last_updated,
            circuit_count=circuit_count,
            prefix_count=prefix_count,
            rack_count=rack_count,
            vlan_count=vlan_count,
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
            device_count=device_count,
            virtualmachine_count=virtualmachine_count,
        )

        site.additional_properties = d
        return site

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
