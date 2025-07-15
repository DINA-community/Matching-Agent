import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_location_request_status import WritableLocationRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_site_request import BriefSiteRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.writable_location_request_custom_fields import WritableLocationRequestCustomFields


T = TypeVar("T", bound="WritableLocationRequest")


@_attrs_define
class WritableLocationRequest:
    """Extends PrimaryModelSerializer to include MPTT support.

    Attributes:
        name (str):
        slug (str):
        site (Union['BriefSiteRequest', int]):
        parent (Union[None, Unset, int]):
        status (Union[Unset, WritableLocationRequestStatus]): * `planned` - Planned
            * `staging` - Staging
            * `active` - Active
            * `decommissioning` - Decommissioning
            * `retired` - Retired
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        facility (Union[Unset, str]): Local facility ID or description
        description (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WritableLocationRequestCustomFields]):
        comments (Union[Unset, str]):
    """

    name: str
    slug: str
    site: Union["BriefSiteRequest", int]
    parent: Union[None, Unset, int] = UNSET
    status: Union[Unset, WritableLocationRequestStatus] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    facility: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WritableLocationRequestCustomFields"] = UNSET
    comments: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_site_request import BriefSiteRequest
        from ..models.brief_tenant_request import BriefTenantRequest

        name = self.name

        slug = self.slug

        site: Union[dict[str, Any], int]
        if isinstance(self.site, BriefSiteRequest):
            site = self.site.to_dict()
        else:
            site = self.site

        parent: Union[None, Unset, int]
        if isinstance(self.parent, Unset):
            parent = UNSET
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

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        slug = (None, str(self.slug).encode(), "text/plain")

        site: tuple[None, bytes, str]

        if isinstance(self.site, int):
            site = (None, str(self.site).encode(), "text/plain")
        else:
            site = (None, json.dumps(self.site.to_dict()).encode(), "application/json")

        parent: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, int):
            parent = (None, str(self.parent).encode(), "text/plain")
        else:
            parent = (None, str(self.parent).encode(), "text/plain")

        status: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

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

        facility = (
            self.facility if isinstance(self.facility, Unset) else (None, str(self.facility).encode(), "text/plain")
        )

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
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

        comments = (
            self.comments if isinstance(self.comments, Unset) else (None, str(self.comments).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

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
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.writable_location_request_custom_fields import WritableLocationRequestCustomFields

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

        def _parse_parent(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent = _parse_parent(d.pop("parent", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, WritableLocationRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WritableLocationRequestStatus(_status)

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
        custom_fields: Union[Unset, WritableLocationRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WritableLocationRequestCustomFields.from_dict(_custom_fields)

        comments = d.pop("comments", UNSET)

        writable_location_request = cls(
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

        writable_location_request.additional_properties = d
        return writable_location_request

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
