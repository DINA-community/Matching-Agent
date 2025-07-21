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
    from ..models.brief_power_port_template import BriefPowerPortTemplate
    from ..models.power_outlet_template_feed_leg_type_0 import (
        PowerOutletTemplateFeedLegType0,
    )
    from ..models.power_outlet_template_type_type_0 import PowerOutletTemplateTypeType0


T = TypeVar("T", bound="PowerOutletTemplate")


@_attrs_define
class PowerOutletTemplate:
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
            type_ (Union['PowerOutletTemplateTypeType0', None, Unset]):
            power_port (Union['BriefPowerPortTemplate', None, Unset]):
            feed_leg (Union['PowerOutletTemplateFeedLegType0', None, Unset]):
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
    type_: Union["PowerOutletTemplateTypeType0", None, Unset] = UNSET
    power_port: Union["BriefPowerPortTemplate", None, Unset] = UNSET
    feed_leg: Union["PowerOutletTemplateFeedLegType0", None, Unset] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device_type import BriefDeviceType
        from ..models.brief_module_type import BriefModuleType
        from ..models.brief_power_port_template import BriefPowerPortTemplate
        from ..models.power_outlet_template_feed_leg_type_0 import (
            PowerOutletTemplateFeedLegType0,
        )
        from ..models.power_outlet_template_type_type_0 import (
            PowerOutletTemplateTypeType0,
        )

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

        type_: Union[None, Unset, dict[str, Any]]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, PowerOutletTemplateTypeType0):
            type_ = self.type_.to_dict()
        else:
            type_ = self.type_

        power_port: Union[None, Unset, dict[str, Any]]
        if isinstance(self.power_port, Unset):
            power_port = UNSET
        elif isinstance(self.power_port, BriefPowerPortTemplate):
            power_port = self.power_port.to_dict()
        else:
            power_port = self.power_port

        feed_leg: Union[None, Unset, dict[str, Any]]
        if isinstance(self.feed_leg, Unset):
            feed_leg = UNSET
        elif isinstance(self.feed_leg, PowerOutletTemplateFeedLegType0):
            feed_leg = self.feed_leg.to_dict()
        else:
            feed_leg = self.feed_leg

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
        if power_port is not UNSET:
            field_dict["power_port"] = power_port
        if feed_leg is not UNSET:
            field_dict["feed_leg"] = feed_leg
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_device_type import BriefDeviceType
        from ..models.brief_module_type import BriefModuleType
        from ..models.brief_power_port_template import BriefPowerPortTemplate
        from ..models.power_outlet_template_feed_leg_type_0 import (
            PowerOutletTemplateFeedLegType0,
        )
        from ..models.power_outlet_template_type_type_0 import (
            PowerOutletTemplateTypeType0,
        )

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

        def _parse_type_(
            data: object,
        ) -> Union["PowerOutletTemplateTypeType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                type_type_0 = PowerOutletTemplateTypeType0.from_dict(data)

                return type_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PowerOutletTemplateTypeType0", None, Unset], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_power_port(
            data: object,
        ) -> Union["BriefPowerPortTemplate", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                power_port_type_1 = BriefPowerPortTemplate.from_dict(data)

                return power_port_type_1
            except:  # noqa: E722
                pass
            return cast(Union["BriefPowerPortTemplate", None, Unset], data)

        power_port = _parse_power_port(d.pop("power_port", UNSET))

        def _parse_feed_leg(
            data: object,
        ) -> Union["PowerOutletTemplateFeedLegType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                feed_leg_type_0 = PowerOutletTemplateFeedLegType0.from_dict(data)

                return feed_leg_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PowerOutletTemplateFeedLegType0", None, Unset], data)

        feed_leg = _parse_feed_leg(d.pop("feed_leg", UNSET))

        description = d.pop("description", UNSET)

        power_outlet_template = cls(
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
            power_port=power_port,
            feed_leg=feed_leg,
            description=description,
        )

        power_outlet_template.additional_properties = d
        return power_outlet_template

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
