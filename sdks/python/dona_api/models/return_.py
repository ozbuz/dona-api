from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.return_items_item import ReturnItemsItem


T = TypeVar("T", bound="Return")


@_attrs_define
class Return:
    """
    Attributes:
        id (UUID):
        order_id (UUID):
        status (str): Known values (open set — tolerate new ones): `requested`, `approved`, `refunded`, `rejected`,
            `disputed`, `closed`.
        type_ (str):
        reason_code (str):
        refund_uzs (int): Integer soʻm (no decimals).
        due_at (datetime.datetime | None):
        items (list[ReturnItemsItem]):
        reason_text (None | str): Buyer-authored; detail only (null on lists).
        created_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
        updated_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
    """

    id: UUID
    order_id: UUID
    status: str
    type_: str
    reason_code: str
    refund_uzs: int
    due_at: datetime.datetime | None
    items: list[ReturnItemsItem]
    reason_text: None | str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        order_id = str(self.order_id)

        status = self.status

        type_ = self.type_

        reason_code = self.reason_code

        refund_uzs = self.refund_uzs

        due_at: None | str
        if isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        reason_text: None | str
        reason_text = self.reason_text

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "order_id": order_id,
                "status": status,
                "type": type_,
                "reason_code": reason_code,
                "refund_uzs": refund_uzs,
                "due_at": due_at,
                "items": items,
                "reason_text": reason_text,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.return_items_item import ReturnItemsItem  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        order_id = UUID(d.pop("order_id"))

        status = d.pop("status")

        type_ = d.pop("type")

        reason_code = d.pop("reason_code")

        refund_uzs = d.pop("refund_uzs")

        def _parse_due_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_at_type_0 = datetime.datetime.fromisoformat(data)

                return due_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        due_at = _parse_due_at(d.pop("due_at"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ReturnItemsItem.from_dict(items_item_data)

            items.append(items_item)

        def _parse_reason_text(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason_text = _parse_reason_text(d.pop("reason_text"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        return_ = cls(
            id=id,
            order_id=order_id,
            status=status,
            type_=type_,
            reason_code=reason_code,
            refund_uzs=refund_uzs,
            due_at=due_at,
            items=items,
            reason_text=reason_text,
            created_at=created_at,
            updated_at=updated_at,
        )

        return_.additional_properties = d
        return return_

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
