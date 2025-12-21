PYTHON ?= python3
VENV ?= .venv

.PHONY: venv install run test lint format clean

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt

run:
	$(VENV)/bin/python -m src.main

test:
	$(VENV)/bin/python -m pytest -q

lint:
	$(VENV)/bin/ruff check src tests

format:
	$(VENV)/bin/ruff format src tests || $(VENV)/bin/black src tests

clean:
	rm -rf $(VENV) .pytest_cache dist build *.egg-info
