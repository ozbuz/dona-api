# Dona API SDKs — everything under sdks/ is produced by `make generate` from spec/openapi.yaml.
# CI runs `make generate verify-clean check` : a hand edit to sdks/ fails verify-clean.
SHELL := /usr/bin/env bash
.SHELLFLAGS := -euo pipefail -c
include generators/versions.env

# SDK version = the contract major + this repo's release counter. Publishing is S6 (see README › Publishing).
SDK_VERSION ?= 0.1.0
BUILD       := build
VIEW        := $(BUILD)/openapi.client.yaml
LANGS       := typescript python go php csharp

.PHONY: all spec-check view generate $(addprefix gen-,$(LANGS)) verify-clean check smoke \
        $(addprefix check-,$(LANGS)) examples-check clean

all: spec-check generate check

spec-check:            ## spec/ = the synced contract = what ozb-backend serves
	scripts/check-spec.sh

view: $(VIEW)
$(VIEW): spec/openapi.yaml tools/clientview/main.go
	@mkdir -p $(BUILD)
	cd tools && go run ./clientview < ../spec/openapi.yaml > ../$(VIEW)

generate: $(addprefix gen-,$(LANGS))

$(addprefix gen-,$(LANGS)): gen-%: $(VIEW)
	generators/$*/generate.sh $(VIEW) sdks/$* $(SDK_VERSION)

# ⛔ The committed sdks/ must equal a fresh generation — tracked changes AND stray untracked files.
verify-clean:
	@if [[ -n "$$(git status --porcelain -- sdks)" ]]; then \
	  git status --porcelain -- sdks | head -40; \
	  git --no-pager diff --stat -- sdks | tail -5; \
	  echo "verify-clean: sdks/ differs from a fresh \`make generate\` — generated code was edited by hand," \
	       "or spec/generators changed without regenerating. Run \`make generate\` and commit sdks/." >&2; \
	  exit 1; \
	fi
	@echo "verify-clean: sdks/ is exactly the generator output"

check: $(addprefix check-,$(LANGS)) examples-check

smoke:                 ## every quickstart against a local mock of the contract (needs docker)
	$(MAKE) -C examples smoke

check-typescript:
	cd sdks/typescript && npm install --no-audit --no-fund --no-package-lock --silent && npx tsc -p tsconfig.json --noEmit

check-python:
	uv run --isolated --no-project --python $(PYTHON_VERSION) python -m compileall -q sdks/python/dona_api
	uv run --isolated --python $(PYTHON_VERSION) --with ./sdks/python python -c \
	  "import dona_api; from dona_api import AuthenticatedClient; from dona_api.api.account import get_me; \
	   from dona_api.api.stock_prices import set_stock; from dona_api.models import HeldForReview; print('python: import ok')"

check-go:
	cd sdks/go && go build ./... && go vet ./...

# Containers run as the calling user: a root-owned bin/ obj/ would break the next checkout on a
# persistent self-hosted runner (git clean cannot delete it).
DOCKER_USER := --user "$$(id -u):$$(id -g)" -e HOME=/tmp -e DOTNET_CLI_HOME=/tmp -e NUGET_PACKAGES=/tmp/nuget \
  -e DOTNET_CLI_TELEMETRY_OPTOUT=1 -e DOTNET_NOLOGO=1

check-php:
	docker run --rm $(DOCKER_USER) -v "$(CURDIR)/sdks/php:/app" -w /app $(PHP_IMAGE) sh -ec \
	  'find lib -name "*.php" -print0 | xargs -0 -n1 -P8 php -l >/dev/null && echo "php: lint ok ($$(find lib -name "*.php" | wc -l) files)"'

check-csharp:
	docker run --rm $(DOCKER_USER) -v "$(CURDIR):/work" -w /work/sdks/csharp $(DOTNET_IMAGE) \
	  sh -ec 'dotnet build src/Dona.Api/Dona.Api.csproj -c Release -o /tmp/dona-build -v quiet -nologo >/tmp/build.log 2>&1 \
	    || { cat /tmp/build.log; exit 1; }; grep -E "Warning\(s\)|Error\(s\)" /tmp/build.log; echo "csharp: build ok"'

examples-check:
	$(MAKE) -C examples check

clean:
	rm -rf $(BUILD) sdks/typescript/node_modules sdks/typescript/dist examples/typescript/node_modules \
	  examples/php/vendor examples/php/composer.lock
