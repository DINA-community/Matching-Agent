import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.circuit_termination_termination_side import (
    CircuitTerminationTerminationSide,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_cable import BriefCable
    from ..models.brief_circuit import BriefCircuit
    from ..models.circuit_termination_custom_fields import (
        CircuitTerminationCustomFields,
    )
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="CircuitTermination")


@_attrs_define
class CircuitTermination:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        circuit (BriefCircuit): Adds support for custom fields and tags.
        term_side (CircuitTerminationTerminationSide): * `A` - A
            * `Z` - Z
        termination (Any):
        cable (Union['BriefCable', None]):
        cable_end (str):
        link_peers (list[Any]):
        link_peers_type (Union[None, str]): Return the type of the peer link terminations, or None.
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        field_occupied (bool):
        termination_type (Union[None, Unset, str]):
        termination_id (Union[None, Unset, int]):
        port_speed (Union[None, Unset, int]): Physical circuit speed
        upstream_speed (Union[None, Unset, int]): Upstream speed, if different from port speed
        xconnect_id (Union[Unset, str]): ID of the local cross-connect
        pp_info (Union[Unset, str]): Patch panel ID and port number(s)
        description (Union[Unset, str]):
        mark_connected (Union[Unset, bool]): Treat as if a cable is connected
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, CircuitTerminationCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    circuit: "BriefCircuit"
    term_side: CircuitTerminationTerminationSide
    termination: Any
    cable: Union["BriefCable", None]
    cable_end: str
    link_peers: list[Any]
    link_peers_type: Union[None, str]
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    field_occupied: bool
    termination_type: Union[None, Unset, str] = UNSET
    termination_id: Union[None, Unset, int] = UNSET
    port_speed: Union[None, Unset, int] = UNSET
    upstream_speed: Union[None, Unset, int] = UNSET
    xconnect_id: Union[Unset, str] = UNSET
    pp_info: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    mark_connected: Union[Unset, bool] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "CircuitTerminationCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_cable import BriefCable

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        circuit = self.circuit.to_dict()

        term_side = self.term_side.value

        termination = self.termination

        cable: Union[None, dict[str, Any]]
        if isinstance(self.cable, BriefCable):
            cable = self.cable.to_dict()
        else:
            cable = self.cable

        cable_end = self.cable_end

        link_peers = self.link_peers

        link_peers_type: Union[None, str]
        link_peers_type = self.link_peers_type

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

        field_occupied = self.field_occupied

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
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "circuit": circuit,
                "term_side": term_side,
                "termination": termination,
                "cable": cable,
                "cable_end": cable_end,
                "link_peers": link_peers,
                "link_peers_type": link_peers_type,
                "created": created,
                "last_updated": last_updated,
                "_occupied": field_occupied,
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
        from ..models.brief_cable import BriefCable
        from ..models.brief_circuit import BriefCircuit
        from ..models.circuit_termination_custom_fields import (
            CircuitTerminationCustomFields,
        )
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        circuit = BriefCircuit.from_dict(d.pop("circuit"))

        term_side = CircuitTerminationTerminationSide(d.pop("term_side"))

        termination = d.pop("termination")

        def _parse_cable(data: object) -> Union["BriefCable", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cable_type_1 = BriefCable.from_dict(data)

                return cable_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefCable", None], data)

        cable = _parse_cable(d.pop("cable"))

        cable_end = d.pop("cable_end")

        link_peers = cast(list[Any], d.pop("link_peers"))

        def _parse_link_peers_type(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        link_peers_type = _parse_link_peers_type(d.pop("link_peers_type"))

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

        field_occupied = d.pop("_occupied")

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
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, CircuitTerminationCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CircuitTerminationCustomFields.from_dict(_custom_fields)

        circuit_termination = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            circuit=circuit,
            term_side=term_side,
            termination=termination,
            cable=cable,
            cable_end=cable_end,
            link_peers=link_peers,
            link_peers_type=link_peers_type,
            created=created,
            last_updated=last_updated,
            field_occupied=field_occupied,
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

        circuit_termination.additional_properties = d
        return circuit_termination

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
