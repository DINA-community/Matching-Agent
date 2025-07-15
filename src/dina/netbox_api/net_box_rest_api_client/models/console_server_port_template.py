import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_device_type import BriefDeviceType
    from ..models.brief_module_type import BriefModuleType
    from ..models.console_server_port_template_type import ConsoleServerPortTemplateType


T = TypeVar("T", bound="ConsoleServerPortTemplate")


@_attrs_define
class ConsoleServerPortTemplate:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            id (int):
            url (str):
            display (str):
            name (str): {module} is accepted as a substitution for the module bay position when attached to a module type.
            created (Union[None, datetime.datetime]):
            last_updated (Union[None, datetime.datetime]):
            device_type (Union['BriefDeviceType', None, Unset]):
            module_type (Union['BriefModuleType', None, Unset]):
            label (Union[Unset, str]): Physical label
            type_ (Union[Unset, ConsoleServerPortTemplateType]):
            description (Union[Unset, str]):
    """

    id: int
    url: str
    display: str
    name: str
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    device_type: Union["BriefDeviceType", None, Unset] = UNSET
    module_type: Union["BriefModuleType", None, Unset] = UNSET
    label: Union[Unset, str] = UNSET
    type_: Union[Unset, "ConsoleServerPortTemplateType"] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device_type import BriefDeviceType
        from ..models.brief_module_type import BriefModuleType

        id = self.id

        url = self.url

        display = self.display

        name = self.name

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

        device_type: Union[None, Unset, dict[str, Any]]
        if isinstance(self.device_type, Unset):
            device_type = UNSET
        elif isinstance(self.device_type, BriefDeviceType):
            device_type = self.device_type.to_dict()
        else:
            device_type = self.device_type

        module_type: Union[None, Unset, dict[str, Any]]
        if isinstance(self.module_type, Unset):
            module_type = UNSET
        elif isinstance(self.module_type, BriefModuleType):
            module_type = self.module_type.to_dict()
        else:
            module_type = self.module_type

        label = self.label

        type_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "name": name,
                "created": created,
                "last_updated": last_updated,
            }
        )
        if device_type is not UNSET:
            field_dict["device_type"] = device_type
        if module_type is not UNSET:
            field_dict["module_type"] = module_type
        if label is not UNSET:
            field_dict["label"] = label
        if type_ is not UNSET:
            field_dict["type"] = type_
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_device_type import BriefDeviceType
        from ..models.brief_module_type import BriefModuleType
        from ..models.console_server_port_template_type import ConsoleServerPortTemplateType

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        name = d.pop("name")

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

        def _parse_device_type(data: object) -> Union["BriefDeviceType", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_type_type_1 = BriefDeviceType.from_dict(data)

                return device_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefDeviceType", None, Unset], data)

        device_type = _parse_device_type(d.pop("device_type", UNSET))

        def _parse_module_type(data: object) -> Union["BriefModuleType", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                module_type_type_1 = BriefModuleType.from_dict(data)

                return module_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefModuleType", None, Unset], data)

        module_type = _parse_module_type(d.pop("module_type", UNSET))

        label = d.pop("label", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ConsoleServerPortTemplateType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ConsoleServerPortTemplateType.from_dict(_type_)

        description = d.pop("description", UNSET)

        console_server_port_template = cls(
            id=id,
            url=url,
            display=display,
            name=name,
            created=created,
            last_updated=last_updated,
            device_type=device_type,
            module_type=module_type,
            label=label,
            type_=type_,
            description=description,
        )

        console_server_port_template.additional_properties = d
        return console_server_port_template

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
