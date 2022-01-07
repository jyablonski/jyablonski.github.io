.PHONY: build-venv
build-venv:
	pipenv install

.PHONY: venv
venv:
	pipenv shell

.PHONY: build
build: 
	python server.py