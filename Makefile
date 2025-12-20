.PHONY: install
install:
	uv sync --group dev

.PHONY: up
up:
	uv run python server.py

.PHONY: build
build:
	uv run python server.py build

.PHONY: test
test:
	uv run pytest

.PHONY: lint
lint:
	uv run ruff check .

.PHONY: lint-fix
lint-fix:
	uv run ruff check . --fix

.PHONY: bump-patch
bump-patch:
	@bump2version patch
	@git push --tags
	@git push

.PHONY: bump-minor
bump-minor:
	@bump2version minor
	@git push --tags
	@git push

.PHONY: bump-major
bump-major:
	@bump2version major
	@git push --tags
	@git push
