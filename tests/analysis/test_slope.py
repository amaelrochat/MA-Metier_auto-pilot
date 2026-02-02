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
    )
    s.add(obj)
    s.commit()
    s.refresh(obj)

    telemetry_points = [
        Telemetry(
            date_time="2023-11-20 10:15",
            altitude=12000.0,
            latitude=37.7749,
            longitude=-122.4194,
            ground_altitude=30.0,
            speed=250.5,
            ground_speed=240.2,
            heading=90.0,
            plane_angle=2.5
        ),
        Telemetry(
            date_time="2023-11-20 10:15",
            altitude=12150.0,
            latitude=37.7755,
            longitude=-122.4188,
            ground_altitude=30.0,
            speed=252.0,
            ground_speed=241.8,
            heading=91.0,
            plane_angle=2.7
        ),
        Telemetry(
            date_time="2023-11-20 10:15",
            altitude=12300.0,
            latitude=37.7761,
            longitude=-122.4182,
            ground_altitude=30.0,
            speed=253.6,
            ground_speed=243.1,
            heading=92.0,
            plane_angle=2.9
        ),
        Telemetry(
            date_time="2023-11-20 10:15",
            altitude=12450.0,
            latitude=37.7767,
            longitude=-122.4176,
            ground_altitude=30.0,
            speed=255.1,
            ground_speed=244.6,
            heading=93.0,
            plane_angle=3.1
        ),
    ]

    for obj in telemetry_points:
        s.add(obj)

    s.commit()
    s.refresh(obj)

    s.close()
    engine.dispose()

    r = calculate_slope(1)
    print(r)

    os.remove("src/databases/test_database.db")
