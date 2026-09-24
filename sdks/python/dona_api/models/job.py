from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.job_progress import JobProgress
    from ..models.line_result import LineResult


T = TypeVar("T", bound="Job")


@_attrs_define
class Job:
    """
    Attributes:
        id (UUID):
        kind (str): Known values (open set — tolerate new ones): `export_products`, `export_orders`, `products_batch`.
        status (str): Known values (open set — tolerate new ones): `pending`, `running`, `ready`, `failed`.
        progress (JobProgress):
        file_url (None | str): Signed, valid 60 min from this response; re-read the job for a fresh one.
        file_expires_at (datetime.datetime | None):
        results (list[LineResult] | None): `products_batch` only: the per-line shape.
        error (None | str): Our code only.
        created_at (datetime.datetime): ISO 8601 with offset (Tashkent `+05:00` on output).
        finished_at (datetime.datetime | None):
        expires_at (datetime.datetime): Row + file swept after this (7 d); then `404 not_found`.
    """

    id: UUID
    kind: str
    status: str
    progress: JobProgress
    file_url: None | str
    file_expires_at: datetime.datetime | None
    results: list[LineResult] | None
    error: None | str
    created_at: datetime.datetime
    finished_at: datetime.datetime | None
    expires_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        kind = self.kind

        status = self.status

        progress = self.progress.to_dict()

        file_url: None | str
        file_url = self.file_url

        file_expires_at: None | str
        if isinstance(self.file_expires_at, datetime.datetime):
            file_expires_at = self.file_expires_at.isoformat()
        else:
            file_expires_at = self.file_expires_at

        results: list[dict[str, Any]] | None
        if isinstance(self.results, list):
            results = []
            for results_type_0_item_data in self.results:
                results_type_0_item = results_type_0_item_data.to_dict()
                results.append(results_type_0_item)

        else:
            results = self.results

        error: None | str
        error = self.error

        created_at = self.created_at.isoformat()

        finished_at: None | str
        if isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "status": status,
                "progress": progress,
                "file_url": file_url,
                "file_expires_at": file_expires_at,
                "results": results,
                "error": error,
                "created_at": created_at,
                "finished_at": finished_at,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_progress import JobProgress  # noqa: PLC0415
        from ..models.line_result import LineResult  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        kind = d.pop("kind")

        status = d.pop("status")

        progress = JobProgress.from_dict(d.pop("progress"))

        def _parse_file_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        file_url = _parse_file_url(d.pop("file_url"))

        def _parse_file_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                file_expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return file_expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        file_expires_at = _parse_file_expires_at(d.pop("file_expires_at"))

        def _parse_results(data: object) -> list[LineResult] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                results_type_0 = []
                _results_type_0 = data
                for results_type_0_item_data in _results_type_0:
                    results_type_0_item = LineResult.from_dict(results_type_0_item_data)

                    results_type_0.append(results_type_0_item)

                return results_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LineResult] | None, data)

        results = _parse_results(d.pop("results"))

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_finished_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = datetime.datetime.fromisoformat(data)

                return finished_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        finished_at = _parse_finished_at(d.pop("finished_at"))

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        job = cls(
            id=id,
            kind=kind,
            status=status,
            progress=progress,
            file_url=file_url,
            file_expires_at=file_expires_at,
            results=results,
            error=error,
            created_at=created_at,
            finished_at=finished_at,
            expires_at=expires_at,
        )

        job.additional_properties = d
        return job

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
