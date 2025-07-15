import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.brief_user import BriefUser
    from ..models.object_change_action import ObjectChangeAction


T = TypeVar("T", bound="ObjectChange")


@_attrs_define
class ObjectChange:
    """
    Attributes:
        id (int):
        url (str):
        display_url (str):
        display (str):
        time (datetime.datetime):
        user (BriefUser): Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the
            associated instance during
            validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)
        user_name (str):
        request_id (UUID):
        action (ObjectChangeAction):
        changed_object_type (str):
        changed_object_id (int):
        changed_object (Any):
        prechange_data (Any):
        postchange_data (Any):
    """

    id: int
    url: str
    display_url: str
    display: str
    time: datetime.datetime
    user: "BriefUser"
    user_name: str
    request_id: UUID
    action: "ObjectChangeAction"
    changed_object_type: str
    changed_object_id: int
    changed_object: Any
    prechange_data: Any
    postchange_data: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        display = self.display

        time = self.time.isoformat()

        user = self.user.to_dict()

        user_name = self.user_name

        request_id = str(self.request_id)

        action = self.action.to_dict()

        changed_object_type = self.changed_object_type

        changed_object_id = self.changed_object_id

        changed_object = self.changed_object

        prechange_data = self.prechange_data

        postchange_data = self.postchange_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "display": display,
                "time": time,
                "user": user,
                "user_name": user_name,
                "request_id": request_id,
                "action": action,
                "changed_object_type": changed_object_type,
                "changed_object_id": changed_object_id,
                "changed_object": changed_object,
                "prechange_data": prechange_data,
                "postchange_data": postchange_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_user import BriefUser
        from ..models.object_change_action import ObjectChangeAction

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        display = d.pop("display")

        time = isoparse(d.pop("time"))

        user = BriefUser.from_dict(d.pop("user"))

        user_name = d.pop("user_name")

        request_id = UUID(d.pop("request_id"))

        action = ObjectChangeAction.from_dict(d.pop("action"))

        changed_object_type = d.pop("changed_object_type")

        changed_object_id = d.pop("changed_object_id")

        changed_object = d.pop("changed_object")

        prechange_data = d.pop("prechange_data")

        postchange_data = d.pop("postchange_data")

        object_change = cls(
            id=id,
            url=url,
            display_url=display_url,
            display=display,
            time=time,
            user=user,
            user_name=user_name,
            request_id=request_id,
            action=action,
            changed_object_type=changed_object_type,
            changed_object_id=changed_object_id,
            changed_object=changed_object,
            prechange_data=prechange_data,
            postchange_data=postchange_data,
        )

        object_change.additional_properties = d
        return object_change

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
