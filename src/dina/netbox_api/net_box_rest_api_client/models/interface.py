import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_cable import BriefCable
    from ..models.brief_device import BriefDevice
    from ..models.brief_l2vpn_termination import BriefL2VPNTermination
    from ..models.brief_mac_address import BriefMACAddress
    from ..models.brief_module import BriefModule
    from ..models.brief_vlan import BriefVLAN
    from ..models.brief_vlan_translation_policy import BriefVLANTranslationPolicy
    from ..models.brief_vrf import BriefVRF
    from ..models.interface_custom_fields import InterfaceCustomFields
    from ..models.interface_duplex_type_0 import InterfaceDuplexType0
    from ..models.interface_mode import InterfaceMode
    from ..models.interface_poe_mode import InterfacePoeMode
    from ..models.interface_poe_type import InterfacePoeType
    from ..models.interface_rf_channel import InterfaceRfChannel
    from ..models.interface_rf_role import InterfaceRfRole
    from ..models.interface_type import InterfaceType
    from ..models.nested_interface import NestedInterface
    from ..models.nested_tag import NestedTag
    from ..models.nested_wireless_link import NestedWirelessLink
    from ..models.virtual_device_context import VirtualDeviceContext
    from ..models.vlan import VLAN
    from ..models.wireless_lan import WirelessLAN


T = TypeVar("T", bound="Interface")


