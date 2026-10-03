// Command quickstart runs the Dona API portal's "Boshlash" steps 2–4 in Go:
// GET /me (who the key is: shop, tier, limits), GET /commission (what Dona charges the shop: the
// rate card, this shop's own range per category, the running offer and its commission campaigns),
// GET /products?limit=5 (the first page of the catalogue), then POST /stock?dry_run=true, which
// re-sends the first product's CURRENT stock as a rehearsal — validated, guarded and rolled back, so
// nothing is written whatever the answer.
//
// Usage:
//
//	DONA_API_KEY=dona_sk_live_… go run ./cmd/quickstart
//
// Optional: DONA_API_BASE_URL (defaults to production, the only environment).
package main

import (
	"context"
	"crypto/rand"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"time"

	dona "github.com/ozbuz/dona-api/sdks/go"
)

func main() {
	apiKey := os.Getenv("DONA_API_KEY")
	if apiKey == "" {
		fmt.Fprintln(os.Stderr, "Set DONA_API_KEY (dona_sk_live_…) — the shop owner mints it in Sozlamalar › API.")
		os.Exit(2)
	}
	opts := []dona.ClientOption{
		dona.WithHTTPClient(&http.Client{Timeout: 30 * time.Second}),
		dona.WithRequestEditorFn(func(_ context.Context, r *http.Request) error {
			r.Header.Set("X-Dona-Integration", "dona-api-examples/go")
			return nil
		}),
	}
	if u := os.Getenv("DONA_API_BASE_URL"); u != "" {
		opts = append(opts, dona.WithBaseURL(u))
	}
	c, err := dona.NewDonaClient(apiKey, opts...)
	check("client", err)
	ctx := context.Background()

	// 1 ─ who am I
	me, err := c.GetMeWithResponse(ctx, &dona.GetMeParams{})
	check("GET /me", err)
	if me.JSON200 == nil {
		fail("GET /me", me.HTTPResponse, me.Body)
	}
	fmt.Printf("shop: %s (%s) · tier %s · writes_enabled %t\n",
		me.JSON200.Shop.Name, me.JSON200.Shop.Status, me.JSON200.Tier, me.JSON200.WritesEnabled)
	h := me.HTTPResponse.Header
	fmt.Printf("rate limit: %s/%s left · policy %s\n",
		h.Get("X-RateLimit-Remaining"), h.Get("X-RateLimit-Limit"), h.Get("RateLimit-Policy"))

	// 2 ─ what Dona charges this shop (read only)
	com, err := c.GetCommissionWithResponse(ctx, &dona.GetCommissionParams{})
	check("GET /commission", err)
	if com.JSON200 == nil {
		fail("GET /commission", com.HTTPResponse, com.Body)
	}
	offer := "none"
	if o := com.JSON200.Offer; o != nil {
		offer = fmt.Sprintf("%s (%s, %g%%)", o.Code, o.State, o.EffectPct)
	}
	fmt.Printf("commission: from %g%% · offer %s · campaigns %d\n", com.JSON200.StartPct, offer, len(com.JSON200.Campaigns))
	for _, r := range com.JSON200.Roots {
		// min/max = the platform's card; effective_* = what THIS shop is charged after its rules and campaigns.
		fmt.Printf("  %s  card %g–%g%% · yours %g–%g%%\n", r.Slug, r.MinPct, r.MaxPct, r.EffectiveMinPct, r.EffectiveMaxPct)
	}
	for _, cp := range com.JSON200.Campaigns {
		fmt.Printf("  campaign %s (%s, %s) %s %g%%\n", cp.Code, cp.Kind, cp.State, cp.EffectType, cp.EffectPct)
	}

	// 3 ─ first five products
	limit := dona.Limit(5)
	page, err := c.ListProductsWithResponse(ctx, &dona.ListProductsParams{Limit: &limit})
	check("GET /products", err)
	if page.JSON200 == nil {
		fail("GET /products", page.HTTPResponse, page.Body)
	}
	for _, p := range page.JSON200.Items {
		fmt.Printf("  %s  %s  stock %d  %s\n", p.Id, deref(p.SellerSku, "-"), p.Stock, deref(p.Title.Uz, deref(p.Title.Ru, "")))
	}

	// 4 ─ rehearse a stock write
	if len(page.JSON200.Items) == 0 {
		fmt.Println("no products yet — skipping the POST /stock rehearsal")
		return
	}
	first := page.JSON200.Items[0]
	line := dona.StockLine{ProductId: &first.Id, Quantity: first.Stock}
	if len(first.Variants) > 0 {
		v := first.Variants[0]
		line.VariantId, line.Quantity = &v.Id, v.Stock
	}
	dryRun := "true"
	res, err := c.SetStockWithResponse(ctx, &dona.SetStockParams{
		DryRun: &dryRun,
		// One key per logical write. Re-send the SAME key on a retry: the answer is replayed for 24 h.
		IdempotencyKey: rand.Text(),
	}, dona.SetStockJSONRequestBody{Items: []dona.StockLine{line}})
	check("POST /stock", err)
	switch {
	case res.JSON202 != nil:
		fmt.Printf("POST /stock held for review: rule %s · approval %s — nothing was written\n", res.JSON202.Rule, res.JSON202.ApprovalId)
	case res.JSON200 != nil:
		s := res.JSON200.Summary
		fmt.Printf("POST /stock dry_run=%t: ok %d · error %d · held %d\n", res.JSON200.DryRun, s.Ok, s.Error, s.Held)
	default:
		fail("POST /stock", res.HTTPResponse, res.Body)
	}
}

// fail prints the error envelope. Branch on `error` (a stable code), never on `message` (localised).
func fail(step string, r *http.Response, body []byte) {
	var e dona.Error
	_ = json.Unmarshal(body, &e)
	fmt.Fprintf(os.Stderr, "%s → HTTP %d %s: %s (request %s)\n", step, r.StatusCode, e.Error, e.Message, e.RequestId)
	if ra := r.Header.Get("Retry-After"); ra != "" {
		fmt.Fprintf(os.Stderr, "  retry after %ss (%s)\n", ra, r.Header.Get("Dona-Rate-Limited-Reason"))
	}
	os.Exit(1)
}

func check(step string, err error) {
	if err != nil {
		fmt.Fprintf(os.Stderr, "%s: %v\n", step, err)
		os.Exit(1)
	}
}

func deref(s *string, fallback string) string {
	if s == nil || *s == "" {
		return fallback
	}
	return *s
}
