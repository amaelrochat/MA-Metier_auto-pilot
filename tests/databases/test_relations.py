import tests.databases.helper
from src.databases.database import SessionLocal, Base, engine
from src.databases.classes.sessions import Session
from src.databases.classes.telemetrics import Telemetry
from src.databases.classes.commands import Command
import os


def test_create_relations():
    Base.metadata.create_all(bind=engine)

    s = SessionLocal()
    obj = Session(
        date_time="2026-01-15 15:41"
    )
    s.add(obj)
    s.commit()
    s.refresh(obj)

    obj = Telemetry(
        date_time="2026-01-15 15:45",
        altitude=1500.0,
        ground_altitude=500.0,
        speed=120.0,
        heading=270.0,
        ground_speed=130.0,
        session_id=1
    )

    s.add(obj)
    s.commit()
    s.refresh(obj)

    obj = Command(
        session_id=1,
        aileron_position=90,
        rudder_position=-45,
        elevator_position=30,
        spoiler_position=15,
        throttle=80,
        date_time="2026-01-15 15:50"
    )
    s.add(obj)
    s.commit()
    s.refresh(obj)

    session = (
        s.query(Session)
        .filter(Session.date_time == "2026-01-15 15:41:00.000000")
        .first()
    )
    telemetry = s.query(Telemetry).filter(
        Telemetry.altitude == 1500.0).first()
    command = s.query(Command).filter(Command.aileron_position == 90).first()

    assert telemetry.Session.id == session.id
    assert command.Session.id == session.id

    s.close()
    engine.dispose()
    os.remove("src/databases/test_database.db")
