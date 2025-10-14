install:
	uv sync

gendiff:
	uv run gendiff gendiff/tests/test_data/file1.json gendiff/tests/test_data/file2.json

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check gendiff

fixlint:
	uv run ruff check gendiff --fix

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml

.PHONY: gendiff install lint fixlint test-coverage