from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductStatusEventData")


@_attrs_define
class ProductStatusEventData:
    """
    Attributes:
        product_id (UUID):
        status (str):
        prev_status (None | str):
        seller_sku (None | str | Unset):
    """

    product_id: UUID
    status: str
    prev_status: None | str
    seller_sku: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = str(self.product_id)

        status = self.status

        prev_status: None | str
        prev_status = self.prev_status

        seller_sku: None | str | Unset
        if isinstance(self.seller_sku, Unset):
            seller_sku = UNSET
        else:
            seller_sku = self.seller_sku

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_id": product_id,
                "status": status,
                "prev_status": prev_status,
            }
        )
        if seller_sku is not UNSET:
            field_dict["seller_sku"] = seller_sku

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = UUID(d.pop("product_id"))

        status = d.pop("status")

        def _parse_prev_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        prev_status = _parse_prev_status(d.pop("prev_status"))

        def _parse_seller_sku(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        seller_sku = _parse_seller_sku(d.pop("seller_sku", UNSET))

        product_status_event_data = cls(
            product_id=product_id,
            status=status,
            prev_status=prev_status,
            seller_sku=seller_sku,
        )

        product_status_event_data.additional_properties = d
        return product_status_event_data

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
