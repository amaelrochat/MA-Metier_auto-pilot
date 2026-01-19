from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

#ENGINE CONFIGURATION
path = os.getenv("DATABASES_URI") or "sqlite:///src/databases/database.db"
engine = create_engine(path)

#DECLARATIVE BASE
Base = declarative_base()

#SESSION FACTORY
SessionLocal = sessionmaker(bind=engine)