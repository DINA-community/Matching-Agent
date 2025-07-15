import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.circuit_request_distance_unit_type_1 import CircuitRequestDistanceUnitType1
from ..models.circuit_request_distance_unit_type_2_type_1 import CircuitRequestDistanceUnitType2Type1
from ..models.circuit_request_distance_unit_type_3_type_1 import CircuitRequestDistanceUnitType3Type1
from ..models.circuit_request_status import CircuitRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_circuit_group_assignment_serializer_request import BriefCircuitGroupAssignmentSerializerRequest
    from ..models.brief_circuit_type_request import BriefCircuitTypeRequest
    from ..models.brief_provider_account_request import BriefProviderAccountRequest
    from ..models.brief_provider_request import BriefProviderRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.circuit_request_custom_fields import CircuitRequestCustomFields
    from ..models.nested_tag_request import NestedTagRequest


T = TypeVar("T", bound="CircuitRequest")


@_attrs_define
class CircuitRequest:
    """Adds support for custom fields and tags.

    Attributes:
        cid (str): Unique circuit ID
        provider (Union['BriefProviderRequest', int]):
        type_ (Union['BriefCircuitTypeRequest', int]):
        provider_account (Union['BriefProviderAccountRequest', None, Unset, int]):
        status (Union[Unset, CircuitRequestStatus]): * `planned` - Planned
            * `provisioning` - Provisioning
            * `active` - Active
            * `offline` - Offline
            * `deprovisioning` - Deprovisioning
            * `decommissioned` - Decommissioned
        tenant (Union['BriefTenantRequest', None, Unset, int]):
        install_date (Union[None, Unset, datetime.date]):
        termination_date (Union[None, Unset, datetime.date]):
        commit_rate (Union[None, Unset, int]): Committed rate
        description (Union[Unset, str]):
        distance (Union[None, Unset, float]):
        distance_unit (Union[CircuitRequestDistanceUnitType1, CircuitRequestDistanceUnitType2Type1,
            CircuitRequestDistanceUnitType3Type1, None, Unset]): * `km` - Kilometers
            * `m` - Meters
            * `mi` - Miles
            * `ft` - Feet
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, CircuitRequestCustomFields]):
        assignments (Union[Unset, list['BriefCircuitGroupAssignmentSerializerRequest']]):
    """

    cid: str
    provider: Union["BriefProviderRequest", int]
    type_: Union["BriefCircuitTypeRequest", int]
    provider_account: Union["BriefProviderAccountRequest", None, Unset, int] = UNSET
    status: Union[Unset, CircuitRequestStatus] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    install_date: Union[None, Unset, datetime.date] = UNSET
    termination_date: Union[None, Unset, datetime.date] = UNSET
    commit_rate: Union[None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    distance: Union[None, Unset, float] = UNSET
    distance_unit: Union[
        CircuitRequestDistanceUnitType1,
        CircuitRequestDistanceUnitType2Type1,
        CircuitRequestDistanceUnitType3Type1,
        None,
        Unset,
    ] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "CircuitRequestCustomFields"] = UNSET
    assignments: Union[Unset, list["BriefCircuitGroupAssignmentSerializerRequest"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_circuit_type_request import BriefCircuitTypeRequest
        from ..models.brief_provider_account_request import BriefProviderAccountRequest
        from ..models.brief_provider_request import BriefProviderRequest
        from ..models.brief_tenant_request import BriefTenantRequest

        cid = self.cid

        provider: Union[dict[str, Any], int]
        if isinstance(self.provider, BriefProviderRequest):
            provider = self.provider.to_dict()
        else:
            provider = self.provider

        type_: Union[dict[str, Any], int]
        if isinstance(self.type_, BriefCircuitTypeRequest):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        provider_account: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.provider_account, Unset):
            provider_account = UNSET
        elif isinstance(self.provider_account, BriefProviderAccountRequest):
            provider_account = self.provider_account.to_dict()
        else:
            provider_account = self.provider_account

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

        install_date: Union[None, Unset, str]
        if isinstance(self.install_date, Unset):
            install_date = UNSET
        elif isinstance(self.install_date, datetime.date):
            install_date = self.install_date.isoformat()
        else:
            install_date = self.install_date

        termination_date: Union[None, Unset, str]
        if isinstance(self.termination_date, Unset):
            termination_date = UNSET
        elif isinstance(self.termination_date, datetime.date):
            termination_date = self.termination_date.isoformat()
        else:
            termination_date = self.termination_date

        commit_rate: Union[None, Unset, int]
        if isinstance(self.commit_rate, Unset):
            commit_rate = UNSET
        else:
            commit_rate = self.commit_rate

        description = self.description

        distance: Union[None, Unset, float]
        if isinstance(self.distance, Unset):
            distance = UNSET
        else:
            distance = self.distance

        distance_unit: Union[None, Unset, str]
        if isinstance(self.distance_unit, Unset):
            distance_unit = UNSET
        elif isinstance(self.distance_unit, CircuitRequestDistanceUnitType1):
            distance_unit = self.distance_unit.value
        elif isinstance(self.distance_unit, CircuitRequestDistanceUnitType2Type1):
            distance_unit = self.distance_unit.value
        elif isinstance(self.distance_unit, CircuitRequestDistanceUnitType3Type1):
            distance_unit = self.distance_unit.value
        else:
            distance_unit = self.distance_unit

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

        assignments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.assignments, Unset):
            assignments = []
            for assignments_item_data in self.assignments:
                assignments_item = assignments_item_data.to_dict()
                assignments.append(assignments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cid": cid,
                "provider": provider,
                "type": type_,
            }
        )
        if provider_account is not UNSET:
            field_dict["provider_account"] = provider_account
        if status is not UNSET:
            field_dict["status"] = status
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if install_date is not UNSET:
            field_dict["install_date"] = install_date
        if termination_date is not UNSET:
            field_dict["termination_date"] = termination_date
        if commit_rate is not UNSET:
            field_dict["commit_rate"] = commit_rate
        if description is not UNSET:
            field_dict["description"] = description
        if distance is not UNSET:
            field_dict["distance"] = distance
        if distance_unit is not UNSET:
            field_dict["distance_unit"] = distance_unit
        if comments is not UNSET:
            field_dict["comments"] = comments
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if assignments is not UNSET:
            field_dict["assignments"] = assignments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_circuit_group_assignment_serializer_request import (
            BriefCircuitGroupAssignmentSerializerRequest,
        )
        from ..models.brief_circuit_type_request import BriefCircuitTypeRequest
        from ..models.brief_provider_account_request import BriefProviderAccountRequest
        from ..models.brief_provider_request import BriefProviderRequest
        from ..models.brief_tenant_request import BriefTenantRequest
        from ..models.circuit_request_custom_fields import CircuitRequestCustomFields
        from ..models.nested_tag_request import NestedTagRequest

        d = dict(src_dict)
        cid = d.pop("cid")

        def _parse_provider(data: object) -> Union["BriefProviderRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_type_1 = BriefProviderRequest.from_dict(data)

                return provider_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefProviderRequest", int], data)

        provider = _parse_provider(d.pop("provider"))

        def _parse_type_(data: object) -> Union["BriefCircuitTypeRequest", int]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                type_type_1 = BriefCircuitTypeRequest.from_dict(data)

                return type_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefCircuitTypeRequest", int], data)

        type_ = _parse_type_(d.pop("type"))

        def _parse_provider_account(data: object) -> Union["BriefProviderAccountRequest", None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_account_type_1_type_1 = BriefProviderAccountRequest.from_dict(data)

                return provider_account_type_1_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefProviderAccountRequest", None, Unset, int], data)

        provider_account = _parse_provider_account(d.pop("provider_account", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, CircuitRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CircuitRequestStatus(_status)

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

        def _parse_install_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                install_date_type_0 = isoparse(data).date()

                return install_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        install_date = _parse_install_date(d.pop("install_date", UNSET))

        def _parse_termination_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                termination_date_type_0 = isoparse(data).date()

                return termination_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        termination_date = _parse_termination_date(d.pop("termination_date", UNSET))

        def _parse_commit_rate(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        commit_rate = _parse_commit_rate(d.pop("commit_rate", UNSET))

        description = d.pop("description", UNSET)

        def _parse_distance(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        distance = _parse_distance(d.pop("distance", UNSET))

        def _parse_distance_unit(
            data: object,
        ) -> Union[
            CircuitRequestDistanceUnitType1,
            CircuitRequestDistanceUnitType2Type1,
            CircuitRequestDistanceUnitType3Type1,
            None,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                distance_unit_type_1 = CircuitRequestDistanceUnitType1(data)

                return distance_unit_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                distance_unit_type_2_type_1 = CircuitRequestDistanceUnitType2Type1(data)

                return distance_unit_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                distance_unit_type_3_type_1 = CircuitRequestDistanceUnitType3Type1(data)

                return distance_unit_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    CircuitRequestDistanceUnitType1,
                    CircuitRequestDistanceUnitType2Type1,
                    CircuitRequestDistanceUnitType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        distance_unit = _parse_distance_unit(d.pop("distance_unit", UNSET))

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTagRequest.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, CircuitRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CircuitRequestCustomFields.from_dict(_custom_fields)

        assignments = []
        _assignments = d.pop("assignments", UNSET)
        for assignments_item_data in _assignments or []:
            assignments_item = BriefCircuitGroupAssignmentSerializerRequest.from_dict(assignments_item_data)

            assignments.append(assignments_item)

        circuit_request = cls(
            cid=cid,
            provider=provider,
            type_=type_,
            provider_account=provider_account,
            status=status,
            tenant=tenant,
            install_date=install_date,
            termination_date=termination_date,
            commit_rate=commit_rate,
            description=description,
            distance=distance,
            distance_unit=distance_unit,
            comments=comments,
            tags=tags,
            custom_fields=custom_fields,
            assignments=assignments,
        )

        circuit_request.additional_properties = d
        return circuit_request

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
