from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.device_with_config_context_request_airflow import DeviceWithConfigContextRequestAirflow
from ..models.device_with_config_context_request_face import DeviceWithConfigContextRequestFace
from ..models.device_with_config_context_request_status import DeviceWithConfigContextRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_cluster_request import BriefClusterRequest
    from ..models.brief_config_template_request import BriefConfigTemplateRequest
    from ..models.brief_device_role_request import BriefDeviceRoleRequest
    from ..models.brief_device_type_request import BriefDeviceTypeRequest
    from ..models.brief_ip_address_request import BriefIPAddressRequest
    from ..models.brief_location_request import BriefLocationRequest
    from ..models.brief_platform_request import BriefPlatformRequest
    from ..models.brief_rack_request import BriefRackRequest
    from ..models.brief_site_request import BriefSiteRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.brief_virtual_chassis_request import BriefVirtualChassisRequest
    from ..models.device_with_config_context_request_custom_fields import DeviceWithConfigContextRequestCustomFields
    from ..models.nested_tag_request import NestedTagRequest


T = TypeVar("T", bound="DeviceWithConfigContextRequest")


@_attrs_define
class DeviceWithConfigContextRequest:
    """Adds support for custom fields and tags.

    Attributes:
        device_type (Union['BriefDeviceTypeRequest', int]):
        role (Union['BriefDeviceRoleRequest', int]):
        site (Union['BriefSiteRequest', int]):
        name (Union[None, Unset, str]):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        platform (Union['BriefPlatformRequest', None, Unset, int]):
        serial (Union[Unset, str]): Chassis serial number, assigned by the manufacturer
        asset_tag (Union[None, Unset, str]): A unique tag used to identify this device
        location (Union['BriefLocationRequest', None, Unset, int]):
        rack (Union['BriefRackRequest', None, Unset, int]):
        position (Union[None, Unset, float]):
        face (Union[Unset, DeviceWithConfigContextRequestFace]): * `front` - Front
            * `rear` - Rear
        latitude (Union[None, Unset, float]): GPS coordinate in decimal format (xx.yyyyyy)
        longitude (Union[None, Unset, float]): GPS coordinate in decimal format (xx.yyyyyy)
        status (Union[Unset, DeviceWithConfigContextRequestStatus]): * `offline` - Offline
            * `active` - Active
            * `planned` - Planned
            * `staged` - Staged
            * `failed` - Failed
            * `inventory` - Inventory
            * `decommissioning` - Decommissioning
        airflow (Union[Unset, DeviceWithConfigContextRequestAirflow]): * `front-to-rear` - Front to rear
            * `rear-to-front` - Rear to front
            * `left-to-right` - Left to right
            * `right-to-left` - Right to left
            * `side-to-rear` - Side to rear
            * `rear-to-side` - Rear to side
            * `bottom-to-top` - Bottom to top
            * `top-to-bottom` - Top to bottom
            * `passive` - Passive
            * `mixed` - Mixed
        primary_ip4 (Union['BriefIPAddressRequest', None, Unset, int]):
        primary_ip6 (Union['BriefIPAddressRequest', None, Unset, int]):
        oob_ip (Union['BriefIPAddressRequest', None, Unset, int]):
        cluster (Union['BriefClusterRequest', None, Unset, int]):
        virtual_chassis (Union['BriefVirtualChassisRequest', None, Unset, int]):
        vc_position (Union[None, Unset, int]):
        vc_priority (Union[None, Unset, int]): Virtual chassis master election priority
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        config_template (Union['BriefConfigTemplateRequest', None, Unset, int]):
        local_context_data (Union[Unset, Any]): Local config context data takes precedence over source contexts in the
            final rendered config context
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, DeviceWithConfigContextRequestCustomFields]):
    """

    device_type: Union["BriefDeviceTypeRequest", int]
    role: Union["BriefDeviceRoleRequest", int]
    site: Union["BriefSiteRequest", int]
    name: Union[None, Unset, str] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    platform: Union["BriefPlatformRequest", None, Unset, int] = UNSET
    serial: Union[Unset, str] = UNSET
    asset_tag: Union[None, Unset, str] = UNSET
    location: Union["BriefLocationRequest", None, Unset, int] = UNSET
    rack: Union["BriefRackRequest", None, Unset, int] = UNSET
    position: Union[None, Unset, float] = UNSET
    face: Union[Unset, DeviceWithConfigContextRequestFace] = UNSET
    latitude: Union[None, Unset, float] = UNSET
    longitude: Union[None, Unset, float] = UNSET
    status: Union[Unset, DeviceWithConfigContextRequestStatus] = UNSET
    airflow: Union[Unset, DeviceWithConfigContextRequestAirflow] = UNSET
    primary_ip4: Union["BriefIPAddressRequest", None, Unset, int] = UNSET
    primary_ip6: Union["BriefIPAddressRequest", None, Unset, int] = UNSET
    oob_ip: Union["BriefIPAddressRequest", None, Unset, int] = UNSET
    cluster: Union["BriefClusterRequest", None, Unset, int] = UNSET
    virtual_chassis: Union["BriefVirtualChassisRequest", None, Unset, int] = UNSET
    vc_position: Union[None, Unset, int] = UNSET
    vc_priority: Union[None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    config_template: Union["BriefConfigTemplateRequest", None, Unset, int] = UNSET
    local_context_data: Union[Unset, Any] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "DeviceWithConfigContextRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_cluster_request import BriefClusterRequest
        from ..models.brief_config_template_request import BriefConfigTemplateRequest
        from ..models.brief_device_role_request import BriefDeviceRoleRequest
        from ..models.brief_device_type_request import BriefDeviceTypeRequest
        from ..models.brief_ip_address_request import BriefIPAddressRequest
        from ..models.brief_location_request import BriefLocationRequest
        from ..models.brief_platform_request import BriefPlatformRequest
        from ..models.brief_rack_request import BriefRackRequest
        from ..models.brief_site_request import BriefSiteRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.brief_virtual_chassis_request import BriefVirtualChassisRequest

        device_type: Union[dict[str, Any], int]
        if isinstance(self.device_type, BriefDeviceTypeRequest):
            device_type = self.device_type.to_dict()
        else:
            device_type = self.device_type

        role: Union[dict[str, Any], int]
        if isinstance(self.role, BriefDeviceRoleRequest):
            role = self.role.to_dict()
        else:
            role = self.role

        site: Union[dict[str, Any], int]
        if isinstance(self.site, BriefSiteRequest):
            site = self.site.to_dict()
        else:
            site = self.site

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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

        serial = self.serial

        asset_tag: Union[None, Unset, str]
        if isinstance(self.asset_tag, Unset):
            asset_tag = UNSET
        else:
            asset_tag = self.asset_tag

        location: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, BriefLocationRequest):
            location = self.location.to_dict()
        else:
            location = self.location

        rack: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.rack, Unset):
            rack = UNSET
        elif isinstance(self.rack, BriefRackRequest):
            rack = self.rack.to_dict()
        else:
            rack = self.rack

        position: Union[None, Unset, float]
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        face: Union[Unset, str] = UNSET
        if not isinstance(self.face, Unset):
            face = self.face.value

        latitude: Union[None, Unset, float]
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: Union[None, Unset, float]
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        airflow: Union[Unset, str] = UNSET
        if not isinstance(self.airflow, Unset):
            airflow = self.airflow.value

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

        oob_ip: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.oob_ip, Unset):
            oob_ip = UNSET
        elif isinstance(self.oob_ip, BriefIPAddressRequest):
            oob_ip = self.oob_ip.to_dict()
        else:
            oob_ip = self.oob_ip

        cluster: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.cluster, Unset):
            cluster = UNSET
        elif isinstance(self.cluster, BriefClusterRequest):
            cluster = self.cluster.to_dict()
        else:
            cluster = self.cluster

        virtual_chassis: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.virtual_chassis, Unset):
            virtual_chassis = UNSET
        elif isinstance(self.virtual_chassis, BriefVirtualChassisRequest):
            virtual_chassis = self.virtual_chassis.to_dict()
        else:
            virtual_chassis = self.virtual_chassis

        vc_position: Union[None, Unset, int]
        if isinstance(self.vc_position, Unset):
            vc_position = UNSET
        else:
            vc_position = self.vc_position

        vc_priority: Union[None, Unset, int]
        if isinstance(self.vc_priority, Unset):
            vc_priority = UNSET
        else:
            vc_priority = self.vc_priority

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
                "device_type": device_type,
                "role": role,
                "site": site,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if platform is not UNSET:
            field_dict["platform"] = platform
        if serial is not UNSET:
            field_dict["serial"] = serial
        if asset_tag is not UNSET:
            field_dict["asset_tag"] = asset_tag
        if location is not UNSET:
            field_dict["location"] = location
        if rack is not UNSET:
            field_dict["rack"] = rack
        if position is not UNSET:
            field_dict["position"] = position
        if face is not UNSET:
            field_dict["face"] = face
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if status is not UNSET:
            field_dict["status"] = status
        if airflow is not UNSET:
            field_dict["airflow"] = airflow
        if primary_ip4 is not UNSET:
            field_dict["primary_ip4"] = primary_ip4
        if primary_ip6 is not UNSET:
            field_dict["primary_ip6"] = primary_ip6
        if oob_ip is not UNSET:
            field_dict["oob_ip"] = oob_ip
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if virtual_chassis is not UNSET:
            field_dict["virtual_chassis"] = virtual_chassis
        if vc_position is not UNSET:
            field_dict["vc_position"] = vc_position
        if vc_priority is not UNSET:
            field_dict["vc_priority"] = vc_priority
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
        from ..models.brief_device_role_request import BriefDeviceRoleRequest
        from ..models.brief_device_type_request import BriefDeviceTypeRequest
        from ..models.brief_ip_address_request import BriefIPAddressRequest
        from ..models.brief_location_request import BriefLocationRequest
        from ..models.brief_platform_request import BriefPlatformRequest
        from ..models.brief_rack_request import BriefRackRequest
        from ..models.brief_site_request import BriefSiteRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.brief_virtual_chassis_request import BriefVirtualChassisRequest
        from ..models.device_with_config_context_request_custom_fields import DeviceWithConfigContextRequestCustomFields
        from ..models.nested_tag_request import NestedTagRequest

        d = dict(src_dict)

        def _parse_device_type(data: object) -> Union["BriefDeviceTypeRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_type_type_1 = BriefDeviceTypeRequest.from_dict(data)

                return device_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDeviceTypeRequest", int], data)

        device_type = _parse_device_type(d.pop("device_type"))

        def _parse_role(data: object) -> Union["BriefDeviceRoleRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                role_type_1 = BriefDeviceRoleRequest.from_dict(data)

                return role_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDeviceRoleRequest", int], data)

        role = _parse_role(d.pop("role"))

        def _parse_site(data: object) -> Union["BriefSiteRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                site_type_1 = BriefSiteRequest.from_dict(data)

                return site_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefSiteRequest", int], data)

        site = _parse_site(d.pop("site"))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

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

        def _parse_platform(data: object) -> Union["BriefPlatformRequest", None, Unset, int]:
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

        serial = d.pop("serial", UNSET)

        def _parse_asset_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_tag = _parse_asset_tag(d.pop("asset_tag", UNSET))

        def _parse_location(data: object) -> Union["BriefLocationRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_1_type_1 = BriefLocationRequest.from_dict(data)

                return location_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefLocationRequest", None, Unset, int], data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_rack(data: object) -> Union["BriefRackRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rack_type_1_type_1 = BriefRackRequest.from_dict(data)

                return rack_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefRackRequest", None, Unset, int], data)

        rack = _parse_rack(d.pop("rack", UNSET))

        def _parse_position(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        position = _parse_position(d.pop("position", UNSET))

        _face = d.pop("face", UNSET)
        face: Union[Unset, DeviceWithConfigContextRequestFace]
        if isinstance(_face, Unset):
            face = UNSET
        else:
            face = DeviceWithConfigContextRequestFace(_face)

        def _parse_latitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, DeviceWithConfigContextRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DeviceWithConfigContextRequestStatus(_status)

        _airflow = d.pop("airflow", UNSET)
        airflow: Union[Unset, DeviceWithConfigContextRequestAirflow]
        if isinstance(_airflow, Unset):
            airflow = UNSET
        else:
            airflow = DeviceWithConfigContextRequestAirflow(_airflow)

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

        def _parse_oob_ip(data: object) -> Union["BriefIPAddressRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                oob_ip_type_1_type_1 = BriefIPAddressRequest.from_dict(data)

                return oob_ip_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefIPAddressRequest", None, Unset, int], data)

        oob_ip = _parse_oob_ip(d.pop("oob_ip", UNSET))

        def _parse_cluster(data: object) -> Union["BriefClusterRequest", None, Unset, int]:
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

        def _parse_virtual_chassis(data: object) -> Union["BriefVirtualChassisRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                virtual_chassis_type_1_type_1 = BriefVirtualChassisRequest.from_dict(data)

                return virtual_chassis_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVirtualChassisRequest", None, Unset, int], data)

        virtual_chassis = _parse_virtual_chassis(d.pop("virtual_chassis", UNSET))

        def _parse_vc_position(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        vc_position = _parse_vc_position(d.pop("vc_position", UNSET))

        def _parse_vc_priority(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        vc_priority = _parse_vc_priority(d.pop("vc_priority", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        def _parse_config_template(data: object) -> Union["BriefConfigTemplateRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_template_type_1_type_1 = BriefConfigTemplateRequest.from_dict(data)

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
        custom_fields: Union[Unset, DeviceWithConfigContextRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = DeviceWithConfigContextRequestCustomFields.from_dict(_custom_fields)

        device_with_config_context_request = cls(
            device_type=device_type,
            role=role,
            site=site,
            name=name,
            tenant=tenant,
            platform=platform,
            serial=serial,
            asset_tag=asset_tag,
            location=location,
            rack=rack,
            position=position,
            face=face,
            latitude=latitude,
            longitude=longitude,
            status=status,
            airflow=airflow,
            primary_ip4=primary_ip4,
            primary_ip6=primary_ip6,
            oob_ip=oob_ip,
            cluster=cluster,
            virtual_chassis=virtual_chassis,
            vc_position=vc_position,
            vc_priority=vc_priority,
            description=description,
            comments=comments,
            config_template=config_template,
            local_context_data=local_context_data,
            tags=tags,
            custom_fields=custom_fields,
        )

        device_with_config_context_request.additional_properties = d
        return device_with_config_context_request

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
