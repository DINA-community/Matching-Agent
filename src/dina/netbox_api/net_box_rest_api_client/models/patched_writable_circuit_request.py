import datetime
import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.patched_writable_circuit_request_distance_unit_type_1 import (
    PatchedWritableCircuitRequestDistanceUnitType1,
)
from ..models.patched_writable_circuit_request_distance_unit_type_2_type_1 import (
    PatchedWritableCircuitRequestDistanceUnitType2Type1,
)
from ..models.patched_writable_circuit_request_distance_unit_type_3_type_1 import (
    PatchedWritableCircuitRequestDistanceUnitType3Type1,
)
from ..models.patched_writable_circuit_request_status import PatchedWritableCircuitRequestStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_circuit_group_assignment_serializer_request import BriefCircuitGroupAssignmentSerializerRequest
    from ..models.brief_circuit_type_request import BriefCircuitTypeRequest
    from ..models.brief_provider_account_request import BriefProviderAccountRequest
    from ..models.brief_provider_request import BriefProviderRequest
    from ..models.brief_tenant_request import BriefTenantRequest
    from ..models.nested_tag_request import NestedTagRequest
    from ..models.patched_writable_circuit_request_custom_fields import PatchedWritableCircuitRequestCustomFields


T = TypeVar("T", bound="PatchedWritableCircuitRequest")


