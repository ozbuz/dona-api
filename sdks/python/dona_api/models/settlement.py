from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Settlement")


@_attrs_define
class Settlement:
    """One ledger line of the shop's payable account.

    Attributes:
        id (UUID):
        txn_id (UUID):
        direction (str): Known values (open set — tolerate new ones): `credit`, `debit`.
        amount_uzs (int): Integer soʻm (no decimals).
        signed_amount_uzs (int):
        order_id (None | UUID):
        memo (str):
        created_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
    """

    id: UUID
    txn_id: UUID
    direction: str
    amount_uzs: int
    signed_amount_uzs: int
    order_id: None | UUID
    memo: str
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        txn_id = str(self.txn_id)

        direction = self.direction

        amount_uzs = self.amount_uzs

        signed_amount_uzs = self.signed_amount_uzs

        order_id: None | str
        if isinstance(self.order_id, UUID):
            order_id = str(self.order_id)
        else:
            order_id = self.order_id

        memo = self.memo

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "txn_id": txn_id,
                "direction": direction,
                "amount_uzs": amount_uzs,
                "signed_amount_uzs": signed_amount_uzs,
                "order_id": order_id,
                "memo": memo,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        txn_id = UUID(d.pop("txn_id"))

        direction = d.pop("direction")

        amount_uzs = d.pop("amount_uzs")

        signed_amount_uzs = d.pop("signed_amount_uzs")

        def _parse_order_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                order_id_type_0 = UUID(data)

                return order_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        order_id = _parse_order_id(d.pop("order_id"))

        memo = d.pop("memo")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        settlement = cls(
            id=id,
            txn_id=txn_id,
            direction=direction,
            amount_uzs=amount_uzs,
            signed_amount_uzs=signed_amount_uzs,
            order_id=order_id,
            memo=memo,
            created_at=created_at,
        )

        settlement.additional_properties = d
        return settlement

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
