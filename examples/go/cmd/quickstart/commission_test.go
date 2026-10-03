package main

// The GET /commission body as ozb-backend BE-C7 (#1005) serves it decodes into the Go SDK's types
// with every commission-campaign field — and a body from before BE-C7 still decodes (an older
// server, or a shop campaigns do not apply to, never breaks a client built on this SDK).

import (
	"encoding/json"
	"testing"

	dona "github.com/ozbuz/dona-api/sdks/go"
)

// A shop on an all-categories campaign that beats its launch offer (offer.code = campaign), plus a
// promised category-scoped grant (nothing dated until the shop opens), and a root whose effective
// range is below the card.
const campaignBody = `{
 "seller_id":"01972a10-2222-7aaa-8bbb-0123456789ab","default_pct":10,"start_pct":10,
 "roots":[{"id":"01972a10-1111-7aaa-8bbb-0123456789ab","slug":"kiyim","name":{"uz":"Kiyim","ru":"Одежда","en":"Clothing"},
   "min_pct":10,"max_pct":20,"leaf_count":65,"l2_names":[],"thumb_url":null,"effective_min_pct":0,"effective_max_pct":5}],
 "offer":{"code":"campaign","rule_id":"","campaign_id":"01972a10-4444-7aaa-8bbb-0123456789ab",
   "name":{"uz":"Yangi doʻkonlar","ru":"Новые магазины","en":"New shops"},"state":"running",
   "effect_type":"absolute_pct","effect_pct":0,"days":60,"starts_at":"2026-10-01T06:12:00Z",
   "ends_at":"2026-11-29T18:59:59Z","days_left":57},
 "saved_uzs":125000,
 "campaigns":[
  {"campaign_id":"01972a10-4444-7aaa-8bbb-0123456789ab","grant_id":"01972a10-5555-7aaa-8bbb-0123456789ab",
   "code":"LAUNCH-0","name":{"uz":"Yangi doʻkonlar"},"kind":"new_registration","state":"running","scope":"all",
   "categories":[],"effect_type":"absolute_pct","effect_pct":0,"combinable":false,"days":60,
   "starts_at":"2026-10-01T06:12:00Z","ends_at":"2026-11-29T18:59:59Z","days_left":57,"progress":null},
  {"campaign_id":"01972a10-6666-7aaa-8bbb-0123456789ab","grant_id":"01972a10-7777-7aaa-8bbb-0123456789ab",
   "code":"KIYIM-5","name":{"uz":"Kiyim −50%"},"kind":"existing_seller","state":"promised","scope":"categories",
   "categories":[{"id":"01972a10-1111-7aaa-8bbb-0123456789ab","name":{"uz":"Kiyim"},"effect_type":"relative_discount_pct","effect_pct":50}],
   "effect_type":"relative_discount_pct","effect_pct":50,"combinable":true,"days":30,
   "starts_at":null,"ends_at":null,"days_left":null,"progress":null}]}`

func TestCommissionCampaignFieldsDecode(t *testing.T) {
	var c dona.Commission
	if err := json.Unmarshal([]byte(campaignBody), &c); err != nil {
		t.Fatalf("decode: %v", err)
	}
	if c.Offer == nil || c.Offer.Code != "campaign" || c.Offer.CampaignId == nil || c.Offer.Name == nil || c.Offer.RuleId != "" {
		t.Fatalf("offer: %+v", c.Offer)
	}
	if c.SavedUzs == nil || *c.SavedUzs != 125000 {
		t.Fatalf("saved_uzs: %v", c.SavedUzs)
	}
	r := c.Roots[0]
	if r.MinPct != 10 || r.MaxPct != 20 || r.EffectiveMinPct != 0 || r.EffectiveMaxPct != 5 {
		t.Fatalf("root: card %g–%g, effective %g–%g", r.MinPct, r.MaxPct, r.EffectiveMinPct, r.EffectiveMaxPct)
	}
	if len(c.Campaigns) != 2 {
		t.Fatalf("campaigns: %d", len(c.Campaigns))
	}
	run, prom := c.Campaigns[0], c.Campaigns[1]
	if run.Code != "LAUNCH-0" || run.Kind != "new_registration" || run.State != "running" || run.Scope != "all" ||
		run.EndsAt == nil || run.DaysLeft == nil || *run.DaysLeft != 57 || run.Progress != nil {
		t.Fatalf("running grant: %+v", run)
	}
	// A promise is undated: starts_at / ends_at / days_left are null, never a zero time or 0 days.
	if prom.State != "promised" || prom.StartsAt != nil || prom.EndsAt != nil || prom.DaysLeft != nil || !prom.Combinable {
		t.Fatalf("promised grant: %+v", prom)
	}
	if len(prom.Categories) != 1 || prom.Categories[0].EffectType != "relative_discount_pct" || prom.Categories[0].EffectPct != 50 {
		t.Fatalf("categories: %+v", prom.Categories)
	}
}

// NEGATIVE: a body from before BE-C7 (no campaigns[], no effective_*, saved_uzs null) still decodes —
// the new fields read as absent, nothing errors.
func TestCommissionPreCampaignBodyStillDecodes(t *testing.T) {
	const old = `{"seller_id":"01972a10-2222-7aaa-8bbb-0123456789ab","default_pct":10,"start_pct":10,
	 "roots":[{"id":"01972a10-1111-7aaa-8bbb-0123456789ab","slug":"kiyim","name":{"uz":"Kiyim"},"min_pct":10,"max_pct":20,
	   "leaf_count":65,"l2_names":[],"thumb_url":null}],
	 "offer":null,"saved_uzs":null}`
	var c dona.Commission
	if err := json.Unmarshal([]byte(old), &c); err != nil {
		t.Fatalf("decode: %v", err)
	}
	if c.Offer != nil || c.SavedUzs != nil || len(c.Campaigns) != 0 || c.Roots[0].EffectiveMaxPct != 0 {
		t.Fatalf("pre-campaign body: %+v", c)
	}
}

// The per-category rate a sale is charged (GET /categories/{id}/requirements) is a field of its own,
// beside the card's commission_pct, and its end is nullable.
func TestRequirementsEffectiveCommission(t *testing.T) {
	var q dona.CategoryRequirements
	body := `{"commission_pct":12,"effective_commission_pct":0,"commission_offer_ends_at":null}`
	if err := json.Unmarshal([]byte(body), &q); err != nil {
		t.Fatalf("decode: %v", err)
	}
	if q.CommissionPct == nil || *q.CommissionPct != 12 || q.EffectiveCommissionPct != 0 || q.CommissionOfferEndsAt != nil {
		t.Fatalf("requirements: pct %v effective %g ends %v", q.CommissionPct, q.EffectiveCommissionPct, q.CommissionOfferEndsAt)
	}
}
