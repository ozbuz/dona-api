from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_attribute_options_item import CategoryAttributeOptionsItem
    from ..models.localized_text import LocalizedText


T = TypeVar("T", bound="CategoryAttribute")


@_attrs_define
class CategoryAttribute:
    """
    Attributes:
        key (str):
        label (LocalizedText): `jsonb {uz,ru,en}`; readers fall back uz → ru → en.
        value_type (str): e.g. `text`, `number`, `enum`, `boolean`.
        requirement (str): Known values (open set — tolerate new ones): `required`, `recommended`, `optional`.
        is_filterable (bool):
        is_variant_axis (bool):
        unit (str | Unset):
        options (list[CategoryAttributeOptionsItem] | Unset):
    """

    key: str
    label: LocalizedText
    value_type: str
    requirement: str
    is_filterable: bool
    is_variant_axis: bool
    unit: str | Unset = UNSET
    options: list[CategoryAttributeOptionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        label = self.label.to_dict()

        value_type = self.value_type

        requirement = self.requirement

        is_filterable = self.is_filterable

        is_variant_axis = self.is_variant_axis

        unit = self.unit

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "label": label,
                "value_type": value_type,
                "requirement": requirement,
                "is_filterable": is_filterable,
                "is_variant_axis": is_variant_axis,
            }
        )
        if unit is not UNSET:
            field_dict["unit"] = unit
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_attribute_options_item import CategoryAttributeOptionsItem  # noqa: PLC0415
        from ..models.localized_text import LocalizedText  # noqa: PLC0415

        d = dict(src_dict)
        key = d.pop("key")

        label = LocalizedText.from_dict(d.pop("label"))

        value_type = d.pop("value_type")

        requirement = d.pop("requirement")

        is_filterable = d.pop("is_filterable")

        is_variant_axis = d.pop("is_variant_axis")

        unit = d.pop("unit", UNSET)

        _options = d.pop("options", UNSET)
        options: list[CategoryAttributeOptionsItem] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = CategoryAttributeOptionsItem.from_dict(options_item_data)

                options.append(options_item)

        category_attribute = cls(
            key=key,
            label=label,
            value_type=value_type,
            requirement=requirement,
            is_filterable=is_filterable,
            is_variant_axis=is_variant_axis,
            unit=unit,
            options=options,
        )

        category_attribute.additional_properties = d
        return category_attribute

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
