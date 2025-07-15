import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_writable_ip_sec_proposal_request_authentication import (
    PatchedWritableIPSecProposalRequestAuthentication,
)
from ..models.patched_writable_ip_sec_proposal_request_encryption import PatchedWritableIPSecProposalRequestEncryption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_writable_ip_sec_proposal_request_custom_fields import (
        PatchedWritableIPSecProposalRequestCustomFields,
    )


T = TypeVar("T", bound="PatchedWritableIPSecProposalRequest")


@_attrs_define
class PatchedWritableIPSecProposalRequest:
    """Adds support for custom fields and tags.

    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        encryption_algorithm (Union[None, PatchedWritableIPSecProposalRequestEncryption, Unset]): * `aes-128-cbc` -
            128-bit AES (CBC)
            * `aes-128-gcm` - 128-bit AES (GCM)
            * `aes-192-cbc` - 192-bit AES (CBC)
            * `aes-192-gcm` - 192-bit AES (GCM)
            * `aes-256-cbc` - 256-bit AES (CBC)
            * `aes-256-gcm` - 256-bit AES (GCM)
            * `3des-cbc` - 3DES
            * `des-cbc` - DES
        authentication_algorithm (Union[None, PatchedWritableIPSecProposalRequestAuthentication, Unset]): * `hmac-sha1`
            - SHA-1 HMAC
            * `hmac-sha256` - SHA-256 HMAC
            * `hmac-sha384` - SHA-384 HMAC
            * `hmac-sha512` - SHA-512 HMAC
            * `hmac-md5` - MD5 HMAC
        sa_lifetime_seconds (Union[None, Unset, int]): Security association lifetime (seconds)
        sa_lifetime_data (Union[None, Unset, int]): Security association lifetime (in kilobytes)
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedWritableIPSecProposalRequestCustomFields]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    encryption_algorithm: Union[None, PatchedWritableIPSecProposalRequestEncryption, Unset] = UNSET
    authentication_algorithm: Union[None, PatchedWritableIPSecProposalRequestAuthentication, Unset] = UNSET
    sa_lifetime_seconds: Union[None, Unset, int] = UNSET
    sa_lifetime_data: Union[None, Unset, int] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedWritableIPSecProposalRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        encryption_algorithm: Union[None, Unset, str]
        if isinstance(self.encryption_algorithm, Unset):
            encryption_algorithm = UNSET
        elif isinstance(self.encryption_algorithm, PatchedWritableIPSecProposalRequestEncryption):
            encryption_algorithm = self.encryption_algorithm.value
        elif isinstance(self.encryption_algorithm, PatchedWritableIPSecProposalRequestEncryption):
            encryption_algorithm = self.encryption_algorithm.value
        elif isinstance(self.encryption_algorithm, PatchedWritableIPSecProposalRequestEncryption):
            encryption_algorithm = self.encryption_algorithm.value
        else:
            encryption_algorithm = self.encryption_algorithm

        authentication_algorithm: Union[None, Unset, str]
        if isinstance(self.authentication_algorithm, Unset):
            authentication_algorithm = UNSET
        elif isinstance(self.authentication_algorithm, PatchedWritableIPSecProposalRequestAuthentication):
            authentication_algorithm = self.authentication_algorithm.value
        elif isinstance(self.authentication_algorithm, PatchedWritableIPSecProposalRequestAuthentication):
            authentication_algorithm = self.authentication_algorithm.value
        elif isinstance(self.authentication_algorithm, PatchedWritableIPSecProposalRequestAuthentication):
            authentication_algorithm = self.authentication_algorithm.value
        else:
            authentication_algorithm = self.authentication_algorithm

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
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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

    def to_multipart(self) -> dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        encryption_algorithm: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.encryption_algorithm, Unset):
            encryption_algorithm = UNSET
        elif isinstance(self.encryption_algorithm, None):
            encryption_algorithm = (None, str(self.encryption_algorithm).encode(), "text/plain")
        elif isinstance(self.encryption_algorithm, PatchedWritableIPSecProposalRequestEncryption):
            encryption_algorithm = (None, str(self.encryption_algorithm.value).encode(), "text/plain")
        elif isinstance(self.encryption_algorithm, None):
            encryption_algorithm = (None, str(self.encryption_algorithm).encode(), "text/plain")
        elif isinstance(self.encryption_algorithm, PatchedWritableIPSecProposalRequestEncryption):
            encryption_algorithm = (None, str(self.encryption_algorithm.value).encode(), "text/plain")
        elif isinstance(self.encryption_algorithm, None):
            encryption_algorithm = (None, str(self.encryption_algorithm).encode(), "text/plain")
        else:
            encryption_algorithm = (None, str(self.encryption_algorithm.value).encode(), "text/plain")

        authentication_algorithm: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.authentication_algorithm, Unset):
            authentication_algorithm = UNSET
        elif isinstance(self.authentication_algorithm, None):
            authentication_algorithm = (None, str(self.authentication_algorithm).encode(), "text/plain")
        elif isinstance(self.authentication_algorithm, PatchedWritableIPSecProposalRequestAuthentication):
            authentication_algorithm = (None, str(self.authentication_algorithm.value).encode(), "text/plain")
        elif isinstance(self.authentication_algorithm, None):
            authentication_algorithm = (None, str(self.authentication_algorithm).encode(), "text/plain")
        elif isinstance(self.authentication_algorithm, PatchedWritableIPSecProposalRequestAuthentication):
            authentication_algorithm = (None, str(self.authentication_algorithm.value).encode(), "text/plain")
        elif isinstance(self.authentication_algorithm, None):
            authentication_algorithm = (None, str(self.authentication_algorithm).encode(), "text/plain")
        else:
            authentication_algorithm = (None, str(self.authentication_algorithm.value).encode(), "text/plain")

        sa_lifetime_seconds: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.sa_lifetime_seconds, Unset):
            sa_lifetime_seconds = UNSET
        elif isinstance(self.sa_lifetime_seconds, int):
            sa_lifetime_seconds = (None, str(self.sa_lifetime_seconds).encode(), "text/plain")
        else:
            sa_lifetime_seconds = (None, str(self.sa_lifetime_seconds).encode(), "text/plain")

        sa_lifetime_data: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.sa_lifetime_data, Unset):
            sa_lifetime_data = UNSET
        elif isinstance(self.sa_lifetime_data, int):
            sa_lifetime_data = (None, str(self.sa_lifetime_data).encode(), "text/plain")
        else:
            sa_lifetime_data = (None, str(self.sa_lifetime_data).encode(), "text/plain")

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

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_writable_ip_sec_proposal_request_custom_fields import (
            PatchedWritableIPSecProposalRequestCustomFields,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        def _parse_encryption_algorithm(
            data: object,
        ) -> Union[None, PatchedWritableIPSecProposalRequestEncryption, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                encryption_algorithm_type_1 = PatchedWritableIPSecProposalRequestEncryption(data)

                return encryption_algorithm_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                encryption_algorithm_type_2_type_1 = PatchedWritableIPSecProposalRequestEncryption(data)

                return encryption_algorithm_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                encryption_algorithm_type_3_type_1 = PatchedWritableIPSecProposalRequestEncryption(data)

                return encryption_algorithm_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, PatchedWritableIPSecProposalRequestEncryption, Unset], data)

        encryption_algorithm = _parse_encryption_algorithm(d.pop("encryption_algorithm", UNSET))

        def _parse_authentication_algorithm(
            data: object,
        ) -> Union[None, PatchedWritableIPSecProposalRequestAuthentication, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                authentication_algorithm_type_1 = PatchedWritableIPSecProposalRequestAuthentication(data)

                return authentication_algorithm_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                authentication_algorithm_type_2_type_1 = PatchedWritableIPSecProposalRequestAuthentication(data)

                return authentication_algorithm_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                authentication_algorithm_type_3_type_1 = PatchedWritableIPSecProposalRequestAuthentication(data)

                return authentication_algorithm_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, PatchedWritableIPSecProposalRequestAuthentication, Unset], data)

        authentication_algorithm = _parse_authentication_algorithm(d.pop("authentication_algorithm", UNSET))

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
        custom_fields: Union[Unset, PatchedWritableIPSecProposalRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedWritableIPSecProposalRequestCustomFields.from_dict(_custom_fields)

        patched_writable_ip_sec_proposal_request = cls(
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

        patched_writable_ip_sec_proposal_request.additional_properties = d
        return patched_writable_ip_sec_proposal_request

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
