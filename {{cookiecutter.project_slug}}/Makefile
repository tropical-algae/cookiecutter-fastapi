SHELL := /bin/bash

# Target section and Global definitions
# -----------------------------------------------------------------------------
.PHONY: all clean test install run deploy down

all: clean test install run deploy down

install: generate_dot_env
	pip install --upgrade pip
	pip install poetry
	poetry config virtualenvs.in-project true
	poetry env use python3
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
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '__pycache__' -exec rm -rf {} \;
	@find . -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;
	@find . -name '*.egg' -exec rm -f {} \;
	@find . -name '*.egg-info' -exec rm -rf {} \;
	rm -rf build/;
	rm -rf dist/;
	rm -rf .eggs/;
	rm -rf *.egg-info;
	rm -f .coverage;
	rm -fr htmlcov/;
	rm -fr .pytest_cache;
	rm -f report.xml;
	rm -f cov.xml;
	rm -fr .mypy_cache;
	rm -fr .ruff_cache;
	rm -rf .cache;
