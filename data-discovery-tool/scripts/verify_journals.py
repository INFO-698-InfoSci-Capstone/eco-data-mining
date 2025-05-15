import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.models import Journal
from db.engine import SessionLocal

session = SessionLocal()

journals = session.query(Journal).all()

for journal in journals:
    authors = journal.creator
    if isinstance(authors, list) and len(authors) > 1:
        print(f"📝 Title: {journal.title}")
        print(f"📍 Location: {journal.location}")
        print(f"📅 Date Published: {journal.date_published}")
        print(f"✍️ Authors: {authors}")
        print(f"🧠 Keyphrases: {journal.keyphrases}")
        print(f"📄 Full Text Preview: {journal.full_text[:300]}...")
        print(f"👥 Number of Authors: {len(authors)}")
        print("-" * 80)
