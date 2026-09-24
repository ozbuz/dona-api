from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_create import ProductCreate
    from ..models.product_update import ProductUpdate


T = TypeVar("T", bound="BatchCommand")


@_attrs_define
class BatchCommand:
    """
    Attributes:
        op (str): Known values (open set — tolerate new ones): `create`, `update`.
        product_id (UUID | Unset): Required when `op=update`.
        create (ProductCreate | Unset):
        update (ProductUpdate | Unset): Partial update: an absent field is unchanged.
    """

    op: str
    product_id: UUID | Unset = UNSET
    create: ProductCreate | Unset = UNSET
    update: ProductUpdate | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        op = self.op

        product_id: str | Unset = UNSET
        if not isinstance(self.product_id, Unset):
            product_id = str(self.product_id)

        create: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create, Unset):
            create = self.create.to_dict()

        update: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "op": op,
            }
        )
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if create is not UNSET:
            field_dict["create"] = create
        if update is not UNSET:
            field_dict["update"] = update

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_create import ProductCreate  # noqa: PLC0415
        from ..models.product_update import ProductUpdate  # noqa: PLC0415

        d = dict(src_dict)
        op = d.pop("op")

        _product_id = d.pop("product_id", UNSET)
        product_id: UUID | Unset
        if isinstance(_product_id, Unset):
            product_id = UNSET
        else:
            product_id = UUID(_product_id)

        _create = d.pop("create", UNSET)
        create: ProductCreate | Unset
        if isinstance(_create, Unset):
            create = UNSET
        else:
            create = ProductCreate.from_dict(_create)

        _update = d.pop("update", UNSET)
        update: ProductUpdate | Unset
        if isinstance(_update, Unset):
            update = UNSET
        else:
            update = ProductUpdate.from_dict(_update)

        batch_command = cls(
            op=op,
            product_id=product_id,
            create=create,
            update=update,
        )

        batch_command.additional_properties = d
        return batch_command

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
