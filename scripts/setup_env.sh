#!/bin/bash
set -e

echo "Setting up FaceVoiceID environment dependencies..."

if command -v apt-get &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y build-essential cmake libopencv-dev portaudio19-dev python3-dev
elif command -v brew &> /dev/null; then
    brew install cmake portaudio opencv
fi

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Environment setup complete!"
