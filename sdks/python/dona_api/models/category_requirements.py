from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.category_attribute import CategoryAttribute


T = TypeVar("T", bound="CategoryRequirements")


@_attrs_define
class CategoryRequirements:
    """The live `GET /catalog/categories/{id}/requirements` payload (`internal/catalog/requirements.go`), resolved through
    the tree — one shape for the form and the API.

        Attributes:
            category_id (UUID):
            status (str):
            listing_policy (str): `open` default; `approval_required`, `licensed`, `restricted`, `prohibited`.
            is_leaf (bool):
            can_list (bool): `status=active AND is_leaf AND listing_policy <> prohibited`.
            min_images (int):
            requires_dimensions (bool):
            requires_brand (bool):
            requires_size_chart (bool):
            commission_pct (float | None):
            attributes (list[CategoryAttribute]):
    """

    category_id: UUID
    status: str
    listing_policy: str
    is_leaf: bool
    can_list: bool
    min_images: int
    requires_dimensions: bool
    requires_brand: bool
    requires_size_chart: bool
    commission_pct: float | None
    attributes: list[CategoryAttribute]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_id = str(self.category_id)

        status = self.status

        listing_policy = self.listing_policy

        is_leaf = self.is_leaf

        can_list = self.can_list

        min_images = self.min_images

        requires_dimensions = self.requires_dimensions

        requires_brand = self.requires_brand

        requires_size_chart = self.requires_size_chart

        commission_pct: float | None
        commission_pct = self.commission_pct

        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()
            attributes.append(attributes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category_id": category_id,
                "status": status,
                "listing_policy": listing_policy,
                "is_leaf": is_leaf,
                "can_list": can_list,
                "min_images": min_images,
                "requires_dimensions": requires_dimensions,
                "requires_brand": requires_brand,
                "requires_size_chart": requires_size_chart,
                "commission_pct": commission_pct,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_attribute import CategoryAttribute  # noqa: PLC0415

        d = dict(src_dict)
        category_id = UUID(d.pop("category_id"))

        status = d.pop("status")

        listing_policy = d.pop("listing_policy")

        is_leaf = d.pop("is_leaf")

        can_list = d.pop("can_list")

        min_images = d.pop("min_images")

        requires_dimensions = d.pop("requires_dimensions")

        requires_brand = d.pop("requires_brand")

        requires_size_chart = d.pop("requires_size_chart")

        def _parse_commission_pct(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        commission_pct = _parse_commission_pct(d.pop("commission_pct"))

        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = CategoryAttribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        category_requirements = cls(
            category_id=category_id,
            status=status,
            listing_policy=listing_policy,
            is_leaf=is_leaf,
            can_list=can_list,
            min_images=min_images,
            requires_dimensions=requires_dimensions,
            requires_brand=requires_brand,
            requires_size_chart=requires_size_chart,
            commission_pct=commission_pct,
            attributes=attributes,
        )

        category_requirements.additional_properties = d
        return category_requirements

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
