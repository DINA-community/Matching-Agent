import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_data_source_request import BriefDataSourceRequest


T = TypeVar("T", bound="ConfigContextRequest")


@_attrs_define
class ConfigContextRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            name (str):
            data (Any):
            weight (Union[Unset, int]):
            description (Union[Unset, str]):
            is_active (Union[Unset, bool]):
            regions (Union[Unset, list[int]]):
            site_groups (Union[Unset, list[int]]):
            sites (Union[Unset, list[int]]):
            locations (Union[Unset, list[int]]):
            device_types (Union[Unset, list[int]]):
            roles (Union[Unset, list[int]]):
            platforms (Union[Unset, list[int]]):
            cluster_types (Union[Unset, list[int]]):
            cluster_groups (Union[Unset, list[int]]):
            clusters (Union[Unset, list[int]]):
            tenant_groups (Union[Unset, list[int]]):
            tenants (Union[Unset, list[int]]):
            tags (Union[Unset, list[str]]):
            data_source (Union['BriefDataSourceRequest', Unset, int]):
    """

    name: str
    data: Any
    weight: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    regions: Union[Unset, list[int]] = UNSET
    site_groups: Union[Unset, list[int]] = UNSET
    sites: Union[Unset, list[int]] = UNSET
    locations: Union[Unset, list[int]] = UNSET
    device_types: Union[Unset, list[int]] = UNSET
    roles: Union[Unset, list[int]] = UNSET
    platforms: Union[Unset, list[int]] = UNSET
    cluster_types: Union[Unset, list[int]] = UNSET
    cluster_groups: Union[Unset, list[int]] = UNSET
    clusters: Union[Unset, list[int]] = UNSET
    tenant_groups: Union[Unset, list[int]] = UNSET
    tenants: Union[Unset, list[int]] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    data_source: Union["BriefDataSourceRequest", Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_data_source_request import BriefDataSourceRequest

        name = self.name

        data = self.data

        weight = self.weight

        description = self.description

        is_active = self.is_active

        regions: Union[Unset, list[int]] = UNSET
        if not isinstance(self.regions, Unset):
            regions = self.regions

        site_groups: Union[Unset, list[int]] = UNSET
        if not isinstance(self.site_groups, Unset):
            site_groups = self.site_groups

        sites: Union[Unset, list[int]] = UNSET
        if not isinstance(self.sites, Unset):
            sites = self.sites

        locations: Union[Unset, list[int]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = self.locations

        device_types: Union[Unset, list[int]] = UNSET
        if not isinstance(self.device_types, Unset):
            device_types = self.device_types

        roles: Union[Unset, list[int]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        platforms: Union[Unset, list[int]] = UNSET
        if not isinstance(self.platforms, Unset):
            platforms = self.platforms

        cluster_types: Union[Unset, list[int]] = UNSET
        if not isinstance(self.cluster_types, Unset):
            cluster_types = self.cluster_types

        cluster_groups: Union[Unset, list[int]] = UNSET
        if not isinstance(self.cluster_groups, Unset):
            cluster_groups = self.cluster_groups

        clusters: Union[Unset, list[int]] = UNSET
        if not isinstance(self.clusters, Unset):
            clusters = self.clusters

        tenant_groups: Union[Unset, list[int]] = UNSET
        if not isinstance(self.tenant_groups, Unset):
            tenant_groups = self.tenant_groups

        tenants: Union[Unset, list[int]] = UNSET
        if not isinstance(self.tenants, Unset):
            tenants = self.tenants

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        data_source: Union[Unset, dict[str, Any], int]
        if isinstance(self.data_source, Unset):
            data_source = UNSET
        elif isinstance(self.data_source, BriefDataSourceRequest):
            data_source = self.data_source.to_dict()
        else:
            data_source = self.data_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "data": data,
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

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        data = (None, str(self.data).encode(), "text/plain")

        weight = (
            self.weight
            if isinstance(self.weight, Unset)
            else (None, str(self.weight).encode(), "text/plain")
        )

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        is_active = (
            self.is_active
            if isinstance(self.is_active, Unset)
            else (None, str(self.is_active).encode(), "text/plain")
        )

        regions: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.regions, Unset):
            _temp_regions = self.regions
            regions = (None, json.dumps(_temp_regions).encode(), "application/json")

        site_groups: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.site_groups, Unset):
            _temp_site_groups = self.site_groups
            site_groups = (
                None,
                json.dumps(_temp_site_groups).encode(),
                "application/json",
            )

        sites: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.sites, Unset):
            _temp_sites = self.sites
            sites = (None, json.dumps(_temp_sites).encode(), "application/json")

        locations: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.locations, Unset):
            _temp_locations = self.locations
            locations = (None, json.dumps(_temp_locations).encode(), "application/json")

        device_types: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.device_types, Unset):
            _temp_device_types = self.device_types
            device_types = (
                None,
                json.dumps(_temp_device_types).encode(),
                "application/json",
            )

        roles: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.roles, Unset):
            _temp_roles = self.roles
            roles = (None, json.dumps(_temp_roles).encode(), "application/json")

        platforms: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.platforms, Unset):
            _temp_platforms = self.platforms
            platforms = (None, json.dumps(_temp_platforms).encode(), "application/json")

        cluster_types: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.cluster_types, Unset):
            _temp_cluster_types = self.cluster_types
            cluster_types = (
                None,
                json.dumps(_temp_cluster_types).encode(),
                "application/json",
            )

        cluster_groups: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.cluster_groups, Unset):
            _temp_cluster_groups = self.cluster_groups
            cluster_groups = (
                None,
                json.dumps(_temp_cluster_groups).encode(),
                "application/json",
            )

        clusters: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.clusters, Unset):
            _temp_clusters = self.clusters
            clusters = (None, json.dumps(_temp_clusters).encode(), "application/json")

        tenant_groups: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tenant_groups, Unset):
            _temp_tenant_groups = self.tenant_groups
            tenant_groups = (
                None,
                json.dumps(_temp_tenant_groups).encode(),
                "application/json",
            )

        tenants: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tenants, Unset):
            _temp_tenants = self.tenants
            tenants = (None, json.dumps(_temp_tenants).encode(), "application/json")

        tags: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tags, Unset):
            _temp_tags = self.tags
            tags = (None, json.dumps(_temp_tags).encode(), "application/json")

        data_source: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.data_source, Unset):
            data_source = UNSET
        elif isinstance(self.data_source, int):
            data_source = (None, str(self.data_source).encode(), "text/plain")
        else:
            data_source = (
                None,
                json.dumps(self.data_source.to_dict()).encode(),
                "application/json",
            )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "name": name,
                "data": data,
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
        from ..models.brief_data_source_request import BriefDataSourceRequest

        d = dict(src_dict)
        name = d.pop("name")

        data = d.pop("data")

        weight = d.pop("weight", UNSET)

        description = d.pop("description", UNSET)

        is_active = d.pop("is_active", UNSET)

        regions = cast(list[int], d.pop("regions", UNSET))

        site_groups = cast(list[int], d.pop("site_groups", UNSET))

        sites = cast(list[int], d.pop("sites", UNSET))

        locations = cast(list[int], d.pop("locations", UNSET))

        device_types = cast(list[int], d.pop("device_types", UNSET))

        roles = cast(list[int], d.pop("roles", UNSET))

        platforms = cast(list[int], d.pop("platforms", UNSET))

        cluster_types = cast(list[int], d.pop("cluster_types", UNSET))

        cluster_groups = cast(list[int], d.pop("cluster_groups", UNSET))

        clusters = cast(list[int], d.pop("clusters", UNSET))

        tenant_groups = cast(list[int], d.pop("tenant_groups", UNSET))

        tenants = cast(list[int], d.pop("tenants", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        def _parse_data_source(
            data: object,
        ) -> Union["BriefDataSourceRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_source_type_1 = BriefDataSourceRequest.from_dict(data)

                return data_source_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDataSourceRequest", Unset, int], data)

        data_source = _parse_data_source(d.pop("data_source", UNSET))

        config_context_request = cls(
            name=name,
            data=data,
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

        config_context_request.additional_properties = d
        return config_context_request

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
