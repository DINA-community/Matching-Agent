import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.writable_interface_template_request_poe_mode_type_1 import WritableInterfaceTemplateRequestPoeModeType1
from ..models.writable_interface_template_request_poe_mode_type_2_type_1 import (
    WritableInterfaceTemplateRequestPoeModeType2Type1,
)
from ..models.writable_interface_template_request_poe_mode_type_3_type_1 import (
    WritableInterfaceTemplateRequestPoeModeType3Type1,
)
from ..models.writable_interface_template_request_poe_type_type_1 import WritableInterfaceTemplateRequestPoeTypeType1
from ..models.writable_interface_template_request_poe_type_type_2_type_1 import (
    WritableInterfaceTemplateRequestPoeTypeType2Type1,
)
from ..models.writable_interface_template_request_poe_type_type_3_type_1 import (
    WritableInterfaceTemplateRequestPoeTypeType3Type1,
)
from ..models.writable_interface_template_request_type import WritableInterfaceTemplateRequestType
from ..models.writable_interface_template_request_wireless_role import WritableInterfaceTemplateRequestWirelessRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_type_request import BriefDeviceTypeRequest
    from ..models.brief_module_type_request import BriefModuleTypeRequest


T = TypeVar("T", bound="WritableInterfaceTemplateRequest")


