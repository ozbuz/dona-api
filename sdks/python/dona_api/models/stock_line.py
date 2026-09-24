from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StockLine")


@_attrs_define
class StockLine:
    """Exactly ONE of `product_id` · `seller_sku` · `barcode` · `external_id`, plus optional `variant_id`.

    Attributes:
        quantity (int): ABSOLUTE stock (not a delta).
        product_id (UUID | Unset):
        seller_sku (str | Unset):
        barcode (str | Unset):
        external_id (str | Unset):
        variant_id (UUID | Unset):
        version (str | Unset): Optional; stale ⇒ line `error: version_conflict`.
        warehouse (str | Unset): Reserved — one stock location per shop. Any value ⇒ the whole request `422
            warehouse_unsupported`.
    """

    quantity: int
    product_id: UUID | Unset = UNSET
    seller_sku: str | Unset = UNSET
    barcode: str | Unset = UNSET
    external_id: str | Unset = UNSET
    variant_id: UUID | Unset = UNSET
    version: str | Unset = UNSET
    warehouse: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        product_id: str | Unset = UNSET
        if not isinstance(self.product_id, Unset):
            product_id = str(self.product_id)

        seller_sku = self.seller_sku

        barcode = self.barcode

        external_id = self.external_id

        variant_id: str | Unset = UNSET
        if not isinstance(self.variant_id, Unset):
            variant_id = str(self.variant_id)

        version = self.version

        warehouse = self.warehouse

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "quantity": quantity,
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
        if version is not UNSET:
            field_dict["version"] = version
        if warehouse is not UNSET:
            field_dict["warehouse"] = warehouse

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quantity = d.pop("quantity")

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

        version = d.pop("version", UNSET)

        warehouse = d.pop("warehouse", UNSET)

        stock_line = cls(
            quantity=quantity,
            product_id=product_id,
            seller_sku=seller_sku,
            barcode=barcode,
            external_id=external_id,
            variant_id=variant_id,
            version=version,
            warehouse=warehouse,
        )

        return stock_line
