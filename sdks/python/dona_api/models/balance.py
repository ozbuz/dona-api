from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Balance")


@_attrs_define
class Balance:
    """From the double-entry ledger (the portal `/sellers/me/balance` numbers). No requisites, PAN or statement URLs.

    Attributes:
        available_uzs (int): Integer soʻm (no decimals).
        lifetime_earned_uzs (int): Integer soʻm (no decimals).
        lifetime_refunded_uzs (int): Integer soʻm (no decimals).
        currency (Literal['UZS']):
        as_of (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
    """

    available_uzs: int
    lifetime_earned_uzs: int
    lifetime_refunded_uzs: int
    currency: Literal["UZS"]
    as_of: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_uzs = self.available_uzs

        lifetime_earned_uzs = self.lifetime_earned_uzs

        lifetime_refunded_uzs = self.lifetime_refunded_uzs

        currency = self.currency

        as_of = self.as_of.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "available_uzs": available_uzs,
                "lifetime_earned_uzs": lifetime_earned_uzs,
                "lifetime_refunded_uzs": lifetime_refunded_uzs,
                "currency": currency,
                "as_of": as_of,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available_uzs = d.pop("available_uzs")

        lifetime_earned_uzs = d.pop("lifetime_earned_uzs")

        lifetime_refunded_uzs = d.pop("lifetime_refunded_uzs")

        currency = cast(Literal["UZS"], d.pop("currency"))
        if currency != "UZS":
            raise ValueError(f"currency must match const 'UZS', got '{currency}'")

        as_of = datetime.datetime.fromisoformat(d.pop("as_of"))

        balance = cls(
            available_uzs=available_uzs,
            lifetime_earned_uzs=lifetime_earned_uzs,
            lifetime_refunded_uzs=lifetime_refunded_uzs,
            currency=currency,
            as_of=as_of,
        )

        balance.additional_properties = d
        return balance

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
