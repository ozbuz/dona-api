from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrderTransition")


@_attrs_define
class OrderTransition:
    """
    Attributes:
        id (UUID):
        status (str):
        payment_status (str):
        accepted_at (datetime.datetime | None):
        shipped_at (datetime.datetime | None):
        cancelled_by (None | str): Known values (open set — tolerate new ones): `seller`, `buyer`, `system`.
        decline_reason_code (None | str):
        updated_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
    """

    id: UUID
    status: str
    payment_status: str
    accepted_at: datetime.datetime | None
    shipped_at: datetime.datetime | None
    cancelled_by: None | str
    decline_reason_code: None | str
    updated_at: datetime.datetime
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        order_transition = cls(
            id=id,
            status=status,
            payment_status=payment_status,
            accepted_at=accepted_at,
            shipped_at=shipped_at,
            cancelled_by=cancelled_by,
            decline_reason_code=decline_reason_code,
            updated_at=updated_at,
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
