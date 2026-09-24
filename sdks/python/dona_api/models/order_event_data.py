from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderEventData")


@_attrs_define
class OrderEventData:
    """
    Attributes:
        order_id (UUID):
        status (str):
        payment_status (str):
        payment_method (str):
        scheme (str): Known values (open set — tolerate new ones): `own_fleet`, `third_party`.
        total_uzs (int): Integer soʻm (no decimals).
        updated_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
        accept_deadline (datetime.datetime | None | Unset):
        ship_by_deadline (datetime.datetime | None | Unset):
    """

    order_id: UUID
    status: str
    payment_status: str
    payment_method: str
    scheme: str
    total_uzs: int
    updated_at: datetime.datetime
    accept_deadline: datetime.datetime | None | Unset = UNSET
    ship_by_deadline: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = str(self.order_id)

        status = self.status

        payment_status = self.payment_status

        payment_method = self.payment_method

        scheme = self.scheme

        total_uzs = self.total_uzs

        updated_at = self.updated_at.isoformat()

        accept_deadline: None | str | Unset
        if isinstance(self.accept_deadline, Unset):
            accept_deadline = UNSET
        elif isinstance(self.accept_deadline, datetime.datetime):
            accept_deadline = self.accept_deadline.isoformat()
        else:
            accept_deadline = self.accept_deadline

        ship_by_deadline: None | str | Unset
        if isinstance(self.ship_by_deadline, Unset):
            ship_by_deadline = UNSET
        elif isinstance(self.ship_by_deadline, datetime.datetime):
            ship_by_deadline = self.ship_by_deadline.isoformat()
        else:
            ship_by_deadline = self.ship_by_deadline

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_id": order_id,
                "status": status,
                "payment_status": payment_status,
                "payment_method": payment_method,
                "scheme": scheme,
                "total_uzs": total_uzs,
                "updated_at": updated_at,
            }
        )
        if accept_deadline is not UNSET:
            field_dict["accept_deadline"] = accept_deadline
        if ship_by_deadline is not UNSET:
            field_dict["ship_by_deadline"] = ship_by_deadline

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_id = UUID(d.pop("order_id"))

        status = d.pop("status")

        payment_status = d.pop("payment_status")

        payment_method = d.pop("payment_method")

        scheme = d.pop("scheme")

        total_uzs = d.pop("total_uzs")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_accept_deadline(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accept_deadline_type_0 = datetime.datetime.fromisoformat(data)

                return accept_deadline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        accept_deadline = _parse_accept_deadline(d.pop("accept_deadline", UNSET))

        def _parse_ship_by_deadline(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ship_by_deadline_type_0 = datetime.datetime.fromisoformat(data)

                return ship_by_deadline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ship_by_deadline = _parse_ship_by_deadline(d.pop("ship_by_deadline", UNSET))

        order_event_data = cls(
            order_id=order_id,
            status=status,
            payment_status=payment_status,
            payment_method=payment_method,
            scheme=scheme,
            total_uzs=total_uzs,
            updated_at=updated_at,
            accept_deadline=accept_deadline,
            ship_by_deadline=ship_by_deadline,
        )

        order_event_data.additional_properties = d
        return order_event_data

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
