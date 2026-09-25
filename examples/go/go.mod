module github.com/ozbuz/dona-api/examples/go

go 1.26.4

require github.com/ozbuz/dona-api/sdks/go v0.0.0

require (
	github.com/apapsch/go-jsonmerge/v2 v2.0.0 // indirect
	github.com/google/uuid v1.6.0 // indirect
	github.com/oapi-codegen/runtime v1.7.0 // indirect
)

// The examples build against the SDK in this repository. In your own module, drop this line and
// `go get github.com/ozbuz/dona-api/sdks/go@<version>` (see README › Install).
replace github.com/ozbuz/dona-api/sdks/go => ../../sdks/go
