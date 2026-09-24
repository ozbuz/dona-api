from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrderLineCancelledEventData")


@_attrs_define
class OrderLineCancelledEventData:
    """
    Attributes:
        order_id (UUID):
        order_item_id (UUID):
        quantity (int):
        reason_code (None | str): A code from the order vocabularies, or null — the buyer's free text is never pushed.
    """

    order_id: UUID
    order_item_id: UUID
    quantity: int
    reason_code: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = str(self.order_id)

        order_item_id = str(self.order_item_id)

        quantity = self.quantity

        reason_code: None | str
        reason_code = self.reason_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_id": order_id,
                "order_item_id": order_item_id,
                "quantity": quantity,
                "reason_code": reason_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_id = UUID(d.pop("order_id"))

        order_item_id = UUID(d.pop("order_item_id"))

        quantity = d.pop("quantity")

        def _parse_reason_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason_code = _parse_reason_code(d.pop("reason_code"))

        order_line_cancelled_event_data = cls(
            order_id=order_id,
            order_item_id=order_item_id,
            quantity=quantity,
            reason_code=reason_code,
        )

        order_line_cancelled_event_data.additional_properties = d
        return order_line_cancelled_event_data

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
