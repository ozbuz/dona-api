from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalizedText")


@_attrs_define
class LocalizedText:
    """`jsonb {uz,ru,en}`; readers fall back uz → ru → en.

    Attributes:
        uz (str | Unset):
        ru (str | Unset):
        en (str | Unset):
    """

    uz: str | Unset = UNSET
    ru: str | Unset = UNSET
    en: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        uz = self.uz

        ru = self.ru

        en = self.en

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if uz is not UNSET:
            field_dict["uz"] = uz
        if ru is not UNSET:
            field_dict["ru"] = ru
        if en is not UNSET:
            field_dict["en"] = en

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uz = d.pop("uz", UNSET)

        ru = d.pop("ru", UNSET)

        en = d.pop("en", UNSET)

        localized_text = cls(
            uz=uz,
            ru=ru,
            en=en,
        )

        return localized_text
