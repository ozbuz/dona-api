// Command openapi2json converts the Dona API contract (OpenAPI 3.1, YAML) into the minified JSON
// the server embeds (docs/openapi/seller-api.json): stdin YAML → stdout JSON, one line.
//
// Mapping order is KEPT — a map[string]any would sort every key and scramble the document a reader
// scrolls through — and a scalar is written as its source text unless its resolved YAML 1.2 tag is
// null, bool, int or float. It is its own module so gopkg.in/yaml.v3 stays out of the server's
// dependency graph; run it through scripts/openapi-sync.sh, never by hand.
package main

import (
	"bufio"
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"os"
	"strconv"

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
	if doc.Kind != yaml.DocumentNode || len(doc.Content) != 1 {
		fail(fmt.Errorf("openapi yaml: not one document"))
	}
	var buf bytes.Buffer
	if err := toJSON(&buf, doc.Content[0]); err != nil {
		fail(err)
	}
	if !json.Valid(buf.Bytes()) {
		fail(fmt.Errorf("openapi yaml: the conversion produced invalid JSON"))
	}
	buf.WriteByte('\n')
	w := bufio.NewWriter(os.Stdout)
	if _, err := w.Write(buf.Bytes()); err != nil {
		fail(err)
	}
	if err := w.Flush(); err != nil {
		fail(err)
	}
}

func fail(err error) {
	fmt.Fprintln(os.Stderr, "openapi2json:", err)
	os.Exit(1)
}

// toJSON writes n as JSON, keeping mapping order.
func toJSON(buf *bytes.Buffer, n *yaml.Node) error {
	switch n.Kind {
	case yaml.AliasNode:
		return toJSON(buf, n.Alias)
	case yaml.MappingNode:
		buf.WriteByte('{')
		for i := 0; i+1 < len(n.Content); i += 2 {
			if i > 0 {
				buf.WriteByte(',')
			}
			jsonString(buf, n.Content[i].Value)
			buf.WriteByte(':')
			if err := toJSON(buf, n.Content[i+1]); err != nil {
				return err
			}
		}
		buf.WriteByte('}')
	case yaml.SequenceNode:
		buf.WriteByte('[')
		for i, c := range n.Content {
			if i > 0 {
				buf.WriteByte(',')
			}
			if err := toJSON(buf, c); err != nil {
				return err
			}
		}
		buf.WriteByte(']')
	case yaml.ScalarNode:
		switch n.ShortTag() {
		case "!!null":
			buf.WriteString("null")
		case "!!bool":
			var b bool
			if err := n.Decode(&b); err != nil {
				return fmt.Errorf("openapi yaml line %d: %w", n.Line, err)
			}
			buf.WriteString(strconv.FormatBool(b))
		case "!!int":
			var i int64
			if err := n.Decode(&i); err != nil {
				return fmt.Errorf("openapi yaml line %d: %w", n.Line, err)
			}
			buf.WriteString(strconv.FormatInt(i, 10))
		case "!!float":
			var f float64
			if err := n.Decode(&f); err != nil {
				return fmt.Errorf("openapi yaml line %d: %w", n.Line, err)
			}
			num, err := json.Marshal(f)
			if err != nil { // ±Inf / NaN have no JSON form
				return fmt.Errorf("openapi yaml line %d: %w", n.Line, err)
			}
			buf.Write(num)
		default: // !!str, !!timestamp, !!binary — the source text, never a re-rendering
			jsonString(buf, n.Value)
		}
	default:
		return fmt.Errorf("openapi yaml line %d: unexpected node kind %d", n.Line, n.Kind)
	}
	return nil
}

func jsonString(buf *bytes.Buffer, s string) {
	enc := json.NewEncoder(buf)
	enc.SetEscapeHTML(false)
	_ = enc.Encode(s)
	buf.Truncate(buf.Len() - 1) // Encode appends a newline
}
