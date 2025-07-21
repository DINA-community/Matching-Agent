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
    from ..models.interface_template_poe_mode_type_0 import (
        InterfaceTemplatePoeModeType0,
    )
    from ..models.interface_template_poe_type_type_0 import (
        InterfaceTemplatePoeTypeType0,
    )
    from ..models.interface_template_rf_role_type_0 import InterfaceTemplateRfRoleType0
    from ..models.interface_template_type import InterfaceTemplateType
    from ..models.nested_interface_template import NestedInterfaceTemplate


T = TypeVar("T", bound="InterfaceTemplate")


@_attrs_define
class InterfaceTemplate:
    """Extends the built-in ModelSerializer to enforce calling full_clean() on a copy of the associated instance during
    validation. (DRF does not do this by default; see https://github.com/encode/django-rest-framework/issues/3144)

        Attributes:
            id (int):
            url (str):
            display (str):
            name (str): {module} is accepted as a substitution for the module bay position when attached to a module type.
            type_ (InterfaceTemplateType):
            created (Union[None, datetime.datetime]):
            last_updated (Union[None, datetime.datetime]):
            device_type (Union['BriefDeviceType', None, Unset]):
            module_type (Union['BriefModuleType', None, Unset]):
            label (Union[Unset, str]): Physical label
            enabled (Union[Unset, bool]):
            mgmt_only (Union[Unset, bool]):
            description (Union[Unset, str]):
            bridge (Union['NestedInterfaceTemplate', None, Unset]):
            poe_mode (Union['InterfaceTemplatePoeModeType0', None, Unset]):
            poe_type (Union['InterfaceTemplatePoeTypeType0', None, Unset]):
            rf_role (Union['InterfaceTemplateRfRoleType0', None, Unset]):
    """

    id: int
    url: str
    display: str
    name: str
    type_: "InterfaceTemplateType"
    created: Union[None, datetime.datetime]
    last_updated: Union[None, datetime.datetime]
    device_type: Union["BriefDeviceType", None, Unset] = UNSET
    module_type: Union["BriefModuleType", None, Unset] = UNSET
    label: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    mgmt_only: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    bridge: Union["NestedInterfaceTemplate", None, Unset] = UNSET
    poe_mode: Union["InterfaceTemplatePoeModeType0", None, Unset] = UNSET
    poe_type: Union["InterfaceTemplatePoeTypeType0", None, Unset] = UNSET
    rf_role: Union["InterfaceTemplateRfRoleType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.brief_device_type import BriefDeviceType
        from ..models.brief_module_type import BriefModuleType
        from ..models.interface_template_poe_mode_type_0 import (
            InterfaceTemplatePoeModeType0,
        )
        from ..models.interface_template_poe_type_type_0 import (
            InterfaceTemplatePoeTypeType0,
        )
        from ..models.interface_template_rf_role_type_0 import (
            InterfaceTemplateRfRoleType0,
        )
        from ..models.nested_interface_template import NestedInterfaceTemplate

        id = self.id

        url = self.url

        display = self.display

        name = self.name

        type_ = self.type_.to_dict()

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

        enabled = self.enabled

        mgmt_only = self.mgmt_only

        description = self.description

        bridge: Union[None, Unset, dict[str, Any]]
        if isinstance(self.bridge, Unset):
            bridge = UNSET
        elif isinstance(self.bridge, NestedInterfaceTemplate):
            bridge = self.bridge.to_dict()
        else:
            bridge = self.bridge

        poe_mode: Union[None, Unset, dict[str, Any]]
        if isinstance(self.poe_mode, Unset):
            poe_mode = UNSET
        elif isinstance(self.poe_mode, InterfaceTemplatePoeModeType0):
            poe_mode = self.poe_mode.to_dict()
        else:
            poe_mode = self.poe_mode

        poe_type: Union[None, Unset, dict[str, Any]]
        if isinstance(self.poe_type, Unset):
            poe_type = UNSET
        elif isinstance(self.poe_type, InterfaceTemplatePoeTypeType0):
            poe_type = self.poe_type.to_dict()
        else:
            poe_type = self.poe_type

        rf_role: Union[None, Unset, dict[str, Any]]
        if isinstance(self.rf_role, Unset):
            rf_role = UNSET
        elif isinstance(self.rf_role, InterfaceTemplateRfRoleType0):
            rf_role = self.rf_role.to_dict()
        else:
            rf_role = self.rf_role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "display": display,
                "name": name,
                "type": type_,
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
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if mgmt_only is not UNSET:
            field_dict["mgmt_only"] = mgmt_only
        if description is not UNSET:
            field_dict["description"] = description
        if bridge is not UNSET:
            field_dict["bridge"] = bridge
        if poe_mode is not UNSET:
            field_dict["poe_mode"] = poe_mode
        if poe_type is not UNSET:
            field_dict["poe_type"] = poe_type
        if rf_role is not UNSET:
            field_dict["rf_role"] = rf_role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brief_device_type import BriefDeviceType
        from ..models.brief_module_type import BriefModuleType
        from ..models.interface_template_poe_mode_type_0 import (
            InterfaceTemplatePoeModeType0,
        )
        from ..models.interface_template_poe_type_type_0 import (
            InterfaceTemplatePoeTypeType0,
        )
        from ..models.interface_template_rf_role_type_0 import (
            InterfaceTemplateRfRoleType0,
        )
        from ..models.interface_template_type import InterfaceTemplateType
        from ..models.nested_interface_template import NestedInterfaceTemplate

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        display = d.pop("display")

        name = d.pop("name")

        type_ = InterfaceTemplateType.from_dict(d.pop("type"))

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

        enabled = d.pop("enabled", UNSET)

        mgmt_only = d.pop("mgmt_only", UNSET)

        description = d.pop("description", UNSET)

        def _parse_bridge(
            data: object,
        ) -> Union["NestedInterfaceTemplate", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bridge_type_1 = NestedInterfaceTemplate.from_dict(data)

                return bridge_type_1
            except:  # noqa: E722
                pass
            return cast(Union["NestedInterfaceTemplate", None, Unset], data)

        bridge = _parse_bridge(d.pop("bridge", UNSET))

        def _parse_poe_mode(
            data: object,
        ) -> Union["InterfaceTemplatePoeModeType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                poe_mode_type_0 = InterfaceTemplatePoeModeType0.from_dict(data)

                return poe_mode_type_0
            except:  # noqa: E722
                pass
            return cast(Union["InterfaceTemplatePoeModeType0", None, Unset], data)

        poe_mode = _parse_poe_mode(d.pop("poe_mode", UNSET))

        def _parse_poe_type(
            data: object,
        ) -> Union["InterfaceTemplatePoeTypeType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                poe_type_type_0 = InterfaceTemplatePoeTypeType0.from_dict(data)

                return poe_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union["InterfaceTemplatePoeTypeType0", None, Unset], data)

        poe_type = _parse_poe_type(d.pop("poe_type", UNSET))

        def _parse_rf_role(
            data: object,
        ) -> Union["InterfaceTemplateRfRoleType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rf_role_type_0 = InterfaceTemplateRfRoleType0.from_dict(data)

                return rf_role_type_0
            except:  # noqa: E722
                pass
            return cast(Union["InterfaceTemplateRfRoleType0", None, Unset], data)

        rf_role = _parse_rf_role(d.pop("rf_role", UNSET))

        interface_template = cls(
            id=id,
            url=url,
            display=display,
            name=name,
            type_=type_,
            created=created,
            last_updated=last_updated,
            device_type=device_type,
            module_type=module_type,
            label=label,
            enabled=enabled,
            mgmt_only=mgmt_only,
            description=description,
            bridge=bridge,
            poe_mode=poe_mode,
            poe_type=poe_type,
            rf_role=rf_role,
        )

        interface_template.additional_properties = d
        return interface_template

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
