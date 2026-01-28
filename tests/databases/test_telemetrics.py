import tests.databases.helper
from src.databases.database import SessionLocal, Base, engine
from src.databases.classes.sessions import Session
from src.databases.classes.telemetrics import Telemetry
from src.databases.classes.commands import Command
import os

os.environ["DATABASES_URI"] = "sqlite:///src/databases/test_database.db"


def test_create_telemetry():
    Base.metadata.create_all(bind=engine)

    s = SessionLocal()

    obj = Telemetry(
        session_id=1,
        date_time="2023-11-20 10:15",
        altitude=1234.5,
        ground_altitude=500.0,
        speed=120.5,
        heading=45.0,
        ground_speed=130.0,
        latitude=46.2044,
        longitude=6.1432,
        plane_angle=5.0,
        angle_of_attack=2.0,
    )

    s.add(obj)
    s.commit()
    s.refresh(obj)

    r = s.query(Telemetry).filter(Telemetry.altitude == 1234.5).first()

    assert r.session_id == obj.session_id

    s.close()
    engine.dispose()
    os.remove("src/databases/test_database.db")
