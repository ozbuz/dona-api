from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StockEffect")


@_attrs_define
class StockEffect:
    """What a decline / cancel did to one line's product, under the 24-hour out-of-stock rule.

    Attributes:
        order_item_id (UUID): The order line (`items[].id`) the entry is about.
        product_id (UUID):
        variant_id (None | UUID): The variation the line resolved to when the lock is one variation's (`scope:
            variant`), else `null`.
        variant_label (None | str):
        scope (str): `variant`: one variation is out of stock and locked; `product`: the whole product is (it has no
            variations, or only one active variation). Known values (open set — tolerate new ones): `variant`, `product`.
        result (str): `zeroed` — taken to stock 0 and locked; `already_zero` — it was at 0, now locked;
            `variant_not_found` — no variation of this shop matched the line, nothing zeroed or locked; `not_applied` — see
            `why`. Known values (open set — tolerate new ones): `zeroed`, `already_zero`, `variant_not_found`,
            `not_applied`.
        why (None | str): Only with `result: not_applied`: `shipped` (a shipped order — the goods come back) or
            `legacy_multi_line` (an order with several lines and no `unavailable_item_ids`). Known values (open set —
            tolerate new ones): `shipped`, `legacy_multi_line`.
        units_removed (int): Units taken off sale by this entry.
        locked_until (datetime.datetime | None): When the product (or variation) may be put back on sale: RFC 3339, UTC
            (`…Z`), whole seconds. `null` when nothing was locked.
    """

    order_item_id: UUID
    product_id: UUID
    variant_id: None | UUID
    variant_label: None | str
    scope: str
    result: str
    why: None | str
    units_removed: int
    locked_until: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_item_id = str(self.order_item_id)

        product_id = str(self.product_id)

        variant_id: None | str
        if isinstance(self.variant_id, UUID):
            variant_id = str(self.variant_id)
        else:
            variant_id = self.variant_id

        variant_label: None | str
        variant_label = self.variant_label

        scope = self.scope

        result = self.result

        why: None | str
        why = self.why

        units_removed = self.units_removed

        locked_until: None | str
        if isinstance(self.locked_until, datetime.datetime):
            locked_until = self.locked_until.isoformat()
        else:
            locked_until = self.locked_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_item_id": order_item_id,
                "product_id": product_id,
                "variant_id": variant_id,
                "variant_label": variant_label,
                "scope": scope,
                "result": result,
                "why": why,
                "units_removed": units_removed,
                "locked_until": locked_until,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_item_id = UUID(d.pop("order_item_id"))

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

        def _parse_variant_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        variant_label = _parse_variant_label(d.pop("variant_label"))

        scope = d.pop("scope")

        result = d.pop("result")

        def _parse_why(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        why = _parse_why(d.pop("why"))

        units_removed = d.pop("units_removed")

        def _parse_locked_until(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                locked_until_type_0 = datetime.datetime.fromisoformat(data)

                return locked_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        locked_until = _parse_locked_until(d.pop("locked_until"))

        stock_effect = cls(
            order_item_id=order_item_id,
            product_id=product_id,
            variant_id=variant_id,
            variant_label=variant_label,
            scope=scope,
            result=result,
            why=why,
            units_removed=units_removed,
            locked_until=locked_until,
        )

        stock_effect.additional_properties = d
        return stock_effect

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