@_attrs_define
class Interface:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        device (BriefDevice): Adds support for custom fields and tags.
        name (str):
        type_ (InterfaceType):
        mac_address (Union[None, str]):
        mac_addresses (Union[None, list['BriefMACAddress']]):
        cable (Union['BriefCable', None]):
        cable_end (str):
        wireless_link (Union['NestedWirelessLink', None]):
        link_peers (list[Any]):
        link_peers_type (Union[None, str]): Return the type of the peer link terminations, or None.
        l2vpn_termination (Union['BriefL2VPNTermination', None]):
        connected_endpoints (Union[None, list[Any]]):
        connected_endpoints_type (Union[None, str]):
        connected_endpoints_reachable (bool):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        count_ipaddresses (int):
        count_fhrp_groups (int):
        field_occupied (bool):
        vdcs (Union[Unset, list['VirtualDeviceContext']]):
        module (Union['BriefModule', None, Unset]):
        label (Union[Unset, str]): Physical label
        enabled (Union[Unset, bool]):
        parent (Union['NestedInterface', None, Unset]):
        bridge (Union['NestedInterface', None, Unset]):
        lag (Union['NestedInterface', None, Unset]):
        mtu (Union[None, Unset, int]):
        primary_mac_address (Union['BriefMACAddress', None, Unset]):
        speed (Union[None, Unset, int]):
        duplex (Union['InterfaceDuplexType0', None, Unset]):
        wwn (Union[None, Unset, str]):
        mgmt_only (Union[Unset, bool]): This interface is used only for out-of-band management
        description (Union[Unset, str]):
        mode (Union[Unset, InterfaceMode]):
        rf_role (Union[Unset, InterfaceRfRole]):
        rf_channel (Union[Unset, InterfaceRfChannel]):
        poe_mode (Union[Unset, InterfacePoeMode]):
        poe_type (Union[Unset, InterfacePoeType]):
        rf_channel_frequency (Union[None, Unset, float]): Populated by selected channel (if set)
        rf_channel_width (Union[None, Unset, float]): Populated by selected channel (if set)
        tx_power (Union[None, Unset, int]):
        untagged_vlan (Union['BriefVLAN', None, Unset]):
        tagged_vlans (Union[Unset, list['VLAN']]):
        qinq_svlan (Union['BriefVLAN', None, Unset]):
        vlan_translation_policy (Union['BriefVLANTranslationPolicy', None, Unset]):
        mark_connected (Union[Unset, bool]): Treat as if a cable is connected
        wireless_lans (Union[Unset, list['WirelessLAN']]):
        vrf (Union['BriefVRF', None, Unset]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, InterfaceCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    device: "BriefDevice"
    name: str
    type_: "InterfaceType"
    mac_address: Union[None, str]
    mac_addresses: Union[None, list["BriefMACAddress"]]
    cable: Union["BriefCable", None]
    cable_end: str
    wireless_link: Union["NestedWirelessLink", None]
    link_peers: list[Any]
    link_peers_type: Union[None, str]
    l2vpn_termination: Union["BriefL2VPNTermination", None]
    connected_endpoints: Union[None, list[Any]]
    connected_endpoints_type: Union[None, str]
    connected_endpoints_reachable: bool
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    count_ipaddresses: int
    count_fhrp_groups: int
    field_occupied: bool
    vdcs: Union[Unset, list["VirtualDeviceContext"]] = UNSET
    module: Union["BriefModule", None, Unset] = UNSET
    label: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    parent: Union["NestedInterface", None, Unset] = UNSET
    bridge: Union["NestedInterface", None, Unset] = UNSET
    lag: Union["NestedInterface", None, Unset] = UNSET
    mtu: Union[None, Unset, int] = UNSET
    primary_mac_address: Union["BriefMACAddress", None, Unset] = UNSET
    speed: Union[None, Unset, int] = UNSET
    duplex: Union["InterfaceDuplexType0", None, Unset] = UNSET
    wwn: Union[None, Unset, str] = UNSET
    mgmt_only: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    mode: Union[Unset, "InterfaceMode"] = UNSET
    rf_role: Union[Unset, "InterfaceRfRole"] = UNSET
    rf_channel: Union[Unset, "InterfaceRfChannel"] = UNSET
    poe_mode: Union[Unset, "InterfacePoeMode"] = UNSET
    poe_type: Union[Unset, "InterfacePoeType"] = UNSET
    rf_channel_frequency: Union[None, Unset, float] = UNSET
    rf_channel_width: Union[None, Unset, float] = UNSET
    tx_power: Union[None, Unset, int] = UNSET
    untagged_vlan: Union["BriefVLAN", None, Unset] = UNSET
    tagged_vlans: Union[Unset, list["VLAN"]] = UNSET
    qinq_svlan: Union["BriefVLAN", None, Unset] = UNSET
    vlan_translation_policy: Union["BriefVLANTranslationPolicy", None, Unset] = UNSET
    mark_connected: Union[Unset, bool] = UNSET
    wireless_lans: Union[Unset, list["WirelessLAN"]] = UNSET
    vrf: Union["BriefVRF", None, Unset] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "InterfaceCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_cable import BriefCable
        from ..models.brief_l2vpn_termination import BriefL2VPNTermination
        from ..models.brief_mac_address import BriefMACAddress
        from ..models.brief_module import BriefModule
        from ..models.brief_vlan import BriefVLAN
        from ..models.brief_vlan_translation_policy import BriefVLANTranslationPolicy
        from ..models.brief_vrf import BriefVRF
        from ..models.interface_duplex_type_0 import InterfaceDuplexType0
        from ..models.nested_interface import NestedInterface
        from ..models.nested_wireless_link import NestedWirelessLink

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        device = self.device.to_dict()

        name = self.name

        type_ = self.type_.to_dict()

        mac_address: Union[None, str]
        mac_address = self.mac_address

        mac_addresses: Union[None, list[dict[str, Any]]]
        if isinstance(self.mac_addresses, list):
            mac_addresses = []
            for mac_addresses_type_0_item_data in self.mac_addresses:
                mac_addresses_type_0_item = mac_addresses_type_0_item_data.to_dict()
                mac_addresses.append(mac_addresses_type_0_item)

        else:
            mac_addresses = self.mac_addresses

        cable: Union[None, dict[str, Any]]
        if isinstance(self.cable, BriefCable):
            cable = self.cable.to_dict()
        else:
            cable = self.cable

        cable_end = self.cable_end

        wireless_link: Union[None, dict[str, Any]]
        if isinstance(self.wireless_link, NestedWirelessLink):
            wireless_link = self.wireless_link.to_dict()
        else:
            wireless_link = self.wireless_link

        link_peers = self.link_peers

        link_peers_type: Union[None, str]
        link_peers_type = self.link_peers_type

        l2vpn_termination: Union[None, dict[str, Any]]
        if isinstance(self.l2vpn_termination, BriefL2VPNTermination):
            l2vpn_termination = self.l2vpn_termination.to_dict()
        else:
            l2vpn_termination = self.l2vpn_termination

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

        count_ipaddresses = self.count_ipaddresses

        count_fhrp_groups = self.count_fhrp_groups

        field_occupied = self.field_occupied

        vdcs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.vdcs, Unset):
            vdcs = []
            for vdcs_item_data in self.vdcs:
                vdcs_item = vdcs_item_data.to_dict()
                vdcs.append(vdcs_item)

        module: Union[None, Unset, dict[str, Any]]
        if isinstance(self.module, Unset):
            module = UNSET
        elif isinstance(self.module, BriefModule):
            module = self.module.to_dict()
        else:
            module = self.module

        label = self.label

        enabled = self.enabled

        parent: Union[None, Unset, dict[str, Any]]
        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, NestedInterface):
            parent = self.parent.to_dict()
        else:
            parent = self.parent

        bridge: Union[None, Unset, dict[str, Any]]
        if isinstance(self.bridge, Unset):
            bridge = UNSET
        elif isinstance(self.bridge, NestedInterface):
            bridge = self.bridge.to_dict()
        else:
            bridge = self.bridge

        lag: Union[None, Unset, dict[str, Any]]
        if isinstance(self.lag, Unset):
            lag = UNSET
        elif isinstance(self.lag, NestedInterface):
            lag = self.lag.to_dict()
        else:
            lag = self.lag

        mtu: Union[None, Unset, int]
        if isinstance(self.mtu, Unset):
            mtu = UNSET
        else:
            mtu = self.mtu

        primary_mac_address: Union[None, Unset, dict[str, Any]]
        if isinstance(self.primary_mac_address, Unset):
            primary_mac_address = UNSET
        elif isinstance(self.primary_mac_address, BriefMACAddress):
            primary_mac_address = self.primary_mac_address.to_dict()
        else:
            primary_mac_address = self.primary_mac_address

        speed: Union[None, Unset, int]
        if isinstance(self.speed, Unset):
            speed = UNSET
        else:
            speed = self.speed

        duplex: Union[None, Unset, dict[str, Any]]
        if isinstance(self.duplex, Unset):
            duplex = UNSET
        elif isinstance(self.duplex, InterfaceDuplexType0):
            duplex = self.duplex.to_dict()
        else:
            duplex = self.duplex

        wwn: Union[None, Unset, str]
        if isinstance(self.wwn, Unset):
            wwn = UNSET
        else:
            wwn = self.wwn

        mgmt_only = self.mgmt_only

        description = self.description

        mode: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.to_dict()

        rf_role: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rf_role, Unset):
            rf_role = self.rf_role.to_dict()

        rf_channel: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rf_channel, Unset):
            rf_channel = self.rf_channel.to_dict()

        poe_mode: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.poe_mode, Unset):
            poe_mode = self.poe_mode.to_dict()

        poe_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.poe_type, Unset):
            poe_type = self.poe_type.to_dict()

        rf_channel_frequency: Union[None, Unset, float]
        if isinstance(self.rf_channel_frequency, Unset):
            rf_channel_frequency = UNSET
        else:
            rf_channel_frequency = self.rf_channel_frequency

        rf_channel_width: Union[None, Unset, float]
        if isinstance(self.rf_channel_width, Unset):
            rf_channel_width = UNSET
        else:
            rf_channel_width = self.rf_channel_width

        tx_power: Union[None, Unset, int]
        if isinstance(self.tx_power, Unset):
            tx_power = UNSET
        else:
            tx_power = self.tx_power

        untagged_vlan: Union[None, Unset, dict[str, Any]]
        if isinstance(self.untagged_vlan, Unset):
            untagged_vlan = UNSET
        elif isinstance(self.untagged_vlan, BriefVLAN):
            untagged_vlan = self.untagged_vlan.to_dict()
        else:
            untagged_vlan = self.untagged_vlan

        tagged_vlans: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tagged_vlans, Unset):
            tagged_vlans = []
            for tagged_vlans_item_data in self.tagged_vlans:
                tagged_vlans_item = tagged_vlans_item_data.to_dict()
                tagged_vlans.append(tagged_vlans_item)

        qinq_svlan: Union[None, Unset, dict[str, Any]]
        if isinstance(self.qinq_svlan, Unset):
            qinq_svlan = UNSET
        elif isinstance(self.qinq_svlan, BriefVLAN):
            qinq_svlan = self.qinq_svlan.to_dict()
        else:
            qinq_svlan = self.qinq_svlan

        vlan_translation_policy: Union[None, Unset, dict[str, Any]]
        if isinstance(self.vlan_translation_policy, Unset):
            vlan_translation_policy = UNSET
        elif isinstance(self.vlan_translation_policy, BriefVLANTranslationPolicy):
            vlan_translation_policy = self.vlan_translation_policy.to_dict()
        else:
            vlan_translation_policy = self.vlan_translation_policy

        mark_connected = self.mark_connected

        wireless_lans: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.wireless_lans, Unset):
            wireless_lans = []
            for wireless_lans_item_data in self.wireless_lans:
                wireless_lans_item = wireless_lans_item_data.to_dict()
                wireless_lans.append(wireless_lans_item)

        vrf: Union[None, Unset, dict[str, Any]]
        if isinstance(self.vrf, Unset):
            vrf = UNSET
        elif isinstance(self.vrf, BriefVRF):
            vrf = self.vrf.to_dict()
        else:
            vrf = self.vrf

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
                "device": device,
                "name": name,
                "type": type_,
                "mac_address": mac_address,
                "mac_addresses": mac_addresses,
                "cable": cable,
                "cable_end": cable_end,
                "wireless_link": wireless_link,
                "link_peers": link_peers,
                "link_peers_type": link_peers_type,
                "l2vpn_termination": l2vpn_termination,
                "connected_endpoints": connected_endpoints,
                "connected_endpoints_type": connected_endpoints_type,
                "connected_endpoints_reachable": connected_endpoints_reachable,
                "created": created,
                "last_updated": last_updated,
                "count_ipaddresses": count_ipaddresses,
                "count_fhrp_groups": count_fhrp_groups,
                "_occupied": field_occupied,
            }
        )
        if vdcs is not UNSET:
            field_dict["vdcs"] = vdcs
        if module is not UNSET:
            field_dict["module"] = module
        if label is not UNSET:
            field_dict["label"] = label
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if parent is not UNSET:
            field_dict["parent"] = parent
        if bridge is not UNSET:
            field_dict["bridge"] = bridge
        if lag is not UNSET:
            field_dict["lag"] = lag
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if primary_mac_address is not UNSET:
            field_dict["primary_mac_address"] = primary_mac_address
        if speed is not UNSET:
            field_dict["speed"] = speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if wwn is not UNSET:
            field_dict["wwn"] = wwn
        if mgmt_only is not UNSET:
            field_dict["mgmt_only"] = mgmt_only
        if description is not UNSET:
            field_dict["description"] = description
        if mode is not UNSET:
            field_dict["mode"] = mode
        if rf_role is not UNSET:
            field_dict["rf_role"] = rf_role
        if rf_channel is not UNSET:
            field_dict["rf_channel"] = rf_channel
        if poe_mode is not UNSET:
            field_dict["poe_mode"] = poe_mode
        if poe_type is not UNSET:
            field_dict["poe_type"] = poe_type
        if rf_channel_frequency is not UNSET:
            field_dict["rf_channel_frequency"] = rf_channel_frequency
        if rf_channel_width is not UNSET:
            field_dict["rf_channel_width"] = rf_channel_width
        if tx_power is not UNSET:
            field_dict["tx_power"] = tx_power
        if untagged_vlan is not UNSET:
            field_dict["untagged_vlan"] = untagged_vlan
        if tagged_vlans is not UNSET:
            field_dict["tagged_vlans"] = tagged_vlans
        if qinq_svlan is not UNSET:
            field_dict["qinq_svlan"] = qinq_svlan
        if vlan_translation_policy is not UNSET:
            field_dict["vlan_translation_policy"] = vlan_translation_policy
        if mark_connected is not UNSET:
            field_dict["mark_connected"] = mark_connected
        if wireless_lans is not UNSET:
            field_dict["wireless_lans"] = wireless_lans
        if vrf is not UNSET:
            field_dict["vrf"] = vrf
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_cable import BriefCable
        from ..models.brief_device import BriefDevice
        from ..models.brief_l2vpn_termination import BriefL2VPNTermination
        from ..models.brief_mac_address import BriefMACAddress
        from ..models.brief_module import BriefModule
        from ..models.brief_vlan import BriefVLAN
        from ..models.brief_vlan_translation_policy import BriefVLANTranslationPolicy
        from ..models.brief_vrf import BriefVRF
        from ..models.interface_custom_fields import InterfaceCustomFields
        from ..models.interface_duplex_type_0 import InterfaceDuplexType0
        from ..models.interface_mode import InterfaceMode
        from ..models.interface_poe_mode import InterfacePoeMode
        from ..models.interface_poe_type import InterfacePoeType
        from ..models.interface_rf_channel import InterfaceRfChannel
        from ..models.interface_rf_role import InterfaceRfRole
        from ..models.interface_type import InterfaceType
        from ..models.nested_interface import NestedInterface
        from ..models.nested_tag import NestedTag
        from ..models.nested_wireless_link import NestedWirelessLink
        from ..models.virtual_device_context import VirtualDeviceContext
        from ..models.vlan import VLAN
        from ..models.wireless_lan import WirelessLAN

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        device = BriefDevice.from_dict(d.pop("device"))

        name = d.pop("name")

        type_ = InterfaceType.from_dict(d.pop("type"))

        def _parse_mac_address(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        mac_address = _parse_mac_address(d.pop("mac_address"))

        def _parse_mac_addresses(data: object) -> Union[None, list["BriefMACAddress"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mac_addresses_type_0 = []
                _mac_addresses_type_0 = data
                for mac_addresses_type_0_item_data in _mac_addresses_type_0:
                    mac_addresses_type_0_item = BriefMACAddress.from_dict(mac_addresses_type_0_item_data)

                    mac_addresses_type_0.append(mac_addresses_type_0_item)

                return mac_addresses_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["BriefMACAddress"]], data)

        mac_addresses = _parse_mac_addresses(d.pop("mac_addresses"))

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

        def _parse_wireless_link(data: object) -> Union["NestedWirelessLink", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                wireless_link_type_1 = NestedWirelessLink.from_dict(data)

                return wireless_link_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NestedWirelessLink", None], data)

        wireless_link = _parse_wireless_link(d.pop("wireless_link"))

        link_peers = cast(list[Any], d.pop("link_peers"))

        def _parse_link_peers_type(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        link_peers_type = _parse_link_peers_type(d.pop("link_peers_type"))

        def _parse_l2vpn_termination(data: object) -> Union["BriefL2VPNTermination", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                l2vpn_termination_type_1 = BriefL2VPNTermination.from_dict(data)

                return l2vpn_termination_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefL2VPNTermination", None], data)

        l2vpn_termination = _parse_l2vpn_termination(d.pop("l2vpn_termination"))

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

        count_ipaddresses = d.pop("count_ipaddresses")

        count_fhrp_groups = d.pop("count_fhrp_groups")

        field_occupied = d.pop("_occupied")

        vdcs = []
        _vdcs = d.pop("vdcs", UNSET)
        for vdcs_item_data in _vdcs or []:
            vdcs_item = VirtualDeviceContext.from_dict(vdcs_item_data)

            vdcs.append(vdcs_item)

        def _parse_module(data: object) -> Union["BriefModule", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                module_type_1 = BriefModule.from_dict(data)

                return module_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefModule", None, Unset], data)

        module = _parse_module(d.pop("module", UNSET))

        label = d.pop("label", UNSET)

        enabled = d.pop("enabled", UNSET)

        def _parse_parent(data: object) -> Union["NestedInterface", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_type_1 = NestedInterface.from_dict(data)

                return parent_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NestedInterface", None, Unset], data)

        parent = _parse_parent(d.pop("parent", UNSET))

        def _parse_bridge(data: object) -> Union["NestedInterface", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bridge_type_1 = NestedInterface.from_dict(data)

                return bridge_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NestedInterface", None, Unset], data)

        bridge = _parse_bridge(d.pop("bridge", UNSET))

        def _parse_lag(data: object) -> Union["NestedInterface", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                lag_type_1 = NestedInterface.from_dict(data)

                return lag_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NestedInterface", None, Unset], data)

        lag = _parse_lag(d.pop("lag", UNSET))

        def _parse_mtu(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        mtu = _parse_mtu(d.pop("mtu", UNSET))

        def _parse_primary_mac_address(data: object) -> Union["BriefMACAddress", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                primary_mac_address_type_1 = BriefMACAddress.from_dict(data)

                return primary_mac_address_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefMACAddress", None, Unset], data)

        primary_mac_address = _parse_primary_mac_address(d.pop("primary_mac_address", UNSET))

        def _parse_speed(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        speed = _parse_speed(d.pop("speed", UNSET))

        def _parse_duplex(data: object) -> Union["InterfaceDuplexType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                duplex_type_0 = InterfaceDuplexType0.from_dict(data)

                return duplex_type_0
            except:  # noqa: E722
                pass
            return cast(Union["InterfaceDuplexType0", None, Unset], data)

        duplex = _parse_duplex(d.pop("duplex", UNSET))

        def _parse_wwn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        wwn = _parse_wwn(d.pop("wwn", UNSET))

        mgmt_only = d.pop("mgmt_only", UNSET)

        description = d.pop("description", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, InterfaceMode]
        # if isinstance(_mode, Unset):
        #     mode = UNSET
        # else:
        #     mode = InterfaceMode.from_dict(_mode)

        _rf_role = d.pop("rf_role", UNSET)
        rf_role: Union[Unset, InterfaceRfRole]
        # if isinstance(_rf_role, Unset):
        #     rf_role = UNSET
        # else:
        #     rf_role = InterfaceRfRole.from_dict(_rf_role)

        _rf_channel = d.pop("rf_channel", UNSET)
        rf_channel: Union[Unset, InterfaceRfChannel]
        # if isinstance(_rf_channel, Unset):
        #     rf_channel = UNSET
        # else:
        #     rf_channel = InterfaceRfChannel.from_dict(_rf_channel)

        _poe_mode = d.pop("poe_mode", UNSET)
        poe_mode: Union[Unset, InterfacePoeMode]
        # if isinstance(_poe_mode, Unset):
        #     poe_mode = UNSET
        # else:
        #     poe_mode = InterfacePoeMode.from_dict(_poe_mode)

        _poe_type = d.pop("poe_type", UNSET)
        poe_type: Union[Unset, InterfacePoeType]
        # if isinstance(_poe_type, Unset):
        #     poe_type = UNSET
        # else:
        #     poe_type = InterfacePoeType.from_dict(_poe_type)

        def _parse_rf_channel_frequency(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        rf_channel_frequency = _parse_rf_channel_frequency(d.pop("rf_channel_frequency", UNSET))

        def _parse_rf_channel_width(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        rf_channel_width = _parse_rf_channel_width(d.pop("rf_channel_width", UNSET))

        def _parse_tx_power(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        tx_power = _parse_tx_power(d.pop("tx_power", UNSET))

        def _parse_untagged_vlan(data: object) -> Union["BriefVLAN", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                untagged_vlan_type_1 = BriefVLAN.from_dict(data)

                return untagged_vlan_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVLAN", None, Unset], data)

        untagged_vlan = _parse_untagged_vlan(d.pop("untagged_vlan", UNSET))

        tagged_vlans = []
        _tagged_vlans = d.pop("tagged_vlans", UNSET)
        for tagged_vlans_item_data in _tagged_vlans or []:
            tagged_vlans_item = VLAN.from_dict(tagged_vlans_item_data)

            tagged_vlans.append(tagged_vlans_item)

        def _parse_qinq_svlan(data: object) -> Union["BriefVLAN", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                qinq_svlan_type_1 = BriefVLAN.from_dict(data)

                return qinq_svlan_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVLAN", None, Unset], data)

        qinq_svlan = _parse_qinq_svlan(d.pop("qinq_svlan", UNSET))

        def _parse_vlan_translation_policy(data: object) -> Union["BriefVLANTranslationPolicy", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vlan_translation_policy_type_1 = BriefVLANTranslationPolicy.from_dict(data)

                return vlan_translation_policy_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVLANTranslationPolicy", None, Unset], data)

        vlan_translation_policy = _parse_vlan_translation_policy(d.pop("vlan_translation_policy", UNSET))

        mark_connected = d.pop("mark_connected", UNSET)

        wireless_lans = []
        _wireless_lans = d.pop("wireless_lans", UNSET)
        for wireless_lans_item_data in _wireless_lans or []:
            wireless_lans_item = WirelessLAN.from_dict(wireless_lans_item_data)

            wireless_lans.append(wireless_lans_item)

        def _parse_vrf(data: object) -> Union["BriefVRF", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vrf_type_1 = BriefVRF.from_dict(data)

                return vrf_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVRF", None, Unset], data)

        vrf = _parse_vrf(d.pop("vrf", UNSET))

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, InterfaceCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = InterfaceCustomFields.from_dict(_custom_fields)

        interface = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            device=device,
            name=name,
            type_=type_,
            mac_address=mac_address,
            mac_addresses=mac_addresses,
            cable=cable,
            cable_end=cable_end,
            wireless_link=wireless_link,
            link_peers=link_peers,
            link_peers_type=link_peers_type,
            l2vpn_termination=l2vpn_termination,
            connected_endpoints=connected_endpoints,
            connected_endpoints_type=connected_endpoints_type,
            connected_endpoints_reachable=connected_endpoints_reachable,
            created=created,
            last_updated=last_updated,
            count_ipaddresses=count_ipaddresses,
            count_fhrp_groups=count_fhrp_groups,
            field_occupied=field_occupied,
            vdcs=vdcs,
            module=module,
            label=label,
            enabled=enabled,
            parent=parent,
            bridge=bridge,
            lag=lag,
            mtu=mtu,
            primary_mac_address=primary_mac_address,
            speed=speed,
            duplex=duplex,
            wwn=wwn,
            mgmt_only=mgmt_only,
            description=description,
#            mode=mode,
#            rf_role=rf_role,
#            rf_channel=rf_channel,
#            poe_mode=poe_mode,
#            poe_type=poe_type,
            rf_channel_frequency=rf_channel_frequency,
            rf_channel_width=rf_channel_width,
            tx_power=tx_power,
            untagged_vlan=untagged_vlan,
            tagged_vlans=tagged_vlans,
            qinq_svlan=qinq_svlan,
            vlan_translation_policy=vlan_translation_policy,
            mark_connected=mark_connected,
            wireless_lans=wireless_lans,
            vrf=vrf,
            tags=tags,
            custom_fields=custom_fields,
        )

        interface.additional_properties = d
        return interface

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
