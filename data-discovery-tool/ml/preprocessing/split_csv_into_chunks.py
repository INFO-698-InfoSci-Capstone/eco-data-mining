import pandas as pd
from pathlib import Path
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from config import DATA_PROCESSED_DIR

# Input CSV
input_path = DATA_PROCESSED_DIR / "ecology_dataset_50k.csv"

# Output directory
output_dir = DATA_PROCESSED_DIR / "splits"
output_dir.mkdir(parents=True, exist_ok=True)

# Chunk size
chunk_size = 1000
chunk_number = 1

print(f"📂 Splitting: {input_path}")
print(f"📤 Output to: {output_dir}")

# Stream the CSV file in chunks
for chunk in pd.read_csv(input_path, chunksize=chunk_size):
    output_file = output_dir / f"ecology_dataset_chunk_{chunk_number}.csv"
    chunk.to_csv(output_file, index=False)
    print(f"✅ Chunk {chunk_number} saved: {output_file.name}")
    chunk_number += 1

print("🎉 All chunks saved successfully!")
