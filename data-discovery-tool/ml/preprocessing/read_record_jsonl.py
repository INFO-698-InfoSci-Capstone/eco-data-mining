import json
import gzip
from pathlib import Path

# ====== Paths ======
input_path = Path("data/raw/54d7df8f-d016-72c1-1841-ff05652a4c9f-jsonl.jsonl")  # Use .jsonl or .jsonl.gz
output_path = Path("data/processed/first_10_records.json")

# ====== Choose open method based on gzip ======
open_func = gzip.open if input_path.suffix == ".gz" else open

# ====== Read first 10 valid records ======
records = []
with open_func(input_path, "rt", encoding="utf-8") as f:
    for line in f:
        if len(records) >= 10:
            break
        try:
            record = json.loads(line)
            records.append(record)
        except json.JSONDecodeError as e:
            print(f"Skipping invalid line: {e}")
            continue

# ====== Write to JSON file ======
output_path.parent.mkdir(parents=True, exist_ok=True)
with open(output_path, "w", encoding="utf-8") as out:
    json.dump(records, out, indent=2)

print(f"First 10 records saved to: {output_path}")
