import os
from cursor_utils import *

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VENV_DIR = os.path.join(SCRIPT_DIR, ".venv")
PY_DIR = os.path.join(VENV_DIR, "Scripts" if os.name == "nt" else "bin")
PYTHON = os.path.join(PY_DIR, "python")
REQ_PATH = os.path.join(SCRIPT_DIR, "requirements.txt")
HOME = os.path.expanduser("~")
TERM_CONFIG = [".bashrc", ".zshrc"]

ALIAS = "alias umake"
COMMAND = f"{ALIAS}=\"'{PYTHON}' '{os.path.join(SCRIPT_DIR, 'main.py')}'\""

# for k, v in list(globals().items()):
#     print(k , v)


def apply_alias(path: str) -> bool:
	path = os.path.join(HOME, path)
	if not os.path.exists(path):
		return False

	with open(path, "r") as f:
		lines = f.readlines()

	alias_line_index = -1
	for i, line in enumerate(lines):
		if ALIAS in line:
			alias_line_index = i
			break

	new_command = COMMAND + '\n'

	if alias_line_index != -1:
		lines[alias_line_index] = new_command
	else:
		if lines and not lines[-1].endswith('\n'):
			lines[-1] += '\n'
		lines.append(new_command)

	with open(path, "w") as f:
		f.writelines(lines)

	return True


print(f'\nCreating venv at "{VENV_DIR}"')
os.system(f'python3 -m venv "{VENV_DIR}" --upgrade')
if not os.path.exists(PYTHON):
	exit(1)
print("Done.")

print(f"\nInstalling requirements...{FG_BLACK}")
os.system(f'"{PYTHON}" -m pip install -r "{REQ_PATH}"')
print(f"{FG_DEFAULT}Done.")

print("\nApplying alias...")
alias_added = 0
for path in TERM_CONFIG:
	if apply_alias(path):
		alias_added += 1
if not alias_added:
	print("No alias applied.")
	print("add this alias to your shell config file:")
	print(f"{ALIAS}=\"{PYTHON} {os.path.join(SCRIPT_DIR, 'main.py')}\"")
	exit(1)
print(f"Alias applied in {alias_added} files.")
print("\nInstallation done. Reload your terminal.")
