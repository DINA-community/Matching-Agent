from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.power_feed_request_phase import PowerFeedRequestPhase
from ..models.power_feed_request_status import PowerFeedRequestStatus
from ..models.power_feed_request_supply import PowerFeedRequestSupply
from ..models.power_feed_request_type import PowerFeedRequestType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_power_panel_request import BriefPowerPanelRequest
    from ..models.brief_rack_request import BriefRackRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.power_feed_request_custom_fields import PowerFeedRequestCustomFields


T = TypeVar("T", bound="PowerFeedRequest")


@_attrs_define
class PowerFeedRequest:
    """Adds support for custom fields and tags.

    Attributes:
        power_panel (Union['BriefPowerPanelRequest', int]):
        name (str):
        rack (Union['BriefRackRequest', None, Unset, int]):
        status (Union[Unset, PowerFeedRequestStatus]): * `offline` - Offline
            * `active` - Active
            * `planned` - Planned
            * `failed` - Failed
        type_ (Union[Unset, PowerFeedRequestType]): * `primary` - Primary
            * `redundant` - Redundant
        supply (Union[Unset, PowerFeedRequestSupply]): * `ac` - AC
            * `dc` - DC
        phase (Union[Unset, PowerFeedRequestPhase]): * `single-phase` - Single phase
            * `three-phase` - Three-phase
        voltage (Union[Unset, int]):
        amperage (Union[Unset, int]):
        max_utilization (Union[Unset, int]): Maximum permissible draw (percentage)
        mark_connected (Union[Unset, bool]): Treat as if a cable is connected
        description (Union[Unset, str]):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PowerFeedRequestCustomFields]):
    """

    power_panel: Union["BriefPowerPanelRequest", int]
    name: str
    rack: Union["BriefRackRequest", None, Unset, int] = UNSET
    status: Union[Unset, PowerFeedRequestStatus] = UNSET
    type_: Union[Unset, PowerFeedRequestType] = UNSET
    supply: Union[Unset, PowerFeedRequestSupply] = UNSET
    phase: Union[Unset, PowerFeedRequestPhase] = UNSET
    voltage: Union[Unset, int] = UNSET
    amperage: Union[Unset, int] = UNSET
    max_utilization: Union[Unset, int] = UNSET
    mark_connected: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PowerFeedRequestCustomFields"] = UNSET
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

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_power_panel_request import BriefPowerPanelRequest
        from ..models.brief_rack_request import BriefRackRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.power_feed_request_custom_fields import PowerFeedRequestCustomFields

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
        status: Union[Unset, PowerFeedRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PowerFeedRequestStatus(_status)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, PowerFeedRequestType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PowerFeedRequestType(_type_)

        _supply = d.pop("supply", UNSET)
        supply: Union[Unset, PowerFeedRequestSupply]
        if isinstance(_supply, Unset):
            supply = UNSET
        else:
            supply = PowerFeedRequestSupply(_supply)

        _phase = d.pop("phase", UNSET)
        phase: Union[Unset, PowerFeedRequestPhase]
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = PowerFeedRequestPhase(_phase)

        voltage = d.pop("voltage", UNSET)

        amperage = d.pop("amperage", UNSET)

        max_utilization = d.pop("max_utilization", UNSET)

        mark_connected = d.pop("mark_connected", UNSET)

        description = d.pop("description", UNSET)

        def _parse_tenant(data: object) -> Union["BriefTenantRequest", None, Unset, int]:
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
        custom_fields: Union[Unset, PowerFeedRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PowerFeedRequestCustomFields.from_dict(_custom_fields)

        power_feed_request = cls(
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

        power_feed_request.additional_properties = d
        return power_feed_request

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
