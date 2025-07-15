import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_circuit_group_assignment_serializer import BriefCircuitGroupAssignmentSerializer
    from ..models.brief_circuit_type import BriefCircuitType
    from ..models.brief_provider import BriefProvider
    from ..models.brief_provider_account import BriefProviderAccount
    from ..models.brief_tenant import BriefTenant
    from ..models.circuit_circuit_termination import CircuitCircuitTermination
    from ..models.circuit_custom_fields import CircuitCustomFields
    from ..models.circuit_distance_unit_type_0 import CircuitDistanceUnitType0
    from ..models.circuit_status import CircuitStatus
    from ..models.nested_tag import NestedTag


T = TypeVar("T", bound="Circuit")


@_attrs_define
class Circuit:
    """Adds support for custom fields and tags.

    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        cid (str): Unique circuit ID
        provider (BriefProvider): Adds support for custom fields and tags.
        type_ (BriefCircuitType): Adds support for custom fields and tags.
        termination_a (Union['CircuitCircuitTermination', None]):
        termination_z (Union['CircuitCircuitTermination', None]):
        created (Union[None, datetime.datetime]):
        last_updated (Union[None, datetime.datetime]):
        provider_account (Union['BriefProviderAccount', None, Unset]):
        status (Union[Unset, CircuitStatus]):
        tenant (Union['BriefTenant', None, Unset]):
        install_date (Union[None, Unset, datetime.date]):
        termination_date (Union[None, Unset, datetime.date]):
        commit_rate (Union[None, Unset, int]): Committed rate
        description (Union[Unset, str]):
        distance (Union[None, Unset, float]):
        distance_unit (Union['CircuitDistanceUnitType0', None, Unset]):
        comments (Union[Unset, str]):
        tags (Union[Unset, list['NestedTag']]):
        custom_fields (Union[Unset, CircuitCustomFields]):
        assignments (Union[Unset, list['BriefCircuitGroupAssignmentSerializer']]):
    """

    id: int
    url: str
    display_url: str
    display: str
    cid: str
    provider: "BriefProvider"
    type_: "BriefCircuitType"
    termination_a: Union["CircuitCircuitTermination", None]
    termination_z: Union["CircuitCircuitTermination", None]
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    provider_account: Union["BriefProviderAccount", None, Unset] = UNSET
    status: Union[Unset, "CircuitStatus"] = UNSET
    tenant: Union["BriefTenant", None, Unset] = UNSET
    install_date: Union[None, Unset, datetime.date] = UNSET
    termination_date: Union[None, Unset, datetime.date] = UNSET
    commit_rate: Union[None, Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    distance: Union[None, Unset, float] = UNSET
    distance_unit: Union["CircuitDistanceUnitType0", None, Unset] = UNSET
    comments: Union[Unset, str] = UNSET
    tags: Union[Unset, list["NestedTag"]] = UNSET
    custom_fields: Union[Unset, "CircuitCustomFields"] = UNSET
    assignments: Union[Unset, list["BriefCircuitGroupAssignmentSerializer"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_provider_account import BriefProviderAccount
        from ..models.brief_tenant import BriefTenant
        from ..models.circuit_circuit_termination import CircuitCircuitTermination
        from ..models.circuit_distance_unit_type_0 import CircuitDistanceUnitType0

        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        cid = self.cid

        provider = self.provider.to_dict()

        type_ = self.type_.to_dict()

        termination_a: Union[None, dict[str, Any]]
        if isinstance(self.termination_a, CircuitCircuitTermination):
            termination_a = self.termination_a.to_dict()
        else:
            termination_a = self.termination_a

        termination_z: Union[None, dict[str, Any]]
        if isinstance(self.termination_z, CircuitCircuitTermination):
            termination_z = self.termination_z.to_dict()
        else:
            termination_z = self.termination_z

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

        provider_account: Union[None, Unset, dict[str, Any]]
        if isinstance(self.provider_account, Unset):
            provider_account = UNSET
        elif isinstance(self.provider_account, BriefProviderAccount):
            provider_account = self.provider_account.to_dict()
        else:
            provider_account = self.provider_account

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

        distance_unit: Union[None, Unset, dict[str, Any]]
        if isinstance(self.distance_unit, Unset):
            distance_unit = UNSET
        elif isinstance(self.distance_unit, CircuitDistanceUnitType0):
            distance_unit = self.distance_unit.to_dict()
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
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "cid": cid,
                "provider": provider,
                "type": type_,
                "termination_a": termination_a,
                "termination_z": termination_z,
                "created": created,
                "last_updated": last_updated,
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
        from ..models.brief_circuit_group_assignment_serializer import BriefCircuitGroupAssignmentSerializer
        from ..models.brief_circuit_type import BriefCircuitType
        from ..models.brief_provider import BriefProvider
        from ..models.brief_provider_account import BriefProviderAccount
        from ..models.brief_tenant import BriefTenant
        from ..models.circuit_circuit_termination import CircuitCircuitTermination
        from ..models.circuit_custom_fields import CircuitCustomFields
        from ..models.circuit_distance_unit_type_0 import CircuitDistanceUnitType0
        from ..models.circuit_status import CircuitStatus
        from ..models.nested_tag import NestedTag

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        cid = d.pop("cid")

        provider = BriefProvider.from_dict(d.pop("provider"))

        type_ = BriefCircuitType.from_dict(d.pop("type"))

        def _parse_termination_a(data: object) -> Union["CircuitCircuitTermination", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                termination_a_type_1 = CircuitCircuitTermination.from_dict(data)

                return termination_a_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CircuitCircuitTermination", None], data)

        termination_a = _parse_termination_a(d.pop("termination_a"))

        def _parse_termination_z(data: object) -> Union["CircuitCircuitTermination", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                termination_z_type_1 = CircuitCircuitTermination.from_dict(data)

                return termination_z_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CircuitCircuitTermination", None], data)

        termination_z = _parse_termination_z(d.pop("termination_z"))

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

        def _parse_provider_account(data: object) -> Union["BriefProviderAccount", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_account_type_1 = BriefProviderAccount.from_dict(data)

                return provider_account_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefProviderAccount", None, Unset], data)

        provider_account = _parse_provider_account(d.pop("provider_account", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, CircuitStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CircuitStatus.from_dict(_status)

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

        def _parse_distance_unit(data: object) -> Union["CircuitDistanceUnitType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                distance_unit_type_0 = CircuitDistanceUnitType0.from_dict(data)

                return distance_unit_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CircuitDistanceUnitType0", None, Unset], data)

        distance_unit = _parse_distance_unit(d.pop("distance_unit", UNSET))

        comments = d.pop("comments", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = NestedTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: Union[Unset, CircuitCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CircuitCustomFields.from_dict(_custom_fields)

        assignments = []
        _assignments = d.pop("assignments", UNSET)
        for assignments_item_data in _assignments or []:
            assignments_item = BriefCircuitGroupAssignmentSerializer.from_dict(assignments_item_data)

            assignments.append(assignments_item)

        circuit = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            cid=cid,
            provider=provider,
            type_=type_,
            termination_a=termination_a,
            termination_z=termination_z,
            created=created,
            last_updated=last_updated,
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

        circuit.additional_properties = d
        return circuit

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
