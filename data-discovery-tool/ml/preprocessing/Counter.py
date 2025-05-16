import json
import os

file_path = "data/raw/54d7df8f-d016-72c1-1841-ff05652a4c9f-jsonl.jsonl"

total_word_count = 0
entry_count = 0
entries_with_text = 0

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        entry_count += 1
        try:
            data = json.loads(line)
            full_text = data.get("fullText")
            if isinstance(full_text, list):
                joined_text = " ".join(full_text)
                words = joined_text.split()
                word_count = len(words)
                total_word_count += word_count
                entries_with_text += 1
        except json.JSONDecodeError:
            print(f"Skipping malformed line at entry {entry_count}")

print("Total entries:", entry_count)
print("Entries with full text:", entries_with_text)
print("Total words in all fullText fields:", total_word_count)
