from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.issue import Issue
    from ..models.product_created_hold_type_0 import ProductCreatedHoldType0


T = TypeVar("T", bound="ProductCreated")


@_attrs_define
class ProductCreated:
    """
    Attributes:
        id (UUID):
        status (str):
        hold (None | ProductCreatedHoldType0):
        issues (list[Issue]):
        created_via (Literal['api']):
    """

    id: UUID
    status: str
    hold: None | ProductCreatedHoldType0
    issues: list[Issue]
    created_via: Literal["api"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.product_created_hold_type_0 import ProductCreatedHoldType0  # noqa: PLC0415

        id = str(self.id)

        status = self.status

        hold: dict[str, Any] | None
        if isinstance(self.hold, ProductCreatedHoldType0):
            hold = self.hold.to_dict()
        else:
            hold = self.hold

        issues = []
        for issues_item_data in self.issues:
            issues_item = issues_item_data.to_dict()
            issues.append(issues_item)

        created_via = self.created_via

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "hold": hold,
                "issues": issues,
                "created_via": created_via,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue import Issue  # noqa: PLC0415
        from ..models.product_created_hold_type_0 import ProductCreatedHoldType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        status = d.pop("status")

        def _parse_hold(data: object) -> None | ProductCreatedHoldType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                hold_type_0 = ProductCreatedHoldType0.from_dict(data)

                return hold_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductCreatedHoldType0, data)

        hold = _parse_hold(d.pop("hold"))

        issues = []
        _issues = d.pop("issues")
        for issues_item_data in _issues:
            issues_item = Issue.from_dict(issues_item_data)

            issues.append(issues_item)

        created_via = cast(Literal["api"], d.pop("created_via"))
        if created_via != "api":
            raise ValueError(f"created_via must match const 'api', got '{created_via}'")

        product_created = cls(
            id=id,
            status=status,
            hold=hold,
            issues=issues,
            created_via=created_via,
        )

        product_created.additional_properties = d
        return product_created

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
