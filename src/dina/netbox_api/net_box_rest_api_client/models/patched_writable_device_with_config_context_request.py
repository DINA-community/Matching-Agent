import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_writable_device_with_config_context_request_airflow_type_1 import (
    PatchedWritableDeviceWithConfigContextRequestAirflowType1,
)
from ..models.patched_writable_device_with_config_context_request_airflow_type_2_type_1 import (
    PatchedWritableDeviceWithConfigContextRequestAirflowType2Type1,
)
from ..models.patched_writable_device_with_config_context_request_airflow_type_3_type_1 import (
    PatchedWritableDeviceWithConfigContextRequestAirflowType3Type1,
)
from ..models.patched_writable_device_with_config_context_request_rack_face import (
    PatchedWritableDeviceWithConfigContextRequestRackFace,
)
from ..models.patched_writable_device_with_config_context_request_status import (
    PatchedWritableDeviceWithConfigContextRequestStatus,
)
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
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_writable_device_with_config_context_request_custom_fields import (
        PatchedWritableDeviceWithConfigContextRequestCustomFields,
    )


T = TypeVar("T", bound="PatchedWritableDeviceWithConfigContextRequest")


@_attrs_define
class PatchedWritableDeviceWithConfigContextRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (Union[None, Unset, str]):
        device_type (Union['BriefDeviceTypeRequest', Unset, int]):
        role (Union['BriefDeviceRoleRequest', Unset, int]):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        platform (Union['BriefPlatformRequest', None, Unset, int]):
        serial (Union[Unset, str]): Chassis serial number, assigned by the manufacturer
        asset_tag (Union[None, Unset, str]): A unique tag used to identify this device
        site (Union['BriefSiteRequest', Unset, int]):
        location (Union['BriefLocationRequest', None, Unset, int]):
        rack (Union['BriefRackRequest', None, Unset, int]):
        position (Union[None, Unset, float]):
        face (Union[None, PatchedWritableDeviceWithConfigContextRequestRackFace, Unset]): * `front` - Front
            * `rear` - Rear
        latitude (Union[None, Unset, float]): GPS coordinate in decimal format (xx.yyyyyy)
        longitude (Union[None, Unset, float]): GPS coordinate in decimal format (xx.yyyyyy)
        status (Union[Unset, PatchedWritableDeviceWithConfigContextRequestStatus]): * `offline` - Offline
            * `active` - Active
            * `planned` - Planned
            * `staged` - Staged
            * `failed` - Failed
            * `inventory` - Inventory
            * `decommissioning` - Decommissioning
        airflow (Union[None, PatchedWritableDeviceWithConfigContextRequestAirflowType1,
            PatchedWritableDeviceWithConfigContextRequestAirflowType2Type1,
            PatchedWritableDeviceWithConfigContextRequestAirflowType3Type1, Unset]): * `front-to-rear` - Front to rear
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
        custom_fields (Union[Unset, PatchedWritableDeviceWithConfigContextRequestCustomFields]):
    """

    name: Union[None, Unset, str] = UNSET
    device_type: Union["BriefDeviceTypeRequest", Unset, int] = UNSET
    role: Union["BriefDeviceRoleRequest", Unset, int] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    platform: Union["BriefPlatformRequest", None, Unset, int] = UNSET
    serial: Union[Unset, str] = UNSET
    asset_tag: Union[None, Unset, str] = UNSET
    site: Union["BriefSiteRequest", Unset, int] = UNSET
    location: Union["BriefLocationRequest", None, Unset, int] = UNSET
    rack: Union["BriefRackRequest", None, Unset, int] = UNSET
    position: Union[None, Unset, float] = UNSET
    face: Union[None, PatchedWritableDeviceWithConfigContextRequestRackFace, Unset] = UNSET
    latitude: Union[None, Unset, float] = UNSET
    longitude: Union[None, Unset, float] = UNSET
    status: Union[Unset, PatchedWritableDeviceWithConfigContextRequestStatus] = UNSET
    airflow: Union[
        None,
        PatchedWritableDeviceWithConfigContextRequestAirflowType1,
        PatchedWritableDeviceWithConfigContextRequestAirflowType2Type1,
        PatchedWritableDeviceWithConfigContextRequestAirflowType3Type1,
        Unset,
    ] = UNSET
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
    custom_fields: Union[Unset, "PatchedWritableDeviceWithConfigContextRequestCustomFields"] = UNSET
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

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        device_type: Union[Unset, dict[str, Any], int]
        if isinstance(self.device_type, Unset):
            device_type = UNSET
        elif isinstance(self.device_type, BriefDeviceTypeRequest):
            device_type = self.device_type.to_dict()
        else:
            device_type = self.device_type

        role: Union[Unset, dict[str, Any], int]
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

        serial = self.serial

        asset_tag: Union[None, Unset, str]
        if isinstance(self.asset_tag, Unset):
            asset_tag = UNSET
        else:
            asset_tag = self.asset_tag

        site: Union[Unset, dict[str, Any], int]
        if isinstance(self.site, Unset):
            site = UNSET
        elif isinstance(self.site, BriefSiteRequest):
            site = self.site.to_dict()
        else:
            site = self.site

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

        face: Union[None, Unset, str]
        if isinstance(self.face, Unset):
            face = UNSET
        elif isinstance(self.face, PatchedWritableDeviceWithConfigContextRequestRackFace):
            face = self.face.value
        elif isinstance(self.face, PatchedWritableDeviceWithConfigContextRequestRackFace):
            face = self.face.value
        elif isinstance(self.face, PatchedWritableDeviceWithConfigContextRequestRackFace):
            face = self.face.value
        else:
            face = self.face

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

        airflow: Union[None, Unset, str]
        if isinstance(self.airflow, Unset):
            airflow = UNSET
        elif isinstance(self.airflow, PatchedWritableDeviceWithConfigContextRequestAirflowType1):
            airflow = self.airflow.value
        elif isinstance(self.airflow, PatchedWritableDeviceWithConfigContextRequestAirflowType2Type1):
            airflow = self.airflow.value
        elif isinstance(self.airflow, PatchedWritableDeviceWithConfigContextRequestAirflowType3Type1):
            airflow = self.airflow.value
        else:
            airflow = self.airflow

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
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if role is not UNSET:
            field_dict["role"] = role
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if platform is not UNSET:
            field_dict["platform"] = platform
        if serial is not UNSET:
            field_dict["serial"] = serial
        if asset_tag is not UNSET:
            field_dict["asset_tag"] = asset_tag
        if site is not UNSET:
            field_dict["site"] = site
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

    def to_multipart(self) -> dict[str, Any]:
        name: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.name, Unset):
            name = UNSET
        elif isinstance(self.name, str):
            name = (None, str(self.name).encode(), "text/plain")
        else:
            name = (None, str(self.name).encode(), "text/plain")

        device_type: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.device_type, Unset):
            device_type = UNSET
        elif isinstance(self.device_type, int):
            device_type = (None, str(self.device_type).encode(), "text/plain")
        else:
            device_type = (None, json.dumps(self.device_type.to_dict()).encode(), "application/json")

        role: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, int):
            role = (None, str(self.role).encode(), "text/plain")
        else:
            role = (None, json.dumps(self.role.to_dict()).encode(), "application/json")

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

        platform: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.platform, Unset):
            platform = UNSET
        elif isinstance(self.platform, int):
            platform = (None, str(self.platform).encode(), "text/plain")
        elif isinstance(self.platform, None):
            platform = (None, str(self.platform).encode(), "text/plain")
        elif isinstance(self.platform, BriefPlatformRequest):
            platform = (None, json.dumps(self.platform.to_dict()).encode(), "application/json")
        else:
            platform = (None, str(self.platform).encode(), "text/plain")

        serial = self.serial if isinstance(self.serial, Unset) else (None, str(self.serial).encode(), "text/plain")

        asset_tag: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.asset_tag, Unset):
            asset_tag = UNSET
        elif isinstance(self.asset_tag, str):
            asset_tag = (None, str(self.asset_tag).encode(), "text/plain")
        else:
            asset_tag = (None, str(self.asset_tag).encode(), "text/plain")

        site: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.site, Unset):
            site = UNSET
        elif isinstance(self.site, int):
            site = (None, str(self.site).encode(), "text/plain")
        else:
            site = (None, json.dumps(self.site.to_dict()).encode(), "application/json")

        location: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, int):
            location = (None, str(self.location).encode(), "text/plain")
        elif isinstance(self.location, None):
            location = (None, str(self.location).encode(), "text/plain")
        elif isinstance(self.location, BriefLocationRequest):
            location = (None, json.dumps(self.location.to_dict()).encode(), "application/json")
        else:
            location = (None, str(self.location).encode(), "text/plain")

        rack: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.rack, Unset):
            rack = UNSET
        elif isinstance(self.rack, int):
            rack = (None, str(self.rack).encode(), "text/plain")
        elif isinstance(self.rack, None):
            rack = (None, str(self.rack).encode(), "text/plain")
        elif isinstance(self.rack, BriefRackRequest):
            rack = (None, json.dumps(self.rack.to_dict()).encode(), "application/json")
        else:
            rack = (None, str(self.rack).encode(), "text/plain")

        position: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.position, Unset):
            position = UNSET
        elif isinstance(self.position, float):
            position = (None, str(self.position).encode(), "text/plain")
        else:
            position = (None, str(self.position).encode(), "text/plain")

        face: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.face, Unset):
            face = UNSET
        elif isinstance(self.face, None):
            face = (None, str(self.face).encode(), "text/plain")
        elif isinstance(self.face, PatchedWritableDeviceWithConfigContextRequestRackFace):
            face = (None, str(self.face.value).encode(), "text/plain")
        elif isinstance(self.face, None):
            face = (None, str(self.face).encode(), "text/plain")
        elif isinstance(self.face, PatchedWritableDeviceWithConfigContextRequestRackFace):
            face = (None, str(self.face.value).encode(), "text/plain")
        elif isinstance(self.face, None):
            face = (None, str(self.face).encode(), "text/plain")
        else:
            face = (None, str(self.face.value).encode(), "text/plain")

        latitude: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.latitude, Unset):
            latitude = UNSET
        elif isinstance(self.latitude, float):
            latitude = (None, str(self.latitude).encode(), "text/plain")
        else:
            latitude = (None, str(self.latitude).encode(), "text/plain")

        longitude: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.longitude, Unset):
            longitude = UNSET
        elif isinstance(self.longitude, float):
            longitude = (None, str(self.longitude).encode(), "text/plain")
        else:
            longitude = (None, str(self.longitude).encode(), "text/plain")

        status: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

        airflow: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.airflow, Unset):
            airflow = UNSET
        elif isinstance(self.airflow, None):
            airflow = (None, str(self.airflow).encode(), "text/plain")
        elif isinstance(self.airflow, PatchedWritableDeviceWithConfigContextRequestAirflowType1):
            airflow = (None, str(self.airflow.value).encode(), "text/plain")
        elif isinstance(self.airflow, None):
            airflow = (None, str(self.airflow).encode(), "text/plain")
        elif isinstance(self.airflow, PatchedWritableDeviceWithConfigContextRequestAirflowType2Type1):
            airflow = (None, str(self.airflow.value).encode(), "text/plain")
        elif isinstance(self.airflow, None):
            airflow = (None, str(self.airflow).encode(), "text/plain")
        else:
            airflow = (None, str(self.airflow.value).encode(), "text/plain")

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

        oob_ip: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.oob_ip, Unset):
            oob_ip = UNSET
        elif isinstance(self.oob_ip, int):
            oob_ip = (None, str(self.oob_ip).encode(), "text/plain")
        elif isinstance(self.oob_ip, None):
            oob_ip = (None, str(self.oob_ip).encode(), "text/plain")
        elif isinstance(self.oob_ip, BriefIPAddressRequest):
            oob_ip = (None, json.dumps(self.oob_ip.to_dict()).encode(), "application/json")
        else:
            oob_ip = (None, str(self.oob_ip).encode(), "text/plain")

        cluster: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.cluster, Unset):
            cluster = UNSET
        elif isinstance(self.cluster, int):
            cluster = (None, str(self.cluster).encode(), "text/plain")
        elif isinstance(self.cluster, None):
            cluster = (None, str(self.cluster).encode(), "text/plain")
        elif isinstance(self.cluster, BriefClusterRequest):
            cluster = (None, json.dumps(self.cluster.to_dict()).encode(), "application/json")
        else:
            cluster = (None, str(self.cluster).encode(), "text/plain")

        virtual_chassis: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.virtual_chassis, Unset):
            virtual_chassis = UNSET
        elif isinstance(self.virtual_chassis, int):
            virtual_chassis = (None, str(self.virtual_chassis).encode(), "text/plain")
        elif isinstance(self.virtual_chassis, None):
            virtual_chassis = (None, str(self.virtual_chassis).encode(), "text/plain")
        elif isinstance(self.virtual_chassis, BriefVirtualChassisRequest):
            virtual_chassis = (None, json.dumps(self.virtual_chassis.to_dict()).encode(), "application/json")
        else:
            virtual_chassis = (None, str(self.virtual_chassis).encode(), "text/plain")

        vc_position: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.vc_position, Unset):
            vc_position = UNSET
        elif isinstance(self.vc_position, int):
            vc_position = (None, str(self.vc_position).encode(), "text/plain")
        else:
            vc_position = (None, str(self.vc_position).encode(), "text/plain")

        vc_priority: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.vc_priority, Unset):
            vc_priority = UNSET
        elif isinstance(self.vc_priority, int):
            vc_priority = (None, str(self.vc_priority).encode(), "text/plain")
        else:
            vc_priority = (None, str(self.vc_priority).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        comments = (
            self.comments if isinstance(self.comments, Unset) else (None, str(self.comments).encode(), "text/plain")
        )

        config_template: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.config_template, Unset):
            config_template = UNSET
        elif isinstance(self.config_template, int):
            config_template = (None, str(self.config_template).encode(), "text/plain")
        elif isinstance(self.config_template, None):
            config_template = (None, str(self.config_template).encode(), "text/plain")
        elif isinstance(self.config_template, BriefConfigTemplateRequest):
            config_template = (None, json.dumps(self.config_template.to_dict()).encode(), "application/json")
        else:
            config_template = (None, str(self.config_template).encode(), "text/plain")

        local_context_data = (
            self.local_context_data
            if isinstance(self.local_context_data, Unset)
            else (None, str(self.local_context_data).encode(), "text/plain")
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
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if role is not UNSET:
            field_dict["role"] = role
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if platform is not UNSET:
            field_dict["platform"] = platform
        if serial is not UNSET:
            field_dict["serial"] = serial
        if asset_tag is not UNSET:
            field_dict["asset_tag"] = asset_tag
        if site is not UNSET:
            field_dict["site"] = site
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
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_writable_device_with_config_context_request_custom_fields import (
            PatchedWritableDeviceWithConfigContextRequestCustomFields,
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_device_type(data: object) -> Union["BriefDeviceTypeRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_type_type_1 = BriefDeviceTypeRequest.from_dict(data)

                return device_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDeviceTypeRequest", Unset, int], data)

        device_type = _parse_device_type(d.pop("device_type", UNSET))

        def _parse_role(data: object) -> Union["BriefDeviceRoleRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                role_type_1 = BriefDeviceRoleRequest.from_dict(data)

                return role_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDeviceRoleRequest", Unset, int], data)

        role = _parse_role(d.pop("role", UNSET))

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

        def _parse_site(data: object) -> Union["BriefSiteRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                site_type_1 = BriefSiteRequest.from_dict(data)

                return site_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefSiteRequest", Unset, int], data)

        site = _parse_site(d.pop("site", UNSET))

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

        def _parse_face(data: object) -> Union[None, PatchedWritableDeviceWithConfigContextRequestRackFace, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                face_type_1 = PatchedWritableDeviceWithConfigContextRequestRackFace(data)

                return face_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                face_type_2_type_1 = PatchedWritableDeviceWithConfigContextRequestRackFace(data)

                return face_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                face_type_3_type_1 = PatchedWritableDeviceWithConfigContextRequestRackFace(data)

                return face_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, PatchedWritableDeviceWithConfigContextRequestRackFace, Unset], data)

        face = _parse_face(d.pop("face", UNSET))

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
        status: Union[Unset, PatchedWritableDeviceWithConfigContextRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PatchedWritableDeviceWithConfigContextRequestStatus(_status)

        def _parse_airflow(
            data: object,
        ) -> Union[
            None,
            PatchedWritableDeviceWithConfigContextRequestAirflowType1,
            PatchedWritableDeviceWithConfigContextRequestAirflowType2Type1,
            PatchedWritableDeviceWithConfigContextRequestAirflowType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                airflow_type_1 = PatchedWritableDeviceWithConfigContextRequestAirflowType1(data)

                return airflow_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                airflow_type_2_type_1 = PatchedWritableDeviceWithConfigContextRequestAirflowType2Type1(data)

                return airflow_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                airflow_type_3_type_1 = PatchedWritableDeviceWithConfigContextRequestAirflowType3Type1(data)

                return airflow_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PatchedWritableDeviceWithConfigContextRequestAirflowType1,
                    PatchedWritableDeviceWithConfigContextRequestAirflowType2Type1,
                    PatchedWritableDeviceWithConfigContextRequestAirflowType3Type1,
                    Unset,
                ],
                data,
            )

        airflow = _parse_airflow(d.pop("airflow", UNSET))

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
        custom_fields: Union[Unset, PatchedWritableDeviceWithConfigContextRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedWritableDeviceWithConfigContextRequestCustomFields.from_dict(_custom_fields)

        patched_writable_device_with_config_context_request = cls(
            name=name,
            device_type=device_type,
            role=role,
            tenant=tenant,
            platform=platform,
            serial=serial,
            asset_tag=asset_tag,
            site=site,
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

        patched_writable_device_with_config_context_request.additional_properties = d
        return patched_writable_device_with_config_context_request

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
