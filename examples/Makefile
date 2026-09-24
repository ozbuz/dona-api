# Dona API examples — every one is compiled/type-checked and its webhook verifier is run against the
# shared vectors (`make check`); `make smoke` then runs every quickstart against a local mock of the
# contract (tools/mockapi) and asserts what each one actually sent. Called from the repo Makefile.
SHELL := /usr/bin/env bash
.SHELLFLAGS := -euo pipefail -c
ROOT := $(abspath ..)
include $(ROOT)/generators/versions.env
# Containers run as the calling user: root-owned bin/ obj/ vendor/ would break the next checkout
# on a persistent self-hosted runner (git clean cannot delete them).
DOCKER_USER := --user "$$(id -u):$$(id -g)" -e HOME=/tmp -e COMPOSER_HOME=/tmp/composer \
  -e DOTNET_CLI_HOME=/tmp -e NUGET_PACKAGES=/tmp/nuget -e DOTNET_CLI_TELEMETRY_OPTOUT=1 -e DOTNET_NOLOGO=1 \
  -e GIT_CONFIG_COUNT=1 -e GIT_CONFIG_KEY_0=safe.directory -e GIT_CONFIG_VALUE_0='*'

.PHONY: check smoke deps $(addprefix check-,typescript python go php csharp)

check: check-typescript check-python check-go check-php check-csharp

deps:
	cd $(ROOT)/sdks/typescript && npm install --no-audit --no-fund --no-package-lock --silent && npx tsc -p tsconfig.json
	cd typescript && npm install --no-audit --no-fund --no-package-lock --silent
	rm -rf php/vendor php/composer.lock   # always resolve against the CURRENT sdks/php
	docker run --rm $(DOCKER_USER) -v "$(ROOT):/work" -w /work/examples/php $(COMPOSER_IMAGE) \
	  install --no-interaction --no-progress --quiet

check-typescript: deps
	cd typescript && npx tsc -p tsconfig.json && node src/webhook-selftest.ts

check-python:
	cd python && uvx ruff@$(RUFF_VERSION) check . && uvx ruff@$(RUFF_VERSION) format --check .
	cd python && uv run --isolated --no-project --python $(PYTHON_VERSION) --with ../../sdks/python --with mypy==$(MYPY_VERSION) \
	  mypy quickstart.py webhook.py webhook_selftest.py
	cd python && uv run --isolated --no-project --python $(PYTHON_VERSION) python webhook_selftest.py

check-go:
	cd go && test -z "$$(gofmt -l .)" && go vet ./... && go build ./... && go test -count=1 ./...

check-php: deps
	docker run --rm $(DOCKER_USER) -v "$(ROOT):/work" -w /work/examples/php --entrypoint sh $(COMPOSER_IMAGE) \
	  -ec 'for f in *.php; do php -l "$$f" >/dev/null; done; php webhook_selftest.php'

check-csharp:
	docker run --rm $(DOCKER_USER) -v "$(ROOT):/work" -w /work/examples/csharp $(DOTNET_IMAGE) sh -ec \
	  'dotnet build -c Release -o /tmp/ex -v quiet -nologo >/tmp/build.log 2>&1 || { cat /tmp/build.log; exit 1; }; \
	   dotnet /tmp/ex/DonaExamples.dll webhook-selftest'

smoke: deps
	ROOT="$(ROOT)" COMPOSER_IMAGE="$(COMPOSER_IMAGE)" DOTNET_IMAGE="$(DOTNET_IMAGE)" PYTHON_VERSION="$(PYTHON_VERSION)" ./smoke.sh
