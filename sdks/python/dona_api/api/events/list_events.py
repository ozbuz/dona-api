from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.event_page import EventPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: UUID | Unset = UNSET,
    since: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    limit: int | Unset = 100,
    if_none_match: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_none_match, Unset):
        headers["If-None-Match"] = if_none_match

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_dona_integration, Unset):
        headers["X-Dona-Integration"] = x_dona_integration

    params: dict[str, Any] = {}

    json_cursor: str | Unset = UNSET
    if not isinstance(cursor, Unset):
        json_cursor = str(cursor)
    params["cursor"] = json_cursor

    params["since"] = since

    json_types: list[str] | Unset = UNSET
    if not isinstance(types, Unset):
        json_types = types

    params["types"] = json_types

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | EventPage | None:
    if response.status_code == 200:
        response_200 = EventPage.from_dict(response.json())

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
) -> Response[Any | Error | EventPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: UUID | Unset = UNSET,
    since: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    limit: int | Unset = 100,
    if_none_match: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Response[Any | Error | EventPage]:
    """The change feed (primary channel)

     Poll `?cursor=<last event id>`; omit it for the oldest retained event or pass `since`. Events are
    readable **30 days** from `occurred_at`. A cursor older than the window ⇒ `400 invalid_body` with
    `details[{field:"cursor",code:"cursor_expired"}]` and `meta.oldest_event_id`: full-reconcile via
    `updated_since`, then restart there. Ordered by `id` (near, not exact, `occurred_at` order). `limit`
    ≤ 200.

    Args:
        cursor (UUID | Unset):
        since (str | Unset):
        types (list[str] | Unset):
        limit (int | Unset):  Default: 100.
        if_none_match (str | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | EventPage]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        since=since,
        types=types,
        limit=limit,
        if_none_match=if_none_match,
        accept_language=accept_language,
        x_dona_integration=x_dona_integration,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    cursor: UUID | Unset = UNSET,
    since: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    limit: int | Unset = 100,
    if_none_match: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Any | Error | EventPage | None:
    """The change feed (primary channel)

     Poll `?cursor=<last event id>`; omit it for the oldest retained event or pass `since`. Events are
    readable **30 days** from `occurred_at`. A cursor older than the window ⇒ `400 invalid_body` with
    `details[{field:"cursor",code:"cursor_expired"}]` and `meta.oldest_event_id`: full-reconcile via
    `updated_since`, then restart there. Ordered by `id` (near, not exact, `occurred_at` order). `limit`
    ≤ 200.

    Args:
        cursor (UUID | Unset):
        since (str | Unset):
        types (list[str] | Unset):
        limit (int | Unset):  Default: 100.
        if_none_match (str | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | EventPage
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        since=since,
        types=types,
        limit=limit,
        if_none_match=if_none_match,
        accept_language=accept_language,
        x_dona_integration=x_dona_integration,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: UUID | Unset = UNSET,
    since: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    limit: int | Unset = 100,
    if_none_match: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Response[Any | Error | EventPage]:
    """The change feed (primary channel)

     Poll `?cursor=<last event id>`; omit it for the oldest retained event or pass `since`. Events are
    readable **30 days** from `occurred_at`. A cursor older than the window ⇒ `400 invalid_body` with
    `details[{field:"cursor",code:"cursor_expired"}]` and `meta.oldest_event_id`: full-reconcile via
    `updated_since`, then restart there. Ordered by `id` (near, not exact, `occurred_at` order). `limit`
    ≤ 200.

    Args:
        cursor (UUID | Unset):
        since (str | Unset):
        types (list[str] | Unset):
        limit (int | Unset):  Default: 100.
        if_none_match (str | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | EventPage]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        since=since,
        types=types,
        limit=limit,
        if_none_match=if_none_match,
        accept_language=accept_language,
        x_dona_integration=x_dona_integration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cursor: UUID | Unset = UNSET,
    since: str | Unset = UNSET,
    types: list[str] | Unset = UNSET,
    limit: int | Unset = 100,
    if_none_match: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Any | Error | EventPage | None:
    """The change feed (primary channel)

     Poll `?cursor=<last event id>`; omit it for the oldest retained event or pass `since`. Events are
    readable **30 days** from `occurred_at`. A cursor older than the window ⇒ `400 invalid_body` with
    `details[{field:"cursor",code:"cursor_expired"}]` and `meta.oldest_event_id`: full-reconcile via
    `updated_since`, then restart there. Ordered by `id` (near, not exact, `occurred_at` order). `limit`
    ≤ 200.

    Args:
        cursor (UUID | Unset):
        since (str | Unset):
        types (list[str] | Unset):
        limit (int | Unset):  Default: 100.
        if_none_match (str | Unset):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | EventPage
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            since=since,
            types=types,
            limit=limit,
            if_none_match=if_none_match,
            accept_language=accept_language,
            x_dona_integration=x_dona_integration,
        )
    ).parsed
