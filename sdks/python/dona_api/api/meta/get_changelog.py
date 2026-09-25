from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

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
    dona_seller: UUID | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(dona_seller, Unset):
        headers["Dona-Seller"] = dona_seller

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
    dona_seller: UUID | Unset = UNSET,
) -> Response[Any | ChangelogEntryPage | Error]:
    """Changelog (JSON, or RSS with Accept)

     Public. `Accept: application/rss+xml` returns RSS. Backed by `seller_api_changelog` (migration 0487,
    S4): published entries only, newest first; the first row is the v1 seed. Written only from Dona
    Control (admin-contract §7). The seller portal reads the same body at `GET /api/v1/sellers/me/api-
    docs/changelog` (portal-contract §6a) — this tree sends no CORS grant. Cached `public, max-age=300`
    with `Vary: Accept-Language, Accept` on BOTH formats, and a weak `ETag` over the exact bytes: `If-
    None-Match` with it answers `304` and no body.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):

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
        dona_seller=dona_seller,
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
    dona_seller: UUID | Unset = UNSET,
) -> Any | ChangelogEntryPage | Error | None:
    """Changelog (JSON, or RSS with Accept)

     Public. `Accept: application/rss+xml` returns RSS. Backed by `seller_api_changelog` (migration 0487,
    S4): published entries only, newest first; the first row is the v1 seed. Written only from Dona
    Control (admin-contract §7). The seller portal reads the same body at `GET /api/v1/sellers/me/api-
    docs/changelog` (portal-contract §6a) — this tree sends no CORS grant. Cached `public, max-age=300`
    with `Vary: Accept-Language, Accept` on BOTH formats, and a weak `ETag` over the exact bytes: `If-
    None-Match` with it answers `304` and no body.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):

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
        dona_seller=dona_seller,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
) -> Response[Any | ChangelogEntryPage | Error]:
    """Changelog (JSON, or RSS with Accept)

     Public. `Accept: application/rss+xml` returns RSS. Backed by `seller_api_changelog` (migration 0487,
    S4): published entries only, newest first; the first row is the v1 seed. Written only from Dona
    Control (admin-contract §7). The seller portal reads the same body at `GET /api/v1/sellers/me/api-
    docs/changelog` (portal-contract §6a) — this tree sends no CORS grant. Cached `public, max-age=300`
    with `Vary: Accept-Language, Accept` on BOTH formats, and a weak `ETag` over the exact bytes: `If-
    None-Match` with it answers `304` and no body.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):

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
        dona_seller=dona_seller,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
) -> Any | ChangelogEntryPage | Error | None:
    """Changelog (JSON, or RSS with Accept)

     Public. `Accept: application/rss+xml` returns RSS. Backed by `seller_api_changelog` (migration 0487,
    S4): published entries only, newest first; the first row is the v1 seed. Written only from Dona
    Control (admin-contract §7). The seller portal reads the same body at `GET /api/v1/sellers/me/api-
    docs/changelog` (portal-contract §6a) — this tree sends no CORS grant. Cached `public, max-age=300`
    with `Vary: Accept-Language, Accept` on BOTH formats, and a weak `ETag` over the exact bytes: `If-
    None-Match` with it answers `304` and no body.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):

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
            dona_seller=dona_seller,
        )
    ).parsed
