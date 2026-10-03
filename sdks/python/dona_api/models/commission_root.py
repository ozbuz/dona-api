from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.localized_text import LocalizedText


T = TypeVar("T", bound="CommissionRoot")


@_attrs_define
class CommissionRoot:
    """One active top-level category and the range of its active leaves' rates.

    Attributes:
        id (UUID):
        slug (str):
        name (LocalizedText): `jsonb {uz,ru,en}`; readers fall back uz → ru → en.
        min_pct (float):
        max_pct (float):
        leaf_count (int):
        l2_names (list[LocalizedText]):
        thumb_url (None | str):
        effective_min_pct (float): This shop's lowest rate in the category after its commission rules and campaigns
            (what a sale is charged). `min_pct` / `max_pct` stay the platform's card.
        effective_max_pct (float): This shop's highest rate in the category after its commission rules and campaigns.
    """

    id: UUID
    slug: str
    name: LocalizedText
    min_pct: float
    max_pct: float
    leaf_count: int
    l2_names: list[LocalizedText]
    thumb_url: None | str
    effective_min_pct: float
    effective_max_pct: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        slug = self.slug

        name = self.name.to_dict()

        min_pct = self.min_pct

        max_pct = self.max_pct

        leaf_count = self.leaf_count

        l2_names = []
        for l2_names_item_data in self.l2_names:
            l2_names_item = l2_names_item_data.to_dict()
            l2_names.append(l2_names_item)

        thumb_url: None | str
        thumb_url = self.thumb_url

        effective_min_pct = self.effective_min_pct

        effective_max_pct = self.effective_max_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "name": name,
                "min_pct": min_pct,
                "max_pct": max_pct,
                "leaf_count": leaf_count,
                "l2_names": l2_names,
                "thumb_url": thumb_url,
                "effective_min_pct": effective_min_pct,
                "effective_max_pct": effective_max_pct,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.localized_text import LocalizedText  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        slug = d.pop("slug")

        name = LocalizedText.from_dict(d.pop("name"))

        min_pct = d.pop("min_pct")

        max_pct = d.pop("max_pct")

        leaf_count = d.pop("leaf_count")

        l2_names = []
        _l2_names = d.pop("l2_names")
        for l2_names_item_data in _l2_names:
            l2_names_item = LocalizedText.from_dict(l2_names_item_data)

            l2_names.append(l2_names_item)

        def _parse_thumb_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        thumb_url = _parse_thumb_url(d.pop("thumb_url"))

        effective_min_pct = d.pop("effective_min_pct")

        effective_max_pct = d.pop("effective_max_pct")

        commission_root = cls(
            id=id,
            slug=slug,
            name=name,
            min_pct=min_pct,
            max_pct=max_pct,
            leaf_count=leaf_count,
            l2_names=l2_names,
            thumb_url=thumb_url,
            effective_min_pct=effective_min_pct,
            effective_max_pct=effective_max_pct,
        )

        commission_root.additional_properties = d
        return commission_root

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
