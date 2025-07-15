import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ike_proposal_authentication_algorithm import IKEProposalAuthenticationAlgorithm
    from ..models.ike_proposal_authentication_method import IKEProposalAuthenticationMethod
    from ..models.ike_proposal_custom_fields import IKEProposalCustomFields
    from ..models.ike_proposal_encryption_algorithm import IKEProposalEncryptionAlgorithm
    from ..models.ike_proposal_group import IKEProposalGroup
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="IKEProposal")


@_attrs_define
class IKEProposal:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        name (str):
        authentication_method (IKEProposalAuthenticationMethod):
        encryption_algorithm (IKEProposalEncryptionAlgorithm):
        group (IKEProposalGroup):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        description (Union[Unset, str]):
        authentication_algorithm (Union[Unset, IKEProposalAuthenticationAlgorithm]):
        sa_lifetime (Union[None, Unset, int]): Security association lifetime (in seconds)
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, IKEProposalCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    name: str
    authentication_method: "IKEProposalAuthenticationMethod"
    encryption_algorithm: "IKEProposalEncryptionAlgorithm"
    group: "IKEProposalGroup"
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    description: Union[Unset, str] = UNSET
    authentication_algorithm: Union[Unset, "IKEProposalAuthenticationAlgorithm"] = UNSET
    sa_lifetime: Union[None, Unset, int] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "IKEProposalCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        name = self.name

        authentication_method = self.authentication_method.to_dict()

        encryption_algorithm = self.encryption_algorithm.to_dict()

        group = self.group.to_dict()

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

        authentication_algorithm: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.authentication_algorithm, Unset):
            authentication_algorithm = self.authentication_algorithm.to_dict()

        sa_lifetime: Union[None, Unset, int]
        if isinstance(self.sa_lifetime, Unset):
            sa_lifetime = UNSET
        else:
            sa_lifetime = self.sa_lifetime

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
                "authentication_method": authentication_method,
                "encryption_algorithm": encryption_algorithm,
                "group": group,
                "created": created,
                "last_updated": last_updated,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if authentication_algorithm is not UNSET:
            field_dict["authentication_algorithm"] = authentication_algorithm
        if sa_lifetime is not UNSET:
            field_dict["sa_lifetime"] = sa_lifetime
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ike_proposal_authentication_algorithm import IKEProposalAuthenticationAlgorithm
        from ..models.ike_proposal_authentication_method import IKEProposalAuthenticationMethod
        from ..models.ike_proposal_custom_fields import IKEProposalCustomFields
        from ..models.ike_proposal_encryption_algorithm import IKEProposalEncryptionAlgorithm
        from ..models.ike_proposal_group import IKEProposalGroup
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        name = d.pop("name")

        authentication_method = IKEProposalAuthenticationMethod.from_dict(d.pop("authentication_method"))

        encryption_algorithm = IKEProposalEncryptionAlgorithm.from_dict(d.pop("encryption_algorithm"))

        group = IKEProposalGroup.from_dict(d.pop("group"))

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

        _authentication_algorithm = d.pop("authentication_algorithm", UNSET)
        authentication_algorithm: Union[Unset, IKEProposalAuthenticationAlgorithm]
        if isinstance(_authentication_algorithm, Unset):
            authentication_algorithm = UNSET
        else:
            authentication_algorithm = IKEProposalAuthenticationAlgorithm.from_dict(_authentication_algorithm)

        def _parse_sa_lifetime(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sa_lifetime = _parse_sa_lifetime(d.pop("sa_lifetime", UNSET))

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, IKEProposalCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = IKEProposalCustomFields.from_dict(_custom_fields)

        ike_proposal = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            name=name,
            authentication_method=authentication_method,
            encryption_algorithm=encryption_algorithm,
            group=group,
            created=created,
            last_updated=last_updated,
            description=description,
            authentication_algorithm=authentication_algorithm,
            sa_lifetime=sa_lifetime,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        ike_proposal.additional_properties = d
        return ike_proposal

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
