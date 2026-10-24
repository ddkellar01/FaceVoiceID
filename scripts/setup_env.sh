#!/bin/bash
set -e

# Automatically navigate to the repository root directory (one level up from scripts/)
cd "$(dirname "$0")/.."

echo "Setting up FaceVoiceID environment dependencies..."

if command -v apt-get &> /dev/null; then
  sudo apt-get update
  sudo apt-get install -y build-essential cmake \
    libopencv-dev portaudio19-dev python3-dev
elif command -v brew &> /dev/null; then
  brew install cmake portaudio opencv
fi

echo "Installing Python dependencies..."
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
pip install --no-cache-dir git+https://github.com/ageitgey/face_recognition_models.git
pip install -e .

echo "Environment setup complete!"
