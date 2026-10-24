#!/bin/bash
set -e

echo "Pulling latest changes ---"
git pull origin main

echo "Upgrading pip and installing dependencies ---"
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
pip install --no-cache-dir git+https://github.com/ageitgey/face_recognition_models.git

# Fixed editable installation (added missing dot)
if [ -f "pyproject.toml" ]; then
  pip install -e .
  echo "Installed project in editable mode via pyproject.toml"
fi

echo "Running Tests ---"
pytest
