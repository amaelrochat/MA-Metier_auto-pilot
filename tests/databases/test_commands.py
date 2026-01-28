import tests.databases.helper
from src.databases.database import SessionLocal, Base, engine
from src.databases.classes.sessions import Session
from src.databases.classes.telemetrics import Telemetry
from src.databases.classes.commands import Command
import os


def test_create_command():
    Base.metadata.create_all(bind=engine)

    s = SessionLocal()
    obj = Command(
        session_id=1,
        aileron_position=45,
        rudder_position=30,
        elevator_position=15,
        spoiler_position=10,
        throttle=75,
        date_time="2023-10-10 14:30"
    )
    s.add(obj)
    s.commit()
    s.refresh(obj)

    r = s.query(Command).filter(Command.date_time ==
                                "2023-10-10 14:30:00.000000").first()

    assert r.session_id == obj.session_id

    s.close()
    engine.dispose()
    os.remove("src/databases/test_database.db")
