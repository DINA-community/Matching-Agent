import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_circuit_group_request_custom_fields import (
        PatchedCircuitGroupRequestCustomFields,
    )


T = TypeVar("T", bound="PatchedCircuitGroupRequest")


@_attrs_define
class PatchedCircuitGroupRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (Union[Unset, str]):
        slug (Union[Unset, str]):
        description (Union[Unset, str]):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedCircuitGroupRequestCustomFields]):
    """

    name: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedCircuitGroupRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_tenant_request import BriefTenantRequest

        name = self.name

        slug = self.slug

        description = self.description

        tenant: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenantRequest):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

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
        if description is not UNSET:
            field_dict["description"] = description
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (
            self.name
            if isinstance(self.name, Unset)
            else (None, str(self.name).encode(), "text/plain")
        )

        slug = (
            self.slug
            if isinstance(self.slug, Unset)
            else (None, str(self.slug).encode(), "text/plain")
        )

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

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

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_circuit_group_request_custom_fields import (
            PatchedCircuitGroupRequestCustomFields,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        description = d.pop("description", UNSET)

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

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedCircuitGroupRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedCircuitGroupRequestCustomFields.from_dict(
                _custom_fields
            )

        patched_circuit_group_request = cls(
            name=name,
            slug=slug,
            description=description,
            tenant=tenant,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_circuit_group_request.additional_properties = d
        return patched_circuit_group_request

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
