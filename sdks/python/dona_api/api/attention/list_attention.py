from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attention_page import AttentionPage
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: str | Unset = "open",
    kind: list[str] | Unset = UNSET,
    severity: list[str] | Unset = UNSET,
    action_required: bool | Unset = UNSET,
    subject_type: str | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    if_none_match: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_none_match, Unset):
        headers["If-None-Match"] = if_none_match

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(dona_seller, Unset):
        headers["Dona-Seller"] = dona_seller

    if not isinstance(x_dona_integration, Unset):
        headers["X-Dona-Integration"] = x_dona_integration

    params: dict[str, Any] = {}

    params["status"] = status

    json_kind: list[str] | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind

    params["kind"] = json_kind

    json_severity: list[str] | Unset = UNSET
    if not isinstance(severity, Unset):
        json_severity = severity

    params["severity"] = json_severity

    params["action_required"] = action_required

    params["subject_type"] = subject_type

    params["updated_since"] = updated_since

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/attention",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | AttentionPage | Error | None:
    if response.status_code == 200:
        response_200 = AttentionPage.from_dict(response.json())

        return response_200

    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | AttentionPage | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = "open",
    kind: list[str] | Unset = UNSET,
    severity: list[str] | Unset = UNSET,
    action_required: bool | Unset = UNSET,
    subject_type: str | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    if_none_match: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Response[Any | AttentionPage | Error]:
    """Errors, warnings, attention required

     Sorted `action_required desc, severity desc, deadline_at nulls last, opened_at desc`. Array filters
    repeat the key (`kind=stock_out&kind=stock_low`).

    Args:
        status (str | Unset): Known values (open set — tolerate new ones): `open`, `resolved`,
            `all`. Default: 'open'.
        kind (list[str] | Unset):
        severity (list[str] | Unset):
        action_required (bool | Unset):
        subject_type (str | Unset):
        updated_since (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        if_none_match (str | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AttentionPage | Error]
    """

    kwargs = _get_kwargs(
        status=status,
        kind=kind,
        severity=severity,
        action_required=action_required,
        subject_type=subject_type,
        updated_since=updated_since,
        cursor=cursor,
        limit=limit,
        if_none_match=if_none_match,
        accept_language=accept_language,
        dona_seller=dona_seller,
        x_dona_integration=x_dona_integration,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = "open",
    kind: list[str] | Unset = UNSET,
    severity: list[str] | Unset = UNSET,
    action_required: bool | Unset = UNSET,
    subject_type: str | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    if_none_match: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Any | AttentionPage | Error | None:
    """Errors, warnings, attention required

     Sorted `action_required desc, severity desc, deadline_at nulls last, opened_at desc`. Array filters
    repeat the key (`kind=stock_out&kind=stock_low`).

    Args:
        status (str | Unset): Known values (open set — tolerate new ones): `open`, `resolved`,
            `all`. Default: 'open'.
        kind (list[str] | Unset):
        severity (list[str] | Unset):
        action_required (bool | Unset):
        subject_type (str | Unset):
        updated_since (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        if_none_match (str | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AttentionPage | Error
    """

    return sync_detailed(
        client=client,
        status=status,
        kind=kind,
        severity=severity,
        action_required=action_required,
        subject_type=subject_type,
        updated_since=updated_since,
        cursor=cursor,
        limit=limit,
        if_none_match=if_none_match,
        accept_language=accept_language,
        dona_seller=dona_seller,
        x_dona_integration=x_dona_integration,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = "open",
    kind: list[str] | Unset = UNSET,
    severity: list[str] | Unset = UNSET,
    action_required: bool | Unset = UNSET,
    subject_type: str | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    if_none_match: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Response[Any | AttentionPage | Error]:
    """Errors, warnings, attention required

     Sorted `action_required desc, severity desc, deadline_at nulls last, opened_at desc`. Array filters
    repeat the key (`kind=stock_out&kind=stock_low`).

    Args:
        status (str | Unset): Known values (open set — tolerate new ones): `open`, `resolved`,
            `all`. Default: 'open'.
        kind (list[str] | Unset):
        severity (list[str] | Unset):
        action_required (bool | Unset):
        subject_type (str | Unset):
        updated_since (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        if_none_match (str | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AttentionPage | Error]
    """

    kwargs = _get_kwargs(
        status=status,
        kind=kind,
        severity=severity,
        action_required=action_required,
        subject_type=subject_type,
        updated_since=updated_since,
        cursor=cursor,
        limit=limit,
        if_none_match=if_none_match,
        accept_language=accept_language,
        dona_seller=dona_seller,
        x_dona_integration=x_dona_integration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: str | Unset = "open",
    kind: list[str] | Unset = UNSET,
    severity: list[str] | Unset = UNSET,
    action_required: bool | Unset = UNSET,
    subject_type: str | Unset = UNSET,
    updated_since: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    if_none_match: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Any | AttentionPage | Error | None:
    """Errors, warnings, attention required

     Sorted `action_required desc, severity desc, deadline_at nulls last, opened_at desc`. Array filters
    repeat the key (`kind=stock_out&kind=stock_low`).

    Args:
        status (str | Unset): Known values (open set — tolerate new ones): `open`, `resolved`,
            `all`. Default: 'open'.
        kind (list[str] | Unset):
        severity (list[str] | Unset):
        action_required (bool | Unset):
        subject_type (str | Unset):
        updated_since (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        if_none_match (str | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AttentionPage | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            kind=kind,
            severity=severity,
            action_required=action_required,
            subject_type=subject_type,
            updated_since=updated_since,
            cursor=cursor,
            limit=limit,
            if_none_match=if_none_match,
            accept_language=accept_language,
            dona_seller=dona_seller,
            x_dona_integration=x_dona_integration,
        )
    ).parsed
