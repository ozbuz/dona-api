from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.changelog_entry_page import ChangelogEntryPage
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    accept_language: str | Unset = "uz",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/changelog",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ChangelogEntryPage | Error | None:
    if response.status_code == 200:
        response_200 = ChangelogEntryPage.from_dict(response.json())

        return response_200

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ChangelogEntryPage | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    accept_language: str | Unset = "uz",
) -> Response[Any | ChangelogEntryPage | Error]:
    """Changelog (JSON, or RSS with Accept)

     Public. `Accept: application/rss+xml` returns RSS. Backed by `seller_api_changelog` (0465, S4) — an
    empty list until then.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ChangelogEntryPage | Error]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    accept_language: str | Unset = "uz",
) -> Any | ChangelogEntryPage | Error | None:
    """Changelog (JSON, or RSS with Accept)

     Public. `Accept: application/rss+xml` returns RSS. Backed by `seller_api_changelog` (0465, S4) — an
    empty list until then.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ChangelogEntryPage | Error
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        limit=limit,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    accept_language: str | Unset = "uz",
) -> Response[Any | ChangelogEntryPage | Error]:
    """Changelog (JSON, or RSS with Accept)

     Public. `Accept: application/rss+xml` returns RSS. Backed by `seller_api_changelog` (0465, S4) — an
    empty list until then.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ChangelogEntryPage | Error]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    accept_language: str | Unset = "uz",
) -> Any | ChangelogEntryPage | Error | None:
    """Changelog (JSON, or RSS with Accept)

     Public. `Accept: application/rss+xml` returns RSS. Backed by `seller_api_changelog` (0465, S4) — an
    empty list until then.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ChangelogEntryPage | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            limit=limit,
            accept_language=accept_language,
        )
    ).parsed