@_attrs_define
class WritableInterfaceTemplateRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            name (str): {module} is accepted as a substitution for the module bay position when attached to a module type.
            type_ (WritableInterfaceTemplateRequestType): * `virtual` - Virtual
                * `bridge` - Bridge
                * `lag` - Link Aggregation Group (LAG)
                * `100base-fx` - 100BASE-FX (10/100ME FIBER)
                * `100base-lfx` - 100BASE-LFX (10/100ME FIBER)
                * `100base-tx` - 100BASE-TX (10/100ME)
                * `100base-t1` - 100BASE-T1 (10/100ME Single Pair)
                * `1000base-t` - 1000BASE-T (1GE)
                * `1000base-sx` - 1000BASE-SX (1GE)
                * `1000base-lx` - 1000BASE-LX (1GE)
                * `1000base-tx` - 1000BASE-TX (1GE)
                * `2.5gbase-t` - 2.5GBASE-T (2.5GE)
                * `5gbase-t` - 5GBASE-T (5GE)
                * `10gbase-t` - 10GBASE-T (10GE)
                * `10gbase-cx4` - 10GBASE-CX4 (10GE)
                * `100base-x-sfp` - SFP (100ME)
                * `1000base-x-gbic` - GBIC (1GE)
                * `1000base-x-sfp` - SFP (1GE)
                * `10gbase-x-sfpp` - SFP+ (10GE)
                * `10gbase-x-xfp` - XFP (10GE)
                * `10gbase-x-xenpak` - XENPAK (10GE)
                * `10gbase-x-x2` - X2 (10GE)
                * `25gbase-x-sfp28` - SFP28 (25GE)
                * `50gbase-x-sfp56` - SFP56 (50GE)
                * `40gbase-x-qsfpp` - QSFP+ (40GE)
                * `50gbase-x-sfp28` - QSFP28 (50GE)
                * `100gbase-x-cfp` - CFP (100GE)
                * `100gbase-x-cfp2` - CFP2 (100GE)
                * `200gbase-x-cfp2` - CFP2 (200GE)
                * `400gbase-x-cfp2` - CFP2 (400GE)
                * `100gbase-x-cfp4` - CFP4 (100GE)
                * `100gbase-x-cxp` - CXP (100GE)
                * `100gbase-x-cpak` - Cisco CPAK (100GE)
                * `100gbase-x-dsfp` - DSFP (100GE)
                * `100gbase-x-sfpdd` - SFP-DD (100GE)
                * `100gbase-x-qsfp28` - QSFP28 (100GE)
                * `100gbase-x-qsfpdd` - QSFP-DD (100GE)
                * `200gbase-x-qsfp56` - QSFP56 (200GE)
                * `200gbase-x-qsfpdd` - QSFP-DD (200GE)
                * `400gbase-x-qsfp112` - QSFP112 (400GE)
                * `400gbase-x-qsfpdd` - QSFP-DD (400GE)
                * `400gbase-x-osfp` - OSFP (400GE)
                * `400gbase-x-osfp-rhs` - OSFP-RHS (400GE)
                * `400gbase-x-cdfp` - CDFP (400GE)
                * `400gbase-x-cfp8` - CPF8 (400GE)
                * `800gbase-x-qsfpdd` - QSFP-DD (800GE)
                * `800gbase-x-osfp` - OSFP (800GE)
                * `1000base-kx` - 1000BASE-KX (1GE)
                * `2.5gbase-kx` - 2.5GBASE-KX (2.5GE)
                * `5gbase-kr` - 5GBASE-KR (5GE)
                * `10gbase-kr` - 10GBASE-KR (10GE)
                * `10gbase-kx4` - 10GBASE-KX4 (10GE)
                * `25gbase-kr` - 25GBASE-KR (25GE)
                * `40gbase-kr4` - 40GBASE-KR4 (40GE)
                * `50gbase-kr` - 50GBASE-KR (50GE)
                * `100gbase-kp4` - 100GBASE-KP4 (100GE)
                * `100gbase-kr2` - 100GBASE-KR2 (100GE)
                * `100gbase-kr4` - 100GBASE-KR4 (100GE)
                * `ieee802.11a` - IEEE 802.11a
                * `ieee802.11g` - IEEE 802.11b/g
                * `ieee802.11n` - IEEE 802.11n
                * `ieee802.11ac` - IEEE 802.11ac
                * `ieee802.11ad` - IEEE 802.11ad
                * `ieee802.11ax` - IEEE 802.11ax
                * `ieee802.11ay` - IEEE 802.11ay
                * `ieee802.11be` - IEEE 802.11be
                * `ieee802.15.1` - IEEE 802.15.1 (Bluetooth)
                * `ieee802.15.4` - IEEE 802.15.4 (LR-WPAN)
                * `other-wireless` - Other (Wireless)
                * `gsm` - GSM
                * `cdma` - CDMA
                * `lte` - LTE
                * `4g` - 4G
                * `5g` - 5G
                * `sonet-oc3` - OC-3/STM-1
                * `sonet-oc12` - OC-12/STM-4
                * `sonet-oc48` - OC-48/STM-16
                * `sonet-oc192` - OC-192/STM-64
                * `sonet-oc768` - OC-768/STM-256
                * `sonet-oc1920` - OC-1920/STM-640
                * `sonet-oc3840` - OC-3840/STM-1234
                * `1gfc-sfp` - SFP (1GFC)
                * `2gfc-sfp` - SFP (2GFC)
                * `4gfc-sfp` - SFP (4GFC)
                * `8gfc-sfpp` - SFP+ (8GFC)
                * `16gfc-sfpp` - SFP+ (16GFC)
                * `32gfc-sfp28` - SFP28 (32GFC)
                * `32gfc-sfpp` - SFP+ (32GFC)
                * `64gfc-qsfpp` - QSFP+ (64GFC)
                * `64gfc-sfpdd` - SFP-DD (64GFC)
                * `64gfc-sfpp` - SFP+ (64GFC)
                * `128gfc-qsfp28` - QSFP28 (128GFC)
                * `infiniband-sdr` - SDR (2 Gbps)
                * `infiniband-ddr` - DDR (4 Gbps)
                * `infiniband-qdr` - QDR (8 Gbps)
                * `infiniband-fdr10` - FDR10 (10 Gbps)
                * `infiniband-fdr` - FDR (13.5 Gbps)
                * `infiniband-edr` - EDR (25 Gbps)
                * `infiniband-hdr` - HDR (50 Gbps)
                * `infiniband-ndr` - NDR (100 Gbps)
                * `infiniband-xdr` - XDR (250 Gbps)
                * `t1` - T1 (1.544 Mbps)
                * `e1` - E1 (2.048 Mbps)
                * `t3` - T3 (45 Mbps)
                * `e3` - E3 (34 Mbps)
                * `xdsl` - xDSL
                * `docsis` - DOCSIS
                * `moca` - MoCA
                * `bpon` - BPON (622 Mbps / 155 Mbps)
                * `epon` - EPON (1 Gbps)
                * `10g-epon` - 10G-EPON (10 Gbps)
                * `gpon` - GPON (2.5 Gbps / 1.25 Gbps)
                * `xg-pon` - XG-PON (10 Gbps / 2.5 Gbps)
                * `xgs-pon` - XGS-PON (10 Gbps)
                * `ng-pon2` - NG-PON2 (TWDM-PON) (4x10 Gbps)
                * `25g-pon` - 25G-PON (25 Gbps)
                * `50g-pon` - 50G-PON (50 Gbps)
                * `cisco-stackwise` - Cisco StackWise
                * `cisco-stackwise-plus` - Cisco StackWise Plus
                * `cisco-flexstack` - Cisco FlexStack
                * `cisco-flexstack-plus` - Cisco FlexStack Plus
                * `cisco-stackwise-80` - Cisco StackWise-80
                * `cisco-stackwise-160` - Cisco StackWise-160
                * `cisco-stackwise-320` - Cisco StackWise-320
                * `cisco-stackwise-480` - Cisco StackWise-480
                * `cisco-stackwise-1t` - Cisco StackWise-1T
                * `juniper-vcp` - Juniper VCP
                * `extreme-summitstack` - Extreme SummitStack
                * `extreme-summitstack-128` - Extreme SummitStack-128
                * `extreme-summitstack-256` - Extreme SummitStack-256
                * `extreme-summitstack-512` - Extreme SummitStack-512
                * `other` - Other
            device_type (Union['BriefDeviceTypeRequest', None, Unset, int]):
            module_type (Union['BriefModuleTypeRequest', None, Unset, int]):
            label (Union[Unset, str]): Physical label
            enabled (Union[Unset, bool]):
            mgmt_only (Union[Unset, bool]):
            description (Union[Unset, str]):
            bridge (Union[None, Unset, int]):
            poe_mode (Union[None, Unset, WritableInterfaceTemplateRequestPoeModeType1,
                WritableInterfaceTemplateRequestPoeModeType2Type1, WritableInterfaceTemplateRequestPoeModeType3Type1]): * `pd` -
                PD
                * `pse` - PSE
            poe_type (Union[None, Unset, WritableInterfaceTemplateRequestPoeTypeType1,
                WritableInterfaceTemplateRequestPoeTypeType2Type1, WritableInterfaceTemplateRequestPoeTypeType3Type1]): *
                `type1-ieee802.3af` - 802.3af (Type 1)
                * `type2-ieee802.3at` - 802.3at (Type 2)
                * `type3-ieee802.3bt` - 802.3bt (Type 3)
                * `type4-ieee802.3bt` - 802.3bt (Type 4)
                * `passive-24v-2pair` - Passive 24V (2-pair)
                * `passive-24v-4pair` - Passive 24V (4-pair)
                * `passive-48v-2pair` - Passive 48V (2-pair)
                * `passive-48v-4pair` - Passive 48V (4-pair)
            rf_role (Union[None, Unset, WritableInterfaceTemplateRequestWirelessRole]): * `ap` - Access point
                * `station` - Station
    """

    name: str
    type_: WritableInterfaceTemplateRequestType
    device_type: Union["BriefDeviceTypeRequest", None, Unset, int] = UNSET
    module_type: Union["BriefModuleTypeRequest", None, Unset, int] = UNSET
    label: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    mgmt_only: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    bridge: Union[None, Unset, int] = UNSET
    poe_mode: Union[
        None,
        Unset,
        WritableInterfaceTemplateRequestPoeModeType1,
        WritableInterfaceTemplateRequestPoeModeType2Type1,
        WritableInterfaceTemplateRequestPoeModeType3Type1,
    ] = UNSET
    poe_type: Union[
        None,
        Unset,
        WritableInterfaceTemplateRequestPoeTypeType1,
        WritableInterfaceTemplateRequestPoeTypeType2Type1,
        WritableInterfaceTemplateRequestPoeTypeType3Type1,
    ] = UNSET
    rf_role: Union[None, Unset, WritableInterfaceTemplateRequestWirelessRole] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device_type_request import BriefDeviceTypeRequest
        from ..models.brief_module_type_request import BriefModuleTypeRequest

        name = self.name

        type_ = self.type_.value

        device_type: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.device_type, Unset):
            device_type = UNSET
        elif isinstance(self.device_type, BriefDeviceTypeRequest):
            device_type = self.device_type.to_dict()
        else:
            device_type = self.device_type

        module_type: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.module_type, Unset):
            module_type = UNSET
        elif isinstance(self.module_type, BriefModuleTypeRequest):
            module_type = self.module_type.to_dict()
        else:
            module_type = self.module_type

        label = self.label

        enabled = self.enabled

        mgmt_only = self.mgmt_only

        description = self.description

        bridge: Union[None, Unset, int]
        if isinstance(self.bridge, Unset):
            bridge = UNSET
        else:
            bridge = self.bridge

        poe_mode: Union[None, Unset, str]
        if isinstance(self.poe_mode, Unset):
            poe_mode = UNSET
        elif isinstance(self.poe_mode, WritableInterfaceTemplateRequestPoeModeType1):
            poe_mode = self.poe_mode.value
        elif isinstance(self.poe_mode, WritableInterfaceTemplateRequestPoeModeType2Type1):
            poe_mode = self.poe_mode.value
        elif isinstance(self.poe_mode, WritableInterfaceTemplateRequestPoeModeType3Type1):
            poe_mode = self.poe_mode.value
        else:
            poe_mode = self.poe_mode

        poe_type: Union[None, Unset, str]
        if isinstance(self.poe_type, Unset):
            poe_type = UNSET
        elif isinstance(self.poe_type, WritableInterfaceTemplateRequestPoeTypeType1):
            poe_type = self.poe_type.value
        elif isinstance(self.poe_type, WritableInterfaceTemplateRequestPoeTypeType2Type1):
            poe_type = self.poe_type.value
        elif isinstance(self.poe_type, WritableInterfaceTemplateRequestPoeTypeType3Type1):
            poe_type = self.poe_type.value
        else:
            poe_type = self.poe_type

        rf_role: Union[None, Unset, str]
        if isinstance(self.rf_role, Unset):
            rf_role = UNSET
        elif isinstance(self.rf_role, WritableInterfaceTemplateRequestWirelessRole):
            rf_role = self.rf_role.value
        elif isinstance(self.rf_role, WritableInterfaceTemplateRequestWirelessRole):
            rf_role = self.rf_role.value
        elif isinstance(self.rf_role, WritableInterfaceTemplateRequestWirelessRole):
            rf_role = self.rf_role.value
        else:
            rf_role = self.rf_role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if module_type is not UNSET:
            field_dict["module_type"] = module_type
        if label is not UNSET:
            field_dict["label"] = label
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if mgmt_only is not UNSET:
            field_dict["mgmt_only"] = mgmt_only
        if description is not UNSET:
            field_dict["description"] = description
        if bridge is not UNSET:
            field_dict["bridge"] = bridge
        if poe_mode is not UNSET:
            field_dict["poe_mode"] = poe_mode
        if poe_type is not UNSET:
            field_dict["poe_type"] = poe_type
        if rf_role is not UNSET:
            field_dict["rf_role"] = rf_role

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (None, str(self.name).encode(), "text/plain")

        type_ = (None, str(self.type_.value).encode(), "text/plain")

        device_type: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.device_type, Unset):
            device_type = UNSET
        elif isinstance(self.device_type, int):
            device_type = (None, str(self.device_type).encode(), "text/plain")
        elif isinstance(self.device_type, None):
            device_type = (None, str(self.device_type).encode(), "text/plain")
        elif isinstance(self.device_type, BriefDeviceTypeRequest):
            device_type = (None, json.dumps(self.device_type.to_dict()).encode(), "application/json")
        else:
            device_type = (None, str(self.device_type).encode(), "text/plain")

        module_type: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.module_type, Unset):
            module_type = UNSET
        elif isinstance(self.module_type, int):
            module_type = (None, str(self.module_type).encode(), "text/plain")
        elif isinstance(self.module_type, None):
            module_type = (None, str(self.module_type).encode(), "text/plain")
        elif isinstance(self.module_type, BriefModuleTypeRequest):
            module_type = (None, json.dumps(self.module_type.to_dict()).encode(), "application/json")
        else:
            module_type = (None, str(self.module_type).encode(), "text/plain")

        label = self.label if isinstance(self.label, Unset) else (None, str(self.label).encode(), "text/plain")

        enabled = self.enabled if isinstance(self.enabled, Unset) else (None, str(self.enabled).encode(), "text/plain")

        mgmt_only = (
            self.mgmt_only if isinstance(self.mgmt_only, Unset) else (None, str(self.mgmt_only).encode(), "text/plain")
        )

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        bridge: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.bridge, Unset):
            bridge = UNSET
        elif isinstance(self.bridge, int):
            bridge = (None, str(self.bridge).encode(), "text/plain")
        else:
            bridge = (None, str(self.bridge).encode(), "text/plain")

        poe_mode: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.poe_mode, Unset):
            poe_mode = UNSET
        elif isinstance(self.poe_mode, None):
            poe_mode = (None, str(self.poe_mode).encode(), "text/plain")
        elif isinstance(self.poe_mode, WritableInterfaceTemplateRequestPoeModeType1):
            poe_mode = (None, str(self.poe_mode.value).encode(), "text/plain")
        elif isinstance(self.poe_mode, None):
            poe_mode = (None, str(self.poe_mode).encode(), "text/plain")
        elif isinstance(self.poe_mode, WritableInterfaceTemplateRequestPoeModeType2Type1):
            poe_mode = (None, str(self.poe_mode.value).encode(), "text/plain")
        elif isinstance(self.poe_mode, None):
            poe_mode = (None, str(self.poe_mode).encode(), "text/plain")
        else:
            poe_mode = (None, str(self.poe_mode.value).encode(), "text/plain")

        poe_type: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.poe_type, Unset):
            poe_type = UNSET
        elif isinstance(self.poe_type, None):
            poe_type = (None, str(self.poe_type).encode(), "text/plain")
        elif isinstance(self.poe_type, WritableInterfaceTemplateRequestPoeTypeType1):
            poe_type = (None, str(self.poe_type.value).encode(), "text/plain")
        elif isinstance(self.poe_type, None):
            poe_type = (None, str(self.poe_type).encode(), "text/plain")
        elif isinstance(self.poe_type, WritableInterfaceTemplateRequestPoeTypeType2Type1):
            poe_type = (None, str(self.poe_type.value).encode(), "text/plain")
        elif isinstance(self.poe_type, None):
            poe_type = (None, str(self.poe_type).encode(), "text/plain")
        else:
            poe_type = (None, str(self.poe_type.value).encode(), "text/plain")

        rf_role: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.rf_role, Unset):
            rf_role = UNSET
        elif isinstance(self.rf_role, None):
            rf_role = (None, str(self.rf_role).encode(), "text/plain")
        elif isinstance(self.rf_role, WritableInterfaceTemplateRequestWirelessRole):
            rf_role = (None, str(self.rf_role.value).encode(), "text/plain")
        elif isinstance(self.rf_role, None):
            rf_role = (None, str(self.rf_role).encode(), "text/plain")
        elif isinstance(self.rf_role, WritableInterfaceTemplateRequestWirelessRole):
            rf_role = (None, str(self.rf_role.value).encode(), "text/plain")
        elif isinstance(self.rf_role, None):
            rf_role = (None, str(self.rf_role).encode(), "text/plain")
        else:
            rf_role = (None, str(self.rf_role.value).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if module_type is not UNSET:
            field_dict["module_type"] = module_type
        if label is not UNSET:
            field_dict["label"] = label
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if mgmt_only is not UNSET:
            field_dict["mgmt_only"] = mgmt_only
        if description is not UNSET:
            field_dict["description"] = description
        if bridge is not UNSET:
            field_dict["bridge"] = bridge
        if poe_mode is not UNSET:
            field_dict["poe_mode"] = poe_mode
        if poe_type is not UNSET:
            field_dict["poe_type"] = poe_type
        if rf_role is not UNSET:
            field_dict["rf_role"] = rf_role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_device_type_request import BriefDeviceTypeRequest
        from ..models.brief_module_type_request import BriefModuleTypeRequest

        d = dict(src_dict)
        name = d.pop("name")

        type_ = WritableInterfaceTemplateRequestType(d.pop("type"))

        def _parse_device_type(data: object) -> Union["BriefDeviceTypeRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_type_type_1_type_1 = BriefDeviceTypeRequest.from_dict(data)

                return device_type_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDeviceTypeRequest", None, Unset, int], data)

        device_type = _parse_device_type(d.pop("device_type", UNSET))

        def _parse_module_type(data: object) -> Union["BriefModuleTypeRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                module_type_type_1_type_1 = BriefModuleTypeRequest.from_dict(data)

                return module_type_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefModuleTypeRequest", None, Unset, int], data)

        module_type = _parse_module_type(d.pop("module_type", UNSET))

        label = d.pop("label", UNSET)

        enabled = d.pop("enabled", UNSET)

        mgmt_only = d.pop("mgmt_only", UNSET)

        description = d.pop("description", UNSET)

        def _parse_bridge(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bridge = _parse_bridge(d.pop("bridge", UNSET))

        def _parse_poe_mode(
            data: object,
        ) -> Union[
            None,
            Unset,
            WritableInterfaceTemplateRequestPoeModeType1,
            WritableInterfaceTemplateRequestPoeModeType2Type1,
            WritableInterfaceTemplateRequestPoeModeType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                poe_mode_type_1 = WritableInterfaceTemplateRequestPoeModeType1(data)

                return poe_mode_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                poe_mode_type_2_type_1 = WritableInterfaceTemplateRequestPoeModeType2Type1(data)

                return poe_mode_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                poe_mode_type_3_type_1 = WritableInterfaceTemplateRequestPoeModeType3Type1(data)

                return poe_mode_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    WritableInterfaceTemplateRequestPoeModeType1,
                    WritableInterfaceTemplateRequestPoeModeType2Type1,
                    WritableInterfaceTemplateRequestPoeModeType3Type1,
                ],
                data,
            )

        poe_mode = _parse_poe_mode(d.pop("poe_mode", UNSET))

        def _parse_poe_type(
            data: object,
        ) -> Union[
            None,
            Unset,
            WritableInterfaceTemplateRequestPoeTypeType1,
            WritableInterfaceTemplateRequestPoeTypeType2Type1,
            WritableInterfaceTemplateRequestPoeTypeType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                poe_type_type_1 = WritableInterfaceTemplateRequestPoeTypeType1(data)

                return poe_type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                poe_type_type_2_type_1 = WritableInterfaceTemplateRequestPoeTypeType2Type1(data)

                return poe_type_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                poe_type_type_3_type_1 = WritableInterfaceTemplateRequestPoeTypeType3Type1(data)

                return poe_type_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    WritableInterfaceTemplateRequestPoeTypeType1,
                    WritableInterfaceTemplateRequestPoeTypeType2Type1,
                    WritableInterfaceTemplateRequestPoeTypeType3Type1,
                ],
                data,
            )

        poe_type = _parse_poe_type(d.pop("poe_type", UNSET))

        def _parse_rf_role(data: object) -> Union[None, Unset, WritableInterfaceTemplateRequestWirelessRole]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rf_role_type_1 = WritableInterfaceTemplateRequestWirelessRole(data)

                return rf_role_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rf_role_type_2_type_1 = WritableInterfaceTemplateRequestWirelessRole(data)

                return rf_role_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rf_role_type_3_type_1 = WritableInterfaceTemplateRequestWirelessRole(data)

                return rf_role_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, WritableInterfaceTemplateRequestWirelessRole], data)

        rf_role = _parse_rf_role(d.pop("rf_role", UNSET))

        writable_interface_template_request = cls(
            name=name,
            type_=type_,
            device_type=device_type,
            module_type=module_type,
            label=label,
            enabled=enabled,
            mgmt_only=mgmt_only,
            description=description,
            bridge=bridge,
            poe_mode=poe_mode,
            poe_type=poe_type,
            rf_role=rf_role,
        )

        writable_interface_template_request.additional_properties = d
        return writable_interface_template_request

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
