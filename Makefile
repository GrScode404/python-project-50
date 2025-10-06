install:
	uv sync

gendiff:
	uv run gendiff data/file1.json data/file2.json

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check gendiff

fixlint:
	uv run ruff check gendiff --fix

.PHONY: gendiff install lint fixlint