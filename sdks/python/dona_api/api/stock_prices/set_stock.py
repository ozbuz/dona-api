from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_result import BulkResult
from ...models.error import Error
from ...models.held_for_review import HeldForReview
from ...models.stock_request import StockRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: StockRequest,
    atomic: bool | Unset = UNSET,
    dry_run: str | Unset = UNSET,
    idempotency_key: str,
    dona_dry_run: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    if not isinstance(dona_dry_run, Unset):
        headers["Dona-Dry-Run"] = dona_dry_run

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(dona_seller, Unset):
        headers["Dona-Seller"] = dona_seller

    if not isinstance(x_dona_integration, Unset):
        headers["X-Dona-Integration"] = x_dona_integration

    params: dict[str, Any] = {}

    params["atomic"] = atomic

    params["dry_run"] = dry_run

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/stock",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BulkResult | Error | HeldForReview | None:
    if response.status_code == 200:
        response_200 = BulkResult.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = HeldForReview.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = Error.from_dict(response.json())

        return response_413

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

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
) -> Response[BulkResult | Error | HeldForReview]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StockRequest,
    atomic: bool | Unset = UNSET,
    dry_run: str | Unset = UNSET,
    idempotency_key: str,
    dona_dry_run: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Response[BulkResult | Error | HeldForReview]:
    """Set absolute stock (≤ 1 000 lines)

     Synchronous, through `catalog.ApplyGuardedStockPrice`. `200` with per-line results — the request is
    refused whole only for shape/budget (400/413/422). `?atomic=true` = all-or-nothing (any held line ⇒
    `202` for the batch). |Δ| > 10× and > 1 000, or zeroing > 50 % of lines ⇒ `held`. One object ≤ 1
    write / 10 s ⇒ line `error: object_cooldown`. Kill switch: `writes_enabled`.

    Args:
        atomic (bool | Unset):
        dry_run (str | Unset): Known values (open set — tolerate new ones): `true`, `false`.
        idempotency_key (str):
        dona_dry_run (str | Unset): Known values (open set — tolerate new ones): `true`, `false`.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):
        body (StockRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkResult | Error | HeldForReview]
    """

    kwargs = _get_kwargs(
        body=body,
        atomic=atomic,
        dry_run=dry_run,
        idempotency_key=idempotency_key,
        dona_dry_run=dona_dry_run,
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
    body: StockRequest,
    atomic: bool | Unset = UNSET,
    dry_run: str | Unset = UNSET,
    idempotency_key: str,
    dona_dry_run: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> BulkResult | Error | HeldForReview | None:
    """Set absolute stock (≤ 1 000 lines)

     Synchronous, through `catalog.ApplyGuardedStockPrice`. `200` with per-line results — the request is
    refused whole only for shape/budget (400/413/422). `?atomic=true` = all-or-nothing (any held line ⇒
    `202` for the batch). |Δ| > 10× and > 1 000, or zeroing > 50 % of lines ⇒ `held`. One object ≤ 1
    write / 10 s ⇒ line `error: object_cooldown`. Kill switch: `writes_enabled`.

    Args:
        atomic (bool | Unset):
        dry_run (str | Unset): Known values (open set — tolerate new ones): `true`, `false`.
        idempotency_key (str):
        dona_dry_run (str | Unset): Known values (open set — tolerate new ones): `true`, `false`.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):
        body (StockRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkResult | Error | HeldForReview
    """

    return sync_detailed(
        client=client,
        body=body,
        atomic=atomic,
        dry_run=dry_run,
        idempotency_key=idempotency_key,
        dona_dry_run=dona_dry_run,
        accept_language=accept_language,
        dona_seller=dona_seller,
        x_dona_integration=x_dona_integration,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StockRequest,
    atomic: bool | Unset = UNSET,
    dry_run: str | Unset = UNSET,
    idempotency_key: str,
    dona_dry_run: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> Response[BulkResult | Error | HeldForReview]:
    """Set absolute stock (≤ 1 000 lines)

     Synchronous, through `catalog.ApplyGuardedStockPrice`. `200` with per-line results — the request is
    refused whole only for shape/budget (400/413/422). `?atomic=true` = all-or-nothing (any held line ⇒
    `202` for the batch). |Δ| > 10× and > 1 000, or zeroing > 50 % of lines ⇒ `held`. One object ≤ 1
    write / 10 s ⇒ line `error: object_cooldown`. Kill switch: `writes_enabled`.

    Args:
        atomic (bool | Unset):
        dry_run (str | Unset): Known values (open set — tolerate new ones): `true`, `false`.
        idempotency_key (str):
        dona_dry_run (str | Unset): Known values (open set — tolerate new ones): `true`, `false`.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):
        body (StockRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkResult | Error | HeldForReview]
    """

    kwargs = _get_kwargs(
        body=body,
        atomic=atomic,
        dry_run=dry_run,
        idempotency_key=idempotency_key,
        dona_dry_run=dona_dry_run,
        accept_language=accept_language,
        dona_seller=dona_seller,
        x_dona_integration=x_dona_integration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: StockRequest,
    atomic: bool | Unset = UNSET,
    dry_run: str | Unset = UNSET,
    idempotency_key: str,
    dona_dry_run: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    dona_seller: UUID | Unset = UNSET,
    x_dona_integration: str | Unset = UNSET,
) -> BulkResult | Error | HeldForReview | None:
    """Set absolute stock (≤ 1 000 lines)

     Synchronous, through `catalog.ApplyGuardedStockPrice`. `200` with per-line results — the request is
    refused whole only for shape/budget (400/413/422). `?atomic=true` = all-or-nothing (any held line ⇒
    `202` for the batch). |Δ| > 10× and > 1 000, or zeroing > 50 % of lines ⇒ `held`. One object ≤ 1
    write / 10 s ⇒ line `error: object_cooldown`. Kill switch: `writes_enabled`.

    Args:
        atomic (bool | Unset):
        dry_run (str | Unset): Known values (open set — tolerate new ones): `true`, `false`.
        idempotency_key (str):
        dona_dry_run (str | Unset): Known values (open set — tolerate new ones): `true`, `false`.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        dona_seller (UUID | Unset):
        x_dona_integration (str | Unset):
        body (StockRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkResult | Error | HeldForReview
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            atomic=atomic,
            dry_run=dry_run,
            idempotency_key=idempotency_key,
            dona_dry_run=dona_dry_run,
            accept_language=accept_language,
            dona_seller=dona_seller,
            x_dona_integration=x_dona_integration,
        )
    ).parsed
