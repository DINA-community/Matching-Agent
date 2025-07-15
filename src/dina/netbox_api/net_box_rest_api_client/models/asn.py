import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asn_custom_fields import ASNCustomFields
    from ..models.brief_rir import BriefRIR
    from ..models.brief_tenant import BriefTenant
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="ASN")


@_attrs_define
class ASN:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        asn (int): 16- or 32-bit autonomous system number
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        site_count (int):
        provider_count (int):
        rir (Union['BriefRIR', None, Unset]):
        tenant (Union['BriefTenant', None, Unset]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, ASNCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    asn: int
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    site_count: int
    provider_count: int
    rir: Union["BriefRIR", None, Unset] = UNSET
    tenant: Union["BriefTenant", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "ASNCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_rir import BriefRIR
        from ..models.brief_tenant import BriefTenant

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        asn = self.asn

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

        site_count = self.site_count

        provider_count = self.provider_count

        rir: Union[None, Unset, dict[str, Any]]
        if isinstance(self.rir, Unset):
            rir = UNSET
        elif isinstance(self.rir, BriefRIR):
            rir = self.rir.to_dict()
        else:
            rir = self.rir

        tenant: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenant):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

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
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "asn": asn,
                "created": created,
                "last_updated": last_updated,
                "site_count": site_count,
                "provider_count": provider_count,
            }
        )
        if rir is not UNSET:
            field_dict["rir"] = rir
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
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
        from ..models.asn_custom_fields import ASNCustomFields
        from ..models.brief_rir import BriefRIR
        from ..models.brief_tenant import BriefTenant
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        asn = d.pop("asn")

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

        site_count = d.pop("site_count")

        provider_count = d.pop("provider_count")

        def _parse_rir(data: object) -> Union["BriefRIR", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rir_type_1 = BriefRIR.from_dict(data)

                return rir_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefRIR", None, Unset], data)

        rir = _parse_rir(d.pop("rir", UNSET))

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

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, ASNCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ASNCustomFields.from_dict(_custom_fields)

        asn = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            asn=asn,
            created=created,
            last_updated=last_updated,
            site_count=site_count,
            provider_count=provider_count,
            rir=rir,
            tenant=tenant,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        asn.additional_properties = d
        return asn

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
