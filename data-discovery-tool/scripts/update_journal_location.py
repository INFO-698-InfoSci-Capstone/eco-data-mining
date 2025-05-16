import os
import sys
from pathlib import Path
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Include the project root in the Python path for module resolution
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import ORM models
from db.models import Journal, FieldStation

# Define the path to the SQLite database
db_path = Path("data/eco.db").resolve()

# Create a SQLAlchemy engine and initialize a session
engine = create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=engine)
session = Session()

print("Starting update of Journal.location based on associated FieldStation...")

# Retrieve all Journal records that are linked to a FieldStation
journals_to_update = session.query(Journal).filter(Journal.field_station_id != None).all()

updated_count = 0  # Counter to track how many records are updated

# Iterate through each journal that needs an update
for journal in journals_to_update:
    # Fetch the corresponding FieldStation by ID
    station = session.query(FieldStation).filter_by(id=journal.field_station_id).first()
    
    if station:
        # Use station's name if available, otherwise fall back to its location
        new_location = station.name or station.location
        
        # Update journal location if it differs from the current one
        if new_location and journal.location != new_location:
            journal.location = new_location
            updated_count += 1

# Save changes to the database
session.commit()

# Close the session
session.close()

print(f"Finished updating journals. Total records updated: {updated_count}")
