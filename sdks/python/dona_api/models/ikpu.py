from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ikpu_packages_item import IkpuPackagesItem


T = TypeVar("T", bound="Ikpu")


@_attrs_define
class Ikpu:
    """From the local `tasnif` copy (0392) — Dona never calls soliq on your behalf.

    Attributes:
        code (str):
        name (str): Localised by `Accept-Language` (tasnif keeps per-language columns).
        active (bool):
        packages (list[IkpuPackagesItem]):
    """

    code: str
    name: str
    active: bool
    packages: list[IkpuPackagesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        name = self.name

        active = self.active

        packages = []
        for packages_item_data in self.packages:
            packages_item = packages_item_data.to_dict()
            packages.append(packages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "name": name,
                "active": active,
                "packages": packages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ikpu_packages_item import IkpuPackagesItem  # noqa: PLC0415

        d = dict(src_dict)
        code = d.pop("code")

        name = d.pop("name")

        active = d.pop("active")

        packages = []
        _packages = d.pop("packages")
        for packages_item_data in _packages:
            packages_item = IkpuPackagesItem.from_dict(packages_item_data)

            packages.append(packages_item)

        ikpu = cls(
            code=code,
            name=name,
            active=active,
            packages=packages,
        )

        ikpu.additional_properties = d
        return ikpu

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
