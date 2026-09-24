from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PriceLine")


@_attrs_define
class PriceLine:
    """Exactly ONE of `product_id` · `seller_sku` · `barcode` · `external_id`, plus optional `variant_id`.

    Attributes:
        price_uzs (int): ABSOLUTE price.
        product_id (UUID | Unset):
        seller_sku (str | Unset):
        barcode (str | Unset):
        external_id (str | Unset):
        variant_id (UUID | Unset):
        compare_at_uzs (int | None | Unset): Must exceed `price_uzs`; `null` clears.
        version (str | Unset):
    """

    price_uzs: int
    product_id: UUID | Unset = UNSET
    seller_sku: str | Unset = UNSET
    barcode: str | Unset = UNSET
    external_id: str | Unset = UNSET
    variant_id: UUID | Unset = UNSET
    compare_at_uzs: int | None | Unset = UNSET
    version: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        price_uzs = self.price_uzs

        product_id: str | Unset = UNSET
        if not isinstance(self.product_id, Unset):
            product_id = str(self.product_id)

        seller_sku = self.seller_sku

        barcode = self.barcode

        external_id = self.external_id

        variant_id: str | Unset = UNSET
        if not isinstance(self.variant_id, Unset):
            variant_id = str(self.variant_id)

        compare_at_uzs: int | None | Unset
        if isinstance(self.compare_at_uzs, Unset):
            compare_at_uzs = UNSET
        else:
            compare_at_uzs = self.compare_at_uzs

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "price_uzs": price_uzs,
            }
        )
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if seller_sku is not UNSET:
            field_dict["seller_sku"] = seller_sku
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if variant_id is not UNSET:
            field_dict["variant_id"] = variant_id
        if compare_at_uzs is not UNSET:
            field_dict["compare_at_uzs"] = compare_at_uzs
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price_uzs = d.pop("price_uzs")

        _product_id = d.pop("product_id", UNSET)
        product_id: UUID | Unset
        if isinstance(_product_id, Unset):
            product_id = UNSET
        else:
            product_id = UUID(_product_id)

        seller_sku = d.pop("seller_sku", UNSET)

        barcode = d.pop("barcode", UNSET)

        external_id = d.pop("external_id", UNSET)

        _variant_id = d.pop("variant_id", UNSET)
        variant_id: UUID | Unset
        if isinstance(_variant_id, Unset):
            variant_id = UNSET
        else:
            variant_id = UUID(_variant_id)

        def _parse_compare_at_uzs(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        compare_at_uzs = _parse_compare_at_uzs(d.pop("compare_at_uzs", UNSET))

        version = d.pop("version", UNSET)

        price_line = cls(
            price_uzs=price_uzs,
            product_id=product_id,
            seller_sku=seller_sku,
            barcode=barcode,
            external_id=external_id,
            variant_id=variant_id,
            compare_at_uzs=compare_at_uzs,
            version=version,
        )

        return price_line
