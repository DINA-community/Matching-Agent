import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_l2vpn_termination import BriefL2VPNTermination
    from ..models.brief_mac_address import BriefMACAddress
    from ..models.brief_virtual_machine import BriefVirtualMachine
    from ..models.brief_vlan import BriefVLAN
    from ..models.brief_vlan_translation_policy import BriefVLANTranslationPolicy
    from ..models.brief_vrf import BriefVRF
    from ..models.nested_tag import NestedTag
    from ..models.nested_vm_interface import NestedVMInterface
    from ..models.vlan import VLAN
    from ..models.vm_interface_custom_fields import VMInterfaceCustomFields
    from ..models.vm_interface_mode import VMInterfaceMode


T = TypeVar("T", bound="VMInterface")


@_attrs_define
class VMInterface:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        virtual_machine (BriefVirtualMachine): Adds support for custom fields and tags.
        name (str):
        mac_address (Union[None, str]):
        mac_addresses (Union[None, list['BriefMACAddress']]):
        l2vpn_termination (Union['BriefL2VPNTermination', None]):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        count_ipaddresses (int):
        count_fhrp_groups (int):
        enabled (Union[Unset, bool]):
        parent (Union['NestedVMInterface', None, Unset]):
        bridge (Union['NestedVMInterface', None, Unset]):
        mtu (Union[None, Unset, int]):
        primary_mac_address (Union['BriefMACAddress', None, Unset]):
        description (Union[Unset, str]):
        mode (Union[Unset, VMInterfaceMode]):
        untagged_vlan (Union['BriefVLAN', None, Unset]):
        tagged_vlans (Union[Unset, list['VLAN']]):
        qinq_svlan (Union['BriefVLAN', None, Unset]):
        vlan_translation_policy (Union['BriefVLANTranslationPolicy', None, Unset]):
        vrf (Union['BriefVRF', None, Unset]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, VMInterfaceCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    virtual_machine: "BriefVirtualMachine"
    name: str
    mac_address: Union[None, str]
    mac_addresses: Union[None, list["BriefMACAddress"]]
    l2vpn_termination: Union["BriefL2VPNTermination", None]
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    count_ipaddresses: int
    count_fhrp_groups: int
    enabled: Union[Unset, bool] = UNSET
    parent: Union["NestedVMInterface", None, Unset] = UNSET
    bridge: Union["NestedVMInterface", None, Unset] = UNSET
    mtu: Union[None, Unset, int] = UNSET
    primary_mac_address: Union["BriefMACAddress", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    mode: Union[Unset, "VMInterfaceMode"] = UNSET
    untagged_vlan: Union["BriefVLAN", None, Unset] = UNSET
    tagged_vlans: Union[Unset, list["VLAN"]] = UNSET
    qinq_svlan: Union["BriefVLAN", None, Unset] = UNSET
    vlan_translation_policy: Union["BriefVLANTranslationPolicy", None, Unset] = UNSET
    vrf: Union["BriefVRF", None, Unset] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "VMInterfaceCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_l2vpn_termination import BriefL2VPNTermination
        from ..models.brief_mac_address import BriefMACAddress
        from ..models.brief_vlan import BriefVLAN
        from ..models.brief_vlan_translation_policy import BriefVLANTranslationPolicy
        from ..models.brief_vrf import BriefVRF
        from ..models.nested_vm_interface import NestedVMInterface

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        virtual_machine = self.virtual_machine.to_dict()

        name = self.name

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

        l2vpn_termination: Union[None, dict[str, Any]]
        if isinstance(self.l2vpn_termination, BriefL2VPNTermination):
            l2vpn_termination = self.l2vpn_termination.to_dict()
        else:
            l2vpn_termination = self.l2vpn_termination

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

        enabled = self.enabled

        parent: Union[None, Unset, dict[str, Any]]
        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, NestedVMInterface):
            parent = self.parent.to_dict()
        else:
            parent = self.parent

        bridge: Union[None, Unset, dict[str, Any]]
        if isinstance(self.bridge, Unset):
            bridge = UNSET
        elif isinstance(self.bridge, NestedVMInterface):
            bridge = self.bridge.to_dict()
        else:
            bridge = self.bridge

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

        description = self.description

        mode: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.to_dict()

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
                "virtual_machine": virtual_machine,
                "name": name,
                "mac_address": mac_address,
                "mac_addresses": mac_addresses,
                "l2vpn_termination": l2vpn_termination,
                "created": created,
                "last_updated": last_updated,
                "count_ipaddresses": count_ipaddresses,
                "count_fhrp_groups": count_fhrp_groups,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if parent is not UNSET:
            field_dict["parent"] = parent
        if bridge is not UNSET:
            field_dict["bridge"] = bridge
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if primary_mac_address is not UNSET:
            field_dict["primary_mac_address"] = primary_mac_address
        if description is not UNSET:
            field_dict["description"] = description
        if mode is not UNSET:
            field_dict["mode"] = mode
        if untagged_vlan is not UNSET:
            field_dict["untagged_vlan"] = untagged_vlan
        if tagged_vlans is not UNSET:
            field_dict["tagged_vlans"] = tagged_vlans
        if qinq_svlan is not UNSET:
            field_dict["qinq_svlan"] = qinq_svlan
        if vlan_translation_policy is not UNSET:
            field_dict["vlan_translation_policy"] = vlan_translation_policy
        if vrf is not UNSET:
            field_dict["vrf"] = vrf
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_l2vpn_termination import BriefL2VPNTermination
        from ..models.brief_mac_address import BriefMACAddress
        from ..models.brief_virtual_machine import BriefVirtualMachine
        from ..models.brief_vlan import BriefVLAN
        from ..models.brief_vlan_translation_policy import BriefVLANTranslationPolicy
        from ..models.brief_vrf import BriefVRF
        from ..models.nested_tag import NestedTag
        from ..models.nested_vm_interface import NestedVMInterface
        from ..models.vlan import VLAN
        from ..models.vm_interface_custom_fields import VMInterfaceCustomFields
        from ..models.vm_interface_mode import VMInterfaceMode

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        virtual_machine = BriefVirtualMachine.from_dict(d.pop("virtual_machine"))

        name = d.pop("name")

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
                    mac_addresses_type_0_item = BriefMACAddress.from_dict(
                        mac_addresses_type_0_item_data
                    )

                    mac_addresses_type_0.append(mac_addresses_type_0_item)

                return mac_addresses_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["BriefMACAddress"]], data)

        mac_addresses = _parse_mac_addresses(d.pop("mac_addresses"))

        def _parse_l2vpn_termination(
            data: object,
        ) -> Union["BriefL2VPNTermination", None]:
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

        enabled = d.pop("enabled", UNSET)

        def _parse_parent(data: object) -> Union["NestedVMInterface", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_type_1 = NestedVMInterface.from_dict(data)

                return parent_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NestedVMInterface", None, Unset], data)

        parent = _parse_parent(d.pop("parent", UNSET))

        def _parse_bridge(data: object) -> Union["NestedVMInterface", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bridge_type_1 = NestedVMInterface.from_dict(data)

                return bridge_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NestedVMInterface", None, Unset], data)

        bridge = _parse_bridge(d.pop("bridge", UNSET))

        def _parse_mtu(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        mtu = _parse_mtu(d.pop("mtu", UNSET))

        def _parse_primary_mac_address(
            data: object,
        ) -> Union["BriefMACAddress", None, Unset]:
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

        primary_mac_address = _parse_primary_mac_address(
            d.pop("primary_mac_address", UNSET)
        )

        description = d.pop("description", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, VMInterfaceMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = VMInterfaceMode.from_dict(_mode)

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

        def _parse_vlan_translation_policy(
            data: object,
        ) -> Union["BriefVLANTranslationPolicy", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vlan_translation_policy_type_1 = BriefVLANTranslationPolicy.from_dict(
                    data
                )

                return vlan_translation_policy_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVLANTranslationPolicy", None, Unset], data)

        vlan_translation_policy = _parse_vlan_translation_policy(
            d.pop("vlan_translation_policy", UNSET)
        )

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
        custom_fields: Union[Unset, VMInterfaceCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = VMInterfaceCustomFields.from_dict(_custom_fields)

        vm_interface = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            virtual_machine=virtual_machine,
            name=name,
            mac_address=mac_address,
            mac_addresses=mac_addresses,
            l2vpn_termination=l2vpn_termination,
            created=created,
            last_updated=last_updated,
            count_ipaddresses=count_ipaddresses,
            count_fhrp_groups=count_fhrp_groups,
            enabled=enabled,
            parent=parent,
            bridge=bridge,
            mtu=mtu,
            primary_mac_address=primary_mac_address,
            description=description,
            mode=mode,
            untagged_vlan=untagged_vlan,
            tagged_vlans=tagged_vlans,
            qinq_svlan=qinq_svlan,
            vlan_translation_policy=vlan_translation_policy,
            vrf=vrf,
            tags=tags,
            custom_fields=custom_fields,
        )

        vm_interface.additional_properties = d
        return vm_interface

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
