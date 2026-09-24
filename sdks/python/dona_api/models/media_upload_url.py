from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MediaUploadUrl")


@_attrs_define
class MediaUploadUrl:
    """
    Attributes:
        key (str):
        upload_url (str): Presigned PUT — send the exact bytes, no Authorization header.
        public_url (str): Use this in `image_urls`.
        expires_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
    """

    key: str
    upload_url: str
    public_url: str
    expires_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        upload_url = self.upload_url

        public_url = self.public_url

        expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "upload_url": upload_url,
                "public_url": public_url,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        upload_url = d.pop("upload_url")

        public_url = d.pop("public_url")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        media_upload_url = cls(
            key=key,
            upload_url=upload_url,
            public_url=public_url,
            expires_at=expires_at,
        )

        media_upload_url.additional_properties = d
        return media_upload_url

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
