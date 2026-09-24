from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Verification")


@_attrs_define
class Verification:
    """From `seller_api_shop_v` only — never the `sellers` row.

    Attributes:
        status (str): Known values (open set — tolerate new ones): `pending`, `approved`, `suspended`, `blocked`,
            `restricted`, `closed`.
        documents_status (str):
        kyc_status (str):
        documents_waived (bool):
        bank_confirmed (bool):
        can_sell (bool):
        tier (str): Key tier, derived per request (never cached): ADVANCED = kyc approved AND documents approved (a
            waiver never counts) AND shop approved AND no active punishment; `seller_api_access.tier_override` may lower or
            raise it but never lifts a sanction. Known values (open set — tolerate new ones): `basic`, `advanced`.
        tier_missing (list[str]): Empty when ADVANCED. A waiver never satisfies `documents_approved`.
    """

    status: str
    documents_status: str
    kyc_status: str
    documents_waived: bool
    bank_confirmed: bool
    can_sell: bool
    tier: str
    tier_missing: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        documents_status = self.documents_status

        kyc_status = self.kyc_status

        documents_waived = self.documents_waived

        bank_confirmed = self.bank_confirmed

        can_sell = self.can_sell

        tier = self.tier

        tier_missing = self.tier_missing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "documents_status": documents_status,
                "kyc_status": kyc_status,
                "documents_waived": documents_waived,
                "bank_confirmed": bank_confirmed,
                "can_sell": can_sell,
                "tier": tier,
                "tier_missing": tier_missing,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        documents_status = d.pop("documents_status")

        kyc_status = d.pop("kyc_status")

        documents_waived = d.pop("documents_waived")

        bank_confirmed = d.pop("bank_confirmed")

        can_sell = d.pop("can_sell")

        tier = d.pop("tier")

        tier_missing = cast(list[str], d.pop("tier_missing"))

        verification = cls(
            status=status,
            documents_status=documents_status,
            kyc_status=kyc_status,
            documents_waived=documents_waived,
            bank_confirmed=bank_confirmed,
            can_sell=can_sell,
            tier=tier,
            tier_missing=tier_missing,
        )

        verification.additional_properties = d
        return verification

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
