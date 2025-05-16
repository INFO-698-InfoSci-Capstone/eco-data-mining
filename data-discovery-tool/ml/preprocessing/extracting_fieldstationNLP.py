import sqlite3
import spacy
import uuid
from datetime import datetime

# Setup spaCy
nlp = spacy.load("en_core_web_sm")

# Connect to DB
db_path = r"C:\Users\VikRuhil\Desktop\MS DS\Capstone\Eco Data Mining\eco-data-mining\data-discovery-tool\data\eco.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Fetch all journals
cursor.execute("SELECT id, full_text FROM journals WHERE full_text IS NOT NULL")
journals = cursor.fetchall()

linked_count = 0

for journal_id, full_text in journals:
    doc = nlp(full_text)
    locations = [ent.text for ent in doc.ents if ent.label_ in ["GPE", "FAC"]]

    if not locations:
        continue  # Skip if no locations found

    # For now, take the **first** detected location
    candidate_location = locations[0]

    # Check if FieldStation already exists
    cursor.execute("SELECT id FROM field_stations WHERE name = ?", (candidate_location,))
    row = cursor.fetchone()

    if row:
        station_id = row[0]
    else:
        # Create a new FieldStation
        station_id = str(uuid.uuid4())
        cursor.execute("""
            INSERT INTO field_stations (id, name, location, created_at)
            VALUES (?, ?, ?, ?)
        """, (station_id, candidate_location, candidate_location, datetime.utcnow()))
        print(f"Created new FieldStation: {candidate_location}")

    # Update journal with field_station_id
    cursor.execute("""
        UPDATE journals SET field_station_id = ? WHERE id = ?
    """, (station_id, journal_id))
    linked_count += 1
    print(f"Linked Journal {journal_id} to FieldStation {candidate_location}")

# Commit changes
conn.commit()
conn.close()

print(f"\nCompleted linking. Total journals linked: {linked_count}")
