import tests.analysis.helper
from src.databases.database import SessionLocal, Base, engine
from src.databases.classes.sessions import Session
from src.databases.classes.telemetrics import Telemetry
from src.databases.classes.commands import Command
from src.analysis.slope_analysis import calculate_slope
import os

def test_slope_analysis():
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

    telemetry_points = [
    Telemetry(
        latitude=46.8223,
        longitude=6.8223,
        altitude=1200,
        horizontal_speed=38.2,
        vertical_speed=1.6,
        time_since_departure="0:15",
        session_id=1,
    ),
    Telemetry(
        latitude=46.8250,
        longitude=6.8300,
        altitude=1050,
        horizontal_speed=38.2,
        vertical_speed=1.6,
        time_since_departure="0:30",
        session_id=1,
    ),
    Telemetry(
        latitude=46.8285,
        longitude=6.8400,
        altitude=900,
        horizontal_speed=38.2,
        vertical_speed=1.6,
        time_since_departure="0:45",
        session_id=1,
    ),
    Telemetry(
        latitude=46.8320,
        longitude=6.8520,
        altitude=750,
        horizontal_speed=38.2,
        vertical_speed=1.6,
        time_since_departure="1:00",
        session_id=1,
    )
    ]

    for obj in telemetry_points:
        s.add(obj)

    s.commit()
    s.refresh(obj)

    s.close()
    engine.dispose()

    r = calculate_slope(1)
    print(r)

    assert r == r

    os.remove("src/databases/test_database.db")