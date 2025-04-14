import requests
import json
import os

API_BASE_URL = "https://api.constellete.org/v1"

def fetch_journals():
    url = f"{API_BASE_URL}/journals"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching journals: {e}")
        return []

def save_to_file(data, filename="journals_raw.json"):
    raw_path = os.path.join("data", "raw", filename)
    os.makedirs(os.path.dirname(raw_path), exist_ok=True)
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Saved {len(data)} journals to {raw_path}")

if __name__ == "__main__":
    journals = fetch_journals()
    if journals:
        save_to_file(journals)
