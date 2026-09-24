from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.job_accepted_links import JobAcceptedLinks


T = TypeVar("T", bound="JobAccepted")


@_attrs_define
class JobAccepted:
    """
    Attributes:
        job_id (UUID):
        status (Literal['pending']):
        links (JobAcceptedLinks):
    """

    job_id: UUID
    status: Literal["pending"]
    links: JobAcceptedLinks
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = str(self.job_id)

        status = self.status

        links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
                "status": status,
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_accepted_links import JobAcceptedLinks  # noqa: PLC0415

        d = dict(src_dict)
        job_id = UUID(d.pop("job_id"))

        status = cast(Literal["pending"], d.pop("status"))
        if status != "pending":
            raise ValueError(f"status must match const 'pending', got '{status}'")

        links = JobAcceptedLinks.from_dict(d.pop("links"))

        job_accepted = cls(
            job_id=job_id,
            status=status,
            links=links,
        )

        job_accepted.additional_properties = d
        return job_accepted

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
