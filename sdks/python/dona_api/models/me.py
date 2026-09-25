from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.limits import Limits
    from ..models.me_api_access import MeApiAccess
    from ..models.me_attention import MeAttention
    from ..models.me_key import MeKey
    from ..models.me_shop import MeShop


T = TypeVar("T", bound="Me")


@_attrs_define
class Me:
    """
    Attributes:
        key (MeKey):
        shop (MeShop):
        tier (str): Key tier, derived per request (never cached): ADVANCED = kyc approved AND documents approved (a
            waiver never counts) AND shop approved AND no active punishment; `seller_api_access.tier_override` may lower or
            raise it but never lifts a sanction. Known values (open set — tolerate new ones): `basic`, `advanced`.
        api_access (MeApiAccess):
        writes_enabled (bool): `app_config.seller_api.writes_enabled` (seeded false until D5).
        limits (Limits):
        attention (MeAttention):
        docs_url (str): The developer docs home in the key owner's language (`https://dona.uz/<uz|ru|en>/developers`;
            the owner's `users.language`, else `Accept-Language`, else uz).
    """

    key: MeKey
    shop: MeShop
    tier: str
    api_access: MeApiAccess
    writes_enabled: bool
    limits: Limits
    attention: MeAttention
    docs_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key.to_dict()

        shop = self.shop.to_dict()

        tier = self.tier

        api_access = self.api_access.to_dict()

        writes_enabled = self.writes_enabled

        limits = self.limits.to_dict()

        attention = self.attention.to_dict()

        docs_url = self.docs_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "shop": shop,
                "tier": tier,
                "api_access": api_access,
                "writes_enabled": writes_enabled,
                "limits": limits,
                "attention": attention,
                "docs_url": docs_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.limits import Limits  # noqa: PLC0415
        from ..models.me_api_access import MeApiAccess  # noqa: PLC0415
        from ..models.me_attention import MeAttention  # noqa: PLC0415
        from ..models.me_key import MeKey  # noqa: PLC0415
        from ..models.me_shop import MeShop  # noqa: PLC0415

        d = dict(src_dict)
        key = MeKey.from_dict(d.pop("key"))

        shop = MeShop.from_dict(d.pop("shop"))

        tier = d.pop("tier")

        api_access = MeApiAccess.from_dict(d.pop("api_access"))

        writes_enabled = d.pop("writes_enabled")

        limits = Limits.from_dict(d.pop("limits"))

        attention = MeAttention.from_dict(d.pop("attention"))

        docs_url = d.pop("docs_url")

        me = cls(
            key=key,
            shop=shop,
            tier=tier,
            api_access=api_access,
            writes_enabled=writes_enabled,
            limits=limits,
            attention=attention,
            docs_url=docs_url,
        )

        me.additional_properties = d
        return me

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
