all: install

configure:
	@poetry install

test:
	@poetry run pytest

lint:
	@poetry run flake8

build: lint test
	@poetry build

install: build
	@pip install --user dist/hexlet_python_package*.whl

.PHONY: all configure test lint build install
