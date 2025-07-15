import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_writable_interface_request_duplex_type_1 import PatchedWritableInterfaceRequestDuplexType1
from ..models.patched_writable_interface_request_duplex_type_2_type_1 import (
    PatchedWritableInterfaceRequestDuplexType2Type1,
)
from ..models.patched_writable_interface_request_duplex_type_3_type_1 import (
    PatchedWritableInterfaceRequestDuplexType3Type1,
)
from ..models.patched_writable_interface_request_mode_type_1 import PatchedWritableInterfaceRequestModeType1
from ..models.patched_writable_interface_request_mode_type_2_type_1 import PatchedWritableInterfaceRequestModeType2Type1
from ..models.patched_writable_interface_request_mode_type_3_type_1 import PatchedWritableInterfaceRequestModeType3Type1
from ..models.patched_writable_interface_request_poe_mode_type_1 import PatchedWritableInterfaceRequestPoeModeType1
from ..models.patched_writable_interface_request_poe_mode_type_2_type_1 import (
    PatchedWritableInterfaceRequestPoeModeType2Type1,
)
from ..models.patched_writable_interface_request_poe_mode_type_3_type_1 import (
    PatchedWritableInterfaceRequestPoeModeType3Type1,
)
from ..models.patched_writable_interface_request_poe_type_type_1 import PatchedWritableInterfaceRequestPoeTypeType1
from ..models.patched_writable_interface_request_poe_type_type_2_type_1 import (
    PatchedWritableInterfaceRequestPoeTypeType2Type1,
)
from ..models.patched_writable_interface_request_poe_type_type_3_type_1 import (
    PatchedWritableInterfaceRequestPoeTypeType3Type1,
)
from ..models.patched_writable_interface_request_type import PatchedWritableInterfaceRequestType
from ..models.patched_writable_interface_request_wireless_channel import PatchedWritableInterfaceRequestWirelessChannel
from ..models.patched_writable_interface_request_wireless_role import PatchedWritableInterfaceRequestWirelessRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_request import BriefDeviceRequest
    from ..models.brief_mac_address_request import BriefMACAddressRequest
    from ..models.brief_module_request import BriefModuleRequest
    from ..models.brief_vlan_request import BriefVLANRequest
    from ..models.brief_vlan_translation_policy_request import BriefVLANTranslationPolicyRequest
    from ..models.brief_vrf_request import BriefVRFRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_writable_interface_request_custom_fields import PatchedWritableInterfaceRequestCustomFields


T = TypeVar("T", bound="PatchedWritableInterfaceRequest")


