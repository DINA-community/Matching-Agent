import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.circuit_termination_request_termination_side import CircuitTerminationRequestTerminationSide
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_circuit_request import BriefCircuitRequest
    from ..models.circuit_termination_request_custom_fields import CircuitTerminationRequestCustomFields
    from ..models.nested_tag_request import NestedTagRequest


T = TypeVar("T", bound="CircuitTerminationRequest")


@_attrs_define
class CircuitTerminationRequest:
    """Adds support for custom fields and tags.

    Attributes:
        circuit (Union['BriefCircuitRequest', int]):
        term_side (CircuitTerminationRequestTerminationSide): * `A` - A
            * `Z` - Z
        termination_type (Union[None, Unset, str]):
        termination_id (Union[None, Unset, int]):
        port_speed (Union[None, Unset, int]): Physical circuit speed
        upstream_speed (Union[None, Unset, int]): Upstream speed, if different from port speed
        xconnect_id (Union[Unset, str]): ID of the local cross-connect
        pp_info (Union[Unset, str]): Patch panel ID and port number(s)
        description (Union[Unset, str]):
        mark_connected (Union[Unset, bool]): Treat as if a cable is connected
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, CircuitTerminationRequestCustomFields]):
    """

    circuit: Union["BriefCircuitRequest", int]
    term_side: CircuitTerminationRequestTerminationSide
    termination_type: Union[None, Unset, str] = UNSET
    termination_id: Union[None, Unset, int] = UNSET
    port_speed: Union[None, Unset, int] = UNSET
    upstream_speed: Union[None, Unset, int] = UNSET
    xconnect_id: Union[Unset, str] = UNSET
    pp_info: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    mark_connected: Union[Unset, bool] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "CircuitTerminationRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_circuit_request import BriefCircuitRequest

        circuit: Union[dict[str, Any], int]
        if isinstance(self.circuit, BriefCircuitRequest):
            circuit = self.circuit.to_dict()
        else:
            circuit = self.circuit

        term_side = self.term_side.value

        termination_type: Union[None, Unset, str]
        if isinstance(self.termination_type, Unset):
            termination_type = UNSET
        else:
            termination_type = self.termination_type

        termination_id: Union[None, Unset, int]
        if isinstance(self.termination_id, Unset):
            termination_id = UNSET
        else:
            termination_id = self.termination_id

        port_speed: Union[None, Unset, int]
        if isinstance(self.port_speed, Unset):
            port_speed = UNSET
        else:
            port_speed = self.port_speed

        upstream_speed: Union[None, Unset, int]
        if isinstance(self.upstream_speed, Unset):
            upstream_speed = UNSET
        else:
            upstream_speed = self.upstream_speed

        xconnect_id = self.xconnect_id

        pp_info = self.pp_info

        description = self.description

        mark_connected = self.mark_connected

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
                "circuit": circuit,
                "term_side": term_side,
            }
        )
        if termination_type is not UNSET:
            field_dict["termination_type"] = termination_type
        if termination_id is not UNSET:
            field_dict["termination_id"] = termination_id
        if port_speed is not UNSET:
            field_dict["port_speed"] = port_speed
        if upstream_speed is not UNSET:
            field_dict["upstream_speed"] = upstream_speed
        if xconnect_id is not UNSET:
            field_dict["xconnect_id"] = xconnect_id
        if pp_info is not UNSET:
            field_dict["pp_info"] = pp_info
        if description is not UNSET:
            field_dict["description"] = description
        if mark_connected is not UNSET:
            field_dict["mark_connected"] = mark_connected
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        circuit: tuple[None, bytes, str]

        if isinstance(self.circuit, int):
            circuit = (None, str(self.circuit).encode(), "text/plain")
        else:
            circuit = (None, json.dumps(self.circuit.to_dict()).encode(), "application/json")

        term_side = (None, str(self.term_side.value).encode(), "text/plain")

        termination_type: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.termination_type, Unset):
            termination_type = UNSET
        elif isinstance(self.termination_type, str):
            termination_type = (None, str(self.termination_type).encode(), "text/plain")
        else:
            termination_type = (None, str(self.termination_type).encode(), "text/plain")

        termination_id: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.termination_id, Unset):
            termination_id = UNSET
        elif isinstance(self.termination_id, int):
            termination_id = (None, str(self.termination_id).encode(), "text/plain")
        else:
            termination_id = (None, str(self.termination_id).encode(), "text/plain")

        port_speed: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.port_speed, Unset):
            port_speed = UNSET
        elif isinstance(self.port_speed, int):
            port_speed = (None, str(self.port_speed).encode(), "text/plain")
        else:
            port_speed = (None, str(self.port_speed).encode(), "text/plain")

        upstream_speed: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.upstream_speed, Unset):
            upstream_speed = UNSET
        elif isinstance(self.upstream_speed, int):
            upstream_speed = (None, str(self.upstream_speed).encode(), "text/plain")
        else:
            upstream_speed = (None, str(self.upstream_speed).encode(), "text/plain")

        xconnect_id = (
            self.xconnect_id
            if isinstance(self.xconnect_id, Unset)
            else (None, str(self.xconnect_id).encode(), "text/plain")
        )

        pp_info = self.pp_info if isinstance(self.pp_info, Unset) else (None, str(self.pp_info).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        mark_connected = (
            self.mark_connected
            if isinstance(self.mark_connected, Unset)
            else (None, str(self.mark_connected).encode(), "text/plain")
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
                "circuit": circuit,
                "term_side": term_side,
            }
        )
        if termination_type is not UNSET:
            field_dict["termination_type"] = termination_type
        if termination_id is not UNSET:
            field_dict["termination_id"] = termination_id
        if port_speed is not UNSET:
            field_dict["port_speed"] = port_speed
        if upstream_speed is not UNSET:
            field_dict["upstream_speed"] = upstream_speed
        if xconnect_id is not UNSET:
            field_dict["xconnect_id"] = xconnect_id
        if pp_info is not UNSET:
            field_dict["pp_info"] = pp_info
        if description is not UNSET:
            field_dict["description"] = description
        if mark_connected is not UNSET:
            field_dict["mark_connected"] = mark_connected
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_circuit_request import BriefCircuitRequest
        from ..models.circuit_termination_request_custom_fields import CircuitTerminationRequestCustomFields
        from ..models.nested_tag_request import NestedTagRequest

        d = dict(src_dict)

        def _parse_circuit(data: object) -> Union["BriefCircuitRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                circuit_type_1 = BriefCircuitRequest.from_dict(data)

                return circuit_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefCircuitRequest", int], data)

        circuit = _parse_circuit(d.pop("circuit"))

        term_side = CircuitTerminationRequestTerminationSide(d.pop("term_side"))

        def _parse_termination_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        termination_type = _parse_termination_type(d.pop("termination_type", UNSET))

        def _parse_termination_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        termination_id = _parse_termination_id(d.pop("termination_id", UNSET))

        def _parse_port_speed(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        port_speed = _parse_port_speed(d.pop("port_speed", UNSET))

        def _parse_upstream_speed(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        upstream_speed = _parse_upstream_speed(d.pop("upstream_speed", UNSET))

        xconnect_id = d.pop("xconnect_id", UNSET)

        pp_info = d.pop("pp_info", UNSET)

        description = d.pop("description", UNSET)

        mark_connected = d.pop("mark_connected", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, CircuitTerminationRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CircuitTerminationRequestCustomFields.from_dict(_custom_fields)

        circuit_termination_request = cls(
            circuit=circuit,
            term_side=term_side,
            termination_type=termination_type,
            termination_id=termination_id,
            port_speed=port_speed,
            upstream_speed=upstream_speed,
            xconnect_id=xconnect_id,
            pp_info=pp_info,
            description=description,
            mark_connected=mark_connected,
            tags=tags,
            custom_fields=custom_fields,
        )

        circuit_termination_request.additional_properties = d
        return circuit_termination_request

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
