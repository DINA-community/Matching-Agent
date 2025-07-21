from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.virtual_machine_with_config_context_request_status import (
    VirtualMachineWithConfigContextRequestStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_cluster_request import BriefClusterRequest
    from ..models.brief_config_template_request import BriefConfigTemplateRequest
    from ..models.brief_device_request import BriefDeviceRequest
    from ..models.brief_device_role_request import BriefDeviceRoleRequest
    from ..models.brief_ip_address_request import BriefIPAddressRequest
    from ..models.brief_platform_request import BriefPlatformRequest
    from ..models.brief_site_request import BriefSiteRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.virtual_machine_with_config_context_request_custom_fields import (
        VirtualMachineWithConfigContextRequestCustomFields,
    )


T = TypeVar("T", bound="VirtualMachineWithConfigContextRequest")


@_attrs_define
class VirtualMachineWithConfigContextRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str):
        status (Union[Unset, VirtualMachineWithConfigContextRequestStatus]): * `offline` - Offline
            * `active` - Active
            * `planned` - Planned
            * `staged` - Staged
            * `failed` - Failed
            * `decommissioning` - Decommissioning
            * `paused` - Paused
        site (Union['BriefSiteRequest', None, Unset, int]):
        cluster (Union['BriefClusterRequest', None, Unset, int]):
        device (Union['BriefDeviceRequest', None, Unset, int]):
        serial (Union[Unset, str]):
        role (Union['BriefDeviceRoleRequest', None, Unset, int]):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        platform (Union['BriefPlatformRequest', None, Unset, int]):
        primary_ip4 (Union['BriefIPAddressRequest', None, Unset, int]):
        primary_ip6 (Union['BriefIPAddressRequest', None, Unset, int]):
        vcpus (Union[None, Unset, float]):
        memory (Union[None, Unset, int]):
        disk (Union[None, Unset, int]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        config_template (Union['BriefConfigTemplateRequest', None, Unset, int]):
        local_context_data (Union[Unset, Any]): Local config context data takes precedence over source contexts in the
            final rendered config context
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, VirtualMachineWithConfigContextRequestCustomFields]):
    """

    name: str
    status: Union[Unset, VirtualMachineWithConfigContextRequestStatus] = UNSET
    site: Union["BriefSiteRequest", None, Unset, int] = UNSET
    cluster: Union["BriefClusterRequest", None, Unset, int] = UNSET
    device: Union["BriefDeviceRequest", None, Unset, int] = UNSET
    serial: Union[Unset, str] = UNSET
    role: Union["BriefDeviceRoleRequest", None, Unset, int] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    platform: Union["BriefPlatformRequest", None, Unset, int] = UNSET
    primary_ip4: Union["BriefIPAddressRequest", None, Unset, int] = UNSET
    primary_ip6: Union["BriefIPAddressRequest", None, Unset, int] = UNSET
    vcpus: Union[None, Unset, float] = UNSET
    memory: Union[None, Unset, int] = UNSET
    disk: Union[None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    config_template: Union["BriefConfigTemplateRequest", None, Unset, int] = UNSET
    local_context_data: Union[Unset, Any] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[
        Unset, "VirtualMachineWithConfigContextRequestCustomFields"
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_cluster_request import BriefClusterRequest
        from ..models.brief_config_template_request import BriefConfigTemplateRequest
        from ..models.brief_device_request import BriefDeviceRequest
        from ..models.brief_device_role_request import BriefDeviceRoleRequest
        from ..models.brief_ip_address_request import BriefIPAddressRequest
        from ..models.brief_platform_request import BriefPlatformRequest
        from ..models.brief_site_request import BriefSiteRequest
        from ..models.brief_tenant_request import BriefTenantRequest

        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        site: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.site, Unset):
            site = UNSET
        elif isinstance(self.site, BriefSiteRequest):
            site = self.site.to_dict()
        else:
            site = self.site

        cluster: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.cluster, Unset):
            cluster = UNSET
        elif isinstance(self.cluster, BriefClusterRequest):
            cluster = self.cluster.to_dict()
        else:
            cluster = self.cluster

        device: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.device, Unset):
            device = UNSET
        elif isinstance(self.device, BriefDeviceRequest):
            device = self.device.to_dict()
        else:
            device = self.device

        serial = self.serial

        role: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, BriefDeviceRoleRequest):
            role = self.role.to_dict()
        else:
            role = self.role

        tenant: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenantRequest):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        platform: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.platform, Unset):
            platform = UNSET
        elif isinstance(self.platform, BriefPlatformRequest):
            platform = self.platform.to_dict()
        else:
            platform = self.platform

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

        config_template: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.config_template, Unset):
            config_template = UNSET
        elif isinstance(self.config_template, BriefConfigTemplateRequest):
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
                "name": name,
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
        from ..models.brief_cluster_request import BriefClusterRequest
        from ..models.brief_config_template_request import BriefConfigTemplateRequest
        from ..models.brief_device_request import BriefDeviceRequest
        from ..models.brief_device_role_request import BriefDeviceRoleRequest
        from ..models.brief_ip_address_request import BriefIPAddressRequest
        from ..models.brief_platform_request import BriefPlatformRequest
        from ..models.brief_site_request import BriefSiteRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.virtual_machine_with_config_context_request_custom_fields import (
            VirtualMachineWithConfigContextRequestCustomFields,
        )

        d = dict(src_dict)
        name = d.pop("name")

        _status = d.pop("status", UNSET)
        status: Union[Unset, VirtualMachineWithConfigContextRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = VirtualMachineWithConfigContextRequestStatus(_status)

        def _parse_site(data: object) -> Union["BriefSiteRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                site_type_1_type_1 = BriefSiteRequest.from_dict(data)

                return site_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefSiteRequest", None, Unset, int], data)

        site = _parse_site(d.pop("site", UNSET))

        def _parse_cluster(
            data: object,
        ) -> Union["BriefClusterRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cluster_type_1_type_1 = BriefClusterRequest.from_dict(data)

                return cluster_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefClusterRequest", None, Unset, int], data)

        cluster = _parse_cluster(d.pop("cluster", UNSET))

        def _parse_device(
            data: object,
        ) -> Union["BriefDeviceRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_type_1_type_1 = BriefDeviceRequest.from_dict(data)

                return device_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDeviceRequest", None, Unset, int], data)

        device = _parse_device(d.pop("device", UNSET))

        serial = d.pop("serial", UNSET)

        def _parse_role(
            data: object,
        ) -> Union["BriefDeviceRoleRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                role_type_1_type_1 = BriefDeviceRoleRequest.from_dict(data)

                return role_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDeviceRoleRequest", None, Unset, int], data)

        role = _parse_role(d.pop("role", UNSET))

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

        def _parse_platform(
            data: object,
        ) -> Union["BriefPlatformRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                platform_type_1_type_1 = BriefPlatformRequest.from_dict(data)

                return platform_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefPlatformRequest", None, Unset, int], data)

        platform = _parse_platform(d.pop("platform", UNSET))

        def _parse_primary_ip4(
            data: object,
        ) -> Union["BriefIPAddressRequest", None, Unset, int]:
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

        def _parse_primary_ip6(
            data: object,
        ) -> Union["BriefIPAddressRequest", None, Unset, int]:
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
        ) -> Union["BriefConfigTemplateRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_template_type_1_type_1 = BriefConfigTemplateRequest.from_dict(
                    data
                )

                return config_template_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefConfigTemplateRequest", None, Unset, int], data)

        config_template = _parse_config_template(d.pop("config_template", UNSET))

        local_context_data = d.pop("local_context_data", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, VirtualMachineWithConfigContextRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = (
                VirtualMachineWithConfigContextRequestCustomFields.from_dict(
                    _custom_fields
                )
            )

        virtual_machine_with_config_context_request = cls(
            name=name,
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

        virtual_machine_with_config_context_request.additional_properties = d
        return virtual_machine_with_config_context_request

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
