import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_writable_l2vpn_request_status import PatchedWritableL2VPNRequestStatus
from ..models.patched_writable_l2vpn_request_type import PatchedWritableL2VPNRequestType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_writable_l2vpn_request_custom_fields import PatchedWritableL2VPNRequestCustomFields


T = TypeVar("T", bound="PatchedWritableL2VPNRequest")


@_attrs_define
class PatchedWritableL2VPNRequest:
    """Adds support for custom fields and tags.

    Attributes:
        identifier (Union[None, Unset, int]):
        name (Union[Unset, str]):
        slug (Union[Unset, str]):
        type_ (Union[Unset, PatchedWritableL2VPNRequestType]): * `vpws` - VPWS
            * `vpls` - VPLS
            * `vxlan` - VXLAN
            * `vxlan-evpn` - VXLAN-EVPN
            * `mpls-evpn` - MPLS EVPN
            * `pbb-evpn` - PBB EVPN
            * `evpn-vpws` - EVPN VPWS
            * `epl` - EPL
            * `evpl` - EVPL
            * `ep-lan` - Ethernet Private LAN
            * `evp-lan` - Ethernet Virtual Private LAN
            * `ep-tree` - Ethernet Private Tree
            * `evp-tree` - Ethernet Virtual Private Tree
            * `spb` - SPB
        status (Union[Unset, PatchedWritableL2VPNRequestStatus]): * `active` - Active
            * `planned` - Planned
            * `decommissioning` - Decommissioning
        import_targets (Union[Unset, list[int]]):
        export_targets (Union[Unset, list[int]]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedWritableL2VPNRequestCustomFields]):
    """

    identifier: Union[None, Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    type_: Union[Unset, PatchedWritableL2VPNRequestType] = UNSET
    status: Union[Unset, PatchedWritableL2VPNRequestStatus] = UNSET
    import_targets: Union[Unset, list[int]] = UNSET
    export_targets: Union[Unset, list[int]] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedWritableL2VPNRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_tenant_request import BriefTenantRequest

        identifier: Union[None, Unset, int]
        if isinstance(self.identifier, Unset):
            identifier = UNSET
        else:
            identifier = self.identifier

        name = self.name

        slug = self.slug

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        import_targets: Union[Unset, list[int]] = UNSET
        if not isinstance(self.import_targets, Unset):
            import_targets = self.import_targets

        export_targets: Union[Unset, list[int]] = UNSET
        if not isinstance(self.export_targets, Unset):
            export_targets = self.export_targets

        description = self.description

        comments = self.comments

        tenant: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenantRequest):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

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
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if import_targets is not UNSET:
            field_dict["import_targets"] = import_targets
        if export_targets is not UNSET:
            field_dict["export_targets"] = export_targets
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        identifier: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.identifier, Unset):
            identifier = UNSET
        elif isinstance(self.identifier, int):
            identifier = (None, str(self.identifier).encode(), "text/plain")
        else:
            identifier = (None, str(self.identifier).encode(), "text/plain")

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        slug = self.slug if isinstance(self.slug, Unset) else (None, str(self.slug).encode(), "text/plain")

        type_: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = (None, str(self.type_.value).encode(), "text/plain")

        status: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

        import_targets: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.import_targets, Unset):
            _temp_import_targets = self.import_targets
            import_targets = (None, json.dumps(_temp_import_targets).encode(), "application/json")

        export_targets: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.export_targets, Unset):
            _temp_export_targets = self.export_targets
            export_targets = (None, json.dumps(_temp_export_targets).encode(), "application/json")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        comments = (
            self.comments if isinstance(self.comments, Unset) else (None, str(self.comments).encode(), "text/plain")
        )

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
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if import_targets is not UNSET:
            field_dict["import_targets"] = import_targets
        if export_targets is not UNSET:
            field_dict["export_targets"] = export_targets
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_writable_l2vpn_request_custom_fields import PatchedWritableL2VPNRequestCustomFields

        d = dict(src_dict)

        def _parse_identifier(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        identifier = _parse_identifier(d.pop("identifier", UNSET))

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, PatchedWritableL2VPNRequestType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PatchedWritableL2VPNRequestType(_type_)

        _status = d.pop("status", UNSET)
        status: Union[Unset, PatchedWritableL2VPNRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PatchedWritableL2VPNRequestStatus(_status)

        import_targets = cast(list[int], d.pop("import_targets", UNSET))

        export_targets = cast(list[int], d.pop("export_targets", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

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

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedWritableL2VPNRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedWritableL2VPNRequestCustomFields.from_dict(_custom_fields)

        patched_writable_l2vpn_request = cls(
            identifier=identifier,
            name=name,
            slug=slug,
            type_=type_,
            status=status,
            import_targets=import_targets,
            export_targets=export_targets,
            description=description,
            comments=comments,
            tenant=tenant,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_writable_l2vpn_request.additional_properties = d
        return patched_writable_l2vpn_request

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