@_attrs_define
class PatchedWritableCircuitRequest:
    """Adds support for custom fields and tags.

    Attributes:
        cid (Union[Unset, str]): Unique circuit ID
        provider (Union['BriefProviderRequest', Unset, int]):
        provider_account (Union['BriefProviderAccountRequest', None, Unset, int]):
        type_ (Union['BriefCircuitTypeRequest', Unset, int]):
        status (Union[Unset, PatchedWritableCircuitRequestStatus]): * `planned` - Planned
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
        distance_unit (Union[None, PatchedWritableCircuitRequestDistanceUnitType1,
            PatchedWritableCircuitRequestDistanceUnitType2Type1, PatchedWritableCircuitRequestDistanceUnitType3Type1,
            Unset]): * `km` - Kilometers
            * `m` - Meters
            * `mi` - Miles
            * `ft` - Feet
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTagRequest']]):
        custom_fields (Union[Unset, PatchedWritableCircuitRequestCustomFields]):
        assignments (Union[Unset, list['BriefCircuitGroupAssignmentSerializerRequest']]):
    """

    cid: Union[Unset, str] = UNSET
    provider: Union["BriefProviderRequest", Unset, int] = UNSET
    provider_account: Union["BriefProviderAccountRequest", None, Unset, int] = UNSET
    type_: Union["BriefCircuitTypeRequest", Unset, int] = UNSET
    status: Union[Unset, PatchedWritableCircuitRequestStatus] = UNSET
    tenant: Union["BriefTenantRequest", None, Unset, int] = UNSET
    install_date: Union[None, Unset, datetime.date] = UNSET
    termination_date: Union[None, Unset, datetime.date] = UNSET
    commit_rate: Union[None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    distance: Union[None, Unset, float] = UNSET
    distance_unit: Union[
        None,
        PatchedWritableCircuitRequestDistanceUnitType1,
        PatchedWritableCircuitRequestDistanceUnitType2Type1,
        PatchedWritableCircuitRequestDistanceUnitType3Type1,
        Unset,
    ] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTagRequest"]] = UNSET
    custom_fields: Union[Unset, "PatchedWritableCircuitRequestCustomFields"] = UNSET
    assignments: Union[Unset, list["BriefCircuitGroupAssignmentSerializerRequest"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_circuit_type_request import BriefCircuitTypeRequest
        from ..models.brief_provider_account_request import BriefProviderAccountRequest
        from ..models.brief_provider_request import BriefProviderRequest
        from ..models.brief_tenant_request import BriefTenantRequest

        cid = self.cid

        provider: Union[Unset, dict[str, Any], int]
        if isinstance(self.provider, Unset):
            provider = UNSET
        elif isinstance(self.provider, BriefProviderRequest):
            provider = self.provider.to_dict()
        else:
            provider = self.provider

        provider_account: Union[None, Unset, dict[str, Any], int]
        if isinstance(self.provider_account, Unset):
            provider_account = UNSET
        elif isinstance(self.provider_account, BriefProviderAccountRequest):
            provider_account = self.provider_account.to_dict()
        else:
            provider_account = self.provider_account

        type_: Union[Unset, dict[str, Any], int]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, BriefCircuitTypeRequest):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

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
        elif isinstance(self.distance_unit, PatchedWritableCircuitRequestDistanceUnitType1):
            distance_unit = self.distance_unit.value
        elif isinstance(self.distance_unit, PatchedWritableCircuitRequestDistanceUnitType2Type1):
            distance_unit = self.distance_unit.value
        elif isinstance(self.distance_unit, PatchedWritableCircuitRequestDistanceUnitType3Type1):
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
        field_dict.update({})
        if cid is not UNSET:
            field_dict["cid"] = cid
        if provider is not UNSET:
            field_dict["provider"] = provider
        if provider_account is not UNSET:
            field_dict["provider_account"] = provider_account
        if type_ is not UNSET:
            field_dict["type"] = type_
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

    def to_multipart(self) -> dict[str, Any]:
        cid = self.cid if isinstance(self.cid, Unset) else (None, str(self.cid).encode(), "text/plain")

        provider: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.provider, Unset):
            provider = UNSET
        elif isinstance(self.provider, int):
            provider = (None, str(self.provider).encode(), "text/plain")
        else:
            provider = (None, json.dumps(self.provider.to_dict()).encode(), "application/json")

        provider_account: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.provider_account, Unset):
            provider_account = UNSET
        elif isinstance(self.provider_account, int):
            provider_account = (None, str(self.provider_account).encode(), "text/plain")
        elif isinstance(self.provider_account, None):
            provider_account = (None, str(self.provider_account).encode(), "text/plain")
        elif isinstance(self.provider_account, BriefProviderAccountRequest):
            provider_account = (None, json.dumps(self.provider_account.to_dict()).encode(), "application/json")
        else:
            provider_account = (None, str(self.provider_account).encode(), "text/plain")

        type_: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, int):
            type_ = (None, str(self.type_).encode(), "text/plain")
        else:
            type_ = (None, json.dumps(self.type_.to_dict()).encode(), "application/json")

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
            tenant = (None, json.dumps(self.tenant.to_dict()).encode(), "application/json")
        else:
            tenant = (None, str(self.tenant).encode(), "text/plain")

        install_date: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.install_date, Unset):
            install_date = UNSET
        elif isinstance(self.install_date, datetime.date):
            install_date = self.install_date.isoformat().encode()
        else:
            install_date = (None, str(self.install_date).encode(), "text/plain")

        termination_date: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.termination_date, Unset):
            termination_date = UNSET
        elif isinstance(self.termination_date, datetime.date):
            termination_date = self.termination_date.isoformat().encode()
        else:
            termination_date = (None, str(self.termination_date).encode(), "text/plain")

        commit_rate: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.commit_rate, Unset):
            commit_rate = UNSET
        elif isinstance(self.commit_rate, int):
            commit_rate = (None, str(self.commit_rate).encode(), "text/plain")
        else:
            commit_rate = (None, str(self.commit_rate).encode(), "text/plain")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )

        distance: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.distance, Unset):
            distance = UNSET
        elif isinstance(self.distance, float):
            distance = (None, str(self.distance).encode(), "text/plain")
        else:
            distance = (None, str(self.distance).encode(), "text/plain")

        distance_unit: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.distance_unit, Unset):
            distance_unit = UNSET
        elif isinstance(self.distance_unit, None):
            distance_unit = (None, str(self.distance_unit).encode(), "text/plain")
        elif isinstance(self.distance_unit, PatchedWritableCircuitRequestDistanceUnitType1):
            distance_unit = (None, str(self.distance_unit.value).encode(), "text/plain")
        elif isinstance(self.distance_unit, None):
            distance_unit = (None, str(self.distance_unit).encode(), "text/plain")
        elif isinstance(self.distance_unit, PatchedWritableCircuitRequestDistanceUnitType2Type1):
            distance_unit = (None, str(self.distance_unit.value).encode(), "text/plain")
        elif isinstance(self.distance_unit, None):
            distance_unit = (None, str(self.distance_unit).encode(), "text/plain")
        else:
            distance_unit = (None, str(self.distance_unit.value).encode(), "text/plain")

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

        assignments: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.assignments, Unset):
            _temp_assignments = []
            for assignments_item_data in self.assignments:
                assignments_item = assignments_item_data.to_dict()
                _temp_assignments.append(assignments_item)
            assignments = (None, json.dumps(_temp_assignments).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if cid is not UNSET:
            field_dict["cid"] = cid
        if provider is not UNSET:
            field_dict["provider"] = provider
        if provider_account is not UNSET:
            field_dict["provider_account"] = provider_account
        if type_ is not UNSET:
            field_dict["type"] = type_
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
        from ..models.nested_tag_request import NestedTagRequest
        from ..models.patched_writable_circuit_request_custom_fields import PatchedWritableCircuitRequestCustomFields

        d = dict(src_dict)
        cid = d.pop("cid", UNSET)

        def _parse_provider(data: object) -> Union["BriefProviderRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_type_1 = BriefProviderRequest.from_dict(data)

                return provider_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefProviderRequest", Unset, int], data)

        provider = _parse_provider(d.pop("provider", UNSET))

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

        def _parse_type_(data: object) -> Union["BriefCircuitTypeRequest", Unset, int]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                type_type_1 = BriefCircuitTypeRequest.from_dict(data)

                return type_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefCircuitTypeRequest", Unset, int], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, PatchedWritableCircuitRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PatchedWritableCircuitRequestStatus(_status)

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
            None,
            PatchedWritableCircuitRequestDistanceUnitType1,
            PatchedWritableCircuitRequestDistanceUnitType2Type1,
            PatchedWritableCircuitRequestDistanceUnitType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                distance_unit_type_1 = PatchedWritableCircuitRequestDistanceUnitType1(data)

                return distance_unit_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                distance_unit_type_2_type_1 = PatchedWritableCircuitRequestDistanceUnitType2Type1(data)

                return distance_unit_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                distance_unit_type_3_type_1 = PatchedWritableCircuitRequestDistanceUnitType3Type1(data)

                return distance_unit_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    PatchedWritableCircuitRequestDistanceUnitType1,
                    PatchedWritableCircuitRequestDistanceUnitType2Type1,
                    PatchedWritableCircuitRequestDistanceUnitType3Type1,
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
        custom_fields: Union[Unset, PatchedWritableCircuitRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PatchedWritableCircuitRequestCustomFields.from_dict(_custom_fields)

        assignments = []
        _assignments = d.pop("assignments", UNSET)
        for assignments_item_data in _assignments or []:
            assignments_item = BriefCircuitGroupAssignmentSerializerRequest.from_dict(assignments_item_data)

            assignments.append(assignments_item)

        patched_writable_circuit_request = cls(
            cid=cid,
            provider=provider,
            provider_account=provider_account,
            type_=type_,
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

        patched_writable_circuit_request.additional_properties = d
        return patched_writable_circuit_request

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
