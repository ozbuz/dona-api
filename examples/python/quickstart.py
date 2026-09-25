"""Dona API quickstart — the portal's "Boshlash" steps 2–4, in Python.

    DONA_API_KEY=dona_sk_live_… uv run --with ../../sdks/python python quickstart.py
    (or: pip install ../../sdks/python && python quickstart.py)

1. GET /me                   who the key is: shop, tier, limits
2. GET /products?limit=5     the first page of the catalogue
3. POST /stock?dry_run=true  re-sends the first product's CURRENT stock as a rehearsal: validated,
                             guarded and rolled back — nothing is written, whatever the answer.

Optional: DONA_API_BASE_URL (defaults to production, the only environment).
"""

import os
import sys
import uuid
from typing import Any, NoReturn

from dona_api import AuthenticatedClient
from dona_api.api.account import get_me
from dona_api.api.catalog import list_products
from dona_api.api.stock_prices import set_stock
from dona_api.models import BulkResult, Error, HeldForReview, StockLine, StockRequest
from dona_api.types import UNSET, Response

BASE_URL = "https://api.dona.im/seller-api/v1"


def fail(step: str, resp: Response[Any]) -> NoReturn:
    # Branch on `error` (a stable code), never on `message` (localised text).
    err = resp.parsed if isinstance(resp.parsed, Error) else None
    code = err.error if err else ""
    msg = err.message if err else resp.content[:200].decode(errors="replace")
    print(f"{step} → HTTP {int(resp.status_code)} {code}: {msg}", file=sys.stderr)
    if "Retry-After" in resp.headers:
        reason = resp.headers.get("Dona-Rate-Limited-Reason", "rate limited")
        print(f"  retry after {resp.headers['Retry-After']}s ({reason})", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    api_key = os.environ.get("DONA_API_KEY")
    if not api_key:
        sys.exit("Set DONA_API_KEY (dona_sk_live_…) — the shop owner mints it in Sozlamalar › API.")

    client = AuthenticatedClient(
        base_url=os.environ.get("DONA_API_BASE_URL", BASE_URL),
        token=api_key,  # sent as `Authorization: Bearer <key>`
        headers={"X-Dona-Integration": "dona-api-examples/python"},
        raise_on_unexpected_status=False,
    )
    with client:
        # 1 ─ who am I
        me = get_me.sync_detailed(client=client)
        if int(me.status_code) != 200 or me.parsed is None or isinstance(me.parsed, Error):
            fail("GET /me", me)
        print(
            f"shop: {me.parsed.shop.name} ({me.parsed.shop.status}) · tier {me.parsed.tier}"
            f" · writes_enabled {str(me.parsed.writes_enabled).lower()}"
        )
        print(
            f"rate limit: {me.headers.get('X-RateLimit-Remaining', '?')}/{me.headers.get('X-RateLimit-Limit', '?')}"
            f" left · policy {me.headers.get('RateLimit-Policy', '?')}"
        )

        # 2 ─ first five products
        page = list_products.sync_detailed(client=client, limit=5)
        if int(page.status_code) != 200 or page.parsed is None or isinstance(page.parsed, Error):
            fail("GET /products", page)
        for p in page.parsed.items:
            title = p.title.uz if p.title.uz is not UNSET else p.title.ru
            print(f"  {p.id}  {p.seller_sku or '-'}  stock {p.stock}  {title}")

        # 3 ─ rehearse a stock write
        if not page.parsed.items:
            print("no products yet — skipping the POST /stock rehearsal")
            return
        first = page.parsed.items[0]
        if first.variants:
            v = first.variants[0]
            line = StockLine(product_id=first.id, variant_id=v.id, quantity=v.stock)
        else:
            line = StockLine(product_id=first.id, quantity=first.stock)

        resp = set_stock.sync_detailed(
            client=client,
            body=StockRequest(items=[line]),
            dry_run="true",
            # One key per logical write. Re-send the SAME key on a retry: the answer is replayed for 24 h.
            idempotency_key=str(uuid.uuid4()),
        )
        if isinstance(resp.parsed, HeldForReview):
            print(
                f"POST /stock held for review: rule {resp.parsed.rule} · approval {resp.parsed.approval_id}"
                " — nothing was written"
            )
        elif isinstance(resp.parsed, BulkResult):
            s = resp.parsed.summary
            print(
                f"POST /stock dry_run={str(resp.parsed.dry_run).lower()}: ok {s.ok} · error {s.error} · held {s.held}"
            )
        else:
            fail("POST /stock", resp)


if __name__ == "__main__":
    main()
