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
        glider_model="glider",
        takeoff_location="ste-croix",
    )
    s.add(obj)
    s.commit()
    s.refresh(obj)

    obj = Telemetry(
        coordonate=46.8223,
        altitude=1234.5,
        horizontal_speed=38.2,
        vertical_speed=1.6,
        time_since_departure="0:15",
        session_id=1,
    )

    s.add(obj)
    s.commit()
    s.refresh(obj)

    obj = Command(x_handle=90, y_handle=-90, crossbar=45, session_id=1)
    s.add(obj)
    s.commit()
    s.refresh(obj)

    session = (
        s.query(Session)
        .filter(Session.date_time == "2026-01-15 15:41:00.000000")
        .first()
    )
    telemetry = s.query(Telemetry).filter(
        Telemetry.coordonate == 46.8223).first()
    command = s.query(Command).filter(Command.x_handle == 90).first()

    assert telemetry.Session.id == session.id
    assert command.Session.id == session.id

    s.close()
    engine.dispose()
    os.remove("src/databases/test_database.db")
