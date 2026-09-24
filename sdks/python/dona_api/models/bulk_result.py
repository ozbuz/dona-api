from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bulk_result_summary import BulkResultSummary
    from ..models.line_result import LineResult


T = TypeVar("T", bound="BulkResult")


@_attrs_define
class BulkResult:
    """
    Attributes:
        results (list[LineResult]):
        summary (BulkResultSummary):
        dry_run (bool):
    """

    results: list[LineResult]
    summary: BulkResultSummary
    dry_run: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        summary = self.summary.to_dict()

        dry_run = self.dry_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "summary": summary,
                "dry_run": dry_run,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_result_summary import BulkResultSummary  # noqa: PLC0415
        from ..models.line_result import LineResult  # noqa: PLC0415

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = LineResult.from_dict(results_item_data)

            results.append(results_item)

        summary = BulkResultSummary.from_dict(d.pop("summary"))

        dry_run = d.pop("dry_run")

        bulk_result = cls(
            results=results,
            summary=summary,
            dry_run=dry_run,
        )

        bulk_result.additional_properties = d
        return bulk_result

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
