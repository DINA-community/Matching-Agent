import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_site import BriefSite
    from ..models.brief_tenant import BriefTenant
    from ..models.location_custom_fields import LocationCustomFields
    from ..models.location_status import LocationStatus
    from ..models.nested_location import NestedLocation
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="Location")


@_attrs_define
class Location:
    """Extends PrimaryModelSerializer to include MPTT support.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        name (str):
        slug (str):
        site (BriefSite): Adds support for custom fields and tags.
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        rack_count (int):  Default: 0.
        prefix_count (int):
        field_depth (int):
        parent (Union['NestedLocation', None, Unset]):
        status (Union[Unset, LocationStatus]):
        tenant (Union['BriefTenant', None, Unset]):
        facility (Union[Unset, str]): Local facility ID or description
        description (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, LocationCustomFields]):
        device_count (Union[Unset, int]):  Default: 0.
        comments (Union[Unset, str]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    slug: str
    site: "BriefSite"
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    prefix_count: int
    field_depth: int
    rack_count: int = 0
    parent: Union["NestedLocation", None, Unset] = UNSET
    status: Union[Unset, "LocationStatus"] = UNSET
    tenant: Union["BriefTenant", None, Unset] = UNSET
    facility: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "LocationCustomFields"] = UNSET
    device_count: Union[Unset, int] = 0
    comments: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_tenant import BriefTenant
        from ..models.nested_location import NestedLocation

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

        slug = self.slug

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

        rack_count = self.rack_count

        prefix_count = self.prefix_count

        field_depth = self.field_depth

        parent: Union[None, Unset, dict[str, Any]]
        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, NestedLocation):
            parent = self.parent.to_dict()
        else:
            parent = self.parent

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        tenant: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenant):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        facility = self.facility

        description = self.description

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

        comments = self.comments

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
                "site": site,
                "created": created,
                "last_updated": last_updated,
                "rack_count": rack_count,
                "prefix_count": prefix_count,
                "_depth": field_depth,
            }
        )
        if parent is not UNSET:
            field_dict["parent"] = parent
        if status is not UNSET:
            field_dict["status"] = status
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if facility is not UNSET:
            field_dict["facility"] = facility
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if device_count is not UNSET:
            field_dict["device_count"] = device_count
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_site import BriefSite
        from ..models.brief_tenant import BriefTenant
        from ..models.location_custom_fields import LocationCustomFields
        from ..models.location_status import LocationStatus
        from ..models.nested_location import NestedLocation
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

        slug = d.pop("slug")

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

        rack_count = d.pop("rack_count")

        prefix_count = d.pop("prefix_count")

        field_depth = d.pop("_depth")

        def _parse_parent(data: object) -> Union["NestedLocation", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_type_1 = NestedLocation.from_dict(data)

                return parent_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NestedLocation", None, Unset], data)

        parent = _parse_parent(d.pop("parent", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, LocationStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LocationStatus.from_dict(_status)

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

        description = d.pop("description", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, LocationCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = LocationCustomFields.from_dict(_custom_fields)

        device_count = d.pop("device_count", UNSET)

        comments = d.pop("comments", UNSET)

        location = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            slug=slug,
            site=site,
            created=created,
            last_updated=last_updated,
            rack_count=rack_count,
            prefix_count=prefix_count,
            field_depth=field_depth,
            parent=parent,
            status=status,
            tenant=tenant,
            facility=facility,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
            device_count=device_count,
            comments=comments,
        )

        location.additional_properties = d
        return location

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
