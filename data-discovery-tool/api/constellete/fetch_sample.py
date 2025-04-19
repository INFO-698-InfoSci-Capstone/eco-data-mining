import constellate
import pandas as pd
import os

# Your JSTOR ecology dataset ID
dataset_id = "eeb16cb4-a04a-5e68-3f20-8d5e677fd5ac"

# ✅ Step 1: Download the sampled dataset
downloaded_path = constellate.get_dataset(dataset_id)

# ✅ Step 2: Read the .jsonl.gz file properly using Constellate helper
documents = list(constellate.dataset_reader(downloaded_path))

# ✅ Step 3: Save as JSON
os.makedirs("data/raw", exist_ok=True)
output_path = f"data/raw/ecology_sample_{dataset_id[:6]}.json"
pd.DataFrame(documents).to_json(output_path, orient="records", indent=2)

print(f"✅ Saved {len(documents)} ecology records to {output_path}")
