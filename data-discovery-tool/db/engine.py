import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Always resolve relative to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "data", "eco.db")

DATABASE_URL = f"sqlite:///{db_path}"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

print(f" Connected to DB at: {db_path}")
