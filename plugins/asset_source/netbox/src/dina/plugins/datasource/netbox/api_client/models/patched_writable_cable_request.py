import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patched_writable_cable_request_length_unit_type_1 import (
    PatchedWritableCableRequestLengthUnitType1,
)
from ..models.patched_writable_cable_request_length_unit_type_2_type_1 import (
    PatchedWritableCableRequestLengthUnitType2Type1,
)
from ..models.patched_writable_cable_request_length_unit_type_3_type_1 import (
    PatchedWritableCableRequestLengthUnitType3Type1,
)
from ..models.patched_writable_cable_request_status import (
    PatchedWritableCableRequestStatus,
)
from ..models.patched_writable_cable_request_type_type_1 import (
    PatchedWritableCableRequestTypeType1,
)
from ..models.patched_writable_cable_request_type_type_2_type_1 import (
    PatchedWritableCableRequestTypeType2Type1,
)
from ..models.patched_writable_cable_request_type_type_3_type_1 import (
    PatchedWritableCableRequestTypeType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.generic_object_request import GenericObjectRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_writable_cable_request_custom_fields import (
        PatchedWritableCableRequestCustomFields,
    )


T = TypeVar("T", bound="PatchedWritableCableRequest")


@_attrs_define
class PatchedWritableCableRequest:
    """Adds support for custom fields and tags.

    Attributes:
        type_ (Union[None, PatchedWritableCableRequestTypeType1, PatchedWritableCableRequestTypeType2Type1,
            PatchedWritableCableRequestTypeType3Type1, Unset]): * `cat3` - CAT3
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
        a_terminations (Union[Unset, list['GenericObjectRequest']]):
        b_terminations (Union[Unset, list['GenericObjectRequest']]):
        status (Union[Unset, PatchedWritableCableRequestStatus]): * `connected` - Connected
            * `planned` - Planned
            * `decommissioning` - Decommissioning
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        label (Union[Unset, str]):
        color (Union[Unset, str]):
        length (Union[None, Unset, float]):
        length_unit (Union[None, PatchedWritableCableRequestLengthUnitType1,
            PatchedWritableCableRequestLengthUnitType2Type1, PatchedWritableCableRequestLengthUnitType3Type1, Unset]): *
            `km` - Kilometers
            * `m` - Meters
            * `cm` - Centimeters
            * `mi` - Miles
            * `ft` - Feet
            * `in` - Inches
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedWritableCableRequestCustomFields]):
    """

    type_: Union[
        None,
        PatchedWritableCableRequestTypeType1,
        PatchedWritableCableRequestTypeType2Type1,
        PatchedWritableCableRequestTypeType3Type1,
        Unset,
    ] = UNSET
    a_terminations: Union[Unset, list["GenericObjectRequest"]] = UNSET
    b_terminations: Union[Unset, list["GenericObjectRequest"]] = UNSET
    status: Union[Unset, PatchedWritableCableRequestStatus] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    label: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    length: Union[None, Unset, float] = UNSET
    length_unit: Union[
        None,
        PatchedWritableCableRequestLengthUnitType1,
        PatchedWritableCableRequestLengthUnitType2Type1,
        PatchedWritableCableRequestLengthUnitType3Type1,
        Unset,
    ] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedWritableCableRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_tenant_request import BriefTenantRequest

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, PatchedWritableCableRequestTypeType1):
            type_ = self.type_.value
        elif isinstance(self.type_, PatchedWritableCableRequestTypeType2Type1):
            type_ = self.type_.value
        elif isinstance(self.type_, PatchedWritableCableRequestTypeType3Type1):
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

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        tenant: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenantRequest):
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

        length_unit: Union[None, Unset, str]
        if isinstance(self.length_unit, Unset):
            length_unit = UNSET
        elif isinstance(self.length_unit, PatchedWritableCableRequestLengthUnitType1):
            length_unit = self.length_unit.value
        elif isinstance(
            self.length_unit, PatchedWritableCableRequestLengthUnitType2Type1
        ):
            length_unit = self.length_unit.value
        elif isinstance(
            self.length_unit, PatchedWritableCableRequestLengthUnitType3Type1
        ):
            length_unit = self.length_unit.value
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
        field_dict.update({})
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

    def to_multipart(self) -> dict[str, Any]:
        type_: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, None):
            type_ = (None, str(self.type_).encode(), "text/plain")
        elif isinstance(self.type_, PatchedWritableCableRequestTypeType1):
            type_ = (None, str(self.type_.value).encode(), "text/plain")
        elif isinstance(self.type_, None):
            type_ = (None, str(self.type_).encode(), "text/plain")
        elif isinstance(self.type_, PatchedWritableCableRequestTypeType2Type1):
            type_ = (None, str(self.type_.value).encode(), "text/plain")
        elif isinstance(self.type_, None):
            type_ = (None, str(self.type_).encode(), "text/plain")
        else:
            type_ = (None, str(self.type_.value).encode(), "text/plain")

        a_terminations: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.a_terminations, Unset):
            _temp_a_terminations = []
            for a_terminations_item_data in self.a_terminations:
                a_terminations_item = a_terminations_item_data.to_dict()
                _temp_a_terminations.append(a_terminations_item)
            a_terminations = (
                None,
                json.dumps(_temp_a_terminations).encode(),
                "application/json",
            )

        b_terminations: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.b_terminations, Unset):
            _temp_b_terminations = []
            for b_terminations_item_data in self.b_terminations:
                b_terminations_item = b_terminations_item_data.to_dict()
                _temp_b_terminations.append(b_terminations_item)
            b_terminations = (
                None,
                json.dumps(_temp_b_terminations).encode(),
                "application/json",
            )

        status: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

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

        label = (
            self.label
            if isinstance(self.label, Unset)
            else (None, str(self.label).encode(), "text/plain")
        )

        color = (
            self.color
            if isinstance(self.color, Unset)
            else (None, str(self.color).encode(), "text/plain")
        )

        length: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.length, Unset):
            length = UNSET
        elif isinstance(self.length, float):
            length = (None, str(self.length).encode(), "text/plain")
        else:
            length = (None, str(self.length).encode(), "text/plain")

        length_unit: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.length_unit, Unset):
            length_unit = UNSET
        elif isinstance(self.length_unit, None):
            length_unit = (None, str(self.length_unit).encode(), "text/plain")
        elif isinstance(self.length_unit, PatchedWritableCableRequestLengthUnitType1):
            length_unit = (None, str(self.length_unit.value).encode(), "text/plain")
        elif isinstance(self.length_unit, None):
            length_unit = (None, str(self.length_unit).encode(), "text/plain")
        elif isinstance(
            self.length_unit, PatchedWritableCableRequestLengthUnitType2Type1
        ):
            length_unit = (None, str(self.length_unit.value).encode(), "text/plain")
        elif isinstance(self.length_unit, None):
            length_unit = (None, str(self.length_unit).encode(), "text/plain")
        else:
            length_unit = (None, str(self.length_unit.value).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

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

        field_dict.update({})
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
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.generic_object_request import GenericObjectRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_writable_cable_request_custom_fields import (
            PatchedWritableCableRequestCustomFields,
        )

        d = dict(src_dict)

        def _parse_type_(
            data: object,
        ) -> Union[
            None,
            PatchedWritableCableRequestTypeType1,
            PatchedWritableCableRequestTypeType2Type1,
            PatchedWritableCableRequestTypeType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = PatchedWritableCableRequestTypeType1(data)

                return type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_2_type_1 = PatchedWritableCableRequestTypeType2Type1(data)

                return type_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_3_type_1 = PatchedWritableCableRequestTypeType3Type1(data)

                return type_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PatchedWritableCableRequestTypeType1,
                    PatchedWritableCableRequestTypeType2Type1,
                    PatchedWritableCableRequestTypeType3Type1,
                    Unset,
                ],
                data,
            )

        type_ = _parse_type_(d.pop("type", UNSET))

        a_terminations = []
        _a_terminations = d.pop("a_terminations", UNSET)
        for a_terminations_item_data in _a_terminations or []:
            a_terminations_item = GenericObjectRequest.from_dict(
                a_terminations_item_data
            )

            a_terminations.append(a_terminations_item)

        b_terminations = []
        _b_terminations = d.pop("b_terminations", UNSET)
        for b_terminations_item_data in _b_terminations or []:
            b_terminations_item = GenericObjectRequest.from_dict(
                b_terminations_item_data
            )

            b_terminations.append(b_terminations_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, PatchedWritableCableRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PatchedWritableCableRequestStatus(_status)

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

        label = d.pop("label", UNSET)

        color = d.pop("color", UNSET)

        def _parse_length(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        length = _parse_length(d.pop("length", UNSET))

        def _parse_length_unit(
            data: object,
        ) -> Union[
            None,
            PatchedWritableCableRequestLengthUnitType1,
            PatchedWritableCableRequestLengthUnitType2Type1,
            PatchedWritableCableRequestLengthUnitType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                length_unit_type_1 = PatchedWritableCableRequestLengthUnitType1(data)

                return length_unit_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                length_unit_type_2_type_1 = (
                    PatchedWritableCableRequestLengthUnitType2Type1(data)
                )

                return length_unit_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                length_unit_type_3_type_1 = (
                    PatchedWritableCableRequestLengthUnitType3Type1(data)
                )

                return length_unit_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PatchedWritableCableRequestLengthUnitType1,
                    PatchedWritableCableRequestLengthUnitType2Type1,
                    PatchedWritableCableRequestLengthUnitType3Type1,
                    Unset,
                ],
                data,
            )

        length_unit = _parse_length_unit(d.pop("length_unit", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, PatchedWritableCableRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedWritableCableRequestCustomFields.from_dict(
                _custom_fields
            )

        patched_writable_cable_request = cls(
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

        patched_writable_cable_request.additional_properties = d
        return patched_writable_cable_request

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
