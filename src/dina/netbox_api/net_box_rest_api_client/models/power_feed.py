import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_cable import BriefCable
    from ..models.brief_power_panel import BriefPowerPanel
    from ..models.brief_rack import BriefRack
    from ..models.brief_tenant import BriefTenant
    from ..models.nested_tag import NestedTag
    from ..models.power_feed_custom_fields import PowerFeedCustomFields
    from ..models.power_feed_phase import PowerFeedPhase
    from ..models.power_feed_status import PowerFeedStatus
    from ..models.power_feed_supply import PowerFeedSupply
    from ..models.power_feed_type import PowerFeedType


T = TypeVar("T", bound="PowerFeed")


@_attrs_define
class PowerFeed:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        power_panel (BriefPowerPanel): Adds support for custom fields and tags.
        name (str):
        cable (Union['BriefCable', None]):
        cable_end (str):
        link_peers (list[Any]):
        link_peers_type (Union[None, str]): Return the type of the peer link terminations, or None.
        connected_endpoints (Union[None, list[Any]]):
        connected_endpoints_type (Union[None, str]):
        connected_endpoints_reachable (bool):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        field_occupied (bool):
        rack (Union['BriefRack', None, Unset]):
        status (Union[Unset, PowerFeedStatus]):
        type_ (Union[Unset, PowerFeedType]):
        supply (Union[Unset, PowerFeedSupply]):
        phase (Union[Unset, PowerFeedPhase]):
        voltage (Union[Unset, int]):
        amperage (Union[Unset, int]):
        max_utilization (Union[Unset, int]): Maximum permissible draw (percentage)
        mark_connected (Union[Unset, bool]): Treat as if a cable is connected
        description (Union[Unset, str]):
        tenant (Union['BriefTenant', None, Unset]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, PowerFeedCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    power_panel: "BriefPowerPanel"
    name: str
    cable: Union["BriefCable", None]
    cable_end: str
    link_peers: list[Any]
    link_peers_type: Union[None, str]
    connected_endpoints: Union[None, list[Any]]
    connected_endpoints_type: Union[None, str]
    connected_endpoints_reachable: bool
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    field_occupied: bool
    rack: Union["BriefRack", None, Unset] = UNSET
    status: Union[Unset, "PowerFeedStatus"] = UNSET
    type_: Union[Unset, "PowerFeedType"] = UNSET
    supply: Union[Unset, "PowerFeedSupply"] = UNSET
    phase: Union[Unset, "PowerFeedPhase"] = UNSET
    voltage: Union[Unset, int] = UNSET
    amperage: Union[Unset, int] = UNSET
    max_utilization: Union[Unset, int] = UNSET
    mark_connected: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    tenant: Union["BriefTenant", None, Unset] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "PowerFeedCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_cable import BriefCable
        from ..models.brief_rack import BriefRack
        from ..models.brief_tenant import BriefTenant

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        power_panel = self.power_panel.to_dict()

        name = self.name

        cable: Union[None, dict[str, Any]]
        if isinstance(self.cable, BriefCable):
            cable = self.cable.to_dict()
        else:
            cable = self.cable

        cable_end = self.cable_end

        link_peers = self.link_peers

        link_peers_type: Union[None, str]
        link_peers_type = self.link_peers_type

        connected_endpoints: Union[None, list[Any]]
        if isinstance(self.connected_endpoints, list):
            connected_endpoints = self.connected_endpoints

        else:
            connected_endpoints = self.connected_endpoints

        connected_endpoints_type: Union[None, str]
        connected_endpoints_type = self.connected_endpoints_type

        connected_endpoints_reachable = self.connected_endpoints_reachable

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

        rack: Union[None, Unset, dict[str, Any]]
        if isinstance(self.rack, Unset):
            rack = UNSET
        elif isinstance(self.rack, BriefRack):
            rack = self.rack.to_dict()
        else:
            rack = self.rack

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        type_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        supply: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.supply, Unset):
            supply = self.supply.to_dict()

        phase: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.phase, Unset):
            phase = self.phase.to_dict()

        voltage = self.voltage

        amperage = self.amperage

        max_utilization = self.max_utilization

        mark_connected = self.mark_connected

        description = self.description

        tenant: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenant):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

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
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "power_panel": power_panel,
                "name": name,
                "cable": cable,
                "cable_end": cable_end,
                "link_peers": link_peers,
                "link_peers_type": link_peers_type,
                "connected_endpoints": connected_endpoints,
                "connected_endpoints_type": connected_endpoints_type,
                "connected_endpoints_reachable": connected_endpoints_reachable,
                "created": created,
                "last_updated": last_updated,
                "_occupied": field_occupied,
            }
        )
        if rack is not UNSET:
            field_dict["rack"] = rack
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_
        if supply is not UNSET:
            field_dict["supply"] = supply
        if phase is not UNSET:
            field_dict["phase"] = phase
        if voltage is not UNSET:
            field_dict["voltage"] = voltage
        if amperage is not UNSET:
            field_dict["amperage"] = amperage
        if max_utilization is not UNSET:
            field_dict["max_utilization"] = max_utilization
        if mark_connected is not UNSET:
            field_dict["mark_connected"] = mark_connected
        if description is not UNSET:
            field_dict["description"] = description
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_cable import BriefCable
        from ..models.brief_power_panel import BriefPowerPanel
        from ..models.brief_rack import BriefRack
        from ..models.brief_tenant import BriefTenant
        from ..models.nested_tag import NestedTag
        from ..models.power_feed_custom_fields import PowerFeedCustomFields
        from ..models.power_feed_phase import PowerFeedPhase
        from ..models.power_feed_status import PowerFeedStatus
        from ..models.power_feed_supply import PowerFeedSupply
        from ..models.power_feed_type import PowerFeedType

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        power_panel = BriefPowerPanel.from_dict(d.pop("power_panel"))

        name = d.pop("name")

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

        def _parse_connected_endpoints(data: object) -> Union[None, list[Any]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                connected_endpoints_type_0 = cast(list[Any], data)

                return connected_endpoints_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[Any]], data)

        connected_endpoints = _parse_connected_endpoints(d.pop("connected_endpoints"))

        def _parse_connected_endpoints_type(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        connected_endpoints_type = _parse_connected_endpoints_type(d.pop("connected_endpoints_type"))

        connected_endpoints_reachable = d.pop("connected_endpoints_reachable")

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

        def _parse_rack(data: object) -> Union["BriefRack", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rack_type_1 = BriefRack.from_dict(data)

                return rack_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefRack", None, Unset], data)

        rack = _parse_rack(d.pop("rack", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, PowerFeedStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PowerFeedStatus.from_dict(_status)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, PowerFeedType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PowerFeedType.from_dict(_type_)

        _supply = d.pop("supply", UNSET)
        supply: Union[Unset, PowerFeedSupply]
        if isinstance(_supply, Unset):
            supply = UNSET
        else:
            supply = PowerFeedSupply.from_dict(_supply)

        _phase = d.pop("phase", UNSET)
        phase: Union[Unset, PowerFeedPhase]
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = PowerFeedPhase.from_dict(_phase)

        voltage = d.pop("voltage", UNSET)

        amperage = d.pop("amperage", UNSET)

        max_utilization = d.pop("max_utilization", UNSET)

        mark_connected = d.pop("mark_connected", UNSET)

        description = d.pop("description", UNSET)

        def _parse_tenant(data: object) -> Union["BriefTenant", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tenant_type_1 = BriefTenant.from_dict(data)

                return tenant_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefTenant", None, Unset], data)

        tenant = _parse_tenant(d.pop("tenant", UNSET))

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PowerFeedCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PowerFeedCustomFields.from_dict(_custom_fields)

        power_feed = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            power_panel=power_panel,
            name=name,
            cable=cable,
            cable_end=cable_end,
            link_peers=link_peers,
            link_peers_type=link_peers_type,
            connected_endpoints=connected_endpoints,
            connected_endpoints_type=connected_endpoints_type,
            connected_endpoints_reachable=connected_endpoints_reachable,
            created=created,
            last_updated=last_updated,
            field_occupied=field_occupied,
            rack=rack,
            status=status,
            type_=type_,
            supply=supply,
            phase=phase,
            voltage=voltage,
            amperage=amperage,
            max_utilization=max_utilization,
            mark_connected=mark_connected,
            description=description,
            tenant=tenant,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        power_feed.additional_properties = d
        return power_feed

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
