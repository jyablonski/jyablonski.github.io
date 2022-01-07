.PHONY: build-venv
build-venv:
	pipenv install

.PHONY: venv
venv:
	pipenv shell

.PHONY: serve
serve: 
	python server.py

.PHONY: build
build: 
	python server.py build