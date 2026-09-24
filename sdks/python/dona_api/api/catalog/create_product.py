from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.held_for_review import HeldForReview
from ...models.product_create import ProductCreate
from ...models.product_created import ProductCreated
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ProductCreate,
    dry_run: bool | Unset = UNSET,
    idempotency_key: str,
    dona_dry_run: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    if not isinstance(dona_dry_run, Unset):
        headers["Dona-Dry-Run"] = dona_dry_run

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_dona_integration, Unset):
        headers["X-Dona-Integration"] = x_dona_integration

    params: dict[str, Any] = {}

    params["dry_run"] = dry_run

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/products",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | HeldForReview | ProductCreated | None:
    if response.status_code == 201:
        response_201 = ProductCreated.from_dict(response.json())

        return response_201

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
) -> Response[Error | HeldForReview | ProductCreated]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ProductCreate,
    dry_run: bool | Unset = UNSET,
    idempotency_key: str,
    dona_dry_run: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Response[Error | HeldForReview | ProductCreated]:
    """Create a product (lands as draft / ai_review)

     `UpsertExternalProduct` with `created_via='api'`. Lands `draft`/`ai_review`; `publish:true` asks to
    publish, and a pending shop's publish waits in `product_shop_holds`
    (`hold.reason=shop_not_activated`). The plausibility guard may answer `202 held_for_review` (e.g.
    `price_floor`). Kill switch: `writes_enabled`.

    Args:
        dry_run (bool | Unset):
        idempotency_key (str):
        dona_dry_run (str | Unset): Known values (open set — tolerate new ones): `true`, `false`.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):
        body (ProductCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | HeldForReview | ProductCreated]
    """

    kwargs = _get_kwargs(
        body=body,
        dry_run=dry_run,
        idempotency_key=idempotency_key,
        dona_dry_run=dona_dry_run,
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
    body: ProductCreate,
    dry_run: bool | Unset = UNSET,
    idempotency_key: str,
    dona_dry_run: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Error | HeldForReview | ProductCreated | None:
    """Create a product (lands as draft / ai_review)

     `UpsertExternalProduct` with `created_via='api'`. Lands `draft`/`ai_review`; `publish:true` asks to
    publish, and a pending shop's publish waits in `product_shop_holds`
    (`hold.reason=shop_not_activated`). The plausibility guard may answer `202 held_for_review` (e.g.
    `price_floor`). Kill switch: `writes_enabled`.

    Args:
        dry_run (bool | Unset):
        idempotency_key (str):
        dona_dry_run (str | Unset): Known values (open set — tolerate new ones): `true`, `false`.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):
        body (ProductCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | HeldForReview | ProductCreated
    """

    return sync_detailed(
        client=client,
        body=body,
        dry_run=dry_run,
        idempotency_key=idempotency_key,
        dona_dry_run=dona_dry_run,
        accept_language=accept_language,
        x_dona_integration=x_dona_integration,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ProductCreate,
    dry_run: bool | Unset = UNSET,
    idempotency_key: str,
    dona_dry_run: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Response[Error | HeldForReview | ProductCreated]:
    """Create a product (lands as draft / ai_review)

     `UpsertExternalProduct` with `created_via='api'`. Lands `draft`/`ai_review`; `publish:true` asks to
    publish, and a pending shop's publish waits in `product_shop_holds`
    (`hold.reason=shop_not_activated`). The plausibility guard may answer `202 held_for_review` (e.g.
    `price_floor`). Kill switch: `writes_enabled`.

    Args:
        dry_run (bool | Unset):
        idempotency_key (str):
        dona_dry_run (str | Unset): Known values (open set — tolerate new ones): `true`, `false`.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):
        body (ProductCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | HeldForReview | ProductCreated]
    """

    kwargs = _get_kwargs(
        body=body,
        dry_run=dry_run,
        idempotency_key=idempotency_key,
        dona_dry_run=dona_dry_run,
        accept_language=accept_language,
        x_dona_integration=x_dona_integration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ProductCreate,
    dry_run: bool | Unset = UNSET,
    idempotency_key: str,
    dona_dry_run: str | Unset = UNSET,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Error | HeldForReview | ProductCreated | None:
    """Create a product (lands as draft / ai_review)

     `UpsertExternalProduct` with `created_via='api'`. Lands `draft`/`ai_review`; `publish:true` asks to
    publish, and a pending shop's publish waits in `product_shop_holds`
    (`hold.reason=shop_not_activated`). The plausibility guard may answer `202 held_for_review` (e.g.
    `price_floor`). Kill switch: `writes_enabled`.

    Args:
        dry_run (bool | Unset):
        idempotency_key (str):
        dona_dry_run (str | Unset): Known values (open set — tolerate new ones): `true`, `false`.
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):
        body (ProductCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | HeldForReview | ProductCreated
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            dry_run=dry_run,
            idempotency_key=idempotency_key,
            dona_dry_run=dona_dry_run,
            accept_language=accept_language,
            x_dona_integration=x_dona_integration,
        )
    ).parsed
