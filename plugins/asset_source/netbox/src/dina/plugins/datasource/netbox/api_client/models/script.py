from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.brief_job import BriefJob


T = TypeVar("T", bound="Script")


@_attrs_define
class Script:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            id (int):
            url (str):
            display_url (str):
            module (int):
            name (str):
            description (Union[None, str]):
            vars_ (Any):
            result (BriefJob):
            display (str):
            is_executable (bool):
    """

    id: int
    url: str
    display_url: str
    module: int
    name: str
    description: Union[None, str]
    vars_: Any
    result: "BriefJob"
    display: str
    is_executable: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        display_url = self.display_url

        module = self.module

        name = self.name

        description: Union[None, str]
        description = self.description

        vars_ = self.vars_

        result = self.result.to_dict()

        display = self.display

        is_executable = self.is_executable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display_url": display_url,
                "module": module,
                "name": name,
                "description": description,
                "vars": vars_,
                "result": result,
                "display": display,
                "is_executable": is_executable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_job import BriefJob

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display_url = d.pop("display_url")

        module = d.pop("module")

        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        vars_ = d.pop("vars")

        result = BriefJob.from_dict(d.pop("result"))

        display = d.pop("display")

        is_executable = d.pop("is_executable")

        script = cls(
            id=id,
            url=url,
            display_url=display_url,
            module=module,
            name=name,
            description=description,
            vars_=vars_,
            result=result,
            display=display,
            is_executable=is_executable,
        )

        script.additional_properties = d
        return script

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
