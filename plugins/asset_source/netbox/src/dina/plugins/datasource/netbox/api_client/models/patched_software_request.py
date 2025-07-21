import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_manufacturer_request import BriefManufacturerRequest
    from ..models.patched_software_request_custom_fields import (
        PatchedSoftwareRequestCustomFields,
    )


T = TypeVar("T", bound="PatchedSoftwareRequest")


@_attrs_define
class PatchedSoftwareRequest:
    """REST API Model Serializer for Software.

    Attributes:
        name (Union[Unset, str]):
        manufacturer (Union['BriefManufacturerRequest', Unset, int]):
        is_firmware (Union[None, Unset, bool]):
        version (Union[None, Unset, str]):
        cpe (Union[None, Unset, str]):
        purl (Union[None, Unset, str]):
        sbom_urls (Union[None, Unset, list[Union[None, str]]]):
        custom_fields (Union[Unset, PatchedSoftwareRequestCustomFields]):
    """

    name: Union[Unset, str] = UNSET
    manufacturer: Union["BriefManufacturerRequest", Unset, int] = UNSET
    is_firmware: Union[None, Unset, bool] = UNSET
    version: Union[None, Unset, str] = UNSET
    cpe: Union[None, Unset, str] = UNSET
    purl: Union[None, Unset, str] = UNSET
    sbom_urls: Union[None, Unset, list[Union[None, str]]] = UNSET
    custom_fields: Union[Unset, "PatchedSoftwareRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_manufacturer_request import BriefManufacturerRequest

        name = self.name

        manufacturer: Union[Unset, dict[str, Any], int]
        if isinstance(self.manufacturer, Unset):
            manufacturer = UNSET
        elif isinstance(self.manufacturer, BriefManufacturerRequest):
            manufacturer = self.manufacturer.to_dict()
        else:
            manufacturer = self.manufacturer

        is_firmware: Union[None, Unset, bool]
        if isinstance(self.is_firmware, Unset):
            is_firmware = UNSET
        else:
            is_firmware = self.is_firmware

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        cpe: Union[None, Unset, str]
        if isinstance(self.cpe, Unset):
            cpe = UNSET
        else:
            cpe = self.cpe

        purl: Union[None, Unset, str]
        if isinstance(self.purl, Unset):
            purl = UNSET
        else:
            purl = self.purl

        sbom_urls: Union[None, Unset, list[Union[None, str]]]
        if isinstance(self.sbom_urls, Unset):
            sbom_urls = UNSET
        elif isinstance(self.sbom_urls, list):
            sbom_urls = []
            for sbom_urls_type_0_item_data in self.sbom_urls:
                sbom_urls_type_0_item: Union[None, str]
                sbom_urls_type_0_item = sbom_urls_type_0_item_data
                sbom_urls.append(sbom_urls_type_0_item)

        else:
            sbom_urls = self.sbom_urls

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if is_firmware is not UNSET:
            field_dict["is_firmware"] = is_firmware
        if version is not UNSET:
            field_dict["version"] = version
        if cpe is not UNSET:
            field_dict["cpe"] = cpe
        if purl is not UNSET:
            field_dict["purl"] = purl
        if sbom_urls is not UNSET:
            field_dict["sbom_urls"] = sbom_urls
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        name = (
            self.name
            if isinstance(self.name, Unset)
            else (None, str(self.name).encode(), "text/plain")
        )

        manufacturer: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.manufacturer, Unset):
            manufacturer = UNSET
        elif isinstance(self.manufacturer, int):
            manufacturer = (None, str(self.manufacturer).encode(), "text/plain")
        else:
            manufacturer = (
                None,
                json.dumps(self.manufacturer.to_dict()).encode(),
                "application/json",
            )

        is_firmware: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.is_firmware, Unset):
            is_firmware = UNSET
        elif isinstance(self.is_firmware, bool):
            is_firmware = (None, str(self.is_firmware).encode(), "text/plain")
        else:
            is_firmware = (None, str(self.is_firmware).encode(), "text/plain")

        version: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.version, Unset):
            version = UNSET
        elif isinstance(self.version, str):
            version = (None, str(self.version).encode(), "text/plain")
        else:
            version = (None, str(self.version).encode(), "text/plain")

        cpe: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.cpe, Unset):
            cpe = UNSET
        elif isinstance(self.cpe, str):
            cpe = (None, str(self.cpe).encode(), "text/plain")
        else:
            cpe = (None, str(self.cpe).encode(), "text/plain")

        purl: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.purl, Unset):
            purl = UNSET
        elif isinstance(self.purl, str):
            purl = (None, str(self.purl).encode(), "text/plain")
        else:
            purl = (None, str(self.purl).encode(), "text/plain")

        sbom_urls: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.sbom_urls, Unset):
            sbom_urls = UNSET
        elif isinstance(self.sbom_urls, list):
            _temp_sbom_urls = []
            for sbom_urls_type_0_item_data in self.sbom_urls:
                sbom_urls_type_0_item: Union[None, str]
                sbom_urls_type_0_item = sbom_urls_type_0_item_data
                _temp_sbom_urls.append(sbom_urls_type_0_item)
            sbom_urls = (None, json.dumps(_temp_sbom_urls).encode(), "application/json")
        else:
            sbom_urls = (None, str(self.sbom_urls).encode(), "text/plain")

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

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if is_firmware is not UNSET:
            field_dict["is_firmware"] = is_firmware
        if version is not UNSET:
            field_dict["version"] = version
        if cpe is not UNSET:
            field_dict["cpe"] = cpe
        if purl is not UNSET:
            field_dict["purl"] = purl
        if sbom_urls is not UNSET:
            field_dict["sbom_urls"] = sbom_urls
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_manufacturer_request import BriefManufacturerRequest
        from ..models.patched_software_request_custom_fields import (
            PatchedSoftwareRequestCustomFields,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_manufacturer(
            data: object,
        ) -> Union["BriefManufacturerRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                manufacturer_type_1 = BriefManufacturerRequest.from_dict(data)

                return manufacturer_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefManufacturerRequest", Unset, int], data)

        manufacturer = _parse_manufacturer(d.pop("manufacturer", UNSET))

        def _parse_is_firmware(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_firmware = _parse_is_firmware(d.pop("is_firmware", UNSET))

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_cpe(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cpe = _parse_cpe(d.pop("cpe", UNSET))

        def _parse_purl(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        purl = _parse_purl(d.pop("purl", UNSET))

        def _parse_sbom_urls(
            data: object,
        ) -> Union[None, Unset, list[Union[None, str]]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sbom_urls_type_0 = []
                _sbom_urls_type_0 = data
                for sbom_urls_type_0_item_data in _sbom_urls_type_0:

                    def _parse_sbom_urls_type_0_item(data: object) -> Union[None, str]:
                        if data is None:
                            return data
                        return cast(Union[None, str], data)

                    sbom_urls_type_0_item = _parse_sbom_urls_type_0_item(
                        sbom_urls_type_0_item_data
                    )

                    sbom_urls_type_0.append(sbom_urls_type_0_item)

                return sbom_urls_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[Union[None, str]]], data)

        sbom_urls = _parse_sbom_urls(d.pop("sbom_urls", UNSET))

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedSoftwareRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedSoftwareRequestCustomFields.from_dict(_custom_fields)

        patched_software_request = cls(
            name=name,
            manufacturer=manufacturer,
            is_firmware=is_firmware,
            version=version,
            cpe=cpe,
            purl=purl,
            sbom_urls=sbom_urls,
            custom_fields=custom_fields,
        )

        patched_software_request.additional_properties = d
        return patched_software_request

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
