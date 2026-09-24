from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductIssueEventData")


@_attrs_define
class ProductIssueEventData:
    """
    Attributes:
        product_id (UUID):
        reason_code (str):
        action_url (str):
        issue_id (None | Unset | UUID):
    """

    product_id: UUID
    reason_code: str
    action_url: str
    issue_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = str(self.product_id)

        reason_code = self.reason_code

        action_url = self.action_url

        issue_id: None | str | Unset
        if isinstance(self.issue_id, Unset):
            issue_id = UNSET
        elif isinstance(self.issue_id, UUID):
            issue_id = str(self.issue_id)
        else:
            issue_id = self.issue_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_id": product_id,
                "reason_code": reason_code,
                "action_url": action_url,
            }
        )
        if issue_id is not UNSET:
            field_dict["issue_id"] = issue_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = UUID(d.pop("product_id"))

        reason_code = d.pop("reason_code")

        action_url = d.pop("action_url")

        def _parse_issue_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                issue_id_type_0 = UUID(data)

                return issue_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        issue_id = _parse_issue_id(d.pop("issue_id", UNSET))

        product_issue_event_data = cls(
            product_id=product_id,
            reason_code=reason_code,
            action_url=action_url,
            issue_id=issue_id,
        )

        product_issue_event_data.additional_properties = d
        return product_issue_event_data

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
