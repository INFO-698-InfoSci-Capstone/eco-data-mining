import sys
from pathlib import Path

# ====== Add project root to sys.path ======
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# ====== SQLAlchemy Setup ======
from sqlalchemy.orm import sessionmaker
from db.engine import engine
from db.models import Journal, JournalNLP, FieldStation

Session = sessionmaker(bind=engine)
session = Session()

print("🔍 Viewing a full journal record...")

# ====== Get first journal entry ======
journal = session.query(Journal).first()

if not journal:
    print("No journal entries found.")
    session.close()
    sys.exit()

# ====== Get related NLP and FieldStation entries ======
nlp_entry = session.query(JournalNLP).filter_by(journal_id=journal.id).first()
station_entry = session.query(FieldStation).filter_by(id=journal.field_station_id).first()

# ====== Pretty print results ======
print("\nJournal Record:")
for col in Journal.__table__.columns:
    print(f"  {col.name}: {getattr(journal, col.name)}")

print("\nNLP Record:")
if nlp_entry:
    for col in JournalNLP.__table__.columns:
        print(f"  {col.name}: {getattr(nlp_entry, col.name)}")
else:
    print("  None")

print("\n Field Station Record:")
if station_entry:
    for col in FieldStation.__table__.columns:
        print(f"  {col.name}: {getattr(station_entry, col.name)}")
else:
    print("  None")

session.close()
