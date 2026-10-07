from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeclineRequest")


@_attrs_define
class DeclineRequest:
    """
    Attributes:
        reason (str): The seller vocabulary — `out_of_stock`, `inventory_mismatch`, `product_damaged`,
            `store_unavailable`, `cannot_fulfill_in_time`, `duplicate_order`, `fraud_suspected`, `buyer_requested` (the
            buyer asked), `other` — OR Uzum's four (`OUT_OF_STOCK`, `OUT_OF_PACKAGE`, `OUT_OF_TIME`, `OTHER`) mapped onto
            them (`OUT_OF_PACKAGE` is stored as `other`). `OTHER`/`other` needs `comment`. Unknown ⇒ `400
            invalid_decline_reason`. **Only `out_of_stock`, `inventory_mismatch` and `OUT_OF_STOCK` carry the stock effect**
            (see `declineOrder`); every other reason cancels and the units go back on the shelf. Known values (open set —
            tolerate new ones): `OUT_OF_STOCK`, `OUT_OF_PACKAGE`, `OUT_OF_TIME`, `OTHER`, `out_of_stock`,
            `inventory_mismatch`, `product_damaged`, `store_unavailable`, `cannot_fulfill_in_time`, `duplicate_order`,
            `fraud_suspected`, `buyer_requested`, `other`.
        comment (str | Unset):
        unavailable_item_ids (list[UUID] | Unset): Which lines of the order are out of stock — `items[].id` of `GET
            /orders/{id}` (a line is live while `quantity − cancelled_quantity > 0`). Read only with `out_of_stock`,
            `inventory_mismatch` or `OUT_OF_STOCK`, and only where Dona applies the stock effect to the shop — for any other
            shop it is accepted and ignored, even malformed. An order with ONE live line needs none (that line is the line).
            With several: send the ids that are out of stock — an empty list ⇒ `400 unavailable_items_required`; an id that
            is not a live line of this order, or not an array of ids ⇒ `400 invalid_unavailable_items`; any id with a reason
            that takes nothing off sale ⇒ `400 unavailable_items_not_allowed`. Leaving the field out on a multi-line order
            changes no stock and answers `marking_needed: true`.
    """

    reason: str
    comment: str | Unset = UNSET
    unavailable_item_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        comment = self.comment

        unavailable_item_ids: list[str] | Unset = UNSET
        if not isinstance(self.unavailable_item_ids, Unset):
            unavailable_item_ids = []
            for unavailable_item_ids_item_data in self.unavailable_item_ids:
                unavailable_item_ids_item = str(unavailable_item_ids_item_data)
                unavailable_item_ids.append(unavailable_item_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if unavailable_item_ids is not UNSET:
            field_dict["unavailable_item_ids"] = unavailable_item_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = d.pop("reason")

        comment = d.pop("comment", UNSET)

        _unavailable_item_ids = d.pop("unavailable_item_ids", UNSET)
        unavailable_item_ids: list[UUID] | Unset = UNSET
        if _unavailable_item_ids is not UNSET:
            unavailable_item_ids = []
            for unavailable_item_ids_item_data in _unavailable_item_ids:
                unavailable_item_ids_item = UUID(unavailable_item_ids_item_data)

                unavailable_item_ids.append(unavailable_item_ids_item)

        decline_request = cls(
            reason=reason,
            comment=comment,
            unavailable_item_ids=unavailable_item_ids,
        )

        decline_request.additional_properties = d
        return decline_request

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
