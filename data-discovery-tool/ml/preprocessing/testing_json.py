import json

with open("data/raw/54d7df8f-d016-72c1-1841-ff05652a4c9f-jsonl.jsonl", "r", encoding="utf-8") as f:
    for i in range(5):  # Load 5 lines for testing
        line = json.loads(f.readline())
        title = line.get("title", "No title")
        word_count = line.get("wordCount", "N/A")
        full_text = line.get("fullText")

        print(f"Title: {title}")
        print(f"Word Count: {word_count}")

        if full_text:
            print(f"Excerpt: {full_text[:300]}...\n")
        else:
            print("❌ No full text available.\n")

        print("=" * 80)
