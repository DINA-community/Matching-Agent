import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_vrf_request_custom_fields import PatchedVRFRequestCustomFields


T = TypeVar("T", bound="PatchedVRFRequest")


@_attrs_define
class PatchedVRFRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (Union[Unset, str]):
        rd (Union[None, Unset, str]): Unique route distinguisher (as defined in RFC 4364)
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        enforce_unique (Union[Unset, bool]): Prevent duplicate prefixes/IP addresses within this VRF
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        import_targets (Union[Unset, list[int]]):
        export_targets (Union[Unset, list[int]]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedVRFRequestCustomFields]):
    """

    name: Union[Unset, str] = UNSET
    rd: Union[None, Unset, str] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    enforce_unique: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    import_targets: Union[Unset, list[int]] = UNSET
    export_targets: Union[Unset, list[int]] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedVRFRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_tenant_request import BriefTenantRequest

        name = self.name

        rd: Union[None, Unset, str]
        if isinstance(self.rd, Unset):
            rd = UNSET
        else:
            rd = self.rd

        tenant: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenantRequest):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        enforce_unique = self.enforce_unique

        description = self.description

        comments = self.comments

        import_targets: Union[Unset, list[int]] = UNSET
        if not isinstance(self.import_targets, Unset):
            import_targets = self.import_targets

        export_targets: Union[Unset, list[int]] = UNSET
        if not isinstance(self.export_targets, Unset):
            export_targets = self.export_targets

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
        if rd is not UNSET:
            field_dict["rd"] = rd
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if enforce_unique is not UNSET:
            field_dict["enforce_unique"] = enforce_unique
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if import_targets is not UNSET:
            field_dict["import_targets"] = import_targets
        if export_targets is not UNSET:
            field_dict["export_targets"] = export_targets
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (
            self.name
            if isinstance(self.name, Unset)
            else (None, str(self.name).encode(), "text/plain")
        )

        rd: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.rd, Unset):
            rd = UNSET
        elif isinstance(self.rd, str):
            rd = (None, str(self.rd).encode(), "text/plain")
        else:
            rd = (None, str(self.rd).encode(), "text/plain")

        tenant: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, int):
            tenant = (None, str(self.tenant).encode(), "text/plain")
        elif isinstance(self.tenant, None):
            tenant = (None, str(self.tenant).encode(), "text/plain")
        elif isinstance(self.tenant, BriefTenantRequest):
            tenant = (
                None,
                json.dumps(self.tenant.to_dict()).encode(),
                "application/json",
            )
        else:
            tenant = (None, str(self.tenant).encode(), "text/plain")

        enforce_unique = (
            self.enforce_unique
            if isinstance(self.enforce_unique, Unset)
            else (None, str(self.enforce_unique).encode(), "text/plain")
        )

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        comments = (
            self.comments
            if isinstance(self.comments, Unset)
            else (None, str(self.comments).encode(), "text/plain")
        )

        import_targets: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.import_targets, Unset):
            _temp_import_targets = self.import_targets
            import_targets = (
                None,
                json.dumps(_temp_import_targets).encode(),
                "application/json",
            )

        export_targets: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.export_targets, Unset):
            _temp_export_targets = self.export_targets
            export_targets = (
                None,
                json.dumps(_temp_export_targets).encode(),
                "application/json",
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
            custom_fields = (
                None,
                json.dumps(self.custom_fields.to_dict()).encode(),
                "application/json",
            )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if rd is not UNSET:
            field_dict["rd"] = rd
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if enforce_unique is not UNSET:
            field_dict["enforce_unique"] = enforce_unique
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if import_targets is not UNSET:
            field_dict["import_targets"] = import_targets
        if export_targets is not UNSET:
            field_dict["export_targets"] = export_targets
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_vrf_request_custom_fields import (
            PatchedVRFRequestCustomFields,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_rd(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rd = _parse_rd(d.pop("rd", UNSET))

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

        enforce_unique = d.pop("enforce_unique", UNSET)

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        import_targets = cast(list[int], d.pop("import_targets", UNSET))

        export_targets = cast(list[int], d.pop("export_targets", UNSET))

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedVRFRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedVRFRequestCustomFields.from_dict(_custom_fields)

        patched_vrf_request = cls(
            name=name,
            rd=rd,
            tenant=tenant,
            enforce_unique=enforce_unique,
            description=description,
            comments=comments,
            import_targets=import_targets,
            export_targets=export_targets,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_vrf_request.additional_properties = d
        return patched_vrf_request

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
