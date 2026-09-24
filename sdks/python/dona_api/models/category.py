from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.localized_text import LocalizedText


T = TypeVar("T", bound="Category")


@_attrs_define
class Category:
    """
    Attributes:
        id (UUID):
        parent_id (None | UUID):
        name (LocalizedText): `jsonb {uz,ru,en}`; readers fall back uz → ru → en.
        level (int):
        is_leaf (bool): Products attach to leaves only.
    """

    id: UUID
    parent_id: None | UUID
    name: LocalizedText
    level: int
    is_leaf: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        parent_id: None | str
        if isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id

        name = self.name.to_dict()

        level = self.level

        is_leaf = self.is_leaf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "parent_id": parent_id,
                "name": name,
                "level": level,
                "is_leaf": is_leaf,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.localized_text import LocalizedText  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_parent_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_id_type_0 = UUID(data)

                return parent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        parent_id = _parse_parent_id(d.pop("parent_id"))

        name = LocalizedText.from_dict(d.pop("name"))

        level = d.pop("level")

        is_leaf = d.pop("is_leaf")

        category = cls(
            id=id,
            parent_id=parent_id,
            name=name,
            level=level,
            is_leaf=is_leaf,
        )

        category.additional_properties = d
        return category

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
