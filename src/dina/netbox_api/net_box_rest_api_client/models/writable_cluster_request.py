import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_cluster_request_status import WritableClusterRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_cluster_group_request import BriefClusterGroupRequest
    from ..models.brief_cluster_type_request import BriefClusterTypeRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.writable_cluster_request_custom_fields import WritableClusterRequestCustomFields


T = TypeVar("T", bound="WritableClusterRequest")


@_attrs_define
class WritableClusterRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str):
        type_ (Union['BriefClusterTypeRequest', int]):
        group (Union['BriefClusterGroupRequest', None, Unset, int]):
        status (Union[Unset, WritableClusterRequestStatus]): * `planned` - Planned
            * `staging` - Staging
            * `active` - Active
            * `decommissioning` - Decommissioning
            * `offline` - Offline
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        scope_type (Union[None, Unset, str]):
        scope_id (Union[None, Unset, int]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WritableClusterRequestCustomFields]):
    """

    name: str
    type_: Union["BriefClusterTypeRequest", int]
    group: Union["BriefClusterGroupRequest", None, Unset, int] = UNSET
    status: Union[Unset, WritableClusterRequestStatus] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    scope_type: Union[None, Unset, str] = UNSET
    scope_id: Union[None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WritableClusterRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_cluster_group_request import BriefClusterGroupRequest
        from ..models.brief_cluster_type_request import BriefClusterTypeRequest
        from ..models.brief_tenant_request import BriefTenantRequest

        name = self.name

        type_: Union[dict[str, Any], int]
        if isinstance(self.type_, BriefClusterTypeRequest):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        group: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.group, Unset):
            group = UNSET
        elif isinstance(self.group, BriefClusterGroupRequest):
            group = self.group.to_dict()
        else:
            group = self.group

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        tenant: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenantRequest):
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
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

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        type_: tuple[None, bytes, str]

        if isinstance(self.type_, int):
            type_ = (None, str(self.type_).encode(), "text/plain")
        else:
            type_ = (None, json.dumps(self.type_.to_dict()).encode(), "application/json")

        group: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.group, Unset):
            group = UNSET
        elif isinstance(self.group, int):
            group = (None, str(self.group).encode(), "text/plain")
        elif isinstance(self.group, None):
            group = (None, str(self.group).encode(), "text/plain")
        elif isinstance(self.group, BriefClusterGroupRequest):
            group = (None, json.dumps(self.group.to_dict()).encode(), "application/json")
        else:
            group = (None, str(self.group).encode(), "text/plain")

        status: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

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

        scope_type: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.scope_type, Unset):
            scope_type = UNSET
        elif isinstance(self.scope_type, str):
            scope_type = (None, str(self.scope_type).encode(), "text/plain")
        else:
            scope_type = (None, str(self.scope_type).encode(), "text/plain")

        scope_id: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.scope_id, Unset):
            scope_id = UNSET
        elif isinstance(self.scope_id, int):
            scope_id = (None, str(self.scope_id).encode(), "text/plain")
        else:
            scope_id = (None, str(self.scope_id).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        comments = (
            self.comments if isinstance(self.comments, Unset) else (None, str(self.comments).encode(), "text/plain")
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

        field_dict.update(
            {
                "name": name,
                "type": type_,
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_cluster_group_request import BriefClusterGroupRequest
        from ..models.brief_cluster_type_request import BriefClusterTypeRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.writable_cluster_request_custom_fields import WritableClusterRequestCustomFields

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_type_(data: object) -> Union["BriefClusterTypeRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                type_type_1 = BriefClusterTypeRequest.from_dict(data)

                return type_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefClusterTypeRequest", int], data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_group(data: object) -> Union["BriefClusterGroupRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                group_type_1_type_1 = BriefClusterGroupRequest.from_dict(data)

                return group_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefClusterGroupRequest", None, Unset, int], data)

        group = _parse_group(d.pop("group", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, WritableClusterRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WritableClusterRequestStatus(_status)

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
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WritableClusterRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WritableClusterRequestCustomFields.from_dict(_custom_fields)

        writable_cluster_request = cls(
            name=name,
            type_=type_,
            group=group,
            status=status,
            tenant=tenant,
            scope_type=scope_type,
            scope_id=scope_id,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        writable_cluster_request.additional_properties = d
        return writable_cluster_request

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
