import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.vlan_group_request_custom_fields import VLANGroupRequestCustomFields


T = TypeVar("T", bound="VLANGroupRequest")


@_attrs_define
class VLANGroupRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str):
        slug (str):
        scope_type (Union[None, Unset, str]):
        scope_id (Union[None, Unset, int]):
        vid_ranges (Union[Unset, list[list[list[int]]]]):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        description (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, VLANGroupRequestCustomFields]):
    """

    name: str
    slug: str
    scope_type: Union[None, Unset, str] = UNSET
    scope_id: Union[None, Unset, int] = UNSET
    vid_ranges: Union[Unset, list[list[list[int]]]] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "VLANGroupRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_tenant_request import BriefTenantRequest

        name = self.name

        slug = self.slug

        scope_type: Union[None, Unset, str]
        if isinstance(self.scope_type, Unset):
            scope_type = UNSET
        else:
            scope_type = self.scope_type

        scope_id: Union[None, Unset, int]
        if isinstance(self.scope_id, Unset):
            scope_id = UNSET
        else:
            scope_id = self.scope_id

        vid_ranges: Union[Unset, list[list[list[int]]]] = UNSET
        if not isinstance(self.vid_ranges, Unset):
            vid_ranges = []
            for vid_ranges_item_data in self.vid_ranges:
                vid_ranges_item = []
                for componentsschemas_integer_range_request_item_data in vid_ranges_item_data:
                    componentsschemas_integer_range_request_item = componentsschemas_integer_range_request_item_data

                    vid_ranges_item.append(componentsschemas_integer_range_request_item)

                vid_ranges.append(vid_ranges_item)

        tenant: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenantRequest):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
            }
        )
        if scope_type is not UNSET:
            field_dict["scope_type"] = scope_type
        if scope_id is not UNSET:
            field_dict["scope_id"] = scope_id
        if vid_ranges is not UNSET:
            field_dict["vid_ranges"] = vid_ranges
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        slug = (None, str(self.slug).encode(), "text/plain")

        scope_type: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.scope_type, Unset):
            scope_type = UNSET
        elif isinstance(self.scope_type, str):
            scope_type = (None, str(self.scope_type).encode(), "text/plain")
        else:
            scope_type = (None, str(self.scope_type).encode(), "text/plain")

        scope_id: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.scope_id, Unset):
            scope_id = UNSET
        elif isinstance(self.scope_id, int):
            scope_id = (None, str(self.scope_id).encode(), "text/plain")
        else:
            scope_id = (None, str(self.scope_id).encode(), "text/plain")

        vid_ranges: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.vid_ranges, Unset):
            _temp_vid_ranges = []
            for vid_ranges_item_data in self.vid_ranges:
                vid_ranges_item = []
                for componentsschemas_integer_range_request_item_data in vid_ranges_item_data:
                    componentsschemas_integer_range_request_item = componentsschemas_integer_range_request_item_data

                    vid_ranges_item.append(componentsschemas_integer_range_request_item)

                _temp_vid_ranges.append(vid_ranges_item)
            vid_ranges = (None, json.dumps(_temp_vid_ranges).encode(), "application/json")

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

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "name": name,
                "slug": slug,
            }
        )
        if scope_type is not UNSET:
            field_dict["scope_type"] = scope_type
        if scope_id is not UNSET:
            field_dict["scope_id"] = scope_id
        if vid_ranges is not UNSET:
            field_dict["vid_ranges"] = vid_ranges
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.vlan_group_request_custom_fields import VLANGroupRequestCustomFields

        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        def _parse_scope_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scope_type = _parse_scope_type(d.pop("scope_type", UNSET))

        def _parse_scope_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        scope_id = _parse_scope_id(d.pop("scope_id", UNSET))

        vid_ranges = []
        _vid_ranges = d.pop("vid_ranges", UNSET)
        for vid_ranges_item_data in _vid_ranges or []:
            vid_ranges_item = []
            _vid_ranges_item = vid_ranges_item_data
            for componentsschemas_integer_range_request_item_data in _vid_ranges_item:
                componentsschemas_integer_range_request_item = cast(
                    list[int], componentsschemas_integer_range_request_item_data
                )

                vid_ranges_item.append(componentsschemas_integer_range_request_item)

            vid_ranges.append(vid_ranges_item)

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

        description = d.pop("description", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, VLANGroupRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = VLANGroupRequestCustomFields.from_dict(_custom_fields)

        vlan_group_request = cls(
            name=name,
            slug=slug,
            scope_type=scope_type,
            scope_id=scope_id,
            vid_ranges=vid_ranges,
            tenant=tenant,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )

        vlan_group_request.additional_properties = d
        return vlan_group_request

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
