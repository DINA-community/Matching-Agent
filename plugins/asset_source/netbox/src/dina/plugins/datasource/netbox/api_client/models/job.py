import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_user import BriefUser
    from ..models.job_status import JobStatus


T = TypeVar("T", bound="Job")


@_attrs_define
class Job:
    """
    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        object_type (str):
        name (str):
        status (JobStatus):
        created (datetime.datetime):
        user (BriefUser): Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the
            associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)
        error (str):
        job_id (UUID):
        object_id (Union[None, Unset, int]):
        scheduled (Union[None, Unset, datetime.datetime]):
        interval (Union[None, Unset, int]): Recurrence interval (in minutes)
        started (Union[None, Unset, datetime.datetime]):
        completed (Union[None, Unset, datetime.datetime]):
        data (Union[Unset, Any]):
    """

    id: int
    url: str
    display_url: str
    display: str
    object_type: str
    name: str
    status: "JobStatus"
    created: datetime.datetime
    user: "BriefUser"
    error: str
    job_id: UUID
    object_id: Union[None, Unset, int] = UNSET
    scheduled: Union[None, Unset, datetime.datetime] = UNSET
    interval: Union[None, Unset, int] = UNSET
    started: Union[None, Unset, datetime.datetime] = UNSET
    completed: Union[None, Unset, datetime.datetime] = UNSET
    data: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        object_type = self.object_type

        name = self.name

        status = self.status.to_dict()

        created = self.created.isoformat()

        user = self.user.to_dict()

        error = self.error

        job_id = str(self.job_id)

        object_id: Union[None, Unset, int]
        if isinstance(self.object_id, Unset):
            object_id = UNSET
        else:
            object_id = self.object_id

        scheduled: Union[None, Unset, str]
        if isinstance(self.scheduled, Unset):
            scheduled = UNSET
        elif isinstance(self.scheduled, datetime.datetime):
            scheduled = self.scheduled.isoformat()
        else:
            scheduled = self.scheduled

        interval: Union[None, Unset, int]
        if isinstance(self.interval, Unset):
            interval = UNSET
        else:
            interval = self.interval

        started: Union[None, Unset, str]
        if isinstance(self.started, Unset):
            started = UNSET
        elif isinstance(self.started, datetime.datetime):
            started = self.started.isoformat()
        else:
            started = self.started

        completed: Union[None, Unset, str]
        if isinstance(self.completed, Unset):
            completed = UNSET
        elif isinstance(self.completed, datetime.datetime):
            completed = self.completed.isoformat()
        else:
            completed = self.completed

        data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "object_type": object_type,
                "name": name,
                "status": status,
                "created": created,
                "user": user,
                "error": error,
                "job_id": job_id,
            }
        )
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if scheduled is not UNSET:
            field_dict["scheduled"] = scheduled
        if interval is not UNSET:
            field_dict["interval"] = interval
        if started is not UNSET:
            field_dict["started"] = started
        if completed is not UNSET:
            field_dict["completed"] = completed
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_user import BriefUser
        from ..models.job_status import JobStatus

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        object_type = d.pop("object_type")

        name = d.pop("name")

        status = JobStatus.from_dict(d.pop("status"))

        created = isoparse(d.pop("created"))

        user = BriefUser.from_dict(d.pop("user"))

        error = d.pop("error")

        job_id = UUID(d.pop("job_id"))

        def _parse_object_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        object_id = _parse_object_id(d.pop("object_id", UNSET))

        def _parse_scheduled(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_type_0 = isoparse(data)

                return scheduled_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        scheduled = _parse_scheduled(d.pop("scheduled", UNSET))

        def _parse_interval(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        interval = _parse_interval(d.pop("interval", UNSET))

        def _parse_started(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_type_0 = isoparse(data)

                return started_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        started = _parse_started(d.pop("started", UNSET))

        def _parse_completed(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_type_0 = isoparse(data)

                return completed_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        completed = _parse_completed(d.pop("completed", UNSET))

        data = d.pop("data", UNSET)

        job = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            object_type=object_type,
            name=name,
            status=status,
            created=created,
            user=user,
            error=error,
            job_id=job_id,
            object_id=object_id,
            scheduled=scheduled,
            interval=interval,
            started=started,
            completed=completed,
            data=data,
        )

        job.additional_properties = d
        return job

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
