from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MeShop")


@_attrs_define
class MeShop:
    """
    Attributes:
        id (UUID):
        name (str):
        status (str): Known values (open set — tolerate new ones): `pending`, `approved`, `suspended`, `blocked`,
            `restricted`, `closed`.
        documents_status (str):
        kyc_status (str):
        can_sell (bool): Documents verdict approved (or waived) AND status approved — `selleraccess.ShopCanList`.
    """

    id: UUID
    name: str
    status: str
    documents_status: str
    kyc_status: str
    can_sell: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        status = self.status

        documents_status = self.documents_status

        kyc_status = self.kyc_status

        can_sell = self.can_sell

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "documents_status": documents_status,
                "kyc_status": kyc_status,
                "can_sell": can_sell,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        status = d.pop("status")

        documents_status = d.pop("documents_status")

        kyc_status = d.pop("kyc_status")

        can_sell = d.pop("can_sell")

        me_shop = cls(
            id=id,
            name=name,
            status=status,
            documents_status=documents_status,
            kyc_status=kyc_status,
            can_sell=can_sell,
        )

        me_shop.additional_properties = d
        return me_shop

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
