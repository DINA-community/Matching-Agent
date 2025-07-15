import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_sec_policy_custom_fields import IPSecPolicyCustomFields
    from ..models.ip_sec_policy_pfs_group import IPSecPolicyPfsGroup
    from ..models.ip_sec_proposal import IPSecProposal
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="IPSecPolicy")


@_attrs_define
class IPSecPolicy:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        name (str):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        description (Union[Unset, str]):
        proposals (Union[Unset, list['IPSecProposal']]):
        pfs_group (Union[Unset, IPSecPolicyPfsGroup]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, IPSecPolicyCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    description: Union[Unset, str] = UNSET
    proposals: Union[Unset, list["IPSecProposal"]] = UNSET
    pfs_group: Union[Unset, "IPSecPolicyPfsGroup"] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "IPSecPolicyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        description = self.description

        proposals: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.proposals, Unset):
            proposals = []
            for proposals_item_data in self.proposals:
                proposals_item = proposals_item_data.to_dict()
                proposals.append(proposals_item)

        pfs_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pfs_group, Unset):
            pfs_group = self.pfs_group.to_dict()

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
                "name": name,
                "created": created,
                "last_updated": last_updated,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if proposals is not UNSET:
            field_dict["proposals"] = proposals
        if pfs_group is not UNSET:
            field_dict["pfs_group"] = pfs_group
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_sec_policy_custom_fields import IPSecPolicyCustomFields
        from ..models.ip_sec_policy_pfs_group import IPSecPolicyPfsGroup
        from ..models.ip_sec_proposal import IPSecProposal
        from ..models.nested_tag import NestedTag

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

        description = d.pop("description", UNSET)

        proposals = []
        _proposals = d.pop("proposals", UNSET)
        for proposals_item_data in _proposals or []:
            proposals_item = IPSecProposal.from_dict(proposals_item_data)

            proposals.append(proposals_item)

        _pfs_group = d.pop("pfs_group", UNSET)
        pfs_group: Union[Unset, IPSecPolicyPfsGroup]
        if isinstance(_pfs_group, Unset):
            pfs_group = UNSET
        else:
            pfs_group = IPSecPolicyPfsGroup.from_dict(_pfs_group)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, IPSecPolicyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = IPSecPolicyCustomFields.from_dict(_custom_fields)

        ip_sec_policy = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            created=created,
            last_updated=last_updated,
            description=description,
            proposals=proposals,
            pfs_group=pfs_group,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        ip_sec_policy.additional_properties = d
        return ip_sec_policy

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