@_attrs_define
class PatchedWritableInterfaceRequest:
    """Adds support for custom fields and tags.

    Attributes:
        device (Union['BriefDeviceRequest', Unset, int]):
        vdcs (Union[Unset, list[int]]):
        module (Union['BriefModuleRequest', None, Unset, int]):
        name (Union[Unset, str]):
        label (Union[Unset, str]): Physical label
        type_ (Union[Unset, PatchedWritableInterfaceRequestType]): * `virtual` - Virtual
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
        enabled (Union[Unset, bool]):
        parent (Union[None, Unset, int]):
        bridge (Union[None, Unset, int]):
        lag (Union[None, Unset, int]):
        mtu (Union[None, Unset, int]):
        primary_mac_address (Union['BriefMACAddressRequest', None, Unset, int]):
        speed (Union[None, Unset, int]):
        duplex (Union[None, PatchedWritableInterfaceRequestDuplexType1, PatchedWritableInterfaceRequestDuplexType2Type1,
            PatchedWritableInterfaceRequestDuplexType3Type1, Unset]): * `half` - Half
            * `full` - Full
            * `auto` - Auto
        wwn (Union[None, Unset, str]):
        mgmt_only (Union[Unset, bool]): This interface is used only for out-of-band management
        description (Union[Unset, str]):
        mode (Union[None, PatchedWritableInterfaceRequestModeType1, PatchedWritableInterfaceRequestModeType2Type1,
            PatchedWritableInterfaceRequestModeType3Type1, Unset]): IEEE 802.1Q tagging strategy

            * `access` - Access
            * `tagged` - Tagged
            * `tagged-all` - Tagged (All)
            * `q-in-q` - Q-in-Q (802.1ad)
        rf_role (Union[None, PatchedWritableInterfaceRequestWirelessRole, Unset]): * `ap` - Access point
            * `station` - Station
        rf_channel (Union[None, PatchedWritableInterfaceRequestWirelessChannel, Unset]): * `2.4g-1-2412-22` - 1 (2412
            MHz)
            * `2.4g-2-2417-22` - 2 (2417 MHz)
            * `2.4g-3-2422-22` - 3 (2422 MHz)
            * `2.4g-4-2427-22` - 4 (2427 MHz)
            * `2.4g-5-2432-22` - 5 (2432 MHz)
            * `2.4g-6-2437-22` - 6 (2437 MHz)
            * `2.4g-7-2442-22` - 7 (2442 MHz)
            * `2.4g-8-2447-22` - 8 (2447 MHz)
            * `2.4g-9-2452-22` - 9 (2452 MHz)
            * `2.4g-10-2457-22` - 10 (2457 MHz)
            * `2.4g-11-2462-22` - 11 (2462 MHz)
            * `2.4g-12-2467-22` - 12 (2467 MHz)
            * `2.4g-13-2472-22` - 13 (2472 MHz)
            * `5g-32-5160-20` - 32 (5160/20 MHz)
            * `5g-34-5170-40` - 34 (5170/40 MHz)
            * `5g-36-5180-20` - 36 (5180/20 MHz)
            * `5g-38-5190-40` - 38 (5190/40 MHz)
            * `5g-40-5200-20` - 40 (5200/20 MHz)
            * `5g-42-5210-80` - 42 (5210/80 MHz)
            * `5g-44-5220-20` - 44 (5220/20 MHz)
            * `5g-46-5230-40` - 46 (5230/40 MHz)
            * `5g-48-5240-20` - 48 (5240/20 MHz)
            * `5g-50-5250-160` - 50 (5250/160 MHz)
            * `5g-52-5260-20` - 52 (5260/20 MHz)
            * `5g-54-5270-40` - 54 (5270/40 MHz)
            * `5g-56-5280-20` - 56 (5280/20 MHz)
            * `5g-58-5290-80` - 58 (5290/80 MHz)
            * `5g-60-5300-20` - 60 (5300/20 MHz)
            * `5g-62-5310-40` - 62 (5310/40 MHz)
            * `5g-64-5320-20` - 64 (5320/20 MHz)
            * `5g-100-5500-20` - 100 (5500/20 MHz)
            * `5g-102-5510-40` - 102 (5510/40 MHz)
            * `5g-104-5520-20` - 104 (5520/20 MHz)
            * `5g-106-5530-80` - 106 (5530/80 MHz)
            * `5g-108-5540-20` - 108 (5540/20 MHz)
            * `5g-110-5550-40` - 110 (5550/40 MHz)
            * `5g-112-5560-20` - 112 (5560/20 MHz)
            * `5g-114-5570-160` - 114 (5570/160 MHz)
            * `5g-116-5580-20` - 116 (5580/20 MHz)
            * `5g-118-5590-40` - 118 (5590/40 MHz)
            * `5g-120-5600-20` - 120 (5600/20 MHz)
            * `5g-122-5610-80` - 122 (5610/80 MHz)
            * `5g-124-5620-20` - 124 (5620/20 MHz)
            * `5g-126-5630-40` - 126 (5630/40 MHz)
            * `5g-128-5640-20` - 128 (5640/20 MHz)
            * `5g-132-5660-20` - 132 (5660/20 MHz)
            * `5g-134-5670-40` - 134 (5670/40 MHz)
            * `5g-136-5680-20` - 136 (5680/20 MHz)
            * `5g-138-5690-80` - 138 (5690/80 MHz)
            * `5g-140-5700-20` - 140 (5700/20 MHz)
            * `5g-142-5710-40` - 142 (5710/40 MHz)
            * `5g-144-5720-20` - 144 (5720/20 MHz)
            * `5g-149-5745-20` - 149 (5745/20 MHz)
            * `5g-151-5755-40` - 151 (5755/40 MHz)
            * `5g-153-5765-20` - 153 (5765/20 MHz)
            * `5g-155-5775-80` - 155 (5775/80 MHz)
            * `5g-157-5785-20` - 157 (5785/20 MHz)
            * `5g-159-5795-40` - 159 (5795/40 MHz)
            * `5g-161-5805-20` - 161 (5805/20 MHz)
            * `5g-163-5815-160` - 163 (5815/160 MHz)
            * `5g-165-5825-20` - 165 (5825/20 MHz)
            * `5g-167-5835-40` - 167 (5835/40 MHz)
            * `5g-169-5845-20` - 169 (5845/20 MHz)
            * `5g-171-5855-80` - 171 (5855/80 MHz)
            * `5g-173-5865-20` - 173 (5865/20 MHz)
            * `5g-175-5875-40` - 175 (5875/40 MHz)
            * `5g-177-5885-20` - 177 (5885/20 MHz)
            * `6g-1-5955-20` - 1 (5955/20 MHz)
            * `6g-3-5965-40` - 3 (5965/40 MHz)
            * `6g-5-5975-20` - 5 (5975/20 MHz)
            * `6g-7-5985-80` - 7 (5985/80 MHz)
            * `6g-9-5995-20` - 9 (5995/20 MHz)
            * `6g-11-6005-40` - 11 (6005/40 MHz)
            * `6g-13-6015-20` - 13 (6015/20 MHz)
            * `6g-15-6025-160` - 15 (6025/160 MHz)
            * `6g-17-6035-20` - 17 (6035/20 MHz)
            * `6g-19-6045-40` - 19 (6045/40 MHz)
            * `6g-21-6055-20` - 21 (6055/20 MHz)
            * `6g-23-6065-80` - 23 (6065/80 MHz)
            * `6g-25-6075-20` - 25 (6075/20 MHz)
            * `6g-27-6085-40` - 27 (6085/40 MHz)
            * `6g-29-6095-20` - 29 (6095/20 MHz)
            * `6g-31-6105-320` - 31 (6105/320 MHz)
            * `6g-33-6115-20` - 33 (6115/20 MHz)
            * `6g-35-6125-40` - 35 (6125/40 MHz)
            * `6g-37-6135-20` - 37 (6135/20 MHz)
            * `6g-39-6145-80` - 39 (6145/80 MHz)
            * `6g-41-6155-20` - 41 (6155/20 MHz)
            * `6g-43-6165-40` - 43 (6165/40 MHz)
            * `6g-45-6175-20` - 45 (6175/20 MHz)
            * `6g-47-6185-160` - 47 (6185/160 MHz)
            * `6g-49-6195-20` - 49 (6195/20 MHz)
            * `6g-51-6205-40` - 51 (6205/40 MHz)
            * `6g-53-6215-20` - 53 (6215/20 MHz)
            * `6g-55-6225-80` - 55 (6225/80 MHz)
            * `6g-57-6235-20` - 57 (6235/20 MHz)
            * `6g-59-6245-40` - 59 (6245/40 MHz)
            * `6g-61-6255-20` - 61 (6255/20 MHz)
            * `6g-65-6275-20` - 65 (6275/20 MHz)
            * `6g-67-6285-40` - 67 (6285/40 MHz)
            * `6g-69-6295-20` - 69 (6295/20 MHz)
            * `6g-71-6305-80` - 71 (6305/80 MHz)
            * `6g-73-6315-20` - 73 (6315/20 MHz)
            * `6g-75-6325-40` - 75 (6325/40 MHz)
            * `6g-77-6335-20` - 77 (6335/20 MHz)
            * `6g-79-6345-160` - 79 (6345/160 MHz)
            * `6g-81-6355-20` - 81 (6355/20 MHz)
            * `6g-83-6365-40` - 83 (6365/40 MHz)
            * `6g-85-6375-20` - 85 (6375/20 MHz)
            * `6g-87-6385-80` - 87 (6385/80 MHz)
            * `6g-89-6395-20` - 89 (6395/20 MHz)
            * `6g-91-6405-40` - 91 (6405/40 MHz)
            * `6g-93-6415-20` - 93 (6415/20 MHz)
            * `6g-95-6425-320` - 95 (6425/320 MHz)
            * `6g-97-6435-20` - 97 (6435/20 MHz)
            * `6g-99-6445-40` - 99 (6445/40 MHz)
            * `6g-101-6455-20` - 101 (6455/20 MHz)
            * `6g-103-6465-80` - 103 (6465/80 MHz)
            * `6g-105-6475-20` - 105 (6475/20 MHz)
            * `6g-107-6485-40` - 107 (6485/40 MHz)
            * `6g-109-6495-20` - 109 (6495/20 MHz)
            * `6g-111-6505-160` - 111 (6505/160 MHz)
            * `6g-113-6515-20` - 113 (6515/20 MHz)
            * `6g-115-6525-40` - 115 (6525/40 MHz)
            * `6g-117-6535-20` - 117 (6535/20 MHz)
            * `6g-119-6545-80` - 119 (6545/80 MHz)
            * `6g-121-6555-20` - 121 (6555/20 MHz)
            * `6g-123-6565-40` - 123 (6565/40 MHz)
            * `6g-125-6575-20` - 125 (6575/20 MHz)
            * `6g-129-6595-20` - 129 (6595/20 MHz)
            * `6g-131-6605-40` - 131 (6605/40 MHz)
            * `6g-133-6615-20` - 133 (6615/20 MHz)
            * `6g-135-6625-80` - 135 (6625/80 MHz)
            * `6g-137-6635-20` - 137 (6635/20 MHz)
            * `6g-139-6645-40` - 139 (6645/40 MHz)
            * `6g-141-6655-20` - 141 (6655/20 MHz)
            * `6g-143-6665-160` - 143 (6665/160 MHz)
            * `6g-145-6675-20` - 145 (6675/20 MHz)
            * `6g-147-6685-40` - 147 (6685/40 MHz)
            * `6g-149-6695-20` - 149 (6695/20 MHz)
            * `6g-151-6705-80` - 151 (6705/80 MHz)
            * `6g-153-6715-20` - 153 (6715/20 MHz)
            * `6g-155-6725-40` - 155 (6725/40 MHz)
            * `6g-157-6735-20` - 157 (6735/20 MHz)
            * `6g-159-6745-320` - 159 (6745/320 MHz)
            * `6g-161-6755-20` - 161 (6755/20 MHz)
            * `6g-163-6765-40` - 163 (6765/40 MHz)
            * `6g-165-6775-20` - 165 (6775/20 MHz)
            * `6g-167-6785-80` - 167 (6785/80 MHz)
            * `6g-169-6795-20` - 169 (6795/20 MHz)
            * `6g-171-6805-40` - 171 (6805/40 MHz)
            * `6g-173-6815-20` - 173 (6815/20 MHz)
            * `6g-175-6825-160` - 175 (6825/160 MHz)
            * `6g-177-6835-20` - 177 (6835/20 MHz)
            * `6g-179-6845-40` - 179 (6845/40 MHz)
            * `6g-181-6855-20` - 181 (6855/20 MHz)
            * `6g-183-6865-80` - 183 (6865/80 MHz)
            * `6g-185-6875-20` - 185 (6875/20 MHz)
            * `6g-187-6885-40` - 187 (6885/40 MHz)
            * `6g-189-6895-20` - 189 (6895/20 MHz)
            * `6g-193-6915-20` - 193 (6915/20 MHz)
            * `6g-195-6925-40` - 195 (6925/40 MHz)
            * `6g-197-6935-20` - 197 (6935/20 MHz)
            * `6g-199-6945-80` - 199 (6945/80 MHz)
            * `6g-201-6955-20` - 201 (6955/20 MHz)
            * `6g-203-6965-40` - 203 (6965/40 MHz)
            * `6g-205-6975-20` - 205 (6975/20 MHz)
            * `6g-207-6985-160` - 207 (6985/160 MHz)
            * `6g-209-6995-20` - 209 (6995/20 MHz)
            * `6g-211-7005-40` - 211 (7005/40 MHz)
            * `6g-213-7015-20` - 213 (7015/20 MHz)
            * `6g-215-7025-80` - 215 (7025/80 MHz)
            * `6g-217-7035-20` - 217 (7035/20 MHz)
            * `6g-219-7045-40` - 219 (7045/40 MHz)
            * `6g-221-7055-20` - 221 (7055/20 MHz)
            * `6g-225-7075-20` - 225 (7075/20 MHz)
            * `6g-227-7085-40` - 227 (7085/40 MHz)
            * `6g-229-7095-20` - 229 (7095/20 MHz)
            * `6g-233-7115-20` - 233 (7115/20 MHz)
            * `60g-1-58320-2160` - 1 (58.32/2.16 GHz)
            * `60g-2-60480-2160` - 2 (60.48/2.16 GHz)
            * `60g-3-62640-2160` - 3 (62.64/2.16 GHz)
            * `60g-4-64800-2160` - 4 (64.80/2.16 GHz)
            * `60g-5-66960-2160` - 5 (66.96/2.16 GHz)
            * `60g-6-69120-2160` - 6 (69.12/2.16 GHz)
            * `60g-9-59400-4320` - 9 (59.40/4.32 GHz)
            * `60g-10-61560-4320` - 10 (61.56/4.32 GHz)
            * `60g-11-63720-4320` - 11 (63.72/4.32 GHz)
            * `60g-12-65880-4320` - 12 (65.88/4.32 GHz)
            * `60g-13-68040-4320` - 13 (68.04/4.32 GHz)
            * `60g-17-60480-6480` - 17 (60.48/6.48 GHz)
            * `60g-18-62640-6480` - 18 (62.64/6.48 GHz)
            * `60g-19-64800-6480` - 19 (64.80/6.48 GHz)
            * `60g-20-66960-6480` - 20 (66.96/6.48 GHz)
            * `60g-25-61560-6480` - 25 (61.56/8.64 GHz)
            * `60g-26-63720-6480` - 26 (63.72/8.64 GHz)
            * `60g-27-65880-6480` - 27 (65.88/8.64 GHz)
        poe_mode (Union[None, PatchedWritableInterfaceRequestPoeModeType1,
            PatchedWritableInterfaceRequestPoeModeType2Type1, PatchedWritableInterfaceRequestPoeModeType3Type1, Unset]): *
            `pd` - PD
            * `pse` - PSE
        poe_type (Union[None, PatchedWritableInterfaceRequestPoeTypeType1,
            PatchedWritableInterfaceRequestPoeTypeType2Type1, PatchedWritableInterfaceRequestPoeTypeType3Type1, Unset]): *
            `type1-ieee802.3af` - 802.3af (Type 1)
            * `type2-ieee802.3at` - 802.3at (Type 2)
            * `type3-ieee802.3bt` - 802.3bt (Type 3)
            * `type4-ieee802.3bt` - 802.3bt (Type 4)
            * `passive-24v-2pair` - Passive 24V (2-pair)
            * `passive-24v-4pair` - Passive 24V (4-pair)
            * `passive-48v-2pair` - Passive 48V (2-pair)
            * `passive-48v-4pair` - Passive 48V (4-pair)
        rf_channel_frequency (Union[None, Unset, float]): Populated by selected channel (if set)
        rf_channel_width (Union[None, Unset, float]): Populated by selected channel (if set)
        tx_power (Union[None, Unset, int]):
        untagged_vlan (Union['BriefVLANRequest', None, Unset, int]):
        tagged_vlans (Union[Unset, list[int]]):
        qinq_svlan (Union['BriefVLANRequest', None, Unset, int]):
        vlan_translation_policy (Union['BriefVLANTranslationPolicyRequest', None, Unset, int]):
        mark_connected (Union[Unset, bool]): Treat as if a cable is connected
        wireless_lans (Union[Unset, list[int]]):
        vrf (Union['BriefVRFRequest', None, Unset, int]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedWritableInterfaceRequestCustomFields]):
    """

    device: Union["BriefDeviceRequest", Unset, int] = UNSET
    vdcs: Union[Unset, list[int]] = UNSET
    module: Union["BriefModuleRequest", None, Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    type_: Union[Unset, PatchedWritableInterfaceRequestType] = UNSET
    enabled: Union[Unset, bool] = UNSET
    parent: Union[None, Unset, int] = UNSET
    bridge: Union[None, Unset, int] = UNSET
    lag: Union[None, Unset, int] = UNSET
    mtu: Union[None, Unset, int] = UNSET
    primary_mac_address: Union["BriefMACAddressRequest", None, Unset, int] = UNSET
    speed: Union[None, Unset, int] = UNSET
    duplex: Union[
        None,
        PatchedWritableInterfaceRequestDuplexType1,
        PatchedWritableInterfaceRequestDuplexType2Type1,
        PatchedWritableInterfaceRequestDuplexType3Type1,
        Unset,
    ] = UNSET
    wwn: Union[None, Unset, str] = UNSET
    mgmt_only: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    mode: Union[
        None,
        PatchedWritableInterfaceRequestModeType1,
        PatchedWritableInterfaceRequestModeType2Type1,
        PatchedWritableInterfaceRequestModeType3Type1,
        Unset,
    ] = UNSET
    rf_role: Union[None, PatchedWritableInterfaceRequestWirelessRole, Unset] = UNSET
    rf_channel: Union[None, PatchedWritableInterfaceRequestWirelessChannel, Unset] = UNSET
    poe_mode: Union[
        None,
        PatchedWritableInterfaceRequestPoeModeType1,
        PatchedWritableInterfaceRequestPoeModeType2Type1,
        PatchedWritableInterfaceRequestPoeModeType3Type1,
        Unset,
    ] = UNSET
    poe_type: Union[
        None,
        PatchedWritableInterfaceRequestPoeTypeType1,
        PatchedWritableInterfaceRequestPoeTypeType2Type1,
        PatchedWritableInterfaceRequestPoeTypeType3Type1,
        Unset,
    ] = UNSET
    rf_channel_frequency: Union[None, Unset, float] = UNSET
    rf_channel_width: Union[None, Unset, float] = UNSET
    tx_power: Union[None, Unset, int] = UNSET
    untagged_vlan: Union["BriefVLANRequest", None, Unset, int] = UNSET
    tagged_vlans: Union[Unset, list[int]] = UNSET
    qinq_svlan: Union["BriefVLANRequest", None, Unset, int] = UNSET
    vlan_translation_policy: Union["BriefVLANTranslationPolicyRequest", None, Unset, int] = UNSET
    mark_connected: Union[Unset, bool] = UNSET
    wireless_lans: Union[Unset, list[int]] = UNSET
    vrf: Union["BriefVRFRequest", None, Unset, int] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedWritableInterfaceRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device_request import BriefDeviceRequest
        from ..models.brief_mac_address_request import BriefMACAddressRequest
        from ..models.brief_module_request import BriefModuleRequest
        from ..models.brief_vlan_request import BriefVLANRequest
        from ..models.brief_vlan_translation_policy_request import BriefVLANTranslationPolicyRequest
        from ..models.brief_vrf_request import BriefVRFRequest

        device: Union[Unset, dict[str, Any], int]
        if isinstance(self.device, Unset):
            device = UNSET
        elif isinstance(self.device, BriefDeviceRequest):
            device = self.device.to_dict()
        else:
            device = self.device

        vdcs: Union[Unset, list[int]] = UNSET
        if not isinstance(self.vdcs, Unset):
            vdcs = self.vdcs

        module: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.module, Unset):
            module = UNSET
        elif isinstance(self.module, BriefModuleRequest):
            module = self.module.to_dict()
        else:
            module = self.module

        name = self.name

        label = self.label

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

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

        lag: Union[None, Unset, int]
        if isinstance(self.lag, Unset):
            lag = UNSET
        else:
            lag = self.lag

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

        speed: Union[None, Unset, int]
        if isinstance(self.speed, Unset):
            speed = UNSET
        else:
            speed = self.speed

        duplex: Union[None, Unset, str]
        if isinstance(self.duplex, Unset):
            duplex = UNSET
        elif isinstance(self.duplex, PatchedWritableInterfaceRequestDuplexType1):
            duplex = self.duplex.value
        elif isinstance(self.duplex, PatchedWritableInterfaceRequestDuplexType2Type1):
            duplex = self.duplex.value
        elif isinstance(self.duplex, PatchedWritableInterfaceRequestDuplexType3Type1):
            duplex = self.duplex.value
        else:
            duplex = self.duplex

        wwn: Union[None, Unset, str]
        if isinstance(self.wwn, Unset):
            wwn = UNSET
        else:
            wwn = self.wwn

        mgmt_only = self.mgmt_only

        description = self.description

        mode: Union[None, Unset, str]
        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, PatchedWritableInterfaceRequestModeType1):
            mode = self.mode.value
        elif isinstance(self.mode, PatchedWritableInterfaceRequestModeType2Type1):
            mode = self.mode.value
        elif isinstance(self.mode, PatchedWritableInterfaceRequestModeType3Type1):
            mode = self.mode.value
        else:
            mode = self.mode

        rf_role: Union[None, Unset, str]
        if isinstance(self.rf_role, Unset):
            rf_role = UNSET
        elif isinstance(self.rf_role, PatchedWritableInterfaceRequestWirelessRole):
            rf_role = self.rf_role.value
        elif isinstance(self.rf_role, PatchedWritableInterfaceRequestWirelessRole):
            rf_role = self.rf_role.value
        elif isinstance(self.rf_role, PatchedWritableInterfaceRequestWirelessRole):
            rf_role = self.rf_role.value
        else:
            rf_role = self.rf_role

        rf_channel: Union[None, Unset, str]
        if isinstance(self.rf_channel, Unset):
            rf_channel = UNSET
        elif isinstance(self.rf_channel, PatchedWritableInterfaceRequestWirelessChannel):
            rf_channel = self.rf_channel.value
        elif isinstance(self.rf_channel, PatchedWritableInterfaceRequestWirelessChannel):
            rf_channel = self.rf_channel.value
        elif isinstance(self.rf_channel, PatchedWritableInterfaceRequestWirelessChannel):
            rf_channel = self.rf_channel.value
        else:
            rf_channel = self.rf_channel

        poe_mode: Union[None, Unset, str]
        if isinstance(self.poe_mode, Unset):
            poe_mode = UNSET
        elif isinstance(self.poe_mode, PatchedWritableInterfaceRequestPoeModeType1):
            poe_mode = self.poe_mode.value
        elif isinstance(self.poe_mode, PatchedWritableInterfaceRequestPoeModeType2Type1):
            poe_mode = self.poe_mode.value
        elif isinstance(self.poe_mode, PatchedWritableInterfaceRequestPoeModeType3Type1):
            poe_mode = self.poe_mode.value
        else:
            poe_mode = self.poe_mode

        poe_type: Union[None, Unset, str]
        if isinstance(self.poe_type, Unset):
            poe_type = UNSET
        elif isinstance(self.poe_type, PatchedWritableInterfaceRequestPoeTypeType1):
            poe_type = self.poe_type.value
        elif isinstance(self.poe_type, PatchedWritableInterfaceRequestPoeTypeType2Type1):
            poe_type = self.poe_type.value
        elif isinstance(self.poe_type, PatchedWritableInterfaceRequestPoeTypeType3Type1):
            poe_type = self.poe_type.value
        else:
            poe_type = self.poe_type

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

        mark_connected = self.mark_connected

        wireless_lans: Union[Unset, list[int]] = UNSET
        if not isinstance(self.wireless_lans, Unset):
            wireless_lans = self.wireless_lans

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
        field_dict.update({})
        if device is not UNSET:
            field_dict["device"] = device
        if vdcs is not UNSET:
            field_dict["vdcs"] = vdcs
        if module is not UNSET:
            field_dict["module"] = module
        if name is not UNSET:
            field_dict["name"] = name
        if label is not UNSET:
            field_dict["label"] = label
        if type_ is not UNSET:
            field_dict["type"] = type_
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

    def to_multipart(self) -> dict[str, Any]:
        device: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.device, Unset):
            device = UNSET
        elif isinstance(self.device, int):
            device = (None, str(self.device).encode(), "text/plain")
        else:
            device = (None, json.dumps(self.device.to_dict()).encode(), "application/json")

        vdcs: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.vdcs, Unset):
            _temp_vdcs = self.vdcs
            vdcs = (None, json.dumps(_temp_vdcs).encode(), "application/json")

        module: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.module, Unset):
            module = UNSET
        elif isinstance(self.module, int):
            module = (None, str(self.module).encode(), "text/plain")
        elif isinstance(self.module, None):
            module = (None, str(self.module).encode(), "text/plain")
        elif isinstance(self.module, BriefModuleRequest):
            module = (None, json.dumps(self.module.to_dict()).encode(), "application/json")
        else:
            module = (None, str(self.module).encode(), "text/plain")

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        label = self.label if isinstance(self.label, Unset) else (None, str(self.label).encode(), "text/plain")

        type_: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = (None, str(self.type_.value).encode(), "text/plain")

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

        lag: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.lag, Unset):
            lag = UNSET
        elif isinstance(self.lag, int):
            lag = (None, str(self.lag).encode(), "text/plain")
        else:
            lag = (None, str(self.lag).encode(), "text/plain")

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

        speed: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.speed, Unset):
            speed = UNSET
        elif isinstance(self.speed, int):
            speed = (None, str(self.speed).encode(), "text/plain")
        else:
            speed = (None, str(self.speed).encode(), "text/plain")

        duplex: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.duplex, Unset):
            duplex = UNSET
        elif isinstance(self.duplex, None):
            duplex = (None, str(self.duplex).encode(), "text/plain")
        elif isinstance(self.duplex, PatchedWritableInterfaceRequestDuplexType1):
            duplex = (None, str(self.duplex.value).encode(), "text/plain")
        elif isinstance(self.duplex, None):
            duplex = (None, str(self.duplex).encode(), "text/plain")
        elif isinstance(self.duplex, PatchedWritableInterfaceRequestDuplexType2Type1):
            duplex = (None, str(self.duplex.value).encode(), "text/plain")
        elif isinstance(self.duplex, None):
            duplex = (None, str(self.duplex).encode(), "text/plain")
        else:
            duplex = (None, str(self.duplex.value).encode(), "text/plain")

        wwn: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.wwn, Unset):
            wwn = UNSET
        elif isinstance(self.wwn, str):
            wwn = (None, str(self.wwn).encode(), "text/plain")
        else:
            wwn = (None, str(self.wwn).encode(), "text/plain")

        mgmt_only = (
            self.mgmt_only if isinstance(self.mgmt_only, Unset) else (None, str(self.mgmt_only).encode(), "text/plain")
        )

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
        elif isinstance(self.mode, PatchedWritableInterfaceRequestModeType1):
            mode = (None, str(self.mode.value).encode(), "text/plain")
        elif isinstance(self.mode, None):
            mode = (None, str(self.mode).encode(), "text/plain")
        elif isinstance(self.mode, PatchedWritableInterfaceRequestModeType2Type1):
            mode = (None, str(self.mode.value).encode(), "text/plain")
        elif isinstance(self.mode, None):
            mode = (None, str(self.mode).encode(), "text/plain")
        else:
            mode = (None, str(self.mode.value).encode(), "text/plain")

        rf_role: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.rf_role, Unset):
            rf_role = UNSET
        elif isinstance(self.rf_role, None):
            rf_role = (None, str(self.rf_role).encode(), "text/plain")
        elif isinstance(self.rf_role, PatchedWritableInterfaceRequestWirelessRole):
            rf_role = (None, str(self.rf_role.value).encode(), "text/plain")
        elif isinstance(self.rf_role, None):
            rf_role = (None, str(self.rf_role).encode(), "text/plain")
        elif isinstance(self.rf_role, PatchedWritableInterfaceRequestWirelessRole):
            rf_role = (None, str(self.rf_role.value).encode(), "text/plain")
        elif isinstance(self.rf_role, None):
            rf_role = (None, str(self.rf_role).encode(), "text/plain")
        else:
            rf_role = (None, str(self.rf_role.value).encode(), "text/plain")

        rf_channel: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.rf_channel, Unset):
            rf_channel = UNSET
        elif isinstance(self.rf_channel, None):
            rf_channel = (None, str(self.rf_channel).encode(), "text/plain")
        elif isinstance(self.rf_channel, PatchedWritableInterfaceRequestWirelessChannel):
            rf_channel = (None, str(self.rf_channel.value).encode(), "text/plain")
        elif isinstance(self.rf_channel, None):
            rf_channel = (None, str(self.rf_channel).encode(), "text/plain")
        elif isinstance(self.rf_channel, PatchedWritableInterfaceRequestWirelessChannel):
            rf_channel = (None, str(self.rf_channel.value).encode(), "text/plain")
        elif isinstance(self.rf_channel, None):
            rf_channel = (None, str(self.rf_channel).encode(), "text/plain")
        else:
            rf_channel = (None, str(self.rf_channel.value).encode(), "text/plain")

        poe_mode: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.poe_mode, Unset):
            poe_mode = UNSET
        elif isinstance(self.poe_mode, None):
            poe_mode = (None, str(self.poe_mode).encode(), "text/plain")
        elif isinstance(self.poe_mode, PatchedWritableInterfaceRequestPoeModeType1):
            poe_mode = (None, str(self.poe_mode.value).encode(), "text/plain")
        elif isinstance(self.poe_mode, None):
            poe_mode = (None, str(self.poe_mode).encode(), "text/plain")
        elif isinstance(self.poe_mode, PatchedWritableInterfaceRequestPoeModeType2Type1):
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
        elif isinstance(self.poe_type, PatchedWritableInterfaceRequestPoeTypeType1):
            poe_type = (None, str(self.poe_type.value).encode(), "text/plain")
        elif isinstance(self.poe_type, None):
            poe_type = (None, str(self.poe_type).encode(), "text/plain")
        elif isinstance(self.poe_type, PatchedWritableInterfaceRequestPoeTypeType2Type1):
            poe_type = (None, str(self.poe_type.value).encode(), "text/plain")
        elif isinstance(self.poe_type, None):
            poe_type = (None, str(self.poe_type).encode(), "text/plain")
        else:
            poe_type = (None, str(self.poe_type.value).encode(), "text/plain")

        rf_channel_frequency: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.rf_channel_frequency, Unset):
            rf_channel_frequency = UNSET
        elif isinstance(self.rf_channel_frequency, float):
            rf_channel_frequency = (None, str(self.rf_channel_frequency).encode(), "text/plain")
        else:
            rf_channel_frequency = (None, str(self.rf_channel_frequency).encode(), "text/plain")

        rf_channel_width: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.rf_channel_width, Unset):
            rf_channel_width = UNSET
        elif isinstance(self.rf_channel_width, float):
            rf_channel_width = (None, str(self.rf_channel_width).encode(), "text/plain")
        else:
            rf_channel_width = (None, str(self.rf_channel_width).encode(), "text/plain")

        tx_power: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.tx_power, Unset):
            tx_power = UNSET
        elif isinstance(self.tx_power, int):
            tx_power = (None, str(self.tx_power).encode(), "text/plain")
        else:
            tx_power = (None, str(self.tx_power).encode(), "text/plain")

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

        mark_connected = (
            self.mark_connected
            if isinstance(self.mark_connected, Unset)
            else (None, str(self.mark_connected).encode(), "text/plain")
        )

        wireless_lans: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.wireless_lans, Unset):
            _temp_wireless_lans = self.wireless_lans
            wireless_lans = (None, json.dumps(_temp_wireless_lans).encode(), "application/json")

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

        field_dict.update({})
        if device is not UNSET:
            field_dict["device"] = device
        if vdcs is not UNSET:
            field_dict["vdcs"] = vdcs
        if module is not UNSET:
            field_dict["module"] = module
        if name is not UNSET:
            field_dict["name"] = name
        if label is not UNSET:
            field_dict["label"] = label
        if type_ is not UNSET:
            field_dict["type"] = type_
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
        from ..models.brief_device_request import BriefDeviceRequest
        from ..models.brief_mac_address_request import BriefMACAddressRequest
        from ..models.brief_module_request import BriefModuleRequest
        from ..models.brief_vlan_request import BriefVLANRequest
        from ..models.brief_vlan_translation_policy_request import BriefVLANTranslationPolicyRequest
        from ..models.brief_vrf_request import BriefVRFRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_writable_interface_request_custom_fields import (
            PatchedWritableInterfaceRequestCustomFields,
        )

        d = dict(src_dict)

        def _parse_device(data: object) -> Union["BriefDeviceRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_type_1 = BriefDeviceRequest.from_dict(data)

                return device_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDeviceRequest", Unset, int], data)

        device = _parse_device(d.pop("device", UNSET))

        vdcs = cast(list[int], d.pop("vdcs", UNSET))

        def _parse_module(data: object) -> Union["BriefModuleRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                module_type_1_type_1 = BriefModuleRequest.from_dict(data)

                return module_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefModuleRequest", None, Unset, int], data)

        module = _parse_module(d.pop("module", UNSET))

        name = d.pop("name", UNSET)

        label = d.pop("label", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, PatchedWritableInterfaceRequestType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PatchedWritableInterfaceRequestType(_type_)

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

        def _parse_lag(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        lag = _parse_lag(d.pop("lag", UNSET))

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

        def _parse_speed(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        speed = _parse_speed(d.pop("speed", UNSET))

        def _parse_duplex(
            data: object,
        ) -> Union[
            None,
            PatchedWritableInterfaceRequestDuplexType1,
            PatchedWritableInterfaceRequestDuplexType2Type1,
            PatchedWritableInterfaceRequestDuplexType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                duplex_type_1 = PatchedWritableInterfaceRequestDuplexType1(data)

                return duplex_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                duplex_type_2_type_1 = PatchedWritableInterfaceRequestDuplexType2Type1(data)

                return duplex_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                duplex_type_3_type_1 = PatchedWritableInterfaceRequestDuplexType3Type1(data)

                return duplex_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PatchedWritableInterfaceRequestDuplexType1,
                    PatchedWritableInterfaceRequestDuplexType2Type1,
                    PatchedWritableInterfaceRequestDuplexType3Type1,
                    Unset,
                ],
                data,
            )

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

        def _parse_mode(
            data: object,
        ) -> Union[
            None,
            PatchedWritableInterfaceRequestModeType1,
            PatchedWritableInterfaceRequestModeType2Type1,
            PatchedWritableInterfaceRequestModeType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_1 = PatchedWritableInterfaceRequestModeType1(data)

                return mode_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_2_type_1 = PatchedWritableInterfaceRequestModeType2Type1(data)

                return mode_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_3_type_1 = PatchedWritableInterfaceRequestModeType3Type1(data)

                return mode_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PatchedWritableInterfaceRequestModeType1,
                    PatchedWritableInterfaceRequestModeType2Type1,
                    PatchedWritableInterfaceRequestModeType3Type1,
                    Unset,
                ],
                data,
            )

        mode = _parse_mode(d.pop("mode", UNSET))

        def _parse_rf_role(data: object) -> Union[None, PatchedWritableInterfaceRequestWirelessRole, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rf_role_type_1 = PatchedWritableInterfaceRequestWirelessRole(data)

                return rf_role_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rf_role_type_2_type_1 = PatchedWritableInterfaceRequestWirelessRole(data)

                return rf_role_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rf_role_type_3_type_1 = PatchedWritableInterfaceRequestWirelessRole(data)

                return rf_role_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, PatchedWritableInterfaceRequestWirelessRole, Unset], data)

        rf_role = _parse_rf_role(d.pop("rf_role", UNSET))

        def _parse_rf_channel(data: object) -> Union[None, PatchedWritableInterfaceRequestWirelessChannel, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rf_channel_type_1 = PatchedWritableInterfaceRequestWirelessChannel(data)

                return rf_channel_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rf_channel_type_2_type_1 = PatchedWritableInterfaceRequestWirelessChannel(data)

                return rf_channel_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rf_channel_type_3_type_1 = PatchedWritableInterfaceRequestWirelessChannel(data)

                return rf_channel_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, PatchedWritableInterfaceRequestWirelessChannel, Unset], data)

        rf_channel = _parse_rf_channel(d.pop("rf_channel", UNSET))

        def _parse_poe_mode(
            data: object,
        ) -> Union[
            None,
            PatchedWritableInterfaceRequestPoeModeType1,
            PatchedWritableInterfaceRequestPoeModeType2Type1,
            PatchedWritableInterfaceRequestPoeModeType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                poe_mode_type_1 = PatchedWritableInterfaceRequestPoeModeType1(data)

                return poe_mode_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                poe_mode_type_2_type_1 = PatchedWritableInterfaceRequestPoeModeType2Type1(data)

                return poe_mode_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                poe_mode_type_3_type_1 = PatchedWritableInterfaceRequestPoeModeType3Type1(data)

                return poe_mode_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PatchedWritableInterfaceRequestPoeModeType1,
                    PatchedWritableInterfaceRequestPoeModeType2Type1,
                    PatchedWritableInterfaceRequestPoeModeType3Type1,
                    Unset,
                ],
                data,
            )

        poe_mode = _parse_poe_mode(d.pop("poe_mode", UNSET))

        def _parse_poe_type(
            data: object,
        ) -> Union[
            None,
            PatchedWritableInterfaceRequestPoeTypeType1,
            PatchedWritableInterfaceRequestPoeTypeType2Type1,
            PatchedWritableInterfaceRequestPoeTypeType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                poe_type_type_1 = PatchedWritableInterfaceRequestPoeTypeType1(data)

                return poe_type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                poe_type_type_2_type_1 = PatchedWritableInterfaceRequestPoeTypeType2Type1(data)

                return poe_type_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                poe_type_type_3_type_1 = PatchedWritableInterfaceRequestPoeTypeType3Type1(data)

                return poe_type_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PatchedWritableInterfaceRequestPoeTypeType1,
                    PatchedWritableInterfaceRequestPoeTypeType2Type1,
                    PatchedWritableInterfaceRequestPoeTypeType3Type1,
                    Unset,
                ],
                data,
            )

        poe_type = _parse_poe_type(d.pop("poe_type", UNSET))

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

        mark_connected = d.pop("mark_connected", UNSET)

        wireless_lans = cast(list[int], d.pop("wireless_lans", UNSET))

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
        custom_fields: Union[Unset, PatchedWritableInterfaceRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedWritableInterfaceRequestCustomFields.from_dict(_custom_fields)

        patched_writable_interface_request = cls(
            device=device,
            vdcs=vdcs,
            module=module,
            name=name,
            label=label,
            type_=type_,
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
            mode=mode,
            rf_role=rf_role,
            rf_channel=rf_channel,
            poe_mode=poe_mode,
            poe_type=poe_type,
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

        patched_writable_interface_request.additional_properties = d
        return patched_writable_interface_request

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
