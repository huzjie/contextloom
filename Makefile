PYTHON ?= python
PIP ?= pip
PYTEST ?= pytest

.PHONY: help install install-dev test lint format typecheck run build-docker clean

help:
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'

install:
	$(PIP) install -r requirements.txt

install-dev:
	$(PIP) install -r requirements-dev.txt
	$(PIP) install -e .

test:
	$(PYTEST) tests/ -v

lint:
	ruff check src tests

format:
	black src tests

typecheck:
	mypy src

run:
	contextloom serve --reload

build-docker:
	docker build -t contextloom:latest .

clean:
	rm -rf build dist *.egg-info .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
