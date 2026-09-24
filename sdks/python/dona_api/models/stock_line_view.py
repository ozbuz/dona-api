from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StockLineView")


@_attrs_define
class StockLineView:
    """
    Attributes:
        product_id (UUID):
        variant_id (None | UUID):
        seller_sku (None | str):
        barcode (None | str):
        external_id (None | str):
        quantity (int):
        version (str):
        updated_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
    """

    product_id: UUID
    variant_id: None | UUID
    seller_sku: None | str
    barcode: None | str
    external_id: None | str
    quantity: int
    version: str
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = str(self.product_id)

        variant_id: None | str
        if isinstance(self.variant_id, UUID):
            variant_id = str(self.variant_id)
        else:
            variant_id = self.variant_id

        seller_sku: None | str
        seller_sku = self.seller_sku

        barcode: None | str
        barcode = self.barcode

        external_id: None | str
        external_id = self.external_id

        quantity = self.quantity

        version = self.version

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_id": product_id,
                "variant_id": variant_id,
                "seller_sku": seller_sku,
                "barcode": barcode,
                "external_id": external_id,
                "quantity": quantity,
                "version": version,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = UUID(d.pop("product_id"))

        def _parse_variant_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                variant_id_type_0 = UUID(data)

                return variant_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        variant_id = _parse_variant_id(d.pop("variant_id"))

        def _parse_seller_sku(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        seller_sku = _parse_seller_sku(d.pop("seller_sku"))

        def _parse_barcode(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        barcode = _parse_barcode(d.pop("barcode"))

        def _parse_external_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_id = _parse_external_id(d.pop("external_id"))

        quantity = d.pop("quantity")

        version = d.pop("version")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        stock_line_view = cls(
            product_id=product_id,
            variant_id=variant_id,
            seller_sku=seller_sku,
            barcode=barcode,
            external_id=external_id,
            quantity=quantity,
            version=version,
            updated_at=updated_at,
        )

        stock_line_view.additional_properties = d
        return stock_line_view

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
