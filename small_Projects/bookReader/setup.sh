#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "--- Starting Setup for Book Voice Reader (2025) ---"

# 1. Determine the correct Python command (prefer python3)
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "Error: Python is not installed. Please install Python 3.10+ to continue."
    exit 1
fi

echo "Using: $($PYTHON_CMD --version)"

# 2. Create virtual environment if it doesn't exist
VENV_DIR=".venv"
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in $VENV_DIR..."
    $PYTHON_CMD -m venv $VENV_DIR
else
    echo "Virtual environment already exists."
fi

# 3. Upgrade pip and install dependencies
echo "Installing dependencies from requirements.txt..."
# Use the python executable inside the venv directly to avoid activation issues in scripts
$VENV_DIR/bin/pip install --upgrade pip
$VENV_DIR/bin/pip install -r requirements.txt

# 4. Verify installation
echo "Checking installed packages..."
$VENV_DIR/bin/pip list | grep -E "pypdf|pyttsx3|PySide6"

echo "------------------------------------------------"
echo "Setup Complete!"
echo "To start the application, run:"
echo "  source $VENV_DIR/bin/activate && python -m src.main"
echo "------------------------------------------------"
