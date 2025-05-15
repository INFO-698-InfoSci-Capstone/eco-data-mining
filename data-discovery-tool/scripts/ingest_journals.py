import os
import sys
import json
from datetime import datetime
from pathlib import Path
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# ===== Add project root to sys.path =====
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.models import Journal  # Adjust if model is in a different module

# ===== Setup DB connection =====
db_path = Path("data/eco.db").resolve()
engine = create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=engine)
session = Session()

print("🔄 Ingesting journal records with n-gram metadata...")

# ===== Read JSONL File =====
jsonl_path = Path("data/raw/54d7df8f-d016-72c1-1841-ff05652a4c9f-jsonl.jsonl").resolve()
with open(jsonl_path, "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, start=1):
        try:
            j = json.loads(line)

            # === Parse publication date ===
            date_obj = None
            if j.get("datePublished"):
                try:
                    date_obj = datetime.strptime(j["datePublished"], "%Y-%m-%d")
                except ValueError:
                    pass

            # === Flatten full text and derive location ===
            full_text_list = j.get("fullText", [])
            full_text_combined = " ".join(full_text_list)

            # === Set location from field station (if available)
            location = None
            field_station_id = j.get("field_station_id")  # Assumes you extract/store this if available
            station = None

            if field_station_id:
                # Optional: validate against DB to ensure field station exists
                from db.models import FieldStation
                station = session.query(FieldStation).filter_by(id=field_station_id).first()
                if station:
                    location = station.name or station.location

            # === Construct metadata block with n-grams ===
            meta_dict = {
                "unigramCount": j.get("unigramCount", {}),
                "bigramCount": j.get("bigramCount", {}),
                "trigramCount": j.get("trigramCount", {}),
                "identifier": j.get("identifier", []),
                "outputFormat": j.get("outputFormat", []),
                "sourceCategory": j.get("sourceCategory", []),
                "tdmCategory": j.get("tdmCategory", []),
            }

            # === Create and add Journal object ===
            journal = Journal(
                title=j.get("title"),
                location=location,
                date_published=date_obj,
                creator=j.get("creator", []),
                keyphrases=j.get("keyphrase", []),
                meta_json=meta_dict,
                full_text=full_text_combined,
                field_station_id=field_station_id
            )
            existing = session.query(Journal).filter_by(title=j.get("title")).first()
            if not existing:
                session.add(journal)

        except Exception as e:
            print(f"⚠️ Skipping line {line_num} due to error: {e}")

# ===== Commit the session =====
session.commit()
session.close()

print(f"✅ Ingestion complete. Source: {jsonl_path.name}")
