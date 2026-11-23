from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductStateHoldType0")


@_attrs_define
class ProductStateHoldType0:
    """
    Attributes:
        reason (str): `shop_not_activated` · a category requirement · `unfulfilled_order` (a fulfilment hold keeps it
            off sale: the write succeeded; release at `ack_url`).
        ack_url (str | Unset): With `reason=unfulfilled_order` only: the seller portal page that releases the product
            (`https://seller.dona.uz/products/{id}?release=1`). The API never releases a fulfilment hold — the seller
            acknowledges in the portal or the app.
        since (datetime.datetime | Unset): With `reason=unfulfilled_order` on a product read: when the fulfilment hold
            began (ISO 8601, Tashkent `+05:00`).
    """

    reason: str
    ack_url: str | Unset = UNSET
    since: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        ack_url = self.ack_url

        since: str | Unset = UNSET
        if not isinstance(self.since, Unset):
            since = self.since.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
            }
        )
        if ack_url is not UNSET:
            field_dict["ack_url"] = ack_url
        if since is not UNSET:
            field_dict["since"] = since

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = d.pop("reason")

        ack_url = d.pop("ack_url", UNSET)

        _since = d.pop("since", UNSET)
        since: datetime.datetime | Unset
        if isinstance(_since, Unset):
            since = UNSET
        else:
            since = datetime.datetime.fromisoformat(_since)

        product_state_hold_type_0 = cls(
            reason=reason,
            ack_url=ack_url,
            since=since,
        )

        product_state_hold_type_0.additional_properties = d
        return product_state_hold_type_0

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
