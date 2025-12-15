#!/bin/bash

# Get the absolute path to the main.py script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
VENV_DIR="$SCRIPT_DIR/.venv"
MAIN_PY_PATH="$SCRIPT_DIR/main.py"
REQUIREMENTS_PATH="$SCRIPT_DIR/requirements.txt"

# --- Create Virtual Environment and Install Dependencies ---

# Check if python3 is available
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found, please install it."
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment in $VENV_DIR..."
python3 -m venv "$VENV_DIR" --upgrade || {
    echo "Error: Failed to create virtual environment."
    echo "On Debian/Ubuntu systems, you may need to run: sudo apt install python3-venv"
    exit 1
}

# Check if venv was created
if [ ! -f "$VENV_DIR/bin/python" ]; then
    echo "Error: Virtual environment created but python binary not found."
    exit 1
fi

# Install dependencies
echo "Installing dependencies from $REQUIREMENTS_PATH..."
"$VENV_DIR/bin/python" -m pip install -r "$REQUIREMENTS_PATH"

# --- Alias Configuration ---

ALIAS_CMD="alias umake=\"$VENV_DIR/bin/python $MAIN_PY_PATH\""
ALIAS_NAME="umake"

# List of shell configuration files to check
SHELL_CONFIG_FILES=(
    "$HOME/.bashrc"
    "$HOME/.zshrc"
    "$HOME/.profile"
    "$HOME/.bash_profile"
    "$HOME/.config/fish/config.fish"
)

# --- Functions ---

# Function to check if an alias already exists
alias_exists() {
    local config_file="$1"
    local alias_name="$2"
    # For fish shell, the syntax is different
    if [[ "$config_file" == *"/fish/config.fish" ]]; then
        # Check for "alias umake 'command'"
        grep -qE "^\s*alias\s+$alias_name\s" "$config_file"
    else
        # For bash/zsh/sh, check for "alias umake="
        grep -qE "^\s*alias\s+$alias_name=" "$config_file"
    fi
}

# Function to add the alias to a file
add_alias() {
    local config_file="$1"
    local alias_command="$2"
    local alias_name="$3"
    
    echo "Adding alias to $config_file..."
    # For fish shell, the syntax is: alias <name> '<command>'
    if [[ "$config_file" == *"/fish/config.fish" ]]; then
        local fish_alias="alias $alias_name '$VENV_DIR/bin/python $MAIN_PY_PATH'"
        echo -e "\n# Alias for UltraMake\n$fish_alias" >> "$config_file"
    else
        # Standard bash/zsh/sh syntax
        echo -e "\n# Alias for UltraMake\n$alias_command" >> "$config_file"
    fi
    echo "Alias added. Please run 'source $config_file' or restart your shell."
}

# --- Main Script ---

# Flag to track if we've found any shell config
found_config=false

# Iterate over the list of shell configuration files
for config_file in "${SHELL_CONFIG_FILES[@]}"; do
    if [ -f "$config_file" ]; then
        found_config=true
        if ! alias_exists "$config_file" "$ALIAS_NAME"; then
            add_alias "$config_file" "$ALIAS_CMD" "$ALIAS_NAME"
        else
            echo "Alias '$ALIAS_NAME' already exists in $config_file. Skipping."
        fi
    fi
done

# If no config file was found, print a message
if ! $found_config; then
    echo "Could not find a shell configuration file."
    echo "Please add the following line to your shell's startup file:"
    echo "$ALIAS_CMD"
fi
