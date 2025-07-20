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
    from ..models.brief_device_role import BriefDeviceRole
    from ..models.brief_device_type import BriefDeviceType
    from ..models.brief_ip_address import BriefIPAddress
    from ..models.brief_location import BriefLocation
    from ..models.brief_platform import BriefPlatform
    from ..models.brief_rack import BriefRack
    from ..models.brief_site import BriefSite
    from ..models.brief_tenant import BriefTenant
    from ..models.brief_virtual_chassis import BriefVirtualChassis
    from ..models.device_with_config_context_airflow import DeviceWithConfigContextAirflow
    from ..models.device_with_config_context_custom_fields import DeviceWithConfigContextCustomFields
    from ..models.device_with_config_context_face import DeviceWithConfigContextFace
    from ..models.device_with_config_context_status import DeviceWithConfigContextStatus
    from ..models.nested_device import NestedDevice
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="DeviceWithConfigContext")


@_attrs_define
class DeviceWithConfigContext:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        device_type (BriefDeviceType): Adds support for custom fields and tags.
        role (BriefDeviceRole): Extends PrimaryModelSerializer to include MPTT support.
        site (BriefSite): Adds support for custom fields and tags.
        parent_device (Union['NestedDevice', None]):
        primary_ip (Union['BriefIPAddress', None]):
        config_context (Any):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        console_port_count (int):
        console_server_port_count (int):
        power_port_count (int):
        power_outlet_count (int):
        interface_count (int):
        front_port_count (int):
        rear_port_count (int):
        device_bay_count (int):
        module_bay_count (int):
        inventory_item_count (int):
        name (Union[None, Unset, str]):
        tenant (Union['BriefTenant', None, Unset]):
        platform (Union['BriefPlatform', None, Unset]):
        serial (Union[Unset, str]): Chassis serial number, assigned by the manufacturer
        asset_tag (Union[None, Unset, str]): A unique tag used to identify this device
        location (Union['BriefLocation', None, Unset]):
        rack (Union['BriefRack', None, Unset]):
        position (Union[None, Unset, float]):
        face (Union[Unset, DeviceWithConfigContextFace]):
        latitude (Union[None, Unset, float]): GPS coordinate in decimal format (xx.yyyyyy)
        longitude (Union[None, Unset, float]): GPS coordinate in decimal format (xx.yyyyyy)
        status (Union[Unset, DeviceWithConfigContextStatus]):
        airflow (Union[Unset, DeviceWithConfigContextAirflow]):
        primary_ip4 (Union['BriefIPAddress', None, Unset]):
        primary_ip6 (Union['BriefIPAddress', None, Unset]):
        oob_ip (Union['BriefIPAddress', None, Unset]):
        cluster (Union['BriefCluster', None, Unset]):
        virtual_chassis (Union['BriefVirtualChassis', None, Unset]):
        vc_position (Union[None, Unset, int]):
        vc_priority (Union[None, Unset, int]): Virtual chassis master election priority
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        config_template (Union['BriefConfigTemplate', None, Unset]):
        local_context_data (Union[Unset, Any]): Local config context data takes precedence over source contexts in the
            final rendered config context
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, DeviceWithConfigContextCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    device_type: "BriefDeviceType"
    role: "BriefDeviceRole"
    site: "BriefSite"
    parent_device: Union["NestedDevice", None]
    primary_ip: Union["BriefIPAddress", None]
    config_context: Any
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    console_port_count: int
    console_server_port_count: int
    power_port_count: int
    power_outlet_count: int
    interface_count: int
    front_port_count: int
    rear_port_count: int
    device_bay_count: int
    module_bay_count: int
    inventory_item_count: int
    name: Union[None, Unset, str] = UNSET
    tenant: Union["BriefTenant", None, Unset] = UNSET
    platform: Union["BriefPlatform", None, Unset] = UNSET
    serial: Union[Unset, str] = UNSET
    asset_tag: Union[None, Unset, str] = UNSET
    location: Union["BriefLocation", None, Unset] = UNSET
    rack: Union["BriefRack", None, Unset] = UNSET
    position: Union[None, Unset, float] = UNSET
    face: Union[Unset, "DeviceWithConfigContextFace"] = UNSET
    latitude: Union[None, Unset, float] = UNSET
    longitude: Union[None, Unset, float] = UNSET
    status: Union[Unset, "DeviceWithConfigContextStatus"] = UNSET
    airflow: Union[Unset, "DeviceWithConfigContextAirflow"] = UNSET
    primary_ip4: Union["BriefIPAddress", None, Unset] = UNSET
    primary_ip6: Union["BriefIPAddress", None, Unset] = UNSET
    oob_ip: Union["BriefIPAddress", None, Unset] = UNSET
    cluster: Union["BriefCluster", None, Unset] = UNSET
    virtual_chassis: Union["BriefVirtualChassis", None, Unset] = UNSET
    vc_position: Union[None, Unset, int] = UNSET
    vc_priority: Union[None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    config_template: Union["BriefConfigTemplate", None, Unset] = UNSET
    local_context_data: Union[Unset, Any] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "DeviceWithConfigContextCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_cluster import BriefCluster
        from ..models.brief_config_template import BriefConfigTemplate
        from ..models.brief_ip_address import BriefIPAddress
        from ..models.brief_location import BriefLocation
        from ..models.brief_platform import BriefPlatform
        from ..models.brief_rack import BriefRack
        from ..models.brief_tenant import BriefTenant
        from ..models.brief_virtual_chassis import BriefVirtualChassis
        from ..models.nested_device import NestedDevice

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        device_type = self.device_type.to_dict()

        role = self.role.to_dict()

        site = self.site.to_dict()

        parent_device: Union[None, dict[str, Any]]
        if isinstance(self.parent_device, NestedDevice):
            parent_device = self.parent_device.to_dict()
        else:
            parent_device = self.parent_device

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

        console_port_count = self.console_port_count

        console_server_port_count = self.console_server_port_count

        power_port_count = self.power_port_count

        power_outlet_count = self.power_outlet_count

        interface_count = self.interface_count

        front_port_count = self.front_port_count

        rear_port_count = self.rear_port_count

        device_bay_count = self.device_bay_count

        module_bay_count = self.module_bay_count

        inventory_item_count = self.inventory_item_count

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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

        serial = self.serial

        asset_tag: Union[None, Unset, str]
        if isinstance(self.asset_tag, Unset):
            asset_tag = UNSET
        else:
            asset_tag = self.asset_tag

        location: Union[None, Unset, dict[str, Any]]
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, BriefLocation):
            location = self.location.to_dict()
        else:
            location = self.location

        rack: Union[None, Unset, dict[str, Any]]
        if isinstance(self.rack, Unset):
            rack = UNSET
        elif isinstance(self.rack, BriefRack):
            rack = self.rack.to_dict()
        else:
            rack = self.rack

        position: Union[None, Unset, float]
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        face: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.face, Unset):
            face = self.face.to_dict()

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

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        airflow: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.airflow, Unset):
            airflow = self.airflow.to_dict()

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

        oob_ip: Union[None, Unset, dict[str, Any]]
        if isinstance(self.oob_ip, Unset):
            oob_ip = UNSET
        elif isinstance(self.oob_ip, BriefIPAddress):
            oob_ip = self.oob_ip.to_dict()
        else:
            oob_ip = self.oob_ip

        cluster: Union[None, Unset, dict[str, Any]]
        if isinstance(self.cluster, Unset):
            cluster = UNSET
        elif isinstance(self.cluster, BriefCluster):
            cluster = self.cluster.to_dict()
        else:
            cluster = self.cluster

        virtual_chassis: Union[None, Unset, dict[str, Any]]
        if isinstance(self.virtual_chassis, Unset):
            virtual_chassis = UNSET
        elif isinstance(self.virtual_chassis, BriefVirtualChassis):
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
                "device_type": device_type,
                "role": role,
                "site": site,
                "parent_device": parent_device,
                "primary_ip": primary_ip,
                "config_context": config_context,
                "created": created,
                "last_updated": last_updated,
                "console_port_count": console_port_count,
                "console_server_port_count": console_server_port_count,
                "power_port_count": power_port_count,
                "power_outlet_count": power_outlet_count,
                "interface_count": interface_count,
                "front_port_count": front_port_count,
                "rear_port_count": rear_port_count,
                "device_bay_count": device_bay_count,
                "module_bay_count": module_bay_count,
                "inventory_item_count": inventory_item_count,
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
        from ..models.brief_cluster import BriefCluster
        from ..models.brief_config_template import BriefConfigTemplate
        from ..models.brief_device_role import BriefDeviceRole
        from ..models.brief_device_type import BriefDeviceType
        from ..models.brief_ip_address import BriefIPAddress
        from ..models.brief_location import BriefLocation
        from ..models.brief_platform import BriefPlatform
        from ..models.brief_rack import BriefRack
        from ..models.brief_site import BriefSite
        from ..models.brief_tenant import BriefTenant
        from ..models.brief_virtual_chassis import BriefVirtualChassis
        from ..models.device_with_config_context_airflow import DeviceWithConfigContextAirflow
        from ..models.device_with_config_context_custom_fields import DeviceWithConfigContextCustomFields
        from ..models.device_with_config_context_face import DeviceWithConfigContextFace
        from ..models.device_with_config_context_status import DeviceWithConfigContextStatus
        from ..models.nested_device import NestedDevice
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        device_type = BriefDeviceType.from_dict(d.pop("device_type"))

        role = BriefDeviceRole.from_dict(d.pop("role"))

        site = BriefSite.from_dict(d.pop("site"))

        def _parse_parent_device(data: object) -> Union["NestedDevice", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_device_type_1 = NestedDevice.from_dict(data)

                return parent_device_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NestedDevice", None], data)

        parent_device = _parse_parent_device(d.pop("parent_device"))

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

        console_port_count = d.pop("console_port_count")

        console_server_port_count = d.pop("console_server_port_count")

        power_port_count = d.pop("power_port_count")

        power_outlet_count = d.pop("power_outlet_count")

        interface_count = d.pop("interface_count")

        front_port_count = d.pop("front_port_count")

        rear_port_count = d.pop("rear_port_count")

        device_bay_count = d.pop("device_bay_count")

        module_bay_count = d.pop("module_bay_count")

        inventory_item_count = d.pop("inventory_item_count")

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

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

        serial = d.pop("serial", UNSET)

        def _parse_asset_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asset_tag = _parse_asset_tag(d.pop("asset_tag", UNSET))

        def _parse_location(data: object) -> Union["BriefLocation", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_1 = BriefLocation.from_dict(data)

                return location_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefLocation", None, Unset], data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_rack(data: object) -> Union["BriefRack", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rack_type_1 = BriefRack.from_dict(data)

                return rack_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefRack", None, Unset], data)

        rack = _parse_rack(d.pop("rack", UNSET))

        def _parse_position(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        position = _parse_position(d.pop("position", UNSET))

        _face = d.pop("face", UNSET)
        face: Union[Unset, DeviceWithConfigContextFace]
        # if isinstance(_face, Unset):
        #     face = UNSET
        # else:
        #     face = DeviceWithConfigContextFace.from_dict(_face)

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
        status: Union[Unset, DeviceWithConfigContextStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DeviceWithConfigContextStatus.from_dict(_status)

        _airflow = d.pop("airflow", UNSET)
        airflow: Union[Unset, DeviceWithConfigContextAirflow]
        # if isinstance(_airflow, Unset):
        #     airflow = UNSET
        # else:
        #     airflow = DeviceWithConfigContextAirflow.from_dict(_airflow)

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

        def _parse_oob_ip(data: object) -> Union["BriefIPAddress", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                oob_ip_type_1 = BriefIPAddress.from_dict(data)

                return oob_ip_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefIPAddress", None, Unset], data)

        oob_ip = _parse_oob_ip(d.pop("oob_ip", UNSET))

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

        def _parse_virtual_chassis(data: object) -> Union["BriefVirtualChassis", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                virtual_chassis_type_1 = BriefVirtualChassis.from_dict(data)

                return virtual_chassis_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVirtualChassis", None, Unset], data)

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

        def _parse_config_template(data: object) -> Union["BriefConfigTemplate", None, Unset]:
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
        custom_fields: Union[Unset, DeviceWithConfigContextCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = DeviceWithConfigContextCustomFields.from_dict(_custom_fields)

        device_with_config_context = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            device_type=device_type,
            role=role,
            site=site,
            parent_device=parent_device,
            primary_ip=primary_ip,
            config_context=config_context,
            created=created,
            last_updated=last_updated,
            console_port_count=console_port_count,
            console_server_port_count=console_server_port_count,
            power_port_count=power_port_count,
            power_outlet_count=power_outlet_count,
            interface_count=interface_count,
            front_port_count=front_port_count,
            rear_port_count=rear_port_count,
            device_bay_count=device_bay_count,
            module_bay_count=module_bay_count,
            inventory_item_count=inventory_item_count,
            name=name,
            tenant=tenant,
            platform=platform,
            serial=serial,
            asset_tag=asset_tag,
            location=location,
            rack=rack,
            #            position=position,
            #            face=face,
            latitude=latitude,
            longitude=longitude,
            status=status,
            #            airflow=airflow,
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

        device_with_config_context.additional_properties = d
        return device_with_config_context

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
