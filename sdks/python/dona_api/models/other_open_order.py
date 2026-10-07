from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OtherOpenOrder")


@_attrs_define
class OtherOpenOrder:
    """Another open order of the shop with a live line on a product or variation the move took off sale.

    Attributes:
        order_id (UUID):
        order_code (str):
        order_item_id (UUID):
    """

    order_id: UUID
    order_code: str
    order_item_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = str(self.order_id)

        order_code = self.order_code

        order_item_id = str(self.order_item_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_id": order_id,
                "order_code": order_code,
                "order_item_id": order_item_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_id = UUID(d.pop("order_id"))

        order_code = d.pop("order_code")

        order_item_id = UUID(d.pop("order_item_id"))

        other_open_order = cls(
            order_id=order_id,
            order_code=order_code,
            order_item_id=order_item_id,
        )

        other_open_order.additional_properties = d
        return other_open_order

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
