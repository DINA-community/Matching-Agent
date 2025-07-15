import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_manufacturer import BriefManufacturer
    from ..models.software_custom_fields import SoftwareCustomFields


T = TypeVar("T", bound="Software")


@_attrs_define
class Software:
    """REST API Model Serializer for Software.

    Attributes:
        id (int):
        display (str):
        url (str):
        name (str):
        manufacturer (BriefManufacturer): Adds support for custom fields and tags.
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        is_firmware (Union[None, Unset, bool]):
        version (Union[None, Unset, str]):
        cpe (Union[None, Unset, str]):
        purl (Union[None, Unset, str]):
        sbom_urls (Union[None, Unset, list[Union[None, str]]]):
        custom_fields (Union[Unset, SoftwareCustomFields]):
    """

    id: int
    display: str
    url: str
    name: str
    manufacturer: "BriefManufacturer"
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    is_firmware: Union[None, Unset, bool] = UNSET
    version: Union[None, Unset, str] = UNSET
    cpe: Union[None, Unset, str] = UNSET
    purl: Union[None, Unset, str] = UNSET
    sbom_urls: Union[None, Unset, list[Union[None, str]]] = UNSET
    custom_fields: Union[Unset, "SoftwareCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display = self.display

        url = self.url

        name = self.name

        manufacturer = self.manufacturer.to_dict()

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
        field_dict.update(
            {
                "id": id,
                "display": display,
                "url": url,
                "name": name,
                "manufacturer": manufacturer,
                "created": created,
                "last_updated": last_updated,
            }
        )
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
        from ..models.brief_manufacturer import BriefManufacturer
        from ..models.software_custom_fields import SoftwareCustomFields

        d = dict(src_dict)
        id = d.pop("id")

        display = d.pop("display")

        url = d.pop("url")

        name = d.pop("name")

        manufacturer = BriefManufacturer.from_dict(d.pop("manufacturer"))

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

        def _parse_sbom_urls(data: object) -> Union[None, Unset, list[Union[None, str]]]:
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

                    sbom_urls_type_0_item = _parse_sbom_urls_type_0_item(sbom_urls_type_0_item_data)

                    sbom_urls_type_0.append(sbom_urls_type_0_item)

                return sbom_urls_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[Union[None, str]]], data)

        sbom_urls = _parse_sbom_urls(d.pop("sbom_urls", UNSET))

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, SoftwareCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = SoftwareCustomFields.from_dict(_custom_fields)

        software = cls(
            id=id,
            display=display,
            url=url,
            name=name,
            manufacturer=manufacturer,
            created=created,
            last_updated=last_updated,
            is_firmware=is_firmware,
            version=version,
            cpe=cpe,
            purl=purl,
            sbom_urls=sbom_urls,
            custom_fields=custom_fields,
        )

        software.additional_properties = d
        return software

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
