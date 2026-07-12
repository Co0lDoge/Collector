#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# Check for custom provider dependencies
if [ -f "/app/providers/requirements.txt" ]; then
    echo "=========================================================="
    echo "Found custom provider requirements. Installing..."
    echo "=========================================================="
    pip install --no-cache-dir -r /app/providers/requirements.txt
fi

# Check for custom storage dependencies
if [ -f "/app/storages/requirements.txt" ]; then
    echo "=========================================================="
    echo "Found custom storage requirements. Installing..."
    echo "=========================================================="
    pip install --no-cache-dir -r /app/storages/requirements.txt
fi

# Hand over control to the main Python process
exec python main.py