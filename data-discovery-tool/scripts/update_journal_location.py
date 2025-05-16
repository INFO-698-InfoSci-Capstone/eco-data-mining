import os
import sys
from pathlib import Path
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.models import Journal, FieldStation

# Setup database connection
db_path = Path("data/eco.db").resolve()
engine = create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=engine)
session = Session()

print(" Updating Journal.location based on FieldStation...")

# Query journals with field_station_id set
journals_to_update = session.query(Journal).filter(Journal.field_station_id != None).all()

count = 0
for journal in journals_to_update:
    station = session.query(FieldStation).filter_by(id=journal.field_station_id).first()
    if station:
        new_location = station.name or station.location
        if new_location and journal.location != new_location:
            journal.location = new_location
            count += 1

# Commit changes
session.commit()
session.close()

print(f" Updated location for {count} journals.")
