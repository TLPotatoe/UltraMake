#!/bin/bash

# Get the absolute path to the main.py script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
VENV_DIR="$SCRIPT_DIR/.venv"
INSTALLER_PY_PATH="$SCRIPT_DIR/install.py"
MAIN_PY_PATH="$SCRIPT_DIR/main.py"
REQUIREMENTS_PATH="$SCRIPT_DIR/requirements.txt"

git stash
git pull origin master

# Check if python3 is available
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found, please install it."
    exit 1
fi

python3 "$INSTALLER_PY_PATH"