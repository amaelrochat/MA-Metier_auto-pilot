import tests.databases.helper
from src.databases.database import SessionLocal, Base, engine
from src.databases.classes.sessions import Session
from src.databases.classes.telemetrics import Telemetry
from src.databases.classes.commands import Command
import os


def test_create_session():
    Base.metadata.create_all(bind=engine)

    s = SessionLocal()
    obj = Session(
        date_time="2026-01-15 15:41",
    )
    s.add(obj)
    s.commit()
    s.refresh(obj)

    r = (
        s.query(Session)
        .filter(Session.date_time == "2026-01-15 15:41:00.000000")
        .first()
    )

    assert r.date_time == obj.date_time

    s.close()
    engine.dispose()
    os.remove("src/databases/test_database.db")
