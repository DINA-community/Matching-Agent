import datetime
import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_rir_request import BriefRIRRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_writable_aggregate_request_custom_fields import PatchedWritableAggregateRequestCustomFields


T = TypeVar("T", bound="PatchedWritableAggregateRequest")


@_attrs_define
class PatchedWritableAggregateRequest:
    """Adds support for custom fields and tags.

    Attributes:
        prefix (Union[Unset, str]):
        rir (Union['BriefRIRRequest', Unset, int]):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        date_added (Union[None, Unset, datetime.date]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedWritableAggregateRequestCustomFields]):
    """

    prefix: Union[Unset, str] = UNSET
    rir: Union["BriefRIRRequest", Unset, int] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    date_added: Union[None, Unset, datetime.date] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedWritableAggregateRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_rir_request import BriefRIRRequest
        from ..models.brief_tenant_request import BriefTenantRequest

        prefix = self.prefix

        rir: Union[Unset, dict[str, Any], int]
        if isinstance(self.rir, Unset):
            rir = UNSET
        elif isinstance(self.rir, BriefRIRRequest):
            rir = self.rir.to_dict()
        else:
            rir = self.rir

        tenant: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenantRequest):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        date_added: Union[None, Unset, str]
        if isinstance(self.date_added, Unset):
            date_added = UNSET
        elif isinstance(self.date_added, datetime.date):
            date_added = self.date_added.isoformat()
        else:
            date_added = self.date_added

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
        field_dict.update({})
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if rir is not UNSET:
            field_dict["rir"] = rir
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
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
        prefix = self.prefix if isinstance(self.prefix, Unset) else (None, str(self.prefix).encode(), "text/plain")

        rir: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.rir, Unset):
            rir = UNSET
        elif isinstance(self.rir, int):
            rir = (None, str(self.rir).encode(), "text/plain")
        else:
            rir = (None, json.dumps(self.rir.to_dict()).encode(), "application/json")

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

        date_added: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.date_added, Unset):
            date_added = UNSET
        elif isinstance(self.date_added, datetime.date):
            date_added = self.date_added.isoformat().encode()
        else:
            date_added = (None, str(self.date_added).encode(), "text/plain")

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

        field_dict.update({})
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if rir is not UNSET:
            field_dict["rir"] = rir
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
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
        from ..models.brief_rir_request import BriefRIRRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_writable_aggregate_request_custom_fields import (
            PatchedWritableAggregateRequestCustomFields,
        )

        d = dict(src_dict)
        prefix = d.pop("prefix", UNSET)

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

        def _parse_date_added(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_added_type_0 = isoparse(data).date()

                return date_added_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date_added = _parse_date_added(d.pop("date_added", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedWritableAggregateRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedWritableAggregateRequestCustomFields.from_dict(_custom_fields)

        patched_writable_aggregate_request = cls(
            prefix=prefix,
            rir=rir,
            tenant=tenant,
            date_added=date_added,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_writable_aggregate_request.additional_properties = d
        return patched_writable_aggregate_request

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
