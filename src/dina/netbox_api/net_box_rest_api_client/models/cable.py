import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.cable_type_type_1 import CableTypeType1
from ..models.cable_type_type_2_type_1 import CableTypeType2Type1
from ..models.cable_type_type_3_type_1 import CableTypeType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_tenant import BriefTenant
    from ..models.cable_custom_fields import CableCustomFields
    from ..models.cable_length_unit_type_0 import CableLengthUnitType0
    from ..models.cable_status import CableStatus
    from ..models.generic_object import GenericObject
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="Cable")


@_attrs_define
class Cable:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        type_ (Union[CableTypeType1, CableTypeType2Type1, CableTypeType3Type1, None, Unset]): * `cat3` - CAT3
            * `cat5` - CAT5
            * `cat5e` - CAT5e
            * `cat6` - CAT6
            * `cat6a` - CAT6a
            * `cat7` - CAT7
            * `cat7a` - CAT7a
            * `cat8` - CAT8
            * `dac-active` - Direct Attach Copper (Active)
            * `dac-passive` - Direct Attach Copper (Passive)
            * `mrj21-trunk` - MRJ21 Trunk
            * `coaxial` - Coaxial
            * `mmf` - Multimode Fiber
            * `mmf-om1` - Multimode Fiber (OM1)
            * `mmf-om2` - Multimode Fiber (OM2)
            * `mmf-om3` - Multimode Fiber (OM3)
            * `mmf-om4` - Multimode Fiber (OM4)
            * `mmf-om5` - Multimode Fiber (OM5)
            * `smf` - Singlemode Fiber
            * `smf-os1` - Singlemode Fiber (OS1)
            * `smf-os2` - Singlemode Fiber (OS2)
            * `aoc` - Active Optical Cabling (AOC)
            * `usb` - USB
            * `power` - Power
        a_terminations (Union[Unset, list['GenericObject']]):
        b_terminations (Union[Unset, list['GenericObject']]):
        status (Union[Unset, CableStatus]):
        tenant (Union['BriefTenant', None, Unset]):
        label (Union[Unset, str]):
        color (Union[Unset, str]):
        length (Union[None, Unset, float]):
        length_unit (Union['CableLengthUnitType0', None, Unset]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, CableCustomFields]):
    """

    id: int
    url: str
    display_url: str
    display: str
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    type_: Union[CableTypeType1, CableTypeType2Type1, CableTypeType3Type1, None, Unset] = UNSET
    a_terminations: Union[Unset, list["GenericObject"]] = UNSET
    b_terminations: Union[Unset, list["GenericObject"]] = UNSET
    status: Union[Unset, "CableStatus"] = UNSET
    tenant: Union["BriefTenant", None, Unset] = UNSET
    label: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    length: Union[None, Unset, float] = UNSET
    length_unit: Union["CableLengthUnitType0", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "CableCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_tenant import BriefTenant
        from ..models.cable_length_unit_type_0 import CableLengthUnitType0

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

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

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, CableTypeType1):
            type_ = self.type_.value
        elif isinstance(self.type_, CableTypeType2Type1):
            type_ = self.type_.value
        elif isinstance(self.type_, CableTypeType3Type1):
            type_ = self.type_.value
        else:
            type_ = self.type_

        a_terminations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.a_terminations, Unset):
            a_terminations = []
            for a_terminations_item_data in self.a_terminations:
                a_terminations_item = a_terminations_item_data.to_dict()
                a_terminations.append(a_terminations_item)

        b_terminations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.b_terminations, Unset):
            b_terminations = []
            for b_terminations_item_data in self.b_terminations:
                b_terminations_item = b_terminations_item_data.to_dict()
                b_terminations.append(b_terminations_item)

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        tenant: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenant):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        label = self.label

        color = self.color

        length: Union[None, Unset, float]
        if isinstance(self.length, Unset):
            length = UNSET
        else:
            length = self.length

        length_unit: Union[None, Unset, dict[str, Any]]
        if isinstance(self.length_unit, Unset):
            length_unit = UNSET
        elif isinstance(self.length_unit, CableLengthUnitType0):
            length_unit = self.length_unit.to_dict()
        else:
            length_unit = self.length_unit

        description = self.description

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
                "created": created,
                "last_updated": last_updated,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if a_terminations is not UNSET:
            field_dict["a_terminations"] = a_terminations
        if b_terminations is not UNSET:
            field_dict["b_terminations"] = b_terminations
        if status is not UNSET:
            field_dict["status"] = status
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if label is not UNSET:
            field_dict["label"] = label
        if color is not UNSET:
            field_dict["color"] = color
        if length is not UNSET:
            field_dict["length"] = length
        if length_unit is not UNSET:
            field_dict["length_unit"] = length_unit
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_tenant import BriefTenant
        from ..models.cable_custom_fields import CableCustomFields
        from ..models.cable_length_unit_type_0 import CableLengthUnitType0
        from ..models.cable_status import CableStatus
        from ..models.generic_object import GenericObject
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

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

        def _parse_type_(data: object) -> Union[CableTypeType1, CableTypeType2Type1, CableTypeType3Type1, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = CableTypeType1(data)

                return type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_2_type_1 = CableTypeType2Type1(data)

                return type_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_3_type_1 = CableTypeType3Type1(data)

                return type_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(Union[CableTypeType1, CableTypeType2Type1, CableTypeType3Type1, None, Unset], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        a_terminations = []
        _a_terminations = d.pop("a_terminations", UNSET)
        for a_terminations_item_data in _a_terminations or []:
            a_terminations_item = GenericObject.from_dict(a_terminations_item_data)

            a_terminations.append(a_terminations_item)

        b_terminations = []
        _b_terminations = d.pop("b_terminations", UNSET)
        for b_terminations_item_data in _b_terminations or []:
            b_terminations_item = GenericObject.from_dict(b_terminations_item_data)

            b_terminations.append(b_terminations_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CableStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CableStatus.from_dict(_status)

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

        label = d.pop("label", UNSET)

        color = d.pop("color", UNSET)

        def _parse_length(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        length = _parse_length(d.pop("length", UNSET))

        def _parse_length_unit(data: object) -> Union["CableLengthUnitType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                length_unit_type_0 = CableLengthUnitType0.from_dict(data)

                return length_unit_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CableLengthUnitType0", None, Unset], data)

        length_unit = _parse_length_unit(d.pop("length_unit", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, CableCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CableCustomFields.from_dict(_custom_fields)

        cable = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            created=created,
            last_updated=last_updated,
            type_=type_,
            a_terminations=a_terminations,
            b_terminations=b_terminations,
            status=status,
            tenant=tenant,
            label=label,
            color=color,
            length=length,
            length_unit=length_unit,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        cable.additional_properties = d
        return cable

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
