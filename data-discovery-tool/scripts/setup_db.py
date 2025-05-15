import os
import sys

# Automatically add the project root to Python path
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from sqlalchemy import create_engine
from db.models import Base

engine = create_engine("sqlite:///data/eco.db")
Base.metadata.create_all(engine)
