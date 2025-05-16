import pandas as pd
from pathlib import Path
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from config import DATA_PROCESSED_DIR

# Path to splits folder
splits_dir = DATA_PROCESSED_DIR / "splits"

# Number of rows to preview from each chunk
preview_rows = 3

# List all CSVs in the splits directory
chunk_files = sorted(splits_dir.glob("*.csv"))

if not chunk_files:
    print("No chunk files found in splits directory.")
else:
    for chunk_file in chunk_files:
        print(f"\n Previewing: {chunk_file.name}")
        df = pd.read_csv(chunk_file, nrows=preview_rows)
        print(df.head(preview_rows))
