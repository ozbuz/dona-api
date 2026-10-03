from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.localized_text import LocalizedText


T = TypeVar("T", bound="CommissionCampaignCategory")


@_attrs_define
class CommissionCampaignCategory:
    """
    Attributes:
        id (UUID):
        name (LocalizedText): `jsonb {uz,ru,en}`; readers fall back uz → ru → en.
        effect_type (str): Known values (open set — tolerate new ones): `absolute_pct`, `relative_discount_pct`.
        effect_pct (float):
    """

    id: UUID
    name: LocalizedText
    effect_type: str
    effect_pct: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name.to_dict()

        effect_type = self.effect_type

        effect_pct = self.effect_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "effect_type": effect_type,
                "effect_pct": effect_pct,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.localized_text import LocalizedText  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = LocalizedText.from_dict(d.pop("name"))

        effect_type = d.pop("effect_type")

        effect_pct = d.pop("effect_pct")

        commission_campaign_category = cls(
            id=id,
            name=name,
            effect_type=effect_type,
            effect_pct=effect_pct,
        )

        commission_campaign_category.additional_properties = d
        return commission_campaign_category

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
