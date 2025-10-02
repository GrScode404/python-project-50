install:
	uv sync

gendiff:
	uv run gendiff

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check gendiff

fixlint:
	uv run ruff check gendiff --fix

.PHONY: gendiff install lint fixlint