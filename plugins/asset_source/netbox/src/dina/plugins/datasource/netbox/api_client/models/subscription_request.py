import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.brief_user_request import BriefUserRequest


T = TypeVar("T", bound="SubscriptionRequest")


@_attrs_define
class SubscriptionRequest:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            object_type (str):
            object_id (int):
            user (Union['BriefUserRequest', int]):
    """

    object_type: str
    object_id: int
    user: Union["BriefUserRequest", int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_user_request import BriefUserRequest

        object_type = self.object_type

        object_id = self.object_id

        user: Union[dict[str, Any], int]
        if isinstance(self.user, BriefUserRequest):
            user = self.user.to_dict()
        else:
            user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_type": object_type,
                "object_id": object_id,
                "user": user,
            }
        )

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        object_type = (None, str(self.object_type).encode(), "text/plain")

        object_id = (None, str(self.object_id).encode(), "text/plain")

        user: tuple[None, bytes, str]

        if isinstance(self.user, int):
            user = (None, str(self.user).encode(), "text/plain")
        else:
            user = (None, json.dumps(self.user.to_dict()).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "object_type": object_type,
                "object_id": object_id,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_user_request import BriefUserRequest

        d = dict(src_dict)
        object_type = d.pop("object_type")

        object_id = d.pop("object_id")

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

        subscription_request = cls(
            object_type=object_type,
            object_id=object_id,
            user=user,
        )

        subscription_request.additional_properties = d
        return subscription_request

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
