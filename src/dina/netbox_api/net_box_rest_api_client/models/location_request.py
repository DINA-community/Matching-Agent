from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.location_request_status import LocationRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_site_request import BriefSiteRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.location_request_custom_fields import LocationRequestCustomFields
    from ..models.nested_location_request import NestedLocationRequest
    from ..models.nested_tag_request import NestedTagRequest


T = TypeVar("T", bound="LocationRequest")


@_attrs_define
class LocationRequest:
    """Extends PrimaryModelSerializer to include MPTT support.

    Attributes:
        name (str):
        slug (str):
        site (Union['BriefSiteRequest', int]):
        parent (Union['NestedLocationRequest', None, Unset]):
        status (Union[Unset, LocationRequestStatus]): * `planned` - Planned
            * `staging` - Staging
            * `active` - Active
            * `decommissioning` - Decommissioning
            * `retired` - Retired
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        facility (Union[Unset, str]): Local facility ID or description
        description (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, LocationRequestCustomFields]):
        comments (Union[Unset, str]):
    """

    name: str
    slug: str
    site: Union["BriefSiteRequest", int]
    parent: Union["NestedLocationRequest", None, Unset] = UNSET
    status: Union[Unset, LocationRequestStatus] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    facility: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "LocationRequestCustomFields"] = UNSET
    comments: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_site_request import BriefSiteRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.nested_location_request import NestedLocationRequest

        name = self.name

        slug = self.slug

        site: Union[dict[str, Any], int]
        if isinstance(self.site, BriefSiteRequest):
            site = self.site.to_dict()
        else:
            site = self.site

        parent: Union[None, Unset, dict[str, Any]]
        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, NestedLocationRequest):
            parent = self.parent.to_dict()
        else:
            parent = self.parent

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        tenant: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenantRequest):
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

        comments = self.comments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
                "site": site,
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
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_site_request import BriefSiteRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.location_request_custom_fields import LocationRequestCustomFields
        from ..models.nested_location_request import NestedLocationRequest
        from ..models.nested_tag_request import NestedTagRequest

        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

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

        def _parse_parent(data: object) -> Union["NestedLocationRequest", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_type_1 = NestedLocationRequest.from_dict(data)

                return parent_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NestedLocationRequest", None, Unset], data)

        parent = _parse_parent(d.pop("parent", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, LocationRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LocationRequestStatus(_status)

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

        facility = d.pop("facility", UNSET)

        description = d.pop("description", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, LocationRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = LocationRequestCustomFields.from_dict(_custom_fields)

        comments = d.pop("comments", UNSET)

        location_request = cls(
            name=name,
            slug=slug,
            site=site,
            parent=parent,
            status=status,
            tenant=tenant,
            facility=facility,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
            comments=comments,
        )

        location_request.additional_properties = d
        return location_request

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
