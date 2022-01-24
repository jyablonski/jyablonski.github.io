.PHONY: build-venv
build-venv:
	pipenv install

# do this first before serve or build
.PHONY: venv
venv:
	pipenv shell

.PHONY: serve
serve: 
	python server.py

.PHONY: build
build: 
	python server.py build