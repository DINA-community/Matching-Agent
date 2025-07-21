import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_provider_account import BriefProviderAccount
    from ..models.brief_provider_network import BriefProviderNetwork
    from ..models.brief_tenant import BriefTenant
    from ..models.brief_virtual_circuit_type import BriefVirtualCircuitType
    from ..models.nested_tag import NestedTag
    from ..models.virtual_circuit_custom_fields import VirtualCircuitCustomFields
    from ..models.virtual_circuit_status import VirtualCircuitStatus


T = TypeVar("T", bound="VirtualCircuit")


@_attrs_define
class VirtualCircuit:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        cid (str): Unique circuit ID
        provider_network (BriefProviderNetwork): Adds support for custom fields and tags.
        type_ (BriefVirtualCircuitType): Adds support for custom fields and tags.
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        provider_account (Union['BriefProviderAccount', None, Unset]):
        status (Union[Unset, VirtualCircuitStatus]):
        tenant (Union['BriefTenant', None, Unset]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, VirtualCircuitCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    cid: str
    provider_network: "BriefProviderNetwork"
    type_: "BriefVirtualCircuitType"
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    provider_account: Union["BriefProviderAccount", None, Unset] = UNSET
    status: Union[Unset, "VirtualCircuitStatus"] = UNSET
    tenant: Union["BriefTenant", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "VirtualCircuitCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_provider_account import BriefProviderAccount
        from ..models.brief_tenant import BriefTenant

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        cid = self.cid

        provider_network = self.provider_network.to_dict()

        type_ = self.type_.to_dict()

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

        provider_account: Union[None, Unset, dict[str, Any]]
        if isinstance(self.provider_account, Unset):
            provider_account = UNSET
        elif isinstance(self.provider_account, BriefProviderAccount):
            provider_account = self.provider_account.to_dict()
        else:
            provider_account = self.provider_account

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
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "cid": cid,
                "provider_network": provider_network,
                "type": type_,
                "created": created,
                "last_updated": last_updated,
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
        from ..models.brief_provider_account import BriefProviderAccount
        from ..models.brief_provider_network import BriefProviderNetwork
        from ..models.brief_tenant import BriefTenant
        from ..models.brief_virtual_circuit_type import BriefVirtualCircuitType
        from ..models.nested_tag import NestedTag
        from ..models.virtual_circuit_custom_fields import VirtualCircuitCustomFields
        from ..models.virtual_circuit_status import VirtualCircuitStatus

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        cid = d.pop("cid")

        provider_network = BriefProviderNetwork.from_dict(d.pop("provider_network"))

        type_ = BriefVirtualCircuitType.from_dict(d.pop("type"))

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

        def _parse_provider_account(
            data: object,
        ) -> Union["BriefProviderAccount", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_account_type_1 = BriefProviderAccount.from_dict(data)

                return provider_account_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefProviderAccount", None, Unset], data)

        provider_account = _parse_provider_account(d.pop("provider_account", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, VirtualCircuitStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = VirtualCircuitStatus.from_dict(_status)

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

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, VirtualCircuitCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = VirtualCircuitCustomFields.from_dict(_custom_fields)

        virtual_circuit = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            cid=cid,
            provider_network=provider_network,
            type_=type_,
            created=created,
            last_updated=last_updated,
            provider_account=provider_account,
            status=status,
            tenant=tenant,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        virtual_circuit.additional_properties = d
        return virtual_circuit

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
