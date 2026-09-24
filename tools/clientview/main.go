// Command clientview derives the CLIENT VIEW of the Dona API contract that the SDK generators read:
// stdin OpenAPI 3.1 YAML → stdout YAML, mapping order and comments kept.
//
// The contract says every enum is OPEN — "new values are additive; clients MUST tolerate an unknown
// value" (info.description › Enums). Several generators (openapi-python-client, openapi-generator's
// php and csharp) turn a JSON-Schema `enum` into a closed type whose deserializer RAISES on a value it
// has not seen, so a server adding `status: "archived"` would break every integrator's sync loop. The
// client view therefore drops `enum` from every string schema and keeps the values as
// `x-dona-known-values` plus one sentence in the description. `const` is left alone: a const is a
// fixed discriminator (`code: held_for_review`), not an open vocabulary.
//
// A second rewrite: an `anyOf`/`oneOf` whose members are ONLY `required: [...]` lists (StockLine,
// PriceLine: "exactly one of product_id · seller_sku · barcode · external_id") is a presence rule, not
// a type. openapi-python-client reads it as a union and types the whole line `Any`, losing every
// field. The client view drops that constraint (the server still enforces it and the description
// already states it) so each SDK keeps the typed object.
//
// Third: info.description (the contract's ~3 kB conventions preamble) is replaced by one paragraph and
// a link. openapi-generator copies it into the header of EVERY php/csharp file and into composer.json;
// the conventions live in the repository README and in the served contract.
//
// It never changes the contract itself: spec/openapi.yaml stays byte-identical to the source of
// truth, and this view lives only in build/ (git-ignored), regenerated on every `make generate`.
package main

import (
	"fmt"
	"io"
	"os"
	"strings"

	"gopkg.in/yaml.v3"
)

func main() {
	src, err := io.ReadAll(os.Stdin)
	if err != nil {
		fail(err)
	}
	var doc yaml.Node
	if err := yaml.Unmarshal(src, &doc); err != nil {
		fail(fmt.Errorf("openapi yaml: %w", err))
	}
	n := 0
	walk(&doc, &n)
	shortInfo(&doc)
	enc := yaml.NewEncoder(os.Stdout)
	enc.SetIndent(2)
	if err := enc.Encode(&doc); err != nil {
		fail(err)
	}
	if err := enc.Close(); err != nil {
		fail(err)
	}
	fmt.Fprintf(os.Stderr, "clientview: opened %d string enums\n", n)
}

func fail(err error) {
	fmt.Fprintln(os.Stderr, "clientview:", err)
	os.Exit(1)
}

func walk(n *yaml.Node, count *int) {
	if n.Kind == yaml.MappingNode {
		openEnum(n, count)
		looseUnion(n)
		dropPresenceRule(n)
	}
	for _, c := range n.Content {
		walk(c, count)
	}
}

// openEnum rewrites one schema mapping in place when it is a string enum.
func openEnum(m *yaml.Node, count *int) {
	enumAt, typ, descAt := -1, (*yaml.Node)(nil), -1
	for i := 0; i+1 < len(m.Content); i += 2 {
		switch m.Content[i].Value {
		case "enum":
			enumAt = i
		case "type":
			typ = m.Content[i+1]
		case "description":
			descAt = i
		}
	}
	if enumAt < 0 || !isString(typ) || m.Content[enumAt+1].Kind != yaml.SequenceNode {
		return
	}
	values := m.Content[enumAt+1]
	var names []string
	for _, v := range values.Content {
		if v.ShortTag() == "!!null" {
			continue
		}
		names = append(names, "`"+v.Value+"`")
	}
	note := "Known values (open set — tolerate new ones): " + strings.Join(names, ", ") + "."
	if descAt >= 0 {
		d := m.Content[descAt+1]
		d.Value = strings.TrimRight(d.Value, "\n") + " " + note
		d.Style = 0
	} else {
		m.Content = append(m.Content,
			&yaml.Node{Kind: yaml.ScalarNode, Tag: "!!str", Value: "description"},
			&yaml.Node{Kind: yaml.ScalarNode, Tag: "!!str", Value: note})
	}
	m.Content[enumAt].Value = "x-dona-known-values"
	*count++
}

