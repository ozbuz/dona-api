from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LineResult")


@_attrs_define
class LineResult:
    """Echoes the line's key fields as sent.

    Attributes:
        index (int):
        status (str): Known values (open set — tolerate new ones): `ok`, `error`, `held`.
        product_id (UUID | Unset):
        variant_id (UUID | Unset):
        seller_sku (str | Unset):
        barcode (str | Unset):
        external_id (str | Unset):
        quantity (int | Unset):
        price_uzs (int | Unset):
        compare_at_uzs (int | None | Unset):
        version (str | Unset): New version after an `ok` line.
        error (str | Unset): On `status=error`: `version_conflict`, `object_cooldown`, `not_found`,
            `stock_not_editable`, `invalid_body`, …
        message (str | Unset):
        retry_after_seconds (int | Unset): On `object_cooldown`.
        approval_id (UUID | Unset):
        rule (str | Unset): Known values (open set — tolerate new ones): `price_floor`, `drop_100x`, `stock_jump_10x`,
            `mass_zero_50pct`, `delist_30pct`, `confirmation_required`.
    """

    index: int
    status: str
    product_id: UUID | Unset = UNSET
    variant_id: UUID | Unset = UNSET
    seller_sku: str | Unset = UNSET
    barcode: str | Unset = UNSET
    external_id: str | Unset = UNSET
    quantity: int | Unset = UNSET
    price_uzs: int | Unset = UNSET
    compare_at_uzs: int | None | Unset = UNSET
    version: str | Unset = UNSET
    error: str | Unset = UNSET
    message: str | Unset = UNSET
    retry_after_seconds: int | Unset = UNSET
    approval_id: UUID | Unset = UNSET
    rule: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        status = self.status

        product_id: str | Unset = UNSET
        if not isinstance(self.product_id, Unset):
            product_id = str(self.product_id)

        variant_id: str | Unset = UNSET
        if not isinstance(self.variant_id, Unset):
            variant_id = str(self.variant_id)

        seller_sku = self.seller_sku

        barcode = self.barcode

        external_id = self.external_id

        quantity = self.quantity

        price_uzs = self.price_uzs

        compare_at_uzs: int | None | Unset
        if isinstance(self.compare_at_uzs, Unset):
            compare_at_uzs = UNSET
        else:
            compare_at_uzs = self.compare_at_uzs

        version = self.version

        error = self.error

        message = self.message

        retry_after_seconds = self.retry_after_seconds

        approval_id: str | Unset = UNSET
        if not isinstance(self.approval_id, Unset):
            approval_id = str(self.approval_id)

        rule = self.rule

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "status": status,
            }
        )
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if variant_id is not UNSET:
            field_dict["variant_id"] = variant_id
        if seller_sku is not UNSET:
            field_dict["seller_sku"] = seller_sku
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if price_uzs is not UNSET:
            field_dict["price_uzs"] = price_uzs
        if compare_at_uzs is not UNSET:
            field_dict["compare_at_uzs"] = compare_at_uzs
        if version is not UNSET:
            field_dict["version"] = version
        if error is not UNSET:
            field_dict["error"] = error
        if message is not UNSET:
            field_dict["message"] = message
        if retry_after_seconds is not UNSET:
            field_dict["retry_after_seconds"] = retry_after_seconds
        if approval_id is not UNSET:
            field_dict["approval_id"] = approval_id
        if rule is not UNSET:
            field_dict["rule"] = rule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index")

        status = d.pop("status")

        _product_id = d.pop("product_id", UNSET)
        product_id: UUID | Unset
        if isinstance(_product_id, Unset):
            product_id = UNSET
        else:
            product_id = UUID(_product_id)

        _variant_id = d.pop("variant_id", UNSET)
        variant_id: UUID | Unset
        if isinstance(_variant_id, Unset):
            variant_id = UNSET
        else:
            variant_id = UUID(_variant_id)

        seller_sku = d.pop("seller_sku", UNSET)

        barcode = d.pop("barcode", UNSET)

        external_id = d.pop("external_id", UNSET)

        quantity = d.pop("quantity", UNSET)

        price_uzs = d.pop("price_uzs", UNSET)

        def _parse_compare_at_uzs(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        compare_at_uzs = _parse_compare_at_uzs(d.pop("compare_at_uzs", UNSET))

        version = d.pop("version", UNSET)

        error = d.pop("error", UNSET)

        message = d.pop("message", UNSET)

        retry_after_seconds = d.pop("retry_after_seconds", UNSET)

        _approval_id = d.pop("approval_id", UNSET)
        approval_id: UUID | Unset
        if isinstance(_approval_id, Unset):
            approval_id = UNSET
        else:
            approval_id = UUID(_approval_id)

        rule = d.pop("rule", UNSET)

        line_result = cls(
            index=index,
            status=status,
            product_id=product_id,
            variant_id=variant_id,
            seller_sku=seller_sku,
            barcode=barcode,
            external_id=external_id,
            quantity=quantity,
            price_uzs=price_uzs,
            compare_at_uzs=compare_at_uzs,
            version=version,
            error=error,
            message=message,
            retry_after_seconds=retry_after_seconds,
            approval_id=approval_id,
            rule=rule,
        )

        line_result.additional_properties = d
        return line_result

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
