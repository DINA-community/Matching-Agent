import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_cluster import BriefCluster
    from ..models.brief_config_template import BriefConfigTemplate
    from ..models.brief_device import BriefDevice
    from ..models.brief_device_role import BriefDeviceRole
    from ..models.brief_ip_address import BriefIPAddress
    from ..models.brief_platform import BriefPlatform
    from ..models.brief_site import BriefSite
    from ..models.brief_tenant import BriefTenant
    from ..models.nested_tag import NestedTag
    from ..models.virtual_machine_with_config_context_custom_fields import (
        VirtualMachineWithConfigContextCustomFields,
    )
    from ..models.virtual_machine_with_config_context_status import (
        VirtualMachineWithConfigContextStatus,
    )


T = TypeVar("T", bound="VirtualMachineWithConfigContext")


@_attrs_define
class VirtualMachineWithConfigContext:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        name (str):
        primary_ip (Union['BriefIPAddress', None]):
        config_context (Any):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        interface_count (int):
        virtual_disk_count (int):
        status (Union[Unset, VirtualMachineWithConfigContextStatus]):
        site (Union['BriefSite', None, Unset]):
        cluster (Union['BriefCluster', None, Unset]):
        device (Union['BriefDevice', None, Unset]):
        serial (Union[Unset, str]):
        role (Union['BriefDeviceRole', None, Unset]):
        tenant (Union['BriefTenant', None, Unset]):
        platform (Union['BriefPlatform', None, Unset]):
        primary_ip4 (Union['BriefIPAddress', None, Unset]):
        primary_ip6 (Union['BriefIPAddress', None, Unset]):
        vcpus (Union[None, Unset, float]):
        memory (Union[None, Unset, int]):
        disk (Union[None, Unset, int]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        config_template (Union['BriefConfigTemplate', None, Unset]):
        local_context_data (Union[Unset, Any]): Local config context data takes precedence over source contexts in the
            final rendered config context
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, VirtualMachineWithConfigContextCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    primary_ip: Union["BriefIPAddress", None]
    config_context: Any
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    interface_count: int
    virtual_disk_count: int
    status: Union[Unset, "VirtualMachineWithConfigContextStatus"] = UNSET
    site: Union["BriefSite", None, Unset] = UNSET
    cluster: Union["BriefCluster", None, Unset] = UNSET
    device: Union["BriefDevice", None, Unset] = UNSET
    serial: Union[Unset, str] = UNSET
    role: Union["BriefDeviceRole", None, Unset] = UNSET
    tenant: Union["BriefTenant", None, Unset] = UNSET
    platform: Union["BriefPlatform", None, Unset] = UNSET
    primary_ip4: Union["BriefIPAddress", None, Unset] = UNSET
    primary_ip6: Union["BriefIPAddress", None, Unset] = UNSET
    vcpus: Union[None, Unset, float] = UNSET
    memory: Union[None, Unset, int] = UNSET
    disk: Union[None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    config_template: Union["BriefConfigTemplate", None, Unset] = UNSET
    local_context_data: Union[Unset, Any] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "VirtualMachineWithConfigContextCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_cluster import BriefCluster
        from ..models.brief_config_template import BriefConfigTemplate
        from ..models.brief_device import BriefDevice
        from ..models.brief_device_role import BriefDeviceRole
        from ..models.brief_ip_address import BriefIPAddress
        from ..models.brief_platform import BriefPlatform
        from ..models.brief_site import BriefSite
        from ..models.brief_tenant import BriefTenant

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

        primary_ip: Union[None, dict[str, Any]]
        if isinstance(self.primary_ip, BriefIPAddress):
            primary_ip = self.primary_ip.to_dict()
        else:
            primary_ip = self.primary_ip

        config_context = self.config_context

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

        virtual_disk_count = self.virtual_disk_count

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        site: Union[None, Unset, dict[str, Any]]
        if isinstance(self.site, Unset):
            site = UNSET
        elif isinstance(self.site, BriefSite):
            site = self.site.to_dict()
        else:
            site = self.site

        cluster: Union[None, Unset, dict[str, Any]]
        if isinstance(self.cluster, Unset):
            cluster = UNSET
        elif isinstance(self.cluster, BriefCluster):
            cluster = self.cluster.to_dict()
        else:
            cluster = self.cluster

        device: Union[None, Unset, dict[str, Any]]
        if isinstance(self.device, Unset):
            device = UNSET
        elif isinstance(self.device, BriefDevice):
            device = self.device.to_dict()
        else:
            device = self.device

        serial = self.serial

        role: Union[None, Unset, dict[str, Any]]
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, BriefDeviceRole):
            role = self.role.to_dict()
        else:
            role = self.role

        tenant: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenant):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        platform: Union[None, Unset, dict[str, Any]]
        if isinstance(self.platform, Unset):
            platform = UNSET
        elif isinstance(self.platform, BriefPlatform):
            platform = self.platform.to_dict()
        else:
            platform = self.platform

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

        vcpus: Union[None, Unset, float]
        if isinstance(self.vcpus, Unset):
            vcpus = UNSET
        else:
            vcpus = self.vcpus

        memory: Union[None, Unset, int]
        if isinstance(self.memory, Unset):
            memory = UNSET
        else:
            memory = self.memory

        disk: Union[None, Unset, int]
        if isinstance(self.disk, Unset):
            disk = UNSET
        else:
            disk = self.disk

        description = self.description

        comments = self.comments

        config_template: Union[None, Unset, dict[str, Any]]
        if isinstance(self.config_template, Unset):
            config_template = UNSET
        elif isinstance(self.config_template, BriefConfigTemplate):
            config_template = self.config_template.to_dict()
        else:
            config_template = self.config_template

        local_context_data = self.local_context_data

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
                "primary_ip": primary_ip,
                "config_context": config_context,
                "created": created,
                "last_updated": last_updated,
                "interface_count": interface_count,
                "virtual_disk_count": virtual_disk_count,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if site is not UNSET:
            field_dict["site"] = site
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if device is not UNSET:
            field_dict["device"] = device
        if serial is not UNSET:
            field_dict["serial"] = serial
        if role is not UNSET:
            field_dict["role"] = role
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if platform is not UNSET:
            field_dict["platform"] = platform
        if primary_ip4 is not UNSET:
            field_dict["primary_ip4"] = primary_ip4
        if primary_ip6 is not UNSET:
            field_dict["primary_ip6"] = primary_ip6
        if vcpus is not UNSET:
            field_dict["vcpus"] = vcpus
        if memory is not UNSET:
            field_dict["memory"] = memory
        if disk is not UNSET:
            field_dict["disk"] = disk
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if config_template is not UNSET:
            field_dict["config_template"] = config_template
        if local_context_data is not UNSET:
            field_dict["local_context_data"] = local_context_data
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_cluster import BriefCluster
        from ..models.brief_config_template import BriefConfigTemplate
        from ..models.brief_device import BriefDevice
        from ..models.brief_device_role import BriefDeviceRole
        from ..models.brief_ip_address import BriefIPAddress
        from ..models.brief_platform import BriefPlatform
        from ..models.brief_site import BriefSite
        from ..models.brief_tenant import BriefTenant
        from ..models.nested_tag import NestedTag
        from ..models.virtual_machine_with_config_context_custom_fields import (
            VirtualMachineWithConfigContextCustomFields,
        )
        from ..models.virtual_machine_with_config_context_status import (
            VirtualMachineWithConfigContextStatus,
        )

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

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

        config_context = d.pop("config_context")

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

        virtual_disk_count = d.pop("virtual_disk_count")

        _status = d.pop("status", UNSET)
        status: Union[Unset, VirtualMachineWithConfigContextStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = VirtualMachineWithConfigContextStatus.from_dict(_status)

        def _parse_site(data: object) -> Union["BriefSite", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                site_type_1 = BriefSite.from_dict(data)

                return site_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefSite", None, Unset], data)

        site = _parse_site(d.pop("site", UNSET))

        def _parse_cluster(data: object) -> Union["BriefCluster", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cluster_type_1 = BriefCluster.from_dict(data)

                return cluster_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefCluster", None, Unset], data)

        cluster = _parse_cluster(d.pop("cluster", UNSET))

        def _parse_device(data: object) -> Union["BriefDevice", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_type_1 = BriefDevice.from_dict(data)

                return device_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDevice", None, Unset], data)

        device = _parse_device(d.pop("device", UNSET))

        serial = d.pop("serial", UNSET)

        def _parse_role(data: object) -> Union["BriefDeviceRole", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                role_type_1 = BriefDeviceRole.from_dict(data)

                return role_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDeviceRole", None, Unset], data)

        role = _parse_role(d.pop("role", UNSET))

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

        def _parse_platform(data: object) -> Union["BriefPlatform", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                platform_type_1 = BriefPlatform.from_dict(data)

                return platform_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefPlatform", None, Unset], data)

        platform = _parse_platform(d.pop("platform", UNSET))

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

        def _parse_vcpus(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        vcpus = _parse_vcpus(d.pop("vcpus", UNSET))

        def _parse_memory(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        memory = _parse_memory(d.pop("memory", UNSET))

        def _parse_disk(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        disk = _parse_disk(d.pop("disk", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        def _parse_config_template(
            data: object,
        ) -> Union["BriefConfigTemplate", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_template_type_1 = BriefConfigTemplate.from_dict(data)

                return config_template_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefConfigTemplate", None, Unset], data)

        config_template = _parse_config_template(d.pop("config_template", UNSET))

        local_context_data = d.pop("local_context_data", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, VirtualMachineWithConfigContextCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = VirtualMachineWithConfigContextCustomFields.from_dict(
                _custom_fields
            )

        virtual_machine_with_config_context = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            primary_ip=primary_ip,
            config_context=config_context,
            created=created,
            last_updated=last_updated,
            interface_count=interface_count,
            virtual_disk_count=virtual_disk_count,
            status=status,
            site=site,
            cluster=cluster,
            device=device,
            serial=serial,
            role=role,
            tenant=tenant,
            platform=platform,
            primary_ip4=primary_ip4,
            primary_ip6=primary_ip6,
            vcpus=vcpus,
            memory=memory,
            disk=disk,
            description=description,
            comments=comments,
            config_template=config_template,
            local_context_data=local_context_data,
            tags=tags,
            custom_fields=custom_fields,
        )

        virtual_machine_with_config_context.additional_properties = d
        return virtual_machine_with_config_context

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
