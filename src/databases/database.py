import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Engine configuration
DATABASE_URI = os.getenv("DATABASES_URI", "sqlite:///src/databases/database.db")
engine = create_engine(DATABASE_URI)

# Declarative base
Base = declarative_base()

# Session factory
SessionLocal = sessionmaker(bind=engine)