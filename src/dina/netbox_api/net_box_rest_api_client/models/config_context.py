import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_data_file import BriefDataFile
    from ..models.brief_data_source import BriefDataSource
    from ..models.cluster import Cluster
    from ..models.cluster_group import ClusterGroup
    from ..models.cluster_type import ClusterType
    from ..models.device_role import DeviceRole
    from ..models.device_type import DeviceType
    from ..models.location import Location
    from ..models.platform import Platform
    from ..models.region import Region
    from ..models.site import Site
    from ..models.site_group import SiteGroup
    from ..models.tenant import Tenant
    from ..models.tenant_group import TenantGroup


T = TypeVar("T", bound="ConfigContext")


@_attrs_define
class ConfigContext:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            id (int):
            url (str):
            display_url (str):
            display (str):
            name (str):
            data_path (str): Path to remote file (relative to data source root)
            data_file (BriefDataFile): Adds support for custom fields and tags.
            data_synced (Union[None, datetime.datetime]):
            data (Any):
            created (Union[None, datetime.datetime]):
            last_updated (Union[None, datetime.datetime]):
            weight (Union[Unset, int]):
            description (Union[Unset, str]):
            is_active (Union[Unset, bool]):
            regions (Union[Unset, list['Region']]):
            site_groups (Union[Unset, list['SiteGroup']]):
            sites (Union[Unset, list['Site']]):
            locations (Union[Unset, list['Location']]):
            device_types (Union[Unset, list['DeviceType']]):
            roles (Union[Unset, list['DeviceRole']]):
            platforms (Union[Unset, list['Platform']]):
            cluster_types (Union[Unset, list['ClusterType']]):
            cluster_groups (Union[Unset, list['ClusterGroup']]):
            clusters (Union[Unset, list['Cluster']]):
            tenant_groups (Union[Unset, list['TenantGroup']]):
            tenants (Union[Unset, list['Tenant']]):
            tags (Union[Unset, list[str]]):
            data_source (Union[Unset, BriefDataSource]): Adds support for custom fields and tags.
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    data_path: str
    data_file: "BriefDataFile"
    data_synced: Union[None, datetime.datetime]
    data: Any
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    weight: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    regions: Union[Unset, list["Region"]] = UNSET
    site_groups: Union[Unset, list["SiteGroup"]] = UNSET
    sites: Union[Unset, list["Site"]] = UNSET
    locations: Union[Unset, list["Location"]] = UNSET
    device_types: Union[Unset, list["DeviceType"]] = UNSET
    roles: Union[Unset, list["DeviceRole"]] = UNSET
    platforms: Union[Unset, list["Platform"]] = UNSET
    cluster_types: Union[Unset, list["ClusterType"]] = UNSET
    cluster_groups: Union[Unset, list["ClusterGroup"]] = UNSET
    clusters: Union[Unset, list["Cluster"]] = UNSET
    tenant_groups: Union[Unset, list["TenantGroup"]] = UNSET
    tenants: Union[Unset, list["Tenant"]] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    data_source: Union[Unset, "BriefDataSource"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

        data_path = self.data_path

        data_file = self.data_file.to_dict()

        data_synced: Union[None, str]
        if isinstance(self.data_synced, datetime.datetime):
            data_synced = self.data_synced.isoformat()
        else:
            data_synced = self.data_synced

        data = self.data

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

        weight = self.weight

        description = self.description

        is_active = self.is_active

        regions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.regions, Unset):
            regions = []
            for regions_item_data in self.regions:
                regions_item = regions_item_data.to_dict()
                regions.append(regions_item)

        site_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.site_groups, Unset):
            site_groups = []
            for site_groups_item_data in self.site_groups:
                site_groups_item = site_groups_item_data.to_dict()
                site_groups.append(site_groups_item)

        sites: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = []
            for sites_item_data in self.sites:
                sites_item = sites_item_data.to_dict()
                sites.append(sites_item)

        locations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)

        device_types: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.device_types, Unset):
            device_types = []
            for device_types_item_data in self.device_types:
                device_types_item = device_types_item_data.to_dict()
                device_types.append(device_types_item)

        roles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        platforms: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = []
            for platforms_item_data in self.platforms:
                platforms_item = platforms_item_data.to_dict()
                platforms.append(platforms_item)

        cluster_types: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cluster_types, Unset):
            cluster_types = []
            for cluster_types_item_data in self.cluster_types:
                cluster_types_item = cluster_types_item_data.to_dict()
                cluster_types.append(cluster_types_item)

        cluster_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cluster_groups, Unset):
            cluster_groups = []
            for cluster_groups_item_data in self.cluster_groups:
                cluster_groups_item = cluster_groups_item_data.to_dict()
                cluster_groups.append(cluster_groups_item)

        clusters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.clusters, Unset):
            clusters = []
            for clusters_item_data in self.clusters:
                clusters_item = clusters_item_data.to_dict()
                clusters.append(clusters_item)

        tenant_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tenant_groups, Unset):
            tenant_groups = []
            for tenant_groups_item_data in self.tenant_groups:
                tenant_groups_item = tenant_groups_item_data.to_dict()
                tenant_groups.append(tenant_groups_item)

        tenants: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tenants, Unset):
            tenants = []
            for tenants_item_data in self.tenants:
                tenants_item = tenants_item_data.to_dict()
                tenants.append(tenants_item)

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        data_source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_source, Unset):
            data_source = self.data_source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "name": name,
                "data_path": data_path,
                "data_file": data_file,
                "data_synced": data_synced,
                "data": data,
                "created": created,
                "last_updated": last_updated,
            }
        )
        if weight is not UNSET:
            field_dict["weight"] = weight
        if description is not UNSET:
            field_dict["description"] = description
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if regions is not UNSET:
            field_dict["regions"] = regions
        if site_groups is not UNSET:
            field_dict["site_groups"] = site_groups
        if sites is not UNSET:
            field_dict["sites"] = sites
        if locations is not UNSET:
            field_dict["locations"] = locations
        if device_types is not UNSET:
            field_dict["device_types"] = device_types
        if roles is not UNSET:
            field_dict["roles"] = roles
        if platforms is not UNSET:
            field_dict["platforms"] = platforms
        if cluster_types is not UNSET:
            field_dict["cluster_types"] = cluster_types
        if cluster_groups is not UNSET:
            field_dict["cluster_groups"] = cluster_groups
        if clusters is not UNSET:
            field_dict["clusters"] = clusters
        if tenant_groups is not UNSET:
            field_dict["tenant_groups"] = tenant_groups
        if tenants is not UNSET:
            field_dict["tenants"] = tenants
        if tags is not UNSET:
            field_dict["tags"] = tags
        if data_source is not UNSET:
            field_dict["data_source"] = data_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_data_file import BriefDataFile
        from ..models.brief_data_source import BriefDataSource
        from ..models.cluster import Cluster
        from ..models.cluster_group import ClusterGroup
        from ..models.cluster_type import ClusterType
        from ..models.device_role import DeviceRole
        from ..models.device_type import DeviceType
        from ..models.location import Location
        from ..models.platform import Platform
        from ..models.region import Region
        from ..models.site import Site
        from ..models.site_group import SiteGroup
        from ..models.tenant import Tenant
        from ..models.tenant_group import TenantGroup

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

        data_path = d.pop("data_path")

        data_file = BriefDataFile.from_dict(d.pop("data_file"))

        def _parse_data_synced(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_synced_type_0 = isoparse(data)

                return data_synced_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        data_synced = _parse_data_synced(d.pop("data_synced"))

        data = d.pop("data")

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

        weight = d.pop("weight", UNSET)

        description = d.pop("description", UNSET)

        is_active = d.pop("is_active", UNSET)

        regions = []
        _regions = d.pop("regions", UNSET)
        for regions_item_data in _regions or []:
            regions_item = Region.from_dict(regions_item_data)

            regions.append(regions_item)

        site_groups = []
        _site_groups = d.pop("site_groups", UNSET)
        for site_groups_item_data in _site_groups or []:
            site_groups_item = SiteGroup.from_dict(site_groups_item_data)

            site_groups.append(site_groups_item)

        sites = []
        _sites = d.pop("sites", UNSET)
        for sites_item_data in _sites or []:
            sites_item = Site.from_dict(sites_item_data)

            sites.append(sites_item)

        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = Location.from_dict(locations_item_data)

            locations.append(locations_item)

        device_types = []
        _device_types = d.pop("device_types", UNSET)
        for device_types_item_data in _device_types or []:
            device_types_item = DeviceType.from_dict(device_types_item_data)

            device_types.append(device_types_item)

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = DeviceRole.from_dict(roles_item_data)

            roles.append(roles_item)

        platforms = []
        _platforms = d.pop("platforms", UNSET)
        for platforms_item_data in _platforms or []:
            platforms_item = Platform.from_dict(platforms_item_data)

            platforms.append(platforms_item)

        cluster_types = []
        _cluster_types = d.pop("cluster_types", UNSET)
        for cluster_types_item_data in _cluster_types or []:
            cluster_types_item = ClusterType.from_dict(cluster_types_item_data)

            cluster_types.append(cluster_types_item)

        cluster_groups = []
        _cluster_groups = d.pop("cluster_groups", UNSET)
        for cluster_groups_item_data in _cluster_groups or []:
            cluster_groups_item = ClusterGroup.from_dict(cluster_groups_item_data)

            cluster_groups.append(cluster_groups_item)

        clusters = []
        _clusters = d.pop("clusters", UNSET)
        for clusters_item_data in _clusters or []:
            clusters_item = Cluster.from_dict(clusters_item_data)

            clusters.append(clusters_item)

        tenant_groups = []
        _tenant_groups = d.pop("tenant_groups", UNSET)
        for tenant_groups_item_data in _tenant_groups or []:
            tenant_groups_item = TenantGroup.from_dict(tenant_groups_item_data)

            tenant_groups.append(tenant_groups_item)

        tenants = []
        _tenants = d.pop("tenants", UNSET)
        for tenants_item_data in _tenants or []:
            tenants_item = Tenant.from_dict(tenants_item_data)

            tenants.append(tenants_item)

        tags = cast(list[str], d.pop("tags", UNSET))

        _data_source = d.pop("data_source", UNSET)
        data_source: Union[Unset, BriefDataSource]
        if isinstance(_data_source, Unset):
            data_source = UNSET
        else:
            data_source = BriefDataSource.from_dict(_data_source)

        config_context = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            data_path=data_path,
            data_file=data_file,
            data_synced=data_synced,
            data=data,
            created=created,
            last_updated=last_updated,
            weight=weight,
            description=description,
            is_active=is_active,
            regions=regions,
            site_groups=site_groups,
            sites=sites,
            locations=locations,
            device_types=device_types,
            roles=roles,
            platforms=platforms,
            cluster_types=cluster_types,
            cluster_groups=cluster_groups,
            clusters=clusters,
            tenant_groups=tenant_groups,
            tenants=tenants,
            tags=tags,
            data_source=data_source,
        )

        config_context.additional_properties = d
        return config_context

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
