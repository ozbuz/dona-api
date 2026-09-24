from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.variant_options import VariantOptions


T = TypeVar("T", bound="Variant")


@_attrs_define
class Variant:
    """
    Attributes:
        id (UUID):
        options (VariantOptions): e.g. `{"color":"Qizil","size":"M"}`
        sku (None | str):
        barcode (None | str):
        price_uzs (int): Integer soʻm (no decimals).
        compare_at_uzs (int | None):
        stock (int):
        status (str):
        version (str): Opaque; echo it verbatim in stock/price lines.
    """

    id: UUID
    options: VariantOptions
    sku: None | str
    barcode: None | str
    price_uzs: int
    compare_at_uzs: int | None
    stock: int
    status: str
    version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        options = self.options.to_dict()

        sku: None | str
        sku = self.sku

        barcode: None | str
        barcode = self.barcode

        price_uzs = self.price_uzs

        compare_at_uzs: int | None
        compare_at_uzs = self.compare_at_uzs

        stock = self.stock

        status = self.status

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "options": options,
                "sku": sku,
                "barcode": barcode,
                "price_uzs": price_uzs,
                "compare_at_uzs": compare_at_uzs,
                "stock": stock,
                "status": status,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.variant_options import VariantOptions  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        options = VariantOptions.from_dict(d.pop("options"))

        def _parse_sku(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sku = _parse_sku(d.pop("sku"))

        def _parse_barcode(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        barcode = _parse_barcode(d.pop("barcode"))

        price_uzs = d.pop("price_uzs")

        def _parse_compare_at_uzs(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        compare_at_uzs = _parse_compare_at_uzs(d.pop("compare_at_uzs"))

        stock = d.pop("stock")

        status = d.pop("status")

        version = d.pop("version")

        variant = cls(
            id=id,
            options=options,
            sku=sku,
            barcode=barcode,
            price_uzs=price_uzs,
            compare_at_uzs=compare_at_uzs,
            stock=stock,
            status=status,
            version=version,
        )

        variant.additional_properties = d
        return variant

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
