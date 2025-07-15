from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedXGenericUriRequest")


@_attrs_define
class PatchedXGenericUriRequest:
    """REST API Model Serializer for XGenericUri.

    Attributes:
        content_type (Union[Unset, str]):
        namespace (Union[Unset, str]):
        uri (Union[Unset, str]):
    """

    content_type: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    uri: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        namespace = self.namespace

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        content_type = (
            self.content_type
            if isinstance(self.content_type, Unset)
            else (None, str(self.content_type).encode(), "text/plain")
        )

        namespace = (
            self.namespace if isinstance(self.namespace, Unset) else (None, str(self.namespace).encode(), "text/plain")
        )

        uri = self.uri if isinstance(self.uri, Unset) else (None, str(self.uri).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_type = d.pop("content_type", UNSET)

        namespace = d.pop("namespace", UNSET)

        uri = d.pop("uri", UNSET)

        patched_x_generic_uri_request = cls(
            content_type=content_type,
            namespace=namespace,
            uri=uri,
        )

        patched_x_generic_uri_request.additional_properties = d
        return patched_x_generic_uri_request

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
