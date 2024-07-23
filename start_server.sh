#!/bin/bash

if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "No virtual environment detected. Attempting to activate virtual environment..."
    # Activate virtual environment if it exists
    if [ -d "env" ]; then
        source ./env/bin/activate
        echo "Virtual environment activated."
    else
        echo "No virtual environment found. Please set up a virtual environment."
        exit 1
    fi
else
    echo "Virtual environment already active."
fi

# Start the FastAPI application
echo "Starting FastAPI application..."
fastapi dev app/main.py