package webhook

import (
	"encoding/json"
	"net/http"
	"os"
	"strconv"
	"testing"
	"time"
)

// TestVectors runs the shared vectors (examples/testdata/webhook-vectors.json).
func TestVectors(t *testing.T) {
	raw, err := os.ReadFile("../../testdata/webhook-vectors.json")
	if err != nil {
		t.Fatal(err)
	}
	var v struct {
		Cases []struct {
			Name, Secret, ID, Body, Signature string
			Timestamp, Now                    int64
			Valid                             bool
		}
	}
	if err := json.Unmarshal(raw, &v); err != nil {
		t.Fatal(err)
	}
	if len(v.Cases) == 0 {
		t.Fatal("no vectors")
	}
	for _, c := range v.Cases {
		h := http.Header{}
		h.Set("webhook-id", c.ID)
		h.Set("webhook-timestamp", strconv.FormatInt(c.Timestamp, 10))
		h.Set("webhook-signature", c.Signature)
		err := Verify(c.Secret, h, []byte(c.Body), time.Unix(c.Now, 0))
		if (err == nil) != c.Valid {
			t.Errorf("%s: err=%v, want valid=%t", c.Name, err, c.Valid)
		}
	}
	t.Logf("go webhook: %d vectors", len(v.Cases))
}
