import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.notification_event import NotificationEvent
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_user import BriefUser


T = TypeVar("T", bound="Notification")


@_attrs_define
class Notification:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            id (int):
            url (str):
            display (str):
            object_type (str):
            object_id (int):
            object_ (Any):
            user (BriefUser): Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the
                associated instance during
                validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)
            created (datetime.datetime):
            event_type (NotificationEvent): * `object_created` - Object created
                * `object_updated` - Object updated
                * `object_deleted` - Object deleted
                * `job_started` - Job started
                * `job_completed` - Job completed
                * `job_failed` - Job failed
                * `job_errored` - Job errored
            read (Union[None, Unset, datetime.datetime]):
    """

    id: int
    url: str
    display: str
    object_type: str
    object_id: int
    object_: Any
    user: "BriefUser"
    created: datetime.datetime
    event_type: NotificationEvent
    read: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display = self.display

        object_type = self.object_type

        object_id = self.object_id

        object_ = self.object_

        user = self.user.to_dict()

        created = self.created.isoformat()

        event_type = self.event_type.value

        read: Union[None, Unset, str]
        if isinstance(self.read, Unset):
            read = UNSET
        elif isinstance(self.read, datetime.datetime):
            read = self.read.isoformat()
        else:
            read = self.read

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "object_type": object_type,
                "object_id": object_id,
                "object": object_,
                "user": user,
                "created": created,
                "event_type": event_type,
            }
        )
        if read is not UNSET:
            field_dict["read"] = read

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_user import BriefUser

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        object_type = d.pop("object_type")

        object_id = d.pop("object_id")

        object_ = d.pop("object")

        user = BriefUser.from_dict(d.pop("user"))

        created = isoparse(d.pop("created"))

        event_type = NotificationEvent(d.pop("event_type"))

        def _parse_read(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                read_type_0 = isoparse(data)

                return read_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        read = _parse_read(d.pop("read", UNSET))

        notification = cls(
            id=id,
            url=url,
            display=display,
            object_type=object_type,
            object_id=object_id,
            object_=object_,
            user=user,
            created=created,
            event_type=event_type,
            read=read,
        )

        notification.additional_properties = d
        return notification

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
