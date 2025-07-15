import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_tenant import BriefTenant
    from ..models.nested_tag import NestedTag
    from ..models.route_target import RouteTarget
    from ..models.vrf_custom_fields import VRFCustomFields


T = TypeVar("T", bound="VRF")


@_attrs_define
class VRF:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        name (str):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        ipaddress_count (int):
        prefix_count (int):
        rd (Union[None, Unset, str]): Unique route distinguisher (as defined in RFC 4364)
        tenant (Union['BriefTenant', None, Unset]):
        enforce_unique (Union[Unset, bool]): Prevent duplicate prefixes/IP addresses within this VRF
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        import_targets (Union[Unset, list['RouteTarget']]):
        export_targets (Union[Unset, list['RouteTarget']]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, VRFCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    ipaddress_count: int
    prefix_count: int
    rd: Union[None, Unset, str] = UNSET
    tenant: Union["BriefTenant", None, Unset] = UNSET
    enforce_unique: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    import_targets: Union[Unset, list["RouteTarget"]] = UNSET
    export_targets: Union[Unset, list["RouteTarget"]] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "VRFCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_tenant import BriefTenant

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

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

        ipaddress_count = self.ipaddress_count

        prefix_count = self.prefix_count

        rd: Union[None, Unset, str]
        if isinstance(self.rd, Unset):
            rd = UNSET
        else:
            rd = self.rd

        tenant: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenant):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        enforce_unique = self.enforce_unique

        description = self.description

        comments = self.comments

        import_targets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.import_targets, Unset):
            import_targets = []
            for import_targets_item_data in self.import_targets:
                import_targets_item = import_targets_item_data.to_dict()
                import_targets.append(import_targets_item)

        export_targets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.export_targets, Unset):
            export_targets = []
            for export_targets_item_data in self.export_targets:
                export_targets_item = export_targets_item_data.to_dict()
                export_targets.append(export_targets_item)

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
                "name": name,
                "created": created,
                "last_updated": last_updated,
                "ipaddress_count": ipaddress_count,
                "prefix_count": prefix_count,
            }
        )
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
        from ..models.brief_tenant import BriefTenant
        from ..models.nested_tag import NestedTag
        from ..models.route_target import RouteTarget
        from ..models.vrf_custom_fields import VRFCustomFields

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

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

        ipaddress_count = d.pop("ipaddress_count")

        prefix_count = d.pop("prefix_count")

        def _parse_rd(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rd = _parse_rd(d.pop("rd", UNSET))

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

        enforce_unique = d.pop("enforce_unique", UNSET)

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        import_targets = []
        _import_targets = d.pop("import_targets", UNSET)
        for import_targets_item_data in _import_targets or []:
            import_targets_item = RouteTarget.from_dict(import_targets_item_data)

            import_targets.append(import_targets_item)

        export_targets = []
        _export_targets = d.pop("export_targets", UNSET)
        for export_targets_item_data in _export_targets or []:
            export_targets_item = RouteTarget.from_dict(export_targets_item_data)

            export_targets.append(export_targets_item)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, VRFCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = VRFCustomFields.from_dict(_custom_fields)

        vrf = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            created=created,
            last_updated=last_updated,
            ipaddress_count=ipaddress_count,
            prefix_count=prefix_count,
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

        vrf.additional_properties = d
        return vrf

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
