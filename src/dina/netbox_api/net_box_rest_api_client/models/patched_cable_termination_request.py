from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_cable_termination_request_end import PatchedCableTerminationRequestEnd
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedCableTerminationRequest")


@_attrs_define
class PatchedCableTerminationRequest:
    """Adds support for custom fields and tags.

    Attributes:
        cable (Union[Unset, int]):
        cable_end (Union[Unset, PatchedCableTerminationRequestEnd]): * `A` - A
            * `B` - B
        termination_type (Union[Unset, str]):
        termination_id (Union[Unset, int]):
    """

    cable: Union[Unset, int] = UNSET
    cable_end: Union[Unset, PatchedCableTerminationRequestEnd] = UNSET
    termination_type: Union[Unset, str] = UNSET
    termination_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cable = self.cable

        cable_end: Union[Unset, str] = UNSET
        if not isinstance(self.cable_end, Unset):
            cable_end = self.cable_end.value

        termination_type = self.termination_type

        termination_id = self.termination_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cable is not UNSET:
            field_dict["cable"] = cable
        if cable_end is not UNSET:
            field_dict["cable_end"] = cable_end
        if termination_type is not UNSET:
            field_dict["termination_type"] = termination_type
        if termination_id is not UNSET:
            field_dict["termination_id"] = termination_id

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        cable = self.cable if isinstance(self.cable, Unset) else (None, str(self.cable).encode(), "text/plain")

        cable_end: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.cable_end, Unset):
            cable_end = (None, str(self.cable_end.value).encode(), "text/plain")

        termination_type = (
            self.termination_type
            if isinstance(self.termination_type, Unset)
            else (None, str(self.termination_type).encode(), "text/plain")
        )

        termination_id = (
            self.termination_id
            if isinstance(self.termination_id, Unset)
            else (None, str(self.termination_id).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if cable is not UNSET:
            field_dict["cable"] = cable
        if cable_end is not UNSET:
            field_dict["cable_end"] = cable_end
        if termination_type is not UNSET:
            field_dict["termination_type"] = termination_type
        if termination_id is not UNSET:
            field_dict["termination_id"] = termination_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cable = d.pop("cable", UNSET)

        _cable_end = d.pop("cable_end", UNSET)
        cable_end: Union[Unset, PatchedCableTerminationRequestEnd]
        if isinstance(_cable_end, Unset):
            cable_end = UNSET
        else:
            cable_end = PatchedCableTerminationRequestEnd(_cable_end)

        termination_type = d.pop("termination_type", UNSET)

        termination_id = d.pop("termination_id", UNSET)

        patched_cable_termination_request = cls(
            cable=cable,
            cable_end=cable_end,
            termination_type=termination_type,
            termination_id=termination_id,
        )

        patched_cable_termination_request.additional_properties = d
        return patched_cable_termination_request

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
