SHELL:=/usr/bin/env bash

.PHONY: format
style:
	black .
	isort .
	pycln .

.PHONY: lint
lint:
	mypy .
	flake8 .

.PHONY: style
style: format lint

.PHONY: unit
unit:
ifeq ($(ci),1)
	pytest --no-testmon
else
	pytest --no-cov
endif

.PHONY: package
package:
	poetry check
	pip check
	safety check --full-report

.PHONY: test
test: style package unit
