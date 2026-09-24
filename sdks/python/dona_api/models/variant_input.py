from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.variant_input_options import VariantInputOptions


T = TypeVar("T", bound="VariantInput")


@_attrs_define
class VariantInput:
    """
    Attributes:
        options (VariantInputOptions):
        price_uzs (int):
        stock (int):
        sku (str | Unset):
        barcode (str | Unset):
        compare_at_uzs (int | None | Unset):
    """

    options: VariantInputOptions
    price_uzs: int
    stock: int
    sku: str | Unset = UNSET
    barcode: str | Unset = UNSET
    compare_at_uzs: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        options = self.options.to_dict()

        price_uzs = self.price_uzs

        stock = self.stock

        sku = self.sku

        barcode = self.barcode

        compare_at_uzs: int | None | Unset
        if isinstance(self.compare_at_uzs, Unset):
            compare_at_uzs = UNSET
        else:
            compare_at_uzs = self.compare_at_uzs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "options": options,
                "price_uzs": price_uzs,
                "stock": stock,
            }
        )
        if sku is not UNSET:
            field_dict["sku"] = sku
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if compare_at_uzs is not UNSET:
            field_dict["compare_at_uzs"] = compare_at_uzs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.variant_input_options import VariantInputOptions  # noqa: PLC0415

        d = dict(src_dict)
        options = VariantInputOptions.from_dict(d.pop("options"))

        price_uzs = d.pop("price_uzs")

        stock = d.pop("stock")

        sku = d.pop("sku", UNSET)

        barcode = d.pop("barcode", UNSET)

        def _parse_compare_at_uzs(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        compare_at_uzs = _parse_compare_at_uzs(d.pop("compare_at_uzs", UNSET))

        variant_input = cls(
            options=options,
            price_uzs=price_uzs,
            stock=stock,
            sku=sku,
            barcode=barcode,
            compare_at_uzs=compare_at_uzs,
        )

        variant_input.additional_properties = d
        return variant_input

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
