from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.other_open_order import OtherOpenOrder
    from ..models.stock_effect import StockEffect


T = TypeVar("T", bound="OrderTransition")


@_attrs_define
class OrderTransition:
    """The order as a decline / cancel left it. `refund_uzs`, `stock_effects`, `other_open_orders` and `marking_needed` are
    optional and additive: they appear only for a shop where Dona applies the out-of-stock rule (see `declineOrder`) —
    every other shop gets exactly the eight required keys.

        Attributes:
            id (UUID):
            status (str):
            payment_status (str):
            accepted_at (datetime.datetime | None):
            shipped_at (datetime.datetime | None):
            cancelled_by (None | str): Known values (open set — tolerate new ones): `seller`, `buyer`, `system`.
            decline_reason_code (None | str):
            updated_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
            refund_uzs (int | Unset): Only on a decline / cancel, only where the stock effect applies to the shop (it comes
                with the three keys below): the integer soʻm the buyer gets back — 0 for a cash-on-delivery or unpaid order,
                never null.
            stock_effects (list[StockEffect] | Unset): Only on a decline / cancel, only where the stock effect applies to
                the shop: one entry per line the move was about (`unavailable_item_ids`, or the one live line) — what became of
                its product. `[]` for a reason that takes nothing off sale.
            other_open_orders (list[OtherOpenOrder] | Unset): The shop's OTHER open orders (not cancelled, shipped or
                delivered; at most 50) holding a product or variation the move took off sale — to review; nothing cancels them.
                Read right AFTER the commit: if that read fails the key is absent, which means "not known", never "none". Absent
                on a dry run.
            marking_needed (bool | Unset): true when the reason takes stock off sale, the order had SEVERAL live lines and
                `unavailable_item_ids` was not sent: no product was taken off sale (the units went back on the shelf as before)
                and the question "which line was it?" stays open for 24 hours on Dona's side. Send `unavailable_item_ids` with
                the call to name the lines.
    """

    id: UUID
    status: str
    payment_status: str
    accepted_at: datetime.datetime | None
    shipped_at: datetime.datetime | None
    cancelled_by: None | str
    decline_reason_code: None | str
    updated_at: datetime.datetime
    refund_uzs: int | Unset = UNSET
    stock_effects: list[StockEffect] | Unset = UNSET
    other_open_orders: list[OtherOpenOrder] | Unset = UNSET
    marking_needed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        status = self.status

        payment_status = self.payment_status

        accepted_at: None | str
        if isinstance(self.accepted_at, datetime.datetime):
            accepted_at = self.accepted_at.isoformat()
        else:
            accepted_at = self.accepted_at

        shipped_at: None | str
        if isinstance(self.shipped_at, datetime.datetime):
            shipped_at = self.shipped_at.isoformat()
        else:
            shipped_at = self.shipped_at

        cancelled_by: None | str
        cancelled_by = self.cancelled_by

        decline_reason_code: None | str
        decline_reason_code = self.decline_reason_code

        updated_at = self.updated_at.isoformat()

        refund_uzs = self.refund_uzs

        stock_effects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stock_effects, Unset):
            stock_effects = []
            for stock_effects_item_data in self.stock_effects:
                stock_effects_item = stock_effects_item_data.to_dict()
                stock_effects.append(stock_effects_item)

        other_open_orders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.other_open_orders, Unset):
            other_open_orders = []
            for other_open_orders_item_data in self.other_open_orders:
                other_open_orders_item = other_open_orders_item_data.to_dict()
                other_open_orders.append(other_open_orders_item)

        marking_needed = self.marking_needed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "payment_status": payment_status,
                "accepted_at": accepted_at,
                "shipped_at": shipped_at,
                "cancelled_by": cancelled_by,
                "decline_reason_code": decline_reason_code,
                "updated_at": updated_at,
            }
        )
        if refund_uzs is not UNSET:
            field_dict["refund_uzs"] = refund_uzs
        if stock_effects is not UNSET:
            field_dict["stock_effects"] = stock_effects
        if other_open_orders is not UNSET:
            field_dict["other_open_orders"] = other_open_orders
        if marking_needed is not UNSET:
            field_dict["marking_needed"] = marking_needed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.other_open_order import OtherOpenOrder  # noqa: PLC0415
        from ..models.stock_effect import StockEffect  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        status = d.pop("status")

        payment_status = d.pop("payment_status")

        def _parse_accepted_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_at_type_0 = datetime.datetime.fromisoformat(data)

                return accepted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        accepted_at = _parse_accepted_at(d.pop("accepted_at"))

        def _parse_shipped_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shipped_at_type_0 = datetime.datetime.fromisoformat(data)

                return shipped_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        shipped_at = _parse_shipped_at(d.pop("shipped_at"))

        def _parse_cancelled_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cancelled_by = _parse_cancelled_by(d.pop("cancelled_by"))

        def _parse_decline_reason_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        decline_reason_code = _parse_decline_reason_code(d.pop("decline_reason_code"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        refund_uzs = d.pop("refund_uzs", UNSET)

        _stock_effects = d.pop("stock_effects", UNSET)
        stock_effects: list[StockEffect] | Unset = UNSET
        if _stock_effects is not UNSET:
            stock_effects = []
            for stock_effects_item_data in _stock_effects:
                stock_effects_item = StockEffect.from_dict(stock_effects_item_data)

                stock_effects.append(stock_effects_item)

        _other_open_orders = d.pop("other_open_orders", UNSET)
        other_open_orders: list[OtherOpenOrder] | Unset = UNSET
        if _other_open_orders is not UNSET:
            other_open_orders = []
            for other_open_orders_item_data in _other_open_orders:
                other_open_orders_item = OtherOpenOrder.from_dict(other_open_orders_item_data)

                other_open_orders.append(other_open_orders_item)

        marking_needed = d.pop("marking_needed", UNSET)

        order_transition = cls(
            id=id,
            status=status,
            payment_status=payment_status,
            accepted_at=accepted_at,
            shipped_at=shipped_at,
            cancelled_by=cancelled_by,
            decline_reason_code=decline_reason_code,
            updated_at=updated_at,
            refund_uzs=refund_uzs,
            stock_effects=stock_effects,
            other_open_orders=other_open_orders,
            marking_needed=marking_needed,
        )

        order_transition.additional_properties = d
        return order_transition

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
