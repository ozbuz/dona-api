from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeclineRequest")


@_attrs_define
class DeclineRequest:
    """
    Attributes:
        reason (str): Uzum subset (`OUT_OF_STOCK`, `OUT_OF_PACKAGE`, `OUT_OF_TIME`, `OTHER`) mapped onto the native
            `declineReasons`, OR a native lowercase code. `OTHER`/`other` needs `comment`. Unknown ⇒ `400
            invalid_decline_reason`. Known values (open set — tolerate new ones): `OUT_OF_STOCK`, `OUT_OF_PACKAGE`,
            `OUT_OF_TIME`, `OTHER`, `out_of_stock`, `inventory_mismatch`, `product_damaged`, `store_unavailable`,
            `cannot_fulfill_in_time`, `duplicate_order`, `fraud_suspected`, `other`.
        comment (str | Unset):
    """

    reason: str
    comment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = d.pop("reason")

        comment = d.pop("comment", UNSET)

        decline_request = cls(
            reason=reason,
            comment=comment,
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
