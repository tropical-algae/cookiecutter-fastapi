SHELL := /bin/bash

# Target section and Global definitions
# -----------------------------------------------------------------------------
.PHONY: all clean test install run deploy down

all: clean test install run deploy down

install: generate_dot_env
	pip install --upgrade pip
	pip install poetry
	poetry update
	poetry install --with dev
	poetry shell

activate:
	poetry shell

deploy: generate_dot_env
	docker-compose build
	docker-compose up -d

down:
	docker-compose down

generate_dot_env:
	@if [[ ! -e .env ]]; then \
		cp .env.example .env; \
	fi

clean:
	@find ./src ./tests -name '*.pyc' -exec rm -rf {} \; || true
	@find ./src ./tests -name '__pycache__' -exec rm -rf {} \; || true
	@find ./src ./tests -name 'Thumbs.db' -exec rm -rf {} \; || true
	@find ./src ./tests -name '*~' -exec rm -rf {} \; || true
	@find ./src ./tests -name '*.egg' -exec rm -f {} \; || true
	@find ./src ./tests -name '*.egg-info' -exec rm -rf {} \; || true
	rm -rf build/;
	rm -rf dist/;
	rm -rf .eggs/;
	rm -rf *.egg-info;
	rm -f .coverage;
	rm -fr htmlcov/;
	rm -fr .pytest_cache;
	rm -f report.xml;
	rm -f cov.xml;
	rm -rf .mypy_cache;
	rm -rf .ruff_cache;
	rm -rf .cache;
