from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.product_state_hold_type_0 import ProductStateHoldType0


T = TypeVar("T", bound="ProductState")


@_attrs_define
class ProductState:
    """
    Attributes:
        id (UUID):
        status (str):
        hold (None | ProductStateHoldType0):
        updated_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
    """

    id: UUID
    status: str
    hold: None | ProductStateHoldType0
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.product_state_hold_type_0 import ProductStateHoldType0  # noqa: PLC0415

        id = str(self.id)

        status = self.status

        hold: dict[str, Any] | None
        if isinstance(self.hold, ProductStateHoldType0):
            hold = self.hold.to_dict()
        else:
            hold = self.hold

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "hold": hold,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_state_hold_type_0 import ProductStateHoldType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        status = d.pop("status")

        def _parse_hold(data: object) -> None | ProductStateHoldType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                hold_type_0 = ProductStateHoldType0.from_dict(data)

                return hold_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductStateHoldType0, data)

        hold = _parse_hold(d.pop("hold"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        product_state = cls(
            id=id,
            status=status,
            hold=hold,
            updated_at=updated_at,
        )

        product_state.additional_properties = d
        return product_state

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
