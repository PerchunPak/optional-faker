SHELL:=/usr/bin/env bash

.PHONY: style
style:
	poetry run black .
	poetry run isort .
	poetry run pycln .
	poetry run mypy --install-types --non-interactive .
	poetry run flake8 .

.PHONY: unit
unit:
ifeq ($(ci),1)
	poetry run pytest --no-testmon
else
	poetry run pytest --no-cov
endif

.PHONY: package
package:
	poetry check
	poetry run pip check
	poetry run safety check --full-report

.PHONY: test
test: style package unit
