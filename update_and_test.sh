#!/bin/bash
set -e

echo "=== Pulling latest changes ==="
git pull origin main

echo "=== Upgrading pip and installing dependencies ==="
python -m pip install --upgrade pip
pip install fastapi httpx pytest

# If your project uses pyproject.toml for editable installation:
if [ -f "pyproject.toml" ]; then
    pip install -e .
    echo "Installed project in editable mode via pyproject.toml."
fi

echo "=== Running Tests ==="
pytest tests/test_api.py
