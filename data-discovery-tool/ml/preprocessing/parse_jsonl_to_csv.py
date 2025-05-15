import gzip
import json
import csv
from pathlib import Path
import sys
import os
from tqdm import tqdm

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from config import DATA_RAW_DIR, DATA_PROCESSED_DIR

# File setup
file_name = "ecology_full_50k.jsonl.gz"
file_path = DATA_RAW_DIR / file_name
output_path = DATA_PROCESSED_DIR / "ecology_dataset_50k.csv"

print(f"🔍 Final resolved file path: {file_path}")
print(f"🧪 File exists? {file_path.exists()}")

if not file_path.exists():
    raise FileNotFoundError(f"🚫 File not found at: {file_path}")

# --------------------------------------
# Pass 1: Collect all unique fieldnames
# --------------------------------------
print("🔍 Pass 1: Scanning for fieldnames...")
fieldnames = set()

with gzip.open(file_path, 'rt', encoding='utf-8') as f:
    for line in tqdm(f, desc="🔍 Scanning Fields"):
        try:
            record = json.loads(line)
            fieldnames.update(record.keys())
        except Exception as e:
            print(f"⚠️ Skipping line due to JSON decode error: {e}")

fieldnames = sorted(fieldnames)
print(f"📑 Total unique fields found: {len(fieldnames)}")

# --------------------------------------
# Pass 2: Write data to CSV
# --------------------------------------
print("✍️ Pass 2: Writing CSV...")
with gzip.open(file_path, 'rt', encoding='utf-8') as f, \
     open(output_path, 'w', newline='', encoding='utf-8') as csvfile:

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for line in tqdm(f, desc="📝 Writing Records"):
        try:
            row = json.loads(line)
            writer.writerow(row)
        except Exception as e:
            print(f"⚠️ Skipping row due to error: {e}")

print(f"✅ CSV successfully saved to: {output_path}")
