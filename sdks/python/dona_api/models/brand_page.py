from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brand import Brand
    from ..models.page_meta import PageMeta


T = TypeVar("T", bound="BrandPage")


@_attrs_define
class BrandPage:
    """
    Attributes:
        items (list[Brand]):
        next_cursor (None | str): Pass back as `?cursor=`. `null` when `has_more` is false.
        has_more (bool):
        meta (PageMeta | Unset): Endpoint-specific facts; clients must tolerate unknown keys.
    """

    items: list[Brand]
    next_cursor: None | str
    has_more: bool
    meta: PageMeta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        next_cursor: None | str
        next_cursor = self.next_cursor

        has_more = self.has_more

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "next_cursor": next_cursor,
                "has_more": has_more,
            }
        )
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.brand import Brand  # noqa: PLC0415
        from ..models.page_meta import PageMeta  # noqa: PLC0415

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = Brand.from_dict(items_item_data)

            items.append(items_item)

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        has_more = d.pop("has_more")

        _meta = d.pop("meta", UNSET)
        meta: PageMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = PageMeta.from_dict(_meta)

        brand_page = cls(
            items=items,
            next_cursor=next_cursor,
            has_more=has_more,
            meta=meta,
        )

        brand_page.additional_properties = d
        return brand_page

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
