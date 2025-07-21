import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_cluster_group import BriefClusterGroup
    from ..models.brief_cluster_type import BriefClusterType
    from ..models.brief_tenant import BriefTenant
    from ..models.cluster_custom_fields import ClusterCustomFields
    from ..models.cluster_status import ClusterStatus
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="Cluster")


@_attrs_define
class Cluster:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        name (str):
        type_ (BriefClusterType): Adds support for custom fields and tags.
        scope (Any):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        allocated_vcpus (float):
        allocated_memory (int):
        allocated_disk (int):
        group (Union['BriefClusterGroup', None, Unset]):
        status (Union[Unset, ClusterStatus]):
        tenant (Union['BriefTenant', None, Unset]):
        scope_type (Union[None, Unset, str]):
        scope_id (Union[None, Unset, int]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, ClusterCustomFields]):
        device_count (Union[Unset, int]):
        virtualmachine_count (Union[Unset, int]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    type_: "BriefClusterType"
    scope: Any
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    allocated_vcpus: float
    allocated_memory: int
    allocated_disk: int
    group: Union["BriefClusterGroup", None, Unset] = UNSET
    status: Union[Unset, "ClusterStatus"] = UNSET
    tenant: Union["BriefTenant", None, Unset] = UNSET
    scope_type: Union[None, Unset, str] = UNSET
    scope_id: Union[None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "ClusterCustomFields"] = UNSET
    device_count: Union[Unset, int] = UNSET
    virtualmachine_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_cluster_group import BriefClusterGroup
        from ..models.brief_tenant import BriefTenant

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

        type_ = self.type_.to_dict()

        scope = self.scope

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

        allocated_vcpus = self.allocated_vcpus

        allocated_memory = self.allocated_memory

        allocated_disk = self.allocated_disk

        group: Union[None, Unset, dict[str, Any]]
        if isinstance(self.group, Unset):
            group = UNSET
        elif isinstance(self.group, BriefClusterGroup):
            group = self.group.to_dict()
        else:
            group = self.group

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

        scope_type: Union[None, Unset, str]
        if isinstance(self.scope_type, Unset):
            scope_type = UNSET
        else:
            scope_type = self.scope_type

        scope_id: Union[None, Unset, int]
        if isinstance(self.scope_id, Unset):
            scope_id = UNSET
        else:
            scope_id = self.scope_id

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

        device_count = self.device_count

        virtualmachine_count = self.virtualmachine_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "name": name,
                "type": type_,
                "scope": scope,
                "created": created,
                "last_updated": last_updated,
                "allocated_vcpus": allocated_vcpus,
                "allocated_memory": allocated_memory,
                "allocated_disk": allocated_disk,
            }
        )
        if group is not UNSET:
            field_dict["group"] = group
        if status is not UNSET:
            field_dict["status"] = status
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if scope_type is not UNSET:
            field_dict["scope_type"] = scope_type
        if scope_id is not UNSET:
            field_dict["scope_id"] = scope_id
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if device_count is not UNSET:
            field_dict["device_count"] = device_count
        if virtualmachine_count is not UNSET:
            field_dict["virtualmachine_count"] = virtualmachine_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_cluster_group import BriefClusterGroup
        from ..models.brief_cluster_type import BriefClusterType
        from ..models.brief_tenant import BriefTenant
        from ..models.cluster_custom_fields import ClusterCustomFields
        from ..models.cluster_status import ClusterStatus
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

        type_ = BriefClusterType.from_dict(d.pop("type"))

        scope = d.pop("scope")

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

        allocated_vcpus = d.pop("allocated_vcpus")

        allocated_memory = d.pop("allocated_memory")

        allocated_disk = d.pop("allocated_disk")

        def _parse_group(data: object) -> Union["BriefClusterGroup", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_1 = BriefClusterGroup.from_dict(data)

                return group_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefClusterGroup", None, Unset], data)

        group = _parse_group(d.pop("group", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, ClusterStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ClusterStatus.from_dict(_status)

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

        def _parse_scope_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scope_type = _parse_scope_type(d.pop("scope_type", UNSET))

        def _parse_scope_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        scope_id = _parse_scope_id(d.pop("scope_id", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, ClusterCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ClusterCustomFields.from_dict(_custom_fields)

        device_count = d.pop("device_count", UNSET)

        virtualmachine_count = d.pop("virtualmachine_count", UNSET)

        cluster = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            type_=type_,
            scope=scope,
            created=created,
            last_updated=last_updated,
            allocated_vcpus=allocated_vcpus,
            allocated_memory=allocated_memory,
            allocated_disk=allocated_disk,
            group=group,
            status=status,
            tenant=tenant,
            scope_type=scope_type,
            scope_id=scope_id,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
            device_count=device_count,
            virtualmachine_count=virtualmachine_count,
        )

        cluster.additional_properties = d
        return cluster

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
