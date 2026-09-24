from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Tombstone")


@_attrs_define
class Tombstone:
    """
    Attributes:
        id (UUID):
        seller_sku (None | str):
        external_id (None | str):
        deleted_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
    """

    id: UUID
    seller_sku: None | str
    external_id: None | str
    deleted_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        seller_sku: None | str
        seller_sku = self.seller_sku

        external_id: None | str
        external_id = self.external_id

        deleted_at = self.deleted_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "seller_sku": seller_sku,
                "external_id": external_id,
                "deleted_at": deleted_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_seller_sku(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        seller_sku = _parse_seller_sku(d.pop("seller_sku"))

        def _parse_external_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_id = _parse_external_id(d.pop("external_id"))

        deleted_at = datetime.datetime.fromisoformat(d.pop("deleted_at"))

        tombstone = cls(
            id=id,
            seller_sku=seller_sku,
            external_id=external_id,
            deleted_at=deleted_at,
        )

        tombstone.additional_properties = d
        return tombstone

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
