import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VENV_DIR = os.path.join(SCRIPT_DIR, ".venv")
PY_DIR = os.path.join(VENV_DIR, "Scripts" if os.name == "nt" else "bin")
PYTHON = os.path.join(PY_DIR, "python")
REQ_PATH = os.path.join(SCRIPT_DIR, "requirements.txt")
HOME = os.path.expanduser("~")
TERM_CONFIG = [
	".bashrc",
	".zshrc"
]

ALIAS = "alias umake"
COMMAND = f"{ALIAS}=\"{PYTHON} {os.path.join(SCRIPT_DIR, 'main.py')}\"\n"

def apply_alias(path: str) -> None:
	path = os.path.join(HOME, path)
	if not os.path.exists(path):
		return
	with open (path, "r+") as f:
		content = f.readlines()
		presence = [line for line in content if ALIAS in line]
		if len(presence):
			content[content.index(presence[0])] = COMMAND
		else:
			content.append(COMMAND)
		f.seek(0)
		f.writelines(content)

print(f"Creating venv at {VENV_DIR}")
os.system(f"python3 -m venv {VENV_DIR} --upgrade")
if (not os.path.exists(PYTHON)):
	exit(1)
print("Done.")

print("Installing requirements...")
os.system(f"{PYTHON} -m pip install -r {REQ_PATH}")
print("Done.")

print("Applying alias...")
for path in TERM_CONFIG:
	apply_alias(path)
print("Done.")
