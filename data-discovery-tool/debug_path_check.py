# debug_path_check.py
from pathlib import Path

path = Path("data/raw/ecology_full_50k.jsonl.gz").resolve()
print("Resolved Path:", path)
print("Exists?", path.exists())

import os
print("\nOS listdir for data/raw:")
print(os.listdir("data/raw"))
