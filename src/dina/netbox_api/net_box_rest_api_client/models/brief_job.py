import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_job_status import BriefJobStatus
    from ..models.brief_user import BriefUser


T = TypeVar("T", bound="BriefJob")


@_attrs_define
class BriefJob:
    """
    Attributes:
        url (str):
        status (BriefJobStatus):
        created (datetime.datetime):
        user (BriefUser): Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the
            associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)
        completed (Union[None, Unset, datetime.datetime]):
    """

    url: str
    status: "BriefJobStatus"
    created: datetime.datetime
    user: "BriefUser"
    completed: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        status = self.status.to_dict()

        created = self.created.isoformat()

        user = self.user.to_dict()

        completed: Union[None, Unset, str]
        if isinstance(self.completed, Unset):
            completed = UNSET
        elif isinstance(self.completed, datetime.datetime):
            completed = self.completed.isoformat()
        else:
            completed = self.completed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "status": status,
                "created": created,
                "user": user,
            }
        )
        if completed is not UNSET:
            field_dict["completed"] = completed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_job_status import BriefJobStatus
        from ..models.brief_user import BriefUser

        d = dict(src_dict)
        url = d.pop("url")

        status = BriefJobStatus.from_dict(d.pop("status"))

        created = isoparse(d.pop("created"))

        user = BriefUser.from_dict(d.pop("user"))

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

        brief_job = cls(
            url=url,
            status=status,
            created=created,
            user=user,
            completed=completed,
        )

        brief_job.additional_properties = d
        return brief_job

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
