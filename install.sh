#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
VENV_DIR="$SCRIPT_DIR/.venv"
INSTALLER_PY_PATH="$SCRIPT_DIR/install.py"
MAIN_PY_PATH="$SCRIPT_DIR/main.py"
REQUIREMENTS_PATH="$SCRIPT_DIR/requirements.txt"

git stash
git pull origin master

if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found, please install it."
    exit 1
fi

python3 "$INSTALLER_PY_PATH"