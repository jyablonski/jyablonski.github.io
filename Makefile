.PHONY: build-venv
build-venv:
	poetry install

# do this first before serve or build
.PHONY: venv
venv:
	poetry shell

.PHONY: up
up:
	@python server.py

.PHONY: build
build: 
	python server.py build

.PHONY: bump-patch
bump-patch:
	@bump2version patch
	@python server.py build
	@git add .
	@git commit -m "updating package"
	@git push --tags
	@git push

.PHONY: bump-minor
bump-minor:
	@bump2version minor
	@python server.py build
	@git add .
	@git commit -m "updating package"
	@git push --tags
	@git push

.PHONY: bump-major
bump-major:
	@bump2version major
	@python server.py build
	@git add .
	@git commit -m "updating package"
	@git push --tags
	@git push