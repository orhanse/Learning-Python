# Variables
PYTHON = python3
VENV = .venv
BIN = $(VENV)/bin

# Check for Windows - use different pathing if on Windows
ifeq ($(OS), Windows_NT)
	PYTHON = python
	BIN = $(VENV)/Scripts
endif

.PHONY: setup run test clean help

help:
	@echo "Available commands:"
	@echo "  make setup  - Create virtual environment and install dependencies"
	@echo "  make run    - Run the application"
	@echo "  make test   - Run unit tests"
	@echo "  make clean  - Remove temporary files and virtual environment"

setup:
	$(PYTHON) -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -r requirements.txt
	@echo "Setup complete. Virtual environment created in $(VENV)."

run:
	$(BIN)/python -m src.main

test:
	$(BIN)/python -m unittest discover tests

clean:
	@echo "Cleaning up..."
	@# Remove python cache
	rm -rf `find . -type d -name "__pycache__"`
	@# Remove virtual environment
	rm -rf $(VENV)
	@# Remove build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	@echo "Clean complete."

# Utility to create requirements if they don't exist
requirements.txt:
	@echo "pypdf==5.1.0" > requirements.txt
	@echo "pyttsx3==2.98" >> requirements.txt
	@echo "PySide6==6.8.1" >> requirements.txt
