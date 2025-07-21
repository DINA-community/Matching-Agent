from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ike_proposal_request_authentication_algorithm import (
    IKEProposalRequestAuthenticationAlgorithm,
)
from ..models.ike_proposal_request_authentication_method import (
    IKEProposalRequestAuthenticationMethod,
)
from ..models.ike_proposal_request_encryption_algorithm import (
    IKEProposalRequestEncryptionAlgorithm,
)
from ..models.ike_proposal_request_group import IKEProposalRequestGroup
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ike_proposal_request_custom_fields import (
        IKEProposalRequestCustomFields,
    )
    from ..models.nested_tag_request import NestedTagRequest


T = TypeVar("T", bound="IKEProposalRequest")


@_attrs_define
class IKEProposalRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (str):
        authentication_method (IKEProposalRequestAuthenticationMethod): * `preshared-keys` - Pre-shared keys
            * `certificates` - Certificates
            * `rsa-signatures` - RSA signatures
            * `dsa-signatures` - DSA signatures
        encryption_algorithm (IKEProposalRequestEncryptionAlgorithm): * `aes-128-cbc` - 128-bit AES (CBC)
            * `aes-128-gcm` - 128-bit AES (GCM)
            * `aes-192-cbc` - 192-bit AES (CBC)
            * `aes-192-gcm` - 192-bit AES (GCM)
            * `aes-256-cbc` - 256-bit AES (CBC)
            * `aes-256-gcm` - 256-bit AES (GCM)
            * `3des-cbc` - 3DES
            * `des-cbc` - DES
        group (IKEProposalRequestGroup): * `1` - Group 1
            * `2` - Group 2
            * `5` - Group 5
            * `14` - Group 14
            * `15` - Group 15
            * `16` - Group 16
            * `17` - Group 17
            * `18` - Group 18
            * `19` - Group 19
            * `20` - Group 20
            * `21` - Group 21
            * `22` - Group 22
            * `23` - Group 23
            * `24` - Group 24
            * `25` - Group 25
            * `26` - Group 26
            * `27` - Group 27
            * `28` - Group 28
            * `29` - Group 29
            * `30` - Group 30
            * `31` - Group 31
            * `32` - Group 32
            * `33` - Group 33
            * `34` - Group 34
        description (Union[Unset, str]):
        authentication_algorithm (Union[Unset, IKEProposalRequestAuthenticationAlgorithm]): * `hmac-sha1` - SHA-1 HMAC
            * `hmac-sha256` - SHA-256 HMAC
            * `hmac-sha384` - SHA-384 HMAC
            * `hmac-sha512` - SHA-512 HMAC
            * `hmac-md5` - MD5 HMAC
        sa_lifetime (Union[None, Unset, int]): Security association lifetime (in seconds)
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, IKEProposalRequestCustomFields]):
    """

    name: str
    authentication_method: IKEProposalRequestAuthenticationMethod
    encryption_algorithm: IKEProposalRequestEncryptionAlgorithm
    group: IKEProposalRequestGroup
    description: Union[Unset, str] = UNSET
    authentication_algorithm: Union[
        Unset, IKEProposalRequestAuthenticationAlgorithm
    ] = UNSET
    sa_lifetime: Union[None, Unset, int] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "IKEProposalRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        authentication_method = self.authentication_method.value

        encryption_algorithm = self.encryption_algorithm.value

        group = self.group.value

        description = self.description

        authentication_algorithm: Union[Unset, str] = UNSET
        if not isinstance(self.authentication_algorithm, Unset):
            authentication_algorithm = self.authentication_algorithm.value

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
                "name": name,
                "authentication_method": authentication_method,
                "encryption_algorithm": encryption_algorithm,
                "group": group,
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
        from ..models.ike_proposal_request_custom_fields import (
            IKEProposalRequestCustomFields,
        )
        from ..models.nested_tag_request import NestedTagRequest

        d = dict(src_dict)
        name = d.pop("name")

        authentication_method = IKEProposalRequestAuthenticationMethod(
            d.pop("authentication_method")
        )

        encryption_algorithm = IKEProposalRequestEncryptionAlgorithm(
            d.pop("encryption_algorithm")
        )

        group = IKEProposalRequestGroup(d.pop("group"))

        description = d.pop("description", UNSET)

        _authentication_algorithm = d.pop("authentication_algorithm", UNSET)
        authentication_algorithm: Union[
            Unset, IKEProposalRequestAuthenticationAlgorithm
        ]
        if isinstance(_authentication_algorithm, Unset):
            authentication_algorithm = UNSET
        else:
            authentication_algorithm = IKEProposalRequestAuthenticationAlgorithm(
                _authentication_algorithm
            )

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
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, IKEProposalRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = IKEProposalRequestCustomFields.from_dict(_custom_fields)

        ike_proposal_request = cls(
            name=name,
            authentication_method=authentication_method,
            encryption_algorithm=encryption_algorithm,
            group=group,
            description=description,
            authentication_algorithm=authentication_algorithm,
            sa_lifetime=sa_lifetime,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        ike_proposal_request.additional_properties = d
        return ike_proposal_request

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
