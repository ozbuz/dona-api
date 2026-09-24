// Command mockapi is a local stand-in for https://api.dona.im/seller-api/v1, used ONLY by
// `make -C examples smoke` to prove each language's quickstart sends what the contract requires and
// can decode what the contract promises. It is not a simulator of Dona's behaviour.
//
// For a request it finds the operation in spec/openapi.yaml (the contract, not the client view), then:
//   - refuses a missing/non-`Bearer dona_…` Authorization with 401 (the contract's error envelope);
//   - refuses a write whose operation declares `Idempotency-Key` when the header is absent (400);
//   - otherwise answers the operation's documented 200 `example`, with the rate-limit headers (and, on a
//     dry run, `dry_run: true` where the example has that field).
//
// Every request is appended to -log as one JSON line; the smoke script asserts on that log.
//
//	mockapi -spec spec/openapi.yaml -log $RUNNER_TEMP/mock.jsonl -addr-file $RUNNER_TEMP/mock.addr
package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"log"
	"net"
	"net/http"
	"os"
	"strings"
	"sync"

	"gopkg.in/yaml.v3"
)

const prefix = "/seller-api/v1"

type operation struct {
	method, template string
	segments         []string
	needsIdempotency bool
	example          any
}

type entry struct {
	Method         string `json:"method"`
	Path           string `json:"path"`
	Query          string `json:"query"`
	Status         int    `json:"status"`
	Authorized     bool   `json:"authorized"`
	IdempotencyKey string `json:"idempotency_key,omitempty"`
	DryRun         bool   `json:"dry_run"`
	Integration    string `json:"integration,omitempty"`
}

func main() {
	specPath := flag.String("spec", "spec/openapi.yaml", "the contract")
	logPath := flag.String("log", "", "append one JSON line per request (required)")
	addr := flag.String("addr", "127.0.0.1:0", "listen address (port 0 = any free port)")
	addrFile := flag.String("addr-file", "", "write the bound host:port here once listening")
	flag.Parse()
	if *logPath == "" {
		log.Fatal("mockapi: -log is required")
	}

	ops, err := load(*specPath)
	if err != nil {
		log.Fatal("mockapi: ", err)
	}
	lf, err := os.OpenFile(*logPath, os.O_CREATE|os.O_APPEND|os.O_WRONLY, 0o644)
	if err != nil {
		log.Fatal("mockapi: ", err)
	}
	var mu sync.Mutex
	record := func(e entry) {
		mu.Lock()
		defer mu.Unlock()
		b, _ := json.Marshal(e)
		_, _ = lf.Write(append(b, '\n'))
	}

	ln, err := net.Listen("tcp", *addr)
	if err != nil {
		log.Fatal("mockapi: ", err)
	}
	if *addrFile != "" {
		if err := os.WriteFile(*addrFile, []byte(ln.Addr().String()), 0o644); err != nil {
			log.Fatal("mockapi: ", err)
		}
	}
	log.Printf("mockapi: %d operations, listening on http://%s%s", len(ops), ln.Addr(), prefix)
	log.Fatal(http.Serve(ln, http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		e := entry{Method: r.Method, Path: r.URL.Path, Query: r.URL.RawQuery,
			IdempotencyKey: r.Header.Get("Idempotency-Key"), Integration: r.Header.Get("X-Dona-Integration"),
			DryRun: r.URL.Query().Get("dry_run") == "true" || r.Header.Get("Dona-Dry-Run") == "true"}
		auth := r.Header.Get("Authorization")
		e.Authorized = strings.HasPrefix(auth, "Bearer dona_") && len(auth) > len("Bearer dona_")
		e.Status = serve(w, r, ops, e)
		record(e)
	})))
}

func serve(w http.ResponseWriter, r *http.Request, ops []operation, e entry) int {
	h := w.Header()
	h.Set("Content-Type", "application/json")
	h.Set("Dona-Request-Id", "req_01997b2e-0000-7000-8000-000000000000")
	h.Set("RateLimit-Policy", `"key-rate";q=600;w=60`)
	h.Set("RateLimit", `"key-rate";r=599;t=60`)
	h.Set("X-RateLimit-Limit", "600")
	h.Set("X-RateLimit-Remaining", "599")
	h.Set("X-RateLimit-Reset", "60")

	op := match(ops, r.Method, strings.TrimPrefix(r.URL.Path, prefix))
	switch {
	case !strings.HasPrefix(r.URL.Path, prefix) || op == nil:
		return fail(w, http.StatusNotFound, "not_found", "No such operation in the contract.")
	case !e.Authorized:
		return fail(w, http.StatusUnauthorized, "api_key_malformed", "API kaliti yuborilmagan yoki notoʻgʻri.")
	case op.needsIdempotency && e.IdempotencyKey == "":
		return fail(w, http.StatusBadRequest, "invalid_body", "Idempotency-Key is required on this write.")
	case op.example == nil:
		return fail(w, http.StatusNotImplemented, "no_example", "The contract has no 200 example for "+op.template+".")
	}
	body := op.example
	if m, ok := body.(map[string]any); ok && e.DryRun {
		if _, has := m["dry_run"]; has { // echo the rehearsal flag the way the server does
			c := make(map[string]any, len(m))
			for k, v := range m {
				c[k] = v
			}
			c["dry_run"] = true
			body = c
		}
	}
	w.WriteHeader(http.StatusOK)
	_ = json.NewEncoder(w).Encode(body)
	return http.StatusOK
}

func fail(w http.ResponseWriter, status int, code, msg string) int {
	w.WriteHeader(status)
	_ = json.NewEncoder(w).Encode(map[string]any{"error": code, "message": msg,
		"request_id": "req_01997b2e-0000-7000-8000-000000000000", "details": []any{},
		"doc_url": "https://api.dona.im/seller-api/v1/openapi.json"})
	return status
}

func match(ops []operation, method, path string) *operation {
	segs := strings.Split(strings.Trim(path, "/"), "/")
	for i := range ops {
		op := &ops[i]
		if op.method != method || len(op.segments) != len(segs) {
			continue
		}
		ok := true
		for j, s := range op.segments {
			if !strings.HasPrefix(s, "{") && s != segs[j] {
				ok = false
				break
			}
		}
		if ok {
			return op
		}
	}
	return nil
}

func load(path string) ([]operation, error) {
	src, err := os.ReadFile(path)
	if err != nil {
		return nil, err
	}
	var doc map[string]any
	if err := yaml.Unmarshal(src, &doc); err != nil {
		return nil, fmt.Errorf("%s: %w", path, err)
	}
	paths, _ := doc["paths"].(map[string]any)
	var ops []operation
	for tmpl, item := range paths {
		methods, _ := item.(map[string]any)
		for m, raw := range methods {
			o, ok := raw.(map[string]any)
			if !ok || m == "parameters" {
				continue
			}
			op := operation{method: strings.ToUpper(m), template: tmpl, segments: strings.Split(strings.Trim(tmpl, "/"), "/")}
			params, _ := o["parameters"].([]any)
			for _, p := range params {
				pm, _ := p.(map[string]any)
				if ref, _ := pm["$ref"].(string); ref == "#/components/parameters/IdempotencyKey" {
					op.needsIdempotency = true
				}
			}
			op.example = dig(o, "responses", "200", "content", "application/json", "example")
			ops = append(ops, op)
		}
	}
	return ops, nil
}

func dig(v any, keys ...string) any {
	for _, k := range keys {
		m, ok := v.(map[string]any)
		if !ok {
			return nil
		}
		v = m[k]
	}
	return v
}
