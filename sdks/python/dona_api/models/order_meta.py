from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrderMeta")


@_attrs_define
class OrderMeta:
    """
    Attributes:
        uzum_status (str): Known values (open set — tolerate new ones): `CREATED`, `PACKING`, `PENDING_DELIVERY`,
            `DELIVERING`, `DELIVERED`, `CANCELED`.
    """

    uzum_status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uzum_status = self.uzum_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uzum_status": uzum_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uzum_status = d.pop("uzum_status")

        order_meta = cls(
            uzum_status=uzum_status,
        )

        order_meta.additional_properties = d
        return order_meta

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
