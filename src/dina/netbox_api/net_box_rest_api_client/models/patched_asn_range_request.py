import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_rir_request import BriefRIRRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_asn_range_request_custom_fields import PatchedASNRangeRequestCustomFields


T = TypeVar("T", bound="PatchedASNRangeRequest")


@_attrs_define
class PatchedASNRangeRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (Union[Unset, str]):
        slug (Union[Unset, str]):
        rir (Union['BriefRIRRequest', Unset, int]):
        start (Union[Unset, int]):
        end (Union[Unset, int]):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        description (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedASNRangeRequestCustomFields]):
    """

    name: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    rir: Union["BriefRIRRequest", Unset, int] = UNSET
    start: Union[Unset, int] = UNSET
    end: Union[Unset, int] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedASNRangeRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_rir_request import BriefRIRRequest
        from ..models.brief_tenant_request import BriefTenantRequest

        name = self.name

        slug = self.slug

        rir: Union[Unset, dict[str, Any], int]
        if isinstance(self.rir, Unset):
            rir = UNSET
        elif isinstance(self.rir, BriefRIRRequest):
            rir = self.rir.to_dict()
        else:
            rir = self.rir

        start = self.start

        end = self.end

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
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if rir is not UNSET:
            field_dict["rir"] = rir
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
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
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        slug = self.slug if isinstance(self.slug, Unset) else (None, str(self.slug).encode(), "text/plain")

        rir: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.rir, Unset):
            rir = UNSET
        elif isinstance(self.rir, int):
            rir = (None, str(self.rir).encode(), "text/plain")
        else:
            rir = (None, json.dumps(self.rir.to_dict()).encode(), "application/json")

        start = self.start if isinstance(self.start, Unset) else (None, str(self.start).encode(), "text/plain")

        end = self.end if isinstance(self.end, Unset) else (None, str(self.end).encode(), "text/plain")

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

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if rir is not UNSET:
            field_dict["rir"] = rir
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
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
        from ..models.brief_rir_request import BriefRIRRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_asn_range_request_custom_fields import PatchedASNRangeRequestCustomFields

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        def _parse_rir(data: object) -> Union["BriefRIRRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rir_type_1 = BriefRIRRequest.from_dict(data)

                return rir_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefRIRRequest", Unset, int], data)

        rir = _parse_rir(d.pop("rir", UNSET))

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

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
        custom_fields: Union[Unset, PatchedASNRangeRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedASNRangeRequestCustomFields.from_dict(_custom_fields)

        patched_asn_range_request = cls(
            name=name,
            slug=slug,
            rir=rir,
            start=start,
            end=end,
            tenant=tenant,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_asn_range_request.additional_properties = d
        return patched_asn_range_request

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
