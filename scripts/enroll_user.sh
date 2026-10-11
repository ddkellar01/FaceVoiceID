#!/bin/bash
set -e

if [ -z "$1" ]; then
    echo "Usage: ./scripts/enroll_user.sh <username>"
    exit 1
fi

USERNAME=$1
echo "Starting enrollment workflow for user: $USERNAME"
python main.py register "$USERNAME"
