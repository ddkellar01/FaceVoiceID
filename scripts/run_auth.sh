#!/bin/bash
set -e

if [ -z "$1" ]; then
    echo "Usage: ./scripts/run_auth.sh <username>"
    exit 1
fi

USERNAME=$1
echo "Starting authentication workflow for user: $USERNAME"
python main.py auth "$USERNAME"
