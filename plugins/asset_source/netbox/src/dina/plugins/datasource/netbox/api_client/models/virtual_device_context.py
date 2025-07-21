import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device import BriefDevice
    from ..models.brief_ip_address import BriefIPAddress
    from ..models.brief_tenant import BriefTenant
    from ..models.nested_tag import NestedTag
    from ..models.virtual_device_context_custom_fields import (
        VirtualDeviceContextCustomFields,
    )
    from ..models.virtual_device_context_status import VirtualDeviceContextStatus


T = TypeVar("T", bound="VirtualDeviceContext")


@_attrs_define
class VirtualDeviceContext:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        name (str):
        device (BriefDevice): Adds support for custom fields and tags.
        primary_ip (Union['BriefIPAddress', None]):
        status (VirtualDeviceContextStatus):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        interface_count (int):
        identifier (Union[None, Unset, int]):
        tenant (Union['BriefTenant', None, Unset]):
        primary_ip4 (Union['BriefIPAddress', None, Unset]):
        primary_ip6 (Union['BriefIPAddress', None, Unset]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, VirtualDeviceContextCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    device: "BriefDevice"
    primary_ip: Union["BriefIPAddress", None]
    status: "VirtualDeviceContextStatus"
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    interface_count: int
    identifier: Union[None, Unset, int] = UNSET
    tenant: Union["BriefTenant", None, Unset] = UNSET
    primary_ip4: Union["BriefIPAddress", None, Unset] = UNSET
    primary_ip6: Union["BriefIPAddress", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "VirtualDeviceContextCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_ip_address import BriefIPAddress
        from ..models.brief_tenant import BriefTenant

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

        device = self.device.to_dict()

        primary_ip: Union[None, dict[str, Any]]
        if isinstance(self.primary_ip, BriefIPAddress):
            primary_ip = self.primary_ip.to_dict()
        else:
            primary_ip = self.primary_ip

        status = self.status.to_dict()

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

        interface_count = self.interface_count

        identifier: Union[None, Unset, int]
        if isinstance(self.identifier, Unset):
            identifier = UNSET
        else:
            identifier = self.identifier

        tenant: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenant):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        primary_ip4: Union[None, Unset, dict[str, Any]]
        if isinstance(self.primary_ip4, Unset):
            primary_ip4 = UNSET
        elif isinstance(self.primary_ip4, BriefIPAddress):
            primary_ip4 = self.primary_ip4.to_dict()
        else:
            primary_ip4 = self.primary_ip4

        primary_ip6: Union[None, Unset, dict[str, Any]]
        if isinstance(self.primary_ip6, Unset):
            primary_ip6 = UNSET
        elif isinstance(self.primary_ip6, BriefIPAddress):
            primary_ip6 = self.primary_ip6.to_dict()
        else:
            primary_ip6 = self.primary_ip6

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
                "name": name,
                "device": device,
                "primary_ip": primary_ip,
                "status": status,
                "created": created,
                "last_updated": last_updated,
                "interface_count": interface_count,
            }
        )
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if primary_ip4 is not UNSET:
            field_dict["primary_ip4"] = primary_ip4
        if primary_ip6 is not UNSET:
            field_dict["primary_ip6"] = primary_ip6
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
        from ..models.brief_device import BriefDevice
        from ..models.brief_ip_address import BriefIPAddress
        from ..models.brief_tenant import BriefTenant
        from ..models.nested_tag import NestedTag
        from ..models.virtual_device_context_custom_fields import (
            VirtualDeviceContextCustomFields,
        )
        from ..models.virtual_device_context_status import VirtualDeviceContextStatus

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

        device = BriefDevice.from_dict(d.pop("device"))

        def _parse_primary_ip(data: object) -> Union["BriefIPAddress", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                primary_ip_type_1 = BriefIPAddress.from_dict(data)

                return primary_ip_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefIPAddress", None], data)

        primary_ip = _parse_primary_ip(d.pop("primary_ip"))

        status = VirtualDeviceContextStatus.from_dict(d.pop("status"))

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

        interface_count = d.pop("interface_count")

        def _parse_identifier(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        identifier = _parse_identifier(d.pop("identifier", UNSET))

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

        def _parse_primary_ip4(data: object) -> Union["BriefIPAddress", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                primary_ip4_type_1 = BriefIPAddress.from_dict(data)

                return primary_ip4_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefIPAddress", None, Unset], data)

        primary_ip4 = _parse_primary_ip4(d.pop("primary_ip4", UNSET))

        def _parse_primary_ip6(data: object) -> Union["BriefIPAddress", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                primary_ip6_type_1 = BriefIPAddress.from_dict(data)

                return primary_ip6_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefIPAddress", None, Unset], data)

        primary_ip6 = _parse_primary_ip6(d.pop("primary_ip6", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, VirtualDeviceContextCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = VirtualDeviceContextCustomFields.from_dict(_custom_fields)

        virtual_device_context = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            device=device,
            primary_ip=primary_ip,
            status=status,
            created=created,
            last_updated=last_updated,
            interface_count=interface_count,
            identifier=identifier,
            tenant=tenant,
            primary_ip4=primary_ip4,
            primary_ip6=primary_ip6,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        virtual_device_context.additional_properties = d
        return virtual_device_context

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
