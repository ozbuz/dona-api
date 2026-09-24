from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.localized_text import LocalizedText


T = TypeVar("T", bound="ChangelogEntry")


@_attrs_define
class ChangelogEntry:
    """
    Attributes:
        id (UUID):
        version (str):
        kind (str): Known values (open set — tolerate new ones): `added`, `changed`, `deprecated`, `removed`, `fixed`,
            `security`.
        title (LocalizedText): `jsonb {uz,ru,en}`; readers fall back uz → ru → en.
        body (LocalizedText): `jsonb {uz,ru,en}`; readers fall back uz → ru → en.
        affects_scopes (list[str]):
        sunset_at (datetime.datetime | None):
        published_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
    """

    id: UUID
    version: str
    kind: str
    title: LocalizedText
    body: LocalizedText
    affects_scopes: list[str]
    sunset_at: datetime.datetime | None
    published_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        version = self.version

        kind = self.kind

        title = self.title.to_dict()

        body = self.body.to_dict()

        affects_scopes = self.affects_scopes

        sunset_at: None | str
        if isinstance(self.sunset_at, datetime.datetime):
            sunset_at = self.sunset_at.isoformat()
        else:
            sunset_at = self.sunset_at

        published_at = self.published_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "version": version,
                "kind": kind,
                "title": title,
                "body": body,
                "affects_scopes": affects_scopes,
                "sunset_at": sunset_at,
                "published_at": published_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.localized_text import LocalizedText  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        version = d.pop("version")

        kind = d.pop("kind")

        title = LocalizedText.from_dict(d.pop("title"))

        body = LocalizedText.from_dict(d.pop("body"))

        affects_scopes = cast(list[str], d.pop("affects_scopes"))

        def _parse_sunset_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sunset_at_type_0 = datetime.datetime.fromisoformat(data)

                return sunset_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        sunset_at = _parse_sunset_at(d.pop("sunset_at"))

        published_at = datetime.datetime.fromisoformat(d.pop("published_at"))

        changelog_entry = cls(
            id=id,
            version=version,
            kind=kind,
            title=title,
            body=body,
            affects_scopes=affects_scopes,
            sunset_at=sunset_at,
            published_at=published_at,
        )

        changelog_entry.additional_properties = d
        return changelog_entry

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
