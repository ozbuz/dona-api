// Package webhook verifies Dona webhook deliveries (Standard Webhooks) — standard library only.
//
// Headers on every delivery: webhook-id · webhook-timestamp · webhook-signature.
//
//	signature = space-delimited "v1,<base64 HMAC-SHA256(base64decode(secret after whsec_), id.ts.rawBody)>"
//	(two entries for 24 h after a secret rotation — accept if ANY matches)
//
// ⚠ Verify the RAW request bytes; re-serialised JSON never matches. Then dedupe on webhook-id for 24 h.
//
//	http.HandleFunc("/dona/webhooks", func(w http.ResponseWriter, r *http.Request) {
//		body, _ := io.ReadAll(http.MaxBytesReader(w, r.Body, 1<<20))
//		if err := webhook.Verify(os.Getenv("DONA_WEBHOOK_SECRET"), r.Header, body, time.Now()); err != nil {
//			http.Error(w, "bad signature", http.StatusUnauthorized)
//			return
//		}
//		w.WriteHeader(http.StatusNoContent) // acknowledge fast; process asynchronously
//	})
package webhook

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/base64"
	"errors"
	"net/http"
	"strconv"
	"strings"
	"time"
)

// Tolerance is the maximum |now − webhook-timestamp|.
const Tolerance = 300 * time.Second

// Errors returned by Verify.
var (
	ErrMissingHeaders = errors.New("webhook: missing webhook-* headers")
	ErrTimestamp      = errors.New("webhook: timestamp outside tolerance")
	ErrSignature      = errors.New("webhook: no matching signature")
)

// Verify returns nil only when the delivery is authentic and fresh.
func Verify(secret string, h http.Header, rawBody []byte, now time.Time) error {
	id, ts, sigs := h.Get("webhook-id"), h.Get("webhook-timestamp"), h.Get("webhook-signature")
	if id == "" || ts == "" || sigs == "" {
		return ErrMissingHeaders
	}
	sec, err := strconv.ParseInt(ts, 10, 64)
	if err != nil {
		return ErrTimestamp
	}
	if d := now.Sub(time.Unix(sec, 0)); d > Tolerance || d < -Tolerance {
		return ErrTimestamp
	}
	key, err := base64.StdEncoding.DecodeString(strings.TrimPrefix(secret, "whsec_"))
	if err != nil {
		return errors.New("webhook: secret is not base64 after whsec_")
	}
	mac := hmac.New(sha256.New, key)
	mac.Write([]byte(id + "." + ts + "."))
	mac.Write(rawBody)
	expected := mac.Sum(nil)
	for _, entry := range strings.Split(sigs, " ") {
		version, sig, ok := strings.Cut(entry, ",")
		if !ok || version != "v1" {
			continue
		}
		got, err := base64.StdEncoding.DecodeString(sig)
		if err == nil && hmac.Equal(got, expected) {
			return nil
		}
	}
	return ErrSignature
}
