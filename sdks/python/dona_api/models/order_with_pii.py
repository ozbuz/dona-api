from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.order_item import OrderItem
    from ..models.order_meta import OrderMeta
    from ..models.recipient import Recipient


T = TypeVar("T", bound="OrderWithPii")


@_attrs_define
class OrderWithPii:
    """`orders:pii` superset — ADVANCED, `sk` keys only, logged `pii=true`, `pii_recipient` recorded at mint. Only on `GET
    /orders/{id}`, never on a list or an event.

        Attributes:
            id (UUID):
            order_code (str): Display handle (0164), e.g. `AB1765543210XZ`; never a route param.
            status (str): `pending`, `paid`, `ready_to_ship`, `shipped`, `delivered`, `cancelled`; tolerate new values.
            payment_status (str):
            payment_method (str):
            scheme (str): Derived: `own_fleet` when the shipment rides the default channel, else `third_party`. Known values
                (open set — tolerate new ones): `own_fleet`, `third_party`.
            total_uzs (int): Integer soʻm (no decimals).
            accepted_at (datetime.datetime | None):
            declined_at (datetime.datetime | None):
            shipped_at (datetime.datetime | None):
            delivered_at (datetime.datetime | None):
            cancelled_by (None | str): Known values (open set — tolerate new ones): `seller`, `buyer`, `system`.
            decline_reason_code (None | str):
            accept_deadline (datetime.datetime | None):
            ship_by_deadline (datetime.datetime | None):
            items (list[OrderItem]):
            meta (OrderMeta):
            created_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
            updated_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
            recipient (Recipient):
    """

    id: UUID
    order_code: str
    status: str
    payment_status: str
    payment_method: str
    scheme: str
    total_uzs: int
    accepted_at: datetime.datetime | None
    declined_at: datetime.datetime | None
    shipped_at: datetime.datetime | None
    delivered_at: datetime.datetime | None
    cancelled_by: None | str
    decline_reason_code: None | str
    accept_deadline: datetime.datetime | None
    ship_by_deadline: datetime.datetime | None
    items: list[OrderItem]
    meta: OrderMeta
    created_at: datetime.datetime
    updated_at: datetime.datetime
    recipient: Recipient
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        order_code = self.order_code

        status = self.status

        payment_status = self.payment_status

        payment_method = self.payment_method

        scheme = self.scheme

        total_uzs = self.total_uzs

        accepted_at: None | str
        if isinstance(self.accepted_at, datetime.datetime):
            accepted_at = self.accepted_at.isoformat()
        else:
            accepted_at = self.accepted_at

        declined_at: None | str
        if isinstance(self.declined_at, datetime.datetime):
            declined_at = self.declined_at.isoformat()
        else:
            declined_at = self.declined_at

        shipped_at: None | str
        if isinstance(self.shipped_at, datetime.datetime):
            shipped_at = self.shipped_at.isoformat()
        else:
            shipped_at = self.shipped_at

        delivered_at: None | str
        if isinstance(self.delivered_at, datetime.datetime):
            delivered_at = self.delivered_at.isoformat()
        else:
            delivered_at = self.delivered_at

        cancelled_by: None | str
        cancelled_by = self.cancelled_by

        decline_reason_code: None | str
        decline_reason_code = self.decline_reason_code

        accept_deadline: None | str
        if isinstance(self.accept_deadline, datetime.datetime):
            accept_deadline = self.accept_deadline.isoformat()
        else:
            accept_deadline = self.accept_deadline

        ship_by_deadline: None | str
        if isinstance(self.ship_by_deadline, datetime.datetime):
            ship_by_deadline = self.ship_by_deadline.isoformat()
        else:
            ship_by_deadline = self.ship_by_deadline

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        meta = self.meta.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        recipient = self.recipient.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "order_code": order_code,
                "status": status,
                "payment_status": payment_status,
                "payment_method": payment_method,
                "scheme": scheme,
                "total_uzs": total_uzs,
                "accepted_at": accepted_at,
                "declined_at": declined_at,
                "shipped_at": shipped_at,
                "delivered_at": delivered_at,
                "cancelled_by": cancelled_by,
                "decline_reason_code": decline_reason_code,
                "accept_deadline": accept_deadline,
                "ship_by_deadline": ship_by_deadline,
                "items": items,
                "meta": meta,
                "created_at": created_at,
                "updated_at": updated_at,
                "recipient": recipient,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_item import OrderItem  # noqa: PLC0415
        from ..models.order_meta import OrderMeta  # noqa: PLC0415
        from ..models.recipient import Recipient  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        order_code = d.pop("order_code")

        status = d.pop("status")

        payment_status = d.pop("payment_status")

        payment_method = d.pop("payment_method")

        scheme = d.pop("scheme")

        total_uzs = d.pop("total_uzs")

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

        def _parse_declined_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                declined_at_type_0 = datetime.datetime.fromisoformat(data)

                return declined_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        declined_at = _parse_declined_at(d.pop("declined_at"))

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

        def _parse_delivered_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivered_at_type_0 = datetime.datetime.fromisoformat(data)

                return delivered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        delivered_at = _parse_delivered_at(d.pop("delivered_at"))

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

        def _parse_accept_deadline(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accept_deadline_type_0 = datetime.datetime.fromisoformat(data)

                return accept_deadline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        accept_deadline = _parse_accept_deadline(d.pop("accept_deadline"))

        def _parse_ship_by_deadline(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ship_by_deadline_type_0 = datetime.datetime.fromisoformat(data)

                return ship_by_deadline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        ship_by_deadline = _parse_ship_by_deadline(d.pop("ship_by_deadline"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = OrderItem.from_dict(items_item_data)

            items.append(items_item)

        meta = OrderMeta.from_dict(d.pop("meta"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        recipient = Recipient.from_dict(d.pop("recipient"))

        order_with_pii = cls(
            id=id,
            order_code=order_code,
            status=status,
            payment_status=payment_status,
            payment_method=payment_method,
            scheme=scheme,
            total_uzs=total_uzs,
            accepted_at=accepted_at,
            declined_at=declined_at,
            shipped_at=shipped_at,
            delivered_at=delivered_at,
            cancelled_by=cancelled_by,
            decline_reason_code=decline_reason_code,
            accept_deadline=accept_deadline,
            ship_by_deadline=ship_by_deadline,
            items=items,
            meta=meta,
            created_at=created_at,
            updated_at=updated_at,
            recipient=recipient,
        )

        order_with_pii.additional_properties = d
        return order_with_pii

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
