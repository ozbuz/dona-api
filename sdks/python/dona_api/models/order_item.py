from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.localized_text import LocalizedText


T = TypeVar("T", bound="OrderItem")


@_attrs_define
class OrderItem:
    """
    Attributes:
        id (UUID):
        product_id (UUID):
        variant_id (None | UUID):
        seller_sku (None | str):
        title (LocalizedText): `jsonb {uz,ru,en}`; readers fall back uz → ru → en.
        quantity (int):
        cancelled_quantity (int):
        unit_price_uzs (int): Integer soʻm (no decimals).
    """

    id: UUID
    product_id: UUID
    variant_id: None | UUID
    seller_sku: None | str
    title: LocalizedText
    quantity: int
    cancelled_quantity: int
    unit_price_uzs: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        product_id = str(self.product_id)

        variant_id: None | str
        if isinstance(self.variant_id, UUID):
            variant_id = str(self.variant_id)
        else:
            variant_id = self.variant_id

        seller_sku: None | str
        seller_sku = self.seller_sku

        title = self.title.to_dict()

        quantity = self.quantity

        cancelled_quantity = self.cancelled_quantity

        unit_price_uzs = self.unit_price_uzs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "product_id": product_id,
                "variant_id": variant_id,
                "seller_sku": seller_sku,
                "title": title,
                "quantity": quantity,
                "cancelled_quantity": cancelled_quantity,
                "unit_price_uzs": unit_price_uzs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.localized_text import LocalizedText  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

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

        title = LocalizedText.from_dict(d.pop("title"))

        quantity = d.pop("quantity")

        cancelled_quantity = d.pop("cancelled_quantity")

        unit_price_uzs = d.pop("unit_price_uzs")

        order_item = cls(
            id=id,
            product_id=product_id,
            variant_id=variant_id,
            seller_sku=seller_sku,
            title=title,
            quantity=quantity,
            cancelled_quantity=cancelled_quantity,
            unit_price_uzs=unit_price_uzs,
        )

        order_item.additional_properties = d
        return order_item

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
