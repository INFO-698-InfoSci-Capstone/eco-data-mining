import json

matches = []

with open("data/raw/54d7df8f-d016-72c1-1841-ff05652a4c9f-jsonl.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        record = json.loads(line)
        # Search all string fields
        for key, value in record.items():
            if isinstance(value, str) and "field station" in value.lower():
                matches.append({
                    "title": record.get("title"),
                    "match_in": key,
                    "value": value[:300]  # Show first 300 chars
                })
                break  # Stop after first match per record

print(f"✅ Found {len(matches)} potential mentions in metadata.\n")

for m in matches[:5]:
    print(f"📘 Title: {m['title']}")
    print(f"🔎 Match in: {m['match_in']}")
    print(f"📄 Snippet: {m['value']}\n")
    print("=" * 80)
