#!/usr/bin/env bash
set -e

PYTHON=${PYTHON:-python3}
VENV=".venv"

$PYTHON -m venv "$VENV"
# shellcheck disable=SC1091
source "$VENV/bin/activate"

pip install --upgrade pip
pip install -r requirements.txt

echo "Environment ready. Activate with: source $VENV/bin/activate"
