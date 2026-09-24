from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delivery import Delivery
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    delivery_id: UUID,
    *,
    idempotency_key: str,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    if not isinstance(x_dona_integration, Unset):
        headers["X-Dona-Integration"] = x_dona_integration

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhooks/{id}/deliveries/{delivery_id}/redeliver".format(
            id=quote(str(id), safe=""),
            delivery_id=quote(str(delivery_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Delivery | Error | None:
    if response.status_code == 200:
        response_200 = Delivery.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Delivery | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    delivery_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    idempotency_key: str,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Response[Delivery | Error]:
    """Redeliver one delivery

     Fresh timestamp + signature, same `webhook-id`; a new attempt chain. ≤ 100/hour/endpoint. An event
    older than 30 d ⇒ `404 not_found`.

    Args:
        id (UUID):
        delivery_id (UUID):
        idempotency_key (str):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Delivery | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        delivery_id=delivery_id,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
        x_dona_integration=x_dona_integration,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    delivery_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    idempotency_key: str,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Delivery | Error | None:
    """Redeliver one delivery

     Fresh timestamp + signature, same `webhook-id`; a new attempt chain. ≤ 100/hour/endpoint. An event
    older than 30 d ⇒ `404 not_found`.

    Args:
        id (UUID):
        delivery_id (UUID):
        idempotency_key (str):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Delivery | Error
    """

    return sync_detailed(
        id=id,
        delivery_id=delivery_id,
        client=client,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
        x_dona_integration=x_dona_integration,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    delivery_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    idempotency_key: str,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Response[Delivery | Error]:
    """Redeliver one delivery

     Fresh timestamp + signature, same `webhook-id`; a new attempt chain. ≤ 100/hour/endpoint. An event
    older than 30 d ⇒ `404 not_found`.

    Args:
        id (UUID):
        delivery_id (UUID):
        idempotency_key (str):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Delivery | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        delivery_id=delivery_id,
        idempotency_key=idempotency_key,
        accept_language=accept_language,
        x_dona_integration=x_dona_integration,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    delivery_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    idempotency_key: str,
    accept_language: str | Unset = "uz",
    x_dona_integration: str | Unset = UNSET,
) -> Delivery | Error | None:
    """Redeliver one delivery

     Fresh timestamp + signature, same `webhook-id`; a new attempt chain. ≤ 100/hour/endpoint. An event
    older than 30 d ⇒ `404 not_found`.

    Args:
        id (UUID):
        delivery_id (UUID):
        idempotency_key (str):
        accept_language (str | Unset): Known values (open set — tolerate new ones): `uz`, `ru`,
            `en`. Default: 'uz'.
        x_dona_integration (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Delivery | Error
    """

    return (
        await asyncio_detailed(
            id=id,
            delivery_id=delivery_id,
            client=client,
            idempotency_key=idempotency_key,
            accept_language=accept_language,
            x_dona_integration=x_dona_integration,
        )
    ).parsed