// looseUnion turns a multi-type union such as `type: [number, string, null]` (Metric.current_value)
// into an untyped schema. No generator we use can express "a number OR a string" as one field
// (oapi-codegen refuses the whole spec), and an untyped schema decodes to the language's
// any/object/interface{} — lossless. The accepted types are named in the description instead.
func looseUnion(m *yaml.Node) {
	for i := 0; i+1 < len(m.Content); i += 2 {
		if m.Content[i].Value != "type" || m.Content[i+1].Kind != yaml.SequenceNode {
			continue
		}
		var kinds []string
		for _, c := range m.Content[i+1].Content {
			if c.Value != "null" {
				kinds = append(kinds, c.Value)
			}
		}
		if len(kinds) < 2 {
			return
		}
		note := "One of: " + strings.Join(kinds, ", ") + " (or null)."
		m.Content = append(m.Content[:i], m.Content[i+2:]...)
		for j := 0; j+1 < len(m.Content); j += 2 {
			if m.Content[j].Value == "description" {
				d := m.Content[j+1]
				d.Value = strings.TrimRight(d.Value, "\n") + " " + note
				d.Style = 0
				return
			}
		}
		m.Content = append(m.Content,
			&yaml.Node{Kind: yaml.ScalarNode, Tag: "!!str", Value: "description"},
			&yaml.Node{Kind: yaml.ScalarNode, Tag: "!!str", Value: note})
		return
	}
}

const infoDescription = "Dona API v1 (https://api.dona.im/seller-api/v1) — client generated from the OpenAPI contract. " +
	"Conventions (auth, errors, idempotency, dry_run, rate limits, 202 held_for_review): " +
	"https://github.com/ozbuz/dona-api#readme · contract: https://api.dona.im/seller-api/v1/openapi.json"

// shortInfo sets info.description to infoDescription.
func shortInfo(doc *yaml.Node) {
	if doc.Kind != yaml.DocumentNode || len(doc.Content) != 1 {
		return
	}
	root := doc.Content[0]
	for i := 0; i+1 < len(root.Content); i += 2 {
		if root.Content[i].Value != "info" {
			continue
		}
		info := root.Content[i+1]
		for j := 0; j+1 < len(info.Content); j += 2 {
			if info.Content[j].Value == "description" {
				info.Content[j+1].Value = infoDescription
				info.Content[j+1].Style = 0
				return
			}
		}
	}
}

// dropPresenceRule removes `anyOf`/`oneOf` from a schema that has `properties` when every member is a
// mapping holding nothing but `required`.
func dropPresenceRule(m *yaml.Node) {
	hasProps := false
	for i := 0; i+1 < len(m.Content); i += 2 {
		if m.Content[i].Value == "properties" {
			hasProps = true
		}
	}
	if !hasProps {
		return
	}
	for i := 0; i+1 < len(m.Content); i += 2 {
		k, v := m.Content[i].Value, m.Content[i+1]
		if (k != "anyOf" && k != "oneOf") || v.Kind != yaml.SequenceNode || len(v.Content) == 0 {
			continue
		}
		presenceOnly := true
		for _, member := range v.Content {
			if member.Kind != yaml.MappingNode || len(member.Content) != 2 || member.Content[0].Value != "required" {
				presenceOnly = false
				break
			}
		}
		if presenceOnly {
			m.Content = append(m.Content[:i], m.Content[i+2:]...)
			return
		}
	}
}

func isString(t *yaml.Node) bool {
	if t == nil {
		return false
	}
	if t.Kind == yaml.ScalarNode {
		return t.Value == "string"
	}
	if t.Kind == yaml.SequenceNode {
		for _, c := range t.Content {
			if c.Value == "string" {
				return true
			}
		}
	}
	return false
}
