from sqlalchemy import Column, String, Float, DateTime, Text, ForeignKey, JSON
from sqlalchemy.orm import declarative_base, relationship
import uuid
from datetime import datetime

Base = declarative_base()

class FieldStation(Base):
    __tablename__ = 'field_stations'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    location = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    ecosystem = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Journal(Base):
    __tablename__ = 'journals'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String)
    location = Column(String)
    date_published = Column(DateTime)
    creator = Column(JSON)
    field_station_id = Column(String, ForeignKey('field_stations.id'), nullable=True)
    keyphrases = Column(JSON)
    meta_json = Column(JSON) 
    full_text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class JournalNLP(Base):
    __tablename__ = 'journal_nlp'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    journal_id = Column(String, ForeignKey('journals.id'))
    topics = Column(JSON)
    ner_entities = Column(JSON)
    embeddings_path = Column(String)
    processed_at = Column(DateTime, default=datetime.utcnow)
