#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# Check for plugin dependencies
if [ -f "/app/plugins/plugin_requirements.txt" ]; then
    echo "=========================================================="
    echo "Found plugin requirements. Installing..."
    echo "=========================================================="
    pip install --no-cache-dir -r /app/plugins/plugin_requirements.txt
fi

# Hand over control to the main Python process
exec python main.py