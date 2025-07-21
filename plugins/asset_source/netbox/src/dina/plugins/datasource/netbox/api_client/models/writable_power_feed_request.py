import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_power_feed_request_phase import WritablePowerFeedRequestPhase
from ..models.writable_power_feed_request_status import WritablePowerFeedRequestStatus
from ..models.writable_power_feed_request_supply import WritablePowerFeedRequestSupply
from ..models.writable_power_feed_request_type import WritablePowerFeedRequestType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_power_panel_request import BriefPowerPanelRequest
    from ..models.brief_rack_request import BriefRackRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.writable_power_feed_request_custom_fields import (
        WritablePowerFeedRequestCustomFields,
    )


T = TypeVar("T", bound="WritablePowerFeedRequest")


@_attrs_define
class WritablePowerFeedRequest:
    """Adds support for custom fields and tags.

    Attributes:
        power_panel (Union['BriefPowerPanelRequest', int]):
        name (str):
        rack (Union['BriefRackRequest', None, Unset, int]):
        status (Union[Unset, WritablePowerFeedRequestStatus]): * `offline` - Offline
            * `active` - Active
            * `planned` - Planned
            * `failed` - Failed
        type_ (Union[Unset, WritablePowerFeedRequestType]): * `primary` - Primary
            * `redundant` - Redundant
        supply (Union[Unset, WritablePowerFeedRequestSupply]): * `ac` - AC
            * `dc` - DC
        phase (Union[Unset, WritablePowerFeedRequestPhase]): * `single-phase` - Single phase
            * `three-phase` - Three-phase
        voltage (Union[Unset, int]):
        amperage (Union[Unset, int]):
        max_utilization (Union[Unset, int]): Maximum permissible draw (percentage)
        mark_connected (Union[Unset, bool]): Treat as if a cable is connected
        description (Union[Unset, str]):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WritablePowerFeedRequestCustomFields]):
    """

    power_panel: Union["BriefPowerPanelRequest", int]
    name: str
    rack: Union["BriefRackRequest", None, Unset, int] = UNSET
    status: Union[Unset, WritablePowerFeedRequestStatus] = UNSET
    type_: Union[Unset, WritablePowerFeedRequestType] = UNSET
    supply: Union[Unset, WritablePowerFeedRequestSupply] = UNSET
    phase: Union[Unset, WritablePowerFeedRequestPhase] = UNSET
    voltage: Union[Unset, int] = UNSET
    amperage: Union[Unset, int] = UNSET
    max_utilization: Union[Unset, int] = UNSET
    mark_connected: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WritablePowerFeedRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_power_panel_request import BriefPowerPanelRequest
        from ..models.brief_rack_request import BriefRackRequest
        from ..models.brief_tenant_request import BriefTenantRequest

        power_panel: Union[dict[str, Any], int]
        if isinstance(self.power_panel, BriefPowerPanelRequest):
            power_panel = self.power_panel.to_dict()
        else:
            power_panel = self.power_panel

        name = self.name

        rack: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.rack, Unset):
            rack = UNSET
        elif isinstance(self.rack, BriefRackRequest):
            rack = self.rack.to_dict()
        else:
            rack = self.rack

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        supply: Union[Unset, str] = UNSET
        if not isinstance(self.supply, Unset):
            supply = self.supply.value

        phase: Union[Unset, str] = UNSET
        if not isinstance(self.phase, Unset):
            phase = self.phase.value

        voltage = self.voltage

        amperage = self.amperage

        max_utilization = self.max_utilization

        mark_connected = self.mark_connected

        description = self.description

        tenant: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenantRequest):
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
                "power_panel": power_panel,
                "name": name,
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

    def to_multipart(self) -> dict[str, Any]:
        power_panel: tuple[None, bytes, str]

        if isinstance(self.power_panel, int):
            power_panel = (None, str(self.power_panel).encode(), "text/plain")
        else:
            power_panel = (
                None,
                json.dumps(self.power_panel.to_dict()).encode(),
                "application/json",
            )

        name = (None, str(self.name).encode(), "text/plain")

        rack: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.rack, Unset):
            rack = UNSET
        elif isinstance(self.rack, int):
            rack = (None, str(self.rack).encode(), "text/plain")
        elif isinstance(self.rack, None):
            rack = (None, str(self.rack).encode(), "text/plain")
        elif isinstance(self.rack, BriefRackRequest):
            rack = (None, json.dumps(self.rack.to_dict()).encode(), "application/json")
        else:
            rack = (None, str(self.rack).encode(), "text/plain")

        status: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

        type_: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = (None, str(self.type_.value).encode(), "text/plain")

        supply: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.supply, Unset):
            supply = (None, str(self.supply.value).encode(), "text/plain")

        phase: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.phase, Unset):
            phase = (None, str(self.phase.value).encode(), "text/plain")

        voltage = (
            self.voltage
            if isinstance(self.voltage, Unset)
            else (None, str(self.voltage).encode(), "text/plain")
        )

        amperage = (
            self.amperage
            if isinstance(self.amperage, Unset)
            else (None, str(self.amperage).encode(), "text/plain")
        )

        max_utilization = (
            self.max_utilization
            if isinstance(self.max_utilization, Unset)
            else (None, str(self.max_utilization).encode(), "text/plain")
        )

        mark_connected = (
            self.mark_connected
            if isinstance(self.mark_connected, Unset)
            else (None, str(self.mark_connected).encode(), "text/plain")
        )

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        tenant: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, int):
            tenant = (None, str(self.tenant).encode(), "text/plain")
        elif isinstance(self.tenant, None):
            tenant = (None, str(self.tenant).encode(), "text/plain")
        elif isinstance(self.tenant, BriefTenantRequest):
            tenant = (
                None,
                json.dumps(self.tenant.to_dict()).encode(),
                "application/json",
            )
        else:
            tenant = (None, str(self.tenant).encode(), "text/plain")

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

        field_dict.update(
            {
                "power_panel": power_panel,
                "name": name,
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
        from ..models.brief_power_panel_request import BriefPowerPanelRequest
        from ..models.brief_rack_request import BriefRackRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.writable_power_feed_request_custom_fields import (
            WritablePowerFeedRequestCustomFields,
        )

        d = dict(src_dict)

        def _parse_power_panel(data: object) -> Union["BriefPowerPanelRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                power_panel_type_1 = BriefPowerPanelRequest.from_dict(data)

                return power_panel_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefPowerPanelRequest", int], data)

        power_panel = _parse_power_panel(d.pop("power_panel"))

        name = d.pop("name")

        def _parse_rack(data: object) -> Union["BriefRackRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rack_type_1_type_1 = BriefRackRequest.from_dict(data)

                return rack_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefRackRequest", None, Unset, int], data)

        rack = _parse_rack(d.pop("rack", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, WritablePowerFeedRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WritablePowerFeedRequestStatus(_status)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, WritablePowerFeedRequestType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = WritablePowerFeedRequestType(_type_)

        _supply = d.pop("supply", UNSET)
        supply: Union[Unset, WritablePowerFeedRequestSupply]
        if isinstance(_supply, Unset):
            supply = UNSET
        else:
            supply = WritablePowerFeedRequestSupply(_supply)

        _phase = d.pop("phase", UNSET)
        phase: Union[Unset, WritablePowerFeedRequestPhase]
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = WritablePowerFeedRequestPhase(_phase)

        voltage = d.pop("voltage", UNSET)

        amperage = d.pop("amperage", UNSET)

        max_utilization = d.pop("max_utilization", UNSET)

        mark_connected = d.pop("mark_connected", UNSET)

        description = d.pop("description", UNSET)

        def _parse_tenant(
            data: object,
        ) -> Union["BriefTenantRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tenant_type_1_type_1 = BriefTenantRequest.from_dict(data)

                return tenant_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefTenantRequest", None, Unset, int], data)

        tenant = _parse_tenant(d.pop("tenant", UNSET))

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WritablePowerFeedRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WritablePowerFeedRequestCustomFields.from_dict(
                _custom_fields
            )

        writable_power_feed_request = cls(
            power_panel=power_panel,
            name=name,
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

        writable_power_feed_request.additional_properties = d
        return writable_power_feed_request

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
