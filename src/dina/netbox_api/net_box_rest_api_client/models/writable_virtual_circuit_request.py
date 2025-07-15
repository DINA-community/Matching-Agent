import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_virtual_circuit_request_status import WritableVirtualCircuitRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_provider_account_request import BriefProviderAccountRequest
    from ..models.brief_provider_network_request import BriefProviderNetworkRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.brief_virtual_circuit_type_request import BriefVirtualCircuitTypeRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.writable_virtual_circuit_request_custom_fields import WritableVirtualCircuitRequestCustomFields


T = TypeVar("T", bound="WritableVirtualCircuitRequest")


@_attrs_define
class WritableVirtualCircuitRequest:
    """Adds support for custom fields and tags.

    Attributes:
        cid (str): Unique circuit ID
        provider_network (Union['BriefProviderNetworkRequest', int]):
        type_ (Union['BriefVirtualCircuitTypeRequest', int]):
        provider_account (Union['BriefProviderAccountRequest', None, Unset, int]):
        status (Union[Unset, WritableVirtualCircuitRequestStatus]): * `planned` - Planned
            * `provisioning` - Provisioning
            * `active` - Active
            * `offline` - Offline
            * `deprovisioning` - Deprovisioning
            * `decommissioned` - Decommissioned
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WritableVirtualCircuitRequestCustomFields]):
    """

    cid: str
    provider_network: Union["BriefProviderNetworkRequest", int]
    type_: Union["BriefVirtualCircuitTypeRequest", int]
    provider_account: Union["BriefProviderAccountRequest", None, Unset, int] = UNSET
    status: Union[Unset, WritableVirtualCircuitRequestStatus] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WritableVirtualCircuitRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_provider_account_request import BriefProviderAccountRequest
        from ..models.brief_provider_network_request import BriefProviderNetworkRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.brief_virtual_circuit_type_request import BriefVirtualCircuitTypeRequest

        cid = self.cid

        provider_network: Union[dict[str, Any], int]
        if isinstance(self.provider_network, BriefProviderNetworkRequest):
            provider_network = self.provider_network.to_dict()
        else:
            provider_network = self.provider_network

        type_: Union[dict[str, Any], int]
        if isinstance(self.type_, BriefVirtualCircuitTypeRequest):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        provider_account: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.provider_account, Unset):
            provider_account = UNSET
        elif isinstance(self.provider_account, BriefProviderAccountRequest):
            provider_account = self.provider_account.to_dict()
        else:
            provider_account = self.provider_account

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
        field_dict.update(
            {
                "cid": cid,
                "provider_network": provider_network,
                "type": type_,
            }
        )
        if provider_account is not UNSET:
            field_dict["provider_account"] = provider_account
        if status is not UNSET:
            field_dict["status"] = status
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
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
        cid = (None, str(self.cid).encode(), "text/plain")

        provider_network: tuple[None, bytes, str]

        if isinstance(self.provider_network, int):
            provider_network = (None, str(self.provider_network).encode(), "text/plain")
        else:
            provider_network = (None, json.dumps(self.provider_network.to_dict()).encode(), "application/json")

        type_: tuple[None, bytes, str]

        if isinstance(self.type_, int):
            type_ = (None, str(self.type_).encode(), "text/plain")
        else:
            type_ = (None, json.dumps(self.type_.to_dict()).encode(), "application/json")

        provider_account: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.provider_account, Unset):
            provider_account = UNSET
        elif isinstance(self.provider_account, int):
            provider_account = (None, str(self.provider_account).encode(), "text/plain")
        elif isinstance(self.provider_account, None):
            provider_account = (None, str(self.provider_account).encode(), "text/plain")
        elif isinstance(self.provider_account, BriefProviderAccountRequest):
            provider_account = (None, json.dumps(self.provider_account.to_dict()).encode(), "application/json")
        else:
            provider_account = (None, str(self.provider_account).encode(), "text/plain")

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

        field_dict.update(
            {
                "cid": cid,
                "provider_network": provider_network,
                "type": type_,
            }
        )
        if provider_account is not UNSET:
            field_dict["provider_account"] = provider_account
        if status is not UNSET:
            field_dict["status"] = status
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
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
        from ..models.brief_provider_account_request import BriefProviderAccountRequest
        from ..models.brief_provider_network_request import BriefProviderNetworkRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.brief_virtual_circuit_type_request import BriefVirtualCircuitTypeRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.writable_virtual_circuit_request_custom_fields import WritableVirtualCircuitRequestCustomFields

        d = dict(src_dict)
        cid = d.pop("cid")

        def _parse_provider_network(data: object) -> Union["BriefProviderNetworkRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_network_type_1 = BriefProviderNetworkRequest.from_dict(data)

                return provider_network_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefProviderNetworkRequest", int], data)

        provider_network = _parse_provider_network(d.pop("provider_network"))

        def _parse_type_(data: object) -> Union["BriefVirtualCircuitTypeRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                type_type_1 = BriefVirtualCircuitTypeRequest.from_dict(data)

                return type_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVirtualCircuitTypeRequest", int], data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_provider_account(data: object) -> Union["BriefProviderAccountRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_account_type_1_type_1 = BriefProviderAccountRequest.from_dict(data)

                return provider_account_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefProviderAccountRequest", None, Unset, int], data)

        provider_account = _parse_provider_account(d.pop("provider_account", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, WritableVirtualCircuitRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WritableVirtualCircuitRequestStatus(_status)

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

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WritableVirtualCircuitRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WritableVirtualCircuitRequestCustomFields.from_dict(_custom_fields)

        writable_virtual_circuit_request = cls(
            cid=cid,
            provider_network=provider_network,
            type_=type_,
            provider_account=provider_account,
            status=status,
            tenant=tenant,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        writable_virtual_circuit_request.additional_properties = d
        return writable_virtual_circuit_request

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
