from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ip_sec_proposal_request_authentication_algorithm import IPSecProposalRequestAuthenticationAlgorithm
from ..models.ip_sec_proposal_request_encryption_algorithm import IPSecProposalRequestEncryptionAlgorithm
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_sec_proposal_request_custom_fields import IPSecProposalRequestCustomFields
    from ..models.nested_tag_request import NestedTagRequest


T = TypeVar("T", bound="IPSecProposalRequest")


@_attrs_define
class IPSecProposalRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str):
        description (Union[Unset, str]):
        encryption_algorithm (Union[Unset, IPSecProposalRequestEncryptionAlgorithm]): * `aes-128-cbc` - 128-bit AES
            (CBC)
            * `aes-128-gcm` - 128-bit AES (GCM)
            * `aes-192-cbc` - 192-bit AES (CBC)
            * `aes-192-gcm` - 192-bit AES (GCM)
            * `aes-256-cbc` - 256-bit AES (CBC)
            * `aes-256-gcm` - 256-bit AES (GCM)
            * `3des-cbc` - 3DES
            * `des-cbc` - DES
        authentication_algorithm (Union[Unset, IPSecProposalRequestAuthenticationAlgorithm]): * `hmac-sha1` - SHA-1 HMAC
            * `hmac-sha256` - SHA-256 HMAC
            * `hmac-sha384` - SHA-384 HMAC
            * `hmac-sha512` - SHA-512 HMAC
            * `hmac-md5` - MD5 HMAC
        sa_lifetime_seconds (Union[None, Unset, int]): Security association lifetime (seconds)
        sa_lifetime_data (Union[None, Unset, int]): Security association lifetime (in kilobytes)
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, IPSecProposalRequestCustomFields]):
    """

    name: str
    description: Union[Unset, str] = UNSET
    encryption_algorithm: Union[Unset, IPSecProposalRequestEncryptionAlgorithm] = UNSET
    authentication_algorithm: Union[Unset, IPSecProposalRequestAuthenticationAlgorithm] = UNSET
    sa_lifetime_seconds: Union[None, Unset, int] = UNSET
    sa_lifetime_data: Union[None, Unset, int] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "IPSecProposalRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        encryption_algorithm: Union[Unset, str] = UNSET
        if not isinstance(self.encryption_algorithm, Unset):
            encryption_algorithm = self.encryption_algorithm.value

        authentication_algorithm: Union[Unset, str] = UNSET
        if not isinstance(self.authentication_algorithm, Unset):
            authentication_algorithm = self.authentication_algorithm.value

        sa_lifetime_seconds: Union[None, Unset, int]
        if isinstance(self.sa_lifetime_seconds, Unset):
            sa_lifetime_seconds = UNSET
        else:
            sa_lifetime_seconds = self.sa_lifetime_seconds

        sa_lifetime_data: Union[None, Unset, int]
        if isinstance(self.sa_lifetime_data, Unset):
            sa_lifetime_data = UNSET
        else:
            sa_lifetime_data = self.sa_lifetime_data

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
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if encryption_algorithm is not UNSET:
            field_dict["encryption_algorithm"] = encryption_algorithm
        if authentication_algorithm is not UNSET:
            field_dict["authentication_algorithm"] = authentication_algorithm
        if sa_lifetime_seconds is not UNSET:
            field_dict["sa_lifetime_seconds"] = sa_lifetime_seconds
        if sa_lifetime_data is not UNSET:
            field_dict["sa_lifetime_data"] = sa_lifetime_data
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_sec_proposal_request_custom_fields import IPSecProposalRequestCustomFields
        from ..models.nested_tag_request import NestedTagRequest

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        _encryption_algorithm = d.pop("encryption_algorithm", UNSET)
        encryption_algorithm: Union[Unset, IPSecProposalRequestEncryptionAlgorithm]
        if isinstance(_encryption_algorithm, Unset):
            encryption_algorithm = UNSET
        else:
            encryption_algorithm = IPSecProposalRequestEncryptionAlgorithm(_encryption_algorithm)

        _authentication_algorithm = d.pop("authentication_algorithm", UNSET)
        authentication_algorithm: Union[Unset, IPSecProposalRequestAuthenticationAlgorithm]
        if isinstance(_authentication_algorithm, Unset):
            authentication_algorithm = UNSET
        else:
            authentication_algorithm = IPSecProposalRequestAuthenticationAlgorithm(_authentication_algorithm)

        def _parse_sa_lifetime_seconds(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sa_lifetime_seconds = _parse_sa_lifetime_seconds(d.pop("sa_lifetime_seconds", UNSET))

        def _parse_sa_lifetime_data(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sa_lifetime_data = _parse_sa_lifetime_data(d.pop("sa_lifetime_data", UNSET))

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, IPSecProposalRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = IPSecProposalRequestCustomFields.from_dict(_custom_fields)

        ip_sec_proposal_request = cls(
            name=name,
            description=description,
            encryption_algorithm=encryption_algorithm,
            authentication_algorithm=authentication_algorithm,
            sa_lifetime_seconds=sa_lifetime_seconds,
            sa_lifetime_data=sa_lifetime_data,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        ip_sec_proposal_request.additional_properties = d
        return ip_sec_proposal_request

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
