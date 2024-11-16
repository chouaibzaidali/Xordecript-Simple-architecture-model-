#!/bin/bash

# Check if virtual environment is activated
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "Please activate your virtual environment before running this script."
    exit 1
fi

# Install dependencies from requirements.txt
pip install -r requirements.txt

echo "All dependencies have been installed successfully!"