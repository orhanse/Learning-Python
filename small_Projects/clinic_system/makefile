VENV=venv
PYTHON=$(VENV)/bin/python3

.PHONY: setup run test clean

setup:
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

run:
	. $(VENV)/bin/activate && python3 main.py

test:
	. $(VENV)/bin/activate && pytest -v

clean:
	rm -rf $(VENV)
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
