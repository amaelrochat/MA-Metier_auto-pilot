from src.databases.classes.commands import Command
from src.databases.classes.telemetrics import Telemetry
from src.databases.classes.sessions import Session
from src.databases.database import SessionLocal, Base, engine
import os

os.environ["DATABASES_URI"] = "sqlite:///src/databases/test_database.db"


def test_create_session():
    Base.metadata.create_all(bind=engine)

    s = SessionLocal()
    obj = Session(
        date_time="2026-01-15 15:41",
        glider_model="glider",
        takeoff_location="ste-croix",
    )
    s.add(obj)
    s.commit()
    s.refresh(obj)

    r = (
        s.query(Session)
        .filter(Session.date_time == "2026-01-15 15:41:00.000000")
        .first()
    )

    assert r.takeoff_location == obj.takeoff_location

    s.close()
    engine.dispose()
    os.remove("src/databases/test_database.db")
