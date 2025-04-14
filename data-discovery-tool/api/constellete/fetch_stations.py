import requests
import json
import os

# You might need to change this to the real URL
API_BASE_URL = "https://api.constellete.org/v1"

def fetch_field_stations():
    url = f"{API_BASE_URL}/stations"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching stations: {e}")
        return []

def save_to_file(data, filename="stations_raw.json"):
    raw_path = os.path.join("data", "raw", filename)
    os.makedirs(os.path.dirname(raw_path), exist_ok=True)
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Saved {len(data)} stations to {raw_path}")

if __name__ == "__main__":
    stations = fetch_field_stations()
    if stations:
        save_to_file(stations)
