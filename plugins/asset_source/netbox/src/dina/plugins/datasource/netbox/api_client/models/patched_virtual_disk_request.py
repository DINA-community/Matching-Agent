import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_virtual_machine_request import BriefVirtualMachineRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_virtual_disk_request_custom_fields import (
        PatchedVirtualDiskRequestCustomFields,
    )


T = TypeVar("T", bound="PatchedVirtualDiskRequest")


@_attrs_define
class PatchedVirtualDiskRequest:
    """Adds support for custom fields and tags.

    Attributes:
        virtual_machine (Union['BriefVirtualMachineRequest', Unset, int]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        size (Union[Unset, int]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedVirtualDiskRequestCustomFields]):
    """

    virtual_machine: Union["BriefVirtualMachineRequest", Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedVirtualDiskRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_virtual_machine_request import BriefVirtualMachineRequest

        virtual_machine: Union[Unset, dict[str, Any], int]
        if isinstance(self.virtual_machine, Unset):
            virtual_machine = UNSET
        elif isinstance(self.virtual_machine, BriefVirtualMachineRequest):
            virtual_machine = self.virtual_machine.to_dict()
        else:
            virtual_machine = self.virtual_machine

        name = self.name

        description = self.description

        size = self.size

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
        if virtual_machine is not UNSET:
            field_dict["virtual_machine"] = virtual_machine
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if size is not UNSET:
            field_dict["size"] = size
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        virtual_machine: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.virtual_machine, Unset):
            virtual_machine = UNSET
        elif isinstance(self.virtual_machine, int):
            virtual_machine = (None, str(self.virtual_machine).encode(), "text/plain")
        else:
            virtual_machine = (
                None,
                json.dumps(self.virtual_machine.to_dict()).encode(),
                "application/json",
            )

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

        size = (
            self.size
            if isinstance(self.size, Unset)
            else (None, str(self.size).encode(), "text/plain")
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
        if virtual_machine is not UNSET:
            field_dict["virtual_machine"] = virtual_machine
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if size is not UNSET:
            field_dict["size"] = size
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_virtual_machine_request import BriefVirtualMachineRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_virtual_disk_request_custom_fields import (
            PatchedVirtualDiskRequestCustomFields,
        )

        d = dict(src_dict)

        def _parse_virtual_machine(
            data: object,
        ) -> Union["BriefVirtualMachineRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                virtual_machine_type_1 = BriefVirtualMachineRequest.from_dict(data)

                return virtual_machine_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVirtualMachineRequest", Unset, int], data)

        virtual_machine = _parse_virtual_machine(d.pop("virtual_machine", UNSET))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        size = d.pop("size", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedVirtualDiskRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedVirtualDiskRequestCustomFields.from_dict(
                _custom_fields
            )

        patched_virtual_disk_request = cls(
            virtual_machine=virtual_machine,
            name=name,
            description=description,
            size=size,
            tags=tags,
            custom_fields=custom_fields,
        )

        patched_virtual_disk_request.additional_properties = d
        return patched_virtual_disk_request

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
