import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_rack_request import BriefRackRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.brief_user_request import BriefUserRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.rack_reservation_request_custom_fields import RackReservationRequestCustomFields


T = TypeVar("T", bound="RackReservationRequest")


@_attrs_define
class RackReservationRequest:
    """Adds support for custom fields and tags.

    Attributes:
        rack (Union['BriefRackRequest', int]):
        units (list[int]):
        user (Union['BriefUserRequest', int]):
        description (str):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, RackReservationRequestCustomFields]):
    """

    rack: Union["BriefRackRequest", int]
    units: list[int]
    user: Union["BriefUserRequest", int]
    description: str
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "RackReservationRequestCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_rack_request import BriefRackRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.brief_user_request import BriefUserRequest

        rack: Union[dict[str, Any], int]
        if isinstance(self.rack, BriefRackRequest):
            rack = self.rack.to_dict()
        else:
            rack = self.rack

        units = self.units

        user: Union[dict[str, Any], int]
        if isinstance(self.user, BriefUserRequest):
            user = self.user.to_dict()
        else:
            user = self.user

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
                "rack": rack,
                "units": units,
                "user": user,
                "description": description,
            }
        )
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        rack: tuple[None, bytes, str]

        if isinstance(self.rack, int):
            rack = (None, str(self.rack).encode(), "text/plain")
        else:
            rack = (None, json.dumps(self.rack.to_dict()).encode(), "application/json")

        _temp_units = self.units
        units = (None, json.dumps(_temp_units).encode(), "application/json")

        user: tuple[None, bytes, str]

        if isinstance(self.user, int):
            user = (None, str(self.user).encode(), "text/plain")
        else:
            user = (None, json.dumps(self.user.to_dict()).encode(), "application/json")

        description = (None, str(self.description).encode(), "text/plain")

        tenant: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, int):
            tenant = (None, str(self.tenant).encode(), "text/plain")
        elif isinstance(self.tenant, None):
            tenant = (None, str(self.tenant).encode(), "text/plain")
        elif isinstance(self.tenant, BriefTenantRequest):
            tenant = (None, json.dumps(self.tenant.to_dict()).encode(), "application/json")
        else:
            tenant = (None, str(self.tenant).encode(), "text/plain")

        comments = (
            self.comments if isinstance(self.comments, Unset) else (None, str(self.comments).encode(), "text/plain")
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
            custom_fields = (None, json.dumps(self.custom_fields.to_dict()).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "rack": rack,
                "units": units,
                "user": user,
                "description": description,
            }
        )
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
        from ..models.brief_rack_request import BriefRackRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.brief_user_request import BriefUserRequest
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.rack_reservation_request_custom_fields import RackReservationRequestCustomFields

        d = dict(src_dict)

        def _parse_rack(data: object) -> Union["BriefRackRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rack_type_1 = BriefRackRequest.from_dict(data)

                return rack_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefRackRequest", int], data)

        rack = _parse_rack(d.pop("rack"))

        units = cast(list[int], d.pop("units"))

        def _parse_user(data: object) -> Union["BriefUserRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_1 = BriefUserRequest.from_dict(data)

                return user_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefUserRequest", int], data)

        user = _parse_user(d.pop("user"))

        description = d.pop("description")

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
        custom_fields: Union[Unset, RackReservationRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = RackReservationRequestCustomFields.from_dict(_custom_fields)

        rack_reservation_request = cls(
            rack=rack,
            units=units,
            user=user,
            description=description,
            tenant=tenant,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
        )

        rack_reservation_request.additional_properties = d
        return rack_reservation_request

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
