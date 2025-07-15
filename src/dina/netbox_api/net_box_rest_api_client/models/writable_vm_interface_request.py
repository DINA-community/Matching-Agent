import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_vm_interface_request_mode_type_1 import WritableVMInterfaceRequestModeType1
from ..models.writable_vm_interface_request_mode_type_2_type_1 import WritableVMInterfaceRequestModeType2Type1
from ..models.writable_vm_interface_request_mode_type_3_type_1 import WritableVMInterfaceRequestModeType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_mac_address_request import BriefMACAddressRequest
    from ..models.brief_virtual_machine_request import BriefVirtualMachineRequest
    from ..models.brief_vlan_request import BriefVLANRequest
    from ..models.brief_vlan_translation_policy_request import BriefVLANTranslationPolicyRequest
    from ..models.brief_vrf_request import BriefVRFRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.writable_vm_interface_request_custom_fields import WritableVMInterfaceRequestCustomFields


T = TypeVar("T", bound="WritableVMInterfaceRequest")


@_attrs_define
class WritableVMInterfaceRequest:
    """Adds support for custom fields and tags.

    Attributes:
        virtual_machine (Union['BriefVirtualMachineRequest', int]):
        name (str):
        enabled (Union[Unset, bool]):
        parent (Union[None, Unset, int]):
        bridge (Union[None, Unset, int]):
        mtu (Union[None, Unset, int]):
        primary_mac_address (Union['BriefMACAddressRequest', None, Unset, int]):
        description (Union[Unset, str]):
        mode (Union[None, Unset, WritableVMInterfaceRequestModeType1, WritableVMInterfaceRequestModeType2Type1,
            WritableVMInterfaceRequestModeType3Type1]): IEEE 802.1Q tagging strategy

            * `access` - Access
            * `tagged` - Tagged
            * `tagged-all` - Tagged (All)
            * `q-in-q` - Q-in-Q (802.1ad)
        untagged_vlan (Union['BriefVLANRequest', None, Unset, int]):
        tagged_vlans (Union[Unset, list[int]]):
        qinq_svlan (Union['BriefVLANRequest', None, Unset, int]):
        vlan_translation_policy (Union['BriefVLANTranslationPolicyRequest', None, Unset, int]):
        vrf (Union['BriefVRFRequest', None, Unset, int]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, WritableVMInterfaceRequestCustomFields]):
    """

    virtual_machine: Union["BriefVirtualMachineRequest", int]
    name: str
    enabled: Union[Unset, bool] = UNSET
    parent: Union[None, Unset, int] = UNSET
    bridge: Union[None, Unset, int] = UNSET
    mtu: Union[None, Unset, int] = UNSET
    primary_mac_address: Union["BriefMACAddressRequest", None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    mode: Union[
        None,
        Unset,
        WritableVMInterfaceRequestModeType1,
        WritableVMInterfaceRequestModeType2Type1,
        WritableVMInterfaceRequestModeType3Type1,
    ] = UNSET
    untagged_vlan: Union["BriefVLANRequest", None, Unset, int] = UNSET
    tagged_vlans: Union[Unset, list[int]] = UNSET
    qinq_svlan: Union["BriefVLANRequest", None, Unset, int] = UNSET
    vlan_translation_policy: Union["BriefVLANTranslationPolicyRequest", None, Unset, int] = UNSET
    vrf: Union["BriefVRFRequest", None, Unset, int] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "WritableVMInterfaceRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_mac_address_request import BriefMACAddressRequest
        from ..models.brief_virtual_machine_request import BriefVirtualMachineRequest
        from ..models.brief_vlan_request import BriefVLANRequest
        from ..models.brief_vlan_translation_policy_request import BriefVLANTranslationPolicyRequest
        from ..models.brief_vrf_request import BriefVRFRequest

        virtual_machine: Union[dict[str, Any], int]
        if isinstance(self.virtual_machine, BriefVirtualMachineRequest):
            virtual_machine = self.virtual_machine.to_dict()
        else:
            virtual_machine = self.virtual_machine

        name = self.name

        enabled = self.enabled

        parent: Union[None, Unset, int]
        if isinstance(self.parent, Unset):
            parent = UNSET
        else:
            parent = self.parent

        bridge: Union[None, Unset, int]
        if isinstance(self.bridge, Unset):
            bridge = UNSET
        else:
            bridge = self.bridge

        mtu: Union[None, Unset, int]
        if isinstance(self.mtu, Unset):
            mtu = UNSET
        else:
            mtu = self.mtu

        primary_mac_address: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.primary_mac_address, Unset):
            primary_mac_address = UNSET
        elif isinstance(self.primary_mac_address, BriefMACAddressRequest):
            primary_mac_address = self.primary_mac_address.to_dict()
        else:
            primary_mac_address = self.primary_mac_address

        description = self.description

        mode: Union[None, Unset, str]
        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, WritableVMInterfaceRequestModeType1):
            mode = self.mode.value
        elif isinstance(self.mode, WritableVMInterfaceRequestModeType2Type1):
            mode = self.mode.value
        elif isinstance(self.mode, WritableVMInterfaceRequestModeType3Type1):
            mode = self.mode.value
        else:
            mode = self.mode

        untagged_vlan: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.untagged_vlan, Unset):
            untagged_vlan = UNSET
        elif isinstance(self.untagged_vlan, BriefVLANRequest):
            untagged_vlan = self.untagged_vlan.to_dict()
        else:
            untagged_vlan = self.untagged_vlan

        tagged_vlans: Union[Unset, list[int]] = UNSET
        if not isinstance(self.tagged_vlans, Unset):
            tagged_vlans = self.tagged_vlans

        qinq_svlan: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.qinq_svlan, Unset):
            qinq_svlan = UNSET
        elif isinstance(self.qinq_svlan, BriefVLANRequest):
            qinq_svlan = self.qinq_svlan.to_dict()
        else:
            qinq_svlan = self.qinq_svlan

        vlan_translation_policy: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.vlan_translation_policy, Unset):
            vlan_translation_policy = UNSET
        elif isinstance(self.vlan_translation_policy, BriefVLANTranslationPolicyRequest):
            vlan_translation_policy = self.vlan_translation_policy.to_dict()
        else:
            vlan_translation_policy = self.vlan_translation_policy

        vrf: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.vrf, Unset):
            vrf = UNSET
        elif isinstance(self.vrf, BriefVRFRequest):
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
                "virtual_machine": virtual_machine,
                "name": name,
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

    def to_multipart(self) -> dict[str, Any]:
        virtual_machine: tuple[None, bytes, str]

        if isinstance(self.virtual_machine, int):
            virtual_machine = (None, str(self.virtual_machine).encode(), "text/plain")
        else:
            virtual_machine = (None, json.dumps(self.virtual_machine.to_dict()).encode(), "application/json")

        name = (None, str(self.name).encode(), "text/plain")

        enabled = self.enabled if isinstance(self.enabled, Unset) else (None, str(self.enabled).encode(), "text/plain")

        parent: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, int):
            parent = (None, str(self.parent).encode(), "text/plain")
        else:
            parent = (None, str(self.parent).encode(), "text/plain")

        bridge: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.bridge, Unset):
            bridge = UNSET
        elif isinstance(self.bridge, int):
            bridge = (None, str(self.bridge).encode(), "text/plain")
        else:
            bridge = (None, str(self.bridge).encode(), "text/plain")

        mtu: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.mtu, Unset):
            mtu = UNSET
        elif isinstance(self.mtu, int):
            mtu = (None, str(self.mtu).encode(), "text/plain")
        else:
            mtu = (None, str(self.mtu).encode(), "text/plain")

        primary_mac_address: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.primary_mac_address, Unset):
            primary_mac_address = UNSET
        elif isinstance(self.primary_mac_address, int):
            primary_mac_address = (None, str(self.primary_mac_address).encode(), "text/plain")
        elif isinstance(self.primary_mac_address, None):
            primary_mac_address = (None, str(self.primary_mac_address).encode(), "text/plain")
        elif isinstance(self.primary_mac_address, BriefMACAddressRequest):
            primary_mac_address = (None, json.dumps(self.primary_mac_address.to_dict()).encode(), "application/json")
        else:
            primary_mac_address = (None, str(self.primary_mac_address).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        mode: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, None):
            mode = (None, str(self.mode).encode(), "text/plain")
        elif isinstance(self.mode, WritableVMInterfaceRequestModeType1):
            mode = (None, str(self.mode.value).encode(), "text/plain")
        elif isinstance(self.mode, None):
            mode = (None, str(self.mode).encode(), "text/plain")
        elif isinstance(self.mode, WritableVMInterfaceRequestModeType2Type1):
            mode = (None, str(self.mode.value).encode(), "text/plain")
        elif isinstance(self.mode, None):
            mode = (None, str(self.mode).encode(), "text/plain")
        else:
            mode = (None, str(self.mode.value).encode(), "text/plain")

        untagged_vlan: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.untagged_vlan, Unset):
            untagged_vlan = UNSET
        elif isinstance(self.untagged_vlan, int):
            untagged_vlan = (None, str(self.untagged_vlan).encode(), "text/plain")
        elif isinstance(self.untagged_vlan, None):
            untagged_vlan = (None, str(self.untagged_vlan).encode(), "text/plain")
        elif isinstance(self.untagged_vlan, BriefVLANRequest):
            untagged_vlan = (None, json.dumps(self.untagged_vlan.to_dict()).encode(), "application/json")
        else:
            untagged_vlan = (None, str(self.untagged_vlan).encode(), "text/plain")

        tagged_vlans: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tagged_vlans, Unset):
            _temp_tagged_vlans = self.tagged_vlans
            tagged_vlans = (None, json.dumps(_temp_tagged_vlans).encode(), "application/json")

        qinq_svlan: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.qinq_svlan, Unset):
            qinq_svlan = UNSET
        elif isinstance(self.qinq_svlan, int):
            qinq_svlan = (None, str(self.qinq_svlan).encode(), "text/plain")
        elif isinstance(self.qinq_svlan, None):
            qinq_svlan = (None, str(self.qinq_svlan).encode(), "text/plain")
        elif isinstance(self.qinq_svlan, BriefVLANRequest):
            qinq_svlan = (None, json.dumps(self.qinq_svlan.to_dict()).encode(), "application/json")
        else:
            qinq_svlan = (None, str(self.qinq_svlan).encode(), "text/plain")

        vlan_translation_policy: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.vlan_translation_policy, Unset):
            vlan_translation_policy = UNSET
        elif isinstance(self.vlan_translation_policy, int):
            vlan_translation_policy = (None, str(self.vlan_translation_policy).encode(), "text/plain")
        elif isinstance(self.vlan_translation_policy, None):
            vlan_translation_policy = (None, str(self.vlan_translation_policy).encode(), "text/plain")
        elif isinstance(self.vlan_translation_policy, BriefVLANTranslationPolicyRequest):
            vlan_translation_policy = (
                None,
                json.dumps(self.vlan_translation_policy.to_dict()).encode(),
                "application/json",
            )
        else:
            vlan_translation_policy = (None, str(self.vlan_translation_policy).encode(), "text/plain")

        vrf: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.vrf, Unset):
            vrf = UNSET
        elif isinstance(self.vrf, int):
            vrf = (None, str(self.vrf).encode(), "text/plain")
        elif isinstance(self.vrf, None):
            vrf = (None, str(self.vrf).encode(), "text/plain")
        elif isinstance(self.vrf, BriefVRFRequest):
            vrf = (None, json.dumps(self.vrf.to_dict()).encode(), "application/json")
        else:
            vrf = (None, str(self.vrf).encode(), "text/plain")

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
                "virtual_machine": virtual_machine,
                "name": name,
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
        from ..models.brief_mac_address_request import BriefMACAddressRequest
        from ..models.brief_virtual_machine_request import BriefVirtualMachineRequest
        from ..models.brief_vlan_request import BriefVLANRequest
        from ..models.brief_vlan_translation_policy_request import BriefVLANTranslationPolicyRequest
        from ..models.brief_vrf_request import BriefVRFRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.writable_vm_interface_request_custom_fields import WritableVMInterfaceRequestCustomFields

        d = dict(src_dict)

        def _parse_virtual_machine(data: object) -> Union["BriefVirtualMachineRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                virtual_machine_type_1 = BriefVirtualMachineRequest.from_dict(data)

                return virtual_machine_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVirtualMachineRequest", int], data)

        virtual_machine = _parse_virtual_machine(d.pop("virtual_machine"))

        name = d.pop("name")

        enabled = d.pop("enabled", UNSET)

        def _parse_parent(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent = _parse_parent(d.pop("parent", UNSET))

        def _parse_bridge(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bridge = _parse_bridge(d.pop("bridge", UNSET))

        def _parse_mtu(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        mtu = _parse_mtu(d.pop("mtu", UNSET))

        def _parse_primary_mac_address(data: object) -> Union["BriefMACAddressRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                primary_mac_address_type_1_type_1 = BriefMACAddressRequest.from_dict(data)

                return primary_mac_address_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefMACAddressRequest", None, Unset, int], data)

        primary_mac_address = _parse_primary_mac_address(d.pop("primary_mac_address", UNSET))

        description = d.pop("description", UNSET)

        def _parse_mode(
            data: object,
        ) -> Union[
            None,
            Unset,
            WritableVMInterfaceRequestModeType1,
            WritableVMInterfaceRequestModeType2Type1,
            WritableVMInterfaceRequestModeType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_1 = WritableVMInterfaceRequestModeType1(data)

                return mode_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_2_type_1 = WritableVMInterfaceRequestModeType2Type1(data)

                return mode_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_3_type_1 = WritableVMInterfaceRequestModeType3Type1(data)

                return mode_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    WritableVMInterfaceRequestModeType1,
                    WritableVMInterfaceRequestModeType2Type1,
                    WritableVMInterfaceRequestModeType3Type1,
                ],
                data,
            )

        mode = _parse_mode(d.pop("mode", UNSET))

        def _parse_untagged_vlan(data: object) -> Union["BriefVLANRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                untagged_vlan_type_1_type_1 = BriefVLANRequest.from_dict(data)

                return untagged_vlan_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVLANRequest", None, Unset, int], data)

        untagged_vlan = _parse_untagged_vlan(d.pop("untagged_vlan", UNSET))

        tagged_vlans = cast(list[int], d.pop("tagged_vlans", UNSET))

        def _parse_qinq_svlan(data: object) -> Union["BriefVLANRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                qinq_svlan_type_1_type_1 = BriefVLANRequest.from_dict(data)

                return qinq_svlan_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVLANRequest", None, Unset, int], data)

        qinq_svlan = _parse_qinq_svlan(d.pop("qinq_svlan", UNSET))

        def _parse_vlan_translation_policy(
            data: object,
        ) -> Union["BriefVLANTranslationPolicyRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vlan_translation_policy_type_1_type_1 = BriefVLANTranslationPolicyRequest.from_dict(data)

                return vlan_translation_policy_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVLANTranslationPolicyRequest", None, Unset, int], data)

        vlan_translation_policy = _parse_vlan_translation_policy(d.pop("vlan_translation_policy", UNSET))

        def _parse_vrf(data: object) -> Union["BriefVRFRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vrf_type_1_type_1 = BriefVRFRequest.from_dict(data)

                return vrf_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefVRFRequest", None, Unset, int], data)

        vrf = _parse_vrf(d.pop("vrf", UNSET))

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, WritableVMInterfaceRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WritableVMInterfaceRequestCustomFields.from_dict(_custom_fields)

        writable_vm_interface_request = cls(
            virtual_machine=virtual_machine,
            name=name,
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

        writable_vm_interface_request.additional_properties = d
        return writable_vm_interface_request

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
