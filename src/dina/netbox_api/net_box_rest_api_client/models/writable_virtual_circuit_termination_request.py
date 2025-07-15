import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_virtual_circuit_termination_request_role import WritableVirtualCircuitTerminationRequestRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_interface_request import BriefInterfaceRequest
    from ..models.brief_virtual_circuit_request import BriefVirtualCircuitRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.writable_virtual_circuit_termination_request_custom_fields import (
        WritableVirtualCircuitTerminationRequestCustomFields,
    )


T = TypeVar("T", bound="WritableVirtualCircuitTerminationRequest")


@_attrs_define
class WritableVirtualCircuitTerminationRequest:
    """Adds support for custom fields and tags.

    Attributes:
        virtual_circuit (Union['BriefVirtualCircuitRequest', int]):
        interface (Union['BriefInterfaceRequest', int]):
        role (Union[Unset, WritableVirtualCircuitTerminationRequestRole]): * `peer` - Peer
            * `hub` - Hub
            * `spoke` - Spoke
        description (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WritableVirtualCircuitTerminationRequestCustomFields]):
    """

    virtual_circuit: Union["BriefVirtualCircuitRequest", int]
    interface: Union["BriefInterfaceRequest", int]
    role: Union[Unset, WritableVirtualCircuitTerminationRequestRole] = UNSET
    description: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WritableVirtualCircuitTerminationRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_interface_request import BriefInterfaceRequest
        from ..models.brief_virtual_circuit_request import BriefVirtualCircuitRequest

        virtual_circuit: Union[dict[str, Any], int]
        if isinstance(self.virtual_circuit, BriefVirtualCircuitRequest):
            virtual_circuit = self.virtual_circuit.to_dict()
        else:
            virtual_circuit = self.virtual_circuit

        interface: Union[dict[str, Any], int]
        if isinstance(self.interface, BriefInterfaceRequest):
            interface = self.interface.to_dict()
        else:
            interface = self.interface

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        description = self.description

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
                "virtual_circuit": virtual_circuit,
                "interface": interface,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        virtual_circuit: tuple[None, bytes, str]

        if isinstance(self.virtual_circuit, int):
            virtual_circuit = (None, str(self.virtual_circuit).encode(), "text/plain")
        else:
            virtual_circuit = (None, json.dumps(self.virtual_circuit.to_dict()).encode(), "application/json")

        interface: tuple[None, bytes, str]

        if isinstance(self.interface, int):
            interface = (None, str(self.interface).encode(), "text/plain")
        else:
            interface = (None, json.dumps(self.interface.to_dict()).encode(), "application/json")

        role: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.role, Unset):
            role = (None, str(self.role.value).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
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

        field_dict.update(
            {
                "virtual_circuit": virtual_circuit,
                "interface": interface,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_interface_request import BriefInterfaceRequest
        from ..models.brief_virtual_circuit_request import BriefVirtualCircuitRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.writable_virtual_circuit_termination_request_custom_fields import (
            WritableVirtualCircuitTerminationRequestCustomFields,
        )

        d = dict(src_dict)

        def _parse_virtual_circuit(data: object) -> Union["BriefVirtualCircuitRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                virtual_circuit_type_1 = BriefVirtualCircuitRequest.from_dict(data)

                return virtual_circuit_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVirtualCircuitRequest", int], data)

        virtual_circuit = _parse_virtual_circuit(d.pop("virtual_circuit"))

        def _parse_interface(data: object) -> Union["BriefInterfaceRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                interface_type_1 = BriefInterfaceRequest.from_dict(data)

                return interface_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefInterfaceRequest", int], data)

        interface = _parse_interface(d.pop("interface"))

        _role = d.pop("role", UNSET)
        role: Union[Unset, WritableVirtualCircuitTerminationRequestRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = WritableVirtualCircuitTerminationRequestRole(_role)

        description = d.pop("description", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WritableVirtualCircuitTerminationRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WritableVirtualCircuitTerminationRequestCustomFields.from_dict(_custom_fields)

        writable_virtual_circuit_termination_request = cls(
            virtual_circuit=virtual_circuit,
            interface=interface,
            role=role,
            description=description,
            tags=tags,
            custom_fields=custom_fields,
        )

        writable_virtual_circuit_termination_request.additional_properties = d
        return writable_virtual_circuit_termination_request

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
