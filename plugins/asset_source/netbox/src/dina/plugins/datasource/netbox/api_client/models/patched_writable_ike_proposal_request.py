import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_writable_ike_proposal_request_authentication_algorithm_type_1 import (
    PatchedWritableIKEProposalRequestAuthenticationAlgorithmType1,
)
from ..models.patched_writable_ike_proposal_request_authentication_algorithm_type_2_type_1 import (
    PatchedWritableIKEProposalRequestAuthenticationAlgorithmType2Type1,
)
from ..models.patched_writable_ike_proposal_request_authentication_algorithm_type_3_type_1 import (
    PatchedWritableIKEProposalRequestAuthenticationAlgorithmType3Type1,
)
from ..models.patched_writable_ike_proposal_request_authentication_method import (
    PatchedWritableIKEProposalRequestAuthenticationMethod,
)
from ..models.patched_writable_ike_proposal_request_encryption_algorithm import (
    PatchedWritableIKEProposalRequestEncryptionAlgorithm,
)
from ..models.patched_writable_ike_proposal_request_group import (
    PatchedWritableIKEProposalRequestGroup,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_writable_ike_proposal_request_custom_fields import (
        PatchedWritableIKEProposalRequestCustomFields,
    )


T = TypeVar("T", bound="PatchedWritableIKEProposalRequest")


@_attrs_define
class PatchedWritableIKEProposalRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        authentication_method (Union[Unset, PatchedWritableIKEProposalRequestAuthenticationMethod]): * `preshared-keys`
            - Pre-shared keys
            * `certificates` - Certificates
            * `rsa-signatures` - RSA signatures
            * `dsa-signatures` - DSA signatures
        encryption_algorithm (Union[Unset, PatchedWritableIKEProposalRequestEncryptionAlgorithm]): * `aes-128-cbc` -
            128-bit AES (CBC)
            * `aes-128-gcm` - 128-bit AES (GCM)
            * `aes-192-cbc` - 192-bit AES (CBC)
            * `aes-192-gcm` - 192-bit AES (GCM)
            * `aes-256-cbc` - 256-bit AES (CBC)
            * `aes-256-gcm` - 256-bit AES (GCM)
            * `3des-cbc` - 3DES
            * `des-cbc` - DES
        authentication_algorithm (Union[None, PatchedWritableIKEProposalRequestAuthenticationAlgorithmType1,
            PatchedWritableIKEProposalRequestAuthenticationAlgorithmType2Type1,
            PatchedWritableIKEProposalRequestAuthenticationAlgorithmType3Type1, Unset]): * `hmac-sha1` - SHA-1 HMAC
            * `hmac-sha256` - SHA-256 HMAC
            * `hmac-sha384` - SHA-384 HMAC
            * `hmac-sha512` - SHA-512 HMAC
            * `hmac-md5` - MD5 HMAC
        group (Union[Unset, PatchedWritableIKEProposalRequestGroup]): Diffie-Hellman group ID

            * `1` - Group 1
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
        sa_lifetime (Union[None, Unset, int]): Security association lifetime (in seconds)
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedWritableIKEProposalRequestCustomFields]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    authentication_method: Union[
        Unset, PatchedWritableIKEProposalRequestAuthenticationMethod
    ] = UNSET
    encryption_algorithm: Union[
        Unset, PatchedWritableIKEProposalRequestEncryptionAlgorithm
    ] = UNSET
    authentication_algorithm: Union[
        None,
        PatchedWritableIKEProposalRequestAuthenticationAlgorithmType1,
        PatchedWritableIKEProposalRequestAuthenticationAlgorithmType2Type1,
        PatchedWritableIKEProposalRequestAuthenticationAlgorithmType3Type1,
        Unset,
    ] = UNSET
    group: Union[Unset, PatchedWritableIKEProposalRequestGroup] = UNSET
    sa_lifetime: Union[None, Unset, int] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedWritableIKEProposalRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        authentication_method: Union[Unset, str] = UNSET
        if not isinstance(self.authentication_method, Unset):
            authentication_method = self.authentication_method.value

        encryption_algorithm: Union[Unset, str] = UNSET
        if not isinstance(self.encryption_algorithm, Unset):
            encryption_algorithm = self.encryption_algorithm.value

        authentication_algorithm: Union[None, Unset, str]
        if isinstance(self.authentication_algorithm, Unset):
            authentication_algorithm = UNSET
        elif isinstance(
            self.authentication_algorithm,
            PatchedWritableIKEProposalRequestAuthenticationAlgorithmType1,
        ):
            authentication_algorithm = self.authentication_algorithm.value
        elif isinstance(
            self.authentication_algorithm,
            PatchedWritableIKEProposalRequestAuthenticationAlgorithmType2Type1,
        ):
            authentication_algorithm = self.authentication_algorithm.value
        elif isinstance(
            self.authentication_algorithm,
            PatchedWritableIKEProposalRequestAuthenticationAlgorithmType3Type1,
        ):
            authentication_algorithm = self.authentication_algorithm.value
        else:
            authentication_algorithm = self.authentication_algorithm

        group: Union[Unset, int] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.value

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
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if authentication_method is not UNSET:
            field_dict["authentication_method"] = authentication_method
        if encryption_algorithm is not UNSET:
            field_dict["encryption_algorithm"] = encryption_algorithm
        if authentication_algorithm is not UNSET:
            field_dict["authentication_algorithm"] = authentication_algorithm
        if group is not UNSET:
            field_dict["group"] = group
        if sa_lifetime is not UNSET:
            field_dict["sa_lifetime"] = sa_lifetime
        if comments is not UNSET:
            field_dict["comments"] = comments
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

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        authentication_method: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.authentication_method, Unset):
            authentication_method = (
                None,
                str(self.authentication_method.value).encode(),
                "text/plain",
            )

        encryption_algorithm: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.encryption_algorithm, Unset):
            encryption_algorithm = (
                None,
                str(self.encryption_algorithm.value).encode(),
                "text/plain",
            )

        authentication_algorithm: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.authentication_algorithm, Unset):
            authentication_algorithm = UNSET
        elif isinstance(self.authentication_algorithm, None):
            authentication_algorithm = (
                None,
                str(self.authentication_algorithm).encode(),
                "text/plain",
            )
        elif isinstance(
            self.authentication_algorithm,
            PatchedWritableIKEProposalRequestAuthenticationAlgorithmType1,
        ):
            authentication_algorithm = (
                None,
                str(self.authentication_algorithm.value).encode(),
                "text/plain",
            )
        elif isinstance(self.authentication_algorithm, None):
            authentication_algorithm = (
                None,
                str(self.authentication_algorithm).encode(),
                "text/plain",
            )
        elif isinstance(
            self.authentication_algorithm,
            PatchedWritableIKEProposalRequestAuthenticationAlgorithmType2Type1,
        ):
            authentication_algorithm = (
                None,
                str(self.authentication_algorithm.value).encode(),
                "text/plain",
            )
        elif isinstance(self.authentication_algorithm, None):
            authentication_algorithm = (
                None,
                str(self.authentication_algorithm).encode(),
                "text/plain",
            )
        else:
            authentication_algorithm = (
                None,
                str(self.authentication_algorithm.value).encode(),
                "text/plain",
            )

        group: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.group, Unset):
            group = (None, str(self.group.value).encode(), "text/plain")

        sa_lifetime: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.sa_lifetime, Unset):
            sa_lifetime = UNSET
        elif isinstance(self.sa_lifetime, int):
            sa_lifetime = (None, str(self.sa_lifetime).encode(), "text/plain")
        else:
            sa_lifetime = (None, str(self.sa_lifetime).encode(), "text/plain")

        comments = (
            self.comments
            if isinstance(self.comments, Unset)
            else (None, str(self.comments).encode(), "text/plain")
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
        if description is not UNSET:
            field_dict["description"] = description
        if authentication_method is not UNSET:
            field_dict["authentication_method"] = authentication_method
        if encryption_algorithm is not UNSET:
            field_dict["encryption_algorithm"] = encryption_algorithm
        if authentication_algorithm is not UNSET:
            field_dict["authentication_algorithm"] = authentication_algorithm
        if group is not UNSET:
            field_dict["group"] = group
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
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_writable_ike_proposal_request_custom_fields import (
            PatchedWritableIKEProposalRequestCustomFields,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _authentication_method = d.pop("authentication_method", UNSET)
        authentication_method: Union[
            Unset, PatchedWritableIKEProposalRequestAuthenticationMethod
        ]
        if isinstance(_authentication_method, Unset):
            authentication_method = UNSET
        else:
            authentication_method = (
                PatchedWritableIKEProposalRequestAuthenticationMethod(
                    _authentication_method
                )
            )

        _encryption_algorithm = d.pop("encryption_algorithm", UNSET)
        encryption_algorithm: Union[
            Unset, PatchedWritableIKEProposalRequestEncryptionAlgorithm
        ]
        if isinstance(_encryption_algorithm, Unset):
            encryption_algorithm = UNSET
        else:
            encryption_algorithm = PatchedWritableIKEProposalRequestEncryptionAlgorithm(
                _encryption_algorithm
            )

        def _parse_authentication_algorithm(
            data: object,
        ) -> Union[
            None,
            PatchedWritableIKEProposalRequestAuthenticationAlgorithmType1,
            PatchedWritableIKEProposalRequestAuthenticationAlgorithmType2Type1,
            PatchedWritableIKEProposalRequestAuthenticationAlgorithmType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                authentication_algorithm_type_1 = (
                    PatchedWritableIKEProposalRequestAuthenticationAlgorithmType1(data)
                )

                return authentication_algorithm_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                authentication_algorithm_type_2_type_1 = (
                    PatchedWritableIKEProposalRequestAuthenticationAlgorithmType2Type1(
                        data
                    )
                )

                return authentication_algorithm_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                authentication_algorithm_type_3_type_1 = (
                    PatchedWritableIKEProposalRequestAuthenticationAlgorithmType3Type1(
                        data
                    )
                )

                return authentication_algorithm_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PatchedWritableIKEProposalRequestAuthenticationAlgorithmType1,
                    PatchedWritableIKEProposalRequestAuthenticationAlgorithmType2Type1,
                    PatchedWritableIKEProposalRequestAuthenticationAlgorithmType3Type1,
                    Unset,
                ],
                data,
            )

        authentication_algorithm = _parse_authentication_algorithm(
            d.pop("authentication_algorithm", UNSET)
        )

        _group = d.pop("group", UNSET)
        group: Union[Unset, PatchedWritableIKEProposalRequestGroup]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = PatchedWritableIKEProposalRequestGroup(_group)

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
        custom_fields: Union[Unset, PatchedWritableIKEProposalRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedWritableIKEProposalRequestCustomFields.from_dict(
                _custom_fields
            )

        patched_writable_ike_proposal_request = cls(
            name=name,
            description=description,
            authentication_method=authentication_method,
            encryption_algorithm=encryption_algorithm,
            authentication_algorithm=authentication_algorithm,
            group=group,
            sa_lifetime=sa_lifetime,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_writable_ike_proposal_request.additional_properties = d
        return patched_writable_ike_proposal_request

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
