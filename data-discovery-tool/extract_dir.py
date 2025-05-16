import os

EXCLUDE_DIRS = {'.git', '__pycache__', 'venv', '.venv', '.mypy_cache', '.idea', '.vscode', 'env', 'build'}
EXCLUDE_FILES = {'.DS_Store', 'Thumbs.db'}
ROOT_DIR = os.path.abspath(".")

def print_tree(current_dir, prefix=""):
    entries = sorted(os.listdir(current_dir))
    entries = [e for e in entries if e not in EXCLUDE_FILES]
    entries = [e for e in entries if not e.startswith('.')]

    for i, entry in enumerate(entries):
        full_path = os.path.join(current_dir, entry)
        connector = "└── " if i == len(entries) - 1 else "├── "
        print(prefix + connector + entry)
        if os.path.isdir(full_path) and entry not in EXCLUDE_DIRS:
            extension = "    " if i == len(entries) - 1 else "│   "
            print_tree(full_path, prefix + extension)

print("data-discovery-tool/")
print_tree(ROOT_DIR)
