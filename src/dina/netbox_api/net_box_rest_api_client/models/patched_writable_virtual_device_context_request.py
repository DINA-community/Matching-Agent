import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_writable_virtual_device_context_request_status import (
    PatchedWritableVirtualDeviceContextRequestStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_request import BriefDeviceRequest
    from ..models.brief_ip_address_request import BriefIPAddressRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_writable_virtual_device_context_request_custom_fields import (
        PatchedWritableVirtualDeviceContextRequestCustomFields,
    )


T = TypeVar("T", bound="PatchedWritableVirtualDeviceContextRequest")


@_attrs_define
class PatchedWritableVirtualDeviceContextRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (Union[Unset, str]):
        device (Union['BriefDeviceRequest', Unset, int]):
        identifier (Union[None, Unset, int]):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        primary_ip4 (Union['BriefIPAddressRequest', None, Unset, int]):
        primary_ip6 (Union['BriefIPAddressRequest', None, Unset, int]):
        status (Union[Unset, PatchedWritableVirtualDeviceContextRequestStatus]): * `active` - Active
            * `planned` - Planned
            * `offline` - Offline
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedWritableVirtualDeviceContextRequestCustomFields]):
    """

    name: Union[Unset, str] = UNSET
    device: Union["BriefDeviceRequest", Unset, int] = UNSET
    identifier: Union[None, Unset, int] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    primary_ip4: Union["BriefIPAddressRequest", None, Unset, int] = UNSET
    primary_ip6: Union["BriefIPAddressRequest", None, Unset, int] = UNSET
    status: Union[Unset, PatchedWritableVirtualDeviceContextRequestStatus] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedWritableVirtualDeviceContextRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device_request import BriefDeviceRequest
        from ..models.brief_ip_address_request import BriefIPAddressRequest
        from ..models.brief_tenant_request import BriefTenantRequest

        name = self.name

        device: Union[Unset, dict[str, Any], int]
        if isinstance(self.device, Unset):
            device = UNSET
        elif isinstance(self.device, BriefDeviceRequest):
            device = self.device.to_dict()
        else:
            device = self.device

        identifier: Union[None, Unset, int]
        if isinstance(self.identifier, Unset):
            identifier = UNSET
        else:
            identifier = self.identifier

        tenant: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenantRequest):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        primary_ip4: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.primary_ip4, Unset):
            primary_ip4 = UNSET
        elif isinstance(self.primary_ip4, BriefIPAddressRequest):
            primary_ip4 = self.primary_ip4.to_dict()
        else:
            primary_ip4 = self.primary_ip4

        primary_ip6: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.primary_ip6, Unset):
            primary_ip6 = UNSET
        elif isinstance(self.primary_ip6, BriefIPAddressRequest):
            primary_ip6 = self.primary_ip6.to_dict()
        else:
            primary_ip6 = self.primary_ip6

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

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
        if name is not UNSET:
            field_dict["name"] = name
        if device is not UNSET:
            field_dict["device"] = device
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if primary_ip4 is not UNSET:
            field_dict["primary_ip4"] = primary_ip4
        if primary_ip6 is not UNSET:
            field_dict["primary_ip6"] = primary_ip6
        if status is not UNSET:
            field_dict["status"] = status
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
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        device: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.device, Unset):
            device = UNSET
        elif isinstance(self.device, int):
            device = (None, str(self.device).encode(), "text/plain")
        else:
            device = (None, json.dumps(self.device.to_dict()).encode(), "application/json")

        identifier: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.identifier, Unset):
            identifier = UNSET
        elif isinstance(self.identifier, int):
            identifier = (None, str(self.identifier).encode(), "text/plain")
        else:
            identifier = (None, str(self.identifier).encode(), "text/plain")

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

        primary_ip4: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.primary_ip4, Unset):
            primary_ip4 = UNSET
        elif isinstance(self.primary_ip4, int):
            primary_ip4 = (None, str(self.primary_ip4).encode(), "text/plain")
        elif isinstance(self.primary_ip4, None):
            primary_ip4 = (None, str(self.primary_ip4).encode(), "text/plain")
        elif isinstance(self.primary_ip4, BriefIPAddressRequest):
            primary_ip4 = (None, json.dumps(self.primary_ip4.to_dict()).encode(), "application/json")
        else:
            primary_ip4 = (None, str(self.primary_ip4).encode(), "text/plain")

        primary_ip6: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.primary_ip6, Unset):
            primary_ip6 = UNSET
        elif isinstance(self.primary_ip6, int):
            primary_ip6 = (None, str(self.primary_ip6).encode(), "text/plain")
        elif isinstance(self.primary_ip6, None):
            primary_ip6 = (None, str(self.primary_ip6).encode(), "text/plain")
        elif isinstance(self.primary_ip6, BriefIPAddressRequest):
            primary_ip6 = (None, json.dumps(self.primary_ip6.to_dict()).encode(), "application/json")
        else:
            primary_ip6 = (None, str(self.primary_ip6).encode(), "text/plain")

        status: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

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
        if name is not UNSET:
            field_dict["name"] = name
        if device is not UNSET:
            field_dict["device"] = device
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if primary_ip4 is not UNSET:
            field_dict["primary_ip4"] = primary_ip4
        if primary_ip6 is not UNSET:
            field_dict["primary_ip6"] = primary_ip6
        if status is not UNSET:
            field_dict["status"] = status
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
        from ..models.brief_device_request import BriefDeviceRequest
        from ..models.brief_ip_address_request import BriefIPAddressRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_writable_virtual_device_context_request_custom_fields import (
            PatchedWritableVirtualDeviceContextRequestCustomFields,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_device(data: object) -> Union["BriefDeviceRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_type_1 = BriefDeviceRequest.from_dict(data)

                return device_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDeviceRequest", Unset, int], data)

        device = _parse_device(d.pop("device", UNSET))

        def _parse_identifier(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        identifier = _parse_identifier(d.pop("identifier", UNSET))

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

        def _parse_primary_ip4(data: object) -> Union["BriefIPAddressRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                primary_ip4_type_1_type_1 = BriefIPAddressRequest.from_dict(data)

                return primary_ip4_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefIPAddressRequest", None, Unset, int], data)

        primary_ip4 = _parse_primary_ip4(d.pop("primary_ip4", UNSET))

        def _parse_primary_ip6(data: object) -> Union["BriefIPAddressRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                primary_ip6_type_1_type_1 = BriefIPAddressRequest.from_dict(data)

                return primary_ip6_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefIPAddressRequest", None, Unset, int], data)

        primary_ip6 = _parse_primary_ip6(d.pop("primary_ip6", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, PatchedWritableVirtualDeviceContextRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PatchedWritableVirtualDeviceContextRequestStatus(_status)

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedWritableVirtualDeviceContextRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedWritableVirtualDeviceContextRequestCustomFields.from_dict(_custom_fields)

        patched_writable_virtual_device_context_request = cls(
            name=name,
            device=device,
            identifier=identifier,
            tenant=tenant,
            primary_ip4=primary_ip4,
            primary_ip6=primary_ip6,
            status=status,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_writable_virtual_device_context_request.additional_properties = d
        return patched_writable_virtual_device_context_request

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
