from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ip_range_request_status import IPRangeRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_role_request import BriefRoleRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.brief_vrf_request import BriefVRFRequest
    from ..models.ip_range_request_custom_fields import IPRangeRequestCustomFields
    from ..models.nested_tag_request import NestedTagRequest


T = TypeVar("T", bound="IPRangeRequest")


@_attrs_define
class IPRangeRequest:
    """Adds support for custom fields and tags.

    Attributes:
        start_address (str):
        end_address (str):
        vrf (Union['BriefVRFRequest', None, Unset, int]):
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        status (Union[Unset, IPRangeRequestStatus]): * `active` - Active
            * `reserved` - Reserved
            * `deprecated` - Deprecated
        role (Union['BriefRoleRequest', None, Unset, int]):
        description (Union[Unset, str]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, IPRangeRequestCustomFields]):
        mark_populated (Union[Unset, bool]): Prevent the creation of IP addresses within this range
        mark_utilized (Union[Unset, bool]): Report space as 100% utilized
    """

    start_address: str
    end_address: str
    vrf: Union["BriefVRFRequest", None, Unset, int] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    status: Union[Unset, IPRangeRequestStatus] = UNSET
    role: Union["BriefRoleRequest", None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "IPRangeRequestCustomFields"] = UNSET
    mark_populated: Union[Unset, bool] = UNSET
    mark_utilized: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_role_request import BriefRoleRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.brief_vrf_request import BriefVRFRequest

        start_address = self.start_address

        end_address = self.end_address

        vrf: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.vrf, Unset):
            vrf = UNSET
        elif isinstance(self.vrf, BriefVRFRequest):
            vrf = self.vrf.to_dict()
        else:
            vrf = self.vrf

        tenant: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, BriefTenantRequest):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        role: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, BriefRoleRequest):
            role = self.role.to_dict()
        else:
            role = self.role

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

        mark_populated = self.mark_populated

        mark_utilized = self.mark_utilized

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_address": start_address,
                "end_address": end_address,
            }
        )
        if vrf is not UNSET:
            field_dict["vrf"] = vrf
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if status is not UNSET:
            field_dict["status"] = status
        if role is not UNSET:
            field_dict["role"] = role
        if description is not UNSET:
            field_dict["description"] = description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if mark_populated is not UNSET:
            field_dict["mark_populated"] = mark_populated
        if mark_utilized is not UNSET:
            field_dict["mark_utilized"] = mark_utilized

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_role_request import BriefRoleRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.brief_vrf_request import BriefVRFRequest
        from ..models.ip_range_request_custom_fields import IPRangeRequestCustomFields
        from ..models.nested_tag_request import NestedTagRequest

        d = dict(src_dict)
        start_address = d.pop("start_address")

        end_address = d.pop("end_address")

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

        _status = d.pop("status", UNSET)
        status: Union[Unset, IPRangeRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IPRangeRequestStatus(_status)

        def _parse_role(data: object) -> Union["BriefRoleRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                role_type_1_type_1 = BriefRoleRequest.from_dict(data)

                return role_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefRoleRequest", None, Unset, int], data)

        role = _parse_role(d.pop("role", UNSET))

        description = d.pop("description", UNSET)

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, IPRangeRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = IPRangeRequestCustomFields.from_dict(_custom_fields)

        mark_populated = d.pop("mark_populated", UNSET)

        mark_utilized = d.pop("mark_utilized", UNSET)

        ip_range_request = cls(
            start_address=start_address,
            end_address=end_address,
            vrf=vrf,
            tenant=tenant,
            status=status,
            role=role,
            description=description,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
            mark_populated=mark_populated,
            mark_utilized=mark_utilized,
        )

        ip_range_request.additional_properties = d
        return ip_range_request

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
